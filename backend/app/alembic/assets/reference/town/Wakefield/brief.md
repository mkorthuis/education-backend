# Wakefield Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Wakefield and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Wakefield/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Wakefield

- **Wakefield** is a town in Carroll County on the Maine border south of Ossipee; its villages include Sanbornville, Union, East Wakefield and North Wakefield. Site town id 543.
- **The Wakefield School District** (site district id 543) is **SAU 101** and runs Paul School (22110), preschool to grade 8, at 60 Taylor Way in Sanbornville. It votes by official ballot (SB2).
- **High school:** Spaulding High School in Rochester (22700) and Bud Carlson Academy under an AREA plan in force since 1970, amended effective July 1, 2018 (`places.yaml`: 148 Wakefield students at Spaulding in 2025-26). The plan lets Wakefield's board approve and pay tuition elsewhere for up to 10% of grades 9–12 each year; 22 Wakefield students were at Kingswood in 2025-26, and no Kingswood agreement was found. Check how those seats are chosen. Rochester and Spaulding (with the Creteau Technology Center) are researched in `town/Rochester/`; Kingswood and the Lakes Region Technology Center (LRTC) in `town/Wolfeboro/`.
- **Milton's research is running now** (`town/Milton/`, SAU 64, a neighbor that may also use Rochester's career center). Agent 3 here owns new Spaulding and Creteau facts (placed `district Rochester`) that Rochester's files lack; put Milton-specific findings in "For another file".
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 616 (2014-15), 657 (2019-20), 566 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Paul School 410, Spaulding High 1,299, Kingswood High 729; cost per pupil FY2025 Wakefield $20,641, state $22,699; 2025 tax rates per $1,000 (Wakefield): total $8.71, local school $4.33, municipal $2.53; Question 2: Wakefield 70.1% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Wakefield's kindergarten cutoff, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Wakefield)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Paul School:** an 8:30 start and before-school care (P1.1); a pre-K lottery (P1.2); bus times and ride lengths from East Wakefield and Union (P1.3, P4.1); Alma (P8.3); a weekend food bag program (P9.2); 'Good Standing' (P10.2); the pickup line at 60 Taylor Way (P12.3); Fresh Picks Café and allergies (P19.1); an interim principal (P16.3); ESL (P20.1).
- **High school:** the odds and timing of a Kingswood seat (P2.1, P14.1); LRTC or Creteau for electrical (P2.2); the ride to Spaulding and late buses (P2.3, P5.1, P5.3); Wakefield's say at Spaulding (P5.2); IEP handoff to Rochester (P7.2); CNA certification (P14.2); Lions Club and other local scholarships (P14.3); Cornerstone Christian and other private options (P15.2).
- **Money:** the HB 1300 tax cap and Question 2 (P3.1, P17.2); special education and busing costs with fewer than 400 students (P3.2); an Area Agreement Committee and Rochester's tuition rate (P3.3); SAU 101's central office (P13.1); tuition's share of the tax bill (P13.2); $200,000+ a year into trust funds (P13.3); board votes against teacher contracts (P17.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Rochester/` | Spaulding High, Bud Carlson Academy and the Creteau Technology Center; Rochester's side of its sending-town agreements. |
| `town/Wolfeboro/` and `town/Ossipee/` (running) | Kingswood Regional High and LRTC; Governor Wentworth's tuition terms for outside students. |
| `town/Farmington/` | A neighboring one-district SAU, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Wakefield, Milton, Moultonborough, Nottingham and Northwood (this wave); Greenland, Rye, Brentwood, Fremont, Chester, Ossipee and New Boston (running). Don't write facts about those towns.

## Where facts go

- `district Wakefield` for Paul School and the district's budget, board and its side of the Spaulding plan.
- `district Rochester` only for Spaulding, Bud Carlson or Creteau facts Rochester's files lack.
- `district Governor Wentworth Regional` only for Kingswood or LRTC facts Wolfeboro's files lack.
- `sau 101` for SAU-wide facts.
- `town Wakefield` for town government, recreation, the Gafney Library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Wakefield/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Paul School's early grades and families: before-school care, pre-K, bus stop times and rides, math challenge, late-bus alerts, scores against neighbors, Alma, homework help, meals and the food bag program, early-release days, class sizes, the pickup line, allergies, lunch accounts, winter recess | `paul-school-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P8.2, P8.3, P9.1, P9.2, P12.1, P12.2, P12.3, P19.1, P19.2, P19.3 |
| 2 | Paul School's upper grades, support and choices: homeschool access and returning, special education support, sports and drama fees, 'Good Standing', technology and STEM, snow days, transferring in for grades 7–8, the principal, behavior and phones, ESL, world languages, bullying | `paul-school-upper-grades-support-and-choices.md` | `raw/middle/` | P6.1, P6.2, P6.3, P7.1, P9.3, P10.2, P11.2, P11.3, P15.3, P16.3, P17.3, P20.1, P20.2, P20.3 |
| 3 | High school from Wakefield: Spaulding, Kingswood seats, LRTC and Creteau, the bus to Rochester and late buses, a say at Spaulding, IEP handoffs, choosing a high school, AP and dual enrollment, transferring mid-high school, CNA certification, local scholarships, enrolling as new residents, private schools, dropouts and online school | `high-school-from-wakefield.md` | `raw/high/` | P2.1, P2.2, P2.3, P5.1, P5.2, P5.3, P7.2, P8.1, P11.1, P14.1, P14.2, P14.3, P15.1, P15.2, P18.2 |
| 4 | Money and governance: the tax cap and cuts, special education and busing costs, the Rochester tuition rate, outside specialists, renters and warrant articles, town against school budgets, SAU 101's central office, tuition's share of taxes, trust funds, the school-town pitch and home values, teacher contracts and pay, hiring, a different high school arrangement, board meetings | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P7.3, P10.1, P10.3, P13.1, P13.2, P13.3, P16.1, P16.2, P17.1, P17.2, P18.1, P18.3 |
