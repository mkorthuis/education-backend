# Auburn Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Auburn and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Auburn/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Auburn

- **Auburn** is a town in Rockingham County east of Manchester, beside Lake Massabesic. Site town id 29.
- **The Auburn School District** (site district id 29) is in **SAU 15** with Candia and Hooksett. It runs Auburn Village School (20530), preschool to grade 8. It decides its budget by official ballot (SB2).
- **High school:** Pinkerton Academy (site district id 999) under a tuition contract from 2013 (`places.yaml`: a 20-year term extending 5 years each July unless notice is given; policy JCB lets up to 5% of a class attend another public high school). Pinkerton is researched in `town/pinkerton/` and Hooksett's side of SAU 15 and Pinkerton in `town/Hooksett/`. Cite them; write Auburn's side.
- **Candia** (also SAU 15) is researched in a later wave and will cite SAU-wide facts written here; place those `sau 15`.
- **Starting pages:** SAU 15, https://www.sau15.net (Auburn School Board, budgets, policies); Auburn Village School's pages; the Town of Auburn's site for taxes and town reports.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 868 (2014-15), 936 (2019-20), 952 (2025-26); school enrollment (the site's "2025" row is the October 1, 2024 count): Auburn Village School 692 in 2024-25; cost per pupil FY2025 Auburn $14,653, state $22,699; 2025 tax rates per $1,000: total $13.88, local school $9.93, municipal $2.21; Question 2: Auburn 61.8% yes (unofficial), adopted by the district.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Auburn's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Auburn)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **AVS:** a before- and after-school waitlist (P1.1); rec buses on early-release days (P1.2); about 59% proficiency (P4.2); class sizes (P4.3); paras and reading specialists (P5.2); the earliest bus (P7.1); full-day kindergarten (P10.1); public preschool (P10.2); Algebra I in grade 8 (P13.3); band (P20.1); fees (P20.2).
- **Pinkerton:** who runs the buses (P2.2); late buses (P2.3, P20.3); a 'private' academy and admission (P4.1); IEPs (P5.3); CTE seats against Derry students (P6.2); AP and dual enrollment (P11.2); parking (P11.3); shadow days (P16.3); out-of-state credits (P19.3).
- **Money:** taxes against enrollment (P3.1); about $15,135 per student (P3.2); a budget cap (P3.3); students sent elsewhere in SAU 15 (P10.3); tuition to Pinkerton (P12.2); sharing SAU 15 (P12.3); a median income over $150,000 and no high school of its own (P17.2).
- **Home education:** sports, band and single classes for homeschoolers (P9.1, P9.3).

## Already researched

| File | What it covers |
|---|---|
| `town/pinkerton/` | Pinkerton Academy: courses, CTE, counseling, student life. |
| `town/Hooksett/` | SAU 15, Hooksett's side of Pinkerton, its tuition and buses. |
| `town/Derry/`, `town/Londonderry/` | Neighboring districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (this wave); Kingston, Jaffrey, Loudon, Alton and Tilton (finishing); Newton, Rindge, Boscawen, Barnstead and Northfield (starting soon). Don't write facts about those towns.

## Where facts go

- `district Auburn` for Auburn Village School, the district's budget, board, policies and its side of the Pinkerton contract.
- `district Pinkerton Academy` only for facts about Pinkerton itself not already in `town/pinkerton/`.
- `sau 15` for SAU-wide facts.
- `town Auburn` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Auburn/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money, taxes and governance belong to agent 4; Pinkerton to agent 3; AVS's middle grades, support and choices to agent 2; AVS's early grades and families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Auburn Village School's early grades and families: before- and after-school care, early-release days, PickUp Patrol changes, scores, class sizes, the earliest bus, storm calls, meal help, full-day kindergarten, public preschool, residency papers, bus routes, recess, homework, volunteering, teacher communication, security, records from out of state | `avs-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.2, P4.3, P7.1, P7.2, P7.3, P10.1, P10.2, P14.1, P14.2, P15.1, P15.3, P18.1, P18.2, P18.3, P19.1 |
| 2 | AVS's middle grades, support and choices: IEPs, paras and reading specialists, shop and life skills, Chromebooks and homework, phones, sports and clubs, homeschool access and re-enrollment, accelerated math and Algebra I, gifted programs, ESL, outdoor learning, bullying, homeroom requests, new students mid-year, band and fees | `avs-middle-grades-support-and-choices.md` | `raw/middle/` | P5.1, P5.2, P6.3, P8.1, P8.2, P8.3, P9.1, P9.2, P9.3, P13.1, P13.2, P13.3, P14.3, P15.2, P16.1, P16.2, P19.2, P20.1, P20.2 |
| 3 | Pinkerton Academy from Auburn: the move to a big school, buses and late buses, admission, IEPs, CTE (welding, electrical, auto) and seats, counseling, AP and dual enrollment, parking, 8th-grade visits, out-of-state credits, staying after school for plays and concerts | `pinkerton-from-auburn.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.1, P5.3, P6.1, P6.2, P11.1, P11.2, P11.3, P16.3, P19.3, P20.3 |
| 4 | Money and governance: school taxes against enrollment, per-pupil spending, a budget cap, SAU 15 and whether students are sent elsewhere, how much of the budget stays at AVS, tuition to Pinkerton, sharing SAU 15, home values, why Auburn has no high school, the yearly tax effect | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P10.3, P12.1, P12.2, P12.3, P17.1, P17.2, P17.3 |
