# Manchester: Research for Ask NH Education Facts

Cited facts and figures for answering Manchester, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 40 resident profiles with 3 questions each, numbered P1.1 to P40.3 in `questions.md`; the people are invented. The research is in the nine files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026. Manchester is the first city researched and the largest district in the state: SAU 37, with 14 elementary schools (K–4), four middle schools (5–8), Central, Memorial and West high schools and the Manchester School of Technology, plus six charter schools in the city. Nashua and Concord were researched at the same time.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | Spanish and French dual language (citywide, through grade 6), Title I and special education preschool, kindergarten, class-size targets, one recess a day, LETRS reading training, the gifted coordinator role, allergy and recess rules | 10 | 43 | 0 | `raw/elementary/` (21 MB) |
| `middle-and-high-schools.md` | Pre-Algebra and Algebra 1 credit in middle school, three course levels in high school, Memorial's counselors and school profile, the districtwide phone ban (Students 166), substitutes, AP lists, West's STEAM program | 10 | 68 | 0 | `raw/secondary/` (18 MB) |
| `mst-and-pathways.md` | MST High School (grade 9 entry, 1–4 grading) and the one-block CTE program from the other high schools, full programs and the essay, RSA 188-E:5 for Manchester, credentials, apprenticeships, local wages, the adult diploma program and HiSET | 9 | 64 | 3 | `raw/pathways/` (5.6 MB) |
| `student-support.md` | Grade 5 in middle school, para, counselor and psychologist positions by school (February 2026 roster), FY2026 cuts, interpreter and translation rules, newcomer programs, foster care contacts, evaluation and placement rules | 6 | 76 | 3 | `raw/support/` (54 MB) |
| `getting-to-school-and-the-day.md` | The 1.4-mile walk radius and exception rules, staggered start times, bus routes for private and charter students, after-school programs and prices, meal debt, the Hallsville and Wilson closings | 6 | 41 | 0 | `raw/daily/` (57 MB) |
| `enrollment-and-choices.md` | The city's school zone map and feeder paths, Goffstown tuition and open enrollment, private school tuition and EFAs, private and home school shares by neighborhood (Census), custody and residency | 4 | 42 | 2 | `raw/choices/` (13 MB) |
| `charter-schools.md` | Mill Falls (family lottery numbers, sibling and carried-over waitlists), Polaris, Kreiva (first come, first served, 470 Pine Street) and Founders (lottery, no sports), charter buses, special education at charters, testing and graduation rules | 11 | 84 | 0 | `raw/charters/` (28 MB) |
| `money-and-governance.md` | The FY2027 budget and the aldermen's tax cap override votes, the charter tax cap, the cuts actually made, spending per pupil compared, para and teacher pay, enrollment since 2005-06, building ages, the ConVal case, Question 2 in a city | 7 | 81 | 6 | `raw/money/` (26 MB) |
| `results-and-community.md` | Proficiency and growth by school against low-income shares, state designations, staff experience by school, chronic absence, rating sites, volunteering and mentoring partners | 8 | 49 | 4 | `raw/results/` (7.3 MB) |
| **Total** | | **71** | **548** | **18** | **230 MB** |

`brief.md` is the brief the research agents worked from. Nine agents (twice the usual question count) used about 3.8 million tokens.

## Checks

- **Parser:** all nine files pass the backend's parser (`tools/check_town.sh Manchester`). Every table is linked to a topic.
- **Topics:** ten new topics were reviewed and added to `../shared-topics.md`: `district-attendance-zones-and-transfers`, `district-school-results-compared`, `local-occupation-wages` (given generic titles; the agents' titles named Manchester), `adult-diploma-and-equivalency-rules`, `career-readiness-and-cte-credit-rules`, `recess-activity-and-homework-rules`, `school-allergy-rules`, `school-rating-sites`, `research-family-income-and-test-scores` and `research-schools-and-home-values`.
- **Places:** `district Manchester` 359, no place 51, `town Manchester` 51, Mill Falls 22, Polaris 17, Kreiva 16, Founders 15, `district Diocese of Manchester` 10, `district Goffstown` 4, `district The Derryfield School` 2, `district Hooksett` 1.
- **Pending facts:** none of the notes say "draft" or "pending".
- **Raw folders:** all under 100 MB.
- **Spot checks:** each agent checked 3 to 8 facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | The aldermen's 10–4 vote setting the FY2027 school appropriation at $238,492,749 | BMA minutes and the district's budget memo |
  | The phone policy's exceptions noted in Aspen (Students 166) | 2026-27 middle school handbook |
  | Bus eligibility at 1.4 miles or more | District transportation guide |
  | Mill Falls' one Family Lottery Number per family | Mill Falls enrollment page |
  | Hallsville's and Wilson's closings | District FY2027 budget memo |
  | No yearly home education evaluation since July 1, 2026 | Library `home-education-rules` 1, 2, 10 |

## Premises checked

| Question says | What the sources show |
|---|---|
| A child at Hallsville School (P4, P33) | Closed in 2021–22; its neighborhood is now mostly in Jewett's zone |
| A 5th grader at Wilson (P22, P23) | Henry Wilson Elementary closed in summer 2024 |
| 5th graders at Highland-Goffe's Falls, Smyth Road or Wilson, or moving to Southside "next year" (P6, P16, P22, P29) | Wrong: since 2024-25 grade 5 is in the four grade 5–8 middle schools |
| French dual language at Weston "through fifth grade" (P5.1) | Started fall 2025 with ten kindergartners; planned through grade 6 |
| Dual language in middle school (P1.2) | The program runs through grade 6, so grades 5–6 are in middle school; the host school isn't stated |
| Recess "twice a day" (P17.2) | The teachers' contract builds the day around one 30-minute recess |
| Early-release Wednesdays (P40.2) | None found |
| Free full-day pre-K for 4-year-olds (P11.2) | None: Title I preschool runs half-day classes in ten school neighborhoods; special education preschool serves ages 3–5 |
| "Each school has its own" phone rule (P24.2) | Wrong: Policy Students 166 bans phones in every school from first bell to dismissal |
| West's STEAM program (P9.1) | Opened in 2014 (STEAM Ahead NH); no current page confirms it still runs |
| MST's 1-to-4 grading (P12.1) | Correct for MST High School |
| MST full-time or "bussed over for shop" (P12.2) | Both exist: full-time MST High School from grade 9, or one 95–100 minute CTE block a day from Central, Memorial or West from grade 10 |
| MST night classes for adults (P35.1) | Not confirmed; the city's adult diploma program is at 340 Granite Street |
| Dual enrollment through Saint Anselm (P16.2) | None found; Saint Anselm's 2026 partnership covers college access, not credit |
| Staggered start times (P16.3) | Correct: middle schools 7:25, high schools 7:38, elementary 8:20 |
| The city drops private and charter bus routes (P27.1) | Partly: the district, not the city, runs the buses; it suspended charter routes in 2023 when a contractor ran short of drivers, and has run its own buses since 2024-25 |
| Free breakfast and lunch for everyone (P4.2) | Not districtwide; unpaid meal debt was expected to reach $400,000 |
| Interpreters need weeks' notice (P7.2) | Wrong: the staff guide allows 48 hours for an interpreter and 5 business days to translate IEPs and evaluations over 5 pages |
| Paras cut under the tax cap (P6.3) | Not in FY2026; the FY2027 para line rose to $8.4 million |
| Kreiva on Pine Street (P31.1) | Correct: 470 Pine Street |
| Kreiva has no school bus (P31.3) | Manchester-resident charter students ride the district's charter routes |
| Polaris "on the West Side" (P10.3) | Address confirmed; no source names the neighborhood |
| Twins in the Mill Falls lottery (P8.1) | One family lottery number draws all of a family's children; each is admitted only if its grade has a seat |
| Paying tuition to attend Goffstown (P11.1) | Allowed, with Goffstown board approval and no bus |
| Mast Road is in Northwest's zone (P11) | Mostly in Parker-Varney's zone |
| Manchester spends "thousands less" than Bedford or Goffstown (P14.1) | Partly wrong: $1,630 less than Bedford and $209 more than Goffstown; $4,679 below the state average (FY2025) |
| Enrollment "thousands of kids lower than 20 years ago" (P32.1) | Correct: 17,511 in 2005-06, 11,980 in 2023-24 |
| "The $250-million-plus school budget" (P32.2) | The adopted FY2027 appropriation is $238,492,749; $251.4 million was the district's baseline request |
| "$16 million in budget cuts" (P34.3) | Out of date: the final budget was $12.9 million below baseline, mostly covered by borrowing and a trust fund; about $2.78 million was cut (41 vacant positions) |
| "If the district sues the state" (P36.1) | Manchester was already a ConVal plaintiff; that case took more than six years and ordered no payment |
| The new law on administrator pay and tax caps (P36.3) | Question 2 got 59.9% yes in Manchester (unofficial), short of 60%, so neither cap applies; the central office budget vote applies only where there's an annual meeting |
| Gossler Park's low scores (P10.1) | True for proficiency (18–19%), but its math growth was typical and its 2025 growth rating was Level 3 of 4 |
| Parker-Varney's staff turnover (P13.2) | Its share of experienced educators fell to 57% in 2024-25, the lowest of the 20 schools; no turnover figures are published |
| Chronic absenteeism at Central and West (P23.1) | Not checkable by school: New Hampshire publishes no chronic absence rates; the district reported 37% for its high schools together (news) |
| Long-term substitutes at Central (P26.1) | Unconfirmed; state rule limits an uncredentialed substitute to 20 consecutive days in one position |
| Mount St. Mary for a future child (P21.3) | K–6 only; $7,900 for 2026-27 |
| A yearly homeschool evaluation (P28.2) | Repealed July 1, 2026 |

## Corrections and additions to earlier files

- **Madison, `cte-admission-and-cost-rules` 2 (note):** its quote of RSA 188-E:5, V left out, at an ellipsis, the exception for Manchester's own students; the note now says so and points here.

Nothing in Manchester's files contradicts an earlier town. The library notes below are for the library's owner; town research doesn't edit `additional-data/`.

## Coverage

36 questions are answered **fully** and 84 **partly**; none has nothing. Most partial answers are partial because the district's website was unreadable (see "Gaps to retry").

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Elena Morales | partial | partial | partial |
| P2 Dan Kowalski | partial | **full** | partial |
| P3 Priya Nair | partial | partial | partial |
| P4 Marcus Vance | partial | partial | partial |
| P5 Claire Moreau | partial | partial | partial |
| P6 Trevor Higgins | partial | partial | partial |
| P7 Amina Hassan | **full** | **full** | partial |
| P8 Greg & Heather Sato | **full** | **full** | partial |
| P9 Lucie Gagnon | partial | partial | **full** |
| P10 Mateo Silva | partial | partial | **full** |
| P11 Brittany Ouellette | **full** | partial | partial |
| P12 Devon Brooks | partial | **full** | partial |
| P13 Nadia Al-Mansoor | partial | partial | partial |
| P14 Kevin & Alyssa Pelletier | **full** | **full** | partial |
| P15 Samantha Nguyen | partial | partial | partial |
| P16 Carlos Rivera | **full** | partial | **full** |
| P17 Hannah Lindqvist | partial | partial | partial |
| P18 Tanya Washington | partial | partial | partial |
| P19 Omar Farah | **full** | partial | partial |
| P20 Rachel & Ben Cohen | partial | partial | **full** |
| P21 Jared Morales | **full** | **full** | partial |
| P22 Sofia Delgado | partial | partial | partial |
| P23 Rev. Paul Mensah | partial | partial | **full** |
| P24 Maya Patel | partial | **full** | **full** |
| P25 Liam O'Connor | **full** | partial | partial |
| P26 Derrick & Simone Baptiste | partial | partial | partial |
| P27 Megan & Chris Kowalczyk | **full** | **full** | partial |
| P28 Amber Desrosiers | partial | **full** | partial |
| P29 Dr. Victor Okafor | **full** | partial | partial |
| P30 Jenna Thibodeau | **full** | partial | partial |
| P31 Toby & Nina Morales | partial | **full** | partial |
| P32 Arthur "Artie" Beaulieu | **full** | **full** | partial |
| P33 Diane Mercer | partial | partial | partial |
| P34 Carlos & Maria Mendez | partial | **full** | partial |
| P35 Jordan Alvarez | partial | partial | **full** |
| P36 Eleanor Vance-Kerr | **full** | **full** | **full** |
| P37 Bradford "Brad" Cole | partial | partial | **full** |
| P38 Kendra & Malik Dorsey | partial | **full** | partial |
| P39 Thomas "Tom" Kelleher | partial | partial | partial |
| P40 Soraia Fernandes | partial | partial | partial |

## Notable findings

- **Scores follow income; growth mostly doesn't.** Across the 12 elementary schools, the share of low-income students tracks 2026 reading proficiency closely (correlation −0.91) but growth only weakly (−0.34). Smyth Road has among the highest scores and the lowest reading growth; Parker-Varney and Webster the highest growth.
- **The gap holds within income groups:** Manchester's low-income students were 13% proficient in math against 24% for low-income students statewide; its other students 27% against 50%.
- **The FY2027 budget:** the aldermen's tax cap override failed 9–5 on June 2, 2026 and passed 11–3 on June 9, setting the school appropriation at $238,492,749. Actual cuts were about $2.78 million, all in vacant positions.
- **MST is two programs:** a full-time high school entered in grade 9, and a one-block-a-day CTE program for the other high schools from grade 10. Five programs were full for 2026-27, and state law (RSA 188-E:5, V) requires the district to enroll and pay for its residents when there is space.
- **Interpreters:** 48 hours' notice, a phone line parents can call themselves, and no use of children or relatives as interpreters. No district liaison speaks Somali or Maay.

## Site data and Ask issues found

- `school_enrollment` has no rows for Hallsville or Henry Wilson schools, so the site's district totals for years before they closed leave them out (the brief's 13,526 for 2015-16 is low).
- `district_class_size` has no rows for any Manchester middle school.
- The site stores test score growth by school, but the Ask can't fetch it; the results file puts it in two tables.

These are in `../recommended-improvements.md`.

## Library notes (not changed here)

- `charter-schools`: Mill Falls' and Polaris's admission policies cite a 10% limit on a town's pupils per grade; current RSA 194-B:9, I(c)(3) has only a district's "published maximum percentage".
- `efa-eligibility-and-cap` 5: the cap rises to 15,625 for 2027-28.
- `budget-question-2-2026-results` 3: Manchester's figures are still WMUR's unofficial tally; the City Clerk posts the ward return forms.
- `refugee-immigrant-family-support` 1: IINE's Manchester office is given as 470 Pine Street; NH Adult Education lists its adult English program at 2013 Elm Street.
- `raw/programs/cte-centers.csv`, MST row: reflects spring 2026; the 2026-27 forms list Kreiva and Mount Zion as sending schools.
- `chronic-absenteeism-nh-data`: Attendance Works' June 2026 report confirms New Hampshire still publishes no chronic absence data.
- A 2025 NH Supreme Court ruling in a Pittsfield case (NHPR, May 29, 2026) on what a home district pays an open enrollment district may belong in the library's open enrollment facts.
- SB 517 (2026), on extending free meals to 200% of poverty, passed the Senate; whether it became law wasn't checked.

## Browser pass, November 15, 2026

mansd.org opens in Chrome. The district renumbered its policies on November 24, 2025 (104.1 is now 508, 106 is 511, 115 is 717, 162 is 562, 126 is 730, 155 is 557, 111 is 713), which is partly why they couldn't be found. Added 12 facts: the dual language entry rules and fine arts offerings, policy 713 (no gifted program) and the homework policy (`elementary-schools.md`), the food allergy protocol (a new `district-meals` section there), policies 508, 717 and 562 on changing schools, grade placement and access for home-educated, EFA, charter and private students (`enrollment-and-choices.md`), the board's 2026–2028 public forum rules, and the MEA and AFSCME agreements' course reimbursement and para wages (`money-and-governance.md`). Manchester now has 559 facts. Skipped as agreed: course catalogs, club lists, MST and adult education pages, the January 2026 special education presentation and the Manchester Ink Link articles.

## Gaps to retry

Every page on mansd.org and its school subdomains returned a bot check on November 15, 2026, and Manchester Ink Link, education.nh.gov and the state labor board's contracts returned HTTP 403. Opening these in a browser would fill most of the partial answers:
- **mansd.org (about 37 pages):** policies on changing schools (104.1), non-resident students (106), grade placement (115), transportation, homework, devices and allergies; course catalogs and AP lists; club lists; the dual language and gifted pages; the elementary fine arts page; board minutes and the January 2026 special education presentation; the school board's public comment rules; MST's program and adult education pages.
- **Manchester Ink Link (10 articles)** and **education.nh.gov (6 pages),** including special education evaluation timeliness reports and the 2025 school designation list.
- **The state labor board:** the current teachers' and paraprofessionals' contracts.
- Not found anywhere: dual language seat allocation; Jewett's kindergarten aides; a list of daycare bus stops; which schools serve free meals to all; crossing guard posts near Parkside; Kreiva students' city bus fares; Trinity's tuition; Goffstown's tuition rate; Gossler Park's reading coaches.

The shared web search limit ran out near the end of several agents' work.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 21 saved bus and transportation copies (23 in all; schools, child care centers, businesses and other public places keep theirs).
