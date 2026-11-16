# Madison School District: Money, Taxes, the Kennett Contracts and SAU 13 Governance

Part of the Madison research (town/Madison). Gathered November 13, 2026.

## Summary

**What's covered:** 8 topics, 107 facts and 6 number tables on the Madison School District's money, taxes, contracts and governance, and on how SAU 13's three boards work together.
- The 2026-27 operating budget, the default budget that took effect after voters rejected the budget in March 2025 and again in March 2026, and the draft 2027 warrant (which includes a draft article to study closing Madison Elementary).
- Where the budget goes: Kennett tuition, special education, the elementary school itself, transportation and the SAU share; cost per pupil against Jackson and Bartlett, with DOE-25 spending per pupil by function (**derived**).
- Budget and tax growth against Social Security COLAs and enrollment back to 1990 (**derived** comparisons).
- The two 2003 Kennett contracts (grades 7–8 and 9–12) page by page: 20-year minimum term, 35/65 formula, notice and renewal; Madison's 2024 notice not to renew; the 2024–2026 search for other options.
- The 2025 revaluation, waterfront base values (Silver Lake $800,000), how the school tax follows assessed value, and why Madison gets no fiscal capacity disparity aid. NH DOE's adequacy aid calculation for Madison, FY2020–FY2027 (including the statewide education tax raised there and a $0 grant for FY2027), is in the site's data (adequacy_aid), so this file does not repeat it.
- The Eidelweiss village district rate, and the elderly exemption amounts and limits. DRA's tax rates and NH DOE's school taxes for Madison and its neighbors are in the site's data (property_tax), so this file does not repeat or compare them.
- SAU 13: its 1991 start, the joint board's seats, votes and meetings, Madison's share of the SAU budget since 2020-21, superintendent pay, the 2026 SAU budget vote and the HB 1300 tax cap vote.
- The capital improvement plan, capital reserves and the 2018 bond; teacher and paraprofessional pay, benefits and turnover.

**Main sources:** Madison's 2026 warrant, sample ballot, MS-26, MS-DSB and HB 1265 report (SAU 13 Financial Reports page); the Madison annual report for the year ending June 30, 2025 (published January 2026); Madison board minutes and packets (2023–November 2026) and SAU 13 joint board minutes and packets (2025–2026); the Town of Madison's ballot results, tax rate history, 2025 revaluation report and 2024 town report (MS-1); Madison and Conway board policies; RSA 40:4, 40:7, 72:39-a, 72:39-b, 194-C:7 and 194-C:8; NH Ed 500 rules; the NHMA moderators' guide; NCES school data (Urban Institute Education Data API); SSA's COLA series (Wayback copy); the library's DRA and DOE town CSVs; and read-only queries of the site database.

**Premises checked:**
- "$9.02/thousand tax rate": $9.02 is DRA's full value (equalized) rate for 2025. The rate on tax bills is $8.98 per $1,000 of assessed value, of which $5.87 is school tax (**derived**: $4.89 local + $0.98 state). Properties in the Village District of Eidelweiss pay $3.27 more ($12.25).
- "~$250k+ share of the SAU #13 budget": out of date. Madison's share was $249,285 in 2021-22, but $442,499 in 2025-26 and $527,065 in 2026-27 (36.16%).
- "Recent law allowing voters to veto SAU administrator pay increases": the closest law is HB 564 (2026 chapter 153), effective August 18, 2026. It puts the SAU budget to voters as a separate article, with all districts' votes added together; if it fails, last year's budget without pay increases takes effect. Madison already voted this way in 2025 and 2026. In March 2026 Madison voted no (258–342), but the SAU budget passed SAU-wide by 20 votes. HB 1300's 6% SAU cap (Question 2) is a separate law.
- "10-year tuition contract with Conway": wrong. Both 2003 contracts have a 20-year minimum term. Madison's board voted on February 5, 2024 to tell Conway it would not renew them. As of November 2026 no new Madison–Conway contract had been found.
- "Elementary enrollment is half what it was a generation ago": about right. NCES counted 235 students in fall 1995. On October 1, 2025 there were 102, or 43% (**derived**).
- "Budget keeps rising faster than COLAs": not borne out for the budget as voted. The operating budget article was $7,051,637 (default) for 2020-21 and $7,114,497 (default, including $400,000 of grants) for 2026-27. The local school tax rose 9.8% from 2018 to 2025, while Social Security COLAs compounded to 28.8% (all **derived**). Cost per pupil did rise faster than inflation: by 20.6% from FY2016 to FY2025 in the district's own inflation-adjusted figures.
- "Joint board meetings": the SAU 13 Joint Board (all 15 members of the three boards) meets about six times a year. Separate SAU 9/SAU 13 joint meetings were cut from four a year to two in 2025.
- Cost per pupil of $35,063 (FY2025) is confirmed by the 2026 warrant. The Advisory Budget Committee's report printed $39,160.

**Main gaps:**
- No published figure for the share of Madison's assessed value or tax on waterfront parcels.
- The MEA collective bargaining agreement and its salary schedule are not posted, so neither the site's salary bands nor para hourly rates could be checked against it.
- The 2025 MS-1 (post-revaluation elderly exemption amounts) and the 2026 tax rate were not available.
- No minutes yet for Madison's November 2, 2026 meeting, where Conway's offer and a Governor Wentworth contract were reported to be discussed.
- No source says whether Madison's Advisory Budget Committee counts as an RSA 32:14 budget committee for the August 2026 default-budget change.

**Proposed shared topic:** `educator-licensing-pathways` (rule, rules, no place): "New Hampshire paraeducator certification and the routes from paraeducator to a teaching license." It holds 2 facts here. Elderly exemption facts sit under `district-tax-and-state-aid` with place `town Madison`; a town-level `town-property-tax-relief` topic may fit better.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P3.3 Madison's per-pupil spending vs Jackson and Bartlett, and where the dollars go | district-budget-and-cost facts 1–5; table madison_doe25_per_pupil_2025; site data: cost per pupil, DOE-25 lines; library: measure-cost-per-pupil | full | FY2025: Madison $35,063, Bartlett $31,530, Jackson $50,323 (all K–6 or K–8 operating cost only). Per-pupil spending by function is **derived** |
| P9.2 How Madison parents can be heard on Kennett curriculum | district-board-and-public-input facts 1–7 | full | Contract joint-board and report clauses; Conway policy BEDH welcomes sending-town families; SAU 9/13 joint meetings now twice a year |
| P11.1 Budget growth vs enrollment and COLAs | district-budget-and-cost facts 6–15; tables madison_operating_budget_votes, madison_enrollment_history | full | All comparisons **derived**; COLA from SSA (Wayback copy) |
| P11.2 Tuition and special education vs running Madison Elementary | district-budget-and-cost facts 16–20; table madison_tuition_lines | full | FY2027 proposed: tuition 34.2%, special education 11.7%, other elementary costs 42.2% (**derived**) |
| P11.3 Elderly exemption amounts and limits | district-tax-and-state-aid facts 9–11 | full | 2024 MS-1 figures; the 2025 revaluation came after them |
| P12.1 Why waterfront property carries a large share of school taxes and SWEPT | district-tax-and-state-aid facts 4–8; site data: adequacy_aid (Madison district: SWEPT, the SWEPT rate and equalized value by year), property_tax (Madison district: rates and valuations by year); library: money-statewide-education-property-tax, money-equalized-valuation | partial | Base waterfront values and the SWEPT rule are given; the waterfront share of total value is not published |
| P12.2 Tax rate and school portion vs Freedom, Tamworth, Ossipee | site data: property_tax (Madison, Freedom and Tamworth districts; Ossipee in the Governor Wentworth Regional district); district-tax-and-state-aid facts 1–3 | full | The rates, school shares and full value rates for 2014–2025 are in the site's data; the Eidelweiss village district rate is fact 2; 2026 rates not set as of October 30, 2026 |
| P12.3 Can non-resident owners speak at the deliberative session? | district-board-and-public-input facts 8–12; library: budget-deliberative-session | full | Moderator and voters decide (RSA 40:4, 40:7; NHMA). Madison has no written rule on non-voters |
| P13.1 SAU 13 vs alignment with SAU 9 | district-consolidation-history facts 1–7; district-sau-governance facts 1–4; library: gov-sau-forming-and-withdrawing | partial | Facts, no verdict. No Madison study or vote on leaving SAU 13 was found |
| P13.2 Teacher salary schedule vs SAU 9 and southern Carroll County; retention | district-budget-and-cost facts 21–25; site data: average salary, salary bands | partial | Madison's 2025-26 average ($57,164.83) is the lowest of 9 nearby districts (**derived**). The CBA schedule is not posted |
| P14.1 Default budget amount and operating budget | district-budget-and-cost facts 26–31; table madison_operating_budget_votes; library: budget-default-budget | full | $7,114,497 took effect for 2026-27 after a 286–316 vote |
| P14.2 SAU pay "veto" law and Madison's SAU share | district-sau-governance facts 5–12; table madison_sau13_share; library: budget-sau-budget-vote, budget-hb-1300-school-tax-cap | full | See premises |
| P14.3 Capital maintenance plan | district-facilities-and-capital facts 1–9; table madison_capital_reserves | full | Septic is not a CIP line; pumping is an operating cost |
| P16.1 Para tuition reimbursement and certification pathways | district-budget-and-cost facts 32–34; educator-licensing-pathways facts 1–2 | partial | The CBA text is not posted; only the board's summary table |
| P16.2 Para wages and benefits vs retail, hospitality and SAU 9 | district-budget-and-cost facts 35–37; Conway file: conway_para_and_regional_wages | partial | Madison pays paras a yearly salary ($34,741); daily hours are not published, so no hourly comparison |
| P19.3 The Conway contract: term, formula, notice, renewal | district-tuition-contracts facts 1–12; Conway file district-tuition-contracts facts 5–9 | full | Corrects the "10-year" premise |
| P20.2 SAU 13 history and how the three boards work together | district-sau-governance facts 1–4 and 13–17 | full | Whether meetings are "productive" is not something the record measures; attendance and recording facts given |

## district-budget-and-cost: Madison's Budget, Cost per Pupil, Default Budgets and Staff Pay

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. NH DOE's cost per pupil for the Madison School District was $35,063 for 2024-25, the figure printed on the March 2026 ballot, against $31,530 for Bartlett and $50,323 for Jackson; all three figures cover only the elementary school each district runs, not Kennett tuition or transportation.
   - citation: Madison School District 2026 Warrant, Article 1; site data (district_cost_per_pupil, 2025)
   - source: https://drive.google.com/file/d/1tZA3upmwnQvVkXsUM4jWpWg4pDp9aGbM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Warrant text: "The average cost-per-pupil for the preceding year as calculated in accordance with RSA 189:75, I(a) is $35,063." Site rows (elementary = total): Madison 35063, Bartlett 31530, Jackson 50323, Freedom 41267, Tamworth 37750. DOE subtracts tuition and transportation (library measure-cost-per-pupil, fact 2) and says only districts serving the same grades should be compared (fact 7); Bartlett runs K–8, Madison and Jackson K–6. Raw: raw/money/district/madison-warrant-2026.ocr.txt; raw/money/state-data/db-q2-cpp.txt
2. In 2024-25 Madison spent less per pupil than Bartlett or Jackson on regular instruction ($10,076 vs $11,079 and $18,539) and special programs ($5,101 vs $7,163 and $10,065), but more than Bartlett on general administration, which includes the SAU share ($4,007 vs $2,370), and on building operation and maintenance ($5,576 vs $3,649) (**derived** from DOE-25 elementary spending divided by ADM).
   - citation: site data (DOE-25 FY2025 elementary expenditure lines; doe_form_adm 2025)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Derived: each line ÷ ADM (Madison 125.70, Bartlett 159.12, Jackson 36.45). Madison rows: "1100 Regular Programs 1266510.82"; "2300 General Administration 503718.17"; "2600 Operation/Maintenance of Plant 700842.27". Madison's SAU share was $467,389 in 2024-25 (district-sau-governance fact 6). Madison's FY2025 plant line includes one-time work, e.g. "Building Refurbishment ... $168,885" for playground phase 1 (raw/money/packets/msb-pk-2026-11-02.txt, p. 17). DOE-25 per-ADM figures are not DOE's cost per pupil. See table madison_doe25_per_pupil_2025. Raw: raw/money/state-data/db-doe25-2025.txt, db-adm.txt
3. Madison's annual report explains its cost per pupil by saying "Madison is a small district, so fixed costs are spread over fewer students," rural transportation costs more per student, and "Administrative and building costs exist regardless of enrollment size"; the same page lists transportation and school debt among included costs, which NH DOE's own definition subtracts or reports separately.
   - citation: Madison School District Annual Report (year ending June 30, 2025), "Understanding Madison's Cost Per Pupil," pp. 44–45
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Why Madison's Cost Per Pupil May Appear High ● Madison is a small district, so fixed costs are spread over fewer students. ● Rural transportation costs are higher on a per-student basis." The report's list ("Transportation ○ Daily transportation"; "School-related debt") differs from library measure-cost-per-pupil facts 2–3. Stated neutrally; DOE's definition governs the published figure. Raw: raw/money/district/madison-ar-2026.txt
4. Madison's Advisory Budget Committee printed a different figure, "Average Cost-per-Pupil (from the 2025 NH DOE-25): $39,160," in its 2026 report, and asked "Are we, as a town, making optimal use of our school and its resources ... especially in light of the cost ... and substandard test scores?"
   - citation: Advisory Budget Committee Report, Madison School District 2026, Madison Annual Report pp. 41–43
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: The committee's views, cited as recorded. The source of $39,160 is not explained; the warrant's $35,063 matches the site's DOE figure. Raw: raw/money/district/madison-ar-2026.txt (p. 42)
5. Madison's cost-per-pupil figures can be set beside its test results, but no Madison document links the two, and the district's own annual report says cost per pupil "is a financial reporting tool, not a measure of academic outcomes."
   - citation: Madison Annual Report, "Q&A: Madison School District Cost Per Pupil," p. 45; library topics measure-cost-per-pupil and comparing-small-schools
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Q: Is cost per pupil a measure of efficiency or school quality? A: No. It is a financial reporting tool, not a measure of academic outcomes, staff effectiveness, or student success." Raw: raw/money/district/madison-ar-2026.txt
6. In the district's own inflation-adjusted figures (November 2025 dollars), Madison's cost per pupil rose from $29,075 in 2015-16 to $35,063 in 2024-25, about 20.6% above inflation (**derived**); before adjustment the site's figures rose from $21,869 to $35,063.
   - citation: Madison School District, "Mandatory Report to Voters on School Expenses" (HB 1265 report), 2026; site data (district_cost_per_pupil)
   - source: https://drive.google.com/file/d/1GptYv8gSdQXkoP6lXWN59ZqXd-dr3uiM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Graph read from the rendered page (raw/money/district/madison-graph-p1.png): 2016 $29,075; 2017 $30,102; 2018 $31,648; 2019 $29,932; 2020 $27,237; 2021 $29,221; 2022 $30,472; 2023 $33,581; 2024 $34,686; 2025 $35,063. The report says values were adjusted "using the Boston-Cambridge-Newton, MA-NH CPI-U." Derived: 35,063 ÷ 29,075 = 1.206. Raw: raw/money/district/hb1265-report.txt, madison-graph.*
7. Madison Elementary's enrollment on October 1 fell from 131 (2016) and 139 (2019) to 102 (2025), and the principal projected 90 students in grades K–6 for 2026-27; Madison residents in grades 7–12 fell from 157 to 100 over the same years.
   - citation: Madison Annual Report, "Report of Official Enrollment as of October 1st," p. 75; Principal's Report, "Projected Enrollment 2026-27," p. 22
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The Madison Elementary School's official enrollment for Grades K through 6, as of October 1st 2025 was 102"; table rows "2016 ... 131", "2019 ... 139"; 7–12: "2025 ... 100", "2016 ... 157"; projection "Total 90 * Estimate based on birth records". See table madison_enrollment_history. Raw: raw/money/district/madison-ar-2026.txt (pp. 22, 78)
8. NCES counted 235 students at Madison Elementary (grades K–6) in fall 1995 and 233 in fall 1993, so the October 2025 count of 102 is about 43% of the mid-1990s level (**derived**).
   - citation: NCES Common Core of Data, school directory, Madison Elementary School (NCES ID 330456000238), via the Urban Institute Education Data Portal
   - source: https://educationdata.urban.org/api/v1/schools/ccd/directory/1995/?ncessch=330456000238
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: API "year" is the fall of the school year. Values: 1990 194; 1993 233; 1995 235; 1997 227; 1999 196; 2002 171; 2005 159; 2010 174; 2015 134; 2020 127; 2023 114 (lowest grade 0 = K, highest 6). Derived: 102 ÷ 235 = 43.4%. Raw: raw/money/nces/mes-dir-*.json
9. Madison's operating budget article (without the SAU share or special articles) was $7,051,637 for 2020-21 (a default budget) and $7,114,497 for 2026-27 (also a default, and the first to include $400,000 of grant spending), up 0.9% (**derived**); voters rejected the proposed budget for both 2025-26 and 2026-27.
   - citation: Madison Annual Report, "7-Year Budget Comparison (Proposed vs Approved)," p. 51; 2026 ballot results
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Table: "FY27 (Proposed) FY26 (Default) FY25 (Approved) FY24 (Approved) FY23 (Approved) FY22 (Default) FY21 (Default) ... $7,343,152.85 $7,314,006.30 $7,110,575.69 $7,440,477.12 $7,314,510.71 $7,185,692.57 $7,051,637.30". The FY26 figure is the $7,190,421 default plus the $123,585 teachers' contract article. Derived: 7,114,497 ÷ 7,051,637 = 1.0089; without the $400,000 of grants, −4.8%. See table madison_operating_budget_votes. Raw: raw/money/district/madison-ar-2026.txt (p. 54)
10. Social Security cost-of-living adjustments effective December 2020 through December 2025 were 1.3%, 5.9%, 8.7%, 3.2%, 2.5% and 2.8%, compounding to about 26.8% (**derived**), and the COLA effective December 2026 is 3.6%.
   - citation: Social Security Administration, Office of the Chief Actuary, "Social Security Cost-Of-Living Adjustments" (Wayback snapshot November 9, 2026)
   - source: https://web.archive.org/web/20261109154037/https://www.ssa.gov/oact/cola/colaseries.html
   - as_of: Wayback snapshot 2026-11-09
   - review_by: 2027-11-13
   - note: For context, not about one place. The live SSA page refused automated requests (403). Page text: "thereafter COLAs have been effective with benefits payable for December." Rows: 2018 2.8, 2019 1.6, 2020 1.3, 2021 5.9, 2022 8.7, 2023 3.2, 2024 2.5, 2025 2.8, 2026 3.6. Raw: raw/money/ssa/ssa-colaseries-wayback-20261109.html, .txt
11. The local school tax Madison raised grew from $5,277,700 in tax year 2018 to $5,795,734 in 2025, or 9.8%, while the seven Social Security COLAs effective December 2018 through December 2024 compounded to about 28.8% (**derived** comparison).
   - citation: NH DRA tax rate data (library raw/town/dra-tax-rates.csv, local_school_tax_effort); SSA COLA series
   - source: https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "Madison 2018 ... 5277700"; "Madison 2025 ... 5795734". A household's own bill also depends on its assessment, which changed with the 2025 revaluation (district-tax-and-state-aid fact 4). Kept for the COLA comparison; Madison's school tax dollars by year are in the site's data (property_tax, Madison district) and match these (checked November 15, 2026). The comparison is illustrative; COLAs measure benefit increases, not school costs. Raw: raw/money/state-data/dra-tax-rates-madison-neighbors.csv
12. Madison has spent well under its budgets in recent years: $551,565.67 of unspent money from 2024-25 was returned to taxpayers, the business administrator projected $886,221.33 more from 2025-26 "largely due to salaries and lower-than-expected out-of-district costs," and 2025-26 spending was $6,565,308 against a voted operating budget of $7,314,006.
   - citation: Madison School Board Minutes, May 4, 2026 (FY26 Projected Fund Balance); Madison 2027-2028 Working Budget v2, November 2, 2026 packet, p. 22
   - source: https://drive.google.com/file/d/1-hgBx39Uwc9eF93kr91uREOtF2dpTsr_/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Minutes: "the $551,565.67 from June 30,2025, was returned to taxpayers as a credit on the MS24 with DRA. The current return to offset taxes is $886,221.33, largely due to salaries and lower-than-expected out-of-district costs." Working budget: "Grand Total: $7,347,131 $6,790,980 $6,565,308 $6,854,634 $7,310,277" (FY24, FY25, FY26 expenditures; FY27 adopted; FY28 working). The board said in April 2026 the surplus came "in large part" from "two open teaching positions" and an avoided out-of-district placement. Raw: raw/money/minutes/msb-2026-05-04.*, msb-2026-04-06.*; raw/money/packets/msb-pk-2026-11-02.txt
13. For 2026-27 the district estimated the school tax to raise would rise $349,409.75 (about $0.29 per $1,000) even though appropriations rose only $68,712.75, mostly because the state adequacy grant fell from $316,877 to $0 and no year-end surplus was budgeted to offset taxes (−$549,629 the year before).
   - citation: Madison Annual Report, "Tax Impacts of Proposed Budget, Warrant Articles, and Revenue Changes 2026-2027," p. 38
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "ESTIMATED ADEQUACY $0.00 ($316,877.00) $316,877.00 $0.267"; "EST FUND BAL TO OFFSET TAXES** $0.00 ($549,629.00) $549,629.00 $0.464"; "TOTAL APPROPRIATIONS $8,070,217.75 $8,001,505.00 $68,712.75 $0.058"; "ESTIMATED TAX IMPACT $7,371,083.75 $7,021,674.00 $349,409.75 $0.29". Based on assessed value of $1,185,340,000. NH DOE's figures in the site's data (adequacy_aid, Madison district): a final FY2026 grant of $315,255.17, $1,621.83 less than the sheet's $316,877, and $0 for FY2027 (October 1, 2026 calculation), with the full calculation. Raw: raw/money/district/madison-ar-2026.txt (p. 41)
14. The Advisory Budget Committee named the main 2026-27 cost drivers as a net $60,190 rise in Kennett tuition (middle school down, high school up) and a 22.3% rise in health insurance premiums, and said the board cut one teaching position and two paraprofessional positions.
   - citation: Advisory Budget Committee Report, Madison Annual Report p. 41
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Kennett Middle School tuition costs were down, but High School tuition is up creating a net increase of $60,190 in tuition. Health insurance premiums were up by 22.3%"; "Paraprofessional positions were reduced by two positions". The MS-DSB also lists "Less 2 teaching positions" and "Less 2 para positions" (raw/money/district/madison-msdsb.ocr.txt). Raw: raw/money/district/madison-ar-2026.txt
15. Madison's policy for staff outside the union (GDB-R) sets yearly raises at "COLA or 3%, whichever is greater," while the MEA union contract gives professional staff 3% to 8% and hourly staff 4%, according to the board's October 2026 comparison table.
   - citation: Madison School Board packet, October 5, 2026, p. 71 ("GBD-R Non-CBA Staff Personnel" vs "MEA CBA")
   - source: https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page viewed (raw/money/images/pk1005-p71.png): "Salary Increases | COLA or 3%, whichever is greater | Range: Professional 3%-8%; Hourly 4%". At the November 17, 2025 SAU budget hearing the public commented on "Medicare and Social Security rates, and impacts in Carroll County for seniors" (raw/money/minutes/jt-2025-11-17.txt). Raw: raw/money/packets/msb-pk-2026-10-05.*
16. Of the $7,343,153 operating budget proposed for 2026-27, Kennett tuition was $2,512,798 (34.2%), special education $857,406 including its transportation (11.7%), other Madison Elementary costs $3,097,769 (42.2%), regular transportation $352,698 (4.8%), grants $400,000, the school bond $78,618 and the school board $43,864 (**derived** shares); the $527,065 SAU share was a separate article.
   - citation: Madison Annual Report, "7-Year Budget Comparison (Proposed vs Approved)," p. 51
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: FY27 column: "Transportation $352,697.95 / Conway Middle $833,542.00 / Conway High $1,679,256.00 / Conway Bond $0.00 / MES Bond $78,617.50 / School Board $43,864.45 / Total Elementary $4,355,174.95 / Sp. Ed. Transportation $40,000.00 / Special Education $817,406.08 / New Total Less SPED $3,497,768.87 / Grant Fund $400,000.00 / New Less Recreation/Grants $3,097,768.87". Check: the first seven lines sum to $7,343,152.85. Shares ÷ $7,343,152.85. Raw: raw/money/district/madison-ar-2026.txt (p. 54)
17. Madison's Kennett tuition lines were $768,672.66 (middle school) and $1,512,830.00 (high school) spent in 2023-24, $833,542 and $1,679,256 adopted for 2026-27, and $961,000 and $1,980,000 in the October 2026 working budget for 2027-28 (+15.3% and +17.9%).
   - citation: Madison 2026-2027 Proposed Budget (Annual Report p. 63); 2027-2028 Working Budget v2 (November 2, 2026 packet)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "01.1100.561.102 MIDDLE SCHOOL TUITION $768,673 $721,527 $1,020,387 $833,542 $961,000 $127,458 15.29"; "01.1100.561.103 HIGH SCHOOL TUITION $1,512,830 $1,612,996 $1,432,221 $1,679,256 $1,980,000 $300,744 17.91". The 2027-28 figures are a working draft while Conway negotiations are open. In October 2026 the business administrator said regular education "expenses are up 11.92% due to Middle & High School costs" (raw/money/minutes/msb-2026-10-05.txt). See table madison_tuition_lines. Raw: raw/money/packets/msb-pk-2026-11-02.txt (p. 33)
18. Madison stopped paying a share of Conway's Kennett building debt after 2023-24 (the "Debt Obligation - Tuition" line was $102,990 that year and $0 since).
   - citation: Madison 2026-2027 Proposed Budget, Annual Report p. 63
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Row: "01.1100.560.102 DEBT OBLIGATION- TUITION $102,990.00 $0.00 $0.00 $0.00". The 7-year table shows "Conway Bond" from $141,986 (FY21) to $0 (FY25). Raw: raw/money/district/madison-ar-2026.txt
19. Madison's special education spending was $1,672,826.90 in 2023-24 and $1,070,396.27 in 2024-25, against state special education aid of $593,541.26 and $458,448.27; out-of-district tuition alone fell from $1,017,967.81 to $207,029.22 and is budgeted at $150,000 for 2026-27.
   - citation: Madison Annual Report, "Statement of Revenues and Expenditures for Special Education Pupil Services" (RSA 32:11-a), p. 46; Proposed Budget p. 64
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "TOTAL EXPENDITURES: $1,672,826.90 $1,070,396.27"; "From State - Special Ed. Aid (formerly Catastrophic Aid) $593,541.26 $458,448.27"; "Out of District Tuition $1,017,967.81 $207,029.22 $390,000.00 $150,000.00". NH DOE's FY2024 special education aid file shows $592,971.29 paid to Madison, $569.97 less than the district's report (its DOE-25 also shows $593,541.26); FY2025 matches. Each year's costs, entitlement and proration are in the site's data (special_education_aid, Madison district). At the end of 2024-25 the district served 5 Kennett Middle and 11 Kennett High students with special services, and no out-of-district placements (p. 17). Raw: raw/money/district/madison-ar-2026.txt
20. Under both Kennett contracts Madison pays Conway, on top of tuition, for special education programs or facilities outside Conway's regular program, for in-district services beyond it (such as aides and counseling), and for any due process costs, attorney fees, awards and compensatory education.
   - citation: Conway Tuition Agreements, Grades 7-8 and 9-12 (Madison, 2003), Section I
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page viewed (raw/money/images/ar26r-p83.png, -p88.png): "Madison School District shall bear all the cost of any such special program or facility ... the Madison School District shall bear the cost of such extra services or facilities ... The Madison School District shall bear the cost of any due process proceedings, attorney fees, awards, out-of-district placements, and compensatory education awards." Contracts printed in the annual report, pp. 80–88. Raw: raw/money/district/madison-ar-2026.pdf
21. NH DOE's 2025-26 average teacher salary for Madison, $57,164.83, is the lowest of nine nearby districts in the site data, below Wakefield ($58,619.19), Conway ($60,390), Bartlett ($61,429), Freedom ($64,764), Jackson ($68,342), Tamworth ($73,624), Moultonborough ($76,043) and Governor Wentworth Regional ($80,090) (**derived** ranking).
   - citation: site data (district_teacher_average_salary, 2026)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: The nine districts were chosen by us (SAU 9, SAU 13 and southern Carroll County). Madison's average was $61,864 in 2024-25, the same value its HB 1265 report shows for 2025. Averages depend on staff experience as well as pay scales. Raw: raw/money/state-data/db-salary.txt
22. The site's 2025-26 salary bands for Madison run from $44,255.44 (bachelor's, first step) to $82,345.56 (master's plus 30, top step) over 14 steps, against bachelor's starting pay of $47,543 at Governor Wentworth, $47,869 in Freedom, $44,350 in Tamworth, $43,800 in Bartlett and $42,174 in Wakefield; Madison's bands show no obvious internal error, but its union schedule is not posted to check them against.
   - citation: site data (district_teacher_salary_band, 2026)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Madison rows: BA 44255.44–70871.92; BA15 45894.53–72511.01; BA30 47533.62–74150.10; MA 49172.72–75789.20; MA15 52450.90–79067.38; MA30 55729.08–82345.56; each band spans $26,616.48. Errors seen elsewhere (recommendation A8): Tamworth 2026 MA max "8579.00"; Jackson 2026 BA min "4600.00"; Conway's BA band is the non-degree column (Conway file). Madison's 2026-27 staff list includes three master's-degree salaries of $79,947.14 (annual report p. 89), above the 2025-26 MA top step, which is consistent with a raise but cannot be checked. Raw: raw/money/state-data/db-salary.txt; raw/money/district/madison-ar-2026.txt
23. The district's HB 1265 report shows Madison's average teacher salary in November 2025 dollars falling from $68,242 (2015-16) to $52,311 (2020-21) and rising to $61,864 (2024-25).
   - citation: Madison School District, "Mandatory Report to Voters on School Expenses," 2026
   - source: https://drive.google.com/file/d/1GptYv8gSdQXkoP6lXWN59ZqXd-dr3uiM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Read from the rendered graph: 2016 $68,242; 2017 $66,612; 2018 $56,685; 2019 $55,250; 2020 $56,947; 2021 $52,311; 2022 $61,090; 2023 $61,171; 2024 $61,383; 2025 $61,864. Raw: raw/money/district/madison-graph-p1.png
24. Of 17 certified staff on Madison Elementary's 2026-27 salary list (teachers, specialists, nurse and counselor), 9 had 3 or fewer years at the school (**derived** count), and the preschool teacher position was vacant; in April 2026 the board said 2025-26 savings came partly from "two open teaching positions."
   - citation: Madison Annual Report, "Staff Salaries Fiscal Year 2026-2027," p. 89; Madison School Board Minutes, April 6, 2026
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Count from the "Years at MES" column, counting rows with 3 or fewer years (9 of 17; the principal and the vacant preschool teacher are left out). No state turnover rate is published for Madison; this is a snapshot, not a rate. Names are omitted on purpose. Minutes text: "due in large part to the two open teaching positions". Raw: raw/money/district/madison-ar-2026.txt (p. 92 of the PDF); raw/money/minutes/msb-2026-04-06.*
25. At the February 2025 deliberative session, staff and residents spoke about pay and retention: a nurse said she took "a pay cut of over $30,000" to work at the school, cited 685 open school positions in New Hampshire, and said "We should not compare ourselves to SAU9," while a budget committee member said three-year contract costs of $640,789 should be renegotiated.
   - citation: Madison School District Deliberative Session Minutes, February 3, 2025, Article 4 (Annual Report pp. 9–10)
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Statements as recorded, not findings. Text: "I took a pay cut of over $30,000 ... Staff turnover is happening everywhere. She cited an example of EDJOBS NH ... 685 school positions open in NH"; "this is a cost of $640,789". Voters approved the contract 316–267 (2025 results, p. 14). Scanned; transcribed from image (OCR). Raw: raw/money/district/madison-ar-2026.ocr.txt (pp. 12–13)
26. Madison voters rejected the 2026-27 operating budget on March 10, 2026 (Article 2, amended at the deliberative session to $7,370,153), 286 yes to 316 no, so the default budget of $7,114,497 (including $400,000 of grant spending with offsetting revenue) took effect.
   - citation: Madison School District Official Ballot Results, March 10, 2026, Article 2
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_SCHOOL-BALLOT_RESULTS_03_10_2026-2.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Ballot text: "ARTICLE 2. (As amended) ... totaling $7,370,153 ... Should this article be defeated, the default budget shall be $7,114,497"; tally "286 YES / 316 NO". After the amendment the Advisory Budget Committee recommended it 4-1-0 (it had opposed the $7,343,153 version 5-0-0). See table madison_operating_budget_votes. Raw: raw/money/district/school-results-2026.*
27. The 2026-27 default budget was $199,509 below the prior year's $7,314,006, mainly because special programs fell $362,792 (two para positions and lower special education costs) and transportation fell $230,042 ("Reduction due to new service provider"), while grant spending of $400,000 was added.
   - citation: NH DRA Form MS-DSB, Madison Local School, 2026 (posted January 17, 2026)
   - source: https://drive.google.com/file/d/1db7JMGLqbYiAL1KEU33f4T3V5aTQejyJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "1200-1299 Special Programs $1,178,676 ($362,792) $O $815,884"; "2700-2799 Student Transportation $627,493 ($230,042) $O $397.451"; "Total Operating Budget Appropriations $7,314,006 ($199,509) $0 $7,114,497". Reasons page: "1100-1199 Plus CBA governed increases, Less 2 teaching positions, Plus increase in Conway tuition". The form was certified by school board members. Scanned; transcribed from image (OCR). Raw: raw/money/district/madison-msdsb.*
28. The year before, voters rejected the 2025-26 operating budget of $7,284,200 on March 11, 2025 (215 yes, 313 no), so the $7,190,421 default took effect; they approved the teachers' contract cost of $123,585 separately.
   - citation: Madison School District Official Ballot Results, March 11, 2025 (Annual Report pp. 13–14)
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "totaling $7,284,200? Should this article be defeated, the default budget shall be $7,190,421 ... 215 YES ... NO 313"; Article 4 "316 YES ... 267". At the session a motion to cut $260,000 failed by secret ballot, 35–32. Transcribed from image (OCR). Raw: raw/money/district/madison-ar-2026.ocr.txt (pp. 11–17)
29. In a default year the difference in the 2026-27 tax was small: the district estimated the proposed budget would have cost $0.052 more per $1,000 than the default, or $26.15 a year on a $500,000 home.
   - citation: Madison Annual Report, "Comparison of Tax Impacts - Proposed Budget vs Default Budget 2026-2027," p. 39
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "ESTIMATED TAX IMPACT PROPOSED OVER DEFAULT $7,371,084 $7,309,098 $61,986 $0.052"; "$500,000.00 $26.15". Raw: raw/money/district/madison-ar-2026.txt
30. The draft 2027 warrant (November 2, 2026 board packet) sets the deliberative session for Monday, February 1, 2027 at 7:00 p.m. and the ballot vote for Tuesday, March 9, 2027, with the operating budget and default budget amounts not yet filled in.
   - citation: Madison School District, "School Warrant Articles 2027" (draft), November 2, 2026 board packet, pp. 52–54
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The first session ... shall be held on Monday, February 1, 2027 at 7:00 PM"; "Tuesday, the 9th day of March 2027"; "totaling $X,XXX,XXX". Draft only. Raw: raw/money/packets/msb-pk-2026-11-02.txt
31. Madison voters kept the official ballot (SB2) system in March 2025: an article to rescind SB2, which Madison adopted on March 9, 2002, got 252 yes to 321 no, short of the three-fifths needed.
   - citation: Madison 2025 ballot results, Article 9 (Annual Report p. 14)
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Shall we rescind the provisions of RSA 40:13 (known as SB 2), as adopted by the Madison School District on March 9, 2002 ... (3/5-majority ballot vote required) ... 252 YES ... NO 321". At the session the moderator said meetings averaged 178 attendees before SB2 and 68 since. Transcribed from image (OCR). Raw: raw/money/district/madison-ar-2026.ocr.txt
32. Madison budgets a "Teacher Tuition Reimbursement" line of $6,000 for 2025-26 and 2026-27 (actual spending was $10,683.99 in 2023-24 and $8,513.12 in 2024-25); no posted Madison or SAU 13 policy describes a program for paraprofessionals to become certified teachers.
   - citation: Madison 2026-2027 Proposed Budget, account 01.2210.240.017 (Annual Report p. 65); Madison policies GCI and GDM
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Row: "Teacher Tuition Reimbursement $10,683.99 $8,513.12 $6,000.00". Policy GDM says classified employees "shall be encouraged to grow in job skills and to take additional training"; it names no reimbursement. The "not found" part is a statement about the policies listed on SAU 13's Madison policy page (raw/money/policies/madison-policy-listing-2026-11-13.tsv). Raw: raw/money/district/madison-ar-2026.txt; raw/money/policies/madison-policy-GDM.*
33. The board's October 2026 summary of the Madison Education Association contract lists professional development of "Teachers: 8 Credit Hours; Hourly: 4 Credit Hours" and 10 workshop days for school-year staff, and a 4-credit allowance for year-round staff.
   - citation: Madison School Board packet, October 5, 2026, p. 71
   - source: https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page viewed (raw/money/images/pk1005-p71.png): "Professional Dev. | $1,500 | 10 TW Days; Teachers: 8 Credit Hours; Hourly: 4 Credit Hours | 4 Credits". The table does not say what each credit hour is worth; the contract itself is not posted. Raw: raw/money/packets/msb-pk-2026-10-05.*
34. All of Madison Elementary's paraprofessionals hold New Hampshire's Paraeducator II certificate, according to the principal's 2026 report.
   - citation: Principal's Annual Report, Madison Annual Report p. 20
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "All paraprofessionals at MES are certified by the New Hampshire Department of Education with Para II credentials." In November 2026 the principal said paras would take part in a monthly book study led by the special education team (raw/money/packets/msb-pk-2026-11-02.txt). Raw: raw/money/district/madison-ar-2026.txt
35. Madison's 2026-27 salary list shows each of its six paraeducators at about $34,741 a year (plus $7,087 in statutory benefits), regardless of years of service or degree, and the MEA contract sets 189 work days, including holidays, for hourly paras.
   - citation: Madison Annual Report, "Staff Salaries Fiscal Year 2026-2027," p. 89; board packet October 5, 2026, p. 71
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "Paraeducator- ... 14 12 Bachelors $34,741.22 $0.00 $7,087.21 $41,828.43"; "... 3 29 Bachelors $34,741.00". Table: "Hourly Paras 189 work days (incl Holidays)". **Derived**: $34,741 ÷ 189 = $183.81 a day. Daily hours are not published, so an hourly rate cannot be computed. Raw: raw/money/district/madison-ar-2026.txt; raw/money/images/pk1005-p71.png
36. Madison's paraeducator pay of $34,741 a year is below the May 2025 mean annual wage BLS reports for teaching assistants in the Northern New Hampshire nonmetropolitan area ($39,780; median $37,350) (**derived** comparison).
   - citation: BLS OEWS May 2025, Northern NH nonmetropolitan area (Conway file, district-budget-and-cost fact 22)
   - source: https://www.bls.gov/oes/2025/may/nh_counties.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: BLS figures from town/Conway/raw/money/wages/bls-api-oews-northern-nh-nonmetro*.json (the area covers Carroll, Coos and Grafton counties). Retail and hospitality wages are hourly (Conway table conway_para_and_regional_wages: retail salespersons $18.05, waiters $18.82, hotel desk clerks $18.25); Conway's own paras earn $20.52–$27.46 an hour in 2026-27. Comparing them with Madison's yearly salary needs daily hours, which are not published. Raw: Conway file paths above
37. Under the MEA contract the district pays 88% of health insurance premiums, offers a health stipend of 20% of the maximum employer contribution, gives hourly staff 8 paid holidays, 13 sick days (accruing to 100), 3 personal days and a sick bank, and offers no disability insurance.
   - citation: Madison School Board packet, October 5, 2026, p. 71
   - source: https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page viewed: "Health Ins | 90% | 88%"; "Health Stipend | 20% of max employer contribution"; "Holidays | 11 | 8 (Hourly Employees)"; "Sick Leave | 15 | 13"; "Sick Bank | None | Available"; "Disability Ins | Policy Provided | None". The first column is non-union staff (policy GDB-R). In March 2026 the MEA chose the "Orange Plan" for 2026-27 (raw/money/minutes/msb-2026-03-05.txt). Raw: raw/money/images/pk1005-p71.png

## district-tax-and-state-aid: Madison's Tax Rate, the 2025 Revaluation, Waterfront Values, SWEPT and the Elderly Exemption

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. The $9.02 per $1,000 quoted for Madison's 2025 tax rate is NH DRA's full value (equalized) rate; the rate on Madison's tax bills, in the town's tax rate history, was $8.98 per $1,000 of assessed value: town $2.39, local school $4.89, state education $0.98 and county $0.72.
   - citation: Town of Madison, "Madison Tax Rate History"; NH DRA 2025 full value tax rate (site data: property_tax)
   - source: https://www.madison-nh.org/wp-content/uploads/2025/11/2025-TAX-RATE-HISTORY.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Town sheet: "2025 2.39 4.89 0.98 0.72 = 8.98 3.27 12.25". Kept to correct the "$9.02" premise in the residents' questions. The rates match DRA's in the site's data (property_tax, Madison district), which also has the full value rate ($9.02), the school share and the other years (checked November 15, 2026). Raw: raw/money/town/tax-rate-history-2025.*; raw/money/state-data/dra-tax-rates-madison-neighbors.csv
2. Properties inside the Village District of Eidelweiss pay an extra $3.27 per $1,000 for village district services, for a 2025 total of $12.25.
   - citation: Town of Madison, "Madison Tax Rate History" (2025); Town of Madison, Property Tax Information page
   - source: https://www.madison-nh.org/wp-content/uploads/2025/11/2025-TAX-RATE-HISTORY.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "District of Eidelweiss is subject to an additional tax that covers services voted by the legal voters of the District at their annual February meeting." Raw: raw/money/town/tax-rate-history-2025.ocr.txt, property-tax-information.txt
3. DRA had not set Madison's 2026 tax rate as of October 30, 2026; Madison does not appear on DRA's list of completed 2026 rates.
   - citation: NH DRA, "Completed Public Tax Rates (As of October 30, 2026)"
   - source: https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2026-municipal-tax-rates.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Library copy additional-data/raw/town/dra/2026-municipal-tax-rates.pdf (2 pages, OCR searched for Madison, Freedom, Tamworth, Ossipee; none listed).
4. Madison's 2025 revaluation roughly doubled its tax base: assessed value with utilities rose from $611,867,353 (2024) to $1,185,340,000 (2025), the equalization ratio went from 51.8% to 100.7%, and the local school rate fell from $8.73 to $4.89.
   - citation: NH DRA tax rates 2024–2025; Town of Madison, Assessing page and Tax Rate History
   - source: https://www.madison-nh.org/departments/assessing/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: DRA rows: "Madison 2024 3.79 1.28 8.73 1.97 15.77 67.9 51.8 8.14 611867353"; "Madison 2025 ... 100.7 9.02 1185340000". Assessing page: "2024 Equalization Ratio = 51.0%" and "See also the 2025 Cyclical Revaluation Report." A ratio near 50% meant assessments were about half of market value. Kept for the reason, the revaluation, which the site's data doesn't give. Madison's DRA rates, ratios and valuations for 2014–2025 are in the site's data (property_tax, Madison district), and these figures match it (checked November 15, 2026); DRA's 2024 ratio there is 51.8%, not the assessing page's 51.0%. Each owner's change depended on how their own property's value changed. Raw: raw/money/state-data/dra-tax-rates-madison-neighbors.csv; raw/money/town/assessing.txt
5. The 2025 revaluation counted 3,160 parcels, of which 1,551 have water frontage and 428 have views; residential land and buildings (1,711 parcels, median $449,300) were valued at $951,601,600 of $1,190,326,748 total taxable value.
   - citation: Avitar Associates, Town of Madison 2025 Cyclical Revaluation (USPAP report), "C. Town Parcel Breakdown," p. 76
   - source: https://www.madison-nh.org/wp-content/uploads/2025/11/Madison-2025-USPAP-Manual-Rev-1.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page viewed (raw/money/images/reval-p80.png): "RESIDENTIAL LAND & BUILDING (not including current use): 1711 $ 951,601,600 Median: $ 449,300"; "TOTAL TAXABLE: 2946 $ 1,190,326,748"; "TOTAL NUMBER OF PARCELS: 3160"; "PROPERTIES WITH VIEWS (included above): 428"; "PROPERTIES WITH WATER FRONTAGE (included above): 1551". The report does not total the value of waterfront parcels. The 92 MB PDF is not saved; text extraction and page images are. Raw: raw/money/town/reval-2025-uspap-extract.txt
6. The revaluation set a base waterfront value of $800,000 for an average Silver Lake site, where 242 parcels have access and 199 have direct private frontage, against $300,000 for the Pea Porridge Ponds (1,135 parcels with access, 161 with frontage), $200,000 for Moores and Whitton ponds and $80,000 for Davis Pond.
   - citation: Avitar Associates, Madison 2025 Revaluation, Section 10, "Waterfront Report," pp. 379–380 and base-rate pages
   - source: https://www.madison-nh.org/wp-content/uploads/2025/11/Madison-2025-USPAP-Manual-Rev-1.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Text (page viewed, raw/money/images/reval-p384.png): "Silver Lake Base - $800,000 There are 242 parcels with access to this water body. 199 of those parcels have direct private water front. Silver Lake has public access and parking with Town pass." "Pea Porridge Ponds Base - $300,000 There are 1,135 parcels with access ... 161 of those parcels have direct private water front." Davis Pond: "A BASE VALUE OF $80,000". Each site is then adjusted for frontage, access, location, topography and condition. Raw: raw/money/town/reval-2025-uspap-extract.txt
7. A property's share of Madison's school taxes follows its assessed value, because one rate per $1,000 applies to all taxable property in town (plus the Eidelweiss district rate where it applies); higher-valued property, including waterfront, therefore pays more in dollars, whether or not the owner votes in Madison.
   - citation: NH DRA 2025 tax rates (rates per $1,000 of assessed value); library topic money-local-school-tax
   - source: https://www.madison-nh.org/wp-content/uploads/2025/11/2025-TAX-RATE-HISTORY.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Tax sheet heading: "PER THOUSAND of ASSESSED VALUE". A plain explanation of how the rate works, not a judgment about fairness. Raw: raw/money/town/tax-rate-history-2025.ocr.txt
8. NH DOE's FY2027 file puts Madison's equalized property value per pupil at $5,996,116.53, far above the $1.6 million level below which fiscal capacity disparity aid is paid, so Madison gets none.
   - citation: NH DOE, FY 2027 Adequacy Aid (October 1, 2026), "EV Per ADM"
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: CSV: "ev_per_pupil 5996116.53"; "fiscal_capacity_disparity_aid 0". Library topic money-fiscal-capacity-disparity-aid has the rule. The $0 aid, equalized value and pupil count are in the site's data (adequacy_aid, Madison district), with the SWEPT, its rate and the grant for each year; value per pupil is not. Raw: raw/money/state-data/adequacy-aid-madison.csv
9. Madison's elderly exemption, as reported on the town's 2024 MS-1, takes $12,000 off the assessed value for owners aged 65–74, $25,000 for ages 75–79 and $50,000 for 80 and older, with an income limit of $35,000 (single or married) and an asset limit of $125,000 (single or married).
   - citation: NH DRA Form MS-1 (2024), Elderly Exemption Report, Town of Madison 2024 Annual Report p. 103
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page viewed (raw/money/images/tr24-p103.png): "65-74 0 $12,000"; "75-79 1 $25,000 $25,000"; "80+ 9 $50,000 $450,000"; "Income Limits Single $35,000 Married $35,000"; "Asset Limits Single $125,000 Married $125,000". These amounts were set before the 2025 revaluation roughly doubled assessments; no 2025 or 2026 warrant article changing them was found (2026 draft town warrant read). Applications are due April 15 (assessing page). Raw: raw/money/town/town-report-2024.*; raw/money/town/assessing.txt
10. In tax year 2024, 10 Madison residents received the elderly exemption (1 aged 75–79 and 9 aged 80 or older), removing $475,000 of assessed value.
   - citation: NH DRA Form MS-1 (2024), Town of Madison 2024 Annual Report pp. 101 and 103
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Text: "13 Elderly Exemption RSA 72:39-a,b $0 10 $475,000". Madison's 2024 tax rate ($15.77 per $1,000) is in the site's data (property_tax, Madison district). Raw: raw/money/town/town-report-2024.ocr.txt
11. Under RSA 72:39-a and 72:39-b, Madison's limits cannot go below the state floors: net income of $13,400 (single) or $20,400 (married), net assets of $35,000 excluding the home and up to 2 acres (or the minimum lot size), and an exemption of at least $5,000; applicants must have lived in New Hampshire for 3 years, and the town changes the amounts by a town meeting vote under RSA 72:27-a.
   - citation: RSA 72:39-a, I; RSA 72:39-b, I–II
   - source: https://gc.nh.gov/rsa/html/V/72/72-39-b.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: town Madison
   - note: Statute text: "Under no circumstances shall the amount determined by the city or town be less than $13,400 for a single person or $20,400 for married persons"; "The amount determined by the city or town shall not be less than $35,000"; "Under no circumstances shall the amounts of the exemption for any age category be less than $5,000"; "A town or city may adopt or modify elderly exemptions by the procedure in RSA 72:27-a." Net income counts Social Security and pensions. Raw: raw/money/law/rsa-72-39-a.*, rsa-72-39-b.*

## district-tuition-contracts: Madison's Kennett Contracts with Conway (2003) and the Search for Other Options

- kind: local
- question_type: governance_money
- description: A district's tuition contracts and agreements with other districts and schools: terms, cost formulas, caps, length, renewal, transportation and special education

1. Madison sends its grades 7–8 and 9–12 students to Conway under two contracts signed in spring 2003 (Madison's board on April 24, Conway's on April 14) and approved by the State Board of Education on May 21, 2003, as part of the plan to build a new Kennett High School and renovate the old one as a middle school.
   - citation: Conway Tuition Agreements, Grades 7-8 and 9-12 (Madison), signature pages; printed in the Madison Annual Report, pp. 80–88
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page viewed (raw/money/images/ar26r-p87.png): "School District of Madison ... 4/24/03"; "School District of Conway ... 4-14-03"; "Reviewed and approved on the 21st day of May, 2003, by the New Hampshire State Board of Education." Section IV of the 7–8 contract refers to "the renovation of Kennett as a middle school". Scanned pages rotated and read. Raw: raw/money/district/madison-ar-2026.pdf (PDF pp. 83–91)
2. Under each contract Madison must send at least 90% of its pupils in those grades to Conway, pays for their transportation, and Conway must educate them on the same terms as Conway's own students.
   - citation: Conway Tuition Agreements (Madison, 7-8 and 9-12), Section I
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Madison School District shall send at least ninety percent (90%) of its pupils, grades 9 through 12, with the exceptions hereinafter noted, to Conway for schooling; and Madison School District shall be responsible for the transportation methods and expenses". Raw: raw/money/images/ar26r-p87.png, ar26r-p83.png
3. Each contract runs a minimum of 20 school years from the school year the new high school opened, and either district could end it at the end of that term by written notice given before the end of the 17th year; otherwise it continues year to year, and ending it then takes notice at least three full fiscal years ahead. It is not a 10-year contract.
   - citation: Conway Tuition Agreements (Madison), Sections II–III
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page viewed (raw/money/images/ar26r-p83.png): "shall continue for a minimum term of twenty (20) school years.* This Agreement shall terminate at the end of such minimum term if either party gives to the other, at any time prior to the expiration of the seventeenth (17th) fiscal school year ending June 30 of such minimum term, written notice"; p. 84: "which shall be at least the third (3rd) full fiscal school year ending June 30 following the school year during which the notice is given." The contract expected occupancy "September 2006"; SAU 9's 2019 study described the 9–12 agreements as beginning July 1, 2007 (Jackson file district-tuition-contracts 6 in `Jackson/money-and-governance.md`), and SAU 9 said in 2023 they expire in 2027 (Bartlett file district-tuition-contracts fact 10).
4. Each district's share of Conway's school operating cost is 35% based on its share of the towns' equalized property value and 65% on its share of attendance (ADM-A); Conway sets the estimate from its approved budget plus the Northeast urban CPI plus 2.5%, adjusts to actual costs the next year, and must notify Madison by November 30, with no cap on increases.
   - citation: Conway Tuition Agreements (Madison), Section X.A.2–4
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page viewed (raw/money/images/ar26r-p85.png): "a combination of 35% of the town's equalized value as a percentage of the total equalized value and 65% of the town's average daily membership in attendance at the junior high school"; "plus an inflation factor equal to US Department of Labor Consumer Price Index - Size A - Northeast Urban (October of current year) plus 2.5% ... in no event later than November 30th". In April 2024 Madison's chair said "we always get that number at the end of our budget process" (raw/money/minutes/msb-april-1-2024.txt). Raw: as fact 1
5. Madison also paid a share of Conway's construction bonds by equalized value (the "Conway Bond" line, which ended after 2023-24) and pays a share of 3% of construction cost a year into a facilities maintenance fund; a district that leaves before the bonds are repaid must keep paying its share.
   - citation: Conway Tuition Agreements (Madison), Sections X.B–X.D
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text (ar26r-p85.png, -p86.png): "The method of apportioning capital expenses (bond issues) shall be the town's equalized value"; "each district (including Conway) shall pay its share of 3% of the actual construction cost divided by 20"; "Should the sending district terminate this agreement prior to the maturity date of said long-term debt ... the sending district agrees to pay its proportionate share of the remaining long-term debt payments." Raw: as fact 1
6. The contracts also provide joint meetings of the Conway board with all sending boards at least three times a year, quarterly written reports to the Madison board on Madison students' achievement and attendance, a remediation plan if the program falls below state or accreditation standards, a three-person dispute panel whose decision is final, and a right to ask the State Board to end or change the contract if state or federal funding changes substantially.
   - citation: Conway Tuition Agreements (Madison), Sections VI, VIII, IX, XII, XIII
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text (ar26r-p84.png): "JOINT BOARD MEETINGS: The Conway School Board will meet jointly with all School Boards (all together) who send pupils to the junior high school ... at least three (3) times a year"; "A written quarterly report will be made to the Madison School Board concerning achievement and attendance records"; p. 86: "the decision of panel shall be final." Raw: as fact 1
7. On February 5, 2024 the Madison School Board voted unanimously "to notify Conway that we do not want to renew the current contract with the middle school or high school"; at an April 2024 public forum the chair said the letter had been sent "but was misplaced" and that the option under consideration "would be school choice for parents."
   - citation: Madison School Board Minutes, February 5, 2024 (item B, Conway Letter) and April 1, 2024 (Public Forum)
   - source: https://drive.google.com/file/d/12H1VfrLy8eUR7BPvbRjt_17PhHRT98H5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Motion by Jeremy Cox to notify Conway that we do not want to renew the current contract with the middle school or high school, seconded by Sarah DeMartino. The motion passed unanimously." April: "Nicole Nordlund asked if we have opted out of the Conway contract. Jim Curran said a letter was sent to Conway but was misplaced"; "Jim Curran said the option would be school choice for parents ... we are not interested in the current contract the way it reads." April minutes URL: https://drive.google.com/file/d/16g8lpJH30JXCLjcndgH9HPr8LY0Yl1rB/view. Raw: raw/money/minutes/msb-february-5-2024.*, msb-april-1-2024.*
8. In October 2024 the board directed the superintendent "to reach out to Governor Wentworth School District and Moultonborough School District regarding school choice contracts and memorandum of understanding of agreement," and in December 2024 it approved a letter to Conway's superintendent and chair "regarding tuition numbers."
   - citation: Madison School Board Minutes, October 7, 2024 and December 2, 2024 (actions after non-public session)
   - source: https://drive.google.com/file/d/15fYJq3zdLxp-rzyo_uZj6e6_NofGftoy/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text quoted. December minutes: "The board approved to send a letter to Conway School District to Superintendent & Chair regarding tuition numbers." December URL: https://drive.google.com/file/d/1GqP-VE50xWsj3ewPNAjC7wLShoPBsSvg/view. Raw: raw/money/minutes/msb-october-7-2024.*, msb-december-2-2024.*
9. Madison and Tamworth each met with Conway's negotiating team in August 2025, and through October 2026 Madison's board discussed "high school tuition negotiations" only in non-public session; in May 2026 the chair said negotiations "are ongoing and remain in non-public session" and the superintendent said they "focus on high school."
   - citation: SAU 13 Joint Board Minutes, August 18, 2025 (Conway Negotiations); Madison School Board Minutes, May 4, 2026 and October 5, 2026
   - source: https://drive.google.com/file/d/1-hgBx39Uwc9eF93kr91uREOtF2dpTsr_/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Tamworth and Madison each have a one hour block scheduled with the Conway negotiation team on 08-19-2025"; "negotiations are ongoing and remain in non-public session ... while current negotiations focus on high school, he agrees the middle school element needs to be addressed"; October non-public: "High school tuition negotiations were discussed." Madison's board has a two-member "Tuition Options" committee (members page). Raw: raw/money/minutes/jt-2025-08-18.*, msb-2026-05-04.*; raw/money/packets/msb-pk-2026-11-02.txt
10. As of November 13, 2026 no new Madison–Conway contract had been posted or voted; Conway board members said in November 2026 that SAU 13 had presented a tuition contract with the Governor Wentworth Regional School District (Kingswood) and that Madison planned to present Conway's offer to its community.
   - citation: Conway file district-tuition-contracts fact 8 (Conway School Board special meeting minutes, draft, November 5, 2026); Madison draft 2027 warrant (November 2, 2026 packet)
   - source: https://drive.google.com/file/d/1nnBOX0aNn_Toc_nQQllAc-taAjVlwl6T/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Conway minutes text: "on Monday night, SAU #13 presented a tuition contract with Governor Wentworth ... Madison plans to present Conway's offer to their community." Madison's draft 2027 warrant has no tuition contract article yet; Madison's November 2, 2026 minutes were not posted. The SAU 9 tuition page lists 2027 contracts only for Albany, Bartlett, Eaton and Jackson. Raw: town/Conway/raw/money/minutes/csb-2026-11-05-special-draft.*; raw/money/packets/msb-pk-2026-11-02.txt
11. Conway's 2027–2032 contracts with other sending towns drop property value from the formula, base charges on Conway's DOE-25 costs and attendance, and cap the yearly inflation factor (CPI plus 2.5%) at 8%, which gives a reference for what a renewed Madison contract could look like.
   - citation: Conway file district-tuition-contracts fact 5; Bartlett file district-tuition-contracts fact 6
   - source: https://drive.google.com/file/d/1VJ2HlQZZYMXnHHPuZ455HJuzTVO5DOW5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Pointer to existing facts; no Madison terms are known. The Conway board chair said in November 2026 that "Conway is taking on more responsibility for tuition with the new formula" (Conway file fact 9).
12. In March 2026, 68 Madison students attended Kennett High School and 31 attended Kennett Middle School, out of 600 and 297.
   - citation: Conway Annual Report (FY2025), enrollment by home district, as of March 2026 (Conway file table conway_kennett_enrollment_by_town)
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Pointer to the Conway table row "Madison | 333 | 2026 | 68 | 31". Madison's own October 2025 count of residents in grades 7–12 was 100 (district-budget-and-cost fact 7).

## district-sau-governance: SAU 13, Its Joint Board, Its Budget and Madison's Share

- kind: local
- question_type: governance_money
- description: How a district shares an SAU: board seats and votes, how SAU costs are divided, and what the local board decides versus the SAU

1. SAU 13, made up of the Freedom, Madison and Tamworth school districts with its office at 881A Tamworth Road in Tamworth, was formed in 1991, according to its website.
   - citation: SAU 13 home page
   - source: https://www.sau13.org/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "School Administrative Unit #13 includes the School Board Districts of Madison, Tamworth and Freedom. It was initially formed in 1991 in an effort to promote excellence in our educational programs and our school districts." Raw: raw/money/sau13/sau13-home-2026-11-08.txt (copy of additional-data/raw/districts/batch-7/sau13-home.txt)
2. The SAU 13 Joint Board is all 15 members of the three five-member school boards; a quorum is more than half of the seats with at least one member from each district, and its policy BBBH-S gives it the duties of electing the superintendent, approving SAU staff, fixing SAU salaries and adopting the SAU budget.
   - citation: Freedom, Madison & Tamworth School Board Policy BBBH-S (adopted 2019); SAU 13 Joint Board members page
   - source: https://www.sau13.org/school-board/sau-joint-board/school-board-members
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Policy text: "SAU OR JOINT BOARD: The combined school boards of the school districts"; "A quorum ... shall consist of more than fifty percent (50%) of total board members (seats)with at least one board member from each constituent District"; "Elect, when necessary, a Superintendent ... Fix the salaries of all SAU personnel ... Adopt a budget". Members page lists five members each for Freedom, Madison and Tamworth. The policy was on the November 2, 2026 Madison agenda for a first reading of a revision. Raw: raw/money/packets/msb-pk-2026-11-02.txt (pp. 94–97); raw/money/sau13/school-board_sau-joint-board_school-board-members.txt
3. Each district has 3 votes on the Joint Board, split equally among its members present (0.6 each when all five attend), and a weighted vote of one vote per 16 resident pupils enrolled in SAU schools can be demanded by a majority of any one district's members present.
   - citation: RSA 194-C:7 and 194-C:8; SAU 13 Policy BBBH-S, sections D–E
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-8.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: sau 13
   - note: Policy table: "5 Member Board ... 5 0.600 / 4 0.750 / 3 1.000 / 2 1.500 / 1 3.000"; "Weighted voting may only be invoked by a majority of the board members of a constituent member who are in attendance". Statute: "each district shall be entitled to one vote for each 16 pupils residing in that district and enrolled in schools under the administrative unit." No SAU 13 record of a weighted vote was found in the 2025–2026 minutes read. Raw: raw/money/law/rsa-194-C-7.*, rsa-194-C-8.*
4. SAU 13's budget is split half by each district's equalized property value and half by attendance (ADM-A); for 2026-27 Madison had 38.11% of the value and 34.21% of the attendance, so it pays 36.16%, or $527,065, while Tamworth pays 37.07% ($540,350) and Freedom 26.76% ($390,071).
   - citation: "Apportionment for Fiscal Year 2026-2027 As Adopted by the Joint Board," Madison Annual Report p. 68
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Rows: "Madison $1,185,297,325 112.55 38.11% 34.21% 36.16% $527,065"; "Tamworth $744,697,730 165.15 23.94% 50.20% 37.07% $540,350"; "Freedom $1,180,099,390 51.26 37.94% 15.58% 26.76% $390,071"; total "$1,457,486" (the $1,527,007 budget less $69,521 of fund balance returned). Raw: raw/money/district/madison-ar-2026.txt (p. 71)
5. Madison's share of the SAU 13 budget was $255,370 in 2020-21 and $249,285 in 2021-22, then $378,779 (2022-23, when a behavior analyst and IT director moved to the SAU), $375,417, $467,389 (2024-25, when the SAU preschool was added), $442,499 (2025-26) and $527,065 (2026-27); the "~$250k+" figure is out of date.
   - citation: "Apportionment History 2021 through 2026 for Madison School District," Madison Annual Report p. 68
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "2025-2026 ... 34.83% $442,499"; "2024-2025 ... 35.49% ** $467,389"; "2022-2023 ... 36.55% * $378,779"; "2021-2022 ... 35.09% $249,285"; "2020-2021 ... 36.11% $255,370"; notes "*2022-2023 Added a full-time BCBA and full-time IT Director position to SAU budget"; "**2024-2025 Added SAU 13 Pre-K program to budget". See table madison_sau13_share. Raw: raw/money/district/madison-ar-2026.txt
6. SAU 13's 2026-27 budget of $1,527,007 (up 8.7%) includes the superintendent's office ($350,215 with a wage pool), the business office ($441,439), student services ($347,266), the preschool ($239,672), technology ($122,389) and the joint board ($13,802); the superintendent's salary went from $133,656.91 to $143,012.89 after a 7% raise the Joint Board voted in August 2025.
   - citation: SAU #13 Proposed Budget 2026-2027 (PHv2), Madison Annual Report pp. 69–71; SAU 13 Joint Board Minutes, November 17, 2025
   - source: https://drive.google.com/file/d/1I5_M0D7gBmXe6DW15kJhGS2xeq8xJDe3/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Rows: "01.2320.110.072.00000 SALARY - SUPERINTENDENT $118,965.00 $124,913.00 $133,656.91 $143,012.89 $9,355.98 7.00%"; "Office of the Superintendent/Wage Pool $270,132.42 $264,007.76 $282,195.45 $350,215.25"; "Finance Office ... $441,438.66"; "Pre-K ... $239,672.01"; total "$1,527,007.12 $123,274.63 8.78%". Minutes: "7% increase voted by the SAU Joint Board in August 2025"; "Wage Pool of 6% ($54,000) does not include the Superintendent". Raw: raw/money/district/madison-ar-2026.txt; raw/money/minutes/jt-2025-11-17.*
7. In Madison's HB 1265 report, Madison's share of the two SAU administrators' 2025-26 salaries was $46,553 for the superintendent and $33,089 for the business administrator.
   - citation: Madison School District, "Mandatory Report to Voters on School Expenses," Top Administrator Salaries (2025-2026)
   - source: https://drive.google.com/file/d/1GptYv8gSdQXkoP6lXWN59ZqXd-dr3uiM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Superintendent $46,553 / Business Admnistrator $33,089"; "the top administrator salaries are not adjusted for inflation, are reported based on the district's SAU apportionment, and reflect the only two positions that meet the RSA's definition of administrator." Raw: raw/money/district/hb1265-report.txt, madison-graph-p1.png
8. Madison voters already decide the SAU budget as a separate ballot article whose votes are added to Freedom's and Tamworth's: in March 2026 Madison voted 258 to 342 against the $1,527,007 SAU budget, but it "passed by 20 votes" SAU-wide, so Madison's $527,065 share took effect instead of the $495,120 share of the $1,438,672 adjusted budget.
   - citation: Madison 2026 Official Ballot Results, Article 3; SAU 13 Joint Board Minutes, March 23, 2026 ("SAU 13 Budget Voting Results")
   - source: https://drive.google.com/file/d/18RaGKLMqMmmvHq31gs299sHbprqf3wP4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Ballot: "This year's adjusted budget of $1,438,672 with $495,120 assigned to the School District budget will be adopted if the article does not receive a majority vote of all the district voters voting in this administrative unit ... 258 YES 342 NO". Minutes: "Budget passed by 20 votes". In 2025 Madison voted 330–249 for the SAU budget. Raw: raw/money/district/school-results-2026.*; raw/money/minutes/jt-2026-03-23.*
9. The "law allowing voters to veto SAU administrator pay increases" matches HB 564 (2026 chapter 153), effective August 18, 2026: the SAU budget goes to all member districts as an unamendable article, votes are combined, and if it fails the prior year's budget takes effect without pay increases, new positions or new services; Madison alone cannot reject it if the SAU-wide total approves.
   - citation: RSA 194-C:9, IV (library topic budget-sau-budget-vote, facts 2–3); state-issues.md (HB 564 is 2026 chapter 153)
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-9.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: sau 13
   - note: Pointer to the library rule, applied to SAU 13. Before August 2026 SAU 13 already used this ballot form under the alternative procedure (RSA 194-C:9-b, since repealed; library fact 4). Raw: raw/money/law/rsa-194-C-9.*
10. Madison voters approved Question 2, the HB 1300 school tax cap, on November 3, 2026, 849 to 552 (60.6%, just over the three-fifths needed); by the site's unofficial counts the SAU 13 towns together voted 2,271 to 1,457 (60.9%) (**derived**), which would also exceed three-fifths for the 6% SAU central office cap.
   - citation: Town of Madison, State General Election results, November 3, 2026; site data (district_question_two, unofficial)
   - source: https://www.madison-nh.org/wp-content/uploads/2026/11/Results-2026_Nov-03.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Results text: "STATUTORY QUESTION REQUIRED BY HB 1300 ... Shall the Town of MADISON limit property tax growth for MADISON SCHOOL DISTRICT (SAU #13) ... 849 YES O 552 NO C 60.59 %". Site rows (is_official false): Freedom 641/320, Madison 849/552, Tamworth 781/585. Derived: 2,271 ÷ 3,728 = 60.92%. Results are certified to DRA through the SAU board secretary (library budget-hb-1300-school-tax-cap fact 4); a cap applies from the FY2028 budget (fact 11). Raw: raw/money/town/results-2026-11-03.*; raw/money/state-data/db-q2-cpp.txt
11. In October 2026 Madison's business administrator told the board that under the tax cap "funds may need to be reallocated from the elementary budget to absorb Middle and High School tuition cost increases."
   - citation: Madison School Board Minutes, October 5, 2026 (Business Administrator's Report)
   - source: https://drive.google.com/file/d/1WyF6kj-vpCHSJ7hlH0ki2gbDXfM_8kxf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text quoted. SAU 13 posted a "Tax Cap Information" page with four videos (sau13.org/home/tax-cap-information). Raw: raw/money/minutes/msb-2026-10-05.*; raw/money/sau13/home_tax-cap-information.txt
12. SAU 13's October 2026 working budget for 2027-28 raises the superintendent's salary to $150,000, calculates a wage pool "based on 3.5% COLA" for other SAU staff, raises health insurance 22% with an 85/15 cost share, and estimates Madison's share at $500,773 (35.94%).
   - citation: SAU 13 Joint Board packet, October 26, 2026, "Change Highlights SAU Working Budget v1 to v2" and draft apportionment, pp. 7–8
   - source: https://drive.google.com/file/d/1OVnVA8ajq9gO3Y9yUwBuwyAcAfXeMkq9/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Page viewed (raw/money/images/jt1026-p8.png): "Increased Superintendent salary to $150,000"; "Calculated Wage Pool based on 3.5% COLA - All Wages Except Superintendent"; "Changed Health Insurance cost share to 85/15"; "Madison $ 1,180,098,300 108.11 36.68% 35.20% 35.94% $ 500,773"; total "$ 1,393,408" after a $76,076 fund balance return. Draft; the public hearing is November 23, 2026. Transcribed from image (OCR checked against the page). Raw: raw/money/packets/jt-pk-2026-10-26.*
13. The SAU 13 Joint Board met seven times in 2025-26 (August 18, October 27, November 17 with the budget hearing, March 4, March 23, May 21 and June 22), rotating among Freedom, Madison and Tamworth, and records many votes by name, such as the 11–2 vote approving the 2026-27 SAU budget.
   - citation: SAU 13 Joint Board approved minutes, 2025-26 folder; Minutes of November 17, 2025
   - source: https://www.sau13.org/school-board/sau-joint-board/agendas-packets-minutes
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Folder files (raw/money/sau13/joint-board-folder-listing-2026-11-13.tsv): "2025-08-18_JOINT SAU BOARD APPROVED MINUTES.pdf" through "2026-06-22_JOINT SAU BOARD APPROVED MINUTES.pdf", seven in all. November text: "The motion passed 11-2-0". Policy BBBH-S calls for an annual meeting between April 1 and June 1 and a budget meeting between October 15 and December 15. Raw: raw/money/minutes/jt-2025-*.*, jt-2026-03-23.*
14. In November 2025 the Joint Board voted 12–1 to release the SAU preschool to the Madison School District if Madison voters funded it, after Freedom felt it "was overpaying for the program"; Tamworth and Freedom now buy services under contracts with Madison and may opt out by December 1 each year.
   - citation: SAU 13 Joint Board Minutes, November 17, 2025; Madison School Board special meeting minutes (draft), September 23, 2026
   - source: https://drive.google.com/file/d/1I5_M0D7gBmXe6DW15kJhGS2xeq8xJDe3/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "the potential program change emerged because the Freedom School District felt it was overpaying for the program"; "Motion by Todd Giles to release the SAU Early Childhood Education / Preschool Program to Madison if Madison passes in their budget ... The motion passed 12-1-0"; "could opt out by December 1 of each year". A motion to cut the preschool from the SAU budget failed 1–12. Preschool details belong to the school agent. Raw: raw/money/minutes/jt-2025-11-17.*
15. Few members of the public attend SAU 13 Joint Board meetings, a member said in March 2026; the board discussed livestreaming or recording them, and in April 2026 Madison's chair asked the local MAD TV channel to film them.
   - citation: SAU 13 Joint Board Minutes, March 23, 2026 (Public Input); Madison School Board Minutes, April 6, 2026
   - source: https://drive.google.com/file/d/18RaGKLMqMmmvHq31gs299sHbprqf3wP4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "Principal Heather Woodward inquired if livestream or recording of Joint Board Meetings has been considered? ... Ed Robinson stated very few public members attend the SAU Joint Board meetings"; April: "Chair Jim Curran asked MAD TV if they could film the SAU #13 Joint Board meetings". Raw: raw/money/minutes/jt-2026-03-23.*, msb-2026-04-06.*
16. SAU 13 searched for a new superintendent in spring 2026, with three members from each district on the search committee, and Dr. Kathleen Scholand was attending Madison board meetings as SAU 13 superintendent by October 2026.
   - citation: SAU 13 Joint Board Minutes, March 23, 2026 (Superintendent Search Process); Madison non-public minutes, October 5, 2026 (November 2, 2026 packet)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "Search Committee will be made up of three individuals from each district plus some SAU staff"; "Dr. Kathleen Scholand, SAU 13 Superintendent". The prior superintendent, Dr. Michael Whaland, signed the 2026 annual report. Raw: raw/money/minutes/jt-2026-03-23.*; raw/money/packets/msb-pk-2026-11-02.txt
17. Each SAU 13 district keeps its own board, budget, warrant and union contract: Madison's board negotiates with the Madison Education Association, sets its own policies (posted separately for each district), and in October 2026 voted to establish "a universal policy book for all three districts."
   - citation: Madison 2025 warrant Article 4 (MEA contract); SAU 13 policy pages; Madison School Board Minutes, October 5, 2026 (item H)
   - source: https://www.sau13.org/school-board/madison/school-board-policies
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "Deb Parsons motioned to establish a universal policy book for all three districts, seconded by Jeremy Cox. The motion passed unanimously 5-0-0." Health insurance is bought as "an SAU 13 group, with each group (Tamworth / Madison / Freedom / SAU) billed individually" (raw/money/minutes/jt-2025-10-27.txt). Raw: raw/money/packets/msb-pk-2026-11-02.txt (p. 8)

## district-board-and-public-input: How Madison Residents and Property Owners Can Be Heard, in Madison and at Kennett

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. Madison has no seat or vote on the Conway School Board, which governs Kennett Middle and High; Madison's influence comes through its contracts, its own board, and joint meetings (Conway file and SAU 9 governance facts).
   - citation: Conway Tuition Agreements (Madison), Sections VI and IX; SAU 9 board structure (Jackson file jackson_sau9_board_seats_and_votes)
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Madison is not an SAU 9 district, so it also has no SAU 9 board seat. Raw: raw/money/images/ar26r-p84.png
2. Conway's policy BEDH says the Conway board "encourages residents and families of sending towns to attend," gives 30 to 45 minutes of public comment at each meeting with 3 minutes per speaker, lets speakers address "agenda items or any other District matters," and lets the public ask for items to be placed on the agenda.
   - citation: Conway School Board Policy BEDH, Public Comment and Participation at Board Meetings (revised July 28, 2025)
   - source: https://drive.google.com/file/d/1VWfHmN3np3l31U5Z9zZVXkjQckfTmDCy/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The Board encourages residents and families of sending towns to attend"; "a minimum of thirty minutes and a maximum of forty-five minutes"; "Speakers are limited to three (3) minutes"; "members of the public may also request initiatives or other items be placed on the Board's agenda." Speakers give their town of residence. Raw: raw/money/conway/conway-policy-BEDH.*
3. Madison's 2003 contracts require the Conway board to meet with all sending boards together at least three times a year about the middle and high school programs and to send the Madison board quarterly reports on Madison students' achievement and attendance.
   - citation: Conway Tuition Agreements (Madison), Sections VI and IX
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: See district-tuition-contracts fact 6. Kennett Middle and High principals' reports are on Madison's board consent agendas (e.g., "Kennett High School Principal Report - March 2026," April 6, 2026 minutes). Raw: raw/money/images/ar26r-p84.png; raw/money/minutes/msb-2026-04-06.*
4. Joint SAU 9 and SAU 13 board meetings were cut from four a year to two in 2025 (for 2025-26, October 15, 2025 and a spring date), after low attendance led the SAUs to tie them to SAU 9 board meetings; Madison names members to an "SAU 9/13 Area Joint Board."
   - citation: SAU 13 Joint Board Minutes, August 18, 2025 (Superintendent's Report); Madison School Board Minutes, October 7, 2024; Madison School Board members page
   - source: https://drive.google.com/file/d/1wmeHE78DSNT0KeI1Sd3K8scHdaVMOv1r/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "SAU13 and SAU9 Conway Joint Board Meetings have been reduced from four per year to two per year"; "Joint SAU 13 & SAU 9 Board Meeting: 10-15-2025 & 03-18-2026"; October 2024: "The meeting itself for SAU 9&13 was to move the meeting to different locations because the attendance has been low." Later Madison calendars list January 8, 2026 and May 28, 2026 joint meetings. Members page: "SAU 9/13 AREA JOINT BOARD Jeremy Cox, Cheri Stackpole, & Debra Parsons". Raw: raw/money/minutes/jt-2025-08-18.*, msb-october-7-2024.*; raw/money/sau13/school-board_madison_school-board-members.txt
5. At an April 2024 Madison forum a resident said "we have no voice with Conway," Madison's chair said the joint SAU 9/13 meeting exists "but it is difficult to have input," and Conway's board chair said the joint group is "more of an informative board" and that Madison board members "are always welcome to come to Conway and join the meetings."
   - citation: Madison School Board Minutes, April 1, 2024 (Public Forum - Middle and High School Contracts)
   - source: https://drive.google.com/file/d/16g8lpJH30JXCLjcndgH9HPr8LY0Yl1rB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Statements as recorded. Text: "Adam Price stated that If we stay with Conway, the academic excellence has to be there ... He said we have no voice with Conway. Jim said there is a regularly-scheduled Joint SAU 9/13 School Board meeting but it is difficult to have input"; "Mr. DiGregorio said he agreed with Jim about the Conway/Madison relationship and said it's more of an informative board. He said Madison Board members are always welcome". Raw: raw/money/minutes/msb-april-1-2024.*
6. Madison's own board gives up to 30 minutes of public comment at the start of each regular meeting, 3 minutes per speaker, open to "members of the public," and meets on the first Monday of the month at Madison Elementary's Ruth Chick Library (5:30 p.m. since April 2026).
   - citation: Madison School Board Policy BEDH (adopted October 3, 2022); Policy BEA; Madison School Board Minutes, April 6, 2026
   - source: https://drive.google.com/file/d/19Qt6Oh8leKU8DSPNSwg-PH0BPTZfw7Jq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: BEDH text: "The Board will provide a maximum of 30 minutes to hear public comments at the beginning of each regular Board meeting"; "members of the public may offer comments on agenda items or upon any other matter of public concern". BEA: "the 1st Monday of each month". April 2026: "Ed Robinson motioned to update policy BEA to change meeting time to 5:30 P.M." In May 2026 the chair said comments come at the start "so the board can address them when the relevant subject arises." Raw: raw/money/policies/madison-policy-BEDH.*, madison-policy-BEA.*; raw/money/minutes/msb-2026-04-06.*, msb-2026-05-04.*
7. Parents can also raise Kennett questions through Madison's board, whose student services director follows Madison students at Kennett, and through the contracts' remediation clause: if Kennett's program fails state or accreditation standards, Conway must form a task force with the sending districts and fix it within three years, or a sending district may petition the State Board.
   - citation: Madison Annual Student Services Report, January 2026 (Annual Report p. 17); Conway Tuition Agreements (Madison), Section VIII
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Report: "the director is also responsible for ... our middle and high school students attending Kennett Middle School and Kennett High School." Contract: "the Conway School District shall convene a task force, with representatives of all sending districts, to create a remediation plan, within 180 days ... a maximum period of three (3) years ... shall entitle the complaining district to petition the State Board of Education". Raw: raw/money/district/madison-ar-2026.txt; raw/money/images/ar26r-p84.png
8. Madison's school deliberative session is held in the James Noyes Memorial Hall (the gym) at Madison Elementary, and voting is in the same building with the town election; 70 Madison voters took part in the February 3, 2025 session.
   - citation: Madison 2026 Warrant; Deliberative Session Minutes, February 3, 2025 (Annual Report pp. 5–12)
   - source: https://drive.google.com/file/d/1tZA3upmwnQvVkXsUM4jWpWg4pDp9aGbM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Warrant: "you are hereby notified to meet in the James Noyes Memorial Hall at Madison Elementary School on Route 113 in Madison." Minutes: "Total number of Madison voters participating in this meeting: 70." The town's election page also lists "James Noyes Hall (Gym)". Raw: raw/money/district/madison-warrant-2026.ocr.txt, madison-ar-2026.ocr.txt; raw/money/town/elections-voting.txt
9. New Hampshire law lets no one speak at a town or school district meeting "without leave of the moderator," and lets the moderator set rules of proceeding that the meeting itself can change, so whether a non-voter may speak is up to the moderator and, ultimately, the voters present.
   - citation: RSA 40:7; RSA 40:4, I
   - source: https://gc.nh.gov/rsa/html/III/40/40-7.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Madison
   - note: RSA 40:7: "No person shall speak in any meeting without leave of the moderator". RSA 40:4, I: "may prescribe rules of proceeding; but such rules may be altered by the town." The SB2 deliberative session is the first session of the annual meeting (RSA 40:13; library budget-deliberative-session). Raw: raw/money/law/rsa-40-7.*, rsa-40-4.*
10. The NH Municipal Association's 2026 moderator training says registered voters speak "in their capacity as legislators," non-voters "have no First Amendment right to address sessions of legislative bodies," "the moderator and (ultimately) the voters decide whether a nonvoter may speak," and anyone, including nonresidents, may attend and record the deliberative session.
   - citation: NHMA, "Moderators: SB 2 Advanced" training slides, January 10, 2026, slides 10–11
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/webinars/moderators_sb2_advanced_2026_01_10_ppt.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Guidance, not law. Text: "Who Can Speak? • Registered voters have the right to speak ... • Non-voters are not legislators • Non-legislators have no First Amendment right to address sessions of legislative bodies • The moderator and (ultimately) the voters decide whether a nonvoter may speak"; "Deliberative session is open and any member of the public can attend (nonresidents, media, etc.)". Raw: raw/money/law/nhma-moderators-sb2-advanced-2026.*
11. Madison's printed "Town and School Meeting Procedures" say "every voter is his or her own representative," that speakers go to a microphone and wait to be recognized, and that the meeting can overrule the moderator by a simple majority; they do not address non-voters, and since spring 2026 the school district's moderator post has been vacant.
   - citation: Madison Annual Report, "Town and School Meeting Procedures," p. 90; Madison School Board Minutes, April 6, 2026 (Vacant Position of School Moderator)
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The Town Meeting is a legislature where every voter is his or her own representative"; "The Town can vote to overrule the Moderator whenever it chooses by a simple majority." April 2026: "D. Vacant Position of School Moderator: The board is currently still looking to fill this position"; still on the November 2, 2026 agenda ("School District Moderator"). SAU 13's Madison board members page still lists George Epstein as moderator, which appears out of date. Raw: raw/money/district/madison-ar-2026.txt; raw/money/minutes/msb-2026-04-06.*; raw/money/sau13/school-board_madison_school-board-members.txt
12. Non-voting property owners can speak during public comment at Madison School Board meetings, which policy BEDH opens to "members of the public"; in April 2024 the board voted to let Conway's board chair, who is not a Madison resident, speak at its forum.
   - citation: Madison Policy BEDH; Madison School Board Minutes, April 1, 2024
   - source: https://drive.google.com/file/d/19Qt6Oh8leKU8DSPNSwg-PH0BPTZfw7Jq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Our reading of the policy. April text: "Conway Board Chair Mike DiGregorio asked if he could speak. Motion by Jeremy Cox to allow Mr. DiGregorio to speak, seconded by Ed Robinson and passed unanimously." Raw: raw/money/policies/madison-policy-BEDH.*; raw/money/minutes/msb-april-1-2024.*

## district-consolidation-history: Madison, SAU 13 and SAU 9: Studies, Talks and Votes

- kind: local
- question_type: governance_money
- description: Studies, votes and discussions about cooperative districts, consolidation or sharing schools

1. Madison took part in the 2020–2022 eight-town cooperative school district study (Albany, Bartlett, Conway, Eaton, Freedom, Jackson, Madison and Tamworth), whose planning committees voted unanimously on January 26, 2022 not to form a cooperative district.
   - citation: Jackson file district-consolidation-history 3 in `Jackson/money-and-governance.md` (Superintendent's Report, Jackson 2022 Annual Report)
   - source: https://drive.google.com/file/d/1pOmM-Vx0XVOrCyTGWfm7tlu1TGwnvfwP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Pointer to the Jackson fact; Madison's own committee records were not read.
2. No Madison warrant article, planning committee or board vote on leaving SAU 13 or joining SAU 9 was found in Madison's 2025, 2026 and draft 2027 warrants or in its board and joint board minutes from August 2023 to October 2026.
   - citation: Madison warrants 2025–2027 (draft); Madison and SAU 13 minutes as listed in raw/money/minutes
   - source: https://www.sau13.org/school-board/madison/agendas-packets-minutes
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: A statement about the documents searched. The process for forming or leaving an SAU (RSA 194-C:2: planning committee, State Board review, 3/5 vote) is library topic gov-sau-forming-and-withdrawing; SAUs that merge offices by July 1, 2030 can get $200 per pupil for 2 years (fact 6). Raw: raw/money/law/rsa-194-C-2.*
3. At a fall 2026 joint SAU 9 and SAU 13 board meeting "a conversation about merger was brought up," a Bartlett board member reported, adding that the process requires a great deal of work; no SAU 9 or SAU 13 vote on a merger was found.
   - citation: Bartlett file district-consolidation-history fact 5 (Bartlett SAU Investigative Committee minutes, draft, October 1, 2026)
   - source: https://drive.google.com/file/d/1VhmHbpiAppBbmzn3tXux6c9koHYFTPu9/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Pointer; Bartlett separately formed a committee in 2026 to study leaving SAU 9 (Bartlett file district-sau-governance fact 7). SAU 13's own minutes for September 2026 special meetings were not posted.
4. Madison's board decided in early 2024 not to send its sixth graders to Kennett Middle School when Conway moved its own grade 6 there, and in November 2025 a resident suggested sending Madison's middle schoolers to Tamworth instead.
   - citation: Madison School Board Minutes, March 4, 2024, April 1, 2024 and November 3, 2025 (Public Comment)
   - source: https://drive.google.com/file/d/17HYMsh2WLDRcc3fkGuuKWsar9G7JhJam/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: April 2024: "It was noted that the board has already taken a position on this and that Madison sixth graders will not be going to Conway." November 2025: "Nan Bartlett suggested our middle school go to Tamworth." Tamworth's K.A. Brett School runs grades K–8. Raw: raw/money/minutes/msb-april-1-2024.*, msb-2025-11-03.*
5. The draft 2027 Madison warrant includes Article 8, asking voters to direct the board to set up an advisory committee to study the potential closure of Madison Elementary School (enrollment, savings or costs, effects on students and future use of the building) and report before the 2028 annual meeting.
   - citation: Madison School District, "School Warrant Articles 2027" (draft), Article 8, November 2, 2026 board packet
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Shall the School District vote to direct the School Board to establish an advisory study committee to evaluate the potential closure of Madison Elementary School and to present its findings and recommendations to the District prior to the 2028 Annual District Meeting." Draft; the board had not voted to place it on the warrant as of the posted record. Raw: raw/money/packets/msb-pk-2026-11-02.txt (pp. 53–54)
6. The Advisory Budget Committee wrote in its 2026 report that enrollment was predicted to drop "from 111 to approximately 80," that asked whether analysis of operating a school at that size had begun, "the Superintendents answer was 'No, we have not,'" and suggested sharing paraprofessionals, music, art and library staff across SAU 13 schools.
   - citation: Advisory Budget Committee Report, Madison Annual Report pp. 41–42
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text quoted. The committee's views. In October 2026 Madison's board asked administration for "recommendations to reduce or consolidate roles" and to see which positions "could be combined or shared with other districts" (raw/money/minutes/msb-2026-10-05.txt). Raw: raw/money/district/madison-ar-2026.txt
7. The facts bearing on SAU 13 versus closer ties to SAU 9 are that Madison pays 36.16% of SAU 13's budget ($527,065), holds 5 of 15 Joint Board seats and 3 of 9 base votes, and has no seat in SAU 9, whose Conway board sets Kennett's budget and tuition; no study has weighed the options, so their pros and cons are not documented.
   - citation: district-sau-governance facts 2–4; Jackson file jackson_sau9_board_seats_and_votes
   - source: https://www.sau13.org/school-board/sau-joint-board/school-board-members
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: A summary of facts in this file for the subjective question P13.1, without a verdict. SAU 9 serves districts that send students to Kennett; joining it would follow RSA 194-C:2.

## district-facilities-and-capital: Madison Elementary's Building, Capital Plan, Reserves and Bond

- kind: local
- question_type: governance_money
- description: A district's school buildings: age, planned repairs, capital reserve funds, bonds and energy projects

1. Madison Elementary has three sections: the east side built in 1980 and remodeled in 2019, the gym, kitchen and mechanical wing built in 1989, and the two-story section built in 2000.
   - citation: Madison School District Capital Improvement Plan (updated May 21, 2026), November 2, 2026 board packet
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Section 1 - Two Story Section - Build Date 2000 / Section 2 - East Side of Building - Build Date 1980, Remodeled 2019 / Section 3 - Gym, Kitchen, Mechanicals - Build Date 1989". Raw: raw/money/packets/msb-pk-2026-11-02.txt
2. Madison's capital improvement plan lists each building system with its last replacement and next due date: all roof sections were replaced in 2018 (next due 2043), boilers in 2017 (2043), the gym-wing HVAC with four propane rooftop units in 2024 for $397,271 (2044), and the security system in 2023 (2033).
   - citation: Madison School District Capital Improvement Plan (updated December 30, 2025), Annual Report pp. 49–50
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows (OCR, checked): "Roof Replacement (Sec. 3- Gym) $180,467 $110,000 2018 Melanson 2043 25"; "Heating Systems - Boilers (All) $90,233 $55,000 2017 AccuTemp 2043 25"; "HVAC (Sec. 3) $590,324 $397,271 2024 Bauen Corp 2044 20"; "Security System (Cameras, Alarm) $108,807 $85,000 2023 Pope Security 2033 10". The superintendent's report says the HVAC project was "finalized with the installation of four propane-powered rooftop units." Scanned; transcribed from image (OCR). Raw: raw/money/district/madison-ar-2026.ocr.txt (pp. 52–53), madison-ar-2026.txt (p. 18)
3. The next large items due under the plan are the water supply pumps and 10,000-gallon underground storage (both from 1993, $45,000, due 2028), the heating controls ($80,693, 2031), the security system and detectors (2032–2033) and the 4,000-gallon underground fuel tank (1989, $108,682, due 2035).
   - citation: Madison Capital Improvement Plan (December 30, 2025 and May 21, 2026 versions)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "Water Supply: Pumps (1 @well, 2 boost in boiler room) 1 $15,000 1993 2028 35"; "Water Supply: Storage (10,000 gal U.G.) 1 $30,000 1993 2028 35"; "Replace/Upgrade UG Fuel Tank (4,000 gallon) $108,682 $60,000 1989 Lyman 2035 30"; "Heating Systems - Controls (All) 2 $80,693 $60,000 2019 XL Automation 2031 12". Raw: raw/money/packets/msb-pk-2026-11-02.txt; raw/money/district/madison-ar-2026.ocr.txt
4. The septic system is not a line in the capital plan; septic pumping is paid from the building's contracted services, and in December 2024 the board was waiting for a contractor to replace one of the septic system's two pumps.
   - citation: Madison 2027-28 Working Budget, account 01.2620.430.120 note; Madison School Board Minutes, December 2, 2024
   - source: https://drive.google.com/file/d/1GqP-VE50xWsj3ewPNAjC7wLShoPBsSvg/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Budget note: "Contracted Services ... HVAC/BOILER MAINT ... SEPTIC PUMPING". Minutes: "Septic Update – is not finalized. Waiting for company to schedule to come out to replace one of the two pumps in the septic." Raw: raw/money/packets/msb-pk-2026-11-02.txt (p. 17); raw/money/minutes/msb-december-2-2024.*
5. The plan aims to pay for all listed projects from the Building Maintenance Capital Reserve Fund "without reliance on additional taxation beyond the planned CRF contributions," recommending $135,000 a year; over 15 years it projects $1,423,123 of projects against $2,025,000 of deposits.
   - citation: "Capital Improvement Plan (CIP) – Capital Reserve Fund Summary," Madison Annual Report p. 48
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "2026–2027 (Year 1) $196,953 $80,000 $80,000 $0 $28,575"; "Years 1–15 $1,423,123 $2,025,000 $1,423,123 $601,877 $692,404". Text: "ensuring that all identified projects are fully funded without reliance on additional taxation beyond the planned CRF contributions." CIP note: "Recommended warrant article for bldg CRF - $135,000". Raw: raw/money/district/madison-ar-2026.txt (p. 51)
6. Voters added $80,000 to the building reserve for 2026-27 (416–172), $15,000 to the special education reserve (409–186) and $25,000 to the Madison Corner Schoolhouse reserve (380–206), and rejected an $80,000 petitioned article for phase 2 of the playground (194–388).
   - citation: Madison 2026 Official Ballot Results, Articles 4–6 and 8
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_SCHOOL-BALLOT_RESULTS_03_10_2026-2.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Tallies: "416 YES 172 NO"; "409 YES 186 NO"; "380 YES 206"; "194 YES 388 NO". In 2025 voters added $175,000 (amended at the session to replace the gym floor, 295–285) and $35,000 from surplus (377–204) to the building reserve. Raw: raw/money/district/school-results-2026.*, madison-ar-2026.ocr.txt
7. Madison's capital reserves held $400,909.22 on June 30, 2025 (special education $225,270.50, building $146,080.90, Madison Corner Schoolhouse $25,394.37, technology $4,163.45), and the draft 2027 warrant lists $255,661 (special education), $239,225 (building) and $76,323 (schoolhouse) as of June 30, 2026.
   - citation: "Madison School District - Capital Reserve Fund Balances," Annual Report p. 47; draft 2027 warrant, Articles 4–6
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Rows: "Spec. Ed. Capital Reserve 225,270.50 10,000.00 - 235,270.50"; "Building Capital Reserve 146,080.90 210,000.00 (210,553.44) 145,527.46"; "400,909.22 245,000.00 (210,553.44) 384,961.41". Draft warrant: "$255,661", "$239,225", "$76,323". See table madison_capital_reserves. Raw: raw/money/district/madison-ar-2026.txt; raw/money/packets/msb-pk-2026-11-02.txt
8. Madison's only school debt is a 12-year, $900,000 NH Municipal Bond Bank loan from 2018 (2018 Series B; $803,125 to repay after a premium), with payments of $78,617.50 in 2026-27 and the last payment due August 15, 2030.
   - citation: NHMBB, "2018 Series B Non Guaranteed 12 Year Debt Schedule for Madison School District," Annual Report p. 79
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Total Proceeds $900,000.00 / Premium to Reduce Loan $96,875.00 / Amount of Loan to be Paid $803,125.00"; "08/15/30 65,000.00 65,000.00"; "TOTALS $803,125.00 $253,529.60 $1,056,654.60". The schedule does not name the project. Scanned; transcribed from image (OCR). Raw: raw/money/district/madison-ar-2026.ocr.txt (p. 82)
9. In October 2026 the board approved up to $13,000 from the building reserve, after a public hearing, for ALPHA Facilities Solutions to inventory and assess the building's capital assets jointly with the Town of Madison and the Village District of Eidelweiss.
   - citation: Madison School Board Minutes, October 5, 2026 (Facilities Management, ALPHA); November 2, 2026 agenda (public hearing)
   - source: https://drive.google.com/file/d/1WyF6kj-vpCHSJ7hlH0ki2gbDXfM_8kxf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Ed Robinson motioned to approve the contract with ALPHA, contingent upon buy-in from the Village of Eidelweiss and the Town of Madison, with funds to come from the Building Capital Reserve Account following a hearing, in an amount not to exceed $13,000.00". Raw: raw/money/minutes/msb-2026-10-05.*, msb-2026-11-02-agenda.*

## educator-licensing-pathways: From Paraeducator to Teacher in New Hampshire

- kind: rule
- question_type: rules
- description: New Hampshire paraeducator certification and the routes from paraeducator to a teaching license

1. New Hampshire's Paraeducator II certificate requires a high school diploma or HiSET plus one of: an associate degree or at least 48 college credits, a passing score on a national test such as the ETS ParaPro, or a portfolio showing knowledge of reading, writing and math instruction; Paraeducator I requires only a high school diploma or HiSET.
   - citation: N.H. Admin. Rules, Ed 504.06 and Ed 504.07
   - source: https://gc.nh.gov/rules/state_agencies/ed500.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "To be certified as a Paraeducator II, an individual shall ... (1) Possess a high school degree or HiSET equivalent; and (2) Meet one of the following requirements: a. Hold an associates degree or a minimum of 48 college credit hours; b. Demonstrate a passing score on a nationally recognized assessment such as the ParaPro offered by ETS; or c. ... portfolio". Raw: raw/money/law/ed500-rules.txt
2. A person can earn a New Hampshire teaching license while employed as a teacher through a Statement of Eligibility and site-based licensing plan, available for endorsements on the state's critical shortage list; elementary K–6 candidates need at least two college content courses each in math, English, social studies and science, and each candidate is assigned a mentor.
   - citation: N.H. Admin. Rules, Ed 505.06 (a), (e), (g), (i)
   - source: https://gc.nh.gov/rules/state_agencies/ed500.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Before beginning an application for an SBLP, a candidate shall obtain an SOE, valid for 3 years ... pertaining to any endorsements on the critical shortage list"; "Applicants for elementary K-6 education and early childhood education shall have successfully completed at least 2 college-level content courses each in mathematics, English, social studies, and science"; "each candidate for this pathway to licensure shall be assigned a mentor". Other endorsements need 15 college credits in the area or a passing subject test (d). The current critical shortage list is on NH DOE's site, which refused automated requests. Raw: raw/money/law/ed500-rules.txt

## madison_operating_budget_votes: Madison School District Operating Budget, Default and Votes (Article 2)

- unit: dollars
- period: Budgets for 2020-21 through 2026-27; year: 2027
- source: Madison Annual Report (year ending June 30, 2025), "7-Year Budget Comparison," p. 51; ballot results 2025 and 2026 — https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view ; https://www.madison-nh.org/wp-content/uploads/2026/03/2026_SCHOOL-BALLOT_RESULTS_03_10_2026-2.pdf
- as_of: 2026-11-13
- raw: raw/money/district/madison-ar-2026.txt, madison-ar-2026.ocr.txt, school-results-2026.ocr.txt, madison-msdsb.ocr.txt
- note: Value is the operating budget in effect (approved or default), without the SAU share and special articles. 2026 includes the $123,585 contract article. 2027 is the first year with $400,000 of grant spending inside the article. Votes are yes–no on the proposed budget.

| Place | Id | Year | Status | Value | Proposed | Default | Votes |
|---|---|---|---|---|---|---|---|
| Madison | 333 | 2021 | Default | 7051637 | | | |
| Madison | 333 | 2022 | Default | 7185693 | | | |
| Madison | 333 | 2023 | Approved | 7314511 | | | |
| Madison | 333 | 2024 | Approved | 7440477 | | | |
| Madison | 333 | 2025 | Approved | 7110576 | | | |
| Madison | 333 | 2026 | Default (+ contract article) | 7314006 | 7284200 | 7190421 | 215–313 |
| Madison | 333 | 2027 | Default | 7114497 | 7370153 (as amended) | 7114497 | 286–316 |

## madison_tuition_lines: Madison's Kennett Tuition and Out-of-District Special Education Lines

- unit: dollars
- period: FY2024 and FY2025 actual, FY2026 actual, FY2027 adopted, FY2028 working draft; year: 2028
- source: Madison 2027-2028 Working Budget v2, November 2, 2026 board packet — https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
- as_of: 2026-11-13
- raw: raw/money/packets/msb-pk-2026-11-02.txt
- note: FY2026 out-of-district tuition spent was $254. FY2028 figures are a draft made while Conway negotiations were open.

| Place | Id | Year | Line | Value |
|---|---|---|---|---|
| Madison | 333 | 2024 | Middle school tuition (Conway) | 768673 |
| Madison | 333 | 2025 | Middle school tuition (Conway) | 721527 |
| Madison | 333 | 2026 | Middle school tuition (Conway) | 1020387 |
| Madison | 333 | 2027 | Middle school tuition (Conway) | 833542 |
| Madison | 333 | 2028 | Middle school tuition (Conway), draft | 961000 |
| Madison | 333 | 2024 | High school tuition (Conway) | 1512830 |
| Madison | 333 | 2025 | High school tuition (Conway) | 1612996 |
| Madison | 333 | 2026 | High school tuition (Conway) | 1432221 |
| Madison | 333 | 2027 | High school tuition (Conway) | 1679256 |
| Madison | 333 | 2028 | High school tuition (Conway), draft | 1980000 |
| Madison | 333 | 2024 | Out-of-district special education tuition | 1017968 |
| Madison | 333 | 2025 | Out-of-district special education tuition | 207029 |
| Madison | 333 | 2027 | Out-of-district special education tuition | 150000 |

## madison_doe25_per_pupil_2025: DOE-25 Elementary Spending per Pupil by Function, Madison, Bartlett and Jackson, 2024-25

- unit: dollars per pupil
- period: 2024-25; year: 2025
- source: site data (DOE-25 FY2025 expenditure lines and ADM) — https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
- as_of: 2026-11-13
- raw: raw/money/state-data/db-doe25-2025.txt, db-adm.txt
- note: **Derived**: each DOE-25 general fund elementary line divided by the district's ADM (Madison 125.70, Bartlett 159.12, Jackson 36.45), rounded. Excludes Kennett tuition (reported on DOE-25's middle and high school pages). General administration includes each district's SAU share. Not NH DOE's cost per pupil.

| Place | Id | Function | Value |
|---|---|---|---|
| Madison | 333 | 1100 Regular instruction | 10076 |
| Bartlett | 35 | 1100 Regular instruction | 11079 |
| Jackson | 271 | 1100 Regular instruction | 18539 |
| Madison | 333 | 1200 Special programs | 5101 |
| Bartlett | 35 | 1200 Special programs | 7163 |
| Jackson | 271 | 1200 Special programs | 10065 |
| Madison | 333 | 2100 Student support | 3728 |
| Bartlett | 35 | 2100 Student support | 3261 |
| Jackson | 271 | 2100 Student support | 5317 |
| Madison | 333 | 2300 General administration | 4007 |
| Bartlett | 35 | 2300 General administration | 2370 |
| Jackson | 271 | 2300 General administration | 3527 |
| Madison | 333 | 2400 School administration | 2306 |
| Bartlett | 35 | 2400 School administration | 2319 |
| Jackson | 271 | 2400 School administration | 6962 |
| Madison | 333 | 2600 Operation and maintenance of plant | 5576 |
| Bartlett | 35 | 2600 Operation and maintenance of plant | 3649 |
| Jackson | 271 | 2600 Operation and maintenance of plant | 8103 |
| Madison | 333 | 2700 Transportation | 1755 |
| Bartlett | 35 | 2700 Transportation | 1616 |
| Jackson | 271 | 2700 Transportation | 4215 |

## madison_enrollment_history: Madison Elementary Enrollment, Fall 1990 to October 2025

- unit: count
- period: Fall 1990–fall 2015 (NCES), October 1, 2016–2025 (district); year: 2026
- source: NCES Common Core of Data via the Urban Institute Education Data Portal — https://educationdata.urban.org/api/v1/schools/ccd/directory/1995/?ncessch=330456000238 ; Madison Annual Report, "Report of Official Enrollment," p. 75
- as_of: 2026-11-13
- raw: raw/money/nces/mes-dir-*.json; raw/money/district/madison-ar-2026.txt
- note: Grades K–6. Year is the school year ending (fall 1995 = 1996). NCES and district counts may differ slightly in method; the site's school_enrollment table also has 2016–2025 counts.

| Place | Id | Year | Value | Source |
|---|---|---|---|---|
| Madison | 333 | 1991 | 194 | NCES |
| Madison | 333 | 1994 | 233 | NCES |
| Madison | 333 | 1996 | 235 | NCES |
| Madison | 333 | 1998 | 227 | NCES |
| Madison | 333 | 2000 | 196 | NCES |
| Madison | 333 | 2003 | 171 | NCES |
| Madison | 333 | 2006 | 159 | NCES |
| Madison | 333 | 2011 | 174 | NCES |
| Madison | 333 | 2016 | 134 | NCES |
| Madison | 333 | 2017 | 131 | District, October 1, 2016 |
| Madison | 333 | 2020 | 139 | District, October 1, 2019 |
| Madison | 333 | 2023 | 124 | District, October 1, 2022 |
| Madison | 333 | 2025 | 110 | District, October 1, 2024 |
| Madison | 333 | 2026 | 102 | District, October 1, 2025 |
| Madison | 333 | 2027 | 90 | Principal's projection for 2026-27 |

## madison_sau13_share: Madison's Share of the SAU 13 Budget

- unit: dollars
- period: 2020-21 to 2027-28 (draft); year: 2028
- source: "Apportionment History 2021 through 2026," Madison Annual Report p. 68; SAU 13 Joint Board packet, October 26, 2026 — https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
- as_of: 2026-11-13
- raw: raw/money/district/madison-ar-2026.txt; raw/money/images/jt1026-p8.png
- note: Share = half equalized value share plus half attendance share. 2028 is the October 2026 draft.

| Place | Id | Year | Share (%) | Value |
|---|---|---|---|---|
| Madison | 333 | 2021 | 36.11 | 255370 |
| Madison | 333 | 2022 | 35.09 | 249285 |
| Madison | 333 | 2023 | 36.55 | 378779 |
| Madison | 333 | 2024 | 35.74 | 375417 |
| Madison | 333 | 2025 | 35.49 | 467389 |
| Madison | 333 | 2026 | 34.83 | 442499 |
| Madison | 333 | 2027 | 36.16 | 527065 |
| Madison | 333 | 2028 | 35.94 | 500773 |

## madison_capital_reserves: Madison School District Capital Reserve Balances

- unit: dollars
- period: June 30, 2025 and June 30, 2026; year: 2026
- source: Madison Annual Report p. 47; draft 2027 warrant (November 2, 2026 packet) — https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
- as_of: 2026-11-13
- raw: raw/money/district/madison-ar-2026.txt; raw/money/packets/msb-pk-2026-11-02.txt
- note: 2026 balances exclude interest; the building balance "including obligations". Technology reserve not listed in the draft warrant.

| Place | Id | Year | Fund | Value |
|---|---|---|---|---|
| Madison | 333 | 2025 | Special Education Capital Reserve | 225270.50 |
| Madison | 333 | 2025 | Building Capital Reserve | 146080.90 |
| Madison | 333 | 2025 | Madison Corner School House Capital Reserve | 25394.37 |
| Madison | 333 | 2025 | Technology Capital Reserve | 4163.45 |
| Madison | 333 | 2026 | Special Education Capital Reserve | 255661 |
| Madison | 333 | 2026 | Building Capital Reserve | 239225 |
| Madison | 333 | 2026 | Madison Corner School House Capital Reserve | 76323 |

## For another file

- **School agent (madison-elementary.md):**
  - October 1 enrollment by grade 2016–2025, projected 2026-27 class sizes (90 students), special services counts (29 IEPs at MES, 17 504 plans, 1 English learner, end of 2024-25), staff roles and the 2026-27 staff list, the paraprofessional book study, and the board's March 2026 discussion of 101 hours of para support. Sources: raw/money/district/madison-ar-2026.txt (pp. 17–22, 75, 89); raw/money/packets/msb-pk-2026-11-02.txt; raw/money/minutes/msb-2026-03-05.txt.
  - The draft 2027 Article 8 (study of closing Madison Elementary) also matters to the school and community files.
- **Daily-life agent:** ESY runs July 6–August 5, 2026, Monday–Wednesday 9:00–12:00 at MES (raw/money/minutes/msb-2026-04-06.txt); 2026-27 transportation fell $230,042 with a "new service provider" (raw/money/district/madison-msdsb.ocr.txt); before and after school program finances (msb-2025-11-03).
- **Kennett agent:** Madison's board decided in 2024 not to send grade 6 to KMS; KMS proposed a joint field trip and PowerSchool help for Madison sixth graders (October 2026); Madison students with special services at KMS (5) and KHS (11). Sources: raw/money/minutes/msb-april-1-2024.*, msb-2026-10-05.*.
- **Community agent:** the Madison Corner School Preservation Committee (Seven to Save listing, $14,000 in donations, LCHIP application); the November 2026 Question 2 vote; the counselor's report that homeless students "increased significantly" in 2025-26. Sources: raw/money/district/madison-ar-2026.txt (pp. 21, 33); raw/money/town/results-2026-11-03.*.
- **Library (`additional-data/district-practices.md`), Madison fact 78:** it says Madison's deliberative session and voting dates "were not found." They are February 2, 2026 at 7:00 p.m. and March 10, 2026 (raw/money/district/madison-warrant-2026.ocr.txt), and, in the draft, February 1 and March 9, 2027.
- **Earlier town files:**
  - Conway file, district-tuition-contracts fact 8: consistent; this file adds Madison's February 5, 2024 vote not to renew and the October 2024 outreach to Governor Wentworth and Moultonborough.
  - Bartlett file, district-consolidation-history fact 5: the fall 2026 SAU 9/13 "merger" conversation is not in SAU 13's posted minutes; SAU 13's August 2025 minutes record that SAU 9/13 joint meetings were cut from four a year to two.
  - Jackson file, district-budget-and-cost 27 in `Jackson/money-and-governance.md` (Madison's high school tuition per pupil read from a 2019 chart) is now joined by Madison's own tuition lines (table madison_tuition_lines).
- **Site data issues (recommendation A8):** Madison's salary bands show no internal error. The site's Tamworth 2026 MA maximum ($8,579) and Jackson 2026 BA minimum ($4,600) are confirmed in the database (raw/money/state-data/db-salary.txt). Madison's DOE-25 ADM for 2025 (125.70) differs from the ADM-A used for the SAU apportionment (112.55 for 2025); the reason is not documented.
- **Shared SAU folder:** the SAU 13 facts here (joint board, apportionment, superintendent pay, preschool move, tax cap vote) belong in a future `town/sau13/` file for Freedom and Tamworth.

## Not retrieved

- **SSA COLA page** (https://www.ssa.gov/oact/cola/colaseries.html and latestCOLA.html): HTTP 403 to curl and WebFetch. Used the Wayback snapshot of November 9, 2026.
- **DRA exemptions summary** (https://www.revenue.nh.gov/mun-prop/property/equalization-2025/documents/etc-alpha-summary.pdf and earlier years): "Access Denied." The elderly exemption figures come from the 2024 MS-1 in the town report; the 2025 MS-1 (after the revaluation) and a 2025 town report (tried /wp-content/uploads/2026/02/0000-2025-Town-Report.pdf and variants: 404) were not found.
- **MEA collective bargaining agreement and salary schedule:** not posted on sau13.org or in the Madison board packets searched (January 2025–November 2026); only the board's October 2026 comparison table and the 2025 warrant's cost figures were found. Para daily hours and hourly rates are therefore unknown.
- **Waterfront share of value:** the 2025 revaluation report (https://www.madison-nh.org/wp-content/uploads/2025/11/Madison-2025-USPAP-Manual-Rev-1.pdf, 559 pages, searched as text) gives parcel counts and base waterfront values but not the total value of waterfront parcels. The town's "Assessment Data" link was not opened.
- **Madison November 2, 2026 minutes:** not yet posted (agenda only), so the reported presentation of Conway's offer and a Governor Wentworth contract could not be checked in Madison's own record.
- **Default budget authority after August 12, 2026:** whether Madison's Advisory Budget Committee (created by town meeting in 1991) is an RSA 32:14 budget committee that now sets the school default budget was not found in any document read.
- **SAU 9/13 joint meeting minutes** (October 15, 2025; January 8, 2026; May 28, 2026; fall 2026): not found on sau13.org; SAU 13 September 2026 special meeting minutes were not posted.
- **NH DOE critical shortage list and paraeducator pages:** NH DOE refuses automated requests (earlier towns' notes); the rules were read on gc.nh.gov instead.
- **Madison 2024 annual report** (https://drive.google.com/file/d/1f59tWwoLzfSw9xYwDIGpw8P_pbdTkR3u/view): downloaded and OCR'd but not cited; older warrant and budget history before 2020-21 was not compiled.
