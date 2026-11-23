# Thornton: Research for Ask NH Education Facts

Cited facts and figures for answering Thornton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch, after Campton's and Plymouth's research on the same SAU and cooperative. Thornton is in SAU 48 (nine districts):
- **Thornton Central School** (kindergarten to grade 8; 168 students in 2025-26, down from 215 earlier and 172 in 2024-25), run by the Thornton School District;
- grades 9–12 go to **Plymouth Regional High School** (PRHS), run by the Pemi-Baker Regional School District, with its career center inside PRHS (the Plymouth Applied Technology Center). Thornton's share of Pemi-Baker's costs is 14.02% of students and 10.69% of SAU 48's cost.

Plymouth's and Campton's files cover Plymouth Elementary, PRHS and Campton's side of the same cooperative; these files cite them and write Thornton's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `thornton-central-and-families.md` | No public pre-K (Campton Elementary's preschool takes Thornton children aged 3 to 5, about 4 road miles away), on-site after-school care by Innovation Learning ($325 a month or $25 drop-in, 3:00 to 5:00; parents raised staffing and communication concerns in fall 2026), SAU 48 administration deciding snow days (no time or process posted), no bus times or stops posted, a Duolingo foreign language pilot since spring 2026 with no language teacher, five Winter Activities Wednesdays with skiing back at Loon Mountain, the town's 2023 Master Plan calling high-speed internet a deficiency and cell service "poor to none" | 19 | 65 | 4 | 12 MB |
| `thornton-central-support-and-choices.md` | 2026 results of 46% in math and 62% in reading against 44% and 55% for the state (57% in math in 2025; 65% in 2019), grade 8 math at 25% against 40%, a "7 to 1" ratio that is all students divided by all teachers (168 ÷ 24, derived) while class sizes average 9.7, 13.0 and 10.8, one full-time counselor, speech, PT and OT bought as services (speech $124,846 in 2026-27), students with IEPs up from 23 to 43, a joint Thornton–Campton field hockey team (21 players, two homeschooled) and policy JJJ (September 28, 2026) giving homeschooled and EFA students the same access | 11 | 81 | 6 | 12 MB |
| `plymouth-regional-from-thornton.md` | A 40-minute ride from Thornton Central to PRHS (6:26 to 7:06; 44 to 46 minutes from earlier stops), 46% of the Class of 2026 planning something other than a four-year college, 19 Thornton EFA applicants against 243 resident students, no welding, electrical, carpentry or construction course at PRHS (automotive typically grades 11–12), Pemi-Baker's acceleration policy and PRHS's handbook giving high school credit for Algebra I or a language taken in middle school, study release for grades 11–12 only | 8 | 40 | 5 | 2.9 MB |
| `money-and-governance.md` | 70.4% of Thornton's 2025-26 school money ($8,259,539, matching the site's local plus state education tax) going to Thornton Central and 29.6% to PRHS, a $4.52 million energy project approved March 7, 2024 (201 to 89; debt service $286,107 in 2026-27), the April 2024 revaluation and the adequacy grant falling from $624,971 to an estimated $377,280, voters rejecting a budget cap (60 to 150) and official ballot voting (55 to 158) in 2025, Question 2 at 54.7%, substitutes at $100 a day, a 2019 projection of 240 students for 2024-25 against an actual 172 | 10 | 49 | 4 | 6.5 MB |
| **Total** | | **48** | **235** | **19** | **33 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.4 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Thornton. All 19 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 33 partial, 1 none (P19.1: no source on how buyers see the schools). Two questions (P14.1, P17.3) are answered wholly by earlier files.
- **Topics:** no new topics.
- **Places:** `district Thornton` 169, `district Pemi-Baker Regional` 33, `town Thornton` 23, `district Rumney` 5, `sau 48` 4, no place 1.
- **Pending facts:** 10, citing draft warrants, draft budgets and a draft schedule (a few only quote a policy's "while it is pending").
- **Raw folders:** each under 100 MB. The 50 saved PDFs are handbooks, policies, the teachers' contract, budgets, winter activity letters (scans, transcribed) and state sheets; none is a route sheet or a roster. Student names are removed from the saved minutes copies.
- **Privacy:** the address scan, including the `--raw` pass, finds only the SAU 48 office, the schools and a USDA civil rights address.
- **Quotes:** 571 of 671 quoted passages found word for word in the raw copies (the misses are mostly minutes and budget pages read from images, and table text).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | $8,259,539 owed to the school districts for 2025, equal to the site's local plus state education tax | The site's `town_school_tax` table and the town report extract |
  | Question 2 at 54.7% in Thornton (735 to 609) | The site's `town_question_two` table |
  | Debt service of $286,107 in 2026-27 | The adopted 2026-27 budget |
  | The adequacy grant of $624,971 in 2021-22 and $377,280 (2026-27 estimate) | The February 5, 2026 budget hearing slides |
  | The $4,519,318 energy project approved 201 to 89 | The March 7, 2024 meeting minutes (read from an image, per the fact's note) |

## Premises checked

| Question says | What the sources show |
|---|---|
| A 40-minute bus ride (P10.1) | Correct for a rider boarding at Thornton Central (6:26 to 7:06); earlier stops ride 44 to 46 minutes; the afternoon ride isn't posted |
| Many graduates choose something other than a four-year college (P2.1) | 46% of the Class of 2026 planned something else |
| "Half the families" use an EFA or homeschool (P14.2) | Not supported: 19 Thornton EFA applicants against 243 resident students; a Census estimate of 0 (±12) for grades 9–12 in private or home school |
| Part-time classes and welding at PRHS (P8.3) | Part-time classes are allowed; welding is not offered |
| A "Plymouth Area Technical Center" (P10.2) | NH DOE's name is the Plymouth Applied Technology Center, inside PRHS |
| An eighth grade visit to PRHS (P13.2) | None posted |
| 57% math and 62% reading | The spring 2025 figures; spring 2026 was 46% and 62% against 44% and 55% |
| "7 to 1" | All students divided by all teachers, not a class size |
| A counselor (the handbook) | One full-time counselor; the handbook still names a Section 504 coordinator who retired in June 2025 and prints older bullying and phone rules |
| The brief's library coverage for Thornton | The library marks Thornton's kindergarten and preschool facts "not found"; this research fills them |
| No public pre-K at Thornton Central | Correct |
| Snow-day calls by the school | SAU 48 administration decides |
| Google Classroom | The handbook names ParentSquare and ALMA, not Google Classroom |
| A tax bill each spring (P2.2) | Bills come twice a year (June and December); enrollment fell from 215 to 172 |
| An SAU bill (P3.2) | SAU 48 serves nine districts; Thornton pays 10.69% |
| A roof problem (P12.2) | The boiler issue was public from 2020; no roof item exists in the capital plan |
| A cap or plan for Owl's Nest (P19.2) | No source ties one to it |
| The board "rubber-stamps" the SAU (P20.2) | Not shown: the minutes show it declining an SAU request |

## Corrections and additions to earlier files

Applied:
- **Plymouth `pes-support-and-choices.md`, the main gaps paragraph:** it said no source showed whether PRHS gives high school credit for Algebra I taken in grade 8. PRHS's 2026-27 handbook says students who complete "Algebra I or a World Language course at their respective middle schools will receive high school credit for those courses" (and a 1991 policy says the same); the paragraph now says so and cites Thornton's file.

Not applied (additions for other files):
- **Plymouth `prhs-and-career-center.md`:** cte-center-programs 4 and 7 describe Level II seats; the 2000 Regional Center Enrollment Policy adds the older seat-sharing rule and lists Construction Technology. Its school-programs-after-grade-6 10 says the 2026-27 handbook has no dual enrollment policy section; Pemi-Baker's policy LEB/IHCD of November 2024 is that policy.
- **Campton `campton-elementary-support-and-choices.md`:** it doesn't mention that its field hockey team is shared with Thornton (its August 13, 2024 minutes list "5-8 combined field hockey with Thornton"); that is `district-pe-outdoor-and-athletics` 3 in Thornton's support file. Campton's Route 175 "Campton Cupboard" stop wasn't checked here.
- **Campton's district-school-day-and-calendar 4:** Campton Recreation let Thornton students attend its after-school program in 2025-26 and bused them; it is for Campton students only in 2026-27, which fits Thornton's file.
- **The Got Lunch pages (town-family-help 3)** say 35% of Thornton students qualify for free or reduced meals, while the site's data show 25.0% for 2025-26 (42 of 168, derived); Campton's file agrees with the site.

## Library notes (for review, not applied)

- **`district-practices.md`** (coverage table and `raw/districts/not-found-notes.csv`) lists Thornton's kindergarten day, cutoff, registration and preschool as "not found"; this research fills them.

## Browser pass

Not done. Not retrieved:
- EIN News' page on the Owl's Nest "$100 million expansion" (HTTP 403), the OPLC electrician apprentice page (403), the Thornton School Board's May 2026 and 2025 minutes (scans, not read), the 2025-26 budget and the May 2025 SAU business meeting (would not download), the menu app, Instagram and parent resources pages;
- bus times and stops (including a Route 3 pickup), a late bus, a time or process for snow-day decisions, a standing winter-gear or fee-help program, a gym-use policy, measured cell coverage, afternoon rides, career center enrollment by town, whether Pemi-Baker would pay for another region's career center, days the speech pathologist is in the building, Thornton's math program and 8th grade placement, how Thornton graduates do in PRHS classes, teacher turnover counts, building size and capacity, a current median sale price and Owl's Nest home counts (not found).
