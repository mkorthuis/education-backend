# Concord: Research for Ask NH Education Facts

Cited facts and figures for answering Concord, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 40 resident profiles with 3 questions each, numbered P1.1 to P40.3 in `questions.md`; the people are invented. The research is in the nine files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Manchester, Nashua, Derry and Dover. Concord is SAU 8: five elementary schools (Mill Brook and Broken Ground paired), Rundlett Middle School, Concord High School and the Concord Regional Technical Center. Penacook, a village of the city, is in the Merrimack Valley School District. **The new middle school is being built on the current Rundlett site on South Street, not at Broken Ground,** which changes the answer to about 15 questions.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `new-middle-school.md` | The site decisions (Broken Ground in 2023, rescinded in January 2025, South Street approved in October 2025), cost estimates over time, borrowing, the guaranteed maximum price, the Nashua comparison, the charter amendments on moving a school, geothermal, wetlands studies, outreach, the old building's future | 5 | 62 | 2 | `raw/middle-school-project/` (84 MB) |
| `getting-to-school-and-safety.md` | The district's own buses (FY2027 $6.6 million), walk zones by grade, the rider fee, Penacook's Merrimack Valley routes, the disputed bus loop at the new school, walking routes the city plows, bus monitors, SROs and the district's tip form | 5 | 56 | 4 | `raw/daily/` (61 MB) |
| `elementary-schools.md` | No gifted program (and NH's 0.7% against 7.0% nationally), grade 8 Algebra, kindergarten class sizes by class, YMCA care at Mill Brook, the free 21C program, preschool and the universal pre-K goal, iPads and screen time, phones and watches | 10 | 62 | 2 | `raw/elementary/` (36 MB) |
| `high-school-and-pathways.md` | The CRTC's programs, credentials and college credit, sending districts' costs, AP courses and how many run, AP participation by race, Early College, the Seal of Biliteracy, computer science and personal finance requirements, civics reporting | 10 | 78 | 6 | `raw/high/` (52 MB) |
| `student-life-and-climate.md` | Suspensions by race (federal data), restorative practices, bullying, student board members, homeschool and EFA access, Rundlett's lunch block, no-cut teams, course levels and English learners, meals | 11 | 93 | 2 | `raw/climate/` (47 MB) |
| `special-education-and-health.md` | Counselors per student, 504 plans (295, 263 for mental health), IEP paperwork hours, AAC devices, transition planning from 14, Riverbend's liaison and Project AWARE, the CARE Team, nurses, evaluation and dispute steps | 9 | 79 | 4 | `raw/sped/` (39 MB) |
| `families-and-support.md` | Homeless students (122 in February 2026), liaisons and contracted interpreters, translation on request, the Care Closet and food backpacks, summer meals, custody and pick-up rules, domestic violence address confidentiality, foster care | 11 | 77 | 2 | `raw/support/` (27 MB) |
| `money-and-governance.md` | Why the school tax rose while the budget held flat, the first $75.95 million bond and its sample costs, state building aid ($0 expected), administration cost per pupil, the revaluation, elderly exemptions, public comment | 7 | 72 | 4 | `raw/money/` (67 MB) |
| `buildings-staff-and-comparisons.md` | Repairs at the current Rundlett, the capital plan, HVAC bonds, Beaver Meadow's humidity problem, custodial and repair budgets, substitutes, teacher absence data, para needs, starting pay against rents, comparisons with Bow, Hopkinton and Pembroke | 7 | 65 | 5 | `raw/staff/` (80 MB) |
| **Total** | | **75** | **644** | **31** | **493 MB** |

`brief.md` is the brief the research agents worked from. Nine agents used about 4.3 million tokens. When the new-middle-school agent confirmed the site, the three agents whose questions assumed Broken Ground were told, and they answered from South Street, citing that file.

## Checks

- **Parser:** all nine files pass the backend's parser (`tools/check_town.sh Concord`). Every table is linked to a topic.
- **Topics:** five new topics were reviewed and added to `../shared-topics.md`: `high-school-offerings-and-seals-rules`, `school-meal-modifications`, `summer-and-vacation-meal-rules`, `teacher-absence-and-diversity-data` and `research-property-tax-and-rents`.
- **Places:** `district Concord` 535, `town Concord` 60, no place 43, `district Merrimack Valley` 6.
- **Draft facts:** eight notes are flagged. Six cite documents marked draft (four 2026-27 handbooks headed "2025-2026 - DRAFT", committee minutes and a draft budget); one is the new school's guaranteed maximum price, still awaiting a board vote; one is the phrase "pending resolution" in a policy.
- **Raw folders:** all under 100 MB.
- **Spot checks:** each agent checked 3 or more facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | Project cost $168,777,480, $155,718,801 after rebates | District information session, October 7, 2025 |
  | The motion to rescind Broken Ground and return to Rundlett | Board minutes, January 22, 2025 |
  | The first bond, $75,950,000 | Debt schedule, March 16, 2026 |
  | 122 students experiencing homelessness | Student Services FY2027 presentation |
  | Concord High's 1,265 students (including 116 from Deerfield) | Board packet, November 2, 2026 |
  | YMCA care at $103 a week (members), $111 (others) | YMCA school-age child care page |
  | Bus eligibility at 1 mile (K–5) and 1.5 miles (6–8) | Policy 711 |

## Premises checked

| Question says | What the sources show |
|---|---|
| The new middle school is moving to Broken Ground (P1.3, P2.1, P3.1, P3.3, P13.1, P18.1, P18.3, P26.1, P29.1, P29.3, P33.1, P34.1, P39.1) | Out of date: the board rescinded Broken Ground on January 22, 2025 (6–3) and approved the South Street project on October 23, 2025 (8–1); ground was broken on September 26, 2026, students move in during 2028-29, and the old building is to be torn down and replaced with fields |
| "$152 million" (P4.1, P24.1) | The July 2024 cap for the Broken Ground design; borrowing of up to $168,777,480 was authorized on January 28, 2026 (9–0), about $155.7 million after expected rebates |
| Nashua built a similar school "for far less" (P4.1) | The district's 2024 comparison put Concord at $475 a square foot against $495–625 for Nashua's McCarthy, with differences in scope |
| No line-by-line comparison of the two sites (P25.1) | The district posted three |
| "The 1955 Rundlett building" (P29.2) | Built in 1957 |
| A citywide referendum on the site (P24.2) | The charter lets the board borrow on a two-thirds vote after a hearing; since July 2025, voter-approved amendments require a district vote to move a school off its parcel or sell more than an acre |
| Wetlands and vernal pools at Broken Ground (P39.1) | 2023 studies found none |
| Net-zero or geothermal (P39.2) | Geothermal heating and cooling, with 84 wells |
| Penacook students and Concord's middle school (P2.1, P14.2, P30.1, P30.2) | Penacook is in the Merrimack Valley School District, whose middle and high schools are in Penacook; it pays Merrimack Valley's school tax rate |
| The 1.5-mile walk zone (P3.3, P15.2) | Correct for grades 6–8; 1 mile for K–5 and 2 miles for grades 9–12, with a $25 high school rider fee |
| Bus monitors on problem routes (P18.2) | Monitors are hired for special-needs buses only |
| The state's "See Something, Say Something" system (P35.3) | Concord's is the district's own tip form |
| Few students in gifted programs (P1.1) | Understated: Concord has no gifted program; in 2023-24 about 0.7% of NH students were in gifted programs, against 7.0% nationally |
| Grade 8 Algebra (P1.2) | Offered; 82 eighth graders took it in 2023-24 |
| No universal public pre-K (P36.1) | Correct; the January 2026 strategic plan includes designing one |
| Half-day or early-release days (P36.3) | None in 2026-27 |
| Hotspots and Chromebooks (P9.2) | No hotspot lending found; take-home Chromebooks start at Rundlett |
| Schools using White Park and Oak Hill (P39.3) | No source shows it; Project SEE uses White Farm and local trails |
| Suspension gaps "in state data" (P4.3) | They're in federal civil rights data (2023-24: 7.5% of Black, 8.9% of Hispanic, 6.0% of multiracial and 3.3% of White students); NH DOE's counts have no race breakdown |
| A 20-minute lunch at Rundlett (P20.3) | A 30-minute lunch and recess block |
| Weighted honors classes (P19.1, P21.2) | Concord High has no honors level ("Advanced" and AP) and weights no courses |
| A voting student board member (P19.2) | State law makes student members nonvoting |
| Cuts from Rundlett's teams (P15.3) | Rundlett's teams don't cut players |
| AP at St. Paul's School (P8.1) | St. Paul's has no AP curriculum |
| Running Start (P32.2) | Now called Early College |
| "Concord Regional Technical Center" (P32.3) | Correct; the library calls it the Technology Center |
| Transition planning "at age 16" (P12.2) | New Hampshire starts it at 14 |
| Concord High's counseling ratio against the state (P5.2) | About 181 students per counselor, against 186 statewide |
| A separate commercial tax burden (P5.3) | New Hampshire doesn't allow a separate commercial rate |
| The budget climbs while enrollment falls (P6.1) | Partly: spending rose 46% over ten years while enrollment fell 16%, but the FY2027 general fund rose about 1.9%; the local school tax rose about 13.7% because other revenue fell about $7.2 million |
| Administrative cost per pupil isn't shrinking (P25.2) | Correct: $1,356 (2016) to $2,802 (2025) |
| Guaranteed state building aid (P25.3) | None is guaranteed; NH DOE says nothing is appropriated, and the district expects $0 instead of $31.8 million |
| Custodial budgets trimmed first (P22.2) | Not in FY2027: custodians got a 3.25% raise; summer repair projects lost $500,000 |
| Aging boilers (P22.3) | Most heating plants were converted to gas in 2012–2017 |
| The school leaving the South End (P34.1) | It stays on South Street |
| Cultural liaisons and bilingual coordinators (P33.2) | No such titles; each school has a home-to-school liaison or social worker, and interpreting is contracted |
| Guaranteed translated report cards and interpreters (P13.3) | No written guarantee; documents are translated when a family asks |
| Chronic teacher absenteeism (P8.3) | No current data: the last federal count (2017-18) put 28.4% of Concord's teachers and 29.6% of NH's absent more than 10 days |

## Corrections and additions to earlier files

- **Nashua, `district-student-support` 46 (note):** its quote of policy JFABE ("children awaiting foster care may also qualify as homeless") reflects the federal definition before December 2016; the note now says so and points to the statute here.

Nothing in Concord's files contradicts an earlier town.

## Coverage

48 questions are answered **fully**, 71 **partly** and 1 by the site's data alone; none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Elena Rostova | **full** | partial | **full** |
| P2 Marcus Vance | **full** | **full** | partial |
| P3 Amina Hassan | partial | partial | partial |
| P4 David & Sarah Miller | **full** | **full** | partial |
| P5 Brenda Kowalski | partial | **full** | partial |
| P6 Carlos Mendez | **full** | **full** | partial |
| P7 Jennifer "Jen" O'Connor | **full** | **full** | partial |
| P8 Dr. Raj Patel | partial | **full** | partial |
| P9 Tanya Brooks | **full** | partial | **full** |
| P10 Greg & Hannah Lindqvist | **full** | partial | **full** |
| P11 Keisha Washington | partial | partial | partial |
| P12 Paul Thibodeau | partial | partial | **full** |
| P13 Mai Nguyen | **full** | partial | partial |
| P14 Stephanie Alverez | partial | partial | partial |
| P15 Derek Henderson | partial | partial | **full** |
| P16 Margaret "Maggie" Sullivan | partial | **full** | partial |
| P17 Jordan Vance-Kerr | **full** | partial | partial |
| P18 Raymond "Ray" Bouchard | **full** | partial | partial |
| P19 Chloe Zhang | partial | **full** | partial |
| P20 Liam O'Malley | **full** | partial | partial |
| P21 Fatima Al-Mansoor | partial | partial | partial |
| P22 Arthur Pendelton | partial | partial | partial |
| P23 Naomi Goldstein | partial | **full** | partial |
| P24 Walter & Eleanor Henderson | partial | **full** | **full** |
| P25 Gerald "Gerry" Morin | **full** | **full** | **full** |
| P26 Patricia "Pat" Simmons | **full** | partial | **full** |
| P27 Rev. Thomas Sterling | **full** | partial | **full** |
| P28 Cynthia Cho | partial | partial | **full** |
| P29 Douglas "Doug" MacLeod | **full** | **full** | partial |
| P30 Barbara Ann Kowalczyk | partial | partial | partial |
| P31 Marcus Aurelius "Marc" Bell | **full** | partial | **full** |
| P32 Dr. Evelyn Vance-Sterling | partial | **full** | partial |
| P33 Samuel "Sam" Osei | partial | partial | partial |
| P34 Megan Gallagher | partial | data only | **full** |
| P35 Officer Brian Callahan | partial | partial | partial |
| P36 Denise Pelletier | **full** | partial | **full** |
| P37 Trevor Jenkins | partial | **full** | **full** |
| P38 Rachelle Beaulieu | partial | **full** | partial |
| P39 Harold "Hal" Perkins | **full** | **full** | partial |
| P40 Vanessa Morales | partial | partial | partial |

## Notable findings

- **The middle school:** after choosing Broken Ground in December 2023, the board returned the project to South Street in 2025. Construction began in fall 2026; the first $75.95 million of bonds sold in March 2026 at 4.08%, and the guaranteed maximum construction price of $132.6 million awaited a vote in November 2026. The planned bus loop through Noyes and Cypress streets is disputed with the city.
- **State building aid:** the project ranks first on NH DOE's list, but no aid is appropriated, and the district expects none; that adds over $17.7 million in interest.
- **The FY2027 tax jump:** the budget held nearly flat with 37 positions cut, but non-property-tax revenue fell about $7.2 million, so the local school tax rose about 13.7%.
- **No gifted program**, in a state where 0.7% of students are in one (7.0% nationally).
- **Homelessness:** 122 students in February 2026, up from 75 a year earlier; the elementary count doubled.

## Library notes (not changed here)

- `money-school-building-aid-2026-27` 6: its $164,623,927 and 214,105 square feet are the January 2025 Rundlett estimate and the aid application's size; the approved project is $168,777,480 gross (about 205,562 square feet), and NH DOE says no building aid is appropriated.
- `cte-centers-overview` 6: the center is the Concord Regional **Technical** Center.
- `kindergarten-entry-cutoff` 16: it quotes the registration page's "NO exceptions (Policy 512)", but Policy 512 (revised July 10, 2023) provides for early admission requests to the superintendent.
- `district-preschool` 18: the handbooks give different preschool times by school.
- `nhdoe-special-education-help` 2 gives the state complaint address as 25 Hall Street; `special-ed-disputes` 6 and Concord's 2025 manual give 101 Pleasant Street.
- `property-tax-relief` (in the Hart's Location file): these state rules belong in the library (also noted by Nashua).

## Browser pass, November 15, 2026

Added from pages read in Chrome or linked from them: the new Deerfield–Concord MOU (a new `district-tuition-contracts` section in `money-and-governance.md`; the places.yaml note mentions it, uncommitted), the state Seal of Biliteracy criteria (`high-school-and-pathways.md` high-school-offerings-and-seals-rules 6; P21.1 updated), and the library's Library of Things, which lists no hotspots (`elementary-schools.md` town-broadband 2). The October 26 minutes and November 2 packet confirmed what the agents had; the guaranteed maximum price still awaits a board vote. NH DOE and ed.gov PDFs (the building aid list, the foster care contact list, CRDC documents) can't be read in Chrome's PDF viewer. Concord now has 647 facts.

## Gaps to retry

- **Blocked to automated requests:** sau8.org (8 pages), education.nh.gov (5), ed.gov (5), concordnh.gov (3), including NH DOE's building aid list, the Seal of Biliteracy page and the November 2 board minutes with the price vote.
- Not found anywhere: Concord High's AP exam results; Concord's own Seal of Biliteracy process; remedial math placement by high school; translated project documents beyond the 2023 hearing invitations; air-quality monitoring of the construction; a deferred maintenance total; staff counts by race; teacher turnover; front-office training on custody orders; vacation-week meals; the tax year 2026 rate.

The shared web search limit ran out early in most agents' work, so news coverage was searched little.
