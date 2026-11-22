# Henniker: Research for Ask NH Education Facts

Cited facts and figures for answering Henniker, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the second ToLoad batch. Henniker is in SAU 24:
- **The Henniker School District** runs Henniker Community School (HCS), preschool to grade 8.
- **The John Stark Regional School District** (Henniker and Weare) runs John Stark Regional High School in Weare (grades 9–12). Its students may take career programs at the Concord Regional Technical Center (CRTC).

Both districts decide their budgets by official ballot. John Stark was already researched in `../Weare/`; these files cite Weare's facts by topic and number and add Henniker's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `hcs-early-grades-and-families.md` | The half-day inclusive preschool ($275 a month; $150,000 approved 244 to 189 in 2023), the kindergarten cutoff, the 2:25–2:35 dismissal, White Birch's care at HCS (after-care to 5:30, vacation weeks), the four bus routes (pickups from 6:51; seven stops on unpaved roads), storm calls, math grouping, scores against Hopkinton and Bow, meals, ParentSquare, infant care | 14 | 67 | 1 | 18 MB |
| `hcs-middle-support-and-choices.md` | Grades 5–8 inside a preschool-to-8 building, the ski team, no grade 7–8 Algebra I (VLACS instead), homeschool and EFA access (JJJ; $2,500 a course for EFA students), co-ops, HCS's own speech-language pathologist, IEPs moving to John Stark, the Student Success Center, the bell-to-bell phone and smartwatch ban, music | 14 | 76 | 0 | 42 MB |
| `john-stark-from-henniker.md` | Getting into the CRTC (about 76 applicants for 17–18 seats), NEC courses for seniors, the four AP courses running in 2026-27 and AP results, VLACS in summer, the closed alternative program, Henniker's morning buses (6:51 at the earliest), parking, the Tuesday late bus, the math–reading gap | 8 | 40 | 4 | 3 MB |
| `money-and-governance.md` | The 2025 school rate ($13.97: Henniker $9.64, John Stark $4.33), the $195,265 aid drop, Henniker's share of John Stark (31.86% of costs, 31.56% of students), Tuesday ballot voting, the 2026-27 budget ($11,186,252, +2.98%), the teachers' contract, the elderly exemption | 7 | 42 | 2 | 59 MB |
| **Total** | | **43** | **225** | **7** | **122 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.95 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Henniker`). All 7 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 33 full, 26 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Henniker` 144, `district John Stark Regional` 48, `town Henniker` 21, `town Weare` 2, `sau 24` 2, no place 8.
- **Pending facts:** 1, citing draft minutes.
- **Raw folders:** each under 100 MB. The bus sheets list stops by house number, so only times and street names are kept. A volunteer's personal email was removed from one saved page.
- **Quotes:** 553 of 627 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Preschool at $275 a month | The June 4, 2025 board minutes |
  | The 2023 preschool article, 244 to 189 | SAU 24's 2023 annual report |
  | Henniker's John Stark share, 31.86% of costs and 31.56% of students | SAU 24's 2025 annual report (proration table) |
  | The earliest morning pickup, 6:51 | The 2026-27 HCS bus routes |

## Premises checked

| Question says | What the sources show |
|---|---|
| Not enough pre-K spots (P1.1) | Can't be confirmed: 18–19 children each October; no capacity or waitlist posted |
| A September 30 kindergarten cutoff (P1.2) | Right, with rare early entry after a district evaluation |
| Bus stops on a dirt road in the dark (P2.3) | Right for some: seven active stops on unpaved roads; 42 of 82 timed stops before the winter sunrise |
| PowerSchool as the parent portal (P11.1) | Partly: report cards now come through ParentSquare |
| Years-long infant care waitlists (P15.3) | Not shown |
| A $300 ski club fee (P3.2) | No fee posted |
| An 8th-grade math track that "locks kids in" (P5.3) | No such track; HCS offers no grade 7–8 Algebra I class, and students may take it through VLACS |
| A shared SAU speech therapist (P8.1) | HCS has its own |
| A sensory room (P17.2) | None described; the Student Success Center is the posted space |
| CRTC construction or electrical (P4.1) | Construction Trades, whose first year covers electrical and plumbing |
| NEC courses for a 10th grader (P5.1) | Seniors only, tuition-free and space-available |
| Henniker pickups at 6:30 (P14.1) | The earliest is 6:51 |
| A parking lottery (P14.2) | None: seniors first |
| A late bus back to Henniker (P14.3) | Tuesdays only, at 5:15 |
| School taxes "nearly 60%" of the bill (P6.1) | 57.9% in 2025 |
| Voting on a Saturday (P13.2) | No: the school budget is a Tuesday ballot; Saturday is the town meeting |
| Weare controls John Stark (P6.2) | Largely right on votes: Henniker casts about a quarter of the ballots |

## Corrections and additions to earlier files

- **Weare** (`../Weare/`): nothing contradicts it. Henniker's files add:
  - John Stark's AP results through 2026, and that only four of the six AP courses Weare's file lists actually run in 2026-27;
  - NEC's terms (principal or counseling approval; only courses without prerequisites; a $75 fee in the 2024 accreditation report);
  - the 1985 board's 2–2–1 seats as a fact;
  - that SAU 24's 2023 "State" SAT baselines match the state's all-grades proficiency, not grade 11's.
- **SAU 24's storm call:** the HCS handbook says announcements come "by 7 AM", while the SAU page says before 6:00 a.m. when possible.

## Library notes (for review, not applied)

- **`district-preschool` 42** says Henniker's site doesn't describe its preschool. The handbook and the June 4, 2025 minutes now do.
- **The kindergarten day-length gap for Henniker** is filled (kindergarten-day-length).

## Browser pass

Not needed for the answers. The agents' blocked pages were:
- the Town of Henniker's site and Pats Peak (HTTP 403);
- John Stark's Simbli policy manual (a bot check);
- the PTA and FinalForms pages (need a sign-in);
- NH DRA's exemptions survey.

The board's minutes after June 2026 are on Simbli and weren't read.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- 5 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- House numbers of home stops removed from quotes in the research files.
