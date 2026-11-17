# Exeter Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Exeter and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Exeter/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Exeter

- **Exeter** is a town in Rockingham County on the Squamscott River, home of Phillips Exeter Academy and Exeter Hospital. Site town id 173. It has a Select Board and a town manager; the school districts are separate.
- **Two school districts serve Exeter, both in SAU 16** (with Brentwood, East Kingston, Kensington, Newfields and Stratham):
  - **The Exeter School District** (site district id 173), preschool to grade 5: Main Street School (20575, preschool to grade 2; the library says the Exeter Developmental Preschool is at 13 School Street, so check where preschool is now) and Lincoln Street Elementary School (20595, grades 3–5).
  - **The Exeter Region Cooperative School District** (site district id 172), grades 6–12 for all six towns: Cooperative Middle School (20590, in Stratham) and Exeter High School (20600, 1 Blue Hawk Drive), which hosts the **Seacoast School of Technology** (SST), a regional career center whose sending schools include Epping, Exeter, Newmarket, Raymond, Sanborn Regional and Winnacunnet (the library's list).
- **Both districts vote by official ballot (SB2)**; the library has their 2026 dates.
- **Starting pages:** SAU 16, https://www.sau16.org (both districts, the boards, budgets, policies, schools); SST, linked from Exeter High's site; the town, https://www.exeternh.gov (the tax rate, assessing and exemptions, elections, recreation, the library).
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 2,234 in 2014-15, 2,049 in 2019-20, 1,775 in 2025-26.
  - Exeter High's enrollment: 1,734 in 2015-16, 1,643 in 2019-20, 1,349 in 2024-25 (all six towns).
  - Cost per pupil, FY2025: Exeter (K–5) $29,439; Exeter Region Cooperative $24,141; state $22,699.
  - Tax rates per $1,000 (NH DRA, 2025): total $18.76, local school $12.46 (Exeter's district plus its cooperative share), municipal $4.48. P4.1 says the 2026 rate is $19.54 and P20.3 "almost $13" for schools: check the 2026 rate.
  - Question 2 (November 2026): Exeter voted 3,460 to 4,603, 42.9% yes (the site's data).
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes (with the cooperative share). Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/*/exeter-*` (the 2026 budget flyer and policy JEB).
- **Library facts already loaded** (don't repeat them): Exeter's kindergarten cutoff, the Exeter Developmental Preschool, both districts' SB2 dates, and the cooperative's member towns (`high-school-tuition-options` 30). Read them: `grep -n -B2 -A10 -E "place: district (Exeter|Exeter Region Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** the 2026 rate of $19.54 and the school share climbing (P4.1, P20.3); how the cooperative splits costs among the six towns, and who subsidizes whom (P4.2; the cooperative's apportionment formula); senior exemptions (P4.3); the state "capping special ed aid increases" and para cuts (P6.3; the library has special education aid); an open enrollment debate in the co-op (P12.2); bonds for Main Street or Lincoln Street (P14.3).
- **Schools and programs:** preschool at Main Street School and its waitlist (P1.1); full-day kindergarten for every child and its times (P1.2); why PreK–2 and 3–5 are split (P10.2); a 7:30 start at Exeter High (P13.2); the bus ride to Stratham and a late bus at CMS (P7.1, P7.2); routes combined for driver shortages (P9.3); SST plumbing and HVAC and its certifications (P2.1, P2.2); SST evening classes for adults (P20.1); "annual homeschool paperwork" (P16.2; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); Great Bay Charter School's lottery (P10.3); Niche ratings (P14.2; `school-rating-sites`).

## Already researched, or being researched now

- **Being researched at the same time** (November 16, 2026): **Hampton** and **Milford**. Exeter's agent 2 owns the **Seacoast School of Technology**: its programs, credentials, schedule, admission and adult classes, placed `district Exeter Region Cooperative`. Hampton's agents write only Winnacunnet's side of SST. Don't write facts about Hampton, Winnacunnet or Milford.
- **Portsmouth** (`town/Portsmouth/`) and **Dover** (`town/Dover/`), finished: Seacoast comparisons, Great Bay Community College options (Dover's `high-school-and-ctc.md`), and Seacoast Charter and other private options (Dover's `choices-and-adult-learning.md`). Cite them for P12.3 and P14.2 comparisons.
- **State rules already written:** the library and earlier towns cover EFAs and school funding, home education access to classes, activities and CTE (`district-homeschool-access`, `cte-admission-and-cost-rules`) and the end of the yearly evaluation, special education and 504 plans, English learner services and translation, free and reduced-price meals, shared custody and records (`student-records-ferpa`), bullying (the library's new `students-hb-131-bullying-law`), phones, Early College and dual enrollment, charter school lotteries, school start times (`research-school-start-times` if present; check shared-topics.md), default budgets and tax caps. Read Manchester's `student-support.md` and `charter-schools.md`, Nashua's `special-education.md`, Concord's `families-and-support.md` and Dover's `money-buildings-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place.

## Where facts go

- `district Exeter` for the Exeter School District, Main Street and Lincoln Street, the preschool, its budget and board.
- `district Exeter Region Cooperative` for Cooperative Middle School, Exeter High School, SST, the cooperative's budget, board and cost sharing.
- `sau 16` for facts that apply to every SAU 16 district (SAU-wide policies, the superintendent's office, shared services). Write them in your own file in `town/Exeter/`; later SAU 16 towns will find them here.
- `town Exeter` for town government and services: the Select Board, the town's tax rate, assessing and exemptions, police and SROs, recreation and before- and after-school programs, the library, food pantries.
- Charter and private schools: their own district record if the site has one (Great Bay Charter School may be under its charter board's name; check the places list the loader accepts), otherwise `town Exeter` with the school named. Phillips Exeter Academy: `town Exeter` with the academy named. No place for general NH rules.

All four agents write in `town/Exeter/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** budgets, taxes, cost sharing, bonds, staffing and pay belong to agent 4; SST to agent 2; Exeter High's own programs to agent 3; the elementary schools and preschool to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Exeter's elementary schools, the early years and family support: preschool and its waitlist, full-day kindergarten and its hours, drop-off near Main Street, advanced learners at Lincoln Street, special education at Main Street and the move to Lincoln Street, before- and after-school care and costs, discreet meals, class sizes and reading results, the PreK–2 and 3–5 split, Great Bay Charter School's lottery, differences from Stratham and Kensington, English learners, diversity and welcome, translated notices | `elementary-schools-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P6.1, P6.2, P9.1, P9.2, P10.1, P10.2, P10.3, P14.1, P15.1, P15.2, P15.3 |
| 2 | Cooperative Middle School, getting there, home education and the Seacoast School of Technology: SST plumbing and HVAC and the high school day, SST credentials, hands-on electives at CMS, the move from Lincoln Street to a six-town school, the bus to Stratham, late buses, mixing across towns, route cuts, Early College and SST credits, EFA students in CMS sports and band, home education paperwork, bullying, vaping and phones at CMS, sixth graders' first year, substitutes, SST evening classes for adults | `cms-sst-and-getting-to-school.md` | `raw/middle/` | P2.1, P2.2, P2.3, P3.2, P7.1, P7.2, P7.3, P9.3, P13.1, P16.1, P16.2, P17.1, P17.2, P17.3, P20.1 |
| 3 | Exeter High School: AP and honors science, portals for two households, clubs for students not in sports, help for average students, the school's identity next to Phillips Exeter and shared programs, counseling for competitive colleges, graduates' readiness against Winnacunnet and Portsmouth, the 7:30 start, help for undecided juniors, placing homeschooled 9th graders, pressure and mental health, traffic at dismissal, electives and independent study | `exeter-high-school.md` | `raw/high/` | P3.3, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P12.3, P13.2, P13.3, P16.3, P18.1, P18.2, P18.3 |
| 4 | Money, governance, buildings, staff and community support: the 2026 rate and the school share, the cooperative's cost sharing, senior exemptions and seeing the budget, school taxes and housing costs, schools and home values, being heard as a resident without children, special education aid and paras, following school votes, open enrollment, ratings against Oyster River and Portsmouth, bonds, food programs, social workers and wait times, partnering with nonprofits, school taxes and buying a home, state aid | `money-governance-and-community.md` | `raw/money/` | P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P6.3, P12.1, P12.2, P14.2, P14.3, P19.1, P19.2, P19.3, P20.2, P20.3 |
