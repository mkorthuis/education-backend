# Bethlehem Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Bethlehem and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Bethlehem/questions.md`: 20 profiles and 60 questions, shared by 5 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Bethlehem

- **Bethlehem** is a town in Grafton County in the White Mountains, on Routes 302 and 142 (ski areas, Bretton Woods nearby). Site town id 53.
- **The Bethlehem School District** (site district id 53) is in **SAU 35** and runs Bethlehem Elementary School (BES; 21400; preschool to grade 6). Students in grades 7–12 attend **Profile** (site district id 450): Profile Junior High (26990; grades 7–8) and Profile Senior High (21395; grades 9–12), both in Bethlehem. SAU 35 also includes Lafayette Regional (Franconia and Sugar Hill; id 288) and Landaff (id 291). Check which towns belong to Profile's cooperative, how its costs are split, and how many school boards and budgets there are.
- **Career programs:** Littleton's Gallen Career and Technical Center is researched in `town/Littleton/`. Cite it; write Bethlehem's side (access from Profile, the bus, credits).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 320 (2014-15), 261 (2019-20), 256 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Bethlehem Elementary 142, Profile Junior High 83, Profile Senior High 133; cost per pupil FY2025 Bethlehem $25,103 (Bethlehem) and $29,875 (Profile), state $22,699; 2025 tax rates per $1,000 (Bethlehem): total $16.19, local school $9.28, state education $1.23, municipal $4.50, county $1.18; Question 2: Bethlehem 57.6% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Bethlehem's kindergarten, preschool and budget-form facts, and Profile's. Read them: `grep -n -B2 -A10 -E "place: district (Bethlehem|Profile)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Bethlehem Elementary:** reliable after-school care until 5:30 p.m. (P1.1); full-day Pre-K (P4.1); a nurse every day (P11.2); an earliest pickup out on the back roads (P11.1); a strict morning drop-off window (P16.1); daily recess and gym (P16.2); how a child coming from Bethlehem Christian School is placed (P20.1); BES against Lafayette Regional in Franconia (P9.1).
- **Profile:** "only around 200 kids" in grades 7–12 (P2.1; the site shows 216 in 2024-25); VLACS (P2.2); counseling five days a week (P15.1); a phone policy (P15.2); co-op teams with Littleton (P12.3); late buses after practices and rehearsals (P19.2); whether Bethlehem kids are as included as Franconia and Sugar Hill kids (P19.3); updated science labs (P18.2); dual enrollment with White Mountains Community College or Plymouth State (P12.2).
- **Money and governance:** four separate school boards under SAU 35 (P13.3); Bethlehem's share of Profile against Franconia, Sugar Hill and Easton (P3.2); The White Mountain School closed and its effect (P10.2); the property tax split between BES, Profile and the SAU (P10.1); security upgrades and code (P13.1); spending per student in Grafton County (P13.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Littleton/` | Littleton High and the Gallen CTC (programs, buses, credits), Lakeway and Daisy Bronson, and Littleton's money and governance. |
| `town/Berlin/` | Berlin's career center and college credit (White Mountains Community College), for comparison. |
| `town/Plymouth/` | Plymouth Regional (Pemi-Baker) and Plymouth State, for dual enrollment comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 22, 2026): Antrim, Bristol, Campton, Canaan, Chesterfield, Chichester, Dunbarton, Gorham, Grantham, Lancaster, Mont Vernon, New Durham, Plainfield, Rollinsford, Sanbornton, Sunapee, Thornton, Tuftonboro, Walpole, Warner and Whitefield (this batch, all running now). Don't write facts about those towns.

## Where facts go

- `district Bethlehem` for Bethlehem Elementary and the Bethlehem district's budget and board.
- `district Profile` for Profile School and the cooperative's budget, cost split and board.
- `sau 35` for SAU-wide facts (the four boards, the central office, special education across towns).
- `town Bethlehem` for town government, recreation, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Bethlehem/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 5; Profile's academics and career programs to agent 3; Profile's student life and support to agent 4; Bethlehem Elementary's upper grades and choices to agent 2; Bethlehem Elementary's early grades and families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Bethlehem Elementary, early grades and families: after-school care, winter bus pickups and early calls, reading help, Pre-K, vacation-week care, school lunch applications, paper notices, the counselor, summer programs, earliest pickups, the nurse, midday alerts, drop-off windows, recess and gym, touring and enrolling | `bethlehem-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P16.1, P16.2, P16.3, P20.3 |
| 2 | Bethlehem Elementary, learning and choices: BES against Lafayette Regional, class size and combined grades, anti-bullying and digital safety lessons, homework, curriculum and scores, volunteers and retired teachers, math enrichment, placing a child from a private school, arts and music, EFAs and homeschool paperwork to SAU 35 | `bethlehem-elementary-learning-and-choices.md` | `raw/learning/` | P6.2, P6.3, P9.1, P9.2, P14.2, P14.3, P17.2, P17.3, P19.1, P20.1, P20.2 |
| 3 | Profile High School and career programs: AP and advanced math at a small school, VLACS, the Littleton tech center and its bus, credit for work and apprenticeships, preparation for work as well as college, outdoor and environmental programs, graduates' plans, dual enrollment, co-op sports with Littleton, college and career advising, science labs, local scholarships | `profile-high-and-career.md` | `raw/high/` | P2.1, P2.2, P5.1, P5.2, P5.3, P9.3, P12.1, P12.2, P12.3, P18.1, P18.2, P18.3 |
| 4 | Profile student life and support: coming in at 7th grade from out of state, sports and band for homeschoolers, the IEP handoff, paras and speech therapists across four towns, IEP disagreements, counseling, phones, 504 plans and quiet spaces, late buses after activities, inclusion of students from four towns | `profile-student-life-and-support.md` | `raw/support/` | P2.3, P6.1, P7.1, P7.2, P7.3, P15.1, P15.2, P15.3, P19.2, P19.3 |
| 5 | Money and governance: why taxes rise with small enrollment, the cost split for Profile among the towns, a plain-English budget, the tax bill's split between BES, Profile and the SAU, The White Mountain School's closing, local purchasing, security and building codes, spending per student, four boards under SAU 35, short-term rentals and enrollment, teacher retention | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P10.1, P10.2, P10.3, P13.1, P13.2, P13.3, P14.1, P17.1 |
