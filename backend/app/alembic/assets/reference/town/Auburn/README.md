# Auburn: Research for Ask NH Education Facts

Cited facts and figures for answering Auburn, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the second ToLoad batch. Auburn is in SAU 15 with Candia and Hooksett:
- **Auburn Village School (AVS)** serves preschool to grade 8.
- **High school:** students attend Pinkerton Academy in Derry under a 20-year tuition agreement from 2013, which extends automatically.

The district votes by official ballot. Pinkerton was researched in `../pinkerton/` and Hooksett's side of SAU 15 in `../Hooksett/`. These files add Auburn's side, and place Pinkerton and SAU 15 facts for Candia and Chester to reuse.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `avs-early-grades-and-families.md` | New Morning's care at AVS (7:00–6:00; $11 and $22 a day; rolling registration), five early-release days, scores (65% math, 67% reading in 2026), class sizes (grades 1–2 above the new 18-to-1 guideline), buses (elementary from 7:47; middle school from 6:43; a one-mile rule), full-day kindergarten (no tuition posted), the PEEP preschool ($300 a month), volunteer checks, an SRO under discussion | 15 | 85 | 2 | 20 MB |
| `avs-middle-grades-support-and-choices.md` | Paras (25 in special education, 12 from an agency; 9 of 18 district jobs filled), no woodshop or life-skills class, phones off, homeschool and EFA access (a revised JJJ at first reading), Algebra I in grade 8 (17 students), the August 2026 bullying policy, band, the ELL teacher on a para line, the FY28 cut list | 11 | 105 | 3 | 22 MB |
| `pinkerton-from-auburn.md` | Pinkerton's size (2,891 to 2,988), registration rather than application, a third Pinkerton bus (pickups from 6:13), no late bus, IEPs (Auburn stays responsible), CTE with no residency priority, AP by prerequisite, parking (no permits for sophomores), out-of-state credits case by case, 299 of 319 Auburn high schoolers at Pinkerton | 6 | 44 | 2 | 11 MB |
| `money-and-governance.md` | Cost per pupil ($14,653 in 2024-25), the cap (adopted; about $467,000 to cut; a $757,570 list led by high school buses), the 2026 rate ($14.93; school $10.86), 29.2% of the budget to Pinkerton, the transcribed Pinkerton agreement, SAU 15's split (Auburn 28.45%, Candia 13.66%, Hooksett 57.89%), median income | 9 | 49 | 7 | 20 MB |
| **Total** | | **41** | **283** | **14** | **73 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.95 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Auburn`). All 14 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 38 full, 21 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Auburn` 257, `district Pinkerton Academy` 12, `town Auburn` 11, `sau 15` 3.
- **Pending facts:** 12, citing draft minutes and the 2027-28 draft budget.
- **Raw folders:** each under 100 MB. The bus sheet's house-number stops were removed before saving, and the original wasn't kept. The address scan finds no home stops. Later, the main session also removed graduates' names and residents' births, marriages and deaths from the saved 2025 town report texts, and deleted that PDF.
- **Quotes:** 584 of 699 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $14.93, and school $10.86 | The town's tax rate page |
  | SAU 15's split, 28.45% for Auburn | The town's 2025 report |

## Premises checked

| Question says | What the sources show |
|---|---|
| A care waitlist (P1.1) | Not supported: rolling registration, openings listed |
| Monthly early release (P1.2) | Five days a year |
| About 59% proficient (P4.2) | Out of date: 65% and 67% in 2026 |
| A bus before 7:15 for a kindergartner (P7.1) | No: elementary pickups from 7:47 |
| Kindergarten tuition (P10.1) | None posted |
| No public preschool (P10.2) | There is one: PEEP |
| Positions sitting open (P5.2) | Partly: agency paras fill district vacancies |
| Woodshop (P6.3) | None |
| 8th-grade Algebra for credit (P13.3) | One class; credit needs prior approval |
| A 3,200-student Pinkerton (P2.1) | Too high: 2,891 to 2,988 |
| Pinkerton runs the buses (P2.2) | No: Auburn contracts First Student |
| A late bus (P2.3, P20.3) | None |
| Applying to Pinkerton (P4.1) | Auburn residents register |
| Derry students first for CTE (P6.2) | No residency priority published |
| About $15,135 per student (P3.2) | That was 2023-24; $14,653 in 2024-25 |
| A cap passing (P3.3) | It passed (61.8%) |
| Students sent to Hooksett (P10.3) | No |
| Median income over $150,000 (P17.2) | About right, within the margin of error |

## Corrections and additions to earlier files

- **Hooksett** (`../Hooksett/`):
  - Its money file didn't find SAU 15's apportionment. It is 28.45 / 13.66 / 57.89 for 2024-25, and both towns' payments match.
  - New Morning's rates and its lack of early-release coverage match Hooksett's.
  - A Hooksett board chair's report gives the out-of-district cap as 10%; the Auburn agreement says 5%.
- **Pinkerton** (`../pinkerton/`): its admissions page now says the fall open house was postponed.

## Library notes (for review, not applied)

- **Auburn `district-preschool` 4:** the PEEP handbook does say $300 a month, invoiced monthly.
- **Auburn budget-form fact 6:** the 2026 ballot was March 10, 2026 (the budget passed 756 to 551).
- **Auburn high-school-tuition-options fact 7:** the agreement's terms are now transcribed in `raw/money/contracts/`.

## Browser pass

Not needed for the answers. Not retrieved:
- www.sau15.net (HTTP 403) and the AVS news feed (Cloudflare);
- the Town of Auburn's site (didn't resolve);
- older town reports on UNH's repository;
- NH DOE's gifted and complaint pages.
