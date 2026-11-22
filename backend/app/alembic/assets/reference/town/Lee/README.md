# Lee: Research for Ask NH Education Facts

Cited facts and figures for answering Lee, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the second ToLoad batch. Lee is in the Oyster River Cooperative School District (SAU 5) with Durham and Madbury:
- Mast Way School, in Lee: K–4;
- Moharimet School, in Madbury: K–4;
- Oyster River Middle School (5–8) and High School (9–12), both in Durham.

The cooperative's facts are placed `district Oyster River Coop` and serve all three towns. Much of the district was already researched in `../Durham/`; these files cite Durham's facts by topic and number and add Lee's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `mast-way-and-families.md` | Mast Way's 3:25 dismissal, bus stops and times on Lee's roads (197 lookups; middle and high school pickups from 6:53), which part of Lee rides Moharimet's buses, delays and the one early release, class sizes, screen time and outdoor learning, help with food and costs, summer camps ($130–$145 a week), no public pre-K in Lee | 13 | 34 | 2 | 11 MB |
| `middle-and-high-school.md` | UNH courses, Grade 8 Algebra, career programs at Dover (welding and electrical) and the district's 12 daily shuttles, AP results, 187 tuition students at ORHS, letter grades at the high school, late buses (4:30 at ORHS), Personal Finance and life skills, adult classes near Lee | 12 | 63 | 4 | 20 MB |
| `money-and-governance.md` | Lee's school taxes against Durham's and Madbury's, Lee's 33.0% share of the FY27 estimate, the "$1.3 million" (the amount above the default budget), the failed 15% cap (1,246 to 1,698), the internal superintendent search, Mast Way's building (1959; boilers from 2017), the FY28 turf and track request ($1,745,000) | 7 | 45 | 2 | 11 MB |
| `support-and-choices.md` | IEP meeting requests (an answer within 21 days), Mast Way's special education staff and counts (38 students, about 10.3%), Eureka Math², homeschoolers in sports and band (policy JJJ), no yearly homeschool filing since July 2026, enrolling mid-year and military families, ORHS credits (25 plus a capstone from the class entering in 2026-27), diversity | 8 | 38 | 2 | 15 MB |
| **Total** | | **40** | **180** | **10** | **57 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.90 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Lee`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 37 full, 23 partial.
- **Topics:** no new topics.
- **Places:** `district Oyster River Coop` 155, `town Lee` 23, `town Durham` 1, no place 1.
- **Pending facts:** 4, citing draft fall 2026 minutes.
- **Raw folders:** each under 100 MB. The bus lookups list stops by house number, so only times and street names are kept.
- **Quotes:** 409 of 499 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Lee's 2024 rate, $25.77 (school $16.63) | The Town of Lee's 2025 Voter's Information Guide |
  | Mast Way's "Extended Resource Room" | Mast Way's staff page |
  | The district's 40-minute ride goal | The 2026 annual report |
  | Mast Way's 38 special education students | The district's October 1, 2025 counts (10.3% derived) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Leaving work at 3:00 for pickup (P1.1) | Mast Way dismisses at 3:25; an after-school program runs in the building |
| Mast Way overcrowded (P6.1) | About 18–19 children per teacher, within guidelines except kindergarten (19.3 against 18) |
| No public pre-K in Lee (P6.2) | Right; the district preschool is at the high school, mainly for children with disabilities |
| School assigned strictly by street (P6.3) | No: balancing grade sizes comes first (policy IIB-A); Lee's northeast corner rides Moharimet's buses |
| Regular early releases (P7.1) | None in 2026-27 except December 23 |
| A morning late bus (P9.3) | None |
| Honors classes at the middle school (P3.2) | Not called honors, but Grade 8 Algebra is a separate course |
| Welding or electrical "in Dover or Rochester" (P4.1) | Both at Dover only |
| Competency grades at the high school (P11.1) | No: ORHS uses letter grades; the competency scale is the middle school's |
| The tax cap "didn't pass" (P2.2) | Right for both: the 15% petition failed, and Question 2's combined district vote fell short |
| A Mast Way bond for a roof or heating (P8.1) | Not supported: boilers from 2017 in good condition |
| The "$1.3 million" increase (P16.1) | The amount above the default budget ($1,382,085), not the rise over FY26 |
| Turf on the ballot soon (P17.3) | The FY28 draft has $1,745,000 for turf, track and fencing |
| Homeschool paperwork each year (P13.2) | None since July 1, 2026 |
| Buddy programs for military children (P18.3) | None found |
| Everything sent only in English (P20.2) | ParentSquare translates messages |

## Corrections and additions to earlier files

- **Durham** (`../Durham/`): nothing contradicts it. Lee's files add:
  - the board seats by town (one each for Durham, Lee and Madbury, plus four at large, all elected district-wide), which Durham's money file hadn't found;
  - the address for mailing meal applications, 55 Coe Drive (Durham's meals note gives the district office, 33 Coe Drive);
  - middle school advanced math shuttles.
- **Barrington** (`../Barrington/high-school-choice.md`): its 183 Barrington students at ORHS fits the district's count of 187 tuition students.

## Browser pass

- **The Town of Lee's site** (leenh.org) loaded once in Chrome. Its other pages, including the tax rate notice, then showed Cloudflare's "Verify you are human" check, which wasn't completed. So the recreation, library, general assistance and 2026 tax rate pages weren't read.
- **The 2025 Voter's Information Guide** is Lee's own document. It was read from the copy on the Town of New London's site, and the facts cite that copy.
- **Not retrieved** (none essential):
  - NH DOE's special education pages and NH DRA's 2026 rates (HTTP 403);
  - UNH's CATS page;
  - the ORHS scholarship spreadsheet (needs a sign-in).
