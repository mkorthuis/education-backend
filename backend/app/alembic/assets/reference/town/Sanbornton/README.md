# Sanbornton: Research for Ask NH Education Facts

Cited facts and figures for answering Sanbornton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch, after the Tilton and Northfield research on the same district. Sanbornton is in the Winnisquam Regional School District (SAU 59, with Tilton and Northfield):
- **Sanbornton Central School** (kindergarten to grade 4, 156 students on October 1, 2026) is in Sanbornton; the Winnisquam Early Learning Center and Southwick School are in Tilton and Northfield;
- **Winnisquam Regional Middle School** and **Winnisquam Regional High School** are on the same campus in Tilton (435 West Main Street), with the Winnisquam Career Center (WiCC) next door; the Huot Center for trades is in Laconia;
- Sant Bani School (a private K–8 school in Sanbornton) and Tilton School are the other nearby options.

Tilton's and Northfield's research already holds the district-wide facts; these files cite it and write Sanbornton's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `sanbornton-central-and-families.md` | No full-day Pre-K (the Early Learning Center is IEP-only and half-day; the private Saplings posts $12,300 full-day tuition with a waiting list), the town's licensed Before & After School Program in the school gym (7:00 to 8:20 and 3:15 to 5:30; fees and forms not found), bus sheets for routes 508, 510 and 512 that Tilton's research left blank in the afternoon (route 510's first stop at 7:33 is 57 minutes from school; the north end 15 to 25 minutes), a loss of Title I eligibility for 2026-27, classes of 11 to 18, foster care policy JFABE and trauma-informed training policy JLCK | 13 | 54 | 4 | 2.6 MB |
| `winnisquam-middle-support-and-choices.md` | Middle school math 49% and reading 39% (Sanbornton Central 67% and 53%; state math 44%), honors math sections in grades 6 and 7, the earliest Sanbornton bus to the middle school boarding at 6:05 and taking 73 minutes (derived), EFA students' access to band and sports under policy JJJ, policy EFC on confidential free and reduced-price lunch, Sant Bani and Winnisquam differing on 19 weekdays, a Sanbornton Central summer reading program budgeted ($2,500 pay, $1,200 books) | 14 | 63 | 4 | 5.1 MB |
| `winnisquam-high-from-sanbornton.md` | A morning Huot class away about 2 hours 39 minutes (38% of the school day; the bus ride about 11%), no late or activity bus (ten afternoon routes leaving at 2:31–2:39), one shared school resource officer, two AP English courses, six Early College courses on campus and honors in five subjects, promotion by credits (6, 12 and 18), a same-day risk assessment promised under the suicide prevention plan, ten Lakes Region Scholarship Foundation funds naming the high school | 10 | 30 | 7 | 4.4 MB |
| `money-and-governance.md` | Sanbornton's rate ($12.04, $12.81 and $13.21 in 2023–2025), a 12.6% rise in its local school tax in 2025 (to $5,668,350), its 26.49% share of district costs against 23.4% of students and 34.4% of value, a $1 million district article adding about $0.26 per $1,000, the 2022 bond that failed at about 55% and a bond of up to $7 million for the middle and high school roofs planned for March 2027, average teacher pay 3.7% under Laconia and 9.1% under Gilford, enrollment down 16.2% | 12 | 43 | 5 | 1.3 MB |
| **Total** | | **49** | **190** | **20** | **13 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.3 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Sanbornton. All 20 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 36 full, 24 partial. Three questions (P6.2, P10.1 and P14.3) are answered wholly by earlier files.
- **Topics:** no new topics.
- **Places:** `district Winnisquam Regional` 134, `town Sanbornton` 45, `district Sant Bani School` 9, `town Laconia` 1, no place 1.
- **Pending facts:** 10, citing draft minutes or draft budgets.
- **Raw folders:** each under 100 MB. The 16 saved PDFs are handbooks, policies and state sheets. The bus sheets are kept as transcriptions of streets and times only; the afternoon route sheets were transcribed from images. The town's 2025 report was not saved (it holds name lists).
- **Privacy:** the address scan, including the `--raw` pass over route files, finds only schools, the Winnisquam office and agency addresses. Minutes copies have residents' names removed.
- **Quotes:** 498 of 609 quoted passages found word for word in the raw copies (the misses are mostly table cells joined across columns, schedule lines and the agents' own wording).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The rates $12.04, $12.81 and $13.21 (2023–2025) and the local school rate rising from $4.82 to $5.22 to $5.83 | The site's `town_property_tax` table |
  | Local school tax of $5,034,969 (2024) and $5,668,350 (2025), up 12.6% | The site's `town_school_tax` table |
  | Sanbornton's shares (23.4139% of students, 34.3840% of equalized value, 26.4855% combined) and the slide's "26.49%" | The derived calculations saved with the research and the district's 2026-27 presentation |
  | Sanbornton Central "no longer qualifies for Title I funding" | The June 15, 2026 board packet excerpt |
  | Route 510's stops and times (Weeks Road at 7:33, Shaw Hill Road at 7:36) | The saved transcription of the sheets |

## Premises checked

| Question says | What the sources show |
|---|---|
| A bus to the Early Learning Center in Tilton (P1.2) | Only special education busing, for families "unable to transport their child" within the three towns |
| After-school care once kindergarten starts, affordable until about 5:00 (P1.3, P5.3) | Yes, run by the town in the school gym, 7:00 to 8:20 and 3:15 to 5:30; fees not found; Concord Hospital is 38.5 minutes away, so a 5:00 p.m. pickup misses the 5:30 close |
| A full-day Pre-K (P1.1) | None: the Early Learning Center is IEP-only and half-day; Saplings (private) has a waiting list |
| Buses on back roads and icy dirt roads (P2.1) | First pickups at 7:47, 7:33 and 8:05 for routes 508, 510 and 512; about half of the town's Class V roads are gravel; no source gives a rule for icy dirt roads |
| Start times across three buildings (P8.1) | 8:45 (elementary), 7:34 (middle school homeroom), 7:37 (high school); on the same road the middle and high school bus comes about 81 minutes before the elementary bus |
| Paperwork for a grandmother to enroll and see grades on Alma (P11.1) | The district asks for a physical, immunization records, birth certificate, proof of residency and a court copy of any guardianship order each year; no source says what a non-parent must show for Alma |
| A kindergartner's ride from the north end (P13.2) | 15 to 25 minutes in the morning and 17 to 30 in the afternoon; up to 57 and 59 from the west side |
| Scores "under 50%" (P3.2) | True for the middle school (math 49%, reading 39%) and the district (46% and 45%); Sanbornton Central is 67% and 53% |
| Everyone "sits through the same stuff" (P3.3) | Not so: honors math in grades 6 and 7, Algebra 1 for high school credit in grade 8 |
| An EFA family signing up for band or sports (P9.1) | Yes, by written request under policy JJJ (re-approved November 16, 2026) |
| Local co-ops or nature programs (P9.3) | None found in Sanbornton; Prescott Farm in Laconia runs a Friday homeschool series that takes EFA payments |
| Free and reduced-price lunch is embarrassing (P11.2) | Policy EFC and the point-of-sale system protect it; one exception noted in the file |
| Vacation weeks and snow days line up with Sant Bani's (P16.1) | They differ on 19 weekdays; each school decides its own snow days |
| AP and dual enrollment "without leaving campus" (P6.2) | Yes but few AP: two AP English courses, honors in five subjects and six Early College courses |
| A late bus back to Sanbornton (P8.3) | None found: ten afternoon routes all leave at 2:31–2:39 |
| A Huot student "misses half their regular classes just riding the bus" (P10.3) | The ride is about 47 minutes round trip (11% of the day); the class takes about 38% of the morning |
| A failed math class means "repeating the whole grade" (P14.2) | No: promotion is by credits (6, 12 and 18) with Bear Block help and summer recovery "when available" |
| The buildings "still need new roofs and sprinklers" (P2.3 in the money file) | Partly: Sanbornton Central's flat roof was replaced in 2026; the middle and high school roofs are still ahead (bond of up to $7 million planned for March 2027); only a 2022 sprinkler comment found |
| "SAU #59" takes a share of the bill (P4.1) | No separate bill: the school taxes (local $5.83, state $1.15) are 52.8% of Sanbornton's 2025 tax raised |
| Winnisquam is losing staff to Laconia and Gilford "over pay" (P7.1) | Partly confirmed by the district's own March 2025 statements; Winnisquam's average pay is 3.7% under Laconia and 9.1% under Gilford |
| Sanbornton's rate is "steadier than neighboring towns" (P13.3) | Not supported: seventh steadiest of nine towns |
| "So few young people stay" (P12.3) | Not visible: residents aged 20–34 are 21.7% (±6.2 points) against 18.7% for the state |

## Corrections and additions to earlier files

Applied:
- **Tilton `early-learning-and-southwick.md`, district-student-support 8:** it said Sanbornton Central is a targeted Title I school (quoting the district's Title I page). The June 15, 2026 board packet says it no longer qualifies for Title I funding; the fact and its note now say both.

Not applied (additions for other files):
- **Tilton's table `winnisquam_elementary_bus_routes_2026_27`:** it leaves the afternoon times of routes 508, 510 and 512 blank; they are in Sanbornton's table `sanbornton_central_bus_runs_2026_27`.
- **Tilton `middle-school-support-and-choices.md`, district-student-support 3:** it gives two school counselors (the 2025-26 plan); the 2026-27 staff page lists one School Counselor and a Student Support Coordinator.
- **Tilton `high-school-and-wicc.md`, school-programs-after-grade-6 4 and its advanced-courses table:** Advanced Chemistry Honors and Advanced Biology Honors are described in the guide as "equivalent to the general chemistry course usually taken during the first year of college" and "equivalent to an introductory college biology course," without an AP label.
- **Tilton's Not retrieved list (village district or precinct rates):** Sanbornton's own 2025 rate breakdown shows only municipal, county, local school and state education rates, so the site's $13.21 is its whole rate.
- **Tilton `town-housing` 1:** gives Sanbornton's median home price ($600,500) inside a Tilton fact; Sanbornton's town-housing 2 repeats it with its own source copy.
- **Northfield `district-homeschool-access` 2:** policy IHBG predates the July 2026 law; Sanbornton's file confirms it.
- **Brief figure:** 177 students at Sanbornton Central in 2024-25 (the site) against "approximately 170" in the district's 2026 annual report and 155 on November 1, 2026.

## Library notes (for review, not applied)

- **Site data:** the WRMS handbook's Title I plan gives free and reduced-price lunch eligibility as 31% for 2023-24; the site's 2026 count is 38.7%.

## Browser pass

Not done. Not retrieved:
- NH DOE's 2023 dyslexia fact sheet and its building-aid list (HTTP 403), the Squam Lakes Natural Science Center's site (403), Sanbornton's town report PDFs (404), the town's FY2027 warrant articles and budget draft and its draft housing chapter (links found, not read), and the 2026 tax rates (not set on November 18);
- fees and forms for the town's after-school program, which dyslexia screener Sanbornton Central uses and how many children it flags, a named foster care contact, what a non-parent guardian must show for an Alma account, a rule for icy dirt roads, Sant Bani's aid totals and share of families, a 2026-27 middle school club list, any homeschool co-op near Sanbornton, art and music minutes at Sanbornton Central, how Winnisquam places a ninth grader from a private K–8 school, the waterfront's share of valuation, a count of Sanbornton students at Tilton School, a WRHS FAFSA completion rate, and teacher and paraeducator turnover (not found).
