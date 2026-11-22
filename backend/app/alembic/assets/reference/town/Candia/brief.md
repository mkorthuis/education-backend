# Candia Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Candia and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Candia/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Candia

- **Candia** is a town in Rockingham County east of Manchester. Site town id 79.
- **The Candia School District** (site district id 79) is in **SAU 15** with Auburn and Hooksett. It runs the Henry W. Moore School (20535); check its grades and preschool. Check its budget form.
- **High school:** Pinkerton Academy under a 2018 tuition contract (`places.yaml`: a 20-year term to 2038, extending 5 years each July from 2023 unless notice; up to 5% may attend another public high school). Pinkerton is researched in `town/pinkerton/`; Hooksett's and Auburn's sides in `town/Hooksett/` and `town/Auburn/` (Auburn is running now).
- **Reuse first.** Much of this town's shared district or high school is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 518 (2014-15), 450 (2019-20), 421 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Henry W. Moore School 272; cost per pupil FY2025 Candia $22,249, state $22,699; 2025 tax rates per $1,000 (Candia): total $12.97, local school $8.71, municipal $2.67; Question 2: Candia 65.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Candia's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Candia)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Moore School:** full-day kindergarten (P1.1); the New Morning after-school program (P1.2); the cutoff (P1.3); scores against Auburn and Hooksett (P6.1); gym, art and music (P6.2); honors math (P9.1); public preschool (P16.1); band and theater (P20.1).
- **Pinkerton:** the bus and late bus (P3.2, P3.3); IEPs (P4.3); CTE seats (P8.1); AP as a freshman (P9.3); team cuts (P15.1); Candia's seat on the board (P10.3).
- **Money:** the tax cap and 23% health insurance (P2.1, P10.2, P19.2); Pinkerton tuition (P2.2); SAU 15 costs (P2.3); the Budget Committee and Board split (P5.2); senior exemptions (P5.3); the building (P17.1).
- **Home education and choice:** an annual homeschool assessment (P7.2; repealed July 1, 2026); EFAs at Jesse Remington (P12.2); busing private school students (P12.3).

## Already researched

| File | What it covers |
|---|---|
| `town/pinkerton/` | Pinkerton Academy: courses, CTE, counseling, student life. |
| `town/Hooksett/`, `town/Auburn/` (running now) | SAU 15 and the other towns' Pinkerton contracts. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Ossipee, Candia, Gilmanton, New Boston and North Hampton (this wave); Allenstown, Epsom, Deerfield, Auburn, Wolfeboro, Newton, Rindge, Boscawen, Barnstead and Northfield (running). Don't write facts about those towns.

## Where facts go

- `district Candia` for Moore School, the district's budget, board and its side of the Pinkerton contract.
- `district Pinkerton Academy` only for Pinkerton facts not already in `town/pinkerton/`.
- `sau 15` for SAU-wide facts not in Hooksett's or Auburn's files.
- `town Candia` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/Candia/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Moore School's early grades and families: full-day kindergarten, New Morning after-school care, the cutoff, scores against Auburn and Hooksett, gym, art and music, the ski bus and after-school sports, delays, meals, the bus company, the school's feel, guardianship enrollment, public preschool, nearby child care, kindergarten registration | `moore-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P6.1, P6.2, P6.3, P11.1, P11.2, P11.3, P13.1, P14.3, P16.1, P16.2, P16.3 |
| 2 | Moore's upper grades, support and choices: reading interventions and IEPs, paras and speech under a cap, homeschool and EFA access, co-ops, accelerated math, Jesse Remington, EFAs and private school busing, bullying, phones, counseling, catching up mid-year, 7th-grade curriculum, military families, band and theater | `moore-upper-grades-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P7.1, P7.2, P7.3, P9.1, P12.1, P12.2, P12.3, P13.2, P13.3, P14.1, P14.2, P17.2, P18.1, P18.2, P20.1 |
| 3 | Pinkerton from Candia: the move to a big school, the bus and late bus, IEPs at Pinkerton, CTE welding and automotive, apprenticeships, dual enrollment, readiness, AP and honors, team cuts, college advising, jobs and the military, military family tuition breaks, music auditions | `pinkerton-from-candia.md` | `raw/high/` | P3.1, P3.2, P3.3, P4.3, P8.1, P8.2, P8.3, P9.2, P9.3, P15.1, P15.2, P15.3, P18.3, P20.2 |
| 4 | Money and governance: the tax cap and health insurance, Pinkerton tuition, SAU 15 costs, warrant articles and the tax bill, the Budget Committee and Board split, senior exemptions, enrollment, shopping for insurance, Candia's Pinkerton trustee seat, the building, board meetings, state against local funding, overriding the cap, cost per pupil, arts cuts | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P5.1, P5.2, P5.3, P10.1, P10.2, P10.3, P17.1, P17.3, P19.1, P19.2, P19.3, P20.3 |
