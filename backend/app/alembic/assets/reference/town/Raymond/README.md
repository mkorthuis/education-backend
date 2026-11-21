# Raymond: Research for Ask NH Education Facts

Cited facts and figures for answering Raymond, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the ToLoad towns. Raymond is SAU 33, a one-district SAU:
- a preschool;
- Lamprey River Elementary: K–3;
- Iber Holmes Gove Middle: grades 4–8;
- Raymond High: grades 9–12.

Students may take career programs at the Seacoast School of Technology.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-middle-school.md` | The preschool ($150 a month, at the high school), Lamprey River class sizes (about 16), before-school care ($150 a month from 7:00) and LEAP to 6:00, IHGMS doors at 7:35 and buses from 7:05, the phone and smartwatch ban, bus changes, meals ($3.60 and $3.75; reduced $0.40), counselors, the move to IHGMS, no gifted program, Algebra I in grade 8, Child Find (read in Chrome) | 11 | 49 | 1 | 15 MB |
| `raymond-high-school.md` | SST (welding, carpentry; about three of seven periods), shop realigned with MCC's manufacturing certificate, 295 students, registration and physicals, Jumpstart orientation, AP (42 exams, mean 3.30), Early College, graduates' plans, counselors (about 148 each), Seacoast Mental Health one day a week, no JROTC, football canceled for 2026, buses (6:50–6:55 arrival), SAT 993 | 10 | 70 | 5 | 36 MB |
| `support-choices-and-daily-life.md` | Paras (three short; $150,000 contracted), special education communication and transport costs, out-of-district placements, homeschool and EFA access (a per-class fee of about $3,815 under policy JFBC), VLACS in the GPA, translation, teams, no activity bus, fields in the 2028-29 capital plan, snow days (remote allowed under policy IC), bullying deadlines, open enrollment (failed 592–619), hardship transfers, military families | 12 | 85 | 4 | 32 MB |
| `money-and-governance.md` | The $32,121,915 budget and the higher default ($32,285,799), the 2025 failure, the Lamprey River replacement ($47,435,000, state aid about 30%, a vote around 2028) and the $250,000 reserve, enrollment (1,524 to 1,103), the tax cap worksheet (six positions and still $451,202 over), teacher pay below the state average, grants | 8 | 83 | 3 | 26 MB |
| **Total** | | **41** | **287** | **13** | **109 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.06 million tokens, including two follow-ups.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Raymond`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 29 full, 28 partial, 3 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Raymond` 275, `town Raymond` 9, no place 3.
- **Pending facts:** 8 cite fall 2026 minutes not yet approved.
- **Raw folders:** all under 100 MB. Bus route sheets list house-numbered stops, so only times summaries are kept.
- **Quotes:** 521 of 603 quoted passages found word for word in the raw copies.
- **Reconciled in review:** the 2026 results PDF's text layer puts Article 2's tally under Article 3, and the library's copy has the same problem. The page image shows Article 2 (open enrollment) failed 592–619 and Article 3 (the budget) passed 850–370, and the files use those figures.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026-27 budget, $32,121,915 | Board minutes, January 21, 2026 |
  | The default budget, $32,285,799 | The budget committee's public hearing slides |
  | The Lamprey River project, $47,435,000 | The construction budget estimate |
  | Open enrollment failing 592–619, the budget passing 850–370 | The 2026 second session minutes |

## Premises checked

| Question says | What the sources show |
|---|---|
| A preschool at the high school (P1.1) | Right; $150 a month |
| Lamprey River classes too big (P1.2) | No: five classes a grade, about 16 each |
| 4th graders moving to IHGMS (P4.2) | Right, since 2020-21 |
| Free meals for everyone (P4.3) | No: families apply each year |
| Early drop-off at IHGMS (P2.1) | Doors at 7:35, no supervision before, no before-school program |
| A $32.1 million budget and a higher default (P3.1) | Right: the default carried the teachers' raises and special education services the budget cut |
| $250,000 for a Lamprey River reserve (P3.2) | Created and funded; the plan is a replacement school |
| About 330 high school students (P7.1) | Out of date: 295 in September 2026 |
| JROTC (P18.1) | None |
| Running Start (P10.1) | Renamed Early College |
| Para shortages (P6.1) | Three short in September 2026 |
| Remote snow days (P16.3) | Allowed when busing is unsafe; other days are made up in June |
| A late or activity bus (P15.2) | None |
| An open enrollment vote (P17.2) | It would have admitted no one, and it failed |
| Flat enrollment and a new school (P20.2) | Enrollment fell from 1,524 to 1,103; the case rests on the 1976 building's condition |
| A personal finance class (P19.1) | An elective, covered as one topic in Economics |

## Corrections and additions to earlier files

None needed.

## Library notes (for review, not applied)

- `district-preschool` 95 says no Raymond preschool tuition is posted; the handbook gives $150 a month and a $75 deposit.
- `early-college-at-your-high-school` 5 says two free Early College courses a year. Raymond's October 2026 presentation says Manchester Community College offers up to four.
- The library's 2026 Raymond results copy has the same misplaced tally; the votes are above.

## Browser pass (November 21, 2026)

sau33.com's web pages blocked automated requests (Cloudflare), but its PDFs download directly.
- **Read in Chrome:** the handbooks, transportation and student support pages. The handbooks, calendar and bus route PDFs they link were passed to the agents, who added facts from them.
- **Still not retrieved:**
  - the policy index (policy JCA on hardship transfers);
  - the report card to the community;
  - NH DOE's building aid rank list (HTTP 403).
