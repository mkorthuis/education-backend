# Hooksett Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hooksett and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hooksett/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hooksett

- **Hooksett** is a town in Merrimack County between Manchester and Concord, along I-93, Routes 3 and 28. Site town id 261.
- **The Hooksett School District** (site district id 261) is in **SAU 15** with Auburn and Candia. It votes by official ballot. Its schools:
-   - Fred C. Underhill (20550), preschool to grade 2;
-   - Hooksett Memorial (20540), grades 3–5;
-   - David R. Cawley Middle (28050), grades 6–8.
- **High school:** `places.yaml` lists tuition contracts for grades 9–12 with Pinkerton Academy, Manchester, Bow, Goffstown, Londonderry and Pembroke. Pinkerton is researched in `town/pinkerton/` (Hooksett is a contracted sending town), and Manchester's high schools in `town/Manchester/`. Write Hooksett's side: the choice and its rules, tuition, buses, students' counts and outcomes.
- **Starting pages:** the district and SAU 15, https://www.sau15.net; the town, https://www.hooksett.org.
- **Site figures:**
-   - Resident students: 1,973 (2014-15), 1,934 (2019-20), 1,893 (2026-27).
-   - Cost per pupil, FY2025: Hooksett $17,848, state $22,699.
-   - 2025 tax rates per $1,000: total $17.19, local school $9.98, municipal $4.28.
-   - Question 2: Hooksett 65.9%, so the cap is adopted (unofficial).
-   - Math proficiency, 2026: Hooksett 67%, state 44%.
- **SAU 15 is shared with Auburn and Candia.** Write SAU-wide facts with `sau 15`; neither town has research yet.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Hooksett's kindergarten, registration, preschool, high school options and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Hooksett)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:**
-   - half-day kindergarten at Underhill (P1.1);
-   - the pre-K lottery (P1.2);
-   - care inside Memorial (P2.1);
-   - Cawley's honors tracks and phones (P11.1, P11.2);
-   - different start times (P12.1);
-   - summer programs (P12.3);
-   - translation (P7.3);
-   - counselors at Cawley (P17.1).
- **High school:**
-   - "locked into Pinkerton" against other schools (P8.1);
-   - Pinkerton's bus times and late buses from Hooksett (P5.2, P8.2, P16.3);
-   - over 3,000 students at Pinkerton (P8.3);
-   - Pinkerton against Manchester School of Technology for trades (P5.3);
-   - who manages an IEP at Pinkerton (P7.2);
-   - private school tuition help (P19.1).
- **Money:**
-   - a 23% health insurance increase and a town tax cap (P3.1, P9.1);
-   - a $45 million budget (P3.2);
-   - Pinkerton tuition against a Hooksett high school (P3.3, P18.3);
-   - SAU 15's cost split (P9.2);
-   - Pinkerton's buildings in tuition (P15.2).

## Already researched

| File | What it covers |
|---|---|
| `town/pinkerton/pinkerton-academics-and-pathways.md`, `pinkerton-student-life.md` | Pinkerton's counselors, CTE and applications, dual enrollment, AP, special education with sending districts, the 7:15 start, phones, clubs, the freshman transition. |
| `town/Manchester/` | Manchester's high schools and Manchester School of Technology. |
| `town/Derry/`, `town/Hampstead/` (Hampstead loaded) | Other Pinkerton sending towns' sides: buses, tuition, contracts. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Amherst, Hollis, Litchfield, Bow (this wave), and Stratham, Epping, Newmarket, Raymond and Durham (running). Don't write facts about those towns.

## Where facts go

- `district Hooksett` for the Hooksett School District, its three schools, the preschool, its budget, board and high school contracts.
- `sau 15` for SAU-wide facts.
- `district Pinkerton Academy` only for a Pinkerton fact Hooksett's side needs that the Pinkerton files lack.
- `town Hooksett` for town government and services.
- No place for general NH rules.

All agents write in `town/Hooksett/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, contracts and governance belong to agent 4; the high school choice and Pinkerton side to agent 3. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Underhill and Memorial: kindergarten, the pre-K lottery, buses, care inside Memorial, late buses, scores against neighbors, moving within town, special education staffing, translation, returning from homeschool, start times, delay notices, summer programs, class sizes, child care in town | `underhill-and-memorial.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P2.3, P6.1, P7.1, P7.3, P10.3, P12.1, P12.2, P12.3, P14.2, P15.3 |
| 2 | Cawley Middle School and home education: the move to 6th grade, advanced math, organization help, honors tracks, bullying and phones, counselors and social workers, 504 timing, clubs, diversity and welcome, STEM enrichment, EFAs and homeschool access and paperwork | `cawley-and-home-education.md` | `raw/middle/` | P4.1, P4.2, P6.2, P10.1, P10.2, P11.1, P11.2, P17.1, P17.2, P17.3, P19.2, P19.3 |
| 3 | High school choice and Pinkerton for Hooksett: welcome at Pinkerton, CTE and late buses, Pinkerton against Manchester for trades, dual enrollment, IEPs at Pinkerton, the choice of schools, bell schedule and bus times, the freshman transition, AP results, sports and clubs, VLACS, outcomes, first-generation counseling, business and culinary, missing the bus, private school tuition | `high-school-choice-and-pinkerton.md` | `raw/high/` | P4.3, P5.1, P5.2, P5.3, P6.3, P7.2, P8.1, P8.2, P8.3, P11.3, P13.1, P13.2, P13.3, P16.1, P16.2, P16.3, P19.1 |
| 4 | Money and governance: health insurance and the tax cap, the budget and enrollment, Pinkerton tuition, cuts under the cap, SAU 15's split, scores against the state, staff retention, following the board, schools and staying, Pinkerton's buildings, spending over time, state aid, a Hooksett high school, the tax split, finding results, the budget vote | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P9.1, P9.2, P9.3, P14.1, P14.3, P15.1, P15.2, P18.1, P18.2, P18.3, P20.1, P20.2, P20.3 |
