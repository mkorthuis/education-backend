# Portsmouth: Research for Ask NH Education Facts

Cited facts and figures for answering Portsmouth, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the five files below, in the reference library's format, ready to load but not loaded.

Gathered November 16, 2026, alongside Hudson, Bedford, Keene, Goffstown and Laconia. Portsmouth is SAU 52, a one-district SAU (the Portsmouth School Department): PEEP (preschool) at Little Harbour, Little Harbour, Mary C. Dondero and New Franklin for kindergarten to grade 5, Portsmouth Middle School (6–8) and Portsmouth High School (9–12) with its Career Technical Education Center, the Little Clipper lab preschool and the Robert J. Lister Academy. Greenland, New Castle, Newington and Rye send high school students; New Castle and Newington also send middle school students. The City Council adopts the school budget.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | The 2025 redistricting and its transition neighborhoods, enrollment reviews, after-school care (ACE full with a waitlist, MC3, PEAK), the kindergarten day, how the three schools compare, the reading pilot, summer programs, military families, PEEP and Little Clipper, specials, volunteering, class sizes and policy JF | 15 | 85 | 2 | 20 MB |
| `middle-high-and-cte.md` | The CTE Center's programs and the welding redesign, the shipyard partnership, the move to middle school (two teams of about 80), math placement, no AP classes since 2023-24 (honors and dual enrollment instead), the bell-to-bell phone ban, Great Bay credit, financial literacy from the Class of 2030, internships, Lister Academy, tryouts, the freshman transition, robotics and coding | 9 | 86 | 4 | 28 MB |
| `student-support.md` | IEP follow-through and counts (429), out-of-district placements falling, meal prices and the free-meals pilot, counselors and social workers, the 2026 bullying policy, inclusion, the DEI law (blocked in court), English learners, translation, transition services to the 22nd birthday, peer programs | 6 | 83 | 2 | 21 MB |
| `money-buildings-and-governance.md` | School budgets FY2016–FY2027, health insurance (SchoolCare up 26.2%), the tax rate, Question 2 and the charter, the AREA tuition formula and 2026-27 rates, cuts in FY2027, per-pupil spending, state aid (1.9% of school funds), goals and reporting, the draft FY2028–FY2033 capital plan, community use of facilities | 7 | 81 | 8 | 42 MB |
| `getting-to-school-choices-and-staff.md` | Bus routes and stop times from Elwyn Park, early-release Wednesdays, the start-time history, where Coast Guard families are based, enrollment projections (NESDEC), EFAs at Saint Patrick Academy, private school counts, why parents choose schools, teacher and para contracts and postings, where staff live | 13 | 62 | 5 | 29 MB |
| **Total** | | **50** | **397** | **21** | **140 MB** |

`brief.md` is the brief the research agents worked from. Five agents used about 2.67 million tokens.

## Checks

- **Parser:** all five files pass the backend's parser (`tools/check_town.sh Portsmouth`). All 21 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 36 partial.
- **Topics:** two new topics were added to `../shared-topics.md`: `district-goals-and-performance-reporting` (a district's goals and the measures it reports besides test scores) and `research-school-choice-reasons` (national surveys of why parents choose a school; the library's `research-private-school-choice` is about effects, not reasons).
- **Places:** `district Portsmouth` 351, `town Portsmouth` 35, no place 7, `district Rye` 2, `district Dover` 1.
- **Places for the backend:** the four SAU 50 rows in `places.yaml` cite Portsmouth's tuition policy; the agreements themselves still aren't online, so no dates can be added. Nothing to change.
- **Draft facts:** 39 notes are flagged. Most cite the draft FY2028–FY2033 capital plan and draft board minutes (including the November 10, 2026 free-meals vote), which are all that's posted; they're accurate as drafts.
- **Raw folders:** all under 100 MB.
- **Quotes:** 859 of 1,072 quoted passages found word for word in the cited raw copies; most of the rest are route sheets and budget tables reformatted in the notes.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Question 2: 43.4% yes | The site's Question 2 data (4,906 to 6,395) |
  | 2026-27 AREA tuition, $25,529 a high school student | Tuition rate memo, October 30, 2026 |
  | FY2027 school budget up $4,380,351 (6.51%), $2,751,313 of it health insurance | The city's FY2027 budget and its May 11, 2026 presentation |
  | Free meals pilot to 260% of poverty from January 1, 2027 | School board minutes, November 10, 2026 (draft) |
  | Lunch $3.50, $4.00 and $4.25 | The district's meals page |

## Premises checked

| Question says | What the sources show |
|---|---|
| Elementary redistricting (P1.1) | Already done: adopted January 28, 2025, in effect 2025-26; no new proposal, though projections are due December 8, 2026 |
| "Little Clipper" preschool and speech therapy (P10.2) | Two programs: Little Clipper is a $4,770-a-year lab preschool at the high school; speech therapy comes free through PEEP after an evaluation |
| Free lunch for everyone (P4.3) | Wrong: lunch costs $3.50–$4.25; a city-funded pilot to 260% of poverty was voted November 10, 2026 |
| AP classes at PHS (P6.2) | Stopped in 2023-24; 19 honors and 28 dual enrollment courses instead; students may still take AP exams |
| Welding, electrical and marine trades (P2.1) | Welding yes (redesigned); no electrical or marine program at PHS |
| Varsity cuts (P11.3) | Policy says open tryouts; no cut counts are published |
| The budget "jumping by millions" (P2.2) | Right: $43.2 million (FY2016) to $71.6 million (FY2027) while resident students fell 9% |
| A local tax cap and override (P5.2) | Question 2 failed (43.4%) and the posted charter has no cap |
| Rye and Newington's "fair share" (P5.3) | They pay a formula rate ($25,529); whether it's fair is a judgment the data can't settle |
| Per-pupil spending "way higher" than the state (P9.1) | Right: $27,609 against $22,699 |
| Cuts to reading specialists, paras or the arts (P8.2, P14.2) | FY2027 cut a net 2.5 paras and 2 tutors; no reading specialist or arts cuts |
| A "massive bond" for a roof or HVAC (P16.2) | No: roofing is spread over six years; high school HVAC and roof work ($6 million) is set for FY2032–FY2033 |
| Many early-release days and Wednesdays off (P7.2) | Eight early releases, all Wednesdays; Veterans Day is the only full Wednesday off |
| A bus before 8 a.m. (P7.3) | Right on 9 of 12 routes (first stops 7:53–7:58) though PHS starts at 8:35; the start moved from 7:30 in 2017-18 |
| Half-empty schools in ten years (P13.3) | Not supported: NESDEC projects 930–982 K–5 students through 2035-36, against 905 now |
| Para and substitute postings (P19.2) | Right: 14 paraeducator and 8 long-term substitute postings on November 16, 2026 |
| Coast Guard families at Pease (P10.3) | Pease is the Air National Guard base; the Coast Guard's cutters are at the shipyard in Kittery |
| The DEI law (P15.2) | It exists, but a federal court has blocked enforcement; no change to clubs was found |
| Services until 21 (P20.1) | Right: to the 22nd birthday or a regular diploma |

## Corrections and additions to earlier files

None to earlier towns. `town/Dover/choices-and-adult-learning.md` (`town-school-options-nearby`) already covers Seacoast Charter, Saint Mary Academy and Portsmouth Christian Academy; these files cite it.

## Library corrections

Applied November 16, 2026 to both library copies (backend commit `c7c868a`), except those marked for review:

- `district-practices.md`, `budget-form-and-vote-dates` 112 (Portsmouth): its note says the city charter has a tax cap; the posted charter has none (`money-buildings-and-governance.md`, `district-tax-and-state-aid`).
- `district-practices.md`, `kindergarten-entry-cutoff` 89 cites a 2017-18 page; policy JFAA (age 5 by September 30) is the current source.

## Not retrieved

The browser pass (November 16, 2026): NH DOE's special education page lists only statewide fact sheets and PDF determinations; PEAK's old page now returns 404 and its rate notice links an attachment; the shipyard's apprentice page redirects to a general careers page listing its 20 skilled trades, with no Portsmouth eligibility rules beyond what `middle-high-and-cte.md` cites. Nothing new was added. Still missing:


- NH DOE pages (HTTP 403): special education compliance and complaints, student race, the Purple Star release.
- The PEAK after-school page (a bot check).
- Portsmouth Naval Shipyard's careers pages and Coast Guard and Navy housing pages (HTTP 403).
- The district's Title I plans and 2026 annual report (Google sign-in; can't be opened without an account).
