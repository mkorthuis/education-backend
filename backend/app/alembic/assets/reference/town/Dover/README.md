# Dover: Research for Ask NH Education Facts

Cited facts and figures for answering Dover, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 30 resident profiles with 3 questions each, numbered P1.1 to P30.3 in `questions.md`; the people are invented. The research is in the seven files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Salem, Rochester and Merrimack. Dover is SAU 11: three elementary schools (Garrison, Horne Street and Woodman Park, K–4), Dover Middle School (grades 5–8), Dover High School with the Dover Regional Career Technical Center, and the Dover Adult Learning Center. Barrington and Nottingham send their high school students to Dover High by tuition contract, and Strafford has a small per-student agreement. Seacoast Charter School is in Dover. The city council sets the school budget under the charter's tax cap.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | The June 2026 capacity report (no room for more classrooms; special education "over capacity"), Garrison's falling enrollment, class-size policy IIB and the withdrawn first-grade cap, Title I at Woodman Park, English learner services at Horne Street, the preschool lottery, summer tutoring in place of summer school | 8 | 62 | 4 | `raw/elementary/` (41 MB) |
| `middle-school-and-staff.md` | Teams in grades 5–8, accelerated math expanded to grades 6 and 7, high school credit in grades 7–8, the substitute shortage and 47 vacancies, paraeducator pay ($17.76 an hour for a new instructional para), the staff survey, UFLI reading intervention | 9 | 59 | 2 | `raw/middle/` (25 MB) |
| `high-school-and-ctc.md` | The CTC's 19 programs and the shared Tri-City application, credentials and college credit, paid work-based learning, the evening electrical apprenticeship, AP and dual enrollment counts, NJROTC, the social studies credit, UNH admission | 8 | 72 | 2 | `raw/high/` (10 MB) |
| `choices-and-adult-learning.md` | The Adult Learning Center (hours, HiSET, the counselor moved into the district budget), Seacoast Charter's lottery and sibling priority, Saint Mary Academy's planned move to Somersworth and its tuition, policy JJJ's access for private, charter and home-educated students, the EFA policy, Title I at private schools | 8 | 62 | 0 | `raw/choices/` (31 MB) |
| `student-support-and-life.md` | Counselors by school (about 177 to 235 students each), social workers and psychologists, the all-day phone ban, bullying timelines, fights and the SRO, religious holidays and chronic absence, military families, translation, the parent portal | 8 | 98 | 1 | `raw/support/` (23 MB) |
| `getting-to-school-and-zones.md` | 22 buses and 41 runs, the bell schedule they set, the free bus to Seacoast Charter, St. Thomas Aquinas's own bus, Tolend Road on Woodman Park's route, YMCA and Seymour Osman after-school care, bus contract rates, the capital plan's road projects | 5 | 67 | 3 | `raw/daily/` (29 MB) |
| `money-buildings-and-governance.md` | The tax cap formula, how the FY2027 budget came in under it (downtown TIF money), overrides in 9 of 18 years, Question 2 in Dover, special education transportation, the settled contracts, the capital plan (Garrison, Woodman Park, the middle school's geothermal system), tax-bill math, rents, housing and enrollment | 7 | 77 | 4 | `raw/money/` (32 MB) |
| **Total** | | **53** | **497** | **16** | **191 MB** |

`brief.md` is the brief the research agents worked from. Seven agents used about 3.3 million tokens.

## Checks

- **Parser:** all seven files pass the backend's parser (`tools/check_town.sh Dover`). Every table is linked to a topic.
- **Topics:** two new topics were reviewed and added to `../shared-topics.md`: `college-admission-requirements-nh` (retitled "Admission Requirements at New Hampshire's Public Colleges", since it isn't only UNH's) and `research-housing-and-school-enrollment`.
- **Places:** `district Dover` 434, `town Dover` 31, no place 12, `district Seacoast Charter School` 9, `district Diocese of Manchester` 5, `district Portsmouth Christian Academy` 4, `town Durham` 1, `town Portsmouth` 1.
- **Places for the backend:** Dover's rows for Barrington and Nottingham (`places.yaml`) match what the agents found. A row was added for Strafford to Dover (grades 9–12), from the capacity report's "limited 10 student per year agreement with Strafford (on a per student basis)"; the agreement and its dates aren't posted. Uncommitted.
- **Duplicate removed:** the choices file's CTE enrollment policy fact repeated `high-school-and-ctc.md` `cte-center-programs` 4–6, so it was removed and its references point there.
- **Draft facts:** two notes are flagged.
- **Raw folders:** all under 100 MB.
- **Spot checks:** each agent checked 3 or more facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | The School Board's budget $1,976,767 over the school share of the cap | Dover School Department release on the adopted FY2027 budget |
  | The council's FY2027 budget, 9–0, $140,161 under the cap after moving $1,831,515 of downtown TIF money | City release; council minutes, April 1, 2026 |
  | Special education transportation $3,723,291, up $527,821 (16.52%) | FY2027 budget book, November 24, 2025 |
  | A new instructional paraeducator: $16.73 (2023–26) to $17.76 an hour | 2023–2026 paraeducator contract; CFO memo, September 10, 2026 |
  | Adult Learning Center: $438,892, up 53% | Budget workshop slides, January 6, 2026, p. 14 |
  | Seacoast Charter bus: first stop 7:28, at school 8:20, leaves 3:20 | Route sheet, October 2025 |
  | CTC applications: March 1 priority date, March 5, 2026 deadline | CTC "How to Apply" page; Dover High counseling page |
  | Garrison: 476 students (2015-16) to 353 (2024-25) | The site's school enrollment |

## Premises checked

| Question says | What the sources show |
|---|---|
| The budget is "past the tax cap by almost $2 million" (P2.1) | Partly: the School Board's budget was $1,976,767 over the school share; the council's final budget was $140,161 under the cap after moving $1,831,515 of downtown TIF money to the schools, so no override vote was needed. Overrides passed in 9 of the 18 years FY2009–FY2026 |
| Special education transportation up "over half a million" (P6.1) | Correct: up $527,821, mostly for out-of-district placements, including $400,000 to cover the FY2026 overrun |
| Three union contracts being negotiated at once (P6.2) | Out of date: all three are settled |
| What the November tax cap ballot question changed (P10.2) | Nothing in Dover: Question 2 got 52.5% yes, short of the 60% needed |
| Bond projects coming (P10.3) | Correct: the middle school's geothermal heating and cooling, $900,000 for Woodman Park and $16.5 million for Garrison are in the city's proposed capital plan |
| "Each new apartment unit only adds 0.25 kids" (P28.2) | Misattributed: 0.25 is a 2024 NH Housing study's average for four case-study towns; for housing built 2014–2023, apartments averaged 0.06 students per unit |
| Dover High "holding up" (P28.3) | The building is new, occupied in 2018 |
| The Adult Learning Center's counselor "losing grant funding" (P12.1) | Partly: the position was grant-funded and moved into the FY2027 district budget because of state and federal cuts |
| Evening electrician and plumbing classes at Dover High (P12.3, P30.2) | Right in substance: the Dover School of Technology's evening apprenticeship classes at the CTC, for registered apprentices, $1,450 a year; whether a plumbing class runs in 2026-27 wasn't found |
| Tri-City CTE with Somersworth and Rochester (P25.1, P30.1) | Right: one shared application for the three centers |
| Robotics, pre-engineering and networking (P18.1) | Pre-Engineering (Project Lead the Way) and Computer Networking and Cyber Security are CTC programs; there's no robotics team, and robotics is taught inside courses |
| Health Science and EMT, Biomedical Science, Culinary Arts, Building Construction, NJROTC (P5.1, P7, P14.3, P16.2, P27.1) | All exist |
| Machining at Dover's CTC (P2.2) | Dover has welding but no machining; Precision Machining is at Rochester, open to Dover students through Tri-City |
| UNH dual enrollment at Dover High (P3.3) | Great Bay credit is offered; no UNH course is listed |
| "The new extra social studies credit" (P7.2) | Applies from the class of 2030; a current junior needs 2.5 credits |
| Families file an "annual homeschool evaluation" (P22.2) | Out of date: repealed July 1, 2026; Dover's posted policy IHBG and intent form still describe it |
| Siblings get priority in Seacoast Charter's lottery (P13.1) | Right, if they apply by the sibling deadline (February 5, 2027 for 2027-28) |
| No bus to Seacoast Charter on Watson Road (P13.2) | Wrong: Dover buses Dover residents there at no cost |
| Saint Mary Academy moving to a campus with St. Ignatius (P20.1) | Right: planned on the St. Ignatius parish campus in Somersworth, opening in 2028 if completed as planned; a $20 million project with a $15 million anonymous gift |
| EFA money comes from Dover property taxes (P9.3) | From the state's education trust fund |
| Team-based learning in grades 5–6 (P29.2) | Right: teams in every grade, 5 through 8 |
| High school algebra in middle school (P3.1) | Partly: policy IMBD allows high school credit in grades 7–8, but no school source names Algebra I in grade 8 |
| Hard to keep paraeducators and substitutes (P21.1) | Partly: the district says it "does not always have enough substitutes"; no turnover data exists |
| Orton-Gillingham mostly in elementary (P26.1) | No source names Orton-Gillingham training at any level |
| A homework jump from grade 5 to 6 (P3.2) | No source measures it |
| Garrison crowded by new housing (P1.1) | Not borne out: Garrison fell from 476 to 353 students (2015-16 to 2024-25) and is projected at 309 for 2026-27 |
| Pre-K only for special education (P8.1) | Partly: built around special education, but some other children are admitted by lottery, for tuition |
| Free summer school (P11.3) | No elementary summer school; the district replaced it with one-on-one tutoring |
| K–4 class sizes capped (P24.3) | Correct; a separate 20-student first-grade cap was withdrawn April 13, 2026 |
| All three elementary schools merge in grade 5 (P29.1) | Correct |
| Tolend Road in Garrison's zone (P24.1) | Not supported: on the 2026-27 route sheet its elementary stops are on Woodman Park's route; no zone map is published |
| Elementary redistricting (P8.3) | No proposal in board minutes from January 2025 to November 2026; the last found was 2007 |
| A bus to St. Thomas Aquinas (P9.1) | Dover runs none; the school runs its own free morning bus with a Dover stop, and no afternoon bus |
| A late bus (P5.2, P17.2) | None found, though the bus contract prices one ($146 a bus a day) |
| Everything on ParentSquare (P17.3) | Dover doesn't use it: Infinite Campus and weekly family emails |
| A "Town Square commons" and open campus (P18.3) | "Town Square" is the cafeteria; no grade has an open campus |
| Military Family Life Counselors (P27.3) | None named; policy JFAM promises licensed counseling, and Dover High lists a regional military school liaison |

## Corrections and additions to earlier files

None to earlier towns. (Rochester's later research added a note to this town's `high-school-and-ctc.md` `cte-center-programs` 14: Rochester's own catalog starts Precision Machining in grade 11, not 10–11.) The choices agent compared Dover's policy JJJ with Nashua's IHBG-R on related services for private, charter and home-educated students: Nashua's says such requests "shall generally be denied", while Dover's sends them to the Director of Student Services. That's a local difference, not an error.

## Coverage

39 questions are answered **fully**, 50 **partly** and 1 by the site's data alone; none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Maya & Devon Brooks | **full** | **full** | **full** |
| P2 Tom Callahan | **full** | partial | **full** |
| P3 Priya Nair | partial | partial | **full** |
| P4 Carlos & Elena Mendoza | partial | partial | partial |
| P5 Rachelle Pelletier | partial | partial | **full** |
| P6 Greg & Hannah O'Connor | partial | partial | **full** |
| P7 Liam Murphy | **full** | **full** | partial |
| P8 Amina Hassan | **full** | data only | partial |
| P9 Bradford & Diane Vance | **full** | **full** | **full** |
| P10 Kevin Cho | partial | **full** | **full** |
| P11 Brenda Kowalski | partial | partial | partial |
| P12 Jordan Alvarez | **full** | partial | partial |
| P13 Stephanie & Mark Boucher | **full** | **full** | partial |
| P14 Dr. Samira Patel | **full** | **full** | **full** |
| P15 Tyler Gagnon | **full** | partial | partial |
| P16 Claire Beaumont | **full** | **full** | **full** |
| P17 Nolan & Tessa Reed | partial | partial | **full** |
| P18 Marcus & Kayla Washington | partial | **full** | **full** |
| P19 Elizabeth "Betty" Morin | **full** | partial | partial |
| P20 Owen & Meg Sullivan | **full** | partial | partial |
| P21 Zackary Pierce | partial | partial | partial |
| P22 Denise & Paul Desjardins | **full** | **full** | **full** |
| P23 Fatima Al-Mansoor | partial | **full** | partial |
| P24 Connor & Brianna Doyle | partial | partial | **full** |
| P25 Sandra Lin | **full** | partial | partial |
| P26 Derrick Cole | partial | partial | partial |
| P27 Jenna & Luke Kowalczyk | partial | partial | partial |
| P28 Arthur "Artie" Bellavance | partial | **full** | partial |
| P29 Keiko Tanaka | partial | **full** | partial |
| P30 Isaiah Bennett | partial | partial | partial |

## Notable findings

- **The tax cap:** the School Board's FY2027 budget was almost $2 million over the school share, but the council brought the whole budget under the cap by moving downtown TIF money to the schools. A $100,000 change in the school budget is about $8 on the average tax bill.
- **Capacity:** the June 2026 capacity report says the elementary schools have no room for more classrooms and special education staffing is "over capacity", and recommends taking no students beyond the tuition towns.
- **Staffing:** 47 vacancies in September 2025 (20 filled through agencies), an agreement paying teachers who absorb uncovered classes, and "Feedback & Coaching" the lowest-rated area (27%) in the 2026 staff survey.
- **The CTC:** 19 programs, one Tri-City application (priority date March 1), seats given by sending school allocations. Work-based learning is usually paid; internships aren't.
- **Housing and enrollment:** apartments built in four case-study towns, Dover among them, from 2014 to 2023 averaged 0.06 public school students per unit.

## Browser pass, November 15, 2026

Added from pages that refused automated requests, read in Chrome: the city charter's tax cap (Section C6-3.1, on ecode360), as `money-buildings-and-governance.md` district-tax-and-state-aid 15. Dover now has 498 facts. Not reachable: NH DOE's district special education reports (the page no longer exists while NH DOE moves to a new website), NH DRA's 2026 tax rates (a PDF on a blocked site; Chrome's PDF viewer can't be read).

## Gaps to retry

- **Blocked to automated requests (for the browser pass):**
  - NH DOE: special education public reporting (Dover's IEP timeliness and parent survey), the 21st Century program page, and the technical advisory on access to curricular and co-curricular programs;
  - the Dover city charter on ecode360 (the tax cap text), NH DRA's tax rate page, the city's 2026 news index;
  - the Navy's NJROTC page, the state electricians' board apprenticeship page, St. Ignatius parish's site;
  - the Seymour Osman Community Center's listing and its 2026 job posting (the agent fetched the job posting a second way after the block, against the brief, and didn't cite it).
- **Behind a sign-in or script:** the Title I plans and compacts on Google Drive, the Tri-City application, Dover's board minutes before February 2026 (each meeting's documents open through JavaScript), menus.
- **Not found anywhere:** CTC applicant and credential counts, partner employers, NJROTC unit size, rider counts, a late bus, a zone map, the Seymour Osman program's fee, paraeducator and substitute turnover, the middle school's world language and how accelerated math students are chosen, the district communication plan, the 2026 tax rate (not certified yet).
