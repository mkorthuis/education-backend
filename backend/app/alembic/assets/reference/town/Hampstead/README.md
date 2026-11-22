# Hampstead: Research for Ask NH Education Facts

Cited facts and figures for answering Hampstead, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the ToLoad towns. Hampstead is SAU 55, a K–8 district with its own SAU office:
- Hampstead Central School: preschool to grade 4.
- Hampstead Middle School: grades 5–8.
- High school: Pinkerton Academy in Derry, under a 20-year rolling tuition contract.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `central-school-and-daily-life.md` | Full-day kindergarten (a 2026-27 pilot), class sizes (76 kindergartners in 5 rooms), the YMCA's care in the building, PickUp Patrol (changes by 1:30), Title I targeted help ($55,074), reading instruction, the preschool, security and the SRO, phones and bullying (policy revised October 2026), delays, one bus stop for two homes, buses (First Student, Durham School Services, FirstView; read in Chrome) | 17 | 90 | 0 | 17 MB |
| `middle-school-and-pinkerton.md` | Hampstead Middle's tech, math (48%) and Ventures enrichment, 8th-grade Algebra I, high school credit (policy IMBD), Pinkerton's size (2,988, not 3,200+), the Pinkerton bus (6:22–6:27 a.m.), no late bus, trades, Early College, graduates' plans (59–64% four-year), 371 Hampstead students at Pinkerton | 8 | 44 | 3 | 15 MB |
| `student-support-and-choices.md` | IEP moves, out-of-district placements and transport, EFAs and home education (policies still describe the repealed yearly evaluation), HMS counselors, statewide Tutor.com, Hampstead Academy and Lexington Academy, Pinkerton's freshman academy and 504 plans, ratings and home values | 13 | 63 | 3 | 16 MB |
| `money-staff-and-governance.md` | Budgets defeated in 2025 and 2026 (default budgets 1.46% and 0.28% lower), the budget up 58.5% as enrollment fell 11.5%, the tax cap scenarios and the $562,804 "gap," Pinkerton tuition ($17,910), SAU 55's office (3.34% of the budget), the 2026 tax rate ($19.49, 78.6% schools), staffing, building work, vote dates | 8 | 68 | 7 | 24 MB |
| **Total** | | **46** | **265** | **13** | **72 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.16 million tokens, including the money agent's follow-up.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Hampstead`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial. P14.1, P14.2 and P20.2 rest mostly on the Pinkerton files.
- **Topics:** one new topic, `statewide-online-tutoring` (Tutor.com for grades 4–12), added to `../shared-topics.md`.
- **Places:**
  - `district Hampstead` 229, `town Hampstead` 19, no place 5;
  - `district Hampstead Academy` 7 and `district Lexington Academy` 1, private schools the Ask now reaches through find_places;
  - `district Pinkerton Academy` 4.
- **Places for the backend:** `places.yaml`'s Hampstead–Pinkerton row is unchanged. It says the contract isn't posted, which is still true; the budget slides describe it as a 20-year rolling agreement.
- **Pending facts:** 8 cite the draft 2027-28 budget.
- **Raw folders:** all under 100 MB.
- **Quotes:** 540 of 665 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2025 budget defeated 801–893 | The 2025 voting results |
  | Pinkerton tuition $17,910 for 371 students in 2026-27 | The November 10, 2026 budget presentation |
  | The 2026 tax rate, $19.49 | The town's 2026 tax rate sheet |
  | 76 kindergartners in 2026-27 | The November 10, 2026 budget presentation |
  | Title I budget $55,073.86 | The district's Title Grants Budget Summary 2026-27 |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day kindergarten for every child (P1.1) | Only for 2026-27, as a pilot |
| Big kindergarten and first-grade classes (P1.3) | No: about 15–16 and 18–19 per room |
| 350 at HMS, over 3,200 at Pinkerton (P2.1) | 344 at HMS; Pinkerton counts 2,988 |
| A late bus from Pinkerton (P2.3) | None found |
| The budget rising with flat enrollment (P3.1) | Up 58.5% (2014-15 to 2025-26) as enrollment fell 11.5% |
| The tax cap (P3.2) | Adopted for Hampstead; the district's scenarios run from $933,644 over to $134,473 under; no cuts named yet |
| Pinkerton tuition per student (P3.3) | $17,910; tuition is about 20% of the budget |
| All iPads and Chromebooks at HMS (P5.3) | No: industrial arts, family and consumer science, a technology teacher |
| HMS math under 50% (P7.1) | Right: 48% |
| Running Start (P14.3) | Renamed Early College |
| A yearly homeschool notice (P8.3) | Repealed July 1, 2026; policy IHBG still describes it |
| A separate SAU office for one K–8 district (P11.1) | Right; it's 3.34% of the budget, under the 6% cap |
| Comparisons with Danville and Sandown (P11.3) | They're part of Timberlane Regional, not their own districts |
| One bus stop or two for shared custody (P18.1) | One regular stop, changed only by year, half year or quarter |
| Attending HCS from a Derry address (P18.3) | No busing outside the district |
| The default budget hurting classrooms (P15.3) | 2025 and 2026 defaults were only 1.46% and 0.28% below the proposals; what was cut isn't posted |

## Corrections and additions to earlier files

- **Timberlane:** Timberlane left SAU 55 and became SAU 106 around 2021-22. The Timberlane research (in `../timberlane/`) covers it.
- **Library notes, for review:**
  - `kindergarten-rules` 6 leaves out that its grant was for fiscal year 2019 only.
  - The brief's "470 students in 2025-26" at HCS is the October 2024 count.

## Browser pass (November 21, 2026)

- **Read in Chrome and added:** the district's Transportation page (`central-school-and-daily-life.md`, district-transportation 8). The Board Documents page lists Google Drive folders: union contracts, board meeting materials, facilities reports.
- **Still not retrieved:**
  - **Those Drive folders:** their links need an access key from the full link. The money agent couldn't open them, so board minutes (what was cut after the default budgets, the class-size cap) and the contracts are unread. Teacher pay comparisons can come from the site's salary schedules.
  - **The HMS handbook:** not linked from HMS's home page.
  - **A state labor board (PELRB) ruling on the SRO post:** HTTP 403.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 7 saved bus and transportation copies (28 in all; schools, child care centers, businesses and other public places keep theirs).
