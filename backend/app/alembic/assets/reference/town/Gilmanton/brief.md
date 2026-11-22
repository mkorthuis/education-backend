# Gilmanton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Gilmanton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Gilmanton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Gilmanton

- **Gilmanton** is a town in Belknap County, with villages including Gilmanton Iron Works. Site town id 195.
- **The Gilmanton School District** (site district id 195) is **SAU 79**. It runs Gilmanton School (21250); check its grades and whether it has a preschool. Check its budget form.
- **High school:** Gilford High School under an AREA agreement (`places.yaml`: the amended plan runs 2023–2035 and phases out by grade from 2035-36 if not extended; Gilmanton's 2025-26 attempt to renegotiate ended in September 2026 with no change). Gilford is researched in `town/Gilford/` (gilford-high-and-huot.md, money-and-governance.md); cite it and write Gilmanton's side.
- **Reuse first.** Much of this town's shared district or high school is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 566 (2014-15), 568 (2019-20), 503 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Gilmanton School 335; cost per pupil FY2025 Gilmanton $22,975, state $22,699; 2025 tax rates per $1,000 (Gilmanton): total $15.25, local school $10.04, municipal $3.35; Question 2: Gilmanton 65.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Gilmanton's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Gilmanton)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Gilmanton School:** preschool (P1.1); before-care (P1.2); class sizes (P3.1); bus times (P4.1); mud-season roads (P8.1); a Blue Ribbon award (P9.2); the earliest drop-off (P20.1); grades 5–8 in one building (P14.1); phones (P14.2); music and art (P14.3); world languages (P19.3).
- **Gilford High:** Huot access (P2.1); the jump to Gilford (P2.2); IEPs (P6.2); shop and ag classes (P8.2); a late bus (P10.1); AP and dual enrollment (P10.3); driver's ed (P12.1); calendars that don't match (P12.3); bus times (P16.2); tuitioning elsewhere (P16.3, P19.1); open enrollment (P17.2).
- **Money:** half the budget to Gilford (P2.3, P5.1); enrollment (P5.2); warrant articles (P5.3); the building (P15.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Gilford/` (gilford-high-and-huot.md, gilford-middle-school.md, money-and-governance.md) | Gilford High, the Huot Center, Gilford's tuition terms and AREA plan. |
| `town/Belmont/`, `town/Laconia/` | Neighboring districts and the Huot Center, for comparisons (P9.1). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Ossipee, Candia, Gilmanton, New Boston and North Hampton (this wave); Allenstown, Epsom, Deerfield, Auburn, Wolfeboro, Newton, Rindge, Boscawen, Barnstead and Northfield (running). Don't write facts about those towns.

## Where facts go

- `district Gilmanton` for Gilmanton School, the district's budget, board and its side of the AREA agreement.
- `district Gilford` only for Gilford High facts Gilford's files lack.
- `sau 79` for SAU-wide facts.
- `town Gilmanton` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/Gilmanton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Gilmanton School's early grades and families: preschool options, before-care, kindergarten registration and cutoff, class sizes, family communication, bus times, discreet meals, delays, mud-season roads, playgroups and rec, a person to call, reading help, records for mid-year moves, security, residency papers, summer camps, earliest drop-off, summer catch-up, storm and outage notices | `gilmanton-school-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.3, P4.1, P4.2, P4.3, P8.1, P9.3, P11.1, P11.2, P13.1, P13.2, P17.1, P17.3, P20.1, P20.2, P20.3 |
| 2 | Gilmanton School's upper grades, support and choices: math challenge, speech and special education staff, SAU 79 contacts, homeschool and EFA access, the library for homeschoolers, farm absences, bullying, counselors, grades 5–8 in one building, phones, music and art, volunteers, the 8th-grade transition, 504 plans, homework, a quiet space, world languages | `gilmanton-school-upper-grades-support-and-choices.md` | `raw/middle/` | P3.2, P6.1, P6.3, P7.1, P7.2, P7.3, P8.3, P11.3, P13.3, P14.1, P14.2, P14.3, P15.1, P16.1, P18.1, P18.2, P18.3, P19.3 |
| 3 | Gilford High and the Huot Center from Gilmanton: Huot access, the jump to Gilford, IEPs, shop and ag classes, the late bus, fitting in, AP and dual enrollment, driver's ed, apprenticeships and work, graduates' plans, bus times, tuitioning elsewhere, open enrollment, town money for another school | `gilford-high-from-gilmanton.md` | `raw/high/` | P2.1, P2.2, P6.2, P8.2, P10.1, P10.2, P10.3, P12.1, P12.2, P15.3, P16.2, P16.3, P17.2, P19.1 |
| 4 | Money and governance: the Gilford tuition bill, the tax bill split, enrollment, warrant articles, comparisons with Belmont and Gilford, the Blue Ribbon award, calendars, the building, test scores | `money-and-governance.md` | `raw/money/` | P2.3, P5.1, P5.2, P5.3, P9.1, P9.2, P12.3, P15.2, P19.2 |
