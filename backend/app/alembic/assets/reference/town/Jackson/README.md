# Jackson: Research for Ask NH Education Facts

Cited facts and figures for answering Jackson, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The site's database doesn't hold any of this. Everything is written in the reference library's format (see `../../additional-data/README.md`), so it can be checked and later loaded.

Gathered November 13, 2026, as the first town. Folded into the shared topics the later towns use on the same day (see "Folded into shared topics" below).

## Files

| File | What's in it | Topics | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `jackson-grammar-school.md` | Classrooms and staff, curriculum and local tests, enrichment, advanced learners, special education and therapies, reading instruction, skiing, PE and the outdoors, devices, homeschool access, preschool | 8 | 96 | 3 | `raw/jgs/` (476 MB) |
| `getting-to-school-and-the-school-day.md` | Jackson's own buses and routes, ride times to Bartlett and Kennett, storm days and plowing, late buses, before- and after-school care, calendar against tourist seasons, absences | 5 | 97 | 3 | `raw/school-day/` (58 MB) |
| `policies-safety-meals-and-support.md` | Meals and summer meals, local food, fees, sports costs, bullying and bus conduct, phones, security grants and drills, parent portals, IEP and 504 moves, English learners, emergency notices | 9 | 125 | 3 | `raw/policies/` (68 MB) |
| `money-and-governance.md` | What cost per pupil covers, budget and tuition lines, the town's tax summary and the 2024 revaluation, SAU 9 cost-sharing and votes, the Bartlett, Kennett and Fryeburg contracts, high school choice, consolidation history | 10 | 117 | 7 | `raw/money/` (181 MB) |
| `after-jackson-grammar.md` | Josiah Bartlett Elementary (grades 7–8), Kennett High (AP, dual enrollment, college outcomes, athletics, support), the career and technical center, Fryeburg Academy, NH and MA test standards, cohort sizes, data portals | 14 | 113 | 10 | `raw/next-schools/` (55 MB) |
| `community-and-families.md` | Household incomes by bracket, Census housing counts, school-age population, licensed child care, private schools within driving range, EFAs, homeschool process, scholarships, police and alerts, home sale prices | 10 | 76 | 9 | `raw/community/` (104 MB) |
| **Total** | | **56** | **624** | **35** | **942 MB** |

Each file starts with a summary and a question table, and ends with a *Not retrieved* list.

## Checks

- **Parser:** all six files pass the backend's own parser (`parse_file` in `education-backend/backend/app/etl/reference.py`). Two facts were rewritten as one-line statements because their bulleted lists cut them off from their sources: `town-streets-and-safe-routes 5` and `district-school-day-and-calendar 23` (both in `getting-to-school-and-the-school-day.md`).
- **Topics:** every topic is a shared topic from `../shared-topics.md` (or the library's `district-preschool`, `high-school-tuition-options` and `comparing-small-schools`), with the shared kind, question type and description.
- **Places:**

  | Place | Facts |
  |---|---|
  | `district Jackson` | 355 |
  | `district Conway` (Kennett, the career center) | 92 |
  | `town Jackson` | 54 |
  | `sau 9` | 50 |
  | `district Bartlett` (JBES) | 30 |
  | `maine Fryeburg Academy` | 11 |
  | `district Northeast Woodland Chartered Public School` | 3 |

  Twenty-nine facts have no place on purpose. They are general context, such as Maine's definition of chronic absenteeism, how the state's security grants work, or a regional housing study.
- **Adequacy aid update (November 14, 2026):** the site's database now holds NH DOE's adequacy aid calculation for FY2020–FY2027. Two facts and the table of adequacy cost against the statewide tax, which only restated it ($0 grant, the statewide tax above the adequacy cost), were removed. The DOE figures kept (value per pupil, resident pupils for SAU 9 votes, SWEPT) were checked against the database and match.
- **Tax rates update (November 15, 2026):** the site's database now holds NH DRA's tax rates by town (tax years 2014–2025) and NH DOE's school taxes by town (2011–2025). Three facts and two tables that only restated them were removed: the school tax dollars, the 2025 rates against Bartlett and Conway, and the match between SWEPT and DRA's state education tax. One fact was cut to the 2024 revaluation, and the derived school share was taken out of the town's example bill. The town's own tax summary and the SAU 9 study figures were kept; they match the database.
- **Spot checks:** every agent checked 3 to 6 of its own facts against its raw copies, and all matched. These were then checked again independently against the raw copies, and all matched:

  | Fact | Checked against |
  |---|---|
  | Jackson's FY2026–27 adequacy figures (since removed; now in the site's data) | `additional-data/raw/town/adequacy-aid.csv` |
  | The FY27 Kennett tuition line ($868,953) | 2026 annual report |
  | Fryeburg's class of 2023 graduation rate (108 of 114, 94.74%) | Maine DOE file |
  | The JGS lunch price ($3.95, $0.40 reduced) | 2026-27 price sheet and handbook |
  | The 12 AP courses | Kennett program of studies |
  | The new Kennett contract's "CPI plus 13%" inflation clause | Contract text |

## Premises checked

The Jackson brief didn't yet ask agents to check the figures and names inside the questions; the later towns' briefs do. These were checked afterward against facts already in these files, the site's data and the later towns' research:

| Question says | What the sources show |
|---|---|
| JGS has "fewer than 35 students" (P3.2) | Close: the site's data shows 38 in 2023-24 and 37 in 2024-25 |
| A graduating 6th-grade class "of 4 or 5 kids" (P6.1) | JGS's grade 6 ranged from 4 to 11 students from 2018-19 to 2024-25 (`school-programs-after-grade-6` in `after-jackson-grammar.md`) |
| Jackson students merge with Madison students in middle school (P6.3) | Not at JBES: Madison students join Conway's Kennett Middle in grade 7 (Conway and Madison research). Jackson and Madison students meet at Kennett High in grade 9 |
| "Strictly locked into Kennett High School" (P7.1) | No: voters approved a Fryeburg Academy agreement 139–30 in March 2026, starting in 2027-28 |
| White Mountain Waldorf as an option (P9.2) | Closed at the end of June 2020; Northeast Woodland, a Waldorf-model public charter in Conway, is open |
| Testing or portfolio reporting required by SAU 9 for homeschoolers (P9.3) | None since July 1, 2026, when the state removed notices and annual evaluations (library topic `home-education-rules`); Jackson's own policy predates the change |
| A public pre-K at JGS (P10.2) | None; a 2018 warrant article to start one tied 97–97 and failed |
| Kennett in "Division II/III" (P11.3) | Division II in most sports for 2026-27; Division III for alpine skiing and Division I for Nordic |
| "AREA" agreements with Bartlett and Conway (P15.2) | None of Jackson's agreements is an AREA agreement; they are tuition contracts under RSA 194:22 |
| Orton-Gillingham reading instruction (P5.3) | Not named in any JGS source; JGS uses Fundations and Leveled Literacy Intervention |
| "Conway Elementary" (P20.2) | Now two schools: Pine Tree Primary (K–2) and Conway Intermediate (3–5) |

## Folded into shared topics

On November 13, 2026, after six more towns had been researched with the shared topics, these files were brought in line with them. No statement, citation or source changed; the facts were regrouped, renumbered and re-placed:

- **Topics:** the 97 Jackson-only topics (`jackson-transport-who-drives`, `jackson-meals-…`) became 56 shared-topic sections, one per topic per file. Most old topics moved whole; 26 facts moved on their own where they belonged elsewhere, for example Kennett's ski racing absences to `district-pe-outdoor-and-athletics` and Maine's definitions to `maine-school-rules`.
- **SAU-wide facts:** 50 facts about SAU 9 as a whole (its meal application, calendars, storm calls, special education manual, budget shares, board votes) now carry `place: sau 9`, as listed in `../sau9/kennett-and-sau9.md`.
- **Fryeburg Academy:** 11 facts about the academy itself now carry `place: maine Fryeburg Academy`, as listed in `../maine/fryeburg-academy.md`. Facts about Jackson's own agreement stay `district Jackson`.
- **Community facts:** 28 Census, child care, nearby-school and family-help facts moved from `district Jackson` to `town Jackson`, as the later towns place them; 3 facts about Northeast Woodland itself now carry its own district place.
- **One-line statements:** 8 more facts whose statements ran onto list lines (bus discipline steps, phone rules, calendar dates, security steps) were rewritten as one line each.
- **References:** every reference to an old topic and fact number, in these files and the other towns' files and READMEs, was rewritten to the new topic and number. The facts stay in these files; the loader merges shared topics across files, and the place decides who sees each fact.

The old-to-new map of every fact (`file|old topic|old number` → new topic and number) is saved with the session's scripts as `fold_jackson_plan.json`.

## Coverage

20 questions are answered **fully**, 40 **partly**, and none has nothing. "Partly" usually means one of two things. Either a source couldn't be reached (NH DOE's iPlatform and nonpublic school list, NH DHHS vital records and the DRA site block automated access), or the question asks for a judgment no data measures ("culture shock", "fit in socially", "treated as equal", "vibrant"). In the second case the files give the facts that bear on it and say what the data can't show.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Remote tech transplant | partial (NAEP-scale cut scores; JGS programs and MAP results) | partial (JGS) | partial (17 private schools with road distances) |
| P2 Hospitality worker | **full** (after-school care to 4:45, sliding scale) | partial (meals) | partial (the site's Census data and incomes by bracket; social fit not measured) |
| P3 Retired homeowner | **full** (cost per pupil covers JGS only; tuition share of tax bill, derived) | partial (budget trend, 2021–22 cooperative study) | **full** (what DRA, DOE and SAU documents show) |
| P4 Ski instructor | **full** (ESSC, Nordic, skiing in PE) | partial (policy JH; nothing on ski racing) | partial (plow priority for bus routes; no record of late runs) |
| P5 Neurodivergent student | partial (contracted therapies, providers not named) | partial (no written JGS-to-JBES procedure) | partial (Fundations, LLI; no Orton-Gillingham named) |
| P6 Rising 7th grader | partial (cohort sizes; orientation in the contract) | **full** (ride times from schedules) | partial (no data by sending town) |
| P7 Second-home owner | **full** (Kennett or Fryeburg from 2027-28) | **full** (12 AP; dual enrollment) | partial (school profile; nothing Jackson-specific) |
| P8 Tradesperson | partial (career center programs; no enrollment) | partial (credit rules; "equal" not measured) | partial (school notices; town alerts; limited cell access) |
| P9 Homeschool-curious | **full** (policy JJJ; revision pending) | **full** (Fryeburg on EFA marketplace; Waldorf school closed 2020) | partial (Jackson's policy predates the July 2026 law change) |
| P10 Young couple | **full** (no licensed care in Jackson, Glen, Intervale or Bartlett) | **full** (no public pre-K; 2018 tie vote) | partial (enrollment and census trend; births blocked) |
| P11 Kennett athletics | partial (late bus "when provided") | partial (no pay-to-play fee found) | partial (NHIAA divisions and titles) |
| P12 Innkeeper | partial (housing data; links not measurable) | partial (English learner program) | partial (Carroll County rooms tax by month; April vacation) |
| P13 Conservationist | partial (device rules; no screen-time limits) | partial (outdoor learning; no WMNF partnership named) | partial (not in USDA Farm to School Census) |
| P14 Grandparent | partial (counselors; no clinician partnerships found) | **full** (parent portal) | **full** (bullying policy covers buses) |
| P15 Governance watchdog | **full** (5 of 29 seats; 3 of 13 votes; weighted votes derived) | **full** (contract terms and dates) | **full** (where budgets and salary schedules are) |
| P16 Gifted/2e | partial (no gifted policy) | partial (Algebra 1 half credit; VLACS) | partial (transition night and freshman day, corrected from the SAU 9 research; no gifted supports found) |
| P17 Working family | partial (fees) | partial (scholarships and camp aid) | **full** (same two buses for both schools) |
| P18 Cross-border explorer | **full** (Fryeburg agreement; families pay until then) | partial (Fryeburg figures; Kennett absenteeism blocked) | **full** (shuttle terms in the agreement) |
| P19 Security-focused parent | partial (security grants; drill details not public) | partial (police size, county dispatch, mutual aid) | **full** (bell-to-bell device bans) |
| P20 Homebuyer | partial (tax rates in the site's data; home values in the site's Census data; the "advantage" is a judgment) | partial (derived ratios; Conway Elementary is now two schools) | partial (GreatSchools and Niche methods; U.S. News blocked) |

## New data concepts

Things the site doesn't have yet that these files bring in. Most are number tables, which the loader skips today:

- **Commute:** bus ride times from published schedules, and road distances (derived, OSRM).
- **Contract terms:** Bartlett (7–8), Kennett (current and 2027–32) and Fryeburg (2027–37): formulas, inflation caps, minimums, transportation.
- **SAU governance:** board seats, statutory votes, weighted votes and cost-sharing by district.
- **Adequacy against the statewide education tax:** now in the site's data (adequacy_aid), so the files no longer repeat it.
- **Chronic absenteeism:** Fryeburg's, from Maine DOE. NH's for Kennett couldn't be reached.
- **NAEP-scale state cut scores:** what NH's and MA's proficiency levels equal on the NAEP scale. The 2022 levels are already in the library; this adds NCES's preliminary 2023-24 levels.
- **School security grants** (SAFE rounds), **Farm to School participation** and **summer meal coverage**.
- **Housing:** 2010 and 2020 Census seasonal and tenure counts, home sale prices and regional housing need. The ACS home values, seasonal share and owner share are now in the site's Census data.
- **Population:** school-age population counts and the district's own anticipated-kindergarten counts.
- **Private school options:** grades, posted tuition and distance.
- **Data portals:** how GreatSchools and Niche handle a 30-student school.

## Before loading into the Ask

Not loaded yet, on purpose: more towns come first. What's still to do before loading is in `../recommended-improvements.md`. For Jackson:

1. **Pending decisions to re-check.** Several facts describe drafts on the November 16, 2026 Jackson School Board agenda: the revised policy JJJ adding EFA students, a new homeschool policy replacing IGBJ (2022), and tuition-student terms (JFAB). Check them after the meeting. The 2026 tax rates were also not out yet.
2. **Raw size.** `raw/` is 942 MB, mostly newsletters and scanned annual reports. Copy only the Markdown files into `assets/reference/`, not `raw/`.

## Follow-ups noted by the research

- **For the transportation file:**
  - Finance Committee notes on bus sizes and hard-to-reach roads (October 29, 2026 draft minutes, `raw/money/finance-committee/`).
  - Kennett's Freedom and Madison late-bus sign-ups (khs.sau9.org).
  - High school shuttle scenarios, including a $680-a-day quote (May 19, 2025 minutes).
- **For the governance file:** October 19, 2026 draft minutes say "Right now we do not have a contract with Fryeburg for 8th grade".
- **For the policy file:** Conway policies IHBH (Extended Learning Opportunities) and IHBI (Alternative Learning Plans) were only partly downloaded.
- **For the care file:** Bartlett Recreation's Adventure Kids after-school program ($8 a day, K–5), Northeast Woodland's aftercare, and the January 2025 note that Jackson was "unable to staff a summer program".
- **For the JGS file:** the November 2026 review of the School Counselor and Family Liaison position, and the "National Forest Reserve" revenue line ($18,989.98 in 2025-26).
- **Not reached at all:**
  - births by town (NH DHHS);
  - Kennett chronic absenteeism (NH DOE iPlatform);
  - NH DOE's free-meals (CEP) list, homeless (McKinney-Vento) liaison list and nonpublic school list;
  - the FCC mobile coverage map;
  - U.S. News pages;
  - NHIAA 2026 ski results;
  - the JBES handbook (access denied).
