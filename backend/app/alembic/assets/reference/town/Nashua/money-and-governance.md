# Nashua: Money, Buildings, Pay and Governance

Part of the Nashua research (town/Nashua). Gathered November 15, 2026.

## Summary

**What's covered:** 8 topics, 66 facts and 4 number tables on the Nashua School District's budget and how it is set inside the city budget, the school share of the city budget, state aid, school bonds (McCarthy Middle School), the Elm Street Middle School property, senior tax relief, teacher and paraeducator contracts, staff openings, school supply money, community use of school gyms and fields, and Board of Education public comment.
- The school appropriation FY2022–FY2027 from the city's own budget documents, what drove the FY2027 increase, the cuts made to reach it, and enrollment, special education and English learner counts since 2014-15.
- The four bonds that paid for McCarthy Middle School and the Fairgrounds and Pennichuck renovations: issue amounts, rates, what is still owed and the FY2027 payments (table).
- Resolution R-24-032 on selling the Elm Street Middle School property for housing, the 2025 finalists, and how the city used the building in FY2026.
- Nashua's elderly exemption amounts and limits (2025 on) and the tax deferral.
- The teachers' 2025–2029 and paraeducators' 2025–2028 contracts, September and November 2026 vacancy reports, and para pay against May 2025 BLS wages for the Manchester-Nashua metro area (**derived**).
- FY2025 DOE-25 general fund spending by function for Nashua, its neighbors and the state (**derived** from the site's data).
- Policy KF (community use of facilities, with the July 2025 fee schedule) and policies BEDH and BEA (public comment and meetings).
- Already in the site's data and not repeated: Nashua's tax rates and school share (property_tax), cost per pupil, average teacher salary and salary schedules, adequacy aid, special education aid and DOE-25 lines.

**Main sources:** the Nashua School District's FY2026 and FY2027 budget notebooks (presentations, enrollment, allocations), its collective bargaining agreements, Board of Education policies, committee pages and HR committee minutes; the City of Nashua's FY2027 Adopted Budget, March 2026 Official Statement, FY2025 ACFR, Resolution R-24-032, Assessing pages and tax bill guide; the BLS public data API; RSA 198:5; IRS Topic 458. Local news (Nashua Telegraph, NH Business Review) only for the 2025 Elm Street finalists and the aldermen's FY2027 vote.

**Premises checked:**
| Premise | What the sources show |
|---|---|
| "The district's FY 2026 budget is $191.2 million" (P26.1) | Correct: $191,262,559, including benefits. Without benefits it was $136,303,459 |
| "Going up 4% a year" (P26.1) | Increases were 3.0%, 3.9%, 4.9% and 5.0% for FY2023–FY2026 (about 4.2% a year), then 7.4% for FY2027 (**derived**) |
| "Enrollment isn't growing" (P26.1) | Correct: 11,488 in 2014-15 to 9,501 in 2025-26 (17.3% fewer, **derived**). Special education students and English learners both rose |
| School share of the tax bill (P26.2) | In the site's data (property_tax). In the city budget, Education is 53.64% of General Fund operating appropriations, about 57.0% with school bond payments (**derived**) |
| What happens to Elm Street (P26.3) | The city planned a sale for housing (R-24-032, 2024); two finalists presented in April 2025. No final decision was found. The city ran a warming station and rentals there in FY2026 |
| "The bond for the new McCarthy Middle School" (P27.2) | Not one bond: four bonds ($114,735,100 issued) paid for McCarthy and the Fairgrounds and Pennichuck renovations together; $109,295,000 of principal was owed on July 1, 2026 |
| Senior relief for owners "who have lived here for 30 years" (P27.1) | Years in Nashua don't count. The elderly exemption depends on age (65+), income, assets and 3 years' New Hampshire residence |
| Nashua spends less or more than Hudson, Merrimack, Hollis (P27.3) | Less: FY2025 cost per pupil $18,376 against $19,704, $23,849 and $23,370 (site data). Hollis runs only grades K–6 |
| Is the district "looking at raising" para pay (P32.1) | The 2025–2028 para contract already adds $1.00 an hour to every step in 2026-27 and 2027-28 |

**Main gaps:**
- No teacher turnover rate by school was found, so P31.1's "higher in some buildings" can't be checked. Only vacancy counts (September and November 2026) were found.
- Nothing after April 2025 on the Elm Street sale (developer chosen, agreement, vote) was found. The web search budget ran out, and the city's search and agenda portals need JavaScript.
- No local programs donating classroom supplies to Nashua teachers were found (not searched once the search budget ran out).
- The 2019 aldermen's bond resolution for the middle school project wasn't retrieved. The ACFR's authorized-debt figures are used instead.

**Proposed shared topics:**
- `district-facility-use` (local, local_practice): "Community use of school buildings and fields: who may use gyms, auditoriums and fields, fees and exempt groups, insurance and how to apply." It holds 7 facts here. No current topic covers rentals (`district-volunteers-and-partners` is about volunteering and donating; `town-recreation-and-summer` is town programs).
- `educator-expense-deduction` (rule, help, no place): "Teachers' unreimbursed classroom expenses: the federal educator expense deduction." It holds 1 fact.
- One fact is added to the library's existing `money-local-school-tax` topic (how_it_works, governance_money, its own description).

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P19.3 Why pay full property taxes for public schools if our kids go to private school? | money-local-school-tax fact 1; district-tax-and-state-aid facts 4, 9, 10; library: money-statewide-education-property-tax facts 1–3, money-local-school-tax, money-efa-funding-link | full | The school taxes are assessed on taxable property, not on who uses the schools. None of Nashua's exemptions is tied to where children go to school |
| P26.1 Why does the $191.2M budget keep rising 4% a year if enrollment isn't growing? | district-budget-and-cost facts 1–10, 21; district-facilities-and-capital facts 11–12; table nashua_education_appropriation | full | Premises checked above. Drivers in the district's own words: benefits, transportation, special education contracts and tuition, English learners. Says what it rose by, not whether it should have |
| P26.2 How much of my tax bill goes to schools versus the city? | site data: property_tax (Nashua: local and state education rates, school share); district-tax-and-state-aid facts 1–5 | full | Rates aren't restated. Local facts: the city budget split, school revenue, the two-year revaluation cycle |
| P26.3 What will happen to the old Elm Street building? | district-facilities-and-capital facts 6–10 | partial | The plan (R-24-032), the 2025 finalists and FY2026 use are covered. No decision after April 2025 was found |
| P27.1 Senior tax relief after 30 years in Nashua | district-tax-and-state-aid facts 6–9; Hart's Location file, property-tax-relief facts 1–3 (state elderly exemption rules and low and moderate income relief) | full | Premise: years in Nashua don't count |
| P27.2 How much is the city still paying on McCarthy's bond? | district-facilities-and-capital facts 1–5; table nashua_middle_school_bonds | full | The bonds are shared with two renovations, and the budget doesn't split them. The 2023 new-school bond is given on its own |
| P27.3 Why does Nashua spend less or more per student than Hudson, Merrimack, Hollis? | site data: cost per pupil, average teacher salary, class size; district-budget-and-cost facts 12, 14; table nashua_doe25_spending_shares; library: measure-cost-per-pupil, research-school-spending | partial | Figures side by side. No source explains the gap, and the data can't say why. Hollis is K–6 only |
| P31.1 Why is teacher turnover higher in some buildings, and how does pay compare? | site data: salary schedules and average salary (Nashua and neighbors); district-budget-and-cost facts 15–16; district-classrooms-and-staff facts 1–4 | partial | Pay comparisons come from the site's data. No turnover by building was found |
| P31.2 Where do new teachers get classroom supplies? | district-budget-and-cost facts 22–24; educator-expense-deduction fact 1 | partial | School allocations and the supply budget are covered. No donation programs were found |
| P32.1 Why is it hard to keep special education paras? Is pay rising? | district-budget-and-cost facts 17–21; district-classrooms-and-staff facts 1–4; table nashua_para_and_metro_wages | full | Wage comparisons are **derived** and hourly only |
| P32.3 Are school gyms open to youth leagues without big fees? | district-facility-use facts 1–7 | full | Listed public youth leagues pay no rental fee |
| P36.1 Why is school funding tied to local property taxes? | library: money-school-revenue-by-source-trend, money-local-school-tax, money-statewide-education-property-tax, money-adequacy-grant-calculation, money-conval-case, money-rand-case; district-tax-and-state-aid facts 2–4 | full | The library holds the statewide answer. This file adds Nashua's own mix (state revenue covers 32.9% of the school appropriation, **derived**) |
| P40.2 How much goes to classrooms versus administration and debt? | district-budget-and-cost facts 11–14; district-facilities-and-capital fact 4; table nashua_doe25_spending_shares | full | DOE-25 shares are **derived**. School bond payments sit in the city's Debt Service department, outside the school budget |
| P40.3 How does public comment work at the Board of Education? | district-board-and-public-input facts 1–6 | full | Policy BEDH |

None of the 14 questions was answered wholly by earlier files. P26.2 and P36.1 rest mostly on the site's data and the library, with Nashua facts added.

## district-budget-and-cost: Nashua's School Budget, What Drives It, Pay and Supplies

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. The Nashua School District's budget for fiscal year 2026 (July 2025 to June 2026) is $191,262,559 including employee benefits ($136,303,459 without them); the district's own summary rounds it to "$191.2M for the Fiscal Year 2026 Budget," alongside 9,501 students, 2,055 staff members and an average class size of 19.4.
   - citation: Nashua School District, Fiscal Year 2027 Budget Presentation to the Board of Aldermen, May 5, 2026, slides 4 and 17
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Slide 4 transcribed from image (raw/money/images/boa-p4.png): "$191.2M for the Fiscal Year 2026 Budget"; "9,501 Students"; "2,055 Staff Members"; "19.4 Average Class Size". Slide 17: "Total $191,262,559 ... Total Without Benefits $136,303,459". The city's FY2027 budget shows the same FY2026 figure under Education. Premise P26.1 ("$191.2 million") is correct. Linked from the FY27 Budget Notebook (https://www.nashua.edu/our-district/board-of-education/nsd-operating-budget/fy27-budget-notebook). Raw: raw/money/district/fy27-boa-presentation-5-5-26.pdf, .txt
2. Nashua's school appropriation grew from $162,316,834 in FY2022 to $191,262,559 in FY2026, rising 3.0%, 3.9%, 4.9% and 5.0% a year (about 4.2% a year on average), and the Board of Aldermen adopted $205,367,867 for FY2027, 7.4% more than FY2026 (all percentages derived).
   - citation: City of Nashua, Official Statement, March 19, 2026, "Budget Summary," p. 38; City of Nashua FY 2027 Adopted Budget, p. 23
   - source: https://www.nashuanh.gov/DocumentCenter/View/35914/2026-Nashua-NH-Official-Statement--March-2026-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: See table nashua_education_appropriation. Official Statement text: "Education 162,316,834 167,231,489 173,793,393 182,240,036 191,262,559" (FY2022–FY2026). FY2027 from the adopted budget (https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF): "School $191,262,559 $206,035,867 $205,367,867 $205,367,867". Growth is year over year; the FY2022–FY2026 average is compound (**derived**). The Education line includes benefits but not school bond payments, which the city carries in its Debt Service department (district-facilities-and-capital fact 4). The district's FY2027 slides label FY2026 "FY 26 FINAL BUDGET 4.0%"; the city's figures give 4.95% including benefits (**derived**). Premise "going up 4% a year": close for FY2023–FY2026; FY2027 was 7.4%. Raw: raw/money/city/os-2026-03.pdf, .txt (PDF page 38); raw/money/city/fy27-adopted-budget-excerpt.pdf, .txt
3. For FY2027 the Nashua Board of Education asked for $206,035,867 and the Board of Aldermen adopted the mayor's figure of $205,367,867, which is $668,000 less (derived), all of it in the "Salary Adjustments" line, cut from a requested $1,000,000 to $332,000.
   - citation: City of Nashua FY 2027 Adopted Budget, pp. 23 and 231–232 (Education appropriations)
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Columns are FY2026 adopted, FY2027 department proposed, mayor proposed and adopted: "51900 - Salary Adjustments $2,939,979 $1,000,000 $332,000 $332,000"; "Total Expenditures $191,262,559 $206,035,867 $205,367,867 $205,367,867". The Nashua Telegraph reported that the aldermen voted 9-4 on June 23, 2026 to pass the city's $502.3 million FY2027 budget (news is the only source found for the vote; raw/money/news/tel-2026-06-25-fy27.txt). The adopted budget's "Total FY27 Proposed Appropriations $ 502,310,192" matches. Raw: raw/money/city/fy27-adopted-budget-excerpt.pdf, .txt (PDF pages 24, 233–235)
4. Nashua's school budget totals include employee benefits estimated by the city: the adopted FY2027 school budget has $105,338,273 for salaries and wages and $61,869,192 for fringe benefits ($20,755,728 for pensions, $31,886,400 for health and other benefits and $8,912,064 for Social Security and Medicare), so the $144.4 million reported as the Board of Education's FY2027 request is the budget without benefits.
   - citation: City of Nashua FY 2027 Adopted Budget, p. 232; Nashua School District FY2027 Budget Presentation, May 5, 2026, slide 35
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Budget text: "52150 - Pension Expense ... $20,755,728"; "52300 - Benefits ... $31,886,400"; "52100 - Fica/Medicare ... $8,912,064". District slide 35: "Total Without Benefits $ 136,303,459 $ 144,481,666 $ 8,178,207 6.0%" and "*Benefits are an estimate - will be calculated by City of Nashua". The Telegraph (March 26, 2026) reported "$144.4 million ... does not yet include the cost of benefits" (raw/money/news/tel-2026-03-26-school.txt). Raw: raw/money/city/fy27-adopted-budget-excerpt.txt; raw/money/district/fy27-boa-presentation-5-5-26.txt
5. In December 2025 Nashua's mayor asked every city department, including the school district, to hold its FY2027 budget increase to 3% or less excluding fringe benefits, citing an expected 12% rise in medical benefit costs and a goal of a tax rate increase under 6%.
   - citation: Mayor Jim Donchess, memorandum "FY2027 Budget Guidelines," December 22, 2025
   - source: https://www.nashua.edu/fs/resource-manager/view/970f9619-3057-4436-a256-d4f43ea62c20
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "we are anticipating a 12% increase in medical benefits. With fringe benefits accounting for approximately 25% of our operating budget"; "The goal is to propose a budget that would deliver a tax rate increase of less than 6%. To achieve this, I am requesting that each department submit its proposed budget with an increase of no more than 3%, excluding fringe benefits." The school budget's increase without benefits was 6.0% (fact 4). Raw: raw/money/district/fy27-mayor-memo.pdf, .txt
6. The Nashua School District's FY2027 draft named its largest increases as benefits (up 12.0%), transportation (to $12,457,228, up 15.8%, in the second year of a five-year bus contract, with the daily cost per bus rising from $482.75 to $550.34 for 95 buses), special education contracted services (to $3.5 million in the operating budget, from $1.7 million), out-of-district special education tuition (to $7.2 million, from $6.2 million) and four new English learner teachers.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slides 15 and 17
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Slide 15: "Budget $12,457,228 - Increase of $1.7M – 15.8%"; "Second year of 5-year contract"; "Daily bus cost $550.34 - from $482.75"; "Total buses 95 - 52 Regular Education and 43 Special Education Buses"; "4 New ELL Teachers"; "$3.5 Million ($1.7M FY 2026) within Operating Budget"; "$7.2 Million ($6.2M FY 2026) within Operating Budget". The adopted budget carries $12,007,228 for transportation (regular $5,961,494 plus special education $6,045,734, **derived** sum) and $7,200,000 for out-of-district tuition (city budget p. 233). Raw: raw/money/district/fy27-boa-presentation-5-5-26.txt
7. Nashua's spending on contracted special education services rose from $33,305 in FY2022 to $3,568,650 in FY2025, with $7,939,411 estimated for FY2026; the district says federal pandemic relief (ESSER) money had paid for some of these contracts and has run out, and that hiring for these positions has been harder since COVID.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slides 18 and 21
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Slide 18: "Contract service expenses have dramatically increased in the past four years • FY 2022: $33,000 • FY 2026: $4,000,000"; "Prior to COVID there was less difficulty hiring the positions needed to service these students, those students then need to havetheir services met with contractors"; "ESSER funds are gone now which has masked this issue ... ESSER I (Sept 2022): ~$500k • ESSER II (Sept 2023): ~$2.3M • ESSER III (Sept 2024): ~$2M". Slide 21 table: FY2022 grand total actual $33,305; FY2025 $3,568,650; FY2026 "$ 7,939,411 EOY Est." Raw: raw/money/district/fy27-boa-presentation-5-5-26.txt
8. The Nashua School District's enrollment fell from 11,488 in 2014-15 to 9,501 in 2025-26 (17.3% fewer, derived) while its teacher FTEs went from 991 to 958; over the same years its special education students rose from 1,856 to 2,235 and its English learners from 1,118 to 2,054, and students in neither group fell from 8,514 to 5,212.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slides 5–6 ("Student Enrollment and Total FTEs," "Total Student Enrollment")
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Transcribed from images (raw/money/images/boa-p5.png, boa-p6.png). Premise P26.1 ("enrollment isn't growing") is correct. The district's official October 2025 count was 9,501, down 200 from 9,701 in 2024-25 (raw/money/district/fy27-enrollment-stats.txt). NH DOE's counts in the site's data differ slightly (9,699 for 2024-25). Raw: raw/money/district/fy27-boa-presentation-5-5-26.pdf
9. To keep the FY2027 increase at 6.0% without benefits, the Nashua superintendent's recommendation cut $3,878,048: $2,428,048 for 56 positions (21 teachers, 18 paraeducators or behavior specialists, 6 clerical, 2 TIAs, 5 instructional coaches and 4 administrators), $450,000 in transportation and $1,000,000 in contract services.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slide 36
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "$3,878,048.00 Total Cuts • Wages • $2,428,048.00 – 56 positions • Teachers - 21 • Paraeducators/Behavior Specialist - 18 • Clerical - 6 • TIA's - 2 • Instructional Coaches - 5 • Administrators - 4 • Transportation • $450,000.00 • Contract Services • $1,000,000.00". The source doesn't spell out "TIA". The aldermen then took a further $668,000 out (fact 3). Raw: raw/money/district/fy27-boa-presentation-5-5-26.txt
10. For FY2026 the Nashua superintendent recommended a 3.5% increase without benefits (5.32% with benefits, from $182,361,021 to $192,060,171), with cuts of 20 elementary, 5.5 middle school and 20.25 high school and career and technical education positions; the city adopted $191,262,559.
   - citation: Nashua School District, FY 2026 Budget Presentation, March 31, 2025, slides 7 and 12
   - source: https://www.nashua.edu/fs/resource-manager/view/5ddb4227-7f71-4d19-ba6e-4ac8b3e7db49
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Total $182,361,020.57 $192,060,171.25 $9,699,150.68 5.32%"; "Total Without Benefits ... 3.49%"; "Superintendent's Budget Recommendation 3.5% for FY 2026"; "Budget Cuts – Positions • Elementary Schools • 20 positions • Middle Schools • 5.5 positions • High School & CTE • 20.25 positions". Linked from the FY26 Budget Notebook. Adopted figure: Official Statement p. 38. Raw: raw/money/district/fy26-presentation-3-31-25.pdf, .txt
11. In Nashua's FY2026 school budget, teachers accounted for 68.6% of salary costs, paraprofessionals 8.4%, custodial and trade staff 6.0%, principals and assistant principals 4.4%, non-union staff 4.2%, other administrators and supervisors 3.6%, secretaries 2.8% and food service workers 2.1%.
   - citation: Nashua School District, FY 2026 Budget Presentation, March 31, 2025, slide 8 ("Salary Overview %")
   - source: https://www.nashua.edu/fs/resource-manager/view/5ddb4227-7f71-4d19-ba6e-4ac8b3e7db49
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Teachers, 68.6% Paraprofessionals, 8.4% Non-Affiliated, 4.2% Custodial and Trade, 6.0% Food Service, 2.1% Secretary, 2.8% NASAS, 3.6% NASP, 4.4%". NASP is the Nashua Association of School Principals and NASAS the Nashua Association of School Administrators and Supervisors (the district's bargaining agreements page, raw/money/district/cba.txt). Raw: raw/money/district/fy26-presentation-3-31-25.txt
12. A Nashua School District comparison of FY2026 salaries put its superintendent at $183,005 (against $164,000 in Derry Cooperative, $166,383 in Bedford, $172,692 in Salem, $184,393 in Merrimack, $185,400 in Exeter, $192,520 in Manchester and $197,000 in Hollis-Brookline), its assistant superintendent at $128,339, the lowest of the eight districts listed, and its business administrator (chief operating officer) at $125,000, second lowest after Salem's $112,100.
   - citation: Nashua School District, FY 2026 Budget Presentation, March 31, 2025, slide 9
   - source: https://www.nashua.edu/fs/resource-manager/view/5ddb4227-7f71-4d19-ba6e-4ac8b3e7db49
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Nashua SAU Office Senior Education Official 183,005.00"; "Nashua SAU Office Assistant Senior Education Official 128,339.00"; "Nashua SAU Office Business Administrator 125,000.00"; "Salem SAU Office Business Administrator 112,100.00". The comparison is the district's own; titles as printed. Raw: raw/money/district/fy26-presentation-3-31-25.txt
13. By type of cost, Nashua's adopted FY2027 school budget is 51.3% salaries and wages, 30.1% fringe benefits, 9.7% other services (mostly bus contracts and out-of-district tuition), 3.6% professional and technical services, 2.4% property services and utilities, 1.6% supplies and materials, 1.2% equipment and 0.3% capital lease payments (shares derived).
   - citation: City of Nashua FY 2027 Adopted Budget, pp. 231–234 (Education, Appropriations Summary)
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Adopted amounts: salaries $105,338,273; benefits $61,869,192; other services $19,933,783 (including regular transportation $5,961,494, special education transportation $6,045,734 and out-of-district tuition $7,200,000); professional and technical $7,352,466; property services $4,906,030; supplies $3,378,483; equipment $2,388,409; capital lease $618,731; offsets of $220,000 and $197,500; total $205,367,867. Shares are each amount divided by the total (**derived**). For spending by function (instruction, administration, debt) see table nashua_doe25_spending_shares. Raw: raw/money/city/fy27-adopted-budget-excerpt.pdf, .txt (PDF pages 232–235)
14. The City of Nashua's own measure of school cost per pupil for FY2025 is $19,937.03: a general fund operating budget of $177,930,800 plus $10,673,504 of debt service, divided by 9,460 students; the same city table counts 890 teaching staff, a pupil/teacher ratio of 10.6.
   - citation: City of Nashua, Annual Comprehensive Financial Report, FY2025, "School Department Operating Statistics – Last Ten Fiscal Years," p. 166
   - source: https://www.nashuanh.gov/DocumentCenter/View/36501/FY2025-ACFRPDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "2025 177,930,800 10,673,504 188,604,304$ 9,460 19,937.03$ 5.2 % 890 10.6"; "(1) Budget is for the General Fund only and excludes special revenue funds and grants." The table uses 9,460 students for both 2024 and 2025. NH DOE's FY2025 cost per pupil for Nashua in the site's data ($18,376) is figured differently (library: measure-cost-per-pupil), so the two shouldn't be compared directly. Raw: raw/money/city/acfr-fy2025.pdf, .txt (PDF page 172)
15. The Nashua teachers' contract (September 1, 2025 to August 31, 2029) raises starting pay with a bachelor's degree from $49,000 (2025-26 and 2026-27) to $50,000 in 2027-28 and $51,000 in 2028-29, raises the top of the bachelor's scale from $83,731 to $92,834 and of the master's scale from $90,360 to $100,184, and shortens the schedule from 24 steps (0–23) to 21 (0–20).
   - citation: Agreement between the Nashua Board of Education and the Nashua Teachers' Union, Local 1044, September 1, 2025 through August 31, 2029, Appendices A-1 to A-4
   - source: https://www.nashua.edu/fs/resource-manager/view/5aa4af56-8404-41ce-a84d-14426c374420
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: A-1 (2025-26): "0 $ 49,000 $ 51,000 $ 53,000 $ 55,000 $ 57,000" ... "23 $ 83,731 $ 86,951 $ 90,360 $ 93,771 $ 96,991". A-4 (2028-29): "0 $ 51,000 ..." ... "20 $ 92,834 $ 96,404 $ 100,184 $ 103,965 $ 107,536". All eligible teachers move up one step each September 1 (Article 4:1). The site's salary schedule data already has the current schedule and neighbors' schedules for comparison; 2027-28 and 2028-29 are new here. Listed on the district's Collective Bargaining Agreements page. Raw: raw/money/district/teacher-2025-2029.pdf, .txt
16. Beginning in 2025-26, Nashua may credit a newly hired teacher with one year on the salary schedule for every two years of career experience in an allied field, and it gives newly hired school nurses full credit for prior registered nursing experience.
   - citation: Nashua teachers' agreement 2025–2029, Article 4:2
   - source: https://www.nashua.edu/fs/resource-manager/view/5aa4af56-8404-41ce-a84d-14426c374420
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Teachers being credited with allied field experience shall receive one credited year of experience on the salary schedule for every two years of career experience in an allied field"; "the District will grant incoming school nurses full credit for all years of satisfactorily demonstrated prior registered nursing experience". Raw: raw/money/district/teacher-2025-2029.txt
17. Nashua's paraeducators (Unit B of the Nashua Teachers' Union) are paid by the hour under a contract running July 1, 2025 to June 30, 2028: instructional paraeducators earn $18.01 to $25.26 an hour in 2025-26, $19.01 to $26.26 in 2026-27 and $20.01 to $27.26 in 2027-28; technical and districtwide special education (intensive needs) paraeducators earn a little more (districtwide $18.94 to $26.27 in 2025-26); and every step rises $1.00 an hour each year (derived).
   - citation: Agreement between the Nashua Board of Education and the Nashua Teachers' Union (Paraeducators), 2025–2028, Appendices A and B
   - source: https://www.nashua.edu/fs/resource-manager/view/3284d3f8-5857-4aa4-8e9c-36e4e2f116f0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Appendix B: "FY25-26 ... Instructional INT 18.01 ... 25.26"; "Districtwide DWS 18.94 ... 26.27"; "FY26-27 ... Instructional INT 19.01 ... 26.26"; "FY27-28 ... Instructional INT 20.01 ... 27.26". 13 steps by credited years (step 13 is 26+ years). Districtwide covers preschool, alternative room and behavior paraeducators (Appendix A). The contract was signed July 11, 2025. Premise P32.1: pay increases for 2026-27 and 2027-28 are already set. See table nashua_para_and_metro_wages. Raw: raw/money/district/para-2025-2028.pdf, .txt
18. Nashua paraeducators who work 30 or more hours a week get health insurance (the Board pays 80% of the single-person premium for any plan offered), single dental coverage at no cost and a $10,000 life insurance policy, while those under 30 hours may buy in at the group rate; paraeducators get overtime after 35 hours a week, and their work year is 180 student days plus the day before school starts and Presidents' Day.
   - citation: Nashua paraeducators' agreement 2025–2028, Articles 4:5, 5:3–5:5 and 7:5
   - source: https://www.nashua.edu/fs/resource-manager/view/3284d3f8-5857-4aa4-8e9c-36e4e2f116f0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "The Board shall contribute 80% of the premium for the single person plan for all insurance plans offered"; "single person dental coverage for the employees who work a regular schedule of 30 or more hours per week"; "policy of $10,000"; "Any paraeducator who is required to work in excess of thirty -five (35) hours per week shall be compensated at one and one-half times"; "The workyear shall consist of 180 pupil days, the day prior to the first pupil day, and effective July 1, 2023, Presidents' Day as a Professional Development day." Raw: raw/money/district/para-2025-2028.txt
19. Nashua's paraeducator contract sets aside $8,000 a year to reimburse tuition for job-related college courses, including courses leading to paraeducator certification, for paraeducators who work 30 or more hours a week.
   - citation: Nashua paraeducators' agreement 2025–2028, Article 4:6
   - source: https://www.nashua.edu/fs/resource-manager/view/3284d3f8-5857-4aa4-8e9c-36e4e2f116f0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "The District agrees to provide the sum of $8,000 for the purpose of reimbursement of tuition costs for employees with a regular work schedule of 30 or more hours per week ... courses completed with a grade of 'C' or better for courses leading to a Degree, or leading to paraeducator certification". Prior written approval is required. Raw: raw/money/district/para-2025-2028.txt
20. In May 2025 the median hourly wage in the Manchester-Nashua metro area was $16.99 for retail salespersons, $15.24 for cashiers, $17.33 for stockers and order fillers and $17.47 for food preparation workers, so a first-step Nashua instructional paraeducator's $19.01 an hour in 2026-27 is $1.54 to $3.77 an hour above those medians (derived); the federal estimate does not publish an hourly wage for the area's teaching assistants, whose annual median was $37,220.
   - citation: U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics, May 2025, Manchester-Nashua, NH metropolitan area (area 31700), via the BLS public data API
   - source: https://api.bls.gov/publicAPI/v1/timeseries/data/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Series OEUM0031700000000 + occupation + data type: 412031 (retail salespersons) 08 = "16.99"; 412011 (cashiers) 08 = "15.24"; 537065 (stockers) 08 = "17.33"; 352021 (food preparation workers) 08 = "17.47"; 259045 (teaching assistants, except postsecondary) 08 = "-", 13 = "37220". Year 2025, period A01. Comparisons are hourly only (**derived**); no annual para pay is computed, because the contract doesn't fix daily hours. See table nashua_para_and_metro_wages. The BLS web page for the area returned HTTP 403. The Manchester research pulled the same series (town/Manchester/raw/money/bls-oews-*.json). Raw: raw/money/state/bls-oews-msa31700-may2025.json, bls-oews-msa31700-request.json
21. Nashua's adopted FY2027 school budget has $1,225,000 for staffing services (staff hired through contractors), up from $950,000 budgeted for FY2026, after $1,256,511 was spent in FY2025.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slide 15; City of Nashua FY 2027 Adopted Budget, p. 232
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Slide: "Staffing Services $ 275,000 • $1,225,000 Increase by $275,000 ($950,000 FY 2026 Budget , $1,256,511 in FY 2025 - Actual) within Operating Budget". City budget: "53452 - Staffing Services $950,000 $1,225,000 $1,225,000 $1,225,000". Raw: raw/money/district/fy27-boa-presentation-5-5-26.txt; raw/money/city/fy27-adopted-budget-excerpt.txt
22. Each Nashua school gets a yearly budget allocation figured mostly per student: for FY2026, $92.97 per elementary student plus $6,361 per school, $150.98 per middle school student plus $5,040 per school, and $112.52 per high school student, rates unchanged since FY2024, plus supplemental amounts; Birch Hill Elementary's total was $34,444 for 332 students, and all schools together received $1,385,671.
   - citation: Nashua School District, Fiscal Year 2026 School Budget Allocations (FY26 Budget Notebook, "School-by-school Budget Allocations")
   - source: https://www.nashua.edu/fs/resource-manager/view/ca5d6840-d8fc-4db3-94a6-695788e8b3ac
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Page viewed (raw/money/images/alloc-p1.png): "Birch Hill 332 $30,866 $6,361 $24,693 $31,054 $3,390 $34,444"; "FY '26 Cost/Pupil $92.97" (elementary, "Increase --> 0.00%"; FY '23 $90.26); middle "$150.98"; high school "FY '26 Base Cost/Pupil+Art $112.52"; "TOTAL 9,664 ... $1,385,671". The sheet doesn't say what the allocations must be spent on. No FY2027 sheet was posted in the FY27 notebook. Raw: raw/money/district/fy26-school-allocations.pdf, .txt
23. Nashua's adopted FY2027 school budget has $1,263,362 for educational supplies (down from $1,373,636 in FY2026), $102,210 for books and $551,111 for subscriptions.
   - citation: City of Nashua FY 2027 Adopted Budget, pp. 233–234 (Education, 61 – Supplies & Materials)
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "61135 - Educational Supplies $1,373,636 $1,263,362 $1,263,362 $1,263,362"; "61875 - Books $32,685 $102,210"; "61830 - Subscriptions $289,040 $551,111". Raw: raw/money/city/fy27-adopted-budget-excerpt.txt
24. Nashua's teachers' contract sets a $10,000 supplementary budget each school year "to provide for needs not previously anticipated and to allow teachers to capitalize on new and innovative materials," and a joint Educational Council of three board and three teacher members may recommend how it is spent.
   - citation: Nashua teachers' agreement 2025–2029, Article X (Educational Council/Supplemental Budget)
   - source: https://www.nashua.edu/fs/resource-manager/view/5aa4af56-8404-41ce-a84d-14426c374420
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "A supplementary budget of $10,000 in each school year shall be established to provide for needs not previously anticipated and to allow teachers to capitalize on new and innovative materials which become available during the course of the school year. The Council may make recommendations to the BOARD concerning the disbursement of said funds." The Council meets at least four times a year. Raw: raw/money/district/teacher-2025-2029.txt

## district-tax-and-state-aid: Nashua's City Budget, School Revenue, Tax Bill and Senior Relief

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. In Nashua's FY2027 city budget, Education ($205,367,867) is 53.64% of General Fund operating appropriations, ahead of Police (11.32%), Fire (9.31%) and Debt Service (6.00%); adding the $12,761,411 of school bond payments carried under Debt Service brings the schools' share to about 57.0% (derived).
   - citation: City of Nashua FY 2027 Adopted Budget, pp. 21–23 (General Fund – Operating, Appropriations by Division) and p. 237 (Debt Service)
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "Education $205,367,867 53.64% Police $43,347,777 11.32% Fire $35,629,994 9.31% Debt Service $22,984,943 6.00%"; operating "Total Expenditures ... $382,870,847". 57.0% = ($205,367,867 + $12,761,411) / $382,870,847 (**derived**). This is the city budget, not the tax bill: the rate split (local and state education against municipal and county) is in the site's data (property_tax). Raw: raw/money/city/fy27-adopted-budget-excerpt.pdf, .txt (PDF pages 22–24, 238)
2. Nashua's FY2027 city budget counts $67,607,277 of revenue for the schools, mostly state adequacy aid ($65,567,936), plus $1,000,000 of special education (catastrophic) aid, $500,000 from Medicaid, $252,000 of vocational aid, $126,341 of school building aid, $50,000 of Education Freedom Account aid and $111,000 in fees; that covers about 32.9% of the school appropriation, and the other $137,760,590 (derived) comes from the city's other revenue and property taxes.
   - citation: City of Nashua FY 2027 Adopted Budget, p. 231 (Nashua School District, Revenue)
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "State Adequacy Aid $64,654,778 $65,567,936 ..."; "Total Intergovernmental Revenue $66,553,119 $67,496,277"; "Total Charges For Services $111,000"; "Total School $66,664,119 $67,607,277". 32.9% = $67,607,277 / $205,367,867 (**derived**); the budget doesn't say which city revenue pays the rest. How adequacy aid is figured is in the site's data and the library (money-adequacy-grant-calculation). Federal grants (about $9.57 million for FY2027) are in separate special revenue funds and aren't counted here. Raw: raw/money/city/fy27-adopted-budget-excerpt.txt (PDF page 232)
3. State adequacy aid made up 90.8% of the Nashua School District's state and other government revenue in FY2022 ($40.3 million of $44.4 million) and 96.6% in FY2026 ($67,017,028 of $69,408,931 actual), the district reports.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slides 18 and 26
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Slide 18: "FY 2022: $44.4M Total Intergovernmental Revenue, $40.3M from Adequacy Aid (90.8% of Total Intergovernmental Revenue)". Slide 26 (FY 2026 Actuals column): "STATE ADEQUACY AID ... $ 67,017,028"; "TOTAL ... $ 69,408,931"; "STATE ADEQUACY AID % ... 96.6%". The site's adequacy aid data has the state's own figures. Raw: raw/money/district/fy27-boa-presentation-5-5-26.txt
4. The City of Nashua's guide to the tax bill says the property tax it raises funds the city's schools, police and fire protection, roads and other services, part of Hillsborough County's costs and the state education tax; the tax levy is the city and school budgets minus revenue from other sources; and the tax depends only on the value of the property owned, not on the owner's income or spending.
   - citation: City of Nashua, "Guide to Understanding Your Tax Bill" (linked from the Tax Rate History page as "Explanation of Your Tax Bill")
   - source: https://www.nashuanh.gov/DocumentCenter/View/2153
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "The money Nashua raises in property taxes funds the City's schools, pays for police and fire protection, maintains roads, and supports many other municipal services ... It also pays for a portion of the costs necessary to support Hillsborough County services, as well as the state education tax"; "These revenues are subtracted from the original budget and the remainder becomes the tax levy"; "The property tax differs from an income tax and a sales tax because it does not depend on how much money you earn or on how much you spend. It is based totally on how much the property you own is worth." The guide is undated. Raw: raw/money/city/taxbill-explained.pdf, .txt
5. Nashua revalues property every two years, according to the city's tax bill guide; the city's tax rate history marks 2018, 2022 and 2024 as update years, gives a 2025 total rate of $16.83 per $1,000 of assessed value, and had no 2026 rate posted as of November 15, 2026.
   - citation: City of Nashua, Tax Rate History; "Guide to Understanding Your Tax Bill"
   - source: https://www.nashuanh.gov/1708/Tax-Rate-History
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Guide: "This is done every two years and sometimes results in shifts in value from one sector to another." History page: "The asterisk star (*) represents an update year"; "2025 | $7.19 | $7.48 | $1.01 | $1.15 | 90.40% | $16.83"; the 2026 row is blank. The city page's 2025 State Ed ($1.01) and County ($1.15) are the reverse of DRA's figures in the site's data (county $1.01, state education $1.15); its ratio (90.40%) also differs from DRA's 89.03%. The site's data is DRA's and should be used. Raw: raw/money/city/taxrate-history.html, .txt; raw/money/city/taxbill-explained.txt
6. Nashua's elderly exemption (RSA 72:39-a) takes $305,000 off the assessed value for owners aged 65 to 74, $350,000 for ages 75 to 79 and $430,000 for 80 and older (the larger amounts began in 2025), for owners with gross income up to $57,000 (single) or $67,000 (married) and assets up to $171,000, not counting the home.
   - citation: City of Nashua Assessing Department, Elderly Exemptions; 2026 Elderly Property Owners Exemption RSA 72:39-a (application information)
   - source: https://www.nashuanh.gov/162/Elderly-Exemptions
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Page text: "Exemptions (Exemption Increases begin 2025) 65-74 years of age as of April 1st = $305,000 75-79 years of age as of April 1st = $350,000 80 years of age and older as April 1st = $430,000"; "Single person income not to exceed $57,000 Married persons joint income not to exceed $67,000"; "Assets not to exceed $171,000 (excluding the home they reside in)". The 2026 sheet (https://www.nashuanh.gov/DocumentCenter/View/34101) gives the same amounts and says the exemption is prorated by share of ownership (RSA 72:41). State rules for the exemption and the state's low and moderate income relief are in the Hart's Location file (property-tax-relief facts 1–3). Raw: raw/money/city/elderly.html, .txt; raw/money/city/elderly-2026.pdf, .txt
7. To qualify for Nashua's elderly exemption, an owner must be 65 and the owner of record by April 1, must have lived in New Hampshire for 3 consecutive years and must live in the home as their main residence, and a married couple must have been married 5 years; how long the owner has lived in Nashua doesn't count, and applications are taken January 1 to April 15 at an in-person appointment with the Assessing Department (603-589-3040).
   - citation: City of Nashua Assessing Department, Elderly Exemptions; Exemptions & Credits
   - source: https://www.nashuanh.gov/162/Elderly-Exemptions
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "Must be 65 years of age on or before April 1. Must be the owner of record on or before April 1. Must reside in the State of New Hampshire for 3 consecutive years on or before April 1. Married couples must have been married for 5 consecutive years on or before April 1."; Exemptions & Credits page: "All residents that are eligible and applying for Disabled or Elderly Exemptions must call 603.589.3040 to make an in-person appointment ... before the April 15th deadline." Premise P27.1 ("lived here for 30 years"): no rule uses years in Nashua. Raw: raw/money/city/elderly.txt; raw/money/city/exemptions.txt
8. Nashua offers a tax deferral (RSA 72:38-a) to owners 65 or older who have owned the home at least 5 years and live in it, or who qualify for Social Security disability benefits; the Board of Assessors may defer all or part of the tax if it would cause undue hardship or possible loss of the property, deferred taxes build up 5% interest a year, total deferrals may not exceed 85% of the assessed value, and a mortgage holder must approve.
   - citation: City of Nashua Assessing Department, Tax Deferral
   - source: https://www.nashuanh.gov/164/Tax-Deferral
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "Is either at least 65 years old or eligible under Title II or Title XVI of the federal Social Security Act for benefits of the disabled; and If at least 65 years old, has owned the property for at least 5 years"; "Annual interest of 5% accrues. Total tax deferrals shall not be more than 85% of assessed value of a property."; "If property is subject to a mortgage, mortgage holder must approve." Raw: raw/money/city/deferral.html, .txt
9. The City of Nashua's exemptions and credits cover blind, disabled and elderly owners, veterans and their surviving spouses, solar energy systems, improvements for persons with disabilities, and religious, educational and charitable property, plus the tax deferral; none of them depends on where a household's children go to school, and all applications are due April 15.
   - citation: City of Nashua Assessing Department, Exemptions & Credits
   - source: https://www.nashuanh.gov/157/Exemptions-Credits
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Links listed: "Blind Exemption; Disabled Exemption; Veterans or Veterans Widow Credit; Solar Energy Systems Exemption; Improvements to Assist Persons with Disabilities; Religious, Educational & Charitable Exemptions; Tax Deferral" plus Elderly Exemptions in the menu; "The deadline for all Exemptions and Credit applications is April 15th." For P19.3: no exemption is tied to private school, home school or public school use. Raw: raw/money/city/exemptions.html, .txt
10. The Nashua School District received state Education Freedom Account aid of $51,413 in FY2024, $55,197 in FY2025 and $92,713 in FY2026, and budgeted $50,000 for FY2027.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slide 26; City of Nashua FY 2027 Adopted Budget, p. 231
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Slide 26: "EDUCATION FREEDOM ACCOUNT AID $ 51,413 $ 55,197 $ 50,000 $ 92,713 $ 50,000" (FY2024, FY2025, FY2026 estimate, FY2026 actuals, FY2027 estimate). The source doesn't explain the payment; how EFA funding relates to adequacy aid is in the library (money-efa-funding-link). Raw: raw/money/district/fy27-boa-presentation-5-5-26.txt

## district-facilities-and-capital: McCarthy's Bonds, the Elm Street Building and School Debt

- kind: local
- question_type: governance_money
- description: A district's school buildings: age, planned repairs, capital reserve funds, bonds and energy projects

1. The City of Nashua paid for the new Brian S. McCarthy Middle School and the Fairgrounds and Pennichuck middle school renovations with four bonds: $45,000,000 issued in 2021 and $35,000,000 in 2022 (both for "FMS/PMS/NMS Renovations & Construction," final payments in 2047), $31,600,000 in 2023 for "NMS Constructions" (final payment 2049) and $3,135,100 in 2024 for additional middle school design and construction (final payment 2044), $114,735,100 in all (derived).
   - citation: City of Nashua FY 2027 Adopted Budget, section 4.2, General Fund – School Debt Service, p. 246
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "FMS/PMS/NMS Renovations & Construction 2021 2047 45,000,000 1.7958%"; "FMS/PMS/NMS Renovations & Construction 2022 2047 35,000,000 3.5506%"; "NMS Constructions 2023 2049 31,600,000 4.4140%"; "Additional Middle Schools Design and Construction 2024 2044 3,135,100 3.4096%". The FY2025 ACFR names the first two "New Middle School & 2 Middle School Renovations" (raw/money/city/acfr-fy2025.txt). See table nashua_middle_school_bonds. Raw: raw/money/city/fy27-adopted-budget-excerpt.pdf, .txt (PDF page 247)
2. On July 1, 2026 Nashua still owed $109,295,000 of principal on the middle school bonds; it budgeted $7,391,056 for them in FY2027 ($3,105,000 principal and $4,286,056 interest), which leaves $106,190,000 of principal and $47,797,591 of scheduled interest to pay after FY2027 (all sums derived).
   - citation: City of Nashua FY 2027 Adopted Budget, section 4.2, General Fund – School Debt Service, p. 246
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Sums of the four bonds' "Beginning Principal Balance," "Principal Payment," "Interest Payment," "Ending Principal Balance" and "Ending Interest Balance" columns (**derived**; see table nashua_middle_school_bonds). Premise P27.2: there is no single McCarthy bond. Two bonds also paid for the Fairgrounds and Pennichuck renovations, and the budget doesn't split them. The 2023 "NMS Constructions" bond alone has $30,160,000 of principal and $19,256,067 of interest left after FY2027. Raw: raw/money/city/fy27-adopted-budget-excerpt.txt
3. The City of Nashua's financial reports show authorized but unissued school debt of $567,000 at June 30, 2019, $118,187,000 at June 30, 2020 and $10,048,850 at June 30, 2025, while issued school debt (with bond premiums) rose from $41,529,060 at June 30, 2021 to $174,978,154 at June 30, 2025.
   - citation: City of Nashua, Annual Comprehensive Financial Report, FY2025, "Ratios of Long Term Debt Outstanding and Legal Debt Limits – Last Ten Fiscal Years," p. 157
   - source: https://www.nashuanh.gov/DocumentCenter/View/36501/FY2025-ACFRPDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Page viewed (raw/money/images/acfr-p163.png): "Authorized Unissued Debt at June 30 ... School Dept 119,000 1,319,000 1,319,000 567,000 118,187,000 124,589,200 ..." (2016–2021); the text layer gives 2022–2025 as "81,648,850 74,648,850 44,548,850 10,048,850". "School Department (includes unamortized bond premiums) ... 41,529,060 [2021] ... 174,978,154 [2025]". The 2019 aldermen's authorizing resolution wasn't retrieved. Raw: raw/money/city/acfr-fy2025.pdf, .txt (PDF page 163)
4. Nashua pays its school bonds through the city's Debt Service department rather than the school budget: the FY2027 budget has $12,761,411 for school debt ($6,546,750 principal and $6,214,661 interest, down from $13,521,828 in FY2026), 55.5% of the city's general fund debt service (derived), on school bonds with $158,682,750 of principal outstanding on July 1, 2026.
   - citation: City of Nashua FY 2027 Adopted Budget, p. 237 (Debt Service, Department 193) and p. 247 (school bond totals)
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "Debt Service-School ... 75100 - Principal $6,422,100 $6,546,750 ... 75200 - Interest $7,099,728 $6,214,661 ... Total Debt Service-School $13,521,828 $12,761,411"; "TOTAL GENERAL OBLIGATION BONDS: $ 158,682,750 $6,546,750 $152,136,000 $67,887,393 $6,214,661 $61,672,732". 55.5% = $12,761,411 / $22,984,943 (**derived**). The school budget itself carries only capital lease payments ($618,731). In NH DOE's DOE-25 report, Nashua's FY2025 general fund includes $10,787,550 of debt service (site data; table nashua_doe25_spending_shares). Raw: raw/money/city/fy27-adopted-budget-excerpt.txt (PDF pages 238, 248)
5. In Nashua, bonds need a two-thirds vote of the 15 aldermen and the mayor can veto a loan authorization; school debt is held to a city limit of 6% of the base valuation, outside the city's 2% general debt limit, and the city's March 2026 official statement estimates $150,341 a year in state school building grants through FY2031.
   - citation: City of Nashua, Official Statement, March 19, 2026, "Indebtedness," pp. 48–51
   - source: https://www.nashuanh.gov/DocumentCenter/View/35914/2026-Nashua-NH-Official-Statement--March-2026-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "Bonds are generally authorized on behalf of the City by a two-thirds vote of the fifteen Aldermen ... The Mayor has veto power over loan authorizations."; "school debt is subject to a limit of not more than 6% of the above described base valuation"; Debt Service Requirements table: "(150,341)" in each year 2026–2031. The ACFR adds: "The City has imposed more restrictive limits (2% City; 6% School) than state statute allows (3% City; 7% School)." Statewide bond voting rules are in the library (budget-school-bonds). Raw: raw/money/city/os-2026-03.pdf, .txt (PDF pages 48–51)
6. Nashua's Board of Aldermen resolution R-24-032 (2024) said the Elm Street Middle School property (117 Elm Street, about 8.87 acres) would no longer be needed for school use after the 2023-24 school year, and it backed selling the property through a request for proposals for development rather than by sealed bid or auction, after a city planning study found a multifamily housing development with a share of affordable units "most advantageous."
   - citation: City of Nashua, Resolution R-24-032 (Amended), "Supporting the Issuance of a Request for Proposals Relative to the Sale of the Elm Street Middle School Property"
   - source: https://www.nashuanh.gov/DocumentCenter/View/30623/R-24-032-AMENDED---Adopted--Attachment-B
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "WHEREAS, after the end of the current school year, the Elm Street Middle School will no longer be used as a middle school"; "the City anticipates a vote by the Board of Education in the summer of 2024, pursuant to New Hampshire RSA 199:4, II, that that the Elm Street Middle School is no longer needed for public school purposes, and to transfer the care and control of the property to the City"; "located at 117 Elm Street ... approximately 8.87 acres"; "a multifamily housing development with a portion of it being set aside as affordable is most advantageous". The document shows no adoption date; NH Business Review (January 22, 2025) reported the aldermen approved it in March 2024 (raw/money/news/nhbr-elm.txt). The Board of Education's transfer vote wasn't retrieved. Raw: raw/money/city/R-24-032.pdf, .txt
7. Resolution R-24-032 requires any Elm Street proposal to include units for residents with federally funded housing vouchers and to keep the Keefe Auditorium, bars proposals that would demolish the auditorium, lets community groups keep using it until redevelopment interferes, and says any sale needs a further vote of the Board of Aldermen.
   - citation: City of Nashua, Resolution R-24-032 (Amended)
   - source: https://www.nashuanh.gov/DocumentCenter/View/30623/R-24-032-AMENDED---Adopted--Attachment-B
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "conveyance of the property shall require further approval by the Board of Aldermen"; "any proposal shall include a portion of units for residents that have federally funded housing vouchers"; "the request for proposals shall not seek nor accept any proposals including the demolition of the Keefe Auditorium"; "the City of Nashua shall continue to allow community and civic groups to utilize the Keefe Auditorium until such a time as any re-development shall interfere". Raw: raw/money/city/R-24-032.txt
8. Nashua received four proposals for the Elm Street Middle School site, and in April 2025 the two finalists presented housing plans in public: the Lansing Melbourne Group (59 affordable and 237 market-rate units, 413 parking spaces, the school demolished except for the Keefe Auditorium, and a community child care center) and Pennrose (168 or 184 units, renovating the front of the building and removing the back).
   - citation: Nashua Telegraph, "Top two developers make pitches to transform Elm Street School into housing," April 16, 2025; NH Business Review, January 22, 2025
   - source: https://www.nashuatelegraph.com/news/2025/04/16/top-two-developers-make-pitches-to-transform-elm-street-school-into-housing/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: News is the only source found for the finalists and plans. Text: "Mayor James Donchess said the city received four proposals with Lansing Melbourne and Pennrose coming out on top"; "The development would include 59 units of affordable housing, 237 units at market rate and 413 parking spaces"; "the school building would be demolished with the exception of the Keefe Auditorium"; Pennrose's first concept "features 168 units"; the second "would allow for 184 units". The presentations were April 10 and 12, 2025 at City Hall (raw/money/news/tel-2025-04-03-elm.txt). No selection, agreement or sale vote after April 2025 was found (see Not retrieved). Raw: raw/money/news/tel-2025-04-16-elm.html, .txt; raw/money/news/nhbr-elm.txt
9. The City of Nashua's FY2027 budget, adopted in June 2026, reports that during FY2026 the city's building staff managed 117 Elm Street, the former Elm Street Middle School, including the Nashua Warming Station and Keefe Auditorium performances, and scheduled rentals at Elm Street Middle School.
   - citation: City of Nashua FY 2027 Adopted Budget, section 3.2.9 City Buildings, "FY26 Highlights & Accomplishments," p. 94; section 3.8.1 Community Services, p. 146
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "Managed facility operations and use at 117 Elm Street, including the Nashua Warming Station and Keefe Auditorium performances"; "Coordinated event scheduling and rental activities across multiple facilities, including Elm Street Middle School, Court Street Theater, and the Hunt Building". Community Services: "Operated the Elm Street Overflow Warming Station ... Approximately 277 unique guests served" (the dates are printed "December 1, 2026- March 14, 2026"). The address is from R-24-032. Raw: raw/money/city/fy27-adopted-budget-excerpt.pdf, .txt (PDF pages 95, 147); raw/money/city/R-24-032.txt (address)
10. Nashua is still paying off a bond for an Elm Street Middle School roof: $105,000 of principal was owed on July 1, 2026, with $17,000 of principal and $4,645 of interest budgeted for FY2027 and the last payment due in 2032.
   - citation: City of Nashua FY 2027 Adopted Budget, section 4.2, General Fund – School Debt Service, p. 246
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Nashua
   - note: Text: "Refunding Elm Street Roof Replacement 2021 2032 166,250 1.7958% 105,000 17,000 88,000 14,985 4,645 10,340". Raw: raw/money/city/fy27-adopted-budget-excerpt.txt (PDF page 247)
11. Nashua's facilities master plan (with Harriman, 2025–2026) found about $197 million of school repairs needed over 10 years, about $167 million of which would go unaddressed at the current $2 million-a-year capital plan, plus about $114 million of program space changes, and room for up to 1,164 more students in the elementary schools based on October 1, 2025 enrollment.
   - citation: Nashua School District, Facilities Master Plan, School Board Workshop presentation, October 21, 2026, slide 4
   - source: https://www.nashua.edu/fs/resource-manager/view/87de9b02-bd48-4e0a-959f-a3a1a15ec4c0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "$197M+/- in repairs identified within the next 10 years. • Current CIP for 10 years based on $2M/year. This will leave $167M in repairs unaddressed"; "$114M+/- in program space modifications"; "Based on October 1, 2025 enrollment, there is capacity for up to 1,164 more students in the elementary schools". Linked from https://www.nashua.edu/our-district/board-of-education/facilities-master-plan-2025. Raw: raw/money/district/fmp-workshop-10-21-26.pdf, .txt
12. Nashua's facilities master plan estimates that each school closed would save about $1.6 to $1.8 million a year in operating costs; its October 2026 options range from repairing all 12 elementary schools (Option A, $164 to $211 million for the elementary schools) to closing Mount Pleasant (F), closing Mount Pleasant and New Searles (B), or replacing two to five older schools with one or two new ones (C to E), and the plan's next step was to narrow the options to one.
   - citation: Nashua School District, Facilities Master Plan, School Board Workshop presentation, October 21, 2026, slides 50, 52, 54 and 56
   - source: https://www.nashua.edu/fs/resource-manager/view/87de9b02-bd48-4e0a-959f-a3a1a15ec4c0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "For Each school that closes it equates to approximately $1.6 to 1.8M in operational savings per year"; "If new schools are built as part of an option there will be cost savings ... but the savings will most likely be less"; Option A "Estimated ROM ES Cost: $164M to $211M"; "Option B Redistributes students into existing buildings and closes ... one in the northern (MP) and one in the southern area (NS)"; "Option F ... closes one school (MP)"; "Next Steps • Narrow the Options • Identify the Final Long-Term Option". Community feedback opposed closing Mount Pleasant and New Searles (slides 45–46). Raw: raw/money/district/fmp-workshop-10-21-26.txt
13. Nashua's FY2027 city budget has $500,000 for school deferred maintenance in capital improvements ($300,000 proposed plus $200,000 added during budget review), and the district's FY2027 capital request also listed a Bicentennial roof ($1.857 million), security system replacements ($500,000), air filtration at both high schools ($1.3 million), complete repaving at Nashua North ($1.4 million) and facilities master plan projects ($1.947 million).
   - citation: City of Nashua FY 2027 Adopted Budget, pp. 12 and 240; Nashua School District FY 2027 Budget Presentation, February 17, 2026, slide 21
   - source: https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: City budget: "Add: Deferred Maintenance - Schools Capital Improvements Dowd 200,000"; "Education $300,000 $300,000 $300,000 $500,000". District slide (https://www.nashua.edu/fs/resource-manager/view/7b0e932b-c7e4-4496-a4bd-ff974263331f): "Our FY27 Capital Request includes replacing the roof at Bicentennial ($1.857M) ... Security System Replacements ($500K), Sanalife Air Filtration at the both HS ($1.3M), NHS North complete repaving ($1.4M) and Facility Master Plan projects ($1.947M)". Which requested projects were funded was not found. Raw: raw/money/city/fy27-adopted-budget-excerpt.txt (PDF pages 13, 241); raw/money/district/fy27-presentation-2-17-26.txt

## district-classrooms-and-staff: Nashua's Staff Openings in 2026-27

- kind: local
- question_type: local_practice
- description: How a district's schools group classes and grades, their staff and roles, staffing changes, substitutes and aides, and how the schools describe themselves

1. On September 14, 2026 the Nashua School District reported 63 openings to the Board of Education's Human Resources Committee, listing 11 teachers, 3 school psychologists, 2 speech-language pathologists, 15 behavior technicians, 36 paraprofessionals, 14 food service, 11 facilities, 8 crossing guard, 4 administrative and 2 secretary positions.
   - citation: Nashua Board of Education, Human Resources Committee minutes, September 14, 2026
   - source: https://drive.google.com/file/d/1zliaR5ONx1240JuRqf5YBB6sHeScujLd/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "The district reported 63 openings: 11 teachers, 3 school psychologists, 2 speech-language pathologists, 15 behavior technicians, 36 paraprofessionals, 14 food service positions, 11 facilities operations positions, 8 crossing guards, 4 administrative positions, and 2 secretaries." The listed counts add to 106 (**derived**), not 63; the minutes are quoted as written. Linked from https://www.nashua.edu/our-district/board-of-education/boe-meeting-agendas-and-minutes/human-resources. Staff names in the minutes are not used. Raw: raw/money/district/hr-2026-09-14-minutes.pdf, .txt
2. Nashua's September 2026 staffing report said contractors were covering four intensive-needs special education openings, other special education staff were covering openings at Amherst Street and Main Dunstable, current math teachers were covering a high school math opening and paraprofessional coverage was "somewhat below full staffing"; elementary openings included a fifth-grade job at Birch Hill and a kindergarten job at New Searles, and the district was recruiting through Ed Jobs New Hampshire, Top School Jobs, K-12 Jobs, Handshake and SchoolSpring.
   - citation: Nashua Board of Education, Human Resources Committee minutes, September 14, 2026
   - source: https://drive.google.com/file/d/1zliaR5ONx1240JuRqf5YBB6sHeScujLd/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Contractors cover the intensive-needs special education positions, while behavior specialists temporarily backfill three of the four positions."; "Existing special education staff are covering vacancies at Amherst Street and Main Dunstable"; "Current math teachers are covering the math opening."; "Paraprofessional coverage remains somewhat below full staffing, although the 36 openings do not represent 36 contractors."; "one fifth-grade position at Birch Hill, one kindergarten position at New Searles". Raw: raw/money/district/hr-2026-09-14-minutes.txt
3. The human resources update in the packet for the Board's November 16, 2026 committee meeting listed 92 openings: 8 teachers (5 elementary, none in middle school, 3 high school), 3 school psychologists, 2 speech-language pathologists, 13 behavior technicians, 39 paraprofessionals ("most being covered by contractors"), 11 food service, 11 plant operations (including 8 crossing guards and 1 custodian), 4 administrators and 1 secretary.
   - citation: Nashua Board of Education, Human Resources Committee agenda and attachments, November 16, 2026 (memo from the Director of Human Resources)
   - source: https://drive.google.com/file/d/1XBPDKVvMSzj6qwP8q1wdlJK0oE_tNX8h/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Job Openings o Total = 92 Teachers for the 26/27 SY = 8 • Elementary – 5 • Middle – 0 • High School – 3 School Psychologist – 3 Speech Language Pathologist – 2 Behavior Tech's – 13 Paras – 39 (most being covered by contractors) Food Service = 11 Plant Operations = 11 • Custodian – 1 • Crossing Guards – 8 Administration = 4 ... Secretaries = 1 (South)". These counts add to 92 (**derived**). The meeting was the day after this check. Raw: raw/money/district/hr-2026-11-16-agenda.pdf, .txt
4. The Nashua School District's FY2027 budget presentations list special education "Workforce shortages persist" and "Staff turnover is leading to the loss of institutional knowledge and increasing the need for training and development" among its challenges, and say it was less difficult to hire for these positions before COVID.
   - citation: Nashua School District FY 2027 Budget Presentation, February 17, 2026, slide 16; FY2027 Budget Presentation, May 5, 2026, slide 18
   - source: https://www.nashua.edu/fs/resource-manager/view/7b0e932b-c7e4-4496-a4bd-ff974263331f
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Slide 16 text: "Challenges: o Workforce shortages persist o Staff turnover is leading to the loss of institutional knowledge and increasing the need for training and development o Rising costs of contracted services"; opportunities listed include "Innovative recruitment strategies". No turnover rate, overall or by school, was found in these or other district documents. Raw: raw/money/district/fy27-presentation-2-17-26.txt; raw/money/district/fy27-boa-presentation-5-5-26.txt

## district-board-and-public-input: The Nashua Board of Education, Its Meetings and Public Comment

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. The Nashua Board of Education has nine members elected citywide to staggered four-year terms (five or four seats are elected every two years), plus two non-voting student members elected each year by students at Nashua High School North and South; it sets policy, approves curriculum, approves personnel decisions, negotiates union contracts and sets the annual operating budget.
   - citation: Nashua School District, Board of Education page
   - source: https://www.nashua.edu/our-district/board-of-education
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "The Board consists of nine members who are each elected to four-year terms. Members serve city-wide and terms of office are offset such that either five or four positions are elected every two years. Since 2013, two high school representatives serve the Board. NHS North students and NHS South students vote each year to elect a student representative from each school to serve as non-voting members of the Board."; "setting policy, approving curriculum and assessment materials and strategies, approving human resource decisions, negotiating union contracts, overseeing operations and finance decisions, and establishing the annual operating budget." How the budget then goes to the aldermen is in the library (district-practices fact 94, budget-city-school-districts). Raw: raw/money/district/boe.html, .txt
2. The Nashua Board of Education generally meets on the second and last Monday of each month, usually in the Nashua High School North Board Room, and its meetings are broadcast live on Nashua ETV; the district calendar listed a regular board meeting on Monday, November 16, 2026 at 6:00 p.m.
   - citation: Nashua School District, Board of Education page; BOE Meeting Schedule (calendar); NSD Operating Budget page
   - source: https://www.nashua.edu/our-district/board-of-education/boe-meeting-schedule
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Board page: "The Nashua Board of Education meetings are generally held the second and last Monday of each month, according to an established schedule." Calendar: "BOE Meeting 6:00 PM - NHS North Board Room" (November 16, 2026). Operating budget page: "Like all Nashua Board of Education meetings, budget committee meetings will be broadcast live on Nashua ETV" (additional-data/raw/districts/batch-2/nashua-operating-budget.txt). Policy BEA: notice is posted on the district website under RSA 91-A, and changes of date, time or place are posted at least 24 hours ahead (raw/money/district/BEA-regular-meetings.txt). Raw: raw/money/district/boe-schedule.html, .txt; raw/money/district/boe.txt
3. The Nashua Board of Education has five standing committees (Budget, which meets as needed from about January to May; Curriculum and Evaluation, quarterly; Finance and Operations, the second Monday of the month; Human Resources, quarterly; and Policy, the first Tuesday of the month), and members also serve on the Joint Special School Building Committee with aldermen and on the Education Council.
   - citation: Nashua School District, Board of Education page
   - source: https://www.nashua.edu/our-district/board-of-education
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "The Board has five standing committees: Budget; Curriculum and Evaluation; Finance and Operations; Human Resources; and Policy, and members serve on two other Committees: Joint Special School Building Committee (JSSBC) and Education Council." Committee table: "Budget as needed during the budget season, which typically runs from January through May"; "Curriculum and Evaluation Quarterly"; "Finance and Operations second Monday of the month"; "Human Resources Quarterly"; "Policy first Tuesday of the month". Agendas and minutes are posted under BOE Meeting Agendas and Minutes. Raw: raw/money/district/boe.txt
4. Under Nashua Board of Education policy BEDH, each regular meeting has 30 minutes of public comment in two 15-minute periods, the first at the start for items on the agenda and the second at the end for other district matters; each speaker gets 3 minutes and can't pass time to another speaker, speakers are asked but not required to sign up beforehand, and they must identify themselves for the minutes.
   - citation: Nashua Board of Education Policy BEDH, Public Comment & Participation at Board Meetings (last approved December 19, 2022)
   - source: https://www.nashua.edu/fs/resource-manager/view/1fe6998c-bd2f-4524-8a22-6b67276a3bf0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "The Board will provide 30 minutes divided into two 15-minute periods to hear public comment. The first 15-minute period shall be at the beginning of each regular Board meeting for items on the agenda. The second 15-minute period shall be at the end of each regular board meeting for other District matters."; "Individual speakers will be allotted three (3) minutes per person. Speakers may not relinquish allotted time to another speaker."; "Although such pre-registration is not required"; "speakers shall identify themselves clearly for the record". Each period may be extended by a majority vote. The state's public comment law is RSA 189:74. Linked from https://www.nashua.edu/our-district/board-of-education/boe-policies-and-procedures. Raw: raw/money/district/BEDH-public-comment.pdf, .txt
5. Nashua's policy BEDH says public comment is not a question-and-answer session and board members usually defer any response to the full board; comments about individual students or employees (other than the superintendent) should go to the superintendent or through the complaint policies KE and KEB; and residents may ask for an item to be put on the agenda by writing to the superintendent at least 14 days before the meeting.
   - citation: Nashua Board of Education Policy BEDH, sections B.5, B.7 and B.8
   - source: https://www.nashua.edu/fs/resource-manager/view/1fe6998c-bd2f-4524-8a22-6b67276a3bf0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "the public comment period is an opportunity for members of the public to provide their input to the Board but is not a questions and answer session ... in most instances, any board response will be deferred pending consideration by the full Board."; "comments (including complaints) regarding individual students, volunteers, or employees (other than the Superintendent) should be directed to the Superintendent or otherwise provided under ... KE-Public Complaints and/or KEB"; "Requests to have a matter placed on an agenda should be presented in writing to the Superintendent no less than fourteen days prior to the next Board meeting". After two warnings, the chair may have a disruptive person leave (section C). Raw: raw/money/district/BEDH-public-comment.txt
6. Residents can write to the Nashua Board of Education at boe@nashua.edu; the board says these emails are public correspondence under New Hampshire's Right-to-Know Law (RSA 91-A), are noted in the meeting minutes and are open to the public, so writers should be careful about including student names or other personal information.
   - citation: Nashua School District, Board of Education page
   - source: https://www.nashua.edu/our-district/board-of-education
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Emails sent to the boe@nashua.edu email address are considered public correspondence with the Board under New Hampshire's Right-to-Know Law, RSA Chapter 91-A. The email will be noted in the Board meeting minutes, and be accessible to members of the public; therefore, we caution writers of emails to be guarded about including student personal information, such as their names." Raw: raw/money/district/boe.txt

## district-facility-use: Community Use of School Buildings and Fields

- kind: local
- question_type: local_practice
- description: Community use of school buildings and fields: who may use gyms, auditoriums and fields, fees and exempt groups, insurance and how to apply

1. Nashua Board of Education policy KF treats school buildings, grounds and athletic fields as community facilities; groups must request space online at least 30 days ahead, and when requests conflict, school-related groups come first, then non-profit youth groups, other non-profits and for-profit groups.
   - citation: Nashua Board of Education Policy KF, Community Use of School Facilities (last approved May 12, 2025)
   - source: https://resources.finalsite.net/images/v1753909148/nashuaedu/ym5cmxml2adg3eqcvcvw/KF_Community_Use_of_School_Facilities.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Nashua public schools and athletic fields are community facilities, and should be accessible for community use within available time and resources."; "must complete and submit an online facility request at least thirty (30) calendar days prior to the date of the event"; "requests shall be granted in the following order: school-related groups; non-profit youth–related groups; other non-profit organizations; and for-profit organizations. Proof is required to demonstrate non-profit status." Requests go through ML Schedules (Facility Rentals page, https://www.nashua.edu/families-community/facility-rental). Raw: raw/money/district/KF-community-use.pdf, .txt; raw/money/district/facility-rental.html, .txt
2. Under Nashua's policy KF, public youth leagues pay no rental fees and are charged custodial overtime only when no staff are already scheduled; the listed leagues include PAL football, cheerleading, cross country and wrestling, the Elks Crusaders, Cal Ripken, Little League, Ray Oban and Babe Ruth baseball and girls softball, Nashua Blast lacrosse, the Nashua Youth Soccer League and the Boys and Girls Club of Greater Nashua, the superintendent may add others, and district groups, city departments, PTOs and Scouts pay no fees at all.
   - citation: Nashua Board of Education Policy KF, "Exempt Groups"
   - source: https://resources.finalsite.net/images/v1753909148/nashuaedu/ym5cmxml2adg3eqcvcvw/KF_Community_Use_of_School_Facilities.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Public access youth leagues, shall be exempt from rental fees. Custodial overtime charges will only be applied to events when staff are not scheduled to be on duty."; list includes "Other teams as determined by the Superintendent"; "Nashua School District-based organizations and teams, City Departments, School District PTOs, and Boy Scouts/Girl Scouts, are not subject to reservation fees, rental fees, or overtime charges." The FAQ says most youth groups are exempt and others "may be approved by the superintendent's office" (raw/money/district/facility-faq-2024.txt). Raw: raw/money/district/KF-community-use.txt
3. For non-profit groups that aren't exempt, Nashua's daily rental fees effective July 1, 2025 are $100 for an elementary school gym, $125 for a middle school gym and $325 for a large high school gym ($200, $250 and $700 for for-profit groups), $40 for a classroom and $250 for a playing field, with a 50% deposit paid by check.
   - citation: Nashua Board of Education Policy KF, "Facilities Rental Fees and Charges for Non-Profit Groups, Effective July 1, 2025"; Facility Rental FAQ (2024)
   - source: https://resources.finalsite.net/images/v1753909148/nashuaedu/ym5cmxml2adg3eqcvcvw/KF_Community_Use_of_School_Facilities.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Fee table: "Elementary School Gym $100 $200"; "Middle School Gym $125 $250"; "High School Gym – Large Wood Floor $325 $700"; "High School Gym – Small Rubber Floor $75 $175"; "High School Auditorium $350 $775"; "Classrooms (all schools) $40 $80"; "Playing Field (excluding Stellos Stadium) $250 $550"; "All rental fees are charged on a daily basis." FAQ: "We do not accept credit or debit cards at this time." Raw: raw/money/district/KF-community-use.txt; raw/money/district/facility-faq-2024.pdf, .txt
4. Nashua charges non-exempt groups $40 an hour per custodian (3-hour minimum) for custodial coverage beyond normal staffing and $30 an hour (3-hour minimum) for the district staff person required at athletic fields; kitchens need a district cook at the overtime rate, and events over 250 people may need extra custodians, crowd management, or police or fire details.
   - citation: Nashua Board of Education Policy KF, "Overtime/Staffing Charges"
   - source: https://resources.finalsite.net/images/v1753909148/nashuaedu/ym5cmxml2adg3eqcvcvw/KF_Community_Use_of_School_Facilities.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "any organization requiring custodial coverage in a school building over and above the normal staffing complement shall be charged a rate of $40 per hour per custodian (3-hour minimum)"; "The use of an athletic field requires the presence of a School District staff person ... at a rate of $30 per hour (3-hour minimum)"; "Events with over 250 attendees may be subject to additional staffing requirements". Raw: raw/money/district/KF-community-use.txt
5. The main gyms at Nashua's two high schools (the Richard Belanger Gymnasium at South and the primary gym at North) are not routinely available to outside groups, and Stellos Stadium, run with the city's Parks and Recreation department, may be used only by youth organizations under a city ordinance and is not rented.
   - citation: Nashua Board of Education Policy KF
   - source: https://resources.finalsite.net/images/v1753909148/nashuaedu/ym5cmxml2adg3eqcvcvw/KF_Community_Use_of_School_Facilities.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Stellos Stadium can only be used by youth organizations (Nashua City Ordinance 0-02-94). Stellos Stadium is not available for rentals."; "The Richard Belanger Gymnasium at Nashua High School South and the primary gymnasium at Nashua High School North are not routinely available to outside groups." The Director of Athletics or Plant Operations may also limit field use to school groups. Raw: raw/money/district/KF-community-use.txt
6. Groups using Nashua school facilities need a district-approved ML Schedules account and a certificate of insurance ($1,000,000 personal injury and $2,000,000 aggregate) naming the City of Nashua, non-profits must upload proof of non-profit status, cancellations need 72 hours' notice, and questions go to event-requests@nashua.edu (buildings) or athletic-requests@nashua.edu (athletic facilities).
   - citation: Nashua School District, Facility Rentals page; Facility Rental FAQ (2024); Policy KF
   - source: https://www.nashua.edu/families-community/facility-rental
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: FAQ: "All accounts must be approved by a facility administrator before you may begin entering requests."; "$1,000,000 personal injury/$2,000,000 general aggregate with the City of Nashua ... listed as the additional insured"; "upload a copy of your IRS 501c3 determination letter"; "at least 72 hours' notice". Page: "event-requests@nashua.edu"; "athletic-requests@nashua.edu" (role addresses; staff names omitted). Raw: raw/money/district/facility-rental.txt; raw/money/district/facility-faq-2024.txt
7. The Nashua School District's facilities rental fund took in $219,377 in FY2024 and $154,042 in FY2025, with $150,000 budgeted for FY2026 and FY2027.
   - citation: Nashua School District FY2027 Budget Presentation, May 5, 2026, slide 28 (Special Revenue – Revenue); City of Nashua FY 2027 Adopted Budget, p. 33
   - source: https://www.nashua.edu/fs/resource-manager/view/06573d9b-776f-4a37-b73e-4b2f5635dee5
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Nashua
   - note: Text: "Dept. 2217 - Facilities Rental $ 219,377 $ 154,042 $ 150,000 $ 45,157 $ 150,000" (actual FY2024, actual FY2025, budget FY2026, FY2026 actual to date, budget FY2027). City budget (School Special Revenue Funds): "School Facilities Rental $150,000 $150,000 $150,000 $150,000". Raw: raw/money/district/fy27-boa-presentation-5-5-26.txt; raw/money/city/fy27-adopted-budget-excerpt.txt (PDF page 34)

## money-local-school-tax: The Local School Tax

- kind: how_it_works
- question_type: governance_money
- description: How the local school tax rate covers the rest of the school budget.

1. New Hampshire law has the money a school district needs raised by a tax assessed "upon the taxable property of the district," so the local school tax is figured from the value of taxable property, not from whether the owner's household uses the public schools.
   - citation: RSA 198:5
   - source: https://gc.nh.gov/rsa/html/XV/198/198-5.htm
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Statute text: "The selectmen of the town, in their next annual assessment, shall assess upon the taxable property of the district a sum sufficient to meet the obligations above enumerated, with such alterations thereof as may be voted by the district, and shall pay the same over to the district treasurer as the school board shall require for the maintenance of schools." The second clause restates what the statute bases the tax on; the statute doesn't mention school use. The statewide education tax is likewise imposed on "all persons and property taxable" (RSA 76:3, library money-statewide-education-property-tax fact 1). For P19.3. Raw: raw/money/state/rsa-198-5.html, .txt

## educator-expense-deduction: Teachers' Classroom Expenses: The Federal Educator Deduction

- kind: rule
- question_type: help
- description: Teachers' unreimbursed classroom expenses: the federal educator expense deduction.

1. An eligible educator (a kindergarten through grade 12 teacher, instructor, counselor, principal or aide who works at least 900 hours a school year) may deduct up to $300 of unreimbursed classroom costs, such as books, supplies, computer equipment and software, supplementary materials and professional development courses, on the federal income tax return ($600 for a married couple filing jointly if both are eligible, up to $300 each).
   - citation: Internal Revenue Service, Topic no. 458, Educator expense deduction (page last reviewed or updated November 9, 2026)
   - source: https://www.irs.gov/taxtopics/tc458
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - note: Text: "If you're an eligible educator, you can deduct up to $300 ($600 if married filing jointly and both spouses are eligible educators, but not more than $300 each) of unreimbursed trade or business expenses. Qualified expenses are amounts you paid or incurred for participation in professional development courses, books, supplies, computer equipment (including related software and services), other equipment, and supplementary materials that you use in the classroom."; "kindergarten through grade 12 teacher, instructor, counselor, principal or aide for at least 900 hours a school year". It is claimed on Schedule 1 (Form 1040). For P31.2. Raw: raw/money/state/tc458.html, .txt

## nashua_education_appropriation: Nashua School (Education) Appropriation, FY2022–FY2027

- unit: dollars
- period: fiscal years 2021-22 to 2026-27; year: the year the fiscal year ends (2027 = 2026-27)
- source: City of Nashua Official Statement, March 19, 2026, "Budget Summary" p. 38 (FY2022–FY2026) — https://www.nashuanh.gov/DocumentCenter/View/35914/2026-Nashua-NH-Official-Statement--March-2026-PDF ; City of Nashua FY 2027 Adopted Budget, p. 23 (FY2027) — https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
- as_of: 2026-11-15
- raw: raw/money/city/os-2026-03.txt (PDF page 38); raw/money/city/fy27-adopted-budget-excerpt.txt
- topic: district-budget-and-cost
- place: district Nashua
- note: Value is the city's General Fund appropriation for Education (the school department), including employee benefits and excluding school bond payments. The Official Statement's footnotes report citywide supplemental appropriations after adoption (for example $19,280,295 in FY2022) without saying how much went to schools. The change column is **derived**. FY2027 is the adopted budget.

| Place | District id | Year | Value | Change from prior year |
|---|---|---|---|---|
| Nashua | 371 | 2022 | 162316834 | |
| Nashua | 371 | 2023 | 167231489 | 3.0% |
| Nashua | 371 | 2024 | 173793393 | 3.9% |
| Nashua | 371 | 2025 | 182240036 | 4.9% |
| Nashua | 371 | 2026 | 191262559 | 5.0% |
| Nashua | 371 | 2027 | 205367867 | 7.4% |

## nashua_doe25_spending_shares: General Fund Spending by Function, FY2025: Nashua, Neighbors and the State

- unit: percent
- period: fiscal year 2024-25; year: 2025
- source: site data: NH DOE DOE-25 expenditure lines (tables expenditure, doe_form, expenditure_state_total), General Fund (elementary, middle, high school, district-wide programs and other financing uses)
- as_of: 2026-11-15
- raw: raw/money/derived/doe25-general-fund-shares-fy2025.csv (query output, November 15, 2026) and .sql.txt (the query)
- topic: district-budget-and-cost
- place: district Nashua
- note: All shares are **derived**: each function's General Fund spending divided by the district's total General Fund spending in DOE-25. Value is instruction (accounts 1100–1400). Support is student and instructional staff support (2100, 2200: counseling, health, library, curriculum, training). General administration is 2300 (superintendent's office and school board); school administration is 2400 (principals' offices); business and central is 2500, 2800 and 2900. Debt is principal and interest (5110, 5120). Other covers transfers, charter school payments and community programs. Rows may not total exactly 100 because of rounding. Hollis runs grades K–6 and the Hollis-Brookline Cooperative grades 7–12, so neither is a like-for-like comparison with Nashua. Merrimack and Litchfield report no general fund debt service. Shares say where money went, not whether it was enough.

| Place | District id | Year | Value | Support | General administration | School administration | Business and central | Plant | Transportation | Debt service | Other | General fund total ($) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nashua | 371 | 2025 | 58.1 | 13.1 | 2.3 | 4.6 | 1.3 | 9.1 | 5.1 | 5.6 | 0.8 | 191861790 |
| Hudson | 267 | 2025 | 58.5 | 11.6 | 2.0 | 5.6 | 3.4 | 10.6 | 5.5 | 1.0 | 1.9 | 63345222 |
| Merrimack | 351 | 2025 | 61.2 | 14.1 | 3.4 | 4.9 | 1.2 | 7.1 | 5.9 | 0.0 | 2.1 | 89258959 |
| Hollis | 259 | 2025 | 59.8 | 11.9 | 4.6 | 5.9 | 0.0 | 6.9 | 3.5 | 6.2 | 1.2 | 17106637 |
| Hollis-Brookline Cooperative | 260 | 2025 | 59.5 | 12.0 | 4.3 | 5.9 | 0.0 | 8.9 | 4.7 | 3.5 | 1.0 | 29118003 |
| Bedford | 41 | 2025 | 62.1 | 10.6 | 2.2 | 7.3 | 1.4 | 7.4 | 4.6 | 3.9 | 0.5 | 84287198 |
| Manchester | 335 | 2025 | 56.1 | 9.3 | 1.3 | 5.2 | 2.3 | 5.4 | 7.9 | 4.7 | 7.7 | 240213454 |
| NH | | 2025 | 60.1 | 10.7 | 3.6 | 5.3 | 1.7 | 8.1 | 5.2 | 3.0 | 2.4 | 3968203433 |

## nashua_middle_school_bonds: Bonds for McCarthy Middle School and the Middle School Renovations

- unit: dollars
- period: FY2027 debt schedule (balances on July 1, 2026 and after FY2027 payments); year: 2027
- source: City of Nashua FY 2027 Adopted Budget, section 4.2, General Fund – School Debt Service, p. 246 — https://www.nashuanh.gov/DocumentCenter/View/36466/FY-2027-Adopted-Budget-PDF
- as_of: 2026-11-15
- raw: raw/money/city/fy27-adopted-budget-excerpt.pdf, .txt (PDF page 247)
- topic: district-facilities-and-capital
- place: town Nashua
- note: Value is the amount issued. Bond names are as printed (FMS = Fairgrounds Middle School, PMS = Pennichuck Middle School, NMS = new middle school, now Brian S. McCarthy Middle School). The two FMS/PMS/NMS bonds paid for the new school and both renovations together. The totals row is **derived**.

| Place | Town id | Bond | Year issued | Final year | Value | Rate | Principal July 1, 2026 | FY2027 principal | FY2027 interest | Principal after FY2027 | Interest after FY2027 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Nashua | 371 | FMS/PMS/NMS Renovations & Construction | 2021 | 2047 | 45000000 | 1.7958% | 42040000 | 1340000 | 1143050 | 40700000 | 10228750 |
| Nashua | 371 | FMS/PMS/NMS Renovations & Construction | 2022 | 2047 | 35000000 | 3.5506% | 33385000 | 870000 | 1502700 | 32515000 | 17267274 |
| Nashua | 371 | NMS Constructions | 2023 | 2049 | 31600000 | 4.4140% | 30895000 | 735000 | 1509506 | 30160000 | 19256067 |
| Nashua | 371 | Additional Middle Schools Design and Construction | 2024 | 2044 | 3135100 | 3.4096% | 2975000 | 160000 | 130800 | 2815000 | 1045500 |
| Nashua | 371 | Total (derived) | | | 114735100 | | 109295000 | 3105000 | 4286056 | 106190000 | 47797591 |

## nashua_para_and_metro_wages: Nashua Paraeducator Pay and Manchester-Nashua Hourly Wages

- unit: dollars per hour
- period: Nashua paraeducator schedules 2025-26 to 2027-28; BLS OEWS May 2025; year: the year the school year ends, or 2025 for BLS
- source: Nashua paraeducators' agreement 2025–2028, Appendix B — https://www.nashua.edu/fs/resource-manager/view/3284d3f8-5857-4aa4-8e9c-36e4e2f116f0 ; BLS OEWS May 2025, Manchester-Nashua, NH metropolitan area (31700), BLS public data API — https://api.bls.gov/publicAPI/v1/timeseries/data/
- as_of: 2026-11-15
- raw: raw/money/district/para-2025-2028.txt; raw/money/state/bls-oews-msa31700-may2025.json
- topic: district-budget-and-cost
- place: district Nashua
- note: The metro area isn't a site town. Value is the Nashua hourly rate or the BLS mean hourly wage; Median is BLS's median hourly wage; Employment is BLS's estimate for the area. BLS publishes no hourly wage for teaching assistants in this area (its annual mean is $38,890 and annual median $37,220, with 2,330 employed). Comparisons are **derived** and hourly only.

| Place | Year | Job | Value | Median | Employment |
|---|---|---|---|---|---|
| Nashua | 2026 | Instructional paraeducator, step 1 (2025-26) | 18.01 | | |
| Nashua | 2026 | Instructional paraeducator, step 13 (2025-26) | 25.26 | | |
| Nashua | 2027 | Instructional paraeducator, step 1 (2026-27) | 19.01 | | |
| Nashua | 2027 | Districtwide special education paraeducator, step 1 (2026-27) | 19.94 | | |
| Nashua | 2027 | Instructional paraeducator, step 13 (2026-27) | 26.26 | | |
| Nashua | 2028 | Instructional paraeducator, step 1 (2027-28) | 20.01 | | |
| Manchester-Nashua metro area | 2025 | Retail salespersons | 18.56 | 16.99 | 6660 |
| Manchester-Nashua metro area | 2025 | Cashiers | 15.53 | 15.24 | 4880 |
| Manchester-Nashua metro area | 2025 | Stockers and order fillers | 17.78 | 17.33 | 3400 |
| Manchester-Nashua metro area | 2025 | Food preparation workers | 17.02 | 17.47 | 860 |

## For another file

- **Special education (agent 5; P13.2, P6.2):** the HR vacancy reports (36–39 para and 13–15 behavior technician openings, "most being covered by contractors"; raw/money/district/hr-2026-09-14-minutes.txt, hr-2026-11-16-agenda.txt). The May 5, 2026 presentation also has out-of-district placements (108 students in 2021-22, 129 in 2024-25, 111 in 2025-26, slide 19) and intensive-needs placements (36 of 228 intensive-needs students attend their neighborhood school, slide 30) (raw/money/district/fy27-boa-presentation-5-5-26.txt).
- **Zones and transportation (agent 7; P29.2, P5.3, P14.2, P8.1):** the facilities master plan's elementary utilization table and closure options with community feedback (raw/money/district/fmp-workshop-10-21-26.txt, slides 45–52). From the February 17, 2026 presentation, slides 28–29: 95 buses (52 regular, 43 special education), about 4,000 daily riders, and charter schools taking about 24 bus tiers, about $1 million a year (raw/money/district/fy27-presentation-2-17-26.txt). Eight crossing guard openings in November 2026.
- **Pathways (agent 4; P32.2):** the para contract's $8,000 tuition pool covers para certification courses (district-budget-and-cost fact 19). The teachers' contract (Article 5:8) reimburses 80% of tuition for approved advanced degree and critical shortage area courses (raw/money/district/teacher-2025-2029.txt).
- **English learners and meals (agent 6):** 1,691 active and 392 monitored English learners; ELL teacher FTEs grew from 21 (2014-15) to 58.5 (2025-26); English learners per ELL teacher 35.1 in 2025-26 (slides 7–8, transcribed from images: raw/money/images/boa-p7.png, boa-p8.png). Lunch prices ($2.75 elementary, $3.00 middle, $3.25 high) and meal debt of $5,351 in January 2026 (February 17 presentation, slide 30).
- **Elementary and middle schools (agents 1, 2):** projected 2026-27 class sizes by school and grade (May 5 presentation, slides 9–10). McCarthy's HVAC maintenance rose when its one-year warranty expired, and an extra custodian was requested (February 17 presentation, slide 20). The Elm Street building and bonds are covered here for P9.1.
- **High schools (agent 3):** the high school schedule redesign (four-block to five-block, slides 12–13) and teachers' comments on it (raw/money/news/tel-2026-03-26-school.txt).
- **Library, district-practices fact 94 (Nashua budget process):** can add that the aldermen adopted $205,367,867 for FY2027 (district-budget-and-cost fact 3).
- **Hart's Location file, property-tax-relief facts 1–3:** these state rules (elderly exemption, low and moderate income relief) are what Nashua's P27.1 answer relies on. They should reach the library with no place.
- **City Tax Rate History page:** for 2025 it lists State Ed $1.01 and County $1.15, the reverse of DRA's figures in the site's data (district-tax-and-state-aid fact 5, note). The site's figures should stand.
- **Manchester money file:** it pulled the same BLS metro series (town/Manchester/raw/money/bls-oews-*.json). My values agree (teaching assistants' annual median $37,220).

## Not retrieved

- https://www.bls.gov/oes/current/oes_31700.htm: HTTP 403 (Access Denied) to an automated request. The same figures came from the BLS public data API.
- Elm Street Middle School redevelopment after April 2025 (developer chosen, purchase and sale or development agreement, aldermen's vote): nothing found. The web search budget ran out before a follow-up search. The city site search (https://www.nashuanh.gov/Search?searchPhrase=Elm%20Street%20Middle%20School) returns results only through JavaScript. The Board of Aldermen agenda portal (https://nashuanh.portal.civicclerk.com/) was not tried (JavaScript application). A search result titled "Redevelopment project for former Nashua school moving forward" (ground.news, an aggregator) was not opened.
- The Board of Education's 2024 vote under RSA 199:4, II releasing Elm Street to the city: not retrieved (Board minutes are Google Drive files by meeting date and weren't searched).
- The Board of Aldermen's late-2019 bond resolution for the middle school project (news reports $118 million): not retrieved. The ACFR's authorized-unissued figure ($118,187,000 at June 30, 2020) is used instead.
- City of Nashua FY2027 Adopted Budget, pages 9–10 (the budget resolutions, scanned images): not transcribed. The adopted figures come from the budget tables. The full 46 MB PDF wasn't kept; a 24-page excerpt and the text of those pages are in raw/money/city/.
- City budget books on ClearGov (https://city-nashua-nh-cleardoc.cleargov.com/26335/1069089/d): JavaScript only. The PDF versions in the city's Document Center were used.
- Teacher turnover by school for Nashua: no district or NH DOE report was found. NH DOE's iPlatform (https://my.doe.nh.gov/iPlatform) wasn't tried; an earlier town file records that it blocks automated access.
- Local programs that give Nashua teachers classroom supplies (an education foundation or business donations): not searched once the web search budget ran out.
- Nashua's MS-1 count of elderly exemptions granted: not retrieved.
- Nashua Telegraph, "Donchess criticized for exceeding three percent budget limit," June 11, 2026 (https://www.nashuatelegraph.com/news/2026/06/11/donchess-criticized-for-exceeding-three-percent-budget-limit/): seen in search results, not opened.
