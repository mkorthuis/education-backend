# New Durham: Research for Ask NH Education Facts

Cited facts and figures for answering New Durham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch, after the Wolfeboro and Ossipee research on the same district. New Durham is in the Governor Wentworth Regional School District (GWRSD, SAU 49), a six-town district (Brookfield, Effingham, New Durham, Ossipee, Tuftonboro and Wolfeboro):
- **New Durham School** (preschool to grade 6; 150 students on October 1, 2025, 13 of them preschoolers), the district's only school in town;
- **Kingswood Regional Middle School** (grades 7–8) and **Kingswood Regional High School** (grades 9–12, 703 students), both in Wolfeboro, and the Lakes Region Technology Center (LRTC) there.

Wolfeboro's and Ossipee's files cover the district's shared schools, policies and money; these files cite them and write New Durham's side. Tuftonboro's research follows in the same batch.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `new-durham-elementary-and-families.md` | No before- or after-school care at the school (the one licensed program, Being Kool After School and Preschool, is about 0.3 mile away; pickup from the school not posted), an integrated preschool for children with disabilities with a few places for other children, GWRSD posting no bus routes or times, the Stopfinder pilot on five routes, a grade 5 teaching position cut for FY2027 ($94,986), reading about half below grade level in fall assessments, no summer meal site in New Durham, nearest infant child care 8 to 15 miles away | 17 | 55 | 3 | 3.7 MB |
| `new-durham-grades-3-6-and-kingswood-middle.md` | New Durham School's 2026 results (57% proficient in reading and 60% in math against 55% and 44% for the state, with 20–25 tested students per grade), the district's own nurses since July 1, 2026 (seven full-time, two half-time), Infinite Campus and bus colors, the March 31, 2026 sixth-grade parent night at Kingswood Middle, one calendar for all schools, phones off from first bell to dismissal (JICJ), 17 New Durham seventh graders at Kingswood Middle in 2025-26 | 15 | 57 | 3 | 12 MB |
| `kingswood-high-from-new-durham.md` | LRTC programs starting in grade 10 at the earliest and priority for grades 11–12, a Nurse Assisting option (106 hours, grades 11–12, needs Health Science I first), a late bus at 5:00 p.m. Monday to Thursday with a pass (the New Durham stop isn't named), no New Durham pickup time published, Kingswood Academy (new in 2026), 15 Early College courses taught in the Kingswood day, 2023-24 dual enrollment of 5.8 per 100 students against a state median of 10.45, four counselors and a social worker for 703 students | 11 | 40 | 4 | 8.8 MB |
| `money-and-governance.md` | The "$8.8 million" on the state's rate sheet ($8,881,609 of net cooperative school appropriations, New Durham's share of the district's budget, not a separate budget), school taxes up 46.3% from 2014 to 2025 while resident students fell 27.1%, the November 3, 2026 tax cap vote (New Durham 1,080 to 414; the six towns 65.2%), designated volunteer drivers (policies EEBA and EEAG), the Health Services function $465,240.84 over budget once committed money is counted, New Durham's 1 of 9 board seats against 16.5% of the students | 9 | 49 | 6 | 69 MB |
| **Total** | | **52** | **201** | **16** | **94 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.2 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus New Durham. All 16 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 36 partial.
- **Topics:** no new topics.
- **Places:** `district Governor Wentworth Regional` 149, `town New Durham` 45, no place 6, `district Farmington` 1.
- **Pending facts:** 1: the town report prints the MS-1 stamped "DRAFT NOT FINALIZED/SUBMITTED"; the fact's note explains that its net valuation matches the state's final rate sheet.
- **Raw folders:** each under 100 MB (the money folder is 69 MB). The 67 saved PDFs are handbooks, policies, budget and financial reports, election results, the town's capital plan and the district's staff request sheet; none is a route sheet or a roster. GWRSD posts no bus routes. The town's 2025 annual report is kept only as cleaned page extracts, because the full report lists residents by name.
- **Privacy:** the address scan finds only Town Hall (4 Main St.), New Durham School, and Kingswood Regional Middle School's address in the LRTC handbook. A student representative's name was removed from the October 5, 2026 board minutes. Staff directory copies keep titles only.
- **Quotes:** 387 of 483 quoted passages found word for word in the raw copies (the misses are mostly table text read from page images and the agents' own wording; the figures I searched for are all in the raw copies).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | New Durham's cap vote of 1,080 to 414 (72.3%), and the six towns' 6,629 to 3,541 (65.2%) | The site's `town_question_two` table (sum of the six towns) |
  | The Health Services function "over budget by $465,240.84 once committed money is counted" | The October 2026 financial report: budget $568,233.21, spent $263,601.56, encumbered $769,872.49 |
  | School taxes (local plus state) up 46.3% from $5,611,459 (2014) to $8,210,189 (2025), and resident students from 395 (2014-15) to 288 (2025-26), down 27.1% | The site's `town_school_tax` ($7,313,652 local in 2025, plus the $896,537 state tax on the rate sheet) and `town_enrollment` tables |
  | $8,881,609 of net cooperative school appropriations | The town's 2025 report extract of the state tax rate sheet |
  | The grade 5 teaching position cut of $94,986 | The FY2027 new staff request sheet |

## Premises checked

| Question says | What the sources show |
|---|---|
| Reliable care right at New Durham School (P1.1) | None at the school; the earliest arrival is 8:15 a.m.; After-School Clubs for grades 1–6 are not care |
| The elementary bus time and ride length on Birch Hill can be found (P1.2) | Not published; a drive from two points on Birch Hill Road to the school is 2.1 and 4.7 miles (4.9 and 10.5 minutes, derived), and a bus takes longer |
| Not enough interventionists for first-grade reading (P1.3) | One reading specialist is listed; the 2025 principal's report said about half of students were below grade level in fall reading |
| A public pre-K a family can get into (P4.1) | Partly: an integrated preschool set up for children with disabilities, with a few other children on a space-available waiting list and a monthly tuition not posted |
| Kindergarten may be half-day (P4.3) | One school day, 8:45 a.m. to 3:15 p.m.; no town day camp found |
| Speech and OT shared with Wolfeboro (P5.1) | Not shown: NDS has its own OT and a "Speech and DPT" |
| Free summer meals nearby (P5.3) | None in New Durham on the county's 2026 list; the sites are in Farmington, Barrington, Rochester and farther |
| A Stopfinder bus app is being piloted (P12.2) | Yes, invitation-only on five routes; whether any is a New Durham route isn't stated |
| "A school of under 150 kids" (P19.2) | About right: 150 on October 1, 2025 including 13 preschoolers (137 in K–6); the 2026 principal's report says 153 |
| Infinite Campus and "bus colors" (P10.3) | Both exist; no page says the bus or stop shows in Infinite Campus |
| The same calendar as Kingswood (P13.3) | Yes: one 2026-27 calendar covers all schools |
| Phones locked up all day or texting in class (P20.2) | Neither: off and in a locker, backpack or bag from first bell to dismissal; Kingswood Middle holds a phone for a period after a first offense |
| A late bus after sports or clubs (P6.1) | One at 5:00 p.m. Monday to Thursday with a pass, to "central locations" in each of the six towns; the New Durham stop isn't named |
| "Running Start" classes (P9.1) | The program is now Early College At Your High School; 15 courses are taught in the Kingswood day |
| LRTC health science is enough for an LNA license before graduation (P9.2) | Nearly: Nurse Assisting is a Board of Nursing–approved 106-hour course, grades 11–12, after Health Science I, with the license a separate application |
| A 9th grader can start culinary or graphic design at the tech center (P13.1) | No: Culinary Arts I is grades 10–11 and Graphic Design I grades 11–12 |
| A school tax cap is "on the ballot" (P3.2) | Already decided: November 3, 2026; New Durham 72.3% yes, the district 65.2% (unofficial); the cap needs 60% and applies from the 2027-28 budget |
| "$8.8 million" school appropriation, how much reaches the classroom (P8.2) | New Durham's share of the district's net budget before state aid, not a separate budget; no source splits it between classrooms and central office |
| A $600,000 nurse salary overage after the district said in-house nursing would save money (P8.1) | No such figure in the posted papers; the Health Services function is $465,240.84 over budget with committed money counted, and no reason is posted |
| Designated volunteers driving students (P6.2) | Policy EEBA covers them (adoption line November 2, 2026); EEAG requires written authorization and $500,000 of coverage for private vehicles carrying students |
| New Durham's voting power on the board | 1 of 9 seats (11.1%) against 16.5% of students; its voters would have changed the outcome of one of 28 results since 2023 (the 2025 budget, failed by 9 votes; derived) |

## Corrections and additions to earlier files

None applied; nothing found contradicts earlier files. Additions for others:
- **Ossipee `money-and-governance.md`, district-tax-and-state-aid 1:** the state handout's allocated amounts don't add to its printed net local assessment for any town (Ossipee: $2,709,116 + $13,851,958 − $2,254,380 − $1,642,969 = $12,663,725, against $12,709,764 printed; New Durham's gap is $24,093 and Wolfeboro's $70,669). The sheet has an adjustments column that is blank or unreadable in the image; the printed totals add exactly across the six towns ($51,364,715). The facts there are as printed.
- **Ossipee `support-and-choices.md`, school-programs-after-grade-6 6:** it found no spring visit for Ossipee Central's sixth graders; New Durham's calendar has a sixth-grade field trip (March 20), a parent night at Kingswood Middle (March 31) and "Bridges Day" (June 8), which may mean the same events exist for Ossipee but weren't posted.
- **Ossipee `kingswood-from-ossipee.md` and Wolfeboro cte-center-programs 5:** the Kingswood catalog's Graphic Design I prerequisites differ between its business listing (page 27, "None") and its LRTC section (page 80, Office Software Applications and Desktop Publishing).
- **Ossipee's `money-and-governance.md` note on the October 5, 2026 superintendent's report:** a $494,000 three-year grant request for expanded after-school transportation for outlying towns' elementary students; winners were to be announced at the end of October 2026 and not checked here.
- **Wolfeboro `district-tax-and-state-aid` 5 and `district-facilities-and-capital` 9:** consistent with this research (the district's projected adequacy grant for New Durham is $420,079; NH DOE's November 2025 estimate in the site's data is $507,877).

## Library notes (for review, not applied)

- **`district-practices.md`** has no entry in its kindergarten-day table for Governor Wentworth; kindergarten-day-length 1 here supplies one.

## Browser pass

Not done. Not retrieved:
- Stopfinder's page and an NH DOE page (HTTP 403), Transfinder (sign-in), the state labor board's contract copies (refused automated requests), Parks and Recreation Commission minutes kept in Google Drive, and the November 2, 2026 board minutes (not posted);
- bus routes, stop locations, ride times and whether any New Durham route is in the Stopfinder pilot, preschool days, hours and tuition, full-time status or caseloads for speech, OT and reading staff, the October 1, 2026 count by grade, any agreement between Parks and Recreation and the school for gym use, the paraprofessional wage scale, a teacher turnover rate, the district's formation papers and articles of agreement, any New Durham withdrawal study, the town's March 10, 2026 ballot results and its tax year 2026 rate, and why Health Services is over budget (not found).
