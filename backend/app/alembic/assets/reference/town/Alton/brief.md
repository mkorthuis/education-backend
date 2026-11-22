# Alton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Alton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Alton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Alton

- **Alton** is a town in Belknap County at the south end of Lake Winnipesaukee, with many seasonal waterfront homes. Site town id 15.
- **The Alton School District** (site district id 15) is **SAU 72**: Alton Central (22480), preschool to grade 8.
- **Prospect Mountain High School** is run by the Prospect Mountain JMA (site district id 970) for Alton and Barnstead (`places.yaml`). Check its governance, cost split and SAU.
- **Shared district, first town.** Barnstead shares this district and is researched in the next wave; it will cite these files. So cover district-wide facts (the middle and high school, the budget, the cost formula, policies) fully, placed with the district, and keep town-only facts placed with the town.
- **Career and technical education:** check where Prospect Mountain students take career programs (the Huot Center in Laconia, researched in `town/Laconia/`, or the Lakes Region Technology Center in Wolfeboro, used by Farmington).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 770 (2014-15), 610 (2019-20), 569 (2025-26); cost per pupil FY2025 Alton $27,428, state $22,699; 2025 tax rates per $1,000 (Alton): total $13.50, local school $6.04, municipal $4.09; Question 2: Alton 69.9%, adopted (unofficial); math proficiency 2026: Alton 32%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Alton's and Prospect Mountain's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Alton|Prospect Mountain JMA)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Alton Central:** class sizes (P1.1); reading help (P1.2); care (P1.3); storm days (P3.3); public pre-K (P4.1); kindergarten (P4.3); honors math in 7th–8th (P3.1); middle school clubs (P7.2); gifted programs (P19.1); world languages (P19.2); late buses on icy roads (P17.2).
- **Prospect Mountain:** AP and college prep (P3.2); CTE and buses (P5.1, P5.2); shop classes (P5.3); dual credit (P6.1); counselors (P6.2); early buses (P14.1); phones (P14.2); an SRO at both schools (P17.1).
- **Money:** the budget each March (P2.1); a reserve fund wiped out (P2.2); value from sharing Prospect Mountain (P2.3); special education busing doubled (P9.2); an SAU study with Barnstead (P10.1); seasonal owners' taxes (P10.3); the fund balance (P13.2); low para and substitute pay (P16.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Laconia/`, `town/Gilford/`, `town/Belmont/` | The Huot Center and neighboring districts. |
| `town/Farmington/` | The Lakes Region Technology Center in Wolfeboro. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Kingston, Jaffrey, Loudon and Tilton (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Alton` for Alton Central, its budget and board.
- `district Prospect Mountain JMA` for Prospect Mountain High, its budget, governance and cost split.
- `sau 72` for SAU-wide facts.
- `town Alton` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Alton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money for both districts belongs to agent 4; Prospect Mountain and CTE to agent 3; Alton Central's upper grades, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Alton Central's early grades and families: class sizes, reading help, care, storm days, pre-K, costs for young families, kindergarten, meals, food and coat programs, volunteers, icy roads, recess, enrichment, grandparents' enrollment papers, summer programs, apps | `alton-central-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.3, P4.1, P4.2, P4.3, P8.1, P8.2, P15.3, P17.2, P17.3, P19.1, P20.1, P20.2, P20.3 |
| 2 | Alton Central's upper grades, support and choices: honors math, mental health support, bullying and phones, middle school sports and clubs, the move to Prospect Mountain, special education staffing and IEPs, staff retention, support for teachers, homeschool access, EFAs, world languages | `alton-central-upper-grades-and-support.md` | `raw/middle/` | P3.1, P6.3, P7.1, P7.2, P7.3, P9.1, P9.3, P12.1, P12.2, P12.3, P15.1, P16.2, P19.2 |
| 3 | Prospect Mountain High and CTE: AP and college prep, regional CTE and buses, shop classes, dual credit, counselors, practical skills, apprenticeships and the military, early buses, phones, clubs, an SRO, scores | `prospect-mountain-and-cte.md` | `raw/high/` | P3.2, P5.1, P5.2, P5.3, P6.1, P6.2, P11.1, P11.2, P11.3, P14.1, P14.2, P14.3, P17.1, P19.3 |
| 4 | Money and governance for Alton and Prospect Mountain: the budget each March, the reserve fund, sharing Prospect Mountain, access to decisions, special education busing, the SAU study with Barnstead, the school share of taxes, seasonal owners, the default budget, the fund balance, teacher contracts, buildings, para and substitute pay, housing for staff, rents, meeting places, cost per student | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P8.3, P9.2, P10.1, P10.2, P10.3, P13.1, P13.2, P13.3, P15.2, P16.1, P16.3, P18.1, P18.2, P18.3 |
