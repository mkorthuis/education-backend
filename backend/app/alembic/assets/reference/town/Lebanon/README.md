# Lebanon: Research for Ask NH Education Facts

Cited facts and figures for answering Lebanon, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the sixth wave of the ToLoad towns. Lebanon is a city and SAU 88, a one-district SAU:
- Mount Lebanon School: preschool to grade 4;
- Hanover Street School: K–4;
- Lebanon Middle School: grades 5–8;
- Lebanon High School: grades 9–12, which also takes Plainfield's and Grantham's students under an AREA agreement from 1967.

Juniors and seniors may take career programs at the Hartford Area Career and Technology Center in White River Junction, Vermont. Ledyard Charter School is in Lebanon.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | The preschool lottery (due February 19, 2027), kindergarten by home address, full-day kindergarten (8:00–3:00, no fee), supervision from 7:30, after-school care (Immersion Montessori at both schools; CCBA $185–$360 a month), bus runs, the winter weather procedure, UFLI and Heggerty, DIBELS screening, the Lau Plan's English-learner time and translation | 14 | 61 | 1 | 54 MB |
| `middle-support-and-choices.md` | LMS grade teams (5–8 since 2012), phones banned all day, counselors (about 153 each), a psychologist and online therapy, policy re-adoptions in August 2026, home education after July 2026, Ledyard Charter (sports yes, prom as a guest; Lebanon's funding), library hotspots, staff and student diversity | 14 | 71 | 0 | 22 MB |
| `high-school-and-pathways.md` | The Hartford center (half-day; buses at 8:00 and 11:00; $15,000 per student paid by Lebanon), college courses (River Valley from grade 10, Dartmouth from grade 11), 16 AP courses (91% scored 3 or higher in 2025), four counselors, no pay-to-play, HiSET prep in SAU 88's adult program | 8 | 72 | 3 | 12 MB |
| `money-and-governance.md` | The 2026 rate ($22.16; schools $12.83), Question 2 failing and the city's own charter cap (city only, from 2028), the two 2027-28 budgets, cost drivers (health insurance +19.6%), ten years of Plainfield and Grantham tuition, bonds, zone counts (Mount Lebanon full), central office costs (4.99%) | 10 | 101 | 9 | 72 MB |
| **Total** | | **46** | **305** | **13** | **160 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.93 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Lebanon`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 34 full, 24 partial, 2 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Lebanon` 261, `town Lebanon` 35, `district Ledyard Charter School` 9. The Hartford center is in Vermont, which the site has no place type for, so its facts are placed `district Lebanon`. A `vermont` place like the `maine` ones could be added later.
- **Pending facts:** 5, citing draft October 2026 minutes.
- **Raw folders:** each under 100 MB.
- **Quotes:** 648 of 768 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $22.16 | The city's tax rate notice and the budget slides |
  | Hartford tuition, $975,000 for 65 students | The 2026 proposed budget (MS-26, OCR) |
  | The charter cap vote, 1,155 to 854 | The city's March 10, 2026 results |
  | CCBA's care, from $185 a month | The district's 2027-28 summary and budget |

## Premises checked

| Question says | What the sources show |
|---|---|
| The preschool at Mount Lebanon (P1.1) | Right; kindergarten then follows the home address |
| Drop-off by 7:00 (P1.2) | Supervision from 7:30, school at 8:00; no before-school program |
| A preschool waitlist (P14.3) | A lottery, due February 19, 2027 |
| Dyslexia screening (P17.2) | Right: DIBELS for K–3 every year |
| After-school care until 5:30 (P5.2) | CCBA takes K–6 until 5:30 |
| Free full-day kindergarten (P10.3) | Full day, 8:00–3:00; no fee listed |
| 5th grade at the middle school (P5.1) | Right, since 2012; each grade has its own team |
| Phones (P11.2) | Banned all day, not just in class |
| Ledyard students at LHS (P13.2) | Sports yes, by state law; prom only as a guest |
| District hotspots (P19.2) | None; the public libraries lend them |
| Social workers at LMS daily (P11.1) | No: a quarter-time social worker |
| CTE fees at Hartford (P2.3) | None found; the district pays tuition |
| College courses for a 9th grader (P6.2) | Not yet: River Valley from grade 10, Dartmouth from grade 11 |
| Pay to play (P15.3) | No fee listed |
| GED prep (P16.3) | New Hampshire uses the HiSET; SAU 88 offers free prep |
| The $22.16 rate (P4.1) | Right; schools are $12.83 of it |
| A school tax cap (P4.2, P15.2) | Question 2 failed in Lebanon; the city's charter cap covers only the city budget |
| Enrollment not skyrocketing (P4.3) | Right: about +6.9% since 2020-21 |
| Plainfield and Grantham crowding LHS (P14.2) | No source says so; it's Mount Lebanon that is full |

## Corrections and additions to earlier files

None needed. The library's career-center CSV matches the Hartford center's guide.

## Library notes (for review, not applied)

- **`early-college-at-your-high-school` 5 and `dual-enrollment-rules` 7** (two free Early College courses a year) differ from Lebanon High's page on what families pay.
- **NH DOE's 2024-25 foster care contact list** (in Rochester's raw files) names a Lebanon contact no longer on the Student Services page.

## Site data issue

The site's class size for Lebanon Middle School in 2024 is 114.5, against 15–24 in every other year. Logged as item 12 in `../recommended-improvements.md` (A8).

## Browser pass

The agents' blocked pages were:
- Ledyard Charter's site (HTTP 403);
- the board policies (script-only);
- the LMS bell schedule (HTTP 401);
- the Title I plans folder (private);
- the city charter site.

None is essential to the answers.
