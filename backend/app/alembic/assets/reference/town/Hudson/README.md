# Hudson: Research for Ask NH Education Facts

Cited facts and figures for answering Hudson, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the four files below, in the reference library's format, ready to load but not loaded.

Gathered November 16, 2026, alongside Bedford, Keene, Portsmouth, Goffstown and Laconia. Hudson is SAU 81, a one-district SAU: the Early Learning Center (kindergarten at Library Street, grade 1 at Dr. H. O. Smith), the integrated preschool at Nottingham West, Hills Garrison and Nottingham West for grades 2–5, Hudson Memorial School (6–8) and Alvirne High School (9–12) with the Wilbur H. Palmer Career and Technical Education Center and the Alvirne Farm.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `schools-and-daily-life.md` | Full-day kindergarten and Champions before- and after-care, math results against Windham and Londonderry and the interventionists, the street list for elementary zones, home education access and re-enrolling, grandparents and the partnership policy, PowerSchool and Schoology, bullying off campus, fees, the bus fleet (25 to 24) and First Student, services for private school students, inspecting curriculum, the phone and smartwatch rules | 16 | 101 | 1 | 16 MB |
| `alvirne-and-palmer-cte.md` | Palmer's programs, credentials and college credit, its 2021 renovation, sending districts (41% of its 569 students), the Maroon/Gold block schedule, competency grading and the 4.3 GPA, AP and Early College, the class-size rule for electives, Alvirne's enrollment since the 1990s (1,550 in 1997-98) and its NHIAA division, the Alvirne Farm, club stipends | 7 | 82 | 9 | 29 MB |
| `student-support-and-staff.md` | IEP counts and out-of-district placements 2017-18 to 2026-27, the new placement program at Hudson Memorial, para pay and vacancies, custodian pay, turnover, ESOL, translation, counselors and psychologists, 504 plans and the block schedule | 6 | 94 | 7 | 54 MB |
| `money-buildings-and-governance.md` | Budgets and enrollment since FY2015, the default budget's history, administration's share of spending, fund balance projections against audits, surpluses returned, capital reserves, the failed Alvirne renovation bonds, Question 2, local tax caps, tax money and religious schools, the teachers' contract | 8 | 78 | 9 | 29 MB |
| **Total** | | **37** | **355** | **26** | **128 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.15 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Hudson`). All 26 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 34 partial (`tools/coverage.py`).
- **Topics:** two new rule topics were added to `../shared-topics.md`: `local-tax-and-budget-caps` (the local-option caps in RSA 32:5-b to 32:5-f, distinct from the library's Question 2 topics) and `public-funds-and-religious-schools`.
- **Places:** `district Hudson` 339, `town Hudson` 6, no place 9.
- **Places for the backend:** `places.yaml` has no Hudson rows, and none are needed: no district sends Hudson students under contract, and Palmer's sending districts are CTE arrangements, not grade assignments.
- **Draft facts:** four notes cite board minutes the district has posted only as drafts (August 5, 2024 and February 2, 2026).
- **Raw folders:** all under 100 MB.
- **Quotes:** a script checked every quoted passage in the notes against the cited raw copy: 834 of 987 found word for word; the rest are mostly table rows the agents reformatted.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Question 2: 6,639 to 3,382 | The town's signed return; the site's Question 2 data |
  | FY2027 appropriation, $74,173,554 (MS-22R) and $74,173,574 (executive summary) | Both appear in the district's own FY28 papers; each fact cites its own |
  | Full-time para pay, $17.30 in 2026-27 | Teachers' and paras' tentative agreement, Para 1 scale |
  | Custodians, $23.33 to start | Teamsters agreement 2026–2029 |
  | Alvirne, 1,550 students in 1997-98 | NCES school directory (Urban Institute API) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Enrollment down "roughly 25%" over a decade (P1.1) | 19.6% from 2015-16 to 2025-26; about 25% only from 2013-14. The budget did rise every year |
| Voters rejecting the budget "again" (P1.3) | It passed 2023–2026; it last failed in 2022 (also 2013 and 2015) |
| Out-of-district placements "eating up" the budget (P2.3) | Partly: 16 of 480 students with IEPs are placed out of district, about 3.7% of the budget (estimate); the district names tuition and transportation as cost drivers |
| Palmer's renovation is complete (P3.1) | Right: finished 2021 ($25 million bond, with state money) |
| Block scheduling (P3.2) and "Maroon and Gold days" (P16.2) | Right: A/B Maroon/Gold blocks since 2022-23 |
| Competency-based grading (P5.2) | Right, alongside a weighted 4.3 GPA |
| "Running Start" (P5.1) | Renamed Early College at Your High School |
| Paid co-ops at Palmer (P3.3) | None found; internships are usually unpaid |
| Before- and after-care at the Early Learning Center (P4.1) | Right: Champions (KinderCare) at Dr. H. O. Smith |
| Math lower than Windham and Londonderry (P4.2) | Right in 2026 at grades 6–8 and 11; in 2025 Hudson's grade 8 beat Londonderry's |
| Schoology grades (P10.1) | Partly: grades are in PowerSchool; Schoology holds assignments |
| Neighbors pay more (P6.1) | Right through 2024-25 |
| Teacher contracts voted down (P6.3) | The teachers' contract last failed in 2013; the current one ends June 30, 2027 |
| Alvirne over 1,500 in the late 1990s, under 1,000 now (P12.1) | Right: 1,550 in 1997-98, 976 in 2024-25; the board capped it at 1,500 then |
| Routes consolidated for driver shortages (P13.3) | Not shown: the fleet went from 25 to 24 buses by rerouting; drivers work for First Student |
| Pay behind retail and warehouse jobs (P15.1) | Mixed: part-time paras ($20) and custodians ($23.33) start above the area's medians; full-time paras start at $17.30 |
| Paras pulled to cover substitutes (P15.2) | Not confirmed: the special services director said IEP para services can't be removed to substitute |
| No tax cap (P17.1) | Hudson passed Question 2, 66.25% yes |
| Schools drive tax increases (P9.1) | Not in 2025: the town rate rose $0.60 while the school rate fell $0.13 |
| A legal right to buses, nursing, textbooks for private school students (P14.1) | Buses within Hudson and borrowed textbooks, yes; nursing isn't required |

## Corrections and additions to earlier files

- **Salem** (`Salem/money-buildings-and-governance.md`, `district-board-and-public-input` 6): the March 2025 budget cap article cited "RSA 32:5-d"; the fact now says so and adds that the per-pupil school budget cap is RSA 32:5-e (adopted under RSA 32:5-f), RSA 32:5-d being the disclosure of state funding. Salem is loaded locally, so the correction is copied to the backend and reloaded with the batch.
- **Merrimack** (`high-school-and-pathways.md`, `cte-center-programs`): Palmer's own list shows 31 Merrimack students in 2025-26; Merrimack's "about 60" counts the Nashua center too. No change needed.

## Library corrections

Applied November 16, 2026 to both library copies (backend commit `c7c868a`), except those marked for review:

- `district-practices.md`, `kindergarten-entry-cutoff` 41 (Hudson) says policy JEB was "not retrieved"; it is now (`schools-and-daily-life.md`, waiver requests by March 15, decisions by May 15).

## For the site's data

`recommended-improvements.md` A8 item 5: the site's 2025-26 average teacher salary for Hudson ($75,165, up from $60,000) and 281.0 teacher FTE don't match the district's own figures (an average base of $66,794.18 and 239.3 FTE for 2026-27). NH DOE's files say the same as the site; the decision (November 16, 2026) is to keep NH DOE's numbers.

## Not retrieved

The browser pass (November 16, 2026) didn't open these: both are PDFs on hosts that refuse automated downloads, and Chrome's PDF viewer can't be read.


- UNH Library's late-1990s Hudson town reports (HTTP 403), for Alvirne's enrollment then and the Litchfield history (P12.1, P12.3).
- A federal 504 guide on ed.gov (HTTP 403); the library's 504 topics already cover it.
