# Conway School District: Money, Buildings, Staff Contracts and Governance

Part of the Conway research (town/Conway). Gathered November 13, 2026.

## Summary

**What's covered:** 8 topics, 98 facts and 7 number tables on the Conway School District's budget, default budgets, tuition revenue, buildings, staff contracts and the Municipal Budget Committee.
- The operating budget and default budget for every vote from 2019 to 2026, the two years the default took effect (2024-25 and 2025-26), and what the board cut each time.
- How the default budget is built (the district's own 2025-26 and 2026-27 calculations).
- Tuition revenue from sending towns (FY2016–FY2027), how the current and 2027 contracts set tuition, Kennett enrollment by town (March 2026), and Conway's 2019-20 share of students against its share of the charge (**derived** reading).
- The John H. Fuller building: closure vote, budgeted building costs, the 2016 bond, the appraisal, the January 2026 vote not to sell, the housing, YMCA and health-care ideas, and the statutes that bear on a sale or lease.
- The Kennett Middle School capital plan (FY2027–FY2032), roof and curtain-wall work, and trust fund balances.
- The Safety and Security Trust Fund (created April 2025): deposits, balance and spending.
- Teacher (CEA 2026–2029) and support staff (CESP 2025–2028) pay, reduction-in-force and recall rules, health insurance, and the new-teacher mentor program.
- Paraprofessional pay against May 2025 BLS wages for retail, food service and lodging jobs in the Northern New Hampshire nonmetropolitan area, and teacher pay against neighbors and local rent (all comparisons **derived**).
- The district's revenue mix and its estimated 2026 school rate. Conway's DRA tax rates (2014–2025) and NH DOE school taxes (2011–2025) are in the site's data (property_tax), so this file does not repeat them.

**Main sources:** Conway voter guides (2019–2026), ballot results (2024–2026), deliberative session minutes and packets (2021–2026), annual reports (FY2019–FY2025, scanned; pages rendered and read), the FY2026 adopted line-item budget and FY2027 draft summaries, school board, Facilities and John Fuller Ad Hoc Committee minutes (2023–November 2026), the CEA and CESP agreements, Conway policies FL, FF and GCPA, the 2027 Albany grade 7–8 contract, RSA 194:2, 194:3, 194:3-f, 194:3-g and 194:61, BLS OEWS (May 2025, via the BLS API), ACS 2020–2024 (DP04), and read-only queries of the site database.

**Premises checked:**
- "$120,000 a year for the Fuller building" was not found in any document. The FY2026 budget carries $193,061 for the building's operation, maintenance and grounds (**derived** sum), and bond payments of $128,295 fell in FY2026.
- "$40M+ budget" is correct: the 2026-27 operating budget is $42,555,376, and all articles passed in April 2026 total $45,011,445 (**derived**).
- "Staffing reductions in the 2025–26 budget" is correct: 7.6 positions were cut when the default budget took effect.
- The "Safety and Security Expendable Trust Fund" exists; voters created it on April 8, 2025.
- 6th grade moved into Kennett Middle School when John Fuller closed in September 2024 (the schools agent covers the history).

**Main gaps:**
- No statute read says whether a school district sale of real estate needs a district vote. RSA 194:2 lets the district "dispose of" property but does not name the deciding body.
- The cost of restoring the Pine Tree and Conway Intermediate names in 2025 was not recorded in minutes or reports.
- The Town of Conway's Municipal Budget Committee minutes after January 2024 are not posted where they could be found; its recorded votes come from the warrants and ballots.
- NHHFA's rental survey and the NH DOE unused-facilities list could not be reached.

**Proposed shared topic:** none. The paraprofessional and teacher pay comparisons sit under `district-budget-and-cost`.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P2.2 Will budget and staffing cuts reduce shop, welding or electrical sections at Kennett? | district-classrooms-and-staff facts 1–8; district-budget-and-cost fact 17 | full | 2025-26 default cuts removed the career center's Computer Science program (one teacher). Automotive, machine tool, construction trades, culinary and CAD teachers stay funded in the FY2026 budget. The 2026-27 budget cuts a Dean and merges the career center director role into a new Dean of Student Programming and CTE. No cut to machine tool/welding or construction sections was found. Kennett programs themselves are the Kennett agent's |
| P2.3 How Conway's school tax relates to sending-town students | district-tuition-contracts facts 1–10; district-tax-and-state-aid facts 1–4; site data: property_tax (Conway district); tables conway_tuition_revenue, conway_kennett_enrollment_by_town; Jackson and Bartlett files (sending-side contract terms) | full | Facts only. In 2019-20 Conway had 48.74% of Kennett attendance and was charged 43.83% of the operating budget (**derived** reading). The 2027 contracts drop property value from the charge. In March 2026, 313 of Kennett's 600 students lived in Conway |
| P4.1 The John Fuller building: closure, carrying cost, when it can be sold or repurposed | district-facilities-and-capital facts 1–14 | partial | Closed by a 7-0-0 board vote, April 17, 2024. Carrying cost: see the premise note. The bond's 10-year call date was August 2026. A sale or lease triggers the charter school right of first refusal (RSA 194:61). The statute naming who must approve a sale was not found |
| P4.2 What do taxpayers get for a $40M+ budget? | district-budget-and-cost facts 1–6; table conway_operating_budget_votes; site data: cost per pupil, assessments, graduation | full | Figures side by side, no judgment. Says plainly what can't be concluded |
| P4.3 How the default budget works and what happened when it took effect | district-budget-and-cost facts 7–14; table conway_operating_budget_votes; library: budget-default-budget, budget-official-ballot-sb2 | full | Default took effect for 2024-25 (Fuller closed a year early) and 2025-26 (7.6 positions and $80,000 of maintenance cut) |
| P8.2 Does the Fuller debate create uncertainty for buyers? | district-facilities-and-capital facts 10–14 | partial | Status only. No source measures an effect on buyers or prices |
| P12.2 (money side) Cost of the Lakeside/Mountainside renaming and restoration | district-budget-and-cost fact 18 | partial | Signs cost $3,595 ($2,000 from the PTO). Staff time was not quantified. The restoration cost was not found. The schools agent covers the history |
| P12.3 Para wages against local retail and hospitality wages | district-budget-and-cost facts 19–22; table conway_para_and_regional_wages | full | Comparisons **derived**. BLS area covers Carroll, Coos and Grafton counties |
| P14.1 Municipal Budget Committee and School Board disagreements | district-board-and-public-input facts 1–9; library: budget-committees | full | Recorded votes 2023–2026 and what members said, as recorded. No "why" beyond the record |
| P14.2 Special education's share of budget growth | district-budget-and-cost facts 23–28; table conway_special_education_spending; site data: special_education_aid (Conway district); library: money-special-education-aid, money-special-education-costs-trends | full | The board said special education was most of the 2025-26 increase. The 2026-27 default adds $413,647 for special education against $1,331,631 for health insurance |
| P14.3 Capital plan for the KMS building and others | district-facilities-and-capital facts 15–21; table conway_kms_capital_plan | full | A $4.5 million five-year plan for KMS is attached to the 2027 middle school contracts |
| P17.2 Safety and Security Trust Fund | district-safety-and-security facts 1–5 | full | At the elementary schools the fund has paid for access controls at Conway Intermediate (June 2026). Pine Tree ADA doors are pending |
| P18.1 Teacher pay and benefits against neighbors and rent | district-budget-and-cost facts 29–34; town-housing fact 1; site data: average salary, salary schedules, census (Conway district: median gross rent) | full | Comparisons **derived**. The site's salary-band rows for Conway appear shifted (see For another file) |
| P18.2 Junior teachers' security under the union contract | district-classrooms-and-staff facts 9–11 | full | Layoffs go by evaluation group first, then seniority. Notice is due by April 15. Recall lasts one year |
| P18.3 Mentoring and professional development for new teachers | district-classrooms-and-staff facts 12–14 | full | Conway School Board records; not shown to be SAU-wide |

## district-budget-and-cost: Conway's Budget, Default Budgets, Special Education and Pay

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. Conway voters approved a 2026-27 operating budget of $42,555,376 (including $1,590,000 offset by grants) on April 14, 2026, 1,226 to 390, with the Municipal Budget Committee recommending it 12-1-0 and the School Board 5-0-0.
   - citation: Conway School District Annual School Election results, April 14, 2026, Article 6
   - source: https://drive.google.com/file/d/14no6-JNdH3d4DmzmXRTwjErl-VWuFujx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Ballot text: "totaling $42,555,376 with $1,590,000 to offset this amount from various grants. (Recommended by the Municipal Budget Committee 12-1-0)... ($42,555,376 is recommended by the School Board 5-0-0)"; tally "1226 Yes / 390 No" (page viewed, raw/money/elections/er-2026-p2.png). See table conway_operating_budget_votes. Raw: raw/money/elections/er-2026.pdf, .txt
2. All 13 money and policy articles on Conway's April 2026 ballot passed, and the appropriations among them total $45,011,445 for 2026-27 (**derived**): the $42,555,376 operating budget, $736,640 for the teachers' contract, $1,000,000 for the buildings maintenance trust, $250,000 for the bus and equipment reserve, $150,000 for the safety and security trust, $100,000 for the special education reserve, $88,000 for Project SUCCEED, $81,429 for the three tuition-contract maintenance trusts and $50,000 for band equipment from fund balance.
   - citation: Conway School District Annual School Election results, April 14, 2026, Articles 2–12
   - source: https://drive.google.com/file/d/14no6-JNdH3d4DmzmXRTwjErl-VWuFujx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Derived sum: 54,443 + 17,086 + 9,900 + 736,640 + 42,555,376 + 88,000 + 250,000 + 1,000,000 + 100,000 + 150,000 + 50,000 = 45,011,445. Each article shows "Yes" above "No" on the results sheet (e.g., Article 9 "999 / 616", Article 11 "981 / 618"). Article 13 (open enrollment) and 14 (advisory EFA resolution) carry no appropriation. The district's own "Grand total appropriation" for 2025-26 was $44,258,972 (2026 packet, p. 24). Raw: raw/money/elections/er-2026.*; raw/money/packets/dp-2026.ocr.txt
3. NH DOE's cost per pupil for Conway was $26,469 in 2024-25, up from $17,462 in 2017-18 and $13,594 in 2009-10, while its average daily membership fell from 1,730.93 (2017-18) to 1,388.51 (2024-25); of 54 districts with elementary, middle and high figures in 2024-25, 11 had a higher total (**derived** count).
   - citation: site data (district_cost_per_pupil and doe_form_adm, Conway, 2010–2025)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Query rows: "2025 | 27870 | 25518 | 25893 | 26469"; "2018 | 17769 | 18429 | 16776 | 17462"; ADM "2018 | ... | 1730.93", "2025 | ... | 1388.51". Count: "higher_k12 11 | k12 54" (our count, not a DOE rank). DOE says cost per pupil should be compared only between districts serving the same grades (library measure-cost-per-pupil). It leaves out tuition and transportation. Raw: raw/money/state-data/site-db-conway-queries.txt
4. Since July 2025, Conway's operating budget article must print the prior year's cost per pupil and proficiency rates, so the April 2026 ballot read: "The average cost-per-pupil for the preceding year ... is $26,469. ELA Proficiency: 51%; Math Proficiency: 32%; Science Proficiency: 30%."
   - citation: Conway School District Warrant and Ballot, April 14, 2026, Article 6; RSA 189:75, I (library topic measure-cost-per-pupil, fact 8)
   - source: https://drive.google.com/file/d/14no6-JNdH3d4DmzmXRTwjErl-VWuFujx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Ballot text quoted. These are 2024-25 results. The site's assessment data show Conway's all-student proficiency for 2025-26 at 37% math, 48% reading and 26% science, and for 2018-19 at 36%, 48% and 26% (raw/money/state-data/site-db-conway-queries.txt). Raw: raw/money/elections/er-2026.*
5. Conway's annual reports describe outcomes mostly in words: the 2026 Kennett principal's report says students "continue to demonstrate meaningful growth from freshman to senior year," that career and technical students often earn college credit, and that the school remains "focused on strengthening our State Assessment performance."
   - citation: Conway School District Annual Report (fiscal year ending June 30, 2025), 2026 Principal's Report (Kennett High School), pp. 22–23
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Academically, students at Kennett High School continue to demonstrate meaningful growth from freshman to senior year ... We remain focused on strengthening our State Assessment performance, with a commitment to achieving proficiency in all content areas." Graduation, college plans and credential counts are in the site data and the SAU 9 file. Scanned; transcribed from image (OCR). Raw: raw/money/annual-reports/ar-fy2025.pdf, .ocr.txt
6. The budget and results figures can be set side by side, but they cannot show whether the spending caused or limited the results: no Conway document links them, cost per pupil excludes tuition and transportation, and test results depend on many things a budget does not measure.
   - citation: library topics measure-cost-per-pupil and comparing-small-schools; Conway ballot, April 14, 2026
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: A statement about the limits of the data, for questions about "return on investment." At the 2025 deliberative session one budget committee member cited a 2022 audit showing 49.8% of spending on instruction against a state average of 61.6%, and the superintendent replied that the "executive administration" category also includes building, maintenance and transportation staff (raw/money/deliberative/dm-2025.ocr.txt, lines 126–135 and 300–304). Raw: raw/money/state-data/site-db-conway-queries.txt
7. In an SB2 district like Conway, the default budget is last year's operating budget adjusted for contracts, debt and obligations required by law, less one-time costs and the pay of positions eliminated in the proposed budget; it takes effect if voters reject the operating budget article (library topic budget-default-budget).
   - citation: RSA 40:13, IX (library topic budget-default-budget); Conway ballot wording, 2019–2026
   - source: https://gc.nh.gov/rsa/html/III/40/40-13.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Conway
   - note: Conway's ballot repeats the rule: "Should this article be defeated, the default budget shall be $... which is the same as last year, with certain adjustments required by previous action of the Conway School District or by law, or the governing body may hold one special meeting ... to take up the issue of a revised operating budget only." Since August 12, 2026, a town budget committee (not the school board) determines the default budget (library topic budget-default-budget, fact 6). Raw: raw/money/elections/er-2026.txt
8. Conway's own calculation of the 2026-27 default budget ($42,565,234) started from the 2025-26 total of $44,258,972, removed $2,859,429 of special articles, and adjusted for the second CESP year (+$122,200), third AFSCME year (+$76,083), SAU share (+$325,168), health insurance (+$1,331,631), special education (+$413,647), retirement (−$134,636), debt service (−$17,294) and positions eliminated in the proposed budget (−$981,132).
   - citation: Conway School District Deliberative Session packet, March 2, 2026, "Conway School District Default Budget for 2026-2027," p. 24
   - source: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Plus SAU Share 325,168 / Plus Health Insurance 1,331,631 / Less Retirement - 134,636 / Plus Dental Insurance 16,699 / Plus Special Education Increase (excl health/dental/retirement) 413,647 ... Less Eliminated Positions in FY27 Proposed -981,132 / Plus Sub Total Additions/Decreases 1,165,691 / TOTAL ESTIMATED 2026-2027 DEFAULT BUDGET 42,565,234". Scanned; transcribed from image (OCR). Raw: raw/money/packets/dp-2026.pdf, .ocr.txt
9. For 2026-27 Conway's default budget ($42,565,234) was $9,858 higher than the operating budget voters approved ($42,555,376) (**derived**), so rejecting the budget would not have lowered spending that year.
   - citation: Conway ballot, April 14, 2026, Article 6
   - source: https://drive.google.com/file/d/14no6-JNdH3d4DmzmXRTwjErl-VWuFujx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Derived: 42,565,234 − 42,555,376 = 9,858. The OCR of the 2026 voter guide's page 4 misread the default as $42,865,234; the ballot (page viewed) and packet read $42,565,234. Raw: raw/money/elections/er-2026-p2.png; raw/money/packets/dp-2026.ocr.txt
10. Conway voters rejected the operating budget twice in a row: on April 9, 2024 (859 yes, 876 no), putting the $39,002,004 default in place for 2024-25 instead of the proposed $40,109,103, and on April 8, 2025 (831 yes, 1,081 no), putting the $40,986,456 default in place for 2025-26 instead of $41,637,542.
   - citation: Conway School District election results, April 9, 2024 and April 8, 2025, Article 6
   - source: https://drive.google.com/file/d/1ESXvMD9XByvg0fC3sJAQgd1YDDCcSzzP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Pages viewed: 2024 "859 YES / NO 876" (raw/money/elections/er-2024-p2.png); 2025 "831 Yes / FAILED 1081 No" (er-2025-p2.png). The FY2024 annual report also prints "YES - 859 NO - 876" (raw/money/annual-reports/ar-fy2024.ocr.txt). 2024 results URL: https://drive.google.com/file/d/1xBzF32J82kO9gLv7ZZxBp2hYlliINh9B/view. Raw: raw/money/elections/er-2024.*, er-2025.*
11. When the 2024 default took effect, the superintendent said it required a $1.107 million reduction, so the closing of an elementary school planned for September 2025 was moved up a year, and on April 17, 2024 the board voted 7-0-0 to close John H. Fuller School for fall 2024.
   - citation: Conway School Board Special Meeting Minutes, April 17, 2024
   - source: https://drive.google.com/file/d/1gwy8LjjAtQWS7FIow4n_MwSdf6o8Bmds/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Unfortunately, with the default budget being voted in and the need to find a $1.107 million reduction in the budget, this process has been moved up a year to go into effect September 2024"; "Mr. Davison moved, seconded by Vice-Chair Wallace to close John Fuller School for Fall 2024. Motion Carried. (7-0-0)." At the 2024 deliberative session the superintendent had said "In this cycle" the default "equals a school closing" (raw/money/deliberative/dm-2024.ocr.txt). Raw: raw/money/minutes/csb-2024-04-17-special.*
12. Under the 2025-26 default, $651,086 below the board's budget, the board approved (5-2 on April 14, 2025) cutting 7.6 positions (0.6 performing arts, 1 career tech, 1 special education, 1 science, 2 paraprofessionals, 1 elementary classroom teacher and 1 school safety secretary), $20,000 from the elementary rotating maintenance fund and $60,000 of Kennett exterior painting, moved to trust funds.
   - citation: Conway Deliberative Session packet, March 2, 2026, "District Personnel Changes ... FY26 Budget," p. 8; Conway School Board Minutes, April 14, 2025, item D
   - source: https://drive.google.com/file/d/1ogmxz0PvV-Zx90zr3k3boolBIvvQCRbB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Packet: "The default reduction included a total of 7.6 FTE positions: .6 Performing Arts teacher, 1 Career Tech teacher, 1 Special Education teacher, 1 Science teacher, 2 paraprofessionals, 1 Elementary Classroom teacher, 1 School Safety Secretary." Minutes: "A motion was made by Hodge to consider the proposed budget reductions, seconded by Beckwith 5-2[Davidson, Stearns]-0". The board had already cut $250,000 ($200,000 of it special education) before the vote. Packet URL: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view. Raw: raw/money/packets/dp-2026.ocr.txt; raw/money/minutes/csb-2025-04-14.*
13. Conway's 2025-26 default ($40,986,456) was built from the 2024-25 total approved budget of $41,543,047, less $2,259,429 of special articles, plus $588,613 for the third CEA year, $436,353 for health insurance, $380,015 for special education and $242,631 for the SAU share, less $165,852 for positions eliminated in the proposed budget.
   - citation: Conway Deliberative Session packet, March 5, 2025, "2025-2026 Default Calculation," p. 22
   - source: https://drive.google.com/file/d/1x4mQl2I6U_YKGR77aK1mkCkJYtWlcRgF/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Plus 3rd Year CEA Negotiated Agreement 588,613 ... Plus Health Insurance 436,353 ... Plus Special Education Increase (excl health/dental/retirement) 380,015 ... Less Eliminated Positions in FY26 Proposed -165,852 ... TOTAL ESTIMATED 2025-2026 DEFAULT BUDGET 40,986,456 / Default budget is less than School Board Proposed Budget by $651,086". Transcribed from image (OCR). Raw: raw/money/packets/dp-2025.pdf, .ocr.txt
14. The school board, not the voters, decides which lines absorb a default-budget reduction; in April 2025 the superintendent said "the only way to get to a number like that is through personnel," and the board's list also cut maintenance, while administrative positions were cut in later budgets (a Dean of Students in 2026-27).
   - citation: Conway School Board Minutes, April 14, 2025; Conway Deliberative Session packet, March 2, 2026, p. 8
   - source: https://drive.google.com/file/d/1ogmxz0PvV-Zx90zr3k3boolBIvvQCRbB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Minutes text: "As we have said many times over, the only way to get to a number like that is through personnel." At the 2024 deliberative session the superintendent described the default as "last year's budget plus any obligations ... minus one-time costs." The default formula itself (library budget-default-budget) does not say which lines must be cut. Raw: raw/money/minutes/csb-2025-04-14.*; raw/money/packets/dp-2026.ocr.txt; raw/money/deliberative/dm-2024.ocr.txt
15. Conway's 2026-27 draft budget by function rose 2.64% to $40,965,375 (before grants), with the largest increases in retiree benefits (+$355,138), school board/SAU services (+$325,437), student services (+$305,258), special education (+$220,624) and transportation (+$177,035), and decreases in regular education (−$519,825) and co-curricular (−$64,932).
   - citation: Conway School District, "2026-2027 Draft Budget, Function Summary" (for the January 7, 2026 CMBC meeting)
   - source: https://drive.google.com/file/d/1OouEQWbPL8Od-2tBRywuqf9g6KmiSKBJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Rows: "Regular Education ... 12,522,302 ... 12,002,477 ... (519,825) -4.15%"; "Special Education ... 6,406,124 ... 6,626,748 ... 220,624 3.44%"; "Grand Total 39,783,673 ... 39,912,042 ... 40,965,375 ... 1,053,333 2.64%". "School Board" includes the SAU 9 share. Draft figures; the adopted operating budget was $42,555,376 including $1,590,000 of grants. Raw: raw/money/budget/fy27-draft-function.pdf, .txt
16. Conway's executive summary lists operating budget figures of $38,566,756 (2019-20), $37,873,652 (2020-21), $38,720,144 (2021-22), $39,987,421 (2022-23), $40,820,244 (2023-24), $39,283,648 (2024-25, default), $41,399,542 (2025-26, default) and $42,555,376 (2026-27), and says personnel are about 74.2% of the operating budget.
   - citation: Conway Deliberative Session packet, March 2, 2026, "FY 2026 Proposed Budget Executive Summary as of 2/10/26," p. 6
   - source: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Eight year operating budget figures: 2019-2020 $38,566,756 ... 2024-2025 $39,283,648 (Default, Includes 2nd year of CEA, 1st year of AFSCME agreements) 2025-2026 $41,399,542 (Default, Includes 3rd year of CEA, 2nd year of AFSCME agreements) 2026-2027 $42,555,376"; "Personnel costs account for approximately 74.2% of the operating budget." These figures include contract cost articles and differ from the Article 6 amounts in table conway_operating_budget_votes. **Derived**: 2019-20 to 2026-27 is +10.3%. Raw: raw/money/packets/dp-2026.ocr.txt
17. The 2025-26 default cuts removed the career center's Computer Science teacher (budgeted at $55,016 in 2024-25, $0 in 2025-26), while the FY2026 budget still funds the automotive ($70,571), machine tool ($62,292), construction trades ($62,292), culinary ($70,842), CAD ($71,364), business, marketing, visual media and part-time criminal justice teachers.
   - citation: Conway FY26 Adopted Budget, Unit 9 Career Tech, account 41-09-1300-5110, p. 62
   - source: https://drive.google.com/file/d/135rQbusiABGRcazlm3fsuTjlvVyAd0Ag/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/budget/fy26-adopted-p62.png): "SALARIES, TCHR COMPUTER SCIENCE ... 55,016 ... -"; "SALARIES, TEACHER MACHINE TOOL ... 59,585 ... 62,292"; "SALARIES, TEACHER, C/T CONSTRUCTION TRADES ... 59,585 ... 62,292". No separate electrical or welding teacher line exists; the board's October 2025 minutes refer to "machine tools/welding" as one program. Unit 9 Career Tech totals $1,610,095 (FY26 adopted) and $1,581,253 (FY27 draft, −1.79%) (raw/money/budget/fy27-draft-unit.txt). Raw: raw/money/budget/fy26-adopted.pdf, .txt
18. The 2024 renaming of the two elementary schools cost $3,595 for signs, of which the PTO donated $2,000 and $1,595 came from activity funds rather than the operating budget, according to the superintendent's response read at the 2025 deliberative session; staff time "has not been quantified," and no cost for restoring the old names after the April 2025 vote was found in minutes or reports.
   - citation: Conway School District Deliberative Session Minutes, March 5, 2025, Article 14
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text (read aloud by Rhoda Quinn): "The manpower hours would have needed to be spent regardless. Therefore that expense has not been quantified ... The expense was the signage only: $3,595.00. PTO donated $2K total for the two signs therefore $1,595 was taken from activity funds and not the operating budget." The superintendent added that reassigning "the 1,500 students one-by-one to new school codes" is "a manpower hour issue." Article 14 passed 1,142–794 (raw/money/elections/er-2025-p3.png). The history of the names is the schools agent's. Transcribed from image (OCR). Raw: raw/money/deliberative/dm-2025.pdf, .ocr.txt
19. Conway paraprofessionals are paid by the hour under the Conway Educational Support Personnel (CESP) agreement for July 1, 2025 to June 30, 2028: in 2025-26 from $19.92 (levels 0–1, no degree) to $26.40 (15+ years), and with a bachelor's degree from $20.42 to $26.90; all staff got a $3.00 raise in 2025-26, then 3% a year (4% at step 15+).
   - citation: CESP Agreement 2025–2028, Article XIII and Appendix A; Conway Annual Report (FY2025), "CESP 2025-26 Salary Schedule," p. 43
   - source: https://files.smartsites.parentsquare.com/10271/cesp_agreement_2025-2028_revised_w_sidebar.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/annual-reports/ar-fy2025-p46.png): "0, 1 $19.92 $20.02 $20.42 $20.92 ... 15+ $26.40 $26.50 $26.90 $27.40". Agreement: "All Employees will receive a minimum $3.00 raise from the previous year plus an additional step increase if applicable". 2026-27: $20.52 to $27.46; 2027-28: $21.13 to $28.55. See table conway_para_and_regional_wages. Raw: raw/money/contracts/cesp-2025-2028.pdf, .ocr.txt
20. Voters approved the CESP contract cost items in April 2025, 1,175 to 743 ($413,087 in year one; $1,627,833 compounded over three years), after the school board recommended it 7-0-0 and the Municipal Budget Committee 7-6-1; the district's voter guide said "The goal of negotiations was to bring the starting salary to a competitive wage."
   - citation: Conway Voters Guide, April 2025, Article 5; election results, April 8, 2025
   - source: https://drive.google.com/file/d/1ePGX6xouAxOPtvLKUIEO5lGFCU7M1gFb/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Guide text: "All staff will have their hourly wage increased by $3.00 in 2025/26 with 3% or 4% increases in years 2 and 3 depending on years of service." Results: "PASSED 1175 Yes / 743 No" (raw/money/elections/er-2025-p2.png). CESP covers about 80 members (2026 packet). A full-time school-year CESP employee works 30 or more hours a week for 191 days, counting paid holidays (agreement Article I). Raw: raw/money/voter-guides/vg-2025.*; raw/money/elections/er-2025.*
21. Conway's 2025-26 starting paraprofessional rate ($19.92 an hour) is above the May 2025 mean hourly wages BLS reports for the Northern New Hampshire nonmetropolitan area (Carroll, Coos and Grafton counties) for retail salespersons ($18.05), cashiers ($15.63), waiters and waitresses ($18.82, tips included), hotel desk clerks ($18.25) and maids and housekeepers ($18.02), and above restaurant cooks ($19.75) (**derived** comparison).
   - citation: CESP Agreement 2025–2028, Appendix A; U.S. Bureau of Labor Statistics, OEWS May 2025, Northern New Hampshire nonmetropolitan area (area 3300001), via the BLS public data API
   - source: https://www.bls.gov/oes/2025/may/nh_counties.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: API values (series OEUM3300001000000XXXXXX03, 2025 annual): 412031 "18.05", 412011 "15.63", 353031 "18.82", 434081 "18.25", 372012 "18.02", 352014 "19.75". County list text: "Carroll County - Northern New Hampshire nonmetropolitan area" (also Coos and Grafton). BLS counts tips in waiters' wages. The comparison is hourly only: paraprofessionals work a school-year schedule, while many hospitality jobs are seasonal or year-round; no source says how many hours either group works. Raw: raw/money/wages/bls-api-oews-northern-nh-nonmetro.json, bls-req.json, bls-nh-counties-2025.html, .txt
22. In the same BLS data, first-line supervisors of retail workers average $25.92 an hour and all occupations $32.99 (median $24.55), and teaching assistants in the area average $39,780 a year (median $37,350); Conway's paraprofessional scale reaches $26.40 an hour only after 15 years (**derived** comparison).
   - citation: BLS OEWS May 2025, Northern New Hampshire nonmetropolitan area; CESP Agreement 2025–2028, Appendix A
   - source: https://www.bls.gov/oes/2025/may/nh_counties.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: API values: 411011 "25.92"; 000000 hourly mean "32.99", median "24.55"; 259045 annual mean "39780", median "37350" (BLS reports teaching assistants as annual pay because many do not work year-round). Employment in the area: retail salespersons 3,050; cashiers 2,190; waiters 1,740; teaching assistants 1,310. No source states para vacancy reasons; the 2026 packet lists 4 paraprofessional vacancies at the high school/career center in 2025-26. Raw: raw/money/wages/bls-api-oews-northern-nh-nonmetro.json, -2.json; raw/money/packets/dp-2026.ocr.txt
23. Conway's local special education spending (excluding federal grants) was $5,889,636 in 2019-20, $5,500,600 in 2020-21, $4,911,262 in 2021-22, $5,274,903 in 2022-23, $5,335,156 in 2023-24 and $6,170,185 in 2024-25, by the district's own expense reports.
   - citation: Conway School District Annual Reports, "Special Education Expenses/Revenue" pages (reports for FY2021, FY2022, FY2023, FY2024, FY2025)
   - source: https://drive.google.com/drive/folders/1lXxwDUcJ7_PsczB2vihTm_62-NMRiq6j
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Sub Total Special Education Expenses, Local $ 5,889,636 $5,500,600" (FY2021 report); "SUSTOTAL SPECIAL EDUCATION EXPENSES (LOCAL) $ 5,335,156 6,170,185" (FY2025 report, page viewed). **Derived**: 2023-24 to 2024-25 rose $835,029 (15.7%). See table conway_special_education_spending. Transcribed from image (OCR). Raw: raw/money/annual-reports/ar-fy2021…ar-fy2025 (.pdf, .ocr.txt)
24. At the 2025 deliberative session, board member Mike DiGregorio said special education was "literally the vast majority" of the board's proposed 2025-26 increase, citing out-of-district placement prices and state requirements, followed by the teachers' and AFSCME contracts and an 8.5% health insurance increase on about $7 million of insurance costs.
   - citation: Conway Deliberative Session Minutes, March 5, 2025, Article 6
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Special Education (SPED) is literally the vast majority of it ... some a lot of it had to do with price reflections of some of our out of district placement, and some where what the State requires of which we had no control over ... Another large expense is health insurance with an 8.5% increase and believes approximately $7 million dollars of our budget is part of health insurance." Budget committee chair Alex Loth said "Fifty (50%) of this year's increase is SPED costs." Statements as recorded. Raw: raw/money/deliberative/dm-2025.ocr.txt
25. In the 2026-27 default calculation, the special education increase ($413,647) was about a third of the health insurance increase ($1,331,631), and in 2025-26 it was $380,015 against $588,613 for the teachers' contract and $436,353 for health insurance (**derived** comparison of the district's own lines).
   - citation: Conway Deliberative Session packets, March 5, 2025 (p. 22) and March 2, 2026 (p. 24)
   - source: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Derived: 413,647 ÷ 1,331,631 = 31%. These are default-budget adjustments, not the full change in the proposed budget, and special education here excludes its health, dental and retirement costs. Special education is a legal duty under IDEA; the share of costs that is "mandated" versus "discretionary" is not split out in any Conway document. Raw: raw/money/packets/dp-2025.ocr.txt, dp-2026.ocr.txt
26. Conway's out-of-district special education tuition lines total $462,000 in the 2025-26 budget (elementary $180,000, middle school $198,000, high school $84,000), against $452,918 actually spent in 2023-24 (**derived** sums); in November 2026 the director of student services said out-of-district placements, including move-in students, had increased.
   - citation: Conway FY26 Adopted Budget, accounts 41-02/03/04-1200-5560; Conway School Board Special Meeting (Budget Review) Minutes (draft), November 5, 2026
   - source: https://drive.google.com/file/d/135rQbusiABGRcazlm3fsuTjlvVyAd0Ag/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Budget rows: "TUITION, SPECIAL EDUCATION ELEMENTARY 350,180 / 297,268 / 302,180 / 180,000"; "TUITION, SPECIAL EDUCATION 172,000 / 155,650 / 125,000 / 84,000" (high school); middle "- / - / 70,000 / 198,000" (FY24 adopted, FY24 actual, FY25 adopted, FY26 adopted). Minutes: "Out-of-District placements including move-in students have increased ... The incoming kindergarten class is approximately 30% special education." Minutes URL: https://drive.google.com/file/d/1nnBOX0aNn_Toc_nQQllAc-taAjVlwl6T/view. Raw: raw/money/budget/fy26-adopted.txt; raw/money/minutes/csb-2026-11-05-special-draft.*
27. Conway reported $143,197 of state special education (catastrophic) aid in FY2020, and its FY2025 annual report estimated $86,637 for FY2026; Conway also counts an "adequacy allocation for special education" of $417,102 in 2024-25.
   - citation: site data (DOE-25 revenue account 3230, Conway); Conway Annual Report (FY2025), Estimated Revenues and Special Education Revenue, pp. 17 and 20
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Query rows: "2020 | 3230 | Special Education Aid | 143196.71", "2021 ... 279629.75", "2022 ... 124156.73", "2025 ... 8217.89" (no rows for 2023–2024). FY2021-FY2025 match NH DOE's special education aid files, which are in the site's data with each year's costs, entitlement and proration (special_education_aid, Conway district); NH DOE's final FY2026 aid was $131,603.83, more than the district's estimate. Rewritten November 14, 2026 to keep only what that data doesn't have. Revenue page (viewed): "Special Education Aid $8,218 $86,637 $0". The $417,102 "adequacy allocation for special education" equals NH DOE's FY2025 special education differentiated aid for Conway ($417,101.81) in the site's data (adequacy_aid). How the aid works is library topic money-special-education-aid. Raw: raw/money/state-data/site-db-conway-queries.txt; raw/money/annual-reports/ar-fy2025-p20.png, ar-fy2025.ocr.txt
28. Conway keeps a Special Education Capital Reserve Fund (established 2008) to absorb unbudgeted special education costs; its balance was $453,721 in early 2026, voters added $100,000 in April 2026 (1,097 to 516), and in October 2025 the business administrator said it had not had to be used that year.
   - citation: Conway Annual Report (FY2025), "Explanation of Conway School Board Warrant Articles 2026-27," p. 7; election results April 14, 2026, Article 10; Conway School Board Minutes, October 27, 2025
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The objective of this fund is to stabilize the impact of non-budgeted special education expenditures that may occur as student needs change throughout the year ... The current balance is: $453,721". Minutes: "Mike Wade says that we have not had to use the Special Ed Trust Fund, although there is potential for that to happen this year." In April 2025 a resident asked why the fund was not tapped to offset the default cut (raw/money/minutes/csb-2025-04-14.txt). Raw: raw/money/annual-reports/ar-fy2025.ocr.txt; raw/money/elections/er-2026-p2.png; raw/money/minutes/csb-2025-10-27.*
29. Conway's teachers are covered by the Conway Education Association (CEA) agreement for July 1, 2026 to June 30, 2029, whose 2026-27 schedule starts at $46,071 (bachelor's, step 1) and $48,801 (master's, step 1), adds $1,000 a step for 25 steps, and tops out at $73,001 (bachelor's) and $84,541 (master's plus 60) at step 25+.
   - citation: CEA Agreement 2026–2029, Article XXV and Appendix B, "Salary Schedule 2026/27," p. 31
   - source: https://files.smartsites.parentsquare.com/10271/cea_agreement_2026-2029_with_signatues.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/contracts/cea-2026-2029-p31.png): "STEP 1000 Base Salary 26-27 46,071 ... 1 46,071 47,162 48,255 48,801 51,077 53,354 ... 25+ 73,001 74,731 76,462 77,327 80,934 84,541". Bases rise to $47,071 (2027-28) and $48,071 (2028-29). No raise may exceed $5,000 a year (25-2). Raw: raw/money/contracts/cea-2026-2029.pdf, .ocr.txt
30. The new CEA schedule replaced a 46-step 2025-26 schedule that started at $42,571 (bachelor's, step 1) and reached $87,571 (bachelor's) and $102,632 (master's plus 60) only at step 46, so starting pay rose $3,500 (8.2%) for 2026-27 (**derived**); voters approved the contract's cost items, $736,640 in year one and $3,879,299 compounded, 1,084 to 559.
   - citation: Conway Annual Report (FY2025), Appendix B, "Conway School District 2025-26 Salary Schedule," p. 42; election results April 14, 2026, Article 5
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/annual-reports/ar-fy2025-p45.png): "STEP – 1,000 Base Salary – 42,571 ... 46 83,192 87,571 ... 102,632". The voter guide said "The goal of negotiations was to bring the starting salary to a competitive wage." At the 2025 deliberative session a board member said Conway teachers had left for raises of $15,000 to $30,000. Derived: 46,071 − 42,571 = 3,500. Raw: raw/money/annual-reports/ar-fy2025.*; raw/money/elections/er-2026.txt; raw/money/voter-guides/vg-2026.ocr.txt
31. Conway's 2026-27 starting teacher salary ($46,071, bachelor's) is $271 above Bartlett's ($45,800) and $71 above Jackson's hiring schedule ($46,000), while Conway's master's start ($48,801) is between Bartlett's ($48,100) and Jackson's ($49,312) (**derived** comparison).
   - citation: CEA Agreement 2026–2029, Appendix B; Bartlett file district-budget-and-cost fact 17; Jackson file district-budget-and-cost 36 in `Jackson/money-and-governance.md`
   - source: https://files.smartsites.parentsquare.com/10271/cea_agreement_2026-2029_with_signatues.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Derived differences. Bartlett's schedule tops out at $63,300 (bachelor's, step 15) and Jackson's at $59,500 (bachelor's, step 10), against Conway's $73,001 at step 25+; the number of steps differs, so top pay and years to reach it both matter. Raw: raw/money/contracts/cea-2026-2029.ocr.txt; town/Bartlett/raw/money/sau9/bea-agreement-2026-27.ocr.txt; town/Jackson/raw/money/sau9/jackson-personnel-contracted-2026-27.txt
32. NH DOE's 2025-26 average teacher salary for Conway, $60,390, was 12th of 14 nearby districts in the site data (above Wakefield and Madison, below Bartlett at $61,429 and Jackson at $68,342), and up from $46,459 in 2018-19 (**derived** ranking).
   - citation: site data (district_teacher_average_salary, 2026)
   - source: https://nhfacts.com
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Query rows: "Governor Wentworth Regional | 80090.00 ... Bartlett | 61429.00 | Littleton | 61271.00 | Conway | 60390.00 | Wakefield | 58619.19 | Madison | 57164.83". The 14 districts were chosen by us as nearby or regional. Averages depend on staff experience as well as the schedule. Raw: raw/money/state-data/site-db-conway-queries.txt
33. Under the CEA agreement Conway pays 80% of the premium for the base Anthem BlueChoice Open Access Advantage HDHP plan, covers the first $500 (single) or $1,000 (two-person or family) of the 2026-27 deductible, pays 90% of single dental, and pays a $4,800 waiver to teachers who take coverage elsewhere; Bartlett also pays 80% of its base premium (Bartlett file fact 18).
   - citation: CEA Agreement 2026–2029, Article XXII
   - source: https://files.smartsites.parentsquare.com/10271/cea_agreement_2026-2029_with_signatues.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The District will pay 80% of the premium cost of the Anthem BlueChoice Open Access Advantage HDHP Plan ... For the 2026/27 school year, the District will cover the first portion of the services of the base plan that apply to the deductible at the rate of: $500 single, $1000 two (2) people, and $1000 family"; "insurance waiver payment of $4,800". Teachers hired after July 1, 2014 get a benefit prorated to their FTE. The 2026-27 budget assumed a not-to-exceed 12.5% rate increase (2026 packet). Raw: raw/money/contracts/cea-2026-2029.ocr.txt
34. A year's rent at Conway's median gross rent for 2020–2024 (American Community Survey; the figure is in the site's Census data) equals about 28.5% of a first-year Conway teacher's 2026-27 salary of $46,071 before taxes, and about 56% of a starting paraprofessional's pay if paid $20.52 for 6 hours a day on 191 days (**derived**, illustrative).
   - citation: U.S. Census Bureau, ACS 5-year 2020–2024, DP04 (Conway town); CEA Agreement 2026–2029; CESP Agreement 2025–2028
   - source: https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP04)&ucgid=0600000US3300314660
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Derived from the ACS median gross rent of $1,095 a month (±$141; DP04_0134E, the same as the site database's 2020-2024 value): 1,095 × 12 = 13,140; 13,140 ÷ 46,071 = 28.5%; 20.52 × 6 × 191 = 23,516; 13,140 ÷ 23,516 = 55.9%. The 191 days count paid holidays. The 6-hour day is an assumption for illustration; the CESP agreement sets 30+ hours a week for full-time school-year staff but lets the board set each position's day. ACS median rent includes utilities and covers existing leases, not current asking rents. Raw: raw/money/census/ACSDP5Y2024.DP04-conway.json (copy of the Jackson research pull)

## district-classrooms-and-staff: Staffing Cuts, Reductions in Force and New-Teacher Support in Conway

- kind: local
- question_type: local_practice
- description: How a district's schools group classes and grades, their staff and roles, staffing changes, substitutes and aides, and how the schools describe themselves

1. In its first year of school consolidation (2024-25), Conway cut 14.7 FTE positions: a principal, a clerical aide, an administrative assistant, a nurse, 2 custodians, a family support liaison, 3 elementary classroom teachers, a library media specialist and 4 paraprofessionals.
   - citation: Conway Deliberative Session packet, March 2, 2026, "District Personnel Changes in the Conway School Board FY 25 Budget," p. 8
   - source: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Through year one of school consolidation in FY 25, the Conway School Board reduced a total of 14.7 FTE positions. These included: 1 Principal, 1 Clerical Aide, 1 Administrative Assistant, 1 nurse, 2 Custodians, 1 Family Support Liaison, 3 Elementary Classroom teachers K-5, 1 Library Media Specialist, and 4 Paraprofessionals." At the 2025 deliberative session the superintendent said eleven classroom teachers resigned or retired during consolidation. Transcribed from image (OCR). Raw: raw/money/packets/dp-2026.ocr.txt; raw/money/deliberative/dm-2025.ocr.txt
2. In April 2025, with the default budget in effect, the superintendent proposed ending the career center's Computer Science program "based on low enrollment, primarily," saying it was "on the lowest enrollment list" each year; board members Randy Davison and Matt Stearns argued to keep it, and the board approved the reduction list 5-2.
   - citation: Conway School Board Minutes, April 14, 2025, item D, "Consider Proposed Budget Reductions"
   - source: https://drive.google.com/file/d/1ogmxz0PvV-Zx90zr3k3boolBIvvQCRbB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Additionally we are proposing reducing a program at the Career Tech Center: Computer Science based on low enrollment, primarily. Each year it is on the lowest enrollment list ... we are as bare bones as we can get with core programming at the high school and had to look at CT this time." The superintendent said "There is board policy, three years in a low enrollment course list – it's conversation for reduction," and that employees had to be notified of a RIF by April 15. Raw: raw/money/minutes/csb-2025-04-14.*
3. No record was found of cuts to machine tool/welding, construction trades, automotive or electrical sections in Conway's 2025-26 or 2026-27 budgets; the 2026-27 proposed reductions at Kennett were a Dean of Students, a custodian, a special education teacher, 4 paraprofessionals and 2 unnamed teaching positions.
   - citation: Conway Deliberative Session packet, March 2, 2026, "District Personnel Changes in the Proposed Conway School Board FY27 Budget," pp. 8–9; Conway FY26 Adopted Budget, Unit 9
   - source: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Packet text: "Kennett High School: Reduction of 1 Dean of Students (administrative position), Reduction of 1 custodian, Reduction of 1 special education teacher, Reduction of 4 paraprofessionals, Reduction of 2 teaching positions". The packet does not name the two teaching positions. Kennett Middle School lost a grade 6 teacher and a unified arts teacher. A statement about the documents searched (minutes July 2023–November 2026, budgets FY2026–FY2027). Raw: raw/money/packets/dp-2026.ocr.txt; raw/money/budget/fy26-adopted-p62.png
4. In January 2026 the board voted 6-1 to restructure Kennett's administration when the career center director retired, replacing two Dean posts with a Dean of Student Programming and Career and Technical Education and a Dean of Instruction and Student Achievement; the superintendent said the change "will not dilute the Career Tech center but make it even stronger."
   - citation: Conway School Board Minutes, January 12, 2026, item f (job descriptions)
   - source: https://drive.google.com/file/d/1ci-SNO7qFnWeie-H2MgZpRztFFo0EUq_/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "We recognized that our Career Tech Director is retiring at the end of the month which creates a vacancy ... The electives offered at the high school are in Career Tech because we have made elective reductions in the high school and not as many reductions in Career Tech"; "The board voted on approving the job description of the High School Dean of Student Programming and Career and Technical Education, as amended. 6-1[Davison]-0". Davison said "our Career Tech center is a gem and the Directors have to be certified." Raw: raw/money/minutes/csb-2026-01-12.*
5. Kennett's career and technical courses are capped at 16 students because of the number of shop stations, and each program has one teacher teaching intro, Level 1 and Level 2 courses; in fall 2025 Intro to Culinary and intro photography each had 64 seats, and 47 primary requests for intro photography went unfilled.
   - citation: Conway School Board Minutes, October 14, 2025 (Kennett course selection presentation)
   - source: https://drive.google.com/file/d/1i3DNgfqzFcoPW2ryw0K-JdWdH48hjiKW/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "CT has teachers 6 to 18 and have slightly lower numbers for the teacher load as the classes have to be capped at 16 so you can't double up on those max stations ... There is only one teacher for each of those programs"; "47 primary requests for students for intro to photography that were unable to get in – 4 sections, 16 each, that is the cap ... Intro to Culinary, again 64 total seats because of those 16 stations". Program detail is the Kennett agent's. Raw: raw/money/minutes/csb-2025-10-14.*
6. In November 2025 the business administrator said a capital plan had been made for the career center shops and suggested adding money to the career tech equipment trust fund, after two of three automotive lifts could not be repaired; one lift was replaced in spring 2026.
   - citation: Conway Facilities Committee Minutes, November 20, 2025 and March 19, 2026
   - source: https://drive.google.com/file/d/1Tp13our9DftC7ys1xgbriolJpS7xep4w/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Mike Wade stated that they went through Career Tech and made a CIP plan specific to the shops. He suggests adding money to the Career Tech equipment trust fund on the warrant in the spring." No career tech equipment article appeared on the April 2026 ballot. The shop CIP itself was not found. March 2026 text: "Mike Wade shared that the lift is being delivered and will be installed ... Mike Wade spoke about meeting with Christine Thompson and is developing a CIP plan for the CTC." Raw: raw/money/facilities/fac-2025-11-20.*, fac-2026-03-19.*
7. At the 2025 deliberative session the superintendent said the $651,000 gap between the board's budget and the default would require cutting "7, 10 or 11 staff people" and "would impact the Career Tech programing, significantly."
   - citation: Conway Deliberative Session Minutes, March 5, 2025, Article 6
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The default budget is approximately $651,000 less than the Conway School Board budget. That would require the reduction of 7, 10 or 11 staff people across all of our schools ... It would impact the Career Tech programing, significantly." The cut made a month later was one career tech teacher (Computer Science) (fact 2). Raw: raw/money/deliberative/dm-2025.ocr.txt
8. Conway's administrator group shrank from 15 people in prior years to 11 in the 2026-27 budget, which also shifts part of the technology coordinator's and one technology aide's pay to SAU 9 and adds an early learning interventionist and a student support paraprofessional at Pine Tree Primary.
   - citation: Conway Deliberative Session packet, March 2, 2026, pp. 7–9
   - source: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "In the FY2027 budget, there are 11 people in this group, compared to 15 in prior years"; "Pine Tree Primary School: Addition of 1 early learning interventionist, Addition of 1 student support paraprofessional". Class sizes and school staffing are the schools agent's. Raw: raw/money/packets/dp-2026.ocr.txt
9. Under the 2026–2029 CEA agreement, layoffs within a teaching classification go first to teachers rated unsatisfactory, then basic, then proficient or distinguished, using the last three years of evaluations, and within each group "teachers having the most seniority going last," with seniority counted by years in the district within the certification area.
   - citation: CEA Agreement 2026–2029, Article 7-2, Reduction in Force
   - source: https://files.smartsites.parentsquare.com/10271/cea_agreement_2026-2029_with_signatues.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Reductions in staff will be made first from the group of teachers determined to be unsatisfactory by the professional evaluation System with teachers having the most seniority going last. If further reductions are needed, they will be made from the group of teachers determined to be basic ... If further reductions are needed, they will be made from the group of teachers determined to be proficient or distinguished". A first-year teacher rated proficient is laid off before a senior proficient teacher in the same certification area, but after any teacher rated basic or unsatisfactory there (**derived** reading). Raw: raw/money/contracts/cea-2026-2029.pdf, .ocr.txt, -p10.png
10. The CEA agreement requires the superintendent to notify the association and affected teachers "as soon as reduction in force is seriously contemplated," requires layoff notice "on or before April 15" before the school year it takes effect, and gives laid-off teachers rated proficient or distinguished one year of recall rights in order of seniority, with two weeks to accept and preference on substitute lists.
   - citation: CEA Agreement 2026–2029, Article 7-2 and 7-2.3
   - source: https://files.smartsites.parentsquare.com/10271/cea_agreement_2026-2029_with_signatues.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "For a one- (1) year period from the end of employment, after a lay-off due to a reduction in force, such members of the bargaining unit who were evaluated Proficient or Distinguished in their last year with the District in order of greatest seniority shall be re-nominated and elected. The recalled individual will have 2 weeks ... Teachers unemployed under this clause shall be given preference on substitute lists". Conway's ballot vote is in April (April 14 in 2026), the day before the notice deadline; in 2025 the board set its cut list on April 14. Board policy GCPA defers to the bargaining agreements (raw/money/policies/policy-GCPA.*). Raw: raw/money/contracts/cea-2026-2029.ocr.txt
11. For paraprofessionals and other CESP staff, the district decides reductions "primarily on the basis of ability and performance of duty" (averaging the last two years of evaluations), then by seniority within the classification, with the least senior laid off first and a one-year recall list.
   - citation: CESP Agreement 2025–2028, Article XI (Reduction in Personnel, Layoff, and Recall)
   - source: https://files.smartsites.parentsquare.com/10271/cesp_agreement_2025-2028_revised_w_sidebar.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The District reserves and shall have the right to decide who shall be reduced (Reduction in Force, 'RIF'), primarily on the basis of ability and performance of duty ... Within that classification, reductions shall be governed by seniority. 12.2 If seniority is the determiner, the person with the least seniority in the District will be laid off first ... kept on a recall list for a maximum of one (1) year." Laid-off staff may keep health and dental coverage through August. Raw: raw/money/contracts/cesp-2025-2028.ocr.txt
12. Since summer 2024 Conway has run a new-teacher program that begins with a three-day onboarding "bootcamp" before school (goal setting and instructional practice), followed by a year-long cohort with monthly meetings in each building led by "new teacher champions" chosen by principals, and three district-wide meetings a year.
   - citation: Conway School Board Minutes, August 26, 2024 and October 15, 2024 (item i)
   - source: https://drive.google.com/file/d/1f4w32hCtw_BwGWEjXDQdvFEHA767AKgH/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: October text: "this was a result of restructuring the new teacher mentor program. In the past, new teachers were assigned a one-on-one mentor ... During the summer we held a 3-day bootcamp/onboarding to do goal settings and instructional practice. Over the course of the year each building identifies their new teacher champions ... All the new teachers and mentors meet here 3 times a year". August 2024 URL: https://drive.google.com/file/d/10hNbs7-OkM-k7V9aMOcaBhX0cp2oGoP4/view. These are Conway School Board records; no SAU-wide version was found. Raw: raw/money/minutes/csb-2024-10-15.*, csb-2024-08-26.*
13. The new-teacher onboarding was first paid with grant funds and was to become a yearly local budget item, and the board approves extra paid hours for new hires and their mentors each year (5-1-0 on August 24, 2026); the 2026 mentor program began August 25, 2026.
   - citation: Conway School Board Minutes, January 22, 2024; August 24, 2026 (items 6k and 12a)
   - source: https://drive.google.com/file/d/1kz1OvzV0GaV1zk6OObfPtIQLsX7klagk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: 2024 text: "Grant funds will be utilized for the onboarding of new teachers this year, but it will become an annual budget item with a varying ask based on the current salaries and the number of participants." 2026 text: "Consider Approval of Hours for Additional New Teacher Hires & Their Mentors 5-1-0 [Mosca]"; "The mentor program for new teachers starts on August 25th." Mosca voted no because the amount was not stated. January 2024 URL: https://drive.google.com/file/d/1M67agCWbQMatoGTYOQ9vuOQ8vteqkoHr/view. Raw: raw/money/minutes/csb-2024-01-22.*, csb-2026-08-24.*
14. The CEA agreement reimburses teachers for up to 12 graduate credits a year at no more than the UNH graduate rate, from a $75,000 pool split $35,000 (summer), $20,000 (fall) and $20,000 (spring); teachers must stay two years or repay it, and the budget must also fund other professional development distributed by principals.
   - citation: CEA Agreement 2026–2029, Article XX (Course Reimbursement), 20-1 and 20-2
   - source: https://files.smartsites.parentsquare.com/10271/cea_agreement_2026-2029_with_signatues.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "with a pool not to exceed $75,000 based upon budgeted trimesters ... The teacher will be required to stay in the district for two (2) years or reimburse the district"; "20-2 The budget presented to the voters of the district will provide funds for professional development beyond course work. The building principal shall distribute and approve funds." Article 5-4 says mentors are not responsible for evaluation. Teachers on an improvement plan are not eligible. Raw: raw/money/contracts/cea-2026-2029.ocr.txt

## district-tax-and-state-aid: Conway's School Tax, Revenue Mix and State Aid

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. For 2026-27 the district estimated that the local school tax (district assessment) would pay 54% of its operating appropriation, sending-town tuition 27%, the statewide education tax 9%, the state adequacy grant 4%, grants 4% and other sources 2%.
   - citation: Conway Annual Report (FY2025), "Conway's Total Estimated 2026-2027 Operating Appropriation," p. 18
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Pie chart viewed (raw/money/annual-reports/ar-fy2025-p21.png): "Conway District Tax 54% ... Sending Town Tuition Pmt. 27% ... NH Education Tax 9% ... NH Adequacy Grant 4% ... Expendable Grants 4% ... State and Federal Sources 1% ... Non-Conway Revenue 1% ... Fund Balance 0%". The revenue page gives the district assessment as $22,764,447 (estimated 2026-27) against $23,735,207 (2025-26). Raw: raw/money/annual-reports/ar-fy2025.*
2. Conway's annual report lists a state adequacy grant of $2,603,652 for 2024-25 and estimates $2,265,372 for 2025-26 and $1,786,171 for 2026-27, the last marked "95% 11/15/25."
   - citation: Conway Annual Report (FY2025), Estimated Revenues 2026-2027, p. 17
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Revenue page (viewed): "State of NH Adequacy Grant $2,603,652 $2,265,372 $1,786,171 ** 95% 11/15/25". The amounts equal NH DOE's grants in the site's data (adequacy_aid, Conway district): $2,603,651.86 (FY2025), $2,265,371.51 (FY2026) and $1,786,171.26 (FY2027, October 1, 2026 calculation). The site's data also has the full calculation and the grants Conway reported on its DOE-25 ($3,740,927.99 for FY2023; $2,603,651.86 for FY2024 and FY2025). How the grant is calculated is library topic money-adequacy-grant-calculation. Raw: raw/money/state-data/site-db-conway-queries.txt; raw/money/annual-reports/ar-fy2025-p20.png
3. The district estimated in February 2026 that the operating budget would need a local school rate of about $6.83 per $1,000 and that all proposed articles together would bring the 2026 school rate (local plus state) to about $8.74, $0.51 above the 2025 rate of $8.23.
   - citation: Conway Deliberative Session packet, March 2, 2026, "Conway School District Estimated School Tax Rate Information," PDF page 25
   - source: https://drive.google.com/file/d/1izkln4SJ-BQ38ATxoTyYIq6GBExmgZsx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page text (OCR, layout jumbled): "$6.83 Per $1000 (Estimate) ... $8.74 Per $1000 (Estimate) $0.51 Per $1000 (Estimate) ... $7.12 $1.11 $8.23 ... NOTE: ESTIMATE BASED ON 2025 NET ASSESSED VALUATION". The 2026 DRA rate for Conway had not been found as of November 13, 2026. Conway's DRA rates for 2014–2025 are in the site's data (property_tax, Conway district); its 2025 local school rate of $7.12 plus state education $1.11 give the $8.23 here (checked November 15, 2026). Raw: raw/money/packets/dp-2026.ocr.txt
4. At the 2025 deliberative session a resident said Conway's taxpayers fund "about 50%" of what voters approve because grants and sending-town tuition offset the rest, and a budget committee member said the school's local tax rose from $19 million to $22.3 million for that year.
   - citation: Conway Deliberative Session Minutes, March 5, 2025, Article 6
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Minutes text (Amy Snow): "when we approve a budget, it is offset by grants, it is offset by tuition contracts from the sending towns and our tax burden is about 50% of what we are voting on"; (Bill Marvel): "the amount that Conway has to pay for through property taxes - that rose from $19M last year to $22.3M this year." Statements as recorded. The site's data (property_tax, Conway district) has DRA's local school tax for Conway: $17,196,486 (tax year 2023), $20,356,634 (2024) and $23,735,207 (2025); the speakers' figures were made before the 2025 rate was set (checked November 15, 2026). Raw: raw/money/deliberative/dm-2025.ocr.txt

## district-tuition-contracts: Tuition From Sending Towns, Seen From Conway's Side

- kind: local
- question_type: governance_money
- description: A district's tuition contracts and agreements with other districts and schools: terms, cost formulas, caps, length, renewal, transportation and special education

1. Conway's tuition revenue from other New Hampshire districts was $9,745,984 in 2024-25, after $10,449,888 in 2023-24 and a high of $10,696,918 in 2021-22, by its DOE-25 reports; the district estimated $10,676,961 for 2025-26 and $11,571,058 for 2026-27.
   - citation: site data (DOE-25 revenue account 1321, Conway, FY2010–FY2025); Conway Annual Report (FY2025), Estimated Revenues 2026-2027, p. 17
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Query rows: "2025 | 1321 | Regular Day School (Within NH) | 9745984.00"; "2022 ... 10696918.34". Revenue page (viewed): "Sub Total Tuition $9,745,987 $10,676,961 $11,571,058" (the $3 difference from DOE-25 is as printed). See table conway_tuition_revenue. Raw: raw/money/state-data/site-db-conway-queries.txt; raw/money/annual-reports/ar-fy2025-p20.png
2. Of that tuition, high school operations brought $6,851,664 in 2024-25 and an estimated $7,442,773 (2025-26) and $8,337,794 (2026-27); middle school $1,887,454 and elementary $835,642 in 2024-25, with smaller amounts for elementary bond and maintenance-trust shares and non-contract students.
   - citation: Conway Annual Report (FY2025), Estimated Revenues 2026-2027, p. 17
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed: "Tuition - Regular Education Elem Operations $835,642 $1,125,016 $1,020,277 / Tuition - Regular Education Middle Sch Operations $1,887,454 $1,962,960 $2,113,957 / Tuition - Regular Education High Sch Operations $6,851,664 $7,442,773 $8,337,794". Elementary tuition comes from Albany, Eaton and Hale's Location (K–6 contracts on SAU 9's tuition page). Albany's K–6 contract posted there is the 2026–2034 contract, with its own formula (town/Albany/money-and-governance.md, district-tuition-contracts; added November 13, 2026). Raw: raw/money/annual-reports/ar-fy2025-p20.png, ar-fy2025.ocr.txt
3. Under the current Kennett contracts each sending district pays a share of the high school's operating cost set 65% by its share of attendance and 35% by its share of the towns' equalized property value; for 2019-20 Conway had 48.74% of the attendance and 34.71% of the property value, for a combined 43.8295% of the operating budget.
   - citation: SAU 9 Study Committee Presentation, February 28, 2019, slide 19; Conway Tuition Agreement (Bartlett and Jackson, 9-12), Section X.A.3 (Bartlett file district-tuition-contracts fact 2)
   - source: https://drive.google.com/file/d/17rVLU-Ui99yNkgX6qk1FnXa93mS0MpIc/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Slide text: "ADM % EQ Val% Combined % / Conway 48.74% 34.71% 43.8295% / Eaton 0.34% ... Bartlett 12.08% 22.56% 15.748% / Jackson 3.67% 8.68% 5.4235% / Tamworth 12.79% 7.87% 11.068% / Operating Budget Only". Raw copy is in the Jackson research: town/Jackson/raw/money/study/study-committee-presentation-2019-02-28.txt
4. Because Conway's share of the towns' property value (34.71%) was smaller than its share of Kennett students (48.74%), the 35% value weighting made Conway's 2019-20 share of the operating charge (43.83%) about 4.9 points lower than its attendance share, and the sending towns' combined charge (56.17%) higher than their attendance share (51.26%) (**derived** reading).
   - citation: SAU 9 Study Committee Presentation, February 28, 2019, slide 19
   - source: https://drive.google.com/file/d/17rVLU-Ui99yNkgX6qk1FnXa93mS0MpIc/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Derived: 48.74 − 43.83 = 4.91; 100 − 48.74 = 51.26; 100 − 43.83 = 56.17. This is one year's formula outcome; no later share table was found. Bond payments and the maintenance fund were shared by property value alone. No source calls this a subsidy either way. Raw: town/Jackson/raw/money/study/study-committee-presentation-2019-02-28.txt
5. Conway's 2027–2032 contracts with Albany, Bartlett and Eaton set each town's charge from Conway's most recent DOE-25 costs and attendance (ADMA) for the school level, plus the Northeast urban CPI plus 2.5% capped at 8% a year, and Jackson's 2027 contract uses CPI plus 13% capped at 20%; none uses property value.
   - citation: Albany/Conway Tuition Agreement, Grades 7-8 (2027), Section VIII.A.1–2; Albany and Eaton 9-12 (2027) contracts; Bartlett file district-tuition-contracts fact 6; Jackson file district-tuition-contracts 8 in `Jackson/money-and-governance.md`
   - source: https://drive.google.com/file/d/1VJ2HlQZZYMXnHHPuZ455HJuzTVO5DOW5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The Conway School Board shall annually set Albany's cost based upon Conway's most recent DOE 25 and ADMA, plus an inflation factor equal to US Department of Labor Consumer Price Index - Size A - Northeast Urban (October of current year) plus 2.5%. CPI plus 2.5% shall not exceed eight percent (8%) in any given year." Costs exclude maintenance trust spending and billable special education. State Board approval of the Albany 7-8 contract: September 10, 2026. Albany and Eaton 9-12 OCR is in the Kennett agent's raw folder (town/sau9/raw/contracts/). Raw: raw/money/contracts/contract-7-8-albany-conway-2027.pdf, .ocr.txt
6. Under the 2027 contracts each sending town also pays one-fifth of its attendance-based share of a five-year capital plan for the school into Conway's maintenance trust; on the current tuition articles, sending towns pay $35,158 of the $54,443 Kennett High maintenance deposit (65%) and $7,287 of the $17,086 middle school deposit (43%) (**derived** shares).
   - citation: Albany/Conway Tuition Agreement (7-8, 2027), Section VIII.B.1; Conway ballot April 14, 2026, Articles 2–3
   - source: https://drive.google.com/file/d/14no6-JNdH3d4DmzmXRTwjErl-VWuFujx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Contract text: "Each sending district shall annually pay one-fifth (1/5th) of the projected five- (5-) year CIP plan based on Appendix B. Calculation of the sending district share shall be based on each district's ADMA for the prior year." Ballot: "$54,443 ... with $35,158 to offset this amount from the sending towns"; "$17,086 ... with $7,287". Derived: 35,158 ÷ 54,443 = 64.6%; 7,287 ÷ 17,086 = 42.6%. Raw: raw/money/contracts/contract-7-8-albany-conway-2027.ocr.txt; raw/money/elections/er-2026.txt
7. In March 2026, 313 of Kennett High School's 600 students lived in Conway (52%), and the rest came from Bartlett (69), Madison (68), Tamworth (68), Freedom (28), Albany (23), Jackson (20), Eaton (10) and elsewhere (1) (**derived** share).
   - citation: Conway Annual Report (FY2025), "Conway School District Enrollment (as of March 2026)," p. 30
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/annual-reports/ar-fy2025-p33.png): "Conway 394 222 313 929 ... TOTAL 432 297 600 1329". Derived: 313 ÷ 600 = 52.2%. At Kennett Middle School, 222 of 297 were from Conway, with Madison 31, Albany 17, Freedom 13 and Eaton 8. Excludes reported homeschooled students. Madison's own October 2026 count is 38 at KMS (21 in grade 7, 17 in grade 8) and 69 at Kennett (town/Madison/kennett-for-madison.md, school-programs-after-grade-6 2; added November 13, 2026). See table conway_kennett_enrollment_by_town. Raw: raw/money/annual-reports/ar-fy2025.* Added November 13, 2026: Freedom's own October 1, 2026 count is 14 at KMS (8 in grade 7, 6 in grade 8) and 25 at Kennett High (town/Freedom/getting-to-school-and-kennett.md).
8. Conway has no 2027 contracts yet with Madison, Freedom and Tamworth (SAU 13); in April 2026 the board chair removed Randy Davison from the tuition negotiating committee after letters from sending towns, and in November 2026 board members said SAU 13 had presented a tuition contract with Governor Wentworth (Kingswood) and Madison planned to present Conway's offer to its voters.
   - citation: Conway School Board Minutes, April 13, 2026 (item 14b) and June 22, 2026; Special Meeting (Budget Review) Minutes (draft), November 5, 2026
   - source: https://drive.google.com/file/d/1wmAAoTaWde1BbK4VjqOrnspG5VRaT1af/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: April text: "He noted the desire to have a contract with all SAU13 towns. He removed Randy Davison from the Tuition Negotiating Committee"; "Davison suggested in a conversation that Madison and Freedom should continue speaking with Kingswood instead of Conway, as Conway would be more expensive." November text: "on Monday night, SAU #13 presented a tuition contract with Governor Wentworth ... Madison plans to present Conway's offer to their community." SAU 9's tuition page lists 2027 contracts only for Albany, Bartlett, Eaton and Jackson. Raw: raw/money/minutes/csb-2026-04-13.*, csb-2026-06-22.*, csb-2026-11-05-special-draft.* Added November 13, 2026: Tamworth's own minutes record its February 15, 2024 vote to give notice ending its contract in 2027, and Conway's 2026-27 charge of $1,549,098 for 76.61 Tamworth students (town/Tamworth/money-and-governance.md); Madison voted not to renew on February 5, 2024 and Freedom on February 12, 2024 (their money files). Freedom already has an agreement with Governor Wentworth approved August 11, 2025, and in October 2026 was still negotiating with Governor Wentworth, Moultonborough, Fryeburg and Conway (town/Freedom/money-and-governance.md, district-tuition-contracts 12 and 15).
9. Planning the 2027-28 budget in November 2026, board members discussed how to budget tuition revenue without knowing whether SAU 13 students will attend, with one suggesting estimating tuition at 50% of total enrollment, and the board chair said "Conway is taking on more responsibility for tuition with the new formula."
   - citation: Conway School Board Special Meeting (Budget Review) Minutes (draft), November 5, 2026
   - source: https://drive.google.com/file/d/1nnBOX0aNn_Toc_nQQllAc-taAjVlwl6T/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Brittany Hodge feels that we cannot budget assuming that all students will attend. Brittany Hodge suggested that we anticipate tuition revenue at 50% of total enrollment"; "Additionally, Conway is taking on more responsibility for tuition with the new formula." The business administrator said grade 6 costs are kept in a separate unit (Unit 6) for tuition purposes because shared middle school costs are split by student count. Draft minutes. Raw: raw/money/minutes/csb-2026-11-05-special-draft.*
10. When Conway returns unspent year-end money, it lowers Conway's tax rate while tuition is adjusted separately: the business administrator said in October 2025 that fund balance "goes to Conway, but adjustments for tuition agreements are made to sending towns," and the board voted that month to return all of the FY2025 unspent balance ($539,011) to taxpayers.
   - citation: Conway School Board Minutes, October 27, 2025; Conway Deliberative Session packet, March 2, 2026, Executive Summary, p. 6
   - source: https://drive.google.com/file/d/1igOXkZ6Y49Su6Efk6vOoY-P1G1cPd-32/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Minutes text: "Randy Davison asks what happens if funds are given back? Does that go to Conway tax rate or back to sending towns? Mike Wade explains that it goes to Conway, but adjustments for tuition agreements are made to sending towns." Packet: "FY25 budget had an unexpended balance of $539,011. In October 2025, the Conway School Board voted to return all of the unexpended fund balance back to the taxpayer." In April 2024 voters defeated (787–940) an article to let the district retain up to 5% of year-end balance. Raw: raw/money/minutes/csb-2025-10-27.*; raw/money/packets/dp-2026.ocr.txt; raw/money/elections/er-2024-p2.png

## district-facilities-and-capital: The John Fuller Building, the KMS Capital Plan and Trust Funds

- kind: local
- question_type: governance_money
- description: A district's school buildings: age, planned repairs, capital reserve funds, bonds and energy projects

1. John H. Fuller School in North Conway closed after the 2023-24 school year: the board voted 7-0-0 on April 17, 2024 to close it for fall 2024, a year earlier than planned, after voters rejected the operating budget; board member Randy Davison cited the building's age, the master plan, community emails and growth in Center Conway and along West Side Road.
   - citation: Conway School Board Special Meeting Minutes, April 17, 2024
   - source: https://drive.google.com/file/d/1gwy8LjjAtQWS7FIow4n_MwSdf6o8Bmds/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Mr. Davison discussed his reasoning for choosing John Fuller School which included the age of the building, the master plan, community emails, and growth within Center Conway and along West Side Road." In April 2023 a non-binding petitioned article to close one of the three elementary schools by 2024-25 failed 754–816 (raw/money/annual-reports/ar-fy2023.ocr.txt). In January 2024 the administration's closure report had recommended closing a school in September 2025 (raw/money/minutes/csb-2024-01-22.txt). Raw: raw/money/minutes/csb-2024-04-17-special.*
2. Conway's FY2026 adopted budget carries $181,561 for operating and maintaining the Fuller building (Unit 6, function 2620) and $11,500 for its grounds, $193,061 in all (**derived**), against $375,634 actually spent in 2023-24 when it was a school; the largest 2025-26 lines are contracted repairs ($52,450), heating fuel ($42,000), electricity ($20,000) and repairs ($19,500).
   - citation: Conway FY26 Adopted Budget, Unit 6, accounts 41-06-2620 and 41-06-2630, p. 52
   - source: https://drive.google.com/file/d/135rQbusiABGRcazlm3fsuTjlvVyAd0Ag/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/budget/fy26-adopted-p52.png): "TOTAL 2620 OPERATION/MAINTENANCE PLANT SERVICES $ 385,755 $ 364,863 $ 181,728 $ 181,561"; "TOTAL 2630 OPERATION/MAINTENANCE GROUNDS $ 18,000 $ 10,771 $ 11,500 $ 11,500" (FY24 adopted, FY24 actual, FY25 adopted, FY26 adopted). Unit 6 is the former John Fuller unit; in 2025-26 it also holds the grade 6 teachers now at Kennett Middle School ($824,676 total; p. 46, raw/money/budget/fy26-adopted-p46.png). A resident asked in January 2026 for a separate unit "so we know what is being spent at the empty school" (raw/money/minutes/csb-2026-01-12.txt). No document gives actual 2024-25 or 2025-26 building spending. Raw: raw/money/budget/fy26-adopted.pdf, .txt
3. The "$120,000 a year" figure for the Fuller building was not found in Conway's budgets, minutes or reports; the closest figures are the $193,061 budgeted for building operation and grounds in 2025-26 (fact 2), bond payments of $128,295 in FY2026 (fact 4), and the superintendent's June 2025 estimate that heating the building costs about $50,000 a year when occupied.
   - citation: Conway FY26 Adopted Budget; John Fuller Ad Hoc Committee Listening Session Minutes, June 30, 2025
   - source: https://drive.google.com/file/d/1kA5EHaWHls9V8MjZS-vgMMTXelBMkm8C/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Listening session text: "The debt repayment at the ten year call date on the bond itself is $1,157,982 and an approximate heating cost when the heating is occupied is: $50K – that's annually." Bond payments continue whether or not the building is used. In April 2025 a board member said "We are spending quite a bit of money there every month" (raw/money/minutes/csb-2025-04-14.txt). A statement about the documents searched. Raw: raw/money/fuller/jf-2025-06-30-listening.*; raw/money/budget/fy26-adopted-p52.png
4. Conway still pays a $1,837,000 NH Municipal Bond Bank bond dated July 14, 2016 that its annual report labels "John Fuller Building," with $2,505,483.59 of total debt service ending August 15, 2036; FY2026 payments were $128,295 and FY2027 payments are $118,651.50.
   - citation: Conway Annual Report (FY2025), "Bond Debt Service (John Fuller Building)," pp. 31–32
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "BOND DEBT SERVICE (John Fuller Building) New Hampshire Municipal Bond Bank Conway School District (6/30 YE) Dated Date 07/14/2016"; "6/30/2026 128,295.00"; "6/30/2027 118,651.50"; "8/15/2036 90,000.00 3.020% 1,359.00 91,359.00 ... 1,837,000.00 667,783.59 2,505,483.59". In April 2025 the superintendent said the district would owe $1,157,982.75 at the 10-year call date in August 2026, and in January 2026 the business administrator gave remaining payments as $1,286,000 with interest (raw/money/fuller/jf-2025-04-09.txt, jf-2026-01-21.txt). Transcribed from image (OCR). Raw: raw/money/annual-reports/ar-fy2025.ocr.txt
5. The 2016 loan agreement barred Conway from paying off the Fuller bond before its 10-year call date and from changing its tax-exempt status before then, so a private sale was not an option before 2026; the superintendent said in 2026 that long-term or regular use of the building must be limited to non-profits to protect the tax-exempt status.
   - citation: John Fuller Ad Hoc Committee Listening Session Minutes, June 30, 2025; John Fuller Ad Hoc Committee Minutes, March 25, 2026
   - source: https://drive.google.com/file/d/1kA5EHaWHls9V8MjZS-vgMMTXelBMkm8C/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: 2025 text: "Loan agreement was signed in 2016 at the time of the sale, which also stated the District would not redeem or pay off the bond prior to that call date ... the District would not change or alter the tax exemption status of the bond until the 10-year mark." (The minutes misstate the year as "2016" where 2026 is meant.) 2026 text: "any long-term/regular use needs to be limited to non-profits only, as anything longer term would potentially place us in violation of the tax-exempt bond status." In August 2026 the superintendent reported bond counsel's preliminary advice that subdividing the land does not affect the bond's status (raw/money/minutes/csb-2026-08-10.txt). March 2026 URL: https://drive.google.com/file/d/123zzej8ksbH101LnMN2gEzob_50vgJ8N/view. Raw: raw/money/fuller/jf-2025-06-30-listening.*, jf-2026-03-25.*
6. New Hampshire law gives a school district, as a corporation, power "to hold and dispose of real and personal property for the use of the schools therein"; the statute does not say whether the school board or the voters must approve a sale.
   - citation: RSA 194:2
   - source: https://gc.nh.gov/rsa/html/XV/194/194-2.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Conway
   - note: Statute text: "All districts legally organized shall be corporations, with power to sue and be sued, to hold and dispose of real and personal property for the use of the schools therein, and to make necessary contracts in relation thereto." RSA 194:3 (powers of districts) lists building, buying, renting and repairing schoolhouses but not selling. The brief's premise that the district meeting must decide a sale could not be confirmed from the statutes read; see Not retrieved. Raw: raw/money/rsa/rsa-194-2.*, rsa-194-3.*
7. If a district offers an "unused facility" for sale or lease to anyone other than a chartered public school, the contract must be subject to a 60-day right of first refusal for any approved New Hampshire charter school, and a charter school may itself start good-faith purchase or lease negotiations; a building is "unused" if it has no academic, extracurricular, administrative or sports use and no board-approved plan for such use within 2 years.
   - citation: RSA 194:61
   - source: https://gc.nh.gov/rsa/html/XV/194/194-61.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Conway
   - note: Statute text: "the contract shall include a provision which makes the purchase or lease subject to the right of first refusal by an approved chartered public school operating in this state"; "the expiration date of the right of first refusal which shall be 60 days after the date of the notification to the charter school administrator"; superintendents report unused facilities to NH DOE each July 1. Conway's board and committee discussed this rule in 2024–2026 (raw/money/minutes/csb-2024-09-23.txt: "They have a right of first refusal to match that"; raw/money/fuller/jf-2025-06-30-listening.txt). Whether John Fuller is on DOE's unused-facilities list was not found. Raw: raw/money/rsa/rsa-194-61.*
8. Since October 8, 2026, closing or moving an elementary or high school requires a majority vote of voters in all towns the school serves, and the town where it sits may then vote to keep running it; John Fuller was closed in 2024, before this law, by a school board vote.
   - citation: RSA 194:3-f and 194:3-g (2026, 303:3, eff. Oct. 8, 2026); library topic gov-school-closure-votes
   - source: https://gc.nh.gov/rsa/html/XV/194/194-3-f.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Conway
   - note: Statute text: "No elementary school ... or high school ... shall be discontinued, or the location thereof be changed, except by a majority vote of voters residing in all municipalities that are served by the school or district." The law governs closing schools, not selling closed buildings. Conway policy FL sets the board's own closing-study steps, including "Alternate uses of the building" and "Costs/savings" (raw/money/policies/policy-FL.*). Raw: raw/money/rsa/rsa-194-3-f.*, rsa-194-3-g.*
9. The Conway School Board set up a John Fuller Ad Hoc Committee on September 9, 2024; it issued a request for proposals to lease, buy or use the building (3 proposals were received by mid-2025, including from Robert Frost Charter School), held a public listening session on June 30, 2025, and had the property appraised by Bergeron Commercial Appraisal.
   - citation: John Fuller Ad Hoc Committee Listening Session Minutes, June 30, 2025; Conway School Board Minutes, September 8, 2025 (item D)
   - source: https://drive.google.com/file/d/1kA5EHaWHls9V8MjZS-vgMMTXelBMkm8C/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "On September 9, 2024, the Conway School Board established this ad hoc committee ... we put out a request for proposals for the lease, sale or use of the vacant building as an exploratory exercise. We've received 3 proposals." September 2025: "Randy Davison made a motion to authorize the appraisal of John Fuller School, seconded by Matt Stearns, 7-0-0." The committee found the Robert Frost proposal "not ... a viable option at this time" in May 2026 (raw/money/fuller/jf-2026-05-13.txt). Raw: raw/money/fuller/jf-2025-06-30-listening.*; raw/money/minutes/csb-2025-09-08.*
10. Bergeron's appraisal put the John Fuller property's value at about $1,880,000, with an estimated market value of $1,950,000 depending on use; a committee member said the appraisal's highest and best use was demolishing the building and selling the land, and the superintendent said the demolition estimate "seems quite low."
   - citation: John Fuller Action Ad Hoc Committee Minutes, January 21, 2026, item 4
   - source: https://drive.google.com/file/d/1sDeO902Mj9--T1Iy0LSBs1PpNuoZqo_f/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "the bottom line number they concluded for worth, which was approximately 1,880,000 with an estimated market value of $1,950,000 depending on the use, demolition of the building, etc. ... Harrison Kanzler clarified that the highest and best use of the building is the demolition of the building and a sale of 1.8 million dollars." In April 2026 a board member cited a $3.5 million value from the Town Report (raw/money/minutes/csb-2026-04-13.txt). The appraisal itself was not found online. Raw: raw/money/fuller/jf-2026-01-21.*
11. On January 26, 2026 the Conway School Board voted 5-1 (Davison opposed) that the John Fuller property be retained and not sold and be used, leased or made available for educational or administrative purposes, and 5-1 to reconstitute the committee to find uses, amended so that the building, not the whole property, would not be sold.
   - citation: Conway School Board Minutes, January 26, 2026, item f
   - source: https://drive.google.com/file/d/19F4UB84J4HkJQMQrWE5-jt6YOroDppEu/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Motion was made by Matt Stearns and seconded by Mike DiGregorio to consider the recommendation that the John Fuller school property be retained by the Conway School District and shall not be sold ... Motion carried 5-1 [Davison]-0"; "Matt Stearns amended the motion to indicate that the building, not the property, not be sold." The committee had recommended this 8-2-0 on January 21, 2026. Scanned; transcribed from image (OCR). Raw: raw/money/minutes/csb-2026-01-26.pdf, .ocr.txt
12. In 2026 the Fuller committee explored a YMCA (a community group was raising money for a feasibility study, not the school district), health-care use with federal Rural Health Transformation funds through White Mountain Community Health Center, and pre-K and child care, and on August 10, 2026 the board voted 6-0-0 to let the committee write a request for proposals for deed-restricted affordable housing on a subdivided parcel.
   - citation: John Fuller Action Ad Hoc Committee Minutes, May 13, July 29 and August 19 (draft), 2026; Conway School Board Minutes, August 10, 2026, item 11a
   - source: https://drive.google.com/file/d/1IZd9El6tsAhuYjLnqj199422kdbBbDwa/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Board text: "Motion was made by Sarah Burke and seconded by Brittany Hodge to allow the John Fuller Ad Hoc Committee to develop an RFP to solicit responses around the development of this parcel for deed-restricted, affordable housing. 6-0-0." A housing coalition sketch fit 16 units on 2.2 of the property's acres (raw/money/fuller/jf-2026-01-21.txt). August committee text: "the School Board is not funding anything at this point." Raw: raw/money/minutes/csb-2026-08-10.*; raw/money/fuller/jf-2026-05-13.*, jf-2026-07-29.*, jf-2026-08-19-draft.*
13. As of October 22, 2026 the Fuller committee had paused: members said the town's talk of extending the North-South Road through the area affects options such as housing, no further work on the housing RFP could be done until the full board gave direction, the committee chair proposed dissolving the committee and moving its subgroups to the full board's agenda, and one member resigned.
   - citation: John Fuller Action Ad Hoc Committee Minutes (draft), October 22, 2026
   - source: https://drive.google.com/file/d/1upcA11Mr_QYYIutS7QibeJ48OhbWTkVC/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Brittany Hodge asked to discuss the town's conversation to extend the North South Road and its impact on the JFS property ... we made a recommendation to the full Board not to sell the property and develop an RFP for affordable housing, on which no further work can be done ... Brittany Hodge feels that the three subgroups plus the housing element needs to be added as agenda items on the full Board agendas and that this committee should be dissolved." Draft minutes; no quorum. Raw: raw/money/fuller/jf-2026-10-22-draft.*
14. No source read measures whether the John Fuller debate has affected home buyers or prices in North Conway Village; the records show only the board's decision to keep the building, the uses under study and the town's road discussion.
   - citation: John Fuller committee and Conway School Board minutes, December 2024–October 2026
   - source: https://drive.google.com/drive/folders/10iiGWRpQQ6bfm25p-klu10euBGbPGLRv
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: A statement about the documents searched. Neighbors spoke at committee meetings about traffic and abutters (raw/money/fuller/jf-2026-01-21.txt). Home sales data for Conway are in the Jackson research's housing folder (NHAR market updates), not read for this question. Raw: raw/money/fuller/
15. A five-year capital plan for A. Crosby Kennett Middle School, attached to the 2027 middle school tuition contracts, totals $4,502,107 for FY2027–FY2032, including five rooftop units ($655,000), an energy recovery unit ($95,000) and two air handlers ($150,000) in 2028, roof sections in 2027–2030, boilers, pumps and trim ($1,800,000) in 2031 and domestic hot water ($300,000) in 2032.
   - citation: Albany/Conway Tuition Agreement, Grades 7-8 (2027), Appendix B, "CIP Plan - Kennett Middle School"
   - source: https://drive.google.com/file/d/1VJ2HlQZZYMXnHHPuZ455HJuzTVO5DOW5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (rotated, raw/money/contracts/contract-7-8-albany-conway-2027-p8.png): "RTU's (x5) 2005 15 2020 655,000.00"; "Boilers - Pumps & Trim 2005 ... 1,800,000.00"; "Domestic Hot Water ... 300,000.00"; yearly totals "136,544.00 900,000.00 98,432.00 1,403,675.00 1,800,000.00 300,000.00 4,502,107.00". The Facilities Committee approved this plan "as the CIP that accompanies the middle school tuition contracts" on August 10, 2026, 2-0-0 (raw/money/facilities/fac-2026-08-10.txt). See table conway_kms_capital_plan. Raw: raw/money/contracts/contract-7-8-albany-conway-2027.*
16. Kennett Middle School's curtain wall and concrete repair, bid three times, was awarded in April 2025 for $590,990 against an original estimate of $350,000 and paid from the maintenance trust, with $21,094 more for deeper window frames; roof sections K and L next to it were replaced in 2026, with up to $200,000 approved from the general maintenance trust.
   - citation: Conway Facilities Committee Minutes, April 22, 2025, August 21, 2025 and April 30, 2026
   - source: https://drive.google.com/file/d/1gm_9xUMUUYN16c4wCFdLuO_6ha690HUf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: 2025 text: "This is the third time it has gone out to bid. It was originally estimated to cost $350,000 and came in at $590,990." 2026 text: "The lowest bid was from Rodd Roofing ... there is not enough money in the middle school maintenance trust fund, so funds would come from the general maintenance trust fund ... Joe Mosca made a motion to take up to $200,000 out of the general maintenance fund ... 3-0-0." The CIP lists sections K, L and P as replaced in 2026. Raw: raw/money/facilities/fac-2025-04-22.*, fac-2025-08-21.*, fac-2026-04-30.*
17. More roof sections and the rooftop units at Kennett Middle School are planned for summer 2027, and the superintendent's FY2028 capital update (November 2026) lists middle school roofs and two middle school rooftop units, the Pine Tree rotating maintenance fund and no major projects at Conway Intermediate.
   - citation: Conway Facilities Committee Minutes, August 10 and November 12 (draft), 2026; Conway School Board Special Meeting (Budget Review) Minutes (draft), November 5, 2026
   - source: https://drive.google.com/file/d/1nnBOX0aNn_Toc_nQQllAc-taAjVlwl6T/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Board text: "Aimee Frechette shared an update on facilities FY28 capital improvement plan including middle school roofs, and two middle school rooftop units. PTPS will have the rotating maintenance fund. There are no major projects slated for CIS." Facilities text (August 10): "Roofing and RTU's - To be replaced in Summer 2027 ... He will also look into going from two rooftop units to one". The November 12 draft says the bid had not yet gone out. Raw: raw/money/minutes/csb-2026-11-05-special-draft.*; raw/money/facilities/fac-2026-08-10.*, fac-2026-11-12.*
18. In March 2025 Siemens gave Conway updated capital plans for John Fuller, Mountainside (Conway Intermediate), Kennett Middle and Kennett High, with one to follow for the K–2 building, to be combined into a master plan; the district says it keeps a five-year capital improvement plan projecting needs over five, ten and more years.
   - citation: Conway Facilities Committee Minutes, March 4, 2025, item 5; Conway Deliberative Session packet, March 2, 2026, p. 9
   - source: https://drive.google.com/file/d/1dbNxoUnp1xmzpnSGMyZeZjIUwdbM_hBd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Siemens provided Aimee and Mike with an updated CIP plan for JFS, Mountainside, KMS, and KHS and they will complete one for the Lakeside building. Aimee and Mike will add this to a master CIP plan." Packet: "The Conway School Board has a five year capital improvement plan that has been projecting long term facility needs over the next five, ten and more years." The master plan itself was not found online. The draft Kennett High plan for FY2028–2032 ($3,835,866.93) is in the Bartlett file (district-tuition-contracts fact 8). Raw: raw/money/facilities/fac-2025-03-04.*; raw/money/packets/dp-2026.ocr.txt
19. Conway's building and equipment trust balances in early 2026 (after approved projects) were $1,623,401 in the general School Buildings Maintenance Fund (set up 1995), $731,990 for Kennett High, $73,135 for Kennett Middle, $72,443 for the elementary schools and $344,439 in the bus and equipment reserve; voters added $1,000,000, $54,443, $17,086, $9,900 and $250,000 in April 2026.
   - citation: Conway Annual Report (FY2025), "Explanation of Conway School Board Warrant Articles 2026-27," pp. 6–7; election results April 14, 2026
   - source: https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Article 2 High School: $54,443.00 ... Current balance: $731,990"; "Article 9 ... The current balance: $1,623,401 **Includes reduction of approved projects"; "Article 8 ... The current balance: $344,439". In September 2026 the business administrator expected about $1.4 million left in the general fund after a Kennett field project and about $720,000 in the Kennett High fund (raw/money/facilities/fac-2026-09-24.txt). See table conway_trust_funds_2026. Raw: raw/money/annual-reports/ar-fy2025.ocr.txt; raw/money/elections/er-2026.*
20. In 2025 Conway moved to funding building maintenance partly from year-end surplus, at the sending towns' request in contract talks: voters approved $1,840,000 for the buildings trust (1,073 to 829) and up to $500,000 more from June 2025 fund balance (1,196 to 702), and a board member said earlier boards should have been setting aside "$2M-$3M a year."
   - citation: Conway Deliberative Session Minutes, March 5, 2025, Articles 9 and 12; election results April 8, 2025
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text (Mike DiGregorio): "the sending Towns have asked us to use the surplus money at the end of the year for maintenance projects ... prior to John Fuller closing down, the buildings that we had was about a half a million of square feet of buildings ... we should have been budgeting $2M-$3M a year we should have been budgeting 20 years ago". Results pages viewed (raw/money/elections/er-2025-p2.png, -p3.png). Raw: raw/money/deliberative/dm-2025.ocr.txt; raw/money/elections/er-2025.*
21. In April 2025 voters rejected, 421 to 1,493, $214,160 to design a relocation of Kennett High School's main entrance and office for security, which the school board had recommended 6-1-0 and the Municipal Budget Committee had not recommended 5-7-2.
   - citation: Conway election results, April 8, 2025, Article 11
   - source: https://drive.google.com/file/d/1ESXvMD9XByvg0fC3sJAQgd1YDDCcSzzP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/elections/er-2025-p3.png): "421 Yes / FAILED 1493 No". At the deliberative session a board member said moving the office to the rear entrance could cut the building to two entrances (raw/money/deliberative/dm-2025.ocr.txt). Raw: raw/money/elections/er-2025.*

## district-safety-and-security: Conway's Safety and Security Trust Fund

- kind: local
- question_type: local_practice
- description: Building security, visitor rules, drills and emergency plans, and school security grants

1. Conway voters created an expendable Safety and Security Trust Fund under RSA 198:20-c on April 8, 2025, "for the purposes of upgrades and maintenance of safety and security items and measures," with $100,000 and the school board as agents to spend it (1,149 to 753); a second article to add up to $500,000 from fund balance failed, 916 to 976.
   - citation: Conway election results, April 8, 2025, Articles 10 and 13
   - source: https://drive.google.com/file/d/1ESXvMD9XByvg0fC3sJAQgd1YDDCcSzzP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page viewed (raw/money/elections/er-2025-p3.png): "PASSED 1149 Yes / 753 No"; Article 13 "916 Yes / FAILED 976 No". Recommendations: Article 10 school board 7-0-0, Municipal Budget Committee 9-3-2; Article 13 school board 7-0-0, budget committee not recommended 6-7-1. Under RSA 198:20-c the board holds a public hearing before each expenditure (Bartlett file district-facilities-and-capital fact 12). Raw: raw/money/elections/er-2025.*
2. A school board member said at the 2025 deliberative session that the fund was meant to act on findings of a Department of Homeland Security audit of Conway's five buildings done about two and a half years earlier, with a new assessment due that spring, and that "$100K is not enough but is a pretty good start."
   - citation: Conway Deliberative Session Minutes, March 5, 2025, Article 10
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text (Matt Stearns): "Two and half years ago we had the Dept. of Homeland come in to do an audit on our 5 buildings. We have a subcommittee hard at work. They are coming back in the spring to do another assessment ... $100K is not enough but is a pretty good start". Opposing speakers called it a "bottomless pit" and preferred school resource officers. Statements as recorded. Raw: raw/money/deliberative/dm-2025.ocr.txt
3. Spending from the fund so far: $14,472 (September 2025) to secure Kennett High's front and rear doors, update cameras and the link to the front office; about $53,000 (February 2026) for district-wide radios and AI phones; and up to $61,469 (June 2026) for access controls at Conway Intermediate School and the middle school.
   - citation: Conway School Board Minutes, September 8, 2025; February 9, 2026; June 8, 2026
   - source: https://drive.google.com/file/d/1mA75b8gZp8UrD-Iok2RGDaXVMHI5j3z2/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Texts: "PUBLIC HEARING on Expenditure of Expendable Safety & Security Trust Fund ($14,472) ... secure Kennett High School front and rear doors including updating cameras and the communication system to the front office"; "This expenditure is for approximately $53,000 for radios and AI phones ... they would be used District-wide"; "authorize the expenditure of up to $61,469 for access controls at Conway Intermediate School and Conway Middle School. 7-0-0." September 2025 URL: https://drive.google.com/file/d/1iOTBzjjl1M2rwMgiwayVnez2COBebDUr/view; February 2026: https://drive.google.com/file/d/1pFMAlzk7u9FrxBkd-C6lIBcWYcPznesS/view. In September 2026 the Facilities Committee noted the AI phone at Conway Intermediate "is working well." Raw: raw/money/minutes/csb-2025-09-08.*, csb-2026-02-09.*, csb-2026-06-08.*
4. The fund's balance was $32,528 in early 2026 after approved projects, and voters added $150,000 on April 14, 2026 (981 to 618), recommended by the school board 5-0-0 and the Municipal Budget Committee 10-3-0.
   - citation: Conway Annual Report (FY2025), "Explanation of Conway School Board Warrant Articles 2026-27," p. 7; election results April 14, 2026, Article 11
   - source: https://drive.google.com/file/d/14no6-JNdH3d4DmzmXRTwjErl-VWuFujx/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Explanation text: "The Conway School Board and Safety and Security Committee recommends $100,000 be added to the Safety and Security Trust fund established in 2025 ... The current balance: $32,528 **Includes reduction of approved projects". The warrant and ballot amount was $150,000 ("raise and appropriate the sum of $150,000"); the explanation's $100,000 is copied as printed. Ballot page viewed (raw/money/elections/er-2026-p2.png). Raw: raw/money/annual-reports/ar-fy2025.ocr.txt; raw/money/elections/er-2026.*
5. At the elementary schools, the trust fund has paid for access controls at Conway Intermediate School; ADA access doors at Pine Tree Primary and Conway Intermediate were pending in November 2026, and the district also applied for state SAFE grants for items the Safety and Security Committee identified.
   - citation: Conway School Board Minutes, June 8, 2026 and November 10, 2025; Conway Facilities Committee Minutes (draft), November 12, 2026
   - source: https://drive.google.com/file/d/1PAXuct_BJ6nuEce2YtgtJSubAdVfyd5d/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: November 2025 text: "she will be applying for the grant specifically to purchase items that the Safety & Security Committee have identified as needs since that warrant article to use surplus funds into the Safety 7 Security fund did not go through. All we have in that fund is $100,000". Facilities agenda item: "ADA Access Doors (PTPS, CIS) - Update". Statewide SAFE grants are in the Jackson policies file. The Safety and Security Committee keeps a "rolling five-year plan" (raw/money/minutes/csb-2026-04-13.txt). Raw: raw/money/minutes/csb-2025-11-10.*, csb-2026-06-08.*; raw/money/facilities/fac-2026-11-12.*

## district-board-and-public-input: The Municipal Budget Committee and the School Board

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. Conway has an RSA 32 municipal budget committee that prepares the school district's budget recommendation, holds the public budget hearing jointly with the school board (February 11, 2026), and prints its vote beside the school board's on every money article; its members include at-large members plus representatives of the selectmen, the school board and the village precincts.
   - citation: Conway Deliberative Session Minutes, March 2, 2026 (attendance); CSB & CMBC Budget Hearing agenda, February 11, 2026; library topic budget-committees
   - source: https://drive.google.com/file/d/12VlFBbW96Nui79TDNd4-YYG39BbbLFE4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Attendance text: "Budget Committee Members present: Chair: Alex Loth; Vice-Chair: Frank Jost; Steve Angers; Bob Drinkall; Kevin Lebel; Dave Jensen; Michael Lacey; Quentin Lewis; Center Conway Fire Rep: Bill Marvel; Selectmen Rep: Ryan Shepard; David Smolen; Wesley Smith". The hearing agenda lists "Discussion and Voting on School Warrant Articles" (raw/money/budget/cmbc-hearing-2026-02-11.pdf). The school board's own "Budget Committee" is a separate board committee. Raw: raw/money/deliberative/dm-2026.ocr.txt
2. Under RSA 32 a budget committee recommends, but voters decide: in an SB2 district the deliberative session may raise the operating budget up to 10% above the committee's recommendation, and since August 12, 2026 the committee, not the school board, sets the default budget (library topic budget-committees, facts 4–5; budget-default-budget, fact 6).
   - citation: RSA 32:18; RSA 32:16, I and III (as amended by 2026, 149:2); library topics budget-committees and budget-default-budget
   - source: https://gc.nh.gov/rsa/html/III/32/32-18.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Conway
   - note: Pointer to the library's statewide rules; no new statewide facts. The first Conway default budget set by the committee will be for 2027-28 (**derived** from the effective date). Raw: none (library)
3. The Municipal Budget Committee recommended against Conway's operating budget three years in a row while the school board recommended it: 3-8-0 in 2023 (passed 902–656), 4-10-0 in 2024 (failed 859–876) and 6-7-0 in 2025 (failed 831–1,081); in 2026 both recommended it (committee 12-1-0) and it passed 1,226–390.
   - citation: Conway ballots and results, April 11, 2023; April 9, 2024; April 8, 2025; April 14, 2026, Article 6
   - source: https://drive.google.com/file/d/1ESXvMD9XByvg0fC3sJAQgd1YDDCcSzzP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Texts: 2023 "(Recommended by the School Board 6-0-0) (Not Recommended by the Municipal Budget Committee 3-8-0) YES - 902 NO - 656 CARRIED" (raw/money/annual-reports/ar-fy2023.ocr.txt); 2024 "(Not recommended by the Municipal Budget Committee 4-10-0) ... ($40,109,103 is recommended by the School Board 4-2-0)"; 2025 "(Recommended by the School Board 5-1-0) (Not Recommended by the Municipal Budget Committee 6-7-0)". From 2019 to 2022 the committee recommended the budget (8-7-0, 14-0-0, 10-2-0, 8-6-0). See table conway_operating_budget_votes. Raw: raw/money/elections/*; raw/money/voter-guides/*
4. For 2025-26 the Municipal Budget Committee's recommended operating budget was $39,413,380 (voted 7-6-1), $2,224,162 below the school board's $41,637,542; at the March 5, 2025 deliberative session the committee's own chair moved to restore the board's figure, which passed by secret ballot 145 to 45 (5.6% above the committee's figure, **derived**), and voters then rejected the budget in April.
   - citation: Conway Deliberative Session Minutes, March 5, 2025, Article 6
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "totaling $39,413,380 ... (Recommended by the Municipal Budget Committee 7-6-1) ... ($41,637,542 is recommended by the School Board 6-1-0). Alex Loth, Budget Committee, made a motion to add $2,224,162.00"; "There were 192 ballots. 145 votes were in favor; 45 were opposed". Derived: 41,637,542 ÷ 39,413,380 = 1.056. The ballot then showed the committee's vote on the amended figure as 6-7-0. Raw: raw/money/deliberative/dm-2025.ocr.txt
5. At the March 4, 2024 deliberative session, budget committee member Bill Marvel said the board's budget, presented as a 1.74% decrease, was "more like a 12 or 13% increase effectively" because a bond of almost $2 million had been retired, and that boards had postponed maintenance "to add staff and add programs while the enrollment is dropping"; member Steve Angers said the default budget did not include closing a school.
   - citation: Conway Deliberative Session Minutes, March 4, 2024, Article 6
   - source: https://drive.google.com/file/d/1HtInnAZ-MMOAPXXUK-Wy88tfnnYiZNHl/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "It is not a 1.74% decrease; it is more like a 12 or 13% increase effectively. Because as someone said, we had a bond retired of almost $2,000,000"; "keep postponing maintenance in order to add staff and add programs while the enrollment is dropping"; "the default budget does not include closing a school." Statements as recorded. Amendments to cut the budget to $38,000,000 (56–188) and $39,500,000 failed at that session. Raw: raw/money/deliberative/dm-2024.ocr.txt
6. School board members answered at the same sessions: in 2024 the board chair said he "was not elected to close a school down" and objected to the committee's roughly $2 million cut recommendation, and in 2025 board members said most of the increase came from special education, voter-approved contracts and health insurance (district-budget-and-cost fact 24).
   - citation: Conway Deliberative Session Minutes, March 4, 2024; Conway Municipal Budget Committee Minutes, January 31, 2024
   - source: https://drive.google.com/file/d/1HtInnAZ-MMOAPXXUK-Wy88tfnnYiZNHl/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: 2024 deliberative text: "Michael DiGregorio, Chair Conway School Board - So, first of all, I was not elected to close a school down." Budget committee minutes (January 31, 2024): "B. Drinkhall- I have a problem with how it has been reported because it has been stated that the budgeters cut 2 million from the schools. We did not, it was simply a recommendation for the school board"; DiGregorio: "you guys go ahead and voted on $2 million recommendation." Committee minutes URL: https://old.conwaynh.gov/wp-content/uploads/2024/06/Conway-Budget-Comm-01312024.pdf. Statements as recorded. Raw: raw/money/deliberative/dm-2024.ocr.txt; raw/money/mbc/mbc-2024-01-31.pdf, .txt
7. Beyond the operating budget, the two bodies split on several articles: the 2024 article to let the district retain up to 5% of year-end fund balance (board 7-0-0, committee 2-11-1 against; failed 787–940), the 2025 Kennett entrance design (board 6-1-0, committee 5-7-2 against; failed 421–1,493), the 2025 $500,000 safety deposit (board 7-0-0, committee 6-7-1 against; failed 916–976) and the 2025 petition restoring school names (board 2-4-0 against, committee 6-4-3 for; passed 1,142–794).
   - citation: Conway ballots and results, April 9, 2024 and April 8, 2025
   - source: https://drive.google.com/file/d/1ESXvMD9XByvg0fC3sJAQgd1YDDCcSzzP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Pages viewed: raw/money/elections/er-2024-p2.png ("Recommended by the School Board (7-0-0) (Not recommended by the Municipal Budget Committee 2- 11-1) 787 YES / NO 940"), er-2025-p3.png. In each split listed, the outcome matched the budget committee's recommendation (**derived** reading). The 2024 results URL: https://drive.google.com/file/d/1xBzF32J82kO9gLv7ZZxBp2hYlliINh9B/view. Raw: raw/money/elections/er-2024.*, er-2025.*
8. The two bodies also disagreed on staff pay: the Municipal Budget Committee recommended the 2025 support staff contract only 7-6-1, and a board member said at the 2025 session it was "rich" to argue pay was too low "when 6 of the Budget Committees members voted against the support staff contract"; in 2026 the committee recommended the teachers' contract 8-3-2.
   - citation: Conway Deliberative Session Minutes, March 5, 2025; Conway Voters Guides, April 2025 and April 2026, Article 5
   - source: https://drive.google.com/file/d/1wqx0hIDYWwPPvaKX3ffiZ9w1uE4d5Mcd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "He finds it rich to say we need to support that when 6 of the Budget Committees members voted against the support staff contract." Guide 2026: "This article is recommended by the CSB (5-0-0) and the MBC (8-3-2)." Statements as recorded. Raw: raw/money/deliberative/dm-2025.ocr.txt; raw/money/voter-guides/vg-2025.txt, vg-2026.ocr.txt
9. In November 2026 the Conway Municipal Budget Committee voted not to endorse HB 1300 (the school tax cap on the 2026 ballot as Question 2), and its chair asked the school board to join a committee reviewing the school's and town's capital plans together.
   - citation: Conway School Board Special Meeting (Budget Review) Minutes (draft), November 5, 2026
   - source: https://drive.google.com/file/d/1nnBOX0aNn_Toc_nQQllAc-taAjVlwl6T/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Megan Beckwith noted that the Conway Municipal Budget committee voted not to endorse HB 1300 in their public meeting ... the sentiment was that legislation such as this is making the lack of state funding a local issue"; "the Budget Committee is looking at the capital improvement plans for the school and the town and wants to form a committee." The law and results are library topics budget-hb-1300-school-tax-cap and budget-question-2-2026-results. Draft minutes; reported secondhand. Raw: raw/money/minutes/csb-2026-11-05-special-draft.*

## town-housing: Rent in Conway

- kind: local
- question_type: local_practice
- description: A town's housing beyond the site's Census estimates: home sales and assessments, short-term rentals, workforce housing, and housing plans and studies

1. The Census Bureau's 2020–2024 American Community Survey estimates that 33.4% (margin of error ±11.5 points) of Conway's 1,325 (±277) renter households paying rent paid 35% or more of household income in rent.
   - citation: U.S. Census Bureau, ACS 5-year estimates 2020–2024, DP04, Conway town
   - source: https://api.census.gov/data/2024/acs/acs5/profile?get=group(DP04)&ucgid=0600000US3300314660
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Conway
   - note: Values: DP04_0142PE "33.4", DP04_0142PM "11.5", DP04_0126E "1325", DP04_0126M "277". Checked against the site database on 2026-11-14 (town_acs_housing, 2020-2024): renter households paying cash rent (B25063_002) 1,325 ±277; paying 35% or more of income (B25070: 40 + 10 + 392 = 442 of the 1,325 with a computed share) = 33.4% (derived). Conway's median gross rent and the share of renters paying 30% or more are in the site's Census data, so they are not repeated here. Pulled by the Jackson research (same files). Raw: raw/money/census/ACSDP5Y2024.DP04-conway.json, labels-DP04.json

## conway_operating_budget_votes: Conway School District Operating Budget, Default and Votes (Article 6)

- unit: dollars
- period: ballot votes April 2019 to April 2026; year: the fiscal year the budget funds (2020 = 2019-20)
- source: Conway School District voter guides, ballots, election results and annual reports 2019–2026 — https://www.sau9.org/conway-home (Drive folders "Voter Guide - Conway," "School Election Results - Conway," "Annual Reports - Conway")
- as_of: 2026-11-13
- raw: raw/money/voter-guides/vg-2019…vg-2026; raw/money/elections/er-2024…er-2026; raw/money/annual-reports/ar-fy2019…ar-fy2025 (.ocr.txt)
- note: Value is the operating budget on the ballot (including grant offsets). The 2020 ballot vote was held May 12, 2020. Committee and board votes are as printed on the ballot. When the article failed, the default became the operating budget. Transcribed from scanned pages.

| Place | District id | Year | Value | Default | Yes | No | Result | Budget committee | School board |
|---|---|---|---|---|---|---|---|---|---|
| Conway | 113 | 2020 | 38328279 | 38129959 | 626 | 375 | Passed | 8-7-0 for | 6-1-0 for |
| Conway | 113 | 2021 | 37740154 | 37687039 | 961 | 448 | Passed | 14-0-0 for | 7-0-0 for |
| Conway | 113 | 2022 | 38653496 | 38414646 | 971 | 456 | Passed | 10-2-0 for | 7-0-0 for |
| Conway | 113 | 2023 | 40303790 | 40014163 | 747 | 397 | Passed | 8-6-0 for | 5-2-0 for |
| Conway | 113 | 2024 | 40254150 | 40121558 | 902 | 656 | Passed | 3-8-0 against | 6-0-0 for |
| Conway | 113 | 2025 | 40109103 | 39002004 | 859 | 876 | Failed; default took effect | 4-10-0 against | 4-2-0 for |
| Conway | 113 | 2026 | 41637542 | 40986456 | 831 | 1081 | Failed; default took effect | 6-7-0 against (recommended $39,413,380, 7-6-1) | 5-1-0 for |
| Conway | 113 | 2027 | 42555376 | 42565234 | 1226 | 390 | Passed | 12-1-0 for | 5-0-0 for |

## conway_tuition_revenue: Conway's Tuition Revenue From Other Districts

- unit: dollars
- period: fiscal years 2015-16 to 2026-27; year: the year the fiscal year ends
- source: site data (DOE-25 revenue account 1321, "Regular Day School (Within NH)"); Conway annual reports, "Estimated Revenues" pages (high school operations line) — https://drive.google.com/drive/folders/1lXxwDUcJ7_PsczB2vihTm_62-NMRiq6j
- as_of: 2026-11-13
- raw: raw/money/state-data/site-db-conway-queries.txt; raw/money/annual-reports/ar-fy2021…ar-fy2025 (.ocr.txt)
- note: Value is total tuition from other New Hampshire districts (DOE-25). 2026 and 2027 are the district's estimates ("Sub Total Tuition"). The high school column is "Tuition - Regular Education High Sch Operations" where the annual reports print it. Excludes sending towns' maintenance trust shares voted as separate articles.

| Place | District id | Year | Value | High school operations | Note |
|---|---|---|---|---|---|
| Conway | 113 | 2016 | 9422941 | | |
| Conway | 113 | 2017 | 9427196 | | |
| Conway | 113 | 2018 | 9788338 | | |
| Conway | 113 | 2019 | 10207518 | | |
| Conway | 113 | 2020 | 10264991 | | |
| Conway | 113 | 2021 | 10616009 | 6964296 | |
| Conway | 113 | 2022 | 10696918 | 7058540 | |
| Conway | 113 | 2023 | 10264096 | 6870760 | |
| Conway | 113 | 2024 | 10449888 | 6843253 | |
| Conway | 113 | 2025 | 9745984 | 6851664 | Annual report prints $9,745,987 |
| Conway | 113 | 2026 | 10676961 | 7442773 | DRA estimate |
| Conway | 113 | 2027 | 11571058 | 8337794 | School board estimate |

## conway_kennett_enrollment_by_town: Students at Conway's Schools by Home District, March 2026

- unit: count
- period: as of March 2026; year: 2026
- source: Conway Annual Report (FY2025), "Conway School District Enrollment (as of March 2026)," p. 30 — https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
- as_of: 2026-11-13
- raw: raw/money/annual-reports/ar-fy2025-p33.png (viewed), ar-fy2025.ocr.txt
- note: Value is Kennett High School students. Middle school is Kennett Middle (grades 6–8); elementary is Pine Tree Primary and Conway Intermediate (K–5). Excludes reported homeschooled students. "Hales" is Hale's Location; "Other" is as printed. Town names match the site's town table where one exists.

| Place | Town id | Year | Value | Middle school | Elementary | Total |
|---|---|---|---|---|---|---|
| Conway | 113 | 2026 | 313 | 222 | 394 | 929 |
| Bartlett | 35 | 2026 | 69 | 1 | 0 | 70 |
| Madison | 333 | 2026 | 68 | 31 | 0 | 99 |
| Tamworth | 525 | 2026 | 68 | 0 | 0 | 68 |
| Freedom | 187 | 2026 | 28 | 13 | 0 | 41 |
| Albany | 5 | 2026 | 23 | 17 | 19 | 59 |
| Jackson | 271 | 2026 | 20 | 0 | 0 | 20 |
| Eaton | 159 | 2026 | 10 | 8 | 16 | 34 |
| Hale's Location | | 2026 | 0 | 1 | 1 | 2 |
| Other | | 2026 | 1 | 4 | 2 | 7 |
| All | | 2026 | 600 | 297 | 432 | 1329 |

## conway_special_education_spending: Conway Special Education Spending and State Aid

- unit: dollars
- period: fiscal years 2019-20 to 2024-25; year: the year the fiscal year ends
- source: Conway annual reports, "Special Education Expenses/Revenue" pages; site data (DOE-25 account 3230) — https://drive.google.com/drive/folders/1lXxwDUcJ7_PsczB2vihTm_62-NMRiq6j
- as_of: 2026-11-13
- raw: raw/money/annual-reports/ar-fy2021…ar-fy2025 (.ocr.txt); raw/money/state-data/site-db-conway-queries.txt
- note: Value is local special education spending (excluding federal grants), as the district reports it; "With grants" adds IDEA and preschool grants. State aid is catastrophic special education aid from DOE-25 (blank = none reported); from FY2021 it matches NH DOE's special education aid files in the site's data (special_education_aid), which also give the costs behind it. Transcribed from scanned pages; the FY2025 page was viewed.

| Place | District id | Year | Value | With grants | State special education aid |
|---|---|---|---|---|---|
| Conway | 113 | 2020 | 5889636 | 6386879 | 143197 |
| Conway | 113 | 2021 | 5500600 | 5942012 | 279630 |
| Conway | 113 | 2022 | 4911262 | 5208621 | 124157 |
| Conway | 113 | 2023 | 5274903 | 5727039 | |
| Conway | 113 | 2024 | 5335156 | 5758803 | |
| Conway | 113 | 2025 | 6170185 | 6526147 | 8218 |

## conway_kms_capital_plan: Kennett Middle School Capital Plan by Fiscal Year

- unit: dollars
- period: fiscal years 2027–2032; year: fiscal year as labeled in the plan
- source: Albany/Conway Tuition Agreement, Grades 7-8 (2027), Appendix B, "CIP Plan - Kennett Middle School" — https://drive.google.com/file/d/1VJ2HlQZZYMXnHHPuZ455HJuzTVO5DOW5/view
- as_of: 2026-11-13
- raw: raw/money/contracts/contract-7-8-albany-conway-2027-p8.png (viewed), .ocr.txt
- note: Value is the plan's projected spending for the year (with a 3% inflation line). The plan is labeled a 5-year total although six year columns appear. Sending towns pay one-fifth of their attendance share each year into the KMS maintenance trust.

| Place | District id | Year | Value | Main items |
|---|---|---|---|---|
| Conway | 113 | 2027 | 136544 | Roof sections H and M |
| Conway | 113 | 2028 | 900000 | Five rooftop units ($655,000), ERV ($95,000), air handlers #11 and #12 ($150,000) |
| Conway | 113 | 2029 | 98432 | Roof sections N and S |
| Conway | 113 | 2030 | 1403675 | Roof sections A1, B, C, E, I, J, O |
| Conway | 113 | 2031 | 1800000 | Boilers, pumps and trim |
| Conway | 113 | 2032 | 300000 | Domestic hot water |
| Conway | 113 | Total | 4502107 | |

## conway_trust_funds_2026: Conway School District Trust and Reserve Fund Balances, Early 2026

- unit: dollars
- period: balances printed for the March 2026 deliberative session (after approved projects); deposits voted April 14, 2026; year: 2026
- source: Conway Annual Report (FY2025), "Explanation of Conway School Board Warrant Articles 2026-27," pp. 6–7; election results April 14, 2026 — https://drive.google.com/file/d/1Hlw-rLE7O1EMIfzVKw2PBmRt8w5m2xIf/view
- as_of: 2026-11-13
- raw: raw/money/annual-reports/ar-fy2025.ocr.txt; raw/money/elections/er-2026.*
- note: Value is the printed current balance. The Safety and Security deposit was $150,000 on the warrant and ballot; the explanation page says $100,000.

| Place | District id | Year | Fund | Value | Deposit approved April 2026 |
|---|---|---|---|---|---|
| Conway | 113 | 2026 | School Buildings Maintenance Fund (1995) | 1623401 | 1000000 |
| Conway | 113 | 2026 | Kennett High School Facilities Maintenance Fund (2007) | 731990 | 54443 (35,158 from sending towns) |
| Conway | 113 | 2026 | Kennett Middle School Facilities Maintenance Fund (2007) | 73135 | 17086 (7,287 from sending towns) |
| Conway | 113 | 2026 | Elementary Schools Facilities Maintenance Fund (2007) | 72443 | 9900 (1,048 from sending towns) |
| Conway | 113 | 2026 | Equipment and/or School Buses Capital Reserve (2019) | 344439 | 250000 |
| Conway | 113 | 2026 | Special Education Capital Reserve (2008) | 453721 | 100000 |
| Conway | 113 | 2026 | Safety and Security Trust Fund (2025) | 32528 | 150000 |

## conway_para_and_regional_wages: Conway Paraprofessional Pay and Regional Hourly Wages

- unit: dollars per hour
- period: Conway CESP schedules 2025-26 and 2026-27; BLS OEWS May 2025; year: 2026
- source: CESP Agreement 2025–2028, Appendix A — https://files.smartsites.parentsquare.com/10271/cesp_agreement_2025-2028_revised_w_sidebar.pdf ; BLS OEWS May 2025, Northern New Hampshire nonmetropolitan area (3300001), BLS public data API — https://www.bls.gov/oes/2025/may/nh_counties.htm
- as_of: 2026-11-13
- raw: raw/money/contracts/cesp-2025-2028.ocr.txt; raw/money/annual-reports/ar-fy2025-p46.png; raw/money/wages/bls-api-oews-northern-nh-nonmetro.json, -2.json
- note: The Place column names the area: the BLS area covers Carroll, Coos and Grafton counties and is not a site town. Value is the hourly rate (Conway) or BLS mean hourly wage; the Median column is BLS's median. Employment is BLS's estimate for the area. Waiters' wages include tips. Comparisons are **derived** and hourly only.

| Place | Year | Job | Value | Median | Employment |
|---|---|---|---|---|---|
| Conway School District | 2026 | Paraprofessional, levels 0–1 (2025-26) | 19.92 | | |
| Conway School District | 2026 | Paraprofessional, 15+ years (2025-26) | 26.40 | | |
| Conway School District | 2027 | Paraprofessional, levels 0–1 (2026-27) | 20.52 | | |
| Northern NH nonmetropolitan area | 2025 | Retail salespersons | 18.05 | 17.30 | 3050 |
| Northern NH nonmetropolitan area | 2025 | Cashiers | 15.63 | 16.00 | 2190 |
| Northern NH nonmetropolitan area | 2025 | Waiters and waitresses | 18.82 | 17.29 | 1740 |
| Northern NH nonmetropolitan area | 2025 | Fast food and counter workers | 15.19 | 14.55 | 1870 |
| Northern NH nonmetropolitan area | 2025 | Cooks, restaurant | 19.75 | 18.66 | 1210 |
| Northern NH nonmetropolitan area | 2025 | Food preparation workers | 17.41 | 17.78 | 620 |
| Northern NH nonmetropolitan area | 2025 | Maids and housekeeping cleaners | 18.02 | 17.66 | 880 |
| Northern NH nonmetropolitan area | 2025 | Hotel, motel and resort desk clerks | 18.25 | 17.90 | 340 |
| Northern NH nonmetropolitan area | 2025 | First-line supervisors of retail sales workers | 25.92 | 23.54 | 850 |
| Northern NH nonmetropolitan area | 2025 | All occupations | 32.99 | 24.55 | 84300 |

## For another file

- **Schools agent:**
  - The 2024-25 consolidation cuts (14.7 FTE), the 2025-26 default cuts (a fourth elementary teacher, 2 paras) and the 2026-27 changes (a grade 6 teacher and a unified arts teacher at KMS; an early learning interventionist and a support para at Pine Tree). Sources: raw/money/packets/dp-2026.ocr.txt (pp. 8–9); raw/money/minutes/csb-2025-04-14.txt.
  - Enrollment by school, October 2021–October 2025 (packet p. 10), and the March 2026 counts by grade. Madison (31), Freedom (13), Albany (17) and Eaton (8) students were at Kennett Middle in March 2026, which bears on the "Madison and Freedom join in grade 7" premise. Sources: raw/money/packets/dp-2026.ocr.txt; raw/money/annual-reports/ar-fy2025-p33.png.
  - The renaming history: board votes on June 24, 2024 (4-3), the 3-3 tie in July 2024, the April 2025 petition (passed 1,142–794), and the May 2025 5-2 vote restoring the names reported by the Conway Daily Sun. Sources: raw/money/minutes/csb-2024-04-29.txt; Drive folder of 2024 minutes. Policy FF (naming) is in raw/money/policies/policy-FF.*.
  - The board's April 2025 debate on moving grade 6 to a content-based middle school model.
- **Kennett agent (town/sau9):**
  - Computer Science was cut from the career center in April 2025. The career center director retired in January 2026, and the role was merged into a Dean of Student Programming and CTE. CTE intro courses are capped at 16 stations. A shop CIP plan exists, and automotive lifts were replaced. Sources: raw/money/minutes/csb-2025-04-14.*, csb-2026-01-12.*, csb-2025-10-14.*; raw/money/facilities/fac-2025-11-20.*.
  - Kennett enrollment by home town (March 2026). The SAU 13 (Madison, Freedom, Tamworth) negotiations, where SAU 13 presented a Governor Wentworth contract in early November 2026, and Davison's removal from the negotiating team. Sources: raw/money/minutes/csb-2026-04-13.*, csb-2026-11-05-special-draft.*.
  - The KMS CIP is in the Albany 7–8 2027 contract, Appendix B (raw/money/contracts/contract-7-8-albany-conway-2027.*). The State Board approved that contract on September 10, 2026.
- **Daily-life agent:**
  - Project SUCCEED is funded by an $88,000 article plus 21st Century grant funds; the district says "We are no longer able to accept fees from parents for this program." Source: raw/money/annual-reports/ar-fy2025.ocr.txt (p. 7).
  - The bus reserve buys one or two buses a year at about $150,000–$230,000, and up to $290,000 was approved from the reserve in June 2026. The AFSCME 2025-26 starting rate for bus drivers is $22.36 an hour. In November 2026 the board discussed possibly cutting a Project SUCCEED bus and one combined K–12 route with staggered starts. Sources: raw/money/annual-reports/ar-fy2025-p46.png; raw/money/minutes/csb-2026-06-08.txt, csb-2026-11-05-special-draft.txt.
- **Community agent:**
  - Robert Frost Charter School's 2025 proposal to lease part of John Fuller was judged "not ... viable at this time" (May 2026).
  - The YMCA exploratory committee and its feasibility study, the Mount Washington Valley Housing Coalition's 16-unit concept, the April 2026 community child care survey (nearly 100 responses), and the CDFA Rural Community Health Infrastructure slides.
  - A charter school enrollment table for Conway, Albany and Eaton students (2026 packet p. 12).
  - Sources: raw/money/fuller/jf-2026-05-13.*, jf-2026-07-29.*; raw/money/packets/dp-2026.ocr.txt.
- **Site data issues (for the site team):**
  - The site's 2025-26 salary-band rows for Conway appear shifted by one column. The "BA" band runs $40,442–$83,192, which is the district's non-degree (ND) column; the bachelor's column runs $42,571–$87,571. The MA band shows 464 steps instead of 46.
  - Jackson's BA minimum shows 4600.00 (the schedule says $46,000), and Tamworth's MA maximum shows 8579.00.
  - Source: raw/money/state-data/site-db-conway-queries.txt against raw/money/annual-reports/ar-fy2025-p45.png.
- **Earlier town files:**
  - Site data, property_tax (Conway district), which replaced the Jackson file's table of valley tax rates: Conway's 2025 local school tax, $23,735,207, matches the district's "DRA estimated" 2025-26 assessment. There is no conflict.
  - The Jackson file says Conway's teacher salary schedules were "scanned and not transcribed." They are now transcribed here: 2025-26 (annual report p. 42) and 2026-27 (CEA Appendix B).
  - Bartlett file, district-tuition-contracts fact 8: the draft Kennett High CIP ($3,835,866.93) is the high school counterpart to the KMS plan here.

## Not retrieved

- **Sale statute.** https://gc.nh.gov/rsa/ (RSA 194, 197, 199 tables of contents): no section was found that says whether a school district sale of real estate needs a district-meeting or ballot vote. RSA 194:2 gives the district power to "dispose of" property without naming the deciding body. https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/technical-advisory-hb-536.pdf (DOE advisory on RSA 194:61) returned HTTP 403.
- **NH DOE unused-facilities list** (RSA 194:61, II): not checked. The DOE site refused automated requests.
- **Restoring the school names.** The May 2025 special meeting minutes on the names, and any cost of the restoration, are not in the 2024-25 minutes folder (https://drive.google.com/drive/folders/1p2G_qmc2f3X2hhTRsxTsrM73BmscbwLq). The Conway Daily Sun's report ("Board bows to voters: Pine Tree, Conway are back," May 2025) was found only through search snippets.
- **Fuller carrying cost.** No source gives actual 2024-25 or 2025-26 spending on the John Fuller building, and no source states the $120,000 figure. The Conway Daily Sun's Fuller articles (e.g., https://www.conwaydailysun.com/news/local/records-show-john-fuller-rented-at-deep-discount/article_0b359021-cbd0-4fdc-8316-1d55c383b678.html) were not opened. The Bergeron appraisal itself is not posted.
- **Town Municipal Budget Committee.** Minutes after January 2024 were not found. https://conwaynh.gov/ is a script-driven site with no budget committee page found. The old wp-content links return 404 on conwaynh.gov and work only on old.conwaynh.gov, which lists minutes only through January 2024. The February 11, 2026 joint hearing document in SAU 9's Drive is the agenda and a blank warrant, not minutes.
- **Rent survey.** NHHFA's Residential Rental Cost Survey (https://www.nhhousing.org/housing-data/rental-housing-cost-survey/): 404, and the PDF URLs tried returned 404.
- **2026 tax rate.** NH DRA's 2026 rate for Conway was not set or not found as of November 13, 2026, and DRA blocks automated requests (Jackson file).
- **Master capital plan.** The Siemens master CIP, the career center shop CIP and the Department of Homeland Security security audits were not posted. They were discussed in minutes only.
- **Superintendent search.** The May 2, 2025 special board meeting and the January 2026 Superintendent Ad Hoc Committee were not read.
- **Annual reports by name.** Conway's annual reports "for the fiscal year ending June 30, 20XX" are printed the following winter, so the FY2025 report holds 2026-27 budget material. The citations name each report by its folder title.
