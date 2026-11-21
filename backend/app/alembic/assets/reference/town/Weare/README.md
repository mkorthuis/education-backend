# Weare: Research for Ask NH Education Facts

Cited facts and figures for answering Weare, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the ToLoad towns. Weare is in SAU 24:
- **The Weare School District** runs Center Woods School (preschool to grade 3) and Weare Middle School (grades 4–8).
- **The John Stark Regional School District** (Weare and Henniker) runs John Stark Regional High School (grades 9–12). Its students may take career programs at the Concord Regional Technical Center (CRTC).

Henniker has no research of its own; facts about John Stark and SAU 24 serve both towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `center-woods-and-early-grades.md` | Care (New Morning at Center Woods, 6:45–6:00, $11 and $22 a day; the Boys & Girls Club at Weare Middle from 6:30), bus routes (pickups 7:12–7:47, rides of 24–52 minutes, a dirt-road stop), the preschool (half day, mainly for special needs; $200 a month for others), full-day kindergarten since 2022 (940–714), grades 4–5 merged into Weare Middle in 2022-23, start times (7:20 and 8:30), meals, medication rules, a homework research topic | 12 | 83 | 4 | 42 MB |
| `middle-and-high-school.md` | Phones banned all day, the 40-minute flex block and competency retakes, CRTC seats (35 funded; 76–79 applicants for 17–18 first-year spots; a $111,000 article), eight shop courses on campus, AP and dual enrollment against Bow and Goffstown, the Tuesday 5:15 late bus, the 9th grade transition | 10 | 75 | 8 | 28 MB |
| `support-choices-and-safety.md` | 45 paraeducators, IEP and therapy questions, homeschool and EFA access (John Stark's $2,500-a-course EFA policy), gym priorities, bullying policies from 2013, the 2022 civil rights complaints at John Stark, security grants ($40,000 and $100,000), no school resource officer, drills, the parent portal | 10 | 88 | 0 | 28 MB |
| `money-and-governance.md` | The 2025 local school rate split ($9.77 Weare, $5.23 John Stark), Weare's 68.14% of John Stark's costs (1985 agreement), the 2026 failed budgets and contracts (both on defaults), open enrollment articles (1% in, 0% out), the SAU 24–SAU 34 shared-services agreement (not a merger), teacher turnover and open positions, the SAU office's $45,000 rent in Henniker | 10 | 79 | 6 | 64 MB |
| **Total** | | **42** | **325** | **18** | **162 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.21 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Weare`). All 18 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 31 full, 28 partial, 1 from the site's data.
- **Topics:** one new topic, `research-homework`, added to `../shared-topics.md`. The library's `recess-activity-and-homework-rules` has the rules.
- **Places:** `district Weare` 162, `district John Stark Regional` 118, `sau 24` 25, `town Weare` 11, no place 6, `district Bow` 2, `district Concord` 1.
- **Pending facts:** 2. Both notes quote board documents that use the word "draft".
- **Raw folders:** each under 100 MB.
- **Quotes:** 646 of 750 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Full-day kindergarten, 940 to 714 | SAU 24's 2022 annual report |
  | Weare's 68.14% of John Stark's costs | SAU 24's 2025 annual report |
  | The $9.77 Weare share of the school rate | Weare's revenue sheet and deliberative session |
  | The $111,000 CRTC seats article | John Stark's 2026 deliberative session and hearing |

## Premises checked

| Question says | What the sources show |
|---|---|
| 4th graders at Weare Middle (P2.1) | Right: grades 4–5 merged into a 4–8 school in 2022-23 |
| Full-day preschool for everyone (P11.1) | No: half day, mainly for children with special needs |
| Free lunch for everyone (P17.2) | No: paid prices, and families reapply each year |
| A doctor's note enough for medication (P17.3) | Also a signed parent request and a pharmacy-labeled bottle |
| Door time on a two-hour delay (P11.3) | Not posted; 10:30 by calculation, and pre-K is cancelled |
| Buses on unplowed roads (P14.2) | No source; one stop moves in winter |
| Different start times (P20.1) | Right: 7:20 and 8:30; no reason written down |
| Phones banned at lunch and passing time (P2.3, P10.2) | Right |
| A 40-minute rule (P10.1) | A 40-minute flex block, with retakes within about two weeks |
| No shop on campus (P6.3) | Wrong: eight courses in 2026-27 |
| Half the day at the CRTC (P6.2) | About 2½ hours, travel included |
| A Tuesday late bus (P19.3) | Right: 5:15 p.m., four stops |
| A WMS late bus (P8.1) | None found |
| Aides pulled to cover classes (P5.1) | No source either way |
| Fees (P8.3) | No amounts posted |
| The John Stark harassment case (P15.3) | The 2022 civil rights complaints, per news reports |
| A school resource officer (P16.1) | None found |
| An open enrollment article (P9.1) | Both districts passed one in 2026 |
| Merging with Hillsboro-Deering (P9.3) | A non-binding agreement to explore shared services, not a merger |
| The SAU office in Henniker (P14.3) | Rented, $45,000 a year |
| Rejected contracts (P20.2) | Both contracts and budgets failed in 2026 |

## Corrections and additions to earlier files

- **Concord** (`../Concord/high-school-and-pathways.md`, cte-center-programs 15): it mentions two districts that capped CRTC seats without naming them. John Stark is one (cte-center-programs 2 here). Not changed.

## Library notes (for review, not applied)

- `district-preschool` 115 says Weare's site doesn't describe the preschool. The handbook and June 2026 minutes now do (district-preschool 1–3 here).
- `kindergarten-entry-cutoff` 110 quotes the registration page ("by September 30th"); policy JEB says "before September 30".

## Browser pass

The agents' blocked pages were:
- the town's sites (weare.nh.gov and wearenh.gov), so the 2026 tax rate and the March 2026 CRTC article's result are missing;
- NH DOE's 2026-27 enrollment by grade;
- the state's 2022 release on John Stark.

The Weare School Board's public Drive folder covered minutes and policies through June 2026. Later minutes are on Simbli and weren't read.
