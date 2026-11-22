# Pelham: Research for Ask NH Education Facts

Cited facts and figures for answering Pelham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the ToLoad towns. Pelham is SAU 28, a one-district SAU, with all three schools on Marsh Road:
- Pelham Elementary: preschool to grade 5.
- Pelham Memorial: grades 6–8.
- Pelham High: grades 9–12.

High school students may take career programs at Salem, Alvirne's Palmer Center or Pinkerton.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-early-years.md` | The Marsh Road campus, before- and after-school care, full-day kindergarten (no fee), class sizes (125 kindergartners in 7 classes), the third reading specialist, the preschool lottery ($180 or $210 a month for peers), IEP and speech timing, bus routes and times (a derived table of all 14), summer reading, the pickup line, building security, recess and the arts rotation, lunch and allergies | 20 | 71 | 2 | 20 MB |
| `memorial-and-high-school.md` | The Memorial renovation ($31.98 million, 2024) and class sizes, middle school math (24–30%, then 45% in 2026) and the Reveal curriculum, AP and honors, dual enrollment (two free community college courses), community service (40 hours since 1992), four years of math (policy IKF), sports and eligibility, away-game buses, summer online courses and GPA, twins, SAT against Windham (site data), graduates' plans | 11 | 86 | 2 | 30 MB |
| `support-buses-and-choices.md` | CTE at Pinkerton (primary), Salem and Alvirne (about 50–56 students a year, Pelham's own buses), out-of-district placements (16 a year), free meals, one ESOL teacher, translation notices, Yondr pouches at Memorial, 504 moves, snow calls (about 5:30–6 a.m.), homeschoolers in sports and single classes (policy IHBG still out of date), working papers | 10 | 61 | 2 | 29 MB |
| `money-staff-and-governance.md` | The school share of taxes (about 65% of $14.41 in 2026, after reassessment), the tax cap (approved 4,680–1,871; the FY2026 levy would have been about $834,600 over), central office at 4.71%, about 11 teaching positions cut over five years, the special education reserve request (up to $168,000 to reach about $400,000), pay against Windham and Salem ($17.51 starting for assistants), retention, the draft FY2028 default budget | 8 | 73 | 8 | 12 MB |
| **Total** | | **49** | **291** | **14** | **91 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.95 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Pelham`). All 14 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 35 full, 24 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Pelham` 279, `town Pelham` 10, no place 2.
- **Places for the backend:** none needed. Pelham runs every grade, and its CTE options are career-program arrangements.
- **Pending facts:** 7 cite the draft FY2028 default budget and 2027 warrant.
- **Raw folders:** all under 100 MB.
- **Quotes:** 491 of 676 quoted passages found word for word in the raw copies. Most misses are tables and slide text.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Question 2 approved 4,680 to 1,871 | The town's November 2026 election results |
  | Pelham Memorial bond, $31,980,000 | The town's 2025 report (bond schedule) |
  | Assistants' starting pay, $17.51 | The 2026 deliberative session slides (PESPA agreement) |
  | The special education reserve, $232,109 on June 30, 2025 | The same slides |

## Premises checked

| Question says | What the sources show |
|---|---|
| All three schools on Marsh Road (P1.1) | Right: built 1964, 1972 and 2001 |
| Kindergarten full or half day, any fee (P6.1) | Full day, no fee posted |
| A reading specialist added (P6.3) | Right: a third, hired for 2026-27 |
| All private daycare for 3- and 4-year-olds (P8.2) | No: a district preschool with tuition-paying peers by lottery |
| A renovated Memorial and smaller classes (P2.3) | Right, though class size fell before the building reopened, with enrollment down 22% |
| Middle school math around 30% (P4.3) | Right for 2022–2025; 45% in 2026 |
| Free dual enrollment (P4.2) | Two community college courses a year are free; SNHU courses cost $100 |
| 40 hours of community service (P7.1) | Right, since 1992 |
| Four years of math (P12.1) | Right: policy IKF, and state rules require math every year |
| Summer online classes left out of GPA (P12.3) | Mostly; VLACS courses count |
| CTE at three centers, and who buses (P2.1, P2.2) | Right: Pelham pays tuition and runs two CTE buses; no HVAC anywhere, electrical only at Pinkerton |
| Free lunch automatically (P11.3) | Only through SNAP, TANF or foster, homeless or Head Start status |
| Working papers through the school office (P17.1) | Partly out of date: a parent can now issue them |
| Two-thirds of the tax bill to schools (P3.1) | Holds: about 65% |
| The tax cap (P3.2) | Adopted; it starts with the FY2028 budget |
| A $400,000 reserve request (P10.2) | Up to $168,000, to bring the fund to about $400,000 |
| Staff cuts while budgets rise (P7.3, P20.3) | About 11 teaching positions over five years, mostly by attrition; assistants are being added |
| Pay against neighbors (P10.3, P20.1) | Assistants start lower than in Windham and Salem; assistant retention 72%, teachers 93% |

## Corrections and additions to earlier files

None needed. Hudson's Palmer count (6 Pelham students), Salem's PHS figures, Windham's Algebra I table and Windham's cost-per-pupil comparison all agree with this research.

## Library notes (for review, not applied)

- The brief gave Memorial 349 students for 2025-26. That's the 2024-25 figure; the district's October 1, 2025 count is 339.

## Browser pass

The agents' blocked pages were:
- psacc-nh.org, the before- and after-school program's rates and waitlist;
- NH DOE's special education and building aid pages;
- one bus driver job posting.

The NH DOE pages are PDFs or report tools Chrome can't read, so they remain gaps.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 8 saved bus and transportation copies (639 in all; schools, child care centers, businesses and other public places keep theirs).
- 2 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- The state's resident birth, marriage and death lists removed from 1 saved town report copy (headings and record counts kept).
