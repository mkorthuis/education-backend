# Epsom Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Epsom and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Epsom/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Epsom

- **Epsom** is a town in Merrimack County. Site town id 167.
- **The Epsom School District** (site district id 167) is in **SAU 53** with Pembroke, Allenstown, Chichester and Deerfield (the SAU office is in Pembroke). It runs Epsom Central School (22600), kindergarten to grade 8; 378 students in 2024-25. It decides its budget by official ballot (SB2).
- **High school:** Pembroke Academy under an AREA agreement (`places.yaml`; Allenstown and Epsom raised reopening it in 2026). Pembroke's money file shows a few Epsom students at Prospect Mountain; check what other high schools Epsom pays for and whether a family may choose Coe-Brown Northwood Academy (P5.1). Coe-Brown is researched in `town/Barrington/high-school-choice.md`.
- **SAU 53 and Pembroke Academy are already researched** in `town/Pembroke/` (SAU 53's cost split and budget, Pembroke Academy's courses, CRTC access, buses, counselors and outcomes). Cite those facts by file, topic and number; write only this town's side. Allenstown, Epsom and Deerfield (all SAU 53) are being researched at the same time, so don't write facts about each other's schools.
- **Career and technical education:** the Concord Regional Technical Center (CRTC), researched in `town/Concord/high-school-and-pathways.md` and from Pembroke Academy's side in `town/Pembroke/pembroke-academy.md`.
- **Starting pages:** SAU 53, https://www.sau53.org (district pages, board agendas and minutes, budgets, policies); the town's own site for taxes and town reports; NH DOE profiles.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 644 (2014-15), 587 (2019-20), 542 (2025-26); school enrollment (the site's "2025" row is the October 1, 2024 count, i.e. 2024-25): Epsom Central School 378 students in 2024-25; cost per pupil FY2025 Epsom $25,297, state $22,699; 2025 tax rates per $1,000: total $17.54, local school $12.12, municipal $2.74; Question 2: Epsom 66.7% yes (unofficial), adopted by the district.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Epsom's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Epsom)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Epsom Central:** full-day kindergarten and care (P1.1); low math scores (P2.3); speech and special education staffing (P3.1); public pre-K in town (P8.3); phonics (P11.1); testing times (P11.2); class sizes (P20.2); security (P17.2); teacher turnover (P17.3).
- **High school:** Coe-Brown instead of Pembroke Academy (P5.1); an 850-student Academy (P5.2); early bus times (P7.1, P16.1); NHTI dual enrollment and Running Start (P7.2, P16.2); a late bus (P16.3); open enrollment elsewhere (P18.3).
- **Money:** about 380 students (P4.1); SAU 53 administration costs (P4.2); being locked in to Pembroke Academy (P4.3); school taxes on a $450,000 house (P8.2); the building's roof and HVAC (P10.2); vouchers costing the town (P13.1); out-of-town transport (P13.2); paras and substitutes (P20.1).
- **Home education:** homeschoolers in sports and band, and EFAs (P9.1, P9.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Pembroke/` | SAU 53 (cost split, budget, policies), Pembroke Academy (courses, CRTC, buses, counselors, outcomes) and the Academy's tuition and AREA terms. |
| `town/Barrington/high-school-choice.md` | Coe-Brown Northwood Academy (admission, tuition, courses). |
| `town/Concord/high-school-and-pathways.md` | CRTC's programs and admission; Concord High for comparison (P18.2). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (this wave); Kingston, Jaffrey, Loudon, Alton and Tilton (finishing); Newton, Rindge, Boscawen, Barnstead and Northfield (starting soon). Don't write facts about those towns.

## Where facts go

- `district Epsom` for Epsom Central School, the district's budget, board, policies and its side of the AREA agreement.
- `sau 53` only for SAU-wide facts not already in Pembroke's files.
- `town Epsom` for town government, recreation, private schools in town and taxes.
- No place for general NH rules.

All agents write in `town/Epsom/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money, taxes, staffing costs and governance belong to agent 4; Pembroke Academy and other high schools to agent 3; Epsom Central's upper grades, support and choices to agent 2; its early grades and families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Epsom Central's early grades and families: full-day kindergarten and care, buses on side roads, kindergarten registration, math scores and help, family communication, the school's reputation, pre-K in town, phonics, testing for learning disabilities, summer reading, split-household buses, delays, security, class sizes | `epsom-central-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.3, P6.2, P8.1, P8.3, P11.1, P11.2, P11.3, P14.1, P17.1, P17.2, P20.2 |
| 2 | Epsom Central's upper grades, support and choices: shop and hands-on classes, special education staff, who to call at SAU 53, the late bus, homework help, homeschool and EFA access, middle school sports and clubs, voucher and private school costs, bullying and social media, counseling, Cornerstone Christian Academy, after-school spaces, advanced math, open enrollment | `epsom-central-upper-grades-support-and-choices.md` | `raw/middle/` | P2.1, P3.1, P3.3, P6.1, P6.3, P9.1, P9.2, P12.2, P13.1, P14.2, P14.3, P15.1, P15.2, P18.1, P18.3 |
| 3 | Pembroke Academy and other high schools from Epsom: CRTC, the IEP move, Coe-Brown, the jump to a bigger school, honors and AP, the Academy bus and early pickups, NHTI and VLACS, safety, 9th grade placement after homeschooling, personal finance, varsity teams, absences for travel sports, prevention and counseling, late buses, STEM against Concord and Coe-Brown, welding and diesel, work-study, local scholarships | `pembroke-academy-from-epsom.md` | `raw/high/` | P2.2, P3.2, P5.1, P5.2, P5.3, P7.1, P7.2, P7.3, P9.3, P10.3, P12.1, P12.3, P15.3, P16.1, P16.2, P16.3, P18.2, P19.1, P19.2, P19.3 |
| 4 | Money and governance: school taxes against enrollment, SAU 53 costs, the Pembroke Academy agreement and tuition, taxes on a $450,000 house and budget votes, warrant articles, the building's condition, out-of-town transport costs, the budget breakdown, teacher turnover, paras and substitutes, the school board | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P8.2, P10.1, P10.2, P13.2, P13.3, P17.3, P20.1, P20.3 |
