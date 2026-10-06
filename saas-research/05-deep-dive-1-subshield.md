# Part 3 — Deep Dive #1: SubShield (COI tracking for contractors) — Score 78.0

## Ideal customer profile (ICP)
- **Company:** US commercial general contractor or large specialty contractor
- **Size:** $5M–$50M revenue, 15–150 employees, 30–250 subs/vendors used per year
- **Stack:** QuickBooks/Sage 100 Contractor/Foundation, maybe Procore, Microsoft 365/Outlook
- **Geography:** start in 1–2 states with heavy commercial construction (TX, FL, GA, NC, AZ)
- **Trigger events:** a recent premium-audit chargeback; an uninsured-sub incident; a new controller/office manager; switching insurance brokers; growth past ~40 subs; a large project with stricter owner insurance requirements
- **Disqualifiers:** uses a wrap-up (OCIP/CCIP) on most jobs; residential-only builders using 5 subs; enterprise GCs already on myCOI/Jones/TrustLayer

## Customer persona
**Dana, project accountant / office manager, 38, at an $18M commercial GC in Dallas.**
- Owns AP, lien waivers, and COIs for ~140 subs. Reports to the owner/CFO.
- Monday mornings: scans Outlook for COIs, opens PDFs, updates an Excel sheet with 14 columns, emails agents about expired ones.
- **Got burned:** last year's workers' comp audit charged the company **$27k** for three subs whose policies had lapsed mid-job. The owner asked, "How did we miss this?"
- Wants: to never get blamed again, fewer chase emails, a clean report when the auditor calls.
- Fears: a complicated tool that becomes a second job; subs complaining about yet another portal.
- Decision: Dana champions it; the owner/CFO approves anything under ~$300/mo on a credit card without procurement.

## Exact problem statement
> "Our subcontractors' insurance certificates expire on staggered dates all year. We track them by hand in a spreadsheet, chase agents by email, and still discover lapses only when our insurer's premium audit charges us for uninsured subs, or worse, after a claim."

## Value proposition
**Every sub on your jobs stays covered, without the spreadsheet.** SubShield collects certificates, reads them in seconds, flags what's expired or wrong, and chases agents automatically. You only review exceptions.

## Product positioning
For **small and mid-size commercial contractors** who track subcontractor insurance in spreadsheets, **SubShield** is the **self-serve COI tracker** that **reads certificates with AI and chases agents for you**. Unlike enterprise vendor-compliance platforms, it **sets up in an afternoon, has public monthly pricing, and costs less than one hour of admin time a week.**

## Product name ideas
SubShield · CertChase · COI Pilot · CoverCheck · ProofPilot · SubCover · CertKeeper · Insured.ly · COIwise · GreenLight COI

## Domain name ideas *(check availability; these are suggestions, not verified)*
subshield.io · getsubshield.com · certchase.com · coipilot.com · trackcoi.com · coiwise.com · subcover.io · greenlightcoi.com

## MVP architecture
**Use the stack your developer ships fastest in.** You know Python/Django, so this is a strong, boring fit:
- **Django monolith** (server-rendered templates + HTMX; no SPA needed) on **Postgres**
- **Background jobs:** Celery + Redis, or Django-Q / Procrastinate (Postgres-backed, one less service)
- **File storage:** S3 or Cloudflare R2, private buckets, signed URLs
- **Email:** Postmark (outbound + **inbound parsing webhook**); separate message streams for transactional vs reminders
- **Extraction:** PDF → text (pdfplumber) + page image → vision-capable LLM with a strict JSON schema → validation rules → review queue
- **Billing:** Stripe Checkout + Customer Portal + webhooks
- **Hosting:** Render/Railway/Fly.io (managed Postgres with point-in-time recovery)
- **Monitoring:** Sentry + uptime check + a daily "jobs ran" heartbeat

```
Email (coi@acme.subshield.io) ─┐
Upload link (no login) ────────┼─> Document intake ─> Extraction worker ─> Rules engine ─> Status
Admin upload / bulk zip ───────┘           │                 │                  │
                                           ▼                 ▼                  ▼
                                    S3/R2 storage      Review queue       Scheduler (daily):
                                                      (human confirm)     reminders, digests,
                                                                           expiries, escalations
```

## Database structure (core tables)
| Table | Key fields |
|---|---|
| `organizations` | id, name, inbox_slug, timezone, plan, vendor_limit, stripe_customer_id, created_at |
| `users` | id, email, name, password_hash/oauth_id, last_login |
| `memberships` | user_id, org_id, role (owner/admin/viewer) |
| `requirement_templates` | org_id, name (e.g., "Standard sub", "Roofing", "Low-risk vendor"), rules JSON: per-line minimum limits (GL each occ/aggregate, auto CSL, WC statutory, EL, umbrella), AI required, WOS required, primary/non-contributory, cert-holder text |
| `vendors` | org_id, name, trade, contact_name/email/phone, agent_name/email, requirement_template_id, status (computed), active flag, notes |
| `projects` *(v1.1)* | org_id, name, owner-specific requirement overrides |
| `documents` | org_id, vendor_id (nullable until matched), source (email/upload/link), file_key, sha256, original_filename, received_at, inbound_email_id |
| `certificates` | document_id, vendor_id, insured_name, producer (agent) name/email, cert_holder, issue_date, extraction_json, confidence, review_status (pending/confirmed/rejected), reviewed_by, reviewed_at |
| `policies` | certificate_id, vendor_id, line (GL/AUTO/WC/EL/UMB/OTHER), carrier, NAIC, policy_number, effective_date, expiration_date, limits JSON, additional_insured bool, waiver_of_subrogation bool |
| `compliance_results` | vendor_id, computed_at, status, deficiencies JSON (e.g., "GL aggregate $1M < required $2M", "WC expires in 9 days") |
| `requests` | vendor_id, kind (initial/renewal/deficiency), recipients, token (hashed), expires_at, status (sent/opened/fulfilled/bounced), sent_at, fulfilled_at |
| `notifications` | org_id, channel, recipient, template, related object, sent_at, status |
| `inbound_emails` | org_id, from, subject, raw_key, parsed_at, match_status |
| `audit_log` | org_id, actor, action, object, before/after JSON, at |

## Frontend pages
1. Marketing site: home, pricing, "free COI audit", template download, blog
2. Sign up / log in (email + Google + **Microsoft**; construction runs on Outlook)
3. Onboarding wizard (4 steps)
4. **Dashboard**
5. Vendors list (filter by status/trade/project; bulk actions "request COI")
6. Vendor detail (current coverage vs requirements, certificate history, request timeline, notes)
7. **Review queue** (PDF on the left, extracted fields on the right, deficiencies highlighted; Confirm / Edit / Reject)
8. Requirement templates editor
9. Reports (expiring 30/60/90; **premium audit report** by date range; export CSV/PDF)
10. Settings: inbox address, email templates, team, notifications, billing
11. **Public upload page** (tokenized, no login, mobile-friendly; for subs and agents)

## Backend services
- **Inbound email processor:** receives the Postmark webhook, stores raw, extracts attachments, dedupes by hash
- **Vendor matcher:** matches by sender email → agent/vendor email on file → fuzzy insured name → else "unmatched" queue
- **Extraction pipeline:** text + image → LLM JSON → schema validation → date sanity checks (expiration after effective; year plausibility) → confidence score
- **Rules engine:** compares policies against the requirement template → status + deficiency list
- **Scheduler (daily at 6am org time):** expiry windows, reminder cadence, escalations, digests
- **Mailer:** templated emails, tracking, bounce handling, per-recipient frequency caps
- **Report generator:** HTML → PDF (WeasyPrint)
- **Billing webhooks:** plan limits and dunning
- **Audit logger:** every status change, confirmation, and email sent (this *is* the product's evidence)

## Integrations
- **MVP:** Postmark (in/out), LLM API, S3/R2, Stripe, Google/Microsoft OAuth
- **v1.1:** QuickBooks Online (vendor sync + "do not pay" flag via a vendor note/custom field)
- **v2:** Procore (vendors/commitments), Sage Intacct, Microsoft 365 shared-mailbox ingestion, Zapier

## Automation workflows
1. **New vendor:** request email to sub + agent (with upload link) → reminders on day 3, 7, 14 → escalate to the admin's digest → optional SMS on day 10.
2. **Certificate arrives:** match → extract → evaluate. If confidence ≥ threshold and fully compliant → *(optional per org)* auto-confirm; otherwise → review queue.
3. **Deficiency found:** auto-email the agent with the exact fix ("Please add Acme Builders as Additional Insured on GL; GL aggregate must be $2M").
4. **Expiry approaching (30/14/7/0 days):** renewal request to agent → reminders → on expiry, "EXPIRED" alert to admin + optional PM email ("Do not allow on site / hold payment").
5. **Weekly digest (Monday 7am):** compliant %, new issues, actions needed.
6. **Monthly:** "audit-ready" report emailed to the owner/CFO (and optionally their broker). This doubles as a **retention touchpoint**.

## Onboarding flow (aim for "aha" in under 15 minutes)
1. Sign up → company name → **pick a requirement template** (pre-filled with common GC requirements; editable)
2. **Import vendors:** paste from Excel or upload CSV (column mapper)
3. **Drag in your existing COI folder** (bulk PDFs) → in minutes the dashboard shows "**23 of 140 vendors are expired, deficient, or missing.**" That is the aha moment.
4. Copy your inbox address, add a forwarding rule, preview the request email, click **"Request missing COIs (23)"**
5. **Concierge alternative:** "Send us your spreadsheet + folder; we'll load everything within 24 hours." (Do this manually for every early customer.)

## Dashboard layout
- **Top KPI row:** Compliant % · Expiring ≤30 days · Expired · Missing · Awaiting response
- **Left column: "Needs you"** — review queue count, unmatched documents, vendors not responding after 14 days
- **Center:** 90-day expiration timeline (bars by week)
- **Bottom:** vendors table with status chips, last activity, next action
- **Right rail:** activity feed ("Agent at Smith Insurance uploaded COI for Rivera Concrete — auto-confirmed")

## Notification system
- **Channels:** email (primary), SMS (subs only, opt-in, v1.1), in-app badges
- **Recipients:** vendors and agents (requests/reminders), admins (digests and instant alerts for expired active vendors), PMs (optional per-project alerts)
- **Controls:** per-org cadence settings, quiet hours, frequency caps (max 1 reminder per recipient per 3 days), one-click "snooze vendor", unsubscribe handling for non-essential mail
- **Deliverability:** SPF/DKIM/DMARC on a sending subdomain, separate streams, bounce → flag the vendor email as bad

## Billing system
- Stripe Checkout with monthly and annual prices per tier; Customer Portal for card updates/cancel
- **Plan enforcement:** active vendor count (archived vendors are free, which keeps history and reduces churn pressure)
- Webhooks: `checkout.session.completed`, `customer.subscription.updated/deleted`, `invoice.payment_failed`
- Smart dunning on; 7-day grace period → read-only mode (never delete data)
- Invoices with company name/address (construction AP needs proper invoices); allow ACH for annual plans

## Authentication system
- Email + password (argon2) + magic link; Google and Microsoft OAuth
- Roles: Owner (billing), Admin (everything else), Viewer (PMs: read-only + their projects)
- Optional TOTP 2FA (required for owners on Business tier)
- Sessions: secure, HttpOnly cookies; 14-day expiry; device list
- **Public upload links:** random 32-byte tokens stored hashed, scoped to one vendor, expire in 30 days, rate-limited

## Admin dashboard (yours)
- Orgs: plan, MRR, trial day, vendor count, last login, health score (logins + confirmations + emails flowing)
- Extraction quality: confidence distribution, % edited by humans by field (your accuracy KPI)
- Queues: unmatched docs, failed inbound, bounced emails, jobs that didn't run
- "Impersonate" with mandatory reason, logged in the audit log
- Revenue: MRR, churn, trials → paid conversion, expansion

## Security requirements
- TLS everywhere; encryption at rest (managed Postgres + S3 SSE)
- Strict tenant isolation: every query scoped by org (Django manager/middleware) + automated tests for cross-tenant access
- Private buckets, short-lived signed URLs; virus scan on upload (ClamAV) and file type/size limits
- Rate limiting on login, upload, and inbound endpoints; CSRF protection; dependency scanning
- Daily backups with PITR, plus a tested restore
- Audit log on all status changes; retention settings (default: keep 7 years, since audits look back)
- LLM provider with no training on your data (check the API terms), and send only the document, not unrelated customer data
- Written security page + DPA template; SOC 2 Type I when you approach ~$10k MRR or when deals require it

## Pricing tiers
| | **Starter** | **Pro** (most popular) | **Business** |
|---|---|---|---|
| Monthly | $99 | $199 | $399 |
| Annual (2 months free) | $990/yr | $1,990/yr | $3,990/yr |
| Active vendors | 50 | 200 | 600 |
| Users | 2 | Unlimited | Unlimited |
| AI reading + auto-chasing | ✓ | ✓ | ✓ |
| Project-specific requirements | – | ✓ | ✓ |
| Premium-audit report | ✓ | ✓ | ✓ |
| QuickBooks sync | – | ✓ | ✓ |
| Multiple entities, 2FA enforcement, priority support | – | – | ✓ |
| **Done-for-you add-on** (we review, chase, call agents) | +$250/mo | +$250/mo | +$450/mo |

## Free trial strategy
- **During validation:** no free trial. Sell a **paid pilot** ($299 for 60 days, credited to an annual plan).
- **After launch:** 14-day trial, **no credit card**, but the trial's centerpiece is the "instant audit" (upload your folder, see your exposure). Book a 15-minute call on day 2; send a personalized exposure report on day 5.
- Trial ends → read-only (data stays), and nothing is deleted for 60 days.

## Annual pricing strategy
- Annual = 10× monthly (2 months free); **default the toggle to annual on the pricing page**
- Pitch annual around their **insurance renewal/premium audit cycle**: "Cover your whole policy year."
- Offer the founding 20 customers a **price lock** for 24 months if they pay annually

## Cancellation flow
1. Self-serve cancel in Settings (never hide it; contractors talk to each other)
2. One-click reason: too expensive / not using / switching tool / company change / other
3. Reason-specific save offer:
   - Too expensive → downgrade, or **Archive mode $29/mo** (read-only, keeps the audit history and export — very sticky because auditors look back 1–3 years)
   - Not using → free 30-minute setup session + 1 month free of the done-for-you add-on
   - Switching → offer full export (CSV + all PDFs as a zip), be gracious
4. Confirm; data kept for 90 days, then deleted (configurable)

## Retention strategy
- **Make the history valuable:** auditors and claims look backward, and the archive is the moat
- Monthly "**Exposure avoided**" email: lapsed policies caught × estimated payroll exposure
- Get PMs involved (viewer seats are free), which spreads usage beyond one champion
- QuickBooks "do-not-pay" flags embed you in the AP process
- Quarterly 15-minute check-in for Pro/Business; annual plans by default
- Churn alarms: no confirmations in 21 days, inbox forwarding stopped, champion user inactive

## Landing page structure
1. Hero: headline, subheadline, CTA "Get a free COI audit", secondary "See pricing"
2. Proof strip: "Built with contractors in Dallas & Houston" (early quotes/logos)
3. The problem: the premium-audit chargeback story (with numbers)
4. How it works: Forward → We read → We chase → You're covered
5. Features (6 tiles)
6. ROI calculator: subs × % lapsing × avg payroll exposure × rate
7. Comparison: Spreadsheet vs Enterprise platforms vs SubShield
8. Testimonials
9. Pricing
10. FAQ
11. Final CTA + "Talk to the founder" calendar link

## Landing page headline
**"Stop paying for your subs' missing insurance."**

Alternates: "Every sub covered. No spreadsheet." / "Your COI tracking, on autopilot."

## Subheadline
"SubShield reads every certificate of insurance, flags what's expired or wrong, and chases agents automatically, so you're audit-ready all year. Set up in an afternoon. No sales call required."

## Features section
- **Forward and forget.** Give agents your SubShield address. Certificates are filed to the right vendor automatically.
- **Reads COIs in seconds.** Limits, dates, additional insured, and waiver of subrogation, checked against *your* requirements.
- **Chases agents for you.** Polite, persistent reminders before policies expire, with a no-login upload link.
- **Exceptions only.** Review what's wrong, not 140 PDFs.
- **Premium-audit report in one click.** Show your auditor every sub's coverage for any date range.
- **Know before they're on site.** PMs get alerts when a sub on their job lapses.

## Pricing page copy
**Simple pricing. Pays for itself the first time it catches a lapse.**
One uninsured sub can add thousands to your premium audit. SubShield costs less than an hour of admin time a week.
- Toggle: Monthly / **Annual (2 months free)**
- Under tiers: "All plans include unlimited certificates, AI reading, automatic reminders, and audit reports. Archived vendors are always free."
- Reassurance: "No setup fees. Cancel anytime. Your data is always exportable."
- Done-for-you callout: "Don't want to touch it at all? Add our team to review and chase for you."

## FAQ
- **Do my subs or their agents need an account?** No. They reply to an email or use a secure upload link.
- **How accurate is the AI?** It reads standard ACORD 25 certificates very reliably, and anything uncertain goes to your review queue. You confirm before anything is marked compliant (or enable auto-approval for clean certificates).
- **Does this replace my insurance broker?** No. We track proof of coverage. Your broker still advises on your requirements, and many brokers recommend us to their clients.
- **Is a COI proof of coverage?** A certificate is informational. SubShield helps you collect, verify, and document them consistently; for critical requirements (like additional insured), request endorsements too.
- **Can I import my spreadsheet?** Yes. Paste it or upload a CSV, or send it to us and we'll do it free.
- **Does it work with Procore or QuickBooks?** QuickBooks sync is on Pro. Procore is on the roadmap. Tell us if you need it.
- **What happens if I cancel?** Export everything anytime. Archive mode keeps your history read-only for $29/mo.
- **Is my data secure?** Encrypted in transit and at rest, isolated per company, with full audit logs. See our security page.

## Cold email template
> **Subject:** subs with expired workers' comp
>
> Hi {{first_name}},
>
> Quick question: how does {{company}} track subcontractor COIs today? Spreadsheet + Outlook folder?
>
> I'm talking to commercial GCs in {{city}} because most find out a sub's policy lapsed only when the premium audit bill shows up (one GC I spoke with paid $27k for three subs).
>
> I'm offering a **free COI audit**: send me your current list and certificates, and within 48 hours I'll send back exactly which subs are expired, under-limit, or missing additional insured. No software to install.
>
> Worth doing before your next audit?
>
> {{your_name}}
> {{phone}}
>
> *(Follow-up 1, day 3:)* "Should I send this to whoever handles your COIs instead?"
> *(Follow-up 2, day 8:)* "Last note: here's the 1-page checklist we use to spot a bad COI in 30 seconds: {{link}}"

*(Only use the "$27k" line once you have a real story you're allowed to share. Never invent a customer anecdote.)*

## LinkedIn outreach message
> Hi {{first_name}}, I'm building a simple tool for GCs that reads subcontractor COIs and chases agents automatically. I'm doing free COI audits for a few contractors in {{state}} to learn how teams handle this. Would you be open to a 15-minute chat, or should I talk to whoever owns COIs at {{company}}?

## Google search keywords
- certificate of insurance tracking software · COI tracking software · COI management software for contractors
- subcontractor insurance tracking · track subcontractor certificates of insurance · subcontractor COI tracking spreadsheet
- ACORD 25 tracking · how to read a certificate of insurance · additional insured vs certificate holder
- premium audit uninsured subcontractor · workers comp audit charged for subcontractors · general liability audit subcontractors
- COI requirements for subcontractors · waiver of subrogation subcontractor · myCOI alternative · TrustLayer alternative

## SEO content ideas
1. "Why your workers' comp audit charged you for subcontractors (and how to stop it)"
2. "How to read an ACORD 25 in 60 seconds" (annotated graphic)
3. "Subcontractor insurance requirements checklist by trade" (download)
4. "Additional insured vs certificate holder: what GCs get wrong"
5. **Free tool:** "COI Checker". Upload one certificate, get an instant deficiency report (lead magnet; uses the same extraction pipeline)
6. **Free template:** COI tracking spreadsheet (captures the exact searcher you want, then show its limits)
7. State guides: WC exemption certificates (e.g., Florida construction exemptions), Texas non-subscribers, ghost policies
8. Comparison pages: "SubShield vs spreadsheet", "Alternatives to myCOI for small contractors"

## Reddit / community strategy
- **Where:** r/Construction, r/ConstructionManagers, r/Accounting, r/smallbusiness; LinkedIn construction-accounting groups; **CFMA** (Construction Financial Management Association) chapter forums and events
- **How:** answer premium-audit and COI questions in detail with no link for the first month; share the free checklist/template when relevant; post a genuine "what I learned from 30 contractor interviews about COIs" write-up
- **Never:** fake accounts, astroturfing, or link-dumping

## Partnership opportunities
1. **Construction-focused insurance brokers** (best channel): they field the audit fallout; offer a 20% recurring referral or a free broker dashboard showing their clients' compliance
2. **CFMA, AGC, ABC chapters:** lunch-and-learn on "premium audit surprises"
3. **Construction accountants/fractional CFOs:** referral fee
4. **Premium audit firms / loss-control consultants**
5. **Marketplaces:** QuickBooks App Store, Procore App Marketplace (later)
6. **Surety agents:** surety underwriters care about contractor controls

## First 10 customers strategy
1. Build a list of 300 commercial GCs in one metro (state license DB + Google Maps + LinkedIn for "project accountant"/"office manager"/"controller").
2. Email + call 20/day with the **free 48-hour COI audit** offer.
3. Do the audits **manually** with the extraction prototype + Google Sheets. Deliver a crisp PDF: "17 of 140 subs non-compliant; 6 expired; est. exposure $X."
4. On the results call, offer the **paid pilot** ($299 for 60 days, credited) and a founding price ($99–$149/mo locked 24 months).
5. Ask 5 construction brokers for introductions; offer to audit one client free as a demo.
6. Attend 1 CFMA chapter meeting.
7. Goal: 25 audits → 10 paying pilots.

## First $1,000 MRR strategy
- **≈7 customers at ~$149 average.** Convert pilots from the audit funnel. Don't build new features; finish onboarding and the review queue.
- Do onboarding by hand (concierge). Every customer gets a "you're covered" report in week 1.
- Ask every customer for 2 referrals and a quote.

## $5,000 MRR strategy (~30 customers, avg ~$170)
- Outbound: 1,000 targeted emails/month across 3–4 metros (separate sending domains, warmed)
- **Broker channel:** sign 5 broker partners; each brings 2–4 clients
- 2 CFMA/AGC talks per quarter
- Ship the QuickBooks sync and "COI Checker" free tool (SEO + lead gen)
- Add the done-for-you add-on (you or a VA reviews/chases). This raises ARPU and lowers churn
- Hire a part-time VA (~$800/mo) for review queue + onboarding imports

## $10,000 MRR strategy (~55–60 customers, avg ~$175)
- Second vertical: **commercial property managers** (vendor COIs) with the same engine and different templates
- Second module: **LicenseLedger** (trade licenses) + W-9 collection. ARPU climbs to $250+
- Procore marketplace listing
- Annual plans >40% of new sales
- SOC 2 Type I (with Vanta/Drata-type tooling) to unlock larger GCs
- Part-time SDR or agency for outbound; you focus on partners and product

## What to do manually behind the scenes first
| Looks automated | Actually done manually at first |
|---|---|
| "We'll load your data in 24 hours" | You clean their spreadsheet and map columns yourself |
| AI review queue | **You** (or a VA) confirm every extraction for the first ~1,000 certs; this also builds your accuracy dataset |
| Vendor matching for unmatched emails | You match them in the admin panel |
| Requirement templates | You write them on the onboarding call |
| Agent chasing escalation | You phone stubborn agents (this is also the done-for-you add-on) |
| Premium-audit report | A Google Doc/PDF assembled by you until the generator is built |
| Billing | Stripe Payment Links before Checkout integration |
| Weekly digest | A templated email you send manually from a SQL query |
