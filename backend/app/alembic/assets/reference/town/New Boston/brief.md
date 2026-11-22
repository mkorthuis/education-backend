# New Boston Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for New Boston and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/New Boston/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about New Boston

- **New Boston** is a town in Hillsborough County west of Goffstown. Site town id 377.
- **The New Boston School District** (site district id 377) is in **SAU 19** with Goffstown (Dunbarton is not in SAU 19; corrected after the research). It runs New Boston Central School (20715); check its grades (K–6 per the questions) and preschool. Check its budget form.
- **Grades 7–12:** Mountain View Middle (7–8) and Goffstown High (9–12) under an AREA agreement renewed by both districts' voters in March 2022 (`places.yaml`). Goffstown is researched in `town/Goffstown/` (mountain-view-high-school-and-mst.md, getting-to-school-and-choices.md, money-buildings-and-governance.md, elementary-and-special-education.md); cite it and write New Boston's side.
- **Reuse first.** Much of this town's shared district or high school is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 983 (2014-15), 1,069 (2019-20), 902 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): New Boston Central 459; cost per pupil FY2025 New Boston $20,442, state $22,699; 2025 tax rates per $1,000 (New Boston): total $23.67, local school $14.83, municipal $6.17; Question 2: New Boston 59.5% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): New Boston's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (New Boston)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **NBCS:** full-day kindergarten class sizes (P1.1); the Rec after-school waitlist (P1.2); enrichment (P4.2); recess (P9.1); preschool (P10.1); snow and mud days (P10.3); counselors and a nurse (P13.2); water testing (P18.3); allergies (P17.1).
- **Grades 7–12:** shop and vocational tracks (P2.1); ride times to Mountain View (P2.2, P15.2); late buses (P2.3); IEPs into 7th grade (P6.2); New Boston students treated equally (P8.3); bus tracking and Wi-Fi (P14.2).
- **Money:** the tax bill (P3.1); the HB 1300 cap vote (P3.2); a growing SAU office (P3.3, P16.3); a new superintendent (P5.3); a bond (P5.2); busing costs (P12.1); tuition to Goffstown (P12.2); teacher turnover (P12.3); deliberative session timing (P16.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Goffstown/` | Mountain View Middle, Goffstown High, MST, SAU 19, the AREA agreement and Goffstown's budget. |
| `town/Weare/`, `town/Bedford/` | Neighboring districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Ossipee, Candia, Gilmanton, New Boston and North Hampton (this wave); Allenstown, Epsom, Deerfield, Auburn, Wolfeboro, Newton, Rindge, Boscawen, Barnstead and Northfield (running). Don't write facts about those towns.

## Where facts go

- `district New Boston` for NBCS, the district's budget, board and its side of the AREA agreement.
- `district Goffstown` only for Mountain View or Goffstown High facts Goffstown's files lack.
- `sau 19` for SAU-wide facts not in Goffstown's files.
- `town New Boston` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/New Boston/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | New Boston Central and young families: kindergarten class sizes, Rec after-school care and waitlists, nearby daycares, scores, communication, recess, reading help, phones and smartwatches, the preschool, drop-off and pickup, snow and mud days, meals, allergies, emergencies, recess and bus supervision, twins' classrooms, early release days | `nbcs-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.3, P9.1, P9.2, P9.3, P10.1, P10.2, P10.3, P15.1, P17.1, P17.2, P17.3, P20.1, P20.2 |
| 2 | Support and choices: enrichment, IEPs at NBCS and into Mountain View, aides under a cap, homeschool and EFA access, entering Goffstown High from homeschool, the move to Mountain View, bullying, equal treatment in Goffstown, counselors and the nurse, welcoming families, outdoor programs, science labs, water testing, alternatives to a big high school, attendance and anxiety | `support-and-choices.md` | `raw/support/` | P4.2, P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P13.2, P13.3, P18.1, P18.2, P18.3, P19.2, P19.3 |
| 3 | Mountain View and Goffstown High from New Boston: shop and vocational tracks, ride times, late buses, college preparation and advanced courses, technology classes, bus tracking, getting there without the bus, fees, graduates' readiness for work, mental health support | `mountain-view-and-goffstown-high.md` | `raw/high/` | P2.1, P2.2, P2.3, P11.1, P14.1, P14.2, P15.2, P15.3, P16.2, P19.1 |
| 4 | Money and governance: the school share of the tax bill, the HB 1300 vote, SAU 19 costs, the budget breakdown, buildings and bonds, the new superintendent, school reputation for buyers, New Boston's voice in Goffstown's schools, busing costs, tuition to Goffstown, teacher turnover, affordability, the two boards, deliberative session timing, board meetings | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P5.1, P5.2, P5.3, P11.2, P11.3, P12.1, P12.2, P12.3, P13.1, P14.3, P16.1, P16.3, P20.3 |
