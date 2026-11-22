# Enfield Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Enfield and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Enfield/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Enfield

- **Enfield** is a town in Grafton County east of Lebanon, on Mascoma Lake (Shaker Village). Site town id 163.
- **The Mascoma Valley Regional School District** (site district id 343) is **SAU 62** and runs Enfield Village School (21325; preschool to grade 4), Canaan Elementary, Indian River School (26405; grades 5–8) and Mascoma Valley Regional High School (21305; grades 9–12). It votes by official ballot (SB2). Check how costs are split among the five towns and how board seats are apportioned.
- **Career programs:** the Hartford Area Career & Technology Center (White River Junction, VT). Check whether `town/Lebanon/` or `town/Hanover/` already covers it; write Mascoma's side (access, buses, credits).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 487 (2014-15), 421 (2019-20), 385 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Enfield Village 195, Indian River 292, Mascoma High 304; cost per pupil FY2025 Mascoma Valley $27,044, state $22,699; 2025 tax rates per $1,000 (Enfield): total $17.83, local school $9.66, municipal $5.88; Question 2: Enfield 46.2% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Mascoma's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Mascoma Valley Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Enfield Village School:** after-school program spots and pickup time (P1.1); hour-long rides from the Route 4A side (P1.2); PTA club sessions (P1.3); storm alerts (P5.1); free meals for all (P5.2); drop-off at a grandparent's (P5.3); public pre-K (P8.1); the kindergarten cutoff (P8.2); the Grafton line (P13.1); ESL (P18.1).
- **Indian River and support:** the move from Enfield Village (P3.1); about 40% math proficiency (P3.2); challenge for advanced 5th graders (P3.3); special education staffing (P6.1); EFAs and homeschool paperwork (P10.1, P10.2); MAPs pathways (P11.1); hunting-season absences (P11.3); a late bus to Enfield (P12.3); 504 plans for anxiety (P16.1); phones (P16.2).
- **Mascoma High:** HACTC busing and credits (P2.1, P2.2); AP every other year (P7.1); Dartmouth Community High School (P7.2); AP and Running Start fees (P7.3, P15.3); homeschool credits for 9th grade (P10.3); 8th graders on JV teams (P11.2); sports for PE credit (P15.1); ELOs (P15.2); credit recovery (P17.1); Butler Bus driver shortages (P17.2); a late bus (P17.3).
- **Money:** taxes with fewer students (P2.3); Enfield's share against the other towns (P4.2); the $32.97 million budget and a higher default (P4.3); program cuts (P9.2); leaving the cooperative (P9.3); five towns and seven board seats (P19.1); spending against Lebanon and Hanover (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Lebanon/`, `town/Hanover/` | Lebanon and Hanover, for comparisons and possibly the Hartford center. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newport, New London, Enfield, Haverhill and Littleton (this wave); Peterborough, New Ipswich, Hinsdale, Winchester, Charlestown, Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (running). Don't write facts about those towns.

## Where facts go

- `district Mascoma Valley Regional` for the schools, the district's side of the Hartford center, and its budget and board.
- `sau 62` for SAU-wide facts.
- `town Enfield` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/Enfield/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Enfield Village School and young families: after-school care and PTA clubs, bus rides, storm alerts, meals, drop-off at another address, public pre-K, kindergarten registration and cutoff, child care, two schools' bus times, how teachers communicate, the Grafton line, internet at home, ESL, diversity and holidays, transferring records | `enfield-village-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P8.1, P8.2, P8.3, P12.1, P12.2, P13.1, P13.3, P18.1, P18.2, P18.3 |
| 2 | Indian River, support and choices: the move from Enfield Village, math scores, challenge for advanced students, special education staffing and disputes, the move to high school support, EFAs and homeschool paperwork, MAPs pathways, attendance rules, a late bus, help for grandparents, counseling, coats and fees, 504 plans, phones, bus bullying | `indian-river-support-and-choices.md` | `raw/middle/` | P3.1, P3.2, P3.3, P6.1, P6.2, P6.3, P10.1, P10.2, P11.1, P11.3, P12.3, P14.1, P14.2, P14.3, P16.1, P16.2, P16.3 |
| 3 | Mascoma High and the Hartford center: HACTC busing and credits, AP scheduling, Dartmouth Community High School, AP and Running Start fees, homeschool credits, 8th graders on JV, PE credit for sports, ELOs, Running Start transfer, credit recovery, Butler Bus, the late bus, agriculture and outdoor courses, college readiness, dual enrollment awareness | `mascoma-high-and-hartford-center.md` | `raw/high/` | P2.1, P2.2, P7.1, P7.2, P7.3, P10.3, P11.2, P15.1, P15.2, P15.3, P17.1, P17.2, P17.3, P19.2, P20.1, P20.2 |
| 4 | Money and governance: taxes and enrollment, the tax bill split, Enfield's share, the budget and default, lakefront owners' taxes, cuts, leaving the cooperative, comparisons with Lebanon and Hanover, board seats, spending comparisons, agendas and budget numbers | `money-and-governance.md` | `raw/money/` | P2.3, P4.1, P4.2, P4.3, P9.1, P9.2, P9.3, P13.2, P19.1, P19.3, P20.3 |
