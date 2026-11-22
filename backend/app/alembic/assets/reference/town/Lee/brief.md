# Lee Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Lee and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Lee/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Lee

- **Lee** is a town in Strafford County west of Durham, on Routes 4, 125 and 155. Site town id 297.
- **The Oyster River Cooperative School District** (site district id 423) is **SAU 5**, for Durham, Lee and Madbury. Mast Way (22805), K–4, is in Lee; Moharimet (26660), K–4, is in Madbury; Oyster River Middle (5–8) and High (9–12) are in Durham. Check how Lee children are assigned between Mast Way and Moharimet (P6.3).
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 688 (2014-15), 709 (2019-20), 719 (2025-26); cost per pupil FY2025 Oyster River $23,921, state $22,699; 2025 tax rates per $1,000 (Lee): total $27.61, local school $18.29, municipal $5.45; Question 2: Lee 55.3% yes, not adopted in Oyster River (unofficial); math proficiency 2026: Oyster River 69%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Oyster River's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Oyster River Coop)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Mast Way:** drop-off and pickup (P1.1); bus routes and rides from far Lee (P1.2, P9.1); overcrowding (P6.1); pre-K (P6.2); Mast Way or Moharimet (P6.3); the building's age (P8.1); a late bus (P9.3); outdoor and farm programs (P9.2).
- **Middle and high school:** UNH classes (P3.1); CTE and its buses (P4.1, P4.2); AP (P10.1); Barrington's students (P10.2); competency grading (P11.1); 5th-grade class sizes (P15.3); a 4:30 late bus (P17.2).
- **Money:** budget and enrollment (P2.1); the failed tax cap (P2.2); spending against other towns (P2.3); the superintendent search (P3.3); Lee's share (P8.2); a $1.3 million increase (P16.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Durham/` (elementary-and-early-years.md, middle-and-high-school.md, support-and-choices.md, money-and-governance.md) | Oyster River's schools, assignment policy, buses, CTE, UNH courses, support, choices, budget, votes and the superintendent search. |
| `town/Barrington/` | Barrington's tuition students at Oyster River (P10.2). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Danville, Sandown, Brookline and Henniker (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Oyster River Coop` for Mast Way and any new district-wide fact.
- `sau 5` for SAU-wide facts.
- `town Lee` for town government, recreation, taxes and community programs.
- No place for general NH rules.

All agents write in `town/Lee/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school to agent 3; support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Mast Way and families in Lee: drop-off and pickup, bus routes and rides, early reading help, Mast Way or Moharimet, class sizes, pre-K, early releases and delays, help with costs, reaching teachers, outdoor and farm programs, late buses, screen time, the same service across neighborhoods, summer programs | `mast-way-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P9.1, P9.2, P9.3, P11.3, P14.1, P14.2 |
| 2 | Support and choices: one-on-one help, inclusion, parents without the portal, counseling, after-school tutoring, homeschoolers in sports, homeschool paperwork, returning for 9th grade, fair treatment, mid-year moves and out-of-state credits, military families, English learners, translation, diversity | `support-and-choices.md` | `raw/support/` | P5.2, P5.3, P12.1, P12.2, P12.3, P13.1, P13.2, P13.3, P14.3, P18.1, P18.2, P18.3, P20.1, P20.2, P20.3 |
| 3 | Oyster River Middle and High from Lee: UNH classes, advanced math, CTE and its buses, the trades, the move to the middle school, AP, Barrington's students, counselors, competency grading, math acceleration, clubs, 5th-grade class sizes, work readiness, internships, sports and late buses, practical classes, adult education | `middle-and-high-school.md` | `raw/high/` | P3.1, P3.2, P4.1, P4.2, P4.3, P5.1, P10.1, P10.2, P10.3, P11.1, P15.1, P15.2, P15.3, P16.2, P16.3, P17.1, P17.2, P19.1, P19.3 |
| 4 | Money and governance from Lee: the budget and enrollment, the failed tax cap, spending against other towns, the superintendent search, Mast Way's building, Lee's share, test results since new buildings, school comparisons, the $1.3 million increase, fields and gyms, where to find election information | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P3.3, P8.1, P8.2, P8.3, P11.2, P16.1, P17.3, P19.2 |
