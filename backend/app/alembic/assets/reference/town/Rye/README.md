# Rye: Research for Ask NH Education Facts

Cited facts and figures for answering Rye, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the sixth wave of the second ToLoad batch. Rye is in SAU 50 with Greenland, New Castle and Newington:
- **Rye Elementary** serves preschool to grade 4.
- **Rye Junior High** serves grades 5–8, and also takes New Castle's students.
- **High school:** Portsmouth High.

The district votes by official ballot. SAU 50 was researched first in `../Greenland/`, and Portsmouth High in `../Portsmouth/` and `../Greenland/`. These files add Rye's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `rye-elementary-and-families.md` | The Rye PreK (8:15–2:15, no bus; first come, first served) and the SAU 50 preschool, no before-school care (supervision from 8:05), Rye Recreation after school ($20 a day; 40 a day), Sagamore Road bus times (7:44–8:04), Spanish and French from kindergarten, dismissal times, early releases, no ESL teacher listed, newsletters | 14 | 64 | 1 | 19 MB |
| `rye-junior-high-support-and-choices.md` | 5th grade at the junior high since 2019-20, no Algebra I or gifted program (2023-24), specialists (a shared behavior analyst; no psychologist listed), team cuts by roster limits, outdoor time, homeschool and EFA access, class sizes of 36–51, no science lab listed in the 1933 building, counseling | 11 | 84 | 5 | 19 MB |
| `portsmouth-high-from-rye.md` | Two Rye routes (first pickups 7:33 and 7:36; none on Route 1), PHS's seven CTE programs, parking for juniors and seniors only, calendars, separate storm calls (no penalty for late arrival on SAU 50 delay days), Rye as about 16% of PHS's public feeder 8th graders, no late bus, clubs during the school day | 7 | 46 | 1 | 9 MB |
| `money-and-governance.md` | Rye's SAU 50 share ($1,033,994, 47.97%), the budget (up 1.58% in 2026-27; 40.4% over ten years), the surplus used to lower taxes ($479,725), spending by school, Portsmouth tuition (about $1.06 per $1,000), the building study (passed 738 to 613; two of four scenarios merge the schools; no bond), capacity (73% and 68%), the Washington Road sidewalk | 12 | 83 | 7 | 17 MB |
| **Total** | | **44** | **277** | **14** | **64 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.29 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Rye`). All 14 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial.
- **Topics:** no new topics.
- **Places:** `district Rye` 234, `town Rye` 22, `district Portsmouth` 13, `sau 50` 8.
- **Pending facts:** 47, mostly citing the October 21 and 26, 2026 draft board minutes.
- **Raw folders:** each under 100 MB. Bus copies have house numbers removed, and the original route sheet wasn't saved. The address scan finds only school and town offices.
- **Quotes:** 660 of 810 quoted passages found word for word in the raw copies.
- **Sources:** many Rye board files can be viewed but not downloaded. The money file used copies the Rye Civic League posts publicly, and says which facts rely on them.
- **Privacy:** SAU 50 posts a sheet of individual students' Portsmouth High grades, row by row, with partly masked IDs. It wasn't saved or used. The district may want to know.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Rye's SAU 50 share, $1,033,994 | The FY27 budget's staffing section |
  | $479,725 of surplus used to lower taxes | The FY26 financial statements |
  | The building study vote, 738 to 613 | The junior high's October 1, 2026 news post |

## Premises checked

| Question says | What the sources show |
|---|---|
| Hard-to-get preschool (P1.1) | Not settled; first come, first served, with a waitlist |
| Preschool 8:15–2:15, no bus (P1.2) | Correct |
| Before-school care (P3.1) | None |
| World languages only from the junior high (P9.2) | Wrong: Spanish and French from kindergarten |
| Different dismissal times (P12.1) | Barely |
| An ESL teacher on site (P14.1) | None listed |
| 5th grade at the junior high (P4.1) | Correct |
| Early algebra (P4.2) | No posted path |
| About 175 students (P6.2) | Correct |
| Science labs (P18.3) | None listed |
| Route 1 bus stops (P7.3) | None on Lafayette Road |
| Out-of-sync calendars (P10.2) | Partly |
| Separate snow calls (P19.2) | Right |
| A math gap (P20.2) | Not measured |
| About 400 students (P2.1) | Right: 386 |
| A Rye Elementary study and bond (P2.3) | The study covers both schools; no bond |
| $470,000 returned (P8.1) | Close: $479,725, used to lower taxes |
| Crowding (P16.1) | No: about 73% and 68% of capacity |
| No sidewalk to the junior high (P20.3) | Correct today; one planned by 2029 |

## Corrections and additions to earlier files

- **Greenland** (`../Greenland/`):
  - Its SAU 50 budget fact reads "SB" in a question log as "school board/SAU". The initials there name the Budget Committee members who asked.
  - Its upper grades file calls the SAU report "five years of Portsmouth High course placement and performance data". This file cites the report directly.
  - This file adds SAU 50 policies DIA, KF and JFAB, placed `sau 50`.
- **Portsmouth** (`../Portsmouth/`): this file adds Rye's side of PHS's FLEX block and calendar.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 120 (Rye):** it says no 2026 dates were found. The deliberative session was February 3, 2026, 6:30 p.m., at Rye Junior High.
- **Coverage table:** it lists Rye's kindergarten day as not found. These files fill it.

## Browser pass

Not needed for the answers. Not retrieved:
- **Board reports and the 2025-26 minutes,** whose downloads are turned off; the Civic League copies covered the money file.
- **The PTA's enrichment sign-up site** (a bot check).
- **NH DOE's** testing pages.
- **The Seacoast Science Center** site (HTTP 403).
