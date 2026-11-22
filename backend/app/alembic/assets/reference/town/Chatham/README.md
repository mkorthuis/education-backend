# Chatham: Research for Ask NH Education Facts

Cited facts and figures for answering Chatham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the reference library's format (`../../additional-data/README.md`) and uses the shared topics in `../shared-topics.md`. It isn't loaded into the Ask yet; see `../recommended-improvements.md`.

Gathered November 13, 2026. Chatham is the fourth SAU 9 town and the first whose students go to school in another state: MSAD 72 for grades K–8 and Fryeburg Academy for high school, both in Fryeburg, Maine. Neither is in the site's tables, so their facts use a new place form (`maine MSAD 72`, `maine Fryeburg Academy`) and sit in the shared `../maine/` folder, where Jackson and Hart's Location can use them too.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `getting-to-school-and-the-day.md` | Chatham's own bus contract, drive times, Route 113 and Evans Notch in winter, MSAD 72 and Fryeburg Academy calendars and early release, after-school care, free meals, attendance and truancy, late buses, ESY | 6 | 52 | 2 | `raw/daily/` |
| `money-and-governance.md` | The 2026-27 budget and the special education jump, tuition lines and per-student costs, the district's estimated 2026 school rate and the 2024 revaluation, state aid in the district's reports, the tax cap vote, policy JECC (Kennett and other SAU 9 schools), the 0% open enrollment vote, residency, special education across states, MSAD 72 votes and bonds, the board's meetings | 12 | 102 | 5 | `raw/money/` |
| `community-and-families.md` | Population and housing, child care, home education after July 2026, EFAs, the Mulford Trust and scholarships, guardianship, the Pleasant Mountain pass, Mountain Top Music Center, emergency services | 10 | 74 | 6 | `raw/community/` |
| `../maine/msad72-schools.md` (shared) | Where Chatham children attend (New Suncook and Molly Ockett), registration, pre-K, staffing and therapists, gifted program, Maine test results and standards, the Brownfield-Denmark closure study | 11 | 100 | 8 | `../maine/raw/msad72/` |
| `../maine/fryeburg-academy.md` (shared) | Day and boarding students, admission for town-tuitioned students, AP and STEM next to Kennett, Lake Region Vocational Center, trades on campus, fees, counseling, world languages, Maine's diploma rules, early college | 11 | 117 | 5 | `../maine/raw/fryeburg-academy/` |
| **Total** | | **50** | **445** | **26** | **134 MB** (Chatham 76, Maine 58) |

`brief.md` is the brief the research agents worked from. Five agents ran in parallel and used about 2.6 million tokens.

## Checks

- **Parser:** all five files pass the backend's parser with `sau` and `maine` places accepted. Four stray list lines in a "For another file" note were rewritten as one line.
- **Topics:** every topic matches `../shared-topics.md`, after the proposals below were reviewed and added. Three agents independently proposed a topic for Maine's school laws; it was added to the shared list as `maine-school-rules`, and the Fryeburg file's `maine-tuition-academy-rules` was folded into it.
- **Places:**

  | Place | Facts |
  |---|---|
  | `maine MSAD 72` | 115 |
  | `maine Fryeburg Academy` | 112 |
  | `district Chatham` | 89 |
  | `town Chatham` | 58 |
  | `sau 9` | 2 |

- **Adequacy aid update (November 14, 2026):** the site's database now holds NH DOE's adequacy aid calculation for FY2020–FY2027. Two facts and the table of adequacy cost against the statewide tax, which only restated it, were removed, and one fact was cut to why Chatham gets no fiscal capacity disparity aid. The district's own revenue figures were kept; they match DOE's.
- **Tax rates update (November 15, 2026):** the site's database now holds NH DRA's tax rates by town (tax years 2014–2025) and NH DOE's school taxes by town (2011–2025). Five facts and two tables that only restated them were removed: the 2025 rates and tax bill split, the school tax dollars, and the comparison with Jackson, Bartlett and Conway. One fact was cut to the 2024 revaluation. The district's estimated 2026 rate was kept; the earlier rates its annual report gives match DRA's and were removed.
- **Spot checks:** each agent checked 3 to 11 quotes against its raw copies. These were checked again independently, and all matched:

  | Fact | Checked against |
  |---|---|
  | The $1,291,161 budget and special education tuition $105,587 → $398,139 | Annual report budget page and October 2026 agenda |
  | The board's move to 9:30 a.m. | December 2025 and April 2026 minutes |
  | The 0% open enrollment vote (Article 9, March 10, 2026) | Annual meeting minutes |
  | 22 Chatham children in MSAD 72 K–8 (12 Molly Ockett, 10 New Suncook) | MSAD 72's October 1 enrollment sheet |
  | Lake Region Vocational Center serves Fryeburg Academy | Lake Region's program page |
  | Fryeburg Academy at 60.9% publicly funded | Maine DOE's 60% enrollment report (October 28, 2026) |
  | The Mulford Trust's $548,511 grant and no grants to individuals | The trust's 2025 Form 990-PF |
  | 341 residents in 2020 | Census API |

## Premises checked

| Question says | What the sources show |
|---|---|
| Chatham children attend "Molly Ockett School" from kindergarten (P1.1, P5) | Most Chatham K–4 children attend New Suncook School in Lovell (9 of 10 in the October count); grades 5–8 attend Molly Ockett, which has been one K–8 school since C.A. Snow closed in 2017 |
| "Universal pre-K" in MSAD 72 (P1.2) | MSAD 72 runs pre-K at one site (with Head Start); 3 Chatham children were enrolled. Eligibility and cost for non-residents weren't found |
| Early-release Wednesdays at 12:30 (P5.1, P15.1) | Weekly in 2025-26; once a month (nine Wednesdays) in 2026-27. Fryeburg Academy releases the same days at 12:45 |
| Maine's universal free meals cover Chatham students (P5.2) | MSAD 72 serves every student free; at Fryeburg Academy, Chatham's district pays for meals through tuition |
| MSAD 72 talk of shutting schools (P2.2, P8.3) | True: a committee is studying Brownfield-Denmark Elementary and is due to recommend by December 2026. Maine requires a local referendum to close a school |
| The board meets "at 9:00 a.m. in Conway" (P2.3) | Moved to 9:30 a.m. in December 2025; fall 2026 meetings were set at Kennett High School. Budget hearing and annual meeting are evenings at the Town Hall |
| Taxes rise to pay MSAD 72 and Fryeburg (P2.1) | Partly: for 2026-27, about 91% of the increase was out-of-district special education tuition; regular tuition rose 4.1% |
| Tuition "strictly locked to Fryeburg" (P3.3) | Policy JECC lets a family choose another SAU 9 school such as Kennett; Chatham pays up to its MSAD 72 or Fryeburg rate, and the family pays the rest and transport |
| NH open enrollment into Bartlett or Conway (P10.3) | Chatham voters set the share who may leave at 0% in March 2026 |
| Chatham residents vote on MSAD 72 bonds (P6.3) | No: only MSAD 72's seven Maine member towns vote; Chatham pays tuition |
| A six-month rental triggers tuition liability (P13.2) | NH law sets no time test; it turns on whether the family has made its home in Chatham |
| A "large international boarding population" (P11.1) | 205 international (29%) and 220 boarders; 484 of 704 students (69%) are day students |
| Region 9 or Lake Region, or Conway's career center (P7.1) | Lake Region Vocational Center serves the academy; Region 9 doesn't; Conway's center takes Kennett students only |
| Running Start at White Mountains Community College (P17.1) | Renamed; the college lists the academy, but no course with it was found. Maine's free early college excludes non-residents |
| Maine's or New Hampshire's graduation requirements (P17.3) | Neither; the academy's own 21 credits (Kennett requires 25) |
| MSAD 72 7th graders start a language early (P14.3) | Only 8th graders can take a language at the academy |
| A Pleasant Mountain locals pass through MSAD 72 (P11.2) | Sold by the ski area, not MSAD 72; Chatham wasn't on its 2025-26 town lists |
| The Clarence E. Mulford Trust gives scholarships (P9.3) | The trust exists but makes no awards to individuals; it funds organizations, including $548,511 to Fryeburg Academy in 2025 |
| Fewer than 400 residents (P9.2) | Correct: 341 in 2020, 347 estimated for 2025 |
| Homeschool notice and evaluation through SAU 9 or the state (P4.2) | Neither has been required since July 1, 2026 |
| A bus on the Evans Notch end of Route 113 (P10.1) | Chatham's buses are its contractor's, not MSAD 72's; the Evans Notch section is in Maine and isn't maintained in winter |
| A caregiver authorization affidavit for grandparents (P18.1) | New Hampshire has none; the 2026 bill to create one died. Guardianship goes through the court |

## Corrections and additions to earlier files

Each was checked against the raw copy before it was made:
- **Jackson, `maine-school-rules 3` in `Jackson/after-jackson-grammar.md` (formerly `jackson-fryeburg-state-data` 7):** now gives Fryeburg's share of publicly funded students (60.9% in October, Maine DOE).
- **Jackson, `school-programs-after-grade-6 32` in `Jackson/after-jackson-grammar.md` (formerly `jackson-fryeburg-state-data` 9; note):** Fryeburg weights AP and its own College Level courses, and outside college courses don't count in the GPA. The note said "AP and dual-enrollment".
- **Jackson, `school-programs-after-grade-6 1` in `Jackson/money-and-governance.md` (formerly `jackson-gov-high-school-choice` 6; note):** now points to Chatham's policies JECC and JECA.
- **Bartlett, `high-school-tuition-options` 4 (note):** a resident's "$5,500 for IEPs" figure matches Fryeburg's Tutorial Support Program fee; no Fryeburg source ties $5,500 to IEPs.

Checked and found consistent: Jackson's Fryeburg enrollment figures (the Quick Facts page now says 712, already noted), Jackson's Fryeburg transport and residency-letter facts, Jackson's SAU 9 vacation dates, and Chatham's resident ADM of 40 in Jackson's SAU 9 table.

**Out of date elsewhere (not research files):** SAU 9's Chatham page and the town's school board page still say the board meets at 9:00 a.m.; the town's page lists board terms ending in 2025.

## Topics added to the shared list

Reviewed with the other towns' proposals on November 13, 2026 and added to `../shared-topics.md`: `cross-state-school-tuition-rules`, `special-education-placements-across-states`, `school-residency-rules` (also used by Hart's Location and Tamworth) and `school-budget-overruns-and-reserves`. `guardianship-of-minors` was proposed for the library but not used as a topic; the library's `kinship-caregiver-support` covers related ground.

## Coverage

30 questions are answered **fully**, 29 **partly** and 1 by the site's data alone; none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Young parents, North Chatham | **full** (New Suncook, registration) | partial (pre-K exists; non-resident terms and private prices not found) | partial (no published route times; ~35-minute drive, derived; PKA care) |
| P2 Retired logger | **full** (budget drivers, aid) | partial (Maine rate formula; Chatham's agreement not found) | **full** (meeting times, hearing, annual meeting) |
| P3 Physician | **full** (AP and STEM side by side) | partial (Chatham responsible; whose staff evaluate not stated) | **full** (policy JECC) |
| P4 Homesteaders | partial (EFA rules; MSAD 72 activities for Maine residents only) | **full** (no filing since July 2026) | partial (homeschool entry rules; no interview stated) |
| P5 Single mom | partial (monthly early release; PKA) | **full** (free meals) | partial (no rule names road closures) |
| P6 Second-home owners | data only (tax split) | **full** (why a district and SAU) | **full** (no vote on MSAD 72 bonds) |
| P7 Mechanic | **full** (Lake Region) | partial (fees not tied to tuition students) | partial (on-campus trades; no apprenticeship program) |
| P8 Portland transplants | **full** (ratios and Maine results, not comparable to NH) | partial (numbers only; feelings not measured) | **full** (closure study) |
| P9 Retired teacher | partial (Maine tests; reporting to NH DOE not found) | **full** (26 elementary, 15 high school budgeted; cost per added student) | partial (no Mulford scholarships; Fair scholarship names Chatham) |
| P10 Trail crew | partial (Evans Notch closed in winter; stop list not public) | partial (wait-list status for Conway programs is in the site's data; no Fryeburg program publishes a waitlist) | **full** (0% open enrollment) |
| P11 Excavation contractor | partial (numbers and rules; experience not measured) | partial (pass sold by ski area; 2026-27 list unreadable) | partial (no late bus toward Chatham) |
| P12 Ecologists | **full** (MSAD 72 programs) | **full** (both states use NGSS) | partial (gifted program; Maine plan not found) |
| P13 Short-term rental hosts | **full** (rates against Jackson, Bartlett, Conway in the site's data; tax base) | **full** (domicile, not time) | **full** (special meetings, reserves) |
| P14 Social worker | **full** (counseling and prevention at both) | **full** (who pays, which state's rules) | partial (8th grade only) |
| P15 Farmhands | **full** (early release and care) | partial (fees not tied to tuition students; no AP fee policy) | partial (Fair Day closed; no rule for farm work) |
| P16 Retired professor | **full** (adequacy grant, no excess tax) | **full** (SAU 9 seats and votes) | partial (no day/boarding split) |
| P17 Veteran and nurse | partial (transfer credit; WMCC course not found) | **full** (NHCF open to NH residents) | **full** (academy's 21 credits) |
| P18 Grandparents | **full** (court guardianship) | partial (MSAD 72 therapists; Chatham's provider not named) | partial (ESY decided by IEP; transport not described) |
| P19 Designer and woodworker | **full** (arts side by side) | partial (no lesson prices) | partial (timeline; interview not stated) |
| P20 Innkeepers | partial (MSAD 72 office; SAU 9 step not stated) | **full** (calendars side by side) | **full** (sources named) |

## Notable findings

- **Special education drove 2026-27:** the budget rose 33% to $1,291,161, and out-of-district special education tuition went from $105,587 to $398,139. The district estimates its 2026 school tax rate at $11.42, up 56%. Voters also passed the school tax cap question 114–51 (unofficial), effective 2027-28.
- **Where the children are:** 22 Chatham children in MSAD 72's K–8 (most K–4 at New Suncook in Lovell) and 14 at Fryeburg Academy.
- **Chatham runs its own buses** through a contractor (Bennett Transportation, contract to June 30, 2027; $85,804 for 2026-27). Routes and times aren't published.
- **No written tuition agreement was found** with MSAD 72 (a 2016 rider ran to June 2021, then year to year) or with Fryeburg Academy.
- **Emergency services come from outside town:** the sheriff and State Police, Saco Valley Fire in North Fryeburg and Fryeburg Rescue.

## Gaps to retry

- Chatham's tuition agreements with MSAD 72 and Fryeburg Academy.
- Chatham's bus routes and times.
- Maine's 2024-25 school-level test results (the state dashboard refused automated export).
- MSAD 72's gifted plan and its pre-K terms for non-residents.
- Who pays a tuition student's AP exams, lab fees and college-course charges at Fryeburg Academy.
- Chatham town reports after 2015, and the DRA 2026 tax rate.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 10 saved bus and transportation copies (357 in all; schools, child care centers, businesses and other public places keep theirs).
- 1 original route sheet (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
