# Kingston: Research for Ask NH Education Facts

Cited facts and figures for answering Kingston, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the second ToLoad batch. Kingston's students attend the Sanborn Regional School District (SAU 17), shared with Newton:
- Daniel J. Bakie Elementary School, in Kingston: preschool to grade 2;
- Memorial Elementary School, in Newton: grades 3–5;
- Sanborn Regional Middle School (6–8) and High School (9–12), both at 17 Danville Road, Kingston. High schoolers may take career programs at the Seacoast School of Technology in Exeter.

Schools go by grade, not by town: every child from both towns attends the same schools. The district decides its budget by official ballot. These files are the first research on Sanborn; Newton's research follows and cites them. District facts are placed `district Sanborn Regional` and serve both towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | Bakie's half-day preschool (by lottery), school hours and pickup, the YMCA's care inside Bakie (7:00–8:30, 3:00–6:00), bus stops at child care centers (none in Plaistow), the calendar (one early release), kindergarten (about 15 per room), reading help in "What I Need" blocks, Title I, paper meal applications, Pickup Patrol and the new app, Kingston Children's Center on no-school days ($77 a day) | 10 | 60 | 2 | 35 MB |
| `support-and-choices.md` | Policy JJJ (September 2026) for home-educated, EFA, charter and private school students, unlocked outer doors and the resource officers, paraprofessionals (64.8 to 53.0 positions since 2019-20), Seacoast Classical Academy on the Newton campus, counselors (about 150 students each at the high school), 504 plans, phones, attendance and truancy, Hampstead Academy | 10 | 66 | 2 | 8 MB |
| `middle-high-and-sst.md` | The 2026-27 course book (24 credits; SST counts 2 a year; two AP courses running), 2026 scores (50% math, 58% reading), SST (enrollment down from 84 to 63; 90-minute classes), Algebra I in grade 8, sports eligibility by quarter, auto, welding and woodworking, the leased Swasey Gym, no activity fee | 10 | 61 | 3 | 25 MB |
| `money-and-governance.md` | Schools by grade, not town; the default budget above the proposed budget both years ($1,464,541 for 2026-27), taxes against a 2% budget growth (Fremont tuition falling), 1,100 students (down 30% since 2019-20), the coming repair bond ($12,885,000 list), the budget survey (143 replies), HB 1300's caps, Kingston's share (54.5% of local school taxes, derived), dates for 2027, a topic on intermunicipal agreements | 9 | 62 | 3 | 47 MB |
| **Total** | | **39** | **249** | **10** | **115 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.12 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Kingston`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 30 partial.
- **Topics:** one new topic, added to `../shared-topics.md`: `intermunicipal-agreements-rules` (RSA 53-A agreements between towns, school districts and SAUs).
- **Places:** `district Sanborn Regional` 232, `town Kingston` 10, `district Seacoast Classical Academy Chartered Public School` 4, `town Newton` 1, no place 2.
- **Pending facts:** none flagged.
- **Raw folders:** each under 100 MB. Later, the main session also removed residents' births, marriages and deaths from the saved Newton town report text, and deleted that PDF.
- **Quotes:** 598 of 710 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026-27 budget, $41,028,910, and default, $42,493,451 | The 2026 ballot article (the difference is derived) |
  | The repair list, $12,885,000 | The November 4, 2026 FY28 budget presentation |
  | Grants of $96,489 | The October 21, 2026 board minutes |
  | Kingston's 2025 rate, $17.90 (school $10.79) | The Tax Collector's page, read in Chrome |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day pre-K (P1.1) | Half-day, by lottery |
| A bus to day care in Plaistow (P1.3) | Buses stop at four centers in Kingston and Newton; none in Plaistow |
| Early-release and workshop days to cover (P8.3) | One early release; the days to cover are no-school days, when the YMCA program is closed |
| Kindergarten crowding (P12.1) | A sixth teacher was hired: about 15 per room |
| A 4th grader at Bakie (P4.1) | Grades 3–5 are at Memorial |
| Scores around 44% and 56% (P2.2) | Those were 2025's; 2026's are 50% and 58%, above the state |
| "Half the day at SST" (P5.2) | About 2¼ hours away, with the drive |
| AP and Running Start canceled (P9.1) | Running Start is now Early College; two of four AP courses run |
| Shop classes cut first (P15.2) | Not supported: auto, welding and woodworking are offered |
| Activity fees (P20.1) | None published |
| Kingston and Newton children split by town (P2.1) | No: schools go by grade |
| About 1,200 students (P3.1) | 1,100 in 2026-27 |
| The default budget would cut spending (P3.2) | Not in the last two cycles: the default was higher |
| A budget survey on "what to cut" (P11.3) | It asked residents to rank priorities |
| A huge bond coming (P17.2) | Right: a repair bond is being prepared |
| Yearly homeschool paperwork (P10.3) | None since July 1, 2026; Sanborn's posted IHBG still describes the old rules |
| Locked entryways and an officer (P12.2) | Inner doors locked; outer doors unlocked during the day |
| Families leaving by middle school (P12.3) | Not shown in the latest year |

## Corrections and additions to earlier files

- **Exeter** (`../Exeter/cms-sst-and-getting-to-school.md`): Sanborn's board heard SST's open house was November 10; Exeter's file says November 5. Not reconciled.
- **Danville** (`../Danville/money-and-governance.md`): its Sanborn average teacher salary ($56,600, 2025-26, the site's data) matches the site; the district's own slide uses $63,532 for 2024-25.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 122** says Sanborn's 2026 deliberative session and vote dates weren't found. The session was February 4, 2026.
- **Policy IKF** still says 28 credits; the 2026-27 program of studies says 24.

## Browser pass (November 21, 2026)

- **sau17.net** (a bot check to agents) loads in Chrome. The middle school site posts no handbook, course list or clubs page; its "Student Information" documents folder is empty.
- **kingstonnh.gov** loads in Chrome. The Tax Collector's page shows the 2024 and 2025 rates only; 2026 isn't posted.
- **Not retrieved:**
  - Kingston's 2025 town report (UNH's copy needs a download);
  - NH DOE's and DRA's apportionment pages (HTTP 403).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- 1 original route sheet (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
