# Charlestown Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Charlestown and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Charlestown/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Charlestown

- **Charlestown** is a town in Sullivan County on the Connecticut River, south of Claremont, with one of the highest tax rates in the state. Site town id 89.
- **The Fall Mountain Regional School District** (site district id 174) is **SAU 60** and runs Charlestown Primary (22985; preschool to grade 4), Charlestown Middle (22975; grades 5–8), Fall Mountain Regional High (22990; grades 9–12) and elementary schools in the other towns. It votes by official ballot (SB2) in each member town. Check how costs are split among the five towns.
- **Career programs:** check what Fall Mountain offers itself and whether students attend the Sugar River Valley Regional Technical Center in Claremont (researched in `town/Claremont/`).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 655 (2014-15), 630 (2019-20), 568 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Charlestown Primary 234, Charlestown Middle 168, Fall Mountain High 479; cost per pupil FY2025 Fall Mountain $24,159, state $22,699; 2025 tax rates per $1,000 (Charlestown): total $36.54, local school $23.34, municipal $8.03; Question 2: Charlestown 68.0% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Fall Mountain's preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Fall Mountain Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Primary school:** pre-K registration and hours (P1.1); the drop-off bottleneck (P1.2); walking from the village (P1.3); a Niche C+ (P4.1); after-school care (P4.3); free meals for all (P5.2); summer meals (P5.3); long bus rides to Main Street and Langdon (P6.2); River Road floods (P6.3); mud season (P15.3); kindergarten class sizes (P18.2).
- **Middle school and support:** special education staffing and the move from the primary school (P7.1, P7.3); homeschool sports and band, EFAs and yearly paperwork (P10.1, P10.2, P10.3); after-school tutoring (P11.2); fair week absences (P15.2); Algebra I in 8th grade (P16.1); bullying and phones (P17.1); building security (P17.2); a sports participation fee (P17.3).
- **High school:** shop, welding and trades or the Claremont center (P2.1); apprenticeships (P2.2); internships (P8.2); options besides Fall Mountain (P9.3, P16.3); RVCC dual enrollment (P12.1); AP and honors running (P12.2); a late bus (P12.3); FFA (P15.1).
- **Money:** Charlestown's share against Walpole and Acworth (P3.1, P19.1); the Cooperative Review Committee (P3.2); the default budget (P3.3); North Charlestown Community School (P6.1); one of the highest tax rates (P9.2); new SAU leadership (P13.2); leaving Fall Mountain to run a K–8 (P19.2); repairs in Langdon against Charlestown (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Claremont/` | Claremont and the Sugar River Valley Regional Technical Center. |
| `town/Keene/` | Keene, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Peterborough, New Ipswich, Hinsdale, Winchester and Charlestown (this wave); Strafford, Pittsfield, Hopkinton, Hillsborough, Wilton, Wakefield, Milton, Moultonborough, Nottingham and Northwood (running). Don't write facts about those towns.

## Where facts go

- `district Fall Mountain Regional` for the schools and the district's budget and board.
- `sau 60` for SAU-wide facts.
- `town Charlestown` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Charlestown/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Charlestown Primary and young families: pre-K, drop-off traffic, walking or busing from the village, ratings and class sizes, scores and reading help, after-school care, the bus company and drop-off changes, free meals and summer meals, bus ride lengths, storm calls and floods, paper notices, enrolling mid-year, mud season, child care in town, private and parochial options | `charlestown-primary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P6.2, P6.3, P11.1, P14.2, P15.3, P18.1, P18.2, P18.3 |
| 2 | Charlestown Middle, support and choices: the grade portal, special education staffing, IEPs and the move up, homeschool access, EFAs and paperwork, math tutoring, counseling, fair week absences, Algebra I, enrichment, bullying and phones, building security, middle school sports | `charlestown-middle-support-and-choices.md` | `raw/middle/` | P2.3, P7.1, P7.2, P7.3, P10.1, P10.2, P10.3, P11.2, P11.3, P15.2, P16.1, P16.2, P17.1, P17.2, P17.3 |
| 3 | Fall Mountain High and career programs: shop, welding and the Claremont center, apprenticeships, job readiness, internships, other high school options, RVCC dual enrollment, AP and honors, the late bus, FFA and agriculture, VLACS and tuitioning elsewhere, graduates' outcomes | `fall-mountain-high.md` | `raw/high/` | P2.1, P2.2, P8.1, P8.2, P9.3, P12.1, P12.2, P12.3, P15.1, P16.3, P20.1 |
| 4 | Money and governance: Charlestown's share against the other towns, the Cooperative Review Committee, the default budget, North Charlestown Community School, accountability, staying in Charlestown, the tax rate, para and driver retention, SAU 60's leadership, budget timing, the tax bill split, home values, the cooperative's history and votes, leaving Fall Mountain, repairs in Langdon, speaking at meetings, the SAU budget in plain English | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.1, P8.3, P9.1, P9.2, P13.1, P13.2, P13.3, P14.1, P14.3, P19.1, P19.2, P19.3, P20.2, P20.3 |
