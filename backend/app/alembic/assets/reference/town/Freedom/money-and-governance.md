# Freedom School District: Money, the Kennett Contract and Governance

Part of the Freedom research (town/Freedom). Gathered November 13, 2026.

## Summary

**What's covered:** 9 topics, 86 facts and 5 number tables on the Freedom School District's budget and cost per pupil, its school tax and state aid, the 2003 Conway (Kennett) tuition agreements and what has happened since Freedom gave notice to leave them, other middle and high school options (Governor Wentworth/Kingswood, Fryeburg Academy, Tamworth), special education costs, the building and its capital plan, the district's own bus fleet, its share of SAU 13, studies of cooperation or consolidation, and how residents can take part.

- **Budget:** 2026-27 operating budget $4,080,728, down 0.7%; ten-year history; the district's own cost-per-pupil sheet by level; budget drivers; special education and out-of-district costs; teacher wage lines and the staff contract.
- **Taxes and aid:** DRA's 2025 school tax calculation as the town report prints it (net school appropriations and the statewide tax kept locally), the board's estimate of the 2026-27 tax rate impact, Freedom's very high property value per pupil (NH DOE's adequacy aid calculation, with no grant since FY2024, is in the site's data, adequacy_aid, so this file does not repeat it), and a **derived** estimate of the Conway tuition part of the school tax rate (about 36% of the school budget). DRA's tax rates and NH DOE's school taxes for Freedom and its neighbors, including the school share and the full value rate, are in the site's data (property_tax), so this file does not repeat them or compare them.
- **The Kennett contract:** the 2003 terms (20 years, 90% attendance, 65% attendance/35% property value formula), the February 12, 2024 notice to exit, the 2026-27 calculation and payments, Conway's January 2026 offer, the February 2026 pause, Conway's September 2026 policy charging non-contract towns a 25% premium, and the October 2026 negotiations with Governor Wentworth, Moultonborough, Fryeburg and Conway. No new contract was in place as of November 13, 2026.
- **Buildings and buses:** the February 2026 capital plan (small items through FY2031, boilers in FY2034), reserve fund balances ($1,197,375.24 in five funds), and a five-bus district-owned fleet.

**Main sources:** Freedom School Board minutes (August 2022 to October 2026) and board packets (February 2024, February 2026, November 9, 2026), Freedom School District annual reports (FY2023, FY2025), the 2026 warrant and MS-26, the 2003 Conway tuition agreements (grades 7–8 and 9–12), the HB 1265 report, the Town of Freedom 2025 annual report, NH DRA tax rates and NH DOE adequacy files (library CSVs), RSA 654:1, 32:5, 197:1 and 40:4, Conway School Board minutes (September 2026), and read-only queries of the site database.

**Premises checked:**
- "Fewer than 60 students": correct. Freedom Elementary had 44 students in K–6 on October 1, 2025 and 33 on October 1, 2026.
- "The current long-term agreement with Conway": out of date. The 2003 agreements still apply, but the board voted on February 12, 2024 to give notice to exit them, and 2026-27 is their last year. No new Conway contract had been signed by November 13, 2026.
- "School taxes make up the bulk of our property tax bill": only about half in 2025. The school parts were $3.72 of Freedom's $7.39 rate (50.3%), against 65–72% in Madison, Tamworth, Ossipee and Conway (DRA's figures, in the site's data: property_tax).
- "Bus fuel and fleet maintenance just to transport grades 7–12": partly right. Freedom owns five buses and employs its drivers, but its budgets do not split the cost of Kennett routes from elementary routes.
- "Eligible for tuitioned enrollment at Fryeburg Academy": not yet. Freedom had no Fryeburg agreement as of November 2026. The board was negotiating with the Academy, which does not offer grades 7–8.
- "Enrollment hovering under 60" (P9.2): enrollment is below that and falling. The October 2026 count of 33 ties the lowest in the annual report's counts since 2016 (33 in 2021).

**Main gaps:**
- The results of the March 9, 2026 district meeting were not posted. The 2026-27 "adopted" column in the district's working budget matches the proposed budget.
- The Governor Wentworth agreement and Freedom's staff contract (FEA) were not posted. The state labor board's copy of the 2022–2024 contract was blocked (HTTP 403).
- No published salary schedule could be checked against the site's salary bands.
- No document defines when a K–6 school becomes "unsustainable".

**Proposed shared topic:** none.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P2.1 Why per-pupil spending is high; Conway tuition share of the tax bill | district-budget-and-cost 5–9; district-tax-and-state-aid 1–4; table freedom_cost_per_pupil_by_level; site data: cost per pupil, ADM, property_tax (Freedom district) | full | NH DOE's $41,267 covers the elementary school only. Freedom's ADM was 51.26 (FY2025). Conway tuition was 36.1% of the 2025-26 school budget, so roughly $1.34 of the $7.39 rate (**derived**, rough) |
| P2.2 Shared services or consolidation studies | district-consolidation-history 1–6; district-sau-governance 5–7; Jackson file district-consolidation-history 3 in `Jackson/money-and-governance.md` | full | 2020–22 eight-town cooperative study and joint maintenance committee (neither went ahead), SAU-level sharing (health insurance quotes, one policy book, BCBA, meals), exploratory special education consortium |
| P2.3 How Conway tuition is calculated | district-tuition-contracts 1–12; table freedom_cost_per_pupil_by_level; Conway file district-tuition-contracts 3–6 | full | 65% attendance / 35% property value of Conway's budget plus CPI + 2.5%. In 2026-27 Freedom had 4.87% of Kennett High attendance but 11.05% of the property value |
| P5.3 Out-of-district special education costs; catastrophic aid; reserves | district-budget-and-cost 12–16; library money-special-education-aid | full | $100,000 budgeted for out-of-district tuition; Special Education reserve $377,733.47; no state special education aid budgeted or received FY2025–FY2027 |
| P8.3 Does the agreement cover summer credit recovery or dual enrollment? | district-tuition-contracts 13–14; sau9 file kennett-pathways school-programs-after-grade-6 32; Jackson file school-programs-after-grade-6 16 in `Jackson/after-jackson-grammar.md` | partial | The 2003 agreement does not mention either. Kennett has no summer school; dual enrollment tuition falls to families under Conway policy unless a board pays. No Freedom vote on paying it was found |
| P9.1 Capital repairs coming due | district-facilities-and-capital 1–7; tables freedom_cip_withdrawals, freedom_capital_reserves | full | Flat roof replaced summer 2025. FY2027–FY2031: about $49,300 planned (driveway sealing). Deferred window replacement; boilers #3–#4 due 2034 |
| P9.2 When a K–6 building becomes unsustainable | district-consolidation-history 7–10; district-budget-and-cost 6–8; table freedom_k6_enrollment | partial | Facts only. "Unsustainable" is not defined in any document. Enrollment 54 (2016) to 33 (2026); estimated $53,355 per elementary pupil for 2026-27; Selectboard raised "continued viability" in August 2026 |
| P9.3 Transport costs for grades 7–12; who runs the buses | district-transportation 1–8; district-tuition-contracts 1 | partial | Freedom owns and runs its buses. Total transportation $249,597 (2026-27). No 7–12 split exists; the 2021-22 options study gave $298,138 for all regular routes |
| P12.1 Teacher pay and retention vs SAU 13 and SAU 9 | district-budget-and-cost 9–11; site data: average salary, salary bands | partial | Pay comparisons come from the site's data (2026 average: Freedom $64,764, Madison $57,165, Tamworth $73,624, Conway $60,390). The FEA contract and schedule were not retrieved, so the site's bands were not checked (see For another file) |
| P13.1 School tax rate vs Madison, Tamworth, Effingham; school share | site data: property_tax (Freedom, Madison and Tamworth districts; Effingham in the Governor Wentworth Regional district); district-tax-and-state-aid 1–2 | full | The rates, full value rates and school shares are in the site's data (2025 full value rates: Freedom 7.20, Madison 9.02, Tamworth 13.33, Effingham 14.53; Freedom's school share 50.3%). Fact 3 explains Freedom's low school rate (property value per pupil) |
| P13.2 Non-resident owners' voice | district-board-and-public-input 1–5 | full | Only people domiciled in Freedom may vote (RSA 654:1). Budget hearings and board meetings are open to anyone. The meeting rules do not address non-voters speaking |
| P14.3 Fryeburg Academy eligibility | high-school-tuition-options 1–5; town/maine/fryeburg-academy.md; Jackson file district-tuition-contracts 13–20 in `Jackson/money-and-governance.md` | full | No agreement as of November 2026; negotiating; Fryeburg has no grades 7–8 |
| P16.1 Adequacy aid for a property-rich, low-enrollment town | district-tax-and-state-aid 2, 5–7; site data: adequacy_aid (Freedom district); library money-adequacy-grant-calculation, money-rand-case | full | Grant $0 except a FY2023 hold-harmless payment. Statewide tax raised in Freedom exceeds the state's adequacy cost by about $0.7 million a year (site data) |
| P16.2 SAU 13 vs a cooperative district or SAU 9 | district-consolidation-history 1–6, 11; district-sau-governance 1; Bartlett file district-consolidation-history 5 | partial | Facts only, no pros-and-cons study found. Board members said a SAU 9/13 combination was explored and Conway declined |
| P16.3 What SAU 13 publishes on ratios, special education spending and central office costs | district-sau-governance 2–4; district-budget-and-cost 12 | partial | Special education spending (RSA 32:11-a statement), the SAU budget and administrator salaries are published. No staff-ratio report was found (the site's staff data covers it) |
| P20.1 Special education and tuition trends vs taxes | district-budget-and-cost 3–4, 12–13; district-tuition-contracts 4–6; district-tax-and-state-aid 3; tables freedom_operating_budget, freedom_cost_per_pupil_by_level | full | Conway tuition ranged from about 36% to 42% of the total budget in 2023-24 to 2026-27 (**derived**). Special education spending rose 22% in 2024-25 |
| P20.3 How the board engages residents before budget votes | district-board-and-public-input 3–9 | full | Monthly meetings with public comment, a February hearing, the annual report with full budget detail, Selectboard on the agenda, and 2024 hearings on middle and high school options. No newsletter on the budget was found |

## district-budget-and-cost: Freedom's Budget, Cost per Pupil, Special Education and Pay

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. At the March 10, 2025 Freedom School District meeting, voters raised and appropriated $4,613,018 in all; the board chair said the 2025-26 operating budget was a 2.12% increase driven by a 7.5% health insurance increase and one added paraprofessional and classroom teacher.
   - citation: Freedom School District Annual Report (FY2025), Annual School District Meeting Minutes, March 10, 2025, pp. 13–17; Town of Freedom 2025 Annual Report, 2025 Town Meeting Minutes (abridged)
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "There is a 2.12% increase over last year. Health insurance costs increased by 7.5%. Also, we are adding one additional paraprofessional and one additional classroom teacher." Town report: "the amount of $4,613,018.00 had been raised and appropriated." Transcribed from image (OCR). Raw: raw/money/annual-report/freedom-ar-fy2025.pdf, .ocr.txt (pages 15–19); raw/money/town/freedom-town-report-2025.ocr.txt
2. The Freedom School Board proposed a 2026-27 operating budget of $4,080,728 (2026 warrant Article 2, recommended 4-0-0), $28,416.75 (0.7%) less than 2025-26's $4,109,144.75; with the $408,678 SAU 13 share, the total raised by taxation was $4,489,406, up $1,534.25 (0.03%).
   - citation: Freedom School District 2026 Warrant, Articles 2–3; FY2025 Annual Report, "FY27 Freedom Proposed Budget & Warrant Comparison," p. 5
   - source: https://drive.google.com/file/d/1kq41YFzDYJxLCMPHgJApy9HjdE0gsZxA/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Warrant: "raise and appropriate the sum of $4,080,728 for the support of schools ... (The school board recommends this appropriation 4-0-0)." The February 9, 2026 hearing minutes corrected the tally to 3-0-1. The meeting results were not posted (see Not retrieved); the November 2026 working budget lists $4,130,728 as "2026-2027 ADOPTED", which equals Article 2 plus the $50,000 Article 4 reserve deposit (**derived** reading). See table freedom_operating_budget. Raw: raw/money/financial/freedom-warrant.pdf, .ocr.txt; raw/money/annual-report/ar-fy2025-rot-p7.png; raw/money/packets/fsb-packet-2026-11-09-p70.png
3. Freedom's operating budget rose from $3,308,343.88 in 2016-17 to $4,080,728 proposed for 2026-27, about 23% over ten years (**derived**), with large swings between years: down 13.1% in 2022-23, then up 8.1% in 2023-24 and 11.0% in 2024-25.
   - citation: Freedom School District Annual Report (FY2025), "FY27 Freedom Proposed Budget & Warrant Comparison," p. 5
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "% Difference between budget yrs. No warrants (except CBA) 3.5% 5.6% 0.5% 7.5% 4.4% -2.0% -13.1% 8.1% 11.0% 2.1% -0.7%". Derived: (4,080,728 − 3,308,343.88) ÷ 3,308,343.88 = 23.3%. In October 2022 the chair told the Selectboard "Recent special education expenses have accounted for the larger swings in the school district budget" (raw/money/minutes/fsb-2022-10-11.txt). Raw: raw/money/annual-report/ar-fy2025-rot-p7.png
4. The board's 2026-27 budget-driver page lists wages down $92,465 (two paraprofessionals, a part-time driver and a redefined transportation coordinator), health insurance and benefits up $15,042 with "22.3% Health insurance increase," and middle and high school tuition plus insurance up $54,691 to $1,769,042, noted "Final year of Conway Contract."
   - citation: Freedom School District Annual Report (FY2025), "Freedom School District 2025-2026 Proposed Budget Budget Drivers," p. 45
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed (rotated): "100s WAGES AND SALARIES 1,259,183 1,166,719 (92,465) Staff reductions: 2 paraprofessionals, 1 part-time driver, redefined transportation coordinator"; "200s HEALTH INS/RETIREMENT/OTHER BENEFITS 644,931 659,973 15,042 22.3% Health insurance increase"; "500s REG ED TUITION (MS/HS), INSURANCE 1,714,351 1,769,042 54,691 Final year of Conway Contract". The page's title says 2025-2026 but its columns are 2025-26 adopted and 2026-27 proposed. Raw: raw/money/annual-report/ar-fy2025-p47.png
5. NH DOE's cost per pupil for Freedom ($41,267 in 2024-25, site data) counts only the operating cost of Freedom Elementary (K–6) divided by its average daily membership (51.26 in 2024-25, down from 59.87 in 2015-16); it leaves out tuition to Conway and transportation (library topic measure-cost-per-pupil).
   - citation: site data (district_cost_per_pupil; doe_form_adm, Freedom, 2016–2025); library topic measure-cost-per-pupil
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Query rows: "Freedom | 2025 | 41267" and ADM "2016 | 59.87", "2025 | 51.26". For scale (**derived**): Madison's 2025 figure was $35,063 at ADM 125.70 and Tamworth's $37,750 at ADM 165.15, so Freedom spreads its school over about 41% of Madison's and 31% of Tamworth's pupils. The 2026 HB 1265 report graphs the same series in November 2025 dollars, peaking at $47,490 in 2022 and $41,268 in 2025 (raw/money/financial/freedom-hb1265-graph-p1.png). Raw: raw/money/state-data/site-db-freedom-queries-2026-11-13.txt
6. At Freedom's March 13, 2023 district meeting, the board chair said the cost per elementary student was $37,771.80 in 2020-21, $43,754.63 in 2021-22 and $33,502.96 in 2022-23 (on an October enrollment of 48), that "A change of just a few students makes a big impact," and that the statewide average was about $20,000.
   - citation: Freedom School District Annual Report (FY2023), Annual School District Meeting Minutes, March 13, 2023, Article 6
   - source: https://drive.google.com/file/d/1Jb1tfeZDjH3fiCfNAs232fbsRMGSOp9B/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "In 2020-21 the cost per elementary student was $37,771.80. In 2021-22 it was $43,754.63. In 2022-23 it is $33,502.96 based on the October student enrollment of 48. A change of just a few students makes a big impact. The average statewide cost per elementary student is about $20,000." Selectman Les Babb added: "This board is working very hard to try to get more students, in order to lower the per student cost." Transcribed from image (OCR). Raw: raw/money/annual-report/freedom-ar-fy2023.pdf, .ocr.txt (page 18)
7. The district's own cost-per-pupil sheet (November 2026) estimates 2026-27 elementary cost at $53,354.53 per pupil on an estimated 32 pupils (ADM-A), up from $42,866.68 in 2025-26 (draft, 42.63 pupils) and $34,610.99 in 2024-25 (52.01 pupils); its middle and high columns are Conway tuition divided by Freedom's Kennett students.
   - citation: Freedom School Board packet, November 9, 2026, "Freedom School District - Cost per Pupil," p. 40
   - source: https://drive.google.com/file/d/1iFpMO1L26C15tON_U4qwap535mmTnfpO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "Estimated CPP SY27 $53,354.53 $35,106.00 $36,960.26 $43,340.00"; "Draft CPP SY26 $42,866.68 $34,872.31 $40,574.06 $40,761.56". The sheet subtracts food service, transportation and "Supplmt Exp" (not defined on the sheet) from elementary expenses, so its figures differ from NH DOE's. See table freedom_cost_per_pupil_by_level. Raw: raw/money/packets/fsb-packet-2026-11-09-p40.png, fsb-packet-2026-11-09.pdf
8. In September 2026 Freedom's board chair "spoke about efficiencies across SAU13, and the cost of operating a rural school such as Freedom Elementary is consistent with other rural schools across the State of New Hampshire," and the board's March 2026 report said "Enrollment is dropping. We are working to find ways manage our fixed costs without the economies of scale."
   - citation: Freedom School Board Minutes (draft), September 16, 2026, Freedom Select Board item; Freedom School Board Report, March 2026 (FY2025 Annual Report, p. 21)
   - source: https://drive.google.com/file/d/1XQN4QcIgbPFHyzp9pHrgfxjCTwdMXPX5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Draft minutes, cited only for what was said. The same minutes list "Budget Drivers: Number of staff; Healthcare options ...; Housing options in the neighboring towns of Ossipee and Effingham are impacting student enrollment." No document gives a statewide comparison of rural K–6 costs. Raw: raw/money/minutes/fsb-2026-09-16-draft.pdf, .txt; raw/money/annual-report/freedom-ar-fy2025.ocr.txt (page 23)
9. Freedom's 2027-28 working budget carries $343,801 on the "WAGES- TEACHERS" line for five classroom teachers (about $68,760 each on average, **derived**), against $345,570 adopted for 2026-27; the 2026 HB 1265 report graphs Freedom's average teacher salary at $59,399 for 2024-25.
   - citation: Freedom School Board packet, November 9, 2026, 2027-2028 Working Budget, account 01.1100.110.077, p. 48; Freedom HB 1265 Mandatory Report to Voters (graph), p. 1
   - source: https://drive.google.com/file/d/1iFpMO1L26C15tON_U4qwap535mmTnfpO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Row text: "01.1100.110.077 WAGES- TEACHERS $243,028 $182,825 $345,570 $343,801 ($1,769) (0.51)", with an account note listing five teachers. Derived: 343,801 ÷ 5 = 68,760. The HB 1265 graph is in November 2025 dollars and shows a low of $44,147 for 2021. Year-by-year average salaries for Freedom, Madison, Tamworth, Conway and Governor Wentworth are in the site's data (2026: $64,764, $57,164.83, $73,624, $60,390, $80,090). Individual salaries are in the annual report's staffing page and are not repeated here. Raw: raw/money/packets/fsb-packet-2026-11-09.txt (page 48); raw/money/financial/freedom-hb1265-graph-p1.png
10. Freedom's staff contract with the Freedom Employee's Association runs three years, 2024-25 to 2026-27 (the February 2024 draft warrant listed increases of $80,881, $29,436 and $30,604; the budget comparison shows $79,129 for the contract in 2024-25); in October 2026 the business administrator said the next contract will be a separate warrant article, and FEA negotiations were being scheduled.
   - citation: Freedom School Board packet, February 12, 2024, draft 2024 warrant, Article 3; FY2025 Annual Report, p. 5; Freedom School Board Minutes (draft), October 19, 2026
   - source: https://drive.google.com/file/d/115Klx3ZNQHzI1nNb3TWIYBCkrOuzkAeL/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Draft warrant text: "approve the cost items included in the Collective Bargaining Agreement reached between the Freedom School Board and the Freedom Employee's Association ... Year 1 2024-2025 $80,881 Year 2 2025-2026 $29,436 Year 3 2026-2027 $30,604". October 2026: "Collective Bargaining Agreement (CBA) will be a separate warrant article"; "CBA health insurance option must change due to sunsetting / no longer available"; "FEA Negotiations Timeline - scheduling underway". The contract and its salary schedule were not found online (see Not retrieved). Raw: raw/money/packets/fsb-packet-2024-02-12.pdf, .txt (page 5); raw/money/minutes/fsb-2026-10-19-draft.txt
11. Of the five classroom teachers on Freedom's 2025-26 staffing page, four were hired in 2023 or later (**derived** from the dates of hire), and in July 2024 the board voted unanimously "to declare that Freedom is in a geographical area of critical shortage of teachers" and declared a one-year emergency authorization to hire a teacher.
   - citation: FY2025 Annual Report, "Freedom School District - Staffing in FY: 2025-2026," p. 40; Freedom School Board Minutes, July 8, 2024, action after non-public session
   - source: https://drive.google.com/file/d/1CniHfd_vsoHlSLW12vkHvXyKS56Z0Kxh/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Derived count from the "DOH" column for the five positions titled "TEACHER" (one 1999, one 2023, two 2024, one 2025). No turnover rate for Freedom, Madison, Tamworth or SAU 9 was found; this is not a retention rate. In 2023 the principal reported a "desperate need" for a guidance position (raw/money/annual-report/freedom-ar-fy2023.ocr.txt). Raw: raw/money/annual-report/ar-fy2025-p42.png; raw/money/minutes/fsb-2024-07-08.pdf, .txt
12. Freedom's annual statement of special education revenues and expenditures (required by RSA 32:11-a) shows $335,801 spent in 2023-24 and $410,670 in 2024-25 (up 22%, **derived**), with $1,723 of Medicaid revenue in 2023-24 and no revenue in 2024-25.
   - citation: FY2025 Annual Report, "Statement of Revenues and Expenditures for Special Education Pupil Services Filed in Accordance with RSA 32:11-a," p. 73
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "Special Education Program (Function 1210) $214,652 $333,470; Psychological Services $21,805 $10,440; Speech Pathology and Audiology $29,024 $11,992; Occupational/Physical Therapy $22,943 $23,715; Transportation (Function 2722) $47,377 $31,052; TOTAL EXPENDITURES: $335,801 $410,670". By function, special education is $391,882.55 of the 2026-27 budget (p. 46), about 9.6% (**derived**). Raw: raw/money/annual-report/ar-fy2025-p75.png, ar-fy2025-p48.png
13. Freedom budgets out-of-district special education tuition on its own line: $5,685 was spent in 2024-25, and $100,000 is budgeted for 2026-27 and again in the 2027-28 working budget; in March 2023 a board member told voters "we have seen substantial out-of-district placement costs of up to $250,000."
   - citation: Freedom School Board packet, November 9, 2026, 2027-2028 Working Budget, account 01.1210.560.109, p. 55; FY2023 Annual Report, Annual Meeting Minutes, March 13, 2023, Article 4
   - source: https://drive.google.com/file/d/1iFpMO1L26C15tON_U4qwap535mmTnfpO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Row text: "01.1210.560.109 OUT OF DISTRICT TUITION $5,685 $0 $100,000 $100,000". 2023 text: "There was an increase in the age requirement that the school is responsible for: up to 22 years old. Also, we have seen substantial out-of-district placement costs of up to $250,000." The 2025-26 column of the working budget is incomplete and not used. Raw: raw/money/packets/fsb-packet-2026-11-09.txt (page 55); raw/money/annual-report/freedom-ar-fy2023.ocr.txt (page 17)
14. Freedom keeps a Special Education Capital Reserve Fund to absorb sudden placement costs; its balance was $377,733.47 on January 31, 2026, above its $350,000 goal ("Goal Met"), and no deposit was asked of voters in 2026.
   - citation: FY2025 Annual Report, "Capital Reserve Fund Balances and Goals," p. 4
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "Special Education $350,000.00 $360,354.88 $17,378.59 $0.00 $377,733.47 ... N/A Goal Met". Voters added up to $50,000 from surplus in March 2023 (raw/money/annual-report/freedom-ar-fy2023.ocr.txt). The historical balance was $100,623.51 at the end of 2018-19. See table freedom_capital_reserves. Raw: raw/money/annual-report/ar-fy2025-rot-p6.png
15. Freedom's 2026 budget form (MS-26) shows $0 of state Special Education Aid (account 3230, the "catastrophic aid" under RSA 186-C:18) actually received in FY2025 and estimated for FY2026 and FY2027; under that law the district pays a student's costs up to 3.5 times the state average cost per pupil before state aid begins (library topic money-special-education-aid).
   - citation: Freedom Local School 2026 MS-26, Revenues, p. 6; library topic money-special-education-aid
   - source: https://drive.google.com/file/d/1CO5PM7v08JPNOOOc84OoFoBOicR1PKcw/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: MS-26 text: "3230 Special Education Aid $O $0 $0". The library topic gives the current formula and the FY2029 change to 2.5 times. Freedom has no row in NH DOE's special education aid files for FY2021-FY2026 (site data: special_education_aid), so it claimed no costs over the threshold in those years. Transcribed from image (OCR). Raw: raw/money/financial/freedom-ms26.pdf, .ocr.txt
16. Under both 2003 Conway agreements Freedom pays the full cost of any out-of-district special education placement of its Kennett students, extra in-district services (aides, counseling) beyond the regular program, and "any due process proceedings, attorney fees, awards, out-of-district placements, and compensatory education awards."
   - citation: Conway Tuition Agreement, Grades 9-12 (Freedom), May 2003, Section I; Conway Tuition Agreement, Grades 7-8 (Freedom), Section I
   - source: https://drive.google.com/file/d/1uhhBFeUbQE9oPLnafPj8AtZ4GaKoe4kv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Freedom School District shall bear all the cost of any such special program or facility." The 2021-22 options study estimated $70,000 of special education tuition at Kennett ($50,000 KHS, $20,000 KMS) and $54,879.22 of special transportation (additional-data/raw/districts/batch-7/freedom-middle-high-options-comparisons.txt, pp. 27–29). Scanned; transcribed from image. Raw: raw/money/contracts/contract-9-12-freedom-conway.pdf, .ocr.txt; contract-7-8-freedom-conway.pdf, .ocr.txt

## district-tax-and-state-aid: Freedom's School Tax, Comparisons and State Aid

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. NH DRA's 2025 tax rate calculation for Freedom, printed in the town's 2025 annual report, sets net local school appropriations of $4,409,844: $3,126,192 raised by the local education tax and $1,283,652 of statewide education tax kept by the district, with none sent to the state; the town paid the school district $4,479,385 during 2025.
   - citation: NH DRA, Appropriations and Revenues, Education (Town of Freedom 2025 Annual Report, p. 56); School District Liability, p. 62
   - source: https://townoffreedomnh.gov/wp-content/uploads/2026/02/Freedom-Town-Report-2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Freedom
   - note: Page text: "Net Local School Appropriations $4,409,844 ... Locally Retained State Education Tax ($1,283,652) Net Required Local Education Tax Effort $3,126,192 ... State Education Tax Not Retained $0". The two tax amounts match DRA's and NH DOE's in the site's data (property_tax, Freedom district), which also has the school share of the rate. Transcribed from image (OCR). Raw: raw/money/town/freedom-town-report-2025.ocr.txt (pages 63, 69)
2. Freedom's low school rate reflects its property value per pupil: its equalized valuation ($1,180,099,390 including utilities) is about the same as Madison's ($1,185,297,325), but its pupils (ADM-A 51.26) are fewer than half of Madison's (112.55), and NH DOE's FY2027 aid file puts Freedom's equalized value per pupil at $13,275,459.34, against $5,996,116.53 in Madison, $3,157,437.47 in Tamworth and $1,597,845.22 in Effingham.
   - citation: FY2025 Annual Report, SAU 13 Apportionment for Fiscal Year 2026-2027, p. 80; NH DOE FY2027 Adequacy Aid (October 1, 2026), "EV Per ADM" (library raw/town/adequacy-aid.csv)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Freedom
   - note: Apportionment page: "Freedom $1,180,099,390 51.26 37.94% 15.58% ... Madison $1,185,297,325 112.55 38.11% 34.21%". CSV component ev_per_pupil, FY2027 (October 1, 2026 calculation, not final); the values match the site's database, which has each town's equalized value and pupil counts (adequacy_aid) but not value per pupil. Through the 2021-22 apportionment Freedom's equalized value was under $500 million (p. 80 history: "$495,298,054" for 2021-22). Raw: raw/money/annual-report/ar-fy2025-p82.png; raw/money/state-data/adequacy-aid-freedom-neighbors.csv
3. A rough estimate: Conway tuition ($1,622,119) was 36.1% of Freedom's 2025-26 school budget with warrant articles ($4,487,871.75), so about $1.34 of Freedom's $3.72 school tax rate per $1,000 (local plus state education) went to Kennett tuition in tax year 2025 (**derived**).
   - citation: FY2025 Annual Report, "2026-2027 Proposed Budget by Function" (function 1100 "Regular Education (Only Conway)"), p. 46; NH DRA 2025 tax rate (site data: property_tax)
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Freedom
   - note: Derived and approximate: 1,622,119 ÷ 4,487,871.75 = 36.14%; 0.3614 × 3.72 = $1.34. It assumes every budget line is paid in the same mix of taxes and other revenue (local appropriation was 98.8% of 2026-27 revenue, p. 47). The Conway share was 39.2% in 2023-24, 41.9% in 2024-25 and 36.3% in 2026-27 (**derived**, same method). Tax year 2025 funds the 2025-26 school year. Freedom's rates are in the site's data (property_tax, Freedom district): for 2025, local education $2.63 plus state education $1.09 (checked November 15, 2026). Raw: raw/money/annual-report/ar-fy2025-p48.png, ar-fy2025-p49.png
4. The board's own estimate for the 2026 warrant was that the 2026-27 operating budget would lower Freedom's school tax rate by $0.045 per $1,000 and the warrant articles (mainly the SAU share) would raise it by $0.040, a net change of −$0.005 per $1,000 of assessed value.
   - citation: FY2025 Annual Report, "Freedom School District Calculation of Tax Rate Impact," p. 79
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "Total Net Increase/(Decrease) -$53,519 -$0.045 Proposed Tax Rate Impact per Thousand"; "Total Cumulative Tax Rate Impact -$0.005 per $1K of assessed valuation". It lists "Adequacy $0" among estimated revenues and uses a local assessed value of $1,187,005,513. Raw: raw/money/annual-report/ar-fy2025-p81.png
5. In December 2024 SAU 13's superintendent reported to the Freedom School Board that "Freedom does not receive Adequate Education funding from the State of NH."
   - citation: Freedom School Board Minutes, December 9, 2024, Superintendent's Report
   - source: https://drive.google.com/file/d/1JSH-kp6Spg0-LHWITR5Ey6G6yBLogvuQ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Minutes text: "SUPERINTENDENT'S REPORT ● Waiting on Conway Tution figures ... ● Freedom does not receive Adequate Education funding from the State of NH". NH DOE's calculation in the site's data (adequacy_aid, Freedom district) shows a $0 grant for every year from FY2020 to FY2027 except FY2023 ($293,583, a SWEPT hold harmless payment for that year's one-time statewide tax reduction), and the statewide tax Freedom keeps above its adequacy cost. Raw: raw/money/minutes/fsb-2024-12-09.txt; raw/money/state-data/adequacy-aid-freedom-neighbors.csv
6. Freedom's equalized property value per pupil, about $13.3 million for FY2027, is far above the $1.6 million limit for New Hampshire's fiscal capacity disparity aid, which helps towns with low property value per pupil, so Freedom receives none.
   - citation: NH DOE FY2027 Adequacy Aid (October 1, 2026), "EV Per ADM" and fiscal capacity disparity aid columns; library topic money-adequacy-aid-amounts
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Freedom
   - note: CSV rows "ev_per_pupil 13275459.34" and "fiscal_capacity_disparity_aid 0" (Freedom, FY2027). The $1.6 million threshold is from the library topic and the Jackson file (district-tax-and-state-aid 6 in `Jackson/money-and-governance.md`). The aid paid to Freedom and its neighbors (Madison and Tamworth $0, Effingham $1,013.51 for FY2027) is in the site's data (adequacy_aid). Raw: raw/money/state-data/adequacy-aid-freedom-neighbors.csv
7. Because Conway's tuition formula and SAU 13's cost split both use equalized property value, Freedom's high value raises its shares of those costs: in 2026-27 Freedom has 15.58% of SAU 13's pupils but pays 26.76% of the SAU budget, and 4.87% of Kennett High's attendance but 11.05% of the eight towns' property value in the high school formula.
   - citation: FY2025 Annual Report, SAU 13 Apportionment, p. 80; "2026-2027 Tuition Contracts" calculation sheet, p. 41
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: SAU 13 splits its budget half by ADM-A and half by equalized value; the Kennett contract weights value 35%. The sheet's middle school columns show Freedom with 6.06% of attendance and 17.89% of value. Raw: raw/money/annual-report/ar-fy2025-p82.png, ar-fy2025-rot-p43.png, ar-fy2025-rot-p44.png

## district-tuition-contracts: Freedom's Kennett Contracts, Their End and the Search for New Ones

- kind: local
- question_type: governance_money
- description: A district's tuition contracts and agreements with other districts and schools: terms, cost formulas, caps, length, renewal, transportation and special education

1. Freedom's current Kennett contracts are two Conway "withdrawal" tuition agreements signed in 2003 (grades 9–12 and grades 7–8), approved by the State Board of Education in May 2003, which require Freedom to send at least 90% of its pupils in those grades to Conway and make Freedom "responsible for the transportation methods and expenses."
   - citation: Conway Tuition Agreement, Grades 9-12 (Freedom), May 2003, Sections I and XIV; Conway Tuition Agreement, Grades 7-8 (Freedom), Section I
   - source: https://drive.google.com/file/d/1uhhBFeUbQE9oPLnafPj8AtZ4GaKoe4kv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Freedom School District shall send at least ninety percent (90%) of its pupils, grades 9 through 12, with the exceptions hereinafter noted, to Conway for schooling; and Freedom School District shall be responsible for the transportation methods and expenses". The grades 7–8 agreement uses the same words for grades 7 and 8. Both are linked from SAU 9's Tuition Agreement Overview page (https://www.sau9.org/tuitions), which lists no 2027 contract for Freedom. Scanned; transcribed from image. Raw: raw/money/contracts/contract-9-12-freedom-conway.pdf, .ocr.txt; contract-7-8-freedom-conway.pdf, .ocr.txt
2. Under the 2003 agreements Conway sets Freedom's charge each year from Conway's current approved budget plus the Northeast urban CPI plus 2.5%, plus or minus the prior year's actual costs, and Freedom's share is 35% its share of the sending towns' equalized property value and 65% its share of average daily membership in attendance; Conway must give the estimate by November 30.
   - citation: Conway Tuition Agreement, Grades 9-12 (Freedom), Section X.A.2–4
   - source: https://drive.google.com/file/d/1uhhBFeUbQE9oPLnafPj8AtZ4GaKoe4kv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Each district's percentage of the operating expenses of the high school ... shall be a combination of 35% of the town's equalized value as a percentage of the total equalized value and 65% of the town's average daily membership in attendance". Bond payments are split by equalized value alone (X.B.1), and each town pays its value share of a Facilities Maintenance Fund of 3% of construction cost divided by 20 (X.D). The Conway file (district-tuition-contracts 3–4) shows the same formula from Conway's side. Raw: raw/money/contracts/contract-9-12-freedom-conway.ocr.txt
3. The 2003 agreements ran a minimum of 20 school years from 2006-07 and then continue year to year until either side gives notice naming a last year at least the third full fiscal year after notice; the Freedom School Board voted unanimously on February 12, 2024 "to give notice to exit current Kennett Middle and High School Contracts," and 2026-27 is their last year.
   - citation: Conway Tuition Agreement, Grades 9-12 (Freedom), Sections II–III; Freedom School Board Minutes, February 12, 2024; FY2025 Annual Report, Annual Meeting Minutes, March 10, 2025
   - source: https://drive.google.com/file/d/13Z2-_fbDJQ1EjUGWj4ZlPPLjEx5p6ZSu/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Minutes: "Intent to notify Conway is due by June 2024 ... VOTE: Motion by Sarah Groleau to give notice to exit current Kennett Middle and High School Contracts, seconded by Jake Stephan. The motion passed unanimously." March 2025: "2026-27 is the last year of the current contract. 2027-28 is the first year of the new contract." The options study says "The current tuition agreement is due to expire in 2027 with notification to exit the agreement in 2024." Raw: raw/money/minutes/fsb-2024-02-12.pdf, .txt; raw/money/annual-report/freedom-ar-fy2025.ocr.txt (page 16)
4. In Conway's 2026-27 calculation Freedom had 30.28 of Kennett High's 622.21 attending pupils (4.87%) but 11.05% of the eight towns' equalized value, giving it about 7.03% of Conway's $14,751,561 high school budget (**derived**); at Kennett Middle it had 13.49 of 222.7 pupils (6.06%) and 17.89% of the five towns' value, and the sheet shows $46,971.29 per Freedom middle schooler against $24,740.84 for Conway's own.
   - citation: FY2025 Annual Report, "2026-2027 Tuition Contracts" calculation sheet, pp. 41–42
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Sheet (rotated, viewed): "HIGH/VOC OPERATIONS ... Freedom ... 11.05% ... 30.28 ... 4.87% ... Plus Conway 25-26 Approved Bdgt. ... $1,037,227 ... HIGH/VOC. OPERATIONS TOTAL ... $1,132,981"; middle school row "$24,740.84 $17,837.85 $24,867.07 $46,971.29 $30,063.24" (Conway, Eaton, Albany, Freedom, Madison). Derived: 0.35 × 11.05 + 0.65 × 4.87 = 7.03%, matching 1,037,227 ÷ 14,751,561. Bond lines are $0 for 2026-27. Raw: raw/money/annual-report/ar-fy2025-rot-p43.png, ar-fy2025-rot-p44.png
5. Freedom's 2026-27 payment schedule to Conway totals $1,629,835 in four quarterly payments of $407,459 (high school operations $247,978, high school facilities fund $1,504, middle school operations $157,213 and middle school facilities fund $764), with no bond payments; this matches the budget's Conway tuition lines.
   - citation: FY2025 Annual Report, "Payment Schedule for 2026-2027 Tuition Contract - Pay to Conway School District," p. 43
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "TOTAL FOR THE FISCAL YEAR $1,629,835". Budget lines: middle school $631,908, high school $997,927 (sum $1,629,835). The calculation sheet's "TOTAL DUE" row shows $1,772,640 for Freedom; the documents do not explain the $142,805 difference (mostly in high school operations). The Conway contract says late payments carry 1% over prime. Raw: raw/money/annual-report/ar-fy2025-p45.png, ar-fy2025-rot-p44.png
6. Per-student Conway charges swing widely: the board told voters in March 2025 that 2024-25 was budgeted at $57,720 per middle school student and $25,378 per high school student, and 2025-26 at $35,732 and $27,893; in December 2024 the board said Conway's cost for its own students was about $17,000 and called the agreement "the only contract the State of New Hampshire that is not a per student tuition rate."
   - citation: FY2025 Annual Report, Annual Meeting Minutes, March 10, 2025, Article 1; Freedom School Board Minutes, December 9, 2024
   - source: https://drive.google.com/file/d/1JSH-kp6Spg0-LHWITR5Ey6G6yBLogvuQ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Meeting text: "The 2024-25 budgeted amounts are $57,720 per student for the middle school; $25,378 per student for the high school. The budget for next year is $35,732 for the middle school, $27,893 for the high school." December 2024: "SAU9 / Conway agreement is 20 years old, and seems to be the only contract the State of New Hampshire that is not a per student tuition rate ○ Conway's cost for their own students is $17,000 per student" (board's statement, not verified). The March 10, 2025 board minutes give $57,750 for 2024-25 middle school. The district's own per-pupil figures are in table freedom_cost_per_pupil_by_level. Raw: raw/money/minutes/fsb-2024-12-09.pdf, .txt; raw/money/annual-report/freedom-ar-fy2025.ocr.txt (page 16)
7. In December 2024 Freedom's board recorded that Conway's 2025-26 tuition figures, due under the contract by November 30, 2024, arrived "almost two weeks late," called this a "Breach of contract," and asked SAU 9 for the number of students using VLACS classes and for address and residency checks.
   - citation: Freedom School Board Minutes, December 9, 2024; January 13, 2025
   - source: https://drive.google.com/file/d/1JSH-kp6Spg0-LHWITR5Ey6G6yBLogvuQ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Conway Tuition numbers for 2025-26 school year were due on November 30, 2024; almost two weeks late; Conway not honoring their own contract"; "Breach of contract for not providing numbers by November 30, 2024". These are the Freedom board's statements. Raw: raw/money/minutes/fsb-2024-12-09.pdf, .txt; fsb-2025-01-13.pdf, .txt
8. Freedom's stated goals for a new Kennett contract were to remove equalized value from the formula and pay a per-student tuition (October 2024), and in March 2025 the chair told voters Conway was "attempting to negotiate with each town individually," SAU 13 was negotiating as one SAU, and "The 90% rule is not being universally enforced, which has an impact on what we are paying."
   - citation: Freedom School Board Minutes, October 21, 2024 (Freedom Select Board); FY2025 Annual Report, Annual Meeting Minutes, March 10, 2025, Article 5
   - source: https://drive.google.com/file/d/1BgYXaeW2k-zGNbz_l4yMcJom6tW5vgCj/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: October 2024: "Freedom School Board would like to remove equalized valuation as a component of the tuition formula ○ Freedom School Board wants a per student tuition cost". March 2025: "our goal is to see a contract with less or no emphasis on valuation, but to be based upon tuition only." Raw: raw/money/minutes/fsb-2024-10-21.pdf, .txt; raw/money/annual-report/freedom-ar-fy2025.ocr.txt (page 18)
9. Conway's tuition committee chair summarized Conway's offer to Freedom on January 29, 2026: a 5-year contract requiring at least 75% of Freedom's grade 9–12 pupils (with homeschool, charter, EFA, open enrollment and manifest-hardship students excepted), base tuition from Conway's DOE-25 current expenditures minus maintenance-trust and billable special education costs, plus inflation and 2.5% capped at 8% combined, plus one-fifth of a 5-year Kennett capital plan by attendance share (about 4.8% for Freedom).
   - citation: Letter, Conway School Board Tuition Committee Chair to the Freedom School Board, January 29, 2026 (Freedom School Board packet, February 9, 2026, pp. 87–88)
   - source: https://drive.google.com/file/d/1PHqe8g14fSrfyKmwz4YTqiqBMbPBTIOL/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "For a 5-year contract term, Freedom shall send at least seventy-five percent (75%) of its pupils, grades 9 through 12, to Conway"; "an inflation factor plus 2.5% shall be added, with these two additions not exceeding a cumulative 8%"; "Each sending district shall annually pay 1/5th of the projected 5-year CIP plan ... (Based on last year's enrollment, this would be about 4.8% of the total enrollment)." The letter says Freedom's chair proposed "a straight cost-per-pupil calculation, with no attendance requirement and no support for building maintenance" as a "line in the sand." These terms match Conway's 2027 contracts with Albany, Bartlett and Eaton (Conway file district-tuition-contracts 5–6). Raw: raw/money/packets/fsb-packet-2026-02-09.pdf, .txt (pages 87–88)
10. On February 9, 2026 the Freedom School Board "unanimously decided to pause negotiations with Conway and focus instead on Freyburg, GWRSD and Tamworth," saying it would revisit Conway after Conway addressed comments a Conway board member made to the media and gave more information on its maintenance cost proposal.
   - citation: Freedom School Board Minutes, February 9, 2026 (public hearing and action after non-public session)
   - source: https://drive.google.com/file/d/1ghgf5l2NjRs-TepzzolJLNVpZz-V86pJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "The Board unanimously decided to pause negotiations with Conway and focus instead on Freyburg, GWRSD and Tamworth. It is the intent to revisit Conway once they have addressed our previous concerns and we have a chance to get more information about the maintenance cost proposal." ("Freyburg" as written.) Conway's board removed that member from its negotiating committee in April 2026 (Conway file district-tuition-contracts 8). By July 2026 Freedom reported weekly follow-ups to Conway "regarding negotiations" (raw/money/minutes/fsb-2026-07-13-draft.txt). Raw: raw/money/minutes/fsb-2026-02-09.pdf, .txt
11. In September 2026 the Conway School Board adopted a revised policy JFAB that charges tuition students from districts without a contract (beyond the open-enrollment limits voters set) the current expenditure per pupil for the same year plus a 25% premium "to cover administrative costs."
   - citation: Conway School Board Minutes, September 14, 2026 (amended), policy JFAB first reading, and September 28, 2026, final reading (6-0-0)
   - source: https://www.sau9.org/conway
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Mosca noted a change, adding a 25% premium on top of the current expenditure per pupil for the same fiscal year to cover administrative costs. Davison said by making changes to this policy, Conway will not have to continually go to the table regarding some of the tuition contracts." Under open enrollment, non-contracted towns' students "will pay 80% of their DOE-25." Raw copies are in the Conway research: town/Conway/raw/daily/minutes/26-9-September-14-2026-Amended.txt, 26-9-September-28-2026.txt
12. At its October 19, 2026 meeting the Freedom School Board listed a tuition negotiations timeline with Governor Wentworth Regional, Moultonborough, Fryeburg and Conway; board members said Conway's no-contract rate would be about $66,200 per Freedom student while "Other contract offers are in the $25-26,000 per student range," and the Selectboard cited a Governor Wentworth cost of $26,293.
   - citation: Freedom School Board Minutes (draft), October 19, 2026, Chairperson's Report, Public Comment and Freedom Select Board items
   - source: https://drive.google.com/file/d/1WY2dKYkIP6ZSi5N8YwrbRf9pG3pEyuA0/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Tuition Negotiations Timeline - Governor Wentworth Regional, Moultonboro, Fryeburg, Conway"; "Conway passed a tuition policy that if there is not a contract in place, the charge to attend Conway schools is 125% of the sending district cost per student, which is approximately $66,200 per student for the Freedom School District. ○ Other contract offers are in the $25-26,000 per student range"; "Governor Wentworth recent cost of $26,293". The $66,200 is the board's estimate. The board also said "they have been working on this for 7 years" and that "There is a legal expectation not to disclose information during the negotiation process." The 2027-28 working budget carries Kennett tuition as a placeholder ($495,000 middle, $770,000 high) plus $55,000 each for Governor Wentworth middle and high school (packet p. 52). Draft minutes. Raw: raw/money/minutes/fsb-2026-10-19-draft.pdf, .txt; raw/money/packets/fsb-packet-2026-11-09-p52.png
13. Neither 2003 Conway agreement mentions summer school, credit recovery or dual (college) enrollment; the charge is built from Kennett's General Fund costs as reported on the DOE-25, and in the student discipline section the "costs of any alternative educational programs beyond the standard program offered at the high school shall be borne by the Freedom School District."
   - citation: Conway Tuition Agreement, Grades 9-12 (Freedom), Sections VII and X.A.1
   - source: https://drive.google.com/file/d/1uhhBFeUbQE9oPLnafPj8AtZ4GaKoe4kv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Searched the contract text for "summer", "credit" and "dual"; none found. "Actual expenses shall refer to high school General Fund expenses as reported in the DOE-25 ... plus student activities cost". A statement about the document read, not a legal interpretation. Raw: raw/money/contracts/contract-9-12-freedom-conway.ocr.txt
14. No Kennett summer school or summer credit-recovery program was found (SAU 9 research), and Conway policy IGBK makes college course tuition the student's responsibility unless the board agrees to pay; no Freedom School Board vote on paying dual or concurrent enrollment costs was found in its 2022–2026 minutes.
   - citation: town/sau9/kennett-pathways.md, school-programs-after-grade-6 fact 32; town/Jackson/after-jackson-grammar.md (school-programs-after-grade-6 16 in `Jackson/after-jackson-grammar.md`); Freedom School Board minutes, August 2022 – October 2026
   - source: https://www.sau13.org/school-board/freedom/agendas-packets-minutes
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: A statement about the documents searched (raw/money/minutes/). The only related Freedom item: in December 2024 the board asked Conway for "number of students utilizing VLACS (Virtual Learning Academy Charter School) classes" while reviewing tuition (fsb-2024-12-09.txt). Dual-enrollment funding rules are in the library topic students-hb-1202-dual-enrollment-funding.
15. Freedom has had a separate agreement with the Governor Wentworth Regional School District (Kingswood) since 2024: its board approved Freedom rates of $21,335 for middle school and $22,861 for high school in May 2024, Freedom students could start that fall (up to 10% under the Conway contract) and finish there, and on August 11, 2025 Freedom's board approved an agreement priced at Governor Wentworth's per-pupil cost.
   - citation: Freedom School Board Minutes, May 13, 2024 (GWRSD Tuition Update); August 11, 2025
   - source: https://drive.google.com/file/d/19f2vQOm7NoYo-1WfdO4B8cw8wengG7CG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: 2024 text: "GWRSD Board approved Freedom student tuition rates of: $21,335 Middle School $22,861 High School ● Students may begin attending in Fall of 2024 ○ up to 10% of students may attend under current Conway contract ... Freedom students who attend GWRSD will be able to finish their educational careers in that district". 2025 text: "Discussion on extending the agreement for five years ● Price per pupil is the tuition rate ... Approximately $21,000 for the 2024-2025 school year VOTE: Motion by Jake Stephan to approve the Governor Wentworth Regional School District Agreement ... passed unanimously." The agreement itself was not posted. Raw: raw/money/minutes/fsb-2024-05-13.pdf, .txt; fsb-2025-08-11.pdf, .txt
16. For 2024-25 the board reported Governor Wentworth tuition of $23,227 (middle) and $22,995 (high) against Conway's $57,750 and $25,378; in September 2025 the board authorized up to $200,000 from the Tuition Stabilization Reserve Fund to pay Governor Wentworth's 2025-26 invoice, when three or four Freedom students were attending, and by October 1, 2026 six were (four at Kingswood Middle, two at Kingswood High).
   - citation: Freedom School Board Minutes (draft), March 10, 2025; September 15, 2025; Freedom School Board packet, November 9, 2026, BOY Enrollment, p. 43
   - source: https://drive.google.com/file/d/1JjtELlnAoT5rvld01MhRx2uHPshWqo_q/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: March 2025 text: "Middle School: Conway/Kennett $57,750 Gov Wentworth $23,227 High School: Conway/Kennett $25,378 Gov Wentworth $22,995". September 2025: "VOTE: Motion by Sarah Groleau to authorize up to $200,000 from the Tuition Stabilization Reserve Fund to pay the Governor Wentworth Regional School District (GWRSD) invoice for 2025-2026 tuition ... passed 3-0-1". Freedom paid both districts for one student in 2024-25 because the move was not formally approved (June 9, 2025 minutes). Raw: raw/money/minutes/fsb-2025-03-10-draft.txt, fsb-2025-09-15.txt, fsb-2025-06-09.txt; raw/money/packets/fsb-packet-2026-11-09-p43.png

## high-school-tuition-options: Middle and High School Options for Freedom Students

- kind: local
- question_type: local_practice
- description: High school options for districts without a high school (already in `additional-data/district-practices.md`)

1. Freedom's administration compared six middle and high school options for the board using 2021-22 data, stressing that "any projected costs are very rough and preliminary": base tuition of $27,497 at Kennett High ($42,366 at Kennett Middle), $16,532 at Moultonborough Academy, $22,500 at Kingswood, $18,200 at Fryeburg Academy, $27,909 at Inter-Lakes and $15,367 at Sacopee Valley, at distances from Freedom of 9.6 miles (Sacopee Valley) to 35.4 miles (Inter-Lakes).
   - citation: Freedom School District, "High School Options Preliminary Comparisons," pp. 2, 11, 25
   - source: https://www.freedomelschool.com
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "It is very important to note that we have not entered into any formal agreements or negotiations with these schools." Distances: Kennett 18.7, Moultonborough 23.8, Kingswood 23.9, Fryeburg 22.2, Inter-Lakes 35.4, Sacopee Valley 9.6 miles. The study is undated; in November 2022 the board chair recommended focusing on "Gov. Wentworth, Kennett, Freyburg, and possibly Sacopee" and called Moultonborough and Inter-Lakes "outliers" (raw/money/minutes/fsb-2022-11-14.txt). The April 2024 hearing said the 31-page report was posted under "Middle / High School Options" on the school website. Raw copy in the library: additional-data/raw/districts/batch-7/freedom-middle-high-options-comparisons.pdf, .txt
2. As of November 13, 2026 Freedom students had no tuitioned path to Fryeburg Academy: in February 2026 the board said it was "in negotiations with Freyburg Academy for a high school option" and awaiting a proposal, and in September 2026 it said Fryeburg (like Governor Wentworth) offers the "average price per pupil" but "does not offer options for 7th and 8th grade."
   - citation: Freedom School Board Minutes, February 9, 2026 (public hearing); Freedom School Board Minutes (draft), September 16, 2026 (Freedom Select Board)
   - source: https://drive.google.com/file/d/1ghgf5l2NjRs-TepzzolJLNVpZz-V86pJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: February text: "School Board is also in negotiations with Freyburg Academy for a high school option"; "Freyburg Academy – Mike is awaiting a proposal from the Academy". September text: "Fryeburg and Governor Wentworth Regional School District (GWRSD) ○ Both offer cost of average price per pupil ○ Fryeburg does not offer options for 7th and 8th grade". In April 2024 the superintendent said "there are challenges with a public / private partnership such as Fryeburg. Distance is also a factor" (fsb-2024-04-08.txt). Families may still enroll and pay privately (town/maine/fryeburg-academy.md). Raw: raw/money/minutes/fsb-2026-02-09.txt, fsb-2026-09-16-draft.txt
3. New Hampshire law lets a district without a high school contract with an academy or high school in another state when distance or transportation makes it necessary, and a State-Board-approved contract school counts as a high school the district maintains (library topic gov-tuition-towns); Jackson signed such an agreement with Fryeburg Academy starting 2027-28 (Jackson file district-tuition-contracts 13–20 in `Jackson/money-and-governance.md`).
   - citation: library topic gov-tuition-towns, fact 3 (RSA 194:22); town/Jackson/money-and-governance.md, district-tuition-contracts 13–20 in `Jackson/money-and-governance.md`
   - source: https://gc.nh.gov/rsa/html/XV/194/194-22.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Freedom
   - note: Pointer only. Whether a Freedom–Fryeburg contract would need State Board approval or a district vote was not stated in Freedom's documents; in September 2026 the chair said "there are many different legal opinions" on how the school of record will be decided (fsb-2026-09-16-draft.txt).
4. Freedom has also looked at middle school in Tamworth (K. A. Brett School): in June 2025 the board authorized the SAU "to look into Freedom students attending the KA Brett School for middle school," and in February 2026 it reported "Early exploration of options at Tamworth Middle School"; in September 2026 it said Sacopee Valley schools "are rather full with limited capacity to receive students."
   - citation: Freedom School Board Minutes, June 9, 2025; February 9, 2026; September 16, 2026 (draft)
   - source: https://drive.google.com/file/d/1ApiK158T28EeLJaap9USbzYlnZ-YF6iX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: In November 2022 the superintendent said Tamworth "would be willing to consider" middle school for Freedom students, and a board member opposed it (fsb-2022-11-14.txt). No Tamworth agreement was found. Raw: raw/money/minutes/fsb-2025-06-09.txt, fsb-2026-02-09.txt, fsb-2026-09-16-draft.txt
5. On October 1, 2026 Freedom's resident students in grades 7–12 were at Kennett Middle (14), Kennett High (25), Kingswood Middle (4) and Kingswood High (2), with others at charter schools, VLACS or using Education Freedom Accounts; in June 2026 the principal reported that of 11 sixth graders, 8 would attend Kennett Middle, 2 Kingswood Middle and 1 a charter school.
   - citation: Freedom School Board packet, November 9, 2026, "Freedom Elementary School BOY Enrollment as of 10/01/2026," p. 43; Freedom School Board Minutes, June 8, 2026
   - source: https://drive.google.com/file/d/1iFpMO1L26C15tON_U4qwap535mmTnfpO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "A. Crosby Kennett Middle School ... 8 6 ... 14"; "Kennett High School 6 6 6 7 25"; "Kingswood Regional Middle School ... 3 1 ... 4"; "Kingswood Regional High School ... 1 0 1 2". June 2026: "2 students will attend Kingswood Middle School ... 1 student will attend Breakthrough Academy Charter School ... 8 students will attend Kennett Middle School"; "Current and projected enrollment is under 10% of Freedom students." Governor Wentworth asked families of 6th graders to decide by March 2027 (fsb-2026-07-13-draft.txt). Raw: raw/money/packets/fsb-packet-2026-11-09-p43.png; raw/money/minutes/fsb-2026-06-08.txt

## district-facilities-and-capital: Freedom Elementary's Building, Capital Plan and Reserves

- kind: local
- question_type: governance_money
- description: A district's school buildings: age, planned repairs, capital reserve funds, bonds and energy projects

1. Freedom's capital plan (updated February 2, 2026) schedules capital reserve withdrawals of $15,951.61 in FY2027, $0 in FY2028, $16,430.16 in FY2029, $0 in FY2030 and $16,923.06 in FY2031 (driveway sealing each time), about $49,300 over the next five years (**derived**); larger items fall later, with $49,473.96 in FY2032 and $227,968.66 in FY2034.
   - citation: FY2025 Annual Report, "Freedom School District Capital Investment Plan," p. 7
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed (rotated): "CRF Withdrawal 35,500.00 15,951.61 - 16,430.16 - 16,923.06 49,473.96 17,430.76 227,968.66 82,225.49" (FY2026–FY2035). Derived: 15,951.61 + 16,430.16 + 16,923.06 = 49,304.83. The November 2026 board packet's summary shows the same plan as "Years 1–5 Anticipated Costs $15,487" and "Years 1–10 $429,086" (packet p. 42). See table freedom_cip_withdrawals. Raw: raw/money/annual-report/ar-fy2025-rot-p9.png; raw/money/packets/fsb-packet-2026-11-09-p42.png
2. The flat roof over the lobby and offices was replaced in summer 2025 for $35,500 from the building reserve (board vote June 9, 2025, bid from Melanson); the three pitched roof sections were replaced in 2016–2018 ($39,870 central over grades 1–3 and library, $34,000 west over grades 4–6 and art, $45,800 east over the gym, kindergarten and garage) and are next due in 2036–2038.
   - citation: FY2025 Annual Report, Capital Reserve Fund Balances and Goals, p. 4, and Capital Investment Plan, p. 7; Freedom School Board Minutes, June 9, 2025
   - source: https://drive.google.com/file/d/1ApiK158T28EeLJaap9USbzYlnZ-YF6iX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Reserve page note: "Flat Roof over Administration Replaced Summer 2025". Minutes: "VOTE: Motion by Todd Giles to accept the bid from Melanson ... VOTE: Motion by Jake Stephan to withdraw up to $35,500 from the Building Maintenance Capital Reserve Fund". Raw: raw/money/annual-report/ar-fy2025-rot-p6.png, ar-fy2025-rot-p9.png; raw/money/minutes/fsb-2025-06-09.pdf, .txt
3. Two of Freedom Elementary's four boilers (HB Smith) were replaced in FY2024 for $76,000 each, with 20-year lives; the two Peerless boilers from 2014 are due in FY2034 at an estimated $108,729.85 each, the plan's largest near-term items, and the HVAC controls (2015) are due in FY2035 at $63,524.25.
   - citation: FY2025 Annual Report, Capital Investment Plan, p. 7
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Row text: "Boiler #3 (Peerless) 2014 $ 16,162.00 Increased Estimate 20 2034 $ 108,729.85"; "Boiler #4 (Peerless) 2014 $ 16,162.00 based on 1 & 2 20 2034 $ 108,729.85". The building heats with oil (two 1,000-gallon underground tanks installed 2021 for $96,578; fuel oil budgeted at $26,000 with Irving at $2.61 a gallon for FY26, packet p. 63). Raw: raw/money/annual-report/ar-fy2025-rot-p9.png; raw/money/packets/fsb-packet-2026-11-09.txt
4. The capital plan carries one deferred item: window replacement in "Add. 2" (installed 2002 for $37,000, replacement due 2022, estimated $54,980.05), and it lists air conditioning mini-splits for 2026 as "Researching"; in March 2025 the business administrator said the planned 2025 withdrawals were mainly "replacement of windows for about $54,000, and adding mini-splits for air conditioning."
   - citation: FY2025 Annual Report, Capital Investment Plan, p. 7 (legend "Deferred Maintenance from Prior Year(s)"); Annual Meeting Minutes, March 10, 2025, Article 3
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Row text: "Window Replacement- Add. 2 2002 $ 37,000.00 Portland Glass 20 2022 $ 54,980.05" (highlighted as deferred). The November 2026 packet version lists the same windows with a 2027 date and $60,702.42 (p. 42). Other recent projects: playground 2023 ($145,000), driveway 2023 ($88,320), gym floor 2023 ($61,400), windows "Add. 1" 2024 ($56,000), fire alarm 2024, lighting 2024, shades 2025. Raw: raw/money/annual-report/ar-fy2025-rot-p9.png; raw/money/packets/fsb-packet-2026-11-09-p42.png
5. The Building Maintenance Capital Reserve Fund held $313,380.36 on January 31, 2026, after a $90,146 deposit voted in 2025 and the $35,500 roof withdrawal; the 2026 warrant asked voters to add up to $50,000 from June 30, 2026 surplus with no new taxation, and the capital plan proposes $80,000 a year from FY2027 to FY2035.
   - citation: FY2025 Annual Report, Capital Reserve Fund Balances and Goals, p. 4; Capital Investment Plan, p. 7; 2026 Warrant, Article 4
   - source: https://drive.google.com/file/d/1kq41YFzDYJxLCMPHgJApy9HjdE0gsZxA/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Warrant text: "raise and appropriate up to $50,000 to be added to the Building Maintenance Capital Reserve Fund previously established. This sum to come from the June 30, 2026 unassigned fund balance ... No amount is to be raised from additional taxation." In January 2026 the board "discussed funding amounts as recommended in the Capital Improvement Plan (CIP) vs projects completed over the last year from fund balance. Board approved $50,000" (fsb-2026-01-12.txt). Raw: raw/money/annual-report/ar-fy2025-rot-p6.png; raw/money/financial/freedom-warrant.ocr.txt
6. Freedom's five capital reserve and trust funds held $1,197,375.24 on January 31, 2026: special education $377,733.47, building maintenance $313,380.36, tuition stabilization (expendable trust) $303,022.09, school bus $178,025.53 and technology $25,213.79.
   - citation: FY2025 Annual Report, Capital Reserve Fund Balances and Goals, p. 4; Freedom School Board packet, November 9, 2026, p. 41
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page text: "Capital Reserve Fund Totals $1,110,791.07 $141,757.99 -$8,541.82 $1,244,007.24 $125,146.00 -$171,778.00 $1,197,375.24". The November 2026 packet shows the same balances "as of 6/30/2026" plus the $50,000 building deposit ($1,247,375.24 at 6/30/2027), excluding interest. The district has no bonded debt (MS-26 debt service $0). See table freedom_capital_reserves. Raw: raw/money/annual-report/ar-fy2025-rot-p6.png; raw/money/packets/fsb-packet-2026-11-09-p41.png
7. Freedom explored adding a kitchen to Freedom Elementary with HL Turner Group in 2023 but decided in February 2024 not to continue, and its March 2026 report lists "Continued cost-benefit analysis of a kitchen at Freedom Elementary School" as a priority; meals are bought under a vended meal contract with the Madison School District.
   - citation: Freedom School Board Minutes, February 12, 2024 (FY2025 budget public hearing); Freedom School Board Report, March 2026 (FY2025 Annual Report, p. 21); Minutes, June 9, 2025
   - source: https://drive.google.com/file/d/13Z2-_fbDJQ1EjUGWj4ZlPPLjEx5p6ZSu/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: February 2024 text: "Not continuing with Kitchen Project exploration". June 2025: "VOTE: Motion by Todd Giles to renew the vended meal contract with the Madison School District". Raw: raw/money/minutes/fsb-2024-02-12.txt, fsb-2025-06-09.txt; raw/money/annual-report/freedom-ar-fy2025.ocr.txt (page 23)

## district-transportation: Freedom's Own Buses and What Transportation Costs

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. The Freedom School District owns its school buses and employs its own drivers, including a lead bus driver; the board noted in September 2024 that "Freedom is in a unique situation with owning its own busses and handling student transportation in house," and the 2003 Conway agreements make Freedom responsible for getting its grade 7–12 students to Conway.
   - citation: Freedom School Board Minutes, September 16, 2024 (Drive file labeled September 6) (Transportation); Conway Tuition Agreement, Grades 9-12 (Freedom), Section I
   - source: https://drive.google.com/file/d/1676w4iIBYWHLPgGr5Vf96ho5NQU-K9V0/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: The 2027-28 working budget lists wages for two bus drivers and a lead bus driver stipend (packet p. 67). In June 2024 the afternoon plan was "1 bus to the Middle School ● 1 bus to the High School ● meet at the 4 corners" (fsb-2024-06-10.txt). Routes and times are in the Freedom daily-life research. Raw: raw/money/minutes/fsb-2024-09-06.pdf, .txt; raw/money/packets/fsb-packet-2026-11-09-p67.png
2. Freedom's fleet as of January 12, 2026 was five buses: a 72-passenger 2022 Freightliner (spare, 56,426 miles), a 42-passenger 2019 Freightliner (bus 5, 175,521 miles, voted surplus December 8, 2025), a 42-passenger 2021 Freightliner (110,279 miles), a 14-passenger 2023 Chevrolet with wheelchair access (28,578 miles) and a new 48-passenger 2026 Freightliner with a wheelchair lift (7,173 miles).
   - citation: FY2025 Annual Report, "Freedom School Bus Assessment/Replacement Schedule (as of 1/12/26)," p. 6
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed (rotated). The schedule assumes a 7-year replacement cycle; the next planned purchase is bus 7 in FY2028 at about $115,000, marked "Pending Review", and there was "No Bus Article on 2026 Warrant." In March 2025 the chair said of one aging bus, "We are not planning on replacing that bus when it ages out. We will reduce our fleet" (freedom-ar-fy2025.ocr.txt, page 18). In October 2024 the board discussed "Right-sizing of bus fleet; having own bus fleets offers pros and cons" (fsb-2024-10-21.txt). Raw: raw/money/annual-report/ar-fy2025-rot-p8.png
3. The School Bus Capital Reserve Fund paid $136,278 for the new 48-passenger lift bus in 2025-26, leaving $178,025.53 on January 31, 2026; voters had added $35,000 from surplus in each of 2024 and 2025.
   - citation: FY2025 Annual Report, Capital Reserve Fund Balances and Goals, p. 4, and Bus Replacement Schedule, p. 6
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page text: "School Bus Per schedule $232,144.58 $47,158.95 $0.00 $279,303.53 $35,000.00 -$136,278.00 $178,025.53 ... Replaced Bus #5 with a 48 Passenger Bus w/ Wheelchair Lift". In January 2026 the board voted to remove a bus reserve article from the 2026 warrant (fsb-2026-01-12.txt). Raw: raw/money/annual-report/ar-fy2025-rot-p6.png, ar-fy2025-rot-p8.png
4. Freedom spent $424,781.18 on transportation in 2023-24 and $270,503.62 in 2024-25, adopted $323,307.78 for 2025-26 and proposed $249,596.97 for 2026-27 (about 6.1% of the operating budget, **derived**); the MS-26 shows $282,432 of student transportation actually spent in FY2025.
   - citation: FY2025 Annual Report, "2026-2027 Proposed Budget by Function," function 2700, p. 46; Freedom 2026 MS-26, Appropriations, p. 2
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page viewed: "2700 TRANSPORTATION 424,781.18 270,503.62 323,307.78 249,596.97 (73,710.81) -22.80%". MS-26 text: "2700-2799 Student Transportation 02 $282,432 $346,146 $249,596". The two FY2025 totals differ as printed. Derived: 249,596.97 ÷ 4,080,727.75 = 6.1%. Raw: raw/money/annual-report/ar-fy2025-p48.png; raw/money/financial/freedom-ms26.ocr.txt
5. Within the 2026-27 adopted budget, regular transportation (drivers' wages and benefits) is $183,022, special education transportation $10,947, field trips $3,253, and bus repairs and maintenance $52,374, including $22,000 for bus repairs, $22,000 for fuel and $6,000 for bus insurance; the 2027-28 working budget totals $242,346 for the same lines (**derived**), with bus repairs raised to $30,000.
   - citation: Freedom School Board packet, November 9, 2026, 2027-2028 Working Budget, functions 2720, 2722, 2725 and 2741, pp. 67–70
   - source: https://drive.google.com/file/d/1iFpMO1L26C15tON_U4qwap535mmTnfpO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Rows: "Func: TRANSPORTATION - 2720 $196,105 ... $183,022 $150,670"; "Func: SPECIAL EDUCATION TRANSPORTATION - 2722 $31,052 ... $10,947 $33,923"; "01.2741.430.099 BUS REPAIRS $21,940 $27,017 $22,000 $30,000"; "01.2741.626.086 FUEL - ALL OTHER ROUTES $17,347 $11,328 $22,000 $22,000"; "Func: TRANSPORTATION REPAIRS & MAINTENANCE - 2741 $41,787 $39,719 $52,374 $54,500". Derived: 150,670 + 33,923 + 3,253 + 54,500 = 242,346. Raw: raw/money/packets/fsb-packet-2026-11-09-p67.png, -p68.png, -p70.png
6. Freedom's budgets do not separate the cost of carrying grades 7–12 to Conway from elementary routes; the only combined figure found is the options study's "Regular Transportation Freedom Elementary and KMS & KHS: $298,138" (2021-22 basis), and the board noted in October 2024 that a late bus from Conway "has been running every day, with 1 to 10 students riding."
   - citation: Freedom School District, "High School Options Preliminary Comparisons," p. 26; Freedom School Board Minutes, October 21, 2024
   - source: https://drive.google.com/file/d/1BgYXaeW2k-zGNbz_l4yMcJom6tW5vgCj/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: A statement about the budget documents read (2024 to 2027-28 working budget): fuel, repairs and wages are budgeted for all routes together. In April 2025 the board noted "Conway has scheduled 17 half days; this will result in overtime for bus drivers" (fsb-2025-04-14.txt). Raw: additional-data/raw/districts/batch-7/freedom-middle-high-options-comparisons.txt; raw/money/minutes/fsb-2024-10-21.txt
7. In January 2026 Freedom eliminated its transportation coordinator position (creating a stipend for the lead bus driver) and discussed outsourcing transportation, noting it would end the need for a bus reserve and might gain "economies of scale if all of SAU 13 districts utilized the same transportation provider," but that outside transportation "may impact flexibility" during the middle and high school negotiations; on October 26, 2026 it consolidated afternoon routes to one bus.
   - citation: Freedom School Board Minutes, January 12, 2026; February 9, 2026; Special Meeting Minutes (draft), October 26, 2026
   - source: https://drive.google.com/file/d/1Ap1eyD0ygrUjSJNtkKs0P12bFK-uNCiw/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: January text: "Transportation Outsourcing discussed: ■ Quote has not yet been received ■ ... If Transportation is outsourced, there would no longer be a need to fund a Bus Capital Reserve ... ■ With high school and middle school negotiations ongoing, a change from district provided transportation may impact flexibility in the future". October 26: "VOTE: Motion by Sarah Groleau to approve consolidation of afternoon bus routes to one bus and continue to monitor". No outsourcing decision was found. Raw: raw/money/minutes/fsb-2026-01-12.txt, fsb-2026-02-09.txt, fsb-2026-10-26-special-draft.txt
8. Freedom does not bus its students to Kingswood: no transportation to Governor Wentworth was offered in 2024-25, and in August 2026 the board said "There is no obligation to provide transportation to Kingswood" but it was willing to explore options such as a cluster stop; Freedom does earn some revenue by billing other districts for rides it provides (about $15,220 in 2024-25).
   - citation: Freedom School Board Minutes, December 9, 2024; August 11, 2025; August 10, 2026 (draft)
   - source: https://drive.google.com/file/d/1dQNp0kKYuUyEmk44PUrtBguHJsxz0zJr/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: December 2024: "Transportation is not offered in the current school year of 2024-25 to GWRSD". August 2026: "Potential cluster bus stop for Freedom students attending Kingswood ■ Confirm GWRSD permission to ride ■ There is no obligation ... ■ The Board is willing to explore transportation options to Kingswood". In September 2026 the chair said "GWRSD is picking up Freedom students at a bus stop" (fsb-2026-09-16-draft.txt). August 2025: Conway was billed for Laura Foundation rides and Tamworth for preschool and ESY rides, "Approximately $15,220 in transportation revenue". Raw: raw/money/minutes/fsb-2024-12-09.txt, fsb-2025-08-11.txt, fsb-2026-08-10-draft.txt

## district-sau-governance: Freedom in SAU 13

- kind: local
- question_type: governance_money
- description: How a district shares an SAU: board seats and votes, how SAU costs are divided, and what the local board decides versus the SAU

1. Freedom's share of the 2026-27 SAU 13 budget is $408,678 of $1,527,007.12 (26.76%), set half by its share of pupils (ADM-A 51.26, 15.58%) and half by its share of equalized value ($1,180,099,390, 37.94%); the default share was $385,036, and an $18,607 SAU fund-balance credit reduced the amount raised.
   - citation: FY2025 Annual Report, "Apportionment for Fiscal Year 2026-2027," p. 80; 2026 Warrant, Article 3; Calculation of Tax Rate Impact, p. 79
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page text: "Each town's share of the SAU budget is based upon taking one-half of the average daily membership in attendance (ADM-A) ... and one-half of the most recently published equalized valuation". Freedom's share rose from $177,427 (2019-20) to $378,727 (2025-26); the page notes a full-time BCBA and IT director added in 2022-23 and an SAU-wide preschool in 2024-25. SAU 13's own budget and history are in the Madison research. Raw: raw/money/annual-report/ar-fy2025-p82.png, ar-fy2025-p81.png
2. Freedom's HB 1265 report to voters lists the district's share of its two administrators' 2025-26 salaries, as apportioned through SAU 13: superintendent $36,061 and business administrator $25,631.
   - citation: Freedom School District, HB 1265 Mandatory Report to Voters on School District Expenses, p. 2; HB 1265 explanatory page
   - source: https://drive.google.com/file/d/1XlwN9jkSLrQOth1_F-o4cc2iWfz6h-Ax/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page text: "Top Administrator Salaries (2025-2026) Administrator Title Current Salary Superintendent $36,061 Business Administrator $25,631". The explanatory page says these "are reported based on the district's SAU apportionment, and reflect the only two positions that meet the RSA's definition of administrator." The report rules are in library topic budget-voter-information. Raw: raw/money/financial/freedom-hb1265-graph.pdf, -p1.png, -p2.png, .ocr.txt; raw/money/financial/hb1265-report.pdf, .txt
3. SAU 13's Financial Reports page posts, for Freedom, the MS-24 revenues, MS-25/DOE-25 financial report, warrant, election warrant, MS-26 budget, auditor's letter and report and the HB 1265 report and graphs, plus the proposed and default SAU budgets; Freedom's annual report adds reserve balances, the bus and capital plans, staffing and pay by position, the Kennett tuition calculation, the line-item budget, the special education statement, the SAU budget, a tax-rate estimate, apportionment and enrollment.
   - citation: SAU 13, Financial Reports page; FY2025 Annual Report, Table of Contents
   - source: https://www.sau13.org/school-board/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Page text: "Freedom School District FREEDOM MS-24, REVISED ESTIMATED REVENUES FREEDOM MS-25 SCHOOL FINANCIAL REPORT FREEDOM DOE-25 ANNUAL FINANCIAL REPORT FREEDOM WARRANT FREEDOM ELECTION OF OFFICERS ... FREEDOM MS-26 AUDITOR'S LETTER , REPORT FREEDOM MS-22 HB1265 MANDATORY REPORT". The "FREEDOM MS-22" entry has no link. Annual reports (2024, 2025) are at https://www.sau13.org/school-board/annual-reports. Each monthly board packet also carries revenue and expenditure reports, cost per pupil, reserve balances, the capital plan and enrollment (e.g., packet November 9, 2026). Raw: raw/money/pages/sau13_school-board_financial-reports.html, .txt; sau13_school-board_annual-reports.html, .txt
4. No SAU 13 or Freedom document reporting student-to-staff ratios was found on the SAU 13 site, in Freedom's annual reports or in 2022–2026 board packets; staff counts and class sizes for Freedom are in the site's data.
   - citation: SAU 13 website (Financial Reports, Annual Reports, board pages); Freedom annual reports FY2023 and FY2025
   - source: https://www.sau13.org/school-board/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: A statement about the documents searched. The annual report's staffing page lists each position with its FTE, from which a ratio could be computed, but none is published. Raw: raw/money/pages/; raw/money/annual-report/
5. Freedom already shares several services through SAU 13 and its partner districts: SAU 13 gets health insurance quotes "as a group," the three boards adopted a single SAU 13 policy book in 2026, Freedom buys a BCBA (behavior analyst) through an inter-district contract and buys meals from Madison, and the SAU runs one preschool for all three towns.
   - citation: Freedom School Board Minutes (draft), September 16, 2026 and October 19, 2026; Minutes, June 9, 2025; Superintendent's Report (FY2025 Annual Report, p. 23)
   - source: https://drive.google.com/file/d/1WY2dKYkIP6ZSi5N8YwrbRf9pG3pEyuA0/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: September 2026: "Inquiry from the public regarding quoting health insurance ○ SAU13 is quoted as a group"; "VOTE: Motion by Todd Giles to approve the BCBA Inter-District Contract". October 2026: "One policy book for SAU13 has been voted on and approved by the Tamworth and Madison school boards VOTE: Motion by Jake Stephan to approve one SAU13 policy book". Raw: raw/money/minutes/fsb-2026-09-16-draft.txt, fsb-2026-10-19-draft.txt, fsb-2025-06-09.txt
6. In May 2025 the SAU 13 superintendent reported that Lakes Region superintendents and special education directors were exploring a consortium to centralize specialized contracted and related special education services, with "cost sharing will result in cost savings"; the memorandum of agreement was "exploratory only," with no financial commitment.
   - citation: Freedom School Board Minutes, May 12, 2025, "Lakes Region Consortium MOA"
   - source: https://drive.google.com/file/d/11OmiPNCw11nsBuj3xPcEfzZrzN1cXO_a/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "exploring the concept of creating a consortium to work together to provide some special education services such as: ○ centralization of contracted services and related services that are specialized in nature ○ cost sharing will result in cost savings ○ discussed during the March 2025 Joint Board meeting ○ no financial contribution or commitment - the MOA is exploratory only". No later report on it was found. Raw: raw/money/minutes/fsb-2025-05-12.pdf, .txt
7. The Freedom School Board's March 2026 report lists as priorities "Strategic Planning to address financial concerns of declining enrollment; including more cost sharing at the SAU level," and understanding the financial effect of open enrollment, homeschooling and Education Freedom Accounts.
   - citation: Freedom School Board Report, March 2026 (FY2025 Annual Report, p. 21)
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Priorities for the future: • Middle and High School Educational options; including transportation considerations. • Mitigating Rising Cost of Health Insurance • Strategic Planning to address financial concerns of declining enrollment; including more cost sharing at the SAU level." Transcribed from image (OCR). Raw: raw/money/annual-report/freedom-ar-fy2025.ocr.txt (page 23)

## district-board-and-public-input: Voting, Hearings and Speaking Up in Freedom

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. The Freedom School District decides its budget at a traditional annual meeting, where voters present debate and vote on each warrant article from the floor (on March 9, 2026 at 7:00 p.m. at Freedom Elementary), while board members and other officers are elected by ballot at the Town Hall during the town election the next day.
   - citation: 2026 Warrant; 2026 Election of Officers warrant and SAU 13 Financial Reports page correction; RSA 197:1
   - source: https://drive.google.com/file/d/1kq41YFzDYJxLCMPHgJApy9HjdE0gsZxA/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Warrant: "You are hereby notified to meet in the Freedom Elementary School on Monday, March 9, 2026 at 7:00 PM". The election warrant says March 9; the SAU 13 page notes "CORRECTION : THE CORRECT DATE IS MARCH 10, 2026." RSA 197:1 requires an annual meeting between March 1 and 25. How traditional meetings work is in library topic budget-traditional-district-meeting. Raw: raw/money/financial/freedom-warrant.ocr.txt, freedom-election-of-officers.ocr.txt; raw/money/rsa/rsa-197-1.txt
2. Only people domiciled in Freedom can vote at its school district meeting: New Hampshire law gives the vote "at any meeting or election" to citizens of voting age in the town where they have "a single established domicile for voting purposes," so a seasonal owner whose domicile is elsewhere cannot vote on Freedom's school budget.
   - citation: RSA 654:1, I
   - source: https://gc.nh.gov/rsa/html/LXIII/654/654-1.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Freedom
   - note: Statute text: "Every inhabitant of the state, having a single established domicile for voting purposes, being a citizen of the United States, of the age provided for in Article 11 ... shall have a right at any meeting or election, to vote in the town, ward, or unincorporated place in which he or she is domiciled." Applying the statute to second-home owners is our plain reading. Raw: raw/money/rsa/rsa-654-1.htm, .txt
3. Before the district meeting the school board must hold at least one public budget hearing, posted at least 7 days ahead and held no later than 25 days before the meeting; the statute does not limit the hearing to voters, and Freedom held its 2026-27 hearing on February 9, 2026 at Freedom Elementary, where members of the public asked about the Governor Wentworth contract, the Fryeburg talks, the Conway negotiations and health care costs.
   - citation: RSA 32:5, I; Freedom School Board Minutes, February 9, 2026 (Public Hearing)
   - source: https://gc.nh.gov/rsa/html/III/32/32-5.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Freedom
   - note: Statute text: "The governing body, or the budget committee if there is one, shall hold at least one public hearing on each budget, not later than 25 days before each annual or special meeting, public notice of which shall be given at least 7 days in advance". Freedom's warrant and MS-26 show only school board recommendations; no budget committee was found. Minutes: "Sarah welcomed Public Input: ● She answered questions about the current contract with GWRSD". Raw: raw/money/rsa/rsa-32-5.htm, .txt; raw/money/minutes/fsb-2026-02-09.pdf, .txt
4. At the district meeting the moderator sets the rules (RSA 40:4), and Freedom's posted rules require each speaker to be recognized by the moderator and give their full name; the rules say nothing about whether non-voters may speak, and 5 voters can require a secret ballot on any article.
   - citation: Freedom School District, "Rules of Procedure" (FY2025 Annual Report, inside front cover); RSA 40:4, I
   - source: https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Rules text: "According to RSA 40 the Moderator determines the procedures to be followed in town or school district meetings ... The voters can overturn the Moderator's rules at any time"; "You must have permission from the Moderator before you can speak"; "A secret written ballot will be used on any article when requested in writing by any 5 voters (RSA 40: 4-a)." Statute: "the moderator ... may prescribe rules of proceeding; but such rules may be altered by the town." Transcribed from image (OCR, page 2). Raw: raw/money/annual-report/freedom-ar-fy2025.pdf; raw/money/rsa/rsa-40-4.txt
5. The Freedom School Board meets monthly, usually the second Monday at 6 p.m. at Freedom Elementary, with public comment at the start and end of each agenda (up to 15 minutes unless extended); its posted guidelines ask anyone who wants a topic discussed in depth to send it to the SAU office 7 days ahead and say the board may not respond to comments on matters it has not discussed.
   - citation: Freedom School Board, "Public Comments/Appearing Before the Board" (board packet, February 12, 2024, p. 3); FY2025 Annual Report, School Board Report
   - source: https://drive.google.com/file/d/115Klx3ZNQHzI1nNb3TWIYBCkrOuzkAeL/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "The Comments section of the agenda may not exceed fifteen (15) minutes unless extended by vote of the Board ... If anyone wishes to discuss a specific topic in greater detail, the Board requests that you submit the topic, supporting materials and/or information to the SAU office seven (7) days prior". The guidelines do not limit speakers to residents. Agendas, packets and minutes are posted at https://www.sau13.org/school-board/freedom/agendas-packets-minutes. Raw: raw/money/packets/fsb-packet-2024-02-12.txt (page 3); raw/money/pages/sau13_school-board_freedom_agendas-packets-minutes.html
6. Freedom's budget is built in public over the fall and winter: staff requests in September and October, budget versions reviewed at the November, December and January board meetings, the public hearing in February and the district meeting in March, with notice of the hearing 7 clear days ahead and the warrant posted 14 clear days before the meeting.
   - citation: Freedom School District, "FY 25 Budget & 2024 Warrant Timeline" (board packet, February 12, 2024, pp. 33–34)
   - source: https://drive.google.com/file/d/115Klx3ZNQHzI1nNb3TWIYBCkrOuzkAeL/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Mon., November 13, 2023: Freedom School Board Meeting: Board reviews Version #1 of budget with administration"; "The public hearing must take place no later than 25 days before the school district meeting"; "Note: 14-'Clear Days' before the annual school district meeting are needed for the posting of the warrant and budget form." For 2027-28 the board said "Budget reviews will occur during regular school board meetings, there will not be any work sessions" (fsb-2026-07-13-draft.txt). Raw: raw/money/packets/fsb-packet-2024-02-12.txt
7. The Freedom Selectboard is a standing item on Freedom School Board agendas (2024–2026), where selectmen have raised tuition costs, budget swings, the school's viability and use of the building, and the two boards have said they coordinate budgets; in 2022 a selectman asked to revive quarterly joint meetings.
   - citation: Freedom School Board Minutes, October 11, 2022; August 10, 2026 (draft); October 19, 2026 (draft)
   - source: https://drive.google.com/file/d/1AJzjvKzYwDaqcHYJ7KRQFg4UONmJ_xHp/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: 2022: "Ernie requested we revitalize the quarterly joint Select Board-School Board meetings." 2023 meeting: "The Board of Selectmen meets with the School Board quarterly" (freedom-ar-fy2023.ocr.txt). October 2026: "Select Board expressed concerns about the disparity of tuition costs between the districts being negotiated with". Raw: raw/money/minutes/fsb-2022-10-11.txt, fsb-2026-08-10-draft.txt, fsb-2026-10-19-draft.txt
8. On the Kennett contract the board held public sessions: a public hearing on middle and high school options on April 8, 2024 (with the 31-page comparison posted on the school website and Conway's board invited), listening-session planning in 2024, a family survey in 2026, and an update at each annual meeting; it told residents in October 2026 that it "wants voters/ taxpayers to have input" but that negotiations themselves are held in non-public session.
   - citation: Freedom School Board Minutes, April 8, 2024 (Public Hearing); January 22, 2024; October 19, 2026 (draft); September 16, 2026 (draft)
   - source: https://drive.google.com/file/d/17CuHbHxx34O0tjmCp1vRWrZYeg2wTSwv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: April 2024: "Full report (31 pages) is available on the Freedom Elementary School website"; "Board reiterated that these decisions and analysis are not done secretly". October 2026: "Survey was conducted with families, with sports and activities noted as important factors"; "There is a legal expectation not to disclose information during the negotiation process". Non-public sessions cite RSA 91-A:3, II(k) for "consideration by a school board of entering into a student or pupil tuition contract" (fsb-2026-09-16-draft.txt). Raw: raw/money/minutes/fsb-2024-04-08.pdf, .txt; fsb-2024-01-22.txt; fsb-2026-10-19-draft.txt; fsb-2026-09-16-draft.txt
9. Before each annual meeting Freedom posts its HB 1265 "Mandatory Report to Voters on School District Expenses," which graphs ten years of cost per pupil and average teacher salary in inflation-adjusted dollars and lists top administrator salaries; its annual report, with the full line-item budget, is the main budget document voters receive.
   - citation: Freedom School District, HB 1265 Mandatory Report to Voters on School District Expenses (explanatory page and graphs)
   - source: https://drive.google.com/file/d/1wM6n3tYJ_rP1UlMxi_tbotwp0eEl9DOK/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "All of the graph dollar values are presented in November 2025 dollars and have been adjusted for inflation using the Boston-Cambridge-Newton, MA-NH CPI-U". The explanatory page is shared by the three SAU 13 districts. No school or district newsletter about the budget was found. Raw: raw/money/financial/hb1265-report.pdf, .txt; freedom-hb1265-graph.pdf, -p1.png

## district-consolidation-history: Cooperation and Consolidation Studies Involving Freedom

- kind: local
- question_type: governance_money
- description: Studies, votes and discussions about cooperative districts, consolidation or sharing schools

1. Freedom took part in the 2020–2022 study of a cooperative school district by the eight towns that use Kennett; its board chair told voters in March 2023 that she, a fellow board member and a resident "were elected by the towns to serve on the Cooperative Committee," that "That work did not proceed, as the towns did not express interest," and that a later Joint Maintenance Unit committee "also did not move forward."
   - citation: FY2023 Annual Report, Annual Meeting Minutes, March 13, 2023, Article 6; Jackson file district-consolidation-history 3 in `Jackson/money-and-governance.md`
   - source: https://drive.google.com/file/d/1Jb1tfeZDjH3fiCfNAs232fbsRMGSOp9B/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Sarah Groleau: Jake, Joel Rhymer and I were elected by the towns to serve on the Cooperative Committee to consider a co-op school district. That work did not proceed, as the towns did not express interest. Then there was a Joint Maintenance Unit committee, which also did not move forward." The eight-town planning board voted on January 26, 2022 not to pursue a cooperative district (Jackson file). Transcribed from image (OCR). Raw: raw/money/annual-report/freedom-ar-fy2023.pdf, .ocr.txt (page 18)
2. In October 2022 Freedom's board told the Selectboard the cooperative committee had been disbanded, that a joint maintenance agreement would be discussed next, and that the board was "beginning to research other options for tuition in surrounding districts – Gov. Wentworth, Moultonborough, Fryeburg, Interlakes, and Conway," to which the Selectboard asked to add Sacopee Valley.
   - citation: Freedom School Board Minutes, October 11, 2022 (Freedom Select Board)
   - source: https://drive.google.com/file/d/1AJzjvKzYwDaqcHYJ7KRQFg4UONmJ_xHp/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "Jake and Sarah provided updates that the Co-Op committee had been disbanded. Upcoming meeting will discuss a Joint Maintenance Agreement ... Mike Whaland clarified that we will need to make a decision about a JMA soon (although we expect this option to be declined by the sending towns)." In November 2022 the board listed what needed to change in the agreement: "the 90% enrollment requirement, the equalized value, athletics options for homeschoolers, risk of Conway raising a bond, middle school contract" (fsb-2022-11-14.txt). Raw: raw/money/minutes/fsb-2022-10-11.pdf, .txt
3. A member of the public said at an October 2024 Freedom board meeting that a cooperative school district had been discussed 35 years earlier; no record of that discussion was found in the documents read.
   - citation: Freedom School Board Minutes, October 21, 2024 (Freedom Select Board)
   - source: https://drive.google.com/file/d/1BgYXaeW2k-zGNbz_l4yMcJom6tW5vgCj/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "● 35 years ago a cooperative school district was discussed". Cited only for what was said. Raw: raw/money/minutes/fsb-2024-10-21.pdf, .txt
4. At Freedom's April 8, 2024 hearing, when a resident asked about joining SAU 9 and SAU 13, a former Freedom board chair explained why SAU 13 was created and noted "Sending towns to SAU9 is 50% of enrollment, with no voice / vote"; in October 2026 two Freedom board members said combining the two SAUs "was explored several years ago, and Conway declined."
   - citation: Freedom School Board Minutes, April 8, 2024 (Public Hearing); October 19, 2026 (draft), Public Comment
   - source: https://drive.google.com/file/d/17CuHbHxx34O0tjmCp1vRWrZYeg2wTSwv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: April 2024 text: "Brian Taylor inquired on joining SAU9 and SAU13 into one organization ○ Alan Fall commented that he was Chair of the Freedom School Board when SAU13 was created ... ○ Sending towns to SAU9 is 50% of enrollment, with no voice / vote". October 2026: "Suggestion for SAU9 and SAU13 to combine ○ Two Board members stated this was explored several years ago, and Conway declined". No study document was found. A Bartlett board member reported "a conversation about merger" at a fall 2026 SAU 9/13 joint meeting (Bartlett file district-consolidation-history 5). Raw: raw/money/minutes/fsb-2024-04-08.txt, fsb-2026-10-19-draft.txt
5. In September 2026 a resident asked Freedom's board about "the potential of Ossipee, Effingham, Freedom and Madison study to discern viability of cooperation"; no such study, warrant article or board vote was found.
   - citation: Freedom School Board Minutes (draft), September 16, 2026, Freedom Select Board public discussion
   - source: https://drive.google.com/file/d/1XQN4QcIgbPFHyzp9pHrgfxjCTwdMXPX5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: A statement about the documents searched (minutes 2022–2026, annual reports FY2023 and FY2025). Ossipee and Effingham belong to the Governor Wentworth Regional School District. Raw: raw/money/minutes/fsb-2026-09-16-draft.txt
6. Freedom has tried to raise its own enrollment: since 2022 it has set elementary tuition for non-resident students low ($10,000 in 2022, $5,000 in 2023-24 through 2026-27, with a $500 rate for staff children), offered Eaton a $9,000 rate in 2024, and asked voters in 2026 to make Freedom Elementary an open enrollment school for up to 10 students per grade.
   - citation: Freedom School Board Minutes, August 8, 2022; May 13, 2024; July 8, 2024; July 13, 2026 (draft); 2026 Warrant, Article 1
   - source: https://drive.google.com/file/d/1kq41YFzDYJxLCMPHgJApy9HjdE0gsZxA/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Warrant: "designate the Freedom School District as an open enrollment school under the provisions of RSA 194-D to allow 10 students per grade (K-6) who reside outside the Freedom School District to attend, and to limit the percentage of Freedom School District students who may attend open enrollment schools ... to 0%". July 2026: "The Freedom School Board wants to increase student enrollment, and balance the point of view and concerns of the town and taxpayers"; "set the tuition rate for Freedom Elementary at $5,000". The result of Article 1 was not found. Raw: raw/money/financial/freedom-warrant.ocr.txt; raw/money/minutes/fsb-2022-08-08.pdf, .txt ("Gail Bizer made a motion to set the tuition at $10,000 for up to 10 students"), fsb-2024-05-13.txt, fsb-2024-07-08.txt, fsb-2026-07-13-draft.txt
7. No Freedom document defines when operating Freedom Elementary would become "unsustainable" or sets an enrollment or cost threshold for reconsidering it; the facts the board reviews are enrollment (44 in K–6 on October 1, 2025; 33 on October 1, 2026), cost per pupil (an estimated $53,354.53 per elementary pupil for 2026-27) and reserves.
   - citation: FY2025 Annual Report, Report of Official Enrollment, p. 81; Freedom School Board packet, November 9, 2026, pp. 40, 43
   - source: https://drive.google.com/file/d/1iFpMO1L26C15tON_U4qwap535mmTnfpO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: A statement about the documents searched. Derived: 33 is 21 fewer than the 54 counted on October 1, 2016 (−39%). The principal projects about 37 students for 2027-28 (kindergarten "8?") in five classes (K, 1/2, 3/4, 5 and 6) (**derived** sum; packet p. 46). See table freedom_k6_enrollment. Raw: raw/money/annual-report/ar-fy2025-p83.png; raw/money/packets/fsb-packet-2026-11-09-p43.png, fsb-packet-2026-11-09.txt
8. In August 2026 the Freedom Selectboard raised concerns about "The continued viability of the school," future town infrastructure costs and the "Best use of the school building"; the interim superintendent recommended a school–town partnership on strategic planning, and the board pointed to the community's support for the school and its goal of bringing in more students.
   - citation: Freedom School Board Minutes (draft), August 10, 2026, "Selectboard Concerns"
   - source: https://drive.google.com/file/d/1dQNp0kKYuUyEmk44PUrtBguHJsxz0zJr/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Text: "The Freedom Selectboard has expressed concern over: ○ The continued viability of the school ○ Future costs of town infrastructure projects ○ Best use of the school building ● Superintendent Dr. Scholand recommends partnership between the School District and the Town on strategic planning ● The Board discussed the history of strong community support for the school, and the Board's goal of bringing in more students to Freedom Elementary". In October 2026 the Selectboard asked about using part of the building as temporary town office space; the board did not think it possible while school is in session (fsb-2026-10-19-draft.txt). Draft minutes. Raw: raw/money/minutes/fsb-2026-08-10-draft.pdf, .txt
9. At the March 2023 meeting a resident noted that "Elementary schools in several nearby towns have been turned into municipal buildings because there are not enough kids" and linked enrollment to housing, and in September 2026 a public member asked whether it would cost the town less to tuition its elementary students elsewhere (the board answered "Not to Conway, based on recent board meeting discussion").
   - citation: FY2023 Annual Report, Annual Meeting Minutes, March 13, 2023, Article 6; Freedom School Board Minutes (draft), September 16, 2026
   - source: https://drive.google.com/file/d/1XQN4QcIgbPFHyzp9pHrgfxjCTwdMXPX5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Freedom
   - note: Residents' views, cited only for what was said. September 2026 text: "Inquiry if it would be less cost to the town to tuition to another school district? ○ Not to Conway, based on recent board meeting discussion". No cost study of tuitioning K–6 students was found. Raw: raw/money/annual-report/freedom-ar-fy2023.ocr.txt (page 19); raw/money/minutes/fsb-2026-09-16-draft.txt
10. Since October 8, 2026, closing an elementary school in New Hampshire needs a majority vote of the voters in the towns it serves (RSA 194:3-f, library topic gov-school-closure-votes), so a decision to close Freedom Elementary would go to Freedom's voters.
   - citation: RSA 194:3-f (library topic gov-school-closure-votes)
   - source: https://gc.nh.gov/rsa/html/XV/194/194-3-f.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Freedom
   - note: Pointer to the library rule; applying it to Freedom is our plain reading. Statute text (quoted in the Conway file district-facilities-and-capital 8): "No elementary school ... shall be discontinued ... except by a majority vote of voters residing in all municipalities that are served by the school or district." No closure proposal for Freedom Elementary was found.
11. Research on merging small districts and schools, and the rules for forming or leaving a cooperative district or SAU, are in library topics research-district-consolidation, gov-cooperative-forming, gov-cooperative-withdrawal and gov-sau-forming-and-withdrawing; no study weighing these options specifically for Freedom was found.
   - citation: library cross-reference
   - source: https://gc.nh.gov/rsa/html/XV/195/195-18.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Freedom
   - note: Pointer only; no new statewide facts here.

## freedom_operating_budget: Freedom School District Operating Budget and Total Raised by Taxation

- unit: dollars
- period: fiscal years 2016-17 through 2026-27; year: the year the fiscal year ends
- source: Freedom School District Annual Report (FY2025), "FY27 Freedom Proposed Budget & Warrant Comparison," p. 5 — https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
- as_of: 2026-11-13
- raw: raw/money/annual-report/ar-fy2025-rot-p7.png
- note: Value is the operating budget (2026-27 as proposed). "Total" is the operating budget, staff contract and warrant articles raised by taxation, including the SAU share. Percent changes are the district's own. 2025-26 total is the public-hearing version.

| Place | District id | Year | Value | Staff contract (CBA) | SAU share | Total raised by taxation | Change in operating budget |
|---|---|---|---|---|---|---|---|
| Freedom | 187 | 2017 | 3308343.88 | 0 | 173,903.00 | 3,528,046.88 | 3.5% |
| Freedom | 187 | 2018 | 3460709.00 | 32,334.00 | 179,773.00 | 3,692,816.00 | 5.6% |
| Freedom | 187 | 2019 | 3509990.81 | 0 | 175,622.13 | 3,685,612.94 | 0.5% |
| Freedom | 187 | 2020 | 3751144.00 | 20,993.00 | 177,427.00 | 3,994,564.00 | 7.5% |
| Freedom | 187 | 2021 | 3937493.91 | 0 | 187,038.00 | 4,164,531.91 | 4.4% |
| Freedom | 187 | 2022 | 3857469.00 | 0 | 178,245.34 | 4,195,714.34 | -2.0% |
| Freedom | 187 | 2023 | 3323544.46 | 28,951.00 | 263,618.00 | 3,616,113.46 | -13.1% |
| Freedom | 187 | 2024 | 3623736.38 | 0 | 257,141.00 | 3,880,877.38 | 8.1% |
| Freedom | 187 | 2025 | 3944524.14 | 79,129.00 | 343,332.00 | 4,366,985.14 | 11.0% |
| Freedom | 187 | 2026 | 4109144.75 | 0 | 378,727.00 | 4,487,871.75 | 2.1% |
| Freedom | 187 | 2027 | 4080728.00 | 0 | 408,678.00 | 4,489,406.00 | -0.7% |

## freedom_cost_per_pupil_by_level: Freedom's Own Cost per Pupil by Level (Elementary, Kennett Middle, Kennett High)

- unit: dollars
- period: school years 2019-20 through 2026-27; year: the year the school year ends
- source: Freedom School Board packet, November 9, 2026, "Freedom School District - Cost per Pupil," p. 40 — https://drive.google.com/file/d/1iFpMO1L26C15tON_U4qwap535mmTnfpO/view
- as_of: 2026-11-13
- raw: raw/money/packets/fsb-packet-2026-11-09-p40.png
- note: Value is the elementary cost per pupil (ADM-A). Middle and high are Freedom's tuition to Conway (and other schools) divided by Freedom's pupils there, so they are per-student tuition, not Kennett's own cost. 2026 is a draft actual and 2027 an estimate on estimated ADM-A. The district subtracts food service, transportation and "Supplmt Exp" from elementary costs, so its figures differ from NH DOE's (site data: $41,267 for 2025).

| Place | District id | Year | Value | Elementary ADM-A | Middle per pupil | Middle ADM-A | High per pupil | High ADM-A | All levels per pupil |
|---|---|---|---|---|---|---|---|---|---|
| Freedom | 187 | 2020 | 38320.33 | 49.19 | 49,243.40 | 11.52 | 28,151.07 | 30.33 | 36,314.62 |
| Freedom | 187 | 2021 | 34131.16 | 48.12 | 45,831.09 | 13.16 | 39,076.66 | 29.20 | 37,428.90 |
| Freedom | 187 | 2022 | 37532.03 | 36.43 | 34,620.39 | 14.46 | 40,672.99 | 28.90 | 38,142.02 |
| Freedom | 187 | 2023 | 33181.70 | 48.44 | 27,194.39 | 21.66 | 28,458.45 | 34.81 | 30,378.33 |
| Freedom | 187 | 2024 | 34604.84 | 48.10 | 41,156.53 | 13.00 | 21,051.06 | 41.03 | 29,993.66 |
| Freedom | 187 | 2025 | 34610.99 | 52.01 | 55,624.02 | 13.49 | 33,852.48 | 31.46 | 37,288.42 |
| Freedom | 187 | 2026 | 42866.68 | 42.63 | 34,872.31 | 14.27 | 40,574.06 | 30.41 | 40,761.56 |
| Freedom | 187 | 2027 | 53354.53 | 32.00 | 35,106.00 | 18.00 | 36,960.26 | 27.00 | 43,340.00 |

## freedom_k6_enrollment: Freedom Elementary Enrollment (K–6) and Freedom Students in Grades 7–12, October 1

- unit: count
- period: October 1, 2016 through October 1, 2026; year: the calendar year of the count
- source: Freedom School District Annual Report (FY2025), "Report of Official Enrollment - As of October 1st," p. 81 — https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view; 2026 from Freedom School Board packet, November 9, 2026, p. 43
- as_of: 2026-11-13
- raw: raw/money/annual-report/ar-fy2025-p83.png; raw/money/packets/fsb-packet-2026-11-09-p43.png
- note: Value is Freedom Elementary K–6 (preschool excluded). Grades 7–12 are Freedom resident students in the district's count; for 2026 the packet lists 14 at Kennett Middle, 25 at Kennett High and 6 at Kingswood, so the 2026 figure (45) is a **derived** sum of those three schools. The site's own enrollment data covers Freedom Elementary in more detail.

| Place | District id | Year | Value | Grades 7–12 | Note |
|---|---|---|---|---|---|
| Freedom | 187 | 2016 | 54 | 47 | |
| Freedom | 187 | 2017 | 55 | 48 | |
| Freedom | 187 | 2018 | 53 | 50 | |
| Freedom | 187 | 2019 | 48 | 46 | |
| Freedom | 187 | 2020 | 49 | 46 | |
| Freedom | 187 | 2021 | 33 | 45 | |
| Freedom | 187 | 2022 | 48 | 56 | |
| Freedom | 187 | 2023 | 48 | 54 | |
| Freedom | 187 | 2024 | 52 | 45 | |
| Freedom | 187 | 2025 | 44 | 41 | 15 homeschooled in K–12 listed separately |
| Freedom | 187 | 2026 | 33 | 45 | Board packet; grade 7–12 figure **derived** (14 + 25 + 6) |

## freedom_capital_reserves: Freedom School District Capital Reserve and Trust Fund Balances

- unit: dollars
- period: balances on January 31, 2026; year: 2026
- source: Freedom School District Annual Report (FY2025), "Capital Reserve Fund Balances and Goals," p. 4 — https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
- as_of: 2026-11-13
- raw: raw/money/annual-report/ar-fy2025-rot-p6.png
- note: Value is the balance on January 31, 2026. Balances exclude interest after June 30, 2025. The November 2026 board packet shows the same balances "as of 6/30/2026" plus a $50,000 building deposit (p. 41).

| Place | District id | Year | Value | Fund | Goal | Balance June 30, 2025 | 2025-26 deposits / withdrawals |
|---|---|---|---|---|---|---|---|
| Freedom | 187 | 2026 | 377733.47 | Special Education | $350,000 (met) | 377,733.47 | none |
| Freedom | 187 | 2026 | 313380.36 | School Building Maintenance | per schedule | 258,734.36 | +90,146.00 / −35,500.00 (flat roof) |
| Freedom | 187 | 2026 | 303022.09 | School Tuition Stabilization (expendable trust) | $200,000 (met) | 303,022.09 | none |
| Freedom | 187 | 2026 | 178025.53 | School Bus | per schedule | 279,303.53 | +35,000.00 / −136,278.00 (new bus) |
| Freedom | 187 | 2026 | 25213.79 | School Technology | $15,000 (met) | 25,213.79 | none |
| Freedom | 187 | 2026 | 1197375.24 | Total | | 1,244,007.24 | +125,146.00 / −171,778.00 |

## freedom_cip_withdrawals: Freedom's Planned Capital Reserve Withdrawals by Fiscal Year

- unit: dollars
- period: fiscal years 2026 through 2035; year: fiscal year
- source: Freedom School District Annual Report (FY2025), "Freedom School District Capital Investment Plan" (updated February 2, 2026), p. 7 — https://drive.google.com/file/d/1WI3gK1vdlWJwmFLLD7qSA2lU9IEi3Epn/view
- as_of: 2026-11-13
- raw: raw/money/annual-report/ar-fy2025-rot-p9.png
- note: Value is the planned withdrawal from the Building Maintenance Capital Reserve Fund. The plan assumes contributions of $90,146 (FY2026) and $80,000 a year afterward. Items named are those whose replacement falls in the year on the plan; estimates include the plan's inflation factors.

| Place | District id | Year | Value | Main items | Proposed contribution | Planned end balance |
|---|---|---|---|---|---|---|
| Freedom | 187 | 2026 | 35500.00 | Flat roof over lobby and offices (done summer 2025) | 90,146.00 | 313,380.36 |
| Freedom | 187 | 2027 | 15951.61 | Driveway sealing | 80,000.00 | 377,428.75 |
| Freedom | 187 | 2028 | 0 | | 80,000.00 | 457,428.75 |
| Freedom | 187 | 2029 | 16430.16 | Driveway sealing | 80,000.00 | 520,998.59 |
| Freedom | 187 | 2030 | 0 | | 80,000.00 | 600,998.59 |
| Freedom | 187 | 2031 | 16923.06 | Driveway sealing | 80,000.00 | 664,075.52 |
| Freedom | 187 | 2032 | 49473.96 | Original windows (meeting room, gym) $38,465.23; flooring machine $11,008.73 | 80,000.00 | 694,601.56 |
| Freedom | 187 | 2033 | 17430.76 | Driveway sealing | 80,000.00 | 757,170.81 |
| Freedom | 187 | 2034 | 227968.66 | Boilers #3 and #4 ($217,459.71 together); classroom wing bathrooms | 80,000.00 | 609,202.15 |
| Freedom | 187 | 2035 | 82225.49 | HVAC controls $63,524.25; flooring; driveway sealing | 80,000.00 | 606,976.66 |

## For another file

- **Freedom community and families agent:** the October 1, 2026 count of Freedom resident students by school (packet November 9, 2026, p. 43: Freedom Elementary 33, SAU preschool 5, Madison Elementary 2, charter schools 12, VLACS 8, Children's Scholarship Fund/EFA 5) and the 2027-28 projection (about 37 K–6). The Selectboard's August 2026 concerns about the school's viability and best use of the building, and its October 2026 question about town office space in the school. Sources: raw/money/packets/fsb-packet-2026-11-09-p43.png, fsb-packet-2026-11-09.txt (p. 46); raw/money/minutes/fsb-2026-08-10-draft.txt, fsb-2026-10-19-draft.txt.
- **Freedom getting-to-school agent:** the afternoon route consolidation to one bus (October 26, 2026); the Kennett late bus ridership (1–10 students, October 2024); the Kingswood cluster-stop discussion (August 2026); the King Pine ski program schedule in the November 9, 2026 principal's report (p. 46), which bears on the "King Pine" premise. Sources: raw/money/minutes/fsb-2026-10-26-special-draft.txt, fsb-2024-10-21.txt, fsb-2026-08-10-draft.txt; raw/money/packets/fsb-packet-2026-11-09.txt.
- **Freedom Elementary agent:** the September 2026 minutes list band participation ("13 out of 19 eligible students"), the math curriculum review (Math and You, Dimensions, Saxon), the after-school program with three families and the BCBA one afternoon a week. Source: raw/money/minutes/fsb-2026-09-16-draft.txt, fsb-2026-10-19-draft.txt.
- **Madison research (SAU 13):** Freedom's minutes record the SAU 13 joint board and budget public hearing on November 23, 2026 in Tamworth; the Lakes Region special education consortium MOA (May 2025); the single SAU 13 policy book (October 2026); and a new interim superintendent (Dr. Ronna HasBrouk) from October 2026. Sources: raw/money/packets/fsb-packet-2026-11-09.txt (p. 1); raw/money/minutes/fsb-2025-05-12.txt, fsb-2026-10-19-draft.txt.
- **Conway file, district-tuition-contracts:** fact 8 says SAU 13 "presented a tuition contract with Governor Wentworth." From Freedom's side, Freedom already has a Governor Wentworth agreement approved August 11, 2025 and was still negotiating with Governor Wentworth, Moultonborough, Fryeburg and Conway in October 2026 (this file, district-tuition-contracts 12, 15). Conway's September 2026 JFAB policy (25% premium for non-contract students) is not in the Conway money file (this file, district-tuition-contracts 11).
- **Conway file, district-tuition-contracts 7 (March 2026 Kennett enrollment by town):** Freedom's own October 1, 2026 count shows 14 at Kennett Middle and 25 at Kennett High (down from 13 and 28 in March 2026).
- **Site salary data (recommendation A8):**
  - Freedom's salary-band rows change from 25 steps (2024) to 8 steps (2025, 2026), and its 2024 rows have no BA15 or BA30 bands. These could not be checked because Freedom's staff contract was not retrieved.
  - Tamworth's 2026 MA maximum is still $8,579 (below its $48,745 minimum), the error the Conway agent reported.
  - Freedom's 2021 average salary in the site data ($38,034) is well below the years around it; the district's HB 1265 graph also shows a dip for 2021 ($44,147 in November 2025 dollars).
  - Source: raw/money/state-data/site-db-freedom-queries-2026-11-13.txt.
- **Jackson file, district-consolidation-history 3 in `Jackson/money-and-governance.md`:** the Freedom March 2023 minutes add that after the cooperative study a "Joint Maintenance Unit committee ... also did not move forward," and that Freedom's three committee members were elected by the towns. The Freedom October 2022 minutes say the JMA option was expected to be declined by the sending towns, and the December 12, 2022 minutes say "JMA – Conway voting tonight" (raw/money/minutes/fsb-2022-12-12.txt).

## Not retrieved

- **March 9, 2026 Freedom School District meeting results:** not in the SAU 13 Drive folders (annual meeting minutes appear only in the next year's annual report) or in the Town of Freedom 2025 report (published February 2026). The result of the open enrollment article is unknown. The November 2026 working budget's "2026-2027 ADOPTED" column matches the proposed budget plus Article 4.
- **Freedom–Governor Wentworth agreement (August 11, 2025) and the 2024 MOU:** not posted in the Freedom board packets read (May and June 2024, August 2025) or on sau13.org.
- **Freedom School District / Freedom Employee's Association contract (2024–2027) and its salary schedule:** not posted on sau13.org (the Staff Resources folder has only benefit forms).
  - https://www.nh.gov/pelrb/collective/coll_a_f.htm and https://www.nh.gov/pelrb/collective/documents/freedom_employees7.pdf (the 2022–2024 contract) returned "Access Denied"/HTTP 403 to curl and WebFetch.
  - So the site's Freedom salary bands could not be checked.
- **Freedom School Board minutes for November 9, 2026:** not yet posted (only the packet). The "Negotiations Update" on that agenda is unknown.
- **SAU 13 tax cap information:** the four "Tax Cap Information" items on https://www.sau13.org/home/tax-cap-information are videos (100+ MB each). They were not reviewed or kept.
- **MS-27 for Freedom:** not posted. The MS-26 and the annual report's line-item budget were used.
- **2021–2022 Freedom School Board minutes:** in the archive folders but not read beyond August 2022. Freedom's own 2020 or 2021 warrant vote creating its cooperative planning committee was not found in the documents read.
- **Teacher turnover or retention rates** for Freedom, Madison, Tamworth or SAU 9: no published figures found.
