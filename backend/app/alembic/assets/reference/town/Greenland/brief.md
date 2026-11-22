# Greenland Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Greenland and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Greenland/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Greenland

- **Greenland** is a town in Rockingham County between Portsmouth and Stratham. Site town id 215.
- **The Greenland School District** (site district id 215) runs Greenland Central School (22450); check its grades, preschool and budget form.
- **SAU 50** serves Greenland, New Castle, Newington and Rye. Greenland and Rye are researched at the same time: Greenland's money agent writes SAU 50-wide facts (the SAU budget and how its cost is split, the superintendent search, shared policies), placed `sau 50`; Rye's files cite them and write only Rye's side.
- **High school:** Portsmouth High School under an AREA agreement (`places.yaml`), researched in `town/Portsmouth/` (middle-high-and-cte.md, getting-to-school-choices-and-staff.md, money-buildings-and-governance.md, student-support.md). Cite it; write this town's side, including its tuition, and place facts about Portsmouth High itself that Portsmouth's files lack `district Portsmouth`.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 560 (2014-15), 596 (2019-20), 516 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Greenland Central 367; cost per pupil FY2025 Greenland $24,874, state $22,699; 2025 tax rates per $1,000 (Greenland): total $13.36, local school $8.27, municipal $3.30; Question 2: Greenland 55.0% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Greenland's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Greenland)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Greenland Central:** full-day kindergarten (P1.1); after-school care (P1.2); public pre-K (P1.3); the FirstView app (P2.1); math near 54% (P7.1); class sizes (P9.2); dyslexia screening (P14.1); houses in K–8 (P20.3); staff turnover and shortages (P19.1, P19.2).
- **Portsmouth High:** a separate bus (P3.2); honors access (P3.3); CTE (P5.1, P5.3); IEPs and aides (P6.2, P6.3); dual enrollment with Great Bay (P17.3); a late bus (P17.2).
- **Money:** the tax bill split (P4.1); tuition to Portsmouth (P4.2); the tax cap question (P4.3); the building (P10.1); sharing SAU 50 (P12.1); the default budget (P12.3); cost per pupil against Rye, Newington and Stratham (P16.1); open enrollment (P16.3); a new superintendent (P19.3).
- **Home education:** an annual letter and assessment to SAU 50 (P15.2; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Portsmouth/` | Portsmouth High School, its career center, buses, tuition policy and student support. |
| `town/Stratham/`, `town/Newmarket/` | Neighboring districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Greenland, Rye, Brentwood, Fremont and Chester (this wave); Ossipee, Candia, Gilmanton, New Boston and North Hampton (running or starting). Don't write facts about those towns.

## Where facts go

- `district Greenland` for Greenland Central and the district's budget, board and AREA side.
- `district Portsmouth` only for Portsmouth High facts its files lack.
- `sau 50` for SAU-wide facts.
- `town Greenland` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Greenland/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Greenland Central's early grades and families: kindergarten, after-school care, public pre-K, the bus app, late arrival calls, meals and fee help, moving within town, class sizes, registering as renters, supply lists, dyslexia screening, reading pull-outs, progress reports, PowerSchool help | `gcs-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.3, P8.1, P8.2, P8.3, P9.2, P13.1, P13.3, P14.1, P14.2, P14.3, P18.3 |
| 2 | Greenland Central's upper grades, support and choices: the move from 4th grade, hands-on classes, IEPs, math results and acceleration, staying public through 8th grade, EFAs and Seacoast Charter, sports, clubs, band and rides to games, military families, homeschool access, laptops, switching teachers, bullying, counselors, houses | `gcs-upper-grades-support-and-choices.md` | `raw/middle/` | P2.2, P5.2, P6.1, P7.1, P7.2, P9.1, P9.3, P11.1, P11.2, P11.3, P13.2, P15.1, P15.2, P18.1, P18.2, P20.1, P20.2, P20.3 |
| 3 | Portsmouth High from Greenland: the move to a big school, the high school bus, honors access, CTE and transport, IEPs and aides, AP readiness, homeschoolers taking classes, family communication, late buses, dual enrollment | `portsmouth-high-from-greenland.md` | `raw/high/` | P3.1, P3.2, P3.3, P5.1, P5.3, P6.2, P6.3, P7.3, P15.3, P17.1, P17.2, P17.3 |
| 4 | Money and governance: the tax bill split, Portsmouth tuition, the tax cap, the building, enrollment, a say at Portsmouth, SAU 50, the budget calendar, the default budget, cost per pupil, budget drivers, open enrollment, substitutes and paras, teacher turnover, the new superintendent | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P10.1, P10.2, P10.3, P12.1, P12.2, P12.3, P16.1, P16.2, P16.3, P19.1, P19.2, P19.3 |
