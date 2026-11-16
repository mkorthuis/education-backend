# Rochester: Research for Ask NH Education Facts

Cited facts and figures for answering Rochester, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 30 resident profiles with 3 questions each, numbered P1.1 to P30.3 in `questions.md`; the people are invented. The research is in the six files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Dover, Salem, Merrimack and Londonderry. Rochester is SAU 54: five elementary schools (Chamberlain Street, East Rochester, Gonic, McClelland and Salmon Falls, which opened in September 2025 and replaced William Allen, School Street and Maple Street Magnet), REACH Preschool at East Rochester, Rochester Middle School, Spaulding High School with the Richard W. Creteau Technology Center, and Bud Carlson Academy. Wakefield sends its high school students to Spaulding under an AREA agreement. The City Council approves the school budget under the charter's tax cap.

**Most of the district's website was out of reach.** rochesterschools.com answers every automated request with a bot check, and rochesternh.gov returns 403. The agents worked from the library's saved district pages, the city's news site, board packets and policies on the district's separate document host, and state and federal data. One agent read eight district pages through the website vendor's host before being told to stop; those facts were checked in a browser on November 15, 2026 and all matched (below).

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | Salmon Falls (no pre-K; opened 2025), REACH Preschool's waiting list, before- and after-school care in every building, Head Start downtown, Title I at East Rochester and Chamberlain Street, reading gains since 2022, school librarians (3.0 positions), summer reading with the city library, twins (Rochester's deadline; the rule is Salem's) | 13 | 60 | 2 | `raw/elementary/` (17 MB) |
| `middle-school.md` | Tryouts and cuts, the participation fee, Algebra I in grade 8 only, counselors (6 for 776 students), no 21st Century program, the library's teen drop-in and the Opera House's classes, Chromebooks, band and instrument loans (Spaulding lends; the middle school doesn't), music and activities budgets | 13 | 60 | 1 | `raw/middle/` (8 MB) |
| `high-school-and-creteau.md` | Creteau's programs and starting grades (no welding, culinary, electrical or computer science; those are at Dover or Somersworth), exploratory courses, Air Force JROTC, Bud Carlson's 20-credit diploma and flexible hours, Spaulding's 26 credits, Early College fees, the phone ban, graduation moved to UNH's Whittemore Center, substance-misuse courses | 9 | 92 | 1 | `raw/high/` (21 MB) |
| `student-support-and-families.md` | The spring 2026 state special education review, therapists on staff, out-of-district placements doubling in the FY2027 budget, Monarch School, suspensions (12.6% against 4.9% statewide), nurses, meals and the no-cost meals study, English learners, PTOs | 9 | 74 | 4 | `raw/support/` (22 MB) |
| `getting-to-school-and-choices.md` | Bus times and ride lengths from the 2026-27 route sheets, no late bus, the zone map (still showing Maple Street Magnet), no in-district transfers for 2026-27, home education access under IHBG, remote days and snow make-up days, St. Charles (a special education program), Tri-City Christian's tuition against the EFA, crossing guards (2021) | 10 | 71 | 2 | `raw/daily/` (25 MB) |
| `money-buildings-and-staff.md` | The FY2027 budget ($83.8 million all funds, a flat $78.0 million general fund), the charter's debt service exception and the 15 restored teaching positions, lower state aid and the 8.2% school tax rise, Salmon Falls' cost and the $1.35 million returned, Wakefield's tuition ($20,042.93), the superintendent's budget options, asbestos and lead rules | 9 | 82 | 6 | `raw/money/` (16 MB) |
| **Total** | | **63** | **439** | **16** | **109 MB** |

`brief.md` is the brief the research agents worked from. Six agents used about 3.0 million tokens.

## Checks

- **Parser:** all six files pass the backend's parser (`tools/check_town.sh Rochester`). Every table is linked to a topic.
- **Topics:** three new topics were reviewed and added to `../shared-topics.md`: `title-i-school-programs`, `remote-learning-and-snow-day-rules` and `school-environmental-health-rules` (asbestos and lead in school buildings).
- **Places:** `district Rochester` 346, `town Rochester` 57, no place 28, `district Tri-City Christian Academy` 6, `district Portsmouth Christian Academy` 1, `district St. Charles School` 1.
- **Places for the backend:** Rochester's one row (Wakefield's AREA agreement, `places.yaml`) matches what the agents found; nothing to change.
- **Draft facts:** two notes are flagged: the board's public comment policy, adopted April 9, 2026, cited from its draft, and a JROTC instructor nomination "pending cert".
- **Raw folders:** all under 100 MB.
- **Spot checks:** each agent checked 3 or more facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | The council's June 2, 2026 debt service exception "to restore the loss of 15 teaching positions," and the estimated $0.63 rate increase ($238 on a $378,000 home) | City news release, June 5, 2026 |
  | The FY2027 budget: $83,812,156 all funds, $78,016,601 general fund | FY2027 approved budget, p. 1 (the city's release says $83,812,489; the fact's note gives both) |
  | $1,350,655.24 left over from Salmon Falls, returned to the city | Board packet, May 14, 2026 |
  | Wakefield's tuition, $20,042.93 | Board minutes, December 11, 2025 |
  | Spaulding's diploma: 26 credits | Spaulding 2026-27 Program of Studies |
  | After-school care: $105 a week afternoons, $180 both | Rochester Child Care Center enrollment page |
  | Rochester Middle: 6 counselors, 776 students (2023-24) | Federal civil rights data (school support and enrollment files) |

## Facts first read through the vendor's host (checked in a browser)

Before it was told to stop, the getting-to-school agent read eight district pages from rochesterpublicschoolsnh.sites.thrillshare.com, which routes around rochesterschools.com's bot check. **In the browser pass (November 15, 2026) each page was opened at its rochesterschools.com address in Chrome, and every quoted fact matched:**

| Page checked | Facts in `getting-to-school-and-choices.md` | Result |
|---|---|---|
| https://www.rochesterschools.com/o/rsd/page/bus-information | district-transportation 1, 3, 4, 9 (and 2) | Matched word for word |
| https://www.rochesterschools.com/o/rsd/page/my-ride-k-12 | district-transportation 8 | Matched (the instructions are in the page's two collapsed "How to access" sections) |
| https://www.rochesterschools.com/article/3004433 | district-transportation 7, 8 | Matched, dated August 18, 2026 |
| https://www.rochesterschools.com/live-feed (pages 1–3) | district-transportation 5, 11, 12; district-school-day-and-calendar 6 | Text matched; the feed shows only relative dates, so fact 11 now says "September 2025" (not September 12) and fact 6 "late January 2026" (not January 26) |
| https://www.rochesterschools.com/o/rsd/page/elementary-placement | district-attendance-zones-and-transfers 1, 2, 3 | Matched |
| https://www.rochesterschools.com/o/rsd/page/policies (Section J) | district-attendance-zones-and-transfers 12 | Matched: no policy JF is posted. The district's own page links Section J to the vendor host's document list |
| https://www.rochesterschools.com/o/shs/page/incoming-freshmen-info | school-programs-after-grade-6 2 | Matched (the welcome letter is an image link) |

The browser copies replaced the raw files under the same names; the vendor copies are kept in `raw/daily/vendor-host/` as a record. The facts can load like any other.

## Browser pass, November 15, 2026: blocked pages read in Chrome

Pages rochesterschools.com and the city blocked to automated requests were opened in Chrome and the facts added (19 in all; Rochester now has 457 facts):
- **Middle school** (`middle-school.md`): the 2026-27 handbook, schedule (six 47-minute periods and a 100-minute Advisory & Lunch block, no study hall), after-school rules (clubs 2:30–3:30; everyone else out by 2:30), clubs (drama "TBA"), sports by season, and the 2026-27 counseling department (a counselor per grade, a restorative counselor, a social worker and a SAP counselor). P23.3 now has an answer; P30.1 is full.
- **Spaulding and Bud Carlson** (`high-school-and-creteau.md`): senior open campus and work co-op dismissal from the handbook; Bud Carlson's diploma, HiSET and extended-day (after-hours) classes and its schedule. P13.3's premise is now "partly right".
- **Student support** (`student-support-and-families.md`): counselors as each school's 504 coordinators, the 504 handbook (plans go to every staff member with responsibilities under them), and ESOL teachers as the contact for information in a family's language. The military families page returned 404.
- **Elementary** (`elementary-schools.md`): Gonic's Title 1 page (which now calls Gonic schoolwide, unlike NH DOE's 2024-25 list) and its handbook's volunteer fingerprinting and device rules.
- **City** (`money-buildings-and-staff.md`): the charter's Section 43-a text (CPI-based limit; two-thirds votes to override or to except capital and bond costs).

- **Contracts** (`money-buildings-and-staff.md` district-budget-and-cost 23–24): the district posts its teachers' (2025–2028) and paraeducators' (2026–2029) contracts on its own Collective Bargaining Agreements page; added the 2026-27 teacher salary schedule and paraeducator wage grid. The site's 2025-26 salary bands predate the teachers' contract; seven corrections from its 2025-26 schedule are in `district_teacher_salary_band_config.yaml` (uncommitted, not yet loaded).

Still not read: NH DES lead results (shared Airtable views, which didn't open); current crossing guard posts (only 2021 job postings on the city site); Bud Carlson's admission process and extended-day class times (not published); City Council minutes for the June 2, 2026 vote.

## Premises checked

| Question says | What the sources show |
|---|---|
| Salmon Falls has Pre-K (P1.1) | No: it opened September 2, 2025 for K–5; the district's preschool is REACH at East Rochester, which has a waiting list |
| East Rochester is a Title I school (P5.1) | Confirmed (schoolwide, 2024-25); Chamberlain Street too; Gonic runs a targeted program |
| Kindergarten may be half-day (P18.1) | Full-day, 8:30 to 3 (derived from the district's single K–5 hours) |
| School librarians cut (P26.1) | Partly: 3.0 full-time-equivalent positions in 2025-26, down from 4.4 in 2017-18; the FY2027 budget cuts library services 10.4% |
| The schools and the city library don't coordinate on summer reading (P26.3) | Wrong: they launch summer reading together every year |
| McClelland's class sizes against Manchester's (P27.2) | About the same |
| Middle school sports cut players (P6.3) | Yes: players are chosen by ability and tryout performance |
| "Everyone lumped together" in math (P4.2) | Not entirely: 51 eighth graders took Algebra I in 2023-24; none in grade 7; no gifted program |
| Free after-school clubs until 5:00 (P11.2) | Not confirmed: the middle school lets out at 2:15 and Rochester has no 21st Century site |
| District-issued laptops (P19.2) | Chromebooks, under a signed agreement |
| Short middle school lunches (P23.2) | Can't be checked; the bell schedule is on the blocked site |
| Arts budgets always under threat (P28.1) | No cut found; FY2027 activities spending rose 84.9% |
| Free instrument loans (P28.2) | Not at the middle school; Spaulding lends school-owned instruments |
| Counselors for a building that size (P30.1) | 6 for 776 students (about 129 each); no social worker reported |
| ROTC at Spaulding (P29.1) | Right: Air Force JROTC, with no military obligation |
| Trades at Creteau: auto, welding (P2.2, P8.2) | Automotive, HVACR, Precision Machining, millwork and drafting at Creteau; welding, electrical and building trades at Dover or Somersworth |
| Computer science or cybersecurity at Creteau (P19.1) | Computer Networking & Telecommunications only; no AP Computer Science; Spaulding reported no computer science classes in 2023-24 |
| Creteau's culinary program and ServSafe (P25.1) | Its program is Restaurant Management |
| Rochester pays for Great Bay courses (P10.3) | No source says so: families pay $150 per Early College course (help available) |
| Bud Carlson is "just a GED program" (P13.2) | Wrong: a 20-credit diploma, plus HiSET preparation |
| Night classes at Bud Carlson (P13.3) | None found; it allows attendance at different times for work or family |
| Graduation as a community event at Spaulding (P25.3) | Moved to UNH's Whittemore Center by a November 2025 board vote |
| Senior privileges and work release (P25.2) | Not found (the handbook is on the blocked site) |
| Monarch School of New England (P9.3) | Real: a state-approved special education day school in Rochester, ages 5–22, paid for by districts |
| A full-time nurse in every elementary school (P16.1) | True in 2023-24; mixed since, with resignations and two traveling nurses |
| The district "just" suspends students (P30.3) | The rate is high (12.6% against 4.9% statewide), and the district also reports other supports |
| A PTA at each school (P27.3) | Only Chamberlain Street's is confirmed |
| Help waits for state test scores (P20.3) | No source ties them together |
| Therapy waits of months (P9.2) | No wait-time data exists |
| Seacoast Charter as an alternative to Spaulding (P4.3) | It runs only through grade 8 |
| A late bus or backup ride (P5.3) | None; the COAST public bus ($2) is the only alternative |
| Downtown zoning (P7.1) | Downtown is split among four zones; Wakefield Street is Chamberlain Street's; the posted map still shows Maple Street Magnet, closed June 30, 2026 |
| "Annual homeschool evaluations" with SAU 54 (P12.2) | Out of date: repealed July 1, 2026; Rochester's policy IHBG still describes the old notice |
| Crossing guards at Chamberlain and Brock (P15.1) | Posts existed there in 2021; no current list was found |
| Remote snow days (P15.2) | Allowed by policy IMBA; none found in 2025-26; five June make-up days in 2026-27 |
| St. Charles School or Tri-City Christian (P24.2) | St. Charles is a K–8 special education program for students placed by public schools; Tri-City Christian is a Pre-K–12 Christian school in Somersworth |
| "A special exception to restore 15 teaching jobs" (P3.1) | Correct: the council used the charter's debt service exception on June 2, 2026 |
| "$83 million" on schools (P3.3) | Correct: $83.8 million all funds |
| "$36 million on Salmon Falls" after closing older schools years ago (P14.3) | About $32.5 million against $34 million approved, with $15.8 million from the state and $1.35 million returned; the older schools closed under the same plan |
| Wakefield's tuition covers the cost (P8.1) | $20,042.93 for 2026-27, excluding debt service, transportation and special education, plus a building rent |
| Cutting classroom teachers first (P8.3) | The superintendent's preferred March 2026 plan avoided classroom cuts |

## Corrections and additions to earlier files

- **Dover, `high-school-and-ctc.md` `cte-center-programs` 14 (note):** Dover's catalog lists Rochester's Precision Machining I for grades 10–11; the note now says Rochester's own 2026-27 catalog starts it in grade 11 and points to this town's file. Dover's catalog also names Rochester's restaurant the "Raider House Restaurant," while Spaulding's catalog names the "Our House Cafe"; no Dover fact states the name.

Nothing else in Rochester's files contradicts an earlier town.

## Coverage

32 questions are answered **fully** and 56 **partly**. Two have only a written gap: P22.3 (no employee child care or pre-K benefit was found) and P23.3 (the middle school's course list, which would show a study hall or organization class, is on the blocked site).

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Jenna | **full** | partial | **full** |
| P2 Derek | partial | **full** | **full** |
| P3 Linda | **full** | partial | **full** |
| P4 Marcus | partial | partial | partial |
| P5 Tammy | partial | **full** | partial |
| P6 Carlos | partial | partial | partial |
| P7 Heather | **full** | partial | **full** |
| P8 Ray | partial | **full** | **full** |
| P9 Brianna | partial | partial | partial |
| P10 Kevin | **full** | **full** | **full** |
| P11 Diane | partial | partial | partial |
| P12 Nadia | **full** | **full** | **full** |
| P13 Tyler | partial | **full** | partial |
| P14 Susan | **full** | **full** | **full** |
| P15 Omar | partial | **full** | partial |
| P16 Megan | partial | **full** | partial |
| P17 Greg | partial | **full** | partial |
| P18 Alyssa | partial | partial | **full** |
| P19 Trevor | **full** | partial | partial |
| P20 Vanessa | partial | partial | partial |
| P21 Pat | partial | partial | partial |
| P22 Chloe | partial | partial | gap |
| P23 Dan | partial | partial | gap |
| P24 Kirsten | **full** | **full** | partial |
| P25 Ben | **full** | partial | **full** |
| P26 Miriam | partial | partial | **full** |
| P27 Jalen | partial | partial | partial |
| P28 Rachel | partial | partial | partial |
| P29 Scott | **full** | partial | partial |
| P30 Paula | partial | partial | partial |

## Notable findings

- **The tax cap:** the council used the charter's debt service exception to restore 15 teaching positions; the school tax rose 8.2% mostly because state aid was budgeted $2.44 million lower, and aid then came in $1.3 million above budget.
- **Special education:** outside placements more than double in the FY2027 budget ($2.74 million to $5.68 million); the state's spring 2026 review found the district compliant but weak on outcomes for students with IEPs.
- **Suspensions:** 12.6% of students had an out-of-school suspension in 2023-24, against 4.9% statewide; 23.2% of students with IEPs.
- **Reading:** grades 3–5 reading rose 13–17 points from 2022 to 2026, against 4–6 statewide; math barely moved.
- **Creteau:** no welding, culinary, electrical or computer science program; those trades are at Dover or Somersworth through Tri-City.

## Gaps to retry

- **Blocked to automated requests (for the browser pass):** all of rochesterschools.com (school pages, handbooks, the middle school's schedule, courses, clubs and sports, Creteau's program pages, Bud Carlson's page, the policy index and the 504, foster care, ESL and military family pages), rochesternh.gov (crossing guards, council minutes, the planning pipeline), the city charter on ecode360, Wakefield's school and town sites, the state labor board's contract library (PELRB) and NH DES lead test results. Each file's "Not retrieved" section lists the URLs.
- **Not found anywhere:** therapy and counseling wait times, a chronic absenteeism rate for Rochester, how many Rochester students attend charter or private schools, current pay scales, any document on Rochester Middle School's repairs, CTE seat and waitlist counts, NH DOE's Title I lists for 2025-26 and later.
