# Moultonborough: Research for Ask NH Education Facts

Cited facts and figures for answering Moultonborough, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the seventh wave of the second ToLoad batch. Moultonborough is SAU 45, a one-district SAU:
- **Moultonborough Central School** serves preschool to grade 5.
- **Middle and high school:** the Moultonborough Middle Level (6–8) and Moultonborough Academy (9–12) share the building on Blake Road.
- **Career programs:** the Lakes Region Technology Center (LRTC) in Wolfeboro.

The district decides its budget at a traditional annual meeting. LRTC was researched in `../Wolfeboro/`, and Inter-Lakes in `../Meredith/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `central-school-and-families.md` | Universal, free, part-day preschool, enrollment by grade (232 in October 2026), the 2:45 dismissal and Beyond the Bell (to 5:00; waitlists of 6), Blizzard Bags (paper for K–3; iPads), a reading and writing specialist (no Orton-Gillingham named), Alma replacing PowerSchool, the ESOL teacher and paraeducator, class sizes of about 12.5–19 | 12 | 78 | 1 | 43 MB |
| `middle-level-support-and-choices.md` | The Middle Level's own principal, door and schedule inside the Academy building, Algebra I Honors for credit from grade 8 (9 of 26 in 2023-24, all passed), one psychologist and one social worker for all schools plus clinicians, homeschool and EFA access (a proposed JJJ), basketball teams, school choice limits, 504 plans, the mentoring program | 10 | 81 | 1 | 40 MB |
| `moultonborough-academy-and-lrtc.md` | About 137 students, 31 classes of 8 or fewer, AP in person, Early College (131 courses in 2024-25), co-ops with Inter-Lakes only, 17 students at LRTC (about 41 minutes away), the school store, 82 scholarships to 23 seniors, families paying for college courses | 7 | 44 | 1 | 52 MB |
| `money-and-governance.md` | The 2026-27 budget ($21,111,300, +2.96%; health insurance +$537,558), the donor-town history and the excess kept (about $4.9 million a year), the tax cap (passed locally), $700,000 of surplus returned, the tuition-free exchange with Inter-Lakes, Tamworth's tuition, a $7.344 million energy bond, facilities needs (no working science lab), about 54% of the tax bill to schools | 9 | 86 | 4 | 64 MB |
| **Total** | | **38** | **289** | **7** | **199 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.07 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Moultonborough`). All 7 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 33 partial, 1 from the site's data.
- **Topics:** two new topics, added to `../shared-topics.md`:
  - `school-counseling-and-psychologist-ratios`: the ratios national associations recommend, and the national and New Hampshire averages;
  - `ap-course-authorization`: how a course, including an online one, earns the AP label.
- **Places:** `district Moultonborough` 253, `town Moultonborough` 31, `district Governor Wentworth Regional` 1, no place 4.
- **Pending facts:** 21, mostly about the proposed policy JJJ revision and draft minutes.
- **Raw folders:** each under 100 MB. The address scan finds no home stops.
- **Privacy:** the main session removed two residents' house numbers from the September 9, 2026 minutes and deleted that PDF. Later, the main session also removed graduates' names from the saved 2026 annual report texts, and deleted those PDFs.
- **Quotes:** 577 of 689 quoted passages found word for word in the raw copies.
- **Search:** two agents ran out of web searches ("SEARCH BLOCKED").
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026-27 budget, $21,111,300 | The district's 2026 annual report |
  | The FY2005 donor payment, $4,033,580 | The Coalition Communities list (not a state source; the fact says so) |
  | The $7.344 million energy bond | The 2025 audit |
  | Health insurance up $537,558 (**derived**) | The agent's sum of 40 budget lines |

## Premises checked

| Question says | What the sources show |
|---|---|
| Universal preschool, full days (P1.1) | Universal and free, but part-day |
| Preschoolers on the bus (P1.2) | Not confirmed |
| Enrollment dipping (P1.3, P20.1) | Partly |
| Leaving work at 2:30 (P5.1) | Dismissal 2:45; Beyond the Bell to 5:00 |
| Blizzard Bags on Chromebooks (P5.2) | They exist; K–3 work on paper |
| Orton-Gillingham (P7.1) | Not named |
| Everything through Alma (P11.1) | True |
| ESL at a small school (P15.1) | An ESOL teacher and paraeducator |
| Grades 6–8 with the high school (P4.1) | Confirmed, with their own schedule |
| Waiting until 9th grade for algebra (P4.2) | Partly wrong: Algebra I Honors in grade 8 |
| A shared psychologist and social worker (P10.2) | Confirmed |
| Basketball only in rec league (P13.2) | Not so |
| About 135 high schoolers (P8.1, P18.1) | Correct: 137 |
| Co-ops with Inter-Lakes or Kingswood (P13.1) | Inter-Lakes only |
| The ABC on small classes (P16.1) | Partly correct |
| A donor town (P3.2) | It was one; it keeps the excess now |
| Half the bill to schools (P6.1) | About 54% |
| A state tax cap (P6.3) | Passed locally, 62.6% |
| Special education aid cuts (P7.3) | That aid is about 0.7% of the cost |

## Corrections and additions to earlier files

- **Tamworth** (`../Tamworth/`): Moultonborough's side of the tuition extension. The board approved it on January 13, 2026 and set its own 2026-27 rate ($20,221).
- **Meredith** (`../Meredith/`):
  - The superintendent confirmed the tuition-free exchange with Inter-Lakes in February 2026.
  - The lacrosse co-op ran through 2025-26.

## Library notes (for review, not applied)

- **`district-preschool` 75** says no schedule or tuition is posted. The 2026-27 handbook gives both: free; 3-year-olds Tuesday–Thursday mornings, 4-year-olds weekday afternoons.
- **`early-college-at-your-high-school` 5** and Moultonborough Academy's catalog say two free Early College courses a year. Lakes Region Community College now says four.
- **Moultonborough budget form:** the 2026 open enrollment article (Article IV) is still marked "outcome not checked".

## Browser pass

Not needed for the answers. Not retrieved:
- sau45news.com (HTTP 403);
- the bus route folder and some policy documents, which need a Google sign-in;
- NH DHHS's regional survey lists (HTTP 403).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- The state's resident birth, marriage and death lists removed from 2 saved town report copies (headings and record counts kept); 1 report PDF deleted.
