# Deep Dive #2: CredCadence (provider credentialing & re-attestation) — Score 75.5

## Ideal customer profile
- Independent **group behavioral-health/therapy practices** with 5–30 clinicians (LCSW, LPC, LMFT, PsyD, PMHNP), billing 5–15 commercial payers + Medicaid/Medicare
- Has an office/practice manager; often uses SimplePractice, TherapyNotes, or Valant for the EHR
- Hiring clinicians regularly (each needs CAQH + payer panels before they can bill)
- **Second ICP (channel):** solo credentialing specialists and small billing companies managing 10–100 practices

## Customer persona
**Marcus, practice manager at a 14-clinician therapy group in Ohio.** He handles credentialing himself between billing and HR. Last quarter, a clinician's CAQH attestation lapsed. One payer suspended the network status, and **$18k of claims denied over six weeks.** He tracks everything in a spreadsheet with 9 tabs and his calendar. He wants one screen that says what's due and who needs to do it.

## Exact problem statement
> "Every clinician has a dozen credentials and enrollments, each on its own renewal cycle (CAQH every 120 days, licenses, malpractice, payer revalidations), and if any lapse, we stop getting paid for that clinician, often without noticing for weeks."

## Value proposition
**Never lose a claim to a lapsed credential.** CredCadence tracks every renewal for every clinician, tells the right person exactly what to do and when, and screens your staff against federal exclusion lists every month.

## Positioning
For **group practices with 5–40 clinicians** that manage credentialing in spreadsheets, CredCadence is the **credentialing calendar and compliance log** that **prevents lapses and documents monthly exclusion screening**. Unlike enterprise credentialing platforms or outsourced firms, it's **self-serve, priced per provider, and set up in a day.**

## Name ideas
CredCadence · PanelGuard · CredKeeper · AttestIQ · ProviderPulse · CleanPanel

## Domain ideas *(unverified)*
credcadence.com · panelguard.io · credkeeper.app · attestiq.com · cleanpanel.io

## MVP architecture
Same boring stack as SubShield (Django + Postgres + job queue + S3 + Postmark + Twilio + Stripe), with **field-level encryption** (e.g., Django encrypted fields with keys in a KMS) for SSN/DOB/DEA numbers.
Additional jobs: **monthly OIG LEIE file download + SAM.gov exclusions API screening**, plus **NPPES lookup** on provider creation.

## Database structure
`organizations`, `users`, `memberships` (owner/admin/provider-self), `providers` (NPI, name, credentials, taxonomy, encrypted SSN/DOB, email/phone, status), `licenses` (state, type, number, issued, expires, verification_url), `dea_registrations`, `board_certifications`, `malpractice_policies`, `caqh_profiles` (caqh_id, last_attested_at, next_due computed = +120d), `payers`, `enrollments` (provider×payer: status, effective date, revalidation due, group/individual), `documents`, `tasks` (type, due, assignee, status), `exclusion_screenings` (run_at, source, result per provider, evidence file), `notifications`, `audit_log`.

## Frontend pages
Dashboard · Providers list · Provider profile (credentials timeline, enrollments grid, documents) · Payer enrollment board (kanban: not started → submitted → pending → active) · Tasks · Exclusion screening log · Reports (expiring, audit export) · Provider self-service page (upload docs, see "your next actions") · Settings/billing.

## Backend services
NPI lookup service · document intake + extraction · renewal rules engine (cadences per credential type, configurable by state) · task generator · exclusion screener (monthly + on new hire) · notifier · report generator · audit logger.

## Integrations
NPPES NPI Registry API (free/public) · OIG LEIE downloadable file (updated monthly) · SAM.gov Exclusions API · Twilio · Postmark · LLM extraction · e-sign (for attestation documents) · later: Nursys e-Notify, state Medicaid exclusion lists, CAQH partnership.

## Automation workflows
1. **New clinician:** NPI lookup → pre-filled profile → task checklist (CAQH profile, license copies, malpractice, payer applications) → provider receives self-service link.
2. **CAQH cadence:** reminder to the provider at day 100, 110, 118 after the last attestation → escalate to the manager.
3. **Expirations:** 90/60/30/7-day alerts for licenses, DEA, malpractice, and board certifications; on renewal, the uploaded doc auto-updates the date.
4. **Monthly exclusion screen:** run against LEIE + SAM → store the evidence PDF → alert immediately on a match.
5. **Payer revalidation:** reminders at 6 months/3 months/1 month.
6. **Monthly report** to the owner: "All 14 clinicians clear; 3 items due next 30 days."

## Onboarding flow
Enter group NPI → auto-import individual NPIs (or a CSV) → choose payers from a list → upload a zip of credential docs (or concierge load) → set CAQH last-attestation dates → first exclusion screen runs instantly (**aha: "All clear — documented"**) → invite providers.

## Dashboard layout
KPI row: Providers clear % · Items due ≤30 days · Overdue · CAQH attestations due · Last exclusion screen (date + result). Below: "Due this week" task list by assignee; enrollments by status; activity feed.

## Notification system
Email + SMS to providers (they ignore email), digests to managers, instant alert on an exclusion match or an expired license. Frequency caps, quiet hours.

## Billing system
Stripe; per-active-provider pricing with a minimum; annual option; firm tier billed per managed provider.

## Authentication system
Email/password + Google/Microsoft; **mandatory 2FA for admins** (sensitive PII); provider self-service via magic links with limited scope; session timeouts of 30 minutes idle.

## Admin dashboard
Orgs/MRR, screening job health (did the monthly LEIE load succeed?), failed notifications, extraction accuracy, provider counts, impersonation with logging.

## Security requirements
Field-level encryption for SSN/DOB/DEA; strict RBAC; audit logs on views of sensitive fields; 2FA; backups; data processing agreement; **be ready to sign a HIPAA BAA** (some customers will insist even if the data is mostly not PHI); never log PII; SOC 2 earlier than in SubShield (~$5k–8k MRR).

## Pricing tiers
| | Practice | Group | Credentialing Firm |
|---|---|---|---|
| Price | $35/provider/mo (min $99) | $29/provider/mo (min $299) | $15/provider/mo (min $299), multi-client |
| Exclusion screening | Monthly | Monthly + new hire | Monthly + new hire |
| Payer enrollment board | ✓ | ✓ | ✓ |
| Provider self-service | ✓ | ✓ | ✓ |
| Done-for-you credentialing | add-on quote | add-on quote | – |

## Free trial strategy
14-day trial with a **free exclusion screen + credential gap report** as the hook; a card is required for the trial on the Firm tier (higher intent).

## Annual pricing strategy
2 months free; position annual around license renewal cycles; firms get annual volume pricing.

## Cancellation flow
Reason survey → offers: downgrade to "Screening only" ($49/mo: monthly exclusion screening + archive, which compliance requires anyway) → export everything (documents zip + CSV).

## Retention strategy
The exclusion-screening audit trail (practices need to show monthly screening history to payers/auditors); provider self-service becomes habit; the enrollment board becomes the source of truth; quarterly "credentialing health report."

## Landing page structure
Hero → "The $18k CAQH mistake" story → how it works → features → ROI ("one lapsed enrollment = X weeks of denied claims") → pricing → FAQ → CTA "Free credentialing health check."

## Headline
**"Never lose a claim to a lapsed credential."**

## Subheadline
"CredCadence tracks every license, CAQH attestation, malpractice policy, and payer revalidation for every clinician, nudges the right person before deadlines, and documents monthly exclusion screening automatically."

## Features section
120-day CAQH autopilot · License & DEA expiry tracking · Payer enrollment board · Monthly OIG/SAM exclusion screening with saved evidence · Provider self-service uploads · Audit-ready reports.

## Pricing page copy
"Priced per clinician. Less than one denied claim per year." Toggle annual. "Includes monthly exclusion screening, which practices often pay for separately."

## FAQ
Do you do the credentialing applications for us? *(No, but our partners can; the software keeps you on top of it.)* · Is this HIPAA compliant? *(We sign BAAs and encrypt sensitive fields; we store credential data, not patient records.)* · Do you verify licenses with the primary source? *(We link to and record your verification; automated primary-source verification is on the roadmap. We don't claim NCQA CVO status.)* · Can credentialing firms manage multiple practices? *(Yes, Firm tier.)* · What happens to our screening history if we cancel? *(Export, or keep it in Screening-only mode.)*

## Cold email template
> **Subject:** CAQH re-attestations at {{practice}}
>
> Hi {{first_name}}, how do you keep track of CAQH re-attestations and license renewals for your {{n}} clinicians?
>
> Most group practices I talk to use a spreadsheet, and they find out about a lapse when claims start denying.
>
> I'll run a **free credentialing health check**: send me your clinician list (names + NPIs), and I'll return their exclusion-screening results and a list of what's likely due in the next 90 days. Takes 10 minutes on your side.
>
> Interested? — {{name}}

## LinkedIn message
> Hi {{first_name}}, I'm building a lightweight credentialing tracker for group practices (CAQH 120-day reminders, license/malpractice expirations, monthly OIG/SAM screening). I'm offering free credentialing health checks to a handful of practices. Open to a 15-minute chat?

## Google keywords
CAQH re-attestation reminder · CAQH attestation every 120 days · provider credentialing software for small practices · credentialing tracking spreadsheet · OIG exclusion screening monthly · SAM exclusion check healthcare · therapist credentialing software · payer enrollment tracker · Medicare revalidation due date lookup.

## SEO content ideas
"CAQH re-attestation: the complete guide for group practices" · "Monthly OIG exclusion screening: is it required and how to document it" · "Credentialing timeline: how long each payer takes" · free **exclusion screening tool** (enter names/NPIs, get results) · credentialing checklist template · state-by-state license renewal cycles for LPC/LCSW/LMFT.

## Reddit / community strategy
r/therapists (practice-owner threads, careful about self-promotion rules), r/medicalbilling, private-practice-owner Facebook groups (very active), credentialing-specialist Facebook groups. Contribute expert answers; share free tools.

## Partnerships
Medical billing companies (white-label/referral) · freelance credentialing specialists (Firm tier) · practice-management consultants · group-practice coaching programs · EHR marketplaces (later).

## First 10 customers
Join 5 practice-owner/credentialing communities → offer free health checks (manually run LEIE/SAM screens + spreadsheet review) → convert to a $99–$299/mo founding plan. Also recruit 3 freelance credentialers to use it for their clients.

## First $1,000 MRR
≈5 group practices at ~$200, or 2 credentialing firms + 2 practices.

## $5,000 MRR
≈20 practices + 5 firms; billing-company partnerships; free screening tool driving SEO leads.

## $10,000 MRR
Firms channel scales (each firm = 20–100 providers); add payer-enrollment workflows; expand to PT/OT and primary care; SOC 2; BAA-ready security program.

## Manual behind the scenes
Exclusion screening run by hand at first (download LEIE, search SAM manually, save PDFs); data entry from credential docs; setting up cadences per state; payer revalidation dates researched by you; reports built in Google Docs.

## Critical risks
- **Data sensitivity** raises your security bar from day one.
- **Practice managers are overloaded**: if the tool adds work, it dies. Design for "provider does it themselves."
- **The market's real money is in services** (doing the credentialing). Expect pressure to become a service business; decide deliberately.
