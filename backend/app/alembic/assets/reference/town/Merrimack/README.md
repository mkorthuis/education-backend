# Merrimack: Research for Ask NH Education Facts

Cited facts and figures for answering Merrimack, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 30 resident profiles with 3 questions each, numbered P1.1 to P30.3 in `questions.md`; the people are invented. The research is in the six files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Dover, Salem, Rochester and Londonderry. Merrimack is SAU 26: three elementary schools for preschool to grade 4 (James Mastricola, Reeds Ferry and Thorntons Ferry), the Merrimack Early Education Program (MEEP), James Mastricola Upper Elementary (grades 5–6), Merrimack Middle School (grades 7–8) and Merrimack High School. Merrimack students attend the Nashua Technology Center and the Palmer Center at Alvirne (Hudson) for CTE. Gate City Charter School for the Arts is in town. The district votes by official ballot (SB2).

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | Full-day kindergarten since 2018, the reinstated grade 4 teacher at Mastricola, care inside the schools (Nashua Adult Learning Center, the town's Naticook program), scores against Bedford and Nashua, reading programs, Acadience screening K–4, MEEP's mixed classrooms, specials cuts, teachers' planning time, screen time and devices | 13 | 74 | 2 | `raw/elementary/` (13 MB) |
| `jmues-middle-and-curriculum.md` | Honors math and grade 8 Algebra I, bullying, clubs, Chromebook coverage and instrument rentals, A–F grades with competency marks, the CATCH health curriculum and opt-outs, Personal Finance and NH History, parents' say over materials, the AI policy, phones, gifted cuts, civics, middle school math since 2019 | 11 | 95 | 1 | `raw/middle/` (13 MB) |
| `high-school-and-pathways.md` | The Nashua Technology Center and Palmer Center from Merrimack (about 60 students, buses at 6:45), 18 AP courses (no AP Computer Science), robotics against Nashua South, NCC and SNHU dual enrollment, the new career-readiness policy, the adult diploma, grade 11 results, no ROTC | 7 | 61 | 1 | `raw/high/` (22 MB) |
| `student-support-and-choices.md` | IEPs (22% of students), the state's ratings, 167 paraeducators, Merrimack High's counselors, open enrollment capped at 5 students, Gate City's preference and buses for Merrimack residents, policy JJJ's access for home-educated, EFA, charter and private students, translation, meals, apps and portals | 13 | 80 | 3 | `raw/support/` (22 MB) |
| `getting-to-school-and-staffing.md` | The bus contract ending after 2026-27, route times and kindergarten rides, driver and paraeducator pay, mid-year vacancies, new-teacher mentoring, security and SROs, drills and alerts, school space and housing (with NH Housing's Merrimack figures), bell times | 8 | 81 | 4 | `raw/daily/` (41 MB) |
| `money-buildings-and-governance.md` | The budget and default budget by year, the roof reserve and deferred special education deposit, the fund balance returned to taxpayers, no bonds and the energy audit, the six-year capital plan, per-pupil and tax comparisons, adequacy aid, the Budget Committee's new role in the default budget, complaints to the board | 6 | 62 | 10 | `raw/money/` (15 MB) |
| **Total** | | **58** | **453** | **21** | **126 MB** |

`brief.md` is the brief the research agents worked from. Six agents used about 2.9 million tokens.

## Checks

- **Parser:** all six files pass the backend's parser (`tools/check_town.sh Merrimack`). Every table is linked to a topic.
- **Topics:** one new topic was reviewed and added to `../shared-topics.md`: `research-school-transitions` (what research says about changing schools in the middle grades).
- **Places:** `district Merrimack` 419, `town Merrimack` 19, `district Hudson` 6 (the Palmer Center at Alvirne), `district Gate City Charter School For the Arts` 4, no place 4, `town Litchfield` 1.
- **Places for the backend:** Merrimack runs its own schools from preschool to grade 12, so `places.yaml` has no Merrimack rows; its CTE students aren't district service arrangements.
- **Draft facts:** one note is flagged; the word is the capital plan's own title ("Draft").
- **Raw folders:** all under 100 MB.
- **Spot checks:** each agent checked 3 or more facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | The 2026-27 budget $96,917,871; default $96,964,324 | 2026-27 warrant, Article 2 |
  | The board's 5–0 vote to reinstate the grade 4 teacher at Mastricola (about $83,515 with benefits) | Board minutes, January 5, 2026 |
  | $150,000 into the roof reserve (5–0), which held $3,989; the special education deposit ($587,434 fund) "deferred until next year" | Board minutes, January 5, 2026 |
  | $1.3 million kept and the rest of the fund balance applied to the December 2026 tax bill (5–0); $4,381,002 derived | Board minutes, July 13, September 21 and October 19, 2026 |
  | Paraeducators: $17.93–$23.81 an hour, 7.25 hours, 183 days | Support staff contract 2024–2027, Section 26.1 and Article XXIV |
  | Full-day kindergarten approved April 10, 2018, 1,792 to 1,192 | 2018 election results |

## Premises checked

| Question says | What the sources show |
|---|---|
| The budget "around $96 million" and a default "higher than what the board proposed" (P2.1) | Correct for 2026-27: $96,917,871 against a $96,964,324 default; the default was higher only in 2021 and 2026, and voters rejected the budget in 2024 and 2025 |
| The board deferred the special education trust deposit while putting $150,000 into a roof reserve (P10.2) | Correct: January 5, 2026; voters approved the roof deposit 3,298 to 669 |
| A massive bond for roofs and HVAC (P4.3) | None proposed, and the district carries no bond payments; it pays for roofs by yearly warrant articles. A 2026 energy audit found much of the heating and ventilation equipment past its service life, with no cost yet |
| No 10-year capital plan (P24.1) | Partly: a six-year plan dated May 14, 2026 is posted, but projects slipped during the default-budget years |
| Flat or dipping enrollment (P10.3) | Correct: down 11.7% from 2014-15 to 2025-26 |
| High athletic fees (P26.1) | No participation fee was found; booster costs weren't found either |
| A C+ Niche rating (P20.1) | Not checked: Niche blocked automated requests |
| The board reinstated a grade 4 teacher at Mastricola (P5.1) | Correct (5–0, January 5, 2026), but two Mastricola grade 3 positions were still cut |
| Expanding full-day kindergarten, or kindergarten tuition (P1.1, P21.2) | Already full-day at all three schools since voters approved it in 2018; no tuition is posted |
| MEEP "mostly for kids with delays" (P11.3) | Its classrooms mix children with and without special needs by design; typical peers pay tuition |
| A separate grades 5–6 building (P1.3) | Correct; the district's reason wasn't found |
| Specials cut (P21.3) | One PE teacher each at Reeds Ferry and Thorntons Ferry was on the cut list |
| A "new K–6 health curriculum pilot" with opt-in (P13.1) | No pilot found: teachers trained on CATCH in fall 2025, and parents opt out rather than in |
| The state now requires Personal Finance and NH History (P13.2) | Correct, from the class of 2030 |
| Competency-based grading at Merrimack High (P8.1) | A–F grades plus "met / not met" competency marks |
| The brother's 7th-grade class much bigger (P28.3) | Not supported by the site's enrollment data |
| Middle school math still recovering (P29.2) | Supported: 50% proficient in 2019, 28% in 2022, 45% in 2026 |
| The FIRST Robotics team (P3.2) | Correct; it ranked 26th in New England in 2026, against 86th for the team Nashua South shares with Nashua North |
| CTE busing to Nashua (P4.2) | Correct: the district runs the buses |
| Dual enrollment through SNHU and Nashua Community College (P16.2) | Correct for both |
| The SAT in grade 11 (P22.3) | Correct |
| Welding at the Nashua Technology Center (P4.1) | Wrong: welding is at the Palmer Center at Alvirne in Hudson; electrical and automotive are at the Nashua Technology Center |
| Evening GED and career classes at the high school (P23.3) | Partly wrong: an evening adult diploma and HiSET help, but no testing there; the district's adult classes are hobby and fitness classes |
| ROTC at Merrimack High (P27.1) | None; the Palmer Center lists Air Force JROTC |
| Every school uses a different app (P22.1) | Partly: the main systems are district-wide, but pages name both Canvas and Google Classroom |
| Other towns' students taking elective spots (P12.3) | Not supported: open enrollment at Merrimack High is capped at 5 students |
| Driver shortages and combined routes (P5.2, P26.3) | Not in the 2025–2026 minutes; the last mention is December 2024 |
| Trouble keeping paraeducators (P17.1) | Partly: positions are open, but no turnover data exist |
| Security upgrades at Thorntons Ferry (P18.1) | Cameras, lock sets, grants and two SROs are district-wide; nothing public is specific to the school |
| A new apartment complex near Route 3 (P20.3) | None on the 2026 Planning Board agendas |
| Two different drop-off times (P30.1) | Confirmed: Reeds Ferry and JMUES start 10 minutes apart |

## Corrections and additions to earlier files

None. Nashua's `elementary-schools.md` table of Merrimack's 2025-26 school results matches this town's figures, and its note on the YMCA's program at the Merrimack YMCA is confirmed.

**A lead for later:** NCES's 2024-25 directory lists "Wellheart Chartered Public School" at 646 Daniel Webster Highway, Merrimack. The site's data has it as district 752 and school 29281, with no enrollment; it may be a charter school not yet open. Gate City's website (in the site's data) now shows an unrelated page, as the Nashua research also found.

## Coverage

37 questions are answered **fully**, 52 **partly** and 1 by the site's data alone (P1.2, scores against Bedford and Nashua); none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Rachel | partial | data only | partial |
| P2 Gary | **full** | **full** | partial |
| P3 Priya | **full** | **full** | partial |
| P4 Dan | partial | partial | partial |
| P5 Megan | partial | partial | partial |
| P6 Tom | partial | partial | partial |
| P7 Brenda | partial | partial | **full** |
| P8 Kevin | partial | partial | partial |
| P9 Elena | **full** | **full** | partial |
| P10 Arthur | **full** | **full** | **full** |
| P11 Tessa | **full** | partial | **full** |
| P12 Marcus | partial | partial | **full** |
| P13 Diane | partial | **full** | **full** |
| P14 Javier | partial | partial | **full** |
| P15 Stephanie | **full** | **full** | partial |
| P16 Greg | **full** | **full** | **full** |
| P17 Linda | partial | partial | **full** |
| P18 Sean | partial | partial | **full** |
| P19 Naomi | partial | **full** | partial |
| P20 Paul | partial | partial | partial |
| P21 Courtney | partial | **full** | partial |
| P22 Raj | **full** | **full** | partial |
| P23 Hannah | partial | partial | **full** |
| P24 Frank | **full** | **full** | **full** |
| P25 Claire | partial | partial | **full** |
| P26 Derek | partial | **full** | partial |
| P27 Sandra | partial | **full** | **full** |
| P28 Owen | partial | partial | partial |
| P29 Diane | **full** | **full** | partial |
| P30 Melissa | partial | partial | partial |

## Notable findings

- **Budgets:** the default was higher than the proposed budget in 2026, voters rejected the budget in 2024 and 2025, and from 2027 the Budget Committee, not the board, sets the default under a 2026 state law.
- **Fund balance:** about $4.38 million went to the December 2026 tax bill (about $0.59 per $1,000); the board kept $1.3 million for energy or safety projects.
- **State aid:** the 2026-27 adequacy grant ($9.63 million) is below the 1999-2000 grant ($10.10 million) before inflation.
- **Middle school math:** 50% proficient in 2019, 28% in 2022, 45% in 2026; grade 11 math fell from 33% to 25% from 2024 to 2026.
- **Open enrollment:** Merrimack High takes at most 5 students from other towns, and Merrimack lets none of its students use other districts' open enrollment schools.

## Browser pass, November 15, 2026

Niche's page, read in Chrome, confirms Merrimack High's C+ and gives its category grades (`high-school-and-pathways.md` high-school-outcomes 10; P20.1 updated). Merrimack now has 454 facts.

## Gaps to retry

- **Blocked to automated requests (for the browser pass):** Niche (the C+ rating), NH DOE (2025-26 enrollment by grade, the state's school security grant list), SNHU's high school course prices.
- **Couldn't open:** the December 1 and 8, 2025 board minutes (the elementary budget sessions); Gate City's website.
- **Not found anywhere:** 2026-27 class sizes, aides in K–2 classrooms, minutes of specials and screen time, MEEP and child care prices, grade 8 Algebra I credit and placement, JMUES clubs, how the phone rule is enforced, CTE acceptance counts, bus on-time data, Thorntons Ferry's own security, staff and principal turnover, booster dues, a building condition report, Bedford's and Amherst's 2026 tax rates, any district breakdown of how EFAs affect its state aid.
