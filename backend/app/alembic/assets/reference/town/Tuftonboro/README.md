# Tuftonboro: Research for Ask NH Education Facts

Cited facts and figures for answering Tuftonboro, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch, after Wolfeboro's, Ossipee's and New Durham's research on the same district. Tuftonboro is in the Governor Wentworth Regional School District (GWRSD, SAU 49), a six-town district (Brookfield, Effingham, New Durham, Ossipee, Tuftonboro and Wolfeboro):
- **Tuftonboro Central School** (kindergarten to grade 6; 110 students on October 1, 2025, up from 99), the district's only school in town;
- **Kingswood Regional Middle School** and **Kingswood Regional High School** (grades 7–8 and 9–12, in Wolfeboro; 36 and 70 Tuftonboro students), with the Lakes Region Technology Center (LRTC) there; Brewster Academy (private, in Wolfeboro) is the nearby private option.

Wolfeboro's, Ossipee's and New Durham's files cover the district's shared schools, policies and money; these files cite them and write Tuftonboro's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `tuftonboro-central-and-families.md` | After-school care by Kids' Corner in the school gym (a private licensed program, K–6, 7:00 to 5:30 on the state record, fees not posted), school starting at 8:45 with doors at 8:25, Melvin Village about 3.3 miles and 7 minutes from school (derived; GWRSD posts no routes), one classroom teacher per grade and the same seven teachers since 2023-24 (derived), a case manager shared with Effingham (70% in 2025-26, planned 100%), a speech pathologist contracted from Boothby Therapy Services, a $10 Hiking Club trip, a winter sports program with no posted cost | 15 | 52 | 4 | 5.8 MB |
| `tuftonboro-grades-3-6-and-kingswood-middle.md` | Grade 4 and 5 results in 2026 below the state (math 33% and 27% against 52% and 43%; only 10 to 25 tested), Kingswood Middle beating Manchester, Nashua, Rochester, Laconia and Concord in every grade and subject, five other towns plus 31 Middleton (tuition) and 2 Freedom students at Kingswood Middle, phones off in a locker or bag, one counselor for 110 students (derived), 8 hours of bus driver training a year under state rules, vaping banned with "immediate suspension and possible expulsion," no yearly filing with SAU 49 since July 1, 2026 | 13 | 61 | 5 | 6.3 MB |
| `kingswood-high-from-tuftonboro.md` | 70 Tuftonboro students at Kingswood High against 71 residents in grades 9–12 (derived), Kingswood grade 11 below the state's share proficient in 8 of 10 years in math and 9 of 10 in reading (2026: math 20% against 30%), no LRTC welding program (welding is in Metal Working I, Collision and Automotive), Marine Tech I and Auto I open to sophomores, Brewster with about 350 students (85% boarders), 15 AP-labeled entries against Kingswood's 7 AP subjects, and no posted college outcomes, a 26-credit diploma with LRTC counting as electives | 13 | 35 | 6 | 13 MB |
| `money-and-governance.md` | The 2025 revaluation (values +30.1%, combined school rate −21%, school dollars +2.8%) and a projected 8.68% rise in school taxes for 2026-27 (rate $3.72), school taxes up 45.4% from 2014 to 2025 while resident students fell 17.0% (derived), a payment of $42,099 per student against $26,114 for Ossipee and $18,602 for Effingham (the 25% by property value formula and no adequacy grant, not waterfront), Question 2 at 65.2% across the six towns, a board seat expiring in 2027 (filing January 20–29, 2027, derived), central office lines up 16.8% against 13.1% for the general fund, the last day of school each June, the town's page on the 2025 revaluation (median assessment 79.6% of market value before it), the town's page on the state's low and moderate income relief program (income limits that don't match the statute's) | 11 | 51 | 5 | 30 MB |
| **Total** | | **52** | **199** | **20** | **55 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.2 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Tuftonboro. All 20 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 34 partial. Three questions (P18.1, P11.3 and P9.2 in the three files) are answered wholly by earlier files.
- **Topics:** one new topic, added to `../shared-topics.md`: `school-vaping-and-tobacco-rules` (RSA 126-K).
- **Places:** `district Governor Wentworth Regional` 154, `town Tuftonboro` 32, no place 6, `district Brewster Academy` 6, `town Laconia` 1.
- **Pending facts:** none flagged.
- **Raw folders:** each under 100 MB (money is 30 MB, mostly the district's financial reports and slides). The 56 saved PDFs are handbooks, policies, budgets and state sheets; none is a route sheet or a roster. Three page images are saved: the cost distribution table, the administrator salary posting (positions, no names) and the school board election results. The declared-candidates list, which prints home addresses, was read but not saved.
- **Privacy:** the address scan, including the `--raw` pass, finds only the town library (221 Middle Road), schools, the SAU office, agency addresses and state regulation text. Minutes copies have names removed.
- **Quotes:** 412 of 497 quoted passages found word for word in the raw copies. The money file's 61 of 113 is low because it quotes financial report tables read from page images; the figures I searched for are in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | School taxes rising 45.4% from $5,830,656 (2014) to $8,476,948 (2025) | The site's `town_school_tax` table (local plus state education tax) |
  | The projected 2026-27 payment of $9,213,021 (+8.68%) and a payment of $42,099.35 per student | The district's FY2027 handout and the saved derived calculations |
  | Question 2: 65.2% across the six towns (Tuftonboro 62.8%) | The site's `town_question_two` table |
  | 70 Tuftonboro students at Kingswood High and 36 at Kingswood Middle on October 1, 2025 | The district's enrollment sheet (its by-town rows add to 733 against a printed 712) |

## Premises checked

| Question says | What the sources show |
|---|---|
| School starts at 8:45 and doors open at 8:25 | Correct (handbook) |
| An hour each way on the bus | Can't be confirmed: Melvin Village is about 3.3 miles and 7 minutes by road (derived) and GWRSD posts no routes |
| "Five other towns" at Kingswood Middle (P7.1) | Right, plus 31 Middleton (tuition) and 2 Freedom students |
| Phones locked up all day (P18.1) | Off and kept in a locker or bag, not locked up |
| A sensory space (P16.1) | None mentioned in any source read |
| Yearly homeschool filing with SAU 49 (P11.3) | None since July 1, 2026 |
| A welding program at LRTC | None: welding is taught in Metal Working I, Collision and Automotive; Marine Tech I and Auto I are open to sophomores and Marine Tech II is grades 11–12 |
| LRTC programs are "all full" | No source gives seats or waitlists |
| A half-day trade program fits graduation | Yes: 26 credits, 7 a year, LRTC counts as electives; summer school is only for repeating failed courses |
| Budget cuts to hands-on electives | None found: the same four tech courses were unavailable in both 2025-26 and 2026-27 |
| A revaluation is coming | It already happened in 2025; values also jumped in 2019 and 2022 |
| Waterfront explains the per-student cost | No: the cause is the formula (25% by property value) and no adequacy grant |
| A tax cap vote is ahead | Already decided: Question 2 passed at 65.2% (unofficial) across the six towns, so the cap and the 6% central office cap apply from the 2027-28 budget |

## Corrections and additions to earlier files

Applied:
- **Wolfeboro `kingswood-high-and-lrtc.md`, the P12.1 premises row, its coverage row, the main gaps and the Not retrieved note:** they said Brewster's own AP course count wasn't found. Tuftonboro's research counted 15 AP-labeled entries on Brewster's department pages (a derived count); those places now say so and cite Tuftonboro's file.

Not applied (additions for other files):
- **Wolfeboro `kingswood-high-and-lrtc.md`:**
  - high-school-outcomes 4 says Kingswood isn't on the College Board's 2025 AP honor roll; GreatSchools' AP participation figure for Kingswood is 12% (2021 federal data), which the honor roll's threshold (40% of graduates taking AP exams) would not meet.
  - town-school-options-nearby 2 gives Brewster's class sizes as 7–12; Brewster's about page says the average is 12 and its day-student page says 11.
  - district-classrooms-and-staff 1 gives 712 students on October 1, 2025; the district's by-town sheet rows add to 733.
- **Ossipee `kingswood-from-ossipee.md`, cte-center-programs 13:** it says Metal Working I teaches welding; LRTC's Collision and Automotive pages also mention welding. The Alton file already notes there is no stand-alone welding program.
- **Wolfeboro `elementary-and-families.md`, district-school-day-and-calendar 3:** no 21st Century after-school site exists at a Wolfeboro school; Tuftonboro's Kids' Corner is a state-licensed private program, not school-run.
- **Ossipee `ossipee-central-and-families.md`, district-special-education-services 2:** Ossipee Central has three speech pathologists; Tuftonboro Central has one.
- **Wolfeboro's money file and the Ossipee and New Durham tables** agree with Tuftonboro's figures. One difference between handouts: the FY2026 handout printed $4.22 as Tuftonboro's 2024-25 school rate while the FY2027 handout prints $4.37, the rate DRA later set, so the January 2025 handout's history was an estimate.

## Library notes (for review, not applied)

- None.

## Browser pass

Partly done (November 22, 2026, in Chrome): the Town of Tuftonboro's site (tuftonboronh.gov) opened. Its Assessing page on the 2025 revaluation is now fact 17 of `district-tax-and-state-aid`, and its Tax Collector page on the state's Low & Moderate Income Tax Relief Program is fact 2 of `property-tax-relief` (its income limits differ from the statute's, so the fact says it is probably out of date); raw copies are in `raw/browser/`. The town's Elderly Exemption Worksheet is a PDF and wasn't read. Not retrieved:
- the UNH copy of its town report (403), NH DOE's special education complaints page (403), the NH Employment Security Tuftonboro profile and the NH Department of Labor youth-employment PDF (403), Niche's Kingswood page (403), and the PTCO minutes (sign-in);
- Tuftonboro's own elderly exemption amounts, bus routes, pickup times and the Tuftonboro late-bus stop, Kids' Corner fees and rules, speech pathologist hours, how long evaluations take, whether kindergarten is full day (never stated), winter sports details, counts of out-of-district placements or disputes, a school lake-ecology program, seats and waitlists by LRTC program, marine placement counts and pay, Brewster's college matriculation list, any follow-up of graduates after two years, candidate forum or statements, snow-day notice times, a building condition study and per-article tax effects (not found).
