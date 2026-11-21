# Durham Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Durham and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Durham/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Durham

- **Durham** is a town in Strafford County, home of the University of New Hampshire, along Routes 4, 108 and 155A. Site town id 151.
- **The Oyster River Cooperative School District** (site district id 423) is **SAU 5**, for Durham, Lee and Madbury, voting by official ballot. Schools: Oyster River Preschool Education Program (29210); Mast Way (22805, in Lee) and Moharimet (26660, in Madbury), K–4; Oyster River Middle (22790), 5–8; Oyster River High (22800), 9–12.
- **Career and technical education:** Oyster River students attend Dover's career center. Dover's research covers it (`town/Dover/high-school-and-ctc.md`); write only Oyster River's side.
- **Starting pages:** the district, https://www.orcsd.org; the town, https://www.ci.durham.nh.us.
- **Site figures:** Durham's resident students 936 (2014-15), 942 (2019-20), 836 (2026-27); cost per pupil FY2025 Oyster River $23,921, Dover and Portsmouth on the site (P8.3), state $22,699; 2025 tax rates per $1,000: Durham total $18.87, local school $10.79, municipal $5.12; Question 2: Durham 38.0% yes, the cooperative 44.7%, so no cap (unofficial; P3.1); math proficiency 2026: Oyster River 69%, state 44%.
- **Oyster River is shared with Lee and Madbury.** Facts about the district are `district Oyster River Coop` and serve all three towns; write them in Durham's folder (Lee and Madbury have no research yet).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Oyster River's kindergarten, registration, preschool and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Oyster River Coop)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** both elementary schools in Lee and Madbury and how Durham families are assigned (P1.1, P18.2); bus rides (P1.2); on-site care (P1.3); ORPEP for children without special needs (P5.2); class sizes (P9.3); the 1–4 report card scale (P13.1); dyslexia screening (P15.3); geometry or algebra II in middle school (P2.1); UNH courses (P2.2); the calendar against UNH's (P2.3); an 8:15 start and later than the middle school (P6.2, P16.2); CTE in Dover and the bus (P7.1, P7.2); the paraeducator contract (P4.1); solar panels and trays (P19.1, P19.2).
- **Money:** a $9.8 million elementary bond that failed by 41 votes (P3.1, P9.1, P9.2); Question 2 voted down (P3.1); 77% on salaries and benefits and Durham's share against Lee and Madbury (P3.2); the turf fund (P6.1); a performance audit article (P8.2); $519,000 added at the deliberative session (P20.2); a superintendent search and the 2026–2031 strategic plan (P14.2, P20.1); UNH land and the tax rolls (P12.3); open enrollment (P18.1, P18.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Dover/high-school-and-ctc.md`, `town/Dover/choices-and-adult-learning.md` | Dover's career center and its sending districts; Seacoast Charter School and St. Thomas Aquinas and other choices. |
| `town/Portsmouth/` | Portsmouth's schools, for the comparisons in P8.3. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Stratham, Epping, Newmarket, Raymond (this wave), and from the first wave Atkinson, Plaistow (shared `town/timberlane/`), Hampstead, Pelham and Seabrook. Don't write facts about those towns.

## Where facts go

- `district Oyster River Coop` for the district, its schools, ORPEP, policies, staff, budget and board.
- `town Durham` for Durham's town government and services (tax rate, exemptions, UNH and the tax rolls, recreation).
- Charter and private schools: their own district record if the loader has one (Seacoast Charter School), otherwise `town Durham` with the school named.
- No place for general NH rules.

All agents write in `town/Durham/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, bonds and governance belong to agent 4; the middle and high school to agent 2; the elementary schools and preschool to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Mast Way, Moharimet and the early years: which school, bus rides, care, renters' enrollment, ORPEP, meals privacy, class sizes, the 1–4 report card, paper notices, counselors, reading instruction and specialists, dyslexia screening, ESL, placing children who move in for a few years, translation, choosing a school | `elementary-and-early-years.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P9.3, P13.1, P13.2, P13.3, P15.1, P15.2, P15.3, P17.1, P17.2, P17.3, P18.2 |
| 2 | Oyster River Middle and High: advanced math in middle school, UNH dual credit, the calendar, the turf, away-game buses and the start time, concussion return-to-learn, CTE in Dover and the bus, apprenticeship credit, middle school phones, laptops and paper, bullying, internships, counselors and AP pressure, start times, competency grading on transcripts, environmental electives | `middle-and-high-school.md` | `raw/high/` | P2.1, P2.2, P2.3, P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P11.1, P11.2, P11.3, P12.2, P16.1, P16.2, P16.3, P19.3 |
| 3 | Support and choices: aides after the paraeducator contract, 504 and IEP moves to the middle school, evaluations and tutoring, EFAs, Seacoast Charter and homeschooling, St. Thomas Aquinas students in ORCSD activities, returning mid-year, open enrollment and its costs, Coe Drive traffic, solar and cafeteria waste | `support-and-choices.md` | `raw/support/` | P4.1, P4.2, P4.3, P10.1, P10.2, P10.3, P12.1, P18.1, P18.3, P19.1, P19.2 |
| 4 | Money and governance: the failed bond and where students go, Question 2, Durham's share against Lee and Madbury, senior tax relief, the performance audit, spending against Dover and Portsmouth, the bond's return, UNH land and taxes, schools and buying a home, the superintendent search, yearly school tax increases, the strategic plan, deliberative session amendments, the FY28 cost driver | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P8.1, P8.2, P8.3, P9.1, P9.2, P12.3, P14.1, P14.2, P14.3, P20.1, P20.2, P20.3 |
