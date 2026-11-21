# Litchfield Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Litchfield and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Litchfield/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Litchfield

- **Litchfield** is a town in Hillsborough County on the Merrimack River between Hudson and Merrimack, along Route 3A. Site town id 315.
- **The Litchfield School District** (site district id 315) is **SAU 27**, voting by official ballot. Its schools:
-   - Griffin Memorial (21095), preschool to grade 4;
-   - Litchfield Middle (26640), grades 5–8;
-   - Campbell High (27715), grades 9–12.
- **Career and technical education:** Campbell students attend Hudson's Palmer Center at Alvirne (Hudson counts 54 Litchfield students in 2025-26). It's researched in `town/Hudson/alvirne-and-palmer-cte.md`; write only Litchfield's side.
- **Starting pages:** the district, https://www.litchfieldsd.org; the town, https://www.litchfieldnh.gov.
- **Site figures:**
-   - Resident students: 1,405 (2014-15), 1,274 (2019-20), 1,069 (2026-27).
-   - Cost per pupil, FY2025: Litchfield $21,147, state $22,699.
-   - 2025 tax rates per $1,000: total $14.20, local school $9.73, municipal $2.62, equalization ratio 99%.
-   - Question 2: Litchfield 59.7%, so no cap (unofficial).
-   - Math proficiency, 2026: Litchfield 50%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Litchfield's kindergarten, registration, preschool and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Litchfield)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:**
-   - free full-day kindergarten (P1.1);
-   - a 2:50 dismissal and care (P1.2);
-   - a 7:00 middle school start (P5.2, P13.2);
-   - bus drop-off at a babysitter's (P5.1);
-   - about 340 students at Campbell (P10.1);
-   - Sophomore and Senior Projects (P6.1);
-   - SNHU courses at Campbell (P6.2);
-   - VLACS for missing APs (P3.3);
-   - about 60% math proficiency at Griffin (P15.1);
-   - Campbell's low online rating (P12.3);
-   - world language start (P18.1);
-   - air conditioning (P20.3).
- **Money:**
-   - warrant articles and default budgets (P2.3, P4.2);
-   - building repairs and fields (P4.3, P10.2);
-   - special education costs (P7.2);
-   - teacher retention against Hudson and Bedford (P7.3);
-   - 5:30 board meetings and online video (P16.2, P16.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Hudson/alvirne-and-palmer-cte.md` | The Palmer Center: programs, sending districts (Litchfield's count), charges to sending districts. |
| `town/Hudson/`, `town/Merrimack/`, `town/Bedford/`, `town/Nashua/` | Comparisons (P3.1, P7.3), Bishop Guertin and private schools near Nashua (P19.1). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Amherst, Hollis, Hooksett and Bow (this wave), and Stratham, Epping, Newmarket, Raymond and Durham (running). Don't write facts about those towns.

## Where facts go

- `district Litchfield` for SAU 27, its schools, the preschool, policies, staff, budget and board.
- `town Litchfield` for town government and services.
- No place for general NH rules.

All agents write in `town/Litchfield/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; LMS and Campbell to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Griffin Memorial and young families: kindergarten and fees, care after 2:50, the cutoff and preschool, babysitter drop-offs, meals, special education and speech, IEPs from Nashua, paras, class sizes, phonics, screens, alerts for grandparents, mid-year registration, help for advanced and struggling students, enrichment, scores against the state | `griffin-memorial-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.3, P8.1, P8.2, P8.3, P9.3, P11.1, P11.2, P11.3, P12.1, P15.1, P15.2, P15.3 |
| 2 | Litchfield Middle and Campbell High: welding and electrical at Palmer, shop classes, math and science tracks, accelerated math, VLACS, the projects, SNHU courses, a small school, sports, late buses, phones, 5th grade's move, bullying and counselors, college help, open blocks, rank, world languages | `middle-and-high-school.md` | `raw/high/` | P2.1, P2.2, P3.1, P3.2, P3.3, P6.1, P6.2, P6.3, P10.1, P10.3, P13.3, P14.1, P14.2, P17.1, P17.2, P17.3, P18.1 |
| 3 | Support, daily life and choices: the 7:00 start and bus times, EFAs and homeschool access, part-time classes, FirstView, Campbell's rating and community support, lunches, translation, diversity and holidays, private schools and returning to Campbell, security, Route 3A traffic, air conditioning | `support-daily-life-and-choices.md` | `raw/support/` | P5.2, P9.1, P9.2, P12.2, P12.3, P13.1, P13.2, P14.3, P18.2, P18.3, P19.1, P19.2, P19.3, P20.2, P20.3 |
| 4 | Money and governance: warrant articles and taxes, the budget's tax effect, the default budget, building work, the budget breakdown, special education costs, teacher retention, fields and the capital plan, the school board, meeting times and video, future tax rates | `money-and-governance.md` | `raw/money/` | P2.3, P4.1, P4.2, P4.3, P7.1, P7.2, P7.3, P10.2, P16.1, P16.2, P16.3, P20.1 |
