# Brentwood: Research for Ask NH Education Facts

Cited facts and figures for answering Brentwood, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the sixth wave of the second ToLoad batch. Brentwood is in SAU 16 with Exeter and its neighbors:
- **Swasey Central School** serves preschool to grade 5. The Brentwood School District decides its budget at a traditional annual meeting.
- **Grades 6–12:** the Exeter Region Cooperative runs Cooperative Middle School (CMS, in Stratham), Exeter High (EHS) and the Seacoast School of Technology (SST). The cooperative votes by official ballot.

The cooperative's schools were researched in `../Exeter/` and `../Stratham/`. These files add Brentwood's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `swasey-and-families.md` | The part-day preschool ($1,300 for community peers; no full-day pre-K), YMCA care in the building (7:00–8:45 and 3:00–6:00), drop-off from 8:35, kindergarten classes of 18, 18 and 17, scores against Stratham and Exeter (78% in math and reading in 2026), no gifted program, lunch, research on starting kindergarten a year later | 15 | 71 | 2 | 17 MB |
| `cms-support-and-choices.md` | The move from Swasey (about 300 students) to CMS (945), two bus schedules for families with children at both, CMS's late bus to Swasey, homeschool and EFA access (policy JJJ revised October 2026), how an EFA affects state aid, shared custody, vaping and phone rules, the calendars | 14 | 48 | 1 | 23 MB |
| `exeter-high-from-brentwood.md` | Brentwood's share of EHS, SST's trades programs, EHS's non-college courses, class size measures, Great Bay Charter School, AP and honors with no cap, counselor caseloads (about 193), private school comparisons, boosters | 7 | 30 | 3 | 25 MB |
| `money-and-governance.md` | Brentwood's school tax split (41.4% Swasey, 58.6% the cooperative; **derived**), tax dollars up 22.4% while resident students fell 20.0%, the FY2027 article ($7,858,303; insurance drove 97.6% of the rise), SAU 16's share ($195,373), the $616,400 solar bond, state aid per student (14th lowest), housing permits | 10 | 49 | 5 | 11 MB |
| **Total** | | **46** | **198** | **11** | **76 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.05 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Brentwood`). All 11 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 36 partial. Many questions turn on bus times and town programs that aren't posted (see Browser pass).
- **Topics:** one new topic, added to `../shared-topics.md`: `research-kindergarten-entry-age`, on national data and research about children who start kindergarten a year late. One fact is added to the library's `budget-default-budget`.
- **Places:** `district Brentwood` 132, `district Exeter Region Cooperative` 35, `town Brentwood` 16, `sau 16` 9, statewide 3, `district Great Bay Charter School` 2, `district Diocese of Manchester` 1.
- **Pending facts:** 20, citing the November 2, 2026 draft minutes and draft budgets.
- **Raw folders:** each under 100 MB. Bus times aren't posted, so no route sheets were saved.
- **Privacy:** the main session removed 17 residents' house numbers from public comment in the May 4 and June 1, 2026 board minutes, saved in several folders, and deleted four PDFs of those minutes. One citation now points to the text copy. The address scan finds only Swasey Central School.
- **Quotes:** 430 of 506 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The FY2027 article, $7,858,303 | The March 2, 2026 annual meeting minutes and the MS-27 |
  | SAU 16's share, $195,373 | The MS-27 and the FY2027 budget detail |
  | The $616,400 solar bond (3.13%, 2025 to 2032) | The FY2025 financial report |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day pre-K at Swasey (P1.1) | No: part-day sessions |
| Buses to "Brentwood Commons" (P1.2) | No such place found; YMCA care at Swasey |
| A school of about 300 (P2.3, P6.1) | Right: 297–299 in fall 2026 |
| Scores against Stratham and Exeter (P3.1) | Swasey higher in 2026; math growth lower |
| Gifted pull-out groups (P3.2) | No gifted program |
| An aide in every kindergarten (P11.3) | Not stated |
| Early drop-off (P14.3) | From 8:35; YMCA care from 7:00 |
| An EFA cutting town funding (P7.2) | Not for a child already homeschooled |
| A late bus (P14.2) | Yes from CMS; none found from EHS |
| Spanish in elementary school (P17.2) | No; from grade 7 |
| Crowded classes at EHS (P3.3) | Not shown; 12.14 students per teacher |
| A cap on AP and dual enrollment (P13.1) | None found |
| Counselors stretched (P13.2) | About 193 students each, under the state cap |
| Boosters pay for everything (P18.3) | No; the budget pays most costs |
| Taxes up every March (P2.3) | Most years, not all |
| A big roof bond (P9.2) | None; only the solar bond |
| Shortchanged by the state (P9.3) | $4,911 per student, 14th lowest of 237 towns |
| Cuts to art, music or librarians (P19.1) | Not found |
| A failed budget falling to a default (P19.3) | No default budget at a traditional meeting; the cooperative has one |
| New housing raising enrollment (P20.2) | Not supported |

## Corrections and additions to earlier files

- **Exeter** (`../Exeter/`):
  - Its EHS file gains the grade-point table. The table's College Prep column isn't mentioned in the handbook sentence the file quotes.
  - Its money file's turf replacement reserve ($155,078, February 2026) gains the June ($157,062) and November ($210,527) balances.
  - Its money file places SAU 16's December 1, 2026 budget hearing at Exeter High; Brentwood's draft minutes say the SAU building. Unresolved.
  - Its elementary file gains Great Bay Charter School's class caps.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 13 (Brentwood):** consistent, but the library's copy of the 2026 warrant has a blank page 2. The copy saved here has all five articles.

## Browser pass

Not needed for the answers. Not retrieved:
- the Town of Brentwood's website (a bot check) and Brentwood Recreation (the connection dropped), for the 2026 tax rate, the reassessment and youth programs;
- bus routes and times for Swasey, CMS and EHS, which SAU 16 emails to families instead of posting;
- the YMCA's Brentwood prices and waitlist;
- the cooperative's articles of agreement and NH DOE's apportionment pages (HTTP 403).
