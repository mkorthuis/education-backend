# Milford: Research for Ask NH Education Facts

Cited facts and figures for answering Milford, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. They arrived labeled "Milton NH," but every profile describes Milford. The research is in the four files below, in the reference library's format, ready to load but not loaded.

Gathered November 16–17, 2026, alongside Hampton and Exeter. Milford is SAU 40, a one-district SAU:
- **Early years and elementary:** the MEEE preschool, Jacques Memorial (K–1) and Heron Pond (2–5).
- **Middle and high school:** Milford Middle (6–8) and Milford High (9–12), with the Applied Technology Center, a regional career center.

Mason sends its grades 6–12 on tuition. The district votes by official ballot.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools-and-daily-life.md` | MEEE sign-up (no waitlist posted), full-day kindergarten at Jacques (out at 2:40), class sizes (15 in K, 16 in grade 1), the two-building split, gifted services for "selected students," grades 3–5 results against Amherst and Hollis, 95 Group phonics and Eureka Math², bell times, delays, fees, registration and immunization papers, a nurse in every school, meals, the Boys & Girls Club's before-school care and vans, reading help | 15 | 76 | 2 | 41 MB |
| `middle-high-and-atc.md` | ATC programs and enrollment by program (waitlists in Carpentry, Culinary and Health Science), welding in Precision Machining (auto and electrical at Nashua's center), the failed CTE bond, AP courses actually run (6 of 11 in 2025-26), dual enrollment, guidance and scholarships, the class of 2026's plans, ATC classes for homeschool and EFA students, middle school phones and bullying (the HB 131 rewrite), athletics and fundraising, the arts, team cuts, employer links | 10 | 90 | 4 | 27 MB |
| `student-support-and-choices.md` | The Office of Special Services and paras, Project DRIVE at the Bales building (no "Sage School"), its referral steps and the plan to move it to 119 West Street, special transportation, Talking Points translation, English learners, clubs and tutoring, home education and EFA access, students by race and ethnicity, credit recovery, social workers in every building, no late bus, one SRO | 8 | 71 | 1 | 32 MB |
| `money-buildings-and-staff.md` | The $52.7 million budget (passed 1,880 to 872), the 35% health insurance rise and 9.85 position cuts, Question 2 (58.9%), spending against results, the school rate on full value ($10.56, near Amherst's), default budgets, enrollment (2,339 to 1,904) and NESDEC's projection, ATC tuition and the state's 50–75% construction aid, teacher pay against Amherst and Bedford, the board and Budget Advisory Committee, five failed bonds since 2023 | 12 | 80 | 7 | 31 MB |
| **Total** | | **45** | **317** | **14** | **131 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.99 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Milford`). All 14 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 35 full, 23 partial, 2 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Milford` 301, `town Milford` 13, no place 3. The three no-place facts are the state's CTE construction and tuition rules (`cte-admission-and-cost-rules`); they agree with the library's `state-issues.md`.
- **Places for the backend:** the Mason row in `places.yaml` now notes that a new tuition agreement is one of the Milford board's 2026-27 goals. The contract's text and term still weren't found. The change is uncommitted.
- **Pending facts:** 21 facts cite board minutes still posted as drafts (September 8 and October 19, 2026), or college credit listed as pending. Check them before loading.
- **Raw folders:** all under 100 MB.
- **Quotes:** 724 of 923 quoted passages found word for word in the raw copies. The misses checked were line-numbered minutes, OCR and quotes saved in another agent's folder.
- **Reconciled in review:** the money file said a recount confirmed the CTE bond's failure, while the high school file found only that a recount was scheduled. The recount (1,626 to 1,130, still short) comes from a selectman's blog. The board's March 16 minutes confirm one was set, and the high school file's question row now gives the result.
- **Sources:** the district removed its 2026 election news page. The vote counts come from the district's own results PDF and the selectman's blog, which match.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Operating budget $52,722,151, passed 1,880 to 872 | The district's results (as captured April 5, 2026) and the selectman's results post |
  | CTE bond 1,629 yes (59.0%), 27 short; recount 1,626 to 1,130 | The district's results PDF; the selectman's post; board minutes, March 16, 2026 |
  | Default budget $52,996,931, $399,780 above the proposed budget | Board minutes, January 13, 2026 |
  | A goal to buy 119 West Street for Project DRIVE | Board minutes, September 8, 2026 (draft) |
  | Boys & Girls Club before-school care, $195 a month | The Club's 2026-27 fee sheet |

## Premises checked

| Question says | What the sources show |
|---|---|
| An MEEE waitlist (P1.1) | None posted; 2026-27 sign-ups opened February 1 and closed when full |
| Kindergarten full- or half-day (P1.2) | Full-day, out at 2:40; some older policy text still says half-day |
| Why two elementary buildings (P3.1) | No reason given; Jacques is called the entry school |
| A real gifted program (P3.2) | Full-time gifted instruction for "selected students" and one enrichment teacher at Heron Pond; no criteria published |
| A budget over $52 million (P2.1) | Right: $52,722,151 |
| The 6% tax cap question (P2.2) | Milford voted 58.9% yes, short of 60%, so neither cap applies |
| Over $22,000 a pupil, a third proficient in math (P2.3) | Right: $22,084; 32% (2025) and 35% (2026) |
| Welding, auto, electrical at the ATC (P4.1) | Welding yes; auto and electrical at Nashua's center; electrical planned for 2027-28 |
| The CTE renovation bond (P4.2) | Failed at 59.0%, 27 votes short; no new shops are scheduled |
| Half the day in CTE (P4.3) | About a quarter of the day (derived) |
| "The Sage School at Bales" (P5.2, P16.3) | No such name; the Bales building holds Project DRIVE, the alternative program |
| Bus routes canceled for driver shortages (P5.3) | No record found |
| A high school tax rate (P7.2) | Mostly an assessment effect: assessments were 62.75% of market value in 2025 |
| Default budget higher than proposed (P8.1) | True in FY2026 and FY2027, lower in FY2024 and FY2025 |
| AP courses run without cancellations (P9.1) | 11 listed, 6 ran in 2025-26 (down from 8–9) |
| Biotech or pre-engineering at the ATC (P10.2) | Pre-engineering is offered but had no teacher or students in 2025-26; no biotech |
| Losing teachers to Amherst and Bedford (P12.2) | The pay gap is real; no source shows where leavers go |
| Different bell times (P13.1) | Confirmed; bus coordination is the only reason given |
| Full-time nurses everywhere (P14.3) | Yes, one in each of the four schools |
| Board and Budget Advisory Committee never agree (P15.1) | Not borne out: they set the FY2027 target together |
| Another roof or HVAC bond (P15.2) | None in the board's plans |
| Late buses after rehearsals (P17.3) | None; every afternoon run leaves by 2:56 |
| No-cut teams (P18.2) | Middle school teams aren't no-cut; the high school's rules don't say |
| A full-time SRO (P18.3) | One for the whole district; the board wants a second on the March 2027 ballot |
| A Boys & Girls Club bus from Heron Pond (P19.2) | The Club's own vans, $50 a month |
| Employers like Hitchiner (P20.1) | No employer partner is named |

## Corrections and additions to earlier files

- **Nashua** (`pathways-and-adult-learning.md`, cte-center-programs 10) lists Advanced Manufacturing at Nashua South. Milford's May 18, 2026 minutes say the Nashua Technology Center was closing its machining program and gave the equipment to Milford. The fact and its note now say so. Nashua is loaded locally, so the folders were re-synced.
- **Hudson** (`alvirne-and-palmer-cte.md`, cte-center-programs 13) counts 15 Milford students at Palmer in 2025-26; Milford's budget book counts 14. The note now gives both. Hudson isn't loaded.

## Library notes (for review, not applied)

- `budget-form-and-vote-dates` (Milford) could add the 2026 outcomes: the budget passed 1,880 to 872, and the CTE bond failed at 59.0%.

## Browser pass (November 17, 2026)

- **NH DOE's special education determinations page** (HTTP 403 to the agents): opened in Chrome. It explains the four rating categories and the rubric but posts no district's rating, so Milford's rating still isn't found.
- **The Union Leader's article on the CTE vote** (HTTP 403): not opened, because the district's own results cover it.
- **Still missing:**
  - Milford's special education rating;
  - AP scores and the 2026-27 AP list;
  - employer partners;
  - the high school's cut policy and fees;
  - the tax year 2026 rate;
  - teacher turnover;
  - the Mason contract.
