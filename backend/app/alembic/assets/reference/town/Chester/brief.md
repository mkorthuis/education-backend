# Chester Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Chester and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Chester/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Chester

- **Chester** is a town in Rockingham County west of Sandown. Site town id 93.
- **The Chester School District** (site district id 93) is **SAU 82** and runs Chester Academy (20500); check its grades, preschool and budget form.
- **High school:** Pinkerton Academy under a tuition contract (`places.yaml`: the contract isn't posted; SAU 82 says students "mainly attend" Pinkerton). Pinkerton is researched in `town/pinkerton/`; Hooksett's, Candia's and Auburn's sides of their contracts are in `town/Hooksett/` and (running now) `town/Candia/` and `town/Auburn/`. Cite them; write Chester's side.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 867 (2014-15), 782 (2019-20), 727 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Chester Academy 508; cost per pupil FY2025 Chester $19,221, state $22,699; 2025 tax rates per $1,000 (Chester): total $16.90, local school $10.26, municipal $4.89; Question 2: Chester 63.6% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Chester's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Chester)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Chester Academy:** care hours (P1.1); public preschool (P1.2); scores (P4.1); class sizes (P4.2); special education and paras (P5.1, P5.3); kindergarten (P14.2); drop-off traffic on Murphy Drive (P16.3); bus rides (P18.2).
- **Pinkerton:** CTE seats (P2.1, P20.2); the bus ride (P2.2); IEPs (P5.2); fees (P6.2); honors readiness (P6.3); Chester's say (P11.2); dual enrollment (P12.1); team cuts (P12.3).
- **Money:** taxes against enrollment (P3.1); Pinkerton tuition (P3.2); teacher salaries (P6.1); the commercial tax base (P8.1); the building (P8.2); one-school administration (P8.3); comparisons with Auburn, Candia and Raymond (P10.2); turnover (P15.1); charter tuition (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/pinkerton/` | Pinkerton Academy. |
| `town/Hooksett/`, `town/Auburn/` and `town/Candia/` (running) | Other towns' Pinkerton contracts and K–8 schools, for comparisons. |
| `town/Derry/`, `town/Raymond/` | Neighboring districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Greenland, Rye, Brentwood, Fremont and Chester (this wave); Ossipee, Candia, Gilmanton, New Boston and North Hampton (running or starting). Don't write facts about those towns.

## Where facts go

- `district Chester` for Chester Academy and the district's budget, board and its side of the Pinkerton contract.
- `district Pinkerton Academy` only for Pinkerton facts its files lack.
- `sau 82` for SAU-wide facts.
- `town Chester` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Chester/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Chester Academy's early grades and families: before- and after-school care, preschool, storm days, scores, class sizes, bus stops and registration, school quality, child care in town, reading help, bus drop-off rules, meals, speech evaluations before kindergarten, kindergarten, welcoming families, drop-off traffic, kindergarten readiness, long bus rides, kindergarten recess | `chester-academy-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P10.1, P10.3, P13.1, P13.2, P13.3, P14.1, P14.2, P14.3, P16.3, P18.1, P18.2, P18.3 |
| 2 | Chester Academy's upper grades, support and choices: special education and paras, homeschool and EFA access, returning to public school, clubs and intramurals, bullying and phones, Algebra I, advanced learners, world languages, volunteering, private and charter schools, readiness for competitive high schools, charter tuition, gaps at 8th grade | `chester-academy-upper-grades-support-and-choices.md` | `raw/middle/` | P5.1, P5.3, P7.1, P7.2, P7.3, P9.1, P9.2, P9.3, P16.1, P16.2, P17.1, P19.1, P19.2, P19.3, P20.1 |
| 3 | Pinkerton from Chester: CTE welding and electrical, the bus ride and late bus, the move to a big school, IEPs, fees, honors readiness, college counseling, Chester's say, dual enrollment, support for a struggling student, team cuts, AP and honors, trades awareness | `pinkerton-from-chester.md` | `raw/high/` | P2.1, P2.2, P2.3, P5.2, P6.2, P6.3, P11.1, P11.2, P12.1, P12.2, P12.3, P15.2, P20.2 |
| 4 | Money and governance: taxes against enrollment, Pinkerton tuition, the deliberative session, teacher salaries, the commercial tax base, the building, one-school administration, comparisons with neighbors, calendars, turnover, board transparency, facility use, needs, young residents' voice | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.1, P8.1, P8.2, P8.3, P10.2, P11.3, P15.1, P15.3, P17.2, P17.3, P20.3 |
