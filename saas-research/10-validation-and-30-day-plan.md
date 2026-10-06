# Part 4 — Validation Test (run BEFORE building) + 30-Day Execution Plan for SubShield

## A. The validation test: "Paid COI Audit → Pilot"

### What we must prove (in this order)
1. **The problem is real and costly:** buyers can name a recent incident (audit chargeback, uninsured claim, sub removed from site, owner/GC rejection) and its dollar cost.
2. **There's a budget owner:** the person feeling the pain can spend $99–$399/mo on a card, or gets the owner to say yes in one conversation.
3. **They'll pay now, not "when it's ready":** money changes hands for a manual/concierge version.
4. **They'll hand over real data:** sending you their actual vendor list + COI PDFs is a strong trust and intent signal. A survey response is not.

### Vanity metrics we explicitly ignore
Email opens, LinkedIn likes, waitlist signups, survey "would you pay" answers, compliments on calls, "send me more info."

### The offer ladder
| Step | Offer | What it proves |
|---|---|---|
| 1 | **20-minute problem interview** (no pitch) | Pain, frequency, current cost, who decides |
| 2 | **Free 48-hour COI audit:** they send their spreadsheet + certificates; you return a deficiency report | Willingness to share real data (strong intent) |
| 3 | **Pricing conversation** on the results call: show the 3 tiers, ask "Which would you pick, and who approves it?" | Price acceptance, buying process |
| 4 | **Paid pilot:** $299 for 60 days of done-with-you tracking (credited to an annual plan), **paid by card on the call or invoice due in 7 days** | Real willingness to pay |
| 5 *(alternative)* | **$99 refundable deposit** to lock founding pricing ($99/mo Pro for 24 months) at launch | Pre-order commitment |
| 6 *(channel)* | **Broker letter of intent:** "We'll introduce SubShield to ≥5 clients within 60 days of launch" | Channel viability |

### Interview script (Mom Test style: ask about the past, not hypotheticals)
1. "Walk me through what happens when a new sub is added to a job."
2. "Who tracks COIs? How many subs/vendors are active right now?"
3. "When was the last time a sub's insurance turned out to be expired or wrong? What happened? What did it cost?"
4. "Have you ever been charged at a premium audit for uninsured subs? How much?"
5. "How many hours a week go into COIs? What would you do with that time?"
6. "What have you tried? Why did you stop / not buy it?" *(Listen for myCOI/TrustLayer/Billy price objections: that's your gap.)*
7. "If this were solved, who else would need to agree to pay for it?"
8. *(Only at the end)* "I'm running free COI audits this month. Want me to run one on your current list?"

### Sample size, pass/fail criteria, and timebox (21 days max)
- **Outreach:** 300 targeted GCs (cold email + calls) + 10 broker conversations
- **Target funnel:** 300 → 30 conversations → 15 audits → **≥5 paid pilots/deposits**

| Signal | PASS (build) | PIVOT-WARNING | KILL |
|---|---|---|---|
| Problem interviews held | ≥25 | 15–24 | <15 after 300 touches (channel problem) |
| Interviewees naming a costed incident in last 24 months | ≥40% | 20–39% | <20% |
| Audits requested (data handed over) | ≥12 | 6–11 | <6 |
| **Paid pilots or deposits** | **≥5 (≥$1,000 collected)** | 2–4 | **0–1** |
| Broker LOIs | ≥2 | 1 | 0 (not fatal alone) |
| Price objection pattern | ≤1/3 say $199 is "too much" | – | majority balk at $99 |

**Decision rule:** PASS → build (Week 2). PIVOT-WARNING → run a second 10-day round on a narrower segment (e.g., only $10–50M GCs, or property managers). KILL → move to **CredCadence** with the same validation design (offer: free credentialing health check → paid $299 setup pilot).

### What "paid" looks like operationally
Stripe Payment Link (no product needed) · simple 1-page pilot agreement: scope (up to 150 vendors, 60 days, weekly status report, you chase agents), price, credit toward annual, data handling + confidentiality, no guarantee of insurance coverage · deliver with Google Sheets + the extraction script + Gmail templates.

---

## B. 30-Day Execution Plan

**Team:** you (founder: sales, ops, concierge delivery) + 1 developer. **Stack:** Django + Postgres + Postmark + S3/R2 + LLM API + Stripe.
**Rule:** the developer builds only throwaway or reusable *pipeline* code until the Day-10 gate passes.

### $1,000 budget *(approximate; verify current prices)*
| Item | Cost |
|---|---|
| Domain + 2 secondary sending domains | ~$40 |
| Google Workspace (3 mailboxes for outbound, 1 month) | ~$45 |
| Cold email sending/warm-up tool (1 month) | ~$40–100 |
| Contact data tool (1 month, starter plan) or VA list-building | ~$100–150 |
| Hosting (Render/Railway/Fly) + managed Postgres + R2 | ~$40 |
| Postmark | ~$15 |
| LLM API usage (thousands of certificates) | ~$50 |
| CFMA/AGC chapter meeting(s) | ~$50–150 |
| Phone number + calling (Twilio/OpenPhone-type) | ~$20 |
| Stripe | $0 (fees only) |
| **Reserve** (legal template review, ads test, surprises) | ~$350–550 |
| **Total** | **≤ $1,000** |

---

### WEEK 1 — Customer validation (Days 1–7)

**Day 1 (Mon)**
- Founder: pick 2 metros (e.g., Dallas–Fort Worth + Houston). Define ICP filters ($5–50M commercial GCs). Buy domains; set up 3 outbound mailboxes on secondary domains (start warm-up today, since cold sending is safer after ~2 weeks; use personal 1:1 sends + calls meanwhile).
- Founder: write the interview script, audit-offer email, call script, and the 1-page pilot agreement.
- Dev: collect 30 sample ACORD 25 PDFs (public samples, your own business insurance, broker friends) and start an **extraction spike**: PDF → JSON (insured, producer, policies, dates, limits, AI/WOS checkboxes). Measure field accuracy.

**Day 2 (Tue)**
- Founder: build a list of 150 GCs (state contractor/registration data where available + Google Maps "commercial general contractor" + LinkedIn titles: project accountant, office manager, controller). Capture name, role, email, phone.
- Founder: 15 personalized emails + 15 calls. Goal: book 3 interviews.
- Dev: extraction spike v1; build a tiny CLI: folder of PDFs → spreadsheet of extracted fields + deficiency flags versus a requirement JSON.

**Day 3 (Wed)**
- Founder: 20 emails + 20 calls. Email 10 commercial insurance brokers who handle contractors: "I'll do a free COI audit for one of your clients."
- Founder: hold the first 2–3 interviews. Log every answer in a validation sheet (incident? cost? tool? decision maker? price reaction?).
- Dev: improve the extraction prompt/schema; add date sanity checks; hit ≥95% field accuracy on the sample set (with human review flags for the rest).

**Day 4 (Thu)**
- Founder: 20 emails + 20 calls + follow-ups. 3–4 interviews. Offer the free audit at the end of each.
- Founder: create the audit deliverable template (Google Doc/PDF): summary, exposure table, list of deficient subs, recommended requirement template.
- Dev: an "audit runner" that ingests a customer's spreadsheet + PDFs and outputs the deficiency report draft.

**Day 5 (Fri)**
- Founder: 3–4 interviews; run the **first 1–2 audits** (manually checked). Attend or schedule a CFMA/AGC chapter event.
- Founder: Friday review: tally the pass/fail metrics so far.
- Dev: harden the audit runner; start the Django skeleton (auth, orgs, vendors, documents, policies models) — this code is reusable either way.

**Day 6 (Sat)**
- Founder: deliver audits; write the results-call script with the pricing conversation + paid pilot offer. Draft a 1-page "how SubShield works" PDF and a 2-minute Loom demo of the audit report.
- Dev: rest or light work (avoid burnout; you'll need them in Week 2).

**Day 7 (Sun)**
- Founder: update the validation sheet. Plan Week 2 call blocks. Personalize next week's 100 emails.

### WEEK 2 — MVP development (Days 8–14) *while validation continues*

**Day 8 (Mon)**
- Founder: results calls for the first audits → **ask for the paid pilot** ($299/60 days). 20 calls + 25 emails. 3 more interviews.
- Dev: Postmark inbound webhook → documents table → extraction job → review queue (basic UI: PDF on the left, fields on the right).

**Day 9 (Tue)**
- Founder: more audits delivered; more pilot asks; broker follow-ups (ask for an LOI or 2 intros).
- Dev: requirement templates + rules engine (compliance status + deficiency list).

**Day 10 (Wed) — 🚦 GO/NO-GO GATE**
- Founder: count paid pilots/deposits, audits, and interviews against the criteria table.
  - **≥3 paid by today with a clear path to 5** → continue building.
  - **0–1 paid** → stop the MVP build; the dev keeps only the audit runner; you narrow the segment or switch to CredCadence validation.
- Dev (if GO): vendor list + CSV import + vendor detail page.

**Day 11 (Thu)**
- Founder: onboard paid pilots *manually* (you load their data with the audit runner). Kick off the first agent-chase emails from your Gmail using templates.
- Dev: outbound request emails with tokenized upload links + public upload page.

**Day 12 (Fri)**
- Founder: 20 calls/emails; 2 interviews; ask each pilot for one referral.
- Dev: scheduler: expiry windows (30/14/7/0), reminder cadence, frequency caps; weekly digest email.

**Day 13 (Sat)**
- Founder: write onboarding emails (day 0, 1, 3, 7) and the "you're covered" week-1 report template.
- Dev: dashboard KPI row + vendors table with status filters.

**Day 14 (Sun)**
- Both: end-to-end test with real (pilot-approved) data: email in → extraction → review → status → reminder. List bugs. Security basics: tenant scoping tests, signed URLs, rate limits.

### WEEK 3 — Beta customers (Days 15–21)

**Day 15 (Mon)**
- Founder: move pilots onto the product (you remain the reviewer behind the scenes). Each gets a dedicated inbox address and forwarding instructions.
- Dev: fix the top 10 bugs from Day 14; add the admin panel (orgs, unmatched docs, impersonation with logging).

**Day 16 (Tue)**
- Founder: daily check-in messages to each pilot ("3 COIs came in overnight, 1 deficient: we've emailed the agent"). Continue outreach (25/day) now with a *live product* demo.
- Dev: audit report generator (PDF by date range) — the hero feature.

**Day 17 (Wed)**
- Founder: watch every pilot user session/log; note confusion. Interview pilots: "What would make you cancel? What would you show your owner?"
- Dev: onboarding wizard (template pick → import → bulk PDF upload → "send requests").

**Day 18 (Thu)**
- Founder: sign 1–2 broker partners (referral agreement: 20% recurring for 12 months). Book a CFMA/AGC lunch-and-learn for next month.
- Dev: Stripe Checkout + Customer Portal + plan limits + webhooks; trial → read-only logic.

**Day 19 (Fri)**
- Founder: collect testimonials/quotes (with permission) and a "before/after" metric (e.g., "compliance went from 71% → 96% in 3 weeks").
- Dev: landing page (structure from the deep dive), pricing page, security page, privacy policy/terms (use a reputable template + the reserve budget for a quick review if possible).

**Day 20 (Sat)**
- Founder: write 3 SEO cornerstone pieces (premium audit chargebacks, how to read an ACORD 25, COI requirements checklist) + the downloadable spreadsheet template.
- Dev: free "COI Checker" single-upload tool (reuses extraction; captures email).

**Day 21 (Sun)**
- Both: retro. Fix onboarding friction. Confirm monitoring (Sentry, uptime, daily job heartbeat, backups + test restore).

### WEEK 4 — Launch & sales (Days 22–30)

**Day 22 (Mon)**
- Founder: convert pilots to subscriptions (annual pitch with founding price lock). Start the 3-step cold email sequence at 40/day per warmed mailbox across 3 mailboxes, plus 20 calls/day.
- Dev: polish the review queue (keyboard shortcuts, auto-approve for high-confidence clean certs as an org setting).

**Day 23 (Tue)**
- Founder: publish the template + COI Checker; post a genuinely useful write-up in construction-accounting communities ("What I learned auditing 1,500 subcontractor COIs").
- Dev: QuickBooks Online vendor import (read-only) if pilots asked for it; otherwise fix the next bugs.

**Day 24 (Wed)**
- Founder: broker outreach round 2 (20 brokers); demo calls booked from outbound.
- Dev: email deliverability hardening (SPF/DKIM/DMARC, bounce handling, unsubscribe for non-essential mail).

**Day 25 (Thu)**
- Founder: 3–5 demos. The demo *is* the instant audit: upload their folder live on the call.
- Dev: cancellation flow (reason + downgrade/archive mode) and data export (CSV + zip of PDFs).

**Day 26 (Fri)**
- Founder: submit the QuickBooks App Store listing (if the integration exists) and directory listings (Capterra/G2 free listings).
- Dev: performance pass (bulk upload of 500 PDFs), job retries, error alerts.

**Day 27 (Sat)**
- Founder: write the case study from the best pilot. Record a 90-second product video.
- Dev: buffer day / bug fixes.

**Day 28 (Sun)**
- Founder: review the funnel: touches → conversations → audits → trials → paid. Find the leakiest step and fix just that one.

**Day 29 (Mon)**
- Founder: follow up with every open trial/demo personally; ask for decisions; offer the annual founding price with a deadline (end of month).
- Dev: ship the top requested pilot feature (only if requested by ≥2 paying customers).

**Day 30 (Tue)**
- Founder + Dev: month-end review against targets:
  - **Good:** 5–10 paying customers, $700–$1,500 MRR, ≥2 broker partners, extraction accuracy ≥97% after human edits, <2 hours/week of your manual review per 10 customers.
  - **Plan month 2:** broker channel + 2 metros of outbound + the LicenseLedger/W-9 module only if customers ask.

### Realistic expectations
- Reaching $1,000 MRR in 30 days is **possible but not typical**. Construction buyers move slower than tech buyers. If you finish with 3–5 paying pilots and a working product, that's still a healthy start.
- The single biggest risk isn't the code; it's **outbound deliverability and reaching the right person**. Calls beat email in this market.
