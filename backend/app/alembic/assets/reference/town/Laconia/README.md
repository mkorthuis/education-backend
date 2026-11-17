# Laconia: Research for Ask NH Education Facts

Cited facts and figures for answering Laconia, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the four files below, in the reference library's format, ready to load but not loaded.

Gathered November 16, 2026, alongside Hudson, Bedford, Keene, Portsmouth and Goffstown. Laconia is SAU 30, a one-district SAU: Elm Street, Pleasant Street and Woodland Heights for preschool to grade 5, Laconia Middle School (6–8) and Laconia High School (9–12) with the Huot Technical Center, a regional career center. The City Council adopts the school budget under the city's charter tax cap.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools-and-daily-life.md` | The preschool's paper packet, Project EXTRA (free, bused, full for 2026-27), the Boys & Girls Club's fees, hours and buses (read in the browser pass), meals on delays, the bus to the Club, Motorcycle Week and the last school days, nurses, full-day kindergarten, report cards and paper copies, summer programs, elementary zones and comparisons, teachers by grade | 19 | 94 | 1 | 22 MB |
| `high-school-and-huot.md` | Huot's programs, schedule and credits, plumbing and the apprenticeship hours, the LNA track and the Board of Nursing's approved list (read in the browser pass), Protective Services and Automotive, graduates' plans, AP and Early College, LRCC's free classes, Plymouth State transfer rules, credit recovery, counselors, phones, truancy, local wages | 11 | 94 | 4 | 19 MB |
| `student-support-and-choices.md` | Aide and speech openings, IEP contacts, policy JJJ access for home-educated, EFA and private students, Holy Trinity (full time only to grade 6), Laconia Christian's aid figures (read in the browser pass), mental health and substance use staff and the Project AWARE grant, English learners and translation, 504 plans and middle school teams, mid-quarter grade reminders, SROs, Laconia Adult Education's evening apprenticeship classes, FAFSA help | 13 | 104 | 1 | 18 MB |
| `money-staff-and-buildings.md` | The FY2027 budget (+4.4%) and the school tax (+9.78%), the charter tax cap (text read in the browser pass) and the $2.63 million debt exclusion, five unfilled teaching jobs, health insurance (+16.9%), state special education aid, Question 2 (63.6%), property value per student against the lake towns, fields and locker rooms, spending shares | 7 | 78 | 4 | 36 MB |
| **Total** | | **50** | **370** | **10** | **94 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.98 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Laconia`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 33 partial, 1 from the site's data (counted before the browser pass, which added to P1.2, P6.2, P10.1 and P11.3).
- **Topics:** one new rule topic was added to `../shared-topics.md`: `occupational-licensing-rules` (trade and LNA licenses; the library's `registered-apprenticeship-basics` covers apprenticeship programs, not licenses).
- **Places:** `district Laconia` 301, `town Laconia` 54, no place 14.
- **Places for the backend:** `places.yaml` has no Laconia rows, and none are needed: Laconia runs every grade, and Huot's sending districts are career-program arrangements.
- **Raw folders:** all under 100 MB.
- **Quotes:** 769 of 928 quoted passages found word for word in the cited raw copies.
- **Reconciled in review:** the support file's summary counted "four LHS counselors"; the counseling office lists a director and three counselors, as the high school file says. The summary now matches.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The FY2027 school budget, $46,237,960, up 4.4% | School board minutes, May 5, 2026; Council minutes, May 11, 2026 |
  | The school tax up $2,653,929 (9.78%) | The city's FY2027 approved budget, page 8 |
  | $2,634,559 of debt service excluded from the cap, 6-0 | Council minutes, June 22, 2026 |
  | Health insurance up 16.9% | School board minutes, November 18, 2025 |
  | Question 2: 63.6% yes | The site's Question 2 data (4,246 to 2,429) |

## Premises checked

| Question says | What the sources show |
|---|---|
| A preschool packet from Harvard Street while everything else is in Alma (P1.1) | Right; both preschool pages return 404 and no 2027-28 notice is posted |
| Meals on half-days and delays (P1.3) | No breakfast on delayed openings; lunch on 1:00 releases isn't stated |
| SAU 30 buses to Holy Trinity (P7.1) | Not shown: no route stop or policy; Holy Trinity's handbook describes family drop-off |
| Holy Trinity to Laconia Middle or High (P7.2) | Holy Trinity now runs full time only through grade 6, so students join Laconia Middle in grade 7 |
| Bike Week in June (P12.1) | Right: the June 12–20, 2027 rally overlaps the last four school days |
| Full-day kindergarten everywhere (P19.1) | Right |
| A 4.4% budget increase (P3.1) | Right for the school general fund; the school tax rose 9.78% as state aid, Medicaid money and reserve transfers fell |
| Exemptions to the tax cap (P3.2) | Partly: the Council excluded $2,634,559 of debt service for FY2027 and about $1.1 million of capital in FY2025; no override was found |
| Five teaching spots cut by attrition (P4.1, P15.2) | Right, plus six support staff changes; about 15 teacher layoffs were expected without the exclusion |
| Health insurance up nearly 17% (P15.1) | Right: 16.9% |
| The state's share of special education (P15.3) | Catastrophic aid covered about 3.6% of special education spending (derived) |
| Lake towns paying a lower rate (P20.3) | Mostly right; Alton's rate is higher than Laconia's |
| Plumbing and HVAC counting toward apprentice hours (P2.1) | Partly: finishing both levels starts a student as a second-year apprentice; school hours don't count toward the 8,000 work hours |
| The Huot block schedule (P2.3) | Right: 90 minutes a day all year; Plumbing and Heating counts as a math credit |
| An LNA license before graduating (P10.1) | Partly: through outside providers, not guaranteed; Huot isn't on the Board of Nursing's approved list |
| Running Start (P10.2) | Renamed Early College |
| Protective Services at Huot (P17.2) | A course group with Law Enforcement I–II; no firefighter or EMT certification |
| Phones locked up (P20.2) | Banned bell to bell, kept in a backpack or locker |
| A welding class at Huot for a homeschooler (P8.1) | No welding program; Digital Media Arts exists |
| Evening trade classes at Huot (P18.1) | Through Laconia Adult Education instead |
| A dedicated SRO every day (P17.1) | SROs are listed at the middle and high schools; their days aren't published |
| Aide and speech openings (P6.1) | 18 aide vacancies in August 2026; no speech opening posted |

## Corrections and additions to earlier files

- **Jackson** (`Jackson/community-and-families.md`, the private schools table): Holy Trinity School's tuition, "not found" there, is $7,900 for 2026-27 (full time PreK–grade 6); the row and the gap note now say so. Jackson is loaded locally, so the change is copied to the backend and reloaded with the batch.
- **Tamworth** (`adult-education-and-workforce-training` 7) lists Laconia Adult Education's classes; it also runs the evening electrical and plumbing apprenticeship classes (`student-support-and-choices.md`, fact 2). No change needed.

## Library corrections

Applied November 16, 2026 to both library copies (backend commit `c7c868a`), except those marked for review:

- `facts-rules-and-rights.md`, `dual-enrollment-rules` 3 calls the fit between CCSNH's "two free courses" and the law's four "unresolved." LRCC's page now says students get up to four tuition-free Early College classes a year across all formats, up to two of them on campus or online (`high-school-and-huot.md`, `early-college-on-campus` 3).

## Browser pass (November 16, 2026)

- **Read in Chrome and added:** the city charter's tax cap, section 5:03.5 (ecode360; `district-tax-and-state-aid` 1–2 now quote it); the Boys & Girls Club's Laconia fees, hours, buses and summer camp (`town-recreation-and-summer` 8–9); Laconia Christian Academy's aid figures (no tuition is posted; `town-school-options-nearby` 8); the Board of Nursing's approved nursing assistant programs (`cte-center-programs` 30).
- **Still not retrieved:** NH DRA's 2026 tax rates (a PDF the site refuses; Laconia's FY2027 estimate is used), NH DOE's October 2026 enrollment files, the district's line-item budget (an Acrobat web viewer), SchoolSpring's job board (a bot check) and the Opechee Day Camp's 2026 fees.

## For the district

A public Google Doc of the district's after-school bus routes, and one Project EXTRA schedule, list children's names. The agent didn't save the names. The district may want to know.
