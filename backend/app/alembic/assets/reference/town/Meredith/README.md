# Meredith: Research for Ask NH Education Facts

Cited facts and figures for answering Meredith, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the ToLoad towns. Meredith's students attend the Inter-Lakes Cooperative School District (SAU 2), shared with Center Harbor and Sandwich:
- Inter-Lakes Elementary: preschool to grade 6;
- Sandwich Central: K–6;
- Inter-Lakes Middle/High School: grades 7–12, on Laker Lane.

Students may take career programs at the Huot Technical Center in Laconia. Center Harbor and Sandwich have no research of their own; facts about Inter-Lakes serve all three towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `inter-lakes-elementary-and-families.md` | Half-day pre-K, the 7-Upper Club (6:30 a.m.; full days on snow days), doors at 7:55, delays (doors at 9:55), all 11 bus routes (earliest pickup 6:40), the reading program (Wonders, 95% Core Phonics), meals (universal free meals voted down; a district-paid pilot to 300% of poverty), the kindergarten cutoff | 11 | 64 | 1 | 29 MB |
| `middle-and-high-school.md` | Huot (buses only; 2.25 credits a year; no boat building or diesel), AP (nine courses in the catalog), Early College with LRCC, competency grades with GPA and decile rank, phones off and away, eligibility rules, the field lights, grade 11 SAT math (36%) | 11 | 81 | 3 | 17 MB |
| `support-choices-and-safety.md` | The 2026-27 para cuts (no inclusion specialist found) and additions (behavior specialist, BCBA), contracted speech services, moving away mid-year (45 tuition-free days), the 2026 bullying policy, a full-time SRO, the Alma portal, home education and EFAs, extended school year | 10 | 84 | 4 | 28 MB |
| `money-and-governance.md` | Meredith's 71.9586% share (half value, half students, since the 1960s), 896 students and a 5.71% budget rise, special education and health insurance drivers, the field lights ($359,000; $226,163 donated), Meredith Bay (a Laconia development), keeping its state education tax, the Wednesday meeting and Tuesday elections | 10 | 55 | 3 | 31 MB |
| **Total** | | **42** | **284** | **11** | **105 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.88 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Meredith`). All 11 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 35 full, 24 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Inter-Lakes Cooperative` 252, `town Meredith` 24, `sau 2` 3, no place 2, `town Laconia` 2, `town Sandwich` 1.
- **Pending facts:** 4, citing minutes the district still marks as draft.
- **Raw folders:** the four total 105 MB; each is under 100 MB.
- **Quotes:** 719 of 830 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Meredith's share, 71.9586% | Inter-Lakes' 2025 annual report |
  | Meredith's state education tax kept, $4,700,502 | The town report and DRA's 2025 rate breakdown |
  | The field lights' donations, $226,163 | The March 4, 2026 annual meeting minutes |
  | Contracted speech services, $191,072 | The 2025 annual report and 2026 meeting materials |
  | 2.25 credits a year at Huot | The 2026-27 program of studies |

## Premises checked

| Question says | What the sources show |
|---|---|
| Half-day or full-day pre-K (P1.1) | Half-day; parents drive |
| A 7-Upper Club waitlist (P1.2) | The club exists; no waitlist posted, and openings were listed in November |
| Drop-off before 7:30 (P7.3) | The school opens at 7:55; the 7-Upper Club at 6:30 |
| A 5th grader at the middle/high school (P12.2) | Grades 5–6 stay at the elementary school |
| Boat building or diesel at Huot (P2.2) | Neither exists at Huot, WiCC or the high school |
| Free LRCC courses (P6.2) | The catalog says two; LRCC says up to four |
| About 45% proficient in math (P15.1) | 44% in 2026, the same as the state |
| A late bus or night classes (P17.3, P16.2) | Neither found |
| Two paras and an inclusion specialist cut (P5.1) | Paras cut and other staff added; no inclusion specialist found |
| A full-time SRO (P14.2) | Right |
| PowerSchool (P14.3) | The portal is Alma |
| A yearly homeschool portfolio to SAU 2 (P11.3) | Out of date since July 1, 2026 |
| Meredith paying over 70% (P3.1) | Right: 71.9586% |
| A budget rising with under 1,000 students (P3.2) | Right: 896 students, +5.71% |
| A robotics camp cut (P2.3) | Not found; a robotics coach stipend was added |
| $359,000 for field lights (P6.3) | The total, but donations paid $226,163 |
| A 10-to-1 ratio (P15.2) | About 9.8 students per teacher; grade 5–8 classes average 16.3 |
| Votes on a Wednesday (P16.3) | Only the budget meeting; officers are elected on the Tuesday town ballot |
| Sending money to the state (P10.2) | No: Meredith kept all of its 2025 state education tax |
| "Meredith Bay" addresses (P4.3) | A gated development in Laconia; its children attend Laconia schools |

## Corrections and additions to earlier files

None needed. Laconia's Huot and private school facts are consistent.

## Library notes (for review, not applied)

- **`early-college-at-your-high-school` 5 and `dual-enrollment-rules` 3:** the high school's catalog still says two free Early College courses; LRCC says up to four.
- **`budget-form-and-vote-dates` 64 (Inter-Lakes):** consistent. It could add that officers are elected on the town ballot day.

## Browser pass

The agents' blocked pages were:
- NHIAA's co-op team pages (HTTP 403), so whether hockey and lacrosse are co-ops is open;
- the federal 504 guide;
- the June 2026 behavior support plan (script-only);
- DRA's 2026 tax rates.

None is essential to the answers.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 26 saved bus and transportation copies (273 in all; schools, child care centers, businesses and other public places keep theirs).
- 22 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- Graduates' names removed from 1 saved annual report copy; 1 PDF deleted.
