# Stratham: Research for Ask NH Education Facts

Cited facts and figures for answering Stratham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the ToLoad towns. Stratham is in SAU 16:
- **The Stratham School District** runs Stratham Memorial School (preschool to grade 5) and decides its budget at a traditional annual meeting.
- **The Exeter Region Cooperative** (Cooperative Middle School, Exeter High and the Seacoast School of Technology) votes by official ballot. It's researched in `../Exeter/`; the files here add Stratham's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `stratham-memorial-and-families.md` | The 8:25–3:05 day and care, First Student, Infinite Campus (replaced ALMA), Fishtank reading (adopted June 2026), the Special Education Suite, reading and math help (69 children), IEP contacts, Gifford Farm Road and Safe Routes, Responsive Classroom (with a research topic), meals and quiet help, PickUp Patrol by 1:30, the preschool (mixed, tuition, Stratham children only), the cutoff and registration | 15 | 80 | 1 | 23 MB |
| `cms-for-stratham.md` | Stratham's 27% of CMS's 5th graders, their scores, the 7:25 start, the late bus (one Stratham stop), the vaping night, Infinite Campus at CMS, math placement into EHS, counselors, home education (policy revised October 2026) | 9 | 32 | 2 | 41 MB |
| `exeter-high-and-sst-for-stratham.md` | Canvas and calling out, freshman classes, SST's Electrical program and licensing, sports at EHS and SST, Early College ($150, two free), AP comparisons (no pass rates published), tryouts and eligibility, costs, internships, the calendar for employers | 9 | 42 | 2 | 17 MB |
| `money-and-governance.md` | The $14.50 rate and the $11,961,745 bond, leftover bond money ($860,000 for windows and flooring), the split between Stratham and the cooperative (51.4% and 48.6% in 2025), the elderly exemption, HB 1300, two budget processes, state aid ($4,873 per student), SAU 16 costs, which board decides what | 8 | 80 | 8 | 33 MB |
| **Total** | | **41** | **234** | **13** | **114 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.97 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Stratham`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 30 partial. P10.2 and P11.1 rest on Exeter's files; P16.2 is answered wholly by them.
- **Topics:** one new topic, `research-classroom-behavior-approaches` (research on approaches like Responsive Classroom). It's added to `../shared-topics.md`, retitled from Responsive Classroom alone.
- **Places:** `district Stratham` 133, `district Exeter Region Cooperative` 58, `town Stratham` 26, `sau 16` 11, no place 6.
- **Pending facts:** 16 cite draft minutes (the Stratham board's October 21, 2026 meeting and others).
- **Raw folders:** all under 100 MB.
- **Quotes:** 467 of 575 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, matched):

  | Fact | Checked against |
  |---|---|
  | The bond, $11,961,745 | The 2026 annual meeting presentation (OCR) |
  | The 2026 tax rate, $14.50 | The town's November 2026 tax rate announcement |

## Premises checked

| Question says | What the sources show |
|---|---|
| An 8:25–3:05 day (P1.1) | Right |
| Buses late or combined (P1.2) | No record of either |
| A special services wing (P3.1) | A Special Education Suite from the summer 2026 renovation |
| Summer 2027 work left (P4.1) | Right; camp at the school wasn't affected in 2026 |
| Responsive Classroom (P4.3) | Right; research on it is in the new topic |
| A 500-student elementary school (P6.1) | About right: 498 in 2024-25 |
| A 7:25 start at CMS (P6.2) | Right; buses unload at 7:00 |
| A late bus to Stratham (P7.1) | Yes, one stop at the Municipal Center |
| Canvas at EHS (P9.1) | Right |
| SST's new Electrical program (P10.1) | Right; no college credit or certifications listed yet |
| Running Start (P11.2) | Renamed Early College |
| AP scores against Portsmouth and Winnacunnet (P11.3) | Not possible: no pass rates are published, and Portsmouth High dropped AP |
| The $14.50 rate and an $11.96 million bond (P13.1) | Right |
| Leftover bond money on windows and flooring (P13.2) | Largely right: about $860,000 of a projected $1.8 million surplus |
| Two budget votes by official ballot (P14.3) | Two processes: a traditional meeting for Stratham, a ballot for the cooperative |
| Yearly homeschool paperwork (P16.1) | Out of date; the revised policy asks for notice only on withdrawal or to use programs |
| A public preschool only for special needs (P19.1) | No: mixed, with tuition, for Stratham children |
| Small state aid (P20.2) | $4,873 per student against $7,078 statewide |

## Corrections and additions to earlier files

- **Exeter** (`../Exeter/elementary-schools-and-families.md`, district-curriculum-and-assessment 6, placed `district Stratham`): its note now says Stratham Memorial adopted Fishtank in June 2026, so the Units of Study description is out of date. Exeter is loaded locally, so it was re-synced.
- **Exeter's CMS and EHS files:** this research adds to them (the CMS assistant principal's teams, the Canvas pairing code, EHS's team list). The facts here are placed `district Exeter Region Cooperative`.

## Library notes (for review, not applied)

- `district-preschool` 107 says Stratham Memorial's preschool pages give no schedule, eligibility or tuition. The 2025-26 flyer does: five days, $2,700 or $3,800.
- `budget-form-and-vote-dates` 131 is consistent; the money file adds what happens at the meeting.

## Browser pass

No pages important to these questions refused the agents. The missing pieces aren't posted:
- the 2026 school rate split between the two districts;
- the November 18 board decision on the remaining surplus;
- CMS bus route sheets.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 5 saved bus and transportation copies (11 in all; schools, child care centers, businesses and other public places keep theirs).
