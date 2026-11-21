# Farmington Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Farmington and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Farmington/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Farmington

- **Farmington** is a town in Strafford County north of Rochester, along Routes 11 and 75. Site town id 175.
- **The Farmington School District** (site district id 175) is **SAU 61**, a one-district SAU. Its schools:
-   - Valley View Community School (27980), preschool to grade 3;
-   - Henry Wilson Memorial (22055), grades 4–8;
-   - Farmington High (22050), grades 9–12.
- **Career and technical education:** check which regional center Farmington High students attend. Rochester's R.W. Creteau Regional Technology Center is a likely one; Rochester's research (`town/Rochester/`) mentions Farmington. Write Farmington's side.
- **Starting pages:** the district, https://www.farmington.k12.nh.us; the town, https://www.farmington.nh.us.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 961 (2014-15), 796 (2019-20), 672 (2025-26); cost per pupil FY2025 Farmington $24,893, state $22,699; 2025 tax rates per $1,000: total $15.64, local school $7.56, municipal $5.29; Question 2: Farmington 69.8%, so the cap is adopted (unofficial); math proficiency 2026: Farmington 31%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Farmington's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Farmington)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** a 7:30 start at Valley View (P1.1); pre-K spots (P2.1); bus drop-offs at another address (P2.3); about a third proficient in math at Henry Wilson (P7.1); Algebra 1 in 8th grade (P7.2); grades 4–8 together (P8.1); a late bus (P8.2); a Special Education Coordinator opening (P6.1); Orton-Gillingham training (P6.2); CTE welding and auto (P11.1); shop classes (P11.3); AP and Running Start (P12.1); athletic fees (P13.3); team rosters (P13.2).
- **Money:** a $160,000 warrant article (P13.1); the budget raising the rate over $3.25 (P16.1); the default budget (P16.2); Question 2 lowering taxes (P16.3); ratings against Strafford (P17.2); teacher turnover (P19.1); old buildings (P19.3); adequacy aid (P20.2); special education costs (P20.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Rochester/` | Rochester's schools and its career center (check Farmington's place in it); comparisons (P2.2). |
| `town/Dover/` | Comparisons (P2.2). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Pembroke, Weare, Barrington, Somersworth (this wave), and Amherst, Hollis, Litchfield and Hooksett (running). Don't write facts about those towns.

## Where facts go

- `district Farmington` for SAU 61, its three schools, the preschool, policies, staff, budget and board.
- `district Rochester` only for a fact about Rochester's career center that Rochester's files lack.
- `town Farmington` for town government and services.
- No place for general NH rules.

All agents write in `town/Farmington/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; Farmington High to agent 3; Henry Wilson to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Valley View and young families: start times and care, meals, delays, pre-K, reading against Dover and Rochester, bus drop-offs, bus rides, phonics help, snacks, PowerSchool, after-school clubs, moving across town, enrollment papers, nurses, counselors | `valley-view-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P2.3, P3.1, P3.2, P3.3, P4.1, P4.2, P4.3, P5.1, P5.2, P5.3 |
| 2 | Henry Wilson: special education staffing and training, IEP moves, math, Algebra 1, screen time, grades 4–8 together, late buses, bullying, EFAs and homeschool access, returning from homeschool, out-of-state placement, the move to the high school | `henry-wilson.md` | `raw/middle/` | P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P9.1, P9.3, P10.1, P10.2 |
| 3 | Farmington High: security and SROs, CTE access and schedule, shop classes, AP and dual enrollment, counselors, college readiness, team rosters, athletic fees, help for freshmen falling behind, phones, attendance calls, transfers, alternative pathways, mental health resources, work-study, money and work skills | `farmington-high-school.md` | `raw/high/` | P10.3, P11.1, P11.2, P11.3, P12.1, P12.2, P12.3, P13.2, P13.3, P14.1, P14.2, P14.3, P15.1, P15.2, P15.3, P18.1, P18.2 |
| 4 | Money and governance: state funding when families leave, the $160,000 article, the rate increase, the default budget, Question 2, the budget breakdown, ratings, home values, scholarships and donations, teacher turnover, community use of buildings, old buildings, rents, adequacy aid, special education costs | `money-and-governance.md` | `raw/money/` | P9.2, P13.1, P16.1, P16.2, P16.3, P17.1, P17.2, P17.3, P18.3, P19.1, P19.2, P19.3, P20.1, P20.2, P20.3 |
