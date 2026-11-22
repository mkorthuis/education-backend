# Milton: Research for Ask NH Education Facts

Cited facts and figures for answering Milton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the seventh wave of the second ToLoad batch. Milton is SAU 64, a one-district SAU:
- **Milton Elementary School** serves preschool to grade 5.
- **Nute Junior High (grades 6–8) and Nute High (9–12)** share one building on Elm Street, with the Nute Library.
- **Career programs:** the Tri-City centers (Creteau at Spaulding in Rochester, and Dover), whichever is nearest.

The district votes by official ballot. Creteau was researched in `../Rochester/`; Wakefield's research (`../Wakefield/`) ran alongside.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `milton-elementary-and-families.md` | The preschool (24 children in 2023-24, 14 with IEPs; no hours or tuition posted), one school day for all grades (8:25–3:05), no after-school care at the school, buses from 2 miles (preschoolers not named), a reading specialist and math interventionist, no crossing guard (the 2025 sidewalk audit on Elm and Dawson), storm rules | 14 | 72 | 1 | 33 MB |
| `nute-junior-high-support-and-choices.md` | Open enrollment adopted 422–395 (10 students in, 1% out), the special education review (turnover; 6 contracted case managers and 16 contracted paras), FY2027 staffing cuts, math at 23% (2024-25), policy JJJ naming EFA students, the bell-to-bell phone ban, grades 6–12 in one building, the Nute Library | 12 | 72 | 2 | 20 MB |
| `nute-high-school.md` | No AP taught in house (honors levels in 16 courses), free VLACS, Great Bay Early College, the Tri-City centers and the "nearest center" rule (welding only at Dover), graduation 86.2% for 2025, Farmington-Nute co-op teams, no JROTC, shop courses without a listed teacher | 10 | 78 | 3 | 8 MB |
| `money-and-governance.md` | The 2026-27 default budget ($13,226,216) above the voted budget ($12,862,856), the budget committee's cut (5-2) and the board's 0-5 vote, a deficit of $2,547,444 found in summer 2026 (no audit since 2023), adequacy aid down $739,165, the tax cap, Dr. Andrew Dolloff's feasibility study (including tuitioning students out) | 13 | 83 | 4 | 21 MB |
| **Total** | | **49** | **305** | **10** | **82 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.13 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Milton`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 29 partial, 1 from the site's data.
- **Topics:** no new topics. One rule fact on related services is added to the library's `special-ed-iep-basics`.
- **Places:** `district Milton` 280, `town Milton` 14, `sau 64` 6, statewide 4, `district Rochester` 1.
- **Pending facts:** 1.
- **Raw folders:** each under 100 MB. Bus route copies keep only times and street names.
- **Privacy:** the address scans find only the schools and the SAU office. The town's sidewalk audit lists problem spots by street number, with no names; it was kept.
- **Quotes:** 606 of 767 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The default budget, $13,226,216, and the voted budget, $12,862,856 | The 2026 warrant and election results |
  | Open enrollment passed 422–395 | The 2026 election results sheet |
  | The deficit, $2,547,444 | The district's September 16, 2026 finance letter |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day pre-K, or a couple of hours (P1.1) | Can't be confirmed; no schedule posted |
| A bus for a pre-K child (P1.2) | Not promised, except under an IEP |
| After-school care at the school (P1.3) | None found |
| Reading specialists (P4.2) | Yes, one, plus a math interventionist |
| A late bus after a missed bus (P10.2) | None |
| Full-day kindergarten (P17.1) | Likely: one school day for all grades |
| A crossing guard at Elm and Dawson (P17.3) | None found |
| Math around 23% (P2.3) | Right for 2024-25; 20% in 2025-26 |
| 6th graders with seniors (P15.1) | Correct |
| Open enrollment (P9.2, P16.3) | Adopted March 2026 |
| Unfilled special education jobs (P5.1) | Partly: turnover and contracted staff |
| About 160 at Nute High (P6.1) | Close: 149 to 166 by different counts |
| AP taught in person (P6.1) | No |
| A 75% graduation rate (P8.1) | Out of date: 86.2% for 2025 |
| Free Great Bay classes (P12.2) | Two a year, then half off |
| JROTC (P18.1) | None at Nute; at Dover and Creteau |
| Shop classes cut (P2.2) | Still listed, but no teacher listed |
| A default budget above the proposal (P3.1, P14.2) | Correct for 2026-27 |
| Adequacy aid "keeps dropping" (P3.3) | Fell for FY2027 after rising |
| A study on closing Nute (P11.1) | Correct: Dr. Andrew Dolloff, no decision |
| A split board and budget committee (P14.1) | Correct |

## Corrections and additions to earlier files

- **Farmington** (`../Farmington/`):
  - Its money file says Milton "hired a consultant": Dr. Andrew Dolloff, October 2026, for under $15,000.
  - Its high school file lists football as a co-op with Milton and says NHIAA classifications weren't retrieved. NHIAA's 2026-27 alignments show Farmington-Nute in Division IV football and Division III boys' soccer.
  - Its notes quote Farmington minutes that "Prospect Mountain is the only district currently having open enrollment". Milton adopted open enrollment in March 2026.
- **Rochester** (`../Rochester/`): Nute's 2025-26 Program of Studies lists 17 Creteau programs, with details the Creteau file lacks (dual enrollment and internships for several).

## Library notes (for review, not applied)

- **`district-preschool` 72 (Milton)** found no preschool details. This research adds the 2023-24 make-up, October counts and the contact, though still no hours or tuition.
- **`kindergarten-day-length` and `kindergarten-entry-cutoff`** list Milton as not found: one school day for all grades, and age 5 before October 1.
- **`raw/programs/cte-centers.csv`** lists Creteau's sending schools as Rochester, Somersworth and Dover only. Milton students attend too, under the Tri-City agreement.
- **`raw/programs/head-start-sites-nh.csv`** marks CAPSC's Milton Children's Center as closed.

## Browser pass

SAU 64's sites show a bot check to automated requests. The main session listed their document library in Chrome (`raw/browser/`); the files download directly, and agents used them.

Not retrieved:
- the Town of Milton's website (a bot check) and its 2025 town report on UNH Scholars, for the March 2026 vote counts, the Nute Library's hours and recreation;
- SAU 64's web pages beyond the document library;
- the 2026-27 board minutes and the November 18, 2026 budgets, not yet posted;
- NHIAA's schedules (HTTP 403).
