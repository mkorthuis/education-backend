# Northfield Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Northfield and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Northfield/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Northfield

- **Northfield** is a town in Merrimack County across the Winnipesaukee River from Tilton. Site town id 404.
- **The Winnisquam Regional School District** (site district id 582) is **SAU 59**, for Northfield, Sanbornton and Tilton. Its schools: Southwick (27070) in Northfield; Sanbornton Central (22925); Winnisquam Early Learning Center (29247) in Tilton; Winnisquam Regional Middle (22955) and High (22950) in Tilton. Union Sanborn School (22945) in Northfield is closed (P6.2). Check Southwick's grades.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 671 (2014-15), 638 (2019-20), 520 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Southwick 251, Winnisquam Early Learning Center 30, Winnisquam Middle 361, Winnisquam High 356; cost per pupil FY2025 Winnisquam $23,715, state $22,699; 2025 tax rates per $1,000 (Northfield): total $14.79, local school $8.28, municipal $3.37; Question 2: Northfield 65.0% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Winnisquam's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Winnisquam Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Southwick:** full-day kindergarten (P1.1); bus times on Zion Hill (P1.2); after-school care (P1.3); early drop-off (P5.1); speech and OT minutes (P7.1); class sizes (P10.1); Spanish translation (P12.1); librarians (P13.1); public pre-K (P17.1).
- **Middle and high school:** the career center's trades and certifications (P2.1, P2.2); advanced math (P4.2); phones (P9.1); after-school tutoring (P9.2); Compass Classical Academy busing (P10.2); dual enrollment (P15.2); North Country Charter Academy (P20.1).
- **Money:** the rate from $8.28 to $9.30 (P3.1); Northfield paying more than Tilton or Sanbornton (P3.2); the old Union Sanborn School (P6.2); state aid (P6.3); renters and school taxes (P8.1); bonds (P18.2); the deliberative session (P18.3).
- **Home education:** filing with SAU 59 (P11.3; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Tilton/` (early-learning-and-southwick.md, middle-school-support-and-choices.md, high-school-and-wicc.md, money-and-governance.md) | Winnisquam's schools, policies, the middle and high school, the career center, the budget, the three-town cost split and votes. |
| `town/Belmont/`, `town/Laconia/` | The Winnisquam Career Center's programs (Belmont's file) and the Huot Center. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newton, Rindge, Boscawen, Barnstead and Northfield (this wave); Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (running). Don't write facts about those towns.

## Where facts go

- `district Winnisquam Regional` for Southwick and any new district-wide fact.
- `sau 59` for SAU-wide facts.
- `town Northfield` for town government, recreation, taxes and community programs.
- No place for general NH rules.

All agents write in `town/Northfield/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school and career programs to agent 3; support and choices to agent 2; the elementary school and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Southwick and young families: full-day kindergarten, bus times, after-school care, early drop-off, meals, delays, speech and OT, class sizes, translation, English learners, family events, librarians, volunteers, split-household buses, parent logins, public pre-K, the drive to Southwick, the school's reputation | `southwick-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P7.1, P10.1, P12.1, P12.2, P12.3, P13.1, P13.3, P16.1, P16.2, P17.1, P17.2, P17.3 |
| 2 | Winnisquam Middle, support and choices: scores, advanced math, paras, who to call at SAU 59, phones, tutoring, bullying and mental health, Compass Classical Academy, teacher turnover, homeschool and EFA access, reading results since the pandemic, sports pickups, LGBTQ+ students | `middle-school-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P7.2, P7.3, P9.1, P9.2, P9.3, P10.2, P10.3, P11.1, P11.2, P11.3, P13.2, P16.3, P19.1 |
| 3 | Winnisquam High and the career center from Northfield: trades and certifications, apprenticeships, AP and college credit, outdoor programs, readiness for non-college paths, college outcomes, dual enrollment, counseling and FAFSA, arts electives, charter alternatives, work-study, absenteeism and credit recovery | `high-school-and-career-center.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.3, P8.2, P14.2, P15.1, P15.2, P15.3, P19.2, P20.1, P20.2, P20.3 |
| 4 | Money and governance: the school rate increase, Northfield's share, senior tax relief, the budget breakdown, the old Union Sanborn School, state aid, renters and school taxes, board and budget votes, which schools Northfield children attend, ratings, the combined tax rate, bonds, the deliberative session, streamed meetings | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.1, P6.2, P6.3, P8.1, P8.3, P14.1, P14.3, P18.1, P18.2, P18.3, P19.3 |
