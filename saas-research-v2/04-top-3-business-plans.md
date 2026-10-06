# Part 5 — Top 3 Mini Business Plans (three genuinely different businesses)

Credentialing (#2) and DQ files (#4) are **the same product shape as SubShield**: an expiring-document tracker. So the top 3 deliberately cover three different *mechanics*, buyers and industries:

| | Mechanic | Industry | Buyer |
|---|---|---|---|
| **A. SubShield** | Collect + track expiring third-party documents | Construction (GCs) | Office manager / controller |
| **B. CommissionCheck** | Reconcile money: expected vs received | Insurance agencies | Agency owner / accountant |
| **C. PayrollProof** | Transform data into regulated weekly reports | Public-works subcontractors | Payroll admin / owner |

---

## A. SubShield — subcontractor COI tracking

**Ideal customer:** commercial GC, $5–50M revenue, 30–250 active subs, QuickBooks/Sage, Outlook, one Sun Belt metro to start.

**Buyer persona:** Dana, project accountant at an $18M GC. Owns AP, lien waivers and COIs for about 140 subs. Was blamed for a premium-audit charge. Can put ≤$300/mo on a card with owner approval in one conversation.

**Customer workflow today:** sub added → email sub for a COI → agent sends a PDF → Dana reads it and types dates into Excel → calendar reminder → chase again at renewal → panic at audit.

**Product workflow:** import vendors → choose requirement template → SubShield emails subs and agents an upload link → COIs arrive via the forwarding inbox or the link → AI extracts → Dana confirms exceptions only → auto-reminders at 30/14/7/0 days → weekly digest → one-click premium-audit report.

**MVP features:** vendor import (CSV/paste); requirement templates; forwarding inbox + no-login upload link; AI ACORD 25 extraction with confirm screen; compliance status + deficiency reasons; automated request and reminder emails to sub + agent; dashboard; audit/expiring reports (CSV/PDF); Stripe billing.

**Features NOT to build:** Procore/Sage integrations, mobile app, lien waivers, prequal, endorsement-document parsing, SSO, multi-entity, payment holds, a broker portal.

**Dashboard:** KPI row (Compliant % · Expiring ≤30d · Expired · Missing · Awaiting reply) → "Needs you" queue → 90-day expiry timeline → vendor table with status chips → activity feed.

**Database entities:** Organization, User, Membership, RequirementTemplate, Vendor, Document, Certificate, Policy (line, carrier, dates, limits, AI/WOS flags), ComplianceResult, Request (tokenized), InboundEmail, Notification, AuditLog, Subscription.

**Backend architecture:** Django monolith + Postgres + background worker (Celery/Redis or Postgres-backed queue) + S3/R2 private storage + scheduled daily job. Pipelines: inbound email → attachment store → vendor match → extraction → rules engine → status → notifications.

**API/integrations:** Postmark (inbound + outbound), vision-capable LLM API, PDF text extraction, Stripe, Google/Microsoft OAuth. Later: QuickBooks Online, Procore.

**Notifications:** email to subs/agents (requests, reminders, deficiency fixes), daily/weekly admin digests, instant alert when an active sub expires; frequency caps; SPF/DKIM/DMARC on a sending subdomain.

**Authentication:** email+password/magic link + Google/Microsoft; roles Owner/Admin/Viewer; optional 2FA; tokenized, expiring, rate-limited upload links for outsiders.

**Subscription billing:** Stripe Checkout + Customer Portal; plans by active vendor count; archived vendors free; annual = 10× monthly; failed payment → 7-day grace → read-only.

**Pricing tiers (adjusted for BCS's free/cheap tiers):**
| Starter $79/mo | Pro $179/mo | Business $349/mo | Done-for-you add-on |
|---|---|---|---|
| ≤50 vendors, 2 users | ≤200 vendors, unlimited users, project requirements | ≤500 vendors, multi-entity, priority | +$200/mo: we review & phone agents |

**Onboarding:** pick template → paste vendor list → drag in the existing COI folder → **aha: "23 of 140 subs are expired, deficient or missing"** → click "Request missing COIs" → set up email forwarding. Concierge alternative: "Send us your spreadsheet + folder; live in 24 hours."

**Landing page:** headline "Stop paying for your subs' missing insurance." · subheadline "SubShield reads every certificate, flags what's expired or wrong, and chases agents for you, so you're audit-ready all year." · CTA "Get a free COI audit" · sections: premium-audit story → 3-step how-it-works → features → ROI calculator → pricing → FAQ.

**Cold outreach:**
> Subject: subs with expired workers' comp
> Hi {{name}}, how does {{company}} track subcontractor COIs today, spreadsheet + Outlook? Most GCs I talk to only find lapses when the premium audit bill arrives. I'm doing free COI audits: send your list + certificates, and in 48 hours you'll know which subs are expired, under-limit or missing additional insured. Worth doing before your next audit? — {{you}}, {{phone}}

**First customer strategy:** free audits done by hand (extraction script + spreadsheet) → results call → pricing conversation → paid pilot.

**First 10 customers:** 300 GCs in one metro; 20 calls + 20 emails/day; 5 construction-focused insurance brokers asked for 2 intros each; target 15 audits → 10 paid pilots.

**First 100 customers:** broker referral program (20% recurring for 12 months), CFMA/AGC lunch-and-learns, 3–4 metros of outbound, SEO (COI spreadsheet template, "how to read an ACORD 25", premium-audit articles, free single-certificate checker), QuickBooks App Store listing.

**$1K MRR path:** about 7 customers at ~$150 average (pilots converting).
**$5K MRR path:** about 30 customers; 5 broker partners; done-for-you add-on raises average revenue to ~$180; part-time VA for the review queue.
**$10K MRR path:** about 55 customers; add commercial property managers as a second vertical; add licenses/W-9/lien-waiver modules; annual plans >40% of new sales; SOC 2 Type I readiness.

**Approximate monthly operating costs (at ~50 customers):** hosting + DB $60–150 · email $30–60 · LLM extraction $30–100 · storage $10 · error monitoring $0–30 · Stripe ~3% · tooling (outbound, data) $100–200 · **≈$300–550/mo + Stripe fees** (excludes a VA).

---

## B. CommissionCheck — carrier commission reconciliation for independent P&C agencies

**Ideal customer:** independent P&C agency, 8–40 staff, 15–60 carrier/MGA/wholesaler relationships, on HawkSoft, EZLynx, NowCerts or AMS360 (not Applied Epic at first), with an owner or bookkeeper who reconciles statements in Excel.

**Buyer persona:** Linda, agency principal/office manager at a 14-person agency. On the 10th of every month she downloads ~35 statements (PDF, Excel, CSV), pastes them into a workbook and ticks them against the AMS. She suspects money is missing from small MGAs but has no time to chase it.

**Customer workflow today:** log into carrier portals → download statements → re-key/paste into Excel → VLOOKUP against the AMS export → highlight mismatches → (rarely) email carriers → producer commissions calculated from the same sheet.

**Product workflow:** forward or upload statements + monthly AMS export → AI normalizes each statement into rows (policy #, insured, transaction, premium, rate, commission) → a matching engine pairs them with expected commissions → exceptions queue (missing, short-paid, rate mismatch, chargeback, unknown policy) → user resolves or opens a recovery item → monthly report + producer-pay export.

**MVP features:** statement intake (upload + forwarding inbox); per-carrier extraction with a saved "template memory" after the first correction; AMS export CSV mapping; matching with fuzzy policy/insured matching; exceptions queue; recovery tracker (status, amount, carrier contact); monthly summary; CSV export.

**Features NOT to build:** direct AMS API integrations, carrier portal scraping/login automation, producer commission plan engine, general ledger posting, life/health override hierarchies.

**Dashboard:** KPI row (Statements received vs expected · Matched % · $ exceptions open · $ recovered YTD) → carrier list with status (missing statement / reconciled / exceptions) → exceptions table by $ → recovery pipeline.

**Database entities:** Agency, User, Carrier, CarrierAlias, Statement (file, period, source), StatementTemplate (extraction hints per carrier), StatementLine, ExpectedCommission (from AMS export), Match, Exception, RecoveryItem, ImportMapping, AuditLog, Subscription.

**Backend architecture:** Django + Postgres + workers. Pipeline: file → text/table extraction (pdfplumber / openpyxl / CSV) → LLM normalization to a strict schema (only where rule-based parsing fails) → validation (totals must equal statement total; **reject when they don't**) → matching engine (deterministic first, fuzzy second) → exceptions.

**API/integrations:** Postmark inbound, LLM API, S3/R2, Stripe, Google/Microsoft OAuth. Later: IVANS download files, HawkSoft/EZLynx exports, QuickBooks.

**Notifications:** "Statement missing from Carrier X for September", monthly reconciliation-complete summary, recovery follow-up reminders, weekly exceptions digest.

**Authentication:** email/password + Microsoft/Google; roles Owner/Accounting/Viewer; 2FA required for Owner (financial data).

**Subscription billing:** Stripe; tiers by statements/month; annual option; one-time paid "backlog reconciliation" ($499) for the last 3–6 months (high-value first sale).

**Pricing tiers:**
| Small $149/mo | Growth $299/mo | Pro $499/mo |
|---|---|---|
| ≤20 statements/mo | ≤60 statements/mo | ≤150, multi-location, priority |

**Onboarding:** upload last month's statements + AMS export → first reconciliation in 24h (you review it by hand behind the scenes) → **aha: "$3,140 in commissions you weren't paid, across 4 carriers"** → set up forwarding → schedule a monthly reminder.

**Landing page:** headline "Find the commissions your carriers didn't pay you." · subheadline "CommissionCheck reads every carrier statement (PDF, Excel or CSV), matches it to your AMS, and shows exactly what's missing, short or charged back, in minutes instead of days." · CTA "Get a free commission check" · sections: the Excel pain → how it works → sample exceptions report → pricing → FAQ (accuracy, which AMSs, data security).

**Cold outreach:**
> Subject: missing commissions at {{agency}}
> Hi {{name}}, how long does it take {{agency}} to reconcile carrier commission statements each month? Agencies I talk to with 20+ carriers usually spend 2–4 days in Excel and still suspect money is missing from smaller carriers and MGAs. Send me last month's statements + your AMS commission report, and I'll return a free reconciliation showing anything unpaid or short-paid. Want to try it? — {{you}}

**First customer strategy:** free reconciliation of one month, done mostly by hand with the extraction script → show $ found → sell the backlog reconciliation ($499) + monthly plan.

**First 10:** 300 independent agencies from state DOI license data + Google Maps in two states; email + LinkedIn + calls; ask 3 agency accounting/bookkeeping consultants for introductions.

**First 100:** partnerships with agency networks/clusters (they aggregate small agencies), agency accounting consultants (referral fee), state Big I chapter events, content ("commission reconciliation template", "how to audit carrier statements"), a HawkSoft/EZLynx user-community presence.

**$1K MRR path:** about 5 agencies at ~$200 plus backlog projects.
**$5K MRR path:** about 22 agencies; 2–3 agency-network partnerships; carrier template library covers the top 100 carriers/MGAs.
**$10K MRR path:** about 40 agencies at ~$250; producer-commission module; IVANS-file ingestion; expand to life/health agencies.

**Approximate monthly operating costs (~25 customers):** hosting/DB $60–120 · LLM $50–200 (more parsing than SubShield) · email $20 · storage $10 · tools $100 · **≈$250–450/mo + Stripe**, plus **significant founder time on accuracy** early on.

**Honest warning:** Applied Recon (inside Epic) and a newer AI startup (Commission Wizard) already target this. Your edge must be non-Epic agencies + MGA/wholesaler statements + done-with-you accuracy.

---

## C. PayrollProof — certified payroll for public-works subcontractors

**Ideal customer:** specialty subcontractor (electrical, concrete, paving, landscaping, HVAC) with 10–80 field workers, doing 2+ prevailing-wage jobs at a time, running payroll in QuickBooks Payroll, Gusto or ADP, starting in **California** (DIR registration + state electronic certified payroll reporting) plus federal Davis-Bacon jobs.

**Buyer persona:** Rosa, office manager at a 35-person concrete sub. Every Monday she exports Gusto payroll, splits hours by project in Excel, types each worker's classification/rate/fringe into WH-347s, uploads to two different agency systems, and fixes rejections. Takes about 6 hours/week.

**Customer workflow today:** timesheets → payroll run → manual hours-by-project split → WH-347 + Statement of Compliance typed → state/agency portal entry → rejection fixes → wet/e-signatures.

**Product workflow:** upload payroll export (+ hours-by-project CSV or simple timesheet grid) → map each worker once to classification per project → load the project's wage determination (the user uploads/selects it; you don't guess) → automatic checks (rate ≥ prevailing, fringe totals, overtime, apprentice ratio warnings) → generate WH-347 + Statement of Compliance PDF + agency/state upload file → e-sign → archive.

**MVP features:** projects (with wage determination attached), workers, classification mapping, payroll CSV import (QuickBooks/Gusto/ADP formats), weekly payroll builder, rate/fringe checks, WH-347 + SOC PDF (current DOL version), "no work performed" weeks, one state's electronic format, archive/history.

**Features NOT to build:** running payroll itself, tax filing, union fringe remittance, all 50 states, direct agency portal API submission, wage-determination scraping (attach PDFs manually at first).

**Dashboard:** this week's payrolls by project (Not started / Ready / Submitted / Rejected) · rate-check warnings · upcoming due dates · missing worker mappings.

**Database entities:** Company, User, Project, WageDetermination (classification, base rate, fringe, effective dates), Worker, WorkerClassification (per project), PayrollImport, PayrollWeek, PayrollLine (hours by day, rate, fringe, deductions), CheckResult, GeneratedReport (PDF/XML/CSV), Signature, AuditLog, Subscription.

**Backend architecture:** Django + Postgres; import parsers per payroll provider; a deterministic rules engine (no AI needed for calculations); a PDF generator (form-accurate WH-347); an XML/CSV generator per target system; immutable report versions with hashes; full audit log.

**API/integrations:** Stripe, Postmark, e-sign (Documenso/Dropbox Sign), file imports. Later: Gusto/QuickBooks APIs, agency-portal upload formats (LCPtracker/Elation-compatible files).

**Notifications:** Monday "payrolls due this week", warnings when a rate is below the determination, rejection follow-ups, project start/end reminders ("submit a final payroll").

**Authentication:** email/password + Google/Microsoft; roles Owner/Payroll/Viewer; 2FA (payroll PII); the federal WH-347 uses an individual identifying number (e.g., last four SSN digits), but some state/agency systems require full SSNs, so encrypt SSN fields and show them only to Payroll/Owner roles.

**Subscription billing:** Stripe; tiers by active public projects; annual; one-time setup fee ($149) to map workers and determinations.

**Pricing tiers:**
| 1 Project $99/mo | Crew $199/mo (≤5 active projects) | Pro $349/mo (unlimited, multi-state) | Done-for-you +$300/mo |

**Onboarding:** add project → attach wage determination → upload last week's payroll export → map workers (one time) → **aha: a correct WH-347 generated in 10 minutes instead of 2 hours** → e-sign → download/upload.

**Landing page:** headline "Certified payroll in 10 minutes, from the payroll you already run." · subheadline "Upload your QuickBooks, Gusto or ADP export, and PayrollProof builds your WH-347, checks every rate against the wage determination, and creates your state upload file." · CTA "Send us last week's payroll — we'll build it free."

**Cold outreach (trigger-based):**
> Subject: certified payroll for the {{project}} job
> Hi {{name}}, congrats on the {{agency}} {{project}} award. Prevailing-wage jobs mean weekly certified payroll. If you're on Gusto or QuickBooks, that's usually hours of retyping per week. Send me one week's payroll export and I'll return a completed WH-347 + state upload file, free, to show you how it works. — {{you}}

**First customer strategy:** do the first 4 weeks of certified payroll *by hand* (with your import script) for $199 → convert to monthly.

**First 10:** California DIR PWC-100 project awards + registered contractor lists → identify subs on recently awarded projects → call + email; partner with 2 construction bookkeepers who do certified payroll for clients.

**First 100:** construction bookkeeper/CPA channel (multi-client tier); trigger-based outreach on new awards each week; content ("WH-347 2025 form changes explained", "certified payroll with Gusto"); AGC/ABC/AGC-affiliated chapters; add a second state.

**$1K MRR path:** about 7 subs at ~$150.
**$5K MRR path:** about 30 subs + 3 bookkeeper partners managing many clients.
**$10K MRR path:** about 50 subs + bookkeepers; 2–3 states; apprentice reporting + fringe-benefit statements module.

**Approximate monthly operating costs:** hosting/DB $50–120 · e-sign API $0–50 · email $20 · storage $10 · tools $100 · **≈$200–300/mo + Stripe** (no AI costs needed).

**Honest warning:** LCPtracker already offers payroll-export uploads and some agencies provide it free to contractors. Interview for "how many different agency systems do you submit to?" Pain multiplies with the number of systems, and that's your opening.
