# Part 6 — Final Decision + 7-Day Validation Plan

## The ten questions

| # | Question | Answer | Why |
|---|---|---|---|
| 1 | Build with only $1,000? | **SubShield (COI tracking)** | Concierge-sellable with a spreadsheet + an extraction script; tiny infrastructure costs; customers are public. |
| 2 | Fastest to $1,000 MRR? | **DOT DQ files** | The FMCSA census gives you thousands of owners with phone numbers; owners decide on the spot; self-serve price points. *But it churns, and the price war is real.* |
| 3 | Fastest to $10,000 MRR? | **SubShield** | Higher revenue per customer (~$180) than DQ, a broker referral channel, low churn, and expansion modules. |
| 4 | Best long-term potential? | **Provider credentialing** | Highest willingness to pay, strongest retention, expands into payer enrollment and verification services. Slower start. |
| 5 | Lowest competition (among ideas worth building)? | **Independent auto dealer title tracking** (STR permits and A/E licensing are similar) | Category C: customers tolerate the pain, which is exactly *why* competition is thin. You pay for it in selling effort. |
| 6 | Easiest customers to find? | **DOT DQ files** | Public FMCSA data with contact details, plus daily new-authority lists. |
| 7 | Least customer education? | **SubShield**, tied with DQ files | Both are Category A with education 2/10. "COI tracking" and "DQ file" are terms customers already search. |
| 8 | Easiest for one developer to build? | **Monthly exclusion screening** (but it's a feature) | Public federal lists + matching + PDF evidence. Of the standalone businesses, the trade-license tracker is easiest. |
| 9 | Most boring but profitable? | **CommissionCheck** | Excel 10/10, boring 10/10, and it directly recovers lost revenue. Nobody brags about reconciling carrier statements. |
| 10 | Start validating tomorrow? | **SubShield** | See below. |

## The one winner: **SubShield — subcontractor COI tracking for commercial GCs**

It matches the brief better than every other idea:

1. **Customers already know they need it.** "COI tracking" is a searched category (awareness 9/10, education 2/10). You never explain *why* the problem exists.
2. **Pain carries a dollar figure the buyer has already felt.** Premium-audit chargebacks and uninsured claims are real invoices, not productivity math.
3. **You can list 100 prospects tonight**, from Google Maps, state contractor license lookups, AGC/ABC/CFMA directories and LinkedIn.
4. **It's recurring by nature.** Some certificate expires every week, every year, forever.
5. **It's solo-buildable in 3–4 weeks** with low domain knowledge, standardized documents (ACORD 25) and low data sensitivity.
6. **It sells before the code exists** through the free audit → paid pilot funnel.

**Why it beats the runners-up:**
- **Credentialing (78.1):** better long-term economics, but SSN/DEA data makes security a day-one cost, practice managers are harder to reach, and the business drifts toward services. Fallback #1.
- **PayrollProof (77.7):** wonderfully boring and weekly, but LCPtracker dominates and wrong wage rates create liability. Needs more domain learning. Fallback #2.
- **DQ files (77.0):** easiest audience, but cheap competitors at $5–$49 and carrier churn would cap you.
- **CommissionCheck (75.6):** a great "money found" story, but accuracy across hundreds of statement formats is a harder build, and Applied plus a newer AI competitor are moving in.

**What would make me abandon it:** the live search this round showed the low end of COI tracking is getting cheap (BCS offers free ≤25 vendors and roughly $0.95/vendor/month self-serve). If interviews show GCs are happy with a cheap storage tool, or say "our broker does this for free," the market is a price war and you switch. **Do not fall in love with it. The 7-day test decides.**

> Note: this is the same winner as my previous analysis. I re-scored it from scratch with your new weights, and new pricing evidence lowered its competition score. It still won narrowly (79.4 vs 78.1). Treat that as a reason to validate quickly and fairly, not as confirmation.

---

## 7-Day Validation Plan (no full application build)

**Goal:** collect money or binding commitments from GCs for COI tracking within 7 days, or prove they won't pay.

### Day 1 — Identify customers
- Pick one metro (e.g., Dallas–Fort Worth). Build a sheet of **200 commercial GCs**: Google Maps ("commercial general contractor", "construction company"), state contractor/registration lookups, AGC/ABC chapter member directories.
- For each: company, website, main phone, and the person who handles COIs (LinkedIn: office manager, project accountant, controller, risk manager). Guess emails with a standard pattern + verify.
- List **15 commercial insurance brokers** with construction practices (Google "construction insurance broker <city>").
- Prep: a 1-page interview guide, the free-audit offer, a 1-page pilot agreement, and a Stripe Payment Link ($299 pilot) and deposit link ($99).
- **Evening check:** ≥200 GCs, ≥100 with a named contact.

### Day 2 — Contact customers
- **60 calls** (8–11am is best for construction offices): "Who handles subcontractor insurance certificates?" → ask for 15 minutes.
- **80 personalized emails** + 20 LinkedIn connection notes.
- **15 broker emails/calls:** "I'll run a free COI audit for one of your contractor clients."
- **Evening check:** ≥8 conversations booked for Days 3–5.

### Day 3 — Interviews
- Hold 5–8 interviews (past behavior only): How many subs? Who tracks? Last lapse? What did it cost? Premium-audit chargebacks? Hours per week? Tools tried and why not bought? Who approves spend?
- Close every interview with: **"Send me your current list + certificates and I'll return a full audit in 48 hours."**
- Keep calling 40/day for more interviews.
- **Evening check:** log incidents with $ amounts; count audits requested.

### Day 4 — Landing page + mockup
- One-page site: headline, 3-step how-it-works, sample audit report (anonymized), pricing table, "Book a free COI audit" button. Keep it to a few hours. It exists for credibility, not traffic.
- Clickable mockup of the dashboard and review queue (Figma or static HTML).
- **Run the first audits by hand:** extraction script or manual reading → spreadsheet → PDF report: "X of Y subs non-compliant, est. exposure $Z."
- **Evening check:** ≥3 audits in progress with real customer data received.

### Day 5 — Pricing test
- On audit results calls, show the three tiers ($79 / $179 / $349 + done-for-you $200) and ask: **"Which of these would you pick, and who besides you needs to approve it?"**
- Note reactions; test the done-for-you add-on with anyone who says "I don't have time to manage another tool."
- Ask brokers: "Would you introduce this to 5 clients if it keeps their audits clean?" → request a short email LOI.
- **Evening check:** price objections tallied by tier; ≥1 broker positive.

### Day 6 — Paid pilot outreach
- Ask every qualified prospect (interviewed or audited) for **one of:**
  1. **Paid pilot:** $299 for 60 days of done-with-you tracking, credited to an annual plan (card or invoice due in 7 days), or
  2. **$99 refundable deposit** locking founding pricing (Pro at $99/mo for 24 months), or
  3. **Scheduled implementation:** a calendar date to load their vendor list, plus a signed pilot agreement.
- Brokers: a signed LOI to introduce ≥5 clients within 60 days of launch.
- **Evening check:** count only money, signatures and calendar commitments.

### Day 7 — Decision

| Evidence (7 days, one metro) | PASS → build MVP | EXTEND 7 days (narrow the segment) | FAIL → switch |
|---|---|---|---|
| Real conversations (interviews/audit calls) | ≥10 | 6–9 | ≤5 |
| Prospects who handed over real COI data | ≥4 | 2–3 | 0–1 |
| **Paid pilots or deposits** | **≥2** (≥$400 collected) | 1 | 0 |
| Scheduled implementations / signed pilot agreements (unpaid) | ≥2 more | 1–2 | 0 |
| Broker LOIs | ≥1 | 0 (not fatal) | — |
| Interviewees with a costed lapse incident in the past 24 months | ≥40% | 25–39% | <25% |
| Dominant objection | Fixable (integration, timing) | Price at $179 | "Broker does it free" / "cheap tool is enough" |

**FAIL path:** run the identical 7-day test on **provider credentialing** (offer: free credentialing health check → $299 setup pilot). If that fails, test **PayrollProof** (offer: we build your next 4 certified payrolls for $199).

**What does NOT count:** likes, compliments, "sounds great, send me info", survey answers, free signups, landing-page visits, LinkedIn connection acceptances.

**Realism note:** construction offices move slowly, so 2 paid pilots in 7 days is a demanding bar. A signed pilot agreement with an invoice due date counts as payment intent; a "maybe next month" does not.
