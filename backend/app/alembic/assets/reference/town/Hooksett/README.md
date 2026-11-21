# Hooksett: Research for Ask NH Education Facts

Cited facts and figures for answering Hooksett, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the ToLoad towns. Hooksett is in SAU 15 with Auburn and Candia. The Hooksett School District runs:
- Fred C. Underhill School: preschool to grade 2;
- Hooksett Memorial School: grades 3–5;
- David R. Cawley Middle School: grades 6–8.

Hooksett has no high school. Most students attend Pinkerton Academy under a tuition contract, and families may petition for other contracted schools. Pinkerton's own facts are in `../pinkerton/` and the Derry, Hampstead and other files.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `underhill-and-memorial.md` | Full-day kindergarten (9:00 to about 3:15), New Morning care at Underhill 7:00–6:00 ($11 and $22 a day; Memorial bused over), the preschool (a February lottery; $200 or $100 a month), special education staffing, First Student (15 buses, rides up to 69 minutes), translation, child care openings | 10 | 64 | 0 | 37 MB |
| `cawley-and-home-education.md` | Grade teams and hallways, phones off in lockers or backpacks, math levels and Algebra I, counselors (about 221 students each), 504 plans, the new access policy JJJ (adopted 4–3 on November 17, 2026; covers EFA students), home education since July 2026, the bullying policy rewrite, enrollment by race | 12 | 81 | 2 | 34 MB |
| `high-school-choice-and-pinkerton.md` | The 2022–2032 Pinkerton agreement (63% of each class), petitions to seven other schools and their caps, 613 high schoolers by school, buses (5:57–6:41 pickups, none home after 2:00), Hooksett's graduation rate at Pinkerton (92.37%), AP results, IEPs, VLACS, storm delays | 10 | 71 | 8 | 63 MB |
| `money-and-governance.md` | The $45,851,643 budget, the school tax cap (4,275 to 2,215), SchoolCare's 23% quote for 2027-28, Pinkerton tuition and its capital share ($2,443 of $16,924), SAU 15's cost split (about 58%), the 2027 deliberative session (January 30) and vote (March 9), past cuts | 9 | 83 | 7 | 59 MB |
| **Total** | | **41** | **299** | **17** | **193 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.03 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Hooksett`). All 17 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 37 full, 21 partial, 2 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Hooksett` 260, `district Pinkerton Academy` 17, `town Hooksett` 12, `sau 15` 9, no place 1.
- **Pending facts:** 12.
- **Raw folders:** each under 100 MB.
- **Quotes:** 582 of 705 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, matched):

  | Fact | Checked against |
  |---|---|
  | The 2026-27 budget, $45,851,643 | The district's HB 1300 guide |
  | The tax cap vote, 4,275 to 2,215 | The town's transcribed November 3, 2026 return |
  | Pinkerton's FY2025 cost, $16,924 | Pinkerton's 2025 financial narrative |
  | Preschool tuition, $200 a month | The preschool FAQ |
  | Hooksett's Pinkerton graduation rate, 92.37% | The October 20, 2026 board packet (read from the page image) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Half-day kindergarten | No: full day |
| A pre-K lottery | Right, for children without an IEP |
| Care inside Memorial | No: at Underhill, with a bus between schools |
| Different start and end times | Both start at 9:00; dismissal 3:15 and 3:25 |
| Staff shortages | Mostly fully staffed; one para short at each school |
| A two-year daycare waitlist | Not supported: 12 of 14 programs reported openings |
| Phones locked away | No: off in lockers or backpacks |
| Honors tracks at Cawley | None; three math levels in grade 8 |
| Yearly homeschool paperwork | Out of date since July 1, 2026 |
| Locked into Pinkerton for free | Partly: petitions to other schools, with parents paying any difference |
| A 6:15 bus and a late bus | Pickups 5:57–6:41; no late bus |
| Over 3,000 at Pinkerton | 2,988 in grades 9–12 |
| A 23% insurance increase | SchoolCare's quote for 2027-28, not yet billed; 3.75% in 2026-27 |
| A town tax cap | A school tax cap, adopted November 3, 2026 |
| A $45 million budget | Right: $45,851,643 |
| Tuition not paying for Pinkerton's buildings | No: tuition includes capital and debt |
| More than its share of SAU 15 | No: about 58%, close to its shares of students and value |

## Corrections and additions to earlier files

None needed. Goffstown's brief (not its facts) says Hooksett pays Goffstown "Pinkerton's rate". The Goffstown memorandum sets tuition near New Boston's rate, and Goffstown's facts already say so.

## Library notes (for review, not applied)

- `district-preschool` 47 says Hooksett's preschool tuition isn't stated. The FAQ posts $200 a month (four days) or $100 (two days).

**Brief year labels:** the brief called the site's 2026 enrollment 2026-27. It is the 2025-26 count, as the money agent found.

## Browser pass

The agents' blocked pages were:
- the "State of our Hooksett Schools" leaflet (its content is in the 2026 Voter Guide, which was used);
- the 2025 deliberative session minutes;
- NH DRA's 2026 tax rates;
- the ALPs site (sign-in).

None is essential to the answers.
