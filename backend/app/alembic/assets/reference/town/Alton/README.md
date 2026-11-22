# Alton: Research for Ask NH Education Facts

Cited facts and figures for answering Alton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the second ToLoad batch. Alton is SAU 72, part of the Prospect Mountain SAU with Barnstead (SAU 86) and the Prospect Mountain JMA (SAU 301):
- **The Alton School District** runs Alton Central School (ACS), preschool to grade 8.
- **Prospect Mountain High School** (grades 9–12), in Alton, is run by a joint board of the Alton and Barnstead school boards under a joint maintenance agreement. Its students take career programs at the Lakes Region Technology Center (LRTC) in Wolfeboro.

Both decide their budgets by official ballot. These files are the first research on Prospect Mountain; Barnstead's research follows and cites them. Facts about the high school are placed `district Prospect Mountain JMA` and serve both towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `alton-central-and-families.md` | Class sizes (about 15 per class), Title I reading help, the 2:50 dismissal and no school-run care, half-day preschool, full-day kindergarten (7:45–2:50), snow days made up in June, meals, End 68 Hours of Hunger's weekend food, plowing bus routes first (22 miles of gravel roads), recess, a grandparent's guardianship petition (RSA 193:12), four family apps | 17 | 53 | 0 | 14 MB |
| `alton-central-upper-grades-and-support.md` | Algebra I in grade 8 (11 students in 2023-24), 13 ACS teams, ACS's share of each PMHS class, counselors (4 and a social worker at PMHS), IEP counts, teacher retention (PMHS 82.1% against 83.8% statewide), the handbook's outdated bullying wording, an IHBG that still describes repealed rules, French in grades 7–8 | 9 | 59 | 2 | 13 MB |
| `prospect-mountain-and-cte.md` | LRTC (38 PMHS students; a bus from PMHS), the 2026-27 catalog (few AP courses, 15 college-credit courses, an associate degree pathway, embedded honors), dual enrollment costs ($100 for SNHU courses), shop classes, financial literacy, retakes and late work, Alton Bay buses (6:52 to PMHS at 7:45; block days an hour later), phones, robotics and drama, the SRO, the bell schedule | 11 | 71 | 1 | 19 MB |
| `money-and-governance.md` | Budgets against enrollment, the SchoolCare assessment ($375,532 paid from the 2024-25 surplus; reserves not touched), Prospect Mountain's cost split (by students yearly, 45.55% Alton in 2026-27; capital 50/50), special education busing doubled, the SAU merger study (needs 60% in each town in March 2027), waterfront taxes, para pay, PMHS's five-year repair plan (just under $5 million) | 9 | 78 | 6 | 67 MB |
| **Total** | | **46** | **261** | **9** | **113 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.91 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Alton`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 32 partial, 4 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Alton` 120, `district Prospect Mountain JMA` 102, `town Alton` 28, `sau 72` 10, no place 1.
- **Pending facts:** 15 flagged. They cite the FY2028 draft budget, the draft SAU merger plan, a calendar whose file name says "Draft", and one set of draft minutes; one note quotes a statute's "pending".
- **Raw folders:** each under 100 MB. The bus route sheets list stops by house number, so only times and street names are kept, and the PDFs were deleted.
- **Quotes:** 422 of 569 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The SchoolCare payment, up to $375,532.44, from the $328,110.02 surplus | The Alton board's October 20, 2025 minutes |
  | Alton's 45.55% share | The 2026 warrant |
  | Reserves of $1,980,827.92 | The trust fund balances, November 30, 2025 |

## Premises checked

| Question says | What the sources show |
|---|---|
| School lets out at 2:50 (P1.3) | Right; no school-run after-school care |
| Snow days as Chromebook days (P3.3) | Not in the handbook; snow days are made up in June |
| Kindergarten full-day or half-day (P4.3) | Full-day; only preschool is half-day |
| Three apps (P20.3) | At least four |
| The same math for everyone until high school (P3.1) | No: Algebra I in grade 8 for eligible students |
| Driving to other towns for sports (P7.2) | Not for school sports: 13 ACS teams |
| Mostly Barnstead kids at PMHS (P7.3) | Right: Barnstead sends more |
| Spanish or French only from 9th grade (P19.2) | Mostly; French is a grade 7–8 elective |
| The reserve fund wiped out (P2.2) | No: paid from the surplus; reserves grew |
| Alton footing too much of PMHS's bill (P2.3) | The split follows enrollment yearly |
| Special education busing doubled (P9.2) | Right for the elementary line |
| The fund balance run to zero (P13.2) | Not supported |
| AP at PMHS (P3.2) | Few AP courses; 15 college-credit courses |
| A bus to the tech center (P5.2) | Yes, from PMHS |
| Unlimited retakes (P11.3) | One retake within 7 days, with conditions |
| A full-time SRO at both schools (P17.1) | Partly wrong |

## Corrections and additions to earlier files

- **Sandown** (`../Sandown/support-and-choices.md`): its statewide teacher retention (89.3%; 91% for elementary schools) counted 31 schools that report more retained than current teachers. It now uses 83.8% at the 440 schools with usable counts.
- **places.yaml:** the Alton and Barnstead → Prospect Mountain notes gave 45.55% and 54.45% as fixed shares. They now say the operating split follows enrollment yearly and capital is split 50/50.

## Library notes (for review, not applied)

- **The SAU 72 row of the SAU contact table, and `district-preschool` 2,** use https://acs.pmsau.nh.gov/o/acs, which no longer resolves. ACS is now https://www.acs.pmsau.nh.gov/o/acs and PMHS https://www.pmhs.pmsau.nh.gov/o/pmhs.
- **`budget-form-and-vote-dates` 3 (Alton)** says the 2027 dates weren't posted. The deliberative session is January 30, 2027 and the vote March 9, 2027.

## Browser pass (November 21, 2026)

The Prospect Mountain SAU sites (www.pmsau.nh.gov, www.acs., www.bes. and www.pmhs.pmsau.nh.gov) load in Chrome but show automated requests a bot check. Their documents are Google Drive and Docs files.
- **Saved in `raw/high/browser/` and added to `prospect-mountain-and-cte.md`:**
  - PMHS's 2026-27 handbook, Program of Studies and bell schedule;
  - the Alton and Barnstead high school bus routes, with house numbers removed;
  - the dual enrollment, technology, athletics and club pages.
- **The money agent's route:** it reached the SAU's documents through direct file links. The SAU's "Policies and Business" page links the same folders publicly.
- **Barnstead:** BES's handbook and bus routes were saved in `../Barnstead/raw/browser/` for its research.
- **Still not retrieved:**
  - ACS's own program and volunteer pages;
  - the board's policy book;
  - JMA board minutes;
  - the tech-center bus times.
