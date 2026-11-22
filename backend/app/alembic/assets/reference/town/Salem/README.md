# Salem: Research for Ask NH Education Facts

Cited facts and figures for answering Salem, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 30 resident profiles with 3 questions each, numbered P1.1 to P30.3 in `questions.md`; the people are invented. The research is in the six files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Dover, Rochester, Merrimack and Londonderry. Salem is SAU 57: five elementary schools (Barron, Fisk, Lancaster, North Salem and Soule, K–5), Salem Preschool in the former Haigh School, Woodbury School (grades 6–8, renovated and reopened in 2024), and Salem High School with its career and technical education center, which also takes students from other towns. The Birches Academy (a K–8 charter school) and St. Joseph Regional Catholic School are in town. The district votes by official ballot (SB2).

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | 83 elementary classes averaging 18.4 (October 2026), before- and after-care in each building, the preschool's first-come places and waitlist, free full-day kindergarten since 2019, curricula (Wit & Wisdom, Eureka Math²), Fisk's math results against the district, no gifted program, the reading interventionist proposal | 13 | 82 | 2 | `raw/elementary/` (35 MB) |
| `woodbury-and-choices.md` | Woodbury's size (781), teams, the move from elementary school, the phone ban and October 2026 bullying policy, The Birches' waitlists by grade and sibling priority, St. Joseph's tuition and the EFA's share, policy on private, charter and home-educated students joining Woodbury activities, AP Cybersecurity from 2027-28 | 9 | 84 | 2 | `raw/woodbury/` (26 MB) |
| `high-school-and-cte.md` | The CTE center's programs (no welding, electrical or landscaping; those are at Pinkerton), out-of-town students (about two in five), admission, robotics Team 6324, AP participation against Windham and Pinkerton, the 7:30–2:15 day, baseball teams, VLACS rules, athletics and club budgets | 9 | 66 | 3 | `raw/high/` (25 MB) |
| `student-support-and-families.md` | Educational assistant openings and pay ($19.56 an hour, about $23,267 a year), outside reading tutors for IEP services, the autism program's growth, evaluation referrals, ParentSquare and translation, religious holidays and excused absences, meal prices and options, counselors per school, guardianship paperwork | 12 | 127 | 1 | `raw/support/` (20 MB) |
| `getting-to-school-and-zones.md` | Zones and Tuscan Village (Fisk), kindergarten overflow waitlists, the district's buses to charter and private schools, no late bus at Woodbury, PickUp Patrol, Boys & Girls Club pick-ups and fees, summer enrichment fees, the twins law, school bus passing penalties from 2027 | 9 | 62 | 1 | `raw/daily/` (11 MB) |
| `money-buildings-and-governance.md` | Every bond and what it built (Woodbury still owed to 2040–42), $25.5 million of unused borrowing rescinded, enrollment down 21.4% since 2011-12, Tuscan Village's taxes and students (Town estimates), the default budget ($852,295 below the proposed), the 2026-27 levy, health insurance, teacher pay against the state, app privacy agreements | 10 | 86 | 6 | `raw/money/` (69 MB) |
| **Total** | | **62** | **507** | **15** | **186 MB** |

`brief.md` is the brief the research agents worked from. Six agents used about 3.0 million tokens.

## Checks

- **Parser:** all six files pass the backend's parser (`tools/check_town.sh Salem`). Every table is linked to a topic.
- **Topics:** one new topic was reviewed and added to `../shared-topics.md`: `twins-classroom-placement` (the state law on placing twins in the same or separate classrooms). The Rochester research was told to cite it for its own twins question.
- **Places:** `district Salem` 444, `town Salem` 31, `district Diocese of Manchester` 12, `district The Birches Academy of Academics & Art A Public Charter Sch` 11, no place 7, `district Windham` 2.
- **Places for the backend:** Salem runs its own schools from preschool to grade 12, so `places.yaml` has no Salem rows; the CTE center's sending schools aren't district service arrangements.
- **Draft facts:** one note is flagged: The Birches' August 2026 waitlist figures come from draft board minutes.
- **Raw folders:** all under 100 MB.
- **Spot checks:** each agent checked 3 or more facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | The default budget $98,272,951, $852,295 below the proposed $99,125,246 | The 2026-27 warrant and default budget posting (OCR) |
  | $70,245 for 3 outside tutors serving 7 students' reading IEP services | 2027-28 budget proposal, new programs section |
  | Educational assistants: $19.56 an hour, 6.5 hours a day, 183 days (about $23,267 a year) | Frontline job postings, November 15, 2026 |
  | 1,524 elementary students; Barron 369 | Enrollment report, October 1, 2026 |
  | Woodbury: 781 students in 2025-26 | The district's Reports and Planning enrollment table |
  | The Birches' waitlists: 19 in kindergarten, 36 in grade 1 | The Birches board minutes, August 11, 2026 (draft) |
  | Salem High's day: 7:30 a.m. to 2:15 p.m. | 2026-27 Salem High handbook |
  | Team 6324's 2025 New England District Championship | FIRST and The Blue Alliance team pages; 2026 annual report |

## Premises checked

| Question says | What the sources show |
|---|---|
| "We already paid for the big Woodbury renovation" (P2.1) | Not yet: voters authorized $48.9 million in 2020; the district borrowed $32.8 million, still owed $27.07 million in June 2025, with final payments in 2040–42. The unborrowed $16.1 million was rescinded in 2025 |
| Enrollment is growing from Route 28 development (P2.2) | Not overall: K–12 enrollment fell from 4,282 (2011-12) to 3,366 (October 2026), 21.4%, and is projected flat. The Town estimates Tuscan Village has added about 50 students |
| No breakdown of school debt (P2.3) | Partly: it's in the warrant's MS-27 and the audit (debt service is 8.7% of the 2026-27 budget), but not on the tax bill |
| Another big bond for the elementary schools (P6.3) | None proposed; all five were renovated under the 2010 and 2013 bonds |
| Health insurance "jumping" (P18.1) | Not in the school budget: the line rose 1.9% for 2026-27, 2.5% proposed next year; contract salaries and benefits were about 49% of the increase |
| Something specific gets cut under a default budget (P18.2) | The default is a formula total ($852,295 below the proposed in 2026-27), and the board decides where to spend; the operating budget passed every March checked (2023–2026) |
| "Another $50 million emergency renovation" at Salem High (P18.3) | The ~$50 million project was Woodbury; Salem High's renovation was planned and approved in 2014 ($74.7 million, a $64.0 million bond) |
| Facilities and CTE "brand new" (P8.2) | Partly: Salem High and the CTE center were renovated about ten years ago; Woodbury reopened in 2024 |
| Salem pays "decent salaries" (P21.1) | Partly: average and starting pay are above the state's, but the bachelor's maximum is below it, and the average fell 6.0% after inflation since 2015-16 |
| Tuscan Village's commercial revenue offsets new families (P21.2) | The Town's estimate: $9.87 million in 2025 taxes, $5.48 million to the schools, against about $750,000 for about 50 students; the revenue includes apartments and condominiums |
| Woodbury's renovation fixed entrance security and bus drop-off (P23.2) | Partly shown: "an updated security layout" is mentioned, but no source describes the entrance or bus loop |
| Infinite Campus as the student system (P7.1, P15.3, P23.3) | Correct, but ParentSquare is the main messaging tool, and it translates messages |
| "900 kids at Woodbury" (P3.2) | 781 in 2025-26; 900 is the renovated building's design size and about Woodbury's size in 2015-16 |
| "Six elementary schools, now that Haigh is just preschool" (P12.1) | Five elementary schools plus the preschool; Haigh closed as an elementary school in 2015-16, and the preschool moved in for 2019-20 |
| Tuscan Village zoned for Soule (P1.2) | Fisk, per the district's street list and bus 308 |
| Kindergarten "overflowed somewhere else" (P14.1) | It can happen: a full school puts children on a waitlist by registration order; North Salem and Soule were full in May 2023 |
| Fisk tested higher than the district in math (P11.2) | True 2021-22 to 2024-25 against the all-grades district figure; false in 2025-26 (43% against 48%); Fisk has been lowest of the five elementary schools for three years but had the highest growth in 2025-26 |
| "3rd-grade strings" (P22.1) | Correct |
| Full-day kindergarten (P6.2) | Free at all five schools since fall 2019 |
| Elementary acceleration (P3.1) | None posted; no Salem school reports a gifted program |
| Welding, automotive, landscaping and construction at the CTE center (P4.1, P27.1) | No welding, electrical or landscaping at Salem (welding is at Pinkerton; landscaping is only a half-credit Pinkerton course); automotive and carpentry start in grade 10 or 11 |
| Pelham, Windham and Pinkerton students take CTE seats (P4.2) | Out-of-town students are about two in five (over 260 of about 660); admission is joint, with no stated residence preference |
| Giving up lunch for CTE and AP (P13.1) | Lunch falls within Block 3, so it can't be traded; the limit is eight course slots a year |
| Freshman baseball, JV2 or intramurals (P27.2) | JV and varsity only |
| Salem High's 7:30–2:30 day (P20.2, P27.3) | 7:30 to 2:15; no board discussion of later start times in 226 sets of minutes (2019 to October 2026) |
| The town should bus to the charter school (P9.3) | The district's buses must carry resident charter students, and do: five 2026-27 routes stop at The Birches |
| A late bus after Woodbury activities (P7.3) | None; the free after-school clubs have no ride home |
| After-school and summer programs cost extra (P16.1) | Partly: summer enrichment charged $35 to $300 a class in 2026; Woodbury's after-school clubs are free |
| A 40-minute Barron pick-up line (P14.3) | Can't be checked; no wait times are published |
| Woodbury's new maker spaces and robotics labs (P15.1) | Only the architect's plans mention them; grade 7 Innovators and Makers and Engineering and Design classes exist |
| A Birches lottery for a sibling (P9.1) | Only kindergarten has a lottery; siblings go first, if there is space |
| Cybersecurity classes (P23.1) | None yet; AP Cybersecurity was approved October 27, 2026 for 2027-28 |
| 9th-grade course requests in Infinite Campus in February; St. Joseph and Massachusetts private high schools in the EFA marketplace | Confirmed |
| Educational assistant openings across the district (P5.1) | Confirmed: every school had a special education assistant posting open on November 15, 2026 |
| Fisk evaluates children for speech (P19.2) | Referrals go to a district coordinator; state timelines apply; no Salem timeliness figure was found |
| Long lunch lines (P16.3) | Not checkable |
| Religious holidays not on the calendar (P28.2) | Confirmed; whether an absence is excused differs between policy JH and the upper schools' handbooks |

## Corrections and additions to earlier files

None. The agents found nothing contradicting earlier towns' files. The student support file cites two federal rules (34 CFR 300.323(d) for IEPs and 7 CFR 245.8 for meal privacy) that earlier towns' questions on IEP handoffs and meal privacy could also cite.

**Errors on Salem's own site** (noted in the facts, not ours to fix): Woodbury's special education timeline page gives outdated limits (15 calendar days and 45 days, against 15 business days and 60 days); meal prices differ between Barron's handbook and the 2026-27 meal packet; policy JH and the Woodbury and Salem High handbooks differ on religious-holiday absences; regulation ID-E still gives Salem High's day as 7:30–2:10.

## Coverage

43 questions are answered **fully**, 46 **partly** and 1 by the site's data alone; none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Danielle Kowalski | partial | **full** | **full** |
| P2 Tom "Sully" Sullivan | **full** | **full** | **full** |
| P3 Priya Nair | partial | partial | partial |
| P4 Marco Bellini | **full** | partial | partial |
| P5 Karen Bouchard | partial | partial | partial |
| P6 Devon & Kelsey Miller | partial | **full** | partial |
| P7 Rosa Morales | partial | **full** | **full** |
| P8 Greg Halvorsen | **full** | partial | **full** |
| P9 Hannah O'Connor | **full** | partial | **full** |
| P10 Dave & Lisa Tremblay | **full** | **full** | partial |
| P11 Jason "Jay" Cho | partial | **full** | partial |
| P12 Evelyn "Evie" Beaulieu | **full** | partial | partial |
| P13 Marcus Vance | **full** | partial | partial |
| P14 Nadia Hassan | partial | **full** | partial |
| P15 Brett Gagnon | partial | partial | **full** |
| P16 Claire Desrosiers | partial | **full** | partial |
| P17 Kevin & Amanda Patel | **full** | **full** | partial |
| P18 Diane Gallagher | **full** | **full** | partial |
| P19 Trevor Brooks | partial | partial | **full** |
| P20 Dr. Samira Al-Mansoor | partial | **full** | partial |
| P21 Gary & Brenda Pelletier | partial | **full** | **full** |
| P22 Stephanie "Steph" Morales | **full** | partial | **full** |
| P23 Liam Doherty | partial | partial | partial |
| P24 Cheryl Nadeau | **full** | partial | **full** |
| P25 Alexei Volkov | **full** | **full** | data only |
| P26 Tanya Jenkins | partial | **full** | **full** |
| P27 Paul & Mateo Silva | **full** | **full** | partial |
| P28 Rachel & Ben Cohen | partial | **full** | partial |
| P29 Officer Mike "Mac" MacAllister | partial | **full** | **full** |
| P30 Olivia Chen | partial | partial | **full** |

## Notable findings

- **Debt and taxes:** Woodbury is still being repaid to 2040–42, but every bond is now matched to its building and $25.5 million of unused borrowing was cancelled in 2025. The district projects the 2026-27 local school levy up 7.02%, partly because it used less savings and fewer impact fees to hold taxes down.
- **Enrollment** is down 21.4% since 2011-12; new positions proposed are mostly special education, where the elementary autism program grew from 12 to 32 students in four years.
- **Staffing gaps:** in 2025–26 staff couldn't cover some reading IEP services, so the district paid outside tutors; every school had an assistant opening in November 2026.
- **CTE:** Salem's center has no welding or electrical program, and about two in five of its students come from other towns.
- **The Birches:** 2026-27 waitlists of 19 in kindergarten and 36 in grade 1, but open seats in grade 6.

## Gaps to retry

- **Blocked to automated requests (for the browser pass):** NH DOE's special education public reporting (Salem's evaluation timeliness), two policy PDFs on ParentSquare's file server (other copies were read), St. Joseph's old domains (its current site was used), BLS area definitions.
- **Behind a password or script:** the School Board Portal (minutes and presentations; only agendas are public), Salem High's bell schedule images, the federal FAFSA completion tracker, the NHIAA school list, the town's crossing guard search.
- **Not found anywhere:** the Town's full Tuscan Village tax report (404), a five-year capital plan or building condition report, Woodbury's elective list, bus on-time data, crossing guards at Woodbury and Broadway, the preschool waitlist size, how Woodbury places students in Algebra I, CTE applicants and waitlists by program, counselor wait times and IEP service data, the 2026 tax rate.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 18 saved bus and transportation copies (1,295 in all; schools, child care centers, businesses and other public places keep theirs).
- 7 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
