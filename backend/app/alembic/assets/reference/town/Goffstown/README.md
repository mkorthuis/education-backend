# Goffstown: Research for Ask NH Education Facts

Cited facts and figures for answering Goffstown, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the four files below, in the reference library's format, ready to load but not loaded.

Gathered November 16, 2026, alongside Hudson, Bedford, Keene, Portsmouth and Laconia. Goffstown is in SAU 19 with New Boston: Glen Lake School (preschool and half-day kindergarten), Bartlett Elementary (Pinardville) and Maple Avenue (the village) for grades 1–4, Mountain View Middle School (5–8) and Goffstown High School (9–12). New Boston sends grades 7–12 under an AREA agreement for 2024–2034, Hooksett students may attend the high school by petition, and Goffstown students take career programs at the Manchester School of Technology. SAU 19-wide facts use `place: sau 19` and sit in these files; a later New Boston study will find them here.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-special-education.md` | Half-day kindergarten at Glen Lake and why, YMCA care (Glen Lake wait-listed), Bartlett against Maple Avenue (Bartlett led in 2026), reading help, the Glen Lake preschool and its tuition places, aides in the FY28 budget, out-of-district tuition, English learner services and interpreters, nurses, no gifted program, the state's gifted-and-talented reporting law | 14 | 69 | 5 | 79 MB |
| `mountain-view-high-school-and-mst.md` | AP (20 courses, 89% scoring 3 or more), honors and Early College through Manchester Community College, Mountain View's math tracks from grade 7, college outcomes, MST (two-year programs, the bus line, tuition shares), athletic costs paid by the district, eligibility at report cards, class sizes in grades 5–8, the four diplomas from the class of 2030, FAFSA help | 9 | 76 | 5 | 37 MB |
| `getting-to-school-and-choices.md` | Ride times from every 2026-27 route sheet, bell times (Mountain View 8:25–3:18), the 5:00 late bus, moves within Pinardville, delays and early release notice, phones, home education access (up to four courses a term), EFAs and sports, homeschoolers and MST, guardianship paperwork, counselors, bullying policy under revision, no buses to private schools | 9 | 88 | 1 | 31 MB |
| `money-buildings-and-governance.md` | The $21.75 tax rate and the school share of the increase, the lowest cost per pupil of NH's K–12 districts, Question 2 (61.4%) and the district's cap math, the superintendent's succession, New Boston's AREA terms and tuition, no bonded debt and the town's capital plan, the teachers' contract and applicant pools, school resource officers, where to see board votes | 11 | 106 | 4 | 72 MB |
| **Total** | | **43** | **339** | **15** | **219 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.10 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Goffstown`). All 15 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 35 full, 25 partial.
- **Topics:** one new rule topic was added to `../shared-topics.md`: `gifted-and-talented-rules` (RSA 189:29-b's yearly report; the shared `district-enrichment-and-advanced-learners` is for a district's own programs).
- **Places:** `district Goffstown` 305, `town Goffstown` 14, `sau 19` 10, `district New Boston` 5, no place 3, `town Manchester` 1.
- **Places for the backend:** New Boston's row (grades 7–12, AREA, July 1, 2024 to June 30, 2034) and Hooksett's petition row (2023–2028) match what the agents found; nothing to change.
- **Draft facts:** six notes are flagged, among them one bell-time fact resting on draft minutes (the school pages match).
- **Raw folders:** all under 100 MB (`raw/elementary/` is 79 MB).
- **Quotes:** 747 of 876 quoted passages found word for word in the cited raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 tax rate, $21.75 | The town's notice of the DRA-approved rate; the district's FY28 presentation packet |
  | New Boston's 2026-27 tuition, $19,842 a high school student | New Boston's FY2027 deliberative session slides |
  | MST transportation, $38,645 a year | FY28 general fund budget with notes |
  | Out-of-district tuition proposed for FY28, $1,659,452 | FY28 budget and presentation packet |
  | AREA renewal, 1,610 to 269 (March 8, 2022) | 2022 Goffstown Annual Report, Article 4 |
  | Question 2: 61.4% yes | The site's Question 2 data (4,691 to 2,949) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day kindergarten at Glen Lake (P1.1) | Wrong: half-day; the board cites no cafeteria, gym or space, and keeps 8 half-day sessions for 2027-28 |
| Bartlett's scores "much lower" than Maple Avenue's (P2.1, P12.2) | Out of date: true through 2024; in 2026 Bartlett led in math (63% to 57%) and reading (60% to 58%) |
| Glen Lake preschool "mostly for kids with delays" (P16.1) | Partly: a special education preschool that also takes up to 56 typically developing children for tuition |
| A gifted program (P16.3) | None found; the policy is one sentence from 2000 |
| Full-time RNs in every building (P14.3) | Right |
| A $21.75 rate (P3.1) | Right; about 87% of the $0.87 increase was the local school rate |
| Spending less per student (P3.2) | Right: the lowest FY2025 cost per pupil of the 54 K–12 districts |
| A tax cap on the schools (P3.2, P8.3) | Question 2 passed in Goffstown (61.4%, uncertified); a 2024 local petition failed |
| A new superintendent (P3.3) | Right: the superintendent retires in 2027; the assistant superintendent is the sole finalist |
| Building bonds coming (P12.3) | None on a ballot and no bonded debt; the town's plan lists a new elementary school around 2031-32 |
| Resource officers in every elementary school (P15.2) | Wrong: two officers cover all five schools |
| New Boston students crowding the schools (P7.1) | Not shown: 157 at Mountain View and 307 at the high school are budgeted |
| When the AREA agreement comes up (P15.3) | It runs to 2034; an extension vote would come about 2032 |
| A daily bus to MST and two-year programs (P5.1, P5.2) | Budgeted ($38,645) and right; cosmetology is three years |
| "28 to a room" (P19.2) | Not as an average: Mountain View's projections are 20–23; policy caps grades 7–12 at 28 |
| A warning before sitting out (P10.2) | None: eligibility is set when report cards come out, with one waiver hearing per career |
| One or two classes for homeschoolers (P11.1) | Up to four a term |
| Buses to private schools in Manchester (P19.3) | None |
| A 3:30 pickup and a late bus for 5th graders (P17.3) | Dismissal is 3:18; the 5:00 late bus takes any student in a supervised activity |
| Middle schoolers starting too early (P14.1) | Mountain View starts at 8:25, five minutes before the pediatricians' 8:30 |
| Routes combined for a driver shortage (P18.3) | Not confirmed by any source |

## Corrections and additions to earlier files

None to earlier towns.

## Library corrections

Applied November 16, 2026 to both library copies (backend commit `c7c868a`), except those marked for review:

- `district-practices.md`, New Boston fact 60: New Boston's FY2027 budget lowers its Goffstown High count from 338 to 307 and sets 2026-27 rates of $18,357 (Mountain View) and $19,842 (high school) (`money-buildings-and-governance.md`, `district-tuition-contracts` 10).
- `district-practices.md`, Goffstown's `budget-form-and-vote-dates` fact: it says no page gave the 2026 deliberative session date; it was February 2, 2026 at the high school theater (`district-board-and-public-input` 11).
- `district-practices.md`, `kindergarten-day-length` 16 (Hampstead): Goffstown's superintendent said in March 2026 that Hampstead has no full-day kindergarten; the library says Hampstead approved a one-year pilot for 2026-27. Worth checking against Hampstead's own pages. **Outcome:** both are true at their dates (the pilot was approved after the March reports); no change.
- The library's `bullying-definition` topic ties the 2026 bullying changes to 2026 chapter 205; Goffstown's policy committee minutes attribute them to HB 1817. Worth confirming which bill amended RSA 193-F:4. **Outcome:** 2026 chapter 205 is HB 131, "relative to bullying and cyberbullying prevention" (approved July 2, 2026; official chaptered text saved at `additional-data/raw/state-issues/students-hb-131-bullying-law/hb131-2026-chaptered-text.html`). The Goffstown minutes' "HB1817" is a mix-up with the EFA-access bill; the library's chapter citation is right. Added November 16, 2026: the library topic `students-hb-131-bullying-law` (backend commit `c473aa4`), and a fact here on where Goffstown's JICK stands against HB 131 (`getting-to-school-and-choices.md`, `district-conduct-policies` 8).

## Not retrieved

- NH DOE's gifted-and-talented report pages (HTTP 403); the reports themselves are posted as files, not pages.
- The athletic participation fee amount (policy requires one; no page gives it), MST bus times, Mountain View's advanced math entry criteria, and the midday kindergarten bus schedule.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 6 saved bus and transportation copies (6 in all; schools, child care centers, businesses and other public places keep theirs).
- The state's resident birth, marriage and death lists removed from 3 saved town report copies (headings and record counts kept); 3 report PDFs deleted.
