# Jackson School District: Money, Tuition Contracts and Governance

Part of the Jackson research (town/Jackson). Gathered November 13, 2026.

## Summary

**What's covered:** 10 shared-topic sections (22 topics before the November 13, 2026 fold), 117 facts and 8 number tables on the Jackson School District's money, contracts and governance.
- Why Jackson's NH DOE cost per pupil is high, and what it leaves out (all Bartlett and Kennett tuition, and transportation).
- The budget lines for Kennett tuition, Bartlett tuition, special education, transportation and the SAU 9 share, from 2018-19 to 2026-27.
- The town's 2025 tax rate summary and example bill, with a rough **derived** estimate of the part that pays Kennett tuition, and the 2024 revaluation. Jackson's DRA tax rates (2014–2025) and NH DOE school taxes (2011–2025), and how they compare with Bartlett and Conway, are in the site's data (property_tax), so this file does not repeat them.
- Why Jackson gets no fiscal capacity disparity aid. NH DOE's adequacy aid calculation for Jackson (FY2020–FY2027: a $0 grant and the statewide education tax it keeps above its adequacy cost) is in the site's data (adequacy_aid), so this file does not repeat it.
- The full terms of all four contracts, read page by page from scanned PDFs:
  - Kennett, 2003 contract (current);
  - Kennett, 2027–2032;
  - Fryeburg Academy, 2027–2037;
  - Bartlett grades 7–8, 2026–2029.
- How SAU 9's budget is apportioned, and Jackson's voting weight on the SAU 9 board.
- The cooperative-district study of 2020–2022, and the March 2026 votes.
- High school choice, paying for Fryeburg before 2027, and high school transportation.
- Where to find budgets and salary schedules, including Jackson's own teacher salary schedule.

**Main sources:**
- Jackson's annual reports for 2017–2026 (scanned; budget pages rendered, rotated and read).
- Warrants and annual meeting minutes for 2019–2026.
- Finance Committee minutes for 2025–26.
- SAU 9 board minutes, the four contract PDFs, the board's High School Options FAQ and its February 2026 contract comparison.
- Fryeburg Academy's tuition page, RSA 194-C:7–9, RSA 194:22 and RSA 193:3.
- The library's DRA and DOE town CSVs, and read-only queries of the site database.

**Main gaps:**
- The 2026 tax rates were not yet posted, and DRA's site refused automated requests.
- No MS-27 forms were found.
- Bartlett's yearly per-pupil tuition rider is not posted.
- The Conway and Bartlett teacher salary schedules are scanned and were not transcribed.
- Only the July and September 2026 SAU 9 minutes were checked for weighted voting.
- No Jackson–Bartlett consolidation study exists in the documents searched.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P3.1 Why is per-pupil spending so high, and how much of my tax bill goes to Conway tuition? | district-budget-and-cost 1–15, 26–27; district-tax-and-state-aid 1–8; district-fees 1; tables jackson_hs_tuition_budget_line, jackson_ms_tuition_budget_line; site data: property_tax and adequacy_aid (Jackson district); site data: cost per pupil (FY2025 $50,323 vs $22,699), DOE-25 lines; library: measure-cost-per-pupil, money-adequacy-grant-calculation, money-rand-case | full | The tuition share of a tax bill is a **derived** estimate (budget share × school portion of the bill); 2026 tax rate not yet set by DRA as of the town's posting |
| P3.2 Is a standalone K–6 for fewer than 35 students sustainable, or should we consolidate with Bartlett? | district-budget-and-cost 16–25; district-consolidation-history 1–6; high-school-tuition-options 1–5; district-board-and-public-input 1; tables jackson_operating_budget, jackson_district_students_by_level (community-and-families.md); library: research-district-consolidation, gov-cooperative-forming, gov-cooperative-district | partial | Facts only, no verdict. No Jackson–Bartlett consolidation study found; the 2021–22 eight-town cooperative study voted not to proceed; the 2026–29 Bartlett contract allows reopening a grade 6 discussion |
| P3.3 How accurate are public finance portals at splitting the local tax rate from SAU 9 shared costs? | district-budget-and-cost 28–30; district-sau-governance 1–5, 13; table jackson_sau9_share; site data: property_tax (Jackson district); library: measure-doe-25, measure-cost-per-pupil, budget-sau-budget-vote | full | Shows what DRA, DOE-25, cost per pupil and SAU 9 documents each show and leave out, including a $6,976 gap between two SAU 9 figures for 2025-26 |
| P15.1 How much voting power does Jackson have on the SAU 9 board compared with Conway? | district-sau-governance 6–12; table jackson_sau9_board_seats_and_votes; library: gov-sau, budget-sau-budget-vote | full | Weighted votes are **derived** from RSA 194-C:8 and DOE resident ADM; no SAU 9 record of a weighted vote being demanded was found |
| P15.2 What are the terms of the tuition agreements with Bartlett and Conway, and when are they up? | district-tuition-contracts 1–28; high-school-tuition-options 1–5; district-board-and-public-input 1; library: gov-area-agreements, gov-tuition-towns, gov-public-academies | full | All four contracts read in full (scanned pages rendered and transcribed). None is an AREA agreement |
| P15.3 Where can residents inspect line-item budgets and salary schedules? | district-budget-and-cost 31–37; district-tuition-contracts 33; district-sau-governance 14; site data: salary schedule, average salary | full | Jackson teachers are covered by board personnel policies with a hiring salary schedule, not a union contract |
| P7.1 Do we have any choice of high school, or are we locked into Kennett? | high-school-tuition-options 6–10; school-programs-after-grade-6 1; district-tuition-contracts 7–20; library: open-enrollment-status, change-of-school-assignment, gov-tuition-towns | full | Choice of Kennett or Fryeburg starts 2027-28; Jackson voted in 2026 to cap outbound open enrollment at 0% |
| P18.1 Can we petition or pay out of pocket to send a high schooler to Fryeburg? | district-tuition-contracts 13–20, 29–32; district-budget-and-cost 26–27; district-fees 1; high-school-tuition-options 6–10; school-programs-after-grade-6 1; table jackson_hs_tuition_per_pupil | full | Fryeburg's own site lists 2027-28 commuter day tuition of $22,500; the 2026-27 rate was not on the site |
| P18.3 What happens to transportation for Fryeburg or another out-of-district high school? | district-transportation 1–5; library: gov-school-transportation, school-transportation-rules | full | Bus routes and ride times are another agent's |
| P20.1 (money side) School and total tax rates for Jackson, Bartlett and Conway | site data: property_tax (Jackson, Bartlett and Conway districts); district-tax-and-state-aid 9 | full | The assessed and full value rates and school shares are in the site's data; fact 9 explains Jackson's 2024 revaluation. Home prices are another agent's |

## district-budget-and-cost: Jackson's School Budget and Costs: Cost per Pupil, Budget Lines, Trend, Pay Schedule and Where to Find the Numbers

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. NH DOE's cost per pupil for the Jackson School District counts only the operating cost of Jackson Grammar School (K–6). It leaves out tuition paid to Bartlett for grades 7–8 and to Conway for grades 9–12, and it leaves out transportation, because NH DOE subtracts tuition and transportation from current operating spending before dividing by average daily membership in attendance (ADM-A).
   - citation: NH DOE, "Cost per Pupil by District, 2024-2025," header note (library topic measure-cost-per-pupil); site data: Jackson cost per pupil by level
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: The site's database shows Jackson with only an "elementary" figure ($50,323 in 2025; middle and high blank) and an elementary ADM of 36.45 for 2025, with middle and high ADM 0.00. Raw copy of the queries: raw/money/state-data/site-db-jackson-cost-per-pupil-adm.txt. The 2025 community letter (fact 4) also says the figure "does not include transportation costs, or tuition students at Bartlett Middle School and Kennett High School".
2. For 2024-25, NH DOE's figures give Jackson an average daily membership of 36.45 pupils. At the published cost per pupil of $50,323, that is about $1.83 million of school operating cost spread over those pupils (**derived**: $50,323 × 36.45 = $1,834,273).
   - citation: site data (district_cost_per_pupil 2025; doe_form_adm 2025)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Derived product shown only to illustrate scale; NH DOE divides by ADM in attendance, which may differ slightly from the ADM figure in the site's table. Raw: raw/money/state-data/site-db-jackson-cost-per-pupil-adm.txt
3. At Jackson's March 2, 2023 district meeting, board member Jerry Dougherty explained that the school's tuition students "do not raise the overall budget, but without them, would increase the per pupil cost." The same minutes record that of 47 students then enrolled at JGS, 43 were residents, two were children of teachers and two were tuition students, and that a resident said tuition students pay $10,000.
   - citation: Jackson School District Annual Meeting Minutes, March 2, 2023, Article 1
   - source: https://drive.google.com/file/d/1mOuHIkWHiE0zx1REWYEsLsr05NbKvpDd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "Of the 47 students enrolled - 43 of the students are residents, two are children of teachers, and two are tuition students. Mr. Dougherty explained that the tuition students do not raise the overall budget, but without them, would increase the per pupil cost." Scanned; transcribed from image (OCR checked). Raw copy: raw/money/meetings/am-2023.pdf and .txt
4. A letter read at Jackson's March 6, 2025 district meeting by residents Ann Bennett, Emily Benson and Tish Hanlon said JGS's cost per pupil was $42,514.09 in 2023-24 against a state average of $22,106.94, that the 2025-26 census showed 29 Jackson students plus five non-resident staff children, and that the annual report listed 21 full- and part-time staff. The letter asked the board not to cut the 2025-26 budget but to build a budget "more appropriate to the student census" as part of its next strategic plan.
   - citation: Jackson School District Annual Meeting Minutes, March 6, 2025, attached "Address to Jackson School Board"
   - source: https://drive.google.com/file/d/1m3lWWF77fokVONYlRu9EAEU3QEtRCnSt/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "The cost per pupil at the Jackson Grammar School was $42,514.09 in 2023/24, (this does not include transportation costs, or tuition students at Bartlett Middle School and Kennett High School) ... our request is not to cut the 2025-26 school district budget." The letter is residents' views; cited only for what was said at the meeting. The $42,514 matches the site's FY2024 figure. Raw copy: raw/money/meetings/am-2025.pdf and .txt (transcribed from image)
5. In budget discussions for 2026-27, SAU 9 business administrator Mike Wade told the Jackson Finance Committee that the main driver of the rising high school tuition line was declining enrollment overall, "which creates proportional increases to all of the districts," with enrollment and equalized valuation shares within fractions of one another.
   - citation: Jackson Finance Committee Minutes, December 17, 2025
   - source: https://drive.google.com/file/d/10a6kiM9xwSeAbkRwB_5SbKKAYA74RhWB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "Mike Wade explained that enrollment and equalized value are within fractions of one another, but the biggest impact is with declining enrollment overall, which creates proportional increases to all of the districts." This is about Kennett tuition, which cost per pupil does not include. Raw copy: raw/money/finance-committee/fc-2025-12-17.pdf and .txt
6. NH DOE says two districts' cost per pupil should be compared only when they serve the same grades. Jackson's figure covers a K–6 school only, while the state average covers all district-operated schools (library topic measure-cost-per-pupil, facts 6–7).
   - citation: NH DOE, "Cost per Pupil by District, 2024-2025," note (library topic measure-cost-per-pupil)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Pointer to the existing library rule; the Jackson-specific part is that Jackson operates only K–6.
7. Jackson voters approved a 2026-27 operating budget of $4,066,810 (Article 1) at the March 5, 2026 district meeting, with $21,000 of it offset by grants; the board recommended it 5-0-0 and no public comment was received.
   - citation: Jackson School District Annual Meeting Minutes, March 5, 2026, Article 1
   - source: https://drive.google.com/file/d/16gP8PVjAV-V-7QnDFMButI5dgFgXZ66L/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "raise and appropriate the sum of $4,066,810 ... with $21,000 offsetting this amount from various grants ... No public comment was received. Motion Carried, Article Passed". Scanned; transcribed from image. Raw copy: raw/money/meetings/am-2026.pdf and .txt
8. In Jackson's 2026-27 budget, the "Tuition, High School" line (Kennett) is $868,953, up $249,468 (40.27%) from $619,485 in 2025-26; actual 2024-25 spending on that line was $644,248.
   - citation: Jackson School District 2026 Annual Report, "2026-2027 Proposed Budget - Summary of Increases & Decreases," p. 6
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Row text: "56 71-10-1100-5560-0103 TUITION, HIGH SCHOOL 644,248 644,248 619,485 868,953 249,468 40.27%". Rotated scanned page; transcribed from image (page viewed). See table jackson_hs_tuition_budget_line. Raw copy: raw/money/annual-reports/ar-2026.pdf, .txt and .rot90.txt (page 9)
9. In Jackson's 2026-27 budget, the "Tuition, Middle School" line (Bartlett) is $384,000, down $64,000 (14.29%) from $448,000 in 2025-26; actual 2024-25 spending was $221,454. At a December 3, 2025 Finance Committee meeting, Mike Wade said the district expected 10 middle school students but budgeted for 12, and expected 22 high school students.
   - citation: Jackson School District 2026 Annual Report, p. 6; Jackson Finance Committee Minutes, December 3, 2025
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Row text: "55 71-10-1100-5560-0102 TUITION, MIDDLE SCHOOL 278,472 221,454 448,000 384,000 (64,000) -14.29%". Minutes text: "we are expecting 10 students, but they have budgeted for 12 in case a few move in ... they are expecting 22 high school students". **Derived**: $384,000 ÷ 12 = $32,000 budgeted per middle school student; $868,953 ÷ 22 = $39,498 per high school student. See table jackson_ms_tuition_budget_line. Raw: raw/money/annual-reports/ar-2026.*; raw/money/finance-committee/fc-2025-12-03-attach.pdf and .txt (minutes are page 1; Finance Committee minutes URL https://drive.google.com/file/d/1bQ6ZQPS_Xw5I5gVKcO8KLjaUN3EUsO3N/view)
10. Jackson's 2026-27 budget sets the "SAU9 Share" at $190,660, up $23,117 (13.80%) from $167,543 in 2025-26; actual 2024-25 was $137,921.
   - citation: Jackson School District 2026 Annual Report, p. 6
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Row text: "225 71-10-2320-5311-0104 SAU9 SHARE 137,921 137,921 167,543 190,660 23,117 13.80%". See table jackson_sau9_share. Raw: raw/money/annual-reports/ar-2026.* (page 9)
11. Jackson's "Tuition, Special Education" line (out-of-district special education placements) is $477,852 in 2026-27, down $135,698 (22.12%) from $613,550 in 2025-26; nothing was budgeted on that line for 2024-25, and actual 2024-25 spending was $240,497.
   - citation: Jackson School District 2026 Annual Report, p. 6
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Row text: "113 71-10-1200-5560-0109 TUITION, SPECIAL EDUCATION - 240,497 613,550 477,852 (135,698) -22.12%". The district's High School Options FAQ says special education costs "follow student needs, not contracts". Raw: raw/money/annual-reports/ar-2026.* (page 9)
12. By function, Jackson's 2026-27 budget puts $1,984,307 in regular education (which includes the Bartlett and Kennett tuition lines), $603,980 in special education instruction, $207,692 in transportation, $190,660 in SAU services, $287,106 in the principal's office and $265,967 in building operation and maintenance, for a total of $4,066,810 (a 2.41% increase over 2025-26's $3,970,978).
   - citation: Jackson School District 2026 Annual Report, "2026-2027 Draft Budget (By Function)," p. 7
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Row text: "1100 Regular Education $1,619,685 $1,545,901 $1,835,461 $1,984,307 ... 2720 Transportation $185,133 $300,269 $191,858 $207,692 ... Grand Total $3,046,203 $3,377,736 $3,970,978 $4,066,810 $95,832 2.41%". Columns: Adopted FY25, Actual FY25, Adopted FY26, Draft FY27. Actual 2024-25 transportation was $300,269. Raw: raw/money/annual-reports/ar-2026.* (page 10)
13. In Jackson's 2026-27 budget, Kennett tuition is about 21% of the operating budget, Bartlett tuition about 9%, out-of-district special education tuition about 12%, transportation about 5% and the SAU 9 share about 5% (**derived**: each line ÷ $4,066,810; 21.37%, 9.44%, 11.75%, 5.11% and 4.69%).
   - citation: Jackson School District 2026 Annual Report, pp. 6–7
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Derived shares from the lines in facts 2–6. Raw: raw/money/annual-reports/ar-2026.*
14. Jackson's Kennett bond payments ended after 2023-24: the "Tuition, HS Bond Share" line was $50,304 in 2023-24 and blank from 2024-25 on. A separate "Tuition, HS Maint Trust Share" line was $4,441 (2024-25 adopted) and $4,556 (2025-26).
   - citation: Jackson School District 2025 Annual Report, "2025-2026 Proposed Budget," p. 8
   - source: https://drive.google.com/file/d/16jP77ozx7pXrm3uWDDEUADqqo4w5_ycT/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Row text: "57 71-10-1100-5561-0103 TUITION, HS BOND SHARE $ 50,304 $ 50,304 $ - $ -" and "58 ... TUITION, HS MAINT TRUST SHARE $ 4,497 $ 4,497 $ 4,441 $ 4,556" (columns Adopted 2023-24, Actual 2023-24, Adopted 2024-25, Proposed 2025-26). Page viewed. Raw: raw/money/annual-reports/ar-2025.* (page 10)
15. In May 2026, Finance Committee member James Glazer said the high school tuition line rose about $250,000 for 2026-27, "with the main driver being Jackson's share of the new roof at Kennett High School." The district's FAQ lists the end of federal COVID-era (ESSER) funding, declining enrollment, shifts in equalized valuation, capital needs including the Kennett roof, and other cost increases as causes, and says Jackson paid $29,800 per high school student in the 2026 budget and $38,600 in the 2027 budget.
   - citation: Jackson Finance Committee Minutes, May 19, 2026; Jackson School District High School Options FAQ, "2026 School Budget FAQ" question 3
   - source: https://drive.google.com/file/d/182yU552bkgreGZpr2zkl7oYOmlPQ6CJi/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Minutes text: "the high school tuition line increased approximately $250,000, with the main driver being Jackson's share of the new roof at Kennett High School." FAQ text: "In the 2026 budget, Jackson pays $29,800 per high school student. In the 2027 budget, that cost rises to $38,600 per student." FAQ: https://docs.google.com/document/d/1W_J4PMEjzDkXRLuSGMhwKyyt2UXjZycgKGBfr2ejxQ4/edit. Raw: raw/money/finance-committee/fc-2026-05-19.*; raw/money/jgs/hs-options-faq.txt
16. Jackson's voter-approved operating budget (Article 1) grew from $2,724,690 for 2019-20 to $4,066,810 for 2026-27 (**derived**: up 49.3%). The largest single-year jump was for 2025-26, from $3,046,203 to $3,970,978.
   - citation: Jackson School District warrants and annual meeting minutes, 2019–2026
   - source: https://www.sau9.org/jackson
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: See table jackson_operating_budget. Warrants are in the "Jackson Warrant Articles" folder and minutes in "Annual Meetings - Jackson" (Drive folders linked from the page). Raw: raw/money/warrants/w-2019…w-2026 and raw/money/meetings/am-2019…am-2026 (.pdf and .txt, transcribed from image)
17. At the March 6, 2025 meeting, a resident from Conway said most of the 2025-26 increase was in special education and in sending students to Bartlett. In the 2025-26 budget, out-of-district special education tuition went from no budgeted amount to $613,550 and Bartlett tuition from $278,472 to $448,000.
   - citation: Jackson School District Annual Meeting Minutes, March 6, 2025; 2025 Annual Report, proposed budget; 2026 Annual Report, p. 6
   - source: https://drive.google.com/file/d/1m3lWWF77fokVONYlRu9EAEU3QEtRCnSt/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Minutes text: "James Wrigley - Conway - the majority of the increase is in special education funding and in sending students to Bartlett." Budget rows from raw/money/annual-reports/ar-2025.rot90.txt and ar-2026 p. 6. The meeting date is March 6, 2025 (title of minutes). Raw: raw/money/meetings/am-2025.*
18. Jackson voters have twice been asked to cut the school budget from the floor. In 2022 they amended Article 1 down by $100,000, to $2,754,739, and passed it; in 2023 a motion to cut $64,496 failed and the $3,104,417 budget passed as proposed.
   - citation: Jackson School District Annual Meeting Minutes, March 3, 2022 and March 2, 2023
   - source: https://drive.google.com/file/d/1db-nBerlVVuPrwwJwPE7x0O0BHMXA3j6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: 2022 text: "Mr. Benson made a motion to reduce the budget down $100,000 to $2,754,739.00 ... MOTION PASSED". 2023 text: "Mr. Benson made a motion to decrease the budget by $64,496 ... MOTION FAILED ... Vote on original article one as presented. MOTION CARRIED". 2023 minutes: https://drive.google.com/file/d/1mOuHIkWHiE0zx1REWYEsLsr05NbKvpDd/view. Raw: raw/money/meetings/am-2022.*, am-2023.*
19. In 2022, Jackson voters rejected a $250,000 Jackson Grammar School Renovation and Construction Capital Reserve Fund. At that meeting a resident said the district "need[s] to examine a partnership with the Bartlett School District," and another challenged the board to work with Bartlett on both schools' challenges.
   - citation: Jackson School District Annual Meeting Minutes, March 3, 2022, Articles 1 and 6
   - source: https://drive.google.com/file/d/1db-nBerlVVuPrwwJwPE7x0O0BHMXA3j6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Ann Bennett ... We need to examine a partnership with the Bartlett School District." "Peter Benson ... He challenged the Board and the leadership of the School to work with Bartlett to address the challenges of both schools." "Ms. Tracy called for a vote on the article. MOTION FAILED". Raw: raw/money/meetings/am-2022.*
20. At a December 17, 2025 Finance Committee meeting, board member James Glazer said community members were concerned about "the viability of the Jackson Grammar School" and asked for a list of possible cuts; principal Erin Messer said she had not heard community members say they wanted to close the school and that she could find about $77,000 in cuts but did not recommend them because of the effect on programs.
   - citation: Jackson Finance Committee Minutes, December 17, 2025
   - source: https://drive.google.com/file/d/10a6kiM9xwSeAbkRwB_5SbKKAYA74RhWB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "James Glazer wants the people in this meeting room to hear clearly that the people in the community are concerned about the viability of the Jackson Grammar School ... Erin Messer stated that she ... has not heard community members state that they are interested in closing their school ... She can make approximately $77,000 in cuts, but not without impact to programming and does not recommend this." Raw: raw/money/finance-committee/fc-2025-12-17.*
21. The 2026-27 budget sent to voters included cuts of $39,949 proposed by the principal (the PE position, turning the reading specialist position into a stipend, and a smaller substitute line), along with a $249,000 reduction in special education tuition, according to draft Finance Committee minutes.
   - citation: Jackson Finance Committee Minutes (draft), January 13, 2026
   - source: https://drive.google.com/file/d/1WBcjfhClRZKkvu9Q2KQj0LQ7HKb6-lKJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "It shows a reduction of $249,000 in special education tuition. It also includes reductions that Erin Messer proposed, which includes the PE position, the reduction of the reading specialist position to a stipend, and a reduction to the substitute line. These reductions total $39,949." These minutes are a draft whose approval was tabled (May 19 and June 30, 2026 minutes). The adopted budget shows "SALARIES, PHYS ED" going from $13,554 to $0. Raw: raw/money/finance-committee/fc-2026-01-13-draft.*
22. For the 2027-28 budget, the Finance Committee's October 29, 2026 draft had an increase of about $93,000 before tuition and the SAU share were added; James Glazer suggested an increase of 3% or less would be "favorably received by the community."
   - citation: Jackson Finance Committee Minutes (draft), October 29, 2026
   - source: https://drive.google.com/file/d/1j2Q4GBFOX-PiBgXTL2LhM8gNQPyz2Z7M/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "There is an increase of $93,000 without tuition and SAU ... James Glazer suggested that a budget with an increase of 3% or less would be favorably received by the community." Draft minutes. Raw: raw/money/finance-committee/fc-2026-10-29-draft.*
23. Jackson's tuition trust fund held about $115,000 in October 2026; the business administrator recommended keeping about $100,000 and neither adding to nor spending from it for now, and the committee agreed to hold the balance "in light of the new contract situation."
   - citation: Jackson Finance Committee Minutes (draft), October 29, 2026
   - source: https://drive.google.com/file/d/1j2Q4GBFOX-PiBgXTL2LhM8gNQPyz2Z7M/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Mike Wade said there is approximately $115,000 in this fund. He recommended not putting money into the fund and not expending from it ... Melinda Foley-Marsello said in light of the new contract situation, they should hold the balance for now." Raw: raw/money/finance-committee/fc-2026-10-29-draft.*
24. In June 2026 the Finance Committee recommended that Jackson keep its tuition for non-resident students at JGS at $10,000 a year, with special services billed separately, under an admission policy that considers capacity and the school community; the committee said extra students "benefit the school more than they cost the community."
   - citation: Jackson Finance Committee Minutes, June 30, 2026
   - source: https://drive.google.com/file/d/16JL7pw0R9GW6uFTggLMNx3DFwz3kRZn6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "the committee agreed to recommend to the Board that the tuition rate remain at $10,000 per student. Special services would be in addition to tuition ... the policy should be focused on attracting extra students, as they benefit the school more than they cost the community." Recommendation only; no board vote found. Raw: raw/money/finance-committee/fc-2026-06-30.*
25. Jackson Grammar School has operated since 1806, according to the cover of the district's annual reports ("Jackson Grammar School 1806-2025"), which also note it was the state's 2014 Elementary School of Excellence. No warrant article to close JGS or to send its K–6 students elsewhere was found in Jackson's warrants for 2019 through 2026.
   - citation: Jackson School District 2026 Annual Report, cover; Jackson warrants 2019–2026
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Cover text: "Jackson Grammar School 1806-2025 The Little School with a BIG Heart ... 2014 Elementary School of Excellence for the State of New Hampshire". The absence of a closure article is from reading all eight warrants (raw/money/warrants/). Raw: raw/money/annual-reports/ar-2026.*
26. The Jackson School Board's February 6, 2026 contract comparison gives Kennett's 2026-27 tuition as $38,603 per pupil (maintenance included), and estimates 2027-28 tuition at $27,855 per pupil for Kennett under the new contract and $26,788 for Fryeburg Academy, with a "legacy" Fryeburg commuter rate of $22,388 for students enrolled before the contract. It estimates transportation to Kennett at $98,000 and leaves special education out of the comparison.
   - citation: Jackson School Board, "High School Contract Comparison," updated February 6, 2026, pp. 3–4
   - source: https://files.smartsites.parentsquare.com/10273/updated_hs_contract_comparison_2026_district_vote_.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Kennett High School 2026/2027 tuition: $38,603 per pupil ... Kennett High School 2027/2028 estimated tuition: $27,855 per pupil ... Fryeburg Academy 2027/2028 estimated tuition: $26,788 per pupil Legacy (commuter) rate: $22,388 per pupil ... Transportation: $98k estimated to transport to KHS"; p. 4: "Per pupil costs are projections based on average annual increases in tuition over the last 5 years for FA and KHS ... Scenarios estimate 20 Jackson students ... Special education costs are not included". Linked from https://jgs.sau9.org/324669_2. See table jackson_hs_tuition_per_pupil. Raw: raw/money/jgs/hs-contract-comparison-2026.pdf and .txt
27. SAU 9's 2019 chart of high school tuition per pupil (operation, maintenance and bond) shows Jackson's rate between about $25,000 and $28,000 a year from 2015-16 to 2019-20, while Conway, Albany, Madison and Tamworth were between about $11,000 and $16,000 (values read from the chart, approximate).
   - citation: SAU 9 Study Committee Presentation, February 28, 2019, slide 22 "High School Tuition Rate History - 5 year"
   - source: https://drive.google.com/file/d/17rVLU-Ui99yNkgX6qk1FnXa93mS0MpIc/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: The chart has no data labels; values were estimated from the gridlines on the rendered slide (transcribed from image). Under the 35/65 formula, a town with a higher share of equalized value than of students pays more per student. Raw: raw/money/study/study-committee-presentation-2019-02-28.pdf
28. NH DRA's tax rate for Jackson splits the school part into a "local education" rate and a "state education" rate, but does not show what the school money is spent on; Kennett tuition, Bartlett tuition, special education and the SAU 9 share are all inside the single local education rate ($3.54 in 2025).
   - citation: NH DRA, Municipal and Village District Tax Rates 2025 (library raw/town/dra-tax-rates.csv)
   - source: https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Library description in additional-data/town-figures.md. Assessed rates are not comparable across towns; DRA's full value rate is. Both are in the site's data (property_tax, Jackson district). Raw: raw/money/state-data/dra-tax-rates-jackson-bartlett-conway.csv
29. NH DOE's DOE-25 report shows Jackson's spending by function and by school level (elementary, middle and high pages), so Bartlett and Kennett tuition appear as purchased services on the middle and high school pages; the SAU 9 share does not appear by name, because the district codes it to function 2320 "SAU Services," which the DOE-25 reports within the 2300 general administration line.
   - citation: site data (DOE-25 expenditure lines for Jackson, FY2025); Jackson School District 2026 Annual Report, p. 7 ("2320 SAU Services"); library topic measure-doe-25
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: In the site's FY2025 DOE-25 data, page 8 line 1 "Regular Programs" purchased services is $221,454.32 (equal to the actual Bartlett tuition) and page 9 line 1 is $648,688.00 (Kennett tuition $644,248 plus the maintenance trust share $4,441, **derived** check). Budget account code "71-10-2320-5311-0104 SAU9 SHARE". Raw: raw/money/annual-reports/ar-2026.*
30. NH DOE's cost per pupil for Jackson leaves out all of the high school and middle school tuition and transportation, so it describes JGS only; it is not a measure of what Jackson taxpayers spend per resident student in grades K–12.
   - citation: library topic measure-cost-per-pupil
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: See district-budget-and-cost 1–6. No published source giving a K–12 per-resident-student figure for Jackson was found.
31. Jackson's line-item budget is printed in the district's annual report each year (proposed budget with prior adopted and actual figures, a summary of increases and decreases, a by-function summary, special education expenses and revenue, the SAU 9 apportionment, enrollment and staff salaries). The reports from 2017 to 2026 are in the "Annual Reports - Jackson" folder linked from SAU 9's Jackson School Board page.
   - citation: SAU 9, Jackson School Board page; Jackson School District 2026 Annual Report, table of contents
   - source: https://www.sau9.org/jackson
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: The page links "Policies, Agendum, Minutes, Committees and Annual Reports" (https://drive.google.com/drive/folders/1ll0qPE0H6RBIT6IJ-x59bDhXIHoAN1EQ). The 2026 report's contents: "2026-27 Budget Summary of Proposed Increases/Decreases 6 / 2026-27 Proposed Budget by Function 7 / 2026-27 Proposed Budget 8 ... Sp. Ed. Expenses/Revenue 28 ... SAU #9 2026-27 Budget with Apportionments 32". The 2024 report also lists "Staff Salaries for the Fiscal Year 2022-23". The reports are scanned images. Raw: raw/money/sau9/board-jackson.*; raw/money/drive/jackson-annual-reports-folder.html
32. Jackson's warrants (2019–2026), annual meeting minutes (2019–2026), school board minutes and agendas, and committee minutes (including the Finance Committee and the High School Options Committee) are in Drive folders linked from SAU 9's Jackson School Board page; board meeting videos are on JacksonFlicks.
   - citation: SAU 9, Jackson School Board page and linked folders; JGS "High School Options" page
   - source: https://www.sau9.org/jackson
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Committee folder: https://drive.google.com/drive/folders/1ymA8zFwq2IYYT_W2J45hzLM9o9Fa2iN2. JGS page text: "Jackson School Board Meetings on Jackson Flicks video" (https://jacksonflicks.com/). Raw: raw/money/drive/*.html; raw/money/jgs/jgs-high-school-options.*
33. Teacher contracts and personnel policies for every SAU 9 district are on SAU 9's "Negotiated Agreements & Personnel Policies" page: Jackson's personnel policies for the principal, contracted employees and non-contracted employees; Bartlett's BEA agreement; Conway's CEA teachers' agreement (2026–2029), AFSCME and CESP agreements; and SAU 9's own personnel policies.
   - citation: SAU 9, Negotiated Agreements & Personnel Policies
   - source: https://www.sau9.org/negotiated-agreements-personnel-pol
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Page text: "Jackson Personnel Policies for Contracted Employees <https://files.smartsites.parentsquare.com/10271/personnel_polices_for_contracted_employees_2026-27_1.pdf>"; "CEA Agreement (2026-2029) ... (Teachers/Nurses)". The Conway and Bartlett agreements were downloaded but are mostly scanned; their salary schedules were not transcribed. Raw: raw/money/sau9/sau9-negotiated.*; raw/money/sau9/cea-agreement-2026-2029.pdf; raw/money/sau9/bea-agreement-2026-27.pdf
34. State-level sources for Jackson's school finances are NH DOE's Financial Reports page (DOE-25, cost per pupil, and the valuations and tax rates of school districts), NH DOE's State Adequate Education Aid page, and NH DRA's municipal tax rate reports; the Town of Jackson posts a yearly tax rate summary.
   - citation: NH DOE Financial Reports; NH DOE State Adequate Education Aid; Town of Jackson property tax info
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Other URLs: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid ; https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village (returned 403 to automated requests today) ; https://www.jackson-nh.gov/wp-content/uploads/2026/01/property_tax_rate_info_2025.pdf. Library topics measure-doe-25 and measure-cost-per-pupil describe the DOE reports.
35. Jackson's teachers are covered by the school board's "Personnel Policies for Contracted Employees" (effective July 1, 2026), not a negotiated union agreement; SAU 9's page lists union agreements for Bartlett and Conway but personnel policies for Jackson.
   - citation: Jackson School District, Personnel Policies for Contracted Employees (effective July 1, 2026); SAU 9 Negotiated Agreements page
   - source: https://files.smartsites.parentsquare.com/10271/personnel_polices_for_contracted_employees_2026-27_1.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Cover text: "Effective July 1st, 2026 PERSONNEL POLICIES FOR CONTRACTED EMPLOYEES OF JACKSON SCHOOL DISTRICT". Raw: raw/money/sau9/jackson-personnel-contracted-2026-27.pdf and .txt
36. Jackson's 2026-27 "Salary Schedule for Hiring" runs from $46,000 (bachelor's, step 1) to $59,500 (bachelor's, step 10) and from $49,312 (master's, step 1) to $69,734 (master's plus 60 credits, step 10), with $1,500 between steps. The board says the schedule is for placing new teachers so that no new hire earns more than a veteran with the same qualifications.
   - citation: Jackson Personnel Policies for Contracted Employees, Article 12 and Appendix A (p. 19)
   - source: https://files.smartsites.parentsquare.com/10271/personnel_polices_for_contracted_employees_2026-27_1.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "STEP $1,500 2026-27 Salary Schedule for Hiring Step B B+6 ... M M+30 M+60 / 1 46,000 46,552 47,104 47,656 48,208 48,760 49,312 51,612 53,912 ... 10 59,500 60,214 60,928 61,642 62,356 63,070 63,784 66,759 69,734". The M+60 step 6 cell reads 60,702, lower than step 5 (60,944); copied as printed. Revised January 20, 2026 (effective July 1, 2026). Raw: as fact 1
37. Jackson teachers' yearly raises depend on their evaluation rating: $0 for unsatisfactory, $1,150 (cumulative) for basic, $2,100 (cumulative) for proficient, and a $500 one-time bonus for distinguished, under a system the board approved December 16, 2013.
   - citation: Jackson Personnel Policies for Contracted Employees, Article 12(A)
   - source: https://files.smartsites.parentsquare.com/10271/personnel_polices_for_contracted_employees_2026-27_1.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Unsatisfactory (0%-42%) – $0.00 • Basic (43%-59%) - $1,150 * (cumulative) • Proficient (60%-84%) - $2,100 * (cumulative) • Distinguished (85%-100%) - $500 (one-time bonus)". The site's database also has Jackson's salary schedule and average salary from NH DOE. Raw: as fact 1

## district-tax-and-state-aid: Jackson's School Taxes, Tax Rates and State Aid

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. Property in Jackson's water precinct pays the precinct's rate on top of the town's tax rate: $2.09 per $1,000 of assessed value in 2025, up from $1.94 in 2024, for a total of $10.70 against $8.69.
   - citation: Town of Jackson, "Important Property Tax Info" (2025 tax rate)
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/01/property_tax_rate_info_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "TOTAL $6.75 $8.61 $1.86 / If your property is in the water precinct / Water Precinct $1.94 $2.09 $0.15 / TOTAL $8.69 $10.70 $2.01". The town's rates without the precinct ($6.75 and $8.61, and their parts) are DRA's and are in the site's data (property_tax, Jackson district; checked November 15, 2026); precinct rates aren't. The notice's average-home example is fact 2. Raw copy: raw/money/town/property-tax-rate-info-2025.pdf and .txt
2. The Town of Jackson's own example for an average $500,000 single-family home in 2025 is a total bill of $4,305: $1,770 local school, $535 state education, $1,625 town and $375 county, against $3,375 in 2024.
   - citation: Town of Jackson, "Important Property Tax Info" (2025)
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/01/property_tax_rate_info_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "Local School $1,040.00 $1,770.00 $730.00 / State Education $525.00 $535.00 $10.00 ... Total $3,375.00 $4,305.00 $930.00". The town's published example; the school share of Jackson's rate is in the site's data (property_tax, Jackson district). Raw: raw/money/town/property-tax-rate-info-2025.*
3. A rough estimate: Kennett tuition was 15.6% of Jackson's 2025-26 school budget ($619,485 of $3,970,978), so on the town's $500,000 example about $360 of the $4,305 bill went to Kennett tuition; Bartlett tuition about $260 and the SAU 9 share about $97 (**derived**: each line's share of the adopted 2025-26 budget × the $2,305 school portion of the bill).
   - citation: Jackson School District 2025 and 2026 Annual Reports; Town of Jackson 2025 property tax info
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Derived and approximate. It assumes every budget line is paid for in the same mix of local school tax, state education tax and other revenue, which no source states. Tax year 2025 funds the 2025-26 school year. Shares: Kennett 15.60%, Bartlett ($448,000) 11.28%, SAU ($167,543) 4.22%. For 2026-27 the Kennett line is 21.37% of the budget, but the 2026 tax rate had not been posted by the town. Raw: raw/money/annual-reports/ar-2026.*; raw/money/town/property-tax-rate-info-2025.*
4. Jackson's High School Options FAQ says that in 2023, 32% of the school district's funding came from the state (mainly the statewide education property tax) and 68% from local property taxes, and that because of Jackson's high property value and few students, the state's formula would give Jackson "very little state funding relative to taxes paid."
   - citation: Jackson School District High School Options FAQ, "2026 School Budget FAQ" question 1
   - source: https://docs.google.com/document/d/1W_J4PMEjzDkXRLuSGMhwKyyt2UXjZycgKGBfr2ejxQ4/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: FAQ text: "In 2023, 32% of funding was from the State (primarily via SWEPT) and 68% from Local Property Taxes ... towns such as Jackson would be eligible for very little state funding relative to taxes paid." Living document; retrieved as plain text. Raw: raw/money/jgs/hs-options-faq.txt
5. Jackson residents can look up their own bill split on the state's tax kiosk, where state funding is labeled "State Education" and local school funding "School," according to the district FAQ.
   - citation: Jackson School District High School Options FAQ
   - source: https://docs.google.com/document/d/1W_J4PMEjzDkXRLuSGMhwKyyt2UXjZycgKGBfr2ejxQ4/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: FAQ text: "you can see how you personally fund the schools on your property tax bill here - https://nhtaxkiosk.com/. State Funding is labeled 'State Education' and Local Funding is labeled 'School'." Kiosk not checked. Raw: raw/money/jgs/hs-options-faq.txt
6. NH DOE's FY2027 aid file lists Jackson's equalized property value per pupil at $16,937,800.60. Fiscal capacity disparity aid goes only to towns below $1.6 million per pupil (the full $1,250 per pupil below $1.0 million), so Jackson gets none.
   - citation: NH DOE, FY 2027 Adequacy Aid (October 1, 2026), "EV Per ADM" and fiscal capacity disparity aid columns
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: CSV components ev_per_pupil 16937800.6 and fiscal_capacity_disparity_aid 0 for Jackson FY2027. The $0 aid, equalized value and pupil count are in the site's data (adequacy_aid, Jackson district), which also shows Jackson's $0 adequacy grant and the statewide tax it keeps above its adequacy cost; value per pupil is not. For scale, the library's town-figures examples give Hampton $4,908,634.08 and Berlin $1,153,001.55. Raw: raw/money/state-data/adequacy-aid-sau9-towns.csv
7. SAU 9's 2019 study committee, using NH DOE data for 2017-18, listed Jackson's equalized value per student at $5,178,507 (95th percentile, rank 12 of 290) and its education tax rate at $5.82 per $1,000 of equalized value (rank 247 of 270), against a state average of $983,646 and $12.70.
   - citation: SAU 9 Study Committee, "MWV Tax Rate Implication" handout (2019)
   - source: https://drive.google.com/file/d/1Ftv7OwVYexUHXXdtWpbDAXvmbT92uZOe/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "Jackson 5,178,507 95% (12) 5.82 8.5% (247)" and "State Average 983,646 12.70". Ranks are the source's own. The $5.82 equals NH DOE's tax year 2017 equalized local ($3.69) plus state education ($2.13) rates for Jackson in the site's data (property_tax). Linked from https://www.sau9.org/tuitions. Raw: raw/money/study/mwv-tax-rate-implication.pdf and .txt
8. The same 2019 handout listed the amount a $1.00 increase in the school tax rate per $1,000 raised in 2017: Conway $1,447,967, Bartlett $1,055,724, Jackson $398,329, Albany $111,970, Eaton $110,384 and Chatham $49,159.
   - citation: SAU 9 Study Committee Presentation, February 28, 2019, slide 28
   - source: https://drive.google.com/file/d/17rVLU-Ui99yNkgX6qk1FnXa93mS0MpIc/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Slide text: "Amount raised by $1.00 increase in taxes/thousand Town 2017 Conway $1,447,967 Bartlett $1,055,724 Jackson $398,329". Jackson's figure is one thousandth of its 2017 assessed valuation with utilities in NH DOE's data ($398,329,826; site data: property_tax). Raw: raw/money/study/study-committee-presentation-2019-02-28.pdf and .txt
9. Jackson's 2024 revaluation cut its rates per $1,000 of assessed value: its equalization ratio went from 60.2% in 2023 to 95.6% in 2024 and its local school rate fell from $4.32 to $2.08, before rising to $3.54 in 2025; the district's High School Options FAQ says "The recent revaluation led to a substantial drop in Jackson's SWEPT tax rate."
   - citation: NH DRA tax rates and equalization ratios, 2023–2025 (library raw/town/dra-tax-rates.csv); Jackson School District High School Options FAQ
   - source: https://www.revenue.nh.gov/about-dra/municipal-and-property-division/property-bureau/equalization
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Kept for the reason, the revaluation, which the site's data doesn't give. Jackson's DRA rates, ratios and valuations for 2014–2025 are in the site's data (property_tax, Jackson district); these figures match it (checked November 15, 2026). The town's hazard mitigation plan also calls 2024 "the year of a town revaluation" (community-and-families, town-housing 4). Raw: raw/money/state-data/dra-tax-rates-jackson-bartlett-conway.csv; raw/money/jgs/hs-options-faq.txt

## district-consolidation-history: Consolidation and Cooperative District Studies Involving Jackson

- kind: local
- question_type: governance_money
- description: Studies, votes and discussions about cooperative districts, consolidation or sharing schools

1. In 2018–19, SAU 9 formed an ad hoc study committee, with members from the member school boards, to understand the eight-town tuition contracts with Conway, explore options and impacts, and learn about governance options for a multi-district SAU. It heard presentations on "Forms of School Organization in NH" (cooperative districts, AREA agreements, tuition agreements and joint maintenance agreements).
   - citation: SAU 9 memo, "Summary Report of SAU 9 Study Committee," Kevin Richard to SAU 9 School Board, May 2, 2019
   - source: https://drive.google.com/file/d/15b0kAKZiHRsv7eAPRyYjbNeiIth4PSEZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: SAU-wide. Text: "The SAU 9 study committee was formed as a result of conversation at the December SAU 9 School Board Meeting ... Overview of 'Forms of School Organization in NH' ... cooperative school districts, AREA agreements, Tuition Agreements, Joint Maintenance Agreements." Linked from https://www.sau9.org/tuitions. Raw: raw/money/study/study-committee-summary-report.*
2. On March 5, 2020, Jackson voters approved Article 7, creating a three-member Cooperative School District Planning Committee under RSA 195:18. SAU 9's superintendent said all districts in the SAU had the article on their warrants and that Bartlett had approved its article.
   - citation: Jackson School District Warrant 2020, Article 7; Annual Meeting Minutes, March 5, 2020
   - source: https://drive.google.com/file/d/1qv5BMi8ZUvscgftizz62HKekdSQ4Q_3y/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "To see if the School District will vote to establish a Cooperative School District Planning Committee in accordance with RSA 195:18 comprised of three (3) members ... Mr. Richard explained that all the Districts in the SAU have this Article on their warrant. Bartlett has approved their Article. Sara Clemons would like to know if this means that we may consider tuitioning out in the future. APPROVED". The library topic gov-cooperative-forming explains RSA 195:18. Raw: raw/money/warrants/w-2020.*, raw/money/meetings/am-2020.*
3. The planning committees of Albany, Bartlett, Conway, Eaton, Freedom, Jackson, Madison and Tamworth met as a joint planning board from September 23, 2021, studying the high school agreement (and the middle school agreement) with Attorney Matt Upton. On January 26, 2022 they voted unanimously, town by town, not to pursue a cooperative school district, and recommended another committee to investigate other forms of school organization.
   - citation: Superintendent's Report (Kevin Richard), Jackson School District 2022 Annual Report, pp. 15–16
   - source: https://drive.google.com/file/d/1pOmM-Vx0XVOrCyTGWfm7tlu1TGwnvfwP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: SAU-wide. Text: "On January 26, 2022 the committee met with Attorney Upton ... 'Should the committee go forward with the formation of a cooperative school district?' With a unanimous vote, each town voted not to pursue a cooperative school district. Even though the committee did not move forward ... each town strongly recommended the formation of another committee to investigate alternative options". The report dates the town articles to spring 2021; Jackson's own article passed in March 2020 (fact 2). Transcribed from image. Raw: raw/money/annual-reports/ar-2022.* Added November 13, 2026: Freedom's March 2023 minutes add that a "Joint Maintenance Unit committee ... also did not move forward" after the cooperative study, and that each town elected its three committee members (town/Freedom/money-and-governance.md).
4. No study, warrant article or board vote on merging the Jackson and Bartlett school districts, or on sending Jackson's K–6 students to Bartlett, was found in Jackson's warrants and annual meeting minutes for 2019–2026, its 2025–26 Finance Committee minutes, or SAU 9 board minutes from 2019–2021 and July–September 2026. At the 2026 meeting, board chair Jessica DellaValla said "Leaving Bartlett was not a consideration to this Board" when asked about middle school choice.
   - citation: Jackson School District Annual Meeting Minutes, March 5, 2026, Article 9
   - source: https://drive.google.com/file/d/16gP8PVjAV-V-7QnDFMButI5dgFgXZ66L/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Is there any consideration of offering choice for middle school? Ms. DellaValla spoke to this topic. Leaving Bartlett was not a consideration to this Board." The "not found" part is a statement about the documents searched, listed in raw/money/. Raw: raw/money/meetings/am-2026.*
5. Jackson's 2026–2029 tuition contract with Bartlett says it "will allow for the reopening of discussion for sixth (6th) grade consideration."
   - citation: Bartlett/Jackson Tuition Contract (2026–2029), opening paragraph
   - source: https://drive.google.com/file/d/15EfUC6h-Afo2KMn8pwWfYZXfSYXojxoU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The contract concerns Jackson students in grades seven (7) and eight (8) who attend the Bartlett School. This contract will allow for the reopening of discussion for sixth (6th) grade consideration." Scanned; transcribed from image p. 1 (viewed). Raw: raw/money/contracts/sau9-contract-7-8-bartlett-jackson-current.pdf, -p1.png, .ocr.txt
6. Research on what merging small districts or schools does to costs and results is summarized in the library topic research-district-consolidation; how a cooperative district is formed or left is in gov-cooperative-forming and gov-cooperative-withdrawal.
   - citation: library cross-reference
   - source: https://gc.nh.gov/rsa/html/XV/195/195-18.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Jackson
   - note: Pointer only; no new statewide facts here.

## high-school-tuition-options: High School Choice for Jackson Families and the March 2026 Votes

- kind: local
- question_type: local_practice
- description: High school options for districts without a high school (already in `additional-data/district-practices.md`)

1. On September 18, 2023, the Jackson School Board voted 5-0-0 to withdraw from its high school contract with the Conway School District.
   - citation: Jackson School Board Minutes, September 18, 2023
   - source: https://drive.google.com/file/d/1hFzSFNJ4Bvazr4W1WnUhWR0IaSFwBrMo/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Ms. DellaValla made a motion to withdraw from the Conway contract. Mr Dougherty seconded. 5-0-0." Raw: raw/money/jsb-minutes/jsb-2023-09-18.*
2. At the March 5, 2026 meeting, Jackson voters approved the 10-year Fryeburg Academy agreement (Article 7) by secret ballot, 139 to 30, and the 5-year Kennett agreement with Conway (Article 8) by secret ballot, 129 to 17. Both had been recommended by the school board 5-0-0.
   - citation: Jackson School District Annual Meeting Minutes, March 5, 2026, Articles 7 and 8
   - source: https://drive.google.com/file/d/16gP8PVjAV-V-7QnDFMButI5dgFgXZ66L/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The count was 139 in favor, 30 against. Article 7 PASSED" and "The ballot vote was 129 in favor, 17 against. Article 8 Passed". Voters also restricted reconsideration of Article 7. Raw: raw/money/meetings/am-2026.*
3. At the same meeting, a resident gave the per-student amounts of the two contracts as $26,788 for Fryeburg and $27,855 for Conway, and board member Majka Burhardt said the current Kennett contract "requires payment for students who are not attending Kennett - paying for empty seats." Board member James Glazer said Jackson previously sent 3% of Kennett's students but paid 13%, that tuition was about $22,000 in 2017 (closer to $26,000 with the bond and upkeep payments), and that Jackson was paying $39,000 that year.
   - citation: Jackson School District Annual Meeting Minutes, March 5, 2026, Article 8 discussion
   - source: https://drive.google.com/file/d/16gP8PVjAV-V-7QnDFMButI5dgFgXZ66L/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Barbara Hamel- amounts of each of the contracts were $26788 Fryeburg and $27855 for Conway ... Ms. Burhardt pointed out that the current Kennett contract requires payment for students who are not attending Kennett - paying for empty seats ... Previously Jackson sent 3% of the Kennett population, but paid 13%. In 2017 - the tuition was $22,000, but when you add in the bond payment and the upkeep payment, we were paying closer to $26,000 per student. This year we are paying $39,000." Statements made at the meeting, as recorded. Raw: raw/money/meetings/am-2026.*
4. Board chair Jessica DellaValla said at the meeting that Conway insisted on the 5-year term for the Kennett contract, and that if voters rejected both contracts the question would go back to the board for a new plan.
   - citation: Jackson School District Annual Meeting Minutes, March 5, 2026
   - source: https://drive.google.com/file/d/16gP8PVjAV-V-7QnDFMButI5dgFgXZ66L/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Tim Scott - why is the Kennett contract 5 years and Fryeburg is 10? Ms. DellaValla explained that Conway insisted on that." and "What happens if the majority votes no on both? Ms. DellaValla responded that it would come back to the Board to figure out a new plan." Raw: raw/money/meetings/am-2026.*
5. Jackson's High School Options FAQ says the board pursued two high school contracts because over 72% of Jackson voters directed it to (in its community survey) and because Jackson students already attended both schools: 7 at Fryeburg Academy and 19 at Kennett at the time the FAQ was written.
   - citation: Jackson School District High School Options FAQ, "High School Contract Overview" question 4
   - source: https://docs.google.com/document/d/1W_J4PMEjzDkXRLuSGMhwKyyt2UXjZycgKGBfr2ejxQ4/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: FAQ text: "Over 72% of Jackson voters directed the board to negotiate two contracts ... 7 Jackson students currently attend Fryeburg Academy. 19 Jackson students attend Kennett High School." The FAQ does not date this line. Raw: raw/money/jgs/hs-options-faq.txt
6. Starting in 2027-28, a Jackson resident in grades 9–12 may attend either Kennett High School (under the new Conway contract) or Fryeburg Academy (under the new agreement), with Jackson paying tuition at either. Board chair Jessica DellaValla said Jackson will not pay for a student to attend both schools.
   - citation: Jackson Warrant 2026, Articles 7–8; Annual Meeting Minutes, March 5, 2026; JGS "High School Options" page
   - source: https://jgs.sau9.org/324669_2
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Warrant: "for the purpose of educating Jackson students in grades 9 through 12 who wish to attend Fryeburg Academy" and "... who wish to attend Kennett High School". Minutes: "We are not paying for a student to go to both schools." Raw: raw/money/jgs/jgs-high-school-options.*; raw/money/meetings/am-2026.*
7. A Jackson family chooses Fryeburg Academy by applying through the academy's regular day-student admissions process; all Jackson students are eligible for "non-selective admission" unless the student poses a documented safety risk or the special education team decides another setting is more appropriate. Jackson must tell the academy the estimated number and names of students by March 1 for the next year.
   - citation: Jackson–Fryeburg Agreement, Sections 5–6
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "all Jackson students shall be eligible to apply for non-selective admission and attend the Academy ... The process will be consistent with the Academy's admissions processes for all other Academy day students ... no later than March 1." Page 4 viewed. Fryeburg's day-student page asks for an application, three recommendations, transcripts and an interview (raw/money/fryeburg/fa-day-students.*). Raw: raw/money/contracts/sau9-contract-9-12-jackson-fryeburg-2027.*
8. Once a Jackson student enrolls at Kennett or Fryeburg under the new contracts, the student may stay there until graduation, subject to good conduct and eligibility. The Fryeburg agreement keeps parents' rights to seek a change of school under RSA 193:3, RSA 194-D, the EFA law and RSA 194:24 (manifest hardship).
   - citation: Jackson/Conway Agreement (2027), Section I; Jackson–Fryeburg Agreement, Sections 1 and 5
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Kennett text: "once a Jackson student enrolls at Kennett High School, the student will remain in attendance until graduation or age twenty-two (22) subject to good conduct". Fryeburg text: "subject to the parent/guardian or adult student's right to seek a change of school or assignment pursuant to RSA 193:3, RSA 194-D, the EFA statute (NH RSA 194-F) or RSA 194:24". The statewide rules are library topics change-of-school-assignment and gov-tuition-towns. Raw: raw/money/contracts/*.ocr.txt
9. Jackson's 2026 open enrollment vote set the share of its students who may attend open enrollment schools outside the district at 0%, so RSA 194-D open enrollment is not a route out of Jackson under that vote; the vote also opened JGS K–6 to nonresident applicants.
   - citation: Jackson Warrant 2026, Article 6 (approved March 5, 2026)
   - source: https://drive.google.com/file/d/10mSffksL1k97gsgdAhCEoLiWf-Hes0op/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: See district-board-and-public-input 1. Library topic open-enrollment-status explains the statewide law and the failed 2026 bills. Raw: raw/money/warrants/w-2026.*
10. For eighth graders choosing for 2027-28, the Finance Committee noted in October 2026 that families do not have to decide which high school until spring, and that the JGS principal is keeping eighth-grade families informed; members "stressed the need not to pressure families."
   - citation: Jackson Finance Committee Minutes (draft), October 29, 2026
   - source: https://drive.google.com/file/d/1j2Q4GBFOX-PiBgXTL2LhM8gNQPyz2Z7M/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "the biggest area is knowing which students will be attending which high school. This decision does not have to be made until spring ... Erin Messer said communication is good with eighth-grade families ... They stressed the need not to pressure families." Raw: raw/money/finance-committee/fc-2026-10-29-draft.*

## district-board-and-public-input: Jackson's March 2026 Open Enrollment Vote

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. Jackson voters also adopted RSA 194-D (Article 6) to make JGS grades K–6 an open enrollment school that nonresident students may apply to, subject to board admission criteria and class-size and school-size limits, and set the share of Jackson's K–12 students who may attend open enrollment schools outside the district at 0%.
   - citation: Jackson School District Warrant 2026, Article 6; Annual Meeting Minutes, March 5, 2026
   - source: https://drive.google.com/file/d/10mSffksL1k97gsgdAhCEoLiWf-Hes0op/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Warrant text: "adopt the provisions of NH RSA Chapter 194-D to designate the Jackson Grammar School grades Kindergarten through six as an Open Enrollment Elementary School ... and further to limit the percentage of resident students grades Kindergarten through 12th grade attending open enrollment schools located outside of the District to 0% of the District's total enrollment." Minutes: "Motion Carried, Article Approved". The statewide rule is library topic open-enrollment-status. Raw: raw/money/warrants/w-2026.*, raw/money/meetings/am-2026.*

## district-tuition-contracts: Jackson's Tuition Agreements With Conway, Fryeburg Academy and Bartlett

- kind: local
- question_type: governance_money
- description: A district's tuition contracts and agreements with other districts and schools: terms, cost formulas, caps, length, renewal, transportation and special education

1. Jackson's current high school contract with the Conway School District was approved by the State Board of Education on May 21, 2003, as part of the plan to build a new Kennett High School for eight towns. It requires Jackson to send at least 90% of its grade 9–12 pupils to Conway, and Conway to give them "the same opportunities" as Conway residents.
   - citation: Conway Tuition Agreement, Grades 9-12 (Jackson), Section I and signature page
   - source: https://drive.google.com/file/d/1ewDeGfHpCcDwouiJsCcI7dNBfE9cJnba/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Jackson School District shall send at least ninety percent (90%) of its pupils, grades 9 through 12 ... to Conway for schooling; and Jackson School District shall be responsible for the transportation methods and expenses"; "Reviewed and approved on the 21st day of May, 2003, by the New Hampshire State Board of Education." Scanned; transcribed from image (p. 9 viewed). Listed as current on https://www.sau9.org/tuitions; the copy downloaded today is identical (same MD5) to the November 8 copy. Raw: raw/money/contracts/sau9-contract-9-12-jackson-conway-current.pdf, .ocr.txt, -p1…p11.png
2. Under the current Kennett contract, each sending district's share of the high school's operating cost is 35% based on its share of the towns' total equalized property value and 65% based on its share of average daily membership in attendance at the high school; bond payments and the facilities maintenance fund are shared by equalized value alone.
   - citation: Conway Tuition Agreement (Jackson, 9-12), Section X.A.3, X.B.1 and X.D.1
   - source: https://drive.google.com/file/d/1ewDeGfHpCcDwouiJsCcI7dNBfE9cJnba/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Each district's percentage of the operating expenses of the high school ... shall be a combination of 35% of the town's equalized value as a percentage of the total equalized value and 65% of the town's average daily membership in attendance"; "The method of apportioning capital expenses (bond issues) shall be the town's equalized value". Transcribed from image p. 5–7. Raw: as fact 1
3. For 2019-20, SAU 9's calculation gave Jackson 3.67% of Kennett's attendance and 8.68% of the towns' equalized value, for a combined 5.4235% of the high school operating budget; Conway's combined share was 43.8295% and Bartlett's 15.748%.
   - citation: SAU 9 Study Committee Presentation, February 28, 2019, slide 19 ("Based on 2019-2020 High School Tuition Calculations")
   - source: https://drive.google.com/file/d/17rVLU-Ui99yNkgX6qk1FnXa93mS0MpIc/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Jackson 3.67% 8.68% 5.4235%". The board's February 2026 comparison put the current maintenance-fund share, based on equalized value, at "Approximately 8.37% with current EV". Raw: raw/money/study/study-committee-presentation-2019-02-28.*
4. Under the current contract, Conway sets each district's estimated cost from its approved budget plus an inflation factor of the Northeast urban CPI plus 2.5%, adjusted each year to actual costs, and must notify sending districts by November 30. Jackson pays quarterly (September 1, December 1, March 1, June 1), with a late charge of 1% over prime.
   - citation: Conway Tuition Agreement (Jackson, 9-12), Sections X.A.2, X.A.4 and XI
   - source: https://drive.google.com/file/d/1ewDeGfHpCcDwouiJsCcI7dNBfE9cJnba/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "an inflation factor equal to US Department of Labor Consumer Price Index - Size A - Northeast Urban (October of current year) plus 2.5%; plus or minus the net actual expenses for the prior year ... but in no event later than November 30th". Raw: as fact 1
5. Under the current contract, Jackson pays all costs of special education placements outside Conway, any in-district services beyond the regular program (aides, counseling and the like), and any due process costs, attorney fees, awards and compensatory education; Conway's team makes IEP and 504 decisions within the regular program.
   - citation: Conway Tuition Agreement (Jackson, 9-12), Section I
   - source: https://drive.google.com/file/d/1ewDeGfHpCcDwouiJsCcI7dNBfE9cJnba/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Jackson School District shall bear all the cost of any such special program or facility ... The Jackson School District shall bear the cost of any due process proceedings, attorney fees, awards, out-of-district placements, and compensatory education awards." Raw: as fact 1
6. The current contract runs a minimum of 20 school years and then continues year to year until either side gives notice at least three full fiscal years ahead. Disputes go to a three-person panel whose decision is final. SAU 9's 2019 study committee described the 9–12 agreements as 20-year agreements beginning July 1, 2007; the 2003 text expected the new building to open in September 2006.
   - citation: Conway Tuition Agreement (Jackson, 9-12), Sections II, III and XIII; SAU 9 Study Committee Presentation, slide 5
   - source: https://drive.google.com/file/d/1ewDeGfHpCcDwouiJsCcI7dNBfE9cJnba/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "shall continue for a minimum term of twenty (20) school years"; "at least the third (3rd) full fiscal school year ending June 30 following the school year during which the notice is given"; slide: "Twenty year (20) agreement beginning on July 1, 2007". Raw: as fact 1; raw/money/study/study-committee-presentation-2019-02-28.*
7. Jackson's new Kennett High School agreement with the Conway School District runs five school years from about September 1, 2027 (ending June 30, 2032, per the warrant). Jackson "shall send any number of its pupils," and Conway must accept them on the same terms as Conway residents; no Jackson student will be denied enrollment during the term, subject to good conduct and eligibility.
   - citation: Jackson/Conway Tuition Agreement, Grades 9-12 (2027), Sections I and II; Jackson Warrant 2026, Article 8
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Jackson School District shall send any number of its pupils, grades 9 through 12 ... No Jackson student will be denied enrollment during the term of this agreement ... commence at the inception of the school year around September 1, 2027 and shall continue for a term of five (5) school years." Scanned; transcribed from image (p. 4 viewed). Same MD5 as the November 8 copy. Raw: raw/money/contracts/sau9-contract-9-12-jackson-conway-2027.pdf, .ocr.txt, -p1…p9.png
8. Under the new Kennett contract, Conway sets Jackson's cost each year from Conway's most recent DOE-25 high school current expenditures (excluding transportation) and attendance (ADMA), plus an inflation factor of the Northeast urban CPI plus 13%, with CPI plus 13% capped at 20% in any year. Conway must give Jackson its estimate by November 15.
   - citation: Jackson/Conway Tuition Agreement (2027), Section VIII.A.1–2
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The Conway School Board shall annually set Jackson's cost based upon Conway's most recent DOE 25 and ADMA, plus an inflation factor equal to US Department of Labor Consumer Price Index - Size A - Northeast Urban (October of current year) plus thirteen percent (13%). CPI plus thirteen percent (13%) shall not exceed twenty percent (20%) in any given year." Page 4 viewed. Raw: as fact 1
9. In addition to tuition, Jackson pays each year one-fifth of its share of Kennett's five-year Capital Improvement Plan into the Kennett High School Maintenance Trust Fund, with its share based on the prior year's attendance (ADMA), as long as Conway pays its own share. If Conway proposes capital work beyond the plan, Jackson gets four months' notice and may decline, but a district that declines is no longer a party to the agreement.
   - citation: Jackson/Conway Tuition Agreement (2027), Section VIII.B and Appendix B (CIP Plan - Kennett High School)
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Each sending district shall annually pay one-fifth (1/5th) of the projected five- (5-) year CIP plan based on Appendix B. Calculation of the sending district share shall be based on each district's ADMA for the prior year ... Thereafter, the district electing not to participate will no longer be considered a party to this agreement". The board's comparison estimated the maintenance payment at about 3% with current ADM, or $20,900 a year. Raw: as fact 1; raw/money/jgs/hs-contract-comparison-2026.*
10. Under the new Kennett contract, Jackson pays for transportation, direct special education costs not in the regular program, out-of-district placements, and due process costs; Conway must keep running the Mount Washington Valley Career and Technical Center and give Jackson students equal access to its courses.
   - citation: Jackson/Conway Tuition Agreement (2027), Sections I, VI and VIII.A.3
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Conway commits to operating the Mt. Washington Valley Career and Technical Center (MWVCTC) and offer Jackson equal access to all MWVCTC course offerings for students enrolled at Kennett High School"; "Jackson will pay direct costs for special education or other specialized programs not included, or unable to be provided in the regular operation of the school." Raw: as fact 1
11. The new Kennett contract ends after its five-year term if either district gives written notice before the end of the third fiscal year; otherwise it continues year to year, and later notice must give at least three full fiscal years. Disputes go first to a three-person panel including a jointly chosen private mediator, then to the State Board of Education. The State Board approved it on August 13, 2026.
   - citation: Jackson/Conway Tuition Agreement (2027), Sections II, III, XI and State Board addendum
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "This Agreement shall terminate at the end of such minimum term if either party gives to the other, at any time prior to the expiration of the third (3rd) fiscal school year ending June 30 of such minimum term, written notice"; addendum: "The State Board of Education acknowledges the approval of this tuition agreement at its regular August 13, 2026 meeting." Raw: as fact 1
12. Under the new Kennett contract, the Conway School Board meets with sending boards up to twice a year at Jackson's request, and Jackson receives achievement, discipline and attendance data on its students and the program of studies.
   - citation: Jackson/Conway Tuition Agreement (2027), Sections IV and VII
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The Conway School Board will meet jointly with all School Boards (all together) who send pupils to the high school ... up to two (2) times a year at the request of the Jackson School District". Raw: as fact 1
13. Jackson's agreement with Fryeburg Academy runs ten years, from July 1, 2027 to June 30, 2037, and renews for one more three-year period unless either side gives written notice before July 1, 2035. Fryeburg Academy "shall accept up to all resident high school students from Jackson" in grades 9–12; Fryeburg may reopen the contract for negotiation if the estimated enrollment exceeds 40 students.
   - citation: Agreement Between Jackson School District and Fryeburg Academy, Sections 1, 3 and 6
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "This agreement shall be for ten (10) years, commencing July 1, 2027, and ending on June 30, 2037. This agreement will be renewed for up to one (1) additional three-year period unless either party notifies the other in writing prior to July 1, 2035"; "Should the estimated enrollment exceed 40 students, Fryeburg Academy reserves the right to reopen the contract for negotiation." Scanned; transcribed from image (pp. 3–4 viewed). Same MD5 as the November 8 copy. Raw: raw/money/contracts/sau9-contract-9-12-jackson-fryeburg-2027.pdf, .ocr.txt, -p1…p16.png
14. Jackson's tuition per student at Fryeburg Academy is set at the academy's Commuter Day rate plus a "guaranteed admission premium" of no more than 20% above that rate, which "secures student admission and supports ongoing capital improvements and program development." Jackson students who enrolled at Fryeburg before the agreement ("Legacy Students") pay no premium.
   - citation: Jackson–Fryeburg Agreement, Section 4(a)–(c)
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "set at the Commuter Day rate as estimated for the following academic year plus a guaranteed admission premium for Jackson students not to exceed twenty percent (20%) above the Commuter Day rate"; "students from Jackson who enrolled at the Academy prior to the effective date of this Agreement ('Legacy Students') shall continue attendance without incurring any admission premium." **Derived**: with Fryeburg's posted 2027-28 Commuter Day tuition of $22,500, the most Jackson could be charged per regular student is $27,000. Raw: as fact 1
15. Fryeburg Academy must give Jackson a written tuition estimate by November 1 each year. Jackson pays in four installments (40% by August 15, 40% by February 1, 15% by May 15 and the balance by June 30), with tuition counted by semester on October 1 and April 1 and adjusted per day for students who enroll or leave after April 1.
   - citation: Jackson–Fryeburg Agreement, Section 4(a), (d) and (f)
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "On or before August 15th, the District shall pay 40% of the estimated tuition ... On or before February 1st ... 40% ... On or before May 15th ... 15% ... On or before June 30th, the District shall pay the remaining tuition". Page 3 viewed. Raw: as fact 1
16. Special education is not included in Fryeburg tuition. Each year by November 1, Fryeburg's head of school and SAU 9's superintendent and special education representative jointly develop a special education budget for Jackson students, which goes to Jackson for its operating budget; Jackson agrees it must pay for all services an IEP team orders, and SAU 9 employs the educational technicians who support Jackson students at the academy.
   - citation: Jackson–Fryeburg Agreement, Sections 4(g) and 8(b)
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The cost of the special education services provided by the Academy to the District students pursuant to this agreement is not included in the tuition payments ... a budget for all separate courses, programs, and any direct services for the District's students with special needs will be developed and approved jointly ... the District shall employ through its SAU No. 9 educational technicians". Fryeburg may deny enrollment where it lacks an appropriate program or the student is a safety risk "as determined jointly by Jackson's LEA representative and the Academy, as well as the IEP Team" (Section 5, p. 4 viewed). Raw: as fact 1
17. Under the Fryeburg agreement, Jackson students get breakfast and lunch included in tuition, the same co-curricular opportunities and fees as other day students, and a laptop or similar device; Fryeburg meets with the Jackson School Board three times a year and sends an annual report. Part-time home-educated or non-public students are prorated (one class 25%, two 50%, three 75%, four or more 100%), and homeschoolers using only co-curriculars are charged 25%.
   - citation: Jackson–Fryeburg Agreement, Sections 7, 9, 11, 12 and 20
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "All enrolled students will have access to breakfast and lunch with associated costs included in the tuition rate"; "For homeschool students accessing co-curriculars but not taking any classes, the tuition charge will be 25%." (p. 11 viewed). Raw: as fact 1
18. Fryeburg Academy may end the agreement within 30 days if Jackson fails to pay tuition lawfully due; if the academy loses its Maine approval and does not fix it within two years, Jackson may give notice and leave at the end of the next full school year. Students already enrolled when the agreement ends may finish high school at the academy under its terms.
   - citation: Jackson–Fryeburg Agreement, Sections 13 and 21
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "in the event that Jackson fails to pay its tuition that is lawfully due and owing to the Academy, the Academy shall have the right to terminate this agreement within thirty (30) days." Raw: as fact 1
19. The Fryeburg agreement says Jackson and the academy will "work collaboratively to explore whether EFAs may be used by Jackson families to reduce the cost to Jackson of the tuition paid hereunder."
   - citation: Jackson–Fryeburg Agreement, Section 4(h)
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Contract term only; how EFAs work is another agent's area and library topics on EFAs. Page 4 viewed. Raw: as fact 1
20. Fryeburg Academy's board chair signed the agreement on July 9, 2026, and the State Board of Education approved it on August 13, 2026 under RSA 194:22 and 194:23, II.
   - citation: Jackson–Fryeburg Agreement, signature and approval pages (pp. 14–16)
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Chris Gordon (Jul 9, 2026 16:42:35 EDT) ... pursuant to NH RSA 194:23(II) and RSA 194:22, the above Agreement is approved by the State Board of Education ... Date: August 13, 2026". Raw: as fact 1
21. Jackson's contract with the Bartlett School District for grades 7 and 8 runs three years, July 1, 2026 to June 30, 2029. Jackson sends all its grade 7–8 students to Bartlett, except students placed elsewhere by an IEP or 504 team, home-educated students, students in private or chartered schools, students reassigned under RSA 193:3, open enrollment students and EFA students.
   - citation: Bartlett/Jackson Tuition Contract (2026–2029), opening paragraph and Section IV
   - source: https://drive.google.com/file/d/15EfUC6h-Afo2KMn8pwWfYZXfSYXojxoU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "effective for the three-year period of July 1, 2026 through June 30, 2029 ... Jackson shall send all of its students, grades seven (7) and eight (8) to Bartlett for schooling and shall be responsible for the transportation methods and expenses". Scanned; transcribed from image (p. 1 viewed). Same MD5 as the November 8 copy. Raw: raw/money/contracts/sau9-contract-7-8-bartlett-jackson-current.pdf, .ocr.txt, -p1…p6.png
22. Bartlett's tuition per Jackson student is its prior-year elementary general fund spending (DOE-25 page 7, line 14), minus transportation, special education costs not part of the regular program, and Jackson's payments for Bartlett staff working at JGS, plus the Northeast urban CPI plus 2.5%, plus or minus the prior year's actual net costs, divided by the prior year's average daily membership. Jackson also pays a yearly rental charge of 2% of the per-pupil tuition, and pays special education and specialized program costs directly. Tuition is billed quarterly by SAU 9.
   - citation: Bartlett/Jackson Tuition Contract (2026–2029), Sections XI–XII
   - source: https://drive.google.com/file/d/15EfUC6h-Afo2KMn8pwWfYZXfSYXojxoU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Jackson shall pay an annual per pupil rental charge of two percent (2%) of the tuition calculation per pupil as calculated by the SAU office and approved by the Department of Education." The yearly calculation report is to be appended as a rider, but no rider is in the posted PDF. Raw: as fact 1
23. Under the Bartlett contract, the two boards decide by October 1 of the second year whether to renew for another three years; without mutual agreement it ends after the third year. A renewal without material changes needs only board motions and a letter; material changes (those affecting tuition or attendance) go to both districts' voters. Seventh graders enrolled when it ends may finish eighth grade at Bartlett.
   - citation: Bartlett/Jackson Tuition Contract (2026–2029), Sections I, II and XIII
   - source: https://drive.google.com/file/d/15EfUC6h-Afo2KMn8pwWfYZXfSYXojxoU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Both Parties shall meet, confer no later than September 1, of the second year of the term and decide no later than October 1, whether they mutually wish to renew ... Amendments which do not affect the tuition rate or student attendance shall not be deemed material". Page 1 viewed. Raw: as fact 1
24. Under the Bartlett contract, the Jackson and Bartlett school boards meet four times a year, and Jackson may have one voting member on Bartlett's Policy Committee and on academic or co-curricular committees affecting grades 7–8. Disputes go to the SAU 9 superintendent and then the Commissioner of Education. The State Board approved the contract on August 13, 2026.
   - citation: Bartlett/Jackson Tuition Contract (2026–2029), Sections IX–X and State Board addendum
   - source: https://drive.google.com/file/d/15EfUC6h-Afo2KMn8pwWfYZXfSYXojxoU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The Jackson and Bartlett School Boards will meet together four (4) times annually ... the Jackson School Board may have one (1) voting representative on the Bartlett Policy Committee". Raw: as fact 1
25. Jackson voters authorized the 2026–2029 Bartlett contract (Article 9) at the March 5, 2026 meeting. A resident noted the town had voted on this contract every three years.
   - citation: Jackson School District Annual Meeting Minutes, March 5, 2026, Article 9
   - source: https://drive.google.com/file/d/16gP8PVjAV-V-7QnDFMButI5dgFgXZ66L/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Jerry Dougherty - this town has voted at this meeting every three years on this contract ... Motion Carried, Article Approved". Earlier three-year contracts were approved in 2019 (Article 6). Raw: raw/money/meetings/am-2026.*, am-2019.*
26. None of Jackson's four posted agreements (Kennett 2003, Kennett 2027, Fryeburg Academy 2027 and Bartlett 2026) is an AREA agreement under RSA 195-A. The two Kennett contracts and the Fryeburg agreement are tuition contracts approved under RSA 194:22, which makes an approved contract school "a high school maintained by the district"; the Fryeburg agreement also cites RSA 194:23, II (public academies), and the Bartlett contract was submitted to the State Board under RSA 194:22, according to the 2026 warrant.
   - citation: Jackson/Conway Agreement (2027), Section XII; Conway Tuition Agreement (2003), Section XIV; Jackson–Fryeburg Agreement, Section 1; Jackson Warrant 2026, Article 9; RSA 194:22
   - source: https://gc.nh.gov/rsa/html/XV/194/194-22.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Kennett 2027 text: "receives approval of the State Board, pursuant to RSA 194:22, designating the high school as a high school maintained by each district". Fryeburg: "Pursuant to NH RSA 194:22 and 194:23(II), upon approval by the State Board of Education and the citizens of the District, the Academy shall be deemed a high school maintained by Jackson". No contract mentions RSA 195-A. The statewide rules are library topics gov-area-agreements, gov-tuition-towns and gov-public-academies. Raw: raw/money/contracts/*.ocr.txt; raw/money/rsa/rsa-194-22.*
27. The Fryeburg agreement also approves Fryeburg Academy as a "school tuition program" under RSA 193:3, VI and VII, citing "distance considerations" as the reason for a contract in another state. RSA 193:3, VI lets a district with no school for a grade either assign all children to approved tuition schools or let each parent choose among them.
   - citation: Jackson–Fryeburg Agreement, recitals; RSA 193:3, VI–VII
   - source: https://gc.nh.gov/rsa/html/XV/193/193-3.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Jackson
   - note: Contract text: "the Jackson School District Board has determined that in order to offer meaningful school choice to its residents that distance considerations make it necessary to make a contract in another state and hereby approves of the Academy as a school tuition program in accord with RSA 193:3(VI) and (VII)." RSA text: "The district may either assign all children to schools that have been approved as a school tuition program, or allow each child's parent to choose a school from among schools that have been approved as a school tuition program." Raw: raw/money/contracts/sau9-contract-9-12-jackson-fryeburg-2027.ocr.txt; raw/money/rsa/rsa-193-3.*
28. The next decision points in Jackson's contracts are: for Bartlett (grades 7–8), the two boards must meet by September 1, 2027 and decide by October 1, 2027 whether to renew past June 30, 2029; for the new Kennett contract, written notice before June 30, 2030 ends it on June 30, 2032, otherwise it continues year to year; for Fryeburg Academy, notice before July 1, 2035 stops the three-year extension past June 30, 2037 (**derived** from each contract's term clauses).
   - citation: Bartlett/Jackson Tuition Contract, Section I; Jackson/Conway Agreement (2027), Sections II–III; Jackson–Fryeburg Agreement, Section 3
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Derivation: Bartlett term July 1, 2026–June 30, 2029, "the second year of the term" is 2027-28; Kennett term starts about September 1, 2027, so "the third (3rd) fiscal school year ending June 30" is June 30, 2030; Fryeburg: "prior to July 1, 2035, two years prior to expiration". Raw: raw/money/contracts/*.ocr.txt
29. Until the agreement starts on July 1, 2027, Jackson does not pay tuition for students attending Fryeburg Academy; families pay. The district's FAQ says "Families fund the intervening years," and a board member said at the 2026 meeting that "right now the town does not pay for the student to go to Fryeburg."
   - citation: Jackson School District High School Options FAQ, "High School Contract Details" question 9; Annual Meeting Minutes, March 5, 2026
   - source: https://docs.google.com/document/d/1W_J4PMEjzDkXRLuSGMhwKyyt2UXjZycgKGBfr2ejxQ4/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: FAQ: "Families fund the intervening years. Fryeburg Academy has offered to work with families in need of financial aid so interested families should reach out to them." Minutes: "Ms. Foley-Marsello - right now the town does not pay for the student to go to Fryeburg. Ms. Hamel spoke about parents currently paying 100%". Raw: raw/money/jgs/hs-options-faq.txt; raw/money/meetings/am-2026.*
30. Under the agreement, Fryeburg Academy adopted a need-blind admissions policy for students entering grade 9 in fall 2026: admission decisions are made without regard to finances, and the academy meets 100% of demonstrated financial need for admitted students. The commitment applies only to fall 2026 entrants and is reviewed yearly.
   - citation: Jackson–Fryeburg Agreement, Section 4(b)
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "the Academy will implement a need-blind admissions policy for students applying as incoming 9th graders for the 2026-2027 academic year ... the Academy shall meet 100% of demonstrated financial need ... This commitment applies only to students entering in Fall 2026". Page 3 viewed. Raw: raw/money/contracts/sau9-contract-9-12-jackson-fryeburg-2027.*
31. Jackson students already enrolled at Fryeburg Academy before July 1, 2027 become "Legacy Students": from 2027-28 Jackson pays their tuition at the commuter day rate with no admission premium. The district's finance committee noted in October 2026 that students at Fryeburg before the contract were privately funded and considered unenrolled from the public schools, and that all Jackson students at Fryeburg will be under the contract, including for special education.
   - citation: Jackson–Fryeburg Agreement, Section 4(b); Jackson Finance Committee Minutes (draft), October 29, 2026
   - source: https://drive.google.com/file/d/1j2Q4GBFOX-PiBgXTL2LhM8gNQPyz2Z7M/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Minutes: "Students who attended Fryeburg Academy prior to the tuition contract were privately funded and considered unenrolled from the public school. Now, all students attending Fryeburg are under the tuition contract and this would include special education." Raw: raw/money/finance-committee/fc-2026-10-29-draft.*; contract as above
32. Before the new contracts, Jackson's current Kennett contract required it to send at least 90% of its high school students to Conway, and the board's comparison describes the current contract as barring a tuition contract with another school.
   - citation: Conway Tuition Agreement (Jackson, 9-12), Section I; Jackson School Board, "High School Contract Comparison" (February 6, 2026), p. 2
   - source: https://files.smartsites.parentsquare.com/10273/updated_hs_contract_comparison_2026_district_vote_.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Comparison text under "CURRENT CONTRACT (2007-2027)": "90% attendance requirement. May not enter a tuition contract with another school." The bar on other contracts is the board's summary; no clause with that wording was found in the 2003 text. Raw: raw/money/jgs/hs-contract-comparison-2026.*
33. All of SAU 9's current and 2027 tuition contracts, plus the 2019 study committee presentations, are posted on SAU 9's "Tuition Agreement Overview" page. Jackson's High School Options site adds the contract comparison, cost presentations, the FAQ, rubrics and survey results.
   - citation: SAU 9, Tuition Agreement Overview; Jackson AD HOC High School Options Committee site
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: High School Options site: https://sites.google.com/sau9.org/jacksonhighschooloptions/home. Raw: raw/money/sau9/sau9-tuitions.*; raw/money/jgs/hs-options-site.*

## district-fees: Fryeburg Academy's Posted Tuition

- kind: local
- question_type: local_practice
- description: Costs families may pay: sports, field trips, supplies, technology, instruments and other fees, and help with them

1. Fryeburg Academy's website lists 2027-28 Commuter Day Tuition of $22,500, and boarding tuition, room and board of $62,100.
   - citation: Fryeburg Academy, "Tuition + Financial Aid," Tuition 2027-28
   - source: https://www.fryeburgacademy.org/admissions/tuition-financial-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Page text: "Tuition 2027-28 ... Boarding Tuition, Room + Board: $62,100 ... Commuter Day Tuition: $22,500". The page's "INCLUDES" list under the commuter rate repeats the boarding list (dormitory, travel days), apparently a page layout error, so it is not used. The 2026-27 rate is no longer shown. Under the agreement (Section 20), breakfast and lunch are included in Jackson's tuition. Raw: raw/money/fryeburg/fa-tuition.html and .txt

## school-programs-after-grade-6: Enrolling at Fryeburg Academy From a Non-Member Town

- kind: local
- question_type: local_practice
- description: Middle and high school programs that a district's students attend: AP, honors, dual enrollment, early credit, transitions between schools, activities

1. Fryeburg Academy's day-student page lists Chatham, New Hampshire, another SAU 9 town, among non-MSAD 72 towns whose residents enroll at Fryeburg with a residency letter from the town office.
   - citation: Fryeburg Academy, "Day Students" page
   - source: https://www.fryeburgacademy.org/admissions/how-to-apply/day-students
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Page text: "Albany, Maine + Chatham, New Hampshire Residents ... Residents who choose to attend Fryeburg Academy, please obtain a letter from the Chatham or Albany town office confirming your residency ... Non-MSAD 72 Towns: Albany Township and Chatham, New Hampshire". Context only; Chatham's terms were not checked here. Updated November 13, 2026: Chatham's own high school terms (policies JECC and JECA) are in town/Chatham/money-and-governance.md, high-school-tuition-options facts 2–3. Raw: raw/money/fryeburg/fa-day-students.*

## district-transportation: Transportation to Kennett, Fryeburg or Another High School

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. Under both Kennett contracts and the Bartlett contract, Jackson is responsible for the "transportation methods and expenses" of its students; Kennett tuition does not include transportation.
   - citation: Conway Tuition Agreement (2003), Section I; Jackson/Conway Agreement (2027), Sections I and VIII.A.1; Bartlett/Jackson Tuition Contract, Section IV
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: 2027 text: "Jackson School District shall be responsible for the transportation methods and expenses in connection with such attendance." Statewide, districts must bus K–8 students living more than 2 miles away but may choose whether to bus grades 9–12 (library topic gov-school-transportation, RSA 189:6). Raw: raw/money/contracts/*.ocr.txt
2. Fryeburg Academy is not responsible for daily transportation of Jackson students; Jackson alone decides whether to provide it. If both sides agree, the academy will help set up a shuttle coordinated with Jackson's Kennett buses to carry students from the Conway area to Fryeburg, at a cost not to exceed $25,000 a year for 14 or fewer students. Jackson students get the same field trip and extracurricular transportation as other day students.
   - citation: Jackson–Fryeburg Agreement, Section 17
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The Academy shall not be responsible for the daily transportation of Jackson students to and from the High School. Jackson shall be solely responsible for determining whether or not it wishes to provide transportation ... Should such a shuttle service be required, the cost shall not exceed $25,000 per annum for 14 students or fewer." Raw: raw/money/contracts/sau9-contract-9-12-jackson-fryeburg-2027.*
3. The board's February 2026 comparison described the planned Fryeburg service as a shuttle from Kennett to Fryeburg with space for 14 students for $25,000, plus an afternoon shuttle back to Kennett for the late bus so students can take part in activities, and estimated Kennett transportation at $98,000 a year.
   - citation: Jackson School Board, "High School Contract Comparison" (February 6, 2026), pp. 2–3
   - source: https://files.smartsites.parentsquare.com/10273/updated_hs_contract_comparison_2026_district_vote_.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Shuttle provided from KHS to Fryeburg with space for 14 students for $25k.* Afternoon shuttle back to KHS for late bus to allow for extracurriculars and academic support." Schedules are another agent's area. Raw: raw/money/jgs/hs-contract-comparison-2026.*
4. In September 2026 the Jackson Finance Committee recommended that the board table, for 2027-28, any expansion of the Fryeburg shuttle to non-resident Fryeburg Academy students from other towns, until the logistics for Jackson students are settled.
   - citation: Jackson Finance Committee Minutes, September 15, 2026
   - source: https://drive.google.com/file/d/16Pm5wzhFllKxb8KDaGIZaxyBXykqvxJI/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Motion was made by James Glazer and seconded that the Committee recommend to the School Board that the consideration of expanding transportation opportunities to non-resident Fryeburg Academy students be tabled for the 2027-28 school year ... Motion carried unanimously." Raw: raw/money/finance-committee/fc-2026-09-15.*
5. For any special education placement outside the academy, Jackson pays for the program and the transportation to it.
   - citation: Jackson–Fryeburg Agreement, Section 8
   - source: https://drive.google.com/file/d/1yH_-1a_Kj2sZRMrAEsA3qPe2F1DniW2h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "Jackson shall bear all the costs of any such special program or facility and the transportation to that facility and/or provider." Raw: as fact 2

## district-sau-governance: SAU 9's Budget, How Shares Are Set, and Board Voting

- kind: local
- question_type: governance_money
- description: How a district shares an SAU: board seats and votes, how SAU costs are divided, and what the local board decides versus the SAU

1. SAU 9 splits its budget among its member districts half by average daily membership and half by equalized property value, the default method in RSA 194-C:9, II (library topic budget-sau-budget-vote). For 2026-27, Jackson had 2.30% of SAU 9's average daily membership (36.45 of 1,584.08) and 11.51% of its equalized value ($886,510,933 of $7,703,079,446), giving it 6.90% of the SAU budget, or $190,660 of $2,761,283.
   - citation: "Proposed School District Apportionment for the School Administrative Unit #9 Budget 2026-2027," Jackson School District 2026 Annual Report, p. 32; RSA 194-C:9, II
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Row text: "Jackson 886,510,933 36.45 11.51% 2.30% 6.90% $190,660 ... Total 7,703,079,446 1,584.08 100.00% 100.00% 100.00% $2,761,283". Rotated scanned page; transcribed from image (viewed). Each district's percentage equals the average of its two shares (**derived** check: (11.51 + 2.30) ÷ 2 = 6.905). See table jackson_sau9_apportionment_2027. Raw: raw/money/annual-reports/ar-2026.* (page 35); raw/money/rsa/rsa-194-C-9.*
2. In SAU 9's apportionment, the average daily membership counted for each district is only pupils in the schools it operates: Jackson's 36.45 is JGS, while Albany, Chatham, Eaton and Hart's Location, which run no schools, have 0 and pay only on property value.
   - citation: SAU 9 Budget 2026-2027 apportionment, Jackson 2026 Annual Report, p. 32
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Rows: "Albany 223,771,174 0.00 2.90% 0.00% 1.45% $40,107 ... Harts Loc. 25,223,383 0.00 0.33% 0.00% 0.16% $4,521". Jackson's 36.45 equals the site's 2024-25 DOE ADM for JGS. Jackson's 7–8 and 9–12 tuition students count in Bartlett's and Conway's ADM. Raw: as fact 1
3. SAU 9's apportioned budget was $1,709,804 in 2021-22 (Jackson 7.22%, $123,435), $1,944,470 in 2024-25 (Jackson 7.09%, $137,921), $2,301,622 in 2025-26 (Jackson 6.98%, $160,567) and $2,761,283 in 2026-27 (Jackson 6.90%, $190,660). The 2026-27 total is 20.0% higher than 2025-26 (**derived**).
   - citation: SAU 9 budget and apportionment pages, Jackson School District Annual Reports 2021, 2024, 2025 and 2026
   - source: https://drive.google.com/drive/folders/1LP1rwzxaO8TST7NY9MI0lD7ihtpLyekv
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: 2021 text: "Total SAU9 Budget for District Apportionment $1,443,466 $1,521,649 $1,713,516 $1,709,804 $123,435" (actual 2018-19, actual 2019-20, adopted 2020-21, adopted 2021-22, Jackson's 7.22%); 2025 row "Jackson 809,929,414 37.62 11.75% 2.20% 6.98% $160,567 ... Total ... $2,301,622". Pages viewed. Raw: raw/money/annual-reports/ar-2021.* (p. 42), ar-2024.* (p. 36), ar-2025.* (p. 33), ar-2026.* (p. 35)
4. In the October 2026 Finance Committee meeting, the SAU business administrator said the draft 2027-28 Jackson budget did not yet include the SAU apportionment because "HB 564 requires the SAU budget be voted on in each district as a separate warrant article," and that technology had been moved into the SAU budget.
   - citation: Jackson Finance Committee Minutes (draft), October 29, 2026
   - source: https://drive.google.com/file/d/1j2Q4GBFOX-PiBgXTL2LhM8gNQPyz2Z7M/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Text: "The draft also does not include the SAU apportionment, as HB 564 requires the SAU budget be voted on in each district as a separate warrant article ... Mike Wade said technology was moved to the SAU budget." The statewide change (RSA 194-C:9, IV as amended effective August 18, 2026; votes added across all districts) is library topic budget-sau-budget-vote. Raw: raw/money/finance-committee/fc-2026-10-29-draft.*
5. SAU 9's 2025-26 budget status report, attached to the September 10, 2026 SAU board minutes, shows a general fund adopted budget of $2,401,622, with $2,272,479.31 spent and $129,142.69 (5.37%) remaining at June 30, 2026.
   - citation: SAU 9 School Board Minutes (draft), September 10, 2026, attached "SAU Budget" report (Report # 17485)
   - source: https://drive.google.com/file/d/1fWEamAunCfXPawPZOjtKwQnRIraFeO2-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: SAU-wide. Text: "TOTAL 01 GENERAL FUND 5.37% $2,401,622.00 $0.00 $2,401,622.00 $2,272,479.31 $0.00 $129,142.69". This is $100,000 more than the $2,301,622 apportioned to districts for 2025-26; no document seen explains the difference. Raw: raw/money/sau9-minutes/sau9-2026-09-10-draft-attach.pdf and .txt
6. The SAU 9 board is made up of the members of its seven district school boards. As of November 2026, SAU 9's pages list 7 Conway members, 5 Bartlett, 5 Jackson, and 3 each for Albany, Chatham, Eaton and Hart's Location, for 29 in all; Jackson holds 17% of the seats (**derived**: 5 ÷ 29).
   - citation: SAU 9 school board pages (Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location, Jackson)
   - source: https://www.sau9.org/school-boards-home
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Counts from each board page (Conway lists Megan Beckwith, Randy Davison, Sarah Burke, Brittany Hodge, Melanie Lebel, Mary Carey Seavey (appointed to April 2027) and Nicole Stanley). The SAU board page says it "Meets on the second Thursday of every other month at 6:00 p.m." Raw: raw/money/sau9/board-*.html and .txt; raw/money/sau9/sau9-board.*
7. Under RSA 194-C:7, each district that maintains a school gets 3 votes on the joint SAU board and each district that maintains none gets one representative with one vote, with each district's votes split among its members present. In SAU 9 that means Conway, Bartlett and Jackson 3 votes each and Albany, Chatham, Eaton and Hart's Location 1 each (**derived** from the statute and SAU 9's apportionment table, which shows those four with no ADM).
   - citation: RSA 194-C:7
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-7.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Jackson
   - note: Statute: "Every school district maintaining one or more public schools shall be entitled to 3 votes on the joint board ... Districts not maintaining schools shall have one representative on the joint board, who shall be entitled to one vote. Each school district board member present shall be entitled to have a proportionate share of the school district's votes". Raw: raw/money/rsa/rsa-194-C-7.*
8. Under RSA 194-C:8, if a majority of the members of any district board present demand it, SAU votes are weighted: one vote per 16 resident pupils enrolled in the SAU's schools (based on the prior year's average daily membership in residence), with a remainder of 8 or more adding a vote. Using NH DOE's 2025-26 resident ADM, Conway would have about 58 weighted votes, Bartlett about 12 and Jackson about 3 (**derived**).
   - citation: RSA 194-C:8; NH DOE FY2027 adequacy file (resident ADM, October 1, 2026 calculation)
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-8.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Jackson
   - note: Statute: "each district shall be entitled to one vote for each 16 pupils residing in that district and enrolled in schools under the administrative unit ... Weighted votes shall only be used upon the demand of a majority of the members of any board present and voting". Derived: Conway 926.6644 ÷ 16 = 57.9 (57 + remainder 14.7 → 58); Bartlett 198.6276 ÷ 16 = 12.4 (remainder 6.6 → 12); Jackson 52.3392 ÷ 16 = 3.3 (remainder 4.3 → 3). Approximate, because DOE's resident ADM also counts residents in schools outside SAU 9; not computed for Albany, Chatham, Eaton and Hart's Location for that reason. The resident ADM figures match the site's database (adequacy_aid, FY2027), which has each district's full calculation. Raw: raw/money/rsa/rsa-194-C-8.*; raw/money/state-data/adequacy-aid-sau9-towns.csv
9. The July 9 and September 10, 2026 SAU 9 board minutes record votes as counts of members present (for example "10-0-0" and "12-0-0"); neither records a demand for weighted voting. Four Jackson members (DellaValla, Auth, Foley-Marsello and Seidel) attended on September 10, 2026, out of 12 board members present.
   - citation: SAU 9 School Board Minutes, July 9, 2026 and September 10, 2026 (draft)
   - source: https://drive.google.com/file/d/1su4GmOnY3WshgAln8zu3bWZwrcYv8NtL/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: September attendance line: "Melanie Lebel (Conway), Andrew Light (Bartlett), Bethany Hicks (Eaton), Emily Calderwood (Bartlett), Randy Davison (Conway), Jessica DellaValla (Jackson), Nicole Stanley (Conway), Kristin Stelmok (Albany), Nicole Auth (Jackson), Melinda Foley-Marsello (Jackson), Tom Seidel (Jackson), Heather Forbes (Bartlett)". Only two meetings' minutes were read; older minutes were not checked for weighted votes. September minutes URL: https://drive.google.com/file/d/1fWEamAunCfXPawPZOjtKwQnRIraFeO2-/view. Raw: raw/money/sau9-minutes/sau9-2026-07-09.*, sau9-2026-09-10-draft-attach.*
10. In July 2026 the SAU 9 board voted 0-10-0 not to advance a new policy on the "Organization and Operation of SAU #9 Board" (BBBH-S), sending it back to the Executive Committee, after Jackson's board chair said it left out important parts of how an SAU operates. At the same meeting a Bartlett member said attendance at SAU 9 board meetings "has been low for years" and that some members felt decisions were made by the Executive Committee.
   - citation: SAU 9 School Board Minutes, July 9, 2026, items 6.a.i and 8.a
   - source: https://drive.google.com/file/d/1su4GmOnY3WshgAln8zu3bWZwrcYv8NtL/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Text: "BBBH-S - Organization and Operation of SAU #9 Board (New) ... DellaValla said it is not ready for adoption ... A vote was taken to move the policy to a second reading. 0-10-0"; "Forbes noted attendance by members at SAU #9 Board meetings has been low for years. There is a feeling that decisions are being made by the Executive Committee and brought to the Board to be rubber-stamped." No adopted SAU 9 policy on board voting was found. Raw: raw/money/sau9-minutes/sau9-2026-07-09.*
11. Jackson pays 6.90% of SAU 9's 2026-27 budget while holding 5 of 29 board seats, 3 of 13 statutory votes and roughly 3 weighted votes of about 73 for the three districts that run schools (**derived** from facts 1–3 and district-sau-governance 1).
   - citation: as facts 1–3
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-8.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Derived comparison; see table jackson_sau9_board_seats_and_votes. Raw: as facts 1–3
12. Jackson voters do not vote on Conway's school budget, which sets Kennett's costs; under the new contract the Conway School Board sets Jackson's charge each year from Conway's own DOE-25 spending and attendance.
   - citation: Jackson/Conway Agreement (2027), Section VIII.A.2; Annual Meeting Minutes, March 5, 2026
   - source: https://drive.google.com/file/d/1cHKhJnI_Yozv2CetoJU818ktgvjG5ZhS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Contract: "The Conway School Board shall annually set Jackson's cost based upon Conway's most recent DOE 25 and ADMA". Minutes (a resident): "We don't get to vote on the Conway budget." Raw: raw/money/contracts/sau9-contract-9-12-jackson-conway-2027.*; raw/money/meetings/am-2026.*
13. SAU 9's budget and each district's dollar share appear in the apportionment table printed in Jackson's annual report, and the SAU's line-item budget status reports are attached to SAU 9 board minutes; the two sources do not always match. For 2025-26, the apportionment table gives Jackson $160,567, while Jackson's budget line "SAU9 Share" is $167,543, a difference of $6,976 (**derived**).
   - citation: Jackson School District 2025 Annual Report, SAU 9 apportionment (printed p. 31) and proposed budget pages; 2026 Annual Report, p. 6
   - source: https://drive.google.com/file/d/16jP77ozx7pXrm3uWDDEUADqqo4w5_ycT/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Apportionment row: "Jackson 809,929,414 37.62 11.75% 2.20% 6.98% $160,567" (page viewed). Budget row: "221 71-10-2320-5311-0104 SAU9 SHARE 137,037 137,037 137,921 167,543". No explanation of the gap was found. Raw: raw/money/annual-reports/ar-2025.* (pp. 7, 16, 33), ar-2026.*
14. SAU 9's budget is shown in each district's annual report (as an apportionment table), and its line-item budget status reports are attached to SAU 9 board minutes in the "Policies, Agendum, Committees and Minutes" folder on SAU 9's board page.
   - citation: SAU 9 School Board page; SAU 9 School Board Minutes, September 10, 2026 with attachment
   - source: https://www.sau9.org/sau9
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Folder: https://drive.google.com/drive/folders/1ca6YRiJRPI-IOGXgG7hcgeSyORm8sUe4. Raw: raw/money/sau9/sau9-board.*; raw/money/sau9-minutes/sau9-2026-09-10-draft-attach.*

## jackson_operating_budget: Jackson School District Operating Budget (Article 1)

- unit: dollars
- period: fiscal years 2019-20 through 2026-27; year: the year the fiscal year ends
- source: Jackson School District warrants and annual meeting minutes, 2019–2026 — https://www.sau9.org/jackson (Drive folders "Jackson Warrant Articles" and "Annual Meetings - Jackson")
- as_of: 2026-11-13
- raw: raw/money/warrants/w-2019.pdf … w-2026.pdf; raw/money/meetings/am-2019.pdf … am-2026.pdf (with .txt transcriptions from images)
- note: Amount voters approved for the operating budget (Article 1), which excludes separate warrant articles such as capital reserve deposits. Grant offsets are in the warrant text.

| Place | District id | Year | Value | Note |
|---|---|---|---|---|
| Jackson | 271 | 2020 | 2724690 | Approved March 7, 2019 |
| Jackson | 271 | 2021 | 2728255 | Approved March 5, 2020; $31,800 offset by grants |
| Jackson | 271 | 2022 | 2993118 | Approved March 4, 2021; $17,100 offset by grants |
| Jackson | 271 | 2023 | 2754739 | Proposed $2,854,739; amended down $100,000 on the floor March 3, 2022 and approved |
| Jackson | 271 | 2024 | 3104417 | Approved March 2, 2023; motion to cut $64,496 failed |
| Jackson | 271 | 2025 | 3046203 | Approved March 7, 2024; $20,400 offset by grants |
| Jackson | 271 | 2026 | 3970978 | Approved March 6, 2025; $21,000 offset by grants |
| Jackson | 271 | 2027 | 4066810 | Approved March 5, 2026; $21,000 offset by grants |

## jackson_hs_tuition_budget_line: Jackson's Kennett High School Tuition Budget Line

- unit: dollars
- period: fiscal years 2018-19 through 2026-27; year: the year the fiscal year ends
- source: Jackson School District annual reports 2021–2026, proposed budget pages (account 71-10-1100-5560-0103 "Tuition, High School") — https://drive.google.com/drive/folders/1LP1rwzxaO8TST7NY9MI0lD7ihtpLyekv
- as_of: 2026-11-13
- raw: raw/money/annual-reports/ar-2021…ar-2026 (.pdf, .txt, .rot90.txt); pages viewed for 2021 (p. 12), 2023 (p. 10), 2024 (p. 11), 2025 (p. 10), 2026 (p. 9)
- note: Value is the adopted (or, for the latest year, voter-approved proposed) budget. The bond share and maintenance trust share are separate lines, given in the note. Transcribed from rotated scanned pages.

| Place | District id | Year | Value | Note |
|---|---|---|---|---|
| Jackson | 271 | 2019 | 650684 | Actual $650,684; bond share $84,633; maintenance trust share $4,972 |
| Jackson | 271 | 2020 | 644742 | Actual $645,926; bond share $72,904 (actual $72,905); maintenance trust $4,728 (actual $3,546) |
| Jackson | 271 | 2021 | 591245 | Actual $591,244; bond share $62,621; maintenance trust $4,356 |
| Jackson | 271 | 2022 | 787264 | Actual $787,264; bond share $63,488; maintenance trust $4,768 |
| Jackson | 271 | 2023 | 514676 | Actual $514,676; bond share $56,577; maintenance trust $4,629 |
| Jackson | 271 | 2024 | 679591 | Actual $679,591; bond share $50,304 (last year); maintenance trust $4,497 |
| Jackson | 271 | 2025 | 644248 | Actual $644,248; no bond share; maintenance trust $4,441 |
| Jackson | 271 | 2026 | 619485 | Maintenance trust $4,556 |
| Jackson | 271 | 2027 | 868953 | Up $249,468 (40.27%); FAQ: about $38,600 per student |

## jackson_ms_tuition_budget_line: Jackson's Bartlett (Grades 7–8) Tuition Budget Line

- unit: dollars
- period: fiscal years 2018-19 through 2026-27; year: the year the fiscal year ends
- source: Jackson School District annual reports 2021–2026, proposed budget pages (account 71-10-1100-5560-0102 "Tuition, Middle School") — https://drive.google.com/drive/folders/1LP1rwzxaO8TST7NY9MI0lD7ihtpLyekv
- as_of: 2026-11-13
- raw: raw/money/annual-reports/ar-2021…ar-2026 (pages as in jackson_hs_tuition_budget_line)
- note: Value is the adopted budget; actual spending in the note. The 2021 report notes FY2022 was budgeted on "7th grade-8, 8th grade-6.15" students.

| Place | District id | Year | Value | Note |
|---|---|---|---|---|
| Jackson | 271 | 2019 | 330400 | Actual $291,101 |
| Jackson | 271 | 2020 | 369332 | Actual $257,602 |
| Jackson | 271 | 2021 | 306800 | Actual $313,002 |
| Jackson | 271 | 2022 | 297995 | Actual $382,846 |
| Jackson | 271 | 2023 | 325059 | Actual $228,145 |
| Jackson | 271 | 2024 | 258084 | Actual $187,517 |
| Jackson | 271 | 2025 | 278472 | Actual $221,454 |
| Jackson | 271 | 2026 | 448000 | |
| Jackson | 271 | 2027 | 384000 | Budgeted for 12 students, 10 expected (Finance Committee, Dec. 3, 2025) |

## jackson_sau9_share: Jackson's SAU 9 Share

- unit: dollars
- period: fiscal years 2018-19 through 2026-27; year: the year the fiscal year ends
- source: Jackson School District annual reports 2021–2026 (account 71-10-2320-5311-0104 "SAU9 Share" and SAU 9 apportionment pages) — https://drive.google.com/drive/folders/1LP1rwzxaO8TST7NY9MI0lD7ihtpLyekv
- as_of: 2026-11-13
- raw: raw/money/annual-reports/ar-2021…ar-2026 (.txt and .rot90.txt); apportionment pages viewed for 2021, 2025, 2026
- note: Value is Jackson's budget line (adopted; actual in note where printed). The SAU apportionment percentage and SAU total are in the note where an apportionment table was found. Budget-line values for 2019–2024 are from OCR of rotated pages and agree across two or three overlapping reports.

| Place | District id | Year | Value | Note |
|---|---|---|---|---|
| Jackson | 271 | 2019 | 110093 | Actual $110,093 |
| Jackson | 271 | 2020 | 117026 | Actual $117,026 |
| Jackson | 271 | 2021 | 117439 | Actual $117,439 |
| Jackson | 271 | 2022 | 123435 | Apportionment 7.22% of $1,709,804 = $123,435 |
| Jackson | 271 | 2023 | 138542 | |
| Jackson | 271 | 2024 | 137037 | Actual $137,037 |
| Jackson | 271 | 2025 | 137921 | Actual $137,921; apportionment 7.09% of $1,944,470 |
| Jackson | 271 | 2026 | 167543 | Apportionment table: 6.98% of $2,301,622 = $160,567 (differs by $6,976) |
| Jackson | 271 | 2027 | 190660 | Apportionment 6.90% of $2,761,283 |

## jackson_sau9_apportionment_2027: SAU 9 Budget Shares by District, 2026-27

- unit: dollars
- period: 2026-27; year: 2027
- source: "Proposed School District Apportionment for the School Administrative Unit #9 Budget 2026-2027," Jackson School District 2026 Annual Report, p. 32 — https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
- as_of: 2026-11-13
- raw: raw/money/annual-reports/ar-2026.pdf (page 35, rotated; viewed) and ar-2026.rot90.txt
- note: Equalized valuation is for 2024 and ADM for 2024-25. Apportionment is half ADM share and half equalized value share (RSA 194-C:9, II).

| Place | District id | Value | Equalized valuation 2024 | ADM 2024-25 | % EV | % ADM | % apportioned |
|---|---|---|---|---|---|---|---|
| Conway | 113 | 1888119 | 3,782,415,877 | 1,388.51 | 49.10% | 87.65% | 68.38% |
| Bartlett | 35 | 578070 | 2,451,485,086 | 159.12 | 31.82% | 10.04% | 20.93% |
| Jackson | 271 | 190660 | 886,510,933 | 36.45 | 11.51% | 2.30% | 6.90% |
| Albany | 5 | 40107 | 223,771,174 | 0.00 | 2.90% | 0.00% | 1.45% |
| Eaton | 159 | 40111 | 223,792,984 | 0.00 | 2.91% | 0.00% | 1.45% |
| Chatham | 91 | 19694 | 109,880,009 | 0.00 | 1.43% | 0.00% | 0.71% |
| Hart's Location | 236 | 4521 | 25,223,383 | 0.00 | 0.33% | 0.00% | 0.16% |
| SAU 9 total | | 2761283 | 7,703,079,446 | 1,584.08 | 100.00% | 100.00% | 100.00% |

## jackson_sau9_board_seats_and_votes: SAU 9 Board Seats and Votes by District

- unit: count
- period: November 2026 (seats); 2025-26 resident ADM (weighted votes); year: 2027
- source: SAU 9 school board pages — https://www.sau9.org/school-boards-home ; RSA 194-C:7 and 194-C:8 — https://gc.nh.gov/rsa/html/XV/194-C/194-C-8.htm ; NH DOE FY2027 adequacy file (resident ADM)
- as_of: 2026-11-13
- raw: raw/money/sau9/board-*.txt; raw/money/rsa/rsa-194-C-7.txt, rsa-194-C-8.txt; raw/money/state-data/adequacy-aid-sau9-towns.csv
- note: Seats are the number of school board members listed on each district's SAU 9 page. Statutory and weighted votes are **derived** from RSA 194-C:7 and 194-C:8; weighted votes use DOE resident ADM, which also counts residents attending schools outside SAU 9, so they are approximate, and they are not computed for districts that run no schools. Weighted votes apply only when demanded. The resident ADM column matches NH DOE's FY2027 calculation in the site's data (adequacy_aid). Added November 13, 2026: the Hart's Location research computed that district's weighted votes as 0, with 1 resident pupil (fewer than 8); see town/Hart's Location/money-and-governance.md, district-sau-governance 4.

| Place | District id | Board seats | RSA 194-C:7 votes (derived) | Resident ADM 2025-26 | Weighted votes (derived) | Share of 2026-27 SAU budget |
|---|---|---|---|---|---|---|
| Conway | 113 | 7 | 3 | 926.6644 | about 58 | 68.38% |
| Bartlett | 35 | 5 | 3 | 198.6276 | about 12 | 20.93% |
| Jackson | 271 | 5 | 3 | 52.3392 | about 3 | 6.90% |
| Albany | 5 | 3 | 1 | 57.5565 | not computed | 1.45% |
| Chatham | 91 | 3 | 1 | 40 | not computed | 0.71% |
| Eaton | 159 | 3 | 1 | 33.6882 | not computed | 1.45% |
| Hart's Location | 236 | 3 | 1 | 1 | not computed | 0.16% |

## jackson_hs_tuition_per_pupil: High School Cost per Jackson Student

- unit: dollars
- period: 2026-27 actual budget rate and 2027-28 estimates; year: 2027 and 2028
- source: Jackson School Board, "High School Contract Comparison," updated February 6, 2026 — https://files.smartsites.parentsquare.com/10273/updated_hs_contract_comparison_2026_district_vote_.pdf ; Fryeburg Academy, Tuition + Financial Aid — https://www.fryeburgacademy.org/admissions/tuition-financial-aid
- as_of: 2026-11-13
- raw: raw/money/jgs/hs-contract-comparison-2026.pdf and .txt; raw/money/fryeburg/fa-tuition.html and .txt
- note: The board's 2027-28 figures are projections from five-year average increases and exclude special education and transportation.

| Place | Year | Value | Note |
|---|---|---|---|
| Kennett High School, current contract | 2027 | 38603 | 2026-27 tuition per pupil, maintenance included (board comparison) |
| Kennett High School, new contract | 2028 | 27855 | Estimate, plus about $20,900 a year maintenance fund payment |
| Fryeburg Academy, Jackson rate | 2028 | 26788 | Estimate (commuter day rate plus premium) |
| Fryeburg Academy, legacy students | 2028 | 22388 | Estimate (commuter day rate, no premium) |
| Fryeburg Academy, Commuter Day Tuition (published) | 2028 | 22500 | Fryeburg's posted 2027-28 rate; Jackson's maximum with a 20% premium would be $27,000 (**derived**) |

## Not retrieved

- https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village: returned HTTP 403 to curl and WebFetch today, so the 2026 tax rates for Jackson, Bartlett and Conway (not in the library's October 30, 2026 list) and any posted MS-27 school budget forms could not be checked. The town's own posting covers only 2025.
- MS-27 forms for the Jackson School District: not found on sau9.org or in the Jackson Drive folders (warrants and annual reports only). The annual reports' line-item budgets were used instead.
- https://scholars.unh.edu/cgi/viewcontent.cgi?article=1131&context=jackson_nh_reports (Town of Jackson annual report for 2025): HTTP 403. The school district's own annual reports were used.
- Bartlett's yearly per-pupil tuition rate for Jackson grades 7–8 (the "rider" the contract says is appended each year): not in the posted contract PDF or the annual reports read; only budget totals were found.
- Conway's CEA (2026–2029) and Bartlett's BEA teacher agreements: downloaded (raw/money/sau9/) but mostly scanned; salary schedules not transcribed (for the Kennett/JBES agents if needed).
- Conway Daily Sun articles on the MWV Cooperative District Planning Board (https://www.conwaydailysun.com/news/local/cooperative-school-planning-board-to-meet-wednesday/article_accae876-3105-11ec-ac29-bf14b9dc3a52.html and https://www.conwaydailysun.com/news/local/khs-tuition-contract-committee-to-meet-thursday/article_14c10c88-1e5b-11ed-881b-d38a0e1ceb78.html): HTTP 429. The primary source (Superintendent's report in the 2022 annual report) was used instead. The planning board's own minutes were not found.
- https://sau9.org/district/tuition_agreement_overview (old "MWV Cooperative District Planning Board" page in search results): the live page no longer has that content.
- SAU 9 board minutes before July 2026 (other than December 12, 2019 and 2020–21 files downloaded to raw/money/sau9-minutes/) were not searched for weighted-vote demands or SAU budget adoption votes.
- Jackson School Board minutes for 2024–2026 (beyond September 18, 2023) and the High School Options Committee's financial presentations (raw/money/jgs/financial-presentation-2024-09-30.pdf, mostly images) were not read in full.
- NH School Board Association school choice memo linked from the High School Options site (Drive id 1wtsfEK_EsPAI7zobjIaKZ7qXCsADjgWt): Drive returned 503.
- Fryeburg Academy's 2026-27 commuter day rate: no longer on its tuition page (which now shows 2027-28); third-party sites were not used.
- For another file (programs/outcomes agents): the Fryeburg agreement's assessment, reporting and alternative learning plan terms (Sections 2, 11, 19) and the board's Fryeburg/Kennett course and CTE comparisons on the High School Options site; the Superintendent's 2025 report on the consolidation of Conway's elementary schools (raw/money/annual-reports/ar-2025.txt, p. 20).
- For another file (transportation agent): Finance Committee notes on bus sizes and hard-to-reach roads such as Wilson Road (October 29, 2026 draft minutes, raw/money/finance-committee/fc-2026-10-29-draft.txt).
