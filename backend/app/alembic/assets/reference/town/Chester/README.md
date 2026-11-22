# Chester: Research for Ask NH Education Facts

Cited facts and figures for answering Chester, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the sixth wave of the second ToLoad batch. Chester is SAU 82, a one-district SAU:
- **Chester Academy** serves preschool to grade 8.
- **High school:** students attend Pinkerton Academy in Derry under a tuition contract.

The district decides its budget at a traditional annual meeting, not a deliberative session. Pinkerton was researched in `../pinkerton/`, and the other Pinkerton towns' contracts in `../Auburn/`, `../Candia/` and `../Hooksett/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `chester-academy-early-grades-and-families.md` | Three care programs (the school's morning program from 6:45; Elite to 6:00, $22 a day; the Boys & Girls Club in Derry to 7:30), the part-day preschool by lottery ($1,600 or $2,200), scores against Hampstead and Derry (55% math in 2026), class sizes, storm plans, Title I reading help, the K–2 bus drop-off rule, full-day kindergarten | 17 | 67 | 2 | 11 MB |
| `chester-academy-upper-grades-support-and-choices.md` | Special education timelines (meeting in 15 days, evaluation in 60), Algebra I three ways (at the school, VLACS or Pinkerton), enrichment, phones off in lockers, bullying, homeschool access, no intramurals, Busche Academy, charter schools (no tuition, no Chester busing), drive distances to high school options | 13 | 90 | 2 | 10 MB |
| `pinkerton-from-chester.md` | Chester's Pinkerton students by year (311 in 2018-19; 224 in 2025-26), CTE from grade 10, no late bus found, IEPs (Chester stays responsible), fees ($99 AP exams), honors for freshmen (Honors Algebra 2 only), two Chester trustees, Early College, team cuts, Pinkerton's audited costs | 9 | 38 | 1 | 13 MB |
| `money-and-governance.md` | Local school tax dollars up 51% (2018–2025) with 9% fewer resident students, Pinkerton at 26.4% of the general fund, the 2026 rate ($17.19; school $10.71), the March 11, 2027 meeting, salaries against neighbors, a 1.7% commercial base, no debt since 2018 and a $4.8 million capital plan, administration costs per pupil, the 95% retention claim | 10 | 61 | 7 | 15 MB |
| **Total** | | **49** | **256** | **12** | **49 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.97 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Chester`). All 12 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 32 partial, 1 from the site's data. P18.2, bus ride lengths, waits on the route sheets (see Browser pass).
- **Topics:** no new topics.
- **Places:** `district Chester` 223, `town Chester` 24, `district Pinkerton Academy` 9.
- **Pending facts:** 7, citing draft minutes and the 2027-28 draft budget.
- **Raw folders:** each under 100 MB.
- **Privacy:** the main session removed 85 residents' house numbers from public comment in the saved minutes and the 2026 annual report text, and deleted the minutes and annual report PDFs. Two citations now point to the text copies. The address scan finds only the school, the town hall and other schools. Later, the main session also removed graduates' names (Chester Academy and Pinkerton) from the saved 2026 annual report text.
- **Quotes:** 542 of 683 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $17.19, and school $10.71 | The town's property tax page |
  | Durham School Services named in board minutes | The September 3, 2025 minutes |

## Premises checked

| Question says | What the sources show |
|---|---|
| Care with a waitlist (P1.1) | Three programs; no waitlist posted |
| A full-day public preschool (P1.2) | No: part-day, by lottery |
| Thin staffing in the elementary grades (P4.2) | Average classes 16.5–18.5 |
| Paras short (P5.3) | Partly: one opening posted |
| Algebra I counting at Pinkerton (P9.3) | Yes, three ways |
| Intramurals (P9.1) | None found |
| Charter tuition and busing (P19.3) | No tuition; no Chester busing |
| Welding as a freshman (P2.1, P20.2) | From grade 10 |
| A late bus (P2.2) | None found |
| A 3,200-student school (P2.3) | High: 2,988 |
| The IEP starting over (P5.2) | No source says so |
| Freshman honors (P6.3) | Honors Algebra 2 only |
| Chester follows Derry (P11.2) | Pinkerton has its own trustees, two from Chester |
| Taxes up, enrollment flat (P3.1) | Partly: dollars up 51%, students down 9% |
| A deliberative session (P3.3) | None: a traditional meeting |
| Lower teacher pay (P6.1) | Mixed |
| Almost no commercial base (P8.1) | Correct: 1.7% |
| A roof or HVAC bond (P8.2) | None |
| High administration costs (P8.3) | Partly |

## Corrections and additions to earlier files

- **Derry** (`../Derry/`): its Boys & Girls Club hours (2:00–7:30) are for Derry's schools. The Chester Academy flyer gives 3:00–7:30.
- **Pinkerton** (`../pinkerton/`): its file counts four freshman counselors; the 2026-27 parent night slides list an assistant director and five.
- **Hooksett** (`../Hooksett/`): a board chair's statement there gives a 10% cap in Auburn's and Chester's contracts; Auburn's agreement says 5%. Chester's contract isn't posted.
- **Bus company:** Chester Academy's 2026-27 route sheets (September 4, 2026) say First Student; board minutes from September 2025 name Durham School Services. Unresolved.

## Library notes (for review, not applied)

- **`district-preschool` 15** says Chester posts no tuition, schedule or eligibility. The registration page and lottery application give them now.
- **`budget-form-and-vote-dates` 18 (Chester):** a traditional annual meeting; 2026 on Wednesday, March 11, and 2027 on Thursday, March 11.

## Browser pass

SAU 82's sites list their files through Google Apps Script frames that only a browser runs. The main session opened them in Chrome and saved four route sheets, house numbers removed (`raw/README-browser.txt`):
- Chester Academy's 2026-27 AM and PM routes (7 each way), in `raw/elementary/browser/`;
- Chester's Pinkerton routes (5 morning, 4 afternoon; first pickups about 6:02), in `raw/high/browser/`.

Not retrieved:
- the Budget page's file frame (empty in Chrome), policies, and minutes after February 2026;
- NH Employment Security and NH DRA (HTTP 403).
