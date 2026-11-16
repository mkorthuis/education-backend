# Hart's Location School District: Money, Contracts and Governance

Part of the Hart's Location research (town/Hart's Location). Gathered November 13, 2026.

## Summary

**What's covered:** 15 topics, 92 facts and 4 number tables on the money and governance of the Hart's Location School District, which runs no schools.
- The K–8 contract with Bartlett, read page by page from the scanned PDF (transcribed from image): what it assigns, how payments are counted, how it renews and ends, and what it leaves out. Points to the Bartlett file for the tuition formula.
- High school arrangements: the 2016 switch of the "school of record" from Fryeburg Academy to Kennett, a Kennett student in 2017–2022, and Fryeburg in 2026-27.
- The district's budget line by line (FY2019–FY2027), what happened when students moved in (2018–2024), the two trust funds and the special education costs.
- Why the local school tax rate swings, the 2025 revaluation, the statewide education tax Hart's Location keeps, and a **derived** estimate of the tax effect of new pupils. NH DOE's adequacy aid calculation for Hart's Location, FY2020–FY2027, and its NH DRA tax rates (tax years 2014–2025) and NH DOE school taxes (2011–2025) are in the site's data (adequacy_aid, property_tax), so this file does not repeat them.
- Federal land money: PILT goes to the town; national forest receipts go to the school district by state law.
- The SAU 9 share, paid on property value alone; Hart's Location's vote on the SAU 9 board; where to see the SAU budget line by line.
- The board: where and when it meets, notices, write-in elections, vacancies, the non-resident treasurer, the 2027 calendar.
- Residency, custody, special education responsibility, catastrophic aid, special meetings and tax relief, as general NH rules.

**Main sources:** Hart's Location School District annual reports for 2017–2026 (scanned; budget pages rendered and read), warrants, annual meeting minutes for 2016–2026 and board minutes for 2009–2010 and 2024–2026, the November 18, 2026 agenda packet, Hart's Location policies JECA and DK, Bartlett policies JFAA and JFAB, the Town of Hart's Location 2025 annual report (MS-636, DRA tax rate breakdown and trustees' report), the US Department of the Interior's PILT tables (FY2022–FY2026) and FAQ, SAU 9's tuition and board pages, RSA 32, 72, 91-A, 186-C, 189, 193, 194, 194-C, 197, 198, 227-H and 671, Ed 1100, the Rand opinion (2025 N.H. 27), the library's DRA and DOE town CSVs, and read-only queries of the site database.

**Premises checked:**
- "Meets at 8:00 AM in Bartlett": correct. The board has met at JBES in the morning since at least 2009. In April 2026 it moved from every other Tuesday to quarterly Wednesdays at 8 a.m. SAU 9's page still says the second Tuesday.
- "Three seats" on the board: correct (3 members, the default under RSA 671:4).
- "High schoolers go to Kennett" and "locked into Kennett": not the current arrangement. Hart's Location has no high school contract. It chose Kennett as its "school of record" in 2016, but its 2026-27 budget pays $21,650 of high school tuition and mileage for one student at Fryeburg Academy.
- "A 2027–28 renegotiation cycle for Hart's Location's contracts": not found. The K–8 contract renews itself each year, and SAU 9 lists no 2027 contract for Hart's Location. The 2027 contracts are Conway's with Albany, Bartlett, Eaton and Jackson, plus Jackson–Fryeburg.
- "Federal PILT offsets the school budget": PILT ($14,886 in FY2025) is paid to the town and counted as town revenue. The school district gets a different federal payment, national forest receipts ($5,579.72 in FY2025).
- "SAU #9 Joint Board weighted votes": as a district with no schools, Hart's Location has one vote under RSA 194-C:7. Weighted votes are used only on demand, and Hart's Location would have none (**derived**: 1 resident pupil, fewer than 8).
- "Donor-town rules": the donor-town system ended in 2011. Hart's Location keeps its excess statewide education tax.
- "Multi-year tuition rates": the contract sets no multi-year rate. It recalculates tuition each year by formula, with no cap.
- "Under 50 voters" and "90%+ federal and state land": left to the community file. The 2026 school district meeting minutes list 11 attendees besides officials and SAU staff. Hart's Location has 5,395 PILT acres, all Forest Service.

**Proposed new shared topics:**
- `school-residency-rules` (rule, rules): "Who counts as a resident for school attendance in New Hampshire: domicile, separated and divorced parents, parenting plans, homelessness and who decides disputes."
- `federal-land-payments` (how_it_works, governance_money): "Federal payments for tax-exempt federal land (PILT) and national forest receipts: who receives them and whether they reach schools."
- `property-tax-relief` (rule, rules): "Local elderly exemptions and the state's low and moderate income homeowners property tax relief."

This file also adds facts to four library topics: `budget-traditional-district-meeting`, `money-special-education-aid`, `gov-school-boards-and-superintendents` and `money-statewide-education-property-tax`.

**Main gaps:**
- Bartlett's yearly per-pupil calculation "rider" is not posted.
- SAU 9's "Annual Residency Verification Attestation" link returns "not found."
- Whether the Town of Hart's Location has adopted an elderly exemption was not found. The town report shows only war service credits.
- No 2026 tax rate is set yet.
- No document gives the reason for the board's 8 a.m. JBES meetings.
- No record of any Bethlehem or Profile tuition discussion was found.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.1 How the K–8 contract works | district-tuition-contracts 1–7; Bartlett file district-tuition-contracts 12–14 (formula, rental fee, joint meetings); table harts_location_school_budget | full | Assigned school K–8. Hart's Location pays transportation and extra special education. Year-to-year renewal; ending it takes notice of at least three full school years. No cap. The yearly rider is not posted |
| P1.3 Pre-K or kindergarten readiness paid by the district | district-budget-and-cost 10; Bartlett file jbes.md district-preschool 1–7; library: early-supports-to-preschool-special-ed; money-special-education-aid 1 (this file) | partial | No preschool line in any budget from FY2017 to FY2027; the contract starts at K. Nothing found on Hart's Location children in the JBES preschool. Preschool special education is the resident district's cost (RSA 186-C:13) |
| P2.1 Tax effect of two new school-age families | district-tax-and-state-aid 2, 4–6; district-budget-and-cost 4–7; site data: property_tax (Hart's Location district) | full | **Derived**: about $0.92 per $1,000 per K–8 pupil, at the 2025-26 tuition budget and the 2025 valuation. The tuition trust (about $79,500) covers about 2 pupils for a year. No adequacy grant until about 6 resident pupils |
| P2.2 Why the board meets at 8 a.m. at JBES; budget hearing notice | district-board-and-public-input 1–5; library: budget-traditional-district-meeting 2–3 (RSA 32:5, RSA 197:7) | partial | Morning JBES meetings go back to at least 2009. **No reason is recorded.** Hearings are at the Town Hall. 2026 had 28 days between hearing and meeting (**derived**). Where Hart's Location posts paper notices was not found |
| P2.3 SAU share in years with no students | district-sau-governance 1–3; table harts_location_school_budget; library: budget-sau-budget-vote 1 | full | The share is set on property value alone. Hart's Location paid it in 2016-17, when it had no K–8 students, and budgets $4,521 for 2026-27 with no K–8 student |
| P3.1 Residency documents in seasonal or employer housing | district-student-support 1–3; school-residency-rules 1, 4; library: military-children-compact (RSA 193:12 VI) | partial | Domicile is the test; no rule turns on who owns the housing. Bartlett asks for "proof of residency satisfactory to the Superintendent." Hart's Location's own residency policy is not posted, and SAU 9's attestation link is broken |
| P4.1 SWEPT with few students | district-tax-and-state-aid 8; money-statewide-education-property-tax 1; site data: adequacy_aid (Hart's Location district: SWEPT, cost and SWEPT above the cost); library: money-statewide-education-property-tax, money-adequacy-grant-calculation, money-rand-case, money-rand-appeal-2026 | full | Hart's Location keeps all the SWEPT it raises. Its FY2027 SWEPT above its adequacy cost ($20,738) is in the site's data |
| P4.2 Voice on Bartlett curriculum and Kennett bonds | district-board-and-public-input 11; Bartlett file district-board-and-public-input 8–10 and district-tuition-contracts 14; district-sau-governance 3 | full | Hart's Location residents don't vote on Bartlett's or Conway's budgets. It pays no Kennett maintenance share, having no Kennett contract. From 2027, SAU budget votes are pooled across all districts |
| P4.3 Per-pupil tuition, Hart's Location vs other SAU 9 towns | table harts_location_tuition_per_pupil_comparison; district-tuition-contracts 7 | partial | **Derived**. Bartlett's yearly rider rates are not posted, so the table uses budget totals ÷ students |
| P6.3 EFAs and a non-operating district | district-budget-and-cost 12; library: money-efa-funding-link, efa-eligibility-and-cap; site data: EFA counts | partial | EFAs are paid from the state's education trust fund. No EFA line in the district budget. The site's data shows no Hart's Location EFA students in 2022–2027 |
| P7.2 Special education contingencies and reserve | district-budget-and-cost 8–9, 13; table harts_location_trust_funds; Bartlett file district-tuition-contracts 15 | full | FY2027: $1,800 of special education lines plus $8,000 to the reserve, 20.1% of $48,650 (**derived**). Reserve $81,143.09 at December 31, 2025 |
| P9.1 Why contracts are renegotiated; 2027-28 changes | district-tuition-contracts 3–6; Jackson and Conway files (Kennett contracts) | full | Hart's Location's contract doesn't change in 2027-28. The Kennett renegotiations covered Conway's sending towns |
| P9.3 Filling seats; conflicts of interest | district-board-and-public-input 6–9; gov-school-boards-and-superintendents 1–2 | partial | Write-in elections, a seat vacant in 2022–2023, a meeting without a quorum. Incompatible offices under RSA 671:18. Hart's Location's posted policies have no Section B (board) policies |
| P10.1 SAU 9 board weighting; superintendent contracts | district-sau-governance 4–5; Jackson file jackson_sau9_board_seats_and_votes; library: gov-sau 4 | full | 3 members, 1 statutory vote, 0 weighted votes (**derived**). The SAU board sets salaries and can remove superintendents |
| P10.2 Unfilled seat after the March meeting | gov-school-boards-and-superintendents 3–4; district-board-and-public-input 6–7 | full | The board appoints until the next election; the selectmen step in if it can't agree |
| P10.3 Where to inspect the SAU apportionment line by line | district-sau-governance 7–8; Jackson file district-budget-and-cost 31–34; district-tuition-contracts 33; district-sau-governance 14 in `Jackson/money-and-governance.md` | full | Hart's Location's annual reports (by function, 2020–2023; apportionment table, 2024–2026); budget status reports in board packets |
| P11.1 Tuitioning north to Bethlehem/Profile | district-tuition-contracts 8–9; library: gov-tuition-towns 3, change-of-school-assignment | partial | No history found. The law allows contracts. Leaving Bartlett for K–8 takes three full school years' notice. Ride times are not computed here |
| P12.1 Elderly exemptions and relief | property-tax-relief 1–3; district-tax-and-state-aid 9; site data: property_tax (Hart's Location district) | partial | Whether the town adopted the exemption was not found. State relief covers only the SWEPT part; its most follows from property-tax-relief fact 3 and the equalization ratio and state rate in the site's data |
| P12.2 Mid-year costly special education: special meeting? | district-budget-and-cost 4–5, 7, 9, 14; budget-traditional-district-meeting 1–4; money-special-education-aid 1–3 | full | Trust funds, an emergency expenditure request, the special education aid exemption, or a special meeting. Hart's Location's 2020-21 experience |
| P12.3 Municipal vs school shares of the tax bill | site data: property_tax (Hart's Location district) | data only | DRA's rates by part and the school share, 2014–2025 (2025: school 46.2%) |
| P13.1 Legal and financial responsibility for an IEP | district-special-education-services 1–3; money-special-education-aid 1 | full | Hart's Location, as district of residence, under RSA 186-C:13 |
| P13.2 Specialized transportation costs | district-special-education-services 4–5; district-budget-and-cost 3 | partial | Hart's Location pays transportation under the contract. Policy DK reimburses parents' mileage. Whether catastrophic aid counts transportation was not checked |
| P14.1 Donor-town and SWEPT retention for vacation homes | money-statewide-education-property-tax 1; district-tax-and-state-aid 8; site data: adequacy_aid (Hart's Location district); library: money-rand-case | full | The SWEPT applies to all property alike, second homes included |
| P14.2 Fryeburg or open enrollment; "locked into Kennett" | high-school-tuition-options 1–5; library: gov-tuition-towns, open-enrollment-status, choice-open-enrollment-2026-bills; Jackson file district-tuition-contracts 13–20 in `Jackson/money-and-governance.md` | full | Fryeburg is already budgeted for 2026-27, with no signed agreement found |
| P14.3 Long-term stability of Bartlett rates | district-tuition-contracts 3–4, 7; table harts_location_school_budget | partial | No cap and no projection. The rate follows Bartlett's elementary spending |
| P16.3 Dual-enrollment credits | district-budget-and-cost 11; sau9 file kennett-pathways school-programs-after-grade-6 8–9; library: dual-enrollment-rules | partial | No dual enrollment line in any budget from FY2017 to FY2027 |
| P17.2 Private academy or online charter | high-school-tuition-options 6; library: gov-tuition-towns 1, charter-schools 4, unh-early-college-online | partial | The state pays charter schools. Hart's Location has approved no "school tuition program" in the documents read |
| P18.1 / P18.3 Joint custody across towns | school-residency-rules 2–3; district-student-support 3; district-tuition-contracts 1; district-board-and-public-input 9 (policy JECA); library: change-of-school-assignment | full | Parents may agree in writing on either district. If they can't agree, SAU 9's superintendent decides for both districts, then the commissioner |
| P19.1 PILT and national forest receipts | district-tax-and-state-aid 10–12; federal-land-payments 1–3; table harts_location_federal_land_payments | full | PILT goes to the town; forest receipts go to the school district |
| P19.3 Adequacy aid with almost no students | district-tax-and-state-aid 6, 8; site data: adequacy_aid (Hart's Location district); library: money-adequacy-aid-amounts | full | No grant FY2024–FY2027. A one-time $9,941 hold harmless grant in FY2023 |
| P20.3 How residents can shape the next agreement | district-board-and-public-input 10–12; library: budget-warrant-articles 1 | full | The 2027 calendar, petitions (10 voters), joint board meetings |

## district-tuition-contracts: Hart's Location's K–8 Contract With Bartlett and Its Other School Arrangements

- kind: local
- question_type: governance_money
- description: A district's tuition contracts and agreements with other districts and schools: terms, cost formulas, caps, length, renewal, transportation and special education

1. The Bartlett–Hart's Location Tuition Agreement makes Bartlett "the assigned school for Hart's Location pupils in grades K through 8 for the purpose of school attendance laws," and requires Bartlett to give them "the same opportunities for education and cultural advancement and improvement" as Bartlett pupils.
   - citation: Bartlett – Hart's Location Tuition Agreement (April 6, 2010), Sections 1 and 6
   - source: https://drive.google.com/file/d/1oWuL7vKJ-z1Ol7rVY8wjGpnbQj1S9AwS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Scanned; 4 pages transcribed from image (viewed). Text: "Bartlett shall be deemed the assigned school for Hart's Location pupils in grades K through 8 for the purpose of school attendance laws." Section 1 also says Hart's Location "shall be responsible for the transportation methods and expenses" and that "Special Education costs, in addition to those included in the regular tuition calculations, will be the responsibility of the Hart's Location School District" (Bartlett file district-tuition-contracts fact 12). SAU 9's tuition page still files it under "K-6 TUITION CONTRACTS." Raw: raw/money/contracts/sau9-contract-k-6-harts-bartlett-current.pdf, harts-bartlett-contract-p1…p4.png, harts-bartlett-contract.ocr.txt; raw/money/sau9/sau9-tuitions.txt
2. Under the Hart's Location contract, tuition is billed only for Hart's Location students who actually attend: each payment is the per-pupil rate multiplied by "the actual number of Hart's Location students attending the Bartlett School," paid on December 15 and June 15.
   - citation: Bartlett – Hart's Location Tuition Agreement, Section 5
   - source: https://drive.google.com/file/d/1oWuL7vKJ-z1Ol7rVY8wjGpnbQj1S9AwS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text (p. 2, transcribed from image): "Tuition payments, calculated by multiplying the applicable per pupil tuition rate by the actual number of Hart's Location students attending the Bartlett School, shall be made on December 15th and June 15th of each year." The rate formula (prior-year elementary spending, CPI plus 2.5%, ADM, 2% rental fee) is in the Bartlett file, district-tuition-contracts fact 13. Raw: as fact 1
3. The Hart's Location contract has no end date: after its first three years (2010-11 to 2012-13) it renews each year, and either board can end it only by written notice naming a last school year at least the third full school year after the notice; notice given in 2026-27 could end it no sooner than June 2030 (**derived** reading).
   - citation: Bartlett – Hart's Location Tuition Agreement, Sections 2–3
   - source: https://drive.google.com/file/d/1oWuL7vKJ-z1Ol7rVY8wjGpnbQj1S9AwS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "This contract shall be automatically extended on a year-to-year basis at the end of the original term unless written notice of termination is given by either party to the other. Such notice shall specify the last school year for which the contract shall be effective, which shall be at least the third full school year following the school year". The school year runs September to August 31. The June 2030 date is our reading: the third full school year after 2026-27 is 2029-30. Raw: as fact 1
4. The Hart's Location contract has no cap on yearly tuition increases, no capital or maintenance payment other than the 2% rental fee, and no reporting duty other than the yearly tuition calculation, which is to be "appended to this agreement as a rider" (no rider is in the posted copy).
   - citation: Bartlett – Hart's Location Tuition Agreement, Sections 1–7
   - source: https://drive.google.com/file/d/1oWuL7vKJ-z1Ol7rVY8wjGpnbQj1S9AwS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: A statement about what the four pages contain, from reading all of them (transcribed from image). By contrast, Bartlett's and Jackson's 2027 Kennett contracts cap the inflation factor (Bartlett file district-tuition-contracts fact 6; Jackson file district-tuition-contracts 7–12 in `Jackson/money-and-governance.md`). Raw: as fact 1
5. The Bartlett School Board approved the Hart's Location contract on April 7, 2009 and the Hart's Location board on June 9, 2009, when its minutes record approving "the amendment to the Tuition Contract with Bartlett"; voters ratified it on March 9, 2010 (Hart's Location) and March 16, 2010 (Bartlett), and the State Board approved it on June 9, 2010.
   - citation: Bartlett – Hart's Location Tuition Agreement, p. 3; Hart's Location School Board Minutes, June 9, 2009; NH DOE letter, June 15, 2010
   - source: https://drive.google.com/file/d/1xNZ-VNZsyb9vrKt5E7SveA5XP0sRxRLt/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Minutes text: "(A) Consider Amendment to Tuition Contract with Bartlett – Nancy Holmes moved to approve the amendment to the Tuition Contract with Bartlett. The motion was seconded by George Holmes and passed 2-0-0." That meeting "was held in the conference room at the Josiah Bartlett Elementary School." The earlier contract was not found. Raw: raw/money/district/hsb-2009-06-09.pdf, .txt; raw/money/contracts/harts-bartlett-contract-p3.png, -p4.png
6. SAU 9's tuition page lists the contracts taking effect in 2027-28 (Albany, Bartlett, Eaton and Jackson with Conway, and Jackson with Fryeburg Academy); none involves Hart's Location, so its 2010 K–8 contract with Bartlett continues unchanged into 2027-28, and Hart's Location has no high school contract on the page.
   - citation: SAU 9, Tuition Agreement Overview, "Tuition Contracts - Effective 2027" and "Tuition Contracts - Current"
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Page text: "The following contracts have been ratified by the respective Boards and approved by the State Board of Education. They will go into effect as of the start of the 2027-28 School Year. 7-8 TUITION CONTRACTS Albany & Conway Eaton & Conway 9-12 TUITION CONTRACTS Albany & Conway Bartlett & Conway Eaton & Conway Jackson & Conway Jackson & Fryeburg Academy". The Kennett contracts were renegotiated because the 2003 agreements were replaced (Jackson file district-tuition-contracts 7–12 in `Jackson/money-and-governance.md`; Bartlett file district-tuition-contracts 5–11). Raw: raw/money/sau9/sau9-tuitions.html, .txt
7. Hart's Location's elementary tuition paid to Bartlett was $27,088 in 2022-23, $26,788 in 2023-24 and $27,682 in 2024-25, with one Hart's Location student each year; the board budgeted $34,182 for one student in 2025-26 and $0 for 2026-27; in 2019 SAU 9 gave the annual cost as "$24,000 for Elementary School students and $35,000 for High School students."
   - citation: Hart's Location School District Annual Reports 2024–2026, proposed budget pages; Annual Meeting Minutes, March 12, 2019 and March 28, 2023; School Board Minutes, January 14, 2025
   - source: https://drive.google.com/file/d/1ci3zjmuwpChrK56QXL7NaNfmR8yveEGG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Budget rows (images viewed): "61-10-1100-5560-0101 TUITION,ELEMENTARY $ 88,500 $ 27,088" (FY23 budget, actual); "Actuals FY24 ... 26,788"; "TUITION, ELEMENTARY 30.941 27,682 $ 34,182 (34,182) -100.00%". Student counts: "We currently have 1 elementary school student" (March 2023); "There is one student in 7th grade currently" (January 2025). DOE resident ADM was 1.2334 for 2022-23. 2019 text: "Becky Jefferson provided the current annual tuition costs of $24,000 for Elementary School students and $35,000 for High School students." See table harts_location_tuition_per_pupil_comparison. Raw: raw/money/district/har-2024-p4-budget.png, har-2025.txt, har-2026.rot90.txt, har-2020.ocr.txt, har-2024.txt, hsb-2025-01-14.txt
8. No warrant article, annual meeting discussion or board minute about sending Hart's Location students to Bethlehem or the Profile School District was found in Hart's Location's annual reports (2017–2026) or board minutes read (2009–2010, 2024–2026).
   - citation: Hart's Location School District annual reports 2017–2026 and minutes as listed
   - source: https://drive.google.com/drive/folders/1CRqOcyeJ7f7iGqdvJSHPuG99glfD7MC6
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: A statement about the documents searched (searched for "Profile", "Bethlehem", "Crawford", "contract", "agreement"). Board minutes for 2011–2023 were not read in full. Profile is site district 450 (SAU 35). Raw: raw/money/district/
9. Under NH law, Hart's Location could contract for any grade it doesn't run with another district's public school or an approved "school tuition program" (RSA 193:3, VI), and for high school with an academy or high school in NH or, when distance or transportation requires, another state (RSA 194:22), with State Board approval of high school contracts; for grades K–8, its Bartlett contract would first have to be ended with three full school years' notice (**derived** reading).
   - citation: RSA 193:3, VI; RSA 194:22; Bartlett – Hart's Location Tuition Agreement, Section 3
   - source: https://gc.nh.gov/rsa/html/XV/193/193-3.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Hart's Location
   - note: RSA 193:3, VI: "If there is no public school for the child's grade in the resident district, the school board may contract with another public school in another school district or with any private school that has been approved as a school tuition program by the school board, and may raise and appropriate money for the purposes of the contract". RSA 194:22: "If the contract is approved by the state board the school with which it is made shall be deemed a high school maintained by the district." Library topic gov-tuition-towns covers both statutes. The link to the K–8 notice rule is our reading. Raw: raw/money/rsa/rsa-193-3.txt, rsa-194-22.txt

## high-school-tuition-options: Hart's Location's High School Arrangements, 2016 to 2026-27

- kind: local
- question_type: local_practice
- description: High school options for districts without a high school (already in `additional-data/district-practices.md`)

1. At Hart's Location's March 8, 2016 school district meeting, SAU 9's finance director explained the change of its high school "school of record" from Fryeburg Academy to Kennett High School: Fryeburg cost about $25,000 plus $9,000 for transportation, while Kennett with transportation cost about $30,000, because "The bus comes up to Harts Location to end of Brandon's driveway for $500.00."
   - citation: Hart's Location School District Meeting Minutes, March 8, 2016 (2017 Annual Report)
   - source: https://drive.google.com/file/d/1nR7C-KtNvAEPYBvJkqjLlyJe81Bgm7EW/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Richard Garabedian questioned the change from Fryeburg to Kennett High School for School of Record and was there a cost savings? Becky Jefferson, Director of Budget and Finance for the School District said yes, there was a cost savings on transportation. There is also a different cost for tuition for each town. Cost for Fryeburg was @ $25,000 with transportation cost of $9000.. Total cost & transportation for Kennett is @ $30,000." Scanned; OCR checked. Raw: raw/money/district/har-2017.pdf, har-2017.ocr.txt
2. The same 2016 minutes record the finance director saying that "the State of New Hampshire REQUIRES that the school of record for our town has to be within our state," that Kennett "was decided upon ... as our school of record at the School District Meeting," and that "Parents could send their child to Fryeburg but NH would not subsidize that student."
   - citation: Hart's Location School District Meeting Minutes, March 8, 2016 (2017 Annual Report)
   - source: https://drive.google.com/file/d/1nR7C-KtNvAEPYBvJkqjLlyJe81Bgm7EW/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: These are statements recorded in minutes, not a legal ruling. RSA 194:22 allows a contract with a school in another state "when distance or transportation facilities make it necessary," and Jackson's agreement with Fryeburg Academy takes effect in 2027-28 (Jackson file district-tuition-contracts 13–20 in `Jackson/money-and-governance.md`). Raw: as fact 1
3. In March 2017 the school district clerk reported that JBES was Hart's Location's school of record for kindergarten to grade 8 (with no students then) and that one student attended Kennett High School; Hart's Location paid $35,219 of high school tuition in 2018-19, $34,961 in 2020-21 and $36,553 in 2021-22, and in March 2022 SAU 9 said its one high school student would graduate.
   - citation: Hart's Location Annual School District Meeting Minutes, March 14, 2017 and March 8, 2022; Annual Reports 2021 and 2023, proposed budget pages
   - source: https://drive.google.com/file/d/1K8LPlegq0eCKeuTJSwtCDwPXqlVOsmGE/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text (2017): "Josiah Bartlett School in Bartlett is the school of record for Kindergarden- 8th grade (no students at this time), and 1 student is currently attending Kennett High School in Conway." 2022: "we have one high school student who will be graduating." Budget rows (image viewed): "TUITION,HIGH SCHOOL ... $ 34,961 ... $ 38,494 $ 36,553" (FY21 actual; FY22 budget, actual). Raw: raw/money/district/har-2018.ocr.txt, har-2023.txt, har-2023-p4-budget.png, har-2021-p4.png (FY19 "TUITION,HIGH SCHOOL ... 35,219" viewed), har-2021.ocr.txt
4. Hart's Location still has no high school contract, and Conway's March 2026 count of Kennett High students by home town lists no Hart's Location row; for 2026-27 its budget pays $21,650 of high school tuition and $6,125 of transportation, which board minutes tie to one student at Fryeburg Academy and mileage for four trips a day (Bartlett file high-school-tuition-options fact 8).
   - citation: Hart's Location School Board Minutes, November 13, 2025, December 9, 2025 and February 10, 2026; Hart's Location Budget Report, November 13, 2026; Conway file conway_kennett_enrollment_by_town
   - source: https://drive.google.com/file/d/1OSkFvkdZPEQCYwQRCTTq1v6gDPHUXHhO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Budget report (agenda item 5-b): "61-10-1100-5560-0103 TUITION,HIGH SCHOOL 21,650.00 0.00 0.00 21,650.00 100.00%" and "61-10-2720-5513-0120 PUPIL TRANSPORTATION 6,125.00". December 2025: "she would be away and would need to do electronic signatures for Fryeburg billing and mileage." November 2025: "whether there needs to be an MOU with Fryeburg and/or Kennett for high school options." No signed Fryeburg agreement was found. Raw: raw/money/district/hsb-agenda-2026-11-18.pdf, .txt; hsb-2025-11-13.txt; hsb-2025-12-09.txt
5. At the February 10, 2026 budget hearing SAU 9's Director of Student Services "shared some information on Open Enrollment," and the board chair gave the tuition trust fund's target as "3-4 students."
   - citation: Hart's Location School Board Minutes, February 10, 2026 (public hearing)
   - source: https://drive.google.com/file/d/11auwhGv2k_5aNsFwLko9ybaPIx5fbVVC/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "A question was raised as to what the target goal for tuition was and Nancy Ritger responded 3- 4 students. Pam Stimpson shared some information on Open Enrollment and there was a brief discussion." The minutes don't say what was shared. Open enrollment law and the failed 2026 statewide bills: library topics open-enrollment-status and choice-open-enrollment-2026-bills. Raw: raw/money/district/hsb-2026-02-10.txt
6. No Hart's Location document read approves a private school as a "school tuition program" or provides for paying tuition to an online or chartered school; under NH law the state, not the district, pays a state-authorized charter school's per-pupil amounts (library charter-schools fact 4).
   - citation: Hart's Location annual reports 2017–2026, policies folder and minutes as listed; RSA 194:27; RSA 193:3, VII
   - source: https://drive.google.com/drive/folders/19vfu68l77x94uGiySPqjbKosj5AzlrAR
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: A statement about the documents searched. Hart's Location's posted policies are only DAF, DK, JECA and JFCJ (raw/money/district/drive-folder-listings.txt). RSA 194:27 requires a district without a high school to pay tuition at "an approved public high school ... an approved public academy, or a private school approved as a school tuition program by the school board pursuant to RSA 193:3, VII." Raw: raw/money/rsa/rsa-194-27.txt, rsa-193-3.txt; raw/money/district/drive-folder-listings.txt

## district-budget-and-cost: Hart's Location School District Budget, Trust Funds and New Students

- kind: local
- question_type: governance_money
- description: A district's budget and its trend, what drives increases, what its cost per pupil covers, salary schedules and contracts, and where to find budget documents

1. Hart's Location's 2026-27 operating budget of $36,650 is $21,650 for high school tuition, $6,125 for transportation, $4,521 for its SAU 9 share, $2,554 for board costs (audit, insurance, workers' compensation, expenses) and $1,800 for special education services, with no elementary tuition; voters added $12,000 for the two trust funds, for $48,650 in all.
   - citation: Hart's Location School District 2026 Annual Report, 2026-27 proposed budget; Hart's Location Budget Report, November 13, 2026
   - source: https://drive.google.com/file/d/1ci3zjmuwpChrK56QXL7NaNfmR8yveEGG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Budget report: "TOTAL 61 GENERAL FUND 86.10% $48,650.00 $2,241.00 $4,521.00 $41,888.00". Special education: OT/PT $100, special education tuition $100, testing/counseling $1,500, speech $100. Board: workers' comp $446, audit $1,000, board expense $200, liability insurance $908. All 2026 articles passed unanimously (Bartlett file district-board-and-public-input fact 8). Raw: raw/money/district/har-2026.rot90.txt, hsb-agenda-2026-11-18.txt
2. Hart's Location's voted operating budget rises and falls with its students: $32,886 for 2019-20, $116,245 for 2020-21, $168,106 for 2021-22, $99,253 for 2022-23, $38,497 for 2023-24, $41,508 for 2024-25, $45,097 for 2025-26 and $36,650 for 2026-27.
   - citation: Hart's Location annual meeting minutes, 2019–2026 (Annual Reports 2020–2026); 2026 Warrant
   - source: https://drive.google.com/drive/folders/15lpWDx42NVWniWRH4jW_wASuB3zlpKpl
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Each year's operating article as moved and passed. NH DOE counted 4 resident pupils in 2020-21 and 2021-22 and about 1 since (table harts_location_school_budget). In March 2022 SAU 9 said "the school budget is down significantly from last year." Raw: raw/money/district/har-2020.ocr.txt … har-2026.txt, ham-2026-03-10.txt
3. In March 2022 SAU 9's superintendent told Hart's Location voters that students living near existing Bartlett bus routes "can travel to school at no additional cost to the town," while families outside Bartlett's bus range drive their children and are "reimbursed on a per mileage basis by the school district."
   - citation: Hart's Location Annual School Meeting Minutes, March 8, 2022 (2023 Annual Report)
   - source: https://drive.google.com/file/d/1oekW96UaGfXwv4N7vwKoCFYe32rc3Klo/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Kevin explained that Hart's Location Students who live in the proximity of existing Bartlett bus routes can travel to school at no additional cost to the town. For those students who reside outside of the Bartlett bus service range, transportation is provided by the individual families and is reimbursed on a per mileage basis by the school district." Transportation actuals were $0 in FY2020, FY2021 and FY2023 and $1,246 in FY2022 (budget page image viewed). Raw: raw/money/district/har-2023.txt, har-2023-p4-budget.png
4. Hart's Location's tuition expendable trust fund was described by SAU 9 in 2020 as "our community's financial buffer against the possibility of another family moving into town," and in 2024 the superintendent said that if "a student or two moves into town during the school year," the board could hold a public hearing to withdraw from it to pay the extra tuition.
   - citation: Hart's Location Annual School Meeting Minutes, March 10, 2020 (2021 Annual Report) and March 12, 2024 (2025 Annual Report)
   - source: https://drive.google.com/file/d/1ppdtwxknL6dtIxa-1stBfEaIxTzPxZhZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: 2020 text: "The town could hold a Special School Meeting and pass a Supplemental Budget or draw from this fund." 2024 text: "Kevin noted that if a student or two moves into town during the school year, the School Board could hold a public hearing with the intent to withdraw from the Expendable Trust Fund for the purpose of paying the additional tuition for the new students." The public hearing rule is RSA 198:20-c, II (budget-traditional-district-meeting fact 3). Raw: raw/money/district/har-2021.ocr.txt, har-2025.txt
5. When new students arrived for 2020-21 that were "not included in the prior year budget," SAU 9 said the district would draw on the tuition trust, and NH DOE's financial report shows $32,348.41 coming from expendable trust funds in fiscal year 2021, the year Hart's Location's elementary tuition reached $65,461 and its local school tax rate $3.82.
   - citation: Hart's Location Annual School District Meeting Minutes, March 9, 2021; site data (DOE-25 revenue account 5252, FY2021); NH DRA tax rate 2020
   - source: https://drive.google.com/file/d/1l68RbddyK5bCXvNOWwsRI93h1u0trTQs/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Minutes text: "Lili Gilligan explained that due to new students not included in the prior year budget, there will be a need to expend from the Tuition Trust Reserve Fund." The 2021 meeting was held at the JBES gym. Query row: "2021 | From Other Expendable Trust Funds | 5252 | 32348.41". The $3.82 local school rate (tax year 2020) matches DRA's in the site's data (property_tax, Hart's Location district), which has every year's rates. Raw: raw/money/district/har-2022.ocr.txt; raw/money/state-data/site-db-harts-queries.txt, dra-tax-rates-harts-and-neighbors.csv
6. At the March 2018 meeting, after a resident asked how the town would handle "a possible influx of new students," the moderator noted the option "to dissolve the town and have the schools funded by the county, but that would mean loss of local control," a resident said "it's our responsibility to raise the funds required," and the clerk noted any tax increase "is shared by all the property owners in the town, not just the residents."
   - citation: Hart's Location Annual School District Meeting Minutes, March 13, 2018 (2019 Annual Report)
   - source: https://drive.google.com/file/d/1NgCs4KSeovbH6SXia8DCwrNd3RMDwDTP/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Katie Landry asked about the ramifications of a possible influx of new students if families moved into town and how the residents would handle the additional costs. Les Schoof detailed the history of town funding of schools in Hart's Location. The option exists to dissolve the town ... Mark noted that there is limited property available in Hart's Location and that new families are always possible, but a large influx of new students in any given year is unlikely." Statements as recorded; dissolving the town was not studied further in the documents read. Raw: raw/money/district/har-2019.ocr.txt
7. In March 2020 SAU 9's finance director said that once voters pass the budget the town "has committed itself to raise the full amount," that a special meeting can raise more money but she knew of no case where a budget was reduced, and that unspent money goes to the year-end balance, "typically used to reduce taxes."
   - citation: Hart's Location Annual School Meeting Minutes, March 10, 2020 (2021 Annual Report), Article 7
   - source: https://drive.google.com/file/d/1bFILeC1alWEBZhUVSYZiVyPAI-Oeitdb/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Lilly Gilligan indicated that if a community needs to raise additional funds, a Special School Meeting could be held and Supplemental budget voted on to raise additional funds, but she is not aware of a case in which the budget could be reduced and that that question would need to be referred to counsel." In 2023 the superintendent said "the town only pays for services actually rendered and that unexpended funds goes back in as revenue." Raw: raw/money/district/har-2021.ocr.txt, har-2024.txt
8. Hart's Location's trustees of trust funds reported the school tuition reserve at $79,547.14 and the school special education fund at $81,143.09 on December 31, 2025, both listed as expendable trusts created in 1992; SAU 9 has suggested targets of about $100,000 for special education (2020, 2023) and $90,000 for tuition (2023).
   - citation: Town of Hart's Location 2025 Annual Report, "2025 Hart's Location School District Capital Reserve and Trust Funds," p. 28; Hart's Location Annual Meeting Minutes, March 10, 2020 and March 28, 2023
   - source: https://hartslocation.com/wp-content/uploads/2026/03/2025-Annual-Town-School-Reports_Digital-Version.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Scanned page; transcribed from image (OCR checked). Text: "School Tuition Reserve School Special Education ... Expendable Trust Expendable Trust ... Bal. 01/01/25 75,507.98 $ 71,104.02 ... Additions: 4000.00 $ 10,000.00 ... Bal. 12/31/25 79,547.14 $ 81,143.09". School documents call the special education fund a "Capital Reserve Fund," and 2010 minutes say the tuition trust was "created for that purpose in 2003." See table harts_location_trust_funds. Raw: raw/money/town/town-annual-report-2025.pdf, town-annual-report-2025-p27-30.ocr.txt; raw/money/district/har-2021.ocr.txt, har-2024.txt, hsb-2010-01-12.txt
9. In 2020-21 a Hart's Location student needing special education started mid-year: SAU 9 later said the first year's cost "was not significant ... ($4k) because the student started midyear, and we withdrew $42k to cover the rest of the school year," and the district's special education tuition was $2,284 in 2019-20 and $42,121 in 2020-21.
   - citation: Hart's Location Annual School Meeting Minutes, March 8, 2022 (2023 Annual Report); Special Education Expenses/Revenue page, 2022 Annual Report
   - source: https://drive.google.com/file/d/1oekW96UaGfXwv4N7vwKoCFYe32rc3Klo/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Kevin Richard responded that the amount was not significant for the first year ($4k) because the student started midyear, and we withdrew $42k to cover the rest of the school year, however this does not represent the cost we would have incurred had it been for a full school year." Report: "1200.560.109 Tuition, Special Education $2,284 $42,121". The 2022 meeting also heard that "much of the Special education costs will be covered in house by staff with those specific capabilities, which includes testing." Raw: raw/money/district/har-2023.txt, har-2022.ocr.txt
10. No Hart's Location budget from 2016-17 to 2026-27 has a preschool or pre-kindergarten line, and its Bartlett contract covers grades K through 8 only.
   - citation: Hart's Location School District Annual Reports 2017–2026, proposed budget pages; Bartlett – Hart's Location Tuition Agreement
   - source: https://drive.google.com/drive/folders/15lpWDx42NVWniWRH4jW_wASuB3zlpKpl
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: A statement about the budgets read. Lines are regular education tuition (elementary, high school), special education (OT/PT, tuition), testing/counseling, speech, board services, SAU share, transportation and trust transfers. JBES's preschool rules are in the Bartlett file jbes.md (district-preschool); no document read says whether Hart's Location children may enroll. Preschool special education is the resident district's cost (RSA 186-C:13; money-special-education-aid fact 1). Raw: raw/money/district/har-20*.txt
11. No Hart's Location budget from 2016-17 to 2026-27 has a line for dual enrollment, Running Start or college courses; its only high school spending lines are tuition and transportation.
   - citation: Hart's Location School District Annual Reports 2017–2026, proposed budget pages
   - source: https://drive.google.com/drive/folders/15lpWDx42NVWniWRH4jW_wASuB3zlpKpl
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: A statement about the budgets read. How Kennett students pay for Running Start and early college courses is in the sau9 file kennett-pathways (school-programs-after-grade-6) and library topics dual-enrollment-rules and early-college-at-your-high-school. Raw: as fact 10
12. Hart's Location's school budget has no line for Education Freedom Accounts, which the state pays from its education trust fund (library money-efa-funding-link); asked about them in March 2025, SAU 9 said "it is an evolving situation," and the site's EFA data shows no Hart's Location EFA students for 2022 through 2027.
   - citation: Hart's Location Annual School District Meeting Minutes, March 11, 2025 (2026 Annual Report); site data (EFA entries, town 236)
   - source: https://drive.google.com/file/d/1ci3zjmuwpChrK56QXL7NaNfmR8yveEGG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Ed Butler asked about how SAU-9 is approaching Freedom Savings Accounts. Pam Stimpson replied that it is an evolving situation and the SAU-9 administration is still working on the matter." Site rows for town 236 show 0 for base aid, free and reduced, special education and English learner counts in every year from 2022 to 2027. Raw: raw/money/district/har-2026.txt; raw/money/state-data/site-db-harts-queries.txt
13. Hart's Location's 2026-27 appropriations put $9,800 toward special education, $1,800 in budget lines plus the $8,000 reserve deposit, or 20.1% of the $48,650 total (**derived**).
   - citation: Hart's Location 2026 Annual Report, proposed budget and Article 5; Budget Report, November 13, 2026
   - source: https://drive.google.com/file/d/1ci3zjmuwpChrK56QXL7NaNfmR8yveEGG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Derived: (100 + 100 + 1,500 + 100 + 8,000) ÷ 48,650 = 20.1%. Article 5 text: "the sum of $8,000 to be placed in the Capital Reserve Fund (Special Education)". In February 2026 SAU 9 said one out-of-district placement "could reach as high as $300,000" and that the tuition trust may not be used for special education (Bartlett file district-tuition-contracts fact 15; raw/money/district/hsb-2026-02-10.txt). Raw: raw/money/district/har-2026.rot90.txt, hw-2026.txt
14. For a hypothetical $300,000 placement, NH's catastrophic aid rule at the 2024-25 state average cost ($21,520 per pupil) would leave Hart's Location about $103,296 and the state about $196,704, with the state's share paid only after the year ends (**derived**).
   - citation: RSA 186-C:18, III and VI(a) (library money-special-education-aid facts 1 and 5); library money-special-education-costs-trends fact 8
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-18.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Hart's Location
   - note: Derived: district pays 3.5 × $21,520 = $75,320, plus 20% of ($215,200 − $75,320) = $27,976, total $103,296. The state pays 80% of $139,880 = $111,904 plus everything above 10 times ($300,000 − $215,200 = $84,800), total $196,704. The $300,000 is SAU 9's February 2026 upper figure, not an actual case. Aid may be prorated down to 80% of the entitlement, and rules change for costs from 2027-28 (library). NH DOE's actual figures for aid paid in FY2026 are in the site's data (special_education_aid): a threshold of $75,319.68 (3.5 times $21,519.91) and a proration of 91.14%; Hart's Location has no row in its files for FY2021-FY2026. Raw: raw/money/rsa/toc-186-C.txt

## district-tax-and-state-aid: Hart's Location's School Tax, the Statewide Education Tax, Aid and Federal Land Payments

- kind: local
- question_type: governance_money
- description: What drives a town's school taxes, beyond the site's tax rate and adequacy aid data: how a district's budget, its state aid and the tax rate fit together locally, its own projected rates, revaluations and their reasons, and village precinct rates

1. Hart's Location's assessed valuation rose from $20,661,097 for 2024 to $36,286,696 for 2025 (without utilities), after a town revaluation, so the same school cost now produces a lower rate per $1,000 than before 2025.
   - citation: NH DRA, 2025 Tax Rate Breakdown, Hart's Location (Municipal MS-1 valuation, current and prior year); 2025 Town Meeting Minutes, Article 8
   - source: https://hartslocation.com/wp-content/uploads/2026/03/2025-Annual-Town-School-Reports_Digital-Version.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Hart's Location
   - note: Text: "Total Assessment Valuation without Utilities $36,286,696 ... Prior Year $21,405,197 $20,661,097". Town meeting: "Mark: Revaluation of Property We should expect our assessments to go up. The tax burden is decided on the whole town valuation." The lower rate per $1,000 is our reading. Kept for the reason, the revaluation, which the site's data doesn't give. Hart's Location's DRA rates and valuations for 2014–2025 are in the site's data (property_tax, Hart's Location district); both valuations here match it (checked November 15, 2026). Raw: raw/money/town/town-annual-report-2025.txt (pages 32 and 36)
2. Hart's Location's local school tax rate swings with enrollment: its two highest years, 2020 ($3.82 per $1,000) and 2021 ($6.88), match the school years NH DOE counted 4 resident pupils, and it was negative in 2023 and 2024, when the district's other revenue, mostly the statewide education tax it keeps, was more than it needed to raise (**derived** reading).
   - citation: NH DRA tax rates 2019–2025 (library CSV); NH DOE adequacy files (resident ADM); Hart's Location Annual School District Meeting Minutes, March 11, 2025
   - source: https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Kept for the reading of why the rate moves, which the site's data doesn't give. Hart's Location's DRA rates for 2014–2025 are in the site's data (property_tax, Hart's Location district) and its resident pupils by year in adequacy_aid; the rates here match it (checked November 15, 2026). DOE resident ADM: 4 for the 2020-21 and 2021-22 school years (FY2022 and FY2023). The March 2025 minutes speak of a "second year in a row of a negative local school tax rate" (fact 7). Raw: raw/money/state-data/dra-tax-rates-harts-and-neighbors.csv, adequacy-aid-harts.csv
3. At the February 10, 2026 hearing SAU 9 estimated that about $2,500 would be returned to the town to reduce taxes, and in September 2026 the board voted to return the 2025-26 year-end balance of $10,732 to taxpayers rather than keep the $637 it was allowed to retain.
   - citation: Hart's Location School Board Minutes, February 10, 2026 and September 9, 2026 (draft)
   - source: https://drive.google.com/file/d/1XsNo6fL6pY9R7QLL8EGWsnmtJYrkHZe4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: February text: "Nicole Bell stated there will be an estimated $2500 returned to the town to reduce taxes." September text: "the end of year fund balance of $10,732 ... The maximum the Board can retain up to $637.00 ... for such little money, it is not worth retaining. Stacy Dunat made a motion to return the balance to the taxpayer". In October 2025 SAU 9 said $637 "was 2.5% of the fund balance and that is the maximum allowed per RSA." Draft minutes. Raw: raw/money/district/hsb-2026-02-10.txt, hsb-2026-09-09-draft.txt, hsb-2025-10-07.txt
4. Each extra Hart's Location pupil at JBES would add about $0.92 per $1,000 to the local school tax (about $461 a year on a $500,000 assessment), so two families with two school-age children each would add about $3.69 per $1,000 (about $1,843 on $500,000), before any use of the trust funds (**derived**).
   - citation: Hart's Location 2025-26 elementary tuition budget ($34,182 for one pupil); NH DRA 2025 local school valuation ($37,099,696)
   - source: https://drive.google.com/file/d/1ci3zjmuwpChrK56QXL7NaNfmR8yveEGG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Derived: $34,182 ÷ ($37,099,696 ÷ 1,000) = $0.92. Four pupils: $136,728 ÷ 37,099.696 = $3.69. Leaves out transportation, special education, any change in Bartlett's rate and later valuation changes. For scale, the whole 2025 tax rate was $2.62. The valuation and rates match NH DOE's and DRA's 2025 figures in the site's data (property_tax, Hart's Location district). Local school rates are set each fall from the budget voted in March, so a family arriving mid-year is paid for from the trust funds or a special meeting (district-budget-and-cost facts 4–5). Raw: raw/money/district/har-2026.rot90.txt; raw/money/state-data/dra-tax-rates-harts-and-neighbors.csv
5. Hart's Location's tuition trust of $79,547.14 (December 31, 2025) would cover about 2.3 years of one K–8 pupil at the 2025-26 tuition budget (**derived**); in 2022 SAU 9 said the fund held enough for "approximately 2 elementary school students or 1 high school student with some funds remaining."
   - citation: Town of Hart's Location 2025 Annual Report, trust funds page; Hart's Location Annual School Meeting Minutes, March 8, 2022
   - source: https://hartslocation.com/wp-content/uploads/2026/03/2025-Annual-Town-School-Reports_Digital-Version.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Derived: $79,547.14 ÷ $34,182 = 2.33. 2022 text: "Kevin Richard explained that currently we have enough in our Tuition Trust Fund to cover approximately 2 elementary school students or 1 high school student with some funds remaining." Raw: raw/money/town/town-annual-report-2025-p27-30.ocr.txt; raw/money/district/har-2023.txt
6. New pupils would not bring Hart's Location state adequacy aid until its adequacy cost passed its statewide education tax: at FY2027 figures ($25,089 of SWEPT, $4,351 per pupil) that takes about 6 resident pupils without extra needs, and aid is based on the prior school year's count (**derived**).
   - citation: NH DOE FY2027 adequacy file (library CSV); RSA 198:40-a, III and 198:38, IV (library money-adequacy-aid-amounts facts 6–7)
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Derived: $25,089 ÷ $4,351 = 5.77, so 6 or more. Pupils eligible for free or reduced-price meals or special education add more per pupil ($2,441 and $2,229 in FY2027), which would lower that number. The SWEPT and rates match the site's database; Hart's Location's full calculation for FY2020–FY2027 is in the site's data (adequacy_aid, Hart's Location district). Raw: raw/money/state-data/adequacy-aid-harts.csv
7. In March 2025, after a "second year in a row of a negative local school tax rate," SAU 9 said no further tuition payments were expected that year, and in November 2025 the board discussed "confusion" over the statewide education tax the town collects and "the bill owed to the district," asking SAU 9 to have NH DOE help explain school funding to the town.
   - citation: Hart's Location Annual School District Meeting Minutes, March 11, 2025; School Board Minutes, November 13, 2025
   - source: https://drive.google.com/file/d/1V0uATFIWr90ycj7gUqK-A-2GYxHkDqh4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: November text: "There was conversation about the SWEPT tax collected by the town and the bill owed to the district. With the confusion about billing, Helen Brandon requests that Aimee Frechette and Mike Wade connect with the DOE and perhaps ask them to help inform the town of Harts about how school funding is allocated". The town's 2025 treasurer's report shows "School Assessment 2024/2025 25482.00" paid to the school district. Raw: raw/money/district/har-2026.txt, hsb-2025-11-13.txt; raw/money/town/town-annual-report-2025-p27-30.ocr.txt
8. Because Hart's Location keeps its whole statewide education tax and has almost no pupils, that tax works much like a local school tax for its owners: in 2025 the $0.73 state rate raised $26,614, more than the $17,691 raised by the $0.48 local school rate (**derived** reading).
   - citation: NH DRA, 2025 Tax Rate Breakdown, Hart's Location
   - source: https://hartslocation.com/wp-content/uploads/2026/03/2025-Annual-Town-School-Reports_Digital-Version.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Net Required Local Education Tax Effort $17,691 State Education Tax $26,614 State Education Tax Not Retained $0". The comparison is our reading; the SWEPT is levied at one statewide rate on every property, second homes included (RSA 76:3, library). The rates and tax dollars match DRA's and NH DOE's 2025 figures in the site's data (property_tax, Hart's Location district), and the $26,614 matches NH DOE's FY2026 SWEPT for Hart's Location in adequacy_aid, which also shows no adequacy grant from FY2020 to FY2027 except FY2023. Raw: raw/money/town/town-annual-report-2025.txt (page 32)
9. The Town of Hart's Location's 2025 tax rate calculation shows $200 of war service credits and no other credits, and the town's 2025 annual report doesn't mention an elderly exemption; whether the town has adopted one under RSA 72:39-b was not found.
   - citation: NH DRA, 2025 Tax Rate Breakdown, Hart's Location; Town of Hart's Location 2025 Annual Report
   - source: https://hartslocation.com/wp-content/uploads/2026/03/2025-Annual-Town-School-Reports_Digital-Version.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Hart's Location
   - note: Text: "Total Property Tax Commitment ... $96,608 ($200) $96,408"; "War Service Credits $200". Searched the report for "elderly", "exemption" and "72:39". An exemption lowers assessed value before the rate is set, so it may not show in these pages; the town's MS-1 was not retrieved (Not retrieved). Raw: raw/money/town/town-annual-report-2025.txt
10. The federal Payment in Lieu of Taxes for Hart's Location's 5,395 acres of Forest Service land is paid to the Town of Hart's Location ($14,185 in FY2024, $14,886 in FY2025, $15,277 in FY2026); the Interior Department's table shows $0 for Carroll County.
   - citation: US Department of the Interior, PILT, "Payments and Acreage By State / County," New Hampshire, FY2022–FY2026; "PILT Acres by Agency," FY2026
   - source: https://pilt.doi.gov/counties.cfm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Hart's Location
   - note: FY2026 rows: "CARROLL COUNTY $0 0"; "HARTS LOCATION TOWN $15,277 5,395". Agency table: Hart's Location 0 BLM acres, 5,395 FS acres, 5,395 total. FY2022 was $8,897 and FY2023 $14,196. Bartlett received $108,202 and Jackson $111,728 for FY2026. Crawford Notch State Park is state land and earns no PILT. See table harts_location_federal_land_payments. Raw: raw/money/federal/pilt-nh-fy2022.txt … pilt-nh-fy2026.txt, pilt-nh-agency-fy2026.txt
11. The Town of Hart's Location books PILT as town revenue: its 2026 budget form (MS-636) lists "Payment in Lieu of Taxes" at $14,886 actual for 2025 and estimated for 2026, among revenues that lower the town's own tax, and the school district's budget has no PILT line.
   - citation: Town of Hart's Location, 2026 MS-636 Revenues (account 3186), and Treasurer's Report 2025, in the 2025 Annual Report
   - source: https://hartslocation.com/wp-content/uploads/2026/03/2025-Annual-Town-School-Reports_Digital-Version.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Hart's Location
   - note: Text: "3186 Payment in Lieu of Taxes 02 $14,886 $14,185 $14,886"; "PILT (Federal Payment in Lieu of Taxes) 14886.00". Total estimated town revenues for 2026: $59,420 against $90,903 of appropriations. The school budgets read (FY2017–FY2027) have no PILT revenue line. Raw: raw/money/town/town-annual-report-2025.txt (pages 22–26)
12. National forest receipts, a different federal payment, go to the Hart's Location School District: NH DOE's financial reports show "Federal Forest Reserve" revenue of $2,637.39 (FY2021), $2,308.42 (FY2022), $2,591.79 (FY2023), $2,548.04 (FY2024) and $5,579.72 (FY2025), and a resident asked at the February 2026 hearing why "the National Forest reserve had decreased."
   - citation: site data (DOE-25 revenue account 4810, Hart's Location, FY2021–FY2025); Hart's Location School Board Minutes, February 10, 2026; RSA 227-H:22
   - source: https://drive.google.com/file/d/11auwhGv2k_5aNsFwLko9ybaPIx5fbVVC/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Query row: "2025 | Federal Forest Reserve | 4810 | 5579.72". Minutes: "A question from the public was asked: why the National Forest reserve had decreased since the 2024-2025 school year? SAU 9 administrators said they would look into it and follow up." Older reports list "National Forest Reserve" revenue of $2,925 (2015-16 estimate) and $2,795 and $2,565 later. The state law is federal-land-payments fact 3. Raw: raw/money/state-data/site-db-harts-queries.txt; raw/money/district/hsb-2026-02-10.txt, har-2017.ocr.txt

## district-sau-governance: Hart's Location in SAU 9: Its Share, Its Vote and Where to See the Budget

- kind: local
- question_type: governance_money
- description: How a district shares an SAU: board seats and votes, how SAU costs are divided, and what the local board decides versus the SAU

1. Hart's Location pays its SAU 9 share on property value alone: SAU 9 counts 0.00 average daily membership for districts that run no schools, so Hart's Location's 0.33% of SAU 9's equalized value gives it 0.16% of the 2026-27 budget, $4,521 of $2,761,283.
   - citation: "Proposed School District Apportionment for the School Administrative Unit #9 Budget 2026-2027," Hart's Location School District 2026 Annual Report
   - source: https://drive.google.com/file/d/1ci3zjmuwpChrK56QXL7NaNfmR8yveEGG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Rotated scanned page; transcribed from image (viewed). Row: "Harts Loc. 25,223,383 0.00 0.33% 0.00% 0.16% $4,521". The method is half ADM and half equalized value (RSA 194-C:9, II; library budget-sau-budget-vote fact 1; Jackson file district-sau-governance 1–5 in `Jackson/money-and-governance.md`). Hart's Location's 2024-25 JBES student counted in Bartlett's 159.12 ADM (Bartlett file district-budget-and-cost fact 3). Raw: raw/money/district/har-2026-p10.png, har-2026.rot90.txt
2. Hart's Location pays its SAU 9 share whether or not it has students: in 2016-17 it had no K–8 students and one high school student, and its 2026-27 budget carries the $4,521 share with no K–8 tuition budgeted; its share was $3,336 (2019-20), $4,803 (2022-23), $3,788 actual (2024-25) and $4,521 (2026-27).
   - citation: Hart's Location Annual Meeting Minutes, March 14, 2017; Annual Reports 2023–2026, proposed budget pages ("SAU #9 SHARE")
   - source: https://drive.google.com/drive/folders/15lpWDx42NVWniWRH4jW_wASuB3zlpKpl
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Budget row (image viewed): "11 61-10-2320-5311-0104 SAU #9 SHARE $ 3,336 $ 3,336 $ 4,051 ... $ 4,235 ... $ 4,803 ... $ 4,341". 2026 report: "SAU #9 SHARE 3,875 $ 3,788 4,098 4,521 423 10.32%". The 2017-18 budget page also shows an SAU #9 share ($3,396). See table harts_location_school_budget. Raw: raw/money/district/har-2023-p4-budget.png, har-2026.rot90.txt, har-2018.ocr.txt, har-2017.ocr.txt
3. Hart's Location's SAU 9 share rose 10.32% for 2026-27, from $4,098 to $4,521; SAU 9's business administrator told the board in December 2025 that the budget "included the addition of SAU 9 technology positions" and that "if it is voted down by the SAU board, the numbers would change."
   - citation: Hart's Location School Board Minutes (draft), December 9, 2025; 2026 Annual Report, proposed budget
   - source: https://drive.google.com/file/d/18BekU0xGXEpT41b5sFSquRT6LKpdPZCp/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Mike Wade explained the budget included the addition of SAU 9 technology positions and if it is voted down by the SAU board, the numbers would change." From the 2027 annual meeting, each district votes on the SAU budget as a separate, unamendable article, and the votes of all districts are added together (library budget-sau-budget-vote fact 2). The November 18, 2026 agenda lists "Discuss Warrant Articles." Raw: raw/money/district/hsb-2025-12-09.txt, hsb-agenda-2026-11-18.txt
4. SAU 9 lists three Hart's Location school board members, but under RSA 194-C:7 a district that maintains no schools has one vote on the SAU board; in a weighted vote, which is used only when demanded, Hart's Location would have none, since one vote needs 8 or more resident pupils and NH DOE counts 1 (**derived**).
   - citation: RSA 194-C:7; RSA 194-C:8; NH DOE FY2027 adequacy file (resident ADM 1); SAU 9 Hart's Location School Board page
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-8.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Hart's Location
   - note: RSA 194-C:8: "each district shall be entitled to one vote for each 16 pupils residing in that district and enrolled in schools under the administrative unit. A balance of 8 or more students shall entitle that district to an additional vote. A balance of fewer than 8 students shall have no net effect". Derived: 1 ÷ 16 = 0, remainder 1. The FY2027 resident count of 1 matches the site's data (adequacy_aid, Hart's Location district). This fills the "not computed" cell for Hart's Location in the Jackson file's jackson_sau9_board_seats_and_votes. Board page: Helen Brandon (chair, term to 2027), Nancy Ritger (to 2028), Stacy Dunat (to 2029). Raw: raw/money/rsa/toc-194-C.txt; raw/money/sau9/harts-location-board.txt; raw/money/state-data/adequacy-aid-harts.csv
5. The SAU 9 board, on which Hart's Location sits, sets the salaries of all SAU staff, divides their cost among the districts and can remove superintendents (library gov-sau fact 4); the Jackson file's reading of the September 10, 2026 SAU 9 minutes lists 12 members present and none from Hart's Location.
   - citation: RSA 194-C:5, III; SAU 9 School Board Minutes (draft), September 10, 2026 (Jackson file district-sau-governance 9 in `Jackson/money-and-governance.md`)
   - source: https://gc.nh.gov/rsa/html/XV/194-C/194-C-5.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Hart's Location
   - note: RSA text: "The school board of each school administrative unit shall fix the salaries of all school administrative unit personnel, shall apportion the expense of the salaries and benefits among the several districts ... The school administrative unit board shall have the authority to remove superintendents and other administrators." Attendance is from the Jackson file's note (members from Conway, Bartlett, Eaton, Albany and Jackson); other meetings were not checked. In June 2025 Hart's Location's board was told "the SAU9 Board will be presented with a recommendation for an Assistant Superintendent." Raw: raw/money/rsa/toc-194-C.txt; raw/money/district/hsb-2025-06-10.txt
6. In September 2026 the Hart's Location board said that keeping SAU 9's Executive Committee "as it has been is efficient" and that doing policy and job-description work with the full SAU board "would result in lengthy meetings and may decrease attendance overall."
   - citation: Hart's Location School Board Minutes (draft), September 9, 2026, item 5.a
   - source: https://drive.google.com/file/d/1XsNo6fL6pY9R7QLL8EGWsnmtJYrkHZe4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Executive Committee & SAU #9 School Board Attendance: The Hart's Board feels that keeping the Executive Committee as it has been is efficient". SAU 9's July 2026 debate on its board's organization is in the Jackson file (district-sau-governance 10 in `Jackson/money-and-governance.md`). Draft minutes. Raw: raw/money/district/hsb-2026-09-09-draft.txt
7. Hart's Location's annual reports for 2020 to 2023 print SAU 9's budget by function with Hart's Location's dollar share of each line; for example, of its $4,803 share for 2022-23, $1,758 was for the Office of Business and Finance, $811 the Office of Superintendent and $657 the Office of Assistant Superintendent.
   - citation: "School Administrative Unit Number 9, 2022-2023 Budget," Hart's Location School District 2022 Annual Report, p. 10
   - source: https://drive.google.com/file/d/1l68RbddyK5bCXvNOWwsRI93h1u0trTQs/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Page viewed (raw/money/district/har-2022-p10.png): "Hart's Location's Share .2491% ... Office of Business and Finance ... 705,809 $ 1,758 ... Office of Superintendent 325,389 $ 811 ... Office of Assistant Superintendent 263,900 657 ... Net Total Expenses $1,927,914 $ 4,803". The 2021 and 2023 reports print the same layout (2020-21 to 2023-24). The 2024–2026 reports print the apportionment table instead. Raw: raw/money/district/har-2022.pdf, har-2021.ocr.txt, har-2023.txt
8. To see the SAU 9 charge to Hart's Location, residents can use the district's annual reports in the "Annual Reports - Hart's Location" folder (2017–2026), the budget status reports in board agenda packets (the November 18, 2026 packet shows the full $4,521 share committed), and SAU 9's own budget reports attached to SAU 9 board minutes.
   - citation: SAU 9, Hart's Location School Board page and linked folders; Hart's Location Budget Report, November 13, 2026; Jackson file district-sau-governance 14 in `Jackson/money-and-governance.md`
   - source: https://www.sau9.org/harts-location
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Page link: "Policies, Agendum, Minutes and Annual Reports" (https://drive.google.com/drive/folders/1CRqOcyeJ7f7iGqdvJSHPuG99glfD7MC6), with subfolders for agendas, annual reports, minutes, policies and warrants (2016–2026). Budget report row: "61-10-2320-5311-0104 SAU #9 SHARE 4,521.00 0.00 4,521.00 0.00 0.00%". Raw: raw/money/sau9/harts-location-board.html, .txt; raw/money/district/hsb-agenda-2026-11-18.txt

## district-board-and-public-input: The Hart's Location School Board, Its Meetings, Notices and Elections

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. The Hart's Location School Board has met on weekday mornings at Josiah Bartlett Elementary School in Bartlett since at least 2009 (8:15 a.m. in the JBES conference room in 2009–2010, 8:00 a.m. now), with the SAU 9 superintendent or staff attending; no minutes read give a reason for the time or place.
   - citation: Hart's Location School Board Minutes, June 9, 2009, November 10, 2009, January 12, 2010; 2024–2026 minutes
   - source: https://drive.google.com/file/d/1oUxvgoGBhFaFVq47kiNfIjxBWa1npVpA/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: 2009 text: "The meeting was held in the conference room at the Josiah Bartlett Elementary School. (1) The meeting was called to order by Chair Nancy Ritger at 8:15 a.m." and "The next meeting will be held on January 12, 2010 at 8:15 a.m. in Bartlett." The SAU 9 board meets in the evening (6 p.m.). The "no reason given" statement covers the minutes read: 2009–2010 and September 2024 to September 2026. Raw: raw/money/district/hsb-2009-06-09.txt, hsb-2009-11-10.txt, hsb-2010-01-12.txt, hsb-2024-09-10.txt
2. SAU 9's page still says the Hart's Location board "Meets on the second Tuesday of every other month at 8:00 a.m. at the Josiah Bartlett Elementary School," but in April 2026 the board agreed to meet quarterly on Wednesday mornings at 8 a.m. at JBES, plus a February budget hearing and the March meeting; its next meetings are Wednesday, November 18 and Tuesday, December 8, 2026 at 8 a.m.
   - citation: SAU 9, Hart's Location School Board page; Hart's Location School Board Minutes, April 24, 2026; Agenda, November 18, 2026
   - source: https://www.sau9.org/harts-location
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Minutes: "The Board agreed to meet quarterly on Wednesday mornings at 8 a.m. at Josiah Bartlett Elementary School. They will add a meeting for the budget hearing in February and the annual meeting in March." Agenda: "Hart's Location School Board - Tuesday, December 8, 2026 at 8 a.m." The page also says: "Please check the events calendar to verify the schedule of upcoming meetings." Raw: raw/money/sau9/harts-location-board.txt; raw/money/district/hsb-2026-04-24.txt, hsb-agenda-2026-11-18.txt
3. Hart's Location holds its budget hearing and annual business meeting at the Hart's Location Town Hall, with exceptions: the 2021 meeting was at the JBES gym and the 2023 meeting moved to the Notchland Inn after the moderator, consulting the Secretary of State, postponed it for a winter storm.
   - citation: Hart's Location Annual School District Meeting Minutes, March 9, 2021 and March 28, 2023; School Board Minutes, November 10, 2009 and February 10, 2026
   - source: https://drive.google.com/file/d/1MMw6sII4au1fRWbAYarXtIXkk43Qd7O9/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: 2023 text: "Les Schoof, Town and School Moderator, in consultation with the NH Secretary of State's office, rescheduled the meeting on March 13th, due to an active Winter Storm Warning for March 14th ... rescheduled to Tuesday March 28th, 2023 at 4:30pm at the Notchland Inn." 2021 heading: "Josiah Bartlett Elementary School Gym, US Route 302, Bartlett, NH, 4:30 p.m." Raw: raw/money/district/har-2024.txt, har-2022.ocr.txt, hsb-2009-11-10.txt, hsb-2026-02-10.txt
4. Hart's Location's 2026 budget hearing (February 10) came 28 days before the March 10 annual meeting, and its 2027 hearing (February 9 at 5 p.m.) is set 28 days before the March 9 meeting, more than the 25 days RSA 32:5 requires (**derived**); minutes and agendas are posted in the board's Drive folder, but where paper notices are posted in town was not found.
   - citation: Hart's Location School Board Minutes, February 10, 2026; Agenda, November 18, 2026; RSA 32:5, I (library budget-traditional-district-meeting fact 2); RSA 91-A:2, II
   - source: https://drive.google.com/file/d/1OSkFvkdZPEQCYwQRCTTq1v6gDPHUXHhO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Derived from the dates. RSA 32:5 requires a hearing at least 25 days before the meeting with 7 days' notice. RSA 91-A:2, II requires each meeting's notice to be "posted in 2 appropriate places one of which may be the public body's Internet website ... at least 24 hours, excluding Sundays and legal holidays." RSA 197:7 requires the warrant to be posted 14 days ahead at the meeting place and one other place. Raw: raw/money/district/hsb-2026-02-10.txt, hsb-agenda-2026-11-18.txt; raw/money/rsa/rsa-91-A-2.txt, ch-32.txt
5. Few residents attend Hart's Location board meetings: the October and December 2025 minutes record no public present, and at the February 11, 2025 budget hearing only one board member came, so "No other Board decisions were made, as there was not a quorum."
   - citation: Hart's Location School Board Minutes, February 11, 2025, October 7, 2025 and December 9, 2025
   - source: https://drive.google.com/file/d/1Fdw01iHd_g-b0Gvdn638JqzZQplkzVa5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Attendance: Nancy Ritger, Aimee Frechette ... No other Board decisions were made, as there was not a quorum of the Board present at the meeting." October 2025: "There was no public in attendance and therefore no public comment." December 2025: "There was no public present." The March 10, 2026 school district meeting minutes list 11 attendees besides officials and SAU staff. Raw: raw/money/district/hsb-2025-02-11.txt, hsb-2025-10-07.txt, hsb-2025-12-09.txt, ham-2026-03-10.txt
6. Hart's Location's school offices are often filled by write-in: in 2024 "all results were write-ins as no-one filed for any office," in 2022 a one-year board seat was "inconclusive, 4 individuals received 1 write in vote each," and in 2023 "There were no ballot votes for the vacant school board seat."
   - citation: Hart's Location Annual School District Meeting Minutes, March 8, 2022, March 28, 2023 and March 12, 2024
   - source: https://drive.google.com/file/d/1ppdtwxknL6dtIxa-1stBfEaIxTzPxZhZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: The 2022 annual report lists the board as "Helen Brandon, Chair ... Nancy Ritger, Vice-chair ... VACANT Term Expires 2023." 2023 text: "Nancy Ritger mentioned that we still need a volunteer to fill the vacant school board seat and indicated that the responsibilities were not onerous, bi monthly meetings and consultation with SAU-9 staff on budget preparation." Stacy Dunat was re-elected in March 2026 to a term ending 2029. Raw: raw/money/district/har-2023.txt, har-2024.txt, har-2025.txt, har-2022.ocr.txt, ham-2026-03-10-p3.ocr.txt
7. Since at least 2016 no qualified resident has stood for Hart's Location school treasurer, so the board reappoints a non-resident property owner each year; in March 2026 SAU 9 said such an appointment lasts one year "based on current statute," and the meeting voted to direct the board to raise the term with the Legislature.
   - citation: Hart's Location Annual School District Meeting Minutes, March 8, 2016, March 9, 2021 and March 10, 2026
   - source: https://drive.google.com/file/d/1YE-06QfJZhiPNDo8uXbCcPkAAHZobJgb/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: 2026 text: "because the position was not filled by a locally elected resident, the appointment of a qualified School Treasurer is for a one-year term based on current statute. Nicole Bell suggested that it would require an act of the legislature to alter that ... A Motion was made and seconded to direct the School Board to discuss the matter {of School Treasurer appointment terms} with the State Legislature. Motion carried unanimously." 2021: "ineligible to be elected as a non-resident property owner." RSA 671:6 lets the board appoint a temporary officer "until the next annual district election" (gov-school-boards-and-superintendents fact 4). Raw: raw/money/district/ham-2026-03-10.txt, har-2022.ocr.txt, har-2017.ocr.txt
8. Hart's Location's posted policies are four: DAF (federal grant funds), DK (special education travel, 2006), JECA (manifest educational hardship, 1998) and JFCJ (weapons); the Drive folder view of its Section B (board governance and operations), where a conflict-of-interest or board-ethics policy would be filed, lists no files.
   - citation: SAU 9, "Policies - Hart's Location" folder
   - source: https://drive.google.com/drive/folders/19vfu68l77x94uGiySPqjbKosj5AzlrAR
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Folder listing (sections A–L): only Sections D (DAF, DK) and J (JECA, JFCJ) list files. Statutory limits on holding offices are in gov-school-boards-and-superintendents fact 2. Raw: raw/money/district/drive-folder-listings.txt; raw/money/policies/harts-policy-JECA.pdf, harts-policy-DK.pdf (and .txt)
9. Hart's Location's JECA policy on manifest educational hardship was adopted on August 17, 1998 and cites State Board rule Ed 320.01, so it predates the 2025 rewrite of RSA 193:3 that added "best interest" transfers (library change-of-school-assignment).
   - citation: Hart's Location School Board Policy JECA, Manifest Educational Hardship (adopted August 17, 1998)
   - source: https://drive.google.com/file/d/1NUUiRoFNcD5qPcISG0bsGbAfunZoVUtw/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "The superintendent or designee shall assign resident pupils to their appropriate public school ... Size of the school will not be considered a factor unless other extenuating factors also apply ... Parents aggrieved by the decision of the board may appeal to the State Board of Education Authority: RSA 193:3; ED 320.01". The comparison with the 2025 law is our reading of the dates. Raw: raw/money/policies/harts-policy-JECA.pdf, .txt
10. The 2027 school calendar for Hart's Location: filing for office January 20 to 29, last day for petitioned articles February 5, budget hearing February 9 at 5 p.m., annual report public March 2, and the annual meeting and officer election Tuesday, March 9, 2027 (business at 4:30 p.m.).
   - citation: Hart's Location School Board Agenda, November 18, 2026, item 7.b
   - source: https://drive.google.com/file/d/1OSkFvkdZPEQCYwQRCTTq1v6gDPHUXHhO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "Filing Dates for Office - Wednesday, January 20 to Friday, January 29, 2027 ii. Last Day for Petitioned Articles - Friday, February 5, 2027 iii. Budget Hearing - Tuesday, February 9, 2027 at 5 p.m. iv. Annual Report Available to Public - Tuesday, March 2, 2027 v. School District Annual Meeting - Tuesday, March 9, 2027 at 4:30 p.m." The same agenda asks the board to appoint a representative to SAU 9's School Start Time Ad Hoc Committee. Raw: raw/money/district/hsb-agenda-2026-11-18.pdf, .txt
11. Hart's Location residents vote on their own district's budget, tuition articles and trust deposits, but not on Bartlett's budget, which sets the cost base for their K–8 tuition, or on Conway's Kennett budget or capital plan; Hart's Location has no Kennett contract, so it pays no share of the Kennett maintenance fund.
   - citation: Bartlett – Hart's Location Tuition Agreement, Sections 4 and 7; SAU 9 Tuition Agreement Overview; Conway file district-tuition-contracts fact 6
   - source: https://drive.google.com/file/d/1oWuL7vKJ-z1Ol7rVY8wjGpnbQj1S9AwS/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Our reading of the contracts. Ways Hart's Location parents can speak at Bartlett meetings and the joint-board requirement are in the Bartlett file (district-board-and-public-input facts 8–10). Raw: raw/money/contracts/harts-bartlett-contract.ocr.txt; raw/money/sau9/sau9-tuitions.txt
12. Hart's Location residents can shape a future tuition agreement by speaking at board meetings and the February budget hearing, petitioning a warrant article (in a district Hart's Location's size, 10 registered voters by February 5 for 2027), and voting at the annual meeting, where the 2010 Bartlett contract was ratified; the contract also requires the two boards to meet jointly at least once a year.
   - citation: RSA 197:6 (library budget-warrant-articles fact 1); RSA 194:22; Bartlett – Hart's Location Tuition Agreement, Section 7 and p. 3; Agenda, November 18, 2026
   - source: https://gc.nh.gov/rsa/html/XV/197/197-6.htm
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: RSA 197:6: "25 or more voters or 2 percent of the voters of the school district, whichever is less, although in no event shall fewer than 10 registered voters be sufficient." The "10" is our reading for a district with under 500 voters. Contract p. 3: "Ratified at Hart's Location Annual School District Meeting on March 9, 2010." No recent joint Bartlett–Hart's Location board meeting was found (Bartlett file fact 10). School boards must allow at least 30 minutes of public comment (library gov-school-boards-and-superintendents fact 6). Raw: raw/money/rsa/toc-197.txt; raw/money/contracts/harts-bartlett-contract-p3.png

## district-special-education-services: Who Is Responsible for a Hart's Location Student's Special Education

- kind: local
- question_type: local_practice
- description: Who provides special education and related services in a district (on staff or contracted), reading specialists, 504 practice, IEP moves between schools, and out-of-district placements

1. A Hart's Location student's special education is Hart's Location's legal and financial responsibility: NH law charges special education expenses to "the school district where the child resides," and Hart's Location's contract makes special education costs beyond regular tuition "the responsibility of the Hart's Location School District."
   - citation: RSA 186-C:13, I; Bartlett – Hart's Location Tuition Agreement, Sections 1 and 4
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-13.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Hart's Location
   - note: RSA text: "All expenses incurred by a school district in administering the law in relation to education for children with disabilities in need of special education and related services shall be paid by the school district where the child resides". Contract Section 4: "Hart's Location will pay direct costs for special education or other specialized programs not included, or unable to be provided in the regular operation of the school." Ed 1102.03(o) defines the "local school board" as the body "responsible for providing elementary and secondary education to all children who reside in the district." Raw: raw/money/rsa/toc-186-C.txt, ed1100.txt; raw/money/contracts/harts-bartlett-contract-p1.png, -p2.png
2. Bartlett's admissions policy JFAB says that for non-resident students it enrolls, "the district in which the student resides shall retain all responsibility for the provision of special education and related services pursuant to RSA 186-C."
   - citation: Bartlett School Board Policy JFAB, Admission of Tuition and Non-Resident Students (revision adopted November 7, 2023)
   - source: https://drive.google.com/file/d/1y4RE9oARehZqKOO8b8CBMQKGF_j_GLDp/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Bartlett
   - note: Legal references listed: "RSA 186-C:13 Special Education; Liability for Expenses; RSA 193:3 Change of School or Assignment; RSA 193:12 Legal Residence Required". Raw: raw/money/policies/bartlett-policy-JFAB.pdf, .txt
3. SAU 9's Special Education Procedures Manual covers all seven districts, Hart's Location included, and lists SAU staff who handle special education for them, including a Director of Special Services and an "Out of District Coordinator/Court Liaison."
   - citation: SAU 9 School District Special Education Procedures Manual (revised October 2022; posted as the 2026 manual)
   - source: https://docs.google.com/document/d/1JwQpGhPRW76itiTFAp7O5dUGKjkiBXsOFlIA9vWAjUA/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "SAU 9 School District Special Education Procedures Manual Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location, Jackson ... DIRECTOR OF SPECIAL SERVICES Pamela L. Stimpson ... OUT OF DISTRICT COORDINATOR/COURT LIAISON". Linked from SAU 9's pages as "SAU#9 School District Special Education Polices and Procedures Manual" (https://www.sau9.org/271524_2). Raw: raw/money/sau9/sau9-special-education-procedures-manual.txt
4. Hart's Location's policy DK (2006) makes the district pay parents the federal mileage rate for driving a child to an out-of-district special education placement, but only for listed trips: the start and end of the program and of extended school year, school closures for holidays and vacations, IEP meetings, approved evaluator appointments, and other trips approved on petition.
   - citation: Hart's Location School Board Policy DK, Reimbursement for Special Education Travel (adopted February 13, 2006)
   - source: https://drive.google.com/file/d/1otpdCBtINKV5PiZdBgyCZdTADunGbk69/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Text: "The Hart's Location School District is financially responsible for the following reimbursable transportation costs to the parents/guardian of an out-of-district placed special needs student. The federal rate of mileage reimbursement for transportation will be used ... Requests for reimbursements should be received in the SAU #9 office within one month of travel. No requests for reimbursements will be accepted after June 30th of each year." Raw: raw/money/policies/harts-policy-DK.pdf, .txt
5. Hart's Location pays all transportation for its K–8 students under the contract, budgets it in one "Pupil Transportation" line ($2,500 a year from 2022-23 to 2025-26, $6,125 for 2026-27), and has no separate line for special education transportation.
   - citation: Bartlett – Hart's Location Tuition Agreement, Section 1; Hart's Location Annual Reports 2024–2026, proposed budgets
   - source: https://drive.google.com/file/d/1ci3zjmuwpChrK56QXL7NaNfmR8yveEGG/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Contract: "shall be responsible for the transportation methods and expenses in connection with such attendance." Budget row: "61-10-2720-5513-0120 PUPIL TRANSPORTATION 2,500 $ 2,500 $ 6,125 3,625 145.00%". Whether NH's catastrophic aid counts transportation was not checked. Raw: raw/money/district/har-2026.rot90.txt, har-2024-p4-budget.png

## district-student-support: Enrollment, Residency and Custody Paperwork for Hart's Location Families

- kind: local
- question_type: local_practice
- description: Counseling, social work and mental health support, English learner services, homeless student support, welcoming families of all backgrounds, and enrollment documents

1. Bartlett's policy JFAA asks families of children entering JBES for the first time for proof of a physical exam, immunization records, a birth certificate and "proof of residency satisfactory to the Superintendent or his/her designee," and defines the district of residence by RSA 193:12, II.
   - citation: Bartlett School Board Policy JFAA, Admission of Resident Students (adopted October 7, 2008; reviewed September 18, 2023)
   - source: https://drive.google.com/file/d/1OaP_NuprClH3vno1OoiCpvwAXpJnlzUZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Bartlett
   - note: Text: "Children entering school for the first time must have proof of physical examination, immunization records, a copy of the child's birth certificate and proof of residency satisfactory to the Superintendent or his/her designee." The policy is written for Bartlett residents. No list of acceptable residency documents was found. Raw: raw/money/policies/bartlett-policy-JFAA.pdf, .txt
2. Hart's Location has no residency or admissions policy in its posted policy folder (its Section J has only JECA and JFCJ), and SAU 9's site-wide "Annual Residency Verification Attestation" link returned "not found" on November 13, 2026.
   - citation: SAU 9, "Policies - Hart's Location" folder (Section J); SAU 9 home page link "Annual Residency Verification Attestation"
   - source: https://www.sau9.org/harts-location
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Hart's Location
   - note: Link target: https://drive.google.com/file/d/1U9KmEYmK5BZTCqjneLjKkJscCPjtCts-/view (HTTP 404, "Page Not Found"). RSA 193:12, VIII requires each district to adopt a policy on admitting non-resident students; whether Hart's Location has one outside the posted folder was not found. Under the contract, SAU 9's superintendent handles enrollment for both districts. Raw: raw/money/sau9/harts-location-board.html, .txt; raw/money/rsa/rsa-193-12.txt
3. Bartlett's policy JFAB says a child of divorced parents who lives mostly outside Bartlett may attend Bartlett schools, as a resident and without tuition, if the decree or parenting plan allows it or the parents agree in writing, but transportation "will not necessarily be provided."
   - citation: Bartlett School Board Policy JFAB, Admission of Tuition and Non-Resident Students
   - source: https://drive.google.com/file/d/1y4RE9oARehZqKOO8b8CBMQKGF_j_GLDp/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Bartlett
   - note: Text: "If a student's parents are divorced and the student lives primarily out of district, the student may nonetheless attend school within the District and be considered a resident of the District for school attendance purposes provided: (1) the divorce decree or parenting plan allows the student to attend the District; (2) or provided the parents have agreed in writing ... Students in this situation will not be charged tuition." For a Hart's Location parent, JBES is already the assigned K–8 school under the contract. Raw: raw/money/policies/bartlett-policy-JFAB.pdf, .txt

## school-residency-rules: Who Counts as a Resident for School in New Hampshire

- kind: rule
- question_type: rules
- description: Which district is legally responsible for a student under New Hampshire law: domicile, guardians, divided homes and parenting plans, moves between districts, attending a district where a student doesn't live, and who decides disputes

1. Under NH law a "legal resident" of a school district is a person "domiciled in the school district" who, if temporarily away, shows an intent to keep a principal dwelling there indefinitely and return, with acts consistent with that intent; a person may have only one legal residence at a time.
   - citation: RSA 193:12, III
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "'legal resident' of a school district means a natural person who is domiciled in the school district and who, if temporarily absent, demonstrates an intent to maintain a principal dwelling place in the school district indefinitely and to return there, coupled with an act or acts consistent with that intent ... A person may have only one legal residence at a given time." The statute does not depend on who owns the dwelling (seasonal or employer housing is not mentioned). Raw: raw/money/rsa/rsa-193-12.txt
2. For a child whose divorced parents share decision-making or legal custody, NH law makes the child's school residence that of the parent the child lives with, but the parents may agree in writing on either parent's district (each giving a copy to the district where that parent lives); if a court gives equal or nearly equal time, residence is as the order states.
   - citation: RSA 193:12, II(a)(2)(A)
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "a child's legal residence for school attendance purposes may be the school district in which either parent resides, provided the parents agree in writing to the district the child will attend and each parent furnishes a copy of the agreement to the school district in which the parent resides ... If the court order is for equal or approximately equal periods of residential responsibility, the child's legal residence for school attendance purposes shall be as stated in the order." Parents who live apart and are not divorced: the residence of the parent the child lives with (II(a)(1)). Subparagraph (B) says no district must transport the child beyond its own limits. Raw: raw/money/rsa/rsa-193-12.txt
3. NH's education commissioner decides residency questions, but when more than one district is involved or parents living apart can't agree, "the respective superintendents shall jointly make such decision," and only if they can't agree does the commissioner decide within 30 days, a decision that can be appealed to court; for Hart's Location and Conway families both districts share SAU 9's superintendent (**derived** observation).
   - citation: RSA 193:12, VI(a) and (c)
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "If more than one school district is involved in a residency dispute, or the parents who live apart cannot agree on the residence of a minor child, the respective superintendents shall jointly make such decision. In those instances when an agreement cannot be reached, the commissioner of the department of education, or designee, shall make a determination within 30 days". The rule that the child stays in the school of origin during a dispute is already in the library (military-children-compact fact 6). Raw: raw/money/rsa/rsa-193-12.txt
4. NH law counts as homeless children who lack "a fixed, regular, and adequate nighttime residence," including those sharing others' housing because of loss of housing or hardship and those living in motels, hotels, trailer parks or campgrounds "due to the lack of alternative adequate accommodations."
   - citation: RSA 193:12, IV
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Children and youths who are sharing the housing of other persons due to loss of housing, economic hardship, or a similar reason; are living in motels, hotels, trailer parks, or camping grounds due to the lack of alternative adequate accommodations". Bartlett and Conway's homeless policies (JFABD) are covered in the Jackson and Conway files. Raw: raw/money/rsa/rsa-193-12.txt

## federal-land-payments: Federal Payments for National Forest Land

- kind: how_it_works
- question_type: governance_money
- description: Federal payments for tax-exempt federal land (PILT) and national forest receipts: who receives them and whether they reach schools

1. The federal PILT Act lets recipients use Payment in Lieu of Taxes "for any governmental purpose," and payments to local governments are "not required to be further distributed to other local government units, such as school districts or cities."
   - citation: 31 U.S.C. 6902 (Chapter 69), as described in US Department of the Interior, PILT FAQs
   - source: https://www.doi.gov/pilt/resources/faqs
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Text: "Section 6902 of the PILT Act (Chapter 69, Title 31 of the U.S. Code) states PILT payments may be used by recipients (usually counties) for any governmental purpose and are not required to be further distributed to other local government units, such as school districts or cities." In New Hampshire the Interior Department's table lists payments to towns and $0 to counties such as Carroll (district-tax-and-state-aid fact 10). Raw: raw/money/federal/pilt-faqs.html, .txt
2. A place's PILT payment is generally $3.55 per acre of qualifying federal land (2026 dollars) minus other federal land payments it received the year before, such as national forest receipts and Secure Rural Schools money, or $0.51 per acre with no deduction, whichever is greater, subject to a population limit; Interior says FY2026 payments rose mainly because Secure Rural Schools was not authorized in FY2025.
   - citation: US Department of the Interior, PILT FAQs ("How are payments calculated?"; "Why is the FY 2026 payment amount higher")
   - source: https://www.doi.gov/pilt/resources/faqs
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Text: "(A) $3.55 (in 2026 dollars) times the number of acres of qualified Federal land in the unit of local government ... reduced by the amount of funds received by the locality in the prior fiscal year under certain other Federal land revenue-sharing programs, such as the Secure Rural Schools program ... (B) $0.51 (in 2026 dollars) times the number of acres". "This reduction was largely due to the non-authorization of Secure Rural Schools (SRS) in FY 2025." Raw: raw/money/federal/pilt-faqs.txt
3. NH law sends the federal money the state receives for the White Mountain National Forest (Weeks Act lands) to schools: NH DOE divides it among the towns by their national forest area and pays each town's share within 90 days to the treasurer of the school district, to be spent "for the benefit of the public schools" in addition to what law requires the town to raise.
   - citation: RSA 227-H:20–22
   - source: https://gc.nh.gov/rsa/html/XIX-A/227-H/227-H-22.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: RSA 227-H:22 text: "The several sums so apportioned to each organized town shall be paid over by the department of education, within 90 days after receipt, to the treasurer of the school district in the town ... and shall be expended for the benefit of the public schools in the organized town, in addition to the sums required by law to be raised for such purposes". RSA 227-H:21 apportions "in proportion to the area of such national forest in each, as determined by the forest service". Raw: raw/money/rsa/ch-227-H.html, .txt

## property-tax-relief: Elderly Exemptions and State Property Tax Relief

- kind: rule
- question_type: rules
- description: Property tax exemptions and credits for elderly, disabled and veteran homeowners, the state's low and moderate income homeowners relief, and how they apply to the school parts of a tax bill

1. NH towns may adopt an elderly property tax exemption, setting their own exemption amounts (at least $5,000) for owners aged 65 to 74, 75 to 79 and 80 or older, with income limits of at least $13,400 single or $20,400 married and an asset limit of at least $35,000 excluding the home.
   - citation: RSA 72:39-b, I–II
   - source: https://gc.nh.gov/rsa/html/V/72/72-39-b.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "An elderly exemption, based on assessed value for qualified taxpayers, may be granted for a different dollar amount determined by the town or city, to a person 65 years of age up to 75 years, to a person 75 years of age up to 80 years, and to a person 80 years of age or older ... Under no circumstances shall the amounts of the exemption for any age category be less than $5,000." Towns adopt or change it by the procedure in RSA 72:27-a. Raw: raw/money/rsa/rsa-72-39-b.txt
2. To get a NH elderly exemption the owner must have lived in New Hampshire at least 3 consecutive years before April 1 and meet the town's income and asset limits; a married couple must have been married at least 5 years if only the spouse owns the home.
   - citation: RSA 72:39-a, I–II
   - source: https://gc.nh.gov/rsa/html/V/72/72-39-a.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "(a) Has resided in this state for at least 3 consecutive years preceding April 1 in the year in which the exemption is claimed." Net assets exclude "the value of the person's actual residence and the land upon which it is located up to the greater of 2 acres or the minimum single family residential lot size". Raw: raw/money/rsa/rsa-72-39-a.txt
3. NH's low and moderate income homeowners property tax relief refunds all or part of the state education property tax on a homestead (up to $220,000 of value times the local equalization ratio) to owners with household income of $37,000 or less (single) or $47,000 or less (married or head of household); applications go to DRA between May 1 and June 30.
   - citation: RSA 198:57, III, IV and VI(a)
   - source: https://gc.nh.gov/rsa/html/XV/198/198-57.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Tiers: single under $23,100, 100%; $23,100–$27,800, 60%; $27,800–$32,400, 40%; $32,400–$37,000, 20%. Married or head of household under $29,400, 100%; to $35,300, 60%; to $41,100, 40%; to $47,000, 20%. It covers only the state education tax (RSA 76:3), not local school, town or county taxes. Raw: raw/money/rsa/ch-198.txt

## budget-traditional-district-meeting: The Traditional School District Meeting

- kind: how_it_works
- question_type: governance_money
- description: How a school budget is adopted at a traditional annual school district meeting.

1. A special school district meeting is held whenever the school board thinks there is occasion for one, or when 50 voters or one quarter of the district's voters, whichever is less, apply in writing; a special meeting may not raise or appropriate money after December 31 of the budget cycle.
   - citation: RSA 197:2; RSA 197:3, V
   - source: https://gc.nh.gov/rsa/html/XV/197/197-2.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: RSA 197:2: "A special meeting of a school district shall be held whenever, in the opinion of the school board, there is occasion therefor, or whenever 50 or more voters, or 1/4 of the voters of the district, whichever is less, shall have made written application". RSA 197:3, V: "no special meeting to raise and appropriate money ... may be held unless the vote is taken on or before December 31 of any budget cycle." The ballot and court-permission rules are fact 4 of this topic in the library. Raw: raw/money/rsa/toc-197.txt
2. To ask the superior court for an emergency special meeting, a school board must notify the commissioner of revenue administration by certified mail 10 days before petitioning, post notice of its vote within 24 hours, and show an "emergency," a sudden or unexpected, serious and urgent situation that demands prompt action; the court weighs whether it was foreseeable and whether other remedies exist.
   - citation: RSA 197:3, I(b)–(c), II and IV
   - source: https://gc.nh.gov/rsa/html/XV/197/197-3.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Factors: "(1) The severity of the harm to be avoided. (2) The urgency of the petitioner's need. (3) Whether the claimed emergency was foreseeable or avoidable. (4) Whether the appropriation could have been made at the annual meeting. (5) Whether there are alternative remedies not requiring an appropriation." Raw: raw/money/rsa/toc-197.txt
3. To spend from a school expendable trust fund, the school board must first hold a public hearing, with notice of its time, place and subject published in a newspaper of general circulation at least 7 days before.
   - citation: RSA 198:20-c, II
   - source: https://gc.nh.gov/rsa/html/XV/198/198-20-c.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "In order to expend such funds, the school board shall hold a public hearing prior to the expenditure to be made. Notice of the time, place, and subject of such hearing shall be published in a newspaper of general circulation in the relevant municipality at least 7 days before the meeting is held." The fund's money may be spent only for its purpose (paragraph I). Raw: raw/money/rsa/ch-198.txt
4. When an unusual circumstance requires spending beyond the district's appropriations, a school board may apply to the commissioner of education for authority before spending (or after, in a sudden emergency); a district with no budget committee must first hold a public hearing, and the board must name the source of money, since neither commissioner may raise the tax rate.
   - citation: RSA 32:11, I–IV
   - source: https://gc.nh.gov/rsa/html/III/32/32-11.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "the school board upon application to the commissioner of education, may be given authority to make such expenditure ... If there is no budget committee, the governing body shall hold a public hearing on the request, with notice as provided in RSA 91-A:2 ... Neither commissioner shall have the authority to increase the town or district's tax rate in order to fund such an expenditure." Raw: raw/money/rsa/ch-32.txt

## money-special-education-aid: Special Education (Catastrophic) Aid

- kind: how_it_works
- question_type: governance_money
- description: State help with very high-cost special education students, and the change coming July 1, 2028.

1. NH law charges special education costs to the school district where the child resides, including when a parent enrolls the child in another district's school under RSA 193:3, IV; exceptions apply to children placed in homes for children, health care facilities or state facilities.
   - citation: RSA 186-C:13, I and IV
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-13.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "IV. When a child is enrolled pursuant to 193:3, IV, the district in which the child resides shall retain the liability for expenses as set forth in this section." Exceptions: RSA 193:29 (homes for children, health care facilities) and RSA 186-C:19 (state facilities). Raw: raw/money/rsa/toc-186-C.txt
2. A district may exceed its annual budget to meet special education costs by the amount of additional special education aid it actually received from the state after the budget was approved.
   - citation: RSA 186-C:13, II
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-13.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "For the purposes of meeting the financial obligation for expenses incurred under this chapter, a school district may exceed its annual budget to the extent of additional special education aid which the district has actually received from the state after the annual school district budget was approved." Raw: raw/money/rsa/toc-186-C.txt
3. Unexpected special education costs that are eligible for state catastrophic aid and could not be identified before the district's budget was adopted are exempt from the statutory limits on spending beyond appropriations (RSA 32:8–32:10).
   - citation: RSA 186-C:18, X
   - source: https://gc.nh.gov/rsa/html/XV/186-C/186-C-18.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Unexpected special education costs incurred by a school district which are eligible for reimbursement from the state pursuant to RSA 186-C:18, III and which could not be identified prior to the adoption of the local district budget shall be exempt from the provisions of RSA 32:8, RSA 32:9 and RSA 32:10." Paragraph VIII lets a district borrow with reimbursement anticipation notes until the state aid arrives. Raw: raw/money/rsa/toc-186-C.txt
4. Each NH school district's annual report must account for its actual special education spending in the previous two fiscal years, with offsetting revenue from state, federal, Medicaid, insurance and other sources.
   - citation: RSA 32:11-a
   - source: https://gc.nh.gov/rsa/html/III/32/32-11-a.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "Each school district shall provide in its annual report an accounting of actual expenditures by the district for special education programs and services for the previous 2 fiscal years." Hart's Location's annual reports carry this as a "Special Education Expenses/Revenue" page. Raw: raw/money/rsa/ch-32.txt; raw/money/district/har-2026.rot90.txt

## gov-school-boards-and-superintendents: School Boards and Superintendents

- kind: term
- question_type: governance_money
- description: The division of duties between elected school boards and superintendents.

1. A NH school district that is not a cooperative has a school board of 3, 5, 7 or 9 members serving 3-year terms, as voters decide at an annual meeting; a district that has not voted otherwise has 3 members.
   - citation: RSA 671:4
   - source: https://gc.nh.gov/rsa/html/LXIII/671/671-4.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The school board of a district which does not otherwise vote shall have 3 members." Raw: raw/money/rsa/toc-671.txt
2. A candidate for a NH school district office must be a registered voter in the district; no one employed on a salary by an SAU or any district in it may be a school board member; and since September 8, 2026 no one may hold more than one of the offices of school board member, district moderator, treasurer, auditor or clerk, or school budget committee member.
   - citation: RSA 671:18, I (as amended by 2026, 295:1, eff. Sept. 8, 2026)
   - source: https://gc.nh.gov/rsa/html/LXIII/671/671-18.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "No person shall simultaneously hold more than one of the following offices: member of school board, school district moderator, school district treasurer, school district auditor, school district clerk, or budget committee member-at-large under RSA 32:15 ... Salaried positions shall include, but are not limited to, the following: teacher, custodian, administrator, secretary, school bus driver (if paid by the district), school lunch worker and teacher's aide." Before September 8, 2026 the rule barred a board member from also being moderator, treasurer or auditor. Raw: raw/money/rsa/toc-671.txt
3. When a NH school board seat is vacant, the remaining board fills it, and the appointee serves until the next district election, when voters elect someone for the rest of the term; if the whole board is vacant or the remaining members can't agree by majority, the town's selectmen appoint.
   - citation: RSA 671:33, II(a); RSA 197:26
   - source: https://gc.nh.gov/rsa/html/LXIII/671/671-33.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The school board shall fill vacancies occurring on the school board ... Appointees of the school board shall serve until the next district election when the voters of the district shall elect a replacement for the unexpired term. In the case of a vacancy of the entire membership of the school board, or if the remaining members are unable, by majority vote, to agree upon an appointment, the selectmen of the town or towns involved shall appoint members by majority vote in convention." A vacancy arising between the start of filing and the election is not filled by ballot until the next year's election (paragraph V). Raw: raw/money/rsa/toc-671.txt, toc-197.txt
4. If a NH school district elects no one to an office such as treasurer, the voters may elect a temporary officer or authorize the school board to appoint one "to serve until the next annual district election," and the board fills other district office vacancies the same way.
   - citation: RSA 671:6; RSA 671:33, II(a)
   - source: https://gc.nh.gov/rsa/html/LXIII/671/671-6.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: RSA 671:6 text: "The school district may, by vote, determine to elect a temporary officer or authorize the school board to appoint a temporary officer to serve until the next annual district election." RSA 671:33, II(a) covers "all other district offices for which no other method of filling a vacancy is provided." Clerk, moderator and treasurer may have 1-, 2- or 3-year terms by petitioned vote (RSA 671:6-a). Raw: raw/money/rsa/toc-671.txt

## money-statewide-education-property-tax: The Statewide Education Property Tax

- kind: how_it_works
- question_type: governance_money
- description: How the state education property tax (SWEPT) is set and where the money goes.

1. Before 2011, NH towns whose statewide education tax raised more than the cost of an adequate education for their pupils had to pay the excess to the state (the so-called "donor towns"); House Bill 337 (2011) amended RSA 76:8, II to end that, and its legislative history describes the purpose as to "[e]liminate[] donor towns by allowing excess property tax revenues raised in a town to be used by the town."
   - citation: Rand v. State, 2025 N.H. 27 (Bassett, J., dissenting in part), footnote 2, quoting RSA 76:8, II as amended by HB 337 (2011) and its legislative history
   - source: https://www.courts.nh.gov/sites/g/files/ehbemt471/files/documents/2025-06/2025027rand.pdf
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "RSA 76:8, II was amended by House Bill 337 in 2011 as follows: ... and, if there is an excess education tax payment due pursuant to RSA 198:46, directing them to assess the amount of the excess payment and pay it to the department of revenue administration for deposit in the education trust fund ... its legislative history demonstrates that its purpose was to '[e]liminate[] donor towns by allowing excess property tax revenues raised in a town to be used by the town.'" The majority upheld retention (library money-rand-case). Source URL as cited in the library topic money-rand-case; it returned HTTP 403 to an automated request today, so the text was read from the library's raw copy (raw/terms/courts/2025-NH-27-Rand-v-State.pdf). Raw: raw/money/state-data/2025-NH-27-Rand-v-State.pdf, .txt

## harts_location_school_budget: Hart's Location School District Budget, Tuition and SAU Share by Year

- unit: dollars
- period: fiscal years 2018-19 to 2026-27; year: the year the fiscal year ends
- source: Hart's Location School District annual reports 2020–2026 (proposed budget pages with actuals) and annual meeting minutes — https://drive.google.com/drive/folders/15lpWDx42NVWniWRH4jW_wASuB3zlpKpl
- as_of: 2026-11-13
- raw: raw/money/district/har-2020.ocr.txt … har-2026.rot90.txt, har-2021-p4.png, har-2023-p4-budget.png, har-2024-p4-budget.png (budget pages viewed)
- note: Value is the operating budget voted at the annual meeting, without the separate trust fund articles. Tuition and SAU columns are actual spending except where marked "budget." NH DOE's count of resident pupils for each year is in the site's data (adequacy_aid, Hart's Location district).

| Place | District id | Year | Value | Elementary tuition | High school tuition | Special education tuition | SAU 9 share | Note |
|---|---|---|---|---|---|---|---|---|
| Hart's Location | 236 | 2019 | 65178 | 22392 | 35219 | 0 | 3729 | |
| Hart's Location | 236 | 2020 | 32886 | 19153 | 0 | 2284 | 3336 | |
| Hart's Location | 236 | 2021 | 116245 | 65461 | 34961 | 42121 | 4051 | $32,348.41 drawn from the tuition trust |
| Hart's Location | 236 | 2022 | 168106 | 81264 | 36553 | 0 | 4235 | |
| Hart's Location | 236 | 2023 | 99253 | 27088 | 0 | 0 | 4803 | |
| Hart's Location | 236 | 2024 | 38497 | 26788 | 0 | 0 | 4341 | |
| Hart's Location | 236 | 2025 | 41508 | 27682 | 0 | 0 | 3788 | One student, grade 7 |
| Hart's Location | 236 | 2026 | 45097 | 34182 (budget) | 0 (budget) | 100 (budget) | 4098 (budget) | |
| Hart's Location | 236 | 2027 | 36650 | 0 (budget) | 21650 (budget) | 100 (budget) | 4521 (budget) | Fryeburg Academy student; mileage in $6,125 transportation |

## harts_location_trust_funds: Hart's Location School Trust Fund Balances as Reported

- unit: dollars
- period: March 2018 to February 2026; year: the year of the report
- source: Hart's Location annual meeting and board minutes (2018–2026); Town of Hart's Location 2025 Annual Report, trustees' report — https://hartslocation.com/wp-content/uploads/2026/03/2025-Annual-Town-School-Reports_Digital-Version.pdf
- as_of: 2026-11-13
- raw: raw/money/district/har-2019.ocr.txt, har-2020.ocr.txt, har-2021.ocr.txt, har-2023.txt, har-2024.txt, har-2025.txt, hsb-2025-01-14.txt, hsb-2026-02-10.txt; raw/money/town/town-annual-report-2025-p27-30.ocr.txt
- note: Value is the balance as stated by SAU 9 at a meeting or by the trustees. Spoken figures are rounded ("approximately") and may not include deposits voted but not yet made (in March 2025 the clerk noted the prior year's deposits had not been made by year's end).

| Place | Fund | Year | Value | Date and source |
|---|---|---|---|---|
| Hart's Location | Special education fund | 2018 | 38000 | March 13, 2018 meeting ("Approximately $38,000") |
| Hart's Location | Special education fund | 2019 | 39900 | March 12, 2019 meeting |
| Hart's Location | Special education fund | 2020 | 43970 | March 10, 2020 meeting |
| Hart's Location | Special education fund | 2022 | 55016 | March 8, 2022 meeting |
| Hart's Location | Special education fund | 2023 | 63036.28 | March 28, 2023 meeting |
| Hart's Location | Special education fund | 2025 | 81143.09 | December 31, 2025, trustees' report |
| Hart's Location | Special education fund | 2026 | 89126 | February 10, 2026 hearing |
| Hart's Location | Tuition trust | 2019 | 85600 | March 12, 2019 meeting |
| Hart's Location | Tuition trust | 2024 | 75000 | March 12, 2024 meeting ("approximately") |
| Hart's Location | Tuition trust | 2025 | 79547.14 | December 31, 2025, trustees' report |

## harts_location_federal_land_payments: Federal Land Payments: PILT to the Town and Forest Receipts to the School District

- unit: dollars
- period: federal fiscal years 2022–2026 (PILT); school fiscal years 2021–2025 (forest receipts); year: the fiscal year
- source: US Department of the Interior, PILT "Payments and Acreage By State / County," New Hampshire — https://pilt.doi.gov/counties.cfm ; site data (DOE-25 revenue account 4810, Hart's Location)
- as_of: 2026-11-13
- raw: raw/money/federal/pilt-nh-fy2022.txt … pilt-nh-fy2026.txt; raw/money/state-data/site-db-harts-queries.txt
- note: Value is the PILT payment to the Town of Hart's Location for 5,395 acres (all Forest Service). National forest receipts are the "Federal Forest Reserve" revenue in the school district's DOE-25. The two programs use different fiscal years, so a row's two figures are not the same 12 months.

| Place | Town id | Year | Value | PILT acres | Forest receipts to school district |
|---|---|---|---|---|---|
| Hart's Location | 236 | 2021 | | | 2637.39 |
| Hart's Location | 236 | 2022 | 8897 | 5395 | 2308.42 |
| Hart's Location | 236 | 2023 | 14196 | 5395 | 2591.79 |
| Hart's Location | 236 | 2024 | 14185 | 5395 | 2548.04 |
| Hart's Location | 236 | 2025 | 14886 | 5395 | 5579.72 |
| Hart's Location | 236 | 2026 | 15277 | 5395 | |

## harts_location_tuition_per_pupil_comparison: Tuition per Student Paid by SAU 9 Sending Districts (Derived)

- unit: dollars
- period: 2022-23 to 2027-28; year: the year the school year ends
- source: Hart's Location annual reports (tuition lines and student counts); Jackson file tables jackson_ms_tuition_budget_line and jackson_hs_tuition_per_pupil; site data (Bartlett cost per pupil) — https://drive.google.com/drive/folders/15lpWDx42NVWniWRH4jW_wASuB3zlpKpl
- as_of: 2026-11-13
- raw: raw/money/district/har-2024-p4-budget.png, har-2025.txt, har-2026.rot90.txt; town/Jackson/money-and-governance.md (tables)
- note: **Derived**: tuition line ÷ students, where the minutes give the count. Bartlett's official per-pupil rates (the yearly contract "riders") are not posted. Budget figures are what a board planned, not what was billed. Excludes transportation and special education. Bartlett's DOE cost per pupil is shown for context; it is not a tuition rate.

| Place | Year | Value | Note |
|---|---|---|---|
| Hart's Location, K–8 at JBES (Bartlett) | 2023 | 27088 | Actual, one elementary student |
| Hart's Location, K–8 at JBES (Bartlett) | 2024 | 26788 | Actual, one student |
| Hart's Location, K–8 at JBES (Bartlett) | 2025 | 27682 | Actual, one student in grade 7 |
| Hart's Location, K–8 at JBES (Bartlett) | 2026 | 34182 | Budget, one student |
| Jackson, grades 7–8 at JBES (Bartlett) | 2027 | 32000 | Budget $384,000 for 12 students (Jackson file) |
| Hart's Location, Fryeburg Academy | 2027 | 21650 | Budget line, one student (tuition only) |
| Jackson, Kennett High (current contract) | 2027 | 38603 | Board comparison, maintenance included (Jackson file) |
| Fryeburg Academy, published commuter day tuition | 2028 | 22500 | Fryeburg's posted 2027-28 rate (Jackson file) |
| Bartlett School District, NH DOE cost per pupil (context) | 2025 | 31530 | Site data; not a tuition rate |

## For another file

- **Schools agent (schools-and-getting-there):**
  - March 2022 minutes: students near Bartlett bus routes ride free; families outside the range drive and are paid mileage (raw/money/district/har-2023.txt).
  - 2016 minutes: the Kennett bus came "to end of Brandon's driveway for $500.00" (raw/money/district/har-2017.ocr.txt).
  - Policy DK, mileage for out-of-district special education placements (raw/money/policies/harts-policy-DK.txt).
  - The 2026-27 budget includes no elementary tuition, which suggests no Hart's Location K–8 student at JBES this year. Worth checking against JBES enrollment.
- **Community agent (community-and-families):**
  - PILT acres: 5,395, all Forest Service (raw/money/federal/pilt-nh-agency-fy2026.txt).
  - The town site gives a population of 43.
  - Attendance: 11 attendees besides officials and SAU staff at the March 10, 2026 school district meeting; 16 ballots at the March 11, 2025 town meeting (raw/money/town/town-annual-report-2025.txt).
  - The site's EFA data shows no Hart's Location students for 2022–2027.
  - SAU 9's residency attestation link is broken.
- **Bartlett file, district-tuition-contracts fact 15:**
  - It gives the special education reserve as "$89,126 in February 2026" (SAU 9 at the hearing). The town trustees report $81,143.09 at December 31, 2025 and list both school funds as expendable trusts created in 1992.
  - January 2010 minutes say the tuition trust was "created for that purpose in 2003." The sources differ; both are recorded here.
- **Bartlett file, district-board-and-public-input fact 8:** Stacy Dunat was re-elected in March 2026; SAU 9 now shows her term ending 2029.
- **Jackson file, jackson_sau9_board_seats_and_votes:** Hart's Location's weighted votes can be computed. With 1 resident pupil (fewer than 8), it has 0 weighted votes (**derived**; district-sau-governance fact 4).
- **SAU 9 page:** the Hart's Location board page still shows the old "second Tuesday of every other month" schedule. The board moved to quarterly Wednesdays in April 2026.
- **Library (`additional-data`):** no topic yet covers RSA 193:12's domicile and custody rules, PILT and national forest receipts, or elderly and low-income tax relief. Three new shared topics are proposed in the summary.

## Not retrieved

- https://drive.google.com/file/d/1U9KmEYmK5BZTCqjneLjKkJscCPjtCts-/view (SAU 9 "Annual Residency Verification Attestation"): HTTP 404 by direct and view URL.
- https://sau9.powerschool.com/public/formbuilder/form.html?formid=4381149 (SAU 9 student registration): a script-driven form; no list of residency documents could be read.
- Bartlett's yearly tuition calculation "riders" for Hart's Location: not in the posted contract or any Hart's Location annual report (2017–2026).
- The original (pre-2009) Bartlett–Hart's Location contract that the June 9, 2009 minutes "amended": not found in the Drive folders.
- Town of Hart's Location MS-1 (exemptions) and any vote adopting an elderly exemption under RSA 72:39-b: not in the 2025 town report text. DRA's municipal report pages were not tried, since other agents got HTTP 403 there. The 2024 town report (https://hartslocation.com/2024-AnnualReport.pdf) is scanned and was not OCR'd.
- 2026 tax rate for Hart's Location: not yet set by DRA as of November 13, 2026.
- Hart's Location School Board minutes for 2011–2023 and 2015–2019 agendas: listed in the Drive folders but not read. They may hold more history on high school choice, Fryeburg and new students.
- Whether NH catastrophic aid (RSA 186-C:18) counts special education transportation: not checked in Ed 1100 or DOE guidance.
- Whether EFA students are counted in a district's resident ADM for adequacy: not checked (RSA 194-F).
- Profile School District (SAU 35) policy on tuition students and drive times from Crawford Notch to Bethlehem: not searched; the drive times belong to the schools agent.
- A Hart's Location MOU or agreement with Fryeburg Academy for 2026-27: not found in minutes, warrants or reports. Fryeburg's 2026-27 commuter day rate is no longer posted (Jackson file).
