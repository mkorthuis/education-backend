# North Hampton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for North Hampton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/North Hampton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about North Hampton

- **North Hampton** is a town in Rockingham County on the coast north of Hampton. Site town id 405.
- **The North Hampton School District** (site district id 405) is in **SAU 21** with Hampton, Hampton Falls, Seabrook and the Winnacunnet Cooperative. It runs North Hampton School (20805); check its grades and pre-K. Check its budget form.
- **High school:** Winnacunnet High School (20780), run by the Winnacunnet Cooperative (site district id 581), of which North Hampton is a member. Winnacunnet is researched in `town/winnacunnet/winnacunnet-high-school.md`, with Hampton's and Seabrook's research in `town/Hampton/` and `town/Seabrook/`; SST in `town/Exeter/`. Cite them and write North Hampton's side.
- **Reuse first.** Much of this town's shared district or high school is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 575 (2014-15), 484 (2019-20), 375 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): North Hampton School 268, Winnacunnet High 970; cost per pupil FY2025 North Hampton $34,105 (Winnacunnet $28,650), state $22,699; 2025 tax rates per $1,000 (North Hampton): total $13.45, local school $6.97, municipal $4.58; Question 2: North Hampton 56.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): North Hampton's and Winnacunnet's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (North Hampton|Winnacunnet Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **North Hampton School:** care on site (P1.1); the Route 111 bus (P1.2); class sizes (P1.3); Algebra and Geometry in 7th and 8th grade (P3.1); a pre-K lottery (P7.1); screen time (P7.3); full-day kindergarten (P10.1); ESOL (P18.1); recess and gym (P12.1); security (P19.2).
- **Winnacunnet:** the jump from small classes (P8.1); SST electrical and HVAC (P4.1, P4.3); AP and dual enrollment (P11.1); transition services to 21 (P16.1–P16.3); an athletic trainer (P19.3); personal finance (P20.3).
- **Money:** about $34,000 per student (P2.1); the split between NHS and Winnacunnet (P2.2); the default budget (P2.3); SAU 21 costs (P6.1); a 3.2% raise (P6.2); the 85-acre campus (P6.3); merging or tuitioning (P17.3); senior tax relief (P9.1).

## Already researched

| File | What it covers |
|---|---|
| `town/winnacunnet/` | Winnacunnet High School (the cooperative's shared folder). |
| `town/Hampton/`, `town/Seabrook/` | SAU 21's other districts: policies, SAU costs, the cooperative's budget and votes. |
| `town/Exeter/` | The Seacoast School of Technology. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Ossipee, Candia, Gilmanton, New Boston and North Hampton (this wave); Allenstown, Epsom, Deerfield, Auburn, Wolfeboro, Newton, Rindge, Boscawen, Barnstead and Northfield (running). Don't write facts about those towns.

## Where facts go

- `district North Hampton` for North Hampton School, the district's budget, board and policies.
- `district Winnacunnet Cooperative` only for Winnacunnet facts the existing files lack.
- `sau 21` for SAU-wide facts not already in Hampton's or Seabrook's files.
- `town North Hampton` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/North Hampton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | North Hampton School's early grades and families: care on site, the Route 111 bus, class sizes, who to call during a long shift, the pre-K lottery, the kindergarten cutoff, screen time, full-day kindergarten, local preschools, recess and gym, residency and guardianship, discreet meals, ESOL, ParentSquare for families new to English, welcoming families | `nhs-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.2, P7.1, P7.2, P7.3, P10.1, P10.2, P12.1, P14.1, P14.3, P18.1, P18.2, P18.3 |
| 2 | North Hampton School's upper grades, support and choices: advanced math, STEM clubs, Orton-Gillingham through an IEP, out-of-district placements, phones, volunteering, discipline, affordable activities, homeschool and EFA access, entering Winnacunnet from homeschool, counseling, community events, cuts to sports and arts, security | `nhs-upper-grades-support-and-choices.md` | `raw/middle/` | P3.1, P3.3, P5.1, P5.3, P8.3, P9.3, P12.2, P12.3, P13.1, P13.2, P13.3, P14.2, P15.2, P19.1, P19.2 |
| 3 | Winnacunnet and SST from North Hampton: readiness of North Hampton 8th graders, electrical and HVAC, counselors and the trades, getting to SST, the jump from small classes, mixing towns, AP and dual enrollment, college outcomes, VLACS, transition services to 21 and vocational rehab, an athletic trainer, reading and math then and now, personal finance | `winnacunnet-from-north-hampton.md` | `raw/high/` | P3.2, P4.1, P4.2, P4.3, P8.1, P8.2, P11.1, P11.2, P11.3, P16.1, P16.2, P16.3, P19.3, P20.1, P20.3 |
| 4 | Money and governance: cost per student, the split between NHS and Winnacunnet, the default budget, SAU 21 costs, staff raises, the campus, senior tax relief, sharing with the town, taxes against neighbors, renters, tracking results, the budget breakdown, merging or tuitioning, affordability for young buyers | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P6.1, P6.2, P6.3, P9.1, P9.2, P10.3, P15.1, P15.3, P17.1, P17.2, P17.3, P20.2 |
