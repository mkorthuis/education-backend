# Northwood: Research for Ask NH Education Facts

Cited facts and figures for answering Northwood, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the seventh wave of the second ToLoad batch. Northwood is SAU 44, now a one-district SAU:
- **Northwood School** serves preschool to grade 8.
- **High school:** Coe-Brown Northwood Academy, the town's school of record under a contract running to 2035.

The district votes by official ballot. Coe-Brown was researched first in `../Barrington/` and `../Deerfield/`. Nottingham's and Strafford's research, running alongside, cites the new Coe-Brown facts here.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `northwood-school-early-grades-and-families.md` | Champions care ($45–$90 a week after school; no waitlist posted), delayed openings (school opens 10:05), the 2026-27 bus runs, the new school app, Step by Step Preschool (half-day, $100 or $150 a month; an interest list, not a lottery), Title I math help, summer programs by invitation only, meals | 12 | 64 | 1 | 35 MB |
| `northwood-school-upper-grades-support-and-choices.md` | Accelerated math in grades 7–8, take-home Chromebooks ($25 insurance), contracted speech services, policy JJJ (equal access for homeschool and EFA students) and JFBC (EFA limits), the out-of-date homeschool notice policy, door security (no resource officer found), team cuts, volunteer fingerprinting | 12 | 70 | 1 | 26 MB |
| `coe-brown-from-northwood.md` | The assignment and the contract's 10% allowance, the 8th-to-9th move, two bus runs starting 6:22 and 6:30 a.m. (no late bus), shop and welding courses (no formal CTE program), 13 AP courses and SNHU credit, Northwood's special education at Coe-Brown (25 students budgeted), FFA, fees | 11 | 66 | 3 | 24 MB |
| `money-and-governance.md` | The FY27 budget ($16,205,552) and teachers' contract, about 30% of the budget for high school (**derived**), a $1,882,074 energy note (4.65%, to 2041; no bond), the hold-harmless grant cut ($83,820.50 in FY2028), salaries against 10 neighbors, SAU 44 from three districts to one, taxes against Epsom and Pittsfield | 6 | 51 | 4 | 25 MB |
| **Total** | | **41** | **251** | **9** | **110 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.24 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Northwood`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 42 full, 17 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Northwood` 203, `district Coe-Brown Northwood Academy` 35, `town Northwood` 8, `sau 44` 4, statewide 1 (the home education law).
- **Pending facts:** 20, citing draft minutes and the FY2028 working budget.
- **Raw folders:** each under 100 MB. The bus route sheets list stops by house number, so only derived files of times and street names were kept.
- **Privacy:** the main session removed two small businesses' street numbers (from the state's EFA provider list) from a fact and its raw copy. The address scan finds only schools and public offices.
- **Quotes:** 563 of 718 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The FY27 budget, $16,205,552 | The 2026 deliberative session packet |
  | The $1,882,074 energy note at 4.65%, due 2041 | The FY2025 audit |
  | The FY2028 hold-harmless grant, $251,461.51 | The business administrator's November 4, 2026 memo |

## Premises checked

| Question says | What the sources show |
|---|---|
| A Champions waitlist (P1.1) | Prices posted; no waitlist |
| A bus app (P1.2) | None; routes are a PDF |
| Care on delay mornings (P1.3) | Not stated |
| A lottery for pre-K (P5.1) | Half-day, but an interest list, not a lottery |
| Step By Step as a private preschool (P16.3) | It's the district's own |
| After-school tutoring (P18.1) | A Title I math tutor; no after-school program |
| Accelerated math in grades 7–8 (P6.2) | Yes |
| A yearly homeschool letter (P12.2) | Out of date: none required since July 1, 2026 |
| A resource officer (P16.2) | None found |
| Team cuts (P19.1) | Possible; cross country takes everyone |
| Coe-Brown paid for by the town (P2.1) | Correct; up to 10% may go elsewhere |
| A late bus (P2.3) | None found |
| A 6:30 a.m. pickup (P14.1) | About right; one run starts at 6:22 |
| Dover or Concord career centers (P4.2) | Unclear: Dover lists Northwood, Concord doesn't |
| Coe-Brown-only tuition discounts (P13.3) | New England College's is open to 39 schools |
| Taxes up with only about 400 students (P3.1) | 413 at Northwood School, plus about 180 at Coe-Brown |
| A big roof bond coming (P9.2) | None; the roof was redone in 2024 under the energy note |
| Higher taxes than Epsom and Pittsfield (P9.1) | Lower: $11.91 against $17.54 and $17.82 |
| A shared superintendent before (P20.2) | Right: with Nottingham and Strafford until 2021 |

## Corrections and additions to earlier files

- **Deerfield** (`../Deerfield/`):
  - Its money file gives Northwood's 2024-25 K–8 cost per pupil as $24,135; the site and Northwood's 2026 report give $22,632.
  - Its CTE file says Coe-Brown's career-center region wasn't found. Dover's center lists Northwood; Concord's lists neither Northwood nor Coe-Brown.
- **Barrington and Deerfield:** both say Coe-Brown assigns counselors "by grade and last name". Coe-Brown's counseling and admissions pages now give different splits from each other.

## Library notes (for review, not applied)

- **`district-preschool` 85 (Northwood)** says SAU 44 posts no schedule, eligibility or tuition. The 2026-27 flyer gives all three: sessions Monday to Thursday, all Northwood 3- and 4-year-olds, $100 or $150 a month.

## Browser pass

SAU 44's sites show a bot check to automated requests. The main session listed their document libraries in Chrome (`raw/browser/`); the files download directly, and agents used them.

Not retrieved:
- coebrown.org's driver education page and the town's website (HTTP 403);
- the Coe-Brown contract in NH DOE's State Board materials (HTTP 403); the 2025 deliberative packet's copy was used instead;
- the town's 2025 annual report on UNH Scholars (a bot check).
