# Farmington: Research for Ask NH Education Facts

Cited facts and figures for answering Farmington, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the ToLoad towns. Farmington is SAU 61, a one-district SAU:
- Valley View Community School: preschool to grade 3;
- Henry Wilson Memorial School: grades 4–8;
- Farmington High School: grades 9–12.

Farmington High students take career programs at the Lakes Region Technology Center (LRTC) in Wolfeboro, not Rochester's center as the brief guessed.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `valley-view-and-families.md` | The 7:45 start (supervision from 7:30), no before-school care, Tiger BEATS after school ($30 a week; free with free meals), meal prices, storm calls by about 5:30, the preschool (30 places; $800 or $1,000 a year), bus rides up to about 87 minutes, bus changes, grade 3 reading against Dover and Rochester, Fundations and the grade 3 pilot | 16 | 105 | 3 | 22 MB |
| `henry-wilson.md` | The special education coordinator opening and a case manager vacancy since June 2025, math results (32% in the site's data), no Algebra 1 in grade 8, the grade 4 / 5–6 / 7–8 teams, no late bus, the August 2026 bullying policy, access for students not enrolled (no EFA wording yet), home education | 12 | 66 | 0 | 15 MB |
| `farmington-high-school.md` | LRTC programs and buses (21–30 minutes each way), no shop at the high school, three AP courses and Early College, counselors (one, plus a part-time hire), absence calls for every absence, two school resource officers, credit recovery, tutoring options, football with Milton, no athletic fee | 10 | 116 | 2 | 15 MB |
| `money-and-governance.md` | The 2026 votes (budget failed 239–337; the $18,076,646 default; the teachers' contract and $160,000 bleachers failed; the oil tank passed), why costs rose (a shortfall, SchoolCare's bill, a mid-year layoff), the missing $700,000 reserve deposits, ratings against Strafford and Alton, the tax cap (1,722–745), no bonds | 10 | 83 | 5 | 40 MB |
| **Total** | | **48** | **370** | **10** | **92 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.11 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Farmington`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 30 partial.
- **Topics:** no new topics.
- **Places:** `district Farmington` 358, `town Farmington` 12.
- **Pending facts:** 1, which quotes the word "pending" from a law.
- **Raw folders:** each under 100 MB.
- **Quotes:** 763 of 895 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The default budget, $18,076,646 | Board minutes, January 31, 2026, and the March 2026 annual report |
  | School reserve funds, $874,432.59 | The 2025 town report's trust fund page |
  | The tax cap vote, 1,722 to 745 | The town's tally and the site's Question 2 row |

## Premises checked

| Question says | What the sources show |
|---|---|
| A 7:30 start at Valley View (P1.1) | 7:45, with supervision from 7:30; no before-school program |
| Free meals for kindergartners (P1.2) | No: $2.00 breakfast, $3.60 lunch; apply yearly |
| Storm texts (P1.3) | Phone calls, usually by 5:30 a.m. |
| A pre-K waitlist (P2.1) | Not confirmed: 30 places, 22 children counted |
| Drop-offs at a sitter's on some days (P2.3) | Changes by year, half year or quarter; one-day emergencies need the principal |
| A special education coordinator opening (P6.1) | Right: posted November 12, 2026 |
| About a third proficient in math at Henry Wilson (P7.1) | Right: 32% in the site's data (39.6% in the district's plan) |
| Algebra 1 in grade 8 (P7.2) | Not found; a pre-algebra half credit |
| Grades 4–8 together (P8.1) | Partly: separate grade 4, 5–6 and 7–8 teams |
| A late bus (P8.2) | None, apart from Tiger BEATS at 5:00 |
| CTE welding and auto in Rochester or Dover (P11.1) | LRTC in Wolfeboro: auto yes, welding only within its auto courses |
| Shop at the high school (P11.3) | None |
| Running Start (P12.1) | Early College; three AP courses, two alternating |
| Enough counselors (P12.2) | Partly: one, plus a part-time counselor since October |
| Athletic fees (P13.3) | None found |
| No call when a student skips (P14.3) | Wrong: a call or email for every absence |
| A $160,000 warrant article (P13.1) | Right; the bleachers failed 153–434 |
| An $18 million default budget (P16.2) | Right |
| A rate rise of over $3.25 (P16.1) | Posted +$4.88, about +$3.48 after amendment; the budget failed |
| Ratings below Strafford and Alton (P17.2) | True for Valley View and the high school, not Henry Wilson |
| Question 2 lowering taxes (P16.3) | No: it limits growth from 2027-28 |
| A bond for old buildings (P19.3) | No bond owed or planned |
| Losing teachers often (P19.1) | The Title I plan cites 35% turnover |

## Corrections and additions to earlier files

- **Brief:** it guessed Rochester's career center; it's LRTC in Wolfeboro. This matches Freedom's and Tamworth's files.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 40 (Farmington)** says the deliberative session and vote dates weren't found. The 2026 dates are here (district-board-and-public-input 1).
- **Preschool, kindergarten hours, cutoff and registration:** the library's Farmington gaps on these are filled here.

## Browser pass

The agents' blocked pages were:
- DRA's 2026 tax rates (HTTP 403);
- Niche;
- NHIAA's team pages;
- NH DOE's gifted page;
- the high school's flipbook program of studies (no readable text).

None is essential to the answers.
