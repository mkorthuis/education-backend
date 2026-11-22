# Keene: Research for Ask NH Education Facts

Cited facts and figures for answering Keene, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the five files below, in the reference library's format, ready to load but not loaded.

Gathered November 16, 2026, alongside Hudson, Bedford, Portsmouth, Goffstown and Laconia. Keene is the largest district in SAU 29 (with Chesterfield, Harrisville, Marlborough, Marlow, Nelson and Westmoreland): Jonathan Daniels School (preschool), Franklin, Fuller, Symonds and Wheelock for kindergarten to grade 5, Keene Middle School (6–8) and Keene High School (9–12) with the Cheshire Career Center. SAU 29's towns and Stoddard, Sullivan and Surry send students to Keene Middle and High under 20-year AREA agreements from July 1, 2026. SAU 29-wide facts use `place: sau 29` and sit in these files; a later SAU 29 town will find them here.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools-and-daily-life.md` | How the four schools differ, the street directory and zone requests, the YMCA's after-school program (Project KEEP ended) and the city's, reading intervention, bus walk limits, GreatSchools' lag, elementary Spanish's vacancy, guardianship paperwork, paper copies, recess, early release and snow days, Jonathan Daniels, the Cheshire Center Preschool (corrected in review), open enrollment under policy JFAB | 16 | 109 | 1 | 40 MB |
| `middle-high-and-career-center.md` | AP and honors STEM (AP Chemistry hasn't run since 2022-23), AP participation against 15 other NH high schools, dual enrollment, Career Center programs and the grades they start, the student electrician's license, late buses and homework club, smaller programs at KHS, computer science, scorecards, transfer credits and NHIAA rules | 13 | 91 | 4 | 42 MB |
| `student-support-and-staff.md` | Evaluation volume and contracted evaluators, vacancies by position, Wheelock's paras and special education posting, the KMS collaborative programs, translation, the bullying notice rule (48 hours, buses included), para and bus driver hiring through the contractor, behavior support | 6 | 90 | 2 | 22 MB |
| `choices-and-adult-learning.md` | Gathering Waters and MC2 (special education stays Keene's responsibility), policy JJJ access for charter, private and home-educated students, St. Joseph Regional's tuition and EFAs, Our Lady of Mercy, home education since July 1, 2026, Keene Community Education's free English, HiSET and diploma classes, River Valley's accounting certificate | 8 | 83 | 0 | 45 MB |
| `money-sau29-and-buildings.md` | The FY2027 budget (+3.4%) and the school tax (+12.74%) with falling adequacy aid, discretionary spending (4.1%), Question 2 (45.7% yes), the AREA tuition formula and 2026-27 rates, KHS's safety plan and how it's paid for, the one bond (to 2039), the 2026 revaluation, the SAU 29 towns' elementary schools | 9 | 70 | 6 | 47 MB |
| **Total** | | **52** | **443** | **13** | **196 MB** |

`brief.md` is the brief the research agents worked from. Five agents used about 2.47 million tokens.

## Checks

- **Parser:** all five files pass the backend's parser (`tools/check_town.sh Keene`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 29 full, 31 partial.
- **Topics:** all shared or library topics; no new ones.
- **Places:** `district Keene` 357, `town Keene` 40, `sau 29` 16, `district Gathering Waters Charter School` 12, `district Making Community Connections Charter School` 8, no place 6, `district Granite Valley Preparatory Chartered Public School` 1.
- **Places for the backend:** the Keene rows in `places.yaml` (Chesterfield, Harrisville, Marlborough, Marlow, Nelson, Stoddard, Sullivan, Surry and Westmoreland, from July 1, 2026 to June 30, 2046) match what the agents found; nothing to change.
- **Draft facts:** two notes are flagged.
- **Raw folders:** all under 100 MB.
- **Quotes:** 1,134 of 1,281 quoted passages found word for word in the cited raw copies.
- **Corrected in review:** the elementary agent wrote that no "Cheshire Center Preschool" existed; the choices agent found it. `town-child-care` 4 now describes it: a half-day laboratory preschool inside Keene High run by the Career Center's Careers in Education program, 8:45 to 11:00, $950 a year, not in the state's licensed child care list (raw: `raw/elementary/cheshire-center-preschool.txt`). The summary and P1.3's row were changed to match.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Question 2: 4,247 yes, 5,049 no | The city's ward tally; the site's Question 2 data |
  | 2026-27 AREA tuition, $18,842 (KHS) and $16,182 (KMS) | The tuition rate memo and worksheet |
  | Operating budget, $82,426,334 | Finance Committee minutes, January 10, 2026; the public hearing presentation |
  | Bond principal outstanding July 1, 2026, $11,425,431 | FY2027 debt service page |
  | St. Joseph Regional's 2026-27 tuition, $7,750 (K–8) | The school's tuition page |

## Premises checked

| Question says | What the sources show |
|---|---|
| The Question 2 cap squeezing "the 4% that isn't locked in" (P1.2, P18.1) | The 4% is right (the district calls $3.37 million, 4.1%, discretionary); the cap failed in Keene (45.7%) and SAU 29-wide, so none applies for FY2028–FY2029 |
| The school tax rising while enrollment shrinks (P2.1) | Right: the FY2027 school tax rose 12.74%, mostly from lost adequacy aid and a smaller surplus; K–12 enrollment fell from 3,424 to 2,857 since 2019-20 |
| KHS "safety renovations" on top of the budget (P2.2, P14.3) | Partly: a safety plan was presented October 6, 2026; its first $400,000 came from a building trust fund, and no bond is planned |
| Tuition towns not covering the cost (P2.3) | Not supported: the formula is the high school's net cost per student plus a building charge; the CFO calls it "break even" |
| "Benjamin Franklin Elementary" and a 2:40 pickup (P3.1) | Right |
| "Cheshire Center Preschool" (P1.3) | Real: Keene High's lab preschool. No preschool waitlist is posted |
| Full-day pre-K (P16.3) | Jonathan Daniels is half-day; no full-day plan was found |
| One elementary Spanish teacher for 400 students (P10.2) | A vacancy, not a cut: two posts, one empty in fall 2026 |
| A remote evaluation idea (P6.1) | No minutes mention it; the district said some contracted services are only virtual and is looking at a "new program" to shorten evaluations |
| Career Center only from junior year (P5.1) | Partly wrong: most programs start in grade 10; some in 11 or 12 |
| Bus walking limits (P3.3) | Right: half a mile for K–3, one mile for grades 4–5, by distance, not income |
| Different early release and snow rules (P16.2) | One calendar and the same closings; only the clock differs |
| An annual homeschool evaluation (P13.3) | Out of date: repealed July 1, 2026 (Keene's policy IHBG still describes it) |
| A medical billing or bookkeeping certificate at Keene Community Education (P17) | Not offered there; River Valley's Keene center has an accounting certificate |
| No busing for charter students (P8.3) | Can't be confirmed: state law requires it on regular routes; no source shows Keene's practice |
| GreatSchools ratings (P7.2) | Calculated in 2025 from spring 2024 results; the site's 2026 results differ a lot |
| No budget dashboard (P18.3) | Partly: budget books, a Q&A, scorecards and a video, but no single page tying spending to results |

## Corrections and additions to earlier files

None to earlier towns.

## Library corrections

Applied November 16, 2026 to both library copies (backend commit `c7c868a`), except those marked for review:

- `district-practices.md`, `kindergarten-day-length` 22 (Keene) says no district page states full or half day; SAU 29's 2026-27 hours give one 8:00–2:40 schedule for each Keene elementary school.
- `additional-data/raw/programs/cte-centers.csv`: the Cheshire Career Center row quotes "one of 25 regional ... centers"; the 2026-27 catalog says "one of twenty-eight." **Outcome:** the CSV quotes the contact page correctly; the counts differ by source and year (Keene's pages say 25 and 28; NH DOE lists 26 in New Hampshire plus 5 in Vermont); no change.

## For the site's data

`recommended-improvements.md` A8 item 6: school records for Our Lady of Mercy Academy, St. Joseph Regional, Granite Valley Preparatory, Gathering Waters and MC2 (wrong websites, a moved upper school, a duplicate record).

## Follow-up (November 16, 2026)

- **The teachers' contract** (Keene Education Association, 2023–2027) was saved through a browser from the labor board's new host and read by OCR: `student-support-and-staff.md`, `district-classrooms-and-staff` 24–25 (the 2026-27 salary schedule and prep time). Its 2025-26 schedule shows NH DOE's bachelor's maximum is transposed ($73,729 for $73,279); the site keeps NH DOE's figure (`recommended-improvements.md` A8 item 7).
- **The paraprofessionals' contract** (2025–2028) is listed at https://mm.nh.gov/files/uploads/pelrb/docs/cba-keene-paraprofessionals.pdf; Chrome blocked a second automatic download from that host, so it wasn't read.
- **MC2's transportation policy:** MC2's own site returns "File not found" (and a gateway time-out) for it; the file is missing on their server, not blocked.
- **NH DOE's district determinations:** NH DOE posts only statewide data and template letters, not each district's determination or evaluation timeliness.

## Not retrieved

The browser pass (November 16, 2026) opened what it could. NH DRA's 2026 tax rates are a PDF the site refuses to download; MC2's policies are PDFs behind a download plugin; NH DOE's page lists statewide fact sheets and district determinations only as PDFs; PELRB's contracts are PDFs. None could be read, so all four remain:


- NH DRA's 2026 tax rate for Keene (HTTP 403).
- MC2's document library (HTTP 403).
- NH DOE's special education evaluation-timeliness data (HTTP 403).
- PELRB's copy of the Keene teachers' contract (HTTP 403).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 8 saved bus and transportation copies (174 in all; schools, child care centers, businesses and other public places keep theirs).
