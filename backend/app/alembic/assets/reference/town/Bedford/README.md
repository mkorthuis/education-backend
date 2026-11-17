# Bedford: Research for Ask NH Education Facts

Cited facts and figures for answering Bedford, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the profiles came with first names only, and the people are invented. The research is in the four files below, in the reference library's format, ready to load but not loaded.

Gathered November 16, 2026, alongside Hudson, Keene, Portsmouth, Goffstown and Laconia. Bedford is SAU 25, a one-district SAU: Memorial, Peter Woodbury and Riddle Brook for kindergarten to grade 4 (BEEP, the preschool, at Riddle Brook from 2026-27), McKelvie Intermediate School (5–6), Ross A. Lurgio Middle School (7–8) and Bedford High School (9–12), with Lurgio and the high school on the Nashua Road campus. Bedford students may take career programs at the Manchester School of Technology.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools-and-families.md` | Checking an address (ZIP 03110 and the town's property database), free full-day kindergarten and its 2025 vote, New Morning after-school care ($22 a day), policy JJJ access for home-educated, EFA, charter and private students, home education since July 1, 2026, English learner support, the PTG, class-size guidelines (20 ± 2 for K–3) and enrollment, BEEP | 13 | 66 | 1 | 22 MB |
| `mckelvie-lurgio-and-getting-to-school.md` | The move to McKelvie (282 fourth graders, 296 fifth graders), math options, two bell-time waves and shared bus routes, the August 2026 phone policy and its survey, choosing grade 9 courses, McKelvie against Founders and Catholic schools, returning from a charter, bullying reports and deadlines, the Nashua Road campus's emergency plan and reunification at Saint Anselm, IEP caseloads | 13 | 125 | 6 | 19 MB |
| `high-school-and-pathways.md` | IB courses for everyone and the Diploma (10–15% of juniors and seniors), equal weighting of IB, AP and honors, exam fees and fee help, sign-up deadlines, AI rules, mental health (the 2025 youth risk survey), MST tuition, dual enrollment, test results by income group, paths besides four-year college | 11 | 84 | 3 | 18 MB |
| `money-buildings-and-staff.md` | The rejected FY2027 budget and the $97.1 million default, $673,649 in cuts, the state tax cap's effect (59.2%, short of 60%), the bond paid off in FY2030 and the long-term capital plan, the teachers' and support staff contracts, para pay, IEP counts and staff, the technology budget, lead tests, community use of buildings | 10 | 92 | 6 | 18 MB |
| **Total** | | **47** | **367** | **16** | **76 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.23 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Bedford`). All 16 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 28 full, 32 partial.
- **Topics:** one new topic was added to `../shared-topics.md`: `ap-and-ib-exam-fees-and-deadlines`.
- **Places:** `district Bedford` 348, `town Bedford` 12, no place 6.
- **Places for the backend:** `places.yaml` has no Bedford rows, and none are needed: Bedford runs every grade, and MST is a career-program arrangement.
- **Raw folders:** all under 100 MB. The bus route sheets list stops by house number, so the agent saved a times-only table instead.
- **Quotes:** 930 of 1,083 quoted passages found word for word in the cited raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | FY2027 budget rejected, 2,032 to 2,158; default $97,136,083 | Election results, March 10, 2026; the warrant |
  | Full-day kindergarten approved 2,516 to 2,502 (March 11, 2025) | 2025 annual report |
  | Paraprofessional pay $17.65 (step 0) to $32.65 (step 30) in 2026-27 | The 2026–2029 support staff agreement, Appendix C (page image) |
  | MST tuition budgeted at $79,800; $128,301 spent in FY2025 | BHS FY2027 budget detail |
  | Question 2: 59.2% yes | The site's Question 2 data (6,719 to 4,633) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Free full-day kindergarten, or a paid second half (P1.2) | Free: approved March 11, 2025 ($885,100), funded in the budget |
| Memorial's pre-K only for special education (P19.1) | BEEP moved to Riddle Brook for 2026-27 and takes typically developing children for tuition |
| New houses raising K–4 class sizes (P16.3) | Not supported: preschool–grade 4 enrollment fell from 1,551 (2018-19) to 1,321 (September 2026) |
| Every child merges at McKelvie (P2.1) | Right |
| McKelvie's later morning (P2.3) and staggered starts (P7.1) | Later, yes (8:50); two waves, not three: McKelvie and Lurgio share hours |
| "Thousands" at the Nashua Road campus (P17.2) | Overstated: about 1,950 students |
| Early AP and IB exam sign-ups (P13.2) | Mostly right: BHS closed November 8, before the College Board's November 13 and IB's November 15 deadlines |
| AI flagged as cheating (P13.1) | Not as stated: AI is allowed when a teacher permits it; the handbook's AI section reads "TBD" |
| Dual enrollment without cost (P4.3) | Possible through the community colleges' two free courses a year; the district doesn't pay for outside courses |
| Athletic fees (P18.3) | No participation fee found; AP ($99) and IB ($127) exams are paid for families on free or reduced meals |
| Outside tutors explain scores (P12.3, P18.1) | No data measures private tutoring; can't be settled |
| The budget rising while enrollment falls (P6.1) | Right; voters rejected the FY2027 budget, so the default applies |
| A move away from commercial textbooks (P6.3, P8.2) | Not supported by any source found |
| "Another big bond" (P6.2) | No new bond proposed; the middle/high school bond ends in FY2030 |
| A cut to the technology budget (P15.1) | Right |
| Deferred maintenance (P20.1) | Partly: some building projects were deferred in the post-vote cuts |
| A high school pool (P20.2) | Not confirmed: no district document lists one |
| "Modest savings" (P20.3) | The phrase wasn't found in 40 minutes or the budget papers |
| Riddle Brook homes selling for more (P16.1) | Can't be settled from public data |
| Filing homeschool paperwork with SAU 25 (P10.2) | Nothing is filed since July 1, 2026 unless a family uses district classes or withdraws a child; Bedford's policy still describes the old rules |

## Corrections and additions to earlier files

None to earlier towns. Merrimack's `research-school-transitions` facts and its table of Bedford's grades 3–6 results already answer the research side of P2.1. Manchester's Founders figure ("about 18–20 students" a class) and the site's and NCES's class-size numbers measure different things, as the McKelvie file notes.

## Library corrections

Applied November 16, 2026 to both library copies (backend commit `c7c868a`), except those marked for review:

- `district-practices.md`, `kindergarten-day-length` 4 (Bedford): its note gives a news count of 2,515 to 2,502; the official result is 2,516 to 2,502.
- `district-practices.md`, `district-preschool` 9 (Bedford): it gives a 90% free or reduced-meal discount from the 2026-27 tuition agreement; BEEP's 2026-27 handbook says a 50% waiver. The two district documents disagree; the fact could name both. **Outcome:** the fact now gives both figures and says the district's documents are inconsistent (backend commit `a0a34d0`).

## Not retrieved

The browser pass (November 16, 2026) found NH DRA's 2026 tax rates only as a PDF the site refuses to download; the Bedford Citizen and IB's pages weren't opened (news and IB's general pages add little to what BHS posts). Still missing:


- The Bedford Citizen (HTTP 403 after one search).
- IB's own pages (HTTP 403).
- NH DRA's 2026 tax rate (HTTP 403), for the school share of the $14.73 rate.
- The district's School Finder street list and BHS's course database (a Google sign-in; can't be opened without an account), the town's recreation portal, and Census commute data (the API now needs a key).
