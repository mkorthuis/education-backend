# Hollis Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hollis and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hollis/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hollis

- **Hollis** is a rural town in Hillsborough County on the Massachusetts line, west of Nashua, along Routes 111, 122 and 130, with orchards and farms. Site town id 259.
- **Two school districts serve Hollis, both in SAU 41** (with Brookline):
-   - **The Hollis School District** (site district id 259), with Hollis Primary (21815), preschool to grade 3, and Hollis Upper Elementary (27530), grades 4–6.
-   - **The Hollis-Brookline Cooperative** (site district id 260), with Hollis-Brookline Middle (21805), grades 7–8, and Hollis-Brookline High (21810), grades 9–12.
- **Career and technical education:** Hollis-Brookline students attend the Nashua Technology Center and Hudson's Palmer Center (Hudson counts 37 Hollis/Brookline students). Both are researched; write only HBHS's side.
- **Starting pages:** SAU 41, https://www.sau41.org; the town, https://www.hollisnh.org.
- **Site figures:**
-   - Resident students: 1,305 (2014-15), 1,302 (2019-20), 1,263 (2026-27).
-   - Cost per pupil, FY2025: Hollis $23,370 (K–6), the cooperative $23,443, Amherst $23,894, state $22,699.
-   - 2025 tax rates per $1,000: total $18.90, local school $12.30, municipal $4.27.
-   - Question 2: Hollis 59.3%, the cooperative 61.1%, so the cap is adopted for the cooperative but not the Hollis district (unofficial; check).
-   - Math proficiency, 2026: Hollis 67%, the cooperative 65%.
- **Shared cooperative:** Hollis-Brookline and SAU 41 serve Brookline too. Write their facts here with `district Hollis-Brookline Cooperative` or `sau 41`.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Hollis's and Hollis-Brookline's kindergarten, registration, preschool and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Hollis|Hollis-Brookline Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:**
-   - HPS at 8:23, HUES at 8:30 and the middle school at 7:35 (P1.3, P5.1);
-   - guaranteed after-school spots (P1.2);
-   - the preschool lottery, tuition and a 2.5-hour session (P9.1, P9.2);
-   - full-day kindergarten (P20.2);
-   - a 3:05 pickup (P6.1);
-   - buses on dirt roads and cul-de-sacs (P10.2);
-   - Latin Honors replacing class rank (P8.1);
-   - AP waitlists (P8.3);
-   - about 675 high school students (P14.3);
-   - an AI policy tabled (P5.2, P19.3).
- **Money:**
-   - the Hollis Primary renovation voted down in March and HREC's next proposal (P1.1, P15.2);
-   - HPS at 400 students in a building for 340 (P20.1);
-   - extra adequacy aid (P2.2);
-   - Brookline growing faster and paying less (P12.1);
-   - the support staff contract through 2028 (P15.1);
-   - special education costs at the cooperative (P19.2);
-   - leaving the cooperative (P18.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Nashua/pathways-and-adult-learning.md`, `town/Hudson/alvirne-and-palmer-cte.md` | The Nashua Technology Center and Palmer Center: programs, admission, sending districts (37 Hollis/Brookline students at Palmer). |
| `town/Nashua/` charter files | The Academy for Science and Design (P11.2). |
| `town/Bedford/`, `town/Merrimack/` | Comparisons. |
| Amherst's research (this wave) | Amherst, for comparisons; use the site's data. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Amherst, Litchfield, Hooksett and Bow (this wave), and Stratham, Epping, Newmarket, Raymond and Durham (running). Don't write facts about those towns.

## Where facts go

- `district Hollis` for the Hollis School District, HPS and HUES, the preschool, its budget and board.
- `district Hollis-Brookline Cooperative` for HBMS, HBHS and the cooperative's budget and board.
- `sau 41` for SAU-wide facts.
- `town Hollis` for town government and services.
- No place for general NH rules.

All agents write in `town/Hollis/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budgets, taxes, bonds and governance belong to agent 4; HBMS and HBHS to agent 2; HPS and HUES to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Hollis Primary and HUES: after-school spots, start times, kindergarten registration, scores against Massachusetts, bus stops, pickup and emergencies, PickUp Patrol for split households, summer programs, IEPs moving to HUES, HUES class sizes, the preschool and its sessions, private preschool, grandparents on the pickup list, mixed-ability teaching, kindergarten | `primary-and-upper-elementary.md` | `raw/elementary/` | P1.2, P1.3, P3.1, P3.2, P3.3, P6.1, P6.2, P6.3, P7.1, P7.3, P9.1, P9.2, P9.3, P10.1, P15.3, P20.2 |
| 2 | Hollis-Brookline Middle and High: practical courses, trades, the 7:35 start, AI rules, algebra in 7th grade, Latin Honors, CTE at Nashua and Hudson, AP and honors sections, bullying and phones, trades support, sports and drama, late buses, team cuts, work-study, class sizes and counseling, credits back from Bishop Guertin | `middle-and-high-school.md` | `raw/high/` | P4.1, P4.2, P5.1, P5.2, P5.3, P8.1, P8.2, P8.3, P10.3, P12.3, P14.1, P14.2, P14.3, P17.2, P18.2, P18.3 |
| 3 | Support, choices and daily life: special transportation, buses on narrow roads, religious holidays, HBHS against ASD, early-release days, homeschoolers in sports and clubs, re-entry testing, renters' access and fees, extra fees, welcome for newcomers, snow days | `support-choices-and-daily-life.md` | `raw/support/` | P7.2, P10.2, P11.1, P11.2, P11.3, P13.1, P13.2, P13.3, P16.1, P16.2, P16.3, P17.1 |
| 4 | Money and governance: the failed HPS renovation and HREC, cooperative spending and enrollment, adequacy aid, the space crunch, farm taxes, Brookline's share, where budgets go, para pay, warrant wording, leaving the cooperative, cost per student against neighbors, special education costs, the tabled policies, HPS capacity, following the board | `money-and-governance.md` | `raw/money/` | P1.1, P2.1, P2.2, P2.3, P4.3, P12.1, P12.2, P15.1, P15.2, P17.3, P18.1, P19.1, P19.2, P19.3, P20.1, P20.3 |
