# Brentwood Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Brentwood and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Brentwood/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Brentwood

- **Brentwood** is a town in Rockingham County west of Exeter. Site town id 63.
- **The Brentwood School District** (site district id 63) is in **SAU 16** and runs Swasey Central School (20555); check its grades and preschool. **The Exeter Region Cooperative** (site district id 172; Brentwood, East Kingston, Exeter, Kensington, Newfields, Stratham) runs Cooperative Middle School (20590, Stratham) and Exeter High School (20600). Check each district's budget form.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 858 (2014-15), 759 (2019-20), 607 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Swasey Central 282, Cooperative Middle 945, Exeter High 1,349; cost per pupil FY2025 Brentwood $23,899; Exeter Region Cooperative $24,141, state $22,699; 2025 tax rates per $1,000 (Brentwood): total $17.13, local school $11.41, municipal $4.11; Question 2: Brentwood 59.5% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Brentwood's and the Exeter Region Cooperative's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Brentwood|Exeter Region Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Swasey:** full-day pre-K (P1.1); after-school care (P1.2); bus times (P1.3); scores against Stratham and Exeter (P3.1); gifted options (P3.2); reading specialists and paras (P5.3); the kindergarten cutoff, class sizes and aides (P11.1, P11.3); before-school drop-off (P14.3).
- **CMS and Exeter High:** the move to CMS (P6.1); class sizes at Exeter High (P3.3); vaping and phones (P12.2); AP and dual enrollment (P13.1); counselors (P13.2); bus times and late buses (P14.1, P14.2); world languages (P17.2).
- **Money:** taxes up every March (P2.3); Swasey against the cooperative share (P4.1); SAU 16 costs (P4.2); buildings (P9.2); state aid (P9.3); the default budget (P19.3); new housing and enrollment (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Exeter/` (cms-sst-and-getting-to-school.md, exeter-high-school.md, money-governance-and-community.md) | The Exeter Region Cooperative: CMS, Exeter High, SST, SAU 16, the cooperative's budget and cost formula. |
| `town/Stratham/` | Another cooperative member town's side: CMS and Exeter High from Stratham, its money file. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Greenland, Rye, Brentwood, Fremont and Chester (this wave); Ossipee, Candia, Gilmanton, New Boston and North Hampton (running or starting). Don't write facts about those towns.

## Where facts go

- `district Brentwood` for Swasey and the district's budget and board.
- `district Exeter Region Cooperative` only for CMS, Exeter High or cooperative facts the Exeter and Stratham files lack.
- `sau 16` for SAU-wide facts those files lack.
- `town Brentwood` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Brentwood/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Swasey Central and young families: pre-K, after-school care, bus times, scores, gifted options, special education and reading staff, lunch, school quality, child care waitlists, kindergarten cutoff, twins' classrooms, kindergarten size and aides, early drop-off, reading help, meals, who to call | `swasey-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.2, P5.1, P5.3, P6.3, P8.1, P8.3, P10.3, P11.1, P11.2, P11.3, P14.3, P15.1, P15.2, P15.3 |
| 2 | CMS, support and choices: IEPs into CMS, the move to CMS, buses for two schools, homeschool and EFA access, entering Exeter High from homeschool, split households and notifications, vaping and phones, bus times and late buses, curriculum transparency, ESL and translation, world languages, three schools' schedules, team cuts | `cms-support-and-choices.md` | `raw/middle/` | P5.2, P6.1, P6.2, P7.1, P7.2, P7.3, P10.1, P10.2, P12.2, P14.1, P14.2, P16.2, P17.1, P17.2, P17.3, P18.1, P18.2 |
| 3 | Exeter High and SST from Brentwood: hands-on and CTE, practical skills, class sizes, alternative programs, tutoring, AP and dual enrollment, counseling, college placement and SAT, private school as an alternative, fields and gyms | `exeter-high-from-brentwood.md` | `raw/high/` | P2.1, P2.2, P3.3, P12.1, P12.3, P13.1, P13.2, P13.3, P16.1, P18.3 |
| 4 | Money and governance: taxes against enrollment, Swasey against the cooperative share, SAU 16 costs, results for the money, taxes on a new home, board agendas, buildings, state aid, teacher turnover, budget stability, a voice in SAU 16, the default budget, comparisons with neighbors, new housing, where to see Brentwood's share | `money-and-governance.md` | `raw/money/` | P2.3, P4.1, P4.2, P4.3, P8.2, P9.1, P9.2, P9.3, P16.3, P19.1, P19.2, P19.3, P20.1, P20.2, P20.3 |
