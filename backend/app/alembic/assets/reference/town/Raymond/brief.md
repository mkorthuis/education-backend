# Raymond Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Raymond and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Raymond/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Raymond

- **Raymond** is a town in Rockingham County along Routes 101, 27 and 102, with Onway, Governors and Pawtuckaway-area lakes. Site town id 453.
- **The Raymond School District** (site district id 453) is **SAU 33**, a one-district SAU voting by official ballot. Schools: the Raymond School District Preschool Program (29233); Lamprey River Elementary (21385), K–3; Iber Holmes Gove Middle (26525), grades 4–8; Raymond High (21390), 9–12.
- **Career and technical education:** Raymond is an SST sending school (`town/Exeter/cms-sst-and-getting-to-school.md`); write only Raymond's side.
- **Starting pages:** the district, https://www.sau33.com; the town, https://www.raymondnh.gov.
- **Site figures:** resident students 1,408 (2014-15), 1,237 (2019-20), 1,089 (2026-27); cost per pupil FY2025 Raymond $22,888, Epping $23,812, state $22,699 (P3.3); 2025 tax rates per $1,000: total $22.96, local school $15.92, municipal $4.60, equalization ratio 62%; Question 2: Raymond 71.6% yes, so the cap is adopted (unofficial); math proficiency 2026: Raymond 43%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Raymond's kindergarten, registration, preschool and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Raymond)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** a preschool at the high school (P1.1); Lamprey River class sizes and renovation talk (P1.2, P14.3, P20.2); after-school waitlists (P1.3); earliest drop-off at IHGMS (P2.1); 4th graders moving to IHGMS (P4.2); universal free meals (P4.3); about 330 high school students (P7.1); JROTC (P18.1); remote snow days (P16.3).
- **Money:** a $32.1 million budget and a higher default (P3.1); $250,000 of surplus for a Lamprey River reserve (P3.2); spending against Epping and Candia (P3.3); teacher turnover (P13.2); grants (P20.3).
- **Choices:** open enrollment voted in March (P17.2); manifest educational hardship (P17.3); single classes for homeschoolers (P8.2); VLACS (P8.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Exeter/cms-sst-and-getting-to-school.md` | SST: programs, sessions, credits, admission, enrollment by sending school (Raymond's count included). |
| Epping's research (running now) | Epping, for comparisons; use the site's data instead. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Stratham, Epping, Newmarket, Durham (this wave), and from the first wave Atkinson, Plaistow (shared `town/timberlane/`), Hampstead, Pelham and Seabrook. Don't write facts about those towns.

## Where facts go

- `district Raymond` for SAU 33, its schools, preschool, policies, staff, budget and board.
- `town Raymond` for town government and services.
- No place for general NH rules.

All agents write in `town/Raymond/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; Raymond High's programs to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Lamprey River and Iber Holmes Gove: the preschool, class sizes, after-school care, early drop-off, 5th-grade curriculum, phones, bus changes, the move to IHGMS, meals, English learners, tutoring, fees, counselors, reading program, screens, enrichment | `elementary-and-middle-school.md` | `raw/k8/` | P1.1, P1.2, P1.3, P2.1, P2.2, P2.3, P4.1, P4.2, P4.3, P9.1, P11.1, P11.2, P11.3, P13.1, P16.1, P16.2 |
| 2 | Raymond High: SST and shop classes, a small school, registration and physicals, the 9th-grade transition, AP and Running Start, graduates' plans, guidance, work readiness, apprenticeships, JROTC and service tracks, counselor access, personal finance, finishing a diploma or HiSET, help for recent grads | `raymond-high-school.md` | `raw/high/` | P5.1, P5.2, P5.3, P7.1, P7.2, P9.2, P10.1, P10.2, P10.3, P12.1, P12.2, P18.1, P18.2, P19.1, P19.2, P19.3 |
| 3 | Support, choices and daily life: paras, special education communication, out-of-district placements, the schools' reputation, EFAs, homeschoolers in classes and sports, VLACS, translation, middle school teams, activity buses, fields and gyms, snow days, bullying, open enrollment, manifest educational hardship, military families | `support-choices-and-daily-life.md` | `raw/support/` | P6.1, P6.2, P6.3, P7.3, P8.1, P8.2, P8.3, P9.3, P15.1, P15.2, P15.3, P16.3, P17.1, P17.2, P17.3, P18.3 |
| 4 | Money and governance: the budget and default budget, the Lamprey River reserve and building plans, spending against neighbors, where the money goes, teacher turnover, the school board, buying a home, taxes against Fremont and Deerfield, a new school's tax effect, the tax breakdown, enrollment, grants | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P12.3, P13.2, P13.3, P14.1, P14.2, P14.3, P20.1, P20.2, P20.3 |
