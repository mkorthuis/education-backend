# Tamworth School District: Money, Tuition Contracts and Governance

Part of the Tamworth research (town/Tamworth). Gathered November 13, 2026.

## Summary

**What's covered:** 8 topics, 99 facts and 8 number tables on the Tamworth School District's money, contracts and governance.
- Why Brett School's cost per pupil keeps rising: falling enrollment, a mostly fixed cost base, Kennett tuition, special education, health insurance and buses, with the district's own breakdowns (FY2024–FY2028).
- How much of the 2025 tax rate the Kennett and Moultonborough Academy tuition lines and Tamworth's SAU 13 share would equal (**derived**, using the district's own per-$1,000 method). Tamworth's DRA tax rates (2014–2025) and NH DOE school taxes (2011–2025) are in the site's data (property_tax), so this file does not repeat them.
- The 2003 Tamworth–Conway contract (read from scanned pages): the 90% clause, the 20-year term, the notice rule and the cost formula; Tamworth's notice to end it in 2027; the negotiations through November 2026; and the 2024–25 and 2026–27 Kennett charge tables.
- Both Moultonborough Academy agreements (2024–25 and 2026–27, read from scanned pages): seats, how students are chosen, tuition cap, special education, transportation and continued attendance.
- The Brett School HVAC project (Phases I–III), boilers, capital reserve funds, the first draft capital plan, and energy items.
- Paraprofessional pay posted by Tamworth, Moultonborough and Conway; state aid in the district's budget and why the extraordinary need grant fell (NH DOE's adequacy aid calculation for FY2020–FY2027 is in the site's data, adequacy_aid, so this file does not repeat it); federal Small, Rural School Achievement awards and Title I; the middle school tuition idea for Madison and Freedom; board meetings, minutes and livestreams.

**Main sources:** Tamworth School Board minutes and packets (July 2023–November 2026, from the SAU 13 site's Drive folders), the 2026 warrant and MS-26, the district's annual reports for FY2023 and FY2025 (scanned; pages rendered and read), the FY2027 working budget, the High School Options Committee's records (2022–2023), the Tamworth–Conway 9–12 agreement (2003), SAU 9's tuition page, Conway School Board minutes (from the Conway research), job postings for SAU 13, SAU 45 and Governor Wentworth, the library's DRA and adequacy CSVs, USAspending.gov, and read-only queries of the site database.

**Premises checked:**
- "Enrollment hovers around 165": Brett's October 1 enrollment was 165 in 2024, but it was 204 in 2016, 154 in 2025, 139 expected for 2026-27 in June 2026, and 126 reported by the board chair on September 17, 2026. It is falling, not flat.
- "$13.33 tax rate": $13.33 is DRA's 2025 full value (equalized) rate for Tamworth. The rate on 2025 tax bills is $14.78 per $1,000, of which $9.59 is the local school rate and $1.09 the state education tax (site data: property_tax).
- "Up to 6" Moultonborough seats and a "boundary": there is no geographic boundary. Any Tamworth resident high school student may apply. The 2024 contract allowed up to 10% of eligible students (the district's 2024 notice said up to 6). The 2026-27 agreement allows up to 10 per grade (40 in all). The board has funded every applicant so far (2 in 2024, 8 in 2025, 7 in 2026).
- "The Kennett agreement expires in 2027 with notice in 2024" (Freedom's study): correct for Tamworth. On February 15, 2024 the Tamworth board voted unanimously to send Kennett a letter cancelling the contract as of 2027. As of November 13, 2026 no new Tamworth–Conway contract is posted, and the board says it is still negotiating.

**Main gaps:**
- Governor Wentworth Regional's (Ossipee's) paraprofessional pay: its job postings give hours and benefits but no rates, and the state labor board's contract library refused automated requests.
- The results of the March 4, 2026 annual meeting (including the SB2 article) were not found; later minutes show the HVAC and special education articles were acted on.
- The October 7, 2026 "School Tuition Presentation," the November 17, 2026 "Community Letter" and "Information Night," and any Governor Wentworth contract terms were not posted.
- No roof project and no adopted five-year capital plan were found; only a June 2026 draft.

**Proposed shared topic:** none. Paraprofessional pay sits under `district-budget-and-cost`; Tamworth's SAU share under `district-sau-governance`.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P2.1 Why does Brett's cost per pupil rise while enrollment "hovers around 165"? | district-budget-and-cost facts 1–15; tables tamworth_official_enrollment, tamworth_article1_budget, tamworth_hs_tuition_lines; site data: cost per pupil, ADM, staff; library: measure-cost-per-pupil | full | Premise corrected: enrollment is falling (204 → 154 on October 1, 2016–2025; 126 in September 2026). DOE's cost per pupil leaves out tuition and transportation. No verdict on value |
| P2.2 How much of the tax rate ($13.33) is high school tuition vs SAU 13 administration? | district-tax-and-state-aid facts 1–5; district-sau-governance facts 1–5; tables tamworth_tax_per_1000_by_line, tamworth_sau13_share; site data: property_tax (Tamworth district) | full | Premise corrected ($14.78 actual; $13.33 is DRA's full value rate, both in the site's data). Per-$1,000 figures are **derived** "if paid wholly from local tax." SAU 13's own budget: SAU 13 fact: see Madison research |
| P6.3 Five-year capital plan for HVAC, roof and energy | district-facilities-and-capital facts 1–13 | partial | HVAC Phases I–III, boilers, reserves, a possible bond and the draft capital plan are covered. No roof project or adopted five-year plan was found |
| P13.1 Support staff wages and benefits vs Conway, Moultonborough and Ossipee | district-budget-and-cost facts 16–21; table tamworth_para_pay_neighbors; Conway file: district-budget-and-cost facts 19–22, table conway_para_and_regional_wages | partial | Para ranges for Tamworth, Moultonborough and Conway are compared (**derived**). Governor Wentworth (Ossipee) rates not found. Brett's buses are run by First Student, so bus drivers are not district employees (daily agent covers buses) |
| P14.2 Boundary and eligibility rule for Moultonborough Academy vs Kennett | high-school-tuition-options facts 1–9; district-tuition-contracts facts 14–17 | full | No boundary: application and, if needed, a lottery. Seats: 10% (2024), 10 per grade (2026-27) |
| P14.3 How stable is the Kennett contract; could Conway cap enrollment? | district-tuition-contracts facts 1–13; Conway file: district-tuition-contracts facts 5, 8–9; Bartlett file: district-tuition-contracts | full | Facts only: the 2003 contract ends June 30, 2027 after Tamworth's notice; no 2027 contract as of November 13, 2026. No forecast |
| P15.1 Per-pupil tuition to Conway vs Moultonborough and how each is calculated | district-tuition-contracts facts 3–5, 14–18; tables tamworth_kennett_charge, tamworth_hs_tuition_lines | full | 2026-27: $20,221 per pupil at both (Kennett **derived** from the charge ÷ ADMA; Moultonborough capped at Kennett's rate) |
| P15.2 Would consolidating grades 6–8 across SAU 13 save money? | district-consolidation-history facts 1–8 | partial | Facts on the 2025 idea of Brett taking Madison and Freedom middle schoolers and the tuition-in rates. No study, committee or vote on SAU-wide consolidation was found; savings can't be stated |
| P15.3 Adequacy aid, federal rural funding, and why the local burden feels heavy | district-tax-and-state-aid facts 6–13; table tamworth_srsa_awards; site data: adequacy_aid (Tamworth district); library: money-adequacy-grant-calculation, money-fy2027-aid-and-tax; site data: DOE-25 revenue lines | full | State grant fell from $2.15 million (FY2024) to $1.46 million (FY2027). "Feels disproportionate" can't be measured; the facts show the shares |
| P20.2 (board side) Communication, conferences and board transparency | district-board-and-public-input facts 1–12; site data: Question 2 vote (Tamworth 781–585, 57.2%) | partial | Meeting schedule, minutes posting, livestreams and hearings. No survey of parents' ratings was found; public data can't rate satisfaction. Conferences and daily communication: Brett School agent |

## district-budget-and-cost: Tamworth's Budget, Cost per Pupil and Support Staff Pay

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. NH DOE's cost per pupil for the Tamworth School District rose from $28,174 in 2018-19 to $37,750 in 2024-25 (up 34%), while its average daily membership fell from 182.23 to 165.15 (down 9%) (**derived** changes); in 2024-25, 9 of the 153 districts with an elementary figure had a higher one (**derived** count).
   - citation: site data (district_cost_per_pupil and doe_form_adm, Tamworth, 2010–2025)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Query rows: "2019 | 28174 ... | 28174", "2025 | 37750 | | | 37750"; ADM "2019 | 182.23", "2025 | 165.15". Derived: 37,750 ÷ 28,174 = 1.340; 165.15 ÷ 182.23 = 0.906. Count query: "higher 9 | with_elem 153" (our count, not a DOE rank). A resident at the March 5, 2025 meeting called Tamworth "6th highest out of 154 districts." Raw: raw/money/state-data/site-db-tamworth-queries.txt
2. Brett School's official October 1 enrollment (grades K–8) fell from 204 in 2016 to 185 in 2023, 165 in 2024 and 154 in 2025, and the number of Tamworth high school students fell from 95 in 2023 to 68 in 2025.
   - citation: Annual Report of the Tamworth School District, FY ending June 30, 2025, "Report of Official Enrollment as of October 1st," p. 65
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Page text: "The K. A. Brett School's official enrollment for Grades K through 8, as of October 1st 2025 was 154." Rows "2024 ... 165", "2016 ... 204"; grades 9–12 "2025 12 16 24 16 68", "2023 25 24 22 24 95". The page also lists 14 homeschooled students and 2 at Northeast Woodland Charter School (October 1, 2025). See table tamworth_official_enrollment. Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.pdf, .ocr.txt
3. For 2026-27 the superintendent reported in June 2026 that Brett expected 139 students (including 10 kindergartners), and on September 17, 2026 the board chair gave the current enrollment as 126; in April 2026 the superintendent said a new charter school expected 19 Tamworth students.
   - citation: Tamworth School Board minutes, June 18, 2026 (Superintendent's Report A), September 17, 2026 (Public Comment), April 16, 2026 (Public Comment)
   - source: https://drive.google.com/file/d/19Gsr_2sNor5icgbRcrT5NZsTUYk8lb_X/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: June text: "Enrollment – next year we have 139 • Kindergarten we have 10 students." September text: "What is the current enrollment number? Shauna Peterson responded '126'." April text: "They currently have 19 students expected to attend from Tamworth, spread throughout the grades." Charter enrollment is the community agent's topic. Raw: raw/money/minutes/tsb-tamworth-june-18-2026-approved-minutes.*, tsb-tamworth-september-17-2026-public-approved-minutes.*, tsb-tamworth-april-16-2026-approved-minutes.*
4. NH DOE's cost per pupil leaves out Kennett and Moultonborough tuition and transportation (library topic measure-cost-per-pupil), a point a board member made at the March 2025 annual meeting, and in April 2024 the board chair said Tamworth's high figure "does not indicate what is offered" but reflects "so few students to 'share the cost'."
   - citation: Annual meeting minutes, March 5, 2025 (Annual Report FY2025, p. 10); Tamworth School Board minutes, April 18, 2024 (Old Business B)
   - source: https://drive.google.com/file/d/16xYNZhKq5-Liwx5Wa0K8ksM_EIb2q3mF/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: 2025 text: "Siena Kaplan-Thompson also commented that ... the cost per pupil does not include transportation costs, Kennett tuition, etc., so it is not a useful number for comparing to other schools." 2024 text: "Tamworth has one of the highest cost per pupil rates in the state. He said that this does not indicate what is offered, but looks bad because there are so few students to 'share the cost'. This is indicative of the density of the student population." Statements as recorded. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt; raw/money/minutes/tsb-tamworth-april-18-2024-draft-corrected-minutes.*
5. The district's own cost-per-pupil sheet for 2022-23 (actual) put Brett's cost at $30,198.89 per pupil in average daily membership and high school (tuition) at $19,467.13 per pupil, or $26,873.69 across both, after taking out food service, transportation and supplemental spending.
   - citation: Tamworth School Board packet, March 21, 2024, "Tamworth School District - Cost Per Pupil," p. 25
   - source: https://drive.google.com/file/d/12lgY9CmD_TAMIGuo2C_jN1b8SH-lkJQc/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text (2022-2023 Actual): "Expenses 6,133,847.68 1,904,063.93 8,037,911.61 ... ADM-A 189.53 85.09 274.62 ... ADM-A Cost Per Pupil SY24 30,198.89$ 19,467.13$ 26,873.69$" (the label reads SY24 on both halves of the sheet). The 2023-24 budgeted half shows $30,470.87 and $15,868.68. This is the district's method, not DOE's. Raw: raw/money/packets/tsb-packet-2024-03-21-p27-cost-per-pupil.*
6. The district's breakdown of its approved 2025-26 operating budget ($8,768,795.48) set aside Kennett tuition ($1,543,997), Moultonborough Academy tuition ($153,292.61), special education ($1,618,736.73), transportation ($621,264.25), food service ($188,812.54) and summer programs, leaving $4,633,538.40, or $29,702.17 for each of 156 students; tuition, special education and transportation were about 45% of the budget (**derived**).
   - citation: Tamworth School Board packet, August 21, 2025, "Tamworth Pro Forma Tuition Rate Calcuation 2025-2026 Budget," p. 25
   - source: https://drive.google.com/file/d/1W4iPryvUN7uRu3pTTKzdCVdcExqAsWVv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Page text: "Total Approved (not including SAU) $ 8,768,795.48 ... Less Kennett High School 1,543,997.00 ... Less Moultonborough Academy 153,292.61 ... Less SPED 1,618,736.73 ... Less Transportation 621,264.25 ... Total Allocation 4,633,538.40 ... Total Allocation to Rate: (Total-Adju)/#students 29,702.17 ... Number of students: 156". Derived: (1,697,289.61 + 1,618,736.73 + 621,264.25) ÷ 8,768,795.48 = 44.9%. See table tamworth_hs_tuition_lines. Raw: raw/money/packets/tsb-packet-2025-08-21-p25-29.pdf, .txt, tsb-packet-2025-08-21-p25.png
7. In August 2026 the business administrator said that "so much of the 'cost per pupil' is fixed costs that stay the same regardless of the number of students," so a student moving in "wouldn't increase the cost," and the board set a tuition rate of $17,216.30 for up to five incoming students, half of the per-student cost left after removing those fixed costs.
   - citation: Tamworth School Board minutes, August 20, 2026 (New Business F; Public Comment)
   - source: https://drive.google.com/file/d/11m35F1QZ5am2vHTLf84WXHuUIbVeJW6-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Tuition rate. Heather took out everything that stays the same regardless of the number of students, and she recommends we set it as half that rate ... If a student wants to come here on manifest hardship or tuition in, we would use this number for the first five students. That's $17,216.30." Later: "in reality having a student come here wouldn't increase the cost, since so much of the 'cost per pupil' is fixed costs." "Realistically, we haven't had any student tuition here in the past few years." Raw: raw/money/minutes/tsb-tamworth-august-20-2026-public-approved-minutes.*
8. Tamworth voters approved operating budgets (Article 1) of $7,759,754 for 2023-24, $8,768,795 for 2025-26, and, as proposed by the board 3-0-0, $9,125,578 for 2026-27; the 2024 warrant proposed $8,583,796 for 2024-25.
   - citation: Annual meeting minutes, March 8, 2023 and March 5, 2025; 2024 and 2026 warrants (annual reports FY2023 and FY2025)
   - source: https://drive.google.com/file/d/1errSVsknSjF7Tc2thdyD5hIGHLgEPozX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: 2023: "Warrant Article 1 to raise and appropriate the sum of $7,759,754 ... The motion passed on a voice vote." 2025: "$8,768,795 ... A voice vote was subsequently taken on Article 1, and the Article passed." 2024 warrant OCR reads "38,583,796" (the 3 is a scanned $ sign). 2026: "$9,125,578 ... (The School Board recommends this appropriation. 3-0-0)." The March 2024 and March 2026 meeting results were not found. See table tamworth_article1_budget. Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2023-excerpt.*, tsd-annual-report-fy2025-excerpt.*, tsd-2026-warrant.*
9. At the February 2025 budget hearing the board chair said regular education was up 9% "mostly due to Conway tuition, which has increased by approximately $400,000 in the past two years," transportation was up $122,664 because the First Student contract rose 12%, and special education was down $399,848 after three paraprofessional positions were cut and out-of-district tuition fell about $200,000.
   - citation: Tamworth Public Hearing and School Board minutes, February 7, 2025 (rescheduled from February 6)
   - source: https://drive.google.com/file/d/1coSMPexYzHIijpM_bSj_9MtATSkYcCSr/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Regular Education is up 9% ■ Mostly due to Conway tuition ... Transportation increased by $122,664 ■ First Student contract is up by 12% due to collective bargaining ... Special Education down $399,848 ■ Three paraprofessional positions cut ■ Out of district tuition down approximately $200,000." Also: "$400,000 increase in past 2 years of Conway tuition is due to the tuition formula" and "Federal / State Funding 16% ● Local Budgets 84%". Raw: raw/money/minutes/tsb-tamworth-february-6-2025-public-hearing-approved-minutes.*
10. In December 2024 the business administrator reported that Kennett tuition for 2025-26 had risen 9.17% because of "a rate increase from Kennett, not an increase in the number of Tamworth students," and the superintendent said the state was cutting Tamworth's adequacy aid by about $170,000 for the next year.
   - citation: Tamworth School Board minutes, December 12, 2024 (Business Administrator's Report B)
   - source: https://drive.google.com/file/d/1JvyUhaWX92Qw0BhK_eX2zt27x_Muuxu6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "High school tuition has increased 9.17%. This is the result of a rate increase from Kennett, not an increase in the number of Tamworth students. The bus contract numbers are up 12% and the total includes the cost of providing a bus for students to attend Moultonborough Academy ... The state is reducing its adequacy contribution by approximately $170,000 next year." That was an estimate; NH DOE's final figures in the site's data (adequacy_aid, Tamworth district) show the adequacy grant fell $202,589.71, from $1,209,243.08 (FY2025) to $1,006,653.37 (FY2026). Raw: raw/money/minutes/tsb-tamworth-december-12-2024-approved-minutes.*
11. In its FY2025 annual report the Tamworth School Board named the main cost drivers it could not control: employee health insurance (up 22.3% in 2025), bus transportation, the Kennett contract ("As the overall number of students goes down, the bill for our tuition goes up") and out-of-district special education costs above $1 million; it reported cutting three teachers, paraprofessionals to the legal minimum, and the garden, Spanish and math coach programs.
   - citation: Annual Report of the Tamworth School District, FY2025, "Tamworth School Board Report," p. 12
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "The number of teachers at the Brett School has been reduced by three, and the number of paraprofessionals has been reduced to the absolute minimum number needed to provide the special education services that are required by law ... the cost of providing health care to the employees of the school has ballooned ... including a 22.3% increase in 2025 alone ... The cost to Tamworth of the Conway high school tuition contract is directly related to the declining numbers of students from the surrounding areas attending Kennett High School. As the overall number of students goes down, the bill for our tuition goes up ... our special education out-of-district costs in this budget exceed one million dollars." The report also criticizes state policy (opinion as printed). Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.*
12. The January 2026 working budget for 2026-27 (version 4) raised out-of-district special education tuition to $1,098,000 (from a 2025-26 budget of $500,850 and 2024-25 spending of $263,560), cut teacher salaries to $1,071,573 (from $1,311,210, down 18.28%), raised paraprofessional health insurance 45.36%, and totaled $9,135,831, up 3.81%.
   - citation: Tamworth School District, "2026-2027 WORKING BUDGET, Corrected v4" (printed January 16, 2026)
   - source: https://drive.google.com/file/d/1ssRzxX50mTnCQlKnTBD9l_HHAUU5pf0i/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Rows (2026-27 | 2025-26 budget | 2024-25 spent | 2023-24 spent | $ change | %): "01.1210.560.109 Out of District Tuition $1,098,000.00 $500,850.00 $263,559.55 $283,139.38 $597,150.00 119.23"; "01.1100.110.077 Teacher Salaries $1,071,573.00 $1,311,210.08 ... (18.28)"; "01.1210.211.002 Health Insurance-Paras $241,432.33 $166,089.31 ... 45.36"; "Grand Total: $9,135,831.03 $8,800,858.35 ... $334,972.68 3.81". The warrant figure ($9,125,578) is slightly lower than v4. In December 2025 the chair put total health insurance at $1,312,257 "and includes the 22.3% increase." Raw: raw/money/packets/tsd-2026-2027-working-budget-v4.*; raw/money/minutes/tsb-tamworth-december-18-2025-approved-minutes.*
13. In June 2026 the superintendent reported 41 students with special education plans among Brett's 139, plus 12 at the high school and 4 in out-of-district placements, and the business administrator said 2025-26 special education was overspent by about $400,000, partly because of an unexpected out-of-district placement, so the budget was frozen and the board held a hearing to use up to $30,000 of set-aside fund balance.
   - citation: Tamworth School Board minutes, June 18, 2026 (Public Hearing; Public Comment; Student Services report)
   - source: https://drive.google.com/file/d/1aFnnqDp5EjrXULxTOIun2Al1S6uvNq9j/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "there was an unexpected out of district placement which is a big piece of it ... special education is overspent by about $400k. That's why we froze the budget. Mike added that that's part of the challenge of planning a budget 18 months before you spend it"; "There are 41 at KA Brett, out of the 139 Brett School enrollment"; "We have 41 identified students at Brett, 5 at charter K-12, 12 at the high school, and 4 out of district placements." **Derived**: 41 ÷ 139 = 29%. Special education services are the Brett School agent's topic. Raw: raw/money/minutes/tsb-tamworth-june-18-2026-approved-minutes.*
14. Tamworth's November 2026 working budget for 2027-28 (version 2) totals $10,239,596 and budgets Kennett tuition at $1,953,000 ("70 x $27,900"), Moultonborough Academy at $279,000 ("10 x $27,900"), out-of-district tuition at $770,000, and health insurance at current premiums plus 22.3%.
   - citation: Tamworth School Board packet, November 17, 2026, "2027-2028 Working Budget v1 to v2" changes, pp. 50–52
   - source: https://drive.google.com/file/d/1LjBjD-dLSbgSPdRK736L2I9dQgBZT9f-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Rows: "01.1100.561.103 KHS TUITION $2,007,500.00 $1,953,000.00 ($54,500.00) Updated to 70 x $27,900"; "01.1100.561.104 MA TUITION $412,800.00 $279,000.00 ($133,800.00) Updated to 10 x $27,900"; "01.1210.560.109 Out of District Tuition $1,098,000.00 $770,000.00 ... Updated per most recent SS Director Guidance"; "Increased Estimate to Current plus 22.3%"; "TOTALS $10,468,291.91 $10,239,596.20". A working draft before the board's December and January reviews; no 2027-28 Kennett contract exists yet. See table tamworth_hs_tuition_lines. Raw: raw/money/packets/tsb-packet-2026-11-17-p1-2-10-37-38-48-52.*
15. At the February 2025 hearing the board chair said "staff pay a percentage of the cost of health insurance," and in January 2026 the board voted 0–5 against a memorandum of understanding with the support staff union (TESPA).
   - citation: Tamworth Public Hearing minutes, February 7, 2025; Tamworth School Board minutes, January 15, 2026 (Action as a result of non-public session)
   - source: https://drive.google.com/file/d/1vT154pmlCnkf_XLoj_5Lq-lct5_azL_h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: 2025 text: "Inquiry about health insurance cost share with staff ● Chair Jack Waldron responded that staff pay a percentage of the cost of health insurance." 2026 text: "VOTE: Motion to approve MOU between TESPA and Tamworth School District was made by Siena Kaplan-Thompson, seconded by Dexter Harding. The vote was 0 Aye-5 Nay." The MOU's subject is not stated. Raw: raw/money/minutes/tsb-tamworth-february-6-2025-public-hearing-approved-minutes.*, tsb-tamworth-january-15-2026-approved-minutes.*
16. Tamworth's posting for special education paraprofessionals at Brett School (open November 13, 2026) offers $21.84 to $24.19 an hour by experience, 6.5 hours a day for 178 days, the district paying 94.9% of individual or two-person health plans and 92.2% of family plans, full single dental, long-term disability, and $300 a year for workshops.
   - citation: SAU 13 job postings, "Special Education Paraprofessionals," JobID 349 (posted 5/29/2026)
   - source: https://www.applitrack.com/sau13/onlineapp/default.aspx?AppliTrackPostingSearch=location:%22Kenneth+A+Brett+School%22
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "The positions are 6.5 hours per day, following the school year calendar and PD days (178 days). Pay range is $21.84 to $24.19 per hour based on prior work experience. 94.9% cost coverage for 2 person or individual health plans and 92.2% cost coverage for family health plan. Full coverage for single plan for dental and ability to purchase family plan. Long Term Disability Insurance. Professional Days and $300 annually to attend workshops." Requires NH Paraeducator II certification or eligibility. **Derived**: 6.5 × 178 × $21.84 = $25,269 and × $24.19 = $27,988 a year before benefits. Raw: raw/money/wages/sau13-applitrack-brett-postings-2026-11-13.*
17. The Moultonborough School District's posting for 2026-27 special education paraeducators gives a pay range of $18.00 to $28.14 an hour "based on experience and qualifications," plus differentials, with medical, dental, life insurance and NH retirement benefits, and requires paraeducator certification within a year of hire.
   - citation: SAU 45, "Job Openings" (26-27 Special Education Paraeducator Openings)
   - source: https://docs.google.com/document/d/1v7YUgs9715KvzXA78yIf284SInETz7KsTH0sSe1q2IM/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Moultonborough
   - note: Text: "MSD offers competitive wages plus applicable differentials as assigned (pay range $18.00-$28.14 based on experience and qualifications), medical, dental, life insurance, and NH retirement benefits. Paraeducator certification required within one year of hire; onboarding and mentor provided. Initial review of applications November 13, 2026." The posting gives no health premium shares. Linked from https://sau45.nh.gov/en-US/employment. Raw: raw/money/wages/sau45-job-openings-2026-11-13.txt
18. Comparing posted ranges, Tamworth's starting paraprofessional rate ($21.84) is above Moultonborough's ($18.00) and Conway's (levels 0–1: $19.92 in 2025-26, $20.52 in 2026-27), while Tamworth's top posted rate ($24.19) is below Moultonborough's ($28.14) and Conway's 15-year rate ($26.40 in 2025-26) (**derived** comparison).
   - citation: SAU 13 posting JobID 349; SAU 45 Job Openings; Conway file district-budget-and-cost fact 19 and table conway_para_and_regional_wages (CESP Agreement 2025–2028)
   - source: https://www.applitrack.com/sau13/onlineapp/default.aspx?AppliTrackPostingSearch=location:%22Kenneth+A+Brett+School%22
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Ranges are not like for like: Tamworth's is a hiring range "based on prior work experience," Moultonborough's includes differentials, and Conway's is a full step schedule (with a degree, $20.42–$26.90 in 2025-26). Tamworth's support staff schedule itself (TESPA) was not found online. See table tamworth_para_pay_neighbors. Raw: raw/money/wages/*; town/Conway/raw/money/contracts/cesp-2025-2028.ocr.txt
19. Governor Wentworth Regional's November 2026 postings for paraprofessionals at Ossipee Central, Tuftonboro and Kingswood list hours (15 to 34 a week) and say full-time positions include benefits, but give no hourly rate.
   - citation: Governor Wentworth Regional School District, Frontline job postings (viewed November 13, 2026)
   - source: https://www.applitrack.com/govwentworth/onlineapp/default.aspx
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Governor Wentworth Regional
   - note: Text: "Beginning the 2026-2027 school year, Ossipee Central School is seeking a dynamic paraprofessional ... The position is full time with benefits at 34 hours per week when school is in session. Please visit gwrsd.org staff tab to view specific benefits"; "This position is 32.5 hours per week, 6.5 hours a day and includes benefits" (Tuftonboro). The employee resource site linked from gwrsd.sau49nh.gov requires a sign-in. Raw: raw/money/wages/gwrsd-applitrack-postings-2026-11-13.*
20. Tamworth pays substitutes $150 a day for teaching positions and $120 a day for paraprofessionals, and $20 an hour for food service and custodial substitutes; in August 2026 the board kept these rates, noting Freedom pays $20 and Madison $25 an hour for food service and custodial substitutes.
   - citation: Kenneth A. Brett School, "Job Opportunities" page (Tamworth Substitute Rate for 2024-2025); Tamworth School Board minutes, August 20, 2026 (New Business E)
   - source: https://sites.google.com/tamworth.k12.nh.us/welcome-ka-brett-school/home/job-opportunities
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Page text: "Certified/No Certification- $150 per day ... Paraprofessional- $120 per day / Food Service Personnel- $20.00/hour / Custodian- $20.00/hour." Minutes: "Other districts do $150 for teachers ... Freedom is $20/hour for both food service and custodian and Madison is $25 for both ... VOTE: Shauna Peterson motioned to approve the current rates for this year." Raw: raw/money/wages/brett-job-opportunities-page.txt; raw/money/minutes/tsb-tamworth-august-20-2026-public-approved-minutes.*
21. Tamworth's support staff contract with the Tamworth Employee Support Association, approved by the board 5-0-0 for the March 2025 warrant, added an estimated $32,063 (2025-26), $32,039 (2026-27) and $31,458 (2027-28) in salary and benefit costs at current staffing; the teachers' contract on the 2026 warrant added $106,820, $77,984 and $86,380.
   - citation: 2025 warrant Article 3 (in Public Hearing minutes, February 7, 2025); 2026 warrant Article 3
   - source: https://drive.google.com/file/d/1errSVsknSjF7Tc2thdyD5hIGHLgEPozX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: 2025 text: "collective bargaining agreement reached between the Tamworth School District and the Tamworth Employee Support Association ... 2026 $32,063 / 2027 $32,039 / 2028 $31,458." The March 5, 2025 meeting minutes call the same article the "Tamworth Teachers Association" agreement and record that it passed on a voice vote. 2026 text: "Tamworth Education Association ... 2027 $106,820 / 2028 $77,984 / 2029 $86,380." Raw: raw/money/minutes/tsb-tamworth-february-6-2025-public-hearing-approved-minutes.*; raw/money/finance/tsd-2026-warrant.*

## district-tax-and-state-aid: Tamworth's School Taxes, Tuition's Share of the Rate, and State and Federal Aid

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. The Tamworth School District booked a "current appropriation" of $7,832,646.76 for 2025-26, which equals the $7,056,574 local school tax plus the $776,073 state education tax that NH DRA's 2025 tax rate setting raised in Tamworth.
   - citation: Tamworth School Board packet, February 26, 2026, p. 30 ("2025-2026 Tamworth Revenue," 2/1/2026); NH DRA 2025 tax rate calculation data (library dra-tax-rates.csv)
   - source: https://drive.google.com/file/d/1d8wVyA1kBtoqLZ16nlfdpPyL2ilzcEVP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Packet text: "01.1111.000.000 CURRENT APPROPRIATION ($7,832,646.76) $0.00 ($4,675,000.00) ($3,157,646.76)" (budget, YTD received $4,675,000, balance). Derived: 7,056,574 + 776,073 = 7,832,647. Tamworth's DRA rates and its local school and state education tax dollars for 2014–2025 are in the site's data (property_tax, Tamworth district); the two amounts match it (checked November 15, 2026). Raw: raw/money/packets/tsb-packet-2026-02-26-p30-fy26-revenue.*; raw/money/state-data/dra-tax-rates-tamworth.csv
2. The district's own tax-impact sheet divides each budget change by Tamworth's total assessed value ($735,906,312 as of December 15, 2025), and by that method its proposed 2026-27 budget and articles would raise the school tax by $1.950 per $1,000 ($195.04 on a $100,000 home), with net assessment rising from $7,796,246 to $9,231,588.
   - citation: Annual Report FY2025, "Tax Impacts of Proposed Budget & Warrant Articles 2026-2027," p. 36
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Tamworth
   - note: Rows read from the rendered page: "Total Appropriations $10,872,748 $9,586,044 $1,286,704 $1.748 ... Estimated Adequacy -$748,713 -$1,006,653 $257,940 $0.351 ... NET ASSESSMENT $9,231,588 $7,796,246 $1,435,342 $1.950"; "TOTAL ASSESSED VALUATION AS OF 12/15/2025 OF $735,906,312 WAS USED FOR CALCULATION OF PROJECTED TAX RATE IMPACTS. ACTUAL CALCUATIONS MAY VARY." The $735,906,312 equals DRA's and NH DOE's 2025 assessed valuation with utilities for Tamworth in the site's data (property_tax, Tamworth district; checked November 15, 2026). Transcribed from image. Raw: raw/money/finance/ar2025r-p36-a.png, ar2025r-p36-b.png; tsd-annual-report-fy2025-excerpt.*
3. By the district's own per-$1,000 method, Tamworth's 2025-26 Kennett tuition ($1,543,997) equals about $2.10 per $1,000 of assessed value, Moultonborough Academy tuition ($153,293) about $0.21, and Tamworth's SAU 13 share ($485,186) about $0.66, or roughly 22%, 2% and 7% of the $9.59 local school rate if each were paid wholly from local property tax (**derived**).
   - citation: Approved 2025-26 budget lines (August 21, 2025 packet, p. 25); 2025 warrant Article 2; DRA 2025 assessed value with utilities
   - source: https://drive.google.com/file/d/1W4iPryvUN7uRu3pTTKzdCVdcExqAsWVv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Tamworth
   - note: Derived: 1,543,997 ÷ 735,906.312 = $2.098; 153,292.61 ÷ 735,906.312 = $0.208; 485,186 ÷ 735,906.312 = $0.659; 2.098 ÷ 9.59 = 21.9%; 0.659 ÷ 9.59 = 6.9%. Illustrative only: the school tax is the whole budget less state aid and other revenue, so no single line is "paid by" the tax. The question asked about the $13.33 equalized rate; these figures use the actual (assessed) basis, as the district does. Tamworth's 2025 local school rate ($9.59, DRA) and its assessed valuation with utilities ($735,906,312, DRA and NH DOE) are in the site's data (property_tax, Tamworth district) and match (checked November 15, 2026). See table tamworth_tax_per_1000_by_line. Raw: raw/money/packets/tsb-packet-2025-08-21-p25-29.*; raw/money/state-data/dra-tax-rates-tamworth.csv
4. For 2026-27 the same method gives about $2.11 per $1,000 for Kennett tuition ($1,549,098), $0.39 for Moultonborough Academy ($283,844) and $0.73 for the SAU 13 share ($540,350), measured against the 2025 assessed value because the 2026 rate was not yet set (**derived**).
   - citation: 2026-27 proposed budget (public hearing packet, February 4, 2026, p. 6); 2026 warrant Article 2
   - source: https://drive.google.com/file/d/1N1C02RanGP6eYfUA2_hgKGNjpWnjyPEa/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Tamworth
   - note: Derived: 1,549,098 ÷ 735,906.312 = $2.105; 283,844 ÷ 735,906.312 = $0.386; 540,350 ÷ 735,906.312 = $0.734. The library's DRA file has no 2026 rate for Tamworth as of November 8, 2026, and the site's data stops at tax year 2025; the valuation is the 2025 one in the site's data (property_tax, Tamworth district). Raw: raw/money/packets/tsb-hearing-packet-2026-02-04-p6.*; raw/money/finance/tsd-2026-warrant.*
5. In 2025-26 the district returned $218,750 of fund balance to reduce taxes and used $300,000 of fund balance for the building capital reserve, and in September 2026 the board voted to keep the full 5% set-aside ($362,629) from 2025-26.
   - citation: Annual Report FY2025, Tax Impacts sheet, p. 36; Tamworth School Board minutes, September 17, 2026 (Business Administrator's Report)
   - source: https://drive.google.com/file/d/19Gsr_2sNor5icgbRcrT5NZsTUYk8lb_X/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Sheet rows: "Fund Balance Voted for Warrant Articles -$200,000 -$300,000 ... Fund Balance Returned to Offset $0 -$218,750." Minutes: "VOTE: Motion by Shauna Peterson to retain the full 5% fund balance ($362,629), seconded by Hillary Behr. All in favor." In August 2024 the board voted "to return $300,000 of undesignated fund balance." Raw: raw/money/finance/ar2025r-p36-a.png; raw/money/minutes/tsb-tamworth-september-17-2026-public-approved-minutes.*, tsb-tamworth-august-15-2024-approved-minutes.*
6. Tamworth's extraordinary need grant, the largest part of the fall in its state aid from FY2024 to FY2027, shrank as its equalized property value per free- or reduced-lunch pupil rose from $4.23 million (FY2024) to $6.94 million (FY2027).
   - citation: NH DOE adequacy aid municipal summaries, FY2024 and FY2027 (library adequacy-aid.csv)
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/fy-27-adequacy-muni-summary.xlsx
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Tamworth
   - note: CSV components: ev_per_frl_pupil "4231339.1713" (2024), "6939899.6564" (2027). Derived: the extraordinary need grant fell $535,895 ($551,094.55 to $15,199.36) of the $694,925 fall in the total state grant ($2,152,101.10 to $1,457,176.12). These DOE figures match the site's database; Tamworth's full calculation for FY2020–FY2027 (each grant, the counts and equalized value) is in the site's data (adequacy_aid, Tamworth district); value per pupil is not. In June 2026 the business administrator said Madison's aid fell "because of the increase in equalized valuation rather than enrollment" and that "The local reval doesn't play into it, the DOE has its own valuation" (minutes, June 18, 2026). Raw: raw/money/state-data/adequacy-aid-tamworth.csv; raw/money/minutes/tsb-tamworth-june-18-2026-approved-minutes.*
7. The district's budget estimates for adequacy aid fell from $1,059,635 for 2025-26 to $748,713 for 2026-27 (down 29.34%), which its tax-impact sheet counts as adding $0.351 per $1,000 to the 2026-27 school rate.
   - citation: Annual Report FY2025, "Tamworth Estimated Revenue," p. 33, and Tax Impacts sheet, p. 36
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Revenue page: "01.3110.000.000 ADEQUACY AID 748,713.00 1,059,635.00 (310,922.00) -29.34%." Tax sheet: "Estimated Adequacy -$748,713 -$1,006,653 $257,940 $0.351" (the sheet's 2025-26 column uses the final $1,006,653). The district's budget estimates differ from NH DOE's grants in the site's data (adequacy_aid, Tamworth district): $1,006,653.37 for FY2026 and $711,277.12 for FY2027 (October 1, 2026). Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.*; ar2025r-p36-a.png
8. At its February 2025 budget hearing the board described the school budget as funded 16% by federal and state money and 84% by local budgets; for 2026-27, the FY2027 state grant ($1,457,176) equals about 13% of the $10,872,748 in proposed appropriations, and the part beyond Tamworth's own state education tax ($711,277) about 7% (**derived**).
   - citation: Tamworth Public Hearing minutes, February 7, 2025; NH DOE FY2027 adequacy calculation; Annual Report FY2025, p. 36
   - source: https://drive.google.com/file/d/1coSMPexYzHIijpM_bSj_9MtATSkYcCSr/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Minutes: "● Federal / State Funding 16% ● Local Budgets 84%." Derived: 1,457,176 ÷ 10,872,748 = 13.4%; 711,277 ÷ 10,872,748 = 6.5%. The FY2027 state grant and adequacy grant match the site's database; the full calculation is in the site's data (adequacy_aid, Tamworth district). Whether the burden is "disproportionate" is a judgment the data can't settle; these are the shares. Raw: raw/money/minutes/tsb-tamworth-february-6-2025-public-hearing-approved-minutes.*; raw/money/state-data/adequacy-aid-tamworth.csv
9. Tamworth School District received federal Small, Rural School Achievement (REAP) awards of $15,258 (2019), $6,849 (2020), $10,412 (2021), $868 (2022) and $7,731 (2023); USAspending.gov lists no later award to the district through September 2026.
   - citation: USAspending.gov award search, CFDA 84.358, recipient "TAMWORTH SCHOOL DISTRICT"
   - source: https://api.usaspending.gov/api/v2/search/spending_by_award/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Rows: "S358A193218 | TAMWORTH SCHOOL DISTRICT | 15258.0 | 2019-07-01 | 84.358 | SRSA APPLICATION"; "S358A232548 | ... | 7731.0 | 2023-07-01 | 84.358 | SMALL, RURAL SCHOOL ACHIEVEMENT PROGRAM." The site's DOE-25 data show $7,731.00 under account 4310 in FY2025, matching the 2023 award. In August 2023 a board member asked what REAP stands for (minutes). ED's FY2025 eligibility spreadsheet could not be opened (data.ed.gov is a script page). See table tamworth_srsa_awards. Raw: raw/money/state-data/usaspending-tamworth-awards.json, usaspending-query.txt
10. Tamworth's Title I allocation was $202,896.41 for 2025-26 and $189,894.36 for 2026-27 (down about 6%, **derived**), alongside IDEA special education grants of $82,218.13 and $81,439.44, and Title II and IV grants of about $22,000–$32,000 each.
   - citation: Tamworth School District Grant Summary as of 11/10/2026 (November 17, 2026 packet, p. 37)
   - source: https://drive.google.com/file/d/1LjBjD-dLSbgSPdRK736L2I9dQgBZT9f-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Rows: "Title I Part A 20270712 8/19/2026 9/30/2027 $189,894.36"; "Title I Part A 20260474 8/16/2025 9/30/2026 $202,896.41"; "IDEA 20270737 9/30/2028 $81,439.44"; "IDEA 20260499 ... $82,218.13"; "Title II Part A ... $32,340.61"; "Title IV Part A ... $22,582.13." In April 2026 the superintendent said Title I would be funded fully nationally but "The poverty level in NH has gone down, so we'll get 6% less" (minutes, April 16, 2026). The 2025 hearing noted Brett "is a Title I school, and can serve all students with additional reading support." Raw: raw/money/packets/tsb-packet-2026-11-17-p1-2-10-37-38-48-52.*; raw/money/minutes/tsb-tamworth-april-16-2026-approved-minutes.*
11. Tamworth's 2026 warrant asked voters to appropriate $400,000 so the district could accept and spend state and federal grants, with nothing raised by local taxation, which the business administrator tied to an expected Title I allocation.
   - citation: 2026 warrant Article 8; Public Hearing minutes, February 4, 2026
   - source: https://drive.google.com/file/d/1errSVsknSjF7Tc2thdyD5hIGHLgEPozX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Warrant: "raise and appropriate the sum of $400,000 for the purpose of applying for, accepting, and expending state and federal grant funds ... with no amount to be raised by local taxation." Hearing: "Business Administrator Heather Sherwood reported that there is an expectation that we will receive funding because of the Title 1 School allocation." Raw: raw/money/finance/tsd-2026-warrant.*; raw/money/minutes/tsb-tamworth-public-hearing-special-school-board-february-4-2026-approved-minutes.*
12. In May 2026 the board voted unanimously to stop billing Medicaid for school services, after the business administrator said a Medicaid audit took 40 hours of staff time and reimbursement, once up to $20,000 a year, had become "much less."
   - citation: Tamworth School Board minutes, May 21, 2026 (Business Administrator's Report)
   - source: https://drive.google.com/file/d/1iABSXKEbM6xyEyLrqiTJWPIaxu9t3SUX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "had a Medicaid audit and it took 40 hours of staff time ... She's proposing that we don't participate in Medicaid to Schools because the administrative burden is so high compared with what we get from it ... We used to get up to $20,000 a year, now it's much less ... VOTE: Motion by Shauna Peterson to stop participating in Medicaid to Schools." Site DOE-25 data show Medicaid revenue of $24,708.94 (FY2023) and $2,574.18 (FY2025). Library topic federal-medicaid-to-schools-nh. Raw: raw/money/minutes/tsb-tamworth-may-21-2026-amended-approved-minutes.*; raw/money/state-data/site-db-tamworth-queries.txt
13. As RSA 32:5-d requires, the SAU 13 business office posts the state aid Tamworth receives; by September 2026 it showed $233,058.93 for 2026-27, including a first adequacy payment of $142,255.00.
   - citation: SAU 13 Business Office, "Tamworth School District - State Aid Received 2026-2027"
   - source: https://docs.google.com/spreadsheets/d/1Nbz82H9HT6CqhQgUay2rOhTUWoPtNCX5oDZB5yURSew
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Sheet text: "State Funding Received for SY 2026-2027,,,\"$233,058.93\"" and "State Adequacy Aid,\"$142,255.00\"". The page cites "RSA 32:5-d requires school districts to post the amount of state aid they receive on their official website within 30 days." Linked from https://sites.google.com/sau13.org/sau-13-business-office/home. Raw: raw/money/finance/tsd-state-aid-received-2026-27.csv

## district-tuition-contracts: Tamworth's Kennett and Moultonborough Academy Agreements

- kind: local
- question_type: governance_money
- description: A district's tuition contracts and agreements with other districts and schools: terms, cost formulas, caps, length, renewal, transportation and special education

1. Under its 2003 agreement with Conway, the Tamworth School District must send "at least ninety percent (90%)" of its grade 9–12 students to Kennett and pay for their transportation, and Conway agrees to accept all high school students Tamworth sends and educate them on the same terms as Conway students.
   - citation: Conway Tuition Agreement, Grades 9-12, Tamworth School District and Conway School District (May 2003), Section I and preamble
   - source: https://drive.google.com/file/d/1yzFePgCx5BWzBzWIiemUeeDmObWxExQI/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "agrees to accept all high school students sent by the Tamworth School District"; "Tamworth School District shall send at least ninety percent (90%) of its pupils, grades 9 through 12, with the exceptions hereinafter noted, to Conway for schooling; and Tamworth School District shall be responsible for the transportation methods and expenses." Signed by Tamworth's board "4-29-03." In February 2025 the board chair said "Current Conway Contract states 10% of student population may attend elsewhere." Transcribed from image. Raw: raw/money/contracts/contract-9-12-tamworth-conway.pdf, .ocr.txt
2. The 2003 agreement runs for a minimum of 20 school years from the opening of the new high school and ends then if either side gives written notice before the end of the 17th fiscal year; otherwise it continues year to year, and either side can end it with notice naming a last year at least three full fiscal years later.
   - citation: Tamworth–Conway Tuition Agreement (2003), Sections II and III
   - source: https://drive.google.com/file/d/1yzFePgCx5BWzBzWIiemUeeDmObWxExQI/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "shall continue for a minimum term of twenty (20) school years. This Agreement shall terminate at the end of such minimum term if either party gives to the other, at any time prior to the expiration of the seventeenth (17) fiscal school year ending June 30 of such minimum term, written notice of such termination"; "Such notice shall specify the last school year for which the agreement shall be effective, which shall be at least the third (3rd) full fiscal school year ending June 30 following the school year during which the notice is given." The contract does not set a cap on how many students Conway accepts. Transcribed from image. Raw: raw/money/contracts/contract-9-12-tamworth-conway.ocr.txt
3. The 2003 agreement sets Tamworth's charge as its share of Kennett's operating cost, figured 65% on its share of average daily membership in attendance and 35% on its share of the towns' equalized property value, applied to Conway's current approved budget plus the Northeast urban CPI plus 2.5%, then trued up to actual cost the next year; bonds and a facilities maintenance fund are shared by property value alone.
   - citation: Tamworth–Conway Tuition Agreement (2003), Section X.A–D
   - source: https://drive.google.com/file/d/1yzFePgCx5BWzBzWIiemUeeDmObWxExQI/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "The Conway School Board shall annually set each district's cost based upon Conway's current year approved budget; plus an inflation factor equal to US Department of Labor Consumer Price Index - Size A - Northeast Urban (October of current year) plus 2.5%; plus or minus the net actual expenses for the prior year ... no later than November 30th"; "a combination of 35% of the town's equalized value ... and 65% of the town's average daily membership in attendance." There is no cap on yearly increases (same as Bartlett's 2003 contract; Bartlett file district-tuition-contracts fact 3). Raw: raw/money/contracts/contract-9-12-tamworth-conway.ocr.txt
4. Conway's charge to Tamworth for 2026-27 is $1,549,098: $1,545,301 for operations (Tamworth's 76.61 students were 12.31% of Kennett's attendance and its property value 6.97% of the towns' total) plus $3,797 for the maintenance trust and no bond payment, or about $20,221 per Tamworth student (**derived**).
   - citation: Annual Report FY2025, "2026-2027 Tuition Contracts," p. 32
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Rows read from the rendered page (Tamworth column): "$744,697,730 / 6.97% / 76.61 / 12.31% ... Plus Conway 25-26 Approved Bdgt. $1,540,667 / +/- 24-25 Adjustment to Prev. Actual $563 / Plus CPI + 2.5% $86,277 / +/- Adjust. to Prev. Yr. ADM ($82,207) / HIGH/VOC. OPERATIONS TOTAL $1,545,301"; maintenance trust "$3,308 $489 $3,797"; bond totals "$0". Derived: 1,549,098 ÷ 76.61 = $20,221; Tamworth's combined share 1,540,667 ÷ 14,751,561 = 10.44%, below its 12.31% attendance share because its property share is lower. The 2026-27 budget line is the same $1,549,098. See table tamworth_kennett_charge. Transcribed from image. Raw: raw/money/finance/ar2025r-p32-top.png, ar2025r-p32-bottom.png
5. For 2024-25 Conway charged Tamworth $1,414,341 ($1,410,252 for operations and $4,089 for the maintenance trust) for 85.09 students, about $16,622 each, so the charge per Tamworth student rose about 22% from 2024-25 to 2026-27 while Tamworth's Kennett attendance fell 10% (**derived**).
   - citation: Annual Report FY2023 (published early 2024), "2024-2025 Tuition Contracts"
   - source: https://drive.google.com/file/d/1JrQuhPXCXaTFqvIZoJUcFlUbSWPz_RAo/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Rows read from the rendered page (Tamworth column): "$667,256,461 / 7.51% / 85.09 / 12.54% ... Plus Conway 23-24 Approved Bdgt. $1,564,770 / ($291,156) / $95,451 / $41,187 / $1,410,252"; maintenance "$3,563 $526 $4,089". Derived: 1,414,341 ÷ 85.09 = $16,622; 20,221 ÷ 16,622 = 1.217; 76.61 ÷ 85.09 = 0.900. Actual 2024-25 spending was $1,414,340 (working budget v4). Transcribed from image. Raw: raw/money/finance/ar2024r-p33-bot.png, tsd-annual-report-fy2023-excerpt.*
6. On February 15, 2024 the Tamworth School Board voted unanimously to send Kennett a letter cancelling the Tamworth–Conway contract as of 2027, after a 2022–23 committee had noted that June 30, 2024 was the deadline to tell Conway if Tamworth would not send all its students to Kennett.
   - citation: Tamworth School Board minutes, February 15, 2024 (New Business A); High School Options Committee minutes, October 18, 2022
   - source: https://drive.google.com/file/d/13kfuf8e_iiGpmqYR-hB5MYQ6jpE7pWcP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "A motion to send Kennett a letter to cancel the contract between the Tamworth and Conway School Boards as of 2027 was made by Siena Kaplan-Thompson and seconded by Dexter Harding. The motion passed unanimously." Committee: "June 30, 2024 – by this date we would tell Conway if we are NOT sending all kids to KHS ... Fall 2027 – earliest date we can send kids anywhere but KHS." Freedom's options study says the agreement "is due to expire in 2027 with notification to exit the agreement in 2024." The letter itself was not found. Raw: raw/money/minutes/tsb-tamworth-february-15-2024-approved-minutes.*; raw/money/hs-options/hsoc-minutes-2022-10-18.txt
7. At the February 2025 hearing the board chair said the Conway contract expires at the end of June 2027, that it was being renegotiated, and that tuition rates for 2025-26 had been set and were locked in.
   - citation: Tamworth Public Hearing minutes, February 7, 2025
   - source: https://drive.google.com/file/d/1coSMPexYzHIijpM_bSj_9MtATSkYcCSr/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "When is the Conway contract expiring? ■ Chair Jack Waldron responded end of June 2027 ■ Currently in the process of negotiation"; "Inquiry about Conway Tuition formula, and if costs are locked in for School Year 2025-26 ● Chair Jack Waldron responded that tuition rates have been set and are locked in." The FY2025 board report says the contract "expires on 6/30/2027." Raw: raw/money/minutes/tsb-tamworth-february-6-2025-public-hearing-approved-minutes.*; raw/money/finance/tsd-annual-report-fy2025-excerpt.*
8. Tamworth's Kennett negotiations have run since 2023: the board chair said in December 2023 they were "basically not happening," Conway was ready to start in July 2024, the SAU 13 boards agreed in June 2025 to negotiate with Kennett separately while keeping each other informed, and Tamworth's team met Conway in August 2025.
   - citation: Tamworth School Board minutes, December 21, 2023; July 18, 2024; June 19, 2025; August 21, 2025
   - source: https://drive.google.com/file/d/16jaEpkYx5Bf_-mWEQgjTH3ts6o-xXlZ5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Texts: "Jack Waldron reported that negotiations are basically not happening" (2023); "Conway is now ready to start negotiations on KHS tuition" (July 2024); "Moving forward each school board will meet independently with Kennett, while keeping the other boards informed" (June 2025); "Jack Waldron, Dexter Harding and Heather Sherwood met with Conway School District to discuss the Kennett High contract" (August 2025). Conway's side: Conway file district-tuition-contracts fact 8. Raw: raw/money/minutes/tsb-tamworth-december-21-2023-approved-minutes.*, tsb-tamworth-june-19-2025-approved-minutes.*, tsb-tamworth-august-21-2025-approved-minutes.*
9. In December 2025 the superintendent said the district's attorney advised against putting a Kennett tuition option on the March 2026 warrant, because if voters rejected it the board would decide where students attend, and in February 2026 he said negotiations continued and "Since there isn't an accepted offer, it is not going on the warrant."
   - citation: Tamworth School Board minutes, December 18, 2025 (Business Administrator's Report C); February 26, 2026 (New Business D.3)
   - source: https://drive.google.com/file/d/1ZZglHlOCawKaOOexz3vEcn_S_R9dTgUJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: December text: "Superintendent Michael Whaland discussed the Kennett Tuition option. o The Attorney to the District advised that the option should not be put on the warrant. If included on the warrant and voters do not approve, the Board would decide where students would attend ... Dr. Whaland stated that the current agreement allows students to finish their education" (about Moultonborough). February text: "Kennett Negotiations: o Dr. Whaland reported that they are still negotiating." Raw: raw/money/minutes/tsb-tamworth-december-18-2025-approved-minutes.*, tsb-tamworth-february-26-2026-amended-approved-minutes.*
10. Through fall 2026 the board discussed "High School negotiations with SAU 9" in non-public sessions (September 1 and October 13), its chair told a resident on September 17 that "we are still in negotiations," a "School Tuition Presentation" was scheduled for October 7, 2026 in the Brett gym, and the November 17, 2026 agenda lists "Negotiations," "Community Letter" and "Information Night."
   - citation: Tamworth School Board minutes, September 1, 2026 (non-public draft, in September 17 packet), September 17, 2026; October 13, 2026 non-public draft minutes and November 17, 2026 agenda (November 17 packet)
   - source: https://drive.google.com/file/d/1LjBjD-dLSbgSPdRK736L2I9dQgBZT9f-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Texts: "Discussion regarding High School negotiations with SAU 9" (September 1); "She wants to know where we are at with the Conway School? Shauna Peterson replied 'we are still in negotiations'" (September 17); "School Tuition Presentation: October 7, 2026 @ 6:00 PM, K. A. Brett Gymnasium"; "Session 2: Discussion regarding ongoing negotiations for High School students ... No actions taken" (October 13); agenda "SUPERINTENDENT'S REPORT ... B. Negotiations C. Community Letter D. Information Night." The presentation's content was not posted. Raw: raw/money/packets/tsb-packet-2026-09-17-p15.*, tsb-packet-2026-11-17-p1-2-10-37-38-48-52.*; raw/money/minutes/tsb-tamworth-september-17-2026-public-approved-minutes.*
11. As of November 13, 2026, SAU 9's tuition page lists 2027 contracts (approved by the State Board, starting in 2027-28) only for Albany, Bartlett, Eaton and Jackson; Tamworth's listed contract is still the current one.
   - citation: SAU 9, "Tuition Agreement Overview" (Tuition Contracts – Current; Tuition Contracts – Effective 2027)
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Page text: "Tuition Contracts - Effective 2027 / Please Note: The following contracts have been ratified by the respective Boards and approved by the State Board of Education. They will go into effect as of the start of the 2027-28 School Year. 7-8 TUITION CONTRACTS Albany & Conway Eaton & Conway 9-12 TUITION CONTRACTS Albany & Conway Bartlett & Conway Eaton & Conway Jackson & Conway Jackson & Fryeburg Academy." Those contracts drop property value from the formula and use Conway's DOE-25 cost per pupil plus CPI plus 2.5% (Conway file district-tuition-contracts fact 5); Bartlett's has a 75% minimum-attendance clause (Bartlett file). Raw: raw/money/web/sau9-tuitions-2026-11-13.*
12. In August 2025 the superintendent reported that some parents had asked SAU 13 to look at a possible agreement with the Governor Wentworth Regional School District (Kingswood), and Conway board members said on November 5, 2026 that SAU 13 had presented a tuition contract with Governor Wentworth the previous Monday; Tamworth's posted minutes through October 2026 record no vote on a Governor Wentworth contract.
   - citation: Tamworth School Board minutes, August 21, 2025 (Superintendent's Report C); Conway School Board special meeting draft minutes, November 5, 2026 (Conway file district-tuition-contracts fact 8)
   - source: https://drive.google.com/file/d/1Gsd2U6ef9Kg7Y0f-t5tt5JdCPTu_6bKv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Tamworth text: "Prospective Tuition Conversation/GWSD / Whaland mentioned that some parents have asked the SAU to looking at a possible agreement with Governor Wentworth School District." Conway text: "on Monday night, SAU #13 presented a tuition contract with Governor Wentworth." Which SAU 13 district the Governor Wentworth contract is for is not stated. In February 2025 the superintendent said Freedom families in Freedom's Governor Wentworth pilot provide their own transportation. Raw: raw/money/minutes/tsb-tamworth-august-21-2025-approved-minutes.*; town/Conway/raw/money/minutes/csb-2026-11-05-special-draft.*
13. The 2003 contract's planning appendix sized the new eight-town high school for 1,000 students (425 from Conway), and Kennett enrolled 600 in March 2026, 68 of them from Tamworth, so the building is well below that planning figure (**derived**); Conway board members said in April 2026 that "Conway wants their students."
   - citation: Tamworth–Conway Tuition Agreement (2003), Appendix B (Banwell Architects, November 27, 2002); Conway file district-tuition-contracts fact 7; Conway School Board minutes, April 13, 2026
   - source: https://drive.google.com/file/d/1yzFePgCx5BWzBzWIiemUeeDmObWxExQI/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Appendix text: "the new facility contemplated would accommodate 1000[425 from Conway] High School (grades 9-12) from Eight Towns." The figure is a 2002 planning estimate, not a rated capacity. Conway text: "He stressed the need to have a good relationship with the sending towns and that Conway wants their students." No document was found in which Conway proposes capping sending-town enrollment. Raw: raw/money/contracts/contract-9-12-tamworth-conway.ocr.txt; town/Conway/raw/money/minutes/csb-2026-04-13.txt
14. Tamworth's first Moultonborough Academy agreement (2024-25), signed by Moultonborough on February 9, 2024 and Tamworth on February 14, 2024 and approved by the Tamworth board April 18, 2024, let Moultonborough accept up to 10% of Tamworth's eligible high school students for a one-year term, renewable by mutual agreement.
   - citation: High School Tuition Agreement between the Tamworth School District and the Moultonborough School District (2024-25), Sections 1–2 (April 18, 2024 packet, pp. 37–42); Tamworth School Board minutes, April 18, 2024
   - source: https://drive.google.com/file/d/14NiqomkOAgoqaid5ABOhh36BoiyOW8qF/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Moultonborough shall accept up to ten percent [10%] of eligible high school students residing in Tamworth"; "The term of this contract shall be for one (1) year ... July 1, 2024, and shall terminate on June 30, 2025, unless renewed by mutual agreement." Signatures "FEB 9, 2024 / 2/14/24." Board vote: "A motion to approve the tuition agreement was made by Kathi Padgett and seconded by Kevin Mahoney. The motion passed unanimously." Extended January 16, 2025 ("A motion to extend the contract with the Moultonborough School District ... passed unanimously"). Transcribed from image. Raw: raw/money/packets/tsb-packet-2024-04-18-p37-42-ma-agreement.*; raw/money/minutes/tsb-tamworth-january-16-2025-approved-minutes.*
15. The 2026-27 Moultonborough agreement, accepted by the Tamworth board unanimously on February 26, 2026 after Moultonborough ratified it, runs July 1, 2026 to June 30, 2027 and requires the two districts to declare by December 10, 2026 whether they intend to renew, expand or let it expire.
   - citation: High School Tuition Agreement (2026-27), Section 2 (February 26, 2026 packet, pp. 39–44); Tamworth School Board minutes, February 26, 2026
   - source: https://drive.google.com/file/d/1d8wVyA1kBtoqLZ16nlfdpPyL2ilzcEVP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "The term of this contract shall be for one (1) year, and shall commence with the school year beginning July 1, 2026, and shall terminate on June 30, 2027, unless renewed by mutual agreement of the parties. By December 10, 2026, the parties shall meet and declare whether it is their intent to renew and extend this Agreement, enter into another Agreement for attendance by more Tamworth students or permit this ..." Minutes: "Dr. Whaland reported that Moultonborough has ratified this agreement. VOTE: Motion by Dexter Harding to accept and enter into agreement ... The motion passed unanimously." The same minutes announce that the superintendent had accepted the Moultonborough superintendency from July 1, 2026. Transcribed from image. Raw: raw/money/packets/tsb-packet-2026-02-26-p45-50-ma-agreement.*; raw/money/minutes/tsb-tamworth-february-26-2026-amended-approved-minutes.*
16. Under both Moultonborough agreements the base tuition is Moultonborough's estimated average cost per high school student (less transportation), capped at the per-student tuition Conway charges Tamworth for the same year, with capital costs included; special education students pay the same base plus the actual cost of extra services in three tiers, and Tamworth pays in three installments (25%, 50%, 25%) with a June true-up.
   - citation: Moultonborough agreements (2024-25 and 2026-27), Sections 4–6
   - source: https://drive.google.com/file/d/1d8wVyA1kBtoqLZ16nlfdpPyL2ilzcEVP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Moultonborough shall charge Tamworth its estimated average per pupil cost for providing its students with a high school education ... However, the base tuition shall not exceed the per student tuition charged Tamworth by the Conway School District for the 2026-2027 school year ... no adjustments shall be made ... other than to back out its student transportation costs"; tiers 1–3 "$ Actual Cost"; "Capital Costs related to Moultonborough Academy shall be deemed to be included in the general tuition rate"; payments "a minimum of 25% ... October 15 ... 50% ... February 15 ... 25% ... May 1." Transcribed from image. Raw: raw/money/packets/tsb-packet-2026-02-26-p45-50-ma-agreement.ocr.txt, tsb-packet-2024-04-18-p37-42-ma-agreement.ocr.txt
17. Tamworth budgeted Moultonborough Academy tuition for 2026-27 at a rate of $20,221 per pupil, the same as its Kennett charge per pupil, and in January 2026 the superintendent said "the same dollar amount is paid for Kennett High School students as Moultonborough Academy students."
   - citation: 2026-27 proposed budget, account note on MA TUITION (public hearing packet, February 4, 2026, p. 6); Tamworth School Board minutes, January 15, 2026 (New Business A)
   - source: https://drive.google.com/file/d/1N1C02RanGP6eYfUA2_hgKGNjpWnjyPEa/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Account note: "SY2026-2027 Rate is $20,221 per pupil / Budgeted amount is: 8 Current Full Rate / 1 Current Reduced Rate / 6 Anticipated Full Rate" against a line of $283,844. Kennett: $1,549,098 ÷ 76.61 = $20,221 (**derived**, fact 4). The 2026-27 agreement also sets $20,221.00 as the rate "as to any Moultonborough Academy employees who are residents of Tamworth and attending Moultonborough Academy" (2024-25: $15,542). Transcribed from image. Raw: raw/money/packets/tsb-hearing-packet-2026-02-04-p6.*; raw/money/minutes/tsb-tamworth-january-15-2026-approved-minutes.*
18. In 2023 Tamworth's administration projected base tuition rates of $15,230 for Kennett, $16,532 for Moultonborough Academy, $18,200 for Fryeburg Academy, $22,500 for Kingswood and $27,909 for Inter-Lakes, alongside a Brett operating cost of $5,875,049 and Kennett tuition of $1,336,996 a year.
   - citation: Final Report of the Tamworth High School Options Committee (July 20, 2023), superintendent's presentation, pp. 28–29
   - source: https://drive.google.com/file/d/1hBKpwYCTt_0A-uPzAvNVuO8Bf2V0VZsd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Slide text: "Projected Base Tuition Rates and Totals / Kennett High School / Moultonborough Academy / Kingswood Regional High School / Fryeburg Academy / Inter-Lakes Middle/High School / $15,230 tuition rate / $16,532 ... $22,500 ... $18,200 ... $27,909"; "Annual Operating Cost of KA Brett $5,875,049 Annual HS Tuition Cost of KHS $1,336,996." Committee minutes (January 10, 2023) said the numbers "are moving targets" and were single-student out-of-town rates. Raw: raw/money/hs-options/hsoc-final-report-2023-07-20.pdf, .txt

## high-school-tuition-options: Who Can Choose Moultonborough Academy Instead of Kennett

- kind: local
- question_type: local_practice
- description: High school options for districts without a high school (already in `additional-data/district-practices.md`)

1. Tamworth has no attendance boundary between Kennett and Moultonborough Academy: any Tamworth resident student entering high school may apply for a Moultonborough seat, Kennett remains where all other Tamworth students go, and the board set a lottery for years when applications exceed the seats.
   - citation: Tamworth School Board minutes, February 15, 2024 (Old Business D) and March 21, 2024 (Old Business C); Moultonborough agreement (2024-25), Section 1
   - source: https://drive.google.com/file/d/14eHRykCsQaj1j59NozjpCMU5HMUOH048/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: February 2024 text: "Applications for MA from interested students must be turned in to the Brett School front office no later than 4:00 PM on April 15, 2024 ... The MA lottery will be held on April 18, 2024 at the school board meeting." March 2024: "A motion to approve the lottery procedure as proposed was made by Kevin Mahoney ... passed unanimously." The agreement covers "eligible high school students residing in Tamworth ... who seek a public high school education, other than at a Chartered Public School." The written lottery procedure was not posted. Raw: raw/money/minutes/tsb-tamworth-february-15-2024-approved-minutes.*, tsb-tamworth-march-21-2024-approved-minutes.*
2. The 2024 contract allowed up to 10% of Tamworth's eligible high school students at Moultonborough Academy, which the district's March 2024 notice described as "up to 6 Tamworth students," while the Kennett contract requires at least 90% of Tamworth's high school students to attend Kennett.
   - citation: Kenneth A. Brett School, High School Options Committee page ("Tamworth School District Notice," updated 3/04/2024); Moultonborough agreement (2024-25), Section 1; Tamworth–Conway agreement (2003), Section I
   - source: https://sites.google.com/tamworth.k12.nh.us/welcome-ka-brett-school/high-school-options-committee
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Notice: "the recently signed contract between Tamworth and Moultonborough which provides for up to 6 Tamworth students to attend Moultonborough Academy in September of 2024." The page was still unchanged on November 13, 2026. In March 2024 the district's lawyer said the 90% clause could be handled by sending fewer than 90% "and see what happens" or by phasing toward a new contract (minutes, March 21, 2024, non-public summary). Raw: raw/money/hs-options/brett-hs-options-committee-page.*; raw/money/minutes/tsb-tamworth-march-21-2024-approved-minutes.*
3. The 2026-27 Moultonborough agreement raises the limit to up to ten Tamworth students per grade, 40 in all.
   - citation: Moultonborough agreement (2026-27), Section 1
   - source: https://drive.google.com/file/d/1d8wVyA1kBtoqLZ16nlfdpPyL2ilzcEVP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Moultonborough shall accept up to ten students per grade level of eligible high school students residing in Tamworth each year, for a total of 40 students." The recital still reads "up to ten percent of its students." Transcribed from image. Raw: raw/money/packets/tsb-packet-2026-02-26-p45-50-ma-agreement.*
4. Every Tamworth applicant has been given a Moultonborough seat so far: two applied for 2024-25 and both were accepted; eight applied for 2025-26 and the board raised the budget from six to eight students; and in January 2026, with seven interested and six budgeted, the board voted to fund all seven without a lottery.
   - citation: Tamworth School Board minutes, April 18, 2024 (Old Business F); January 16, 2025 (New Business A); January 15, 2026 (New Business A)
   - source: https://drive.google.com/file/d/1vT154pmlCnkf_XLoj_5Lq-lct5_azL_h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Texts: "There were two students who applied to go to Moultonborough Academy next year, so both will be able to attend" (2024); "there were 8 students who submitted applications ... the budget for sending students to MA be increased from the current 6 students to 8" (2025); "seven (7) students are interested ... Currently, there are six (6) students budgeted ... VOTE: Motion to allocate all seven spots to Moultonborough Academy and not hold a lottery ... passed unanimously" (2026). Raw: raw/money/minutes/tsb-tamworth-april-18-2024-draft-corrected-minutes.*, tsb-tamworth-january-16-2025-approved-minutes.*, tsb-tamworth-january-15-2026-approved-minutes.*
5. Under the Moultonborough agreements, transportation is Tamworth's responsibility and "within the sole discretion of the Tamworth School Board"; Tamworth runs a bus, which the board chair put at $90,000 at the March 2025 meeting, and in January 2026 the principal said about three students ride it.
   - citation: Moultonborough agreements, Sections 4(b) and 14; annual meeting minutes, March 5, 2025; Tamworth School Board minutes, January 15, 2026
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Agreement: "The decision whether or not to provide transportation shall be within the sole discretion of the Tamworth School Board." 2025 meeting: "The budget includes ... a bus for 6-8 students attending high school at Moultonborough Academy ... Diane Bowles asked how much the bus to Moultonborough cost, and Jack Waldron said it costs $90,000." January 2026: "Principal Kara Robdau believes there are currently three students"; February 4, 2026 hearing: "the number fluctuates based on season, sports, etc." Bus routes are the daily agent's topic. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt; raw/money/minutes/tsb-tamworth-january-15-2026-approved-minutes.*
6. A Tamworth student accepted at Moultonborough Academy may stay through graduation even if the agreement ends, as long as the student shows "appropriate citizenship, attendance, and academic progress," and may be denied re-admission for failing to follow school rules after a hearing with the superintendent.
   - citation: Moultonborough agreements, Sections 6–7
   - source: https://drive.google.com/file/d/1d8wVyA1kBtoqLZ16nlfdpPyL2ilzcEVP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Upon expiration or termination of this Agreement, Moultonborough agrees to allow the continued attendance through graduation of those students initially accepted at Moultonborough Academy who exhibit appropriate citizenship, attendance, and academic progress"; "Tamworth students may be denied re-admission in subsequent years for failure to abide by school rules after a formal hearing with the Superintendent." Transcribed from image. Raw: raw/money/packets/tsb-packet-2026-02-26-p45-50-ma-agreement.ocr.txt
7. Tamworth students at Moultonborough Academy get the same access to career and technical education (the Lakes Region Technology Center) as Moultonborough students, including any school-day transportation Moultonborough provides to it, and Tamworth keeps its right to place special education students elsewhere and to reassign students for best interest or manifest educational hardship.
   - citation: Moultonborough agreements, Sections 1 and 19
   - source: https://drive.google.com/file/d/1d8wVyA1kBtoqLZ16nlfdpPyL2ilzcEVP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Tamworth students enrolled at Moultonborough Academy shall be afforded the same access to Career and Technical Education as is afforded to Moultonborough students. Any school day transportation provided to Moultonborough resident students to and from Career and Technical Training sites shall be provided to Tamworth students"; "Tamworth reserves the right to reassign regular education students ... in accordance with RSA 193:3 (I) or who demonstrate a manifest educational hardship in accordance with RSA 193:3 (II)." The career center name is from the 2023 committee comparison. Transcribed from image. Raw: raw/money/packets/tsb-packet-2026-02-26-p45-50-ma-agreement.ocr.txt
8. In July 2023 Tamworth's High School Options Committee recommended that the district pursue contracts with Kennett, Moultonborough Academy and Fryeburg Academy so families could choose among the three, with the same per-pupil cost and transportation to each as goals, after a survey with 143 responses.
   - citation: Final Report of the Tamworth High School Options Committee, July 20, 2023, p. 1–2
   - source: https://drive.google.com/file/d/1hBKpwYCTt_0A-uPzAvNVuO8Bf2V0VZsd/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "the committee finds that all three schools are appropriate for Tamworth students grades 9-12, and recommends the district pursue contracts with all three schools with the goal of offering Tamworth families a choice of the three high schools ... • Arrange that the per pupil cost be the same for each high school • Arrange transportation to each school"; "143 responses were ultimately gathered, from January 16 through May 25, 2023." At the February 2025 hearing the chair said Fryeburg's "Tuition rate and Maine Special Education impact consideration of Fryeburg Academy as an option." School comparisons are the high school agent's topic. Raw: raw/money/hs-options/hsoc-final-report-2023-07-20.*; raw/money/minutes/tsb-tamworth-february-6-2025-public-hearing-approved-minutes.*
9. The superintendent's FY2025 annual report calls the Moultonborough arrangement a "pilot" in its second year (2025-26) that "allows up to 10 percent of Tamworth's students to enroll at the Academy," and the board's report says it chose to continue the pilot for a third year.
   - citation: Annual Report FY2025, Superintendent of Schools Report, p. 13, and School Board Report, p. 12
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "The Tamworth School District is continuing its second year of a pilot tuition agreement with Moultonborough Academy through a formal Memorandum of Understanding. This partnership allows up to 10 percent of Tamworth's students to enroll at the Academy"; board: "deciding to continue for a third year the 'pilot' program of sending self-selecting Tamworth students to Moultonborough Academy." The 2026-27 agreement itself sets 10 per grade (fact 3). Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt

## district-facilities-and-capital: The Brett School HVAC Project, Boilers, Reserves and the Draft Capital Plan

- kind: local
- question_type: governance_money
- description: A district's school buildings: age, planned repairs, capital reserve funds, bonds and energy projects

1. The Tamworth School Board reported in early 2024 that the first of the three sections of the Brett School was "approaching 70 years of age," that an engineering study found much of the heating pipe "beyond its serviceable lifetime," and that federal COVID relief funds paid for the H L Turner system redesign and $160,000 of pipe.
   - citation: Annual Report FY2023 (published early 2024), Tamworth School Board Report
   - source: https://drive.google.com/file/d/1JrQuhPXCXaTFqvIZoJUcFlUbSWPz_RAo/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "We will begin work on revamping out HVAC system this summer. The first of the 3 sections in which Brett was constructed is approaching 70 years of age. During our engineering study we discovered that much of the current pipe is beyond its serviceable lifetime ... Both the redesign of the system by H L Turner and $160,000 worth or pipe needed for the project was paid for with Federal Covid relief funds ... At the conclusion of the project we will have a more energy efficient building with clean, healthy air circulation." Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2023-excerpt.*
2. Voters at an October 10, 2023 special meeting unanimously added $437,919 of extra state aid to the 2023-24 budget for the HVAC system, and the 2023-24 budget had already raised building costs 57% ($758,932 against $483,447) for HVAC equipment using federal relief funds.
   - citation: Special school district meeting minutes, October 10, 2023; annual meeting minutes, March 8, 2023 (Annual Report FY2023, p. 8)
   - source: https://drive.google.com/file/d/1355UDIEJDEAiqzzQQ5b4b4UhiWMZV72E/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: October text: "Article 1, which proposed the appropriation of $437,919 to be added to the current year School Budget ... the School Board is asking that the funds be added to the budget for this year rather taken as revenue, due to the need for a new HVAC ... system at the School, with the work spread over 6-7 years ... All members present voted aye." March 2023: "the largest increase in the budget this year is for the building ($758,932 proposed budget compared with $483,447 current budget, a 57% increase). This is related to upgrading the HVAC equipment using SFER funds." Raw: raw/money/minutes/tsb-special-school-board-meeting-october-10-2023-approved.*; raw/money/finance/tsd-annual-report-fy2023-excerpt.ocr.txt
3. The HVAC upgrade was first estimated at $3,500,000 and split into phases; Phase I (ducts and piping) was finished in July 2024, and the board chair then hoped to budget $500,000 a year, with a rooftop unit for classroom dehumidification estimated at $600,000–$700,000.
   - citation: Public Hearing minutes, February 4, 2026; Tamworth School Board minutes, August 15, 2024 (HVAC Report)
   - source: https://drive.google.com/file/d/1grtnHNy0zkbfdYNzn01it4COKKMXw3h6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: 2026 text: "Extra funds from COVID-19 were used to begin the project of updating the 70-year-old HVAC System. ▪ The original estimate was $3,500,000. ▪ It was determined that the project could be done in phases. ▪ Phase I was completed in July 2024." 2024 text: "Phase I (Laying Groundwork) of the HVAC finishing up ... Jack would like to see $500,000 budgeted every year ... A rooftop unit would allow dehumidification of some classrooms; cost currently estimated at $600-700,000." Raw: raw/money/minutes/tsb-tamworth-public-hearing-special-school-board-february-4-2026-approved-minutes.*, tsb-tamworth-august-15-2024-approved-minutes.*
4. The 2026 warrant asked for $500,000 raised by taxation to complete HVAC Phase II in summer 2026, placed as a separate article "so that the entire budget doesn't have to be voted down for one item," with a fallback article adding $200,000 to the building reserve if it failed.
   - citation: 2026 warrant Articles 4 and 5; Public Hearing minutes, February 4, 2026
   - source: https://drive.google.com/file/d/1errSVsknSjF7Tc2thdyD5hIGHLgEPozX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Warrant: "ARTICLE 4: To see if the School District will vote to raise and appropriate the sum of $500,000 for the purpose of completing Phase II of the HVAC project scheduled for summer 2026. This shall be a special warrant article pursuant to RSA 32:3, VI(d) and RSA 32:7, V. Said sum shall be raised by taxation." Hearing: "This was separated from the operating budget so that the entire budget doesn't have to be voted down for one item." The MS-26 shows the $500,000 as $1 engineering plus $499,999 building improvement. The meeting result was not found; the board later spent on Phase II (facts 5–6). Raw: raw/money/finance/tsd-2026-warrant.*, tsd-2026-ms26.*
5. On March 19, 2026 the board chose Meridian Construction's Phase II Option 1, priced just under $1,000,000 (two rooftop units and drop-in classroom units), over Option 2 ($588,150, one rooftop unit), and was told Phase III would cost an estimated $1.3–1.5 million.
   - citation: Tamworth School Board minutes, March 19, 2026 (Superintendent's Report A)
   - source: https://drive.google.com/file/d/1DjrGqMouYDMByhfzt4MvFpH6YAs228DN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Option #1 is coming in right under $1,000,000 and would provide 2 rooftop units and drop-in units into the classrooms ... Option #2 covers the main area and shared spaces. Only 1 rooftop unit would be installed, however, this would give the ability to do more with the boilers now, as they are approaching end of life. The total is $588,150 ... The cost of Phase III is estimated to be between $1.3 - $1.5 million. VOTE: Motion by Siena Kaplan-Thompson to accept Option #1 ... passed unanimously." Raw: raw/money/minutes/tsb-tamworth-march-19-2026-amended-approved-minutes.*
6. In July 2026 the board approved a $66,210 Meridian change order (steel reinforcement for the largest rooftop unit, extra masonry and a new controls interface), and in September 2026 it voted to spend up to $300,000 from the Renovation and Emergency Repairs capital reserve for Phase II.
   - citation: Tamworth School Board minutes, July 23, 2026 (Business Administrator's Report B); September 17, 2026 (New Business)
   - source: https://drive.google.com/file/d/15P3_IJt77di6si3_gjWP8XAKfdKcVLAm/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: July text: "a steel reinforcement is needed to better accommodate the weight of the largest rooftop unit ... unanticipated layers of masonry ... the old JACE will not communicate with the new system. The total amount of these changes are $66,210.00 ... passed unanimously." September text: "VOTE: Motion by Siena Kaplan-Thompson seconded by Hillary Behr to expend from Renovation and Emergency Repairs to School Facilities Capital Fund up to $300,000 for HVAC Phase II. All in favor." Raw: raw/money/minutes/tsb-tamworth-july-23-2026-public-approved-minutes.*, tsb-tamworth-september-17-2026-public-approved-minutes.*
7. Brett's two heating boilers are to be replaced only in Phase III; over winter break 2025-26 one failed, freezing pipes led to about $24,000 of repairs and insulation, and then the second boiler failed.
   - citation: Tamworth School Board minutes, January 15, 2026 (Superintendent's Report A)
   - source: https://drive.google.com/file/d/1vT154pmlCnkf_XLoj_5Lq-lct5_azL_h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "over the Winter Break, one of the boilers of the two-boiler system went down. There was also an issue with pipes freezing due to poor insulation. Repairs totaling approximately $24,000 were made ... Just after the 1st boiler was repaired, the 2nd boiler went out ... the boilers were not going to be replaced until Phase III of the HVAC project, and that any problems until then will require fixing." Raw: raw/money/minutes/tsb-tamworth-january-15-2026-approved-minutes.*
8. In August 2026 the business administrator said she would get updated Meridian pricing for Phase III, possibly $1.5–1.6 million, and information on bonding it, which would let the work happen in summer 2027 and "even out the tax bill"; otherwise about $800,000 would be needed in each of two budgets, and a bond would need a warrant article.
   - citation: Tamworth School Board minutes, August 20, 2026 (Business Administrator's Report B); September 17, 2026
   - source: https://drive.google.com/file/d/11m35F1QZ5am2vHTLf84WXHuUIbVeJW6-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Heather is seriously considering having Meridian give us a phase 3 pricing to complete the project ... Then she wants to consider bonding it. This was originally priced in 2022 ... we might be looking at a final phase 3 of $1.5 mil or $1.6. Bonding - she knows you pay interest, but it would even out the tax bill ... It would be on a warrant article ... Otherwise, we'd need to put half in the budget next year, then half the year after, and it could be $800k each year." September: "Talk of a potential bond to finish the project and even the tax implications." The district has no current debt (MS-26 debt service $0). Library topic budget-school-bonds. Raw: raw/money/minutes/tsb-tamworth-august-20-2026-public-approved-minutes.*; raw/money/finance/tsd-2026-ms26.ocr.txt
9. In January 2026 the Building Maintenance capital reserve held $418,415 and the Special Education capital reserve $283,702 (before interest); voters added up to $300,000 to the building reserve from fund balance in March 2025, and the 2026 warrant added up to $200,000 to the special education reserve.
   - citation: Tamworth School Board minutes, January 15, 2026 (Business Administrator's Report B); annual meeting minutes, March 5, 2025 (Article 4); 2026 warrant Article 7; minutes April 16, 2026
   - source: https://drive.google.com/file/d/1vT154pmlCnkf_XLoj_5Lq-lct5_azL_h/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: January text: "the current balance of the Special Education CRF is $283,702 not including interest. The Building Maintenance CRF balance is $418,415." 2025: Article 4 "up to $300,000 to be added to the Renovation and Emergency Repairs to School Facilities Capital Reserve Fund ... The motion passed on a voice vote." April 2026: "the warrant article to add $200k to the special education fund that was approved at the annual meeting helps." Raw: raw/money/minutes/tsb-tamworth-january-15-2026-approved-minutes.*, tsb-tamworth-april-16-2026-approved-minutes.*; raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt
10. Tamworth had no detailed capital improvement plan until June 2026, when a board member brought a rough draft of capital purchases and maintenance suggesting about $89,797.64 be set aside each year; in July 2026 the board created a Buildings and Grounds Committee, and in October 2026 it reviewed a form for tracking items in a seven-year plan.
   - citation: Tamworth School Board minutes, June 18, 2026 (Business Administrator's Report B); July 23, 2026 (Committee updates); October 13, 2026 draft (Old Business A)
   - source: https://drive.google.com/file/d/1aFnnqDp5EjrXULxTOIun2Al1S6uvNq9j/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: June text: "a rough draft of a CIP. We haven't had a detailed one in Tamworth, and the HVAC was in motion when she got here ... This is a mix of capital purchases and maintenance ... It comes to about $89,797.64, which should be set aside." July: "VOTE: A motion was made by Shauna Peterson to create a Buildings and Grounds Committee ... passed unanimously." October: "show more detail and tracking of CIP items in the 7-year plan ... Discussion about playground replacement, safety and boiler concerns." The draft plan itself was not posted. Raw: raw/money/minutes/tsb-tamworth-june-18-2026-approved-minutes.*, tsb-tamworth-july-23-2026-public-approved-minutes.*, tsb-tamworth-october-13-2026-public-draft-minutes.*
11. Other building items in 2025–2026 minutes include windows that do not open (some replaced earlier with federal relief funds), a driveway resealing moved to summer 2027 because of HVAC work, light fixtures put on hold during the HVAC project, and a fire suppression system and heat detector repair in June 2026.
   - citation: Tamworth School Board minutes, June 18, 2026; April 16, 2026 (Business Administrator's Report C); October 13, 2026 draft
   - source: https://drive.google.com/file/d/1LAdvc1YuudsJEjP5PF_bXRumaWstAnDa/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Texts: "There are some windows that don't open, we replaced some but not all with ESSR" (June); "VOTE: Shauna Peterson moved to expend the funds required to repair the heat detectors and the fire suppression system" (June); "Heather suggested moving the driveway work to next summer. The board agreed" (April); "Discussion on light fixtures being placed on hold due to HVAC project" (October). Raw: raw/money/minutes/tsb-tamworth-june-18-2026-approved-minutes.*, tsb-tamworth-april-16-2026-approved-minutes.*, tsb-tamworth-october-13-2026-public-draft-minutes.*
12. On energy, the board approved an LED lighting proposal in September 2026 subject to a check on flickering, LED lights were installed in 2023, and in 2025 the board tabled a Revision Energy solar contract offering rebates to the school and town until its questions were answered.
   - citation: Tamworth School Board minutes, September 17, 2026; August 17, 2023; February 20, 2025 and April 17, 2025 (Solar Project)
   - source: https://drive.google.com/file/d/19Gsr_2sNor5icgbRcrT5NZsTUYk8lb_X/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: September 2026: "VOTE: Motion by Shauna Peterson to approve the LED lighting proposal after the Business Administrator's investigation of flickering ... All in favor." February 2025: "Revision Energy is obligated by the state to offer rebates to school and town offices. The town has signed on already ... This decision has been tabled until the board has seen the contract." April 2025: "the proposed contract is currently being looked at." No later solar decision was found. Raw: raw/money/minutes/tsb-tamworth-september-17-2026-public-approved-minutes.*, tsb-tamworth-april-17-2025-approved-minutes.*
13. No roof project, roof assessment or roof reserve appears in Tamworth School Board minutes from July 2023 through October 2026, and no adopted five-year capital plan was found; the June 2026 draft is the first.
   - citation: Tamworth School Board minutes and packets, July 2023 – November 2026 (searched)
   - source: https://www.sau13.org/school-board/tamworth/agendas-packets-minutes
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: A statement about the documents searched (about 50 sets of minutes and about 30 board packets from July 2023 to November 2026; cited ones are in raw/money/; terms searched: roof, rooftop, shingle, membrane). "Rooftop" appears only for HVAC units. At Madison's June 1, 2026 board meeting the SAU 13 business administrator said "Tamworth would like to participate" in an infrastructure assessment ("ALPHA") (town/Madison/raw/kennett/minutes/madison-june-1-2026-public-approved-minutes.txt). Raw: raw/money/web/sau13-tamworth-drive-folder-listings.txt

## district-sau-governance: Tamworth's Share of SAU 13

- kind: local
- question_type: governance_money
- description: How a district shares an SAU: board seats and votes, how SAU costs are divided, and what the local board decides versus the SAU

1. Each SAU 13 district's share of the SAU budget is set half by its average daily membership in attendance and half by its equalized property value; for 2026-27 Tamworth has 50.20% of the students but 23.94% of the value, so it is apportioned 37.07%, or $540,350 of $1,457,486.
   - citation: Annual Report FY2025, "Apportionment for Fiscal Year 2026-2027 As Adopted by the Joint Board," p. 31
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Page text: "Each town's share of the SAU budget is based upon taking one-half of the average daily membership in attendance (ADM-A) at the end of the previous school year and one-half of the most recently published equalized valuation, including utilities"; row "Tamworth $744,697,730 165.15 23.94% 50.20% 37.07% $540,350"; total "$3,110,094,446 328.96 100.00% 100.00% 100.00% $1,457,486." The whole SAU budget and its history: SAU 13 fact: see Madison research. Read from the rendered page. Raw: raw/money/finance/ar2025-p31.png, tsd-annual-report-fy2025-excerpt.*
2. Tamworth's share of the SAU 13 budget grew from $252,935 in 2019-20 to $506,240 in 2024-25, dipped to $485,186 in 2025-26, and is $540,350 for 2026-27, while its share percentage stayed between about 37% and 40%.
   - citation: Annual Report FY2025, "Apportionment History 2020 through 2025 For Tamworth School District," p. 31; 2026 warrant Article 2
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Rows: "2025-2026 $711,885,882 175.73 24.52% 51.87% 38.19% $485,186 / 2024-2025 $667,256,461 189.45 24.59% 52.28% 38.44% $506,240 ... 2019-2020 $349,020,385 196.60 26.36% 49.42% 37.89% $252,935." See table tamworth_sau13_share. Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt
3. Tamworth voters approved the 2025-26 SAU budget article 86–13 at the March 2025 meeting after a board member said Tamworth's portion was down even though the overall budget was up, and a resident asked why the SAU budget had doubled in five years; the SAU budget is voted by all three towns and hand-counted in Tamworth because Madison uses SB2.
   - citation: Annual meeting minutes, March 5, 2025 (Article 2); Public Hearing minutes, February 4, 2026 (Article 2)
   - source: https://drive.google.com/file/d/1grtnHNy0zkbfdYNzn01it4COKKMXw3h6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: 2025 text: "Shauna Peterson ... clarified that while the overall budget is up, Tamworth's portion is down compared to last year ... Kit Morgan asked a question about why the SAU budget doubled in the past five years ... The Superintendent responded that the budget provides savings within the three districts ... 86 voted in favor and 13 voted against." 2026 text: "Budget is voted on by all three (3) towns. • Article is a hand count vote, due to Madison having an SB2 form of government." Library topic budget-sau-budget-vote. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt; raw/money/minutes/tsb-tamworth-public-hearing-special-school-board-february-4-2026-approved-minutes.*
4. At the February 2026 hearing the board said Tamworth's SAU share could fall by about $85,000 if Madison took over the SAU 13 preschool program.
   - citation: Public Hearing minutes, February 4, 2026
   - source: https://drive.google.com/file/d/1grtnHNy0zkbfdYNzn01it4COKKMXw3h6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Discussion on the Tamworth share of the SAU Budget. o Possible reduction of $85,000 if Madison takes over the Preschool Program. o Superintendent Michael Whaland explained governance changes." Whether this happened, and the preschool itself: SAU 13 fact: see Madison research. Raw: raw/money/minutes/tsb-tamworth-public-hearing-special-school-board-february-4-2026-approved-minutes.*
5. Tamworth's HB 1265 report to voters lists the 2025-26 salaries of the two SAU administrators as apportioned to Tamworth: $51,044 for the superintendent and $36,281 for the business administrator.
   - citation: Annual Report FY2025, "HB 1265 - Mandatory Report to Voters on School District Expenses," pp. 66–68
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Top Administrator Salaries (2025-2026) / Superintendant $51,044 / Business Administrator $36,281"; "the top administrator salaries are not adjusted for inflation, are reported based on the district's SAU apportionment, and reflect the only two positions that meet the RSA's definition of administrator." Library topic budget-voter-information. Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt

## district-board-and-public-input: Tamworth School Board Meetings, Minutes, Livestreams and Hearings

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. Under Policy BEA (adopted September 18, 2025), the Tamworth School Board meets at least monthly, normally on the third Thursday at 5:30 p.m. at the Brett School, posts notice at least 24 hours ahead, sets aside time for public comment at every meeting (which may be limited to agenda items), and adjourns by 8:00 p.m. unless a majority votes to continue.
   - citation: Tamworth School Board Policy BEA, Regular Board Meetings
   - source: https://drive.google.com/file/d/1wqcreLkneZUDhl7We0YfjZrlrsmYysmu/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "regular meetings of the Board shall be held at the K.A. Brett School on the third Thursday of each month ... and shall begin at 5:30 p.m. Notice of all Board meetings will be posted in two appropriate places or printed in the local newspaper at least twenty-four (24) hours prior ... There will be time set aside at every meeting for public comment; such comments may be restricted to agenda items only ... School Board meetings will adjourn no later than 8:00 PM unless there is a majority vote." The board approved a revised BEA on April 16, 2026 (confirming the website is a posting place); the posted file is the 2025 version. Raw: raw/money/web/tamworth-policy-BEA.*; raw/money/minutes/tsb-tamworth-april-16-2026-approved-minutes.*
2. Tamworth's agendas, board packets and minutes are posted in folders on the SAU 13 website, by school year back to 2018-19, with draft and approved versions of public minutes and, when not sealed, non-public minutes; for example, the September 17, 2026 draft minutes were posted September 28 and the approved version October 14 (**derived** from the folder dates).
   - citation: SAU 13, "Tamworth - Agendas, Packets, & Minutes" (Drive folders viewed November 13, 2026)
   - source: https://www.sau13.org/school-board/tamworth/agendas-packets-minutes
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Listing rows: "TAMWORTH SEPTEMBER 17, 2026 PUBLIC DRAFT MINUTES.pdf Sep 28"; "TAMWORTH SEPTEMBER 17, 2026 PUBLIC APPROVED MINUTES.pdf Oct 14"; "TAMWORTH AUGUST 20, 2026 NON PUBLIC APPROVED MINUTES.pdf Oct 14"; packets such as "TAMWORTH NOVEMBER 17, 2026 BOARD PACKET.pdf Nov 12." Archive folders run "2018-2019" to "2025-2026." Raw: raw/money/web/sau13-tamworth-drive-folder-listings.txt, sau13-tamworth-agendas-packets-minutes.html
3. The SAU 13 minutes policy (BEDG) requires draft public minutes to be available at the SAU office within 5 business days of a meeting (unsealed non-public drafts within 72 hours) and approved, unsealed minutes to be posted on the district website.
   - citation: Freedom, Madison & Tamworth School Board Policy BEDG, Meeting Minutes, Section B
   - source: https://drive.google.com/file/d/1DNSiyevk_6IZmWPAy2RxMjL-uI7dRiJ6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Drafts for public sessions must be available within 5 business days of the meeting, while drafts of non-public session minutes that have not been sealed by the Board must be available within 72 hours (3 calendar days) of the meeting"; "all approved and unsealed minutes shall be posted in a consistent and reasonably accessible location on the District's web site." In March 2026 the minutes record that a board member "reported that there are some things that aren't being done, leading to a disagreement in the handling of non-public minutes" (minutes, March 19, 2026). Transcribed from image. Raw: raw/money/web/sau13-policy-BEDG.*; raw/money/minutes/tsb-tamworth-march-19-2026-amended-approved-minutes.*
4. On May 21, 2026 the board voted unanimously to livestream every meeting on YouTube Live with an Owl camera and keep the recordings on the school's YouTube account, with comments turned off and a conference kit for anyone who must attend remotely; the November 17, 2026 agenda lists the channel youtube.com/@KABSchoolTV.
   - citation: Tamworth School Board minutes, May 21, 2026 (Livestreaming and recording meetings); November 17, 2026 agenda
   - source: https://drive.google.com/file/d/1iABSXKEbM6xyEyLrqiTJWPIaxu9t3SUX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "The proposal is to livestream every meeting, and to record the livestream. o The recordings would be available on the school's YouTube account ... Comments will be turned off ... If someone needs to attend the meeting remotely, we'll use the conference kit ... VOTE: Motion by Hillary Behr to stream meetings through Youtube Live and the Owl ... passed unanimously." Agenda: "YouTube Link for online meeting access: https://www.youtube.com/@KABSchoolTV." The October 13, 2026 meeting was not streamed because it was rescheduled. In April 2026 the board noted earlier COVID-era streaming had "low participation." Raw: raw/money/minutes/tsb-tamworth-may-21-2026-amended-approved-minutes.*, tsb-tamworth-april-16-2026-approved-minutes.*; raw/money/packets/tsb-packet-2026-11-17-p1-2-10-37-38-48-52.*
5. Tamworth holds a budget hearing in early February and a traditional annual district meeting in the Brett gym in early March where voters debate and vote on the budget and articles, with board members elected by ballot the following week; for 2027 the hearing is set for February 10 and the meeting for March 3, with ballot voting on March 9.
   - citation: FY2028 Budget Timeline (November 17, 2026 packet, pp. 48–49); 2026 warrant; Public Hearing minutes, February 4, 2026
   - source: https://drive.google.com/file/d/1LjBjD-dLSbgSPdRK736L2I9dQgBZT9f-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Timeline text: "Wednesday, February 10, 2027: A public hearing is held for the proposed 2027-2028 budget and 2027 warrant ... Wednesday, March 3, 2027: The annual school district meeting takes place in the Kenneth A Brett School gymnasium where the school district warrant articles (including the budget) will be voted on by the public. Monday, March 9, 2027: Ballot voting for town and school district officials." The February 4, 2026 hearing drew "24 members of the public in person." Library topic budget-traditional-district-meeting. Raw: raw/money/packets/tsb-packet-2026-11-17-p1-2-10-37-38-48-52.*; raw/money/minutes/tsb-tamworth-public-hearing-special-school-board-february-4-2026-approved-minutes.*
6. At the March 5, 2025 annual meeting, an amendment to cut the operating budget by $750,000 failed 29–73 on a paper ballot and the budget then passed by voice vote, and the SAU article passed 86–13.
   - citation: Annual meeting minutes, March 5, 2025 (Annual Report FY2025, pp. 9–11)
   - source: https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "Mary Chase proposed an amendment to Article 1 to change the sum to $8,018,795 (a cut of $750,000) ... A vote was taken by paper ballot on the motion. The amendment did not pass, with 29 voting yes and 73 voting no. A voice vote was subsequently taken on Article 1, and the Article passed." Meeting ran 7:09–8:09 p.m. Transcribed from image. Raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.ocr.txt
7. The board voted 2–1 to put an article on the March 2026 warrant to adopt SB2 (official ballot voting on all school district questions, needing a three-fifths majority); the result was not found, but the district's FY2028 timeline still plans a traditional annual meeting on March 3, 2027.
   - citation: Public Hearing minutes, February 4, 2026 (New Article 10); 2026 warrant Article 10; FY2028 Budget Timeline
   - source: https://drive.google.com/file/d/1errSVsknSjF7Tc2thdyD5hIGHLgEPozX/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Warrant: "ARTICLE 10: To see if the School District will vote to ADOPT the provisions of RSA 40:13 (known as SB2) to allow official ballot voting on all issues before the Tamworth School District on the second Tuesday of March? (3/5-majority ballot vote required) (The School Board recommends this article. 2-1-0)." Library topics budget-adopting-rescinding-sb2 and budget-official-ballot-sb2. Raw: raw/money/finance/tsd-2026-warrant.*; raw/money/minutes/tsb-tamworth-public-hearing-special-school-board-february-4-2026-approved-minutes.*
8. The Tamworth School Board has five members (terms ending 2027–2029); its 2026-27 committees include a two-member negotiations committee, a capital improvement plan representative, a data committee and an SAU 9/13 joint board seat filled by the whole board.
   - citation: SAU 13, "Tamworth School Board Members" page; Tamworth School Board minutes, March 19, 2026 and September 1, 2026
   - source: https://www.sau13.org/school-board/tamworth/school-board-members
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Page text: "Shauna Peterson (2028) - Chairperson / Siena Kaplan-Thompson (2027) Vice Chair / Melanie Streeter (2029) / Devon Ames (2029) / Hillary Behr (2027) ... NEGOTIATIONS COMMITTEE Devon Ames, Shauna Peterson ... SAU 9/13 AREA JOINT BOARD Board as a whole ... CIP Hillary Behr ... DATA COMMITTEE Board as a whole." Elected officials' names as posted. Raw: raw/money/web/sau13-tamworth-board-members.txt
9. Tamworth residents have no vote on the Conway or Moultonborough school boards; the Kennett contract requires Conway to meet jointly with all sending boards at least three times a year, and the Moultonborough agreement gives Tamworth a non-voting member on Moultonborough's board, two joint board meetings a year, and the right for Tamworth citizens to address Moultonborough's board on high school issues.
   - citation: Tamworth–Conway agreement (2003), Section VI; Moultonborough agreement (2026-27), Sections 9–11; High School Options Committee minutes, January 10, 2023
   - source: https://drive.google.com/file/d/1d8wVyA1kBtoqLZ16nlfdpPyL2ilzcEVP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Conway text: "The Conway School Board will meet jointly with all School Boards (all together) who send pupils to the high school ... at least three (3) times a year." Moultonborough text: "the Tamworth School District shall annually appoint one of its members to be a non-voting representative to the Moultonborough School Board"; "Tamworth citizens shall be entitled to attend Moultonborough School Board meetings and address the School Board in the same manner ... as to issues pertaining to the high school." Committee: "A long running complaint about our KHS experience ... has been that we have no representation in governance there." Transcribed from image. Raw: raw/money/contracts/contract-9-12-tamworth-conway.ocr.txt; raw/money/packets/tsb-packet-2026-02-26-p45-50-ma-agreement.ocr.txt; raw/money/hs-options/hsoc-minutes-2023-01-10.*
10. In September 2026 the Tamworth board set its yearly goals, with community communication and student behavior and belonging each receiving all five members' votes, staff climate and culture four, and math one; ideas under communication included publicizing school events and a "Better Together" district brand.
   - citation: Tamworth School Board working meeting minutes, September 1, 2026; minutes September 17, 2026
   - source: https://drive.google.com/file/d/1e0G6pHzdspPy8ayFhvRsWhFWLOf-QMQo/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "● Math academic goal, proficiency and enjoyment (1 vote) ● Community volunteers ● Community communication (5 votes) ● Behavior, student belonging (5 votes) ● Climate and culture for staff (4 votes)"; "Branding for district – 'Better Together' ● Publicizing things happening in the school." September 17 lists four goals including "math skills and enjoyment." Raw: raw/money/minutes/tsb-tamworth-september-1-2026-public-approved-minutes.*, tsb-tamworth-september-17-2026-public-approved-minutes.*
11. No survey of Tamworth parents' or residents' ratings of school communication or board transparency was found; in mid-2026 the board planned listening sessions and community, parent and staff surveys as part of strategic planning, and in September 2026 its minutes say "Strategic plan is on hold."
   - citation: Tamworth School Board minutes, June 18, 2026 (Strategic planning update); July 23, 2026; September 17, 2026
   - source: https://drive.google.com/file/d/19Gsr_2sNor5icgbRcrT5NZsTUYk8lb_X/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: June text: "Siena and Shauna discussed having listening sessions and a survey over the summer. One for the community, one for parents, and one for staff." July: "The proposal is some listening sessions and a survey that ideally will shine light on both the positive and negative areas, perceived or real, within the school." September: "Old business: Strategic plan is on hold." Public data can't rate how parents feel about communication. Raw: raw/money/minutes/tsb-tamworth-june-18-2026-approved-minutes.*, tsb-tamworth-july-23-2026-public-approved-minutes.*, tsb-tamworth-september-17-2026-public-approved-minutes.*
12. Tamworth's SAU leadership changed three times in 2026: the superintendent who had served since at least 2022 left for Moultonborough on July 1, 2026, his successor started in July and resigned in September for personal reasons, and an interim superintendent attended the October 13 meeting.
   - citation: Tamworth School Board minutes, February 26, 2026 (Announcements); July 23, 2026; September 17, 2026; October 13, 2026 draft
   - source: https://drive.google.com/file/d/1ZZglHlOCawKaOOexz3vEcn_S_R9dTgUJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Texts: "Superintendent Michael Whaland has accepted a position as Superintendent with the Moultonborough School District beginning July 1, 2026" (February); "Superintendent Dr. Kathleen Scholand" (July); "She saw in the Conway Daily Sun that the superintendent is resigning. Is it a personal reason ... The superintendent responded 'personal'" (September); "Interim Superintendent Dr. Ronna HasBrouck" (October). The SAU superintendent search itself: SAU 13 fact: see Madison research. Raw: raw/money/minutes/tsb-tamworth-february-26-2026-amended-approved-minutes.*, tsb-tamworth-july-23-2026-public-approved-minutes.*, tsb-tamworth-september-17-2026-public-approved-minutes.*, tsb-tamworth-october-13-2026-public-draft-minutes.*

## district-consolidation-history: Middle School Sharing and Restructuring Ideas in Tamworth

- kind: local
- question_type: governance_money
- description: Studies, votes and discussions about cooperative districts, consolidation or sharing schools

1. In June 2025 the superintendent told the Tamworth board that SAU 13 was discussing middle school options for Madison and Freedom (whose grades 7–8 attend Kennett Middle School) and asked whether Tamworth wanted to explore offering middle school to them for 2027; the board agreed to have him look into it further.
   - citation: Tamworth School Board minutes, June 19, 2025 (Middle School Receiving Tuition)
   - source: https://drive.google.com/file/d/16jaEpkYx5Bf_-mWEQgjTH3ts6o-xXlZ5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "conversations are currently taking place within the SAU regarding the middle school options for Madison and Freedom, and asked whether the board has any interest in exploring the possibility of providing middle school to Madison and Freedom as an option for the 2027 school year. A conversation was held, and it was agreed to have the superintendent look into this more thoroughly and report in the future." Madison and Freedom's middle schoolers at Kennett Middle: Conway file district-tuition-contracts fact 7. Raw: raw/money/minutes/tsb-tamworth-june-19-2025-approved-minutes.*
2. In August 2025 the business administrator presented a "pro forma" tuition calculation for taking Madison and Freedom middle schoolers at Brett: after removing tuition, special education, transportation and other costs, Brett's cost was $29,702.17 per student, and she recommended charging $14,851.08 (half) for each additional student, limited to five.
   - citation: Tamworth School Board minutes, August 21, 2025 (Business Administrator's Report C); August 21, 2025 packet, p. 25
   - source: https://drive.google.com/file/d/1W4iPryvUN7uRu3pTTKzdCVdcExqAsWVv/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Minutes: "Heather Sherwood gave information about the costs and financial benefits if Madison and Freedom sent their students to Brett School for middle school instead of to Kennett Middle School." Packet: "Tuition Rate Recommendation for each additional student (limited to 5 additional students): 14,851.08." A resident asked "How will bringing Madison and Freedom middle schoolers to Brett affect the 6-8 grade model?" No board vote on the idea was found. Raw: raw/money/minutes/tsb-tamworth-august-21-2025-approved-minutes.*; raw/money/packets/tsb-packet-2025-08-21-p25-29.*
3. In August 2026 the board set a tuition rate of $17,216.30 for up to five students coming to Brett from outside Tamworth (for example on manifest hardship), again half of the per-student cost left after fixed costs; the business administrator said "we haven't had any student tuition here in the past few years."
   - citation: Tamworth School Board minutes, August 20, 2026 (New Business F; Public Comment)
   - source: https://drive.google.com/file/d/11m35F1QZ5am2vHTLf84WXHuUIbVeJW6-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Text: "VOTE: Shauna Peterson motioned to approve the tuition rate of $17,216.30 for up to five students, Melanie streeter seconded. Motion approved unanimously by roll call vote"; "Is this related to open enrollment? Not exactly, it's more about manifest hardship." The 2026 warrant's Article 9 proposed open enrollment for 5 incoming students and 0% outgoing (library topic open-enrollment-status). Raw: raw/money/minutes/tsb-tamworth-august-20-2026-public-approved-minutes.*; raw/money/finance/tsd-2026-warrant.*
4. Tamworth's 2022–23 High School Options Committee considered whether to move its middle schoolers too, but ruled it outside its scope, and reported that Moultonborough, the only option with a middle school, was "not interested in taking our middle schoolers at this time."
   - citation: High School Options Committee FAQ; Final Report, July 20, 2023, p. 2
   - source: https://drive.google.com/file/d/1bCFhZP6Ir30K8WysuCQpUbwYCn-VPz6F/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: FAQ: "Is a new middle school option for Tamworth students a possibility? The committee has discussed this question but it's outside the scope of their mission and would require a different process. The only school we're considering that includes a middle school is Moultonborough, and they are not interested in taking our middle schoolers at this time." October 2022 minutes: "Several people raise a big question regarding middle school – should we move our middle schoolers or keep them at KAB? ... how will changing middle schools likely change the school budget." Raw: raw/money/hs-options/hsoc-faq.*, hsoc-minutes-2022-10-18.*
5. The committee's records also note "tangent discussions of Cooperative and JMA structures with Conway" in 2022 and say a separate effort with other Kennett sending towns to gain representation was "not looking like any of the options are going to work out."
   - citation: High School Options Committee minutes, October 18, 2022; FAQ
   - source: https://drive.google.com/file/d/1E8BCfkW3GeJ0bXbNpEthP31WAGYI3RhC/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Minutes: "Timeline draft overview and discussion… tangent discussions of Cooperative and JMA structures with Conway." FAQ: "Through a separate process, Tamworth has been working with other sending schools to Kennett to explore options for representation. Unfortunately, it's not looking like any of the options are going to work out at this point." The 2019 SAU 9 study is in the Jackson file (district-consolidation-history in `Jackson/money-and-governance.md`). Library topics gov-cooperative-district and gov-area-agreements. Raw: raw/money/hs-options/hsoc-minutes-2022-10-18.txt, hsoc-faq.txt
6. With enrollment falling, residents at the September 17, 2026 meeting urged a "restructuring committee," suggested "dividing students into different SAU #13 schools," asked whether Brett could become a charter school if it left SAU 13, and advised against joining SAU 9; in October a board member asked about combining classes.
   - citation: Tamworth School Board minutes, September 17, 2026 (Public Comment); October 13, 2026 draft (Business Administrator's Report B)
   - source: https://drive.google.com/file/d/19Gsr_2sNor5icgbRcrT5NZsTUYk8lb_X/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Texts: "She urged for a restructuring committee to look at options"; "With enrollment down, can the Brett school become a Charter School if it resigns from SAU 13? She advised to not join SAU#9"; "She thinks we should look at some options such as dividing students into different SAU #13 schools" (September); "Melanie Streeter asked about combining classes. o BA Sherwood stated that she will discuss with Principal Schinaman and Interim Superintendent HasBrouck in November/December" (October). Statements as recorded. Library topic gov-sau-forming-and-withdrawing. Raw: raw/money/minutes/tsb-tamworth-september-17-2026-public-approved-minutes.*, tsb-tamworth-october-13-2026-public-draft-minutes.*
7. The Tamworth board's November 17, 2026 agenda lists a "Middle School Discussion" under new business; no documents for it were in the packet.
   - citation: Tamworth School Board Regular Meeting Agenda, November 17, 2026 (New Business B)
   - source: https://drive.google.com/file/d/1LjBjD-dLSbgSPdRK736L2I9dQgBZT9f-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: Agenda text: "New Business ... B. Middle School Discussion / C. Review Field Trip Policy IJOA." The meeting is after this research date. Raw: raw/money/packets/tsb-packet-2026-11-17-p1-2-10-37-38-48-52.*
8. No study, committee report, cost estimate or vote on consolidating grades 6–8 across Tamworth, Madison and Freedom was found in Tamworth's minutes and packets from July 2023 through November 2026, so whether it would save money can't be answered from public records.
   - citation: Tamworth School Board minutes and packets, July 2023 – November 2026 (searched)
   - source: https://www.sau13.org/school-board/tamworth/agendas-packets-minutes
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Tamworth
   - note: A statement about the documents searched (terms: middle school, consolidat, cooperative, restructur, regional, grades 6-8). The only cost figures found are the per-student tuition calculations in facts 2–3, which price a few extra students at Brett, not a merger. SAU-wide discussions: SAU 13 fact: see Madison research. Raw: raw/money/web/sau13-tamworth-drive-folder-listings.txt

## tamworth_official_enrollment: Tamworth Students on October 1 (Brett K–8 and High School)

- unit: count
- period: October 1 counts, 2016–2025; year: school year ending (2026 = October 1, 2025)
- source: Annual Report of the Tamworth School District, FY2025, "Report of Official Enrollment as of October 1st," p. 65 — https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
- as_of: 2026-11-13
- raw: raw/money/finance/tsd-annual-report-fy2025-excerpt.pdf, .ocr.txt
- note: K–8 is the Kenneth A. Brett School; 9–12 counts Tamworth resident students in high school (mostly Kennett). Transcribed from image. The site database has Brett enrollment by grade from NH DOE; these are the district's own October 1 counts. The board reported 126 at Brett on September 17, 2026.

| Place | Year | K–8 (Brett) | Grades 9–12 | Note |
|---|---|---|---|---|
| Tamworth (525) | 2017 | 204 | 86 | October 1, 2016 |
| Tamworth (525) | 2018 | 194 | 94 | |
| Tamworth (525) | 2019 | 186 | 98 | |
| Tamworth (525) | 2020 | 197 | 90 | |
| Tamworth (525) | 2021 | 173 | 100 | |
| Tamworth (525) | 2022 | 192 | 87 | |
| Tamworth (525) | 2023 | 183 | 91 | |
| Tamworth (525) | 2024 | 185 | 95 | |
| Tamworth (525) | 2025 | 165 | 81 | |
| Tamworth (525) | 2026 | 154 | 68 | October 1, 2025 |

## tamworth_article1_budget: Tamworth School District Operating Budget (Article 1) and SAU Share

- unit: dollars
- period: Fiscal years 2023-24 to 2026-27; year: fiscal year ending
- source: Annual meeting minutes (2023, 2025), 2024 and 2026 warrants, Annual Reports FY2023 and FY2025 — https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
- as_of: 2026-11-13
- raw: raw/money/finance/tsd-annual-report-fy2023-excerpt.*, tsd-annual-report-fy2025-excerpt.*, tsd-2026-warrant.*
- note: Article 1 excludes the SAU share, contract cost items and special articles. 2024-25 and 2026-27 are the amounts on the warrant; the meeting results for 2024 and 2026 were not found. Transcribed from image.

| Place | Year | Value | SAU share (Article 2) | Note |
|---|---|---|---|---|
| Tamworth (525) | 2024 | 7759754 | 417853 | Passed by voice vote, March 8, 2023 |
| Tamworth (525) | 2025 | 8583796 | 506240 | 2024 warrant (board 4-1-0) |
| Tamworth (525) | 2026 | 8768795 | 485186 | Passed by voice vote after a $750,000 cut failed 29–73, March 5, 2025 |
| Tamworth (525) | 2027 | 9125578 | 540350 | 2026 warrant (board 3-0-0) |

## tamworth_hs_tuition_lines: Tamworth's High School Tuition Budget Lines

- unit: dollars
- period: FY2024–FY2028 (actual spending, budgets and working budget); year: fiscal year ending
- source: Tamworth 2026-2027 Working Budget v4 (January 2026); public hearing packet February 4, 2026, p. 6; November 17, 2026 packet, p. 50 — https://drive.google.com/file/d/1ssRzxX50mTnCQlKnTBD9l_HHAUU5pf0i/view
- as_of: 2026-11-13
- raw: raw/money/packets/tsd-2026-2027-working-budget-v4.*, tsb-hearing-packet-2026-02-04-p6.*, tsb-packet-2026-11-17-p1-2-10-37-38-48-52.*
- note: Account 01.1100.561.103 (KHS TUITION) and 01.1100.561.104 (MA TUITION). FY2028 is a working draft (v2) using 70 Kennett and 10 Moultonborough students at $27,900; no 2027-28 contract exists. Moultonborough Academy attendance began in 2024-25.

| Place | Year | Kennett (KHS) | Moultonborough Academy | Status |
|---|---|---|---|---|
| Tamworth (525) | 2024 | 1244623 | 0 | Spent |
| Tamworth (525) | 2025 | 1414340 | 33109 | Spent |
| Tamworth (525) | 2026 | 1543997 | 153293 | Budget |
| Tamworth (525) | 2027 | 1549098 | 283844 | Budget |
| Tamworth (525) | 2028 | 1953000 | 279000 | Working budget v2, November 2026 |

## tamworth_kennett_charge: Conway's Kennett Charge to Tamworth

- unit: dollars
- period: 2024-25 and 2026-27 tuition contract tables; year: fiscal year ending
- source: Annual Report FY2023 ("2024-2025 Tuition Contracts") and Annual Report FY2025 ("2026-2027 Tuition Contracts," p. 32) — https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
- as_of: 2026-11-13
- raw: raw/money/finance/ar2024r-p33-bot.png, ar2025r-p32-top.png, ar2025r-p32-bottom.png
- note: Read from rendered page images. Per-student figures are **derived** (total ÷ ADMA). Bond payments were $0 in both years. Shares are of the eight towns' totals under the 2003 formula (65% ADMA, 35% equalized value).

| Place | Year | ADMA | % ADMA | % equalized value | Operations | Maintenance trust | Total | Per ADMA (derived) |
|---|---|---|---|---|---|---|---|---|
| Tamworth (525) | 2025 | 85.09 | 12.54 | 7.51 | 1410252 | 4089 | 1414341 | 16622 |
| Tamworth (525) | 2027 | 76.61 | 12.31 | 6.97 | 1545301 | 3797 | 1549098 | 20221 |

## tamworth_sau13_share: Tamworth's Share of the SAU 13 Budget

- unit: dollars
- period: 2019-20 to 2026-27; year: fiscal year ending
- source: Annual Report FY2025, "Apportionment History" and "Apportionment for Fiscal Year 2026-2027," p. 31 — https://drive.google.com/file/d/1H-TGQ9K1KEMk5l75o4-AYHbDfx8KdsZZ/view
- as_of: 2026-11-13
- raw: raw/money/finance/ar2025-p31.png, tsd-annual-report-fy2025-excerpt.ocr.txt
- note: Percent apportioned = average of Tamworth's share of equalized value and of ADM. Transcribed from image.

| Place | Year | Value | % apportioned | ADM | Note |
|---|---|---|---|---|---|
| Tamworth (525) | 2020 | 252935 | 37.89 | 196.60 | |
| Tamworth (525) | 2021 | 259479 | 37.44 | 182.25 | |
| Tamworth (525) | 2022 | 282982 | 39.83 | 199.16 | |
| Tamworth (525) | 2023 | 394052 | 38.02 | 178.65 | |
| Tamworth (525) | 2024 | 417853 | 39.78 | 195.44 | |
| Tamworth (525) | 2025 | 506240 | 38.44 | 189.45 | |
| Tamworth (525) | 2026 | 485186 | 38.19 | 175.73 | |
| Tamworth (525) | 2027 | 540350 | 37.07 | 165.15 | Default budget share would be $507,600 |

## tamworth_tax_per_1000_by_line: Selected School Budget Lines per $1,000 of Tamworth Assessed Value

- unit: dollars per $1,000 of assessed value
- period: 2025-26 budget (tax year 2025) and 2026-27 proposed; year: fiscal year ending
- source: Tamworth budget lines (August 21, 2025 packet p. 25; February 4, 2026 hearing packet p. 6; 2025 and 2026 warrants); DRA 2025 assessed value with utilities $735,906,312 — https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2025-municipal-and-village-district-tax-rates.xlsx
- as_of: 2026-11-13
- raw: raw/money/packets/tsb-packet-2025-08-21-p25-29.*, tsb-hearing-packet-2026-02-04-p6.*; raw/money/state-data/dra-tax-rates-tamworth.csv
- note: All values **derived**: budget line ÷ ($735,906,312 ÷ 1,000), the district's own method on its tax-impact sheet. Illustrative "if paid wholly from local tax"; the actual school rate is the whole budget less aid and other revenue. For scale, the 2025 local school rate is $9.59 and the total rate $14.78 (DRA); both are in the site's data (property_tax, Tamworth district). The $735,906,312 matches DRA's and NH DOE's 2025 assessed valuation with utilities in the site's data (checked November 15, 2026).

| Place | Year | Line | Budget | Value |
|---|---|---|---|---|
| Tamworth (525) | 2026 | Kennett tuition | 1543997 | 2.10 |
| Tamworth (525) | 2026 | Moultonborough Academy tuition | 153293 | 0.21 |
| Tamworth (525) | 2026 | SAU 13 share | 485186 | 0.66 |
| Tamworth (525) | 2027 | Kennett tuition | 1549098 | 2.11 |
| Tamworth (525) | 2027 | Moultonborough Academy tuition | 283844 | 0.39 |
| Tamworth (525) | 2027 | SAU 13 share | 540350 | 0.73 |

## tamworth_para_pay_neighbors: Posted Paraprofessional Pay, Tamworth and Neighbors

- unit: dollars per hour
- period: Postings open November 13, 2026; Conway CESP schedule 2025-26 and 2026-27; year: 2027
- source: SAU 13 posting JobID 349 — https://www.applitrack.com/sau13/onlineapp/default.aspx?AppliTrackPostingSearch=location:%22Kenneth+A+Brett+School%22 ; SAU 45 Job Openings — https://docs.google.com/document/d/1v7YUgs9715KvzXA78yIf284SInETz7KsTH0sSe1q2IM/edit ; Conway CESP 2025–2028 (Conway file table conway_para_and_regional_wages)
- as_of: 2026-11-13
- raw: raw/money/wages/sau13-applitrack-brett-postings-2026-11-13.*, sau45-job-openings-2026-11-13.txt, gwrsd-applitrack-postings-2026-11-13.*; town/Conway/raw/money/contracts/cesp-2025-2028.ocr.txt
- note: Postings are hiring ranges, not full schedules, and are not strictly comparable (fact 18). Governor Wentworth Regional's postings give no rate. Comparisons are **derived**.

| Place | Year | Low | High | Note |
|---|---|---|---|---|
| Tamworth (525) | 2027 | 21.84 | 24.19 | Special education paraprofessional, 6.5 hours, 178 days; 94.9%/92.2% health |
| Moultonborough (369) | 2027 | 18.00 | 28.14 | 2026-27 special education paraeducator openings; plus differentials |
| Conway (113) | 2026 | 19.92 | 26.40 | CESP 2025-26, levels 0–1 to 15+ years, no degree |
| Conway (113) | 2027 | 20.52 | | CESP 2026-27 levels 0–1 (Conway file) |
| Governor Wentworth Regional (208) | 2027 | | | Not posted |

## tamworth_srsa_awards: Federal Small, Rural School Achievement Awards to Tamworth

- unit: dollars
- period: Award start dates July 1, 2019 – July 1, 2023; year: award year (start date)
- source: USAspending.gov award search, CFDA 84.358 — https://api.usaspending.gov/api/v2/search/spending_by_award/
- as_of: 2026-11-13
- raw: raw/money/state-data/usaspending-tamworth-awards.json, usaspending-query.txt
- note: No award with a later start date was returned for the Tamworth School District (search through September 30, 2026).

| Place | Year | Value | Award ID |
|---|---|---|---|
| Tamworth (525) | 2019 | 15258 | S358A193218 |
| Tamworth (525) | 2020 | 6849 | S358A202466 |
| Tamworth (525) | 2021 | 10412 | S358A212819 |
| Tamworth (525) | 2022 | 868 | S358A222676 |
| Tamworth (525) | 2023 | 7731 | S358A232548 |

## For another file

- **Brett School agent (brett-school.md):**
  - 41 of 139 Brett students had special education plans in June 2026; 32 at Brett, 9 at Kennett, 3 at Moultonborough Academy, 5 at charters and 2 out of district in August 2026; a contracted BCBA from New Era and an RBT-trained para for the Student Support Center (minutes June 18 and August 20, 2026; raw/money/minutes/).
  - The math coach was eliminated in January 2026 (3–2); Envision Math replaced Math in Focus in fall 2026; the LETRS "Bridging the Gap 603" literacy grant ($10,000 a year for two years). Sources: minutes January 15, July 23 and August 20, 2026; December 18, 2025.
  - The ski team was dropped for 2025-26 for lack of a coach and is being restarted in 2026-27 (minutes December 18, 2025; October 13, 2026 draft).
- **Daily agent (getting-to-school-and-the-day.md):** Brett's buses are contracted with First Student (up 12% in 2025-26 due to collective bargaining); the Moultonborough bus costs about $90,000 and carries about three students; residents asked for better Kennett bus options like Bartlett's and Eaton's (minutes January 15, 2026). Raw: raw/money/minutes/.
- **High school agent (high-school.md):** The High School Options Committee's 2023 comparison (Kennett 713 students, Fryeburg 620, Moultonborough 144; distances 18.5, 22.8 and 12.5 miles; AP counts; post-graduation plans) is in raw/money/hs-options/hsoc-final-report-2023-07-20.* and the comparison spreadsheet (https://drive.google.com/file/d/1KdeBHOm7degTLzQIJdXt5R3InSRiopNF/view).
- **Community agent:** 14 homeschooled students and 2 at Northeast Woodland Charter on October 1, 2025 (annual report p. 65); 17–19 Tamworth students expected at Breakthrough Academy charter school (minutes February 26 and April 16, 2026).
- **Madison research (SAU 13):** The SAU 13 joint board's 2026-27 apportionment (Freedom $390,071, Madison $527,065, Tamworth $540,350 of $1,457,486) and the superintendent turnover in 2026 (raw/money/finance/ar2025-p31.png; minutes cited in district-board-and-public-input fact 12).
- **Conway file (town/Conway/money-and-governance.md), district-tuition-contracts fact 8:** Tamworth's own minutes confirm no 2027 contract as of November 2026 and add that Tamworth voted on February 15, 2024 to give notice ending its contract in 2027, that Tamworth's attorney advised against a warrant vote on a Kennett option (December 2025), and that the 2026-27 Kennett charge to Tamworth is $1,549,098 for 76.61 students.
- **Conway file, fact 4 (65/35 formula reading):** for Tamworth alone the property weighting lowers its share: 10.44% of the 2026-27 operating base against 12.31% of attendance (raw/money/finance/ar2025r-p32-bottom.png).
- **additional-data/district-practices.md, fact 78 (Tamworth):** the "up to 6" Moultonborough figure is out of date: the 2026-27 agreement allows up to 10 per grade (40 in all), and the board funded 7 students for 2026-27. The 2026 annual meeting date was March 4, 2026 and the 2027 meeting is set for March 3, 2027 (fact 134 says the 2026 date was not found).

## Not retrieved

- https://www.nh.gov/pelrb/collective/index.htm: the state labor board's library of collective bargaining agreements (which may hold Tamworth's TESPA and Governor Wentworth support staff contracts) returned HTTP 403 to curl and to the fetch tool.
- Governor Wentworth Regional employee resources (https://sites.google.com/sau49nh.gov/employeeresourcehub/home): requires a Google sign-in; postings at https://www.applitrack.com/govwentworth/onlineapp/ give no pay rates.
- Tamworth TESPA (support staff) wage schedule: not posted on the SAU 13 site, the Brett site or in any 2023–2026 board packet searched; only one page of a support staff agreement (April 18, 2024 packet, p. 36) appears.
- Results of the March 4, 2026 annual district meeting (Articles 1–11, including SB2): the FY2026 annual report is not yet posted; Tamworth minutes after March 4 do not list results; a news search found nothing.
- The October 7, 2026 "School Tuition Presentation," the November 17, 2026 "Community Letter" and "Information Night," and the Governor Wentworth tuition contract that SAU 13 presented in early November 2026: not posted in Tamworth's or the SAU joint board's folders as of November 13, 2026.
- The written Moultonborough lottery procedure and application form approved March 21, 2024: not in the posted packets.
- The letter Tamworth sent Conway after the February 15, 2024 vote: not posted.
- ED's REAP FY2025 master eligibility spreadsheet (https://data.ed.gov/dataset/reap-fy-2025-master-eligibility-spreadsheet/resources): the page is a script-only app; catalog.data.gov's API returned "Not Found"; ed.gov's SRSA page returned 403. Awards were taken from USAspending instead.
- The 2025-26 tuition contract table (Tamworth's 2025-26 Kennett ADMA): it would be in the FY2024 annual report, which is not posted on the SAU 13 site (the site lists FY2023 and FY2025 reports).
- Tamworth's June 2026 draft capital improvement plan and the October 2026 seven-year plan form: discussed in minutes but not included in posted packets.
