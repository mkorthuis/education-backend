# Hanover Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hanover and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hanover/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hanover

- **Hanover** is a town in Grafton County on the Connecticut River, home of Dartmouth College; Etna is a village in the town. Site town id 233.
- **Two districts serve Hanover, both in SAU 70:**
-   - **The Hanover School District** (site district id 233): Ray School (20830), K–5.
-   - **The Dresden School District** (site district id 142), an interstate district of Hanover and Norwich, Vermont: Richmond Middle (20825), grades 6–8, and Hanover High (20820), grades 9–12. Check how its costs are split between the two towns (P2.1, P2.2).
- **Norwich, Vermont** runs Marion Cross School (K–6), which isn't in the site's data. Write facts about it only as they bear on Hanover's questions, with `district Dresden` when they concern Dresden.
- **Tuition:** Lyme (site district id 327) and Cornish send grades 9–12 to Dresden (`places.yaml`).
- **Career and technical education:** check where Hanover High students take career programs (the Hartford Area Career and Technology Center in Vermont is likely; P4.1).
- **Starting pages:** SAU 70, https://www.sau70.org (check); the town, https://www.hanovernh.org.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,199 (2014-15), 1,161 (2019-20), 1,083 (2025-26); cost per pupil FY2025 Hanover $25,559, Dresden $27,527, state $22,699; 2025 tax rates per $1,000: total $12.78, local school $7.23, municipal $3.30; Question 2: Hanover 34.6%, Dresden 34.6%, so no cap (unofficial); math proficiency 2026: Hanover 79%, Dresden 78%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Hanover's and Dresden's kindergarten, registration and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Hanover|Dresden)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Ray School:** pre-K at Marion Cross but none at Ray (P3.1); kindergarten registration and full day (P3.2, P14.2); late pickup (P1.1); bus changes (P1.3); walking and biking (P5.2); class sizes (P5.3); reading screening (P6.1); bus rides from Etna and mud season (P8.1, P8.2); K–2 children met at the bus (P8.3); early drop-off and after-school spots (P10.1, P10.2); Advance Transit (P14.3).
- **Richmond and Hanover High:** the 6th-grade merge with Norwich (P1.2); trades and career classes (P4.1); fees (P4.3); a rigid freshman schedule (P7.2); stress (P7.3); parking (P13.3); independent study (P19.1); AI rules (P19.2); a late bus (P17.3).
- **Money:** the Dresden assessment climbing (P2.1); Hanover's share against Norwich (P2.2); about 6.7 FTEs cut (P15.1); Lyme's tuition (P15.2); buildings (P15.3); tax relief (P9.2).

## Already researched

| File | What it covers |
|---|---|
| Lebanon's research (this wave) | A neighboring district and the same Vermont career centers. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Berlin, Claremont, Lebanon and Swanzey (this wave), and Belmont, Gilford, Meredith, Franklin and Plymouth (queued). Don't write facts about those towns.

## Where facts go

- `district Hanover` for the Hanover School District, Ray School, its budget and board.
- `district Dresden` for Richmond, Hanover High, the interstate agreement, the cost split, its budget, board and tuition contracts.
- `sau 70` for SAU-wide facts.
- `district Lyme` only for Lyme's own side of its contract.
- `town Hanover` for town government, tax relief, recreation and Advance Transit.
- No place for general NH rules.

All agents write in `town/Hanover/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Both districts' budgets, the cost split and governance belong to agent 4; Hanover High to agent 3; Richmond, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Ray School and families: late pickup, bus changes, pre-K and Marion Cross, kindergarten registration and full day, English learners, walking and biking, class sizes, reading screening, bus rides from Etna, mud season, the K–2 bus rule, early drop-off, after-school spots, early-release days, preschools, Advance Transit, meals | `ray-school-and-families.md` | `raw/elementary/` | P1.1, P1.3, P3.1, P3.2, P3.3, P5.2, P5.3, P6.1, P8.1, P8.2, P8.3, P10.1, P10.2, P10.3, P14.1, P14.2, P14.3, P17.1 |
| 2 | Richmond Middle, support and choices: the 6th-grade transition, support teams moving to Richmond, homeschoolers in sports, EFAs, returning for 9th grade, welcoming newcomers, picking 9th-grade electives, phones, ADHD support, bullying, quiet spaces, trip costs, late buses, portals, guardianship papers, Ray's counselor | `richmond-support-and-choices.md` | `raw/middle/` | P1.2, P6.2, P11.1, P11.2, P11.3, P12.2, P12.3, P13.2, P16.1, P16.2, P16.3, P17.2, P17.3, P20.1, P20.2, P20.3 |
| 3 | Hanover High: trades and career-tech classes, counseling for non-college paths, fees, advanced math and computer science, the freshman schedule, stress, transferring mid-year, away games and homework, parking, students from private middle schools, college counseling, languages and arts, independent study, AI rules | `hanover-high-school.md` | `raw/high/` | P4.1, P4.2, P4.3, P7.1, P7.2, P7.3, P12.1, P13.1, P13.3, P18.1, P18.2, P18.3, P19.1, P19.2 |
| 4 | Money and governance: the Dresden assessment, Hanover's share against Norwich, the tax rate and budget votes, whether the schools are worth the cost, paraprofessionals in staff cuts, the budget explained, tax relief, community use of buildings, the 6.7 FTE cut, Lyme's tuition, buildings, young people's housing | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P5.1, P6.3, P9.1, P9.2, P9.3, P15.1, P15.2, P15.3, P19.3 |
