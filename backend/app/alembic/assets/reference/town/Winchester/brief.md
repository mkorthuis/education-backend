# Winchester Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Winchester and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Winchester/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Winchester

- **Winchester** is a town in Cheshire County on the Massachusetts border, with the village of Ashuelot. Site town id 573.
- **The Winchester School District** (site district id 573) is **SAU 94** and runs Winchester School (21735), preschool to grade 8. It is listed as an official ballot (SB2) district; check its deliberative session and vote dates.
- **High school** (`places.yaml`): Keene High since 2006, ended by Keene in February 2024 (no new 9th graders from 2026; enrolled students finish, the class of 2028 by an addendum); Hinsdale High as the anchor school from the class of 2030 under a 2026–2033 agreement; Pioneer Valley Regional (Northfield, MA) under a 2026–2031 agreement; Monadnock Regional and Franklin County Technical School as listed choices; up to 20% may choose a school other than Hinsdale, with the district paying up to its Hinsdale rate. Keene is researched in `town/Keene/` and Monadnock in `town/Swanzey/`.
- **Hinsdale's research is running now** (`town/Hinsdale/`): its agent 3 owns Hinsdale High facts. Agent 3 here starts after it and cites them; write Winchester's side.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 584 (2014-15), 530 (2019-20), 455 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Winchester School 322; cost per pupil FY2025 Winchester $22,279, state $22,699; 2025 tax rates per $1,000 (Winchester): total $19.67, local school $11.11, municipal $5.54; Question 2: Winchester 60.5% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Winchester's preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Winchester)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Winchester School:** half-day, lottery-based pre-K (P1.1); after-school care until 5 (P1.2); bus stop times on Route 10 (P1.3); free meals for all (P7.2); many early release days (P15.1); recess in January (P15.3); the kindergarten cutoff (P17.3); class sizes (P19.1).
- **Support and choices:** paras (P5.2); exiting CSI status (P6.1); honors or enrichment in middle school (P6.2); middle school teams (P11.2); EFAs and part-time access (P13.1, P13.2); a yearly portfolio to SAU 94 (P13.3); interventionists after federal COVID money (P19.2); phones (P20.2).
- **High school:** paying the difference for Monadnock or Keene (P2.1, P20.3); the 20% lottery (P2.2); the Cheshire Career Center from Hinsdale (P2.3); calendars and buses for Keene and Hinsdale (P3.1, P3.2, P3.3); special education at Hinsdale (P5.3); AP and dual enrollment at Hinsdale (P6.3); the Keene bus before 2029 (P8.1); joint activities with Hinsdale (P8.2); Keene internships for seniors (P14.1); football co-ops (P18.2).
- **Money:** $500,000 in savings over four years (P4.1); special education and tuition shares (P4.2); adequacy aid (P4.3); the default budget (P9.1); gym repairs and a bond (P9.2); enrollment against homeschool and private (P9.3); substitute pay (P10.1); the Hinsdale deal locked to 2033 (P16.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Keene/` | Keene High and the Cheshire Career Center. |
| `town/Swanzey/` | Monadnock Regional High. |
| `town/Hinsdale/` (running) | Hinsdale High, Winchester's anchor high school. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Peterborough, New Ipswich, Hinsdale, Winchester and Charlestown (this wave); Strafford, Pittsfield, Hopkinton, Hillsborough, Wilton, Wakefield, Milton, Moultonborough, Nottingham and Northwood (running). Don't write facts about those towns.

## Where facts go

- `district Winchester` for Winchester School and the district's budget, board and its side of the high school agreements.
- `sau 94` for SAU-wide facts.
- `town Winchester` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Winchester/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Winchester School's early grades and families: pre-K, after-school care, bus stop times, free meals, help for English learners and translated notices, the parent portal, a missed bus, help with forms and fees, early release days, snow days, recess, enrolling mid-year, preschool screening, child care subsidies, the kindergarten cutoff, class sizes | `winchester-school-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P7.2, P11.1, P11.3, P12.1, P12.2, P15.1, P15.2, P15.3, P16.2, P17.1, P17.2, P17.3, P19.1 |
| 2 | Winchester School's upper grades, support and choices: IEP evaluations, paras, scores since CSI, enrichment, counseling and social work, volunteers and donations, medications on long bus rides, middle school teams, math tutoring, EFAs, part-time access, homeschool paperwork, interventionists, behavior and bullying, phones | `winchester-school-upper-grades-support-and-choices.md` | `raw/middle/` | P5.1, P5.2, P6.1, P6.2, P7.1, P7.3, P8.3, P11.2, P12.3, P13.1, P13.2, P13.3, P19.2, P20.1, P20.2 |
| 3 | High school choice from Winchester: Hinsdale, Keene, Monadnock and Pioneer Valley, the 20% choice and its lottery, the Cheshire Career Center, calendars and buses, late buses, special education at Hinsdale, AP and dual enrollment, the Keene bus, joining Hinsdale students, Keene internships for seniors, scholarships, career fairs, hands-on classes, football, reading help, getting into Keene | `high-school-choice.md` | `raw/high/` | P2.1, P2.2, P2.3, P3.1, P3.2, P3.3, P5.3, P6.3, P8.1, P8.2, P14.1, P14.2, P14.3, P18.1, P18.2, P18.3, P20.3 |
| 4 | Money and governance: the Hinsdale contract's savings, special education and tuition costs, adequacy aid, the default budget, the gym and bonds, enrollment, substitute pay and hiring, turnover, spending against neighbors, the high school deal's term, board meetings | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P9.1, P9.2, P9.3, P10.1, P10.2, P10.3, P16.1, P16.3, P19.3 |
