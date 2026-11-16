# Derry: Research for Ask NH Education Facts

Cited facts and figures for answering Derry, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 30 resident profiles with 3 questions each, numbered P1.1 to P30.3 in `questions.md`; the people are invented. The research is in the five files below and the two shared Pinkerton files in `../pinkerton/`, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Manchester, Nashua, Concord, Dover and Salem. Derry is SAU 10: the Derry Cooperative School District runs four K–4 elementary schools, West Running Brook (grades 5–6), Gilbert H. Hood Middle School (7–8) and the DEEP preschool. Its high school students attend **Pinkerton Academy**, a private academy that also serves Auburn, Candia, Chester, Hampstead, Hooksett and Fremont, so its facts went to the shared folder `../pinkerton/` for those towns to reuse.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | DEEP (tuition, 142 children, a fifth classroom), class sizes, kindergarten overflow, early release days cut from six to two, Grinnell and Barka results against income, enrichment, homework and devices, playgrounds, English learners, behavior support, the bullying policy rewrite | 11 | 80 | 3 | `raw/elementary/` (22 MB) |
| `grades-5-to-8-and-staff.md` | PACE acceleration (math grades 4–8, Algebra I in grade 8), computer science, homeschool access and Derry's outdated home education policy, the AI policy, para pay and the bus contractor, counselors, recess | 9 | 75 | 3 | `raw/grades5-8/` (8.5 MB) |
| `getting-to-school-and-safety.md` | The 8:50 elementary start and three-tier bus plan, posted routes and ride times, no late buses, before-school care, snow days, no SROs this fall, security grants, emergency messages | 7 | 72 | 2 | `raw/daily/` (50 MB) |
| `families-and-choices.md` | The parent portal, meal prices and unpaid balances, translation, Next Charter (Derry seats, enrollment, the Pinkerton partnership, no buses), fees, public comment, nurses, conferences, in-district transfers, substitutes | 12 | 105 | 3 | `raw/families/` (11 MB) |
| `money-and-governance.md` | The $113.4 million budget, the 2025 facilities bond, the Pinkerton contract and trustees, Question 2 and the draft 2027-28 budget, taxes against inflation, Next Charter tuition, the four elementary schools, voting and turnout, elderly exemptions, the new law on a town school department | 9 | 78 | 9 | `raw/money/` (23 MB) |
| **Total (Derry folder)** | | **48** | **410** | **20** | **115 MB** |
| `../pinkerton/pinkerton-academics-and-pathways.md` | Counselors and senior meetings, honors placement, CTE programs and applications, agriscience, dual enrollment and its limits, personal finance from the class of 2028, college outcomes and AP scores, the PACE adult diploma, Derry's adult studies center | 7 | 74 | 4 | `../pinkerton/raw/academics/` (76 MB) |
| `../pinkerton/pinkerton-student-life.md` | Special education with sending districts, the start time committee, phones and vaping, attendance rules, parking, mental health and drug prevention, clubs and intramurals, alternative programs | 10 | 121 | 5 | `../pinkerton/raw/life/` (42 MB) |

`brief.md` is the brief the research agents worked from. Seven agents used about 3.6 million tokens.

## Checks

- **Parser:** all seven files pass the backend's parser (`tools/check_town.sh Derry` and `pinkerton`). Every table is linked to a topic.
- **Topics:** every topic matches `../shared-topics.md`; none was new.
- **Places:** Derry folder: `district Derry Cooperative` 338, `town Derry` 25, `district Next Charter School` 24, `district Pinkerton Academy` 15, no place 7, `district Londonderry` 1. Pinkerton folder: `district Pinkerton Academy` 179, `district Derry Cooperative` 9, no place 5, `town Derry` 2.
- **Draft facts:** three, the draft 2027-28 budget figures, which carry an earlier review date.
- **Raw folders:** all under 100 MB.
- **Spot checks,** checked again here against the raw copies, all matched:

  | Fact | Checked against |
  |---|---|
  | The 2026-27 budget of $113,427,524 (default $113,765,475) | 2026 election results |
  | The 2025 facilities bond: $24,601,951 at 3.94%, 2026–2040 | 2025 annual report |
  | Pinkerton's 14 listed trustees, 4 from Derry | Pinkerton's board page |
  | Elementary hours 8:50–3:10 | Grinnell handbook, 2026-27 |
  | Pinkerton's day, 7:15–1:58 | Start time committee presentation |
  | Early release days September 23 and May 18 | 2026-27 calendar |

  Note: one Pinkerton fact quotes its "eighteen-member Board of Trustees", while its 2026-27 list shows 14; both are cited as written.

## Premises checked

| Question says | What the sources show |
|---|---|
| The elementary start "pushed to 8:50" (P1.1) | Correct: the board voted April 14, 2026 (from 8:35), with grades 5–8 starting 40 minutes later |
| A DEEP waitlist (P1.2) | IEP children come first and others as space allows; 142 children on October 1, 2026 and a fifth classroom; no waitlist is published; 2025-26 tuition was $1,700 or $2,100 a year |
| "So many early release days" (P6.2) | Cut from six (2025-26) to two plus two half days (2026-27) |
| Grinnell and Barka differ (P10.1) | Barka's proficiency was higher every year 2022–2026; Grinnell's growth was higher in 2025 and 2026, and Grinnell has more low-income students (32% against 20%) |
| Barka's playground falling behind (P10.3) | The equipment is in good condition; the surfacing needs $150,000 of work |
| "The budget jumped to $113 million" (P2.1) | Correct: $113,427,524, up 8.79%, while enrollment fell 22% |
| Millions in building repairs (P2.2) | Correct: the 2025 facilities bond is $24.6 million at 3.94% through 2040; about $10 million was unspent in September 2026 |
| No say over Pinkerton (P2.3) | Partly: sending towns hold trustee seats by contract (4 of 14 from Derry), but Pinkerton's trustees turned down contract changes giving sending towns more input |
| Another tax hike from the bond (P4.2) | Mostly already in the budget: payments peak in 2026-27 and shrink after |
| "The $110 million budget cap" (P12.2) | An amendment at the deliberative session; it failed |
| Taxes "faster than inflation" (P15.1) | For the total raised: the local school tax rose 64% from 2015 to 2025 against 33% for prices, though the rate fell |
| Who pays for Next Charter (P15.2) | Derry pays tuition for its own students ($11,568.61 each in 2026-27); the state pays for students from other towns |
| Four elementary schools (P15.3) | Correct |
| Voting at Pinkerton's gym (P25.1) | Correct |
| "Annual homeschool evaluations" (P9.2) | Repealed July 1, 2026; Derry's January 2022 policy still describes them |
| Homeschoolers in Hood sports (P9.1) | Correct |
| "The middle schools" (P14.2) | One intermediate school (5–6) and one middle school (7–8); no accelerated science and no pre-AP before Pinkerton |
| Banning AI (P20.3) | Wrong: the board adopted a policy on October 13, 2026 allowing approved tools |
| Free lunch for everyone (P7.2) | Not free: lunch is $3.10–$3.30, with unpaid balances of $24,369.65 |
| Evening conferences (P26.3) | Conferences are a daytime no-school day (November 10, 2026) |
| Nurses split between buildings (P22.3) | The handbook says every school has a full-time registered nurse |
| A late bus or a stop on Crystal Ave (P5.3) | No late or activity bus, and no Crystal Ave stop |
| Crossing guards near Grinnell (P11.2) | Not supported by any source found |
| Remote learning on snow days (P16.2) | Allowed, but none was used; the March 6, 2026 closure was a regular one |
| SROs in every building (P18.1) | None currently, because of police staffing (September 22, 2026) |
| Bus rides of "almost an hour" (P21.2) | The longest scheduled rides are 42 minutes in the morning and 47 in the afternoon |
| No bus to Next Charter (P17.3) | Correct: Next runs no buses, and Derry posts no route |
| "A crowd of 3,200 kids" at Pinkerton (P8.1) | High: 2,891 in 2024-25 (site), about 3,100 by Pinkerton's count; it last topped 3,200 in 2018-19 |
| A 6:00 a.m. bus to Pinkerton (P30.1) | Correct: first pickups run 5:45–6:03 for a 7:15 start |
| Automotive and welding at Pinkerton (P8.2) | Both exist and need an application; area schools share the welding seats |
| Placement testing at Pinkerton (P9.3) | No general placement test, only a math test for Honors Algebra 2 |
| Adult certificate classes at Pinkerton (P13.2) | Its afternoon PACE program (2–6 p.m.) leads to an adult diploma; SAU 10's Derry Center for Adult Studies offers free HiSET and English classes |
| Personal finance at Pinkerton (P23.1) | Required only from the class of 2028 |
| Pinkerton's agriculture and forestry (P21.1) | Ten agriscience courses in 2025-26 and 2026-27; no forestry course |
| Switching to an alternative program mid-year (P30.3) | Partly: the adult diploma program's second semester starts February 1, 2027, and the Academy Learning Community has a waiting list |

## Corrections and additions to earlier files

None were needed; nothing here contradicts an earlier town. Jackson's file has the same AI policy code (EHAG), adopted December 15, 2025; Derry's version adds a public list of approved tools.

## Coverage

34 questions are answered **fully** and 56 **partly**; none has nothing. Questions about Pinkerton are answered in `../pinkerton/`.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Danielle Mercer | partial | partial | partial |
| P2 Tom Callahan | **full** | **full** | partial |
| P3 Priya Patel | partial | partial | partial |
| P4 Marcus Vance | partial | **full** | **full** |
| P5 Brenda Kowalski | **full** | **full** | partial |
| P6 Greg & Heather Lindqvist | partial | partial | **full** |
| P7 Eleanor "Ellie" Thibodeau | **full** | **full** | partial |
| P8 Javier Morales | **full** | partial | **full** |
| P9 Sarah Jenkins | partial | **full** | **full** |
| P10 Kevin O'Connor | **full** | partial | partial |
| P11 Amina Hassan | partial | partial | partial |
| P12 Bradford "Brad" Sterling | partial | partial | **full** |
| P13 Chloe Deschamps | partial | partial | partial |
| P14 Dr. Samira Al-Mansoor | partial | **full** | partial |
| P15 Dale & Cindy Perkins | **full** | **full** | **full** |
| P16 Tyler Brooks | partial | **full** | partial |
| P17 Megan Flanagan | partial | partial | partial |
| P18 Arthur "Artie" Rossi | **full** | partial | partial |
| P19 Nina Lindstrom | partial | partial | **full** |
| P20 Derek Washington | partial | partial | **full** |
| P21 Lori & Pete Henderson | partial | partial | **full** |
| P22 Kayla Nguyen | **full** | **full** | **full** |
| P23 Connor MacLeod | **full** | partial | partial |
| P24 Rebecca "Becca" Alvarez | partial | partial | partial |
| P25 Harold "Hal" Zimmerman | partial | **full** | **full** |
| P26 Tasha Williams | partial | partial | partial |
| P27 Owen & Maya Gallagher | **full** | partial | partial |
| P28 Pastor David Cho | partial | **full** | partial |
| P29 Stephanie "Steph" Bouchard | partial | partial | partial |
| P30 Raymond "Ray" Cote | **full** | **full** | partial |

## Notable findings

- **No school resource officers this fall,** because of police staffing, though the town budgeted officers for Pinkerton, West Running Brook and Hood.
- **Question 2 passed in Derry (65%),** and the district estimates its draft 2027-28 budget is about $2.5 million over the new cap.
- **A new 2026 state law** lets the Derry Town Council propose making the school district a town department, by a charter amendment voters would decide.
- **Pinkerton and special education:** the sending district, not Pinkerton, holds the district seat at IEP meetings, approves changes and pays for services beyond the contract.
- **Turnout:** 8.8% at the March 2026 school vote, against 12,677 ballots in November.

## Site data issues found

- The site's school enrollment totals for Derry are too low before 2024-25: the closed West Running Brook Middle School and Derry Village School have no rows (A10 in `../recommended-improvements.md`).

## Library notes (not changed here)

- `district-preschool` 23 (note): says DEEP's tuition wasn't found, but DEEP's notices page in the library's own `raw/districts/batch-3/` gives it ($1,700 or $2,100 in 2025-26).
- `kindergarten-entry-cutoff` 21: the 2026-27 handbook adds that first graders must be six by September 30.
- `high-school-tuition-options` 22 (note): the district, not the town, pays Pinkerton tuition.
- `budget-question-2-2026-results`: the Town of Derry's own return (7,772 yes, 4,189 no) matches the site's figures.

## Gaps to retry

- **Not posted online:** the Derry–Pinkerton agreement and Derry's agreement with Next Charter.
- **Blocked to automated requests or timed out:** sau10.nh.gov (5 pages), pinkertonacademy.org (5), Google Drive documents (9), NH DOE's iReport (school report cards).
- Not found anywhere: deliberative session minutes and attendance; the West Running Brook drop-off study; measured bus ride times; before-care rates; specials minutes; how PACE students are chosen; counselor wait times; teacher turnover; whether Next students can take Pinkerton AP courses.

The shared web search limit was used up before most Derry agents started, so nearly all sources came from direct visits to known sites.
