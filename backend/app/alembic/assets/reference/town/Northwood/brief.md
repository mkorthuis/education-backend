# Northwood Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Northwood and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Northwood/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Northwood

- **Northwood** is a town in Rockingham County on Route 4 between Concord and Lee. Site town id 411.
- **The Northwood School District** (site district id 411) is **SAU 44** and runs Northwood School (22085; listed in the site's data as Northwood Elementary School), preschool to grade 8. It votes by official ballot (SB2). Check when SAU 44's other members (Nottingham, Strafford) left.
- **High school:** Coe-Brown Northwood Academy (22025, site district id 998) under a contract signed in November 2024 and approved by the State Board December 12, 2024 (`places.yaml`: through June 30, 2035, renewable to 2040; Northwood may send up to 10% of its high schoolers elsewhere). Coe-Brown is already researched in `town/Barrington/high-school-choice.md` and `town/Deerfield/high-school-choice.md` (facts placed `district Coe-Brown Northwood Academy`: FFA and agriculture, counseling, advisory, home-education entry, welding). Agent 3 here owns new Coe-Brown facts; **Nottingham's research is running now** and will cite them.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 660 (2014-15), 614 (2019-20), 544 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Northwood School 413, Coe-Brown 654; cost per pupil FY2025 Northwood $22,632, state $22,699; 2025 tax rates per $1,000 (Northwood): total $11.91, local school $8.46, municipal $2.01; Question 2: Northwood 56.2% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Northwood's kindergarten cutoff, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Northwood)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Northwood School:** a Champions after-school waitlist and cost (P1.1); a bus app (P1.2); care on delay mornings (P1.3); a lottery-based pre-K (P5.1); the kindergarten cutoff (P5.3); the Northwood School app and paper notices (P7.2); busing to a sitter (P10.1); summer programs (P10.2); Step By Step Preschool (P16.3); math intervention (P18.1).
- **Upper grades and support:** advanced math in grades 7–8 (P6.2); Chromebooks (P6.3); speech and OT (P11.1); homeschool access and notification (P12.1, P12.2); a resource officer (P16.2); middle school sports, cuts, band and theater (P19.1, P19.2).
- **Coe-Brown:** choice beyond Coe-Brown (P2.1); the 8th-to-9th transition (P2.2); late buses and a 6:30 a.m. pickup (P2.3, P14.1); shop, welding and auto (P4.1); Dover or Concord career centers (P4.2); driver's ed (P4.3); IEPs (P11.2); placement tests for homeschoolers (P12.3); AP and SNHU credits (P13.1); FFA (P15.1); fees and waivers (P15.3).
- **Money:** taxes with about 400 students (P3.1); tuition against the school (P3.2); taxes against Pittsfield and Epsom (P9.1); a building bond (P9.2); enrollment trend (P17.1); SAU 44 now covering only Northwood (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Barrington/`, `town/Deerfield/` | Coe-Brown Northwood Academy, and those towns' contracts with it. |
| `town/Dover/`, `town/Concord/` | The Dover and Concord career centers. |
| `town/Epsom/` | A neighbor, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Wakefield, Milton, Moultonborough, Nottingham and Northwood (this wave); Greenland, Rye, Brentwood, Fremont, Chester, Ossipee and New Boston (running). Don't write facts about those towns.

## Where facts go

- `district Northwood` for Northwood School and the district's budget, board and its side of the Coe-Brown contract.
- `district Coe-Brown Northwood Academy` for Coe-Brown facts the earlier files lack.
- `sau 44` for SAU-wide facts.
- `town Northwood` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/Northwood/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Northwood School's early grades and families: Champions after-school care, bus times and the bus app, care on delay days, pre-K, reading help, the kindergarten cutoff and registration, the school app and paper notices, meals, enrolling new students, class sizes, busing to a sitter, summer programs, lunch accounts, local preschools, math help and curriculum, grade updates | `northwood-school-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P7.2, P7.3, P8.1, P8.2, P10.1, P10.2, P10.3, P16.3, P18.1, P18.2, P18.3 |
| 2 | Northwood School's upper grades, support and choices: advanced math, Chromebooks, the counselor, bullying, special education and speech, IEP disputes, homeschool access and notification, private and charter choices, safety and a resource officer, middle school sports, band and theater, volunteering | `northwood-school-upper-grades-support-and-choices.md` | `raw/middle/` | P6.2, P6.3, P7.1, P8.3, P11.1, P11.3, P12.1, P12.2, P16.1, P16.2, P19.1, P19.2, P19.3 |
| 3 | Coe-Brown from Northwood: choice beyond Coe-Brown, the transition, late buses and pickup times, shop and trades, career centers, driver's ed, IEPs, homeschoolers' placement, AP and SNHU credits, college counseling, tuition discounts, phones and absences, FFA, work credit, fees | `coe-brown-from-northwood.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.1, P4.2, P4.3, P11.2, P12.3, P13.1, P13.2, P13.3, P14.1, P14.2, P14.3, P15.1, P15.2, P15.3 |
| 4 | Money and governance: the school tax and enrollment, Coe-Brown tuition against the school, the deliberative session and budget, test scores against neighbors, taxes against neighbors, the building, how graduates do, enrollment, cost per pupil, adequacy aid, board meetings and public comment, SAU 44's history, salaries and administrative costs | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.1, P9.1, P9.2, P9.3, P17.1, P17.2, P17.3, P20.1, P20.2, P20.3 |
