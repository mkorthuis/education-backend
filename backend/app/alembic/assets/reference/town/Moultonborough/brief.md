# Moultonborough Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Moultonborough and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Moultonborough/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Moultonborough

- **Moultonborough** is a town in Carroll County on the north shore of Lake Winnipesaukee; it has a large share of seasonal homes and a very low tax rate. Site town id 369.
- **The Moultonborough School District** (site district id 369) is **SAU 45** and runs Moultonborough Central School (22115; preschool to grade 5), the Moultonborough Middle Level (26960; grades 6–8) and Moultonborough Academy (22120; grades 9–12). It decides its budget at a traditional annual meeting (March 14, 2026).
- **Career programs:** the Lakes Region Technology Center (LRTC) at Kingswood in Wolfeboro, researched in `town/Wolfeboro/` (kingswood-high-and-lrtc.md) and by Farmington's research. Cite them; write Moultonborough's side (access, the bus, how many students attend).
- **Comparisons** with Inter-Lakes (`town/Meredith/`), Gilford (`town/Gilford/`) and Kingswood (`town/Wolfeboro/`) can use those files and the site's data.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 500 (2014-15), 435 (2019-20), 435 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Moultonborough Central 245, Middle Level 109, Moultonborough Academy 137; cost per pupil FY2025 Moultonborough $34,375, state $22,699; 2025 tax rates per $1,000 (Moultonborough): total $5.33, local school $1.85, municipal $1.68; Question 2: Moultonborough 62.6% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Moultonborough's kindergarten cutoff, kindergarten day, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Moultonborough)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Central School:** universal preschool and its hours and bus (P1.1, P1.2); enrollment dipping (P1.3, P3.1, P20.1); care before and after school (P5.1); Blizzard Bag days (P5.2); a reading specialist and Orton-Gillingham (P7.1); Alma (P11.1); the Black Point bus ride (P14.2); ESL (P15.1).
- **Middle Level and Academy:** how separate grades 6–8 are from the high school (P4.1); early algebra or coding (P4.2); a shared psychologist and social worker (P10.2); about 135 high schoolers and live AP or honors (P8.1, P18.1); ELOs (P8.2); LRTC bus time (P2.1); shop or marine classes (P2.2); sports co-ops (P13.1); electives at risk (P16.1); a mentoring program at MCS (P19.3); dual enrollment at Lakes Region Community College (P20.3).
- **Money:** a 'donor town' return (P3.2); sharing with Meredith or Sandwich (P3.3); half the tax bill to schools (P6.1); tuitioning to Inter-Lakes or Kingswood (P6.2); state special education aid cuts (P7.3); support staff jobs (P10.1); spending against scores (P16.3, P17.1); school choice from the Center Harbor line (P17.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Wolfeboro/`, `town/Farmington/` | LRTC and Kingswood. |
| `town/Meredith/`, `town/Gilford/` | Inter-Lakes and Gilford, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Wakefield, Milton, Moultonborough, Nottingham and Northwood (this wave); Greenland, Rye, Brentwood, Fremont, Chester, Ossipee and New Boston (running). Don't write facts about those towns.

## Where facts go

- `district Moultonborough` for the three schools and the district's budget, meeting and board.
- `district Governor Wentworth Regional` only for LRTC facts Wolfeboro's files lack.
- `sau 45` for SAU-wide facts.
- `town Moultonborough` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Moultonborough/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Moultonborough Central School and young families: universal preschool and its bus, class sizes, before- and after-school care, Blizzard Bag days, meals, reading help and structured literacy, small classes, Alma help, welcoming newcomers, bus rides, phones and screens, translation and ESL, summer programs, a missed bus | `central-school-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P7.1, P10.3, P11.1, P14.1, P14.2, P14.3, P15.1, P15.2, P15.3 |
| 2 | The Middle Level, support and choices: grades 6–8 beside the high school, advanced math and coding, IEPs at Blake Road, the psychologist and social worker, tutoring and counseling, EFA and homeschool access, homeschool credits, middle school basketball, school choice, 504 plans, the high school mentoring program | `middle-level-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P7.2, P10.2, P11.2, P11.3, P12.1, P12.3, P13.2, P17.2, P18.2, P19.3 |
| 3 | Moultonborough Academy and LRTC: the LRTC bus, shop and marine classes, trades help, AP and honors, ELOs, college counseling, trades and emergency services, sports co-ops, electives at risk, school climate, a small school for an anxious student, half days and ELOs, new practical courses, stress, local scholarships, dual enrollment costs | `moultonborough-academy-and-lrtc.md` | `raw/high/` | P2.1, P2.2, P2.3, P8.1, P8.2, P8.3, P9.2, P13.1, P16.1, P17.3, P18.1, P18.3, P19.1, P19.2, P20.2, P20.3 |
| 4 | Money and governance: budgets against enrollment, donor-town risk, sharing with neighbors, comparisons with Inter-Lakes and Gilford, value for seasonal owners, tuitioning out, a tax cap, special education aid, teacher housing, warrant articles in plain English, support staff jobs, families leaving, facilities, budget drivers, spending against scores, consolidation | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P4.3, P6.1, P6.2, P6.3, P7.3, P9.1, P9.3, P10.1, P12.2, P13.3, P16.2, P16.3, P17.1, P20.1 |
