# Ossipee: Research for Ask NH Education Facts

Cited facts and figures for answering Ossipee, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the second ToLoad batch. Ossipee's students attend the Governor Wentworth Regional School District (SAU 49), shared with Brookfield, Effingham, New Durham, Tuftonboro and Wolfeboro:
- **Ossipee Central School (OCS)** serves preschool to grade 6, in Center Ossipee.
- **Kingswood Regional Middle School** (7–8) and **High School** (9–12) are in Wolfeboro, with the Lakes Region Technology Center (LRTC).

The district votes by official ballot. It was researched first in `../Wolfeboro/`; these files cite Wolfeboro's facts and add Ossipee's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `ossipee-central-and-families.md` | The preschool (a few role-model spots, with tuition), School's Out (grades 1–6; until 5:15; a federal grant of $80,000 a year), the cutoff (5 by September 30), scores (44% math in 2026), shared and contracted speech staff, meal prices ($3.75 lunch; free to 300% of poverty), art and music kept, traditional snow days, the library's Pre-K Story Time, the Title I plan | 16 | 71 | 2 | 16 MB |
| `support-and-choices.md` | Ossipee students at Kingswood (78 middle, 184 high), start times (7:24 and 7:25), phones off but not locked away, moving within the district, homeschool access and EFA providers, the late bus (Monday–Thursday), counselors and a psychologist at OCS, weekend food programs, the 2023 youth health survey, 504 plans staying with the district | 12 | 71 | 3 | 16 MB |
| `kingswood-from-ossipee.md` | Construction Trades from grade 10, LRTC inside the school day, 7 AP subjects and 15 Early College courses, Huggins Hospital's student rotation, Kingswood Academy (new in 2026), no adult nursing classes, work credit for seniors, no JROTC (the ASVAB is offered), early graduation, the alumni and Tranchita scholarships, community college distances | 5 | 50 | 2 | 11 MB |
| `money-and-governance.md` | Ossipee's school taxes up 81.7% from 2014 to 2025 (the six towns 55.4%), its rising student share and falling adequacy grant, the budget not split by school, Wolfeboro's share of ballots (43–49%), the superintendent search, substitute nurse pay ($50 an hour), the tax cap for 2027-28 | 5 | 39 | 2 | 30 MB |
| **Total** | | **38** | **231** | **9** | **73 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.84 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Ossipee`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 33 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Governor Wentworth Regional` 185, `town Ossipee` 35, `town Laconia` 3 and `town Berlin` 2 (the community colleges), no place 6.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB. The address scan finds only Ossipee Central's own address, the town hall and colleges.
- **Quotes:** 561 of 638 quoted passages found word for word in the raw copies.
- **Search:** the support agent ran out of web searches partway through ("SEARCH BLOCKED"). It finished from pages reached directly.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | School taxes up 81.7% (**derived**) | Recomputed from the tax totals in the raw copies ($7,138,881 to $12,970,362) |
  | Substitute nurse pay of $50 an hour | The October 5, 2026 board minutes |
  | School's Out's $80,000 grant | The district's FY2027 staff requests |

## Premises checked

| Question says | What the sources show |
|---|---|
| A preschool spot for a 4-year-old (P1.1) | Partly: a few role-model spots, with tuition |
| School's Out for a 4-year-old (P1.2) | No: grades 1–6 |
| A bus on Main Street (P1.3) | Can't be checked: no stops posted |
| Shared speech staff (P5.1) | Both own and shared |
| Every child pays for lunch (P7.2) | Partly: free to 300% of poverty |
| School's Out depends on town meeting (P13.1) | Not guaranteed either way |
| Art and music cut (P13.2) | No cut found |
| Blizzard bags (P16.2) | Traditional snow days |
| A start around 7:30 (P2.2) | About right |
| Phones locked up (P6.2) | No: off and put away |
| Homeschoolers shut out (P11.1) | No |
| A late bus (P12.3) | Yes, Monday–Thursday |
| A 504 plan starting over (P20.2) | No: same district |
| Construction Trades in 9th grade (P2.1) | No: from grade 10 |
| Kingswood Academy (P10.3) | It exists, new in 2026 |
| JROTC (P20.1) | None |
| Wolfeboro outvotes Ossipee (P3.3) | Not usually |
| A superintendent search (P6.1) | Right |
| $50 an hour for substitute nurses (P10.2) | Right |
| Nicer facilities in Wolfeboro (P14.2) | Partly; one district |

## Corrections and additions to earlier files

- **Wolfeboro** (`../Wolfeboro/`): the main session added three notes and reloaded Wolfeboro.
  - **School's Out:** the elementary file gives grades K–6, from NH DOE's list. Ossipee Central's handbook says grades 1–6, with kindergartners from the second trimester.
  - **Chromebooks:** the middle school file's quote from "one elementary school's" annual report is Ossipee Central's principal's report.
  - **Counselors:** the middle school file counts four KRHS counselors, from the assignment sheet. The district's Drug and Alcohol Resources page lists five, plus a social worker.
- **Wolfeboro's money file** is consistent: its table already shows Ossipee's share of school taxes, and this file adds why it rose.
- **Graduation credits:** policy IKF was revised November 2, 2026, after Wolfeboro's file was written. Its Class of 2030 social studies credits differ from the 2026-27 catalog.

## Browser pass

Not needed for the answers. Not retrieved:
- **ossipee.org** (a bot check) and its town reports on UNH's repository. Ossipee's town scholarship funds, precinct rates, exemptions and the 2026 tax rate are therefore missing.
- **NH DRA's** rate tables.
- **NH DOE's** grant pages.
