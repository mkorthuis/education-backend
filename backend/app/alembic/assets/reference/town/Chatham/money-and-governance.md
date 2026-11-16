# Chatham School District: Money, Tuition Arrangements and Governance

Part of the Chatham research (town/Chatham). Gathered November 13, 2026.

## Summary

**What's covered:** 12 topics, 102 facts and 5 number tables on the Chatham School District's money, its tuition arrangements with MSAD 72 and Fryeburg Academy, and its governance. Eight topics use shared slugs; four are proposed new general topics (below).
- The 2026-27 budget ($1,291,161, up 33.25%) and what drove it: out-of-district special education tuition rose from $105,587 to $398,139, about 91% of the increase (**derived**). Regular tuition rose 4.10%.
- Budget, tuition and enrollment trends from the district's annual reports (2017–2026), the 2025-26 year-end summary and budget status reports, and board minutes from 2013 to October 2026.
- The estimated 2026 school rate ($11.42, up 56.22%) and the 2024 revaluation. Chatham's DRA tax rates (2014–2025) and NH DOE school taxes (2011–2025), and how they compare with Jackson, Bartlett and Conway, are in the site's data (property_tax), so this file does not repeat them.
- State aid as the district's reports show it, and why Chatham gets no fiscal capacity disparity aid. NH DOE's adequacy aid calculation for Chatham, FY2020–FY2027, is in the site's data (adequacy_aid), so this file does not repeat it; unlike Jackson, Chatham gets a grant every year and keeps no excess statewide tax.
- The history of Chatham's tuition agreement with MSAD 72 (a 2016 rider to June 2021, then year to year by 2022). Also what MSAD 72 budgets from Chatham, Maine's tuition-rate laws (including the 10% debt service factor and the private academy "insured value factor"), and why Chatham voters cannot vote on MSAD 72 bonds.
- High school choice under Chatham policies JECC (other SAU 9 schools, with partial reimbursement) and JECA (manifest hardship), and Chatham's 2026 open enrollment vote (0% may leave).
- Who is legally responsible for and pays for special education for a Chatham child educated in Maine, and the rules for out-of-state placements.
- Residency rules, Chatham's Chatham/Stow split-house dispute, and what Chatham can do if costs jump mid-year (special meetings, emergency spending, reserves, retained fund balance, the new tax cap).
- Chatham's role in SAU 9 (seats, votes, an apportionment based only on property value) and how residents can take part in Chatham's and MSAD 72's decisions.

**Main sources:** the Chatham School District's annual reports 2017–2026 (scanned; pages rendered and read), board minutes and agendas (2013–October 2026), the 2025 and 2026 annual meeting minutes, policies JECC, JECA and DK, and SAU 9's Chatham and tuition pages. Also MSAD 72's budget documents, warrant, board list, policy JFAB and April 2023 minutes, and Maine DOE tuition-rate files. Laws read: Maine statutes (20-A §§1251, 1310, 1311, 1351, 5801, 5804, 5806), NH statutes (RSA 186-C, 189:1-a, 193:12, 194:22, 194-C, 194-D, 197, 198:4-b, 32:11), Ed 1100 and 34 CFR 300.146 and 300.325. Data: the library's DRA, DOE and adequacy CSVs, and read-only site database queries.

**Main gaps:**
- No written Chatham–MSAD 72 or Chatham–Fryeburg Academy agreement was found anywhere posted. Chatham's per-student rates are therefore **derived** from budget lines.
- DRA's 2026 tax rate for Chatham was not retrieved (HTTP 403).
- Chatham policy JFAA (resident admission, adopted June 2025) is not in the posted policy folder.
- No Chatham public comment policy or meeting recordings were found.

**Proposed new general topics** (no shared topic fits these statewide or Maine rules):
- `cross-state-school-tuition-rules` (rule, rules): how Maine sets the tuition its districts and private academies may charge, who votes on a Maine school district's budget and bonds, and New Hampshire's rule for contracting with a school in another state.
- `school-residency-rules` (rule, rules): which district is legally responsible for a student under NH law (legal residence, domicile, guardians, residency disputes).
- `special-education-placements-across-states` (rule, rules): who is responsible for and pays for special education when a NH district educates a student in another state or a private school.
- `school-budget-overruns-and-reserves` (rule, rules): what a NH school district can do when costs exceed its budget mid-year.

**Premises checked:**
- "The board meets at 9:00 a.m. in Conway" (P2.3) is out of date. The board voted in December 2025 to meet at 9:30 a.m., and since September 2026 it has met in the Kennett High School conference room. Its budget hearing and annual meeting are evening meetings at the Chatham Town Hall. SAU 9's and the town's web pages still say 9:00 a.m.
- "Taxes keep going up to pay MSAD 72 and Fryeburg tuition" (P2.1) is partly right. For 2026-27, regular tuition rose 4.10%; most of the increase was out-of-district special education tuition. The 2024 school tax was also held down by $256,698 of fund balance.
- "The formula barely helps" (P2.1): Chatham received a $111,416 adequacy grant plus $98,299 of statewide tax in FY2026, about 22% of 2025-26 revenue (**derived**). The grant falls to $71,320 in FY2027.
- "Chatham's per-pupil assessment" (P2.2): MSAD 72 assesses only its seven Maine member towns. Chatham pays tuition, which MSAD 72 budgets as revenue.
- "Tuition strictly locked to Fryeburg" (P3.3): policy JECC lets a family choose another public school in SAU 9 (such as Kennett), with Chatham paying up to the MSAD 72 and Fryeburg rates.
- "Can residents vote on MSAD 72 bonds?" (P6.3): no. Only voters of the seven Maine member towns vote, and MSAD 72's board has no Chatham director.
- "NH open enrollment into Bartlett or Conway" (P10.3): both now take outside students. But Chatham voters in March 2026 set at 0% the share of Chatham students who may attend open enrollment schools outside the district.
- "The town is on the hook after six months" (P13.2): NH law has no time test. Residence turns on domicile, the intent to make a home there.
- "Molly Ockett from kindergarten" (P1.1, agent 1's area): MSAD 72's April 2025 count shows Chatham's K–4 pupils mostly at New Suncook in Lovell (12) and none in kindergarten or grade 1 at Molly Ockett.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P2.1 Why do school taxes keep rising? | district-budget-and-cost facts 1–9, 15; district-tax-and-state-aid facts 1–3, 5–6; tables chatham_operating_budget, chatham_budget_lines; site data: property_tax and adequacy_aid (Chatham district); library: money-adequacy-grant-calculation, gov-tuition-towns | full | Special education tuition is the main 2026-27 driver; fund balance use in 2024-25 and a falling adequacy grant also matter |
| P2.2 If MSAD 72 reconfigures schools, does Chatham's cost drop or shift to capital? | district-tuition-contracts facts 3–10; cross-state-school-tuition-rules facts 1–4, 8; table chatham_msad72_tuition_revenue | partial | Maine's rate formula and capital rules are documented; Chatham's own agreement terms were not found. No forecast. MSAD 72's BDES study is agent 1's |
| P2.3 How can seniors weigh in when the board meets mornings in Conway? | district-board-and-public-input facts 1–11; library: budget-traditional-district-meeting, budget-committees | full | Premise out of date (9:30 a.m.; Kennett HS); hearing and annual meeting are evenings in Chatham |
| P3.2 (legal side) Who evaluates and pays for an IEP or 504 student | district-special-education-services facts 1–7; special-education-placements-across-states facts 1–8; library: special-ed-iep-basics, section-504-plans | partial | NH law makes Chatham (the district of residence) responsible; documents read don't say whose staff do evaluations at MSAD 72 (agent 1) |
| P3.3 Can Chatham high schoolers switch to Kennett? | high-school-tuition-options facts 1–7; library: change-of-school-assignment, open-enrollment-status | full | Policy JECC allows it with partial reimbursement and no transport |
| P6.1 School vs town vs county shares of the bill | site data: property_tax (Chatham district) | data only | DRA's rates by part and the school share, 2014–2025 (2025: school 86.3%) |
| P6.2 Why Chatham has a district, board and SAU membership | district-sau-governance facts 1–4; library: gov-school-district, gov-sau | full | |
| P6.3 Can residents vote on MSAD 72 bonds? | district-board-and-public-input facts 10–11; cross-state-school-tuition-rules facts 5–7 | full | No |
| P9.2 How many students and how volatile is the budget | district-budget-and-cost facts 10–14; table chatham_students_by_level | full | Per-student and tax-rate effects are **derived** |
| P10.3 NH open enrollment into Bartlett or Conway | high-school-tuition-options facts 5–6; library: open-enrollment-status, choice-open-enrollment-2026-bills; Bartlett file: high-school-tuition-options fact 6 | full | Chatham set 0% |
| P13.1 Chatham's school tax rate vs Jackson, Bartlett, Conway | site data: property_tax (Chatham, Jackson, Bartlett and Conway districts); district-tax-and-state-aid fact 4 | full | The rates, equalized rates and full value rates are in the site's data; 2026 rates not yet retrieved |
| P13.2 When is a renting family Chatham's responsibility? | school-residency-rules facts 1–6; district-student-support facts 1–4 | full | No minimum stay in NH law |
| P13.3 Could an enrollment jump force a special meeting or mid-year tax rise? | district-budget-and-cost facts 10, 15–18; school-budget-overruns-and-reserves facts 1–6; district-tax-and-state-aid fact 7 | full | The tax rate is set once a year; the 2026 tax cap applies from 2027-28 |
| P14.2 Out-of-state special education placements: who pays, which rules | special-education-placements-across-states facts 1–8; district-special-education-services facts 1–7; library: money-special-education-aid | full | |
| P16.1 Adequacy aid vs statewide education tax | district-tax-and-state-aid facts 3, 5–6; site data: adequacy_aid (Chatham district) | full | No excess SWEPT in any year (site data) |
| P16.2 Say in SAU 9 decisions, including the superintendent | district-sau-governance facts 3–8; Jackson file: jackson_sau9_board_seats_and_votes, district-sau-governance 6–12 in `Jackson/money-and-governance.md` | full | |

## district-budget-and-cost: Chatham's School Budget, What Drives It, and Its Reserves

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. Chatham voters approved a 2026-27 operating budget of $1,291,161 (with $9,500 offset by grants) at the March 10, 2026 district meeting, recommended 3-0-0 by the school board and 8-0-0 by the budget committee; it is $322,172 (33.25%) more than 2025-26's $968,989.
   - citation: Chatham School District Annual Meeting Minutes, March 10, 2026, Article 6; 2026 Annual Report, "2026-2027 Proposed Budget," p. 2 of 2
   - source: https://drive.google.com/file/d/1eFqzxGPifEKUkG_ZghveKp7UbjU5d9sx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Warrant text: "totaling $1,291,161 with $9,500 offsetting this amount by various grants ... (Recommended by the School Board 3-0-0) (Recommended by the Budget Committee 8-0-0)"; handwritten: "Article 6 was voted on and approved." Budget page: "TOTAL GENERAL FUND & GRANT FUNDS 946,000 908,880 968,989 1,291,161 322,172 33.25%". Scanned; transcribed from image (pages viewed). Raw: raw/money/minutes/am-2026-03-10.pdf, .ocr.txt; raw/money/reports/ar-2026.pdf, .ocr.txt (pp. 5–6)
2. In Chatham's 2026-27 budget, elementary tuition (MSAD 72) is $446,375, high school tuition (Fryeburg Academy) $299,475, special education tuition $398,139, transportation $85,804 and the SAU 9 share $19,694; these are about 35%, 23%, 31%, 7% and 2% of the budget (**derived**).
   - citation: Chatham School District 2026 Annual Report, "2026-2027 Proposed Budget," pp. 1–2 of 2
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Rows: "TUITION,ELEMENTARY 335,682 384,193 452,439 446,375 (6,064) -1.34%"; "TUITION,HIGH SCHOOL 258,754 246,118 264,011 299,475 35,464 13.43%"; "TUITION, SPECIAL EDUCATION 202,100 155,649 105,587 398,139 292,552 277.07%"; "TOTAL 2720 PUPIL TRANSPORTATION ... 85,804"; "SAU#9 DISTRICT SHARE ... 19,694 4,621 30.66%" (columns: adopted 2024-25, actual 2024-25, adopted 2025-26, proposed 2026-27). Shares: 34.57%, 23.19%, 30.84%, 6.65%, 1.53% of $1,291,161. The remaining lines are special education services ($24,874), school board services ($7,299) and grants ($9,500). Rotated scanned page; transcribed from image. See table chatham_budget_lines. Raw: raw/money/reports/ar-2026.*
3. Out-of-district special education tuition is the largest single change in the 2026-27 budget: it rose $292,552 (277.07%) from $105,587, about 91% of the whole $322,172 increase (**derived**), while elementary tuition fell 1.34% and high school tuition rose 13.43%.
   - citation: Chatham School District 2026 Annual Report, "2026-2027 Proposed Budget"
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Derived: 292,552 ÷ 322,172 = 90.8%. The budget shows the 2025-26 special education tuition line as $105,587; by June 5, 2026 the district had spent $161,886.24 and encumbered $73,319.58 on it (fact 4). Raw: raw/money/reports/ar-2026.*; raw/money/agendas/ag-2026-06-09-msad72.pdf, .txt (p. 4)
4. For 2025-26, Chatham spent $960,135 against a $979,489 budget: special education came in $83,878 over budget ($192,465 against $108,587) while regular education tuition came in $84,553 under ($631,897 against $716,450), leaving a fund balance of $41,977 on June 30, 2026.
   - citation: Chatham School District, "Summary of Expenses & Receipts 2025-2026" (August 21, 2026), attached to the September 8, 2026 board agenda
   - source: https://drive.google.com/file/d/1NqWAn2DTw0So0IZYy_OaWGgYWFhQ1H2c/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "1100 Regular Education 716,450 $ 631,897 $ 84,553 ... 1200 Special Education 108,587 $ 192,465 $ (83,878)$ Spec.Ed. Tuition ... TOTAL EXPENSES 979,489 $ 960,135"; "Ending Fund Bal. 6/30/26 41,977". The $979,489 includes the $20,000 capital reserve deposit. On September 8, 2026 the board voted 3-0-0 to return about $1,900 to taxpayers after $40,000 went to the special education reserve (Article 8). Raw: raw/money/agendas/ag-2026-09-08-attach.pdf, .txt; raw/money/minutes/csb-2026-09-08.pdf, .txt
5. Chatham's actual tuition spending was $325,470 (elementary) and $199,021 (high school) in 2022-23, $320,035 and $207,661 in 2023-24, and $384,193 and $246,118 in 2024-25; out-of-district special education tuition was $244,172, $175,205 and $155,649 in those years.
   - citation: Chatham School District 2024 Annual Report (FY25 Proposed Budget, "Actuals FY23"); Budget attached to December 9, 2025 board minutes ("Actuals 7/1/23–6/30/24"); 2026 Annual Report ("Actuals 7/1/24–6/30/25")
   - source: https://drive.google.com/file/d/1X7DXxpuu1v4p92UZskoEukNwRxtZLSk7/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: FY23 rows (2024 report p. 4, viewed): "TUITION,ELEMENTARY ... 325,470"; "TUITION,HIGH SCHOOL ... 199,021"; "TUITION, SPECIAL EDUCATION ... 244,172". FY24 (December 2025 attachment p. 3, viewed): "320,035 ... 207,661 ... 175,205". The 2024-25 actuals match the site's DOE-25 lines ($384,192.88 and $246,118.27, raw/money/state-data/site-db-chatham-doe25-expenditures.txt). See table chatham_budget_lines. Raw: raw/money/reports/ar-2024.*; raw/money/minutes/csb-2025-12-09-attach.pdf, .ocr.txt
6. When the board drafted the 2026-27 budget in December 2025, the SAU 9 business administrator said the new MSAD 72 and Fryeburg tuition rates were not yet available ("they should be coming out in mid December") and the draft used a projection based on the prior year's increase; in January 2026 he said the MSAD 72 invoice was "less than expected" and the budget reflected "an average from prior years."
   - citation: Chatham School Board Minutes, December 9, 2025 and January 20, 2026
   - source: https://drive.google.com/file/d/1o1qaAlttNtiHNDxgB_i1150E9lZ9Kv0w/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: December text: "Mike Wade explained that we do not have the most recent tuition rates at this time, but that they should be coming out in mid December. What is included in the draft is a projection based on the increase from last year." January text: "Mike Wade stated that they received the invoice from MSAD 72, which was less than expected. We have not received the new rates for next year yet. Therefore, the budget reflects an average from prior years." Raw: raw/money/minutes/csb-2025-12-09-attach.*, csb-2026-01-20.pdf, .txt
7. Chatham's school operating budget (the main warrant article) was $891,363 for 2017-18, between $904,603 and $951,709 from 2019-20 to 2022-23, $1,091,536 for 2023-24, $946,000 for 2024-25, $968,989 for 2025-26 and $1,291,161 for 2026-27; it rose 7.1% from 2019-20 to 2025-26 and 44.9% from 2017-18 to 2026-27 (**derived**).
   - citation: Chatham School District warrants and annual meeting minutes printed in the annual reports, 2017–2026
   - source: https://drive.google.com/drive/folders/1CggerU2PCy8oLHiypV1weX1GgCJMVptc
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Every budget article in the minutes read was "voted on and approved" without a floor change, except 2020's, where a typo ($591,709) was corrected to $951,709. See table chatham_operating_budget. Raw: raw/money/reports/ar-2017…ar-2026 (.pdf, .ocr.txt)
8. In October 2025 the SAU 9 business administrator told the Chatham board that "the biggest expenses are tuition and special education," and in December 2025 the board discussed the cost of out-of-district placements and "whether or not they go all year," noting "a lot of unknowns when predicting costs associated with placements."
   - citation: Chatham School Board Minutes, October 7, 2025 and December 9, 2025
   - source: https://drive.google.com/file/d/1eylfK2PhkPVUoVuMDa5Iy-ZS1BaXbPpk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: October text: "The biggest expenses are tuition and special education. Pam Stimpson stated that she anticipates the special education costs staying fairly stable." December text: "There was conversation about the cost of out of district placements and whether or not they go all year, the school year, or a combination. There are a lot of unknowns when predicting costs associated with placements." Raw: raw/money/minutes/csb-2025-10-07.pdf, .txt; csb-2025-12-09-attach.*
9. Chatham contracts with Bennett Transportation for buses; the 2026-27 transportation budget is $85,804 ($68,189 contracted service, $7,200 special education transport and $10,415 fuel), and the contract ends June 30, 2027, with a renewal being drafted after the contractor said he preferred a three-year term because of fuel and other changes.
   - citation: Chatham School District 2026 Annual Report, budget p. 2 of 2; Chatham School Board Minutes, December 9, 2025 and June 30, 2026
   - source: https://drive.google.com/file/d/19aFgV21YcDG4UWbR_04nqsIrvrhQIZ67/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Rows: "TRANSPORTATION,CONT SERVICE 64,400 60,570 66,203 68,189"; "TRANSPORTATION,SPECIAL ED 10,000 7,773 7,480 7,200"; "FUEL, BUSES 10,415 8,956 10,415 10,415". June 2026 text: "William Bennett stated that he preferred a three-year contract, given all of the changes in fuel, etc. The current contract expires in June 2027. Mike Wade will begin drafting a contract with Bennett." Routes and times are agent 2's area. Raw: raw/money/reports/ar-2026.*; raw/money/minutes/csb-2026-06-30.pdf, .txt
10. For 2026-27 the board budgeted for 26 elementary students and 15 high school students plus one high school "placeholder," and decided that in future years it will budget elementary tuition at 10% over the prior year while keeping at least one high school placeholder; in December 2025 it expected three graduates, two incoming kindergartners and three new ninth graders.
   - citation: Chatham School Board Minutes, January 20, 2026 and December 9, 2025
   - source: https://drive.google.com/file/d/1o1qaAlttNtiHNDxgB_i1150E9lZ9Kv0w/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: January text: "15 high school students and one placeholder. There are 26 students slated for elementary. In future years, we will only budget for 10% over last year for elementary students, but will continue to budget for at least one placeholder student at the high school." December text: "There are three students graduating this year and the District is aware of two incoming Kindergarteners. There are three high school students entering 9th grade. In the budget there is one placeholder for K-8 and one placeholder for 9-12." The 2025-26 budget included "14 students at the high school, which includes two 'ghost' students" (January 7, 2025 minutes). Raw: raw/money/minutes/csb-2026-01-20.*, csb-2025-12-09-attach.*, csb-2025-01-07.*
11. Chatham's annual reports list 26 students in grades K–8 and 14 at Fryeburg Academy for 2025-26, and between 29 and 36 in K–8 and 13 to 16 in grades 9–12 each year since 2019-20.
   - citation: Chatham School District Annual Reports 2020–2026, enrollment page
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: 2026 text: "Total K-8 ... 26 Total 9-12 ... 14 ... Total enrolled at Fryeburg Academy 14". Some pages disagree internally: the 2022 report's header says 14 in grades 9–12 but its grade rows sum to 16, and the 2025 report's header says 30 in K–8 while its grade rows sum to 29. See table chatham_students_by_level. Earlier reports list students by name; only totals are used here. Raw: raw/money/reports/ar-2020…ar-2026 (.pdf, .ocr.txt)
12. MSAD 72's April 1, 2025 enrollment count showed 28 Chatham students in grades K–8: 12 in grades K–4 at New Suncook Elementary in Lovell, 16 in grades 2–8 at the Molly Ockett School in Fryeburg, and none at Brownfield-Denmark Elementary (plus one Chatham child in Head Start pre-K, not counted).
   - citation: MSAD 72, "April 1st K-8 Enrollment by Town/School 2025," attached to Chatham School Board Minutes, June 17, 2025
   - source: https://drive.google.com/file/d/1iIVh4EDAYBrcKx2jVDhmPrmKho-3nZ1N/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Column CHTM: New Suncook K 4, 1 1, 2 3, 3 2, 4 2; Molly Ockett K 0, 1 0, 2 1, 3 1, 4 2, 5 3, 6 2, 7 4, 8 3; Brownfield Denmark 0; total 28; "Headstart Pre-K - NS" 1. Footnote: "Headstart Pre-K numbers are included for informational purposes. They are not included in total numbers for towns." Rotated scanned page; transcribed from image (viewed). The same minutes record MSAD 72's superintendent saying "There are currently 28 students across Brownfield Denmark, New Suncook, and Molly Ockett." Raw: raw/money/minutes/csb-2025-06-17.pdf, .ocr.txt (p. 5)
13. Chatham's spending per tuition student, **derived** from actual tuition lines and the annual report enrollment, was about $10,700–$12,800 per K–8 student (2022-23 to 2024-25) and about $15,300 rising to $18,900 per high school student (2022-23 to 2025-26), before any special education costs.
   - citation: Chatham School District Annual Reports 2023–2026; Summary of Expenses 2025-26 and June 2026 budget status report
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Derived: elementary $325,470 ÷ 30 = $10,849 (2022-23); $320,035 ÷ 30 = $10,668 (2023-24); $384,193 ÷ 30 = $12,806 (2024-25). High school $199,021 ÷ 13 = $15,309; $207,661 ÷ 13 = $15,974; $246,118 ÷ 13 = $18,932; $264,011 ÷ 14 = $18,858 (2025-26, spent plus encumbered by June 5, 2026). Approximate: enrollment is a fall count, while tuition is billed through the year and may include students who came or left. The district does not publish per-student rates. NH DOE's cost per pupil for Chatham is blank in the site's data. Raw: raw/money/reports/*; raw/money/agendas/ag-2026-06-09-msad72.txt
14. As a rough guide, one more high school student at about $18,900 would add about $0.18 per $1,000 to Chatham's school tax rate (about $70 a year on a $400,000 home), and one more K–8 student at about $12,800 about $0.12 per $1,000 (about $48), using the district's figure that each $1.00 on the rate raises $107,211.84 (**derived**).
   - citation: Chatham School District 2026 Annual Report, "Estimated Tax Rate" page
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "2025 Net Assessed Valuation: $107,211,838 $1.00 Increase in taxes raises: $107,211.84". Derived: 18,900 ÷ 107,211.84 = 0.176; × 400 = $70.5; 12,800 ÷ 107,211.84 = 0.119; × 400 = $47.8. Leaves out special education, transportation and changes in state aid. The state's base adequacy amount for FY2027 is $4,351 per resident pupil (library money-adequacy-aid-amounts fact 7), paid through the adequacy grant on the prior year's count. A single out-of-district special education placement can cost far more (fact 3). Raw: raw/money/reports/ar-2026.* (p. 8)
15. Chatham voters have added $20,000 a year to a Capital Reserve Fund (Special Education) since at least 2017, and $80,000 in 2026 ($40,000 from taxes and $40,000 from June 30, 2026 fund balance); the board reported about $150,000 in the fund in January 2023, $171,895.90 in December 2025 and about $191,000 in January 2026.
   - citation: Chatham School District warrants and minutes 2017–2026; Chatham School Board Minutes, January 3, 2023, December 9, 2025 and January 20, 2026
   - source: https://drive.google.com/file/d/1X7DXxpuu1v4p92UZskoEukNwRxtZLSk7/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: December 2025 text: "Mike Wade stated that in the special education trust fund has a balance of $171, 895.90, there will be $20,000 added this year." January 2026 text: "There is approximately $191,000 in the trust fund currently." 2026 Articles 7 and 8 passed (budget committee 7-1-0 on each). Exception: in January 2024 the board decided not to request reserve money for that year. Raw: raw/money/minutes/csb-2023-01-03.*, csb-2025-12-09-attach.*, csb-2026-01-20.*, csb-2024-01-02.*, am-2026-03-10.*
16. In March 2019 Chatham voters approved a $30,000 supplemental appropriation "for additional special education costs for the current school year," paid by withdrawing $30,000 from the special education capital reserve; it was handled at the regular annual meeting, not a special meeting.
   - citation: Minutes of the Chatham School District Meeting, March 12, 2019, Article 7 (2020 Annual Report)
   - source: https://drive.google.com/file/d/1NHz4gtPOjRSR84rn5a9PQ4JYmDPsTgIP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "To see if the School District will vote to raise and appropriate a supplemental appropriation of $30,000 for additional special education costs for the current school year and authorize the withdrawal of $30,000 from the Capital Reserve Fund (Special Education) created for that purpose ... Article 7 was voted on and approved as written." Raw: raw/money/reports/ar-2020.pdf, .ocr.txt (p. 8)
17. Chatham also has a Tuition Expendable Trust Fund, which held $39,595 in December 2025; the board decided in January 2024 and January 2025 not to add to it.
   - citation: Chatham School Board Minutes, December 9, 2025, January 2, 2024 and January 7, 2025
   - source: https://drive.google.com/file/d/1X7DXxpuu1v4p92UZskoEukNwRxtZLSk7/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "In the regular education tuition trust fund there is $39,595." January 2025: "The Board decided not to add anything to the tuition trust fund at this time." The annual reports' revenue pages list "Tuition Expendable Trust Fund" with no draw in the years read. Raw: raw/money/minutes/csb-2025-12-09-attach.*, csb-2024-01-02.*, csb-2025-01-07.*
18. Chatham voters authorized the district in 2018 to keep year-end unassigned funds up to 2.5% of the net assessment under RSA 198:4-b, II, usable only to reduce the tax rate or for emergencies approved by the Department of Education; the board retained $17,976 in 2023, $24,693 in 2024 and the 2.5% maximum ($14,429) in 2025, and in October 2025 discussed a warrant article to raise the limit to the 5% the law now allows.
   - citation: Minutes of the Chatham School District Meeting, 2018, Article 7 (2019 Annual Report); Chatham School Board Minutes, September 12, 2023, September 3, 2024 and October 7, 2025
   - source: https://drive.google.com/file/d/137wfqkLSgCVs3xZyNtHUPX_3DMzLHS5w/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: 2018 text: "to retain year-end unassigned general funds in an amount not to exceed, in any fiscal year, 2.5% of the current fiscal year's net assessment, in accordance with RSA 198:4-b, II. Such fund balance retained may only be used to reduce the tax rate or for emergencies to be approved by the Department of Education under RSA 32:11 ... Article 7 was voted on and approved as written." October 2025: "retain the maximum 2.5% of the total appropriation, which is $14, 429 ... districts to retain up to 5% of the net assessment with expenditures going to a public hearing ... This would be added to the warrant for voter approval." No such article was on the 2026 warrant. Raw: raw/money/reports/ar-2019.*; raw/money/minutes/csb-2023-09-12.*, csb-2024-09-03.*, csb-2025-10-07.*
19. Fryeburg Academy bills Chatham for breakfast and lunch for Chatham students as part of the tuition bills: in September 2024 the board asked the academy to keep providing meals "at no cost to the students nor their families" and to bill the district "as was done for the 2023-2024 school year," and in November 2024 it agreed to keep funding them.
   - citation: Chatham School Board Minutes, September 3, 2024 and November 5, 2024
   - source: https://drive.google.com/file/d/1yrh_q6tNqK4r-4qMl1T7NtgJdIKAcVW4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "Confirm lunches will continue to be provided for all Chatham students at no cost to the students nor their families. The board would like Fryeburg Academy to bill the Chatham School District for meals as was done for the 2023-2024 school year in the tuition bills." November: "the board will continue funding meals for Chatham students enrolled at Fryeburg Academy". Meals are agent 2's area. Raw: raw/money/minutes/csb-2024-09-03.*, csb-2024-11-05.*
20. Chatham's budgets, warrants, annual reports (2017–2026), board agendas and minutes (2010 on) and policies are posted in Google Drive folders linked from SAU 9's Chatham School Board page; each annual report contains the warrant, line-item budget, estimated revenue, estimated tax rate, special education costs, SAU 9 apportionment and enrollment.
   - citation: SAU 9, Chatham School Board page; "Policies, Agendum, Minutes and Annual Reports" and "Chatham Warrant Articles" folders
   - source: https://www.sau9.org/chatham
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Folder listing: "Agendum - Chatham", "Annual Reports - Chatham", "Minutes - Chatham", "Policies - Chatham", "Warrant Articles - Chatham" (Chatham Warrant 2019–2026). The site's DOE-25 expenditure data also has Chatham's lines (site data). Raw: raw/money/sau9/sau9-chatham.html, .txt; raw/money/drive/chatham-*-folder.html, .txt

## district-tax-and-state-aid: Chatham's Tax Bill, School Tax Rate and State Aid

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. Chatham's total tax rate fell from $16.42 per $1,000 of assessed value in 2023 to $7.09 in 2024 after a revaluation, planned with NH DRA and the town's appraiser in spring 2024, raised its assessed valuation from $59,360,330 to $104,194,928 and its equalization ratio from 68.4% to 97.7%.
   - citation: NH DRA tax rates and equalization ratios, 2023–2024 (library CSV); Town of Chatham Board of Selectmen minutes, April 11, 2024
   - source: https://www.revenue.nh.gov/about-dra/municipal-and-property-division/property-bureau/equalization
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Chatham
   - note: Kept for the reason, the revaluation, which the site's data doesn't give. Chatham's DRA rates, ratios and valuations for 2014–2025 are in the site's data (property_tax, Chatham district); these figures match it (checked November 15, 2026). Minutes text: "A revaluation meeting will be set up with Denise Roy (DRA), Rod Wood (town appraiser) and the Selectmen." Raw: raw/money/state-data/dra-tax-rates-chatham-valley.csv; raw/community/town/minutes/minutes-to-meetings-April-11-2024.txt
2. Chatham's 2024 school tax was held down by fund balance: the district's revenue for 2024-25 included $256,698 of unencumbered balance from prior years, against $70,267 in 2025-26 and none for 2026-27 (where $14,067 of retained fund balance is used instead).
   - citation: Chatham School District 2026 Annual Report, "Estimated Revenue"
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "Unencumbered Balance 256,698 70,267 0 / Retained Fund Balance PY 0 0 14,067 ... DISTRICT ASSESSMENT 465,207 663,431 1,071,021" (columns actual 2024-25, estimated 2025-26, estimated 2026-27). Page viewed. Raw: raw/money/reports/ar-2026.* (p. 7)
3. The district estimated in February 2026 that its 2026-27 school tax rate would be $11.42 per $1,000 ($9.99 for the budget, $0.37 for the reserve article and $1.06 state education), up $4.11 (56.22%) from 2025's $7.31; the district assessment was estimated at $1,071,021 after subtracting $110,753 of state education tax, a $71,320 adequacy grant and $38,067 of other revenue from the $1,291,161 budget.
   - citation: Chatham School District 2026 Annual Report, "Estimated Tax Rate"
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "2026-2027 Proposed School Board's Budget $1,291,161 Less State Educaton Taxes (Adeq. Education) -$110,753 Less State Adequacy Grant -$71,320 Less Estimated Revenues -$38,067 ... $1,071,021 $9.99 Per $1000 ... $1.06 Per $1000 ... Total Net Special Articles for Taxes $40,000 $0.37 ... ESTIMATED 2026-2027 SCHOOL TAX RATE $11.42 Per $1000 PROPOSED SCHOOL TAX RATE INCREASE $4.11 Per $1000 56.22% Incr/Decr OVER TOTAL SCHOOL TAX RATE". It is an estimate made before DRA set the 2026 rate, which was not retrieved. Chatham's DRA rates for 2014–2025 are in the site's data (property_tax, Chatham district); its 2025 local school rate of $6.37 plus state education $0.94 give the $7.31 here (checked November 15, 2026). The revenue page lists the grant as "STATE OF NH ADEQUACY GRANT ... 71,320 **95% Est."; NH DOE's October 1, 2026 calculation in the site's data (adequacy_aid, Chatham district) gives $71,319.87 for FY2027 and $110,753 of statewide tax, with the full calculation. Rotated page; transcribed from image. Raw: raw/money/reports/ar-2026.* (pp. 7–8)
4. A $1.00 increase in Chatham's tax rate raised $49,159 in 2017, according to SAU 9's 2019 study committee, and $107,211.84 on the 2025 valuation, according to the district; Chatham's is the smallest tax base in SAU 9 except Hart's Location.
   - citation: SAU 9 Study Committee Presentation, February 28, 2019, slide 28 (Jackson file, district-tax-and-state-aid 8 in `Jackson/money-and-governance.md`); Chatham School District 2026 Annual Report; SAU 9 2026-27 apportionment
   - source: https://drive.google.com/file/d/17rVLU-Ui99yNkgX6qk1FnXa93mS0MpIc/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: The 2019 figure is from the Jackson research (town/Jackson/raw/money/study/study-committee-presentation-2019-02-28.txt). The ranking is from SAU 9's 2024 equalized valuations: Chatham $109,880,009, Hart's Location $25,223,383, all others higher (table jackson_sau9_apportionment_2027). Raw: raw/money/reports/ar-2026.* (pp. 8, 13)
5. For FY2027, Chatham's equalized property value per pupil, $2,747,000, was above the $1,600,000 limit for New Hampshire's new fiscal capacity disparity aid, so Chatham received none.
   - citation: NH DOE, FY 2027 Adequacy Aid (October 1, 2026), Chatham row (library CSV); library topic money-fiscal-capacity-disparity-aid
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: CSV 2027: equalized_valuation 109880009.06; resident_adm_base 40; fiscal_capacity_disparity_aid 0. Derived: 109,880,009.06 ÷ 40 = 2,747,000.23. The $0 aid, equalized value and pupil count are in the site's data (adequacy_aid, Chatham district); value per pupil is not. Library gov-tuition-towns fact 7: a district that tuitions all its pupils gets the lesser of the regular formula or its actual current spending minus SWEPT; Chatham's spending is several times its adequacy cost, so the regular formula is the lesser (**derived**). Raw: raw/money/state-data/adequacy-aid-chatham.csv
6. State sources (the adequacy grant plus the statewide education tax) were about 22% of Chatham's 2025-26 school revenue and are estimated at about 14% for 2026-27; Chatham received no catastrophic special education aid in 2023-24 or 2024-25, and federal National Forest Reserve payments brought $29,898 in 2024-25.
   - citation: Chatham School District 2026 Annual Report, "Estimated Revenue" and "Special Education Expenses/Revenue"
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Derived: (111,416 + 98,299) ÷ 968,989 = 21.64%; (71,320 + 110,753) ÷ 1,291,161 = 14.10%. Special education page: "Special Education Aid $0 $0 ... NH State Adequacy Allocation $4,188 $22,384". Revenue page: "National Forest Reserve 29,898 15,326 14,500". The grant and statewide tax figures equal NH DOE's FY2026 and FY2027 figures in the site's data (adequacy_aid, Chatham district); the "NH State Adequacy Allocation" equals DOE's special education differentiated aid for FY2024 and FY2025. Chatham has no row in NH DOE's special education aid files for FY2021-FY2026 (site data: special_education_aid). Catastrophic aid rules: library money-special-education-aid. Raw: raw/money/reports/ar-2026.* (pp. 7, 12)
7. Chatham voters approved Question 2, the school tax cap under RSA 32:5-i, on November 3, 2026, by 114 to 51 (69.1% yes, unofficial), above the 60% needed; a cap approved in 2026 first applies to the 2027-28 (FY2028) budget and can be overridden by a three-fifths ballot vote at the annual meeting.
   - citation: site data (district_question_two, Chatham, 2026, unofficial); library topics budget-hb-1300-school-tax-cap (facts 4, 9–11) and budget-question-2-2026-results
   - source: https://gc.nh.gov/bill_status/legacy/bs2016/billText.aspx?sy=2026&id=2080&txtFormat=html
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Query row: "91 | 2026 | 114 | 51 | 69.10 | t | Chatham | f" (is_official false). The Ask can fetch this from the site's data; it is noted here because it limits future budgets. Results are not final until certified. An October 2026 NHSBA and NHSAA guide in the board's packet explains the cap. Raw: raw/money/agendas/ag-2026-10-13.pdf, .txt, .ocr.txt

## district-tuition-contracts: Chatham's Tuition Arrangements with MSAD 72 and Fryeburg Academy

- kind: local
- question_type: governance_money
- description: A district's tuition contracts and agreements with other districts and schools: terms, cost formulas, caps, length, renewal, transportation and special education

1. No written tuition agreement between Chatham and MSAD 72 or between Chatham and Fryeburg Academy was found posted: SAU 9's Tuition Agreement Overview lists contracts for other SAU 9 districts but none for Chatham, Chatham's Drive folders hold no contract, and no warrant article on such an agreement appears in Chatham's warrants for 2017–2026.
   - citation: SAU 9, "Tuition Agreement Overview"; Chatham School District Drive folders; warrants in the 2017–2026 annual reports
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: The tuitions page lists K-6, 7-8 and 9-12 contracts for Albany, Bartlett, Eaton, Freedom, Hale's Location, Hart's Location, Jackson, Madison and Tamworth, plus Jackson & Fryeburg Academy (2027). A "not found" statement about the documents searched. Raw: raw/money/sau9/sau9-tuitions.html, .txt; raw/money/drive/*.txt; raw/money/reports/*
2. Chatham's policies say its "K-12 program is provided through Tuition Agreements with MSAD #72 and Fryeburg Academy," that "Chatham students attend schools that are part of MSAD #72," and that "the high school of record is Fryeburg Academy."
   - citation: Chatham School Board Policy JECC, School Choice (adopted June 14, 2017); Policy JECA, Manifest Educational Hardship (revised February 3, 2016)
   - source: https://drive.google.com/file/d/1D7nfX5oLUqeMkG1pNPfTpsIGiYRw-9l8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: JECC text: "A K‐12 program is provided through Tuition Agreements with MSAD #72 and Fryeburg Academy." JECA text: "Chatham students attend schools that are part of MSAD #72. The high school of record is Fryeburg Academy." JECA source: https://drive.google.com/file/d/1auYiq3BO4t0IpGJ2oyxxAuTqaG0RmF0H/view. Raw: raw/money/policies/policy-JECC.pdf, .txt; policy-JECA.pdf, .txt
3. Chatham's elementary tuition contract with MSAD 72 was extended by a rider through June 30, 2021, which the board chair signed in January 2016; in 2019–2020 the board sought a further extension and was told a "rider" would follow, and in November 2022 the minutes say "currently there is a year to year agreement" and that a multi-year agreement would need a district meeting warrant article.
   - citation: Chatham School Board Minutes, November 10, 2015, January 19, 2016, November 5, 2019, February 5, 2020 and November 1, 2022
   - source: https://drive.google.com/file/d/14UL_eH1z0KvIhzS_2JZ6d3hyTYAnVwH5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: 2016 text: "Signing of Tuition Contract with MSAD #72 – Sue Perry signed a rider to the tuition contract with MSAD #72 extending it through June 30, 2021." 2020 text: "Discussions with MSAD #72 will continue, and a 'rider' to the current contract will be presented at a later date." 2022 text: "The tuition agreements between Chatham and MSAD 72 need to get updated as currently there is a year to year agreement. If there is a multi-year agreement there will need to be a warrant article for the annual school district meeting." No later minutes read record a new agreement. Raw: raw/money/minutes/csb-2015-11-10.*, csb-2016-01-19.*, csb-2019-11-05.*, csb-2020-02-05.*, csb-2022-11-01.*
4. MSAD 72's own policy JFAB (adopted May 7, 2025) lets its superintendent accept non-resident students "under an agreement with another local school administrative unit," and says tuition will be charged retroactively for students found to be nonresidents and ineligible.
   - citation: MSAD 72 Policy JFAB, Admission of Non-Resident Students
   - source: https://docs.google.com/document/d/1v79vcT-MnGqZ9RUfwshWz2N4wuC-31wWU3OkJxy0O20/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Text: "Individual non-resident students may be accepted under any of the following conditions if approved by the Superintendent: 1. Under an agreement with another local school administrative unit ... Retroactive tuition will be assessed for students found to be nonresidents and ineligible for enrollment under law or Board policy ... Adopted: 5/7/2025". Linked from the MSAD 72 policies page. Raw: raw/money/maine/msad72-policy-JFAB.txt; raw/money/maine/msad72-policies.html, .txt
5. MSAD 72 counts Chatham's tuition as revenue in its own budget: it budgeted $293,164.80 for 32 Chatham students in FY2022, $307,367.61 for 33 in FY2023, $300,732.55 for 31 in FY2024 and $285,650.55 for 27 in FY2025, about $9,200 to $10,600 per student (**derived**), plus a smaller "Transportation Chatham" revenue line ($3,773, $13,142.50 and $6,500 in FY2023–FY2025).
   - citation: MSAD 72 budget documents, "Revenues" FY22–FY25
   - source: https://drive.google.com/file/d/1aH2CShsKGiT4vJu3FXrPl_x3ym_dy-OM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: FY25 text: "Tuition: Chatham, NH (27) ($ 285,650.55) ... Transportation Chatham ($ 6,500.00)". FY24: "Chatham, NH (31) ($ 300,732.55) ... Transportation Chatham ($ 13,142.50)". FY23 (scanned; transcribed from image): "Chatham, NH (33) 307,367.61 ... Transportation Chatham 3,773". FY22: "Chatham, NH (32) 293,164.80". Derived per student: $9,161.40, $9,314.17, $9,701.05, $10,579.65. These are MSAD 72's budget estimates. Chatham's actual elementary tuition was higher ($320,035 in 2023-24; $384,193 in 2024-25), and the documents read do not explain the difference. See table chatham_msad72_tuition_revenue. Raw: raw/money/maine/msad72-fy22-revenues.*, msad72-fy23-revenues.* (incl. .ocr.txt), msad72-fy24-revenues.*, msad72-fy25-revenues.*
6. Maine DOE's legal elementary tuition rate for MSAD 72 for 2025-26 is $13,331.89 per pupil, its 2024-25 K–8 operating expense ($9,312,324.24) divided by its K–8 attending enrollment (698.5).
   - citation: Maine DOE, School Finance, "FY26 Elementary Public Tuition Rates by SAU" (report generated December 9, 2025)
   - source: https://www.maine.gov/doe/sites/maine.gov.doe/files/inline-files/School%20Finance%20-%20FY26%20Elementary%20Public%20Tuition%20Rates%20by%20SAU%20-%2012.12.2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Row text: "RSU 72/MSAD 72 $9,312,324.24 698.5 $13,331.89" under columns "2024 - 25 Operating Expense K-8 / Attending Enrollment / 2025 - 26 Elementary Tuition Rate". The state total row is $13,077.51. This is the Maine rate under 20-A §5804 (cross-state-school-tuition-rules fact 2). Whether Chatham's agreement uses it was not found. Raw: raw/money/maine/me-doe-fy26-elem-tuition.pdf, .txt
7. MSAD 72's bond for the Molly Ockett School addition costs $1,280,096 in debt service in FY2027, and beginning that year the State of Maine pays the full principal and interest, where before Denmark, Lovell and Stoneham had paid most of it.
   - citation: MSAD 72 Budget Review FY27, "Debt Service"; FY27 Frequently Asked Budget Questions
   - source: https://drive.google.com/file/d/1F26MB3ms_dD6ea8sHNo_bprw3SUGoowo/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Text: "Debt Service 1,301,081.44 1,280,095.64 -20,986 -1.6% ... Beginning in FY27 ... the Principal and Interest payments for major capital projects are fully paid by the State ... instead of Denmark, Lovell, and Stoneham paying the bulk of the debt service on the bond that is paying for the Molly Ockett addition, the entire $1,280,096 will be paid by the State." Whether any debt service factor is in Chatham's tuition was not found. Q&A: https://drive.google.com/file/d/18Ag-l4frUVOlSvUZGglbb4YVxAwWx27p/view. Raw: raw/money/maine/msad72-fy27-debt.pdf, .txt; msad72-fy27-qa.pdf, .txt
8. MSAD 72's school board has set up an ad hoc committee on the long-term future of Brownfield-Denmark Elementary School, due to make a "fact-based recommendation by December 2026" on options "from maintaining current operations to significant restructuring or closure"; MSAD 72's April 2025 count showed no Chatham students at that school.
   - citation: MSAD 72, "Future of BDES" page; MSAD 72 April 1, 2025 enrollment by town (Chatham minutes, June 17, 2025)
   - source: https://www.msad72.org/information/school-board/future-of-bdes
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Page text: "The school board has established an ad hoc committee to determine the long-term future of Brownfield Denmark Elementary School (BDES). This committee is tasked with providing a fact-based recommendation by December 2026, weighing options that range from maintaining current operations to significant restructuring or closure." The study itself is agent 1's area. Raw: raw/money/maine/msad72-future-of-bdes.html, .txt; raw/money/minutes/csb-2025-06-17.*
9. Under Maine's private-school tuition law, the most a Maine school unit must pay Fryeburg Academy for 2025-26 before the "insured value factor" (a capital allowance) is $15,055.22 per student, the state average public secondary rate, the same cap as most Maine academies; MSAD 72 says its own contract with Fryeburg Academy pays more than the state's funding model recognizes.
   - citation: Maine DOE, "FY21-FY26 Secondary Private School Tuition Rates" (October 7, 2026); MSAD 72 FY27 Frequently Asked Budget Questions
   - source: https://www.maine.gov/doe/sites/maine.gov.doe/files/inline-files/School%20Finance%20-%20FY21-FY26%20Secondary%20Private%20School%20Tuition%20Rates%20-%2010.7.2026.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Row text: "Fryeburg Fryeburg Academy $15,055.22 $14,080.88 $ 14,098.13 $ 13,312.43 $ 12,480.36 $ 11,951.60" (2025-26 back to 2020-21). MSAD 72 Q&A: "we pay higher secondary tuition costs as part of our contract with Fryeburg Academy, which exceed the costs recognized within EPS." The rule is cross-state-school-tuition-rules fact 4. Chatham's own Fryeburg rate was not found; its 2025-26 spending was about $18,858 per student (district-budget-and-cost fact 13, **derived**). Fryeburg's posted commuter day rates are in the Fryeburg file (agent 3) and the Jackson file (district-tuition-contracts 13–20 in `Jackson/money-and-governance.md`). Raw: raw/money/maine/me-doe-fy21-fy26-sec-private-tuition.pdf, .txt; msad72-fy27-qa.*
10. For comparison, Jackson's new Fryeburg Academy agreement (2027–2037) sets tuition at the academy's commuter day rate plus a "guaranteed admission premium" of up to 20%, keeps special education outside tuition and leaves daily transportation to Jackson; Chatham's terms with the academy were not found.
   - citation: Jackson file, district-tuition-contracts 13–16 in `Jackson/money-and-governance.md` and district-transportation 2 in `Jackson/money-and-governance.md`
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Pointer to the Jackson research (town/Jackson/money-and-governance.md); no Chatham-specific term is implied. Chatham's budget pays its own bus contract (district-budget-and-cost fact 9).

## high-school-tuition-options: High School Choices for Chatham Students

- kind: local
- question_type: local_practice
- description: High school options for districts without a high school (already in `additional-data/district-practices.md`)

1. Fryeburg Academy, a private academy in Fryeburg, Maine, is the Chatham School District's high school of record, and 14 Chatham students were enrolled there in 2025-26; the academy asks Chatham residents to bring a letter from the Chatham town office confirming residency to enroll.
   - citation: Chatham Policy JECA; Chatham School District 2026 Annual Report, enrollment; Fryeburg Academy, "Day Students" page
   - source: https://www.fryeburgacademy.org/admissions/how-to-apply/day-students
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Fryeburg page text: "Albany, Maine + Chatham, New Hampshire Residents ... Residents who choose to attend Fryeburg Academy, please obtain a letter from the Chatham or Albany town office confirming your residency ... Non-MSAD 72 Towns: Albany Township and Chatham, New Hampshire". This fills the library's missing "HS options" entry for Chatham (district-practices coverage table). Admissions details are agent 3's. Raw: raw/money/sau9/fa-day-students.html, .txt; raw/money/policies/policy-JECA.*; raw/money/reports/ar-2026.*
2. Under Chatham's School Choice policy (JECC), a family may send a child to "another publically approved school within SAU #9," such as Kennett High School, and Chatham will reimburse the actual tuition up to the current MSAD 72 or Fryeburg Academy tuition; the family pays any remaining tuition and provides transportation, and requests go to the SAU 9 superintendent by May 1 of the year before, who reviews them for class size and capacity.
   - citation: Chatham School Board Policy JECC, School Choice (adopted June 14, 2017)
   - source: https://drive.google.com/file/d/1D7nfX5oLUqeMkG1pNPfTpsIGiYRw-9l8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "If the parent/guardian should choose to send their child to another publically approved school within SAU #9, the Chatham School District will reimburse the actual costs of current tuition charge up to but not exceeding the current school tuition fee of MSAD #72 and Fryeburg Academy. The parent/guardian will be responsible for the remaining tuition. Transportation will be the responsibility of the parent/guardian or student. Requests for school choice outside of MSAD #72 and Fryeburg Academy need to be submitted to the Superintendent of Schools of SAU #9 by May 1 of the preceding year." Adopted at the June 14, 2017 board meeting, 2-0-0. How many Chatham students have used it was not found. Raw: raw/money/policies/policy-JECC.*; raw/money/minutes/csb-2017-06-14.pdf, .txt
3. Chatham's Manifest Educational Hardship policy (JECA) lets a parent ask in writing to have a student reassigned to another public school under RSA 193:3; the board hears the request in nonpublic session, a program-based request must show the program is "essential for student success" or for college, "perceived quality of any program is not a satisfactory reason" if the assigned school is approved or accredited, and decisions can be appealed to the State Board of Education.
   - citation: Chatham School Board Policy JECA, Manifest Educational Hardship (adopted July 29, 1998; revised February 3, 2016)
   - source: https://drive.google.com/file/d/1auYiq3BO4t0IpGJ2oyxxAuTqaG0RmF0H/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "Any program related requests must include documentation that a program not offered at the assigned school is essential for student success or is essential for the student to qualify for college. Perceived quality of any program is not a satisfactory reason if the assigned school has approval status from the State of New Hampshire, the State of Maine, of if the New England Association of Schools and Colleges accredits the school ... Parents/guardians aggrieved by the decision of the Board may appeal to the State Board of Education." The statewide rule is library topic change-of-school-assignment. Raw: raw/money/policies/policy-JECA.*
4. No Chatham tuition contract with the Conway School District for Kennett High School is posted on SAU 9's tuition page, and in September 2021, when the Kennett agreements of other towns were nearing their end, the superintendent noted that "Chatham is currently happy with the arrangement with Fryeburg Academy and MSAD 72."
   - citation: SAU 9 "Tuition Agreement Overview"; Chatham School Board Minutes, September 7, 2021
   - source: https://drive.google.com/file/d/1OCBwLgJ16l_0Ikaxa-ezga-HbcmouObF/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Minutes text: "The tuition agreements in Conway will expire in a few years and the sending towns and Conway are beginning to explore educational options. Chatham is currently happy with the arrangement with Fryeburg Academy and MSAD 72." In November 2024 board members were told of a "Tuition Contracts Roundtable with the Conway School Board" (November 5, 2024 minutes); no Chatham action followed in the minutes read. Raw: raw/money/minutes/csb-2021-09-07.*, csb-2024-11-05.*; raw/money/sau9/sau9-tuitions.*
5. At the March 10, 2026 district meeting, Chatham voters adopted RSA 194-D open enrollment on terms that admit 0 students from outside the district and limit Chatham resident K–12 students "attending open enrollment schools located outside of the Chatham School District and outside of existing tuition agreements" to 0% (board 3-0-0; budget committee 7-1-0).
   - citation: Chatham School District Warrant 2026, Article 9; Annual Meeting Minutes, March 10, 2026
   - source: https://drive.google.com/file/d/12d447FkkJAe8DQZQlbcpWbWmgR_MY8Au/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Warrant text (page 2 image, read): "to admit 0 students from outside the Chatham School District and further to limit the percentage of Chatham resident students attending open enrollment schools located outside of the Chatham School District and outside of existing tuition agreements to 0% of the District's total enrollment of resident students in grades K-12." Minutes: "Article 9 was voted on and approved." Under RSA 194-D:3, I(e), it took effect July 1, 2026. The 2026-27 budget has a $1 "Tuition, Open Enrollment" placeholder line. Raw: additional-data/raw/districts/batch-1/chatham-warrant-2026-p2.png; raw/money/minutes/am-2026-03-10.*; raw/money/rsa/rsa-194-D-mrg.*
6. Bartlett (25 outside students in K–8) and Conway (20 each in K–2, 3–5 and 6–8, and 50 in grades 9–12) both adopted open enrollment for outside students in spring 2026, but with Chatham's 0% limit a Chatham student cannot use RSA 194-D open enrollment to attend them; Chatham's own School Choice policy (fact 2) remains a separate, partly paid route within SAU 9.
   - citation: Conway School District Annual School Election, April 14, 2026, Article 13; Bartlett file, high-school-tuition-options fact 6; RSA 194-D:3, I(c)
   - source: https://gc.nh.gov/rsa/html/XV/194-D/194-D-3.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Conway ballot text: "to admit 20 students from outside the Conway School District to grades K-2, 20 students ... to grades 3-5, 20 students ... to grades 6-8, and 50 students from outside the Conway School District to grades 9-12 ... (1107 Yes / 485 No)". RSA 194-D:3, I(c)(1): a district "shall impose limitations on the number of its resident pupils who may attend open enrollment schools located inside and outside the school district." That the two routes combine this way is our reading of the policy and the vote. Under RSA 194-D:5, I the sending district pays at least 80% of its average cost per pupil. Raw: raw/money/sau9/conway-school-election-results-2026-p2.png; raw/money/rsa/rsa-194-D-mrg.*
7. In November 2015 the Chatham board voted 0-2-0 against a motion to consider authorizing tuition payments to private schools, and no later action to pay tuition to private schools other than Fryeburg Academy was found in the minutes read.
   - citation: Chatham School Board Minutes, November 10, 2015
   - source: https://drive.google.com/file/d/17BQmy4t6jdbyu2cPQDXlLyYCKF3we3iQ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "Consider Student Tuition to Private School – Sue Perry moved to consider authorizing tuition payments to private schools. The motion was seconded by Jane Lounsbury and failed by a vote of 0-2-0." RSA 189:1-a, IV now lets a board contract with an approved nonpublic school where it has no public school at the pupil's grade level and the board decides it is in the pupil's best interest. Raw: raw/money/minutes/csb-2015-11-10.*; raw/money/rsa/rsa-189-1-a.*

## district-special-education-services: Special Education for Chatham Students: Who Pays and Who Manages It

- kind: local
- question_type: local_practice
- description: Who provides special education and related services in a district (on staff or contracted), reading specialists, 504 practice, IEP moves between schools, and out-of-district placements

1. The Chatham School District pays for its students' special education: its 2026-27 budget has $398,139 for special education tuition (out-of-district placements), $3,500 for contracted special education services, $1,000 for extended school year services, $9,481 for speech, $8,861 for occupational therapy, $2,032 for psychological services and $7,200 for special education transportation.
   - citation: Chatham School District 2026 Annual Report, "2026-2027 Proposed Budget"
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Rows: "CONTR SERV, SPECIAL EDUCATION ... 3,500"; "CONTR SERV, ESY SPEC EDUC ... 1,000"; "TUITION, SPECIAL EDUCATION ... 398,139"; "PSYCHOLOGICAL SERVICES ... 2,032"; "SPEECH SERVICES ... 9,481"; "OCCUPATIONAL THERAPY ... 8,861"; "TRANSPORTATION,SPECIAL ED ... 7,200". Who delivers the services at MSAD 72 is agent 1's area. Raw: raw/money/reports/ar-2026.*
2. Chatham's actual special education spending was $233,390 in 2023-24 and $193,755 in 2024-25, against special education revenue of $4,188 and $22,384 (all from the NH adequacy allocation; no catastrophic aid or Medicaid).
   - citation: Chatham School District 2026 Annual Report, "Special Education Expenses/Revenue 2023-2024, 2024-2025"
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "Tuition, Special Education $175,205 $155,649 ... TOTAL SPECIAL EDUCATION EXPENSES $233,390 $193,755 ... Special Education Aid $0 $0 / NH State Adequacy Allocation $4,188 $22,384 / Medicaid Reimbursement $0 $0". Earlier reports: $316,425 (2022-23) and $243,952 (2021-22). The adequacy allocation equals NH DOE's special education differentiated aid for Chatham in FY2024 ($4,188.24) and FY2025 ($22,383.90) in the site's data (adequacy_aid); Chatham has no row in NH DOE's special education aid files for FY2021-FY2026 (site data: special_education_aid). Raw: raw/money/reports/ar-2026.* (p. 12); ar-2025.*
3. SAU 9's director of student services manages Chatham's special education budget and reports to the Chatham board: in January 2025 she described "out of district placements and episodes of treatment as they relate to budget impact" and said a roughly $100,000 drop in special education costs reflected "real students and actual service needs."
   - citation: Chatham School Board Minutes, January 7, 2025
   - source: https://drive.google.com/file/d/18Br9zX528IhyV6acwg8wEReghQkxCPF3/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "There has been a shift in special education services reflecting a decrease of approximately $100,000.00. Psychological and speech services have decreased slightly. All of these figures are based on real students and actual service needs ... Pam Stimpson described out of district placements and episodes of treatment as they relate to budget impact." The 2026 annual report lists her title as Director of Student Services. Raw: raw/money/minutes/csb-2025-01-07.*; raw/money/reports/ar-2026.* (p. 1)
4. Chatham's federal special education (IDEA) money is combined with Conway's and Eaton's through a "consolidated agreement" the board approves each year; the board was told in June 2025 that Chatham's IDEA grant for 2025-26 was $10,363 and its preschool IDEA grant $1,300.
   - citation: Chatham School Board Minutes, September 10, 2013 through April 6, 2021 (consolidated agreements); June 17, 2025
   - source: https://drive.google.com/file/d/1iIVh4EDAYBrcKx2jVDhmPrmKho-3nZ1N/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: April 2021 text: "Acceptance of Consolidated Agreement- Motion by Sue Crowley, seconded by Sue Perry to approve the IDEA Special Education grants along with the Towns of Conway and Eaton passed 2-0-0." June 2025 text: "Pam Stimpson shared that IDEA grant for next year is $10, 363, pre-K IDEA is $1,300." Raw: raw/money/minutes/csb-2021-04-06.*, csb-2025-06-17.*
5. In June 2026 the SAU 9 director explained a bill from Northeast Woodland Chartered Public School in Conway for special education support shared with a Chatham student, saying a staffing gap in November had caused a lapse in services and a state review, and that she was working with the NH Department of Education and the school to provide compensatory services.
   - citation: Chatham School Board Minutes, June 30, 2026
   - source: https://drive.google.com/file/d/19aFgV21YcDG4UWbR_04nqsIrvrhQIZ67/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "A question was raised regarding a bill from Northeast Woodlands Public Chartered School. Pam Stimpson explained that this was a result of shared special education support provided to a Chatham student. Pam explained that there was a staffing issue in November, which caused a lapse in service and also prompted a due diligence review by the state. Pam is working closely with the department of education and with the charter school to provide compensatory services as needed to certain students." Charter school special education rules changed in 2026 (library choice-charter-district-special-education). Raw: raw/money/minutes/csb-2026-06-30.*
6. Chatham's policy DK reimburses parents of a student in an out-of-district special education placement at the federal mileage rate for set trips: the start and end of the program and of extended school year, school closures on the placement's calendar, IEP meetings, approved evaluator appointments, and other trips approved by the superintendent and board, with claims due within a month and by June 30.
   - citation: Chatham School Board Policy DK, Reimbursement for Special Education Travel (adopted November 14, 2005)
   - source: https://drive.google.com/file/d/1iXw0cFG2jem4_-2mvW_XXH39_OBM0SDy/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "The Chatham School District is financially responsible for the following reimbursable transportation costs to the parents/guardian of an out-of-district placed special needs student. The federal rate of mileage reimbursement for transportation will be used ... Requests for reimbursements should be received in the SAU #9 office within one month of travel. No requests for reimbursements will be accepted after June 30th of each year." Raw: raw/money/policies/policy-DK.pdf, .txt
7. Chatham's hardship policy requires that any reassignment of "an educationally handicapped student" include a recommendation from a placement team that included a Chatham representative, and MSAD 72's special education director reports to the Chatham board at its yearly joint meeting.
   - citation: Chatham Policy JECA; Chatham School Board Minutes, June 1, 2022, June 6, 2023 and June 17, 2025
   - source: https://drive.google.com/file/d/1auYiq3BO4t0IpGJ2oyxxAuTqaG0RmF0H/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: JECA text: "Any consideration for an educationally handicapped student must include a recommendation from a placement team that included a Chatham representative." June 2025: "Pat Menzel gave a special education update." The documents read do not say which agency's staff conduct evaluations of Chatham students at MSAD 72. Raw: raw/money/policies/policy-JECA.*; raw/money/minutes/csb-2022-06-01.*, csb-2023-06-07.*, csb-2025-06-17.*

## district-sau-governance: Chatham's Place in SAU 9

- kind: local
- question_type: governance_money
- description: How a district shares an SAU: board seats and votes, how SAU costs are divided, and what the local board decides versus the SAU

1. Chatham is a single-town school district: NH DOE lists it as one, and NH law makes each town a school district whose board must provide elementary and secondary education "at district expense" to all resident pupils, even where, as in Chatham, the district operates no school.
   - citation: NH DOE valuations report (library school-tax-by-town.csv, doe_row_type); RSA 189:1-a, I; library topic gov-school-district
   - source: https://gc.nh.gov/rsa/html/XV/189/189-1-a.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Chatham
   - note: CSV text: "Chatham,91,2025,2025-26,CHATHAM,91,single-town school district". RSA text: "It shall be the duty of the school board to provide, at district expense, elementary and secondary education to all pupils who reside in the district until such time as the pupil has acquired a high school diploma or has reached age 21". Raw: raw/money/state-data/school-tax-by-town-chatham.csv; raw/money/rsa/rsa-189-1-a.*
2. Every NH district must receive "superintendent services" through an SAU, including business administration, special education compliance, transportation, budgeting and the school calendar (library gov-sau fact 2); for Chatham, SAU 9's superintendent, business administrator and director of student services prepare its budget, manage its contracts and special education, and attend its board meetings.
   - citation: RSA 194-C:4; library topic gov-sau; Chatham School Board Minutes 2024–2026 (attendance lines)
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-4.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Attendance lines, e.g. April 7, 2026: "Attendance: Sue Perry, Sue Crowley, Beverly Aiman, Aimee Frechette, Pam Stimpson, Mike Wade" (the last three SAU 9 staff). Raw: raw/money/minutes/csb-2026-04-07.*; raw/money/rsa/rsa-194-C-mrg.*
3. Chatham pays 0.71% of SAU 9's 2026-27 budget ($19,694 of $2,761,283), all of it based on property value: SAU 9 splits costs half by average daily membership and half by equalized value, and Chatham, with no school of its own, has 0 membership and 1.43% of the value.
   - citation: "Proposed School District Apportionment for the School Administrative Unit #9 Budget 2026-2027," Chatham School District 2026 Annual Report
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Row text: "Chatham 109,880,009 0.00 1.43% 0.00% 0.71% $19,694". Chatham's share was 0.7828% ($13,385) in 2021-22, 0.7287% ($14,048) in 2022-23, 0.65% ($12,717) in 2024-25 and 0.65% ($15,073) in 2025-26. See table chatham_sau9_share and the Jackson file's jackson_sau9_apportionment_2027. Raw: raw/money/reports/ar-2026.* (p. 13), ar-2022.*, ar-2024.*, ar-2025.*
4. Chatham's board chair asked in January 2026 how Chatham pays for SAU services it "does not technically receive," and the business administrator said Chatham's contribution is based on equalized valuation because it has no students in SAU 9 schools and that the apportionment is set by statute; in January 2025 she asked whether SAU services not related to Chatham could be separated, and the SAU said it would look into it.
   - citation: Chatham School Board Minutes, January 20, 2026 and January 7, 2025
   - source: https://drive.google.com/file/d/1o1qaAlttNtiHNDxgB_i1150E9lZ9Kv0w/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: 2026 text: "Sue Perry asked about the SAU budget and how Chatham pays for services they do not technically receive. Mike Wade explained that Chatham's contributions are based on Equalized Valuation, as they do not have students that attend our schools. The SAU apportionment is per RSA." 2025 text: "Sue Perry asked if there was a way to separate the SAU services that do not pertain to Chatham. The SAU will continue to investigate this". In December 2025 the board was told moving two Conway technology positions into the SAU budget would raise Chatham's share by about $2,000. Raw: raw/money/minutes/csb-2026-01-20.*, csb-2025-01-07.*, csb-2025-12-09-attach.*
5. Chatham's three school board members are also members of the SAU 9 board, where Chatham holds 3 of 29 seats (about 10%) but one vote of 13 under RSA 194-C:7, because districts that run no schools get one vote (**derived** in the Jackson research).
   - citation: Jackson file, jackson_sau9_board_seats_and_votes and district-sau-governance 6–8 in `Jackson/money-and-governance.md`; RSA 194-C:7
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-7.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Pointer to the Jackson tables, which list Chatham with 3 seats, 1 statutory vote, resident ADM 40 and weighted votes "not computed". Derived: 3 ÷ 29 = 10.3%; 1 ÷ 13 = 7.7%. Not redone here.
6. The SAU 9 board as a whole fixes the salaries of all SAU staff, divides their cost among the districts and has the authority to remove the superintendent and other administrators; Chatham's members take part in those decisions through the SAU board, and in 2023 Chatham's chair asked to be involved in the search for a new SAU 9 superintendent.
   - citation: RSA 194-C:5, III; Chatham School Board Minutes, June 6, 2023
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-5.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Statute: "The school board of each school administrative unit shall fix the salaries of all school administrative unit personnel, shall apportion the expense ... The school administrative unit board shall have the authority to remove superintendents and other administrators." Minutes: "Kevin Richard updated the board on the SAU 9 superintendent search that is beginning at this time. Sue Perry is interested in being involved with the process." Whether she joined the search was not found. Raw: raw/money/rsa/rsa-194-C-mrg.*; raw/money/minutes/csb-2023-06-07.*
7. No Chatham board member was listed as present at the SAU 9 board meetings of July 9 and September 10, 2026, and the Chatham board's September 8, 2026 agenda included an item on "Executive Committee & SAU #9 School Board Attendance."
   - citation: SAU 9 School Board Minutes, July 9, 2026 and September 10, 2026 (draft); Chatham School Board Agenda and Minutes, September 8, 2026
   - source: https://drive.google.com/file/d/1su4GmOnY3WshgAln8zu3bWZwrcYv8NtL/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: July attendance: "Melanie Lebel, Andrew Light, Kristin Stelmok, Sarah Burke, Heather Forbes, Randy Davison, Tom Seidel, Jessica DellaValla, Nicole Auth, Emily Calderwood" plus SAU staff; September attendance is quoted in the Jackson file (district-sau-governance 9 in `Jackson/money-and-governance.md`). The Chatham minutes record no discussion under the item. Only these two SAU meetings were checked. Raw: raw/money/sau9/sau9-2026-07-09.*, sau9-2026-09-10-draft-attach.*; raw/money/agendas/ag-2026-09-08-attach.*
8. Starting with the March 9, 2027 district meeting, Chatham voters will vote on SAU 9's budget as a separate warrant article under HB 564, with votes pooled across all SAU 9 districts; in October 2026 the Chatham board discussed whether the article's wording can state Chatham's own share of the full SAU budget.
   - citation: Chatham School Board Minutes (draft), October 13, 2026; library topic budget-sau-budget-vote (facts 1–3)
   - source: https://drive.google.com/file/d/1L3K4PO3zbSLmrGKbRlXNT45GnSw8ywCi/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "Aimee Frechette explained HB 1300 and HB 564. The formula for calculating the tax caps was discussed by the Board. The warrant article for the SAU budget at the annual meeting was discussed. The language of the warrant relative to HB 564 was discussed in terms of whether we can state Chatham's specific apportionment of the full SAU budget." Draft minutes. Raw: raw/money/minutes/csb-2026-10-13-draft.*; raw/money/agendas/ag-2026-10-13.*

## district-board-and-public-input: Chatham School Board Meetings and How Residents Take Part

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. The Chatham School Board has three members elected at the annual district meeting for three-year terms (Susan Perry, chair, to 2029; Susan Crowley, vice chair, to 2027; Beverly Aiman, to 2028), and voters also elect a clerk, treasurer, auditor and moderator.
   - citation: SAU 9, Chatham School Board page; Chatham School District Annual Meeting Minutes, March 10, 2026
   - source: https://www.sau9.org/chatham
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "Susan Perry Chatham Board Chairperson Term Expires 2029 ... Susan Crowley Chatham Vice-Chairperson Term Expires 2027 ... Beverly Aiman Chatham Board Member Term Expires 2028 ... Stephen Fink School Treasurer ... Sheryl Emery School Clerk ... Ronald Briggs School Moderator ... Maryann Eastman Auditor". The page also links each member's SAU 9 email. Raw: raw/money/sau9/sau9-chatham.*; raw/money/minutes/am-2026-03-10.*
2. SAU 9's page says the Chatham board meets "on the first Tuesday of every other month at 9:00 a.m. at the SAU #9 Office," but in December 2025 the board agreed to move future meetings to 9:30 a.m., confirmed at its April 2026 reorganization, and its September, October and December 2026 meetings were set for the conference room at Kennett High School.
   - citation: SAU 9 Chatham School Board page; Chatham School Board Minutes, December 9, 2025, April 7, 2026, September 8, 2026 and October 13, 2026 (draft)
   - source: https://drive.google.com/file/d/1Rb1xChTQvwOEM9vGIQD1STnHXYnrN9Tu/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: December 2025: "The Board agreed to move all future meetings to 9:30am instead of 9:00am." April 2026: "The Board agreed to continue to meet on the first Tuesday every other month at 9:30am in the SAU9 conference room." September 2026 heading: "Tuesday, September 8, 2026 at 9:30 a.m. Conference Room at Kennett High School"; October: "Chatham School Board - Tuesday, December 8, 2026 at 9:30 a.m. ... will be held at Kennett High School." The Town of Chatham's school board page also still says 9:00 a.m. (raw/money/town/chathamnh-school-board.*). Raw: raw/money/minutes/csb-2025-12-09-attach.*, csb-2026-04-07.*, csb-2026-09-08.*, csb-2026-10-13-draft.*; raw/money/sau9/sau9-chatham.*
3. The budget hearing and the district meeting are evening meetings in Chatham: the Municipal Budget Committee holds the public hearing on the school budget at the Chatham Town Hall (February 4, 2026 at 5:30 p.m.; next on February 9, 2027 at 6:30 p.m.), and the annual district meeting, where voters act on the budget, is at the Town Hall at 6:00 p.m. (next on March 9, 2027).
   - citation: Chatham School Board Minutes, January 20, February 4 and October 13, 2026 (draft)
   - source: https://drive.google.com/file/d/1L3K4PO3zbSLmrGKbRlXNT45GnSw8ywCi/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: October 2026 text: "Filing Dates for Office - Wednesday, January 20 - Friday, January 29, 2027 / Last Date for Petitioned Articles - Friday, February 5, 2027 / Budget Hearing - Tuesday, February 9, 2027 at 6:30 p.m. / Annual Report Available to Public - Tuesday, March 2, 2027 / School District Annual Meeting - Tuesday, March 9, 2027 at 6 p.m." February 2026: "PUBLIC HEARING on Proposed 2026-27 Budget - The Municipal Budget Committee will hold a hearing on the School District's proposed budget at 5:30 p.m." The library's district-practices fact 17 has the 2026 meeting. Raw: raw/money/minutes/csb-2026-10-13-draft.*, csb-2026-02-04.*, csb-2026-01-20.*
4. Chatham's annual district meetings are brief: in 2025 and 2026 every article passed as written with no floor amendments recorded, and the meetings adjourned at 6:05 p.m. and 6:12 p.m.; at a traditional meeting voters may amend the budget article, within the budget committee's 10% limit (library topics budget-traditional-district-meeting and budget-committees).
   - citation: Chatham School District Annual Meeting Minutes, March 11, 2025 and March 10, 2026
   - source: https://drive.google.com/file/d/1CKwa9FVcHraRGdsdCSJTWB6PMEITSA9f/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: 2025 text: "Article 5 was voted on and approved ... Article 6 was voted on and approved ... There was no other business ... Meeting was adjourned at 6:05 p.m." 2026: "Meeting was adjourned at 6:12 PM" (handwritten; image viewed). The minutes record no vote counts or attendance. Raw: raw/money/minutes/am-2025-03-11.*, am-2026-03-10.*
5. Chatham's Municipal Budget Committee, which reviews and recommends the school budget, lists six members plus a selectmen's representative on the town website; it recommended the 2026-27 budget 8-0-0 and the 2026 reserve and open enrollment articles 7-1-0, and a school board member serves as the board's representative to it.
   - citation: Town of Chatham, "Budget Committee" page; Chatham School District Warrant 2026; Chatham School Board Minutes, April 7, 2020
   - source: https://www.chathamnh.org/budget-commitee/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Chatham
   - note: Page text: "Budget Committee Members Chair Lisa Lewis Ellie Eastman Micha Voter Kim Callan Maria Palmisano Stephen Fink Selectmen's Rep: Bill Briggs" (the page may not show the school board member). 2020 minutes: "Beverly Aiman moved that she be the Board's representative to the Chatham Municipal Budget Committee." How budget committees work: library budget-committees. Raw: raw/money/town/chathamnh-budget-committee.html, .txt; raw/money/minutes/csb-2020-04-07.*
6. Once a year, usually in June, the Chatham board meets in the evening with MSAD 72's superintendent and Fryeburg Academy's head of school for an "End of Year Summary for Chatham Students," often in Fryeburg (June 1, 2022 and June 6, 2023 at Fryeburg Academy at 6:00 p.m.; June 17, 2025 at 6 p.m.; a joint meeting was set for June 9, 2026 at Fryeburg Academy).
   - citation: Chatham School Board Minutes, April 6, 2021, June 1, 2022, June 6, 2023 and June 17, 2025; Chatham/MSAD #72 Joint School Boards Agenda, June 9, 2026
   - source: https://drive.google.com/file/d/1PqXmT6uIO6cUHRJdaCfbDrz43QHQ9Akh/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: 2021 text: "the last meeting in June will be coordinated with MSAD 72 Superintendent and Head of School at Fryeburg Academy. This is usually an evening meeting on location in Fryeburg." 2026 agenda heading: "CHATHAM/MSAD #72 JOINT SCHOOL BOARDS Tuesday, June 9, 2026 at 6 p.m. Main Building at Fryeburg Academy". No minutes of the June 9, 2026 meeting were posted; the next minutes are for a June 30, 2026 meeting at 8:00 a.m. Raw: raw/money/minutes/csb-2021-04-06.*, csb-2022-06-01.*, csb-2023-06-07.*, csb-2025-06-17.*; raw/money/agendas/ag-2026-06-09-msad72.pdf, .txt
7. Chatham's board agendas and minutes are posted in its Drive folders, but no public comment item appears on the 2025–2026 agendas read, the "Section B - Board Governance & Operations" policy folder is empty (so no public comment policy is posted), and no recordings of Chatham board meetings were found.
   - citation: Chatham School Board agendas and minutes 2025–2026; Chatham "Policies - Chatham" Drive folder; Valley Vision site search
   - source: https://drive.google.com/drive/folders/1E95qUtB6W_Aic_iL5-PJgfTSutnXPTJN
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: The policy folder holds only Section D (DAF, DK) and Section J (JECA, JECC, JFCJ) files; Section B listed no files. Valley Vision's search for "Chatham" returned "Nothing Found for - Chatham" (Bartlett's meetings are posted there). Agenda items are "Call to Order, Approval of Minutes, Business Affairs, Any Other Business, Board Member Issues, Nonpublic Session, Adjournment". A "not found" statement about what was searched. Raw: raw/money/drive/pol-*.txt, chatham-policies-folder.txt; raw/money/sau9/valleyvision-search-chatham.*; raw/money/agendas/ag-2026-10-13.txt
8. Chatham's chair asked in 2025 that board agendas go out five days before meetings and that the tax rate impact be sent to members before the annual meeting.
   - citation: Chatham School Board Minutes, February 10, 2025 and January 7, 2025
   - source: https://drive.google.com/file/d/10AWR5T30pQ_D8_Ix2rqQDVMc4cGEtoPX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Text: "Sue Perry asked for the meeting agendas 5 days prior to meetings and to have the tax rate impact sent to board members prior to the Annual meeting." January: "Sue Perry would like to see the agendas for meetings come out earlier." Raw: raw/money/minutes/csb-2025-02-10.*, csb-2025-01-07.*
9. MSAD 72's school board, which decides the schools Chatham's K–8 students attend, meets on Wednesdays at 7:00 p.m. in the Molly Ockett School gym, sets aside the first 15 minutes of each meeting for public comment, and posts 360-degree videos of its meetings; SAU 9's superintendent used that comment period in April 2023 to raise Chatham's split-house tuition question.
   - citation: MSAD 72, "2026 - 2027 School Board Meetings"; MSAD 72 Board Minutes, April 12, 2023; MSAD 72 School Board page
   - source: https://www.msad72.org/information/school-board
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Schedule text: "All meetings start at 7:00 unless otherwise noted. Meetings held in Molly Ockett Middle School Gym. All meetings are on Wednesdays." Minutes: "The first fifteen minutes of each Board meeting is designated for public participation. During this time, members of the public may express opinions and concerns related to matters regarding education or MSAD 72 schools ... Kevin Richards, Superintendent of Schools in SAU 9, NH: Kevin came to request the Board to look at a situation where a family resides in both Chatham, NH and Stow, ME." Board page: "This is a 360° video that captures the entire school board and all audience members". The BDES committee also takes feedback through an online form (Future of BDES page). Schedule doc: https://docs.google.com/document/d/1iRAW7T0PYFhxtV0uk2LpNZ493RjKamJaoi96GxcnKZ0/edit. Raw: raw/money/maine/msad72-board-schedule-2026-27.txt, msad72-minutes-2023-04-12.*, msad72-school-board.*, msad72-future-of-bdes.*
10. MSAD 72's 2026-27 board of directors has 15 directors and 8 alternates from its seven member towns (Brownfield, Denmark, Fryeburg, Lovell, Stoneham, Stow and Sweden) and none from Chatham, and its district budget meeting (May 27, 2026) was called for the voters of those seven towns only.
   - citation: MSAD 72, "Board of Directors 2026-2027" (updated July 1, 2026); Warrant to Call MSAD No. 72 Budget Meeting (FY27)
   - source: https://drive.google.com/file/d/1n2dWPgiwyhprIZjnLFmpW_eKpS7jw9zl/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Warrant text: "Maine School Administrative District No. 72 (the 'District') composed of the Towns of Brownfield, Denmark, Fryeburg, Lovell, Stoneham, Stow, and Sweden ... notify the voters of each of the municipalities within the District ... that a District Budget Meeting will be held at The Molly Ockett School ... at 7:00 P.M. on May 27, 2026". MSAD 72's "About" page says the district "is comprised of the towns of Fryeburg, Brownfield, Denmark, Sweden, Lovell, Stoneham, and Stow in Maine and also Chatham, NH," but Chatham appears in its budget as a tuition payer, not a member (district-tuition-contracts fact 5). Board list: https://docs.google.com/spreadsheets/d/1TFEXXSPCcHgHaqtQz_37KW2lAQrKN1FE1G5hup-8XXk. Raw: raw/money/maine/msad72-fy27-warrant.*, msad72-board-directors-2026-27.csv, msad72-about.*
11. Chatham residents therefore do not vote on MSAD 72's budget or on its school construction bonds, which Maine law sends to a referendum of the district's voters (cross-state-school-tuition-rules facts 5–6); Chatham's say runs through its own board, which negotiates its tuition arrangement, and the public comment period at MSAD 72 board meetings.
   - citation: 20-A M.R.S. §§1311(2), 1351; MSAD 72 FY27 warrant; MSAD 72 Board of Directors 2026-27
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec1311.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Chatham
   - note: **Derived** from facts 9–10 and the statutes. The board's role in negotiating is shown in district-tuition-contracts fact 3. Raw: raw/money/maine/me-20A-1311.*, me-20A-1351.*

## district-student-support: Residency Checks for Chatham Students

- kind: local
- question_type: local_practice
- description: Counseling, social work and mental health support, English learner services, homeless student support, welcoming families of all backgrounds, and enrollment documents

1. The Chatham board reviews the list of Chatham students at MSAD 72 and Fryeburg Academy each year "to ensure all students are residents of Chatham," and in 2023 discussed checking addresses "to ensure that the students and families are actually living in Chatham."
   - citation: Chatham School Board Minutes, November 7, 2023 and September 12, 2023
   - source: https://drive.google.com/file/d/1X1Oamu6iJ7TcrkfZdezNy_uAXRCDkS9m/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: November text: "A list of all students attending MSAD 72 and Fryeburg Academy schools was provided to the school board. School board members will review the list to ensure all students are residents of Chatham." September text ends "...address to ensure that the students and families are actually living in Chatham." In 2019 the board asked for "a roster of students from MSAD #72 and Fryeburg" (September 3, 2019). Raw: raw/money/minutes/csb-2023-11-07.*, csb-2023-09-12.*, csb-2019-09-03.*
2. The Chatham board adopted policy JFAA, "Admission and Continued Enrollment of Resident Students," on second reading on June 17, 2025, after asking about confirming enrollment and homeschooled students; the adopted text is not in Chatham's posted policy folder.
   - citation: Chatham School Board Minutes, February 10, April 1 and June 17, 2025
   - source: https://drive.google.com/file/d/1iIVh4EDAYBrcKx2jVDhmPrmKho-3nZ1N/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: February text: "Sue Crowley asked about confirmation of student enrollment and homeschooled students living in Chatham. Pam Stimpson explained the Conway, Bartlett, Jackson Policy JFAA." June text: "Second Reading of Policy JFAA - Admission and Continued Enrollment of Resident Students - Sue Crowley made a motion to approve policy JFAA for second reading, seconded by Sue Perry 2-0-0." The Section J folder lists only JECA, JECC and JFCJ (raw/money/drive/pol-J.txt). Raw: raw/money/minutes/csb-2025-02-10.*, csb-2025-04-01.*, csb-2025-06-17.*
3. Since 2022 Chatham has disputed with the Town of Stow, Maine, which district should pay for children living in a house on Main Road whose town line runs through the middle; Chatham proposed splitting tuition 50/50, its attorney advised in 2024 that the town of residence (where parents vote and register their car) is responsible, a surveyor was sought in 2025, and in December 2025 the attorney advised that it "will not be resolved and should be monitored."
   - citation: Chatham School District Annual Meeting Minutes, March 8, 2022; Chatham School Board Minutes, November 1, 2022, June 6, 2023, April 1, 2024, April 1, 2025 and December 9, 2025
   - source: https://drive.google.com/file/d/1X7DXxpuu1v4p92UZskoEukNwRxtZLSk7/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: 2023 text: "Stowe's select board position is that the town of Chatham is responsible for paying for educating students who live in that house. Superintendent Richard stated that in NH, residency for students is where they lay their head to sleep." 2024: "The response indicated that the town of residence (where parents are registered to vote, register their car) would be responsible for education." December 2025: "Legal advice from the attorney is that this will not be resolved and should be monitored at this point." The board then cut its legal line to $2,500. Statements as recorded, not legal findings; the household is not identified here. Raw: raw/money/reports/ar-2023.* (p. 8); raw/money/minutes/csb-2022-11-01.*, csb-2023-06-07.*, csb-2024-04-02.*, csb-2025-04-01.*, csb-2025-12-09-attach.*
4. To enroll at Fryeburg Academy, a Chatham family brings a letter from the Chatham town office confirming residency (high-school-tuition-options fact 1); MSAD 72's policy JFAB charges retroactive tuition for students later found to be nonresidents and ineligible (district-tuition-contracts fact 4).
   - citation: Fryeburg Academy, "Day Students"; MSAD 72 Policy JFAB
   - source: https://www.fryeburgacademy.org/admissions/how-to-apply/day-students
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Cross-reference fact; registration steps at MSAD 72 are agent 1's area. Raw: raw/money/sau9/fa-day-students.*; raw/money/maine/msad72-policy-JFAB.txt

## cross-state-school-tuition-rules: How Maine Tuition Rates and Votes Work, and NH's Out-of-State Contract Rule

- kind: rule
- question_type: rules
- description: How Maine sets the tuition its public districts and private academies may charge, who votes on a Maine school district's budget and bonds, and New Hampshire's rule for contracting with a school in another state

1. Under Maine law, a school board decides whether its schools will accept tuition students whose parents live in another school administrative unit.
   - citation: 20-A M.R.S. §5801
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5801.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "A school board may decide whether schools in its school administrative unit shall accept tuition students whose parents reside in another school administrative unit." Raw: raw/money/maine/me-20A-5801.html, .txt
2. Under Maine law, the most a Maine public school unit may charge for an elementary tuition student is its per-student cost for the preceding year as calculated by the Maine education commissioner, though the sending unit's school board may vote to pay more.
   - citation: 20-A M.R.S. §5804(1)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5804.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The maximum tuition payments shall not exceed the receiving school administrative unit's per student cost for the preceding year as calculated by the commissioner. The school board of the sending unit may vote to pay a higher tuition rate." Maine DOE's rate files show the operating expense and attending enrollment used (district-tuition-contracts fact 6). The statute addresses Maine units; no source read says whether it binds a New Hampshire district's agreement. Raw: raw/money/maine/me-20A-5804.*
3. Maine law lets a receiving school unit add a "debt service factor" to tuition for newly incurred capital outlay and debt service, but only in an amount agreed by both the sending and receiving units with the commissioner's approval, no more than 10% of the legal tuition rate per student in any year, no longer than the repayment period, and in proportion to the project's cost and the number of tuition students.
   - citation: 20-A M.R.S. §5804(3)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5804.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "a school administrative unit may charge a debt service factor for newly incurred capital outlay and debt service ... The debt service factor must be an amount agreed upon by both the sending and receiving units, with the approval of the commissioner, and may not exceed 10% of a school's legal tuition rate per student in any one year." Raw: raw/money/maine/me-20A-5804.*
4. Under Maine law, the most a private school (such as a Maine academy) may charge a Maine school unit is the lower of its own per-student rate or the state average public secondary cost, plus an "insured value factor" (5% of the insured value of its buildings and equipment divided by its pupils, generally between 6% and 10% of tuition); it may charge up to 15% more where it has a tuition contract with a public school unit, if that unit's voters authorize paying it.
   - citation: 20-A M.R.S. §5806(2)–(3)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5806.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The maximum allowable tuition charged to a school administrative unit by a private school is the rate established under subsection 1 or the state average per public secondary student cost as adjusted, whichever is lower, plus an insured value factor ... In no case may the insured value factor be less than 6% or greater than 10% of the school's tuition rate per student, unless the legislative body ... votes"; "(3) A private school may charge tuition above the allowable maximum ... to a maximum excess charge of 15% above the otherwise allowable maximum, in those cases when the private school has a tuition contract with a public school unit". MSAD 72's FY26 budget summary listed "Fryeburg Academy Tuition $221,000 increase (5%)" and "Fryeburg Academy IVF $130,700 increase" (https://drive.google.com/file/d/1Fm24N0wzH7KPEXQvVyYAH9N-HpBPGzI9/view; raw/money/maine/msad72-fy26-budget-summary.pdf, .txt). Raw: raw/money/maine/me-20A-5806.*
5. A Maine school administrative district's bonds or notes for school construction must first be approved by a majority of the district's voters at a referendum called by its board of directors.
   - citation: 20-A M.R.S. §1311(2); §1351(1)(A)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec1311.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Bonds or notes for school construction purposes shall first be approved by a majority of voters of the district voting at an election called by the board of directors and held as provided in sections 1351 to 1354". §1351 also requires a referendum to authorize the board "to contract for the schooling of secondary pupils" and to change how costs are shared among member municipalities. Raw: raw/money/maine/me-20A-1311.*, me-20A-1351.*
6. A Maine school administrative district's board must include at least one director from each member municipality, and the district's costs are assessed on the member municipalities, whose assessors levy them on local property.
   - citation: 20-A M.R.S. §1251(1); §1310(1)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec1310.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: §1251 text: "It shall include at least one director from each municipality or subdistrict." §1310 text: "the board of directors shall issue its warrants to the assessors of each member municipality requiring them to assess upon the taxable estates within the municipality an amount which is that municipality's share of the district's costs." Raw: raw/money/maine/me-20A-1251.*, me-20A-1310.*
7. New Hampshire law lets a school district contract with an academy or high school in another state "when distance or transportation facilities make it necessary," and a contract approved by the State Board of Education makes that school a high school maintained by the district.
   - citation: RSA 194:22; library topic gov-tuition-towns fact 3
   - source: https://gc.nh.gov/rsa/html/XV/194/194-22.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Any school district may make a contract with an academy, high school or other literary institution located in this or, when distance or transportation facilities make it necessary, in another state, and raise and appropriate money to carry the contract into effect. If the contract is approved by the state board the school with which it is made shall be deemed a high school maintained by the district." Raw: raw/money/rsa/rsa-194-22.*
8. Because Maine's elementary tuition rate is based on the receiving unit's per-student cost in the preceding year, a change in a Maine district's operating costs or enrollment, such as closing or combining a school, would show up in the legal tuition rate the following year rather than immediately (**derived** from 20-A §5804(1)).
   - citation: 20-A M.R.S. §5804(1); Maine DOE FY26 Elementary Public Tuition Rates
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5804.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Our reading of how the formula works; it is not a forecast for MSAD 72 or Chatham. The FY26 rate uses 2024-25 operating expense (district-tuition-contracts fact 6). Raw: raw/money/maine/me-20A-5804.*, me-doe-fy26-elem-tuition.*

## school-residency-rules: Which NH District Is Responsible for a Student

- kind: rule
- question_type: rules
- description: Which district is legally responsible for a student under New Hampshire law: domicile, guardians, divided homes and parenting plans, moves between districts, attending a district where a student doesn't live, and who decides disputes

1. Under New Hampshire law, no one may attend school in a district where the pupil is not a legal resident without the consent of the district or school board, except as the residency law, RSA 193:3 or RSA 193:28 allow.
   - citation: RSA 193:12, I
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "no person shall attend school, or send a pupil to the school, in any district of which the pupil is not a legal resident, without the consent of the district or of the school board except as otherwise provided in this section, RSA 193:3, or RSA 193:28." Raw: raw/money/rsa/rsa-193-12.html, .txt
2. Under New Hampshire law, a minor's legal residence for school is where the parents reside, with rules for parents living apart (the parent the child lives with, or as a court order or written parental agreement says) and for a court-appointed guardian (where the guardian lives).
   - citation: RSA 193:12, II(a)
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "In the case of a minor, legal residence is where his or her parents reside, except that: (1) If the parents live apart and are not divorced, legal residence is the residence of the parent with whom the child resides ... (3) If the minor is in the custody of a legal guardian ... legal residence is where the guardian resides." Guardianship is also covered in library special-ed-who-is-parent fact 6. Raw: raw/money/rsa/rsa-193-12.*
3. New Hampshire law defines a "legal resident" of a school district as a person domiciled there who intends to keep a principal dwelling there indefinitely, shown by acts consistent with that intent; a person has only one legal residence at a time, and someone who moves to another town intending to stay there indefinitely loses residence in the old town; the law sets no minimum length of stay.
   - citation: RSA 193:12, III
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "'legal resident' of a school district means a natural person who is domiciled in the school district and who, if temporarily absent, demonstrates an intent to maintain a principal dwelling place in the school district indefinitely and to return there, coupled with an act or acts consistent with that intent ... A person may have only one legal residence at a given time." "No minimum length of stay" is our reading: no time period appears in the section. Raw: raw/money/rsa/rsa-193-12.*
4. When districts disagree about a pupil's residence, the superintendents decide jointly; if they cannot agree, the NH education commissioner decides within 30 days (14 if services would be interrupted), and the pupil stays in the school of origin meanwhile; no district may deny attendance or an existing IEP during the dispute.
   - citation: RSA 193:12, VI(a)–(b)
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "If more than one school district is involved in a residency dispute ... the respective superintendents shall jointly make such decision. In those instances when an agreement cannot be reached, the commissioner ... shall make a determination within 30 days ... No school district shall deny a pupil attendance or implementation of an existing individualized education program." The statute addresses disputes between NH districts; Chatham's dispute is with a Maine town (district-student-support fact 3). Raw: raw/money/rsa/rsa-193-12.*
5. Every New Hampshire school district must adopt a policy on admitting and attending non-resident students, and no district must provide transportation beyond its own borders under the residency law.
   - citation: RSA 193:12, VII–VIII
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "VII. Nothing in this section shall require a district to provide transportation for a student beyond the geographical limits of that district. VIII. Each school district shall adopt an admission and attendance of non-resident students policy." Raw: raw/money/rsa/rsa-193-12.*
6. The NH education commissioner may make agreements with other states on who pays educational costs, including special education, for students placed in New Hampshire by those states or placed outside New Hampshire.
   - citation: RSA 193:12, IX
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The commissioner of education may enter into agreements with other states relative to liability for educational costs, including special education costs, of students placed in New Hampshire by those states, or of students placed outside the state of New Hampshire." Raw: raw/money/rsa/rsa-193-12.*

## special-education-placements-across-states: Special Education When a NH District Educates a Student Elsewhere

- kind: rule
- question_type: rules
- description: Who is responsible for and pays for special education when a New Hampshire district educates a student in another state or a private school, including approval of out-of-state programs, rates and catastrophic aid

1. Under New Hampshire law, developing a child's individualized education program (IEP) is the responsibility of the school district where the child resides or the district that bears financial responsibility for the child's education.
   - citation: RSA 186-C:7, I
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-7.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The development of an individualized education program for each child with a disability shall be the responsibility of the school district in which the child resides or of the school district which bears financial responsibility for the child's education." IEP basics are in library special-ed-iep-basics. Raw: raw/money/rsa/rsa-186-C-mrg.html, .txt
2. A New Hampshire school district must run approved special education programs, join with other districts to provide them, or pay tuition to an approved program run by another district or a private organization.
   - citation: RSA 186-C:10
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-10.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "A school district shall establish an approved program or programs for children with disabilities, or shall enter into cooperative agreements with other districts to provide approved programs for children with disabilities, or shall pay tuition to such an approved program maintained by another school district or by a private organization." Raw: raw/money/rsa/rsa-186-C-mrg.*
3. Under New Hampshire law, the school district where a child resides pays the special education expenses for that child, except for children placed in a home for children, health care facility or state facility, whose costs follow separate rules.
   - citation: RSA 186-C:13, I
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-13.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "All expenses incurred by a school district in administering the law in relation to education for children with disabilities in need of special education and related services shall be paid by the school district where the child resides, except as follows". Raw: raw/money/rsa/rsa-186-C-mrg.*
4. Under federal special education rules, when a public agency places a child in a private school or facility, the agency must hold the IEP meeting with the school taking part, parents and an agency representative must agree to any IEP changes, and responsibility for compliance "remains with the public agency and the SEA" even if the private school carries out the IEP; the child must receive services at no cost to the parents.
   - citation: 34 CFR 300.325; 34 CFR 300.146
   - source: https://www.ecfr.gov/current/title-34/section-300.325
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: §300.325(c): "Even if a private school or facility implements a child's IEP, responsibility for compliance with this part remains with the public agency and the SEA." §300.146(a)(2): "At no cost to the parents". Raw: raw/money/rsa/cfr-300-325.html, .txt; cfr-300-146.html, .txt
5. New Hampshire's rules allow a public agency to place a child with a disability in an out-of-state school or program only if the host state approves it to provide special education (with any of the host state's limits), and an LEA may not place a student in an out-of-state program that does not meet New Hampshire's program standards in Ed 1114.07–1114.09.
   - citation: N.H. Code Admin. R. Ed 1126.06
   - source: https://gc.nh.gov/rules/state_agencies/ed1100.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Public agencies shall place children with disabilities, for the purpose of receiving special education and related services, in only those out-of-state schools, classes, or programs which are approved by the host state ... If an out-of-state program does not meet the standards of Ed 1114.07-1114.09, the LEA shall not place a student in the program." Raw: additional-data/raw/terms/rules/ed1100.txt (library copy; lines 4787–4800)
6. Under New Hampshire's rate rules, the rate paid to an out-of-state special education agency is the rate set by the rate-setting authority of the state where the agency is located; where that state has none, the NH Department of Education sets it.
   - citation: N.H. Code Admin. R. Ed 1129.09(k)
   - source: https://gc.nh.gov/rules/state_agencies/ed1100.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Rates for out-of-state agencies shall be set at the rate established by the rate-setting authority in the state where the agency is located. In states where no rate-setting authority exists, the department shall establish the rate payable to the agency through application of these rules." Whether this applies to a Maine public district's charges to Chatham was not found. Raw: additional-data/raw/terms/rules/ed1100.txt (line 6171)
7. When a New Hampshire LEA places a child with a private provider or other non-LEA program, it must send the child's IEP before enrollment, the provider may not change the IEP on its own, and the sending LEA and provider conduct a mid-year review and annual evaluation of the child's progress.
   - citation: N.H. Code Admin. R. Ed 1114.05(c), 1114.05(e) and 1114.06(g)
   - source: https://gc.nh.gov/rules/state_agencies/ed1100.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Prior to enrollment, the sending LEA shall send a copy of the child's IEP ... The private provider of special education or other non-LEA program shall not unilaterally modify a child's IEP ... A mid-year review and annual evaluation of each child's progress relative to the written IEP shall be conducted by the sending LEA and the private provider". Raw: additional-data/raw/terms/rules/ed1100.txt (lines 2153–2250)
8. The responsible district pays a high-cost special education student's costs up to 3.5 times the state average cost per pupil, plus 20% of the costs between 3.5 and 10 times, with the state paying the rest through catastrophic aid, which changes starting with fiscal year 2029 (library topic money-special-education-aid).
   - citation: RSA 186-C:18, III; library topic money-special-education-aid facts 1–3
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-18.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Pointer to the existing library rule; Chatham's receipts are in district-tax-and-state-aid fact 6. Raw: raw/money/rsa/rsa-186-C-mrg.* (lines 776–800)

## school-budget-overruns-and-reserves: When NH School Costs Exceed the Budget Mid-Year

- kind: rule
- question_type: rules
- description: What a New Hampshire school district can do when costs exceed its budget during the year: special meetings, emergency overexpenditures, retained fund balance, contingency funds and special education reserves

1. A New Hampshire school district holds a special meeting whenever the school board sees occasion for one, or when 50 voters or one-quarter of the voters (whichever is less) petition the board in writing.
   - citation: RSA 197:2
   - source: https://gc.nh.gov/rsa/html/XV/197/197-2.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "A special meeting of a school district shall be held whenever, in the opinion of the school board, there is occasion therefor, or whenever 50 or more voters, or 1/4 of the voters of the district, whichever is less, shall have made written application to the school board therefor". Raw: raw/money/rsa/rsa-197-mrg.html, .txt
2. A school district may raise or appropriate money at a special meeting only by ballot with ballots equal to at least half the voters at the last regular meeting, unless the superior court allows an emergency meeting; the court weighs how severe and urgent the need is, whether it was foreseeable, whether it could have been handled at the annual meeting, and whether other remedies exist.
   - citation: RSA 197:3, I(a)–(c); library topic budget-traditional-district-meeting fact 4
   - source: https://gc.nh.gov/rsa/html/XV/197/197-3.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "(3) Whether the claimed emergency was foreseeable or avoidable. (4) Whether the appropriation could have been made at the annual meeting. (5) Whether there are alternative remedies not requiring an appropriation." The school board must notify the DRA commissioner 10 days before petitioning the court (197:3, II). Raw: raw/money/rsa/rsa-197-mrg.*
3. When an unusual circumstance makes it necessary to spend more than was appropriated, a school board may apply to the NH education commissioner for authority to overspend, with a majority of the budget committee approving in writing beforehand (or after, for a sudden emergency); the board must name the revenue source, and the commissioner may not raise the district's tax rate to pay for it.
   - citation: RSA 32:11, I–IV
   - source: https://gc.nh.gov/rsa/html/III/32/32-11.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "No such authority shall be granted until a majority of the budget committee, if any, has approved the application in writing ... Neither commissioner shall have the authority to increase the town or district's tax rate in order to fund such an expenditure." Raw: raw/money/rsa/rsa-32-11.html, .txt
4. A New Hampshire school district may, by a separate warrant article, set up a contingency fund for unanticipated expenses, and its voters may authorize it to keep unused year-end funds up to 5% of the current year's net assessment, which the board may spend only after a public hearing with seven days' published notice.
   - citation: RSA 198:4-b, I–II
   - source: https://gc.nh.gov/rsa/html/XV/198/198-4-b.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "may establish a contingency fund to meet the cost of unanticipated expenses that may arise during the year ... retain any unused portion of the year-end unassigned general funds ... provided that the total amount of year-end unassigned general funds does not exceed, in any fiscal year, 5 percent of the current fiscal year's net assessment ... Prior to expending retained general funds, the school board shall hold a prior public hearing". Chatham's 2018 authorization is for 2.5% (district-budget-and-cost fact 18). Raw: raw/money/rsa/rsa-198-4-b.html, .txt
5. A school district may exceed its annual budget to meet special education expenses to the extent of any additional special education aid it actually receives from the state after the budget was approved.
   - citation: RSA 186-C:13, II
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-13.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "For the purposes of meeting the financial obligation for expenses incurred under this chapter, a school district may exceed its annual budget to the extent of additional special education aid which the district has actually received from the state after the annual school district budget was approved." Raw: raw/money/rsa/rsa-186-C-mrg.*
6. Local school tax rates are set once a year by the NH Department of Revenue Administration from the appropriations voted and revenue estimates (library money-local-school-tax facts 3–4), and where a school tax cap under RSA 32:5-i applies, DRA may not approve a rate above the cap unless the district shows a valid override vote (library budget-hb-1300-school-tax-cap facts 9–10).
   - citation: library topics money-local-school-tax and budget-hb-1300-school-tax-cap; RSA 32:5-i
   - source: https://gc.nh.gov/bill_status/legacy/bs2016/billText.aspx?sy=2026&id=2080&txtFormat=html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Pointer to existing library rules, placed here because they answer whether a "mid-year tax spike" can happen. Chatham's 2026 Question 2 result is district-tax-and-state-aid fact 7.

## chatham_operating_budget: Chatham School District Operating Budget (Main Warrant Article)

- unit: dollars
- period: fiscal years 2017-18 through 2026-27; year: the year the fiscal year ends
- source: Chatham School District warrants and annual meeting minutes printed in the annual reports 2017–2026, and the 2025 and 2026 annual meeting minutes — https://drive.google.com/drive/folders/1CggerU2PCy8oLHiypV1weX1GgCJMVptc
- as_of: 2026-11-13
- raw: raw/money/reports/ar-2017…ar-2026 (.pdf, .ocr.txt); raw/money/minutes/am-2025-03-11.*, am-2026-03-10.*
- note: Value is the operating budget article as approved, including grant offsets ($9,500 in 2025-26 and 2026-27). Special articles (reserve deposits, the 2019 supplemental appropriation) are excluded. Transcribed from scanned pages.

| Place | District id | Year | Value | Note |
|---|---|---|---|---|
| Chatham | 91 | 2018 | 891363 | Approved 2017; budget committee 5-0-0 |
| Chatham | 91 | 2019 | 894555 | Approved 2018 |
| Chatham | 91 | 2020 | 904603 | Approved March 12, 2019 |
| Chatham | 91 | 2021 | 951709 | Approved 2020 after a typo ($591,709) was corrected on the floor |
| Chatham | 91 | 2022 | 924255 | Approved 2021 |
| Chatham | 91 | 2023 | 925000 | Approved March 8, 2022 |
| Chatham | 91 | 2024 | 1091536 | Approved 2023 |
| Chatham | 91 | 2025 | 946000 | Approved 2024 |
| Chatham | 91 | 2026 | 968989 | Approved March 11, 2025 |
| Chatham | 91 | 2027 | 1291161 | Approved March 10, 2026 |

## chatham_budget_lines: Chatham's Main Budget Lines, Actual and Budgeted

- unit: dollars
- period: fiscal years 2022-23 through 2026-27; year: the year the fiscal year ends
- source: Chatham School District annual reports 2024 and 2026 (proposed budget pages) and the budget attached to the December 9, 2025 board minutes — https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
- as_of: 2026-11-13
- raw: raw/money/reports/ar-2024.* (pp. 4–5), ar-2026.* (pp. 5–6); raw/money/minutes/csb-2025-12-09-attach.* (pp. 3–4)
- note: Value is the general fund total, including the $20,000 capital reserve deposit where it appears, and grants in 2025-26 and 2026-27. "Actual" years are spending; "budget" years are adopted or proposed. Transportation is all of function 2720. For 2025-26 actuals by function, see district-budget-and-cost fact 4. Rotated scanned pages; transcribed from images.

| Place | District id | Year | Value | Basis | Elementary tuition | High school tuition | Special education tuition | Transportation | SAU 9 share |
|---|---|---|---|---|---|---|---|---|---|
| Chatham | 91 | 2023 | 925608 | actual | 325,470 | 199,021 | 244,172 | 79,474 | 14,048 |
| Chatham | 91 | 2024 | 844851 | actual | 320,035 | 207,661 | 175,205 | 73,444 | 14,048 |
| Chatham | 91 | 2025 | 908880 | actual | 384,193 | 246,118 | 155,649 | 77,298 | 12,813 |
| Chatham | 91 | 2026 | 968989 | adopted budget | 452,439 | 264,011 | 105,587 | 84,098 | 15,073 |
| Chatham | 91 | 2027 | 1291161 | adopted budget | 446,375 | 299,475 | 398,139 | 85,804 | 19,694 |

## chatham_students_by_level: Chatham Students by Level (Annual Report Enrollment Page)

- unit: count
- period: school years 2019-20 through 2025-26; year: the year the school year ends
- source: Chatham School District annual reports 2020–2026, enrollment page — https://drive.google.com/drive/folders/1CggerU2PCy8oLHiypV1weX1GgCJMVptc
- as_of: 2026-11-13
- raw: raw/money/reports/ar-2020…ar-2026 (.pdf, .ocr.txt)
- note: Value is K–12 total (**derived** sum). K–8 students attend MSAD 72 schools; grades 9–12 attend Fryeburg Academy. Counts are as of October 1 where the report says so. Header totals are used; where grade rows disagree, the note says so.

| Place | District id | Year | Value | K–8 | 9–12 | Note |
|---|---|---|---|---|---|---|
| Chatham | 91 | 2020 | 50 | 36 | 14 | As of October 1, 2019 |
| Chatham | 91 | 2021 | 43 | 29 | 14 | "Enrollment for 2020-2021"; from the "total enrolled" rows |
| Chatham | 91 | 2022 | 47 | 33 | 14 | As of October 1, 2021; grade 9–12 rows sum to 16 |
| Chatham | 91 | 2023 | 43 | 30 | 13 | As of October 1, 2022 |
| Chatham | 91 | 2024 | 43 | 30 | 13 | As of October 1, 2023 |
| Chatham | 91 | 2025 | 43 | 30 | 13 | Date not stated; K–8 grade rows sum to 29 |
| Chatham | 91 | 2026 | 40 | 26 | 14 | Date not stated |

## chatham_msad72_tuition_revenue: Tuition MSAD 72 Budgeted from Chatham

- unit: dollars
- period: MSAD 72 fiscal years 2021-22 through 2024-25; year: the year the fiscal year ends
- source: MSAD 72 budget documents, "Revenues" FY22–FY25 — https://www.msad72.org/information/school-board/sb-budget
- as_of: 2026-11-13
- raw: raw/money/maine/msad72-fy22-revenues.*, msad72-fy23-revenues.* (scanned; .ocr.txt), msad72-fy24-revenues.*, msad72-fy25-revenues.*
- note: Value is MSAD 72's budgeted tuition revenue from Chatham; the student count is MSAD 72's, in parentheses in its documents. Per-student amount is **derived**. These are MSAD 72's budget estimates, not Chatham's payments.

| Place | District id | Year | Value | Students | Per student (derived) | Transportation revenue from Chatham |
|---|---|---|---|---|---|---|
| Chatham | 91 | 2022 | 293164.80 | 32 | 9,161.40 | not listed |
| Chatham | 91 | 2023 | 307367.61 | 33 | 9,314.17 | 3,773 |
| Chatham | 91 | 2024 | 300732.55 | 31 | 9,701.05 | 13,142.50 |
| Chatham | 91 | 2025 | 285650.55 | 27 | 10,579.65 | 6,500 |

## chatham_sau9_share: Chatham's Share of the SAU 9 Budget

- unit: dollars
- period: 2021-22 through 2026-27; year: the year the fiscal year ends
- source: SAU 9 budget and apportionment pages in the Chatham School District annual reports 2022, 2024, 2025 and 2026 — https://drive.google.com/drive/folders/1CggerU2PCy8oLHiypV1weX1GgCJMVptc
- as_of: 2026-11-13
- raw: raw/money/reports/ar-2022.* (p. 10), ar-2024.* (p. 12), ar-2025.* (p. 12), ar-2026.* (p. 13)
- note: Value is Chatham's apportioned share. Chatham has no average daily membership in SAU 9 schools, so its percentage is half its share of SAU 9's equalized value. The 2023-24 apportionment page was not in the reports read. Chatham's budgeted line can differ slightly (e.g., $13,007 budgeted for 2024-25).

| Place | District id | Year | Value | Share of SAU budget | SAU 9 apportioned total |
|---|---|---|---|---|---|
| Chatham | 91 | 2022 | 13385 | 0.7828% | 1,709,804 |
| Chatham | 91 | 2023 | 14048 | 0.7287% | 1,927,914 |
| Chatham | 91 | 2025 | 12717 | 0.65% | 1,944,470 |
| Chatham | 91 | 2026 | 15073 | 0.65% | 2,301,622 |
| Chatham | 91 | 2027 | 19694 | 0.71% | 2,761,283 |

## For another file

- **Agent 1 (MSAD 72 schools):**
  - MSAD 72's April 1, 2025 enrollment by town and school: Chatham 12 at New Suncook (K–4), 16 at Molly Ockett (grades 2–8), 0 at Brownfield-Denmark. Source: raw/money/minutes/csb-2025-06-17.pdf, p. 5. The 2026 annual report lists "K-5 New Suncook School, Lovell" and "K-8 Molly Ockett School" as Chatham's schools.
  - The June 2025 MSAD 72 curriculum update (HMH Into Reading, i-Ready, SEPUP) and the new state pre-K mandate discussion (same minutes, pp. 1–4).
  - The FY27 cuts: "Combined K/1 at BDES; Some Multi-Age K-4 at TMOS; Reconfigured Teams 6-8" in the FY26 summary; the FY27 one-page summary. Both were downloaded, then removed as uncited; URLs are on https://www.msad72.org/information/school-board/sb-budget.
  - The BDES ad hoc committee and its feedback form.
  - MSAD 72's K–4 school placement request procedure, which uses neighborhood schools and decides requests in late August: https://docs.google.com/document/d/1VGRvYKbM1GtpoeI6FlyKm3wYDMJQIjmV3l8wqdBaahU/edit.
  - MSAD 72 residency requirements (a town residency affidavit or a letter from the town clerk): https://docs.google.com/document/d/1VPIoMdQhN_EOWtaxU-CQPYj1dMNYPxM31x4LEwLgvks/edit.
- **Agent 2 (daily):**
  - Maine's universal free meals do not cover Chatham students. MSAD 72 said Chatham students would get free breakfast and lunch, and Chatham pays Fryeburg Academy for them (minutes September 6, 2022; September 12, 2023; September 3 and November 5, 2024).
  - The Bennett Transportation contract runs to June 30, 2027.
  - April 4, 2023: SAU 9 reviewed every Chatham bus stop and pickup time ("no recommended changes").
  - June 2021: MSAD 72 took over transportation for the Maine towns, while Bennett continued for Chatham.
  - MSAD 72 budgets "Transportation Chatham" revenue.
  - The amended 2026-27 SAU 9 calendar is in raw/money/agendas/ag-2026-09-08-attach.txt (p. 6).
- **Agent 3 (Fryeburg Academy):**
  - June 17, 2025: the head of school reported 689 students, 14 from Chatham; new courses (Ceramics, AP Art, Aviation, Electricity Tech, AP Economics); paid internships for ten seniors; about 40 international students unable to get visa appointments.
  - Maine's 2025-26 maximum private-school rate for Fryeburg is $15,055.22 plus the insured value factor.
  - November 22, 2016 minutes: discussion of Fryeburg career and technical students going to Kennett (the career center).
- **Agent 5 (community):**
  - The town website (https://www.chathamnh.org/) posts town annual reports only for 2012–2015; UNH Scholars has Chatham town reports to 2020.
  - The town's school board page still says 9:00 a.m.
  - Search results mention a December 2023 selectmen's discussion of a warrant article for a fund to help Chatham children attend Fryeburg Rec. This is unverified; the minutes were not opened.
  - January 2021 board minutes: SAU 9 described a NH DOE scholarship of up to $650 for summer camps.
- **Earlier files:**
  - The brief and SAU 9's Chatham page ("9:00 a.m. at the SAU #9 Office") are out of date (district-board-and-public-input fact 2).
  - The Jackson file's school-programs-after-grade-6 1 in `Jackson/money-and-governance.md` said "Chatham's terms were not checked." Chatham's policies JECC and JECA now cover this (high-school-tuition-options facts 2–3).
  - The Jackson SAU 9 table's Chatham resident ADM of 40 matches NH DOE's FY2027 adequacy file.
  - The library's district-practices coverage table lists Chatham's "HS options" as missing; high-school-tuition-options fact 1 fills it.
  - The library has no general NH residency topic (RSA 193:12, I–III) and no topic on RSA 32:11 or RSA 198:4-b. Both are proposed above.

## Not retrieved

- **A written Chatham–MSAD 72 or Chatham–Fryeburg Academy agreement.** Not on https://www.sau9.org/tuitions, in Chatham's Drive folders (Agendum, Annual Reports, Minutes, Policies, Warrant Articles), in Chatham's 2017–2026 warrants, or in MSAD 72's posted budget pages and policies. Web searches for the agreement and for a State Board of Education approval found nothing. The 2016 rider and the 2020 "rider" mentioned in minutes are not posted.
- **The DRA 2026 tax rate for Chatham** (https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village): HTTP 403 to curl. The library's 2026-municipal-tax-rates.pdf has no town names in its text layer. The district's own February 2026 estimate is used instead.
- **Chatham policy JFAA** (adopted June 17, 2025): not in the "Section J - Students" Drive folder. The Section B folder (board operations, public comment) is empty.
- **SAU 9's "Annual Residency Verification Attestation"** (https://drive.google.com/file/d/1U9KmEYmK5BZTCqjneLjKkJscCPjtCts-/view, linked from sau9.org): Drive returned 404.
- **Minutes of the June 9, 2026 Chatham/MSAD 72 joint meeting:** not posted. The agenda is saved.
- **Chatham's sealed nonpublic minutes** (November 2025, June and September 2026): sealed; not available.
- **MSAD 72 board minutes** from April 2023 to August 2026 were downloaded and searched for "Chatham." Only the April 12, 2023 minutes mention it. No MSAD 72 vote on a Chatham agreement or rate was found.
- **Recordings of Chatham board meetings:** none found on Valley Vision (search "Chatham": nothing found). SAU 9's YouTube channel was not searched.
- **Town of Chatham annual reports for 2016–2025:** not on https://www.chathamnh.org/annual-report/ (2012–2015 only). UNH Scholars (https://scholars.unh.edu/chatham_nh_reports/) lists reports through 2020 only. The school district's own reports were used instead.
- **Which agency's staff evaluate Chatham students for special education at MSAD 72:** not stated in any Chatham document read. Agent 1 covers MSAD 72's services.
