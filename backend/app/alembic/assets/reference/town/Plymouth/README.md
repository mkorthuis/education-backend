# Plymouth: Research for Ask NH Education Facts

Cited facts and figures for answering Plymouth, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the ToLoad towns. Plymouth is in SAU 48:
- **The Plymouth School District** runs Plymouth Elementary School (PES), preschool to grade 8.
- **The Pemi-Baker Regional School District**, a seven-town cooperative that includes Plymouth, runs Plymouth Regional High School (PRHS) and its career and technical center.

Mountain Village Charter School and Holderness School are nearby choices.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `pes-and-families.md` | Door times (8:25; buses 8:20), after-school care moved to the Pemi Youth Center ($60 a month, 30 places), the preschool ($15 a day, residents in order), Head Start (part-day), full-day kindergarten and the September 30 cutoff, meals ($3.40 lunch), Chromebooks home only in grade 8, the Winter Program and ski passes | 16 | 67 | 2 | 24 MB |
| `pes-support-and-choices.md` | Math results (52%), Algebra I and Spanish I for high school credit, Mountain Village (grades 1–8, a lottery, Montessori), policy JJJ for homeschool and EFA students, the EFA marketplace near Plymouth, Holderness School aid, speech caseloads, translation on request | 15 | 84 | 0 | 16 MB |
| `prhs-and-career-center.md` | The CTE programs (automotive, culinary, health science, outdoor recreation, TV & media, drafting, marketing), credits CTE earns, Early College and Plymouth State costs, 2026 AP results (93% scored 3 or higher), SAT means, college and aid advising, phones banned all day, no late bus, a credentials topic | 11 | 67 | 4 | 11 MB |
| `money-and-governance.md` | The seven-town cost split (half students, half value; Plymouth 24.0%), only 27 tuition students at PRHS, the tax split (about 74% PES, 26% PRHS), the 2026 increases (Plymouth +$718,443), new teacher contracts ($49,280 start), vote dates for 2027, the two calendars, public comment at meetings | 11 | 70 | 3 | 24 MB |
| **Total** | | **53** | **288** | **9** | **75 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.87 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Plymouth`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 29 partial, 1 from the site's data.
- **Topics:** one new topic, `industry-credentials-explained`, added to `../shared-topics.md`. Berlin's research proposed the same topic, and it now uses this slug.
- **Places:**
  - `district Plymouth` 115, `district Pemi-Baker Regional` 103, `town Plymouth` 23, `sau 48` 18.
  - `district Mountain Village Charter School` 14, no place 9, `district Holderness School` 5, `district Campton` 1.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB.
- **Quotes:** 665 of 764 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Plymouth's increase, $718,443 | The 2026-27 adopted budget |
  | Starting pay, $49,280 | The 2026–2029 teachers' agreement |
  | AP results, 93% at 3 or higher | PRHS's college planning page and Pemi-Baker's 2025 annual report |

## Premises checked

| Question says | What the sources show |
|---|---|
| 30 to 55 children a grade at PES (P3.2) | About right, from the school's own page |
| Door times (P1.1) | 8:25, with buses at 8:20 since October 2026 |
| Parks & Rec after-school (P1.2) | Moved to the Pemi Youth Center in May 2026 |
| Pre-K open to everyone (P3.1) | $15 a day, by order of packets, with a lower rate for eligible incomes |
| PSU student teachers at PES (P3.3) | No current source names PES as a site |
| Free lunch (P5.1) | $3.40 |
| About half proficient in math at PES (P6.1) | Right: 52% in 2026 |
| Algebra I or Spanish in grade 8 (P17.3) | Right |
| Mountain Village's lottery for a kindergartner (P7.1) | It takes grades 1–8, and children must be 6 by September 30 |
| Health Science in 9th grade (P12.2) | Not possible; prerequisites usually put it in junior year |
| PRHS reading around 72% (P14.2) | That was 2025; 2026 was 68% reading, 36% math |
| Running Start (P6.3) | Now Early College |
| A late bus (P12.3) | None posted |
| Fire/EMT ride-alongs for credit (P20.1) | One firefighter placement in 2024-25; no ride-along program |
| Other towns not paying their share of PRHS (P2.3) | Mostly wrong: a seven-town cooperative; only 27 tuition students |
| Over $26,000 per pupil (P4.1) | Right: $26,555 |
| No crossing guard on Old Ward Bridge Road (P16.1) | The town has a school crossing guard; the road was repaved in 2025 |
| Different early-release days (P20.2) | Right: PES early releases against PRHS delayed openings |

## Corrections and additions to earlier files

None needed. Jackson's Holderness School tuition and Laconia's LRCC facts are consistent.

## Library notes (for review, not applied)

- **`district-preschool` 93** says PES posts no eligibility rules or tuition. The registration packet does (district-preschool 1–3 here).
- **The coverage table** lists Plymouth's kindergarten day and cutoff as not found. Both are here now.
- **Ashland fact 6** says Ashland's report doesn't describe its PRHS arrangement. Pemi-Baker's 2026 warrant and apportionment do.

## Browser pass

The agents' blocked pages were:
- Mountain Village's charter on NH DOE's site (HTTP 403);
- four SAU 48 Drive files (sign-in);
- the police site;
- NH DOE's enrollment report.

None is essential to the answers.
