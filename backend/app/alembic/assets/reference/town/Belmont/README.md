# Belmont: Research for Ask NH Education Facts

Cited facts and figures for answering Belmont, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the ToLoad towns. Belmont's students attend the Shaker Regional School District (SAU 80), shared with Canterbury:
- Belmont Elementary (BES): preschool to grade 4;
- Canterbury Elementary: K–5;
- Belmont Middle (BMS): grades 5–8;
- Belmont High (BHS): grades 9–12.

BHS students may take career programs at the Huot Technical Center in Laconia or the Winnisquam Career Center (WiCC). Canterbury has no research of its own; facts about Shaker serve both towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | Boys & Girls Club care in the BES gym (6:45 a.m.–5:30 p.m.; $59 and up to $83 a week), BES bus runs and Main Street stops, staff openings, the free preschool (lottery when full), volunteers' background checks paid by the district, the homeless liaison, no foster care policy | 14 | 64 | 2 | 32 MB |
| `middle-school-and-choices.md` | Math results (43% in 2025) and the district's plan, arts and music, the November 2026 list of possible cuts, the late bus (to Canterbury only), IEP meeting timing, EFAs and Laconia-area private schools, homeschool paperwork after July 2026 | 15 | 87 | 0 | 22 MB |
| `belmont-high-and-huot.md` | Huot and WiCC bus runs, proficiency grading and Habits of Work, Early College with LRCC, JV softball suspended, no athletic fee found, NH Scholars, transcripts and records, no adult education at BHS, the Lakes Region course-sharing agreement | 11 | 62 | 2 | 24 MB |
| `money-and-governance.md` | The rate ($19.61; +10.48% in 2025, +12.77% in 2026), $1.47 million less state aid, health insurance (+20.1%), the cap's estimated $1,144,613 cut, the cost split (Belmont 75.8%), teacher resignations, no bonded debt, the ballot vote and Thursday deliberative session, the 2023 Canterbury withdrawal study | 8 | 71 | 3 | 62 MB |
| **Total** | | **48** | **284** | **7** | **140 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.98 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Belmont`). All 7 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 27 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Shaker Regional` 258, `town Belmont` 15, no place 9, `district Winnisquam Regional` 2.
- **Pending facts:** 14, citing the November 10, 2026 draft minutes.
- **Raw folders:** each under 100 MB.
- **Quotes:** 508 of 780 quoted passages found word for word. The lower rate is because Shaker's minutes number every line, so the text copies break passages with line numbers. A sampled miss matched the minutes once those breaks were allowed for.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $19.61 | The town's assessing page and 2026 rate notice |
  | Belmont's share, 75.8% | The 2026-27 deliberative session book |
  | The cap's estimated cut, $1,144,613 | Board minutes, November 10, 2026 |

## Premises checked

| Question says | What the sources show |
|---|---|
| Care only in Laconia (P1.1) | No: the Boys & Girls Club runs care in the BES gym on school days |
| Volunteers pay for checks (P14.3) | No: the district pays |
| About 43% proficient in math (P1.2) | Right for 2025 (40% in the site's 2026 data) |
| Arts and music cut (P5.2) | Still offered; on the board's list of possible 2027-28 cuts |
| A late bus (P2.3) | Only to Canterbury, at 4:50 |
| Homeschool paperwork with SAU 80 (P9.3) | Out of date since July 1, 2026 |
| Running Start (P3.3) | Early College with LRCC, five course pairs |
| Nursing at Huot (P3.1) | Partly: the LNA license comes through outside providers |
| Electrical at Huot (P19.1) | Neither Huot nor WiCC has an electrical program |
| An NH Scholar cord (P19.3) | No BHS source mentions one |
| JV teams struggling (P7.1) | JV softball suspended for 2026-27; JV on the possible cut list |
| Adult education at BHS (P20.3) | None; the nearest are in Laconia, Franklin and Concord |
| The tax jump (P10.3, P13.1) | Right: +10.48% in 2025, +12.77% in 2026; schools are 62–64% of the rate |
| A tax cap's cuts (P13.2) | Adopted; an estimated $1,144,613 cut; no decisions yet |
| The Belmont–Canterbury split (P13.3) | Half by students, half by value: Belmont pays 75.8% |
| A bond (P16.2) | None proposed; no bonded debt |
| A separate ballot and a Saturday session (P18.1) | Ballot in March; the school session is a Thursday evening; Saturday is the town's |

## Corrections and additions to earlier files

- **Laconia** (`../Laconia/high-school-and-huot.md`): consistent. WiCC's five programs are new and are written with `district Winnisquam Regional`.
- **Albany** (`../Albany/programs-and-outcomes.md`, cte-admission-and-cost-rules 4): it gives the sending district's share as 25% of the CTE portion of cost per pupil. Shaker's business administrator told the board "20% of the tuition costs". The bases may differ, so it's worth checking. Not changed.

## Library notes (for review, not applied)

- **`district-preschool` 102 (Shaker)** says no tuition is posted. The application says the program is free.
- **`budget-form-and-vote-dates` 124 (Shaker):** still correct.

## Browser pass

The agents' blocked pages were:
- the registration page (HTTP 403);
- NH DOE's liaison lists;
- nhscholars.org (Windham's printed copy was used);
- the State Board's December 2023 minutes.

None is essential to the answers.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 7 saved bus and transportation copies (1,634 in all; schools, child care centers, businesses and other public places keep theirs).
- 3 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- House numbers of home stops removed from quotes in the research files.
