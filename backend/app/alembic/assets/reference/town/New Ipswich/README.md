# New Ipswich: Research for Ask NH Education Facts

Cited facts and figures for answering New Ipswich, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the ninth wave of the second ToLoad batch. New Ipswich and Greenville form the Mascenic Regional School District, SAU 87:
- **Highbridge Hill Elementary** serves preschool to grade 4.
- **Boynton Middle School** serves grades 5–8.
- **Mascenic Regional High** serves grades 9–12. Career programs are through the Region 14 center at ConVal High, and Mascenic now hosts Region 14's construction trades.

The district votes by official ballot. Region 14 was researched in `../Peterborough/` (alongside this town) and `../Jaffrey/`. Mascenic's website shows a bot check to automated requests, so the agents worked from the district's linked Google Drive files.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `highbridge-hill-and-families.md` | Full-day kindergarten (9:00–3:05), the preschool (now 4-year-olds only; full, with a wait list; a half-day cut on hold), Healthy Kids care (6:30 to 5:30; licensed November 13, 2026), Boynton drop-off from 7:30, students per teacher (**derived**), lunch $3.60, bus stops by road | 16 | 72 | 2 | 13 MB |
| `boynton-support-and-choices.md` | Math at 27% in 2025-26, no late bus or homework club, policy JJJ (October 2026) for homeschool and EFA students, private school busing within the district only, special education openings, teams open to grades 5–8 (paid for by fundraising after the default budget cut them), no gifted program, Chromebooks kept in classrooms | 14 | 81 | 3 | 25 MB |
| `mascenic-high-and-region-14.md` | Building trades restarted in fall 2026 ($192,000 approved), the amended Region 14 agreement (25% of seats for sending districts), Mascenic's vans to ConVal, weighted GPA and class rank, AP Calculus cut then restored, about 40% of graduates to work or the military, no football or hockey, military recruiter rules | 12 | 66 | 2 | 13 MB |
| `money-and-governance.md` | Three default budgets in a row (2026: $467,678 below the proposal; $580,048 of cuts), the 75/25 cost formula (New Ipswich 76.05%), the failed support staff contract and para pay, the repair reserve ($241,623), the Highbridge Hill bond ending, enrollment (833 in October 2026), the February 3, 2027 deliberative session | 10 | 84 | 11 | 27 MB |
| **Total** | | **52** | **303** | **18** | **78 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.09 million tokens.

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus New Ipswich. All 18 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 33 full, 27 partial.
- **Topics:** one new topic, added to `../shared-topics.md`: `military-recruiter-access-rules`, the federal rules on recruiters' access to high school students and how parents opt out.
- **Places:** `district Mascenic Regional` 286, `town New Ipswich` 15, statewide 2.
- **Pending facts:** 14, citing draft budgets and draft minutes.
- **Raw folders:** each under 100 MB. Bus copies have house numbers removed; the original route sheets weren't saved.
- **Privacy:** the address scans, including the text of every saved PDF, find only the schools and the SAU office.
- **Quotes:** 614 of 708 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 proposed budget, $23,899,107, and default, $23,431,429 | The February 4, 2026 deliberative session minutes |
  | The March 2026 votes by town (open enrollment 921–664 overall, New Ipswich 759–604) | The district's signed 2026 voting results |
  | The repair reserve, $241,623 | The FY28 draft 2 board materials |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day kindergarten (P1.1) | Correct |
| A preschool lottery (P1.1) | No lottery; rolling admission and a wait list |
| Care at the school (P1.3) | Healthy Kids, licensed after a delay |
| Boynton drop-off at 7:30 (P2.1) | Correct |
| Appleton closed (P9.1) | Correct, in 2011 |
| Paid lunches (P19.2) | Correct |
| Math around 32% (P2.2) | Right for 2024-25; 27% in 2025-26 |
| A late bus or homework club (P2.3) | Neither found |
| Homeschoolers on teams (P3.1) | Yes, by written request |
| Private school busing (P11.1) | Only within the district |
| Sports only for grades 7–8 (P12.1) | No: grades 5–8 |
| Sports fees (P12.3) | None; pay-to-play rejected |
| Gifted programs (P16.1) | None found |
| About 250 high schoolers (P5.1) | Right: 263 |
| Building trades gone (P18.2) | Restarted in fall 2026 |
| Football or hockey co-ops (P20.2) | No football, no hockey, no co-op |
| Under 900 students (P6.1) | Right: 887, then 833 |
| A proposed and a default budget (P6.3) | Right: $467,678 apart in 2026 |
| A teachers' contract vote coming (P10.2) | No: it runs 2025–2028; the support staff contract failed |
| The deliberative session in February (P20.3) | Right: February 3, 2027 |

## Corrections and additions to earlier files

- **Jaffrey** (`../Jaffrey/`): its fact on Mascenic's open enrollment vote gave the district total (921–664) as New Ipswich's vote, following the Ledger-Transcript. The main session corrected it from Mascenic's signed results: New Ipswich 759–604, Greenville 162–60.
- **Peterborough and Jaffrey:** Mascenic's own records confirm that construction trades is taught at Mascenic (an instructor hired; the program running in September 2026).

## Library notes (for review, not applied)

- **Coverage table:** it lists Mascenic's kindergarten day as not found and its preschool as a state count only; this research fills both.
- **`raw/programs/cte-centers.csv`:** Mascenic is a Region 14 receiving district for automotive and construction trades under the December 2025 agreement.

## Browser pass

Not needed for the answers. Not retrieved:
- mascenic.org's own pages (a bot check), including Boynton's and athletics pages;
- NH DRA's apportionment worksheet (HTTP 403), so the inputs behind the 76.05% share come from news reports;
- the November 16, 2026 minutes, not yet posted.
