# Haverhill Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Haverhill and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Haverhill/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Haverhill

- **Haverhill** is a town in Grafton County on the Connecticut River across from Wells River, Vermont; its villages include Woodsville, North Haverhill, Haverhill Corner, Pike and East Haverhill. Site town id 238.
- **The Haverhill Cooperative School District** (site district id 238) is in **SAU 23** with the Bath, Benton, Piermont and Warren districts, and runs Woodsville Elementary (20905; preschool to grade 3), Haverhill Cooperative Middle (26875; grades 4–8) and Woodsville High (20910; grades 9–12). Check its budget form (the library has no entry) and how SAU 23's costs are shared.
- **Tuition students** (`places.yaml`): Bath (grades 7–12, with Lisbon as the alternative), Benton (all grades, with an 11.72% discount), Piermont and Warren (Woodsville High, $20,453 for 2026-27) send students to Haverhill.
- **Career programs:** River Bend Career & Technical Center in Bradford, Vermont. **Littleton's research is running now** and may compare itself with Woodsville; don't write Littleton facts.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 612 (2014-15), 560 (2019-20), 496 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Woodsville Elementary 176, Haverhill Middle 229, Woodsville High 221; cost per pupil FY2025 Haverhill Cooperative $23,509, state $22,699; 2025 tax rates per $1,000 (Haverhill): total $22.74, local school $13.89, municipal $6.67; Question 2: Haverhill 66.7% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Haverhill's preschool and kindergarten facts. Read them: `grep -n -B2 -A10 -E "place: district (Haverhill Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Woodsville Elementary:** door times and care (P1.1); pre-K hours and cost (P1.2); early release days (P1.3); Route 10 buses and mud season (P2.1); remote days and mountain roads (P3.2); free lunch for all (P6.3); class sizes and bus rides (P14.2, P14.3); hotspots (P20.1).
- **Middle school and support:** fair and haying absences (P2.3); math around 17–21% (P3.1); gifted groups (P3.3); the move to grade 4 (P6.1); special education staffing (P8.1); French Pond School and out-of-district placements (P8.2); the IEP into Woodsville High (P8.3); homeschool access, River Bend and portfolios (P10.1, P10.2, P10.3); open enrollment, VLACS and tuitioning elsewhere (P11.2, P11.3); behavior and phones (P15.3).
- **Woodsville High and River Bend:** shop classes (P2.2); River Bend credits (P5.1); free Running Start (P5.2); work-study (P9.1); Blue Mountain and Oxbow comparisons (P11.1); about 200 students and co-ops (P13.1); a late bus (P13.2); AP and honors in person (P16.1); four-year college rates (P16.2); trades pathways and credit recovery (P18.1, P18.2).
- **Money:** the local budget cap and the 6% SAU cap (P4.1, P19.1); taxes with fewer students (P4.2); the PK–3 and 4–8 split (P6.2); families leaving (P7.1); building bonds (P7.2); ratings (P14.1); a two-year cap from 2027-28 (P15.1); turnover to Lebanon, Littleton or Vermont (P15.2); Haverhill subsidizing smaller towns (P17.1); leadership turnover (P19.2); adequacy aid (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Plymouth/`, `town/Lebanon/` | Other Grafton County districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newport, New London, Enfield, Haverhill and Littleton (this wave); Peterborough, New Ipswich, Hinsdale, Winchester, Charlestown, Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (running). Don't write facts about those towns.

## Where facts go

- `district Haverhill Cooperative` for the three schools, the tuition agreements from Haverhill's side, and the district's budget and board.
- `sau 23` for SAU-wide facts (the SAU budget and its split, administration).
- `town Haverhill` for town government, recreation, the libraries and taxes.
- No place for general NH rules.

All agents write in `town/Haverhill/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Woodsville Elementary and young families: door times and care, pre-K, early release days, Route 10 buses and mud season, snow and remote days, free lunch, the parent portal, reading help, guardianship papers, kindergarten and first grade class sizes, bus rides by area, internet and hotspots, conferences by phone, summer programs | `woodsville-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P3.2, P6.3, P12.1, P12.2, P12.3, P14.2, P14.3, P20.1, P20.2, P20.3 |
| 2 | Haverhill Cooperative Middle School, support and choices: farm and fair absences, math scores, gifted groups, the move to grade 4, special education staffing, out-of-district placements, IEPs into high school, homeschool access, River Bend for homeschoolers, portfolios, open enrollment and VLACS, tuitioning elsewhere, behavior and phones | `middle-school-support-and-choices.md` | `raw/middle/` | P2.3, P3.1, P3.3, P6.1, P8.1, P8.2, P8.3, P10.1, P10.2, P10.3, P11.2, P11.3, P15.3 |
| 3 | Woodsville High and River Bend: shop classes, River Bend credits, Running Start, apprenticeships and aid, work-study, shop math, sponsoring internships, comparisons with Blue Mountain and Oxbow, co-op teams, the late bus, eligibility, AP and honors, college going, counseling, trades pathways, credit recovery, the trades and military | `woodsville-high-and-river-bend.md` | `raw/high/` | P2.2, P5.1, P5.2, P5.3, P9.1, P9.2, P9.3, P11.1, P13.1, P13.2, P13.3, P16.1, P16.2, P16.3, P18.1, P18.2, P18.3 |
| 4 | Money and governance: the local and SAU caps, taxes and enrollment, the spending breakdown, the grade split, families moving in or out, buildings and bonds, community use, ratings, cuts under the cap, turnover, Haverhill's share in SAU 23, mid-year cost spikes, budget hearings, leadership, adequacy aid | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P6.2, P7.1, P7.2, P7.3, P14.1, P15.1, P15.2, P17.1, P17.2, P17.3, P19.1, P19.2, P19.3 |
