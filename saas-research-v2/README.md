# Boring SaaS Opportunities v2 — 40 ideas, scored for a solo technical founder

## Files
| File | What's inside |
|---|---|
| [01-all-40-ideas.md](01-all-40-ideas.md) | All 40 ideas × 30 analysis fields + boring/Excel/must-have/feasibility scores, first-customer test, payment test, recurring test |
| [02-ranking.md](02-ranking.md) | Weights + the final ranked table with verdicts |
| [03-top-10.md](03-top-10.md) | Top 10: why now, why pay, why stay, find/contact, first offer, MVP, pricing, competitors, advantage, risk |
| [04-top-3-business-plans.md](04-top-3-business-plans.md) | Mini business plans for three different businesses: SubShield, CommissionCheck, PayrollProof |
| [05-final-decision-and-7-day-validation.md](05-final-decision-and-7-day-validation.md) | Answers to the 10 questions, the single winner, and the 7-day validation plan with PASS/FAIL |
| `_build/` | Score data + generator (`python3 _build/render.py` regenerates files 01 and 02) |

## Bottom line
- **Winner: SubShield**, subcontractor COI tracking for commercial GCs (79.4/100, the only BUILD verdict).
- **Fallbacks, in order:** provider credentialing (78.1), PayrollProof certified payroll (77.7).
- **No idea scored above 80.** Verdicts: 1 BUILD, 5 VALIDATE, 9 NICHE OPPORTUNITY, 9 TOO COMPETITIVE, 6 FEATURE NOT COMPANY, 4 TOO HARD, 6 AVOID.

## What the live searches changed (October 2026)
A handful of live web searches checked the biggest assumptions. They changed several scores:
- **COI tracking** now has a cheap low end: BCS is free up to 25 vendors and about $0.95/vendor/month self-serve. The competition score went down, and SubShield must win on automation, service and distribution.
- **DQ files** has $5–$49/mo self-serve competitors (Core Compliance, Roadworthy HQ, DOTDriverFiles). Verdict: TOO COMPETITIVE.
- **Lien waivers** has $49/mo tools (Waivr, LienDone). Verdict: feature of SubShield.
- **Producer licensing:** TrustLayer is free for up to 50 producers. Verdict: TOO COMPETITIVE.
- **Certified payroll:** LCPtracker's contractor product already imports QuickBooks and other payroll exports. Competition score lowered.
- **Commission reconciliation:** Applied Recon (inside Epic) and Commission Wizard (from ~$199/mo) exist.
- **Home care compliance** is bundled into agency platforms (HHAeXchange, CareTime, ShiftCare). Verdict: FEATURE.

**The pattern:** AI made "expiring-document tracker" products cheap to build, so 2025–26 brought a flood of $5–$49 tools. Your moat is no longer the code. It's **distribution (brokers, associations, public registries), vertical depth (rules, templates), and a done-for-you service layer.**

## "Hidden boring" signals used
Search phrases that point at spreadsheet-run, money-adjacent work, and where they lead:

| Phrase | Where it pointed |
|---|---|
| "certificate expiration", "vendor paperwork" | COI tracking (#1), franchisee docs (#32), food supplier docs (#24) |
| "employee credentials", "annual certification" | credentialing (#11), staffing credentials (#34), trade licenses (#4), childcare (#29) |
| "monthly reconciliation" | carrier commissions (#28), 3PL billing (#39), vet controlled-substance balances (#40) |
| "manual reporting" | certified payroll (#3), IFTA (#8) |
| "compliance checklist", "audit preparation" | DQ files (#7), calibration (#23), facility inspections (#38) |
| "permit renewal", "license renewal" | STR permits (#19), A/E licensing (#35), rental registration (#15) |
| "we track this manually", "spreadsheet" | nearly all of the above; highest Excel-replacement scores in #28, #39, #3, #1 |

## Sources (live searches, October 2026)
- [BCS COI Tracker pricing](https://getbcs.com/pricing) · [Vertikal RMS: COI tracking cost guide](https://vertikalrms.com/article/how-much-does-coi-tracking-software-cost-2025-pricing-guide/) · [Capterra: Constrafor](https://www.capterra.com/p/211555/Paylocity/)
- [Certified Payroll WH-347 pricing (SaaSworthy)](https://www.saasworthy.com/product/certified-payroll-wh-347/pricing) · [SaaSRat: construction payroll software](https://saasrat.com/blog/best-payroll-software-for-construction/) · [LCPtracker LCPcertified](https://lcptracker.com/solutions/lcpcertified/) · [Can Gusto do certified payroll?](https://officeconsumer.com/can-gusto-do-certified-payroll-w-examples-faqs/)
- [CA DIR public works notices](https://www.dir.ca.gov/public-works/Public_Works_Notices.html) · [Fennemore: DIR registration program](https://www.fennemorelaw.com/department-of-industrial-relations-new-registration-program-for-public-works-projects/)
- [Commission Wizard](https://www.producthunt.com/products/commission-wizard) · [Applied Systems: AI reconciliation](https://www1.appliedsystems.com/en-us/resources/videos/ai-powered-reconciliation-solution-agency-finance-teams-need) · [IVANS commission download](https://prep.ivans.com/resources/demos/efficiently-reconcile-commissions-with-commission-download/)
- [Roadworthy HQ](https://www.getapp.com/all-software/a/roadworthy-hq/) · [Core Compliance (Capterra)](https://www.capterra.com/p/10038965/Core-Compliance/) · [DOTDriverFiles (Capterra)](https://www.capterra.com/p/10025636/DOTDriverFiles/)
- [HHAeXchange on homecare automation](https://hhaexchange.com/blog/say-goodbye-to-manual-processes-the-abcs-of-homecare-automation) · [CareTime caregiver compliance](https://caretime.us/blog/how-to-ensure-your-caregivers-remain-compliant)
- [VetSnap controlled drug logs](https://go.vetsnap.com/controlled-drug-log-software) · [Vet S8](https://www.softwareadvice.com.au/software/560914/Vet-S8)
- [Rabbet lien waivers](https://rabbet.com/features/lien-waiver-management-software) · [Waivr](https://www.saasworthy.com/product/waivr)
- [TrustLayer NIPR](https://www.trustlayer.io/pages/trustlayer-nipr-integration) · [TrustLayer franchise COI](https://www.trustlayer.io/resources/blog-franchise-coi-automation-compliance)
- [Tokay user guide (Yakima)](https://www.yakimawa.gov/services/water-irrigation/files/Tokay-User-Guide.pdf) · [Park City backflow (SwiftComply)](https://parkcity.org/departments/public-utilities/backflow-prevention)
- [Cleverence: 3PL billing systems](https://www.cleverence.com/articles/reviews-3pl/10-leading-billing-invoicing-systems-for-3pl-small-business-4627)

Everything not covered by these sources (other competitors' pricing, market sizes, the scores themselves) is judgment based on prior knowledge. Treat it as a hypothesis for interviews to test.
