# Greenland: Research for Ask NH Education Facts

Cited facts and figures for answering Greenland, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the sixth wave of the second ToLoad batch. Greenland is in SAU 50 with New Castle, Newington and Rye:
- **Greenland Central School (GCS)** serves kindergarten to grade 8. Greenland runs no preschool.
- **High school:** Portsmouth High (PHS), under the AREA agreement.

The district votes by official ballot. Portsmouth High was researched in `../Portsmouth/`. This town's money file holds the SAU 50-wide facts (placed `sau 50`); Rye's research (`../Rye/`), done alongside, adds Rye's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `gcs-early-grades-and-families.md` | Full-day kindergarten (no fee), no preschool in town (the SAU 50 preschool at Rye, about 6 miles), after-school care (PEAK in the building; the YMCA to 6:00), the 1:30 p.m. cutoff for dismissal changes, FirstView bus tracking and 2026-27 bus times, lunch at $3.25, class sizes near 15, dyslexia screening | 15 | 55 | 1 | 27 MB |
| `gcs-upper-grades-support-and-choices.md` | The K–2, 3–5 and 6–8 houses (grade 5 still one class), Encore electives, math (no posted Algebra I path), sports open to all with team buses, counselors by grade span, special education procedures, bullying policy JICK, homeschool access, charter and private schools nearby | 11 | 80 | 3 | 54 MB |
| `portsmouth-high-from-greenland.md` | 166 Greenland students at PHS, one Greenland bus (first stop 6:56; no late bus), honors open to all, CTE in the building (welding and automotive; no electrical), IEPs staying with SAU 50, the Class of 2025's plans and SAT scores by town, two portals (PHS and GCS), dual enrollment with Great Bay | 10 | 29 | 2 | 14 MB |
| `money-and-governance.md` | The FY2028 budget (the October draft +10.35%; approved +4.09% after $971,608 of net cuts), PHS tuition ($25,529 a student; 2026-27 line $159,064 over budget), the tuition trust fund, Question 2 (55.0% yes; failed), the building (no bond; cafeteria roof and air unit pulled from the budget), SAU 50's formula, shares and new superintendent | 10 | 74 | 6 | 45 MB |
| **Total** | | **46** | **238** | **12** | **140 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.11 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Greenland`). All 12 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 33 full, 27 partial.
- **Topics:** no new topics. One fact uses the library's `early-college-on-campus`.
- **Places:** `district Greenland` 189, `sau 50` 34, `district Portsmouth` 9, `town Greenland` 5, `town Portsmouth` 1.
- **Pending facts:** 15, citing the November 2026 draft minutes and the FY2028 working budget.
- **Raw folders:** each under 100 MB. The bus sheet copy has house numbers removed; the original wasn't kept.
- **Privacy:** the main session ran OCR on the scanned board minutes the agents saved. The August 10, 2026 minutes gave a resident's home address in public comment, so the main session deleted that PDF; the facts cite a partial text copy without it. The other scanned minutes are clean. The address scan finds only the school, the SAU office and child care centers.
- **Quotes:** 532 of 617 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The FY2028 budget up 4.09% ($633,339.86) | The board's November 9, 2026 budget summary |
  | PHS tuition of $25,529, and $159,064 over budget (**derived**: 166 × $25,529 less $4,078,750) | Portsmouth's October 30, 2026 rate memo, and Greenland's November 11 financial report |
  | Question 2 in Greenland, 55.0% yes | WMUR's unofficial results |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day kindergarten, maybe with a fee (P1.1) | Full-day, no fee |
| Public pre-K, or a drive to Rye or Newington (P1.3) | None in Greenland; families drive |
| FirstView in real time (P2.1) | "Near real-time" by its own account |
| Free lunch for all (P8.1) | No: $3.25 |
| Classes of 15 or 24 (P9.2) | Closer to 15 |
| 54% math, 76% reading (P7.1) | Spring 2025 figures; spring 2026 was 65% and 70% |
| Self-contained grade 4, then a 5–8 middle school (P2.2) | Partly out of date: houses K–2, 3–5, 6–8 |
| Team cuts (P11.1) | None found; teams open to all |
| Rides to away games (P11.3) | Team buses |
| A yearly homeschool letter (P15.2) | Out of date since July 1, 2026 |
| A late bus from PHS (P3.2, P17.2) | None |
| AP classes at PHS (P7.3) | None since 2023-24; honors and dual enrollment instead |
| An IEP starting over at PHS (P6.2) | Stays with SAU 50 |
| A one-on-one aide billed separately (P6.3) | Unsettled; the AREA agreement isn't posted |
| Under 400 students, taxes rising (P4.1) | 344 at GCS plus 166 at PHS; levy up 8.8% |
| Tuition a flat rate (P4.2) | Per student |
| A big renovation or bond (P10.1) | None planned |
| A December Budget Committee review (P12.2) | Not confirmed; last cycle's hearing was in January |
| A new superintendent (P19.3) | Correct: Dr. Ellen Kaschuluk |

## Corrections and additions to earlier files

- **Rye** (`../Rye/`):
  - This town's table `sau50_phs_class_2025_by_town` has Rye's Class of 2025 rows at PHS (40 graduates, SAT means 566 and 532), placed `district Rye`. It fills a gap Rye's file reports.
  - Rye's README says the PHS data SAU 50 received in November 2026 were for 2025–26 only, not "five years". Both wordings have a source: the written report says 2025–26, the November 16 draft minutes say "a five-year dataset". The minutes aren't approved yet.
- **This town's money file:** its SAU 50 share facts and table said Rye's share wasn't found. The main session added Rye's $1,033,994 from Rye's research; the four shares add to SAU 50's $2,155,675. It also corrected the reading of "SB" in the Rye Budget Committee's question log, as Rye's review noted.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 48 (Greenland)** says no 2026 dates were found. They were: the Budget Committee hearing January 13, the deliberative session February 2 and the vote March 10, 2026.
- **`district-practices.md` Greenland 15** quotes SAU 50's "close to 400" students. GCS's own pages say about 360 to 380; the site's data has 367 for 2024-25.
- **`high-school-tuition-options` 34 (Greenland)** quotes only JFAC's first sentence. The policy also makes an exception, allowing tuition for graduates identified for special education.
- **Coverage table:** it lists Greenland's kindergarten registration as not found; this research fills it.

## Browser pass

Not needed for the answers. Not retrieved:
- the Town of Greenland's website (HTTP 401), for the Budget Committee schedule and 2026 tax rate;
- PEAK's operator, Seacoast Community School (a bot check);
- the board's 2025-26 files and earlier budgets, whose downloads are turned off;
- SAU 50 policy full texts (shown only in an in-page viewer);
- NH DOE's special education determinations and NH DRA's 2026 tax rates (HTTP 403).
