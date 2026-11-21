# Berlin Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Berlin and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Berlin/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Berlin

- **Berlin** is a small city in Coös County on the Androscoggin River, a former paper-mill city. Site town id 51.
- **The Berlin School District** (site district id 51) is **SAU 3**, a one-district SAU. Its schools: Berlin Elementary (27035), preschool to grade 5; Berlin Middle (20045), grades 6–8; Berlin Senior High (20050), grades 9–12. Check whether the middle and high schools share one building (P2.1), the career center's name and programs, and how the City Council approves the school budget (P19.2).
- **Tuition and neighbors:** Dummer and Milan send grades 7–12 to Berlin (`places.yaml`). Gorham (the Gorham Randolph Shelburne Cooperative, site district id 203) and White Mountains Regional (568, in Whitefield) are nearby districts with their own programs (P6.2, P8.3, P18.2).
- **Starting pages:** SAU 3, https://www.sau3.org (check); the city, https://www.berlinnh.gov (check); White Mountains Community College, https://www.wmcc.edu.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,136 (2014-15), 1,019 (2019-20), 918 (2025-26); cost per pupil FY2025 Berlin $24,101, state $22,699; 2025 tax rates per $1,000: total $33.60, local school $12.66, municipal $16.20; Question 2: Berlin 63.9% (check whether it applies to a city district); math proficiency 2026: Berlin 23%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Berlin's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Berlin)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** Project Youth until 5:45 (P1.1); busing eligibility (P1.2); full-day pre-K spots (P3.1); free meals for everyone (P5.1); a crossing guard near State Street (P5.2); grades 6–12 in one building (P2.1); about a quarter of middle schoolers proficient (P2.3); French and North Country history (P4.2); an "Enrichment" referral (P11.2); Northern Human Services transition plans (P11.3).
- **Career and college:** welding and automotive certifications (P6.1); a heavy-equipment program at White Mountains Regional (P6.2); free Early College at WMCC and $150 dual enrollment (P7.1, P7.2); a WMCC early childhood agreement (P9.1); Berlin and Gorham sharing CTE (P8.3).
- **Money:** paraprofessionals quitting for better pay (P9.2); population loss since the mills closed (P16.1); administrators (P16.3); adequacy court rulings (P17.1); unfilled positions (P17.2); vacant school buildings (P17.3); a tax cap (P18.3); the City Council's vote (P19.2); cost per student against Gorham and Groveton (P19.1).
- **Home education:** "annual portfolios" (P12.2; the yearly evaluation was repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Conway/` and the shared `town/sau9/` | Another North Country district and its career center, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Claremont, Lebanon, Hanover and Swanzey (this wave), and Belmont, Gilford, Meredith, Franklin and Plymouth (queued). Don't write facts about those towns.

## Where facts go

- `district Berlin` for SAU 3, its schools, the career center, policies, staff, budget, board and tuition contracts.
- `district Gorham Randolph Shelburne Cooperative` and `district White Mountains Regional` only for their own programs.
- `town Berlin` for city government, the City Council, recreation (Project Youth) and taxes.
- No place for general NH rules.

All agents write in `town/Berlin/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, staffing and governance belong to agent 4; the career center and college courses to agent 3; the middle and high school academics and support to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Berlin Elementary and families: care after Project Youth, busing eligibility, Title I reading, pre-K, academics for families moving in, storm notices, pickups in storms, meals, crossing guards, family events, speech therapy, enrollment with a caregiver letter, food bags, counselors, advanced learners, daycares | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.2, P3.3, P4.1, P5.1, P5.2, P5.3, P11.1, P13.1, P13.2, P13.3, P14.1, P20.2 |
| 2 | Berlin Middle and High: one building for grades 6–12, sports, middle school scores, French and local history, AP not offered, enrichment referrals, transition plans, EFAs and homeschooling, bullying, private school options, credit recovery, truancy, half-day schedules, comparing scores | `middle-high-and-support.md` | `raw/middle/` | P2.1, P2.2, P2.3, P4.2, P4.3, P11.2, P11.3, P12.1, P12.2, P14.2, P14.3, P15.1, P15.2, P15.3, P20.3 |
| 3 | The career center and college courses: welding and automotive certifications, White Mountains Regional's programs, credit for work, Early College at WMCC, dual enrollment costs, shop skills, business sponsors, Berlin–Gorham sharing, early childhood pathways, the starting grade for CTE, financial literacy, coding and IT | `career-center-and-college.md` | `raw/high/` | P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P9.1, P10.1, P10.2, P10.3 |
| 4 | Money and governance: paraprofessional pay and tuition help, EFA effects on aid, population and budgets, the school share of taxes, administrators, adequacy rulings, unfilled positions, vacant buildings, young families, partnering with Gorham, a tax cap, cost per student, the City Council's role, budget drivers, the schools' future | `money-and-governance.md` | `raw/money/` | P9.2, P9.3, P12.3, P16.1, P16.2, P16.3, P17.1, P17.2, P17.3, P18.1, P18.2, P18.3, P19.1, P19.2, P19.3, P20.1 |
