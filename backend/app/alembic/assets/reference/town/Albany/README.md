# Albany: Research for Ask NH Education Facts

Cited facts and figures for answering Albany, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the reference library's format (`../../additional-data/README.md`) and uses the shared topics in `../shared-topics.md`. It isn't loaded into the Ask yet; see `../recommended-improvements.md`.

Gathered November 13, 2026. Albany is an SAU 9 town that runs no schools and sends every grade to Conway (Pine Tree Primary, Conway Intermediate, Kennett Middle and Kennett High). Conway and Kennett were researched first, so the four agents matched each question to existing facts and researched what was missing or specific to Albany.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `programs-and-outcomes.md` | The contracts' reporting clauses and the missing reports, why Albany students can't be separated in results, the career center (no heavy equipment), work rules for teens, CTE seats, Kennett's diversity and SRO, parent rights and opt-outs (Conway's policies apply) | 15 | 84 | 2 | `raw/programs/` |
| `getting-to-school-and-the-day.md` | Albany's own bus contractor, no stop on the upper Kancamagus, derived ride times, Title I, free and reduced-price meals (about 53% of resident students, derived), no public preschool, kindergarten day, storm days, McKinney-Vento | 10 | 46 | 1 | `raw/daily/` |
| `money-and-governance.md` | All five Albany–Conway contracts (K–6 to 2034; new 7–8 and 9–12 for 2027–2032), the 2025 tax jump, the hold harmless phase-out and why Albany gets no extraordinary need aid, the 0% open enrollment vote, special education responsibility, SAU 9 share, the veterans' credit, board seats and vacancies | 14 | 107 | 2 | `raw/money/` |
| `community-and-families.md` | Census and enrollment trend, Carroll County and sale-price comparisons, child care costs, homeschool access, Conway Recreation camp, the Lora Johnson Pierce Scholarship, therapy for ages 3–4, food help, fire and EMS from Conway | 10 | 79 | 11 | `raw/community/` |
| **Total** | | **49** | **316** | **16** | **155 MB** |

`brief.md` is the brief the research agents worked from. Four agents ran in parallel and used about 2.2 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser with `sau` places accepted.
- **Topics:** every topic matches `../shared-topics.md`, after the proposals below were reviewed and added.
- **Places:** `district Albany` 135, `district Conway` 69, `town Albany` 53, `sau 9` 13, `town Conway` 7, `town Berlin` 1 (White Mountains Community College).
- **Adequacy aid update (November 14, 2026):** the site's database now holds NH DOE's adequacy aid calculation for FY2020–FY2027. Three facts and two tables that only restated it (aid by component, and the free or reduced-price share of resident pupils) were removed. Three facts were cut to the parts the database doesn't have: enrollment from the annual reports, value per free or reduced-price meal pupil, and how EFA students affect the count. The DOE figures kept were checked against the database and match.
- **Tax rates update (November 15, 2026):** the site's database now holds NH DRA's tax rates by town (tax years 2014–2025) and NH DOE's school taxes by town (2011–2025). Two facts and one table that only restated them were removed: the 2025 rates and school share, and a tax on a sample home. One fact was cut to the town's explanation of the 2025 tax jump after the revaluation. The district's revenue figures, the SAU 9 share of the rate and the veterans' credits were kept; their DRA and DOE figures match the database.
- **Spot checks:** each agent checked 3 to 5 quotes against its raw copies. These were checked again independently, and all matched:

  | Fact | Checked against |
  |---|---|
  | The K–6 contract: eight school years from July 1, 2026, notice before the third year ends, and "the final decision shall be up to Conway" on in-district programs | Contract page image |
  | The 2027 contracts: "No Albany student will be denied enrollment" | Contract text |
  | The 2025 school appropriation of $1,149,589 | DRA tax rate setting sheet |
  | The Lora Johnson Pierce Scholarship for Albany residents | Kennett scholarship list |

## Premises checked

| Question says | What the sources show |
|---|---|
| A choice between "Pine Tree Elementary or Conway Elementary" (P1.1) | Out of date: Conway's schools are grouped by grade (K–2, 3–5), so the grade decides the school; one Albany bus serves both |
| Albany's "high poverty rate" (P1.3) | Partly supported: about 53% of resident students qualify for free or reduced-price meals (derived, against 25% statewide), but the Census Bureau's school district poverty estimate fell for 2024, and the ACS estimates in the site's Census data have wide margins |
| A bus ride from the upper Kancamagus to Kennett Middle (P3.1) | No route reaches that area; Albany's Route 16 run takes 39–60 minutes (derived) |
| "Remote learning days" in storms (P3.3) | Allowed by policy, but none was found in use |
| Outdoor or forestry electives at Kennett Middle (P3.2) | None |
| A gifted program at Kennett Middle (P4.2) | None; accelerated math only |
| Heavy equipment at the career center (P6.1) | No such program; welding is within Advanced Manufacturing. Federal rules bar under-18s from most heavy equipment |
| Priority for Conway residents in career-center seats (P6.3) | None found; seats go by prerequisite and grade, and the contracts promise equal access |
| "5- and 8-year" contracts and an "8-year K–6" contract (P8.2, P20.2) | Correct: K–6 runs from July 2026 to at least June 2034; the new 7–8 and 9–12 contracts run five years from 2027 |
| An Albany "RSA 194-D open-enrollment policy" (P11.2) | Not a board policy: a March 2026 warrant article setting 0% outside Conway |
| Tuition "true-up" bills (P11.3) | Adjustments are folded into the next year's bill under the current contracts; the 2027 contracts have none |
| Hold harmless phase-out and equalized value per free or reduced-price pupil (P11.1) | Current law; Albany has received no extraordinary need aid since FY2026, and its hold harmless grant falls about $50,254 a step from FY2028 (derived) |
| A Conway renovation bond (P2.2) | None proposed; the 2027 contracts replace bond shares with a five-year capital plan |
| No Fryeburg Academy contract (P15.1) | Correct; the "Albany" on Fryeburg's page is Albany, Maine |
| A three-person board (P20.3) | Correct |
| The annual homeschool notice (P7.3) | No longer required since July 1, 2026 |
| School-age population "steady" while median age rises (P20.1) | Median age rose (45.6 to 50.7); Albany's student count fell from 96 to 58 (2019 to 2026) |

## Corrections and additions to earlier files

Each was checked against the raw copy before it was made:
- **Conway, `district-transportation` 2 (note):** Albany pays for its own transport; Eldridge's contract runs to 2031, and Conway's buses pick up the Passaconaway Road students.
- **Conway, `district-curriculum-and-assessment` 1 (note, schools file):** NH DOE's list confirms both elementary schools are schoolwide Title I and the Kennett schools aren't Title I.
- **Conway, `district-tuition-contracts` 2 (note):** Albany's posted K–6 contract is the 2026–2034 one, with its own formula.
- **Conway, `town-family-help` 1 (note):** the weekend food program's own page still lists closed schools.
- **Jackson, community "Not retrieved":** Conway's day camp is limited to Conway and Albany residents.

Noted but not changed: the Conway file counts 59 Albany students in March 2026 and Albany's page counts 58 in February; the career center's forklift is described differently in two sources; Kennett's Program of Studies says college classes open in sophomore year while policy IGBK says juniors and seniors.

## Topics added to the shared list

Reviewed with the other towns' proposals on November 13, 2026 and added to `../shared-topics.md`: `homeless-student-school-stability`, `dyslexia-screening-and-intervention` (Albany's `early-reading-screening` merged with Tamworth's), `cte-admission-and-cost-rules` (merged with Madison's `cte-center-access-rules`), `youth-employment-rules`, `district-parent-rights-and-materials`, `property-tax-relief` (Albany's `property-tax-credits-and-exemptions` merged with Hart's Location's) and `special-education-advocacy-help` (renamed from `disability-rights-center-nh`, so the topic isn't about one organization). `school-volunteer-background-checks` wasn't used as a topic; volunteer checks sit under `district-volunteers-and-partners`.

## Coverage

34 questions are answered **fully** and 26 **partly**; none has nothing. P12.2 (mental health at Kennett) wasn't assigned to an agent by mistake; Kennett's counseling and student assistance program are already in `../sau9/kennett-pathways.md` (`district-student-support`), which doesn't confirm staffing, so it counts as partial.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Hotel supervisor | **full** (grade decides school) | partial (Project SUCCEED opens 7:30) | **full** (one application; Title I schools) |
| P2 Retired carpenter | **full** (budget drivers) | **full** (bond shares and the capital plan) | **full** (79% tuition, 2.1% SAU 9, derived) |
| P3 Forest technician | partial (no Kanc route; Route 16 times) | partial (no such elective) | **full** (closings, delays, remote-day policy) |
| P4 Software engineer | partial (Albany students can't be separated) | **full** (accelerated math; no gifted program) | **full** (contracts require reports; none found) |
| P5 Grandparent with an IEP | **full** (Albany responsible) | **full** (Albany pays, including transport) | **full** (who advocates) |
| P6 Excavation contractor | partial (no heavy equipment) | partial (co-ops and ELOs; labor rules) | **full** (equal access) |
| P7 Homeschooling parent | **full** (EFA students and adequacy) | partial (no written answer for Albany residents) | **full** (no notice since July 2026) |
| P8 Young couple | **full** (no public preschool) | **full** (no student denied) | **full** (reports, meetings, SAU vote) |
| P9 Ski area worker | **full** (full-day K; bus times) | partial (Conway camp; fees not posted) | partial (no fee schedule posted) |
| P10 Line cook | partial (earlier files; no Spanish materials found) | **full** (Kennett 90.8% White, derived; policies) | partial (interpreters; no named liaison) |
| P11 Selectboard member | **full** (hold harmless steps, derived) | **full** (the 0% vote) | partial (no record of past adjustment sizes) |
| P12 Nurse | **full** (AP, Running Start) | partial (earlier files; staffing not confirmed) | partial (side by side from different years) |
| P13 Retired HR director | partial (state shares; library) | **full** (per-pupil tuition, derived) | partial (volunteer steps; mentoring roles) |
| P14 Recent graduate | **full** (Lora Johnson Pierce) | partial (persistence; no WMCC data) | partial (transcripts; no alumni counseling) |
| P15 Parent seeking alternatives | **full** (families pay; hardship exceptions) | **full** (0% outside Conway) | **full** (Alternative Program) |
| P16 Disabled veteran | partial (credit rules; Albany's amount not found) | partial (counselor; no military-family program) | **full** (SRO, drills, plans) |
| P17 Early childhood teacher | partial (dyslexia screening; alignment not documented) | partial (Child Find from 2.5) | partial (para shortages; no turnover rate) |
| P18 Homestead farmer | **full** (Conway's policies) | **full** (statutes and policies) | **full** (SAU share by property value; leaving) |
| P19 Hospitality couple | **full** (school of origin) | partial (no timeline) | partial (liaison; no Albany pantry) |
| P20 Board observer | **full** (enrollment and the rate) | **full** (term to 2034; closure rules) | partial (record and powers; reasons not stated) |

## Notable findings

- **No reports reach Albany's board:** all five Conway contracts require reports on Albany students, quarterly under the current ones, and none appears in Albany's minutes, packets or reports from 2019 to November 2026.
- **Albany's local school tax nearly doubled in 2025,** from $582,846 to $1,149,589: the budget rose $420,185 and adequacy aid fell $194,440.
- **The 2027 contracts change the formula:** no annual true-up and no property-value share; instead a share of Conway's five-year repair plan ($4.5 million for the middle school, $3.8 million for the high school).
- **Board seats are hard to fill:** members were elected with 2 votes each in 2025 and one-vote write-ins in 2026; openings in 2021 and 2024 drew no applicants.
- **Albany has no police or fire department:** Conway Fire answered 176 Albany calls in 2025, and the contract is being renegotiated.

## Gaps to retry

- The sizes of past tuition adjustments.
- Albany's adopted veterans' credit (DRA blocked automated access).
- Conway Recreation camp fees, posted in spring.
- Cell coverage along the Kancamagus and NHDOT's winter standards for Route 112.
- The 2026 town meeting results.
