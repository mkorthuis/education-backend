# Grantham: Research for Ask NH Education Facts

Cited facts and figures for answering Grantham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch. Grantham is a single-town district in SAU 75:
- **Grantham Village School** (preschool to grade 6; 235 students in October 2026, capacity 378), run by the Grantham School District, which also runs the Before School Program;
- grades 7–12 go to **Lebanon Middle School** and **Lebanon High School** under the Grantham–Lebanon–Plainfield AREA agreement (2021), with the Hartford Area Career and Technology Center for career programs; Grantham runs its own buses to Lebanon;
- Eastman, a large planned community inside Grantham, has its own village district and fees.

Lebanon's research (Lebanon Middle, Lebanon High, the AREA's terms) was already done; these files cite it and write Grantham's side. Plainfield (same AREA) is being researched in the same batch.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `grantham-village-school-and-families.md` | The Before School Program (7:30 to 8:10, $5.00 a day, not run on a delay), after-school care by The Outing Club Village and Grantham Children's Academy (no waitlist data), both preschool classes full for 2026-27 with an interest list, PickUp Patrol's 2:00 p.m. hard cutoff, K–3 children returned to school if no adult is at the stop, bus rides of 22 to 36 minutes, Alma for registration, free and reduced-price meals ($0.40 reduced lunch, free breakfast), the 2026-27 calendar | 14 | 53 | 1 | 13 MB |
| `lebanon-middle-from-grantham.md` | Grantham's three buses to Lebanon (first stops 6:17–6:55, Lebanon High at 7:05–7:07, Lebanon Middle at 7:15–7:16, then back for GVS students at 8:28), LMS's 7:30 start and Lebanon's study of changing it, Grantham staying the "LEA" for its students' IEPs, about 36 Grantham seventh graders in a grade of about 130, GVS's 2026 test results (reading 88%, math 93%) against Hanover, Lebanon and the state, policy IHBG still describing repealed homeschool steps | 14 | 40 | 1 | 3.8 MB |
| `lebanon-high-from-grantham.md` | Bus times to Lebanon High by route (including the Eastman route G6), no late or activity bus documented, what happens when Grantham closes and Lebanon doesn't (excused, work made up), the Hartford center reached in two legs (LHS buses at 8:00 and 11:00), AP prerequisites, Kimball Union Academy's $52,500 day tuition against the AREA rate, LHS's grade 11 SAT (1097 against 988 for the state and 1208 for Hanover High), the state's Youth Risk Behavior Survey | 14 | 52 | 4 | 3.3 MB |
| `money-and-governance.md` | AREA tuition lines for 2026-27 ($1,604,411 for Lebanon Middle and $2,473,688 for Lebanon High; 31.4% of the operating budget), the final 2026 rates (local school $12.45, state $1.39, $13.84 together against $14.39 projected; the whole town rate $21.40; the school share 64.7%), the 0% open enrollment vote, Question 2 (976 to 1,054; 48.1%), SAU 75's three positions and $489,101 budget, room at GVS, board agendas and public input, the bus contract, Eastman's fees ($4,501 a year for a house or condo) and the teachers' contract | 12 | 85 | 6 | 9 MB |
| **Total** | | **54** | **230** | **12** | **29 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.3 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Grantham. All 12 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 35 partial, 1 from the site's data (P2.1).
- **Topics:** one new topic, added to `../shared-topics.md`: `nh-youth-risk-behavior-survey`.
- **Places:** `district Grantham` 142, `district Lebanon` 44, `town Grantham` 25, no place 7, `sau 75` 7, `district Kimball Union Academy` 3, `town Lebanon` 1, `district Ledyard Charter School` 1.
- **Pending facts:** 5, citing draft or unapproved minutes.
- **Raw folders:** each under 100 MB. The 45 saved PDFs are handbooks, policies, a contract, the AREA agreement, a state report and state sheets; a few are scans the agents transcribed. None is a route sheet or a roster: the bus sheets are kept as cleaned copies of streets and times only.
- **Privacy:** the address scan finds only Lebanon High (195 Hanover Street), Ledyard (39 Hanover Street), Grantham Village School, Lebanon Middle, the gym where the district meeting is held and USDA's civil rights address in the meals forms. LHS's school profile lists "Recent Acceptances" as colleges, not students. Hearing and meeting copies have speakers' names and addresses removed.
- **Quotes:** 526 of 613 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The final 2026 rates: local school $12.45, state education $1.39, $13.84 together; the town's $21.40 (town $4.75, county $2.81); Eastman's village district rate of $2.34 | The superintendent's November 2026 report and the Town's tax rate page (the parts add to $21.40) |
  | The tuition budget lines of $1,604,411 and $2,473,688 | The board-approved 2026-27 budget and the FY28 draft |
  | Question 2: 976 yes and 1,054 no in Grantham (48.1%, unofficial) | The site's `town_question_two` table |
  | GVS's math proficiency of 93% (levels 3 and 4 added), 88% in reading | The board's March 2026 slides and the site's data |
  | The AREA rates of $20,309 and $19,344 | The board's March 3, 2026 slides (page 54, OCR), which call them the "current AREA Agreement" rates |

## Premises checked

| Question says | What the sources show |
|---|---|
| The Before School Program doesn't open until 7:30 (P1.1) | Correct: 7:30 to 8:10; doors locked and no staff before 7:30; Grantham Children's Academy lists 7:00 openings |
| The morning program is canceled on a two-hour delay (P1.2) | Correct, in the program page and the board-approved guidelines |
| Pre-K has a waitlist (P5.1) | Both classes are full for 2026-27; the school keeps an interest list for 2026-27 to 2028-29, not a posted waitlist |
| A driver won't release K–3 children without an adult (P8.1) | Correct: they are returned to school after the route; grade 4 and up may be dropped |
| PickUp Patrol has a 2:00 p.m. cutoff (P8.3) | Correct and a hard stop in the system; call the front office after 2:00 |
| A long bus ride (P14.2) | The longest GVS-leg ride is 33 minutes in the morning and 36 in the afternoon; rides to Lebanon Middle are about 21 to 58 minutes in the morning (derived) |
| LMS starts at 7:30 (P16.2, P18.1) | Correct; Lebanon began a study of changing LMS and LHS start times in fall 2026 |
| "Two completely different morning bus schedules" (P18.1) | Two times at one stop on the same bus: a first run to Lebanon and a second to GVS, about an hour apart |
| The bus might drop a student near Ledyard (P13.2) | The Grantham buses stop at LHS, about a mile from Ledyard; no Ledyard stop is listed |
| Grantham has an annual homeschool notice and evaluation to undo (P9.3) | Partly out of date: policy IHBG (adopted September 1, 2026) still describes them; the state repealed them July 1, 2026 |
| Lebanon charges "$20,000 to $21,000 a kid" (P3.1) | $20,309 at LMS and $19,344 at LHS for 2026-27 |
| Grantham's per-pupil cost is "so much higher than bigger towns" (P3.1) | $25,958.78 for 2024-25 against $22,699.85 statewide; Lebanon $29,144.42, Plainfield $32,881.91; DOE says to compare only districts with the same grades |
| The HB 1300 cap vote is ahead (P3.2) | Already held November 3, 2026: 48.1% yes in Grantham, short of 60% (unofficial) |
| A bus driver shortage and combined routes (P12.1) | Not found in minutes, reports or budgets; a September 2025 newsletter says "we are down to 2 buses" in explaining a change to the Unity Day hike |
| Eastman is "mostly year-round families" (P6.1) | About 65% full time in 2026 (60% in 2021), per Eastman's survey as reported by the Valley News |
| Over half the property tax goes to the school (P10.1) | Correct: 64.7% in 2026 (58.3% on an Eastman property) |
| A representative on the Lebanon School Board (P17.3) | None; one non-voting seat on each of two Lebanon committees and three joint board meetings a year |
| A late bus after practices (P11.1) | None found; the afternoon buses leave LHS at 2:33 |
| A lot of fighting over budgets (P19.3) | The 2026 minutes record the opposite: unanimous votes at four meetings and no public comment recorded; the one long session was the HB 1300 hearing (six speakers) |

## Corrections and additions to earlier files

Applied:
- **Lebanon `money-and-governance.md`, district-tuition-contracts 7:** its note said the source doesn't say whether the "2027" rates ($19,344 and $20,309) mean 2026-27 or 2027-28. Grantham's March 3, 2026 slide calls the same figures the "current AREA Agreement" rates in its analysis of its 2026-27 budget; the note now says so and that this suggests 2026-27. (It isn't a proof: the slide doesn't name the year.)

Not applied (additions for Lebanon's files):
- **district-tuition-contracts 8–9:** they count 77 Grantham students at Lebanon Middle for 2026; Grantham's annual report counts 75 on October 1, 2025 (74 from the grade rows). The dates differ.
- **District-transportation 1:** it gives LHS's day as 7:30 to 2:35 (the bell schedule page); the 2026-27 handbook says the day "officially ends for all students at 2:30 after Academic Block."
- **Middle-school file, policy JJJ:** it says Lebanon's JJJ was unreadable; Grantham's JJJ (adopted October 6, 2026) is saved in Grantham's `raw/high/`.

## Library notes (for review, not applied)

- **`gov-school-boards-and-superintendents` fact 6** says school boards must give a public comment period of at least 30 minutes (RSA 189:74). Grantham's November 17, 2026 agenda allots 10 minutes at its first public participation period, and a second period comes near the end; the second period's length isn't posted. Not necessarily a conflict.
- **`budget-hb-1300-school-tax-cap` 2–11 and `budget-question-2-2026-results`** don't list Grantham's result; the site has it (unofficial).
- **`district-practices.md`:** district-preschool 36 (Grantham) says both classes were full for 2026-27 and the school's page now also links interest forms for 2027-28 and 2028-29; kindergarten-registration 26 says no dates were posted, while the Alma instructions say current families re-enroll when Alma opens in late July or early August.
- **Site data:** the child care table lists The Outing Club Village - Grantham as not accepting the NH Child Care Scholarship, but the program's own page says it accepts NH Childcare Assistance Funding.

## Browser pass

Not done. Not retrieved:
- The board's policy folders on Google Drive (policies JF and JF-R on enrollment capacity, "Scholastic Probation Standards for Going into Seventh Grade", JJJ, IHBG, JICJ and JICK were found but not opened), the SAU's Board Meeting Materials folder past December 2025 (no 2026 minutes found), the GVS preschool handbook (sign-in), U.S. News's page for LHS, NH DHHS regional survey reports, and plainfieldnh.org (HTTP 403, for Plainfield's tax rate);
- how many children are on the Before School Program or its waitlist, whether its fee is reduced in 2026-27 (the handbook and the board-approved guidelines disagree), Outing Club and preschool waitlist lengths, a walkthrough of Alma registration, whether a child kept home by a Grantham closure may practice that day, when the Hartford buses return to LHS, and school-level survey data for LHS (not found).
