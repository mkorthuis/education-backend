# Barnstead Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Barnstead and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Barnstead/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Barnstead

- **Barnstead** is a town in Belknap County, with the Locke Lake community. Site town id 31.
- **The Barnstead School District** (site district id 31) is **SAU 86**. It runs Barnstead Elementary (22485); check its grades. Its high school students attend Prospect Mountain High School (28215), run by the Prospect Mountain JMA (site district id 970), a joint board of the Alton and Barnstead school boards (`places.yaml`). Check whether Barnstead and Alton share a superintendent (P10.2).
- **Saved in a browser pass (the pmsau.nh.gov sites show automated requests a bot check):** in `town/Barnstead/raw/browser/`, the BES 2026-27 Student/Parent Handbook (`bes-handbook-2026-27.txt`, from its Google Doc) and the 2026-27 BES bus routes (`bes-bus-routes-2026-27-redacted.txt`, house numbers removed). In `town/Alton/raw/high/browser/`, Prospect Mountain's 2026-27 handbook (`pmhs-handbook-2026-27.txt`), Program of Studies (`pmhs-program-of-studies-2026-27.txt`), bell schedule (`pmhs-bell-schedule.txt`) and the Alton and Barnstead high school bus routes (redacted). BES's site is https://www.bes.pmsau.nh.gov (its preschool page says "Coming Soon"); Prospect Mountain's is https://www.pmhs.pmsau.nh.gov. Cite these copies; don't try to get around the bot check.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Career and technical education:** check which regional center Prospect Mountain students use (Alton's research).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 706 (2014-15), 690 (2019-20), 624 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Barnstead Elementary 449, Prospect Mountain High 403; cost per pupil FY2025 Barnstead $19,493, state $22,699; 2025 tax rates per $1,000 (Barnstead): total $17.15, local school $11.08, municipal $3.98; Question 2: Barnstead 68.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Barnstead's and Prospect Mountain's kindergarten, registration, preschool, high school and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Barnstead|Prospect Mountain JMA)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **BES:** bus times at Locke Lake (P1.1); after-school care (P1.2); pre-K (P1.3); math scores (P4.1); Chromebooks (P4.3); reading help (P5.3); staff turnover (P6.2, P10.1); bullying (P9.1); full-day kindergarten (P13.1); dirt camp roads in winter (P19.2).
- **Prospect Mountain:** the Lakes Region center for welding (P3.1); open enrollment and crowding (P2.3, P14.3); AP and college credit (P8.1); a late bus (P14.1); ride times (P14.2); music, drama and robotics cuts (P18.2).
- **Money:** the BES expansion and renovation (P2.1, P19.1); the Alton–Barnstead split (P2.2, P20.3); sharing a superintendent (P10.2); one K–8 school (P16.1); spending below the state average (P20.1); 55% state building aid (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Alton/` (alton-central-and-families.md, alton-central-upper-grades-and-support.md, prospect-mountain-and-cte.md, money-and-governance.md) | Prospect Mountain High School, the JMA's budget and cost split, career programs, and Alton's K–8 for comparison. |
| `town/Laconia/`, `town/Belmont/`, `town/Gilford/` | The Huot Center and nearby districts, for comparisons (P8.3). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newton, Rindge, Boscawen, Barnstead and Northfield (this wave); Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (running). Don't write facts about those towns.

## Where facts go

- `district Barnstead` for BES, the district's budget, board and policies.
- `district Prospect Mountain JMA` only for Prospect Mountain facts Alton's files lack.
- `sau 86` for SAU-wide facts.
- `town Barnstead` for town government, recreation, roads and taxes.
- No place for general NH rules.

All agents write in `town/Barnstead/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school and career programs to agent 3; support and choices to agent 2; the elementary school and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Barnstead Elementary's early grades and families: buses at Locke Lake, after-school care, pre-K, Chromebooks, delays, meals, reading help, registering mid-year, phonics, notices, math homework help, full-day kindergarten and the cutoff, families staying, the drop-off line, foster children, summer camps, dirt roads in winter | `bes-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.3, P5.1, P5.2, P5.3, P9.2, P10.3, P12.1, P12.2, P13.1, P13.2, P13.3, P15.1, P15.3, P16.3, P19.2 |
| 2 | BES's upper grades, support and choices: readiness for high school, math scores, clubs and sports, special education and behavior support, staff turnover, IEP disputes, homeschool and EFA access, bullying, rules for 7th and 8th graders, counseling, trauma training, advanced math, gifted programs, the renovation for middle school classrooms | `bes-upper-grades-support-and-choices.md` | `raw/middle/` | P3.2, P4.1, P4.2, P6.1, P6.2, P6.3, P7.1, P7.3, P9.1, P9.3, P12.3, P15.2, P17.1, P17.2, P19.1 |
| 3 | Prospect Mountain from Barnstead: welding and carpentry at the regional center, sports Prospect Mountain lacks, enrolling from homeschool, AP and college credit, college and aid counseling, readiness, internships, late buses and ride times, crowding from open enrollment, honors classes, adult education, music, drama and robotics, young people leaving, new freshmen | `prospect-mountain-from-barnstead.md` | `raw/high/` | P3.1, P3.3, P7.2, P8.1, P8.2, P8.3, P11.2, P14.1, P14.2, P14.3, P17.3, P18.1, P18.2, P18.3, P19.3 |
| 4 | Money and governance: the BES expansion and its tax effect, the Alton–Barnstead split for Prospect Mountain, open enrollment revenue, teacher pay, sharing a superintendent, the budget breakdown, one K–8 school, state against local funding, spending per student, 55% building aid, enrollment shifts between the towns | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P10.1, P10.2, P11.1, P11.3, P16.1, P16.2, P20.1, P20.2, P20.3 |
