# Deep Dive #5: InspectLoop (recurring fire & life-safety inspections) — Score 71.0

> **Honest framing:** this is the biggest prize of the five (a system of record with very low churn), but it's the **worst fit for a 2–6 week solo MVP**. It's included because the scores put it there. Build it only if you or a cofounder has worked in fire protection.

## Ideal customer profile
Fire-protection service companies with **2–15 technicians**, focused on **portable extinguishers + kitchen hood suppression + emergency lighting** (simpler, high-volume inspection types) in one metro, running on paper or a generic FSM, with 300–3,000 recurring customer locations.

## Customer persona
**Tony, owner of a 6-tech extinguisher & hood company.** Grew up in the trade. His wife does scheduling from a whiteboard and QuickBooks. Techs fill paper reports that get scanned "eventually." He knows that deficiencies found on inspections are unquoted money left on the table, and that some customers' annual inspections silently get missed every year.

## Exact problem statement
> "We have hundreds of buildings that need inspections on fixed cycles. Scheduling them, getting reports to customers (and sometimes the fire marshal), and turning deficiencies into repair work all happens on paper, so visits get missed and repair revenue leaks."

## Value proposition
**Never miss a recurring inspection or an unquoted deficiency again.**

## Positioning
For **small fire & life-safety contractors**, InspectLoop is the **inspection-first field app** that **schedules recurring visits automatically and turns every deficiency into a quote**. Unlike heavy field-service suites, it's **set up in a day and priced for 2–15 techs.**

## Name ideas
InspectLoop · TagDay · RecurInspect · DeficiencyIQ · LifeSafe Ops

## Domain ideas *(unverified)*
inspectloop.com · tagday.io · recurinspect.com

## MVP architecture
Django backend + **offline-capable PWA** for techs (IndexedDB queue, background sync), Postgres, S3 for photos, PDF generation, Stripe, QuickBooks Online API. Offline is non-negotiable (basements, mechanical rooms).

## Database structure
`customers`, `sites` (address, AHJ, contacts), `systems` (type: extinguisher/hood/sprinkler/alarm/e-light; specs), `assets` (each extinguisher: location, type, size, manufacture date, hydro-test due, 6-year maintenance due), `inspection_templates` (versioned checklists), `schedules` (system × frequency), `visits` (date, tech, status), `inspection_results` (per asset item pass/fail/notes/photos), `deficiencies` (severity, description, photo, status), `quotes`/`quote_lines`, `reports`, `users` (office/tech roles), `notifications`, `audit_log`.

## Frontend pages
Office: dashboard, schedule calendar/map list, customers/sites, site detail (systems, assets, history), deficiencies pipeline, quotes, reports, settings. Tech PWA: today's route, site checklist, asset-by-asset inspection, photo capture, signature capture, sync status.

## Backend services
Recurrence engine (monthly/semiannual/annual + asset-level due dates like hydrostatic tests) · offline sync API (conflict handling) · report generator (immutable PDF with hash) · deficiency→quote generator with price book · customer reminder emails · QBO sync (customers, invoices).

## Integrations
QuickBooks Online · Twilio/Postmark · Google Maps (routing later) · AHJ portals manually at first (many jurisdictions use third-party reporting portals; integration is a later moat).

## Automation workflows
Visits auto-generated 30 days before due → office assigns → tech completes offline → report PDF auto-emailed to the customer → deficiencies auto-quoted from the price book → quote follow-ups at 3/7/14 days → accepted quotes become jobs → missed visit alerts.

## Onboarding flow
Import customer/site list (CSV from QBO) → choose inspection types → bulk-create schedules → load assets as techs visit (first visit builds the asset inventory) → aha: "Deficiency pipeline: $14,200 in unquoted repairs this month."

## Dashboard layout
KPIs: visits due this month · overdue · completion rate · deficiencies found · quoted $ · accepted $. Then calendar, overdue list, deficiency pipeline.

## Notification system
Customer reminders/reports (email), office alerts (overdue, quote accepted), tech daily schedule (SMS/push).

## Billing system
Stripe; per-tech pricing with an office-seat minimum; annual discount.

## Authentication system
Office users (email/password + Google + 2FA), tech users (PIN-based login on company devices, long-lived offline sessions with remote revocation).

## Admin dashboard
Sync errors, report generation failures, org health (visits/week), MRR.

## Security requirements
Report integrity (immutable PDFs, hash, audit trail: these are life-safety records), offline data encryption on devices, RBAC, backups, retention for years.

## Pricing tiers
Starter $199/mo (≤3 techs) · Growth $399 (≤8) · Pro $599 (≤15) · extra tech $49. Customer portal and AHJ submission service as add-ons.

## Free trial strategy
No self-serve trial (setup-heavy). **Paid onboarding** ($500, credited) with data import done for them, then month-to-month.

## Annual pricing strategy
2 months free; most customers will go annual after the first busy season.

## Cancellation flow
Export all site/asset/report history (they're legally needed), read-only archive at $49/mo.

## Retention strategy
Asset history and report archive are a near-total lock-in; deficiency revenue reports show ROI monthly.

## Landing page
- **Headline:** "Every inspection on time. Every deficiency quoted."
- **Subheadline:** "InspectLoop schedules recurring fire & life-safety inspections, gives techs an offline app that builds the report as they go, and turns deficiencies into quotes automatically."
- **Features:** recurring schedules · offline tech app · instant branded reports · deficiency-to-quote · customer reminders · QuickBooks sync.
- **Pricing copy:** "Recover one missed deficiency quote a month and it pays for itself."
- **FAQ:** works offline? NFPA forms? AHJ submission? data import? QuickBooks?

## Cold outreach
> **Subject:** unquoted deficiencies
> Hi {{first_name}}, quick question for {{company}}: when your techs find a deficiency on an extinguisher or hood inspection, how does it become a quote today? Most 3–10 tech shops I talk to estimate 30%+ never get quoted. I'm building a simple inspection app that fixes that, and I'd love 15 minutes to learn how you run things.

**LinkedIn:** low yield. Phone and in-person visits at distributor counters work better.

## Google keywords
fire extinguisher inspection software · hood suppression inspection app · fire inspection report software · NFPA 10 inspection app · fire protection service software small business.

## SEO content
NFPA 10 inspection checklist (PDF) · "6-year maintenance and hydrostatic test schedules explained" · deficiency pricing guides.

## Community / partnerships
NAFED (extinguisher distributors association), state fire-equipment dealer associations, equipment distributors, fire-marshal events.

## First 10 / $1k / $5k / $10k MRR
10 customers need in-person demos and data migration. $1k MRR = ~4 customers. $5k = ~17. $10k = ~33 (fewer customers needed thanks to high ARPU, but each takes far longer to land and onboard).

## Manual behind the scenes
Data migration, building inspection templates per customer, price book setup, AHJ uploads done by you as a service.

## Why it's not my pick for you
6–10 week MVP minimum (offline sync is genuinely hard), domain knowledge needed to earn trust, support-heavy onboarding, and PE roll-ups are consolidating this industry onto ServiceTrade/BuildOps-class platforms.
