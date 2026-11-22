# Rye Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Rye and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Rye/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Rye

- **Rye** is a coastal town in Rockingham County south of Portsmouth. Site town id 471.
- **The Rye School District** (site district id 471) runs Rye Elementary (22475) and Rye Junior High (22470); check their grades, the SAU 50 preschool at Rye Elementary and the district's budget form. New Castle families may choose Rye Junior High (`places.yaml`).
- **SAU 50** serves Greenland, New Castle, Newington and Rye. Greenland and Rye are researched at the same time: Greenland's money agent writes SAU 50-wide facts (the SAU budget and how its cost is split, the superintendent search, shared policies), placed `sau 50`; Rye's files cite them and write only Rye's side.
- **High school:** Portsmouth High School under an AREA agreement (`places.yaml`), researched in `town/Portsmouth/` (middle-high-and-cte.md, getting-to-school-choices-and-staff.md, money-buildings-and-governance.md, student-support.md). Cite it; write this town's side, including its tuition, and place facts about Portsmouth High itself that Portsmouth's files lack `district Portsmouth`.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 653 (2014-15), 549 (2019-20), 501 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Rye Elementary 211, Rye Junior High 175; cost per pupil FY2025 Rye $32,559, state $22,699; 2025 tax rates per $1,000 (Rye): total $8.37, local school $3.68, municipal $2.24; Question 2: Rye 50.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Rye's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Rye)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Rye Elementary:** the SAU 50 preschool (P1.1, P1.2); kindergarten size (P1.3); before-school care (P3.1); bus times on Sagamore Road (P3.2); world languages (P9.2); different dismissal times (P12.1); ESL (P14.1).
- **Rye Junior High:** 5th grade there (P4.1); math placement (P4.2); specialists (P5.1); teams and cuts (P11.1); arts (P15.1); labs (P18.3).
- **Portsmouth High:** the jump (P4.3); CTE (P7.1); the bus from Route 1 (P7.3, P20.1); parking (P10.1); calendars (P10.2); varsity chances (P11.2); the math gap (P20.2).
- **Money:** the budget against about 400 students (P2.1); Portsmouth tuition (P2.2); the Rye Elementary building study (P2.3); $470,000 returned (P8.1); control over costs (P8.2); state funding and vouchers (P8.3); crowding (P16.1); sidewalks (P20.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Portsmouth/` | Portsmouth High School, its career center, buses, tuition policy and student support. |
| `town/Greenland/` (running now) | SAU 50-wide facts, written by Greenland's money agent. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Greenland, Rye, Brentwood, Fremont and Chester (this wave); Ossipee, Candia, Gilmanton, New Boston and North Hampton (running or starting). Don't write facts about those towns.

## Where facts go

- `district Rye` for Rye Elementary, Rye Junior High and the district's budget, board and AREA side.
- `district Portsmouth` only for Portsmouth High facts its files lack.
- `sau 50` only for SAU-wide facts Greenland's files lack.
- `town Rye` for town government, recreation, the coast and taxes.
- No place for general NH rules.

All agents write in `town/Rye/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Rye Elementary and young families: the preschool and care, kindergarten size, before-school care, bus times, reading help, early releases, world languages, who to talk to, dismissal times, lunch, pickup rules, enrolling mid-year, ESL, the PTA, testing time, homework, three schools' communications | `rye-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.2, P3.3, P9.1, P9.2, P9.3, P12.1, P12.2, P12.3, P13.1, P14.1, P14.3, P17.1, P17.3, P19.1 |
| 2 | Rye Junior High, support and choices: 5th grade at the junior high, math placement, specialists and quiet spaces, comparisons with other middle schools, clubs and sports, gym and recess, homeschool and EFA access, arts, bullying, counseling, coastal learning, screen rules, science labs | `rye-junior-high-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P5.1, P5.2, P6.1, P6.2, P11.1, P11.3, P13.2, P13.3, P15.1, P15.2, P17.2, P18.1, P18.2, P18.3 |
| 3 | Portsmouth High from Rye: the jump to a big school, IEPs, college counseling, CTE, Rye students' standing, the bus from Route 1, parking, calendars, AP and dual enrollment, varsity chances, finding a niche, snow days, the math gap | `portsmouth-high-from-rye.md` | `raw/high/` | P4.3, P5.3, P6.3, P7.1, P7.2, P7.3, P10.1, P10.2, P10.3, P11.2, P15.3, P19.2, P20.1, P20.2 |
| 4 | Money and governance: the budget against enrollment, Portsmouth tuition, the building study, the money returned to the town, cost control, state funding and vouchers, moving to Greenland or Portsmouth, crowding, warrant articles, community use of fields, field trip costs, sidewalks | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P8.1, P8.2, P8.3, P14.2, P16.1, P16.2, P16.3, P19.3, P20.3 |
