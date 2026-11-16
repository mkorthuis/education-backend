# Londonderry: Research for Ask NH Education Facts

Cited facts and figures for answering Londonderry, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 30 resident profiles with 3 questions each, numbered P1.1 to P30.3 in `questions.md`; the people are invented. The research is in the seven files below, in the reference library's format, and isn't loaded into the Ask yet.

Gathered November 15, 2026, alongside Dover, Salem, Rochester and Merrimack. Londonderry is SAU 12: Moose Hill School (the LEEP preschool), three elementary schools for kindergarten to grade 5 (Matthew Thornton, North and South, with full-day kindergarten from 2026-27), Londonderry Middle School, Londonderry High School and Lancer Academy (opened at the high school in 2026-27). Hooksett students may attend the high school by petition. Londonderry is a charter school district: voters choose the board's budget (A) or the default (B) on one ballot question. Its tax cap question failed on November 3, 2026 (51.9%, short of 60%). **The district offices haven't moved into Moose Hill:** voters approved a Town Hall addition in 2026, and the offices stay in rented space until about July 2027.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools.md` | Full-day kindergarten and where its classrooms are (the portables went to Matthew Thornton, not South), the YMCA's waitlists at South, class sizes (South's grade 1 averages 24.7; kindergarten capped at 18), i-Ready and Acadience, LEEP from age 3, its peer lottery and 2026-27 tuition, a proposed full-day preschool, screen time in grade 2, extended school year | 9 | 63 | 2 | `raw/elementary/` (44 MB) |
| `middle-school-and-activities.md` | Bullying policy and investigation counts, office referral trends, the phone rule and 497 phone detentions at the high school, team cuts and the number of middle school teams, fees and hardship help, Unified sports and courses, arts on the tax cap cut list, cursive, multiplication tables and civics laws | 9 | 92 | 4 | `raw/middle/` (46 MB) |
| `high-school-and-pathways.md` | CTE at MST and the Palmer Center (and the budget book's "now Pinkerton"), AP exams and pass rates, courses dropped from the 2026-27 catalog, canceled sections, Open Campus limited to study halls, SAT and college plans against Pinkerton and Bedford, counselors per student, 22 charter and private high schools nearby, excused college visits | 7 | 80 | 6 | `raw/high/` (20 MB) |
| `student-support-and-health.md` | Speech staff and aide hours, aides moved to Matthew Thornton, nurses in every building, nut-free kitchens but no nut-free classroom rule, menu labels and meatless days, confidential free meals and meal debt, Resource and Lancer Lab study skills courses, 504 plans, counselors, ESL, guardianship paperwork | 9 | 94 | 4 | `raw/support/` (35 MB) |
| `getting-to-school-and-choices.md` | Midday kindergarten runs cut (about $280,000 saved), morning pickup windows, the street lookup and kindergarten overflow, bell times, home education under IHBG (still describing repealed evaluations), JJJ access, EFAs, snow alerts by text, drills and emergency notices, data privacy, board meeting video lengths | 9 | 77 | 2 | `raw/daily/` (22 MB) |
| `budget-and-governance.md` | The failed tax cap and what a cap would have cut, the A/B ballot and its history (the board's budget won 7 of 8), the budget ($95.9 million voted), health premiums and positions cut, the school share of the tax bill (71.6%), rates against Derry and Hudson, Hooksett's tuition, adequacy aid, surplus to the tax rate, escrow | 7 | 75 | 6 | `raw/money/` (30 MB) |
| `buildings-and-staff.md` | The failed 2025 Moose Hill office bond, the 2026 Town Hall addition and the Kitty Hawk rent, the 2025–2028 teachers' contract, support staff raises, para and substitute pay and vacancies, portables at Matthew Thornton and North, building needs (no bond in five years), the turf field campaign, home values against Windham and Bedford | 7 | 51 | 1 | `raw/staff/` (44 MB) |
| **Total** | | **57** | **532** | **25** | **241 MB** |

`brief.md` is the brief the research agents worked from. Seven agents used about 3.5 million tokens. The middle school agent was the costliest of any town so far (about 633,000 tokens).

## Checks

- **Parser:** all seven files pass the backend's parser (`tools/check_town.sh Londonderry`). Every table is linked to a topic.
- **Topics:** three new topics were reviewed and added to `../shared-topics.md`: `required-instruction-rules` (cursive, multiplication tables and civics time; graduation requirements stay in `graduation-requirements`), `extended-school-year-rules` and `property-tax-bills-and-escrow`.
- **Places:** `district Londonderry` 495, `town Londonderry` 15, no place 11, `district Diocese of Manchester` 2, and one each for Hooksett, Hudson (the Palmer Center), Bedford, Pinkerton Academy, the Academy for Science and Design, Next Charter, Spark Academy, The Founders Academy and The Derryfield School.
- **Places for the backend:** Hooksett's row (`places.yaml`: the 2023–2028 memorandum, up to 40 a grade, at Pinkerton's rate) matches what the agents found; nothing to change.
- **Draft facts:** two notes are flagged, both false hits on quoted words ("computer drafting", "impending").
- **Raw folders:** all under 100 MB.
- **Added in review:** `high-school-and-pathways.md` `cte-center-programs` 13, the budget book's statement that Career Connected Learning money lets students take classes "in Hudson, Manchester, and now Pinkerton" (found by the budget agent); fact 7 and the P8.2 premise now point to it.
- **Spot checks:** each agent checked 3 or more facts against its raw copies. These were checked again here, and all matched:

  | Fact | Checked against |
  |---|---|
  | The Town Hall office lease article, 3,210 to 1,211 | Town election results, March 10, 2026 (transcribed) |
  | Office rent at Kitty Hawk Landing, $230,284 | FY2027 budget book (10,175 square feet at $14.99) |
  | The teachers' contract: $1,920,879, $1,682,340, $1,647,733 | 2025 warrant, Article 4 |
  | 2025 tax rates: Londonderry $14.47, Derry $18.99, Hudson $17.11; school share 71.6% (64.13% + 7.46%) | The site's tax data; the town's November 7, 2026 budget presentation |
  | About $280,000 a year saved on midday kindergarten buses | Board minutes, August 5, 2025 |
  | 497 students with a phone detention in 2025-26 | Board packet, July 14, 2026 |
  | LEEP tuition: $160, $190 and $210 a month | LEEP 2026-27 tuition sheet |

## Premises checked

| Question says | What the sources show |
|---|---|
| The school tax cap just failed (P6.1) | Right: 51.9% yes, short of 60%; no state cap for 2027-28 or 2028-29 |
| A budget "climbing toward $100 million" with flat enrollment (P6.2) | Partly: the operating budget is $94.75 million; enrollment is falling, from 4,120 to 3,843 |
| District offices moved into Moose Hill to save lease money (P6.3, P7.3, P23.1) | Wrong: the 2025 Moose Hill office bond failed (56.5%, needing 60%); in 2026 voters approved a $3.9 million office addition at Town Hall, leased from the Town and built without a bond. The offices stay at Kitty Hawk Landing ($230,284 rent in FY2027) until about July 1, 2027, so no savings yet. Moose Hill is LEEP plus storage |
| A $1.6 million jump in the teachers' contract (P10.1) | Close: $1,920,879, then $1,682,340, then $1,647,733 |
| Higher taxes than Derry or Hudson (P9.1) | Wrong on rates: Londonderry $14.47 in 2025, Derry $18.99, Hudson $17.11 |
| A Friday or Saturday deliberative session (P10.2) | Both: the school session is a Friday evening, the town's a Saturday morning |
| What Hooksett pays (P10.3) | Its Pinkerton rate, about 80% of the high school's cost per pupil (about $1.31 million a year) |
| Schools are three-quarters of the tax bill (P13.1) | Close: 71.6% in 2025 |
| "The $96 million school budget" (P13.2) | Close: $95,885,819 with the board's special articles |
| Fights over default budgets every March (P18.2) | Wrong: the board's budget won 7 of 8 votes; the default won only in 2020 |
| Cutting $1–2 million (P23.3) | Only under the cap, which failed; the district's cap list included buses, AP sections, clubs, electives and arts |
| Budget workshops in November and December (P24.3) | Mostly December and January |
| New modular classrooms at South (P1.1, P19.3) | Wrong: South's kindergarten is in existing rooms; Moose Hill's two portables went to Matthew Thornton, and North has a leased modular |
| Midday kindergarten runs cut (P1.3) | Right: about $280,000 a year saved; no on-time figures are published |
| First graders behind on i-Ready (P3.1) | The district did say so; full-day kindergarten's first class takes the grade 1 test in fall 2027 |
| Matthew Thornton is the biggest (P3.2) | Right (643 students), but South's grades 1 and 2 have the largest classes |
| LEEP before age 4 (P7.1) | LEEP takes children from age 3 |
| A small lottery for peers (P27.1) | Right; peers must also be toilet trained and have clear speech |
| A class-size cap for grades 1–5 (P22.2) | None in policy or the teachers' contract; kindergarten is capped at 18 |
| CTE "at Pinkerton or Manchester" (P8.2) | Manchester yes (MST, with district buses), and the Palmer Center in Hudson; Pinkerton is unclear: the catalog and handbook don't name it and Pinkerton's area page doesn't list Londonderry, but the budget book says "and now Pinkerton" |
| Open Campus tightened for juniors and seniors (P5.3, P14.1) | Partly: the 2026-27 handbook limits it to non-credit study halls; no reason was published |
| Families leaving for the Academy for Science and Design (P5.2) | Can't be measured |
| AP and computer science sections canceled (P14.2) | Allowed for low enrollment but never counted; 15–16 AP courses ran each year against 22–23 in the catalog |
| Family commitments and college visits excused (P28.2) | Only senior college visits, up to 5 a year |
| Annual homeschool evaluations (P15.3) | Out of date: repealed July 1, 2026, but the district's page and policy IHBG still describe them |
| Two different drop-offs (P17.1) | Right: the middle school starts at 7:44; elementary drop-off is 8:30–8:42 |
| Drop-off early enough for I-93 by 7:30 (P2.3) | School drop-off opens at 8:30; YMCA before-care is the only earlier option |
| Three hours of procedure at board meetings (P29.3) | The 15 regular meetings streamed in 2026 had a median of 1 hour 33 minutes |
| Adaptive PE (P21.1) | Unified sports and courses exist; no adaptive PE program is named |
| Arts cut first (P21.2) | Not supported: arts were on the cap cut list alongside buses, AP and administration, in no order |
| Cuts unless club year-round; heavy middle school cuts; a big grade 5 to 6 workload jump (P8.3, P26.1, P4.2) | Can't be measured |
| Everything on tablets (P30.2) | Partly; state law has required cursive since 2023 |
| Co-taught classes at the high school (P12.2) | No co-taught label at the high school; team-taught at the middle school |
| A full-time RN in every building (P20.2) | Every building has budgeted nursing (2 FTE at four schools), but full-time RN status isn't confirmed |
| Nut-free classrooms (P20.1) | Elementary kitchens are nut-free; no rule makes classrooms nut-free |
| Social workers in elementary schools (P25.2) | None; one is shared by the middle and high schools |

## Corrections and additions to earlier files

None to earlier towns. The Manchester file lists Londonderry as an MST sending school; this town adds the Palmer Center as the second partner. **A caution for comparisons:** Pinkerton's "88% pass rate" for AP (Pinkerton file) and Londonderry's "75% of AP students" use different definitions, so they shouldn't be set side by side without saying so.

## Library corrections (made November 15, 2026)

Both copies of `district-practices.md` (`additional-data/` and the backend's `assets/reference/`) were corrected; the raw copies were added to `additional-data/raw/districts/batch-4/`:
- `district-preschool` 60: now gives LEEP's 2026-27 tuition ($160, $190 and $210 a month) instead of "not posted," and notes the district's own October 31 count (121) beside NH DOE's (114).
- `budget-form-and-vote-dates` 77: now says Londonderry votes under its own official ballot charter (not SB2, though it follows SB2's deadlines) with an A/B budget question, and gives the tax cap result (51.9%, short of 60%). Whether the 2026 law giving SB2 budget committees the default budget reaches a charter district is still open.

**Place names:** the site's district names for the Arts Academy of New Hampshire (and World Academy, per Nashua) end in a space; worth trimming before more towns cite them.

## Coverage

40 questions are answered **fully** and 50 **partly**; none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Jenna | partial | **full** | partial |
| P2 Marcus | partial | **full** | partial |
| P3 Carla | partial | partial | **full** |
| P4 Derek | **full** | partial | **full** |
| P5 Priya | **full** | partial | partial |
| P6 Tom | partial | **full** | **full** |
| P7 Samantha | **full** | partial | **full** |
| P8 Kevin | partial | **full** | partial |
| P9 Elena | partial | partial | partial |
| P10 Ray | partial | **full** | **full** |
| P11 Hannah | partial | **full** | **full** |
| P12 Greg | partial | partial | **full** |
| P13 Meredith | **full** | **full** | **full** |
| P14 Noah | partial | partial | partial |
| P15 Brenda | **full** | **full** | **full** |
| P16 Carlos | partial | partial | **full** |
| P17 Tricia | **full** | **full** | partial |
| P18 Ben | partial | **full** | partial |
| P19 Diane | partial | **full** | partial |
| P20 Owen | partial | partial | partial |
| P21 Lisa | partial | partial | partial |
| P22 Samir | **full** | **full** | partial |
| P23 Kelsey | **full** | **full** | partial |
| P24 Victor | **full** | **full** | partial |
| P25 Rachel | **full** | **full** | partial |
| P26 Trevor | partial | partial | partial |
| P27 Nadia | partial | **full** | partial |
| P28 Paul | partial | **full** | partial |
| P29 Amber | partial | **full** | **full** |
| P30 Bill | **full** | partial | partial |

## Notable findings

- **The offices:** two office plans failed (a new office bond in 2022 and Moose Hill in 2025) before voters approved the Town Hall lease in 2026.
- **The tax cap:** the district said a cap would have meant about a $2 million shortfall; after it failed, the superintendent still cited its "long shadow" in holding back a $0.85–1.1 million gym air-conditioning project.
- **Budgets:** health premiums (+$2.4 million) drove the 2026-27 increase, and 17.9 positions were cut over three budgets; only $150,000 of surplus goes to the 2026 tax rate, against $1.37 million the year before.
- **Phones:** 497 high school students (about 41%) got a phone detention in 2025-26, and the share with no office referral fell from 79% to 54%.
- **The catalog:** robotics, digital electronics and civil engineering courses were dropped for 2026-27, and there's no AP Computer Science A.

## Gaps to retry

- **Behind a sign-in or script:** SharePoint letters and Google Drive files (the 2022 master plan, office and kindergarten infographics), the street lookup for school zones, the middle and high school staff directories, Final Forms, the district job board.
- **Blocked:** Niche.
- **Not found anywhere:** current i-Ready results, LEEP's peer seat count, an elementary summer school, translation of report cards and IEPs, a middle-to-high-school IEP handoff procedure, an allergy procedure on buses, how the portables hold up in winter, track condition and booster spending, canceled section counts, how many Londonderry students attend ASD, private schools or each CTE program, late buses, workshop attendance, the 2026 tax rate, the 2027-28 budget (presented November 24, 2026).
