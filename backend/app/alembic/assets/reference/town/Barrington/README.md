# Barrington: Research for Ask NH Education Facts

Cited facts and figures for answering Barrington, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the ToLoad towns. Barrington is SAU 74, a one-district SAU:
- the Early Childhood Learning Center: preschool and kindergarten;
- Barrington Elementary School: grades 1–4;
- Barrington Middle School: grades 5–8.

Barrington has no high school. Students choose among Dover High, Oyster River High and Coe-Brown Northwood Academy under tuition agreements. Dover's and Oyster River's own facts are in `../Dover/` and `../Durham/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `early-childhood-and-elementary.md` | The preschool lottery (March 1, for children without IEPs), class sizes (about 19 in grade 2; limit 22), full-day kindergarten (8:45–2:55, free), Recreation care 7:00–5:30, Route 125 bus stops, meals with no money in the account, residency and guardianship papers, Chromebooks from grade 3, reading screening and Title I letters | 19 | 68 | 2 | 21 MB |
| `middle-school-and-home-education.md` | Required Tech Ed with real shop projects, a new computer science teacher, Algebra (one class), no gifted program, high school credit with the receiving principal's approval, phones banned all day, the bullying policy's old wording, sports eligibility, home education and EFA access after the 2026 laws | 12 | 83 | 0 | 25 MB |
| `high-school-choice.md` | Where students go (Oyster River 183, Dover 155, Coe-Brown 91), choice dates (Oyster River's lottery October 22–January 29; Coe-Brown's January 8 and February 11), Coe-Brown's deposit, Dover's career center, bus rides (up to 94–117 minutes), no late sports buses, special education at the three schools, Oyster River's data on Barrington students | 9 | 69 | 3 | 34 MB |
| `money-and-governance.md` | The default budget ($34,077,082) after the 2026 budget failed, health insurance (+34.8%), tuition (26.6% of the budget), the Dover (cost per pupil plus 8%), Oyster River (55 9th graders a year) and new Coe-Brown (2027–2030) agreements, enrollment (1,308, falling), taxes against Durham and Lee, capital needs | 8 | 60 | 5 | 30 MB |
| **Total** | | **48** | **280** | **10** | **110 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.18 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Barrington`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 26 partial, 2 from the site's data.
- **Topics:** no new topics.
- **Places:**
  - `district Barrington` 250, `district Coe-Brown Northwood Academy` 21, `town Barrington` 5, no place 2.
  - One each for `district Oyster River Coop` and `district Dover`.
- **Pending facts:** 6, citing draft 2027-28 budget documents and draft minutes.
- **Raw folders:** the four total 110 MB; each is under 100 MB.
- **Quotes:** 604 of 794 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The default budget, $34,077,082 | The 2027-28 budget considerations |
  | Health insurance up 34.8% | The same document and the March 9, 2026 board packet |
  | The 1,186 enrollment projection | The 2026-27 enrollment study |

## Premises checked

| Question says | What the sources show |
|---|---|
| A preschool lottery (P1.1) | Right, for children without disabilities |
| Large grade 2 classes (P1.2) | About 19 per teacher; the limit is 22 |
| Full-day kindergarten at a cost (P6.1) | Full day, no tuition |
| Bus stops on Route 125 (P8.1) | Three routes stop there; changes go to the superintendent |
| Chromebooks in grade 1 (P15.2) | 1-to-1 starts in grade 3 |
| Tutoring, late buses or free summer catch-up (P15.3, P18.2) | None found |
| A gifted program (P16.1) | None |
| High school credit in grade 8 (P16.2) | Allowed if the high school's principal approves first |
| Updated tech and shop (P20.2) | Mixed: the Tech Ed page is unchanged since 2019, but a computer science teacher was added |
| Yearly homeschool paperwork (P10.2) | Out of date since July 1, 2026 |
| One deadline for choosing a high school (P3.1) | No: each school has its own dates |
| Coe-Brown's deposit (P3.2) | Real; it covers class dues and the laptop deposit; no amount posted |
| Guaranteed seats at Oyster River (P9.1) | No: 55 9th graders a year, by lottery; Dover takes everyone who chooses it |
| A late sports bus (P14.2) | None |
| The new Dover contract's price (P4.2) | A formula: Dover's cost per pupil plus 8% |
| A three-year teachers' contract (P7.2) | Right: 2025–2028 |
| New houses filling the schools (P7.1) | Enrollment is still falling |
| Taxes lower than Durham and Lee (P19.1) | By assessed rate, between them; by full value, the lowest of the three |

## Corrections and additions to earlier files

- **`places.yaml`:** the Barrington → Oyster River note now gives the agreement's caps: 55 9th graders a year (68 from 2028-29), and 200 students in all, rising to 260 by 2032-33. The 2027–2030 Coe-Brown row was already there.

## Library notes (for review, not applied)

- **`high-school-tuition-options` 9 (Barrington)** lists the 2025–2027 Coe-Brown memorandum. The page now holds the 2027–2030 one, signed October 21–22, 2026.
- **`district-preschool` 6** gives hours of 8:25–11:00 and 12:00–2:45. The 2026-27 handbook gives 8:45–11:00 and 12:15–2:55.
- **The coverage table** lists Barrington's kindergarten day and cutoff as not found. Both are here now.

## Browser pass

The agents' blocked pages were:
- barrington.nh.gov and NH DRA (HTTP 403), so the 2026 tax rate, the town report and per-article 2026 results are missing;
- the elementary care page;
- Dover's records portal (script-only).

None is essential to the answers.
