# Claremont: Research for Ask NH Education Facts

Cited facts and figures for answering Claremont, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the sixth wave of the ToLoad towns. Claremont is a city and SAU 6, which since July 1, 2026 serves only Claremont. Since Bluff Elementary closed and a September 2026 vote, the Claremont School District runs:
- Disnard Elementary School: preschool to grade 2;
- Maple Avenue Elementary School: grades 3–5;
- Claremont Middle School: grades 6–8;
- Stevens High School: grades 9–12, with the Sugar River Valley Regional Technical Center on two campuses, Claremont and Newport.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | The September 16, 2026 vote ending zones, the end of free meals for all ($3.75 lunch), preschool only for children with IEPs, reading screening (49–65% below benchmark in fall 2026), crowded kindergarten at Disnard, start times (Maple Avenue 8:50), Title I and ParentSquare | 14 | 80 | 0 | 24 MB |
| `middle-support-and-choices.md` | Special education capacity (15 staff short; 63% of IEPs out of compliance; evening and weekend staff), CMS openings, bus driver shortage, bell times (CMS 7:35), homeschool and EFA access, Claremont Christian Academy ($7,900 for grades 6–12), open enrollment (0% out) | 11 | 89 | 2 | 25 MB |
| `stevens-high-and-tech-center.md` | The tech center (machine tool cut; nursing assistant added; electrical teacher hired; participation projected to double), credentials and college credit by program, state monitoring reports, NEASC accreditation (in good standing), sports funding, no AP but about 19 Early College courses | 11 | 66 | 3 | 18 MB |
| `money-and-governance.md` | The deficit (estimated at $5 million, now "about $1M or less"; unaudited), the $4 million bank loan against state aid (repaid; interest returned), the draft FY2022 audit, the state's appeal of the Claremont rulings, the Bluff building (sale approved 1,675–201; unsold), Unity's exit from SAU 6, lapsed tuition agreements, Question 2 (60.8%) | 13 | 104 | 2 | 60 MB |
| **Total** | | **49** | **339** | **7** | **127 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.14 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Claremont`). All 7 tables are linked to a topic.
- **Coverage:** all 60 questions are listed: 29 full, 28 partial, 2 from the site's data, and 1 with none (P6.3, crossing guards, not found).
- **Topics:** no new topics.
- **Places:**
  - `district Claremont` 309, `town Claremont` 19, no place 5.
  - `district Claremont Christian School` 4, and one each for `district Unity` and `district Cornish`.
- **Pending facts:** 43. Many cite the only versions posted: draft minutes and the draft FY2022 audit report. Their notes say so.
- **Raw folders:** the four total 127 MB; each is under 100 MB.
- **Quotes:** 575 of 698 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The bank's returned interest, $10,563.11 | June 17, 2026 board minutes and the SAU news item |
  | The Bluff sale vote, 1,675 to 201 | Board minutes, April and June 2026 |
  | Excess fund balance used, $1,059,738 | The draft FY2022 audit report |
  | Elementary lunch, $3.75 | SAU 6's meal pages and the June 3, 2026 price item |

## Premises checked

| Question says | What the sources show |
|---|---|
| Combined third-grade classes after Bluff (P16.3) | Bluff's classes moved intact; grades 3–5 are now all at Maple Avenue |
| Disnard or Maple Avenue zones (P13.2, P20.1) | No zones since September 16, 2026: PreK–2 Disnard, 3–5 Maple Avenue |
| Free meals for everyone (P6.1) | Ended with Bluff, the only school on the federal free-meal program |
| Maple Avenue starting at 8:30 | 8:50 |
| A Community Center program with busing (P17.2) | No bus stop there found |
| Crossing guards (P6.3) | Not found |
| Evening special education staff (P5.2) | Right: posted for evening and weekend hours |
| A 7:30 middle school start (P17.1) | 7:35 |
| Bus routes cut (P1.3) | No cut; a driver shortage doubles up routes when someone is out |
| "CCA" (P10) | Claremont Christian Academy; grades 6–12 are in Charlestown |
| Trades cut at Stevens (P3.1) | Partly: machine tool cut; welding and automotive were always at Newport; the center is growing |
| Accreditation trouble (P7.3) | NEASC lists Stevens as accredited and not on probation |
| Sports and band cuts (P7.2) | Activities were cut in August 2025 and sports ran on donations; no new cut found |
| Athletic fees (P15.3) | None found |
| Running Start (P7.1) | Early College; about 19 courses; no AP listed |
| A $5 million deficit (P11.1) | Roughly, but unaudited; now estimated at about $1 million or less |
| A state loan to pay back (P2.1) | No: a $4 million bank loan against state aid, repaid |
| The state appealing the Claremont rulings (P2.2) | Right; the appeal is pending |
| Bluff for sale (P2.3, P14.3) | Approved 1,675–201; unsold in November 2026 |
| Cornish and Unity pulling back from SAU 6 (P18.2) | Unity left July 1, 2026; Cornish left in 2017 |

## Corrections and additions to earlier files

- **`places.yaml`:** the Unity, Cornish and Croydon → Claremont notes now add the superintendent's November 2026 report:
  - agreements had expired in June 2026 or been breached, and new ones were being sent;
  - Unity left SAU 6 on July 1, 2026.

## Library notes (for review, not applied)

- **`kindergarten-day-length` 8** gives Claremont's kindergarten dismissal as 3:10. The 2026-27 handbook and bus sheets give 2:55 at Disnard.
- **`district-preschool`** has no Claremont fact; facts 1–5 here fill it.
- **The SAU directory row** reads "SAU 6 (Claremont and Unity)". Since July 1, 2026 it is Claremont only.
- **`programs-and-help.md`** lists no sending schools for the Sugar River Valley center. The director's memo gives Stevens 324, Newport 13 and Fall Mountain 1 for 2026-27.

## Browser pass

The agents' blocked pages were:
- DRA's 2026 tax rates (HTTP 403);
- NH DOT's sidewalk grant application;
- two board policies behind a sign-in;
- Newport's tech center pages (bot check);
- Claremont Christian Academy's site (read through WebFetch; no verbatim copy).

None is essential to the answers.
