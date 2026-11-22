# Nottingham: Research for Ask NH Education Facts

Cited facts and figures for answering Nottingham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the seventh wave of the second ToLoad batch. Nottingham is SAU 107, a one-district SAU since it left SAU 44 in 2022:
- **Nottingham School** serves preschool to grade 8.
- **High school:** families choose Coe-Brown Northwood Academy or Dover High (with Dover's career center), under contracts with each.

The district votes by official ballot. Coe-Brown was researched in `../Barrington/`, `../Deerfield/` and `../Northwood/` (alongside this town), Dover High in `../Dover/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `nottingham-school-early-grades-and-families.md` | The preschool (its own site says lottery; the main page says first come, first served), full-day kindergarten, no school-run before- or after-school care (supervision from 7:45), bus rides (up to 55 minutes in the morning), the driver shortage and "Plan B" routes, dyslexia screening, Title I reading help, lunch $3.15, no grace period for a mid-year move | 12 | 54 | 1 | 5 MB |
| `nottingham-school-upper-grades-support-and-choices.md` | No shop class (technology classes with robots and 3D printing), eighth grade algebra by a prognosis test, one nurse and two counselors, therapists in the building, policy JJJ for homeschool and EFA students (27 homeschooled children counted), the bullying policy, the phone ban, no world language in the school day | 10 | 75 | 1 | 11 MB |
| `high-school-choice.md` | Where students go (137 at Coe-Brown and 79 at Dover, October 2026), the new Coe-Brown agreement (IEP case management at Coe-Brown, Nottingham at every IEP meeting), the 8th-grade steps, bus times (Dover's first stop 5:56 a.m.), no late bus, calendars, fees, Coe-Brown's 2024 report on Nottingham students | 9 | 56 | 7 | 15 MB |
| `money-and-governance.md` | Leaving SAU 44 (the plan's "at least $157,891" a year of savings against FY2025 costs of $712,505), the school levy up 46% from 2018 to 2025, Dover's rate ($22,720.93, up 11.12%) against Coe-Brown's ($21,617), Question 2 (57.2%, short of 60%), the crowded building and NESDEC's projection, the board | 9 | 51 | 7 | 13 MB |
| **Total** | | **40** | **236** | **16** | **44 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.84 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Nottingham`). All 16 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 35 full, 23 partial, 2 from the site's data.
- **Topics:** no new topics. Nottingham is added to the library's `kindergarten-day-length`.
- **Places:** `district Nottingham` 223, `town Nottingham` 8, `district Coe-Brown Northwood Academy` 3, `district Dover` 2.
- **Pending facts:** 20, citing draft budgets, the draft capital plan and draft minutes.
- **Raw folders:** each under 100 MB. Bus copies keep only times and street names; the original route sheets weren't saved. The 2020 SAU planning report is cited from Northwood's raw folder (`../Northwood/raw/money/`).
- **Privacy:** the address scans find only Nottingham School and Dover High.
- **Quotes:** 542 of 713 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Dover's 2026-27 rate estimate, $22,720.93 | Dover's rate sheet in the December 17, 2025 board packet |
  | FY2025 central costs, $712,505 (**derived**: $514,348 + $198,157) | The 2026-27 MS-27 |
  | The 2020 plan's savings, "at least $157,891" | The November 2020 SAU planning report |

## Premises checked

| Question says | What the sources show |
|---|---|
| A preschool lottery and waitlist (P1.1) | Yes, though the main Pre-K page says first come, first served |
| Long rides from the lake (P1.3) | Partly: 43+ minutes; other routes are longer |
| After-school care at the school (P3.3) | None run by the school |
| Care from 6:30 a.m. (P6.1) | Not at the school; supervision from 7:45 |
| Free meals for all (P11.1) | No |
| No buses on dirt roads (P15.1) | Not settled; one route uses a gravel road |
| An ESL teacher (P19.1) | None listed |
| Shop classes (P2.3) | None; technology classes instead |
| Yearly homeschool portfolios (P9.3) | Out of date since July 1, 2026 |
| World language (P14.1) | None in the school day |
| Tuition fully covered for Dover (P2.1) | Mostly; no separate career center charge found |
| The Dover bus earlier (P2.2) | Correct: 5:56 a.m. against 6:25 and 6:32 |
| The Coe-Brown bus home later (P16.1) | No; the Dover bus is the late one |
| A lock-in date (P5.1) | No single deadline |
| Oyster River as an option (P8.3) | Only at the family's cost |
| A late bus (P13.2) | None |
| Leaving SAU 44 saved money (P4.1) | Costs now exceed the plan |
| About 520 students (P4.2) | 527, plus about 216–240 high schoolers |
| Roof and septic articles every year (P12.1) | Not in 2026; reserve deposits from surplus |
| About $18,500 per pupil (P15.2) | Correct: $18,527, without tuition and buses |
| Caps on tuition increases (P18.1) | No percentage cap |

## Corrections and additions to earlier files

- **Northwood** (`../Northwood/`): its SAU history quotes the 2020 plan's expectation that a single-district SAU would cost "significantly less". Nottingham's actual costs are here (district-sau-governance 4–6).
- **Barrington and Deerfield:** their files give the sending district the final say on IEPs at Coe-Brown. Nottingham's 2026 agreement gives the IEP team the final say.
- **Barrington** (`../Barrington/`): its table shows Dover's 2025-26 per-pupil figure as $19,965.73. Dover's rate sheet for Nottingham gives $20,447.87, so Dover figures the two towns' rates differently.

## Library notes (for review, not applied)

- **`places.yaml` (Nottingham–Coe-Brown):** it ends the contract June 30, 2037, from the warrant. The agreement's own text runs July 1, 2026 to June 30, 2036, ten years, with a three-year renewal.
- **`district-preschool` 86 (Nottingham)** matches the preschool's own site, but the school's main Pre-K page says peer-model places are first come, first served.
- **No statewide rule fact covers capital reserve funds** (RSA 35:1, 35:15). This town's facts quote them in a note.

## Browser pass

Not needed for the answers. Not retrieved:
- the Town of Nottingham's website (a bot check), for the March 2026 vote counts, the tax-cap petition result and the 2021 SAU vote;
- the Dover–Nottingham contract in NH DOE's State Board materials (HTTP 403);
- the Southeast League's schedules (the linked site now redirects elsewhere).
