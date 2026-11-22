# Amherst: Research for Ask NH Education Facts

Cited facts and figures for answering Amherst, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the ToLoad towns. Amherst is in SAU 39:
- **The Amherst School District** runs Clark School (kindergarten and the preschool), Wilkins School (grades 1–4) and Amherst Middle School (grades 5–8).
- **The Souhegan Cooperative School District** (Amherst and Mont Vernon) runs Souhegan High School (grades 9–12).

Mont Vernon has no research of its own. Facts about Souhegan are placed `district Souhegan Cooperative` and serve both towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `clark-wilkins-and-families.md` | Bell times (7:45–2:25 against the middle school's 8:30–3:24), early-release days (three a year), YMCA care inside Wilkins to 6 p.m. and Hampshire Hills' van, bus routes on Baboosic Lake Road, kindergarten (83 children in 6 classes; seven aides budgeted), the portable (approved 1,627–1,551), the 2026 Wilkins plan (grade 5 stays at the middle school), grade 3–4 scores against Bedford, Hollis and the state, a state drill-law topic | 15 | 73 | 3 | 61 MB |
| `amherst-middle-school.md` | Yondr pouches 8:30–3:24 with lunch, the lower (5–6) and upper (7–8) schools, learning specialists and programs, paraprofessional cuts (4 in FY27, 3 more proposed), no late bus on the 2026-27 route sheets, shared buses with Souhegan, electives, charter school busing (none), EFAs (130 eligible) and private high school admission, home education (Amherst's April 2026 policy IHBG, read in Chrome) | 11 | 58 | 1 | 33 MB |
| `souhegan-high-school.md` | Work Study Practices (not "Whole Schooling"), unleveled classes with Honors Challenge, 17 AP courses, CTE (43 students; reserved seats at Nashua and Milford, Palmer space-available), the 2026-27 Program of Studies and CTE Supplement (read in Chrome), sports fees ($100–$450, a $400 family cap without hockey), co-op hockey, reassessment rules, the science lab design (no construction money), graduates' plans, a competency transcript topic | 11 | 84 | 5 | 54 MB |
| `money-and-governance.md` | The failed $52.9 million bond (55%, needing 60%), the $32.99 million Wilkins plan for March 2027 (about $0.67 per $1,000), the 2026 rate ($17.76) after revaluation (school dollars up 7.8%), FY27 special education costs, Mont Vernon's 15.4464% share of Souhegan, the FY28 drafts, enrollment projections (K–8 down 7.8% by 2036-37), four boards, the Attorney General's electioneering letter, an electioneering topic | 11 | 65 | 5 | 60 MB |
| **Total** | | **48** | **280** | **14** | **209 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.1 million tokens, including one follow-up.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Amherst`). All 14 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 30 partial.
- **Topics:** three new topics, added to `../shared-topics.md`:
  - `competency-transcripts-and-college-admissions`: how colleges read competency-based transcripts;
  - `electioneering-by-public-employees`: New Hampshire's law on school staff electioneering;
  - `school-emergency-operations-plan-rules`: RSA 189:64's plans and drills. Earlier towns' district-safety-and-security facts give each district's own practice.
- **Places:** `district Amherst` 132, `district Souhegan Cooperative` 89, `sau 39` 26, `town Amherst` 20, no place 8, `district Academy for Science and Design Charter School` 3, `town Nashua` 1, `district The Derryfield School` 1.
- **Pending facts:** 16, mostly citing the FY28 budget drafts.
- **Raw folders:** each under 100 MB.
- **Quotes:** 667 of 808 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 tax rate, $17.76 | The town's 2026 tax rate breakdown (OCR) |
  | The FY25 bond, $52,921,828, and the 2026 plan, $32,990,000 | The Wilkins FY25/FY27 comparison sheet |
  | The portable, 1,627 to 1,551; the budget, 1,919 to 1,261 | The certified March 10, 2026 results |
  | Mont Vernon's share, 15.4464% | Souhegan's FY27 budget workbook (0.154464) |
  | The $400 family cap on sports fees | Souhegan's 2025-26 athlete handbook |

## Premises checked

| Question says | What the sources show |
|---|---|
| Portables at Wilkins | Right: approved in March 2026, 1,627 to 1,551 |
| Grade 5 moving back to Wilkins in 2028 (P2.2) | Out of date: the 2026 plan keeps grade 5 at the middle school, and it still needs a March 2027 vote |
| Early-release Wednesdays | Three a year, not weekly |
| Care open by 6:45 a.m. | None found for Clark-Wilkins; the YMCA runs care at the middle school from 7:00 |
| Different bell times | Right: 7:45–2:25 and 8:30–3:24; no reason posted |
| Kindergarten aides in every room | Partly: seven budgeted for the seven planned classes |
| A late bus (P3.3) | None on the 2026-27 route sheets |
| 5th and 8th graders mixing (P5.3) | Shared buses; separate teams, counselors and lunches inside |
| Busing to charter schools (P11.1) | None |
| Phones locked away (P6.1) | Right: Yondr pouches all day |
| Annual homeschool notice and portfolio (P13.1) | Out of date since July 1, 2026; Amherst's policy already asked for no annual notice |
| "Whole Schooling scores" (P8.1) | Work Study Practices, scored apart from grades |
| 42 students in CTE (P9.3) | Right for 2024-25; 43 in 2025-26 |
| A 30-minute bus to CTE (P9.1) | 15 to 40 minutes, depending on the center |
| An honors STEM track (P11.3) | None; Honors Challenge work within courses |
| Retakes "forever" (P14.2) | No: the grading guide allows one reassessment |
| Lab renovation soon (P14.3) | Design only; no construction money through FY2034 |
| The $52.9 million bond (P6.2) | Right: 55% yes, short of 60% |
| Three school boards (P17.2) | Four: Amherst, Souhegan, Mont Vernon and SAU 39 |
| 30% building aid | State law allows 30–60%, and none is guaranteed |
| The 2026 Attorney General letter (P17.3) | Right, per news reports; the letter itself wasn't found |
| Surplus to trust funds | Partly; some also lowers the tax rate |

## Corrections and additions to earlier files

- **Merrimack** (`../Merrimack/money-buildings-and-governance.md`): its P20.2 row said Amherst's 2026 rate wasn't found; it now points to Amherst's $17.76. No facts changed.
- **Milford and Hudson:** their counts of Souhegan students at Milford's ATC (12) and Palmer (7) are consistent with Souhegan's 43 in all.

## Library notes (for review, not applied)

- `kindergarten-day-length` 1 and `district-preschool` 3 (Amherst) still match the 2026-27 handbook. The handbook's 2:20 Clark dismissal differs from the calendar's single 2:25 time.

## Browser pass (November 21, 2026)

- **SAU 39's Simbli portal** refused the agents with a bot check, but loads in Chrome. Read:
  - Amherst's policy IHBG (revised April 16, 2026; no annual notice, and an evaluation section the July 2026 law repealed);
  - the listing dates for IHBG-RG(1) (2018) and JJJ (2019).

  Board minutes there weren't read.
- **Souhegan's Program of Studies and CTE Supplement** are Google Docs behind view-only Drive links. Their basic views were saved, and the Souhegan agent added facts from them.
- **Still not retrieved:**
  - the Attorney General's letters;
  - NH DOE's building aid rates (HTTP 403);
  - the FY28 Amherst budget workbook;
  - the staff directories and recreation lists (script pages);
  - Beaver Brook and Hampshire Hills prices;
  - Census commute times.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 9 saved bus and transportation copies (537 in all; schools, child care centers, businesses and other public places keep theirs).
- 3 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
