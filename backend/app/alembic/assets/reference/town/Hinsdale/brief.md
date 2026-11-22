# Hinsdale Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hinsdale and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hinsdale/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hinsdale

- **Hinsdale** is a town in Cheshire County on the Connecticut River across from Brattleboro, Vermont. Site town id 255.
- **The Hinsdale School District** (site district id 255) is **SAU 92** and runs Hinsdale Elementary (21680; preschool to grade 5) and Hinsdale Middle High (Middle 26985, grades 6–8; High 21675, grades 9–12). It decides its budget at a traditional annual meeting.
- **Winchester's students:** under a 2026–2033 agreement, Hinsdale High is Winchester's anchor high school from the class of 2030 (`places.yaml`). **Winchester's research is running now** (`town/Winchester/`); agent 3 here owns Hinsdale High facts, including the agreement from Hinsdale's side, and Winchester will cite them.
- **Career programs:** check which center serves Hinsdale (the Cheshire Career Center at Keene High, researched in `town/Keene/`, or another).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 509 (2014-15), 502 (2019-20), 502 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Hinsdale Elementary 242, Hinsdale Middle 121, Hinsdale High 155; cost per pupil FY2025 Hinsdale $25,363, state $22,699; 2025 tax rates per $1,000 (Hinsdale): total $31.08, local school $18.03, municipal $8.83; Question 2: Hinsdale 66.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Hinsdale's preschool, kindergarten and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Hinsdale)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** class sizes after $1.6 million in cuts (P1.1); principal turnover (P1.2); care for parents working in Brattleboro (P1.3); bus times (P4.1); full-day kindergarten and after-care costs (P4.2); support staff and speech cuts (P5.1); reading specialists (P5.3); public pre-K and a waitlist (P12.2, P15.1).
- **Middle High and support:** math around 22% (P2.3); EFA and homeschool access (P7.1); speech evaluations for homeschoolers (P7.2); grades 6–12 in one building (P10.1, P10.2); turnover to Keene (P13.2); arts cuts (P17.1); bullying (P17.2).
- **High school and career programs:** cuts to sports, shop or buses (P2.1); trades against Keene and Brattleboro (P2.2); the Cheshire Career Center bus and sports (P6.1, P6.2); electives, AP and languages if cut (P9.1); dual enrollment and VLACS (P9.2, P14.1); the new SRO (P9.3); co-op teams (P14.2); fees and waivers (P19.1); a late bus (P19.2).
- **Money:** the tax cap and an override (P3.1); over $25,000 per student with about 520 students (P3.2); $66,000 in lunch debt (P3.3); accreditation risk (P8.1); tuitioning high schoolers out (P8.2); a $2.5 million drop in assessed value (P8.3); SAU 92's administrators and sharing with Winchester (P16.2); consolidation (P20.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Keene/` | Keene High and the Cheshire Career Center. |
| `town/Swanzey/` | Monadnock Regional, a neighbor. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Peterborough, New Ipswich, Hinsdale, Winchester and Charlestown (this wave); Strafford, Pittsfield, Hopkinton, Hillsborough, Wilton, Wakefield, Milton, Moultonborough, Nottingham and Northwood (running). Don't write facts about those towns.

## Where facts go

- `district Hinsdale` for both schools, the Winchester agreement from Hinsdale's side, and the district's budget and board.
- `sau 92` for SAU-wide facts.
- `town Hinsdale` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/Hinsdale/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Hinsdale Elementary and young families: class sizes, the principal, before- and after-school care, bus times, kindergarten and after-care, free meals, paras and speech, special education, reading specialists, counseling, summer programs, the parent portal, public pre-K, walking home, safety and visitor rules | `hinsdale-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P11.1, P11.2, P11.3, P12.2, P15.1, P15.2, P15.3 |
| 2 | The middle school grades, support and choices: math scores and help, EFAs and homeschool access, speech evaluations, returning in 6th grade, grades 6–12 in one building, storm calls, scores against Winchester and Brattleboro, teacher turnover, the parent portal, arts, bullying, screen time | `middle-grades-support-and-choices.md` | `raw/middle/` | P2.3, P7.1, P7.2, P7.3, P10.1, P10.2, P10.3, P12.3, P13.1, P13.2, P13.3, P17.1, P17.2, P17.3 |
| 3 | Hinsdale High and career programs: trades against Keene and Brattleboro, the Cheshire Career Center bus and sports, non-college paths, electives, AP and languages, colleges' view, the SRO, in-person and online courses, co-op teams, early graduation, curriculum changes, apprenticeships, fees, the late bus, FAFSA help, computer science, the Winchester agreement | `hinsdale-high-and-career-programs.md` | `raw/high/` | P2.2, P6.1, P6.2, P6.3, P9.1, P9.2, P9.3, P14.1, P14.2, P14.3, P18.1, P18.2, P19.1, P19.2, P19.3, P20.2 |
| 4 | Money and governance: cuts and what goes first, the tax cap and an override, cost per student, lunch debt, accreditation, tuitioning out, assessed value, the schools and home prices, deferred maintenance, SAU 92's administrators, the line-by-line budget, families leaving, transportation cuts, consolidation | `money-and-governance.md` | `raw/money/` | P2.1, P3.1, P3.2, P3.3, P8.1, P8.2, P8.3, P12.1, P16.1, P16.2, P16.3, P18.3, P20.1, P20.3 |
