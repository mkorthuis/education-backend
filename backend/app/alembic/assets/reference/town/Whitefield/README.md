# Whitefield: Research for Ask NH Education Facts

Cited facts and figures for answering Whitefield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the third ToLoad batch, after Lancaster's research on the same district. Whitefield is in the White Mountains Regional School District (SAU 36), a five-town district (Carroll, Dalton, Jefferson, Lancaster and Whitefield):
- **Whitefield Elementary School** (preschool to grade 6) is in Whitefield; grades 7 and 8 moved to the **White Mountains Regional Middle High School** on Regional Road in Whitefield on July 1, 2026;
- the Paradice career center is inside the high school, with White Mountains Community College (Early College) and the Gallen center in Littleton nearby.

The district-wide research (the high school, student life and the district's money) is in `../Lancaster/`; these files cite it and write Whitefield's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `whitefield-elementary-and-families.md` | The Town's ASAP after-school program (K–6, 2:15–6:00, $10 a day, a bus from the school, a sliding fee on request), two-hour-delay texts posted 5:09–5:55 a.m. (median about 5:32; opt in at registration), preschool Monday–Thursday with 8 seats for new students, grade 3 reading 44% (state 51%; 17% in 2022), 0.65 of a speech pathologist and one counselor (down from two), half-time music | 19 | 91 | 6 | 4.7 MB |
| `whitefield-grades-6-8-and-regional-road.md` | Seventh and eighth graders on the high school's start and end times but their own block schedule, bus rides 10–14 minutes longer than an elementary rider's, a closed campus for grades 7–12 from 2026-27, current vaping 18.8% against 15.6% in NH (high school survey), one English learner teacher for the district, PowerSchool replaced by Alma | 10 | 62 | 5 | 0.2 MB |
| `white-mountains-regional-from-whitefield.md` | Eight AP courses authorized in 2025-26 and 2026-27 (College Board ledger; no online AP provider), grade 11 math 15% proficient (state 31%), only a half-credit welding intro and no diesel, two free Early College courses a year, most WMCC sections online, Coos Adult Education closed in fall 2024 (Above the Notch serves Whitefield) | 9 | 51 | 4 | 3.4 MB |
| `money-and-governance.md` | School taxes up 45.3% from 2018 to 2025 ($2.55 million to $3.71 million) while resident students fell 16.4%, the 7–8 move (about $1.7 million saved either way; approved unanimously June 18, 2025), teacher departures of 9, 18 and 8 in the last three years, board meetings in other towns at 5 of 21 meetings in 2024-25 | 16 | 48 | 7 | 0.3 MB |
| **Total** | | **54** | **252** | **22** | **8 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.8 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Whitefield. All 22 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 16 full, 44 partial.
- **Topics:** no new topics.
- **Places:** `district White Mountains Regional` 223, `town Whitefield` 26, no place 3.
- **Pending facts:** 2, citing draft minutes.
- **Raw folders:** each under 100 MB. The 9 saved PDFs are policies, a handbook, a budget, the WMCC application and the ASAP packet (a scan, transcribed); none is a route sheet or a list of names. The scanned 2025-26 bus sheet is kept as a transcription of times and stops only.
- **Privacy:** the address scan finds only federal and state agency addresses in handbooks and forms.
- **Quotes:** 446 of 586 quoted passages found word for word in the raw copies (the misses are mostly minutes with names bracketed, and the agents' own wording).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | School taxes of $2,552,133 (2018) and $3,708,852 (2025), up 45.3%, and resident students from 293 to 245 (down 16.4%) | The site's `town_school_tax` and `town_enrollment` tables |
  | The ASAP fee of $10 a day and the sliding scale | The ASAP packet's transcription and the August 2026 news post |
  | Coos Adult Education closed in fall 2024, with services at Above the Notch | North Country Education Services' page (saved copy) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day pre-K at Whitefield Elementary | Preschool is Monday to Thursday only, with 8 seats for new students and a waitlist; Head Start in Whitefield runs 4 hours a day |
| A full-time speech therapist | A speech pathologist is listed; full-time isn't confirmed (the FY27 budget charges Whitefield 0.65) |
| A counselor every day | Not stated; the FY27 budget charges one counselor, down from two |
| 7th and 8th grade moved to the high school | True from 2026-27; the principal said the layout change "has been a bit bumpy" |
| STEM, robotics or aviation clubs at the elementary school | None; the high school has an intro robotics course and no aviation course |
| Keeping 12- and 13-year-olds apart from seniors | Closed campus from 2026-27; grades 7–8 have their own block schedule |
| An earlier bus pickup on Regional Road | Next year's sheet isn't published; a 7th grader gets the same stop time as an elementary rider and rides 10–14 minutes longer |
| PowerSchool and parent portals | PowerSchool has been replaced by Alma |
| Welding or diesel in 9th grade | Only a half-credit intro with basic welding; no diesel |
| "Free" Early College classes | Two free courses a year, subject to funding; the school's own book contradicts itself on the $150 fee |
| Laptops and Wi-Fi | Wi-Fi access points replaced in February 2024; Chromebooks bought in April 2026 |
| Agriculture and maple sugaring for science credit | Listed as CTE courses; nothing says they count as science |
| Tax bill "climbs every March" | Bills aren't issued in March; the rate fell after the 2024 revaluation but the dollars rose 45.3% |
| Moving 7th and 8th grade saved money | The district said staying and moving would each save about $1.7 million; it was framed as avoiding cuts |
| An "SAU 36 school board" | The district's board is the White Mountains Regional School Board |
| Annual homeschool evaluations | Repealed July 1, 2026 |
| Ten broken links on the district website | Not found: all 17 links on the School Year Information page opened |
| A lower graduation rate than Littleton's | Littleton's four-year rate was higher in 8 of 10 years; White Mountains Regional's was higher in 2025; both classes are small |

## Corrections and additions to earlier files

Applied:
- **Lancaster `white-mountains-regional-high-and-career.md`, adult-education-and-workforce-training 3:** it listed the Coos Adult Education and Literacy Program's offices as current; North Country Education Services says the program closed in fall 2024 and moved to Above the Notch. The fact now says so, and the NCES page is saved in Lancaster's `raw/browser/`. (Berlin's `middle-high-and-support.md` fact 1 already says Above the Notch serves Berlin as "Coos Adult Education", so it stands.)

Not applied (additions for Lancaster's files):
- **`white-mountains-regional-high-and-career.md`:** the College Board ledger authorizes AP Physics 1 for 2025-26 and 2026-27, which settles the "AP Physics" conflict in its summary; the 2026-27 handbook's staff list shows a Criminal Justice teacher (its cte-center-programs 13 says it isn't stated whether the position was filled); the director's report says Digital Media moved from the Gallen center to the Paradice center midway through 2024-25.
- **`white-mountains-regional-high-and-career.md`, cte-center-programs 3 and school-programs-after-grade-6 2:** the minutes name the speaker of the February 19, 2026 answers only as "Rob", listed in December 2025 minutes as the Assistant Superintendent, not the superintendent.
- **`money-and-governance.md`, district-board-and-public-input 2:** it says all 32 agendas from July 2025 were in Whitefield; the 2024-25 minutes show 5 of 21 meetings held in other buildings and towns.
- **`white-mountains-regional-student-life-and-support.md`:** the athletic participation fee in policy JJIC wasn't found there; the athletic director said "we do not charge" on April 24, 2025 (unclear whether it settles the policy's fee). The August 28, 2026 sports bus post's schedule image shows a bus running from Whitefield Elementary (2:45) to the Middle High School (3:00) to Lancaster Elementary (3:15), with no return time. The 2025 YRBS report is saved in Lancaster's raw folder; its figures are in Whitefield's `district-goals-and-performance-reporting` 2–3.

## Library notes (for review, not applied)

- None.

## Browser pass

Not done. Not retrieved:
- NH DHHS survey pages (HTTP 403), an NH DOT airport page (403), NHIAA division and co-op lists, the NH DOE charter list, a Civil Air Patrol site (did not resolve), the SRO safety letter (404), and the Weathervane Theatre search (not run when the search budget ran out);
- this year's kindergarten and grade 1 headcounts, preschool seats for fall 2027, counselor and speech schedules, field trip costs, a boots program, the district's gifted-and-talented report, hallway rules for grades 7–8, homework minutes, where the English learner teacher is based, whether Alma's Spanish portal is on, the district's savings slides behind the $1.7 million, any plan for the freed classrooms, turnover rates, Whitefield's town budget and 2026 tax rate, and whether athletic fees are charged (not found).
