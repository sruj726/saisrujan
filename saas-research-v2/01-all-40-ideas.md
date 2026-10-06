# Part 2 — All 40 Opportunities, Analyzed

Ideas are numbered by ID (the ranking is in `02-ranking.md`). Scores come from `_build/` data, so the arithmetic is reproducible.
Competitor pricing marked *(via search Oct 2026)* was checked with a live web search; everything else is approximate from prior knowledge, so verify it before relying on it.

---

## 1. SubShield — subcontractor COI tracking
*Construction* · **Score 79.4/100** · **Verdict: BUILD** · Boring-business test: 1,2,3,4,5,6,9,10,12 (9/12)

1. **Product concept:** Collect, read (AI), check and auto-chase subcontractor certificates of insurance against the GC's requirements; alert before expiry; audit-ready export.
2. **Target customer:** Commercial GCs & large specialty contractors, $5–50M revenue, 30–250 subs/yr
3. **Buyer:** Office manager / project accountant / controller
4. **Problem:** Every sub needs valid GL/auto/WC/umbrella coverage + endorsements; policies expire on staggered dates all year.
5. **Current manual process:** Excel sheet + Outlook folder + calendar reminders; staff read ACORD 25 PDFs by hand and email agents.
6. **Why it sucks:** Reading PDFs, chasing agents, and discovering lapses only at the insurer's premium audit.
7. **Frequency:** Weekly (some cert expires every week)
8. **Consequence of ignoring it:** Premium-audit chargebacks for uninsured subs ($5k–$50k+), uninsured claims hitting the GC's policy.
9. **Existing software category:** COI / vendor insurance compliance tracking
10. **Major competitors:** BCS, myCOI, TrustLayer, Jones, Billy, PINS Advantage, SmartCompliance, Constrafor, Procore fields
11. **Typical competitor pricing:** BCS: free ≤25 vendors, ~$0.95/vendor/mo self-serve (verified via search Oct 2026); entry tools ~$800–2,000/yr; enterprise $10k+/yr minimums
12. **Market gaps:** Low end is now cheap but mostly 'storage + reminders'; true automation (inbox ingestion, AI reading, agent chasing, premium-audit report) sits in sales-led tiers.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3–4 weeks
20. **Willingness to pay:** 7/10 · 21. **Price:** $99–$399/mo · 22. **Retention:** 9/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 8/10 · 25. **First 10 reachable:** 8/10 · 26. **First 100 reachable:** 7/10 · 27. **Expansion:** 8/10
28. **Primary acquisition channel:** Outbound (calls + email) to GCs + construction insurance broker referrals
29. **Best starting niche:** Commercial GCs $5–50M in one Sun Belt metro
30. **Biggest reason NOT to build it:** Crowded and price-compressed at the low end (BCS free tier); you must win on automation and distribution, not on features.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 9/10 | Critical | 8/10 | 8/10 | 9/10 |

- **Customer value:** Prevents fines/chargebacks, reduces liability, helps pass audits, saves admin time
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps 'commercial general contractor <city>', state contractor license lookups (e.g., TX/FL/NC/AZ boards), AGC/ABC chapter member directories, LinkedIn titles 'project accountant'.
- **Payment test:** Short demo required (self-serve possible at $99)
- **Recurring test:** Month 1: Initial cleanup: dozens of expired/deficient certs found and chased. · Month 6: Renewals keep arriving weekly; the archive becomes audit evidence. · Year 2: Premium audits look back a year+; history + agent relationships make leaving painful.

---

## 2. Lien waiver collection for GCs
*Construction* · **Score 72.1/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,2,3,4,5,9,10 (7/12)

1. **Product concept:** Each pay cycle, request conditional/unconditional lien waivers from subs & suppliers, e-sign, match to payments, block payment until received.
2. **Target customer:** Commercial/residential GCs with 20+ subs per month
3. **Buyer:** Project accountant / AP
4. **Problem:** Monthly pay apps require matching waivers from every sub and often lower tiers.
5. **Current manual process:** Email PDFs, DocuSign one-offs, spreadsheet checklist per job.
6. **Why it sucks:** Chasing signatures, wrong forms per state, payments delayed or released without waivers.
7. **Frequency:** Monthly per job
8. **Consequence of ignoring it:** Double-payment/lien exposure, owner/lender withholding draws.
9. **Existing software category:** Lien waiver management
10. **Major competitors:** Procore Pay/Levelset, Built, Rabbet, Beam, Waivr, LienDone, GCPay, Textura
11. **Typical competitor pricing:** Waivr and LienDone ~$49/mo (verified via search Oct 2026); enterprise via quote
12. **Market gaps:** Low end already served cheaply; high end bundled with payments.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3–4 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$199/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 2/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Same GC outbound as #1
29. **Best starting niche:** GCs on QuickBooks without Procore
30. **Biggest reason NOT to build it:** $49 competitors + payment platforms bundling it free; best as a module of #1.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 8/10 | Important | 7/10 | 7/10 | 10/10 |

- **Customer value:** Reduces liability, prevents lost money
- **First-customer test (100 prospects tonight?):** **YES**. Same sources as #1.
- **Payment test:** Self-service
- **Recurring test:** Month 1: Set up pay-cycle templates. · Month 6: Monthly pay cycles continue. · Year 2: Stays while projects run; but cheap substitutes exist.

---

## 3. PayrollProof — certified payroll (WH-347) for public-works subcontractors
*Construction / Government contracts* · **Score 77.7/100** · **Verdict: VALIDATE** · Boring-business test: 1,2,3,4,7,8,9,10,12 (9/12)

1. **Product concept:** Import weekly payroll from QuickBooks/Gusto/ADP exports, map workers to projects & prevailing-wage classifications, check rates, generate WH-347 + Statement of Compliance + state forms/upload files.
2. **Target customer:** Subcontractors (electrical, concrete, paving, HVAC) with 10–150 workers doing prevailing-wage public works
3. **Buyer:** Owner / payroll admin / office manager
4. **Problem:** Every week on every public job, a certified payroll must be submitted with correct classifications, rates and fringes.
5. **Current manual process:** Retyping payroll into WH-347 PDFs or Excel templates, then re-entering into agency portals (e.g., LCPtracker, state systems).
6. **Why it sucks:** Hours of double entry weekly; rate errors trigger rejections, withheld payments, restitution.
7. **Frequency:** Weekly
8. **Consequence of ignoring it:** Withheld progress payments, back-wage restitution, penalties, debarment risk.
9. **Existing software category:** Certified payroll software
10. **Major competitors:** LCPtracker (LCPcertified / LCPtracker Pro — imports QuickBooks & other payroll exports), Certified Payroll WH-347 (standalone), eBacon, Points North, Foundation/Sage/Viewpoint payroll modules
11. **Typical competitor pricing:** Standalone WH-347 tool from ~$79/mo; LCPtracker Pro/eBacon ~$200–600/mo quote-based (via search Oct 2026)
12. **Market gaps:** LCPtracker already covers 'upload payroll export → federal/state CPRs', and many agencies pay for LCPtracker themselves. Remaining gaps: Gusto users (Gusto has no native certified payroll), small subs on many different agency portals, and pre-submission rate/fringe error checking.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 4–6 weeks
20. **Willingness to pay:** 7/10 · 21. **Price:** $99–$349/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 7/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Outbound to contractors on public bid lists + construction bookkeepers/CPAs
29. **Best starting niche:** One state with its own prevailing-wage system (e.g., CA DIR registered contractors or a Midwest state) + federal Davis-Bacon
30. **Biggest reason NOT to build it:** LCPtracker dominates both the agency and contractor sides; rules complexity (fringes, apprentices, state forms, WH-347 revisions) creates liability — a wrong rate on your watch is a customer's restitution bill.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 9/10 | Critical | 6/10 | 9/10 | 10/10 |

- **Customer value:** Saves admin time, prevents fines/withheld payments, helps pass audits
- **First-customer test (100 prospects tonight?):** **YES**. California DIR public-works contractor registration search (public), state DOT bid tabulations & awarded-contract lists, USAspending.gov subaward data, AGC chapter lists.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: First weekly payrolls generated; immediate hours saved. · Month 6: Still weekly for every active public job. · Year 2: Public-works contractors bid public work year after year; history needed for audits.

---

## 4. Trade workforce license & certification tracker
*Construction / Home services* · **Score 70.4/100** · **Verdict: FEATURE, NOT COMPANY** · Boring-business test: 1,2,3,4,5,6,10 (7/12)

1. **Product concept:** Techs text in license/OSHA/EPA card photos; renewals & CE tracked; QR credential card; prequal packets.
2. **Target customer:** Electrical/plumbing/HVAC contractors with 15–150 field staff
3. **Buyer:** HR/office manager
4. **Problem:** Licenses & certs renew on staggered cycles with CE requirements.
5. **Current manual process:** Spreadsheet + photocopies.
6. **Why it sucks:** Lost cards, missed CE, scrambling for prequal packets.
7. **Frequency:** Monthly renewals; weekly requests for proof
8. **Consequence of ignoring it:** Techs pulled from jobs, permit problems, fines.
9. **Existing software category:** Certification/expiration tracking
10. **Major competitors:** Expiration Reminder, SafetyCulture, Procore certifications, Connecteam, BambooHR/Rippling fields
11. **Typical competitor pricing:** ~$2–8/employee/mo or bundled (approx., unverified)
12. **Market gaps:** Generic; not trade-rule aware.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 8/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 3/10 · 19. **MVP estimate:** 2–3 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $59–$249/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 6/10
28. **Primary acquisition channel:** Trade associations + #1 cross-sell
29. **Best starting niche:** Electrical contractors in one licensing-heavy state
30. **Biggest reason NOT to build it:** Moderate pain; HR tools absorb it; better as a module of #1.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 9/10 | Important | 8/10 | 6/10 | 8/10 |

- **Customer value:** Prevents fines, saves time
- **First-customer test (100 prospects tonight?):** **YES**. State electrical contractor license lists, Google Maps, IEC/PHCC chapters.
- **Payment test:** Self-service
- **Recurring test:** Month 1: Card collection. · Month 6: Renewals + turnover. · Year 2: CE history; only if bundled.

---

## 5. Subcontractor prequalification
*Construction* · **Score 63.3/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,4,5,10 (4/12)

1. **Product concept:** Collect sub financials, EMR, safety programs, references; score and approve subs.
2. **Target customer:** GCs $20M+
3. **Buyer:** Risk manager / preconstruction
4. **Problem:** Annual prequal of every sub.
5. **Current manual process:** Emailed questionnaires + Excel scoring.
6. **Why it sucks:** Chasing forms, inconsistent scoring.
7. **Frequency:** Annual per sub (rolling)
8. **Consequence of ignoring it:** Sub default risk.
9. **Existing software category:** Prequalification platforms
10. **Major competitors:** Autodesk TradeTapp, Highwire, ISNetworld, Avetta, Billy, Constrafor
11. **Typical competitor pricing:** Mostly quote-based enterprise (unverified)
12. **Market gaps:** Small GCs priced out, but they also prequal less.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 6/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 4/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 4 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $149–$399/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 6/10
28. **Primary acquisition channel:** GC outbound
29. **Best starting niche:** Mid-size GCs without TradeTapp
30. **Biggest reason NOT to build it:** Annual cadence + buyer is larger GCs who already use enterprise tools.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 8/10 | 8/10 | Important | 7/10 | 6/10 | 6/10 |

- **Customer value:** Reduces liability
- **First-customer test (100 prospects tonight?):** **YES**. Same as #1.
- **Payment test:** Sales call required
- **Recurring test:** Month 1: Questionnaires sent. · Month 6: Quiet months. · Year 2: Annual refresh only.

---

## 6. OSHA 300 log & 300A electronic submission
*Construction / Manufacturing / Warehouses* · **Score 61.2/100** · **Verdict: AVOID** · Boring-business test: 1,3,4,10 (4/12)

1. **Product concept:** Record injuries, auto-build OSHA 300/301/300A, remind and prepare annual ITA submission.
2. **Target customer:** Employers with 20–250 staff in high-hazard industries
3. **Buyer:** Safety/HR manager
4. **Problem:** Injury recordkeeping + annual posting & electronic submission.
5. **Current manual process:** Paper OSHA forms, Excel.
6. **Why it sucks:** Annual scramble; recordability confusion.
7. **Frequency:** Per incident + annual
8. **Consequence of ignoring it:** OSHA citations.
9. **Existing software category:** EHS incident management
10. **Major competitors:** OSHA's free ITA site, VelocityEHS, Intelex, SafetyCulture, many EHS suites
11. **Typical competitor pricing:** Free government tooling to enterprise EHS (approx.)
12. **Market gaps:** Little; free forms suffice for small employers.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 8/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 2/10 · 19. **MVP estimate:** 1–2 weeks
20. **Willingness to pay:** 4/10 · 21. **Price:** $29–$79/mo · 22. **Retention:** 4/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 4/10
28. **Primary acquisition channel:** SEO
29. **Best starting niche:** Small manufacturers
30. **Biggest reason NOT to build it:** Annual task + free government tools = subscribe-and-cancel.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Important | 8/10 | 5/10 | 4/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps, state manufacturer directories.
- **Payment test:** Self-service
- **Recurring test:** Month 1: Log entered. · Month 6: Nothing to do. · Year 2: Cancels between filing seasons.

---

## 7. DOT driver qualification (DQ) files
*Trucking* · **Score 77.0/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,2,3,4,5,6,9,10,12 (9/12)

1. **Product concept:** Digital DQ files per 49 CFR 391; drivers text in med cards/CDLs; expiry alerts; audit export.
2. **Target customer:** Carriers with 3–50 trucks, especially new entrants
3. **Buyer:** Owner / safety manager
4. **Problem:** Required DQ documents expire constantly; new-entrant safety audit within 12 months.
5. **Current manual process:** Paper binders, phone photos, spreadsheet.
6. **Why it sucks:** Paper chaos, missed med cards.
7. **Frequency:** Monthly expirations; continuous hiring
8. **Consequence of ignoring it:** Audit violations, conditional rating, insurance impact.
9. **Existing software category:** DQ file management
10. **Major competitors:** Roadworthy HQ, Core Compliance, DOTDriverFiles, J.J. Keller, Foley, Tenstreet, Motive/Samsara
11. **Typical competitor pricing:** Core Compliance $15–$349/mo; Roadworthy HQ $39–$149/mo; DOTDriverFiles from ~$5/user (via search Oct 2026)
12. **Market gaps:** Cheap self-serve tools already exist; gap is mainly bilingual SMS-first UX and done-for-you setup.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 10/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $49–$199/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 2/10 (10 = little competition)
24. **Market size:** 8/10 · 25. **First 10 reachable:** 9/10 · 26. **First 100 reachable:** 8/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** FMCSA census list → calls/email; insurance agents; factoring cos
29. **Best starting niche:** New-entrant carriers (0–18 months) with 2–15 trucks
30. **Biggest reason NOT to build it:** Price war already underway ($15–$49 tools) + tiny carriers churn hard.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Critical | 7/10 | 8/10 | 9/10 |

- **Customer value:** Prevents fines, helps pass audits
- **First-customer test (100 prospects tonight?):** **YES**. FMCSA Company Census file / SAFER (public; includes many carrier emails & phones), FMCSA Register of new authority applicants.
- **Payment test:** Self-service
- **Recurring test:** Month 1: File cleanup. · Month 6: Med cards & reviews renew. · Year 2: Retention rule (employment + 3 yrs) — if the carrier survives.

---

## 8. IFTA quarterly fuel tax reporting
*Trucking* · **Score 74.1/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,2,3,4,7,8 (6/12)

1. **Product concept:** Import miles by state + fuel receipts, compute IFTA return quarterly.
2. **Target customer:** Small interstate carriers without ELD IFTA reports
3. **Buyer:** Owner
4. **Problem:** Quarterly mileage/fuel tax returns.
5. **Current manual process:** Trip sheets + receipts in shoeboxes + spreadsheets.
6. **Why it sucks:** Tedious; audit risk.
7. **Frequency:** Quarterly
8. **Consequence of ignoring it:** Penalties, audits, license suspension.
9. **Existing software category:** IFTA software
10. **Major competitors:** Motive/Samsara/other ELD built-ins, ExpressIFTA, TruckingOffice, IFTA filing services
11. **Typical competitor pricing:** Often included free with ELD; standalone ~$10–$50/quarter (approx.)
12. **Market gaps:** Essentially none.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 10/10 · 15. **Customer attraction:** 10/10 · 16. **Education required:** 1/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $15–$49/mo · 22. **Retention:** 6/10 · 23. **Competition opportunity:** 1/10 (10 = little competition)
24. **Market size:** 8/10 · 25. **First 10 reachable:** 8/10 · 26. **First 100 reachable:** 7/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** FMCSA lists
29. **Best starting niche:** Non-ELD exempt carriers
30. **Biggest reason NOT to build it:** ELDs give it away; quarterly use invites churn.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 6/10 | Critical | 7/10 | 7/10 | 9/10 |

- **Customer value:** Saves time, prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. FMCSA census.
- **Payment test:** Self-service
- **Recurring test:** Month 1: One return. · Month 6: Two returns. · Year 2: Switches to ELD bundle.

---

## 9. Fleet maintenance & annual DOT inspection tracker
*Trucking / Field services* · **Score 70.4/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,2,3,4,9,10 (6/12)

1. **Product concept:** PM schedules, annual inspection records, DVIR defects.
2. **Target customer:** Fleets 5–100 vehicles
3. **Buyer:** Fleet manager
4. **Problem:** Recurring PM + annual inspection proof.
5. **Current manual process:** Spreadsheets + paper.
6. **Why it sucks:** Missed services.
7. **Frequency:** Weekly/monthly
8. **Consequence of ignoring it:** Breakdowns, roadside violations.
9. **Existing software category:** Fleet maintenance software
10. **Major competitors:** Fleetio, Whip Around, Samsara, Motive, AUTOsist, Fleet Maintenance Pro
11. **Typical competitor pricing:** ~$4–$10/vehicle/mo (approx.)
12. **Market gaps:** Very few.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 9/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 4 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$199/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 1/10 (10 = little competition)
24. **Market size:** 8/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 6/10
28. **Primary acquisition channel:** FMCSA lists
29. **Best starting niche:** Small fleets
30. **Biggest reason NOT to build it:** Mature, well-funded competitors with integrations.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 7/10 | 7/10 | Important | 7/10 | 6/10 | 9/10 |

- **Customer value:** Prevents downtime/fines
- **First-customer test (100 prospects tonight?):** **YES**. FMCSA census.
- **Payment test:** Self-service
- **Recurring test:** Month 1: Asset setup. · Month 6: Ongoing PMs. · Year 2: Sticky — but for incumbents.

---

## 10. Freight broker carrier vetting & monitoring
*Logistics* · **Score 74.4/100** · **Verdict: TOO HARD** · Boring-business test: 1,2,3,5,9,10,12 (7/12)

1. **Product concept:** Monitor carrier authority, insurance, safety and fraud signals before tendering loads.
2. **Target customer:** Freight brokerages
3. **Buyer:** Carrier relations / compliance
4. **Problem:** Double brokering & fraud; insurance lapses.
5. **Current manual process:** SAFER lookups, calls.
6. **Why it sucks:** Fraud losses.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** Stolen loads, liability.
9. **Existing software category:** Carrier onboarding/monitoring
10. **Major competitors:** Highway, Carrier Assure, RMIS (Truckstop), MyCarrierPackets, Carrier411, DAT
11. **Typical competitor pricing:** Hundreds to thousands per month (approx.)
12. **Market gaps:** Fraud-signal data is the moat; incumbents have it.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 10/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 1/10 (lower is better)
17. **Domain knowledge:** High · 18. **Build difficulty:** 7/10 · 19. **MVP estimate:** 2–3 months
20. **Willingness to pay:** 8/10 · 21. **Price:** $200–$1,000/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 1/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Broker outbound
29. **Best starting niche:** Small brokerages
30. **Biggest reason NOT to build it:** Data-network moat + fierce incumbents; fraud detection needs proprietary data.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 6/10 | 3/10 | Critical | 4/10 | 8/10 | 10/10 |

- **Customer value:** Prevents losses, reduces liability
- **First-customer test (100 prospects tonight?):** **YES**. FMCSA broker authority list.
- **Payment test:** Sales call required
- **Recurring test:** Month 1: Onboarding. · Month 6: Daily use. · Year 2: Sticky for winners.

---

## 11. Provider credentialing & CAQH re-attestation tracker
*Healthcare administration* · **Score 78.1/100** · **Verdict: VALIDATE** · Boring-business test: 1,2,3,4,5,6,9,10,12 (9/12)

1. **Product concept:** Track licenses, DEA, board certs, malpractice, CAQH 120-day attestation, payer revalidation; provider self-service; monthly exclusion checks.
2. **Target customer:** Group practices (behavioral health, PT, primary care) with 5–40 clinicians; freelance credentialers
3. **Buyer:** Practice manager / credentialing specialist
4. **Problem:** Dozens of overlapping renewal cycles; lapses stop billing.
5. **Current manual process:** Spreadsheets, portal logins, calendar.
6. **Why it sucks:** Denials discovered weeks later; knowledge lost with staff turnover.
7. **Frequency:** Weekly (across providers)
8. **Consequence of ignoring it:** Denied/delayed claims ($10k+ per lapse), compliance findings.
9. **Existing software category:** Credentialing software / CVO
10. **Major competitors:** Medallion, Verifiable, CredentialStream, symplr, Modio, Andros, outsourced credentialing firms
11. **Typical competitor pricing:** Outsourced ~$100–$300/provider/mo; software mostly quote-based (approx., unverified)
12. **Market gaps:** Venture players moving upmarket; small groups underserved by self-serve software.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 4–5 weeks
20. **Willingness to pay:** 8/10 · 21. **Price:** $99–$499/mo · 22. **Retention:** 9/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 8/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 8/10
28. **Primary acquisition channel:** Practice-owner communities, billing companies, freelance credentialers
29. **Best starting niche:** Behavioral-health group practices 5–30 clinicians
30. **Biggest reason NOT to build it:** Sensitive PII (SSN/DOB/DEA) raises security bar; buyers overloaded; money pulls toward services.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Critical | 6/10 | 9/10 | 9/10 |

- **Customer value:** Prevents lost revenue, helps pass audits, saves time
- **First-customer test (100 prospects tonight?):** **YES**. CMS NPPES NPI registry (public, filter by taxonomy + organization), state licensing boards, Psychology Today group listings.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Data loaded; gaps found. · Month 6: CAQH cycles + renewals. · Year 2: Source of truth for every provider; switching is painful.

---

## 12. Monthly OIG/SAM/state Medicaid exclusion screening
*Healthcare administration* · **Score 76.1/100** · **Verdict: FEATURE, NOT COMPANY** · Boring-business test: 1,2,3,9,10,12 (6/12)

1. **Product concept:** Screen every employee/contractor monthly against federal and state exclusion lists; store evidence.
2. **Target customer:** Home health, pharmacies, DME, clinics, behavioral health employers 10–500 staff
3. **Buyer:** Compliance/HR
4. **Problem:** Monthly screening expected by Medicaid programs; hiring excluded persons risks repayment.
5. **Current manual process:** Manual searches on OIG/SAM sites, screenshots to folders.
6. **Why it sucks:** Tedious, easily skipped.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Civil monetary penalties, overpayment recovery.
9. **Existing software category:** Exclusion screening
10. **Major competitors:** ProviderTrust, Verisys, Streamline Verify, Exclusion Screening LLC, background-check vendors
11. **Typical competitor pricing:** ~$1–$5/person/mo or flat (approx., unverified)
12. **Market gaps:** Commodity; cheap options exist.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 3/10 · 19. **MVP estimate:** 2–3 weeks (federal), +weeks per state list
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$199/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** SEO + healthcare compliance consultants
29. **Best starting niche:** Home health agencies in one state
30. **Biggest reason NOT to build it:** Commodity data product; state-list maintenance is grindy; better as a feature of #11/#13.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 6/10 | Critical | 8/10 | 7/10 | 10/10 |

- **Customer value:** Prevents fines, helps pass audits
- **First-customer test (100 prospects tonight?):** **YES**. CMS Care Compare provider data, state licensing lists.
- **Payment test:** Self-service
- **Recurring test:** Month 1: First screen. · Month 6: Monthly screens + evidence. · Year 2: Audit trail retained.

---

## 13. Home care caregiver compliance files
*Healthcare administration* · **Score 74.5/100** · **Verdict: FEATURE, NOT COMPANY** · Boring-business test: 1,2,3,4,5,6,10 (7/12)

1. **Product concept:** Track caregiver TB tests, CPR, background checks, training hours, I-9, competencies against state rules.
2. **Target customer:** Private-duty/home care agencies 20–300 caregivers
3. **Buyer:** Agency owner / HR coordinator
4. **Problem:** State surveys check staff files; caregiver turnover is extreme.
5. **Current manual process:** Spreadsheets + paper files.
6. **Why it sucks:** Constant churn = constant gaps.
7. **Frequency:** Weekly
8. **Consequence of ignoring it:** Survey citations, payer audits.
9. **Existing software category:** Home care agency software (compliance module)
10. **Major competitors:** HHAeXchange, CareTime, ShiftCare, AxisCare, WellSky, AlayaCare, eCaring
11. **Typical competitor pricing:** Bundled into agency platforms (via search Oct 2026)
12. **Market gaps:** Mostly covered inside the systems agencies already use.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 9/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $99–$299/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 7/10 · 27. **Expansion:** 6/10
28. **Primary acquisition channel:** State home care associations
29. **Best starting niche:** Agencies on weak scheduling software
30. **Biggest reason NOT to build it:** Agency platforms already include expiring-document tracking; you'd be a redundant add-on.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Important | 7/10 | 8/10 | 9/10 |

- **Customer value:** Helps pass audits
- **First-customer test (100 prospects tonight?):** **YES**. State home care license lists, Google Maps.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Files cleaned. · Month 6: Turnover keeps it busy. · Year 2: Unless platform replaces it.

---

## 14. Dental insurance eligibility & benefits verification
*Healthcare administration* · **Score 74.0/100** · **Verdict: TOO HARD** · Boring-business test: 1,2,4,8,12 (5/12)

1. **Product concept:** Verify patients' coverage before appointments; write breakdowns into the PMS.
2. **Target customer:** Dental practices 1–10 locations
3. **Buyer:** Office manager
4. **Problem:** Front desk spends hours on portals/phones.
5. **Current manual process:** Portals, phone calls, offshore teams.
6. **Why it sucks:** Slow, error-prone.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** Surprise balances, write-offs.
9. **Existing software category:** Dental RCM/eligibility
10. **Major competitors:** Vyne Trellis, Zuub, Onederful, DentalXChange, AI voice-agent startups, offshore VAs
11. **Typical competitor pricing:** ~$300–$1,000+/location/mo (approx.)
12. **Market gaps:** Data completeness; still needs humans.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** High · 18. **Build difficulty:** 9/10 · 19. **MVP estimate:** 3+ months
20. **Willingness to pay:** 8/10 · 21. **Price:** $299–$799/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 8/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 8/10
28. **Primary acquisition channel:** Dental consultants
29. **Best starting niche:** Open Dental practices
30. **Biggest reason NOT to build it:** PMS integrations + PHI + payer variance = not a solo 2–6 week build.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 7/10 | 6/10 | Important | 3/10 | 9/10 | 10/10 |

- **Customer value:** Saves staff cost, prevents lost revenue
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps, state dental boards.
- **Payment test:** Sales call required
- **Recurring test:** Month 1: Daily use. · Month 6: Daily use. · Year 2: Sticky if accurate.

---

## 15. City rental license & registration compliance
*Property management* · **Score 59.3/100** · **Verdict: AVOID** · Boring-business test: 1,2,3,4,6 (5/12)

1. **Product concept:** Track per-property rental licenses, registrations, inspections, lead/smoke certificates by city.
2. **Target customer:** Landlords/PMs with 20–500 doors across several cities
3. **Buyer:** Owner / PM
4. **Problem:** City rental programs renew annually with inspections.
5. **Current manual process:** Calendar + folders.
6. **Why it sucks:** Every city differs.
7. **Frequency:** Annual per property (monthly across portfolio)
8. **Consequence of ignoring it:** Fines, inability to evict/collect in some cities.
9. **Existing software category:** None clear
10. **Major competitors:** PM software notes, consultants
11. **Typical competitor pricing:** n/a
12. **Market gaps:** Open, but data curation heavy.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 5/10 · 15. **Customer attraction:** 6/10 · 16. **Education required:** 5/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 4 weeks + data
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$199/mo · 22. **Retention:** 6/10 · 23. **Competition opportunity:** 7/10 (10 = little competition)
24. **Market size:** 5/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** Local landlord associations
29. **Best starting niche:** One metro with strict programs
30. **Biggest reason NOT to build it:** Customers tolerate it; per-city rule curation is endless.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Important | 5/10 | 6/10 | 7/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **MAYBE**. City rental registries (some public), landlord associations.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Setup. · Month 6: Few events. · Year 2: Low engagement.

---

## 16. Renter's insurance verification for PMs
*Property management* · **Score 63.6/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,3,5,6,9 (5/12)

1. **Product concept:** Verify tenants keep required renter's insurance.
2. **Target customer:** PMs 200+ units
3. **Buyer:** PM ops
4. **Problem:** Leases require coverage; tenants lapse.
5. **Current manual process:** Email/PDF checks.
6. **Why it sucks:** Endless follow-up.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Uninsured damage.
9. **Existing software category:** Insurance compliance for PMs
10. **Major competitors:** Second Nature, Sure, Assurant, AppFolio/Buildium programs, master-policy providers
11. **Typical competitor pricing:** Often free to PMs (they earn revenue from master policies)
12. **Market gaps:** None — incumbents pay PMs.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $99–$299/mo · 22. **Retention:** 6/10 · 23. **Competition opportunity:** 1/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Competitors give it away and pay PMs a revenue share.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 8/10 | 6/10 | Important | 6/10 | 6/10 | 9/10 |

- **Customer value:** Reduces liability
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps, NARPM.
- **Payment test:** Sales call required
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 17. Affordable housing tenant income recertifications
*Property management* · **Score 71.0/100** · **Verdict: TOO HARD** · Boring-business test: 1,2,3,4,5,10,12 (7/12)

1. **Product concept:** Annual LIHTC/HUD recertification workflows.
2. **Target customer:** Affordable housing PMs
3. **Buyer:** Compliance director
4. **Problem:** Annual recerts with strict rules.
5. **Current manual process:** Paper files + specialized software.
6. **Why it sucks:** Complex, audited.
7. **Frequency:** Monthly across portfolio
8. **Consequence of ignoring it:** Loss of tax credits, findings.
9. **Existing software category:** Affordable housing compliance
10. **Major competitors:** Yardi, RealPage, Entrata, Boston Post, specialized consultants
11. **Typical competitor pricing:** Enterprise
12. **Market gaps:** Rules expertise is the barrier.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 6/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** High · 18. **Build difficulty:** 9/10 · 19. **MVP estimate:** 3+ months
20. **Willingness to pay:** 8/10 · 21. **Price:** $300+/mo · 22. **Retention:** 9/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 4/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Industry events
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Requires deep regulatory expertise; errors are catastrophic.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 6/10 | Critical | 2/10 | 9/10 | 10/10 |

- **Customer value:** Prevents loss of credits
- **First-customer test (100 prospects tonight?):** **MAYBE**. State housing finance agency property lists.
- **Payment test:** Enterprise sales required
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 18. Bookkeeper client 'missing items' chaser
*Accounting* · **Score 69.7/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,4,5,11 (4/12)

1. **Product concept:** Text/email clients about uncategorized transactions & missing receipts; answers write back.
2. **Target customer:** Bookkeeping firms 15–150 clients
3. **Buyer:** Firm owner
4. **Problem:** Month-end blocked by unresponsive clients.
5. **Current manual process:** Emailed spreadsheets.
6. **Why it sucks:** Clients ignore emails.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Late closes, unhappy clients.
9. **Existing software category:** Client request tools
10. **Major competitors:** Keeper, Financial Cents, Karbon, Content Snare, TaxDome, QuickBooks Ask Client
11. **Typical competitor pricing:** ~$20–$80/user/mo (approx.)
12. **Market gaps:** Keeper covers this specifically and well.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$199/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 1/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** Bookkeeper communities
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Well-funded incumbent solves exactly this.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 8/10 | 8/10 | Important | 7/10 | 7/10 | 10/10 |

- **Customer value:** Saves time
- **First-customer test (100 prospects tonight?):** **YES**. QuickBooks ProAdvisor directory, Google Maps.
- **Payment test:** Self-service
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 19. STR permit & occupancy-tax deadline tracker
*Property management (short-term rentals)* · **Score 65.8/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,2,3,4,6 (5/12)

1. **Product concept:** Per-listing local permit numbers, renewals, inspections and occupancy-tax filing deadlines across jurisdictions.
2. **Target customer:** STR property managers with 10–300 listings across several cities
3. **Buyer:** Owner / ops manager
4. **Problem:** Local STR rules, permits and tax filings differ by city and change often.
5. **Current manual process:** Spreadsheets + calendars + city portals.
6. **Why it sucks:** Every jurisdiction differs; rules change; permit numbers must appear on listings.
7. **Frequency:** Monthly (filings) / annual (permits)
8. **Consequence of ignoring it:** Fines, delisting, lost bookings.
9. **Existing software category:** STR compliance (operator side)
10. **Major competitors:** Avalara MyLodgeTax (tax filing), Granicus Host Compliance (sells to cities), consultants
11. **Typical competitor pricing:** Tax filing services per listing/filing (approx., unverified)
12. **Market gaps:** Operator-side permit tracking poorly served.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 6/10 · 16. **Education required:** 4/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 4 weeks + data curation
20. **Willingness to pay:** 6/10 · 21. **Price:** $79–$299/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 6/10 (10 = little competition)
24. **Market size:** 5/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** PMS marketplaces (Hostaway/Guesty), VRMA, STR groups
29. **Best starting niche:** Managers in 1–2 heavily regulated states
30. **Biggest reason NOT to build it:** Endless jurisdiction-data maintenance; regulation can ban a market overnight.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Critical | 5/10 | 7/10 | 8/10 |

- **Customer value:** Prevents fines, prevents lost revenue
- **First-customer test (100 prospects tonight?):** **MAYBE**. Airbnb/VRBO host profiles, VRMA members, Google Maps 'vacation rental management'.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Permits mapped. · Month 6: Filings + renewals. · Year 2: Data moat — if markets survive.

---

## 20. Vendor W-9 collection & 1099 prep
*Accounting* · **Score 60.6/100** · **Verdict: FEATURE, NOT COMPANY** · Boring-business test: 1,2,3,5 (4/12)

1. **Product concept:** Collect W-9s, TIN-match, prepare 1099s.
2. **Target customer:** SMBs & bookkeepers
3. **Buyer:** AP / bookkeeper
4. **Problem:** Missing W-9s at year-end.
5. **Current manual process:** Email + PDFs.
6. **Why it sucks:** January scramble.
7. **Frequency:** Annual peak
8. **Consequence of ignoring it:** IRS penalties.
9. **Existing software category:** 1099 software
10. **Major competitors:** Track1099, Tax1099, QuickBooks, Gusto, Bill.com
11. **Typical competitor pricing:** Per-form pricing (approx.)
12. **Market gaps:** None.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 2/10 · 19. **MVP estimate:** 2 weeks
20. **Willingness to pay:** 4/10 · 21. **Price:** $19–$49/mo · 22. **Retention:** 3/10 · 23. **Competition opportunity:** 2/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 4/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Seasonal; bundled everywhere — a feature of #1.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Important | 9/10 | 5/10 | 3/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. Anywhere.
- **Payment test:** Self-service
- **Recurring test:** Month 1: — · Month 6: Idle. · Year 2: Cancelled.

---

## 21. Attorney CLE tracking for firms
*Legal operations* · **Score 61.7/100** · **Verdict: AVOID** · Boring-business test: 1,3,4,6 (4/12)

1. **Product concept:** Track each attorney's CLE credits & deadlines across states.
2. **Target customer:** Law firms 10–100 attorneys
3. **Buyer:** Office administrator
4. **Problem:** Multi-state CLE deadlines.
5. **Current manual process:** Spreadsheet + bar portals.
6. **Why it sucks:** Last-minute scrambles.
7. **Frequency:** Annual/biennial
8. **Consequence of ignoring it:** Late fees, suspension (rare).
9. **Existing software category:** CLE tracking
10. **Major competitors:** State bar portals, CLE providers' trackers, practice management add-ons
11. **Typical competitor pricing:** Often free
12. **Market gaps:** Little.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 2/10 · 19. **MVP estimate:** 2 weeks
20. **Willingness to pay:** 4/10 · 21. **Price:** $49–$149/mo · 22. **Retention:** 5/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 5/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 4/10
28. **Primary acquisition channel:** Legal admin associations
29. **Best starting niche:** Multi-state firms
30. **Biggest reason NOT to build it:** Bars and CLE vendors provide free tracking; low urgency.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 7/10 | Convenience | 8/10 | 4/10 | 6/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. State bar directories, Martindale.
- **Payment test:** Self-service
- **Recurring test:** Month 1: Setup. · Month 6: Idle. · Year 2: Low value.

---

## 22. Court deadline docketing for small law firms
*Legal operations* · **Score 75.2/100** · **Verdict: TOO HARD** · Boring-business test: 1,2,3,9,10 (5/12)

1. **Product concept:** Rules-based deadline calculation from court events.
2. **Target customer:** Litigation firms 2–30 lawyers
3. **Buyer:** Managing partner
4. **Problem:** Missed deadlines = malpractice.
5. **Current manual process:** Paralegal calendars.
6. **Why it sucks:** High-stakes manual math.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** Malpractice claims.
9. **Existing software category:** Docketing/court rules
10. **Major competitors:** CompuLaw (Aderant), LawToolBox, CalendarRules, Clio integrations
11. **Typical competitor pricing:** ~$50–$200/user/mo (approx.)
12. **Market gaps:** Rules data is the moat.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** High · 18. **Build difficulty:** 8/10 · 19. **MVP estimate:** 6+ months
20. **Willingness to pay:** 8/10 · 21. **Price:** $200+/mo · 22. **Retention:** 9/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Rules database maintenance + malpractice liability; incumbent moat.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 5/10 | Critical | 3/10 | 9/10 | 10/10 |

- **Customer value:** Reduces liability
- **First-customer test (100 prospects tonight?):** **YES**. State bar directories.
- **Payment test:** Sales call required
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 23. Calibration & gauge management for ISO shops/labs
*Manufacturing* · **Score 69.3/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,3,4,6,9,10 (6/12)

1. **Product concept:** Asset register, calibration due dates, AI cert intake, out-of-tolerance log, audit report.
2. **Target customer:** Machine shops/small manufacturers/labs with 50–2,000 gauges
3. **Buyer:** Quality manager
4. **Problem:** 6–12-month calibration cycles; auditors demand traceability.
5. **Current manual process:** Spreadsheets + emailed cal certs.
6. **Why it sucks:** Old desktop tools; audit scrambles.
7. **Frequency:** Weekly due items
8. **Consequence of ignoring it:** ISO audit findings; customer loss.
9. **Existing software category:** Calibration management
10. **Major competitors:** GAGEtrak, IndySoft, Qualer, CMMS vendors (MaintainX, UpKeep, Limble)
11. **Typical competitor pricing:** Desktop licences/quotes (approx.)
12. **Market gaps:** Modern, cheap, cloud UX.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 6/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $79–$249/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 5/10 (10 = little competition)
24. **Market size:** 5/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 6/10
28. **Primary acquisition channel:** ISO consultants & registrars
29. **Best starting niche:** ISO 9001 machine shops
30. **Biggest reason NOT to build it:** Slower sales; modest market; CMMS tools creep in.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 9/10 | Important | 8/10 | 6/10 | 8/10 |

- **Customer value:** Helps pass audits
- **First-customer test (100 prospects tonight?):** **YES**. IAF CertSearch / registrar certified-company lists, Thomasnet, Google Maps 'machine shop'.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Assets loaded. · Month 6: Cal cycles. · Year 2: Audit history.

---

## 24. Supplier document management for small food manufacturers (FSMA)
*Manufacturing (food)* · **Score 70.3/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,2,3,4,5,6,10 (7/12)

1. **Product concept:** Collect & track supplier COAs, GFSI certificates, allergen statements, insurance, letters of guarantee; expiry alerts; audit binder.
2. **Target customer:** Food manufacturers/co-packers with 30–300 ingredient suppliers
3. **Buyer:** QA/food safety manager
4. **Problem:** FSMA supplier verification + SQF/BRCGS audits require current supplier docs.
5. **Current manual process:** Shared folders + spreadsheets + email.
6. **Why it sucks:** Expired certs found during audits; endless chasing.
7. **Frequency:** Weekly
8. **Consequence of ignoring it:** Audit non-conformances, lost retailer accounts, recalls.
9. **Existing software category:** Supplier compliance management
10. **Major competitors:** TraceGains, Trustwell (FoodLogiQ), SafetyChain, Redzone, generic QMS
11. **Typical competitor pricing:** Mostly quote-based mid-market/enterprise (approx., unverified)
12. **Market gaps:** Small plants (<$50M) priced out; spreadsheets dominate.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 6/10 · 16. **Education required:** 4/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 4 weeks
20. **Willingness to pay:** 7/10 · 21. **Price:** $149–$399/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 5/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** GFSI certified-site directories → outbound; food safety consultants
29. **Best starting niche:** SQF-certified small manufacturers
30. **Biggest reason NOT to build it:** Buyer reach is fragmented; QA managers buy slowly; TraceGains network effect.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 9/10 | Critical | 6/10 | 7/10 | 9/10 |

- **Customer value:** Helps pass audits, reduces liability
- **First-customer test (100 prospects tonight?):** **YES**. SQFI certified-site search and BRCGS directory (public), state food processor licenses.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Supplier docs collected. · Month 6: Continuous expirations. · Year 2: Audit history + supplier network.

---

## 25. Forklift operator certs & daily pre-shift inspections
*Warehouses* · **Score 63.9/100** · **Verdict: FEATURE, NOT COMPANY** · Boring-business test: 1,3,9,10 (4/12)

1. **Product concept:** Operator 3-year evaluations + daily checklist by phone.
2. **Target customer:** Warehouses 10–200 staff
3. **Buyer:** Ops/safety manager
4. **Problem:** OSHA 1910.178 training & inspections.
5. **Current manual process:** Paper checklists.
6. **Why it sucks:** Pencil-whipped paper.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** OSHA citations, injuries.
9. **Existing software category:** Inspection checklists
10. **Major competitors:** SafetyCulture, telematics vendors, paper
11. **Typical competitor pricing:** ~$0–$25/user (approx.)
12. **Market gaps:** Little.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 6/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 4/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 3/10 · 19. **MVP estimate:** 2 weeks
20. **Willingness to pay:** 4/10 · 21. **Price:** $29–$99/mo · 22. **Retention:** 6/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 4/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Low WTP; generic checklist apps cover it.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 8/10 | 4/10 | Important | 8/10 | 5/10 | 9/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps 'warehouse'.
- **Payment test:** Self-service
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 26. Safety Data Sheet (SDS) library management
*Manufacturing / Facilities* · **Score 63.9/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,3,6,10 (4/12)

1. **Product concept:** Maintain current SDS binder, QR access.
2. **Target customer:** Any chemical-using business
3. **Buyer:** Safety manager
4. **Problem:** HazCom requires accessible current SDSs.
5. **Current manual process:** Paper binders.
6. **Why it sucks:** Outdated sheets.
7. **Frequency:** Monthly updates
8. **Consequence of ignoring it:** OSHA HazCom citations.
9. **Existing software category:** SDS management
10. **Major competitors:** VelocityEHS (MSDSonline), Chemical Safety, SDS Manager, KHA
11. **Typical competitor pricing:** Free tiers to enterprise
12. **Market gaps:** None.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $29–$99/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 1/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Mature market with free tiers and large SDS databases.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 6/10 | Important | 7/10 | 5/10 | 6/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps.
- **Payment test:** Self-service
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 27. Insurance agency producer license & appointment tracking
*Insurance administration* · **Score 69.3/100** · **Verdict: TOO COMPETITIVE** · Boring-business test: 1,2,3,4,6 (5/12)

1. **Product concept:** NIPR-synced license/CE/appointment tracking for agency producers.
2. **Target customer:** P&C/life agencies 5–50 producers
3. **Buyer:** Agency principal / ops
4. **Problem:** Multi-state licenses & CE renew constantly.
5. **Current manual process:** Spreadsheet + NIPR alerts.
6. **Why it sucks:** Missed CE, unlicensed sales.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Regulatory fines, commission chargebacks.
9. **Existing software category:** Producer licensing
10. **Major competitors:** TrustLayer (free ≤50 producers), AgentSync, InsureTrek, Agenzee, Sircon, NIPR alerts
11. **Typical competitor pricing:** TrustLayer free for up to 50 producers (via search Oct 2026)
12. **Market gaps:** None at the small end.
13. **Awareness category:** A — already knows they need it
14. **Awareness:** 9/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 2/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 3/10 · 19. **MVP estimate:** 2 weeks
20. **Willingness to pay:** 4/10 · 21. **Price:** $49–$149/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 1/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** A free, well-funded competitor owns the small-agency tier.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 8/10 | Important | 8/10 | 6/10 | 8/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. State DOI agency license lookups, Google Maps.
- **Payment test:** Self-service
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 28. CommissionCheck — carrier commission reconciliation for independent P&C agencies
*Insurance administration* · **Score 75.6/100** · **Verdict: VALIDATE** · Boring-business test: 1,2,4,5,7,8,9,12 (8/12)

1. **Product concept:** Upload/forward monthly carrier commission statements (PDF/Excel/CSV) + AMS export; AI normalizes and matches policies; flags missing, short-paid and chargeback items; tracks recovery.
2. **Target customer:** Independent P&C agencies with $1–15M premium-based revenue and 10–60 carrier/MGA relationships
3. **Buyer:** Agency owner / office manager / agency accountant
4. **Problem:** Dozens of carrier statements in different formats every month must be reconciled to expected commissions.
5. **Current manual process:** Download statements from carrier portals, retype or paste into Excel, tick-and-tie against AMS reports.
6. **Why it sucks:** Days per month of tedious matching; missed commissions are rarely recovered.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Lost revenue (missed/short-paid commissions), producer pay errors, messy books.
9. **Existing software category:** Commission reconciliation
10. **Major competitors:** Applied Recon (inside Applied Epic), AMS direct-bill/commission features (HawkSoft, AMS360, EZLynx, NowCerts), IVANS commission download, Commission Wizard, outsourced accounting
11. **Typical competitor pricing:** Commission Wizard from ~$199/mo (via search Oct 2026); Applied Recon bundled/priced for Epic users
12. **Market gaps:** Small agencies on non-Epic AMSs with many MGA/wholesaler statements that don't come via IVANS download.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 9/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 6/10 · 19. **MVP estimate:** 4–6 weeks
20. **Willingness to pay:** 7/10 · 21. **Price:** $149–$499/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 7/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Outbound to independent agencies + agency accounting consultants + Big I / agency networks
29. **Best starting niche:** Agencies with 15–60 carriers/MGAs on HawkSoft/EZLynx/NowCerts
30. **Biggest reason NOT to build it:** Statement format chaos makes accuracy hard; Applied/AMS vendors are moving in; a newer AI competitor already targets this exact niche.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 10/10 | Important | 6/10 | 8/10 | 10/10 |

- **Customer value:** Prevents lost revenue, saves admin time
- **First-customer test (100 prospects tonight?):** **YES**. State DOI agency license databases, Google Maps 'independent insurance agency', Trusted Choice/Big I directories, agency network member lists.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Backlog reconciled; first missing commissions found. · Month 6: Monthly statements never stop. · Year 2: Mapping rules per carrier accumulate — switching cost.

---

## 29. Childcare center staff compliance files
*Education administration* · **Score 70.0/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,3,4,6,10 (5/12)

1. **Product concept:** Track staff background checks, CPR, TB, training hours vs state licensing; inspector-ready export.
2. **Target customer:** Childcare centers 1–10 sites
3. **Buyer:** Center director / owner
4. **Problem:** Licensing inspectors review staff files; high turnover.
5. **Current manual process:** Paper binders.
6. **Why it sucks:** Gaps found at inspection.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Citations.
9. **Existing software category:** Childcare management (staff module)
10. **Major competitors:** Brightwheel, Procare, Kangarootime, Playground, state training registries
11. **Typical competitor pricing:** Bundled
12. **Market gaps:** Staff compliance secondary in parent-facing platforms.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 6/10 · 15. **Customer attraction:** 9/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 3/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$149/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** State childcare associations
29. **Best starting niche:** Independent centers in one state
30. **Biggest reason NOT to build it:** Thin-margin buyers; platforms likely to bundle.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Important | 7/10 | 7/10 | 8/10 |

- **Customer value:** Helps pass inspections
- **First-customer test (100 prospects tonight?):** **YES**. State childcare licensing search databases (public).
- **Payment test:** Self-service
- **Recurring test:** Month 1: Files fixed. · Month 6: Turnover. · Year 2: Annual hours.

---

## 30. Nonprofit grant reporting deadline tracker
*Nonprofits* · **Score 60.6/100** · **Verdict: AVOID** · Boring-business test: 1,2,4,7 (4/12)

1. **Product concept:** Track grant deliverables, reports, and budgets.
2. **Target customer:** Nonprofits with 10+ grants
3. **Buyer:** Development director
4. **Problem:** Missed grant reports.
5. **Current manual process:** Spreadsheets.
6. **Why it sucks:** Scattered deadlines.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Lost future funding.
9. **Existing software category:** Grant management
10. **Major competitors:** Instrumentl, Submittable, Fluxx, Foundant
11. **Typical competitor pricing:** ~$100–$300/mo (approx.)
12. **Market gaps:** Few.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 6/10 · 15. **Customer attraction:** 6/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 3/10 · 19. **MVP estimate:** 2 weeks
20. **Willingness to pay:** 3/10 · 21. **Price:** $29–$99/mo · 22. **Retention:** 6/10 · 23. **Competition opportunity:** 5/10 (10 = little competition)
24. **Market size:** 5/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 4/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Weak wallets; long approvals.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 8/10 | 9/10 | Important | 8/10 | 5/10 | 7/10 |

- **Customer value:** Prevents lost funding
- **First-customer test (100 prospects tonight?):** **YES**. IRS EO data, Candid/GuideStar.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 31. Backflow tester route & retest manager
*Home services / Field services* · **Score 70.0/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,2,3,4,9,10 (6/12)

1. **Product concept:** Tester's customer device list, annual retest reminders to customers, mobile test entry, PDF report, utility submission tracking.
2. **Target customer:** Certified backflow testers & small plumbing companies with 200–3,000 devices
3. **Buyer:** Owner-tester
4. **Problem:** Every device needs an annual test and a report filed with the utility within days.
5. **Current manual process:** Paper forms, spreadsheets, utility portals.
6. **Why it sucks:** Retests missed = lost revenue; duplicate data entry into utility portals.
7. **Frequency:** Daily in season; annual per device
8. **Consequence of ignoring it:** Lost repeat revenue; late report penalties from utilities.
9. **Existing software category:** Backflow software (tester side)
10. **Major competitors:** FAST Tester, Syncta, utility portals (Tokay, SwiftComply, BSI Online)
11. **Typical competitor pricing:** Utility portals free to testers; tester apps vary (via search Oct 2026)
12. **Market gaps:** Tester-side revenue tools (retest reminders) are thin.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$99/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 5/10 (10 = little competition)
24. **Market size:** 3/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 4/10
28. **Primary acquisition channel:** State certified tester lists
29. **Best starting niche:** Testers in one state
30. **Biggest reason NOT to build it:** Small market; low ARPU; utility portals cover reporting.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 7/10 | Important | 8/10 | 6/10 | 9/10 |

- **Customer value:** Makes money (retest revenue), prevents penalties
- **First-customer test (100 prospects tonight?):** **YES**. State/utility certified backflow tester lists (often public PDFs).
- **Payment test:** Self-service
- **Recurring test:** Month 1: Device list loaded. · Month 6: Retests flowing. · Year 2: Revenue engine.

---

## 32. Franchisee compliance document collection
*Franchises* · **Score 69.7/100** · **Verdict: FEATURE, NOT COMPANY** · Boring-business test: 1,3,5,6,10,11 (6/12)

1. **Product concept:** Franchisor collects each location's COIs, licenses, health inspections, and required reports with reminders.
2. **Target customer:** Franchisors with 20–300 units
3. **Buyer:** Franchise ops / compliance
4. **Problem:** Franchise agreements require ongoing proof from franchisees.
5. **Current manual process:** Email + shared drives.
6. **Why it sucks:** Chasing hundreds of owners.
7. **Frequency:** Monthly
8. **Consequence of ignoring it:** Brand liability, uninsured incidents.
9. **Existing software category:** Franchise compliance / COI
10. **Major competitors:** TrustLayer, BCS, FranConnect, Naranga, FranIQ, AI agent builders
11. **Typical competitor pricing:** Varies; BCS/TrustLayer serve franchise COIs
12. **Market gaps:** Mixed documents beyond COIs.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 6/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 4/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $199–$599/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 3/10 (10 = little competition)
24. **Market size:** 5/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Franchise directories + FDD filings
29. **Best starting niche:** Emerging franchisors 20–100 units
30. **Biggest reason NOT to build it:** Sales-led; COI vendors already market to franchisors; it's #1 with a different buyer.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Important | 7/10 | 7/10 | 9/10 |

- **Customer value:** Reduces liability
- **First-customer test (100 prospects tonight?):** **YES**. State FDD databases (CA DFPI, WI, MN — public), Entrepreneur Franchise 500, IFA members.
- **Payment test:** Sales call required
- **Recurring test:** Month 1: Docs collected. · Month 6: Renewals. · Year 2: Sticky.

---

## 33. Restaurant food-safety temp logs
*Restaurants* · **Score 62.9/100** · **Verdict: AVOID** · Boring-business test: 1,3,9,10 (4/12)

1. **Product concept:** Digital temp logs + checklists.
2. **Target customer:** Restaurants 1–20 units
3. **Buyer:** Owner/GM
4. **Problem:** Daily logs for inspections.
5. **Current manual process:** Paper clipboards.
6. **Why it sucks:** Pencil-whipping.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** Health violations.
9. **Existing software category:** Food safety
10. **Major competitors:** Jolt, ComplianceMate, Crunchtime, FoodDocs, SafetyCulture
11. **Typical competitor pricing:** ~$50–$150/location (approx.)
12. **Market gaps:** Hardware sensors needed for real value.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 8/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 7/10 · 19. **MVP estimate:** 3 weeks (sensors months)
20. **Willingness to pay:** 5/10 · 21. **Price:** $49–$149/mo · 22. **Retention:** 6/10 · 23. **Competition opportunity:** 2/10 (10 = little competition)
24. **Market size:** 7/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** —
29. **Best starting niche:** —
30. **Biggest reason NOT to build it:** Hardware, thin margins, high churn.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 8/10 | 3/10 | Important | 4/10 | 6/10 | 10/10 |

- **Customer value:** Prevents fines
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps, health inspection data.
- **Payment test:** Self-service
- **Recurring test:** Month 1: — · Month 6: — · Year 2: —

---

## 34. Healthcare staffing agency credential files
*Staffing agencies* · **Score 73.6/100** · **Verdict: VALIDATE** · Boring-business test: 1,2,3,4,5,6,10 (7/12)

1. **Product concept:** Collect nurse/allied candidates' licenses, certs, health records, skills checklists; build client-ready submission packets.
2. **Target customer:** Healthcare staffing agencies 20–500 active clinicians
3. **Buyer:** Credentialing coordinator / ops
4. **Problem:** Every placement needs a complete compliance file; clients/Joint Commission audit them.
5. **Current manual process:** ATS attachments + spreadsheets.
6. **Why it sucks:** Expired docs block placements; constant chasing.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** Lost placements (revenue), audit findings.
9. **Existing software category:** Staffing credentialing
10. **Major competitors:** Bullhorn + add-ons, Ceipal, Credentially, ShiftWise/Aya tools, ATS modules
11. **Typical competitor pricing:** Quote-based (approx., unverified)
12. **Market gaps:** Small agencies on general ATSs.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 8/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 4 weeks
20. **Willingness to pay:** 7/10 · 21. **Price:** $199–$499/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 4/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Staffing associations, LinkedIn
29. **Best starting niche:** Per diem nurse staffing agencies
30. **Biggest reason NOT to build it:** ATS ecosystems + agency churn; mid-market sales motion.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 8/10 | Critical | 6/10 | 8/10 | 9/10 |

- **Customer value:** Prevents lost revenue, helps pass audits
- **First-customer test (100 prospects tonight?):** **MAYBE**. Google Maps 'nurse staffing agency', state staffing agency registrations (some states), LinkedIn.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Files built. · Month 6: Every placement. · Year 2: Sticky.

---

## 35. Engineering/architecture firm license & CE tracking
*Professional services* · **Score 67.1/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,3,4,6 (4/12)

1. **Product concept:** Track PE/RA licenses, firm certificates of authorization, CE hours across states.
2. **Target customer:** A/E firms 20–300 staff
3. **Buyer:** Ops/HR
4. **Problem:** Multi-state licenses for staff and firm.
5. **Current manual process:** Spreadsheet.
6. **Why it sucks:** Missed renewals block project stamping.
7. **Frequency:** Monthly across staff
8. **Consequence of ignoring it:** Can't seal drawings; board discipline.
9. **Existing software category:** License tracking
10. **Major competitors:** Generic expiration trackers, HRIS, Deltek add-ons
11. **Typical competitor pricing:** Varies
12. **Market gaps:** Few dedicated tools.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 6/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 3/10 · 19. **MVP estimate:** 2 weeks
20. **Willingness to pay:** 5/10 · 21. **Price:** $79–$199/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 6/10 (10 = little competition)
24. **Market size:** 3/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 4/10
28. **Primary acquisition channel:** ACEC/AIA chapters
29. **Best starting niche:** Multi-state civil firms
30. **Biggest reason NOT to build it:** Small market; low urgency except at renewal.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 9/10 | Important | 8/10 | 6/10 | 7/10 |

- **Customer value:** Prevents compliance problems
- **First-customer test (100 prospects tonight?):** **YES**. State engineering board firm directories, ACEC member lists.
- **Payment test:** Self-service
- **Recurring test:** Month 1: Setup. · Month 6: Renewals. · Year 2: CE history.

---

## 36. Independent auto dealer title & temp-tag tracker
*Automotive* · **Score 68.6/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,2,3,4,9 (5/12)

1. **Product concept:** Track each sale's title receipt, payoff, temp tag expiry and DMV submission deadlines.
2. **Target customer:** Independent used-car dealers selling 20–200 cars/month
3. **Buyer:** Title clerk / owner
4. **Problem:** State deadlines to deliver titles/registrations; temp tags expire.
5. **Current manual process:** Paper deal jackets + spreadsheets.
6. **Why it sucks:** Lost titles, angry buyers, DMV complaints.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** Fines, dealer license complaints, chargebacks from lenders.
9. **Existing software category:** Dealer management systems (title module)
10. **Major competitors:** Frazer, DealerCenter, Wayne Reaves, AutoManager, state e-title systems
11. **Typical competitor pricing:** DMS ~$100–$300/mo (approx.)
12. **Market gaps:** Title workflow weak in some DMSs.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 5/10 · 15. **Customer attraction:** 9/10 · 16. **Education required:** 5/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 3–4 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $79–$199/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 6/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** State dealer license lists
29. **Best starting niche:** Buy-here-pay-here dealers in one state
30. **Biggest reason NOT to build it:** DMS overlap; dealers tolerate the pain; state-specific rules.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 7/10 | Important | 6/10 | 7/10 | 9/10 |

- **Customer value:** Prevents fines, reduces customer complaints
- **First-customer test (100 prospects tonight?):** **YES**. State dealer license databases (public in many states), Google Maps 'used car dealer'.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Open deals tracked. · Month 6: Daily use. · Year 2: Habit.

---

## 37. Small government contractor deliverables & reporting tracker
*Government contractors* · **Score 63.4/100** · **Verdict: AVOID** · Boring-business test: 1,2,4,7,11 (5/12)

1. **Product concept:** Track contract deliverables (CDRLs), reports, option dates, SAM renewal, small-business reporting.
2. **Target customer:** GovCons 10–200 staff
3. **Buyer:** Contracts manager
4. **Problem:** Many contract-specific deadlines.
5. **Current manual process:** Spreadsheets.
6. **Why it sucks:** Missed deliverables hurt CPARS.
7. **Frequency:** Weekly
8. **Consequence of ignoring it:** Poor past performance ratings, payment holds.
9. **Existing software category:** GovCon contract management
10. **Major competitors:** Deltek, Unanet, GovDash, spreadsheets
11. **Typical competitor pricing:** Mid-market ERP pricing
12. **Market gaps:** Lightweight tools.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 5/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 6/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 5/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $99–$299/mo · 22. **Retention:** 7/10 · 23. **Competition opportunity:** 6/10 (10 = little competition)
24. **Market size:** 5/10 · 25. **First 10 reachable:** 5/10 · 26. **First 100 reachable:** 4/10 · 27. **Expansion:** 6/10
28. **Primary acquisition channel:** SAM.gov entity data, APEX accelerators
29. **Best starting niche:** Service contractors 10–50 staff
30. **Biggest reason NOT to build it:** Customers see it as spreadsheet work; ERP vendors bundle.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 9/10 | Important | 6/10 | 6/10 | 8/10 |

- **Customer value:** Prevents missed deadlines
- **First-customer test (100 prospects tonight?):** **YES**. SAM.gov entity registrations & USAspending awards (public).
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Contracts loaded. · Month 6: Deliverables. · Year 2: Contract lifecycles.

---

## 38. Multi-site facility compliance inspection calendar
*Facilities management* · **Score 70.6/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,2,3,4,5,9,10,11 (8/12)

1. **Product concept:** Track recurring vendor inspections (fire, elevator, boiler, backflow, generator), collect reports, flag deficiencies per site.
2. **Target customer:** Multi-site orgs (private schools, churches, retail chains, small PM firms) with 5–100 sites
3. **Buyer:** Facilities director
4. **Problem:** Dozens of statutory inspections per site on different cycles.
5. **Current manual process:** Spreadsheet + vendor emails with PDFs.
6. **Why it sucks:** Missed inspections found by fire marshal/insurer.
7. **Frequency:** Weekly across sites
8. **Consequence of ignoring it:** Fines, insurance issues, life-safety risk.
9. **Existing software category:** CMMS / compliance management
10. **Major competitors:** UpKeep, MaintainX, Limble, Brightly (Siemens), spreadsheets
11. **Typical competitor pricing:** CMMS ~$20–$75/user/mo (approx.)
12. **Market gaps:** CMMS is work-order-centric, not compliance-evidence-centric.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 5/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Low · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $99–$399/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 5/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 4/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** Facility manager associations (IFMA), LinkedIn
29. **Best starting niche:** Private school networks / dioceses
30. **Biggest reason NOT to build it:** Buyers are hard to list; CMMS vendors can add a compliance view.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 9/10 | Critical | 7/10 | 7/10 | 9/10 |

- **Customer value:** Prevents fines, reduces liability
- **First-customer test (100 prospects tonight?):** **MAYBE**. LinkedIn 'facilities director', private school directories, IFMA chapters.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Inventory built. · Month 6: Inspections recur. · Year 2: Evidence archive.

---

## 39. 3PL monthly client billing from warehouse activity
*Warehouses / Logistics* · **Score 72.8/100** · **Verdict: VALIDATE** · Boring-business test: 1,2,4,7,8,9 (6/12)

1. **Product concept:** Import WMS/shipping activity, apply each client's rate card (storage, picks, VAS), produce invoices + audit detail.
2. **Target customer:** Small 3PLs with 10–100 clients
3. **Buyer:** Owner / billing manager
4. **Problem:** Monthly billing compiled by hand from multiple exports.
5. **Current manual process:** Excel rate cards + WMS exports.
6. **Why it sucks:** Days of work; unbilled activity; disputes.
7. **Frequency:** Monthly (some weekly)
8. **Consequence of ignoring it:** Lost revenue (unbilled fees), disputes.
9. **Existing software category:** 3PL billing
10. **Major competitors:** 3PL WMS billing modules (Extensiv, Logiwa, Packiyo, Deposco), tariff managers, QuickBooks
11. **Typical competitor pricing:** Included in WMS; standalone varies (approx.)
12. **Market gaps:** 3PLs on WMSs with weak billing.
13. **Awareness category:** B — knows the problem, not the software category
14. **Awareness:** 7/10 · 15. **Customer attraction:** 7/10 · 16. **Education required:** 3/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 6/10 · 19. **MVP estimate:** 5–6 weeks
20. **Willingness to pay:** 7/10 · 21. **Price:** $199–$499/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 5/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 6/10 · 26. **First 100 reachable:** 5/10 · 27. **Expansion:** 7/10
28. **Primary acquisition channel:** 3PL directories, Google Maps
29. **Best starting niche:** E-commerce fulfillment 3PLs on ShipStation-type stacks
30. **Biggest reason NOT to build it:** WMS integration variety; WMS vendors' billing modules.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 9/10 | 10/10 | Important | 5/10 | 8/10 | 10/10 |

- **Customer value:** Prevents lost revenue, saves time
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps '3PL fulfillment', 3PL directories (e.g., fulfillment marketplaces), LinkedIn.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: First invoice run. · Month 6: Monthly. · Year 2: Rate-card logic accumulates.

---

## 40. Veterinary controlled-substance log & DEA inventory
*Healthcare administration (veterinary)* · **Score 73.6/100** · **Verdict: NICHE OPPORTUNITY** · Boring-business test: 1,2,3,9,10 (5/12)

1. **Product concept:** Digital controlled-drug logs, running balances, discrepancy flags, biennial inventory, audit export.
2. **Target customer:** Independent vet clinics (1–5 locations)
3. **Buyer:** Practice manager / DEA registrant vet
4. **Problem:** Every dose logged; balances reconciled; biennial inventory.
5. **Current manual process:** Paper logbooks.
6. **Why it sucks:** Math errors, illegible entries, audit anxiety.
7. **Frequency:** Daily
8. **Consequence of ignoring it:** DEA fines, registration risk, diversion.
9. **Existing software category:** Controlled-substance log software
10. **Major competitors:** VetSnap, Vet S8, PIMS modules, dispensing cabinets (e.g., Cubex)
11. **Typical competitor pricing:** Varies (via search Oct 2026)
12. **Market gaps:** Paper still common in independents.
13. **Awareness category:** C — tolerates it ('how we've always done it')
14. **Awareness:** 6/10 · 15. **Customer attraction:** 9/10 · 16. **Education required:** 4/10 (lower is better)
17. **Domain knowledge:** Medium · 18. **Build difficulty:** 4/10 · 19. **MVP estimate:** 3–4 weeks
20. **Willingness to pay:** 6/10 · 21. **Price:** $79–$199/mo · 22. **Retention:** 8/10 · 23. **Competition opportunity:** 5/10 (10 = little competition)
24. **Market size:** 6/10 · 25. **First 10 reachable:** 7/10 · 26. **First 100 reachable:** 6/10 · 27. **Expansion:** 5/10
28. **Primary acquisition channel:** Google Maps vet clinics + vet practice-manager groups (VHMA)
29. **Best starting niche:** Independent small-animal clinics
30. **Biggest reason NOT to build it:** Must meet DEA recordkeeping rules exactly; specialized competitors exist; clinics tolerate paper.

| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |
|---|---|---|---|---|---|
| 10/10 | 3/10 | Critical | 7/10 | 7/10 | 10/10 |

- **Customer value:** Prevents fines, helps pass audits
- **First-customer test (100 prospects tonight?):** **YES**. Google Maps 'veterinary clinic' (~30k US clinics), state veterinary board lists.
- **Payment test:** Short demo required
- **Recurring test:** Month 1: Logs digitized. · Month 6: Daily use. · Year 2: Records retention.
