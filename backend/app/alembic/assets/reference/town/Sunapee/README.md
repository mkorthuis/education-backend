# Sunapee: Research for Ask NH Education Facts

Cited facts and figures for answering Sunapee, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch. Sunapee is a single-district SAU (SAU 85, with an office at 70 Lower Main Street):
- **Sunapee Central Elementary School** (preschool to grade 5; 217 students in October 2025 with 22 in pre-K) and **Sunapee Middle High School** (grades 6–12, 10 North Road; 263 students in October 2025 and 270 in October 2026), both run by the Sunapee School District, which takes in tuition students from other towns (480 students on October 1, 2025 against 363 resident students);
- career programs at the Region 10 career center in Newport (Sunapee had 32 students there in 2026-27) and Claremont, under an agreement signed by Sunapee, Claremont and Newport; Kearsarge Regional (New London) is the nearest comparison district, and Mount Royal Academy (private, Sunapee) is the nearby private option.

The district had no research before this batch; Newport's, Claremont's and Kearsarge's files are cited where they apply.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `sunapee-central-and-families.md` | After care run by The Outing Club Village ($25 a day or $541 a month; the program posts no hours, the state's data lists 3:00–5:30), a kindergarten cutoff of five before September 30 (policy JEB), a Residency Affidavit from the Town as proof of residency (policy JFAA), a $100,000 SAFE School grant for access controls, derived class sizes (about 15.5 in kindergarten, 20.5 in grade 3, 12 in grade 4), no gifted program in the federal data, four failed elementary bonds (2019–2022) and the renovation approved in March 2022 and 100% complete by October 2023 | 20 | 71 | 3 | 6.8 MB |
| `sunapee-middle-high-support-and-choices.md` | Policy EEA giving non-public school pupils "the same routes and termination points," policy JJJ giving the same access to teams, band and courses, no full-time social worker (0.5 FTE middle and 0.33 FTE high in the federal file), FY2024-25 substitute spending of $128,463 against a $60,000 budget, the grounds reserve of $100,265 with $70,000 planned for the upper field, a football co-op that could cancel a soccer season, policy JCA's change-of-school request and "manifest educational hardship" hearing | 15 | 102 | 0 | 5.7 MB |
| `sunapee-high-and-tech-center.md` | Seven AP courses taught at the school (no online AP provider), grade 11 SAT totals above Kearsarge's every year from 2023 to 2026 (1068 against 990 in 2025; tested groups of only 20 to 45), the Region 10 agreement's two reserved seats per program per center and Sunapee paying at least 25% of tuition, 32 students at Newport (6.1 miles, about 14 minutes, derived), a $150 Running Start fee in the catalog against the state's two free courses a year, a half-credit personal finance course required for the Class of 2030 and later, Sunapee not on ApprenticeshipNH's western hub list | 13 | 69 | 5 | 7 MB |
| `money-and-governance.md` | The 2026-27 budget of $15,715,564 (approved 573 to 367), the tax levy up 5.1% against a 2.7% rise in appropriations because non-tax revenue falls 14.1%, all of Sunapee's statewide education tax ($2,981,989 for FY2027) staying in town with an adequacy grant of $0, the middle high school roof estimated at $500,000 with $80,639 in reserve, a special education reserve of $497,160 and a contingency fund of $649,732 against $400,000–$600,000 for one residential placement, average teacher pay of $80,197 against $69,706 at Kearsarge, enrollment of 401 rising to 480 because of tuition students, the town's elderly exemption criteria (65 by April 1, three years in the state, income and assets; amounts in PDFs) | 11 | 77 | 9 | 3.7 MB |
| **Total** | | **59** | **319** | **17** | **23 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.2 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Sunapee. All 17 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 21 full, 39 partial. None is answered wholly by earlier files.
- **Topics:** one new topic, added to `../shared-topics.md`: `money-nh-school-funding-history` (how New Hampshire came to fund schools with a statewide property tax: the Claremont cases, Rand, SWEPT).
- **Places:** `district Sunapee` 290, `town Sunapee` 18, no place 8, `sau 85` 3. The Mount Royal Academy fact carries `town Sunapee` because the private school isn't in the district or outside-school tables.
- **Pending facts:** 11, citing draft or unapproved minutes (including Newport's handbook, a draft).
- **Raw folders:** each under 100 MB. The 36 saved PDFs are handbooks, the program of studies, policies, budget sheets, the Region 10 agreement (a scan, transcribed) and state sheets. The two images of the Region 10 agreement's signature pages were deleted by the main session (the transcription keeps the notarized dates); three page images of its other sections remain. None is a route sheet or a roster.
- **Privacy:** the address scan, including the `--raw` pass, finds only the schools, the SAU office and agency addresses. Minutes copies have names removed; the SAU staff list kept titles only.
- **Quotes:** 475 of 608 quoted passages found word for word in the raw copies. The money file's 81 of 146 is low because it quotes budget-line tables (read from OCR or page images) and derived commentary; the headline figures I searched for are in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026-27 appropriation of $15,715,564 and SWEPT of $2,981,989 | The budget hearing slides and the annual report |
  | An adequate education costing $1,905,966 and an adequacy grant of $0 for FY2027 | The site's `town_adequacy_aid` data (saved in the raw extract) |
  | The Grounds reserve and special education fund balances ($80,639 in the roof reserve) | The December 2025 capital plan and fund balances page |
  | The Region 10 agreement's notarized dates (July 9, 2024; December 4, 2024; February 20, 2025) | The saved transcription, read from the pages before the images were removed |
  | The school's local education rate rising from $4.04 (2024) to $4.31 (2025) | The site's `town_property_tax` table |

## Premises checked

| Question says | What the sources show |
|---|---|
| AP is all online (P4.1) | Wrong: the 2026-27 catalog lists seven AP courses taught at the school, and the College Board ledger shows no online AP provider |
| Carpentry at Newport (P2.2) | Carpentry-type courses are at the Claremont campus; welding and auto are at Newport |
| A co-op for a team (P7.2) | Sunapee is in no NHIAA co-op for 2026-27 and doesn't sponsor football, hockey, lacrosse or wrestling |
| "390–400" students (P12.3) | Matches the site's resident count (363 in 2025-26); the district reports 480 (482 in 2026) including tuition students and 150 in grades 9–12 |
| Running Start is free (P16.1) | The catalog lists a $150 fee on the course; the state's two free courses a year aren't mentioned in the catalog |
| No personal finance (P18.1) | A half-credit course exists and is required for the Class of 2030 and later |
| A bond voted down and the school never fixed (P6.2) | Four bonds failed (2019–2022); a smaller project of more than $5.5 million ($4.99 million borrowed) was approved in March 2022 and reported 100% complete in October 2023; windows are staged |
| Open positions at the middle high school (P9.1) | Neither confirmed nor ruled out |
| A phone rule (P10.2) | It exists, but the handbook's penalties differ from policy JICJ's |
| Buses for non-public school pupils (P11.1) | Policy EEA gives them the same routes and stops; it doesn't mention EFAs or taxes |
| A tax break for seniors who lived in Sunapee 30+ years (P6.1) | The town's elderly exemption depends on age 65 by April 1, three years' residence in New Hampshire, and income and assets, not years in Sunapee; the amounts are in PDFs that weren't read |
| A homeschool notice (P13) | Sunapee's policy IHBG (2022) still describes the pre-July 2026 notice and testing |
| A full-time social worker (P19.2) | None: 0.5 FTE (middle) and 0.33 FTE (high) in the federal 2023-24 file |
| About 150 high schoolers; plans to tuition students out | 150 is the district's grades 9–12 count, about 50 of them tuition students from other towns; no plan to tuition students out was found, and Sunapee takes tuition students in |
| Fewer kids | The district's own enrollment rose from 401 to 480 since 2021-22 because of tuition students; resident children fell to 323 in 2024-25 and rose to 363 |
| A 350-student merger rule | It matches Arkansas's law; no New Hampshire statute read sets an enrollment number for merging or closing a district |

## Corrections and additions to earlier files

None applied; nothing found contradicts earlier files. Additions for others:
- **Newport's cte-center-programs 5 and 18:** 5 counts 20 Sunapee students at the Newport tech center and 18 gives 32 (October 2026); Sunapee's file uses 32 for 2026-27 (the counts are for different years).
- **Claremont `stevens-high-and-tech-center.md`, cte-center-programs 8:** it quotes its superintendent that the Region 10 agreement "was not properly renewed"; the signed copy shows all three districts' signatures and a four-year term from the last one, so the minutes don't say what was not done properly. No correction proposed.
- **Newport `district-tuition-contracts` 2 and Claremont's 2:** Goshen keeps tuition contracts with Sunapee (24 Goshen students in 2025-26 on Sunapee's slide); Unity's agreement with Claremont expired in June 2026 and Sunapee's slide shows 10 Unity students.
- **Kearsarge's table `kearsarge_crdc_ap_and_dual_enrollment_compared_2023_24`:** Sunapee's row (133 students, 6 AP courses, 51 AP students, 32 dual enrollment) matches Sunapee's file.
- **Kearsarge's New London file `kres-new-london-and-families.md`:** describes The Outing Club's New London program; Sunapee's file adds its Sunapee after-care program.

## Library notes (for review, not applied)

- **Site data:** the site's school enrollment shows Sunapee Central kindergarten 17 and grade 3 21 for October 1, 2024 against the district profile's 30 and 23; the brief's "168 students in 2024-25" adds the site's K–5 figures against the district profile's 183 for kindergarten to grade 5 plus 15 in preschool. The site's Sunapee Sr. High count for October 1, 2024 is 131 against the district's 133. The site's 2026 rows for Sunapee Central weren't loaded.

## Browser pass

Partly done (November 22, 2026, in Chrome): the Town of Sunapee's Assessing page opened; its elderly exemption criteria and the posted application deadline are now fact 1 of `property-tax-relief` in the money file (a topic added to this file; raw copy in `raw/browser/`). The exemption amounts and income limits are in PDFs, which can't be read through the browser tool and weren't downloaded. Not retrieved:
- the town's budget book and capital plan, sunapeeathletics.org (403: youth leagues and the gym), Kearsarge's site (the tuition rate), NH DOE's gifted-reports page (403), the courts site, and the district's Google Sheet of bus routes (401: pickup times, ride lengths and Mount Royal stops);
- the Sunapee Central family handbook (needs a Google sign-in: kindergarten day length and registration date), policy lists and board minutes after March 2024 (script-loaded; no storm-closing, fee or field-trip policies), preschool hours, tuition and waitlists, open-position counts, therapy sessions missed, substitute fill rates, JV roster sizes and cuts, the 2026 NESDEC projections, the financing of the 2022 renovation, paraeducator pay, and why New Hampshire has no broad income or sales tax (not found).
