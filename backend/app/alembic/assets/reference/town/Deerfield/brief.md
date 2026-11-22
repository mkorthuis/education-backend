# Deerfield Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Deerfield and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Deerfield/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Deerfield

- **Deerfield** is a town in Rockingham County east of Concord. Site town id 127.
- **The Deerfield School District** (site district id 127) is in **SAU 53** with Pembroke, Allenstown, Chichester and Epsom (the SAU office is in Pembroke). It runs Deerfield Community School (22595), preschool to grade 8; 506 students in 2024-25. It decides its budget by official ballot (SB2).
- **High school choice:** three tuition contracts, all ending June 30, 2027 (`places.yaml`): Concord High (a new one-year MOU from July 1, 2027 was on Concord's November 2, 2026 agenda), Pembroke Academy and Coe-Brown Northwood Academy (site district id 998, a private academy in Northwood).
- **Shared school, first town.** Northwood (Coe-Brown's home town) is researched in a later wave and will cite these files. Barrington's research already covers Coe-Brown (`town/Barrington/high-school-choice.md`); cite it, and write what it lacks about Coe-Brown fully, placed `district Coe-Brown Northwood Academy`.
- **SAU 53 and Pembroke Academy are already researched** in `town/Pembroke/` (SAU 53's cost split and budget, Pembroke Academy's courses, CRTC access, buses, counselors and outcomes). Cite those facts by file, topic and number; write only this town's side. Allenstown, Epsom and Deerfield (all SAU 53) are being researched at the same time, so don't write facts about each other's schools.
- **Career and technical education:** the Concord Regional Technical Center (CRTC), researched in `town/Concord/high-school-and-pathways.md` and from Pembroke Academy's side in `town/Pembroke/pembroke-academy.md`.
- **Starting pages:** SAU 53, https://www.sau53.org (district pages, board agendas and minutes, budgets, policies); the town's own site for taxes and town reports; NH DOE profiles.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 651 (2014-15), 691 (2019-20), 668 (2025-26); school enrollment (the site's "2025" row is the October 1, 2024 count, i.e. 2024-25): Deerfield Community School 506 students in 2024-25; cost per pupil FY2025 Deerfield $22,622, state $22,699; 2025 tax rates per $1,000: total $15.54, local school $11.39, municipal $2.57; Question 2: Deerfield 65.7% yes (unofficial), adopted by the district.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Deerfield's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Deerfield)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **DCS:** preschool spots and tuition (P1.1); care in town (P1.2); kindergarten size and recess (P1.3); long bus rides (P2.1); about half proficient (P2.2); special education staffing (P5.1); Algebra I in grade 8 (P6.1); shop classes (P7.2); gravel roads in mud season (P19.1); world languages (P18.3).
- **High school choice:** whether the town pays the same for each school (P3.1, P4.2); a cap on Coe-Brown seats (P3.2); IEPs at each school (P5.3); AP and SNHU courses (P6.2); late buses (P11.1); switching schools after 9th grade (P15.3); agriculture programs (P19.2).
- **Money:** tax growth (P4.1); the choice locked in (P10.1); ratings (P10.2); SAU 53 membership and costs (P16.1, P16.2); home values against Candia and Northwood (P16.3); DCS near capacity and a bond (P17.2); teacher turnover (P14.3).
- **Home education:** filing with the town or SAU for an EFA (P9.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Pembroke/` | SAU 53 (cost split, budget, policies) and Pembroke Academy. |
| `town/Concord/` | Concord High School and CRTC. |
| `town/Barrington/high-school-choice.md` | Coe-Brown Northwood Academy (admission, tuition, courses, its Barrington contract). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (this wave); Kingston, Jaffrey, Loudon, Alton and Tilton (finishing); Newton, Rindge, Boscawen, Barnstead and Northfield (starting soon). Don't write facts about those towns.

## Where facts go

- `district Deerfield` for DCS, the district's budget, board, policies and its side of the three tuition contracts.
- `district Coe-Brown Northwood Academy` for facts about Coe-Brown itself that Barrington's file lacks.
- `sau 53` only for SAU-wide facts not already in Pembroke's files.
- `town Deerfield` for town government, recreation, the fair and taxes.
- No place for general NH rules.

All agents write in `town/Deerfield/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money, taxes and governance belong to agent 4; the three high schools and CRTC to agent 3; DCS's upper grades, support and choices to agent 2; DCS's early grades and families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Deerfield Community School's early grades and families: the preschool, care in town, kindergarten size and recess, bus rides, delays, the parent portal, pickup when sick, security, internet and Chromebooks, report cards and conferences, reading differentiation, the kindergarten cutoff and day, the nurse, gravel roads | `dcs-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.3, P8.1, P8.3, P12.1, P13.1, P13.3, P14.2, P17.1, P17.3, P19.1 |
| 2 | DCS's upper grades, support and choices: scores, speech and special education staff, who decides special education, advanced math, VLACS, shop classes, fees and help, homeschool and EFA access, middle school sports and clubs, practical skills, counselors, bullying and phones, math intervention, world languages, attendance, readiness for high school | `dcs-upper-grades-support-and-choices.md` | `raw/middle/` | P2.2, P5.1, P5.2, P6.1, P6.3, P7.2, P8.2, P9.1, P9.3, P11.3, P12.2, P13.2, P14.1, P18.1, P18.3, P19.3, P20.1 |
| 3 | High school choice and CRTC: how the three-school choice works and is paid for, Coe-Brown seats, the move to a big school, IEPs at each school, AP and dual enrollment, welding and diesel at CRTC, apprenticeships and trade schools, returning to public school for 9th grade, late buses, sports and playing time, the smallest and most supportive school, 504 plans, switching schools, welcoming students, agriculture programs, counseling, gap years and jobs | `high-school-choice.md` | `raw/high/` | P3.1, P3.2, P3.3, P5.3, P6.2, P7.1, P7.3, P9.2, P11.1, P11.2, P15.1, P15.2, P15.3, P18.2, P19.2, P20.2, P20.3 |
| 4 | Money and governance: tax growth against enrollment, tuition per student at each high school, the budget for the deliberative session, whether choice is locked in, school ratings, the school share of the tax bill, combined tax growth, teacher turnover, SAU 53 membership and its costs, home values, DCS's capacity and any bond | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P10.1, P10.2, P10.3, P12.3, P14.3, P16.1, P16.2, P16.3, P17.2 |
