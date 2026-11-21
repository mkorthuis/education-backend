# Newmarket Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Newmarket and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Newmarket/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Newmarket

- **Newmarket** is a town in Rockingham County on the Lamprey River, with its downtown mill buildings, between Durham, Exeter and Newfields. Site town id 399.
- **The Newmarket School District** (site district id 399) is **SAU 31**, a one-district SAU voting by official ballot. Schools: Newmarket Elementary (21300), preschool to grade 5; Newmarket Junior-Senior High (23115 for 9–12, 26560 for 6–8 in the site's data), grades 6–12.
- **Career and technical education:** Newmarket is an SST sending school (`town/Exeter/cms-sst-and-getting-to-school.md`); write only Newmarket's side.
- **Starting pages:** the district, https://www.newmarket.k12.nh.us; the town, https://www.newmarketnh.gov.
- **Site figures:** resident students 999 (2014-15), 1,039 (2019-20), 964 (2026-27); cost per pupil FY2025 Newmarket $24,105, state $22,699; 2025 tax rates per $1,000: total $19.42, local school $12.85, municipal $4.87; Question 2: Newmarket 44.9% yes, so no cap (unofficial); math proficiency 2026: Newmarket 53%, Oyster River 69%, state 44% (P2.1).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Newmarket's kindergarten, registration, preschool and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Newmarket)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** walking from the mills (P1.2); public preschool (P5.1); class sizes (P5.2); full-day kindergarten and cost (P16.1); dyslexia screening (P18.1); a separate middle school wing (P2.3); UNH courses (P2.2); AP in person against VLACS (P12.1, P12.2); counselor caseloads (P12.3); JV and varsity and co-op teams (P15.1, P15.2); trimmed music time and 7th-grade band (P19.1); senior project and credits (P20.1).
- **Money:** a $39 million renovation being paid off (P3.1); repairs since (P3.2); a $100,000 building reserve (P8.1); unfilled positions and leftover money (P8.2); about a thousand students (P8.3); rents and budgets (P11.1); the commercial tax share (P17.3).
- **Choices:** a yearly homeschool filing with SAU 31 (P10.2; repealed July 1, 2026); downtown traffic (P17.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Exeter/cms-sst-and-getting-to-school.md` | SST: programs, sessions, credits, admission, enrollment by sending school (Newmarket's count included). |
| Durham's research (running now) | Oyster River, for the comparison in P2.1; cite the site's data instead. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Stratham, Epping, Raymond and Durham (this wave), and from the first wave Atkinson, Plaistow (shared `town/timberlane/`), Hampstead, Pelham and Seabrook. Don't write facts about those towns.

## Where facts go

- `district Newmarket` for SAU 31, its schools, preschool, policies, staff, budget and board.
- `town Newmarket` for town government and services (tax rate, relief, recreation, fields, downtown traffic).
- No place for general NH rules.

All agents write in `town/Newmarket/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; the Junior-Senior High's programs to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Newmarket Elementary: care, walking and buses, meals and fees, reading and English help, preschool, class sizes, earliest drop-off, enrolling with records, math placement for newcomers, making friends, full-day kindergarten, dyslexia screening, reading specialists, summer reading | `elementary-school.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.2, P5.1, P5.2, P9.1, P14.1, P14.2, P14.3, P16.1, P18.1, P18.2, P18.3 |
| 2 | Newmarket Junior-Senior High: comparison with Oyster River, advanced math and UNH, the middle school's own wing, college and financial aid help, SST and the bus, guidance for trades, AP in person and VLACS, counselor caseloads, work-study, band, instruments, arts clubs, credits and the senior project, Running Start and GBCC, scholarships | `junior-senior-high.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.3, P7.1, P7.2, P7.3, P12.1, P12.2, P12.3, P17.1, P19.1, P19.2, P19.3, P20.1, P20.2, P20.3 |
| 3 | Support, daily life and choices: translation, paras and one-on-one help, the 5th-to-6th special education move, therapy pull-outs, delay notices, bus reliability, EFA and homeschool access and paperwork, re-entry placement, the portal, phones, counselors, sports teams and co-ops, late buses, drop-off traffic | `support-daily-life-and-choices.md` | `raw/support/` | P4.1, P6.1, P6.2, P6.3, P9.2, P9.3, P10.1, P10.2, P10.3, P13.1, P13.2, P13.3, P15.1, P15.2, P15.3, P17.2 |
| 4 | Money and governance: the renovation bond and repairs, classroom against central office, staying through high school, the building reserve, unfilled positions, enrollment and programs, rents, renters' say, community use of fields, tax relief, family costs, the commercial tax share | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P5.3, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P16.2, P16.3, P17.3 |
