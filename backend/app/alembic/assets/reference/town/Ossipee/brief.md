# Ossipee Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Ossipee and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Ossipee/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Ossipee

- **Ossipee** is a town in Carroll County south of Conway. Site town id 419.
- **The Governor Wentworth Regional School District** (site district id 208) is **SAU 49**. Ossipee Central School (22405) is in Center Ossipee; check its grades. Kingswood Regional Middle (22440) and High (22425) are in Wolfeboro. It votes by official ballot (SB2).
- **Reuse first.** Much of this town's shared district or high school is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Wolfeboro's research is running now** (`town/Wolfeboro/`: elementary-and-families.md, middle-school-support-and-choices.md, kingswood-high-and-lrtc.md, money-and-governance.md). Its files will be finished before most of yours; read them as they appear and cite them.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 560 (2014-15), 568 (2019-20), 548 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Ossipee Central 275, Kingswood Middle 345, Kingswood High 729; cost per pupil FY2025 Governor Wentworth $26,293, state $22,699; 2025 tax rates per $1,000 (Ossipee): total $12.77, local school $7.22, municipal $3.69; Question 2: Ossipee 72.3% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Governor Wentworth's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Governor Wentworth Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Ossipee Central:** preschool spots (P1.1); School's Out after-school care (P1.2, P13.1); the kindergarten cutoff and buses (P1.3); scores (P4.1); speech and special education staff (P5.1); lunch (P7.2); art and music (P13.2); snow days and blizzard bags (P16.2).
- **Middle and high school:** West Ossipee bus times and ride length (P2.2, P19.3); Kingswood Academy (P10.3); LRTC and sports (P2.3); Health Science shadowing at Huggins (P9.3); JROTC (P20.1); the late bus (P12.3).
- **Money:** tax growth (P3.1); Ossipee's share against Kingswood (P3.2); a superintendent search (P6.1); substitute nurse pay of $50 an hour (P10.2); Wolfeboro's facilities (P14.2).
- **Home education:** sports for homeschoolers and EFAs (P11.1, P11.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Wolfeboro/` (running now) | Governor Wentworth: Kingswood, LRTC, policies, the budget, the cost formula and votes. |
| `town/Freedom/`, `town/Madison/`, `town/Tamworth/` | SAU 13's Kingswood agreements; Effingham and Tamworth for P8.2. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Ossipee, Candia, Gilmanton, New Boston and North Hampton (this wave); Allenstown, Epsom, Deerfield, Auburn, Wolfeboro, Newton, Rindge, Boscawen, Barnstead and Northfield (running). Don't write facts about those towns.

## Where facts go

- `district Governor Wentworth Regional` for Ossipee Central and any new district-wide fact.
- `sau 49` for SAU-wide facts.
- `town Ossipee` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Ossipee/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Ossipee Central and young families: preschool, after-school care and School's Out, the kindergarten cutoff and buses, scores, reading challenge, speech and special education staff, IEP reading help, summer programs, fee help, lunch, child care and playgroups, storm alerts, translation, art and music, the PTO, snow days | `ossipee-central-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P5.1, P5.2, P5.3, P7.1, P7.2, P8.1, P8.3, P12.1, P12.2, P13.1, P13.2, P13.3, P16.2 |
| 2 | Support, Kingswood Middle and choices: West Ossipee buses, the move to Kingswood, bullying and phones, storm calls across towns, counseling, moving within the district, homeschool and EFA access, re-entering at 9th grade, the late bus, attendance, mental health and prevention, food and housing help, backpack programs, 7th-grade orientation, 6th-grade tech skills, ride length, 504 plans | `support-and-choices.md` | `raw/support/` | P2.2, P4.3, P6.2, P6.3, P7.3, P8.2, P11.1, P11.2, P11.3, P12.3, P16.3, P17.1, P17.2, P17.3, P19.1, P19.2, P19.3, P20.2 |
| 3 | Kingswood High and LRTC from Ossipee: Construction Trades, LRTC and sports, AP and dual enrollment, college counseling, Health Science at Huggins, personal finance and trades, Kingswood Academy, adult nursing pathways, help for recent graduates, scholarships, Culinary Arts hours, JROTC and the ASVAB, early graduation | `kingswood-from-ossipee.md` | `raw/high/` | P2.1, P2.3, P9.1, P9.2, P9.3, P10.1, P10.3, P15.1, P15.2, P15.3, P16.1, P20.1, P20.3 |
| 4 | Money and governance: tax growth, Ossipee's share, the budget hearing and vote, the superintendent search, substitute nurse pay, the school part of the tax bill, facilities in Wolfeboro against Ossipee, spending records, renters, board meetings, long-term value | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.1, P10.2, P14.1, P14.2, P14.3, P18.1, P18.2, P18.3 |
