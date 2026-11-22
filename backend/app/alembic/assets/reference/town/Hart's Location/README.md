# Hart's Location: Research for Ask NH Education Facts

Cited facts and figures for answering Hart's Location, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the reference library's format (`../../additional-data/README.md`) and uses the shared topics in `../shared-topics.md`. It isn't loaded into the Ask yet; see `../recommended-improvements.md`.

Gathered November 13, 2026. Hart's Location is the fifth SAU 9 town and one of New Hampshire's smallest (68 residents in 2020). Its K–8 students attend Josiah Bartlett Elementary under a contract, which the Bartlett research covered, and Kennett is covered in `../sau9/`. So the three agents first matched each question to existing facts and researched only what was missing or specific to Hart's Location.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `schools-and-getting-there.md` | Getting a Hart's Location child to JBES (no bus stop; mileage), the grade 7–8 premise, the JBES ski program, Kennett's resource officer and rankings, substitutes and volunteers, busing between two homes, derived road distances | 11 | 50 | 1 | `raw/schools/` |
| `money-and-governance.md` | The 2010 K–8 contract (renews yearly, three school years' notice), high school with no contract, the tax effect of a new pupil (derived), why the school rate swings and the 2025 revaluation, SAU 9 share and votes, PILT and national forest receipts, the statewide education tax Hart's Location keeps, reserves, residency and custody, board seats and vacancies, the board's new schedule | 15 | 92 | 4 | `raw/money/` |
| `community-and-families.md` | 2010 and 2020 Census counts, voters and midnight voting, land in the national forest and state park (derived), housing and lot rules, child care distances, early intervention, home education after July 2026, cell coverage, Route 302 closures, emergency services | 8 | 76 | 7 | `raw/community/` |
| **Total** | | **34** | **218** | **12** | **86 MB** |

`brief.md` is the brief the research agents worked from. Three agents ran in parallel and used about 1.45 million tokens.

## Checks

- **Parser:** all three files pass the backend's parser with `sau` places accepted.
- **Topics:** every topic matches `../shared-topics.md`, after the proposals below were reviewed and added.
- **Places:**

  | Place | Facts |
  |---|---|
  | `district Hart's Location` | 88 |
  | `town Hart's Location` | 74 |
  | `district Bartlett` | 15 |
  | `district Conway` | 12 |
  | `sau 9` | 5 |

- **Adequacy aid update (November 14, 2026):** the site's database now holds NH DOE's adequacy aid calculation for FY2020–FY2027. Two facts that only restated it were removed, and the resident pupil column was cut from `harts_location_school_budget`. The DOE figures kept (the statewide tax, the rates and the pupil counts) were checked against the database and match.
- **Tax rates update (November 15, 2026):** the site's database now holds NH DRA's tax rates by town (tax years 2014–2025) and NH DOE's school taxes by town (2011–2025). Three facts and one table that only restated them were removed: the 2025 tax bill split, DRA's statewide full value rank, the most state relief at the 2025 rate (worked out from the rates), and the table of DRA's rates by year. One fact was cut to why the local school rate swings. The revaluation, the tax effect of a new pupil and the statewide tax Hart's Location keeps were kept; their figures match the database.
- **Spot checks:** each agent checked 3 to 8 quotes against its raw copies. These were checked again independently, and all matched:

  | Fact | Checked against |
  |---|---|
  | PILT of $14,886 (FY2025) and $15,277 (FY2026) paid to the town | Town reports and the federal PILT data |
  | National forest receipts of $5,579.72 to the school district in FY2025 | The site's DOE-25 revenue rows (account 4810) |
  | The contract's year-to-year renewal and notice clause | Contract text |
  | 68 residents in 2020 | Census API |
  | Kennett's resource officer line ($78,505) | Conway's FY2026 budget page; matches the Albany research's four-school total of $86,605 |

## Premises checked

| Question says | What the sources show |
|---|---|
| SAU 9 buses through Crawford Notch (P1.2) | No route stops in Hart's Location; the contract makes the town's district responsible for transport. It spent $0 on transport in 2024-25; how its one JBES student traveled isn't recorded |
| Grades 7–8 at JBES or Kennett Middle (P5.1) | JBES: the contract covers K–8 (SAU 9's page files it under K–6). There is no 7–8 contract with Conway |
| High schoolers go to Kennett; "locked into Kennett" (P8.1, P14.2) | No high school contract. Kennett was named the "school of record" in 2016, but the 2026-27 budget pays $21,650 tuition and mileage for one Fryeburg Academy student |
| The board meets at 8:00 a.m. in Bartlett (P2.2) | Correct (at JBES since at least 2009). In April 2026 it moved from every other Tuesday to quarterly Wednesdays at 8 a.m.; SAU 9's page still shows the old schedule |
| Three board seats (P9.3) | Correct (the default under RSA 671:4) |
| A "Thursday afternoon Ski & Ride" (P11.2) | Partly: in 2024-25 grades 1–6 skied with the Eastern Slope Ski Club on Thursdays after lunch; snowboarding only in grades 5–6. No 2026-27 day or fee is published |
| A 2027–28 renegotiation (P9.1, P20.3) | Not for Hart's Location: its contract renews itself yearly. The 2027 contracts are other towns' |
| PILT offsets the school budget (P19.1) | PILT goes to the town as general revenue; the school district gets national forest receipts by law (RSA 227-H:22) |
| "SAU #9 Joint Board" weighted votes (P10.1) | One vote under RSA 194-C:7; weighted votes, used only on demand, would be 0 (derived: 1 resident pupil) |
| Donor-town rules (P14.1) | The donor-town system ended in 2011; Hart's Location keeps its excess statewide education tax |
| Multi-year tuition rates (P14.3) | The contract recalculates tuition each year by formula, with no cap |
| "Under 50 voters" (P9.3) | Consistent with ballots cast (at most 43 found); the checklist count couldn't be read |
| "90%+" federal and state land (P19.1) | About right but slightly high: 89.9% (derived from state maps; 45.7% national forest, 44.0% state park); the 2018 emergency plan gave 87.8% |
| The midnight voting tradition (P10) | Last held in February 2020; later elections used regular hours |
| A "participating agency" for home education (P6.1) | Removed by the July 2026 law, with notices and annual evaluations |
| Cellular dead zones (P8.3) | Correct: no cell tower in town and no service on a 10-mile stretch of Route 302 |
| A parent-to-staff ratio in special education (P13.3) | Not published |

## Corrections and additions to earlier files

Each was checked against the raw copy before it was made:
- **Bartlett, `bartlett_jbes_enrollment_by_grade_2025_26` (note):** said JBES includes "Hart's Location (K–6)"; now K–8 under the contract.
- **Bartlett, `district-tuition-contracts` 15 (note):** adds the trustees' report (both school funds are expendable trusts created in 1992; $81,143.09 at December 31, 2025) and the 2010 minutes' different date for the tuition trust.
- **Jackson, `jackson_sau9_board_seats_and_votes` (note):** adds Hart's Location's derived weighted votes (0).

Also confirmed: the Bartlett finding that Hart's Location minutes don't say how its JBES student travels holds for all 21 sets of minutes from September 2022 to September 2026, and the Bartlett file's CSF feed check.

**Out of date elsewhere:** SAU 9's Hart's Location board page (old meeting schedule); the town website's "population of 43" and its "fewer than 100 residents" midnight-voting rule, which isn't in the statutes.

## Topics added to the shared list

Reviewed with the other towns' proposals on November 13, 2026 and added to `../shared-topics.md`: `school-residency-rules` (shared with Chatham and Tamworth), `federal-land-payments` and `property-tax-relief` (merged with Albany's credits and exemptions topic).

## Coverage

30 questions are answered **fully**, 28 **partly** and 2 by the site's data alone; none has nothing. P16.1 wasn't assigned to an agent by mistake; it is answered by the same facts as P1.1 and P20.1 (K–8 at JBES alongside Bartlett's children) and counted as full.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Young family | **full** (the K–8 contract) | partial (no bus stop; mileage) | partial (preschool access not stated; child care 18–30 miles) |
| P2 Innkeeper | **full** (about $0.92 per $1,000 per pupil, derived) | partial (schedule and notices; no reason recorded for mornings) | **full** (SAU share on property value alone) |
| P3 Hut caretaker | partial (domicile rules; SAU attestation link broken) | **full** (outdoor programs) | partial (care distances; few posted hours) |
| P4 Retired couple | **full** (statewide education tax kept locally) | **full** (no vote on Bartlett or Conway matters) | partial (formula; Bartlett's yearly figures not posted) |
| P5 Hotel supervisor | **full** (JBES for 7–8) | partial (SAU 9 practice; no Hart's Location storm plan) | **full** (meals and counseling) |
| P6 Homesteaders | **full** (no participating agency since July 2026) | partial (access for a tuition town's homeschoolers unclear) | partial (0 EFA students; budget interaction) |
| P7 Retired trooper | partial (Bartlett bus rules; no tracking system found) | **full** (reserves) | partial (Conway Police officer; no Sheriff or State Police link found) |
| P8 Tech executive | partial (rankings and AP; GreatSchools 4/10) | partial (buyer views can't be measured) | partial (no SAU broadband program; coverage gaps) |
| P9 Plow contractor | **full** (no 2027 change for Hart's Location) | **full** (career center) | partial (seats and conflict rules; vacancies) |
| P10 Election official | **full** (one vote; 0 weighted) | **full** (vacancy appointments) | **full** (where to inspect the apportionment) |
| P11 Ski patroller | partial (law allows contracts north; no history) | partial (2024-25 schedule) | partial (early supports; providers) |
| P12 Retired postmistress | partial (state relief; local exemption not found) | **full** (special meetings, reserves, catastrophic aid) | data only (town vs school shares) |
| P13 Special education parents | **full** (district of residence responsible) | partial (transport funding) | partial (staff counts; no caseloads) |
| P14 Rental investor | **full** (excess tax kept; donor towns ended) | **full** (no contract; Fryeburg student funded) | partial (yearly formula) |
| P15 Retired teacher | data only (JBES results) | **full** (Kennett library, arts, AP) | **full** (substitutes and volunteers) |
| P16 Railroad mechanic | **full** (K–8 at JBES) | **full** (career center) | partial (dual enrollment costs) |
| P17 Parent seeking alternatives | **full** (Alternative Program) | partial (charter funding; no district policy) | partial (Bartlett's transfer at Intervale) |
| P18 Divorced parent | **full** (residency and custody rules) | partial (Bartlett's busing policy for two homes) | **full** (who decides) |
| P19 Land steward | **full** (PILT to town; forest receipts to schools) | partial (partnerships named) | **full** (adequacy with almost no students) |
| P20 New couple | **full** (K–12 pipeline) | partial (class sizes; peer life not measured) | **full** (district meeting votes on contracts) |

## Notable findings

- **One student, two schools:** in 2026-27 the district budgets $0 for K–8 tuition and $21,650 plus mileage for one Fryeburg Academy student (about 118–120 miles a school day, derived).
- **A new K–8 pupil adds about $0.92 per $1,000** to the tax rate (derived). The tuition trust ($79,547) covers about two pupil-years.
- **The SAU 9 share is set by property value alone** ($4,521 in 2026-27), so it is owed even in years with no K–8 students.
- **No cell tower:** a 10-mile stretch of Route 302 has no service; fiber was due in July 2026 but couldn't be confirmed.

## Gaps to retry

- How Hart's Location's JBES student gets to school, and any storm plan.
- Bartlett's yearly per-pupil tuition calculations.
- Whether the town adopted an elderly exemption.
- The voter checklist count, the FCC broadband maps and NHDOT's winter pages (all refused automated access).
- Board minutes for 2011–2023.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 2 saved bus and transportation copies (2 in all; schools, child care centers, businesses and other public places keep theirs).
