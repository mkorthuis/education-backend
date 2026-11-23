# Warner: Research for Ask NH Education Facts

Cited facts and figures for answering Warner, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch, after New London's research on the same district. Warner is in the Kearsarge Regional School District (SAU 65), a seven-town district (Bradford, New London, Newbury, Springfield, Sutton, Warner and Wilmot):
- **Simonds Elementary School** (kindergarten to grade 5; 121 students in October 2025, about 120 in 2026), which the board voted on September 3, 2026 to prepare to close and on October 22 voted 7-0-1 to stop pursuing (a closing now needs a majority of voters in all seven towns);
- **Kearsarge Regional Middle School** and **Kearsarge Regional High School** (New London; 89 Warner students at the middle school, 101 at the high school), with the Concord Regional Technical Center (CRTC) for career programs.

New London's research already covers the district's shared schools, money and the other towns; these files cite it and write Warner's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `simonds-elementary-and-families.md` | The Boys & Girls Club at Simonds before school (from 7:00), after school (to 6:00) and on vacations for ages K–8, the Warner Early Learning Center (49 West Main Street, also a Club program; infants "not enrolling at this time"), a kindergarten day of 8:45 to 3:15 that the handbook never calls "full-day," snow-day alerts generally between 5:30 and 6:15, no licensed toddler program in Hopkinton (Henniker at 6.9 straight-line miles and Bradford at 7.3 are nearer than Concord at 11.2, derived), no licensed program within 20 miles listing a regular closing after 6:00 | 12 | 36 | 1 | 0.3 MB |
| `simonds-grades-3-5-and-kearsarge-middle.md` | "About 130" students at Simonds against 132 (October 2024), 121 (October 2025) and about 120 now, the former "James House" preschool now Kearsarge Regional Preschool (Warner children go to the Bradford site), Buses 71 and 72 (first pickups 6:29 and 6:31; Bus 72 reaches the middle school at 7:25 for a 7:35 start), a late bus leaving at 4:35 with Warner stops at 4:58 and 5:05, RSA 110-D:6, V letting a superintendent grant extra excused absences for Guard members on active-duty orders, a gifted plan process and math league at Simonds (but no gifted program reported to the 2023-24 federal survey), 89 Warner students at the middle school (21% of 422) | 17 | 66 | 1 | 2.4 MB |
| `kearsarge-high-from-warner.md` | The Warner late bus leaving the high school at 4:45 with stops at the Warner Park & Ride (4:58) and "Reeds North & Warner Town Hall" (5:05), about 16 minutes by car from Town Hall (derived), a CRTC class and drive of about 170 of 400 minutes (43% of the day, derived), no summer school at the high school (the 2022-23 handbook listed one), Kearsarge's 504 handbook (referral to the guidance counselor), Warner's two town scholarship funds ($47,763.73 combined at the end of 2025), the Kearsarge Adult Diploma Program in North Sutton (evening terms starting September, January and May, weekly for 15 weeks, typically 5 to 8 p.m., ages 16 and up; read in Chrome), 7 shop-type courses listed for 2026-27 with 2 marked not offered | 10 | 28 | 1 | 0.6 MB |
| `money-and-governance.md` | Total budget per student of $33,720 for 2025-26 against NH DOE's $27,691 (FY2025), Warner's total rate falling from $30.89 to $17.32 after the 2025 revaluation (not a tax cut) and $17.81 in 2026 with $10.40 (58.4%) for the school lines, the highest local school rate of the seven towns ($9.37 in 2025-26) and the lowest cost per student ($24,867), each $1 million saved or added moving Warner's share by about $154,525 ($0.24 per $1,000, derived), the January 2025 petition to cap spending at $27,000 per student losing 1,435 to 113, the Simonds closing votes | 10 | 43 | 3 | 4.5 MB |
| **Total** | | **49** | **173** | **6** | **8 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.2 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Warner. All 6 tables are linked to a topic.
- **Coverage:** 59 of 60 questions have facts: 22 full, 36 partial, 1 from the site's data (P4.2), 1 none (P8.1). Three questions (P10.1, P10.2 and P9.1) are answered wholly by New London's file.
- **Topics:** no new topics (one library topic, `military-children-compact`, is used).
- **Places:** `district Kearsarge Regional` 129, `town Warner` 41, no place 1, `district Concord` 1.
- **Pending facts:** none flagged.
- **Raw folders:** each under 100 MB. The 14 saved PDFs are handbooks, policies, budgets, the bus transfer guide and the late run changes sheet (scans; their stops are public places such as the Park & Ride and Town Hall) and state sheets. The Warner route sheets (Buses 71 and 72) are kept as transcribed times and streets only; the original PDFs were deleted. Warner's 2025 town report lists residents' births, marriages and deaths by name, so only excerpts without names are saved.
- **Privacy:** the address scan, including the `--raw` pass, finds nothing in Warner's folder; the address lines from the stricter checks are the district office and public buildings.
- **Quotes:** 431 of 536 quoted passages found word for word in the raw copies (the misses are mostly titles, table text and the agents' own wording).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Warner's total rate of $31.72 (2023), $30.89 (2024) and $17.32 (2025) and the local school rate of $9.37 in 2025 | The site's `town_property_tax` table |
  | The January 2025 cap petition losing 1,435 to 113 | The saved Concord Monitor and NHPR articles |
  | Question 2 in Warner: 657 to 771 (46.0% yes) | The site's `town_question_two` table |
  | NH DOE's cost per pupil of $27,691 for FY2025 against the district's total budget per student | The agent's site-data extract and the file's derived calculation |

## Premises checked

| Question says | What the sources show |
|---|---|
| Spending "over $33,000 a student" (P2.1) | Depends on the measure: $33,720 is the total budget divided by students for 2025-26; NH DOE's cost per pupil for FY2025 is $27,691 |
| Taxes fell from $30.89 to $17.32 | The 2025 revaluation roughly doubled the town's assessed value, so it wasn't a cut in taxes |
| Simonds may close | The board voted on September 3 to prepare for it and on October 22 voted 7-0-1 to stop; a closing needs a majority of voters in all seven towns |
| Homeschool "annual testing" | Not required for home education since July 1, 2026; EFA families still owe a yearly test or portfolio |
| "Vote no again" on the budget | No rejected operating budget found for 2022 to 2026 |
| The Boys & Girls Club at Simonds (P1.1) | True: before school from 7:00, after school to 6:00 and vacations, K–8 |
| The Warner Early Learning Center (P3.1) | Real, at 49 West Main Street, also a Club program for toddlers and preschoolers |
| Full-day kindergarten (P3.2) | One school day of 8:45 to 3:15; the handbook never says "full-day" |
| Snow-day calls early enough (P8.2) | Alerts generally 5:30 to 6:15 a.m. |
| "About 130 kids" at Simonds (P4.1, P13.2) | A little high: 132 (October 2024), 121 (October 2025), about 120 now |
| The "James House" preschool | Now Kearsarge Regional Preschool, with Warner children going to the Bradford site |
| A late bus and a robotics club | A late bus exists; no robotics club found |
| Shop classes at the high school | Partly true: 7 shop-type courses are listed for 2026-27 with 2 marked not offered, against 6 offered in 2025-26 |
| "Running Start" | Now called Early College |
| FAFSA is required to graduate | KRHS told families so in 2023; state law since July 2024 only requires schools to offer information |

## Corrections and additions to earlier files

None applied; nothing found contradicts earlier files. Additions for other files:
- **New London `money-and-governance.md`, district-tax-and-state-aid 10:** the district's January 2026 table swaps New London's and Newbury's state-aid figures; Warner's row agrees with NH DOE (statewide education tax $633,257; adequacy grant $1,120,255.84 against the $1,130,908 estimate). New London's file counts Simonds at 121 students (the district's enrollment page) while the resident membership table in the same report shows 119.
- **New London `kearsarge-middle-support-and-choices.md`, district-transportation 9–10:** KRMS's own 2026-27 handbook gives a 4:15 p.m. late-bus pickup while the September 2026 flyer has a 4:30 line-up and 4:35 departure.
- **New London `district-enrichment-and-advanced-learners` 2:** KRMS and KRES-NL reported no gifted program to the federal survey; Simonds and all eight Kearsarge schools did the same, though Simonds' handbook and enrichment coordinator's site describe a gifted plan process.
- **New London `kearsarge-high-and-career-programs.md`:** its district-fees 4 gap (the athletic participation fee) still stands; the 2022-23 KRHS handbook listed summer school as a credit recovery option.
- **Concord `high-school-and-pathways.md`:** cte-center-programs 4's 90-minute classes and the CRTC's 2026 scholarship list aren't in Concord's file; no CRTC page read mentions adult courses.
- **Hillsborough `hdhs-and-crtc.md`:** its drive time to the Kearsarge Adult Diploma Program (25.0 miles, 50 minutes from the high school) matches the program's address.
- **Library:** RSA 110-D:6, V (deployment absences) isn't in `military-children-compact`; House Bill 1015 (2024), the reading and math instruction law the district's newsletters cite, isn't in the library.

## Library notes (for review, not applied)

- None.

## Browser pass

Partly done (November 22, 2026, in Chrome): the Kearsarge Adult Diploma Program page (kearsarge.org/node/196) opened and is now fact 3 of `adult-education-and-workforce-training` (raw copy in `raw/browser/`). Not retrieved:
- the rest of kearsarge.org's pages (HTTP 403 to automated requests: Simonds' page, policy EEA, the Bus Routes page, the Facilities Project site and tax calculator, the district's savings estimates for closing Simonds or Sutton Central, the teachers' contract, calendar policy IC and the 2027 deliberative session date), Warner's 2025 report (a PDF with name lists), and the Club's enrollment portal;
- policy EEA and the 2026-27 bus sheets (mud-season stops, riding to different places on different weekdays, how far a child must live to ride), KRHS's CRTC bus times, the Club's waitlist (the state shows 8 school-age openings), the athletic participation fee amount, the Adult Diploma Program's fees (only "affordable"), help with college application essays, the Warner Park & Ride location, a 2026 scholarship packet, a Kearsarge military program, evaluation and speech therapy wait times, screen-time minutes, teacher turnover, bus driver pay, substitute fill rates and Simonds newsletters (not found).
