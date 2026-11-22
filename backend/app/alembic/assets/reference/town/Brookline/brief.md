# Brookline Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Brookline and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Brookline/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Brookline

- **Brookline** is a town in Hillsborough County west of Hollis, on Route 130. Site town id 71.
- **Two districts serve Brookline, both in SAU 41:**
-   - **The Brookline School District** (site district id 71): Richard Maghakian Memorial (21800), preschool to grade 3, and Captain Samuel Douglass Academy (27765), grades 4–6.
-   - **The Hollis-Brookline Cooperative** (site district id 260): Hollis-Brookline Middle (7–8) and High (9–12) in Hollis, researched in `../Hollis/`.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,108 (2014-15), 1,128 (2019-20), 1,042 (2025-26); cost per pupil FY2025 Brookline $19,967, Hollis-Brookline $23,443, state $22,699; 2025 tax rates per $1,000 (Brookline): total $24.64, local school $17.81, municipal $4.73; Question 2: Brookline 63.9% yes; the cooperative adopted it (61.1%, unofficial); math proficiency 2026: Brookline 64%, Hollis-Brookline 65%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Brookline's and the cooperative's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Brookline|Hollis-Brookline Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Brookline's schools:** full-day kindergarten (P1.1); care around an 8:25 start (P1.2); the RMMS preschool (P1.3); CSDA's scores (P3.3); speech and OT (P5.1); bus rides and the Route 130 line (P7.1, P7.3); crowding (P9.2); 5th-grade math (P17.1); dyslexia screening and class sizes (P20.1, P20.2).
- **The cooperative:** AP and honors STEM (P3.1); Latin Honors (P3.2); CTE in Nashua (P4.1); about 750 students (P10.1); 50+ clubs and a late bus (P15.3); honors math at HBMS (P17.2).
- **Money:** extra adequacy aid (P2.1); two budgets (P2.2); a $33.11 million co-op placeholder (P8.1); Brookline's share (P8.2); health insurance (P8.3); special education costs (P5.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Hollis/` (all four files) | The cooperative's middle and high schools, SAU 41, the cost split between Hollis and Brookline, the FY2028 drafts, policies on home education and access. |
| `town/Nashua/`, `town/Hudson/` | Nashua's career center, the Academy for Science and Design and Hudson's Palmer Center (P4.1, P13.1). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Danville, Sandown, Lee and Henniker (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Brookline` for RMMS, CSDA, the Brookline budget and board.
- `district Hollis-Brookline Cooperative` only for cooperative facts Hollis's files lack.
- `sau 41` for SAU-wide facts.
- `town Brookline` for town government and taxes.
- No place for general NH rules.

All agents write in `town/Brookline/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money for both districts belongs to agent 4; HBHS and pathways to agent 3; HBMS, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | RMMS, CSDA and families: full-day kindergarten, care, the preschool, CSDA's scores, speech and OT, bus rides, delays, the drop-off line, crowding, comparisons with Hollis's schools, Chromebooks and apps, meals, 5th-grade math, three schedules, dyslexia screening, class sizes, anxiety support | `rmms-csda-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.3, P5.1, P7.1, P7.2, P7.3, P9.2, P9.3, P14.1, P14.2, P14.3, P17.1, P18.1, P20.1, P20.2, P20.3 |
| 2 | HBMS, support and choices: IEPs at HBMS, homeschool paperwork and access, the move from CSDA, homework, bullying, charter schools, EFAs, making a team, para and substitute pay and licensing, staffing, honors math, math teams | `hbms-support-and-choices.md` | `raw/middle/` | P5.3, P6.1, P6.2, P6.3, P11.1, P11.2, P11.3, P13.1, P13.2, P15.1, P16.1, P16.2, P16.3, P17.2, P17.3 |
| 3 | Hollis-Brookline High and pathways: AP and honors STEM, Latin Honors, CTE in Nashua, trades and graduation, counselors, dual enrollment, college costs, work readiness, internships, science and robotics, fields at Cavanaugh, late buses | `hbhs-and-pathways.md` | `raw/high/` | P3.1, P3.2, P4.1, P4.2, P4.3, P10.1, P10.2, P10.3, P12.1, P12.2, P13.3, P15.2, P15.3 |
| 4 | Money and governance: adequacy aid, two budgets, tax relief, special education costs, the co-op placeholder budget, Brookline's share, health insurance, home values, commercial taxes, the same calendars, where to speak up, the deliberative session, teacher contracts, building maintenance | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P5.2, P8.1, P8.2, P8.3, P9.1, P12.3, P18.2, P18.3, P19.1, P19.2, P19.3 |
