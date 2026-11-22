# Newton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Newton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Newton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Newton

- **Newton** is a town in Rockingham County on the Massachusetts border, east of Plaistow. Site town id 403.
- **The Sanborn Regional School District** (site district id 476) is **SAU 17**, for Kingston and Newton. Its schools: Daniel J. Bakie (20625), preschool to grade 2, in Kingston; Memorial (20635), grades 3–5, in Newton; Sanborn Regional Middle (20630) and High (20620), both in Kingston.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 711 (2014-15), 607 (2019-20), 534 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Bakie 269, Memorial 239, Sanborn Middle 251, Sanborn High 448; cost per pupil FY2025 Sanborn $27,191, state $22,699; 2025 tax rates per $1,000 (Newton): total $16.77, local school $12.22, municipal $2.91; Question 2: Newton 72.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Sanborn's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Sanborn Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** the bus ride to Bakie (P1.1); full-day kindergarten (P1.2); two schools in two towns (P2.1); care at Memorial (P3.1); scores against Atkinson and Exeter (P3.2); ESL at Memorial (P10.3); preschool screening and the district preschool (P20.1–P20.3).
- **Middle and high school:** phones (P6.1); a late bus to Newton (P6.2); AP and honors (P7.1); class sizes (P7.3); SST and its schedule (P8.1, P8.3); internships (P14.1); graduates' plans (P17.1).
- **Money:** Newton's share rising while enrollment falls (P11.1, P19.2); the state tax cap (P11.3); empty classrooms and consolidation (P12.2); Sanborn against Timberlane (P18.3); the default budget (P19.3).
- **Support:** foster care (P15.1, P15.2); counselors at Memorial (P16.2); Massachusetts calendars (P10.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Kingston/` (elementary-and-families.md, support-and-choices.md, middle-high-and-sst.md, money-and-governance.md) | Sanborn's schools, buses, care, policies, the middle and high school, SST, the budget, the Kingston–Newton cost split and votes. |
| `town/Exeter/` | The Seacoast School of Technology. |
| `town/timberlane/`, `town/Atkinson/`, `town/Plaistow/` | Timberlane, for comparisons (P18.3). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newton, Rindge, Boscawen, Barnstead and Northfield (this wave); Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (running). Don't write facts about those towns.

## Where facts go

- `district Sanborn Regional` for Memorial and any new district-wide fact.
- `sau 17` for SAU-wide facts.
- `town Newton` for town government, recreation, taxes and community programs.
- No place for general NH rules.

All agents write in `town/Newton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school and career programs to agent 3; support and choices to agent 2; the elementary school and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Memorial, Bakie and young families: the bus to Bakie, full-day kindergarten, registration, two schools in two towns, buses and delays, care at Memorial, scores, early drop-off, bus changes, meals, summer programs, English learners, the pickup list, menus and notices, the nurse, preschool screening and the district preschool | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P2.3, P3.1, P3.2, P3.3, P5.1, P5.2, P5.3, P10.3, P13.1, P13.2, P13.3, P20.1, P20.2, P20.3 |
| 2 | Support and choices: speech and OT, evaluations, IEPs moving to the middle school, homeschool and EFA access, returning to public school, enrolling mid-year, the calendar against Massachusetts, foster care, counseling, bullying, counselors at Memorial, safety follow-up | `support-and-choices.md` | `raw/support/` | P4.1, P4.2, P4.3, P9.1, P9.2, P9.3, P10.1, P10.2, P15.1, P15.2, P15.3, P16.1, P16.2, P16.3 |
| 3 | Sanborn Middle and High School and SST from Newton: phones, the late bus, homework, AP and honors, college credit, class sizes, SST welding and automotive, shop classes, the half-day schedule, internships, work permits, graduates' plans, FAFSA and scholarships, graduating early and VLACS, residents' use of the track | `middle-high-and-sst.md` | `raw/high/` | P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P14.1, P14.3, P17.1, P17.2, P17.3, P18.2 |
| 4 | Money and governance: Newton's share of the school tax, the school part of the tax bill, the state tax cap, per-pupil spending, empty classrooms and consolidation, voting and the deliberative session, district contracts, school quality and home values, Sanborn against Timberlane, board meetings online, the Kingston–Newton split, the default budget | `money-and-governance.md` | `raw/money/` | P11.1, P11.2, P11.3, P12.1, P12.2, P12.3, P14.2, P18.1, P18.3, P19.1, P19.2, P19.3 |
