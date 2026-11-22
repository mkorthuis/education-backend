# Peterborough Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Peterborough and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Peterborough/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Peterborough

- **Peterborough** is a town in Hillsborough County, the commercial center of the Monadnock region; it revalued property in 2025. Site town id 431.
- **The Contoocook Valley School District** (site district id 112) is **SAU 1** and runs Peterborough Elementary (22310; preschool to grade 4), South Meadow School (22295; grades 5–8) and ConVal Regional High School (22290; grades 9–12), plus elementary schools in the other towns. It votes by official ballot (SB2), with each town voting on the same day.
- **Region 14 Applied Technology Center** is at ConVal High. Jaffrey-Rindge's research (`town/Jaffrey/`, `town/Rindge/`) already describes it from Conant's side. Agent 3 here owns new Region 14 facts (placed `district Contoocook Valley`); **New Ipswich's research is running now** and will cite them.
- **The ConVal lawsuit** (ConVal School District v. State, school funding) is covered in the library; cite it and add only what's new.
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 782 (2014-15), 701 (2019-20), 601 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Peterborough Elementary 254, South Meadow 332, ConVal High 645; cost per pupil FY2025 ConVal $26,979, state $22,699; 2025 tax rates per $1,000 (Peterborough): total $22.35, local school $10.77, municipal $9.50; Question 2: Peterborough 46.9% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): ConVal's kindergarten, preschool and budget-form facts, and the library's ConVal lawsuit and adequacy facts. Read them: `grep -n -B2 -A10 -E "place: district (Contoocook Valley)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** SKIP before- and after-school care and drop-off times (P1.1); First Friends pre-K for children without IEPs (P1.2); kindergarten class sizes and aides (P6.1); switching in from Happy Valley or The Well School (P6.2); bus pickup at the end of a driveway (P10.2); the Monadnock Community Early Learning Center and Robin's Nest waitlists (P15.1).
- **South Meadow:** early algebra (P3.2); phones locked away (P11.1); counselors (P11.3); homeschoolers at ConVal High (P13.1, P13.2); the move from PES (P18.1); earlier buses (P18.2); a separate 5th-grade wing (P18.3).
- **ConVal High:** AP and dual credit (P3.3); Region 14 certifications and a CTE wing renovation (P4.1, P4.2); a late activity bus (P14.1); booster costs (P14.3); arts cuts (P16.1); MacDowell and Peterborough Players partnerships (P16.2); Running Start costs and transfer (P17.1).
- **Money:** the 2025 revaluation and ConVal's share of the bill (P2.1, P12.1); closing or combining small elementary schools (P2.2, P12.2); towns withdrawing (P2.3); the lawsuit (P8.2); board votes by town (P8.3); turnover (P19.1); building bonds (P19.2); spending against Jaffrey-Rindge and Keene (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Jaffrey/`, `town/Rindge/` | Jaffrey-Rindge and Conant, with Region 14 from Conant's side. |
| `town/Keene/` | Keene, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Peterborough, New Ipswich, Hinsdale, Winchester and Charlestown (this wave); Strafford, Pittsfield, Hopkinton, Hillsborough, Wilton, Wakefield, Milton, Moultonborough, Nottingham and Northwood (running). Don't write facts about those towns.

## Where facts go

- `district Contoocook Valley` for the schools, Region 14 and the district's budget and board.
- `sau 1` for SAU-wide facts.
- `town Peterborough` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Peterborough/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Peterborough Elementary and young families: before- and after-school care, First Friends pre-K, two-hour delays, moving mid-year, meals and fee help, half days, kindergarten size and aides, coming from private schools, outdoor time and art, English learners and Spanish, driveway pickup, child care waitlists and prices, part-time preschool | `pes-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P6.1, P6.2, P6.3, P9.1, P9.2, P9.3, P10.2, P15.1, P15.2, P15.3 |
| 2 | South Meadow, support and choices: early algebra, special education and paras, who to call at the SAU, guardianship papers, after-school tutoring, phones, bullying, counselors, homeschool access and EFAs, the move from PES, bus times, 5th graders with 8th graders | `south-meadow-support-and-choices.md` | `raw/middle/` | P3.2, P7.1, P7.2, P7.3, P10.1, P10.3, P11.1, P11.2, P11.3, P13.1, P13.2, P13.3, P18.1, P18.2, P18.3 |
| 3 | ConVal High and Region 14: AP and dual credit, Region 14 certifications, the CTE wing, apprenticeships and work-study, the late bus, grade checks, booster costs, the arts and local partnerships, portfolios, Running Start, college and non-college counseling, FAFSA and scholarships, AP workload, internships for credit, Wi-Fi and laptops | `conval-high-and-region-14.md` | `raw/high/` | P3.3, P4.1, P4.2, P4.3, P14.1, P14.2, P14.3, P16.1, P16.2, P16.3, P17.1, P17.2, P17.3, P20.1, P20.2, P20.3 |
| 4 | Money and governance: the tax bill after revaluation, consolidating elementary schools, towns withdrawing, scores against other towns, budget drivers, the ConVal lawsuit, board votes by town, the school share of taxes, watching meetings and voting, turnover, buildings and bonds, spending against Jaffrey-Rindge and Keene | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P3.1, P8.1, P8.2, P8.3, P12.1, P12.2, P12.3, P19.1, P19.2, P19.3 |
