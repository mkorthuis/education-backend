# Fremont: Research for Ask NH Education Facts

Cited facts and figures for answering Fremont, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the sixth wave of the second ToLoad batch. Fremont is SAU 83, a one-district SAU:
- **Ellis School** serves preschool to grade 8.
- **High school:** from fall 2026, entering 9th graders choose Epping High or Pinkerton Academy under ten-year agreements (2026–2036). Fremont students already at Sanborn Regional finish there, through the class of 2029.

The district votes by official ballot. Pinkerton was researched in `../pinkerton/`, Epping in `../Epping/` and Sanborn in `../Kingston/` and `../Newton/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `ellis-early-grades-and-families.md` | No drop-off before 8:20, a Healthy Kids care program approved in February 2026 (not confirmed open), the preschool lottery ($225 a month), storm calls and WMUR, the cutoff (5 by September 30; earlier entry by approval), 12 early-release Wednesdays (12:50), Spanish in grades 6–8 only, Butler Bus Service, bus changes by policy EEAB, Whitsons meals ($3.50), volunteer checks, drills, the police liaison (no SRO) | 14 | 45 | 1 | 22 MB |
| `ellis-upper-grades-support-and-choices.md` | No shop class, two paras added for IEPs, the special education trust fund ($304,103), five middle school teams, homeschool and EFA access (JJJ, August 2026), Algebra I possible by policy (none offered in 2023-24), clubs, the August 2026 bullying policy, counselors and a behavioral health coordinator, Chromebooks (grades 1 and 5), phones banned all day, a math interventionist | 12 | 71 | 4 | 15 MB |
| `high-school-choice.md` | Epping or Pinkerton with no limit, Pinkerton buses from 6:00–6:04 (none late), SST only through Epping or Sanborn, IEP steps in each agreement, calendars that match, the Sanborn phase-out (73 Fremont students in October 2026), no switching between schools, Pinkerton's size (2,988), the 2024 vote (648 to 131) | 9 | 38 | 4 | 12 MB |
| `money-and-governance.md` | The failed 2026 budget (347 to 464) and the $14,694,498 default, 507 students paid for, tuition rates (Sanborn $27,329.63; Epping $19,764.55; Pinkerton $17,909.87), the failed teacher contract (twice), no bond (roofs replaced 2019–2020), cost per pupil ($22,802), the January 30, 2027 deliberative session, free facility use for town recreation | 7 | 75 | 4 | 29 MB |
| **Total** | | **42** | **229** | **13** | **79 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.14 million tokens, plus two follow-up passes.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Fremont`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 39 full, 21 partial.
- **Topics:** no new topics.
- **Places:** `district Fremont` 212, `town Fremont` 12, `district Epping` 2, no place 3.
- **Pending facts:** 5. Two are false alarms that quote "DRAFT" or "pending petition" from the source.
- **Raw folders:** each under 100 MB.
- **Privacy** (main session):
  - **Bus routes:** the high school sheet keeps only times and streets.
  - **Board members:** their home addresses and phone numbers in both handbook copies were removed.
  - **Public comment:** residents' house numbers were removed from the board minutes text, and the minutes and handbook PDFs were deleted.
  - **Address scan:** the only remaining addresses are the school, the town hall, other schools and businesses.
- **Quotes:** 600 of 701 quoted passages found word for word in the raw copies.
- **Search:** three agents ran out of web searches ("SEARCH BLOCKED"); the shared search limit ran out that evening.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The default budget, $14,694,498 | The January 31, 2026 deliberative session minutes |
  | Sanborn's rate, $27,329.63 | The April 14, 2026 board minutes |
  | The budget vote, 347 to 464 | The board's March 17, 2026 packet |
  | The 2024 vote, 648 to 131 | The 2024 voting results |
  | Pinkerton pickups from 6:00 | The 2026-27 high school route sheet |

## Premises checked

| Question says | What the sources show |
|---|---|
| About 43% proficient in math (P6.1, P16.1) | Out of date: 35% in 2025-26 |
| Care at Ellis (P1.1) | Approved in February 2026; not confirmed open |
| A preschool lottery, half-day (P1.2) | Correct |
| Early drop-off (P1.3, P11.1) | None before 8:20 |
| Busing to a sitter (P11.3) | Only as a regular change, by policy |
| A late-September birthday waits (P17.1) | No: 5 by September 30 |
| Spanish at Ellis (P17.3) | Grades 6–8 only |
| An SRO (P20.2) | None; a police liaison |
| Trades classes gone (P4.3) | None found |
| An annual homeschool evaluation (P9.2) | Repealed July 1, 2026 |
| Phones locked up (P15.2) | Banned all day; kept off and put away |
| A late bus from Pinkerton (P2.3) | None |
| SST from Pinkerton (P4.1) | Only through Epping or Sanborn |
| Calendars that don't line up (P7.1) | They match in 2026-27 |
| Almost $15 million for under 400 kids (P3.1) | The budget failed; it pays for 507 students |
| A new teacher contract (P10.3) | None: rejected twice |
| A roof or HVAC bond (P16.2) | None |
| A one-school SAU (P16.3) | Correct, and common (85 of 108) |

## Corrections and additions to earlier files

- **Kingston** (`../Kingston/`): its note says Fremont's March 12, 2024 vote wasn't checked. It was 648 to 131.
- **Epping** (`../Epping/`): its gap on Fremont students at Epping: Fremont counted 1 in October 2025. The Epping agreement's later pages are now transcribed.
- **Pinkerton** (`../pinkerton/`): its class-of-2026 table leaves Fremont out because the contract starts in 2026-27. Fremont students were already attending by petition: 21 in October 2024 and 48 in October 2025.

## Library notes (for review, not applied)

- **`district-preschool` 33** calls Ellis's afternoon preschool "daily". The 2026-27 handbook shows two afternoon groups, Monday/Thursday and Tuesday/Friday.
- **`high-school-tuition-options` 31 (Fremont):** the agreements' terms are now known: Epping and Pinkerton July 1, 2026 to June 30, 2036, and families choose freely between the two.

## Browser pass

sau83.org shows a bot check to automated requests, so the main session read its pages in Chrome. They are saved in `raw/browser/`:
- school hours, registration, food services, health office, preschool, curriculum, athletics, student services, future high school, budget and the performing arts page;
- `sau83-documents-index.tsv`, an index of the district's 2,093 posted documents taken from the site's own document API. The files download directly.

Two agents then folded these in, which took the early-grades file from 1 fully answered question to 11.

Not retrieved: SAU 83's technology page, even in Chrome.
