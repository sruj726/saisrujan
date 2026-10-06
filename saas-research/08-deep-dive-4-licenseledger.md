# Deep Dive #4: LicenseLedger (trade workforce licenses & certifications) — Score 72.5

> **Recommendation up front:** build this as **SubShield's second module**, not as a separate company. The buyer (contractor office/admin), the mechanics (expiring documents + reminders + extraction), and the channel (contractor associations, brokers) are identical. This deep dive is written as standalone so you can compare, but the go-to-market section assumes the bundle.

## Ideal customer profile
Electrical (and secondarily plumbing/HVAC) contractors with **15–150 field employees** in a state with journeyman/master licensing **and continuing-education requirements**, doing commercial work where GCs/owners request license proof and prequal packets.

## Customer persona
**Karen, HR/office manager at a 60-electrician contractor in North Carolina.** Tracks journeyman/master licenses, OSHA 10/30 cards, lift certifications, and a few CDLs in a spreadsheet. A tech's license lapsed on a hospital job last year and the GC removed him from site for 2 weeks. GCs keep asking for "a packet of everyone's certs" in prequal forms.

## Exact problem statement
> "Our technicians hold dozens of licenses and certifications that expire on different dates and require CE hours. We track them by hand, chase techs for photos of their cards, and scramble every time a GC or inspector asks for proof."

## Value proposition
**Every tech licensed, every card on file, every packet ready in one click.**

## Positioning
For **specialty trade contractors**, LicenseLedger is the **text-first credential tracker** that **collects card photos from techs, tracks CE and renewals, and builds prequal packets instantly**. Unlike generic HR software, it **knows trade license rules**.

## Name ideas
LicenseLedger · CardCheck · CrewCreds · TradeCreds · CertCrew

## Domain ideas *(unverified)*
licenseledger.com · crewcreds.com · tradecreds.io · certcrew.app

## MVP architecture
The same codebase as SubShield (Django + Postgres + Twilio + LLM extraction + S3 + Stripe), with "people" as a second entity type next to "vendors."

## Database structure
`employees` (name, phone, role, status, hire date), `credential_types` (library: name, issuing body, renewal cycle, CE hours, state), `employee_credentials` (number, issued, expires, CE hours logged, document_id, status), `company_credentials` (contractor license, bonds, business licenses), `ce_records`, `packets` (generated bundles for a project/GC), shared `documents`, `requests`, `notifications`, `audit_log`.

## Frontend pages
Dashboard · Employees list (compliance %) · Employee profile · Credential library/rules · Company licenses & bonds · **Packet builder** (select crew → PDF of cards) · Tech mobile upload page · **Public QR credential card** (shows verified-by-company status, not raw PII) · Reports · Settings.

## Backend services
Rules engine (renewal + CE cadence) · SMS requests · extraction (card photos) · packet PDF generator · QR card renderer · scheduler.

## Integrations
Twilio, LLM, e-sign (optional) · later: Gusto/ADP roster sync, ServiceTitan/Procore crew data, state license lookup links.

## Automation workflows
New hire → SMS asks for license + card photos → extraction → status. 90/60/30-day renewal reminders to the tech + manager, with CE hour shortfall warnings. Expired → alert + "remove from license-required jobs" note. Packet requests → generated in seconds.

## Onboarding flow
Choose trade + state → library pre-loads credential types → import employees (CSV/paste) → texts go out → the dashboard fills in live (aha: "38 of 60 techs fully documented; 6 licenses expire within 90 days").

## Dashboard layout
KPI row: Crew compliant % · Expiring ≤90 days · Expired · Missing cards. Then: renewals calendar, CE shortfalls, company license/bond expirations, recent uploads.

## Notification system
SMS to techs; email digests to the admin; monthly report to the owner.

## Billing system
Stripe; $4/employee/month (min $59); bundled discount with SubShield.

## Authentication system
Admin accounts like SubShield; techs use scoped magic links; QR card pages are public but show only name/photo/credential type/valid-through, and can be revoked.

## Admin dashboard
Shared with SubShield admin.

## Security requirements
Employee PII (license numbers, DOB on cards): encryption, minimal display on QR pages, RBAC, audit logs, deletion on request (respecting retention needs).

## Pricing tiers
Crew (≤25 employees) $79 · Company (≤100) $249 · Enterprise (≤300) $499 · **Bundle with SubShield Pro: +$99/mo**.

## Free trial strategy
Free "crew credential audit" via a CSV import; 14-day trial.

## Annual pricing strategy
2 months free; align with the state license renewal cycle.

## Cancellation flow
Same as SubShield; archive mode at $19/mo.

## Retention strategy
CE history, packet library, QR cards in the field (techs and GCs rely on them), integration with the COI module.

## Landing page structure / headline / subheadline
- **Headline:** "Every tech licensed. Every card on file."
- **Subheadline:** "LicenseLedger collects license and certification photos by text, tracks renewals and CE hours, and builds prequal packets in one click."
- **Sections:** problem story (tech pulled from site) → how it works → features → pricing → FAQ.

## Features section
Text-to-upload card photos · Trade license rules library · CE hour tracking · Company license & bond tracking · One-click prequal packets · QR credential cards.

## Pricing page copy
"Less than the cost of one day with a tech pulled off a job."

## FAQ
Does it verify with the state board? *(It links to the board's lookup and records your verification; automatic verification is on the roadmap.)* · Do techs need an app? *(No.)* · Can GCs scan a QR to verify? *(Yes, with limited info.)*

## Cold email
> **Subject:** license packets for GCs
> Hi {{first_name}}, how long does it take {{company}} to pull together license and OSHA card copies when a GC asks for them? I built a simple tool where techs text in their cards and you get a one-click packet, plus renewal and CE reminders. Want a free crew credential audit?

## LinkedIn message
> Hi {{first_name}}, I'm working with electrical contractors on tracking journeyman/master licenses and CE renewals without spreadsheets. Open to a quick chat on how you handle it today?

## Google keywords
contractor license tracking software · employee certification tracking construction · journeyman license renewal reminder · OSHA card tracking · CE hours tracking electricians · prequalification packet contractors.

## SEO content ideas
State-by-state electrical license renewal and CE guides (very long-tail, very boring, very rankable) · "Prequal packet checklist" · "Certification tracking spreadsheet template."

## Reddit / community
r/electricians (mostly techs, so use it for research), IEC/IBEW-adjacent groups, contractor owner Facebook groups.

## Partnerships
IEC/ABC chapters, CE course providers (cross-promotion: "your license is due, take CE here" earns an affiliate fee), supply houses, insurance brokers (same as SubShield).

## First 10 / $1k / $5k / $10k MRR
As a **module**, the plan is: sell it to existing SubShield customers first (target a 30% attach rate) → $1k MRR from ~12 bundles → then market standalone to electrical contractors via state CE-guide SEO and IEC chapters. As a standalone company, I would not expect $10k MRR faster than SubShield, which is why it's a module.

## Manual behind the scenes
Build the credential rules library by hand for 1 state; data entry from card photos; packet assembly.

## Critical risks
Moderate pain ("nice to have" until something goes wrong); HRIS vendors can add it; standalone ARPU is low for small crews.
