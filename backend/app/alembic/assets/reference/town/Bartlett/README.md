# Bartlett: Research for Ask NH Education Facts

Cited facts and figures for answering Bartlett, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The research is in the reference library's format (`../../additional-data/README.md`) and uses the shared topics in `../shared-topics.md`. It isn't loaded into the Ask yet; see `../recommended-improvements.md`.

Gathered November 13, 2026. This is the second town, after Jackson, and the first to use the shared topics, the `place: sau 9` tag, and the shared SAU 9 folder.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `jbes.md` | Josiah Bartlett Elementary: classrooms and staff, math, Spanish and Algebra, special education and 504s, preschool, ski days and recess, arts, English learners, counseling, Chromebooks, homeschool access | 11 | 103 | 2 | `raw/jbes/` (40 MB) |
| `money-and-governance.md` | Cost per pupil, budget drivers, Kennett contracts (current and 2027–32), Kennett's share of the school tax (derived), state aid in the district's reports, capital and energy, the SAU 9 study committee, Hart's Location's contract and voice, board vs SAU | 8 | 94 | 6 | `raw/money/` (78 MB) |
| `daily-life-and-community.md` | School hours and care, buses and drivers, attendance, meals, fees, homeschool rules, EFA tutors and programs, infant care, Bartlett Recreation and summer, late buses, Safe Routes, Hart's Location storms | 10 | 84 | 5 | `raw/community/` (36 MB) |
| `../sau9/kennett-and-sau9.md` (shared) | Kennett transition steps, STEM and college destinations, career center access and credentials, dual enrollment, IEP moves to Kennett, translated notices, AP and dual enrollment research, clubs | 7 | 86 | 2 | `../sau9/raw/` (80 MB) |
| **Total** | | **36** | **367** | **15** | **234 MB** |

`brief.md` is the brief the research agents worked from: the Bartlett facts plus a table of what the Jackson research already covered. Jackson's files answer parts of many Bartlett questions (Kennett, SAU 9 policies, storm days, child care); the question tables point to them by topic.

## Checks

- **Parser:** all four files pass the backend's parser (`parse_file`), with one change: `place: sau 9` is accepted. The parser would reject the 10 SAU facts today.
- **Shared topics:** every topic slug, kind and question type matches `../shared-topics.md`.
- **No stray bullets:** no statement runs onto a second line.
- **Places:** every place matches the site's tables: `district Bartlett` (245 facts), `district Conway` (59), `town Bartlett` (28), `district Hart's Location` (11), `sau 9` (10).
- **Adequacy aid update (November 14, 2026):** the site's database now holds NH DOE's adequacy aid calculation for FY2020–FY2027. One fact and the table of adequacy cost against the statewide tax, which only restated it, were removed. Three facts were cut to what the database doesn't have: Bartlett's own revenue page, its FY2023 statement of revenues and Hart's Location's tax rates. The kept figures were checked against the database; the district's 2026-27 estimate of the statewide tax differs from DOE's, as the note says.
- **Tax rates update (November 15, 2026):** the site's database now holds NH DRA's tax rates by town (tax years 2014–2025) and NH DOE's school taxes by town (2011–2025). One fact (Bartlett's 2025 rates and school share) and the table of school taxes in Bartlett and Hart's Location, which only restated them, were removed. Two facts were cut: the estimate of Kennett's share of the school rate no longer works out a tax per $100,000 of value, and Hart's Location's rates were cut to SAU 9's 2026-27 estimate. The figures kept match the database.
- **Spot checks:** each agent checked 3 or 4 of its facts against its raw copies, and all matched. These were then checked again independently, and all matched:

  | Fact | Checked against |
  |---|---|
  | Bartlett's FY2026 adequacy cost and the statewide education tax raised ($1,129,367 and $2,529,838; since removed, now in the site's data) | `additional-data/raw/town/adequacy-aid.csv` |
  | The RSA 91-A:3, II(k) quote on making negotiated contracts and nonpublic minutes public | Saved statute |
  | The deletion of Bartlett's fees policy JN | December 23, 2025 board minutes |
  | JBES hours of 9:00 to 3:15 | 2026-27 handbook |

## Corrections this research made

**To the Jackson files** (all checked against the sources and corrected in place, with a "Corrected" note on each fact):

| Jackson fact | Was | Now |
|---|---|---|
| `school-programs-after-grade-6 25` in `Jackson/after-jackson-grammar.md` | No Kennett step-up day or freshman orientation found | Kennett holds an Eighth Grade Transition Night, staff registration visits and a freshmen-only Transition Day (2024 letter, principal's reports) |
| `district-fees 8` in `Jackson/policies-safety-meals-and-support.md` | Bartlett's fees policy JN in force | Bartlett deleted JN on December 23, 2025 |
| `district-school-day-and-calendar 4` in `Jackson/getting-to-school-and-the-school-day.md` | Current JBES hours not found | 9:00 a.m. to 3:15 p.m. (2026-27 handbook) |
| `district-school-day-and-calendar 26` in `Jackson/getting-to-school-and-the-school-day.md` | JBES handbook couldn't be read | It has no planned-absence or vacation procedure |

**To the Bartlett questions and brief:**
- Hart's Location's contract with Bartlett covers **K–8**, not K–6 as SAU 9's page labels it.
- Bartlett's 2027 Kennett contract **does** have a minimum-attendance clause: 75% of its high schoolers.
- Conway Elementary no longer exists under that name.

## Coverage

27 questions are answered **fully**, 33 **partly**, and none has nothing. As with Jackson, "partly" means either a document isn't posted (ski fees, a fee schedule, 504 timing, camp prices, child care wait lengths) or the question asks for a judgment no data measures ("how well students transition", "stigma", "staying connected"). In those cases the files give the facts that bear on it.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Attitash worker | **full** (JBES 9:00–3:15, no before-school care, Adventure Kids to 4:45) | partial (ESSC ski days; fees not posted) | partial (routes and drivers; no written stop-change rule) |
| P2 Retiree | **full** (what cost per pupil covers) | **full** (tuition share, derived; 8% cap from 2027) | **full** (no bonds 2019–2026; heating lease) |
| P3 Remote tech worker | **full** (no Algebra 1a section; VLACS; Spanish) | partial (transition steps; outcomes by town not published) | partial (STEM courses, destinations) |
| P4 Carpenter | partial (equal access in contracts; no capacity data) | partial (credential and credit counts) | partial (math program; screen time not measured) |
| P5 Homesteader | **full** (JJJ, revision adding EFA students) | **full** (IGBJ predates the 2026 law) | **full** (EFA rules for tutors; 31 valley providers) |
| P6 Rental investor | **full** (formula, cap, term) | partial (how staff presented results) | partial (no K–8 regionalization study) |
| P7 Special education parent | **full** (SLP and reading specialist on staff) | partial (case management; no written procedure) | **full** (budgeting and reserves) |
| P8 Retired teacher | **full** (teacher FTE 23.4 → 17.0 → 20.0; salaries) | partial (academic freedom clause) | partial (shortages 2024–25; filled 2026) |
| P9 Young couple | **full** (preschool ages 3–4, waitlist not lottery, 18 seats) | partial (site data grades 1–2; no K class size) | partial (no program in Bartlett; no waitlist data) |
| P10 Cross-border parent | partial (Jackson counts by grade; joint planning) | **full** (high school choice discussions) | **full** (Bartlett Recreation serves Jackson and Hart's Location) |
| P11 Outdoor guide | partial (Tin Mountain trips) | partial (no planned-absence procedure) | partial (recess required; no cold-weather rule) |
| P12 Fiscal conservative | **full** (budget drivers) | **full** (adequacy vs statewide tax, in the site's data) | **full** (where documents are) |
| P13 Immigrant supervisor | partial (ESOL teacher; 0 English learners in site data) | partial (ParentSquare features; use unknown) | partial (policies, belonging goal, survey) |
| P14 Kinship grandparent | **full** (meal account rules) | **full** (counselor, family liaison, BCBA consultant) | partial (no fee schedule; JN deleted) |
| P15 Kennett sophomore | partial (late bus; no stop list) | **full** (NACAC survey, College Board, research) | partial (clubs, advisory; connection not measured) |
| P16 Private school parent | partial (placement, grade 7 size) | partial (Spanish in grades 3–8; VLACS) | partial (music and art staff, concerts) |
| P17 Conservation volunteer | **full** (energy projects) | partial (no Safe Routes project; NHDOT blocked) | partial (board goal; no student presentations found) |
| P18 Work-from-home parent | partial (SAU 9: "within a reasonable time") | partial (assigned Chromebooks; no screen-time data) | partial (B.E.A.R. format; recent prices missing) |
| P19 Hart's Location parent | partial (no Hart's Location bus stop; mileage paid) | **full** (input as a tuition town) | **full** (K–8 at JBES; one student, Fryeburg mileage) |
| P20 Board candidate | **full** (board vs SAU) | **full** (renewal terms, 75% minimum) | **full** (meetings and outreach) |

## Notable findings

- **Kennett contracts:**
  - Bartlett's 2027–32 contract caps the yearly increase at 8% (Jackson's: 20%) and requires at least 75% of Bartlett's high schoolers to attend.
  - It drops property value from the cost formula and adds about $84,000 a year toward Kennett's building plan (derived).
  - Kennett tuition is 27.0% of Bartlett's 2026-27 school budget.
- **Leaving SAU 9?** A 2026 petition to leave SAU 9 became a study committee. It is comparing Bartlett's roughly $570,000 a year to SAU 9 with single-district SAUs costing $200,000–$300,000.
- **Teacher staffing** fell from 23.4 FTE (2018) to 17.0 (2025), then rose to 20.0 (2026), per the site's data.
- **Advanced math and Spanish:** JBES ran no Algebra 1a section in 2026-27; three students take VLACS Algebra in flex time. Spanish moved into Unified Arts for grades 3–8.
- **Bartlett runs its own buses:** it went from four driver positions to three for 2026-27, and its routes have no stop in Hart's Location.
- **Bartlett Recreation** is a nonprofit serving Bartlett, Jackson and Hart's Location. The school district pays it $24,500 a year, and it gives about $10,000 a year in scholarships.
- **Hart's Location** has one student. It budgets high school tuition and Fryeburg mileage, but no high school contract is posted.

## Gaps to retry

- Bartlett's 2026 tax rate; MS-26 forms.
- Conway's November 15 estimate of the 2027-28 Kennett charge.
- The sealed Kennett negotiation minutes, which RSA 91-A:3, II(k) says must be made public before the district votes.
- ESSC ski program fees.
- Recent B.E.A.R. summer prices.
- NHDOT Safe Routes and Ten Year Plan lists (blocked).
- Career center enrollment and capacity.
- Results for Kennett students by sending town.
- Whether ParentSquare translation is on.
- A written JBES-to-Kennett IEP procedure.
