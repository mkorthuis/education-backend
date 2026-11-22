# Wolfeboro Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Wolfeboro and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Wolfeboro/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Wolfeboro

- **Wolfeboro** is a town in Carroll County on Lake Winnipesaukee. Site town id 583.
- **The Governor Wentworth Regional School District** (site district id 208) is **SAU 49**, for Brookfield, Effingham, New Durham, Ossipee, Tuftonboro and Wolfeboro. Its schools: Carpenter (22430) and Crescent Lake (27515) in Wolfeboro; Effingham Elementary (22395), New Durham Elementary (22400), Ossipee Central (22405), Tuftonboro Central (22410); Kingswood Regional Middle (22440) and High (22425) in Wolfeboro. Check which grades Carpenter and Crescent Lake hold (P1.2). It decides its budget by official ballot (SB2).
- **Shared district, first town.** Ossipee shares this district and is researched in the next wave; it will cite these files. So cover district-wide facts (Kingswood, the Lakes Region Technology Center, the budget, the cost formula, policies) fully, placed with the district, and keep town-only facts placed with the town.
- **Tuition students:** Kingswood takes Middleton's grades 7–12 under a long-term agreement, and SAU 13's towns (Freedom, Madison, Tamworth) gained Kingswood agreements after leaving Kennett (`places.yaml`; Freedom's, Madison's and Tamworth's research). Write Governor Wentworth's side.
- **Starting pages:** GWRSD, https://www.gwrsd.org (board, budget, policies, schools); the Town of Wolfeboro's site for taxes; NH DOE profiles.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 728 (2014-15), 704 (2019-20), 564 (2025-26); school enrollment in 2024-25 (the site's "2025" row): Carpenter 183, Crescent Lake 181, Kingswood Middle 345, Kingswood High 729; cost per pupil FY2025 Governor Wentworth $26,293, state $22,699; 2025 tax rates per $1,000 (Wolfeboro): total $8.36, local school $3.37, municipal $3.21; Question 2: Wolfeboro 56.4% yes, the district 65.2% (unofficial), adopted.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Governor Wentworth's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Governor Wentworth Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** after-school care at Carpenter (P1.1); the building switch in 3rd grade (P1.2); pre-K on snow days (P1.3); scores (P4.1); gifted groups (P4.2); speech and reading staff (P8.1); public pre-K (P15.1); class sizes K–3 (P15.2); competency report cards (P16.1); petition articles for playgrounds (P18.1).
- **Middle school:** bus times (P6.1); phones and bullying (P6.2); fee help (P6.3); a late bus (P13.2); rides over an hour (P14.1); snow days across six towns (P14.2); the bus fleet (P14.3); world languages (P19.1); counselors (P19.2).
- **Kingswood and LRTC:** sports with LRTC classes (P2.1); equipment (P2.2); crowding from SAU 13 students (P2.3, P5.2); college credit (P5.1); a 900-student school (P12.3); AP and arts (P12.1); AI and phones (P19.3).
- **Money:** tax growth (P3.1); Wolfeboro's share of the budget (P3.2); the default budget (P3.3); tuition revenue and SAU 13 (P10.1, P20.2); a surprise bond (P10.2); aide and support staff pay (P11.1, P11.2); teacher contract votes (P15.3); state against local funding (P7.2, P20.1).
- **Home education:** sports, band and single classes for homeschoolers, and EFAs (P9.1–P9.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Freedom/`, `town/Madison/`, `town/Tamworth/` | SAU 13's move from Kennett to Kingswood and Moultonborough: their tuition agreements and Kingswood facts. |
| `town/Meredith/`, `town/Gilford/`, `town/Alton/` | Neighboring districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (this wave); Kingston, Jaffrey, Loudon, Alton and Tilton (finishing); Newton, Rindge, Boscawen, Barnstead and Northfield (starting soon). Don't write facts about those towns.

## Where facts go

- `district Governor Wentworth Regional` for all its schools, LRTC, policies, budget and board.
- `sau 49` for SAU-wide facts.
- `town Wolfeboro` for town government, recreation, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Wolfeboro/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; Kingswood High and LRTC to agent 3; Kingswood Middle, support and choices to agent 2; the Wolfeboro elementary schools to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Carpenter, Crescent Lake and young families: after-school care, the building switch, pre-K and snow days, scores, gifted groups, volunteering, speech and reading staff, IEPs between schools, public pre-K, class sizes, competency report cards, math help, summer programs, young families and enrollment, playgrounds | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P7.3, P8.1, P8.2, P15.1, P15.2, P16.1, P16.2, P16.3, P17.2, P18.1 |
| 2 | Kingswood Middle, support and choices: bus times and early care, phones and bullying, fee help, special education funding, homeschool and EFA access, the move to the high school, late buses, long rides, snow days across six towns, the bus fleet, laptops and internet, gym schedules, world languages, counselors | `middle-school-support-and-choices.md` | `raw/middle/` | P6.1, P6.2, P6.3, P8.3, P9.1, P9.2, P9.3, P13.1, P13.2, P14.1, P14.2, P14.3, P17.3, P18.2, P19.1, P19.2 |
| 3 | Kingswood Regional High and the Lakes Region Technology Center: sports with LRTC classes, equipment, crowding from new tuition students, college outcomes, college credit, scholarships, the Arts Center for residents, graduates in local trades, AP and arts, college aid, a 900-student school, the calendar, AI and phones | `kingswood-high-and-lrtc.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.3, P5.1, P5.2, P5.3, P7.1, P10.3, P12.1, P12.2, P12.3, P13.3, P19.3 |
| 4 | Money and governance: tax growth, Wolfeboro's share, the default budget, state against local funding, tuition revenue from SAU 13 and Middleton, buildings and bonds, aide and support staff pay, bus drivers, staff housing, teacher contract votes, taxes on a $450,000 house, when to speak to the board, where the money comes from and goes | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P7.2, P10.1, P10.2, P11.1, P11.2, P11.3, P15.3, P17.1, P18.3, P20.1, P20.2, P20.3 |
