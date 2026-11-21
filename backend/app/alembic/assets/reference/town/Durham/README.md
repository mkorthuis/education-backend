# Durham: Research for Ask NH Education Facts

Cited facts and figures for answering Durham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the ToLoad towns. Durham's students attend the Oyster River Cooperative School District (SAU 5), shared with Lee and Madbury:
- the preschool program;
- Mast Way (in Lee) and Moharimet (in Madbury), K–4;
- Oyster River Middle (5–8) and Oyster River High (9–12), both in Durham.

Facts about the cooperative are placed `district Oyster River Coop` and serve all three towns; Lee and Madbury have no research of their own yet.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-early-years.md` | School assignment (policy IIB-A: balancing grades before zones), bus times (a derived table), care (Seven Rivers at Moharimet, $35 a day), renters' enrollment, the preschool, meals, class sizes (18–19 in kindergarten), reading (Fundations, CKLA adopted June 2026), Acadience screening, counselors, ESOL (contracted at Mast Way), enrollment by school and town | 13 | 75 | 3 | 46 MB |
| `middle-and-high-school.md` | Grade 8 Algebra and high school credit (policy IMBD), UNH courses (one free a year for juniors and seniors), the calendar, the turf (2016) and the track project, the 8:15 start at both schools, concussions and return to learn, CTE in Dover, Somersworth and Rochester (128 of 150 accepted), apprenticeship credit, phones, laptops, bullying, internships, counselors, letter grades on transcripts, environmental electives | 13 | 117 | 0 | 52 MB |
| `support-and-choices.md` | The paraeducator contract ($21.92–$29.87 an hour), 504 and IEP moves, evaluations, EFAs (not with full-time Seacoast Charter), St. Thomas Aquinas students in sports (NHIAA), returning mid-year, Article 9 (no open enrollment school), Barrington's tuition students (182), Coe Drive (buses only), solar (from the 2022 building), composting since 2014 | 11 | 60 | 0 | 68 MB |
| `money-and-governance.md` | The failed $9,827,000 elementary bond (49.3%, needing 60%), Question 2 (38% in Durham), Durham's share (about 52–54% of taxes with 41–45% of students), salaries and benefits at 77%, the elderly exemption, the $100 audit article (cut from $60,000), spending against Dover and Portsmouth, UNH's agreements, the superintendent search, the 2026 rate ($20.81), the $519,000 floor amendment, the FY28 draft (+8.6%) | 8 | 80 | 2 | 27 MB |
| **Total** | | **45** | **332** | **5** | **193 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.98 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Durham`). All 5 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 39 full, 19 partial, 2 from the site's data.
- **Topics:** the middle and high school file proposed `student-sports-head-injury-rules`. It was merged into `school-sports-rules`, which the Epping research added the same day.
- **Places:** `district Oyster River Coop` 298, `town Durham` 21, no place 11, `district Diocese of Manchester` 2 (St. Thomas Aquinas).
- **Places for the backend:** `places.yaml` already has Barrington's tuition row to Oyster River. No change.
- **Pending facts:** 6 cite draft budgets, the draft strategic plan or unapproved minutes.
- **Raw folders:** all under 100 MB.
- **Quotes:** 587 of 678 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The elementary bond, $9,827,000 | The March 2026 ballot |
  | The bond vote, 1,490 yes and 1,531 no | The district's March 10, 2026 results |
  | The 2026 tax rate, $20.81 | The town's assessing page |
  | The $519,000 restored at the deliberative session | Board minutes, May 6, 2026 |
  | The support staff contract, $543,972 for 2026-27 | The March 2026 ballot |

## Premises checked

| Question says | What the sources show |
|---|---|
| Both elementary schools outside Durham (P1.1) | Right; assignment balances grade sizes first |
| Renters' extra hoops (P5.1) | None |
| The preschool only for special needs (P5.2) | Mainly, with some community children |
| Balanced literacy (P15.1) | Out of date: Fundations and CKLA |
| A private clinic for dyslexia screening (P15.3) | No: the district screens K–3 with Acadience |
| Geometry or algebra II in middle school (P2.1) | No; Grade 8 Algebra, and high school credit under policy IMBD |
| Free UNH courses (P2.2) | One a year for juniors and seniors; $300 a credit after |
| The turf fund (P6.1) | A turf trust holds $292,611; the 2026 ballot's $125,000 went to the general facilities trust |
| A later high school start (P16.2) | No: both schools start at 8:15 |
| Competency grades on transcripts (P16.3) | No: letter grades, without weighting or rank |
| The paraeducator contract passed (P4.1) | Right |
| Article 9 opening Oyster River to other towns (P18.1) | No: it set $0 for students leaving; no open enrollment school |
| Open enrollment students coming in (P18.3) | None; Barrington's students come by tuition contract |
| Money set aside for solar (P19.1) | The panels came with the 2022 building; no savings data |
| The bond failing by 41 votes (P3.1, P9.1) | Only by the yes/no count; it got 49.3% and needed 60% |
| 77% on salaries and benefits (P3.2) | Right |
| A $100 audit article (P8.2) | The petition asked $60,000; the deliberative session cut it to $100 |
| Spending above Dover and Portsmouth (P8.3) | Above Dover, below Portsmouth |
| UNH land taken off the tax rolls by local choice (P12.3) | UNH is exempt under state law; 2016 agreements pay Durham for some costs |
| A superintendent search (P14.2) | Right; the superintendent resigned as of June 30, 2026 |
| $519,000 added at the deliberative session (P20.2) | Right; it restored six staff cuts |

## Corrections and additions to earlier files

- **Dover** (`../Dover/high-school-and-ctc.md`): Oyster River's Program of Studies still links a 2025-26 Tri-City enrollment guide at a different address. It's not a correction to Dover's facts.

## Library notes (for review, not applied)

- `kindergarten-entry-cutoff` 81 (Oyster River) could add Policy JEB's transfer-placement clause, now in `elementary-and-early-years.md`, district-student-support 7.

## Browser pass

The agents' blocked pages were:
- NH DOE's cost-sharing and NH DRA's exempt property pages;
- UNH's CATS page;
- the middle school's solar monitor (a script page).

The first three are PDFs or refuse automated requests, and the monitor needs a browser. None is essential.
