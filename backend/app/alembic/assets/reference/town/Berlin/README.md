# Berlin: Research for Ask NH Education Facts

Cited facts and figures for answering Berlin, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the sixth wave of the ToLoad towns. Berlin is a city and SAU 3, and the Berlin School District runs:
- Berlin Elementary School: preschool to grade 5;
- Berlin Middle School and Berlin High School: grades 6–12, sharing one building at 550 Willard Street;
- a regional career and technical center, which Gorham uses as its own vocational program.

Dummer and Milan send grades 7–12 to Berlin. The City Council appropriates the school budget. SAU 3's site showed a bot check to the agents, so the main session read its pages in Chrome.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | Project Youth (K–5 2:40–5:40, grades 6–8 2:20–5:00), busing rules (free over 0.6 mile for K–5 and one mile for 6–8; passes sold by month), the special education preschool and Head Start, meals (no community eligibility), a contracted speech therapist ($132,000), counselors by grade band | 15 | 49 | 2 | 27 MB |
| `middle-high-and-support.md` | Grades 6–12 in one building, scores (20–23% math), the 2026-27 Program of Studies (French and Spanish I–IV, six AP courses, three free VLACS credits, 26 credits to graduate), the Enriched Learning Center, North Country Charter Academy's Berlin site, Catholic and Christian schools nearby, the bullying policy | 15 | 71 | 1 | 24 MB |
| `career-center-and-college.md` | Eight CTE programs and the credentials they prepare for (AWS welding, ASE G1, LNA), nine Early College courses (two free a year, then $150), ELOs up to 5 credits, WMCC's welding testing, the HB Logging apprenticeship, personal finance inside economics, a credentials topic | 10 | 56 | 3 | 14 MB |
| `money-and-governance.md` | The City Council's role (less than the board asked in 22 of 23 years; $25,124,908 adopted), out-of-district special education (+$546,028), unfilled positions, the school share of taxes (41.4%), Brown School now apartments, the Gorham study, the voter report (three central office administrators; teacher and administrator pay over time) | 13 | 86 | 10 | 40 MB |
| **Total** | | **53** | **262** | **16** | **105 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.1 million tokens, including four follow-ups from the browser pass.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Berlin`). All 16 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 33 partial, 3 from the site's data.
- **Topics:** the career center file proposed `industry-credentials-for-students`. It was merged into `industry-credentials-explained`, which the Plymouth research added the same day.
- **Places:**
  - `district Berlin` 187, `town Berlin` 45, no place 20, `district North Country Charter Academy` 6.
  - `district White Mountains Regional` 2, `district Gorham Randolph Shelburne Cooperative` 1, `town Littleton` 1.
- **Pending facts:** none.
- **Raw folders:** the four total 105 MB; each is under 100 MB. Student photo captions were removed from the saved Program of Studies.
- **Quotes:** 523 of 649 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The adopted budget, $25,124,908 | The city's FY27 final budget and the June 15, 2026 council minutes |
  | Out-of-district special education, +$546,028 | The FY27 budget book (OCR) |
  | The contracted speech therapist, $132,000 | The FY27 budget book |
  | Administrator pay in 2025, $849,576 | The voter report's chart (transcribed from the image) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Project Youth ending at 5:45 (P1.1) | The page says 5:40 for K–5; no licensed program in Coös County lists hours past 5:30 |
| Full-day pre-K spots (P3.1) | No: a part-day special education preschool; Head Start runs 6 hours |
| Free meals for everyone (P5.1) | No: none of Berlin's schools uses community eligibility |
| Grades 6–12 in one building (P2.1) | Right |
| About a quarter proficient in math (P2.3) | Slightly high: 20–23% |
| AP not offered | Wrong: six AP courses listed |
| French or local history cut (P4.2) | French I–IV is offered; NH history is required, but no North Country course |
| An "Enrichment" referral (P11.2) | The Enriched Learning Center is a private special education school |
| Northern Human Services stepping in (P11.3) | Only invited to IEP meetings with parent consent |
| Annual homeschool portfolios (P12.2) | Out of date since July 1, 2026 |
| Credit recovery at night (P15.1) | No night program; online or summer, at the family's cost |
| Certifications before graduating (P6.1) | Preparation for AWS welding, ASE G1 and LNA; full ASE also needs work experience |
| A heavy-equipment program at White Mountains Regional (P6.2) | None found |
| $150 dual enrollment (P7.2) | Only after a student's two free courses that year |
| A WMCC early childhood agreement (P9.1) | Right; the agreement itself wasn't found |
| CTE only from 10th grade (P10.1) | Two-year programs start in grade 11; intro shop courses from grade 9 |
| Vacant schools costing the city (P17.3) | Partly: Brown School is now apartments |
| Adequacy rulings forcing more aid (P17.1) | None yet |
| Paras quitting for retail pay (P9.2) | Not shown |
| The City Council's role (P19.2) | Right: it sets the total; the board sets line items |
| What's driving the increase (P19.3) | Out-of-district special education, about half of it |
| Too many administrators (P16.3) | Three central office administrators |

## Corrections and additions to earlier files

None needed. Conway's Northern New Hampshire wage figures apply to Berlin's P9.2.

## Library notes (for review, not applied)

- **The coverage table** marks Berlin's kindergarten day, registration and preschool as not found. All three are here now.
- **`budget-form-and-vote-dates` summary** lists Berlin's budget form as not found. The City Council appropriates the school budget under the charter.
- **`cte-centers-overview` 4:** NH DOE's grid lists seven program areas; Berlin's own site lists eight, including Graphic Arts.
- **`community-colleges-early-college.csv`:** WMCC's Early College number is now 603-342-3019.
- **Personal finance:** a 2024 statewide survey says Berlin requires a stand-alone course; the 2026-27 Program of Studies puts it inside economics.

## Browser pass (November 21, 2026)

SAU 3's site loads in Chrome.
- **Read and saved:**
  - the after-school, transportation, bus schedule, food services and guidance pages, including graduation requirements;
  - the 2026-27 Program of Studies;
  - the four HB 1265 voter report files.

  The agents added facts from them.
- **Not posted:** a student/parent handbook.
- **Not read:**
  - the bus stop lists, in a Drive folder;
  - board minutes;
  - the labor board's contract library (HTTP 403), so paraprofessional pay is missing.
