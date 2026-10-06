# Part 2 — Scoring & Opportunity Score

## Method

Each dimension is scored 1–10, where **10 is always good for you**:
- **Competition 10** = little effective competition
- **Acquisition 10** = easy to find and reach buyers
- **Ease of dev 10** = easy to build

| Dimension | Weight | Why this weight |
|---|---|---|
| Pain level | 15% | No pain, no sale |
| Willingness to pay | 15% | Pain without budget is a charity |
| Recurring need | 10% | Subscription must map to a recurring job |
| Ease of development | 10% | 2–6 week MVP constraint |
| Competition | 10% | Room to win |
| Customer acquisition (ease) | 10% | Boring SaaS lives or dies on distribution |
| Profitability | 10% | Margin after support/services |
| Retention | 10% | Churn kills small SaaS |
| Scalability | 5% | Path to a larger company |
| Founder friendliness | 5% | Solo-buildable, low support, no domain moat you lack |

**Opportunity Score = Σ(score × weight) out of 100.**

## Scores

| # | Idea | Pain | WTP | Recur | Ease | Comp | Acq | Profit | Retain | Scale | Founder | **Score** | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SubShield (COI tracking, contractors) | 8 | 8 | 9 | 7 | 6 | 7 | 8 | 9 | 8 | 8 | **78.0** | BUILD |
| 3 | CredCadence (provider credentialing) | 9 | 9 | 9 | 5 | 5 | 6 | 8 | 9 | 8 | 5 | **75.5** | BUILD |
| 2 | FleetFile (DOT DQ files) | 9 | 8 | 9 | 6 | 5 | 6 | 8 | 9 | 7 | 6 | **75.0** | BUILD |
| 4 | LicenseLedger (trade certifications) | 7 | 7 | 8 | 8 | 6 | 7 | 7 | 8 | 7 | 8 | **72.5** | Module of #1 |
| 5 | InspectLoop (fire inspections) | 8 | 8 | 9 | 4 | 5 | 6 | 8 | 9 | 7 | 5 | **71.0** | Only with domain expertise |
| 7 | ChaseDocs (bookkeeper doc chaser) | 7 | 7 | 10 | 7 | 3 | 7 | 7 | 8 | 7 | 8 | **70.5** | Strong incumbent |
| 16 | EligiBot (dental insurance verification) | 9 | 8 | 10 | 3 | 4 | 5 | 8 | 8 | 8 | 3 | **69.0** | Team play, not solo |
| 6 | NudgePay (AR reminders) | 8 | 7 | 9 | 7 | 3 | 5 | 7 | 7 | 8 | 7 | **68.0** | Vertical only |
| 12 | EntityDesk (entity compliance for CPAs) | 7 | 6 | 8 | 7 | 6 | 6 | 7 | 8 | 6 | 7 | **68.0** | Conditional |
| 10 | PermitPilot (STR permits) | 7 | 7 | 8 | 5 | 7 | 6 | 7 | 8 | 6 | 5 | **67.5** | Data-heavy |
| 13 | LienClock (lien deadlines) | 8 | 7 | 8 | 5 | 4 | 5 | 7 | 7 | 7 | 5 | **64.5** | Legal risk |
| 14 | CalibrateIQ (calibration) | 6 | 6 | 8 | 7 | 5 | 5 | 6 | 8 | 6 | 7 | **63.5** | Solid but slow |
| 8 | CloseReport (bookkeeper reports) | 6 | 6 | 9 | 6 | 3 | 6 | 6 | 7 | 7 | 7 | **62.0** | Reject |
| 9 | RentalCheck (rental inspections) | 6 | 6 | 7 | 6 | 4 | 6 | 6 | 7 | 7 | 6 | **60.5** | Reject |
| 18 | ReorderAlert (Shopify inventory) | 6 | 5 | 9 | 7 | 3 | 7 | 5 | 6 | 7 | 7 | **60.5** | Reject |
| 15 | ToolboxTrack (OSHA talks) | 6 | 5 | 8 | 7 | 4 | 6 | 5 | 7 | 6 | 7 | **60.0** | Feature |
| 19 | HOAWatch | 6 | 5 | 8 | 6 | 4 | 5 | 6 | 8 | 5 | 6 | **59.0** | Reject |
| 30 | RatioReady (childcare) | 7 | 5 | 8 | 6 | 4 | 5 | 5 | 7 | 5 | 5 | **58.0** | Weak |
| 11 | RenewalRadar (contract renewals) | 5 | 5 | 7 | 8 | 4 | 4 | 6 | 6 | 7 | 8 | **57.5** | Reject |
| 17 | CleanCRM (HubSpot hygiene) | 5 | 5 | 7 | 7 | 4 | 6 | 6 | 5 | 6 | 8 | **57.0** | Reject |
| 21 | ShiftProof (janitorial QA) | 5 | 5 | 8 | 7 | 5 | 5 | 5 | 6 | 5 | 7 | **57.0** | Weak |
| 20 | TempLog (restaurant food safety) | 6 | 5 | 10 | 4 | 4 | 4 | 5 | 7 | 6 | 4 | **55.5** | Reject |
| 28 | CloseClock (RE transactions) | 6 | 5 | 9 | 6 | 2 | 5 | 5 | 6 | 5 | 6 | **55.0** | Reject |
| 25 | ReviewLoop | 5 | 6 | 8 | 7 | 1 | 4 | 5 | 5 | 6 | 6 | **52.5** | Reject |
| 24 | MissedCall Rescue | 6 | 5 | 8 | 8 | 1 | 4 | 5 | 4 | 5 | 6 | **52.0** | Reject |
| 29 | GrantGuard | 5 | 3 | 7 | 7 | 5 | 5 | 4 | 6 | 4 | 7 | **51.5** | Reject |
| 22 | RankRecap (SEO reports) | 4 | 5 | 9 | 6 | 1 | 4 | 5 | 6 | 6 | 6 | **50.5** | Reject |
| 27 | W9Collect | 6 | 5 | 3 | 8 | 3 | 5 | 5 | 3 | 5 | 7 | **49.5** | Feature of #1 |
| 23 | SiteCare Reports (WP) | 3 | 4 | 8 | 6 | 1 | 5 | 4 | 6 | 5 | 6 | **46.0** | Reject |
| 26 | OnboardKit | 5 | 4 | 5 | 7 | 1 | 3 | 4 | 4 | 5 | 6 | **43.0** | Reject |

## What the scores reveal

1. **The winners share one pattern:** a *document that expires* + *a third party who must supply it* + *a financial or legal penalty when it lapses* + *an identifiable buyer whose job is to prevent the lapse*. That is the "boring compliance loop", and it's the most reliable pattern for small-team subscription software.
2. **The losers share one pattern:** they were horizontal, marketing-flavored, or something a platform (HubSpot, Shopify, QuickBooks, Gusto, GoHighLevel resellers) bundles for free.
3. **Ideas #1, #4, and #27 form one product** (contractor vendor compliance). That's good: it gives the winner a natural expansion path.
4. **Scores are judgment calls.** A ±1 change on any dimension moves scores by 0.5–1.5 points, so the top 3 (78 / 75.5 / 75) are statistically close. Validation results, not this table, should decide between them.

## Top five selected

1. **SubShield** — COI tracking for contractors (78.0)
2. **CredCadence** — provider credentialing & re-attestation (75.5)
3. **FleetFile** — DOT driver qualification files (75.0)
4. **LicenseLedger** — trade workforce certifications (72.5). Analyzed as a standalone, but I recommend it as SubShield's second module.
5. **InspectLoop** — fire & life-safety inspections (71.0). Analyzed honestly, including why it's the riskiest of the five for you.
