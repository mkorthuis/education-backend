# Epping: Research for Ask NH Education Facts

Cited facts and figures for answering Epping, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the ToLoad towns. Epping is SAU 14, a one-district SAU:
- Epping Elementary: preschool to grade 5.
- Epping Middle School and Epping High School: grades 6–8 and 9–12, sharing one building.

Students may take career programs at the Seacoast School of Technology.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | Drop-off (doors at 8:15) and the town's care (6:45 a.m.–5:45 p.m., $12 mornings and $18 afternoons), bus rides (30–50 minutes; FirstView), remote days, meals, child care bus stops (policy EEA), help with costs, the preschool ($150 a month, at the SAU office, a waiting list), the portal, homework help, bullying contacts, ESOL, translation, volunteering | 12 | 100 | 1 | 28 MB |
| `middle-high-school.md` | SST (applying, the bus on Epping's workshop days, second-years missing 2 of 4 blocks), the A/B block schedule (grades 9–12), competency grading, about 230 high school students, AP courses by year (AP Chemistry last ran in 2024-25), Early College, math, separate lunches, 24/27/30-credit diplomas (rising for the class of 2030), semester grades, guidance | 9 | 73 | 6 | 31 MB |
| `support-safety-and-choices.md` | Special education openings (6 of 10 postings), evaluation timing, pull-outs, homeschoolers and EFAs in sports and band, the town's ski bus, re-entry, teams (football with Newmarket), athletic trainers and concussions, late buses (none), phones (off, in a locker or bag), counselors, security and SAFE grants ($126,139), nurses, allergies, military families | 13 | 92 | 0 | 27 MB |
| `money-and-governance.md` | Spending and scores (the ballot's 2025 figures; 2026 lower), the wastewater bond ($38 million, a town cost), Question 2 (60.14%, about 5 votes to spare) and the $888,000 shortfall estimate for FY2028, the June special meeting (unsigned budget form), the SAU budget's own article from 2027, surplus use (44.5% to lower taxes), the 2025 building project ($6,945,718 note to 2042), work study, the calendar, enrollment | 13 | 88 | 5 | 39 MB |
| **Total** | | **47** | **353** | **12** | **125 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.87 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Epping`). All 12 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial. P10.3 (the kindergarten cutoff) is answered wholly by the library.
- **Topics:** one new topic, `school-sports-rules` (concussion law, medical coverage at games, NHIAA cooperative teams), added to `../shared-topics.md`; the library had none.
- **Places:** `district Epping` 313, `town Epping` 28, no place 12.
- **Pending facts:** 2.
- **Raw folders:** all under 100 MB.
- **Quotes:** 639 of 782 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2025 building note, $6,945,718 | SAU 14's FY2025 audit (OCR) |
  | The FY2028 shortfall, "almost $888,000" | School board minutes, November 5, 2026 |
  | After-school care pricing | The town's spring 2027 registration form |

## Premises checked

| Question says | What the sources show |
|---|---|
| Care until 5:30 or 6:00 (P1.1) | The town's program runs 6:45 a.m.–5:45 p.m. in the school gym |
| A bus app (P1.2) | Right: FirstView, new for 2026-27 |
| Remote days (P1.3) | A remote day plan exists; no posted policy |
| An SST bus on Epping workshop days (P2.2) | It runs, and students are expected to go |
| Over $23,000 a pupil and 38% proficient (P3.1) | Right as printed on the ballot (2025 results); 2026 was 32% |
| The wastewater plant and the school tax (P3.2) | $38 million approved in March 2026, about $1 per $1,000, outside the school cap |
| A budget form mix-up (P3.3) | Right: posted without the budget committee's signatures; no figures changed |
| An A/B block schedule and no quarter grades (P5.1, P20.2) | Right for grades 9–12 |
| About 220 high school students (P5.3) | About 230 now |
| AP classes changing each year (P7.1) | Right |
| SAU costs on their own article (P9.1) | From March 2027, under the 2026 law |
| Leftover money not returned (P9.2) | Partly: 44.5% of the FY2026 surplus lowered taxes |
| New roofs, boilers and air handlers (P9.3) | Right; more items on the capital plan |
| A preschool lottery (P10.1) | Current pages describe a waiting list |
| A work-study program (P11.1) | "Work Study Practices" are graded habits; internships earn credit through ELOs |
| The ski bus through the school (P8.2) | No: the town's recreation department runs it |
| Phones locked up (P14.2) | No: off and in a locker or bag |
| A nurse in each building every day (P19.1) | One per building; no schedule posted |
| 24/27/30-credit diplomas (P20.1) | Right for the classes of 2027–2029; higher from 2030 |

## Corrections and additions to earlier files

None needed.

## Library notes (for review, not applied)

- `district-preschool` 26 says no Epping preschool tuition or schedule is posted. Both now are: $150 a month, Monday–Thursday half days.

## Browser pass

The agents' blocked pages were:
- NH DOE's SAFE grant page (the legislature's copy of the award list was used instead);
- the federal FAFSA completion data;
- the district's job portal (a script page).

None is essential to the answers.

**Site data labels:** the site's town enrollment year "2026" is the October 1, 2025 count (2025-26). The brief called it 2026-27.
