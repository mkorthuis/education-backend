# Gilford: Research for Ask NH Education Facts

Cited facts and figures for answering Gilford, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the ToLoad towns. Gilford is SAU 73, a one-district SAU:
- Gilford Elementary School (GES): K–4;
- Gilford Middle School (GMS): grades 5–8;
- Gilford High School (GHS): grades 9–12.

GHS also takes Gilmanton's high school students under an AREA agreement to 2035. GHS students may take career programs at the Huot Technical Center in Laconia or the Winnisquam Career Center in Tilton. The district's site is now sau73nh.gov.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `gilford-elementary-and-families.md` | The Youth Center's "Rise and Shine" (7:00–8:30, bused to school) and After School Club ($60 a week; Wednesday and Thursday waitlisted), Extended Day ($20 a day to 5:30; closed on early releases and snow days), Gilford Got Lunch (no income test), no public pre-K, the September 30 cutoff, class-size policy, a 45-day evaluation deadline, Title I in the classroom | 16 | 83 | 0 | 21 MB |
| `gilford-middle-school.md` | Algebra I in grade 8 (21 students in 2023-24), high school credit under policy IMBD, phones in lockers bell to bell, Chromebooks home nightly, bus runs (first stops 6:37–6:49), policy JJJ for home-educated and EFA students, the out-of-date home education policy, ski teams, absences for sports | 12 | 76 | 1 | 12 MB |
| `gilford-high-and-huot.md` | Huot (auto, no welding; a run at 8:42) and WiCC (welding; 7 Gilford students), 26 credits from the Class of 2030, six AP and eight Early College courses on a trimester schedule, AP access under the revised policy IHCD, graduation at the Bank of NH Pavilion in 2026, boys' hockey with Belmont, counselors (4.0 since 2017-18), internships | 11 | 58 | 3 | 32 MB |
| `money-and-governance.md` | The 2026-27 budget ($32,185,627; +2.81%, 4.26% with the teachers' contract), the budget up 20.4% from 2021-22 while enrollment fell 8.6%, Gilmanton's AREA tuition ($4,471,465 budgeted; average net cost plus a bond charge), the superintendent search (new superintendent July 1, 2027), SB 2 dates, meeting access | 7 | 62 | 2 | 17 MB |
| **Total** | | **46** | **279** | **6** | **82 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.87 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Gilford`). All 6 tables are linked to a topic.
- **Coverage:** all 60 questions are listed: 22 full, 34 partial, 2 from the site's data, and 2 with none:
  - P17.3: sports bus return times aren't published;
  - P18.2: no instrument rule was found.
- **Topics:** no new topics.
- **Places:** `district Gilford` 260, `town Gilford` 15, `district Gilmanton` 2, `district Laconia` 2.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB. Only the text of the 79 MB Program of Studies is kept.
- **Quotes:** 563 of 675 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The budget, $32,185,627 | The 2026 warrant (MS-27) and approved minutes |
  | Gilmanton tuition revenue, $4,471,465 | The 2026 warrant |
  | 26 credits from the Class of 2030 | The 2026-27 school profile and Program of Studies |

## Premises checked

| Question says | What the sources show |
|---|---|
| The Good Morning Club (P1.1) | Not under that name; the Youth Center's "Rise and Shine" runs 7:00–8:30 |
| Extended Day closing on early releases (P1.2) | Right, and on snow days; the Youth Center club closes too |
| Lunch prices going up (P5.1) | Can't be confirmed; only 2026-27 prices are posted |
| Income rules for Gilford Got Lunch (P5.3) | None: any Gilford student may join |
| Public pre-K (P9.1) | None, apart from services for children with disabilities |
| Full-day kindergarten and the cutoff (P9.2) | One 8:50–3:00 day; five by September 30 |
| A ski club bus to Gunstock (P10.2) | Not confirmed; GMS has alpine and Nordic teams |
| Algebra 1 in grade 8 (P12.3) | Right |
| Yearly homeschool paperwork (P13.3) | Wrong under the July 2026 law |
| Welding at Huot (P3.1) | No: welding is at the Winnisquam center |
| A bus to Huot (P3.2) | Right |
| Graduation at the Bank of NH Pavilion (P11.3) | Right for 2026; it may move to campus; no ticket limit posted |
| Co-op teams with Laconia (P17.1) | None; only boys' hockey, with Belmont |
| More counselors (P20.1) | Not supported: 4.0 positions every year from 2017-18 to 2023-24 |
| A 2.8% budget increase (P15.1) | Right: 2.81% (4.26% with the teachers' contract) |
| Superintendent retiring (P7.3) | A new superintendent starts July 1, 2027; no reason posted |
| Cuts from falling enrollment, arts cuts (P14.2, P18.1) | None in the posted budgets or minutes |

## Corrections and additions to earlier files

- **Laconia** (`../Laconia/high-school-and-huot.md`): the federal data table's note quotes Gilford's 2023-24 answer that students may not choose AP courses. It now adds that Gilford's policy IHCD, revised October 5, 2026, permits any student who meets the criteria. Laconia is re-synced.
- **`places.yaml`:** the Gilmanton → Gilford note says Gilmanton's renegotiation "ended in September 2026 with no change." Gilford's posted records show an agreement approved April 6, 2026, and nothing after June, so the note isn't confirmed here. Not changed.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 42 (Gilford)** says the 2026 deliberative session date wasn't found. It was Tuesday, February 3, 2026, 7:00 p.m., at GHS.
- **The coverage table's Gilford columns** say the kindergarten cutoff and preschool weren't found. Both are here now.

## Browser pass

The agents' blocked pages were:
- the town site and the 2025 town report (HTTP 403), so the 2026 tax rate and exemptions are missing;
- Gunstock's pages;
- the town's programs page;
- NH DOE's enrollment reports.

None is essential to the answers.
