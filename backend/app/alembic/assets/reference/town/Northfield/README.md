# Northfield: Research for Ask NH Education Facts

Cited facts and figures for answering Northfield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the second ToLoad batch. Northfield's students attend the Winnisquam Regional School District (SAU 59), shared with Sanbornton and Tilton:
- Southwick School, in Northfield: K–4;
- Winnisquam Regional Middle School (5–8) and High School (9–12), both in Tilton. The Winnisquam Career Center opened beside the high school in 2025.

The district decides its budget at a traditional district meeting, Saturday, March 20, 2027. It was researched first in `../Tilton/`; these files cite Tilton's facts and add Northfield's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `southwick-and-families.md` | Kindergarten's full 8:45–3:15 day, the Zion Hill bus (8:18), drop-off from 8:20 (the middle school from 7:20), storm calls by 6:15 a.m., meals (27% free, 2% reduced), public pre-K for IEPs only (Head Start in Franklin), translation and English learners (9), librarians funded, split-household bus rules (EEA, EEAB), the drive from Bay Hill Road, a 2026-27 handbook and Title I plan | 11 | 30 | 2 | 14 MB |
| `middle-school-support-and-choices.md` | WRMS (grades 5–8 since 2022-23) math above most Merrimack County middle schools and reading below, honors math in grades 6–7 and Algebra I in grade 8, phones kept off in lockers, no formal tutoring program, Compass busing on existing routes, teacher retention (57% at Southwick, 68% at WRMS), reading since 2019, the policy manual posted, Riverbend's mental health region, no LGBTQ+ club listed (a new statewide survey topic) | 12 | 39 | 2 | 8 MB |
| `high-school-and-career-center.md` | The career center (renovated, 1.1 miles from Town Hall; 90-minute classes, three named credentials), the Huot Center by district bus (Concord's center doesn't list Winnisquam), Early College, North Country Charter Academy (67.8 miles away), ELO credit instead of work-study, ApprenticeshipNH, football missing from the NHIAA's 2026-27 lists, habitual truancy (125 students in 2024-25), trades wages | 10 | 31 | 5 | 7 MB |
| `money-and-governance.md` | The 2025 school rate ($8.28, up from $7.15; no source for $9.30), Northfield's share (37.56% of costs, the least per student, the highest rate), what drove the 2025 rise, the hold-harmless aid step-down (about $0.62 per $1,000 in FY2028), Union Sanborn sold to Compass ($2.2 million, 2023), budget shares (teacher salaries 27.5%), rotating board meetings, no deliberative session | 6 | 25 | 2 | 16 MB |
| **Total** | | **39** | **125** | **11** | **45 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.89 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Northfield`). All 11 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 37 full, 22 partial, 1 from the site's data.
- **Topics:** one new topic, added to `../shared-topics.md`: `lgbtq-students-nh-survey-data` (what statewide surveys show about LGBTQ+ students).
- **Places:** `district Winnisquam Regional` 100, `town Northfield` 20, `district North Country Charter Academy` 1, no place 4.
- **Pending facts:** 10, citing draft board minutes.
- **Raw folders:** each under 100 MB.
- **Privacy:** the main session removed house numbers from the saved route sheets and deleted the route PDFs. The address scan finds only the Pines Community Center. Later, the main session also removed graduates' names from the saved 2026 Winnisquam annual report texts, and deleted those PDFs.
- **Quotes:** 357 of 425 quoted passages found word for word in the raw copies.
- **Search:** the elementary agent ran out of web searches after its first search ("SEARCH BLOCKED"). It finished from pages reached directly.

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day kindergarten (P1.1) | In practice yes: the same 8:45–3:15 day |
| The Zion Hill bus (P1.2) | 8:18 a.m. |
| Drop-off by 8:00 (P5.1) | Southwick from 8:20; the middle school from 7:20 |
| Free lunch for all (P5.2) | No: 27% free, 2% reduced |
| Librarians cut (P13.1) | Not cut |
| Public pre-K (P17.1) | Only with an IEP |
| A middle school for grades 6–8 | Grades 5–8 since 2022-23 |
| One math track (P4.2) | Honors in grades 6–7; Algebra I in grade 8 |
| Phones locked away (P9.1) | Kept off in lockers |
| After-school tutoring (P9.2) | No formal program |
| Compass busing (P10.2) | The district buses, on existing routes only |
| Annual homeschool filing (P11.3) | Repealed July 1, 2026; policy IHBG still describes it |
| Reading back to pre-pandemic (P13.2) | Grades 3–4 yes; grades 5–8 no |
| A bus to Concord's career center (P2.1) | No; the Huot Center by district bus |
| Running Start (P15.2) | Renamed Early College |
| Work-study (P20.2) | ELO credit, up to one a year |
| The rate from $8.28 to $9.30 (P3.1) | $8.28 is 2025's; $9.30 appears nowhere |
| Northfield pays more (P3.2) | The biggest share, but the least per student |
| The empty Union Sanborn (P6.2) | Sold to Compass in 2023 |
| A deliberative session (P18.3) | None: a traditional meeting |

## Corrections and additions to earlier files

- **Tilton** (`../Tilton/`):
  - **Football:** its high school file lists varsity football from the 2025-26 profile; the NHIAA's 2026-27 alignment doesn't list Winnisquam.
  - **Policy manual:** its middle school file says the board's manual wasn't found. It is posted on the "WRSD Policies" page, and IHBG is saved here.
  - **New documents:** a 2026-27 elementary handbook and Title I plan are now posted.
  - **Storm calls:** cancellations go out by 6:15 a.m., which fills a gap.
- **Alton's** statewide retention (83.8% over 440 schools) is within one school of this file's calculation (83.9% over 441).

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` and `budget-form-statewide-list`** have no Winnisquam entry. It decides its budget at a traditional meeting (March 20, 2027, 9:00 a.m.).
- **`kindergarten-day-length`** still has no Winnisquam entry; the 2026-27 handbook gives one 8:45–3:15 day.

## Browser pass

Not needed for the answers. Not retrieved:
- the Town of Northfield's site and UNH-hosted reports (a bot check), so the elderly exemption, fire district rate and 2026 rate are missing;
- Niche;
- the OSHA training pages (HTTP 403);
- studentaid.gov;
- a Laconia Daily Sun story (HTTP 429).
