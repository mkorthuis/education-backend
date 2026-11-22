# Hampton: Research for Ask NH Education Facts

Cited facts and figures for answering Hampton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the three files below and the shared Winnacunnet file, in the reference library's format, ready to load but not loaded.

Gathered November 16–17, 2026, alongside Milford and Exeter. Two school districts serve Hampton:
- **The Hampton School District (SAU 90),** preschool to grade 8: Centre School (preschool–2), Marston School (3–5) and Hampton Academy (6–8).
- **The Winnacunnet Cooperative (SAU 21),** grades 9–12 at Winnacunnet High School, shared with Hampton Falls, North Hampton and Seabrook, with South Hampton sending students on tuition.

Both districts vote by official ballot.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `k8-schools-and-daily-life.md` | The half-day preschool and HATCh playgroup, kindergarten aides, the YMCA's care at Marston, clubs, reading and math teaching, counselors and advisory, the 2026-27 calendar against Winnacunnet's. From the Chrome pass: bell times, drop-off and pickup rules, delays, busing eligibility, the gifted and phone policies. Also flood-prone roads and the Meadow Pond drainage work | 13 | 56 | 1 | 38 MB |
| `student-support-and-community.md` | Out-of-state IEPs, Sacred Heart services and the 2026 petition vote, bullying programs, SROs and safety grants, storm and lockdown plans, 504 staffing, summer help, discreet meals, community use of buildings, how SAU 90 and SAU 21 fit together, comparisons with North Hampton and Portsmouth, getting involved | 19 | 79 | 2 | 85 MB |
| `money-and-governance.md` | Both 2026 budgets (about $32 million each), the HVAC and seating articles, the Centre boiler and pond work, the 2024 revaluation and exemptions, the $600,000-home petition, default budgets, Hampton's share of Winnacunnet (46–47%), tax year 2026 rates, voting rules, non-union raises | 11 | 66 | 6 | 46 MB |
| `../winnacunnet/winnacunnet-high-school.md` (shared) | Winnacunnet High School; see `../winnacunnet/README.md` | 14 | 107 | 5 | 40 MB |
| **Total** | | **57** | **308** | **14** | **209 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.82 million tokens.

## Checks

- **Parser:** all files pass the backend's parser (`tools/check_town.sh Hampton`, `tools/check_town.sh winnacunnet`). All 14 tables are linked to a topic.
- **Coverage:** 59 of the 60 questions have facts: 18 full and 41 partial. P17.3 (late buses at Hampton Academy) has none: neither the budget nor the 2026-27 handbook describes one.
- **Topics:** one new topic was added to `../shared-topics.md`, `voting-in-local-elections` (who may vote, absentee voting, turnout by age). The library's `budget-voter-information` covers what voters are told, not who votes.
- **Places:**
  - Hampton's files: `district Hampton` 115, `town Hampton` 36, `district Winnacunnet Cooperative` 32, `sau 21` 6, no place 12.
  - The Winnacunnet file: `district Winnacunnet Cooperative` 104, `sau 21` 2, no place 1.
  - Five of the no-place rules repeat earlier files, with the same terms: RSA 72:38-a deferral (Concord), comparable services for transfers (library), discreet meals (Hudson), RSA 72:6 (Derry), RSA 654:1 (Derry).
- **Places for the backend:** `places.yaml` already has Hampton's Winnacunnet row and the other member towns' rows. No change.
- **Raw folders:** all under 100 MB.
- **Quotes:** 644 of 764 quoted passages found word for word in the raw copies (357 of 444 in Hampton's files, 287 of 320 in Winnacunnet's).
- **Reconciled in review:**
  - **Counselor counts:** the Winnacunnet file's "five counselors" and "10.0 counseling positions" agree. Five counselors carry caseloads, and SAU 21's 10 counting positions include the college, 504, behavior and special services counselors. The file says so.
  - **SST count:** the Winnacunnet file said no count of its students at SST was found. Exeter's research found SST's own count (79 in 2026-27), and the file now points to it.
  - **Bell times:** the K–8 file said Winnacunnet's bell times couldn't be read. The Winnacunnet file has them (7:45 to 2:30), and the K–8 file now points there.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Sacred Heart child benefit article, $48,626, failed 1,084 to 1,734 | The town's official 2026 election results |
  | Hawley Library redesign, $192,698, passed 2,528 to 2,500 | SAU 21's 2026 election results; the 2025-26 annual report's warrant |
  | Winnacunnet HVAC article, $497,581 | The 2025-26 Winnacunnet annual report |
  | Centre School boiler $300,000 and pond clean-up $50,000 | SAU 90's 2026 ballot |
  | Tax year 2026 total rate, $12.78 | The town assessing page |

## Premises checked

| Question says | What the sources show |
|---|---|
| Centre PreK full- or half-day (P1.1) | Half-day: 2.5 hours, Monday to Thursday, with limited space |
| A 3:00 pickup (P1.3) | Close: Centre and Marston run 8:20 to 2:52 (read in Chrome) |
| Voting on "SAU 90 and SAU 21" budgets (P2.1) | Partly right: the votes are on two school district budgets, Hampton's and Winnacunnet's; SAU 21's office budget is adopted by its joint board |
| HVAC and seat articles on a $32 million budget (P2.2) | Right size, wrong district: both were Winnacunnet's; HVAC passed and the seats failed |
| Buses rerouted for flooding and king tides (P3.3, P20.3) | No district statement. The delay page names snow, unplowed roads and building problems; the town lists the roads that flood; Meadow Pond flooding now clears in hours after the 2025 drainage work |
| Hampton Academy a "bigger building" (P3.2, P11.2) | By enrollment about the same as Marston (313 and 303) |
| Hampton children join "four other towns" at Winnacunnet (P5.1) | True: 459 of 970 students are from Hampton (47.3%) |
| $350,000 for Centre School and Batchelder Pond (P6.1) | Right: $300,000 for a boiler and $50,000 for the pond, part of a yearly program |
| Buses and services for Sacred Heart students (P6.3, P8.1) | Partly: busing is owed by law (policy EEA says same routes and stops); other services were a petition article voters rejected in 2026 |
| Coastal revaluations and a senior exemption (P10.1) | The 2024 revaluation covered every property; exemptions run $175,000 to $300,000 |
| A $600,000-home tax impact petition (P10.2) | Right: passed 1,826 to 850 |
| SROs in all four buildings (P12.1) | Police reports name SROs at Centre, Hampton Academy and Winnacunnet, not Marston |
| Bell times and early releases line up (P12.3) | Four of five early-release dates match Winnacunnet's; the K–8 schools let out at noon or 11:30, Winnacunnet at 11:56 |
| Hampton's K–8 schools in SAU 21 (P14.1) | No: Hampton's K–8 district is SAU 90 |
| Hampton's 47% share of Winnacunnet (P14.2) | About right: 47.3% of local taxes in 2025-26, 46.4% in 2026-27 |
| Marston always hiring techs and paras (P15.1) | Two Marston openings of 11 in the district on November 16, 2026 |
| Non-union paras' raises (P19.1) | Partly wrong: paras are unionized (contract to 2029); 59 non-union staff's raise sat above the default budget |
| Counselors stretched thin at Winnacunnet (P9.2) | About 194 students per counselor, under the state's 300 |
| The Hawley Library redesign "on the ballot" (P9.3) | Hawley is Winnacunnet's own library; the redesign passed in March 2026 |
| Sports fees (P7.3) | None listed in the handbook or on the athletics registration page |
| Phones (P18.3) | Banned bell to bell at Winnacunnet and in SAU 90 (policy JICJ), including lunch |

## Corrections and additions to earlier files

None needed. Hart's Location's elderly exemption minimums and Portsmouth's and Dover's files agree with Hampton's.

## Library notes (for review, not applied)

- `kindergarten-entry-cutoff` 33 (Hampton) is right. Policy JEB, read in Chrome, says "before September 30." A search snippet saying "on or before" came from a page that now returns 404.
- `district-preschool` 39 (Hampton): the program's own site now calls it "Hampton Preschool at Centre School."
- `high-school-tuition-options` 36 says Hampton's Winnacunnet membership "is not stated on a Hampton page." Winnacunnet's 2025-26 annual report confirms Hampton's board seat and students.

## Browser pass (November 17, 2026)

- **Read in Chrome and added:**
  - **sau90.org,** a bot check to the agents: the 2026-27 Student-Family Handbook, the delay and closing page, and policies JEB, EEA, IHBB and JICJ. These became 8 facts in `k8-schools-and-daily-life.md` (district-school-day-and-calendar 8–10, district-transportation 4–6, district-technology-and-phones 3, district-enrichment-and-advanced-learners 7).
  - **winnacunnet.org,** HTTP 403 to the agents: the prospective students and athletics registration pages, plus the athletics handbook they link (the 2021-22 edition). These became 2 facts in the Winnacunnet file (district-student-support 15, district-fees 5).
- **Still not retrieved:**
  - Winnacunnet's school profile (a PDF, which Chrome can't read).
  - SAU 21's board portal (a bot check).
  - SAU 90's bus route files, attendance and enrollment policies (JH, JEC), and board minutes.
  - YMCA rates (HTTP 429).
  - NH DES's tide-gauge page.
  - DRA's 2026 split of the school rate between the two districts.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- The state's resident birth, marriage and death lists removed from 1 saved town report copy (headings and record counts kept).
