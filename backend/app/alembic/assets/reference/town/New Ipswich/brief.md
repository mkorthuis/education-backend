# New Ipswich Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for New Ipswich and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/New Ipswich/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about New Ipswich

- **New Ipswich** is a town in Hillsborough County on the Massachusetts border; Greenville is its partner town in the cooperative. Site town id 393.
- **The Mascenic Regional School District** (site district id 342) is **SAU 87** and runs Highbridge Hill Elementary (28990; preschool to grade 4), Boynton Middle School (26685; grades 5–8) and Mascenic Regional High School (23050; grades 9–12). It votes by official ballot (SB2). Check how costs are split with Greenville.
- **Career programs:** the Region 14 Applied Technology Center at ConVal High. **Peterborough's research is running now** (`town/Peterborough/`); its agent 3 owns new Region 14 facts, so put Region 14 program findings in "For another file" and write Mascenic's side (access, the bus, how many students attend). Jaffrey-Rindge (`town/Jaffrey/`, `town/Rindge/`) are neighbors already researched.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 792 (2014-15), 743 (2019-20), 718 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Highbridge Hill 363, Boynton 260, Mascenic High 252; cost per pupil FY2025 Mascenic $19,935, state $22,699; 2025 tax rates per $1,000 (New Ipswich): total $17.03, local school $12.39, municipal $2.65; Question 2: New Ipswich 53.5% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Mascenic's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Mascenic Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Highbridge Hill:** full-day kindergarten and a preschool lottery (P1.1); buses on dirt roads off Route 123 (P1.2); care at the school (P1.3); drop-off times at two schools (P2.1); Appleton Elementary's closing (P9.1); a bus stop near a blind curve (P13.2); allergies (P19.1).
- **Boynton and support:** math around 32% (P2.2); a late bus or homework club (P2.3); homeschool sports and band (P3.1); special education staffing (P7.2); busing to private schools (P11.1); sports for 5th and 6th graders and fees (P12.1, P12.3); gifted programs and early Algebra I (P16.1, P16.2).
- **Mascenic High and Region 14:** hands-on classes and the ride to ConVal (P4.1, P8.1); certifications (P4.2); 40% of graduates with no plans (P4.3); AP and honors with about 250 students (P5.1); Running Start (P5.2); VLACS (P5.3); Viking Block (P8.2); reading around 68% and math around 25% (P14.1); ASVAB (P17.1); dropped electives (P20.1); football or hockey co-ops (P20.2).
- **Money:** taxes with under 900 students (P6.1); the New Ipswich–Greenville split (P6.2); the default budget (P6.3); the capital reserve (P10.1); a contract's tax effect (P10.2); para pay against ConVal and Jaffrey-Rindge (P15.1); substitutes (P15.2); traffic on Turnpike Road (P18.1); the youth population (P18.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Jaffrey/`, `town/Rindge/` | Jaffrey-Rindge, a neighbor, with Region 14 from Conant's side. |
| `town/Peterborough/` (running) | ConVal High and the Region 14 Applied Technology Center. |
| `town/Milford/`, `town/Wilton/` (running) | Neighbors, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Peterborough, New Ipswich, Hinsdale, Winchester and Charlestown (this wave); Strafford, Pittsfield, Hopkinton, Hillsborough, Wilton, Wakefield, Milton, Moultonborough, Nottingham and Northwood (running). Don't write facts about those towns.

## Where facts go

- `district Mascenic Regional` for the three schools and the district's budget and board.
- `sau 87` for SAU-wide facts.
- `town New Ipswich` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/New Ipswich/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Highbridge Hill and young families: kindergarten and preschool, buses on dirt roads, care at the school, drop-off at two schools, free meals, the schools since Appleton closed, kindergarten and first grade class sizes, online systems for grandparents, an unsafe bus stop, reading help, allergies, lunch costs, storm alerts | `highbridge-hill-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P7.3, P9.1, P9.3, P13.1, P13.2, P13.3, P19.1, P19.2, P19.3 |
| 2 | Boynton Middle School, support and choices: math scores and help, the late bus and homework club, homeschool access and EFAs, IEPs into Boynton, special education staffing, private schools and their busing, returning to Mascenic, middle school sports, activity buses and fees, counseling and bullying, gifted programs and early algebra, STEM clubs, Chromebooks | `boynton-support-and-choices.md` | `raw/middle/` | P2.2, P2.3, P3.1, P3.2, P7.1, P7.2, P11.1, P11.3, P12.1, P12.2, P12.3, P14.2, P15.3, P16.1, P16.2, P16.3 |
| 3 | Mascenic High and Region 14: classes for homeschoolers, trades and certifications, graduates' plans, AP and honors, Running Start, VLACS, the Region 14 bus, Viking Block, class rank, reading and math results, the military and ASVAB, counseling and FAFSA, transcripts after a gap year, apprenticeships, electives, sports co-ops | `mascenic-high-and-region-14.md` | `raw/high/` | P3.3, P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P8.1, P8.2, P8.3, P14.1, P17.1, P17.2, P17.3, P18.2, P20.1, P20.2 |
| 4 | Money and governance: taxes and enrollment, the New Ipswich–Greenville split, the default budget, comparisons with Rindge and Jaffrey, the capital reserve, contract costs, spending against other districts, private school families' taxes, board meetings, para pay, substitutes, Turnpike Road traffic, the youth population, the deliberative session | `money-and-governance.md` | `raw/money/` | P6.1, P6.2, P6.3, P9.2, P10.1, P10.2, P10.3, P11.2, P14.3, P15.1, P15.2, P18.1, P18.3, P20.3 |
