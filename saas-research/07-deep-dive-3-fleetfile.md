# Deep Dive #3: FleetFile (DOT driver qualification files) — Score 75.0

## Ideal customer profile
- US interstate motor carrier with **3–40 power units**, 1–5 years old (or a new entrant facing the safety audit)
- Owner-operator-turned-fleet-owner; no dedicated safety manager or a part-time one
- Uses an ELD (Motive, Samsara, etc.) but not its compliance add-ons
- Also: construction/waste companies running CDL trucks under their own USDOT number

## Customer persona
**Luis, owner of a 9-truck flatbed carrier in Texas, authority 14 months old.** Dispatch, sales, and safety are all him plus his wife. DQ files live in a filing cabinet and his phone's photo roll. He got the new-entrant safety audit letter and panicked. A safety consultant quoted $1,500 to "clean up files." He prefers WhatsApp/text over email, and his drivers do too. Half his drivers prefer Spanish.

## Exact problem statement
> "I have to keep a complete, current qualification file for every driver: med cards, MVRs, annual reviews, Clearinghouse queries. Drivers come and go, documents expire, and I only find out what's missing when an auditor or my insurance company asks."

## Value proposition
**Audit-ready driver files, collected by text.** FleetFile tells you exactly what's missing for every driver, gets drivers to send it from their phone, and reminds you before anything expires.

## Positioning
For **small trucking fleets** that keep DQ files on paper, FleetFile is the **text-first DQ file manager** that **makes you audit-ready in a weekend and keeps you that way**. Unlike enterprise safety suites and recruiting platforms, it's **simple, bilingual, and priced for 3–40 trucks.**

## Name ideas
FleetFile · DQ Ready · AuditReady Fleet · DriverFile · RigReady · CleanDQ

## Domain ideas *(unverified)*
fleetfile.io · dqready.com · driverfile.app · rigready.io · cleandq.com

## MVP architecture
Django + Postgres + job queue + S3 + **Twilio (SMS-first)** + Postmark + LLM vision extraction + e-sign (Documenso/Dropbox Sign API) + Stripe. Mobile-first web pages for drivers (no app install). English/Spanish i18n from day one.

## Database structure
`carriers` (USDOT, MC, legal name, address, fleet size from FMCSA data), `users`, `drivers` (name, CDL number/state/class, DOB encrypted, hire date, status, phone, language), `dq_requirements` (catalog: application, MVR initial, MVR annual, annual review, med cert, road test/CDL copy, previous employer inquiries, Clearinghouse pre-employment + annual, etc., with cadence rules), `driver_items` (driver×requirement: status, document_id, effective, expires, due), `documents`, `driver_requests` (token, SMS sent, status), `annual_reviews` (signed doc), `notifications`, `audit_log`, `subscriptions`.

## Frontend pages
Dashboard · Drivers list (completion % per driver) · Driver file (checklist with status chips, docs, history) · **Driver mobile upload page** (snap photo of med card/CDL, sign forms) · Driver application form (public link, FMCSA-compliant fields) · Reports/Audit export (one PDF per driver, ordered per audit expectations) · Settings/billing.

## Backend services
FMCSA carrier lookup (by USDOT on signup) · SMS sender with conversation threading · extraction (med cert expiry, CDL expiry/class/endorsements) · rules engine (what's due when) · e-sign service · PDF DQ file assembler · scheduler.

## Integrations
FMCSA public data (SAFER/QCMobile API) · Twilio (10DLC registration needed) · e-sign API · LLM · later: MVR providers (via a consumer reporting agency), D&A consortium partners, ELD APIs for driver roster sync.

## Automation workflows
1. **Signup:** enter USDOT → company auto-filled → add drivers (name + phone) → each driver gets a bilingual text: "Your company needs 3 documents. Tap to upload."
2. **Upload:** driver photographs the med card → extraction → item marked complete with expiry → owner notified.
3. **Expiry engine:** med cert 60/30/14/7 days → SMS driver + alert owner; on expiry → "DRIVER NOT QUALIFIED" alert.
4. **Annual tasks:** annual MVR review and Clearinghouse limited query reminders; e-sign review form.
5. **New hire:** the application link goes to the candidate → creates a driver file → generates the previous-employer inquiry checklist.
6. **Audit mode:** one click → zip/PDF of every driver's DQ file + a gap report.

## Onboarding flow
USDOT lookup → add drivers → **instant gap report** (aha: "You're 41% audit-ready; 23 items missing") → send texts → watch the completion % climb in real time. Concierge option: "Mail/scan us your binders; we'll build the files" ($299).

## Dashboard layout
Big audit-readiness % gauge · drivers not qualified (red) · expiring ≤30 days · items awaiting driver · recent uploads feed · "Audit export" button.

## Notification system
SMS (primary, drivers + owner), email digests for the owner, WhatsApp later (popular with drivers). Bilingual templates. Quiet hours (drivers sleep at odd times; let them text back "LATER").

## Billing system
Stripe; $49 base + $8 per active driver/month; annual 2 months free; setup service as a one-time charge.

## Authentication system
Owner/admin accounts (email/password + Google + 2FA optional); drivers never get accounts, only **scoped, expiring magic links** per request.

## Admin dashboard
Carriers, MRR, SMS delivery rates/costs, extraction accuracy, 10DLC compliance status, failed jobs, churn-risk list (no uploads in 30 days).

## Security requirements
Encrypt DL numbers, DOB, and medical certs; RBAC; signed URLs; audit log; retention logic (DQ files kept for employment + 3 years, so do not auto-delete on driver termination); TCPA-compliant SMS consent; FCRA compliance if you ever handle MVR/background data (use a licensed CRA partner, never resell raw reports yourself).

## Pricing tiers
| | Starter | Fleet | Fleet+ |
|---|---|---|---|
| Price | $49 + $8/driver | $99 + $7/driver | $199 + $6/driver |
| Drivers | up to 10 | up to 50 | up to 150 |
| DQ checklist + SMS collection + alerts | ✓ | ✓ | ✓ |
| E-sign annual reviews & applications | – | ✓ | ✓ |
| Vehicle maintenance files | – | – | ✓ (v2) |
| Done-for-you DQ build | $299 one-time | $299 | included |

## Free trial strategy
Free **audit-readiness gap report** (no card). Paid plan to send texts to drivers. Or 14-day trial capped at 3 drivers.

## Annual pricing strategy
2 months free; target the **new-entrant audit window** ("Cover your first 18 months"). Note: annual plans reduce the high monthly churn of tiny carriers.

## Cancellation flow
Reason → if "closing the business": offer an **archive export** (legally they must retain records), pause option ($15/mo read-only) → if "too expensive": downgrade → export.

## Retention strategy
Retention requirement (records must be kept 3 years after employment ends, so archive mode is valuable); Clearinghouse annual reminders; CSA/inspection monitoring alerts (v2); maintenance files (v2) make it the fleet's safety binder.

## Landing page structure
Hero → "New entrant safety audit? Get ready this weekend." → how it works (USDOT → drivers text docs → you're ready) → checklist graphic → pricing → bilingual testimonials → FAQ → CTA "Free audit-readiness report."

## Headline
**"Audit-ready driver files. Collected by text."**

## Subheadline
"FleetFile shows exactly what's missing in every driver's DQ file, gets drivers to send it from their phone, and alerts you before med cards and reviews expire. Built for fleets of 3 to 50 trucks."

## Features section
USDOT-based setup in 2 minutes · Text-to-upload (English/Spanish) · Med card & CDL expiry reading · Annual review e-sign · Driver application link · One-click audit export.

## Pricing page copy
"Cheaper than one audit violation. Priced per driver, cancel anytime. Records always exportable."

## FAQ
Do drivers need an app? *(No, just a text link.)* · Is this legal advice? *(No. It organizes the federal requirements; consult a safety professional for your situation.)* · Do you pull MVRs? *(Not yet; upload your MVRs. Integration coming via a licensed provider.)* · Clearinghouse? *(We remind you and store the query records.)* · What if I sell my trucks? *(Export or keep an archive, since retention rules still apply.)*

## Cold email / call script (calls work better than email in trucking)
> "Hi Luis, this is {{name}}. I saw your authority became active last year. Has FMCSA scheduled your new-entrant safety audit yet? … Most small carriers fail on driver qualification files. I have a free tool that shows exactly what's missing in each driver file in 5 minutes. Want me to text you the link?"

Email version:
> **Subject:** your new entrant safety audit
> Hi {{first_name}}, new carriers most often get cited for incomplete driver qualification files. I built FleetFile to fix that: drivers text in their med cards, and you see exactly what's missing. Want a free audit-readiness report for {{company}}? Reply "yes" and I'll send the link.

## LinkedIn message
LinkedIn is weak for this ICP. Use Facebook trucking groups, phone, and SMS instead. For safety consultants on LinkedIn: "I built a DQ file tool that consultants can use for their carrier clients, with a reseller margin. Open to a quick look?"

## Google keywords
driver qualification file checklist · DQ file requirements · new entrant safety audit checklist · FMCSA driver file requirements · medical card expiration tracking · DOT audit preparation · driver qualification file software · annual review of driving record form.

## SEO content ideas
"New entrant safety audit: the complete checklist" · "DQ file checklist (free PDF, English/Spanish)" · "What happens if a driver's med card expires" · "Clearinghouse queries explained" · YouTube: "Building a DQ file in 10 minutes" · free DQ checklist generator.

## Reddit / community strategy
r/Truckers and r/trucking (mostly drivers, limited), **Facebook groups for small fleet owners/new authorities** (much better), YouTube comment sections of trucking business channels, TruckersReport forums. Lead with genuinely helpful audit prep content.

## Partnerships
Trucking insurance agents (they want audit-ready insureds) · factoring companies (they want carriers to survive) · authority-setup/filing services · CDL schools · safety consultants (reseller tier) · ELD resellers.

## First 10 customers
Pull the FMCSA new authority list for your state → call 30/day → offer the free gap report → convert with "$199 setup + first month free." Partner with 1 trucking insurance agent.

## First $1,000 MRR
≈10 carriers × ~$100. Achievable fast via phone; expect churn.

## $5,000 MRR
≈45 carriers; 3–5 insurance agent/factoring partners; bilingual YouTube content; reseller program for safety consultants.

## $10,000 MRR
≈80 carriers, plus the vehicle maintenance file module and D&A consortium partnership referrals; move upmarket to 20–75-truck fleets (lower churn).

## Manual behind the scenes
Build DQ files from scanned binders yourself (paid setup); verify extraction; manually generate audit PDFs; phone drivers who don't respond; research state-specific intrastate rules on demand.

## Critical risks
- **Tiny carriers churn hard** (business failure in freight downturns). Move upmarket fast.
- **ELD vendors** (Motive, Samsara) could make DQ management a free bundle.
- **Regulatory correctness** is a liability. Get a DOT compliance consultant to review your checklist logic (pay them, or make them a partner).
