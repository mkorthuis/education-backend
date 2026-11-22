# Nashua: Research for Ask NH Education Facts

Cited facts and figures for answering Nashua, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 40 resident profiles with 3 questions each, numbered P1.1 to P40.3 in `questions.md`; the people are invented. The research is in the nine files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Manchester and Concord. Nashua is SAU 42: 12 elementary schools (K–5), the Franklin Street preschool, three middle schools (McCarthy, which replaced Elm Street in August 2024, Fairgrounds and Pennichuck), Nashua High School North and South, and Brentwood Academy. The Academy for Science and Design and Riverwood Academy (formerly MicroSociety) are charter schools in the city.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | Franklin Street (special education preschool) and PlayPals, before- and after-school care at Ledge Street, class-size caps, twins' placement (RSA 193:3-a), reading scores by school against meal eligibility, kindergarten, gifted services | 10 | 76 | 3 | `raw/elementary/` (36 MB) |
| `middle-schools.md` | McCarthy and the Elm Street move, zones redrawn, capacity, sixth-grade teams, phones, Fairgrounds math, grade 8 high school credit, honors placement, Chromebooks, tech ed, Aspen | 11 | 90 | 2 | `raw/middle/` (17 MB) |
| `high-schools.md` | AP counts and 2025 pass rates, North and South compared, counselors, the daily shuttle, VLACS and outside credits, graduation requirements, credit recovery, Brentwood Academy, the adult diploma program, the attendance plan, SAT participation | 7 | 83 | 3 | `raw/high/` (11 MB) |
| `pathways-and-adult-learning.md` | The Nashua Technology Center (HVAC and Electrical at South), Early College costs, apprenticeships, the Adult Learning Center's English and HiSET classes, para-to-teacher help, college transfer, the public library | 10 | 66 | 0 | `raw/pathways/` (44 MB) |
| `special-education.md` | Speech and related services, contracted therapists, 92 openings, out-of-district placements, independent evaluations, 504 plans and middle school teams, EFAs and special education, guardianship papers | 9 | 85 | 7 | `raw/sped/` (29 MB) |
| `families-and-support.md` | The English learner plan, the 2026 service shortfall and the Justice Department settlement, counselors per school, meal prices and applications, translation, military families, foster care contacts | 7 | 108 | 3 | `raw/support/` (30 MB) |
| `getting-to-school-and-zones.md` | Before-school care, bus contract rates, crossing guard vacancies, charter buses, start times, staying at a school after a move, open enrollment, zones and the facilities plan's closure options, home values | 9 | 64 | 3 | `raw/daily/` (56 MB) |
| `charter-private-and-home.md` | ASD's lottery, waitlist and programs, Riverwood (renamed August 31, 2026), Gate City's scores, Bishop Guertin and EFAs, World Academy, home education since July 2026, activities for charter and home-educated students | 8 | 72 | 0 | `raw/choices/` (12 MB) |
| `money-and-governance.md` | The budget's growth, schools' 53.6% of the city's general fund, the middle school bonds, the Elm Street sale plan, senior exemptions, spending compared, para and teacher pay, facility rental, public comment | 8 | 66 | 4 | `raw/money/` (31 MB) |
| **Total** | | **79** | **710** | **25** | **266 MB** |

`brief.md` is the brief the research agents worked from. Nine agents used about 4.2 million tokens.

## Checks

- **Parser:** all nine files pass the backend's parser (`tools/check_town.sh Nashua`). Every table is linked to a topic.
- **Topics:** five new topics were reviewed and added to `../shared-topics.md`: `district-facility-use`, `town-library-services`, `college-transfer-nh` (the last two given generic titles), `educator-expense-deduction` and `research-school-start-times`. The zone facts use Manchester's `district-attendance-zones-and-transfers`.
- **Places:** `district Nashua` 544, no place 67, `town Nashua` 66, `district Academy for Science and Design Charter School` 27, `district MicroSociety Academy Charter School Foundation` 6. World Academy's and Bishop Guertin's facts use `town Nashua` (World Academy's district name in the site's data ends with a space).
- **Draft facts:** four notes cite drafts: the 2026-27 open enrollment procedures (later adopted) and the city's draft Skills Gap Analysis. A fifth flag is the word "pending" in the board's public comment policy.
- **Raw folders:** all under 100 MB.
- **Spot checks:** each agent checked 3 to 10 facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | The FY2027 education appropriation of $205,367,867 (53.64% of the general fund) | City's adopted budget |
  | $109,295,000 of middle school bond principal owed on July 1, 2026 (sum of four bonds) | City's adopted budget, bond schedules |
  | 1,663 students owed English learner services (867 at levels 1–2, 796 at levels 3–4) | February 2026 ELL presentation |
  | PlayPals tuition of $240 a month | NEEP PlayPals page |
  | 58% of crossing guard posts unstaffed at the start of 2023-24 | September 12, 2023 committee agenda |
  | MicroSociety becoming Riverwood Academy on August 31, 2026 | The school's release |

## Premises checked

| Question says | What the sources show |
|---|---|
| "The district's FY 2026 budget is $191.2 million" (P26.1) | Correct ($191,262,559 with benefits) |
| "Going up 4% a year" (P26.1) | 3.0–5.0% a year for FY2023–FY2026, then 7.4% to $205,367,867 for FY2027 |
| "Enrollment isn't growing" (P26.1) | Correct: down 17.3% since 2014-15, while special education and English learner counts rose |
| McCarthy "replaced Elm Street Middle" (P9.1) | Correct: Elm Street closed and McCarthy opened in August 2024, and all three middle school zones were redrawn |
| Elm Street's overcrowding (P9.1) | Supported: 1,093 students in 2018-19 against a goal of about 800; McCarthy has 653 with room for 917 |
| "The bond for the new McCarthy Middle School" (P27.2) | No single bond: four bonds ($114.7 million) also paid for the Fairgrounds and Pennichuck renovations; $109.3 million of principal was owed on July 1, 2026 |
| The old Elm Street building (P26.3) | Resolution R-24-032 plans its sale for housing, with conditions; it served as a warming station in FY2026 |
| Senior relief for "30 years" in Nashua (P27.1) | Years in Nashua don't count: the exemption depends on age, income, assets and 3 years in New Hampshire |
| Nashua spends less than Hudson, Merrimack or Hollis (P27.3) | Correct (FY2025); Hollis runs only K–6 |
| Fairgrounds math "lower than the state average" (P10.3) | Correct: 29% proficient in spring 2026, against 40–44% statewide in grades 6–8 |
| "Six different teachers" in middle school (P12.1) | Middle schoolers are on teams of 4 teachers |
| Shop classes cut (P39.2) | Not supported: all three middle schools list tech ed |
| "1,500-plus kids at South" (P16.3) | Correct: 1,663 in October 2024 |
| How many AP classes South offers (P16.1) | Sources disagree: 17 (South's home page), 19 (May 2026 board presentation), 22 (college profile) and 25 (2026-27 catalog) |
| Buses between North and South (P18.1) | Shuttles still run daily |
| HVAC or electrical "at North" (P15.2) | Only at South; North students take the shuttle |
| Running Start (P17.1) | Now called Early College at Your High School |
| Brentwood Academy as an alternative school (P20.2) | It's a therapeutic special education program entered by referral; the adult diploma program (mostly 3–6 p.m.) is open to any student |
| Scholarships for Nashua graduates in nursing or business (P17.2) | None found just for them |
| A medical assistant certificate at the Adult Learning Center (P33.2) | Not offered; the route found is a paid NCC and Southern NH Health apprenticeship |
| City training grants (P34.2) | The city offers none |
| The Franklin Street preschool (P1.1) | A special education preschool (about 80% of children have special needs); other 3-year-olds enter through PlayPals ($240 a month), which keeps a waitlist |
| Before- and after-school programs at Ledge Street (P1.2) | No before-school program; the after-school program costs $2.50–$10 a day by meal status |
| Free full-day kindergarten (P7.1) | No charge is listed, though no page says "free" |
| Gifted groups at Bicentennial (P2.1) | No gifted program found |
| "MicroSociety Academy Charter School" (P14) | Renamed Riverwood Academy on August 31, 2026; preschool to grade 8 |
| ASD's lottery "for fifth grade" (P2.3) | Correct; the 2027-28 deadline is January 6, 2027, and the waitlist was 176 |
| Gate City's scores "lower than the Nashua average" (P21.1) | Correct for all grades, 2024–2026; its 2026 growth was higher than Nashua's |
| EFA funds for Bishop Guertin (P19.1) | Bishop Guertin accepts them; the 2026-27 enrollment cap was reached |
| A homeschool notice and year-end assessment (P23.1) | Out of date since July 1, 2026 |
| World Academy through high school (P24.1) | No: it ends at grade 8 |
| Bus driver shortages (P5.3) | Fall 2024 problems the board called "unprecedented"; 2025-26 started smoother |
| Crossing guards at all busy intersections (P8.1) | No: 58% of posts were empty in September 2023 and 30% in March 2024, and eight were advertised in November 2026; guards are school district employees |
| A city bus to charter schools (P14.2) | The buses are the school district's |
| Later high school start times (P35.3) | Both start at 7:20 a.m., and no proposal appears in the minutes from 2021 to 2026 |
| Recent zone changes and redistricting (P29.2) | No elementary changes since 2023; the facilities plan's options would close one to five schools, most of them Mount Pleasant |
| Time in the ELL program (P33.3) | Students exit at a 4.5 score and are monitored for 4 years; most already spend most of the day in regular classes |
| Notices in Arabic (P8.3) | Arabic isn't one of the district's translation languages; translation or an interpreter is given on request |
| A military family liaison (P37.1) | None found; the military compact doesn't cover drill weekends |
| Free meals for foster children (P38.3) | Correct, automatically |
| Free and reduced meals cover breakfast (P5.2) | Correct; reduced-price breakfast costs nothing |

## Corrections and additions to earlier files

None were needed. Nashua's home education policy is out of date in the same way as Conway's (both describe the rules before July 2026), and Nashua's foster care policy cites the 2017 state guidance where Conway's facts use the 2024 version; neither is a conflict.

Manchester and Nashua each wrote some of the same state rules with no place (guardianship, special education evaluations). These are merged in one pass after Concord and Derry finish.

## Coverage

63 questions are answered **fully**, 54 **partly** and 3 by the site's data alone; none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Elena Morales | **full** | **full** | **full** |
| P2 Marcus & Priya Patel | partial | **full** | **full** |
| P3 Trevor Jenkins | partial | partial | **full** |
| P4 Hannah Lindqvist | partial | **full** | partial |
| P5 Carlos & Sofia Mendes | partial | **full** | partial |
| P6 Brittany O'Connor | partial | partial | **full** |
| P7 Devon & Maya Brooks | partial | data only | **full** |
| P8 Amina Hassan | partial | **full** | partial |
| P9 Greg Kowalski | partial | partial | partial |
| P10 Lauren & Chris Beaulieu | partial | **full** | partial |
| P11 Sanjay Rao | partial | **full** | partial |
| P12 Tasha Williams | partial | **full** | **full** |
| P13 Kevin & Rachel Dubois | partial | partial | **full** |
| P14 Nadia Al-Mansoor | partial | **full** | data only |
| P15 Anthony Russo | **full** | partial | partial |
| P16 Michelle & David Chen | partial | partial | **full** |
| P17 Mateo Silva | **full** | partial | **full** |
| P18 Zoe Kravitz-Miller | **full** | **full** | **full** |
| P19 Diane & Robert Pelletier | **full** | partial | **full** |
| P20 Jasmine Ortiz | **full** | **full** | **full** |
| P21 Samantha & Ben Gallagher | data only | **full** | **full** |
| P22 Priya Nair | partial | **full** | **full** |
| P23 Rebecca & Luke Vance | **full** | **full** | **full** |
| P24 Ken & Chloe Tran | **full** | partial | partial |
| P25 Miriam Goldstein | partial | **full** | **full** |
| P26 Arthur "Artie" Deschamps | **full** | **full** | partial |
| P27 Linda & Paul Mercier | **full** | **full** | partial |
| P28 Rajesh Verma | **full** | partial | partial |
| P29 Stephanie Vance-Keller | partial | **full** | **full** |
| P30 Tomás Herrera | partial | partial | **full** |
| P31 Megan Callahan | partial | partial | **full** |
| P32 Darnell Washington | **full** | **full** | **full** |
| P33 Fatima Al-Khoury | partial | **full** | partial |
| P34 Jordan Reyes | partial | **full** | partial |
| P35 Dr. Evelyn Park | **full** | partial | **full** |
| P36 Caleb & Hannah Foster | **full** | partial | partial |
| P37 Sgt. Brian Miller | partial | **full** | **full** |
| P38 Brenda Novak | **full** | **full** | partial |
| P39 Victor Almeida | partial | **full** | partial |
| P40 Clara Lin | partial | **full** | **full** |

## Notable findings

- **AP results:** 91% of South's 284 AP students and 86% of North's 214 scored 3 or higher in 2025, up from 75% and 63% in 2021.
- **English learners:** in February 2026 the district said it was missing required English learner time in half its elementary schools (1,663 students owed services); the FY2027 budget adds 4 teachers. The Justice Department's 2021 settlement over English learner services ended in May 2025.
- **Special education contracts** went from $33,305 in FY2022 to an estimated $7.94 million in FY2026, and the district listed 92 openings in November 2026, 39 of them paraprofessionals.
- **Reading by school:** 2025-26 reading proficiency ranged from 17% to 65% across the 12 elementary schools; the five with the most meal-eligible students had the five lowest rates (derived from the site's data).
- **The facilities plan:** most of its options close Mount Pleasant; none has been adopted.

## Site data issues found

- Elm Street Middle School's enrollment and safety counts aren't in the site's data (closed schools; see A10 in `../recommended-improvements.md`).
- World Academy's district name ends with a space.
- Riverwood Academy has no 2026 school-level test results, though the 2026 results by grade are there.
- Gate City's and Riverwood's web addresses in the site's data are stale; Gate City's old address now shows an unrelated gambling page.
- The city's tax rate page swaps the 2025 county and state education rates; the site's DRA figures are right.

## Library notes (not changed here)

- `granite-edvance` 1: the phone is given as 603-225-6612; Granite Edvance's site now lists 603-227-5444 for FAFSA and college questions and 855-887-5430 for loans.
- `budget-form-and-vote-dates` 94: the aldermen adopted $205,367,867 for FY2027.
- `dual-enrollment-rules` 3 and 7: Nashua's Program of Studies words the free courses as "Students over the age of 16 receive (2) Free Classes", a third version beside the statute and CCSNH's.
- `cte-centers-overview`: has no Nashua Technology Center facts; `pathways-and-adult-learning.md` here fills that in.
- `property-tax-relief` (in the Hart's Location file, no place): these state rules belong in the library.
- ASD doesn't take part in the federal free and reduced-price meal program, which explains its low counts in the site's data.

## Gaps to retry

- **nashua.edu (about 10 pages) and its school subdomains, education.nh.gov and my.doe.nh.gov (8),** blocked to automated requests; open in a browser.
- Gate City's current website (the listed address is gone).
- Not found anywhere: on-time bus data; crossing guard posts by school; an elementary zone map; teacher turnover by school; gifted services; recess and specials minutes at Charlotte Avenue; which middle schools teach Algebra 1 in grade 8; middle school activity fees; how charter and private students fare after moving to South; college enrollment by high school.

The shared web search limit ran out partway through most agents' work, so news coverage was searched little.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 14 saved bus and transportation copies (20 in all; schools, child care centers, businesses and other public places keep theirs).
