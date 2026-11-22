# Kingston Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Kingston and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Kingston/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Kingston

- **Kingston** is a town in Rockingham County north of Plaistow and east of Danville. Site town id 283.
- **The Sanborn Regional School District** (site district id 476) is **SAU 17**, for Kingston and Newton. Its schools: Daniel J. Bakie (20625), preschool to grade 2; Memorial (20635), grades 3–5; Sanborn Regional Middle (20630), grades 6–8; Sanborn Regional High (20620), grades 9–12. Check which towns' children attend which elementary school (P2.1).
- **Shared district, first town.** Newton shares this district and is researched in the next wave; it will cite these files. So cover district-wide facts (the middle and high school, the budget, the cost formula, policies) fully, placed with the district, and keep town-only facts placed with the town.
- **Career and technical education:** the Seacoast School of Technology, researched in `town/Exeter/` (and `town/Stratham/`, `town/Raymond/`). Write Sanborn's side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 819 (2014-15), 726 (2019-20), 580 (2025-26); cost per pupil FY2025 Sanborn $27,191, state $22,699; 2025 tax rates per $1,000 (Kingston): total $17.90, local school $10.79, municipal $5.34; Question 2: Kingston 70.5%, Sanborn adopted it (71.5%, unofficial); math proficiency 2026: Sanborn 50%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Sanborn's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Sanborn Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** full-day pre-K (P1.1); bus drop-offs in Plaistow (P1.3); scores around 44% (P2.2); Pickup Patrol and Alma (P7.1); early-release care (P8.3); kindergarten crowding (P12.1); a nurse every day (P19.2).
- **Middle and high school:** SST applications and schedule (P5.1, P5.2); advanced math (P6.1); AP and Running Start (P9.1); grades and sports (P13.2); fields at 17 Danville Road (P13.3); shop classes (P15.2).
- **Money:** the Kingston–Newton split (P2.1, P11.2); falling enrollment (P3.1); the default budget (P3.2); a budget survey (P11.3); teacher turnover (P15.1); a state budget cap (P17.1); building systems (P17.2).
- **Home education:** filing each year with SAU 17 (P10.3; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Exeter/` | The Seacoast School of Technology: programs, admission, schedule, sending schools. |
| `town/timberlane/`, `town/Atkinson/`, `town/Hampstead/` | Neighboring districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Jaffrey, Loudon, Alton and Tilton (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Sanborn Regional` for all Sanborn schools, policies, budget and board.
- `sau 17` for SAU-wide facts.
- `town Kingston` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Kingston/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school and SST to agent 3; support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Bakie, Memorial and families: pre-K, drop-off and pickup, buses to care elsewhere, registration, speech and OT follow-through, apps, contacts, homework help, meals, early releases, kindergarten size, reading help, first-grade size, progress reports, delays, nurses, translation | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.3, P4.1, P7.1, P7.2, P7.3, P8.1, P8.3, P12.1, P16.1, P16.2, P16.3, P19.1, P19.2, P20.2 |
| 2 | Support and choices: IEPs into the middle school, special education costs, homeschool access and paperwork, security, staying with Sanborn, bullying and phones, private and charter schools, counselors and social workers, 504 plans, quiet spaces, absences | `support-and-choices.md` | `raw/support/` | P4.2, P4.3, P10.1, P10.2, P10.3, P12.2, P12.3, P14.1, P14.2, P14.3, P18.1, P18.2, P18.3, P19.3 |
| 3 | Sanborn Middle and High and SST: scores, SST admission and schedule, apprenticeships and dual enrollment, advanced math, coding and robotics, Chromebooks, sports fees and eligibility, AP and Running Start, college admissions, counselors, work readiness, athletics schedules, fields, shop and career prep, band and drama | `middle-high-and-sst.md` | `raw/high/` | P2.2, P5.1, P5.2, P5.3, P6.1, P6.2, P6.3, P8.2, P9.1, P9.2, P9.3, P11.1, P13.1, P13.2, P13.3, P15.2, P20.1 |
| 4 | Money and governance: the Kingston–Newton split, falling enrollment, the default budget, administration costs, the budget survey, teacher turnover, budget committee meetings, a state budget cap, building systems, shared town services, school board seats | `money-and-governance.md` | `raw/money/` | P2.1, P3.1, P3.2, P3.3, P11.2, P11.3, P15.1, P15.3, P17.1, P17.2, P17.3, P20.3 |
