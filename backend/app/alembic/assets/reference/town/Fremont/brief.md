# Fremont Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Fremont and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Fremont/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Fremont

- **Fremont** is a town in Rockingham County between Raymond and Kingston. Site town id 189.
- **The Fremont School District** (site district id 189) is **SAU 83** and runs Ellis School (20525); check its grades, preschool and budget form.
- **High school:** tuition contracts with Pinkerton Academy and Epping (grades 9–12) and Sanborn Regional (grades 10–12, being phased out) (`places.yaml`). Researched in `town/pinkerton/`, `town/Epping/` (middle-high-school.md, money-and-governance.md) and `town/Kingston/` (Sanborn); SST in `town/Exeter/`. Cite them; write Fremont's side.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 673 (2014-15), 592 (2019-20), 460 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Ellis School 353; cost per pupil FY2025 Fremont $22,802, state $22,699; 2025 tax rates per $1,000 (Fremont): total $16.95, local school $12.07, municipal $3.28; Question 2: Fremont 72.5% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Fremont's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Fremont)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Ellis:** after-school care (P1.1); the preschool lottery (P1.2); early drop-off (P1.3, P11.1); scores near 43% (P6.1, P16.1); speech and paras (P5.1); trades classes (P4.3); Algebra I (P12.1); Chromebooks and phones (P15.1, P15.2); world languages (P17.3).
- **High school choice:** Pinkerton or Epping (P2.1); bus times and late buses (P2.2, P2.3); SST (P4.1, P4.2, P14.1); IEPs (P5.3); Sanborn seniors (P7.2); spring breaks (P7.1); switching schools (P18.3).
- **Money:** a $15 million budget (P3.1); savings from leaving Sanborn (P3.2); a failed budget (P3.3); cost per pupil over $22,000 (P10.1); the teacher contract (P10.3); the building (P16.2); a one-school SAU (P16.3).
- **Home education:** an annual evaluation to SAU 83 (P9.2; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/pinkerton/` | Pinkerton Academy. |
| `town/Epping/` | Epping High School and Epping's side of its Fremont contract. |
| `town/Kingston/` | Sanborn Regional and its Fremont tuition. |
| `town/Exeter/` | SST. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Greenland, Rye, Brentwood, Fremont and Chester (this wave); Ossipee, Candia, Gilmanton, New Boston and North Hampton (running or starting). Don't write facts about those towns.

## Where facts go

- `district Fremont` for Ellis and the district's budget, board and tuition contracts.
- `district Pinkerton Academy`, `district Epping` or `district Sanborn Regional` only for facts about those schools that their files lack.
- `sau 83` for SAU-wide facts.
- `town Fremont` for town government, recreation, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Fremont/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Ellis School's early grades and families: after-school care, the preschool lottery, drop-off times, scores, before-school care, storm notices, bus changes, paper notices, the kindergarten cutoff, mid-year registration, world languages, volunteering, lunch, early-release Wednesdays, emergencies, drills, bus cameras | `ellis-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P6.1, P11.1, P11.2, P11.3, P13.2, P17.1, P17.2, P17.3, P19.1, P19.2, P19.3, P20.1, P20.2, P20.3 |
| 2 | Ellis's upper grades, support and choices: trades classes, speech and paras, specialized placements, middle school sports, homeschool and EFA access, entering high school from homeschool, Algebra I, academic clubs, bus bullying, counseling, Chromebooks, phones, the 6th-grade transition, math results | `ellis-upper-grades-support-and-choices.md` | `raw/middle/` | P4.3, P5.1, P5.2, P8.3, P9.1, P9.2, P9.3, P12.1, P12.3, P13.1, P13.3, P15.1, P15.2, P15.3, P16.1, P18.2 |
| 3 | High school choice and SST from Fremont: Pinkerton or Epping, bus times and late buses, SST and transport, IEPs into high school, the choice itself, calendars, Sanborn seniors, fitting in at Epping, varsity chances, AP and dual enrollment, SST awareness, scholarships, credit recovery, size, switching schools | `high-school-choice.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.1, P4.2, P5.3, P6.2, P7.1, P7.2, P7.3, P8.2, P12.2, P14.1, P14.2, P14.3, P18.1, P18.3 |
| 4 | Money and governance: the budget against enrollment, savings from leaving Sanborn, a failed budget, serving on the board, facility rentals, cost per pupil, the deliberative session, the teacher contract, the building, a one-school SAU | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.3, P8.1, P10.1, P10.2, P10.3, P16.2, P16.3 |
