# Rollinsford: Research for Ask NH Education Facts

Cited facts and figures for answering Rollinsford, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the five files below, in the reference library's format. These files are the first research on the Marshwood schools (MSAD 35) and on SAU 104.

Gathered November 22, 2026, in the fourth ToLoad batch. Rollinsford is its own district in its own SAU (SAU 104; it left SAU 56 with Somersworth):
- **Rollinsford Grade School** (preschool to grade 6, with multi-age classrooms; 147 students in September 2026), run by the Rollinsford School District, which became an open enrollment school for 2026-27;
- grades 7–12 go to **Marshwood Middle School** (Eliot, Maine) and **Marshwood High School** (South Berwick, Maine) under a tuition agreement with Maine's MSAD 35 (approved October 10, 2024, for 2025 to 2030; about 130 students), with career programs at the Sanford Regional Technical Center in Maine and the Dover Career Technical Center in New Hampshire.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `rollinsford-grade-school-and-families.md` | No general public pre-K ("grades K-12 and Special Education Pre-K"; the nearest licensed programs are 9.4 to 12.6 minutes away in Somersworth and Dover, derived), Horizons before and after care 7:00 to 5:30 ($100 to $285 a month, 30% off for free or reduced-price lunch families, "not registered as a daycare"), a written request to the Superintendent's office (policy EEA) and a waiver to change an afternoon drop-off, a full-day kindergarten with a September 30 cutoff and a waiver process, lunch $3.35 and breakfast $2.10, open enrollment for 2026-27 (up to two students in grades 1 to 6; passed 455 to 223) | 17 | 72 | 3 | 11 MB |
| `rollinsford-grade-school-support-and-choices.md` | SAU 104 "oversight" but the school's own special education, speech and occupational therapy staff (speech 1.00 FTE, nurse and counselor 1.00 FTE each), no gifted program reported to the federal civil rights survey, Seacoast Charter arts-integrated (not Montessori), Seacoast Christian School in South Berwick, Maine (not Dover), no town bus to Dover, band, chorus, drama and intramurals, policy JJJ giving homeschool and EFA students the same access and fees, policy IHBG (2019) still describing the repealed annual evaluation, the special education contract with MSAD 35 expiring after 2026-27 | 13 | 68 | 1 | 11 MB |
| `marshwood-middle-from-rollinsford.md` | Calendars matching except December 23 and January 15, a 9:00 start on Thursdays, RGS snow-day decisions that "align with MSAD 35," Rollinsford students entering in grade 7 (Marshwood's own in grade 6; Step Up Day June 5, 2026), buses reaching the middle school at 7:10 and leaving at 2:30, a late bus Monday to Thursday with a Rollinsford stop at about 4:48 (Rollinsford pays for it) despite MSAD 35's statement that its students "may not travel across state borders" on buses, no page saying whether New Hampshire or Maine special education rules apply, a grade of 21 sixth graders against 149 to 172 per grade at Marshwood Middle | 10 | 62 | 4 | 12 MB |
| `marshwood-high-from-rollinsford.md` | 24 programs at Sanford Regional Technical Center and 3 at Dover's center, an AP count of 15, 12 or 13 depending on the page, the Class of 2026 SAT of 541 reading and writing and 523 math with 59% going to four-year colleges, free dual-enrollment credits for New Hampshire students only through York County Community College, UNH in-state tuition following the parent's New Hampshire residence, five counselors, St. Thomas Aquinas at $20,566 plus a $650 fee, Berwick Academy with no AP-labeled courses, no alternative diploma, summer school or driver's education found | 12 | 68 | 5 | 14 MB |
| `money-and-governance.md` | School tax (local plus state) of $4,871,631 (2023), $5,500,904 (2024, +12.9%), $5,930,640 (2025, +7.8%) and $5,955,681 (2026, +0.4%) with the 2026 rate $12.04, the Marshwood base rate of $14,143.19 (131 students, $1,852,758; $2,231,035 in all; up 6.3% for 2027-28), SAU 104 about $87,909 above staying in SAU 56 (the district's own figures), the 1936 school on the National Register with no item rated "poor," the deliberative session on February 2, 2027 | 10 | 78 | 12 | 24 MB |
| **Total** | | **62** | **348** | **25** | **72 MB** |

`brief.md` is the brief the research agents worked from. Five agents used about 2.7 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all five files pass the backend's loader, run against the loaded towns plus Rollinsford. All 25 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 28 full, 32 partial.
- **Topics:** one new topic, added to `../shared-topics.md`: `college-residency-for-tuition-and-aid`.
- **Places:** `district Rollinsford` 214, `maine MSAD 35` 86, `town Rollinsford` 19, no place 12 (including the 2 Berwick Academy facts), `sau 104` 10, `district Diocese of Manchester` 4, `district Seacoast Charter School` 2, `district Portsmouth Christian Academy` 1. Berwick Academy isn't in `places.yaml`; adding it would imply an arrangement the district doesn't have.
- **Pending facts:** 25: the loader counts any note that contains "draft" or "pending"; many cite draft minutes (November 2026) or quote calendar wording ("pending snow days", "draft calendar"). Check them before loading.
- **Raw folders:** each under 100 MB (money is 24 MB). The 62 saved PDFs are handbooks, a budget book (a scan; the agents read pages as images), policies, calendars and state and Maine sheets. Nine page images are saved: two calendars, budget pages (staffing, Marshwood tuition and special education rates) and ballot result pages. None is a route sheet or a roster. The First Student route sheet for the grade school is not saved (it lists homes by house number); the Marshwood runs are cleaned text.
- **Privacy:** the address scan, including the `--raw` pass, finds only First Student's yard address in Somersworth, schools, the town hall and the American Legion. Minutes, newsletters and the Summer 2026 newsletter have student and resident names removed (two students named as honor society inductees were not kept).
- **Quotes:** 686 of 818 quoted passages found word for word in the raw copies (the misses are mostly table text read from scans and budget-book OCR).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | School tax (local plus state) of $4,871,631, $5,500,904 and $5,930,640 for 2023 to 2025 | The site's `town_school_tax` table (local plus state education tax) |
  | The 2026 school rate of $12.04 (local $10.82 and state $1.22) | The budget report of November 12, 2026 |
  | Open enrollment article: 455 yes and 223 no | The ballot results page, read as an image (crop of article 11) |
  | The Marshwood base rate of $14,143.19 for 2026-27 and "an increase of $346 per student" | The FY2027 budget book's OCR |
  | Marshwood Middle at 626 H.L. Dow Highway, Eliot | The school's own site (a correction to the brief and to `places.yaml`) |

## Premises checked

| Question says | What the sources show |
|---|---|
| A public pre-K at the grade school (P1.1) | No general pre-K; the district's budget says "grades K-12 and Special Education Pre-K" |
| Care before and after school | Horizons runs 7:00 to 5:30 but says it is "not registered as a daycare"; the school nurse is not available during its program |
| Kindergarten registration, day and age cutoff (P1.2) | Full day; a September 30 cutoff with a waiver process |
| Lunch free for everyone | No: $3.35 lunch and $2.10 breakfast, with free or reduced-price meals by yearly application |
| A Spanish speaker or Spanish newsletters (P7.1, P7.2) | None found |
| "About 140 kids" at the grade school and taxes that "jump again" (P4.1) | 153 (October 2024) and 147 (September 2026), but the school tax also pays for about 130 to 134 students at Marshwood, so about 277 to 296 in all |
| The tax jump (P4.1) | True for 2024 and 2025 (+12.9% and +7.8%), not for 2026 (+0.4%) |
| The contract with Marshwood is "up" (P4.3) | Two contracts: the tuition agreement runs 2025 to 2030; a separate two-year special education services contract is up for renewal in 2026 |
| The SAU, building age, deliberative session and enrollment | Confirmed or clarified: SAU 104 costs about $87,909 more than staying with SAU 56 by the district's own figures; the school was built in 1936; deliberative session February 2, 2027 |
| 8/10 on some school sites and a "C+" on others (P13.2) | 8/10 confirmed; Niche could not be read (HTTP 403); the 8/10 versus 4/10 gap comes partly from different test years |
| A "Montessori or arts-focused" school (P16.2) | Seacoast Charter is arts-integrated and never says Montessori |
| A Marshwood middle school in South Berwick (the brief; P8.3 asks about Eliot) | It is in Eliot; Marshwood Great Works School is in South Berwick |
| The late bus back to the Legion, and robotics (P6.2) | Yes, Monday to Thursday, with a Rollinsford "Legion Turnaround" stop at about 4:48; MSAD 35 also says its students may not ride across state lines; no robotics club is in the 2026 catalog or the school profile |
| AP at Berwick Academy (P10.1) | No AP-labeled courses; a 2017 post describes a shift to "Pinnacle" courses |
| An alternative diploma, summer school, credit recovery or driver's education at Marshwood (P17.1 to P17.3) | None found |
| Dual enrollment only through Maine colleges (P20.1) | No: but New Hampshire students' 18 free credits are offered only through York County Community College, which conflicts in part with Maine's rule limiting free credits to Maine residents |
| Homeschool paperwork (P11.2) | Rollinsford's policy (2019) still describes the annual evaluation the state repealed |

## Corrections and additions to earlier files

Applied:
- **Backend `places.yaml`, the Rollinsford–MSAD 35 row (uncommitted):** the note said "Marshwood Middle and High (South Berwick, Maine)"; it now says Marshwood Middle (Eliot, Maine) and High (South Berwick, Maine).

Not applied (additions for other files):
- **Dover `high-school-and-ctc.md`, cte-center-programs 1:** says Dover CTC offers 19 programs; Marshwood's pages give its students three of them (cte-center-programs 6 in Rollinsford's Marshwood High file).
- **Dover's policy IHBG note** says the policy "still describe[s]" the pre-July 2026 homeschool process; Rollinsford's IHBG has the same gap.
- **Somersworth `support-and-choices.md`, table `efa_applicants_somersworth_area_2026_27`:** shows the same Rollinsford numbers (33, 31, 21, 4 and 2) as Rollinsford's town-school-options-nearby 1.
- **Somersworth `town-child-care` 1–3 (Head Start at Idlehurst, 18 funded places):** applies to Rollinsford families only if Head Start accepts them; eligibility is by family income, not by town.

## Library notes (for review, not applied)

- **`kindergarten-day-length` and `district-preschool`** have no Rollinsford entries because the school's pages gave neither (`additional-data/raw/districts/not-found-notes.csv`); this research fills both. `kindergarten-registration` fact 73 ("no start or end dates") is consistent with the new facts.
- **MSAD 35's First Student phone number:** (603) 692-4406 on MSAD 35's page and 603-694-4406 in the Marshwood handbook.

## Browser pass

Not done. Not retrieved:
- Maine's Chapter 101 (HTTP 403), NH DOE (403: State Board approval of the 2024 renewal), the NH DMV driver education page (403), York County Community College's early college page (403), Husson's ECAP page (404), Niche and Homes.com (403), Census and South Berwick home values (403 or needs a key), the SAU feasibility study (404), the Canva clubs page, the Reading Intervention slides (401) and the PTO's Facebook page;
- the Marshwood agreement's text (minimums and withdrawal terms), any written transition plan or 2027 dates, how a 504 plan is handed from the grade school to the middle school, whether Dover's or Somersworth's preschools or Head Start take Rollinsford children, the NH Child Care Scholarship income table, who pays tuition and transportation for a Rollinsford student at either career center, how many Rollinsford students attend Marshwood, whether Great Bay's free courses reach a New Hampshire resident at a Maine school, the town's own budget, and a nut-free rule or allergy plan (not found).
