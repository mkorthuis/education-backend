# Epping Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Epping and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Epping/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Epping

- **Epping** is a town in Rockingham County along Routes 101, 125 and 27, with Brickyard Square. Site town id 165.
- **The Epping School District** (site district id 165) is **SAU 14**, a one-district SAU, voting by official ballot. Schools: Epping Elementary (26510), preschool to grade 5; Epping Middle (26505), grades 6–8; Epping High (20515), grades 9–12, sharing a building as Epping Middle High School.
- **Career and technical education:** Epping is a sending school of the **Seacoast School of Technology**, researched in `town/Exeter/cms-sst-and-getting-to-school.md`; write only Epping's side.
- **Starting pages:** the district, https://www.sau14.org; the town, https://www.townofepping.com.
- **Site figures:** resident students 963 (2014-15), 940 (2019-20), 863 (2026-27); cost per pupil FY2025 Epping $23,812 (P3.1 says over $23,000), state $22,699; 2025 tax rates per $1,000: total $15.00, local school $10.18, municipal $3.23; Question 2: Epping 60.1% yes, so the cap is adopted, narrowly (unofficial); math proficiency 2026: Epping 32% (P3.1 says 38%), state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Epping's kindergarten cutoff, registration, preschool and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Epping)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** drop-off and care to 5:30 (P1.1); a bus app (P1.2); remote days (P1.3); the preschool lottery, cost and day (P10.1, P10.2); an A/B block schedule and no quarter report cards (P5.1, P20.2); competency grading (P5.2); about 220 high school students (P5.3); changing AP classes (P7.1); separating middle schoolers from seniors (P14.1); a nurse in both buildings every day (P19.1); 24-, 27- and 30-credit diplomas (P20.1).
- **Money:** over $23,000 a student and 38% proficient (P3.1); the wastewater plant and the school tax (P3.2); a special meeting over a budget form mix-up (P3.3); a new law putting SAU costs on their own article (P9.1); leftover money (P9.2); roofs, boilers and air handlers (P9.3).
- **SST:** applying, buses on Epping's workshop days, the diploma (P2.1–P2.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Exeter/cms-sst-and-getting-to-school.md` | SST: programs, sessions and bell schedule, credits, certifications, admission, enrollment by sending school (Epping's count included). |
| `town/Exeter/`, `town/Hampton/`, `town/Windham/` | Comparisons (Exeter's schools; P15.1). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Stratham, Newmarket, Raymond and Durham (this wave), and from the first wave Atkinson, Plaistow (shared `town/timberlane/`), Hampstead, Pelham and Seabrook. Don't write facts about those towns.

## Where facts go

- `district Epping` for SAU 14, its schools, the preschool, policies, staff, budget and board.
- `town Epping` for town government and services (the tax rate, the wastewater project, recreation and its ski bus).
- No place for general NH rules.

All agents write in `town/Epping/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; Epping Middle High's programs to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Epping Elementary and young families: drop-off and care, bus times and apps, early release and snow, meals, bus changes, help with costs, the preschool and kindergarten cutoff, the parent portal, homework help, bullying contacts, English learners, translation, volunteering | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P10.1, P10.2, P10.3, P13.1, P13.2, P13.3, P16.1, P16.2, P16.3 |
| 2 | Epping Middle High: SST access and the diploma, the A/B schedule and reporting, competency grading, clubs and electives in a small school, AP, Early College and dual enrollment, math curriculum and scores, the 6th-grade move, lunch, the 27- and 30-credit diplomas, semester grades, guidance and FAFSA | `middle-high-school.md` | `raw/high/` | P2.1, P2.2, P2.3, P5.1, P5.2, P5.3, P7.1, P7.2, P7.3, P17.1, P17.2, P17.3, P20.1, P20.2, P20.3 |
| 3 | Support, safety and choices: special education staffing, evaluation timing, pull-outs, homeschoolers and EFAs in sports and band, the ski bus, re-entry placement, team cuts, athletic trainers and concussions, late buses, separating ages, phones, counselors, security, emergency notices, military families, nurses, allergies, medication forms | `support-safety-and-choices.md` | `raw/support/` | P6.1, P6.2, P6.3, P8.1, P8.2, P8.3, P12.1, P12.2, P12.3, P14.1, P14.2, P14.3, P18.1, P18.2, P18.3, P19.1, P19.2, P19.3 |
| 4 | Money and governance: spending and scores, the school tax with the wastewater project, the special meeting, the SAU warrant article law, surpluses, building work, work-study and the calendar for employers, job readiness, comparisons and home values, the budget breakdown, enrollment | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P9.1, P9.2, P9.3, P11.1, P11.2, P11.3, P15.1, P15.2, P15.3 |
