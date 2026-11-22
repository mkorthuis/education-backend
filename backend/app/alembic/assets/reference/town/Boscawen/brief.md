# Boscawen Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Boscawen and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Boscawen/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Boscawen

- **Boscawen** is a town in Merrimack County north of Concord. Site town id 55.
- **The Merrimack Valley School District** (site district id 352) is **SAU 46**, for Boscawen, Loudon, Penacook (Concord), Salisbury and Webster. Its schools: Boscawen Elementary (22155), Loudon Elementary (22180), Penacook Elementary (22185), Salisbury Elementary (22200), Webster Elementary (22205), Merrimack Valley Middle (26585) and High (22195).
- **Don't quote the district's budget-page explainer.** Loudon's research found it gives figures that conflict with the official documents (a "$98,450,000" budget; "We contract with First Student", though the board voted 6–5 against outsourcing buses). Use the budget, warrant and minutes instead.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Career and technical education:** the Concord Regional Technical Center, researched in `town/Concord/high-school-and-pathways.md`.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 489 (2014-15), 473 (2019-20), 464 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Boscawen Elementary 240, Merrimack Valley Middle 466, Merrimack Valley High 742; cost per pupil FY2025 Merrimack Valley $19,767, state $22,699; 2025 tax rates per $1,000 (Boscawen): total $20.80, local school $12.25, municipal $5.79; Question 2: Boscawen 65.9% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Merrimack Valley's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Merrimack Valley)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Boscawen Elementary:** care in the building (P1.1); full-day kindergarten (P1.2); pre-K (P1.3); speech and reading start times (P4.1); first-grade class sizes (P8.1, P19.2); the water testing letter (P8.2); Title I help (P11.1).
- **Middle and high school:** packed, late buses (P2.2); MVHS against Concord High (P5.1); AP cancellations (P5.2); NHTI and NEC courses (P5.3, P15.1); an alternative program (P10.2); fees (P10.3); early start times (P20.2); late buses (P20.3).
- **Money:** consolidation (P2.1, P18.2); the $2.3 million surplus (P3.2); tax caps (P3.3); technology spending (P9.1); five towns sharing (P9.3); senior exemptions (P12.1); the building's condition (P16.2); Boscawen's enrollment against Loudon's (P18.3).
- **Choices:** busing to Bishop Brady (P14.1); EFAs (P6.2, P14.3); homeschoolers at CRTC (P6.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Loudon/` (loudon-elementary-and-families.md, support-and-choices.md, middle-and-high-school.md, money-and-governance.md) | Merrimack Valley's schools, policies, the middle and high school, career programs, the budget, the five-town cost split and votes. |
| `town/Concord/` | CRTC and Concord High, for comparisons (P5.1). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newton, Rindge, Boscawen, Barnstead and Northfield (this wave); Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (running). Don't write facts about those towns.

## Where facts go

- `district Merrimack Valley` for Boscawen Elementary and any new district-wide fact.
- `sau 46` for SAU-wide facts.
- `town Boscawen` for town government, recreation, taxes and community programs.
- No place for general NH rules.

All agents write in `town/Boscawen/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school and career programs to agent 3; support and choices to agent 2; the elementary school and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Boscawen Elementary and young families: care in the building, kindergarten and bus stops, pre-K, speech and reading services, sensory needs, class sizes, drinking water, recess and specials, Title I help, meals, storm calls, homework when sick, discreet breakfast, infant care, 504 plans and IEPs, aides, summer programs | `boscawen-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P13.1, P13.2, P16.3, P19.1, P19.2, P19.3 |
| 2 | Support, the middle school and choices: the middle school buses, out-of-district transport, homeschool and EFA access, homeschoolers at CRTC, safety and fights at the middle school, moving to Penacook mid-year, busing to private schools, the move to the middle school, EFAs for private school, discrimination and phone policies, start times | `support-and-choices.md` | `raw/support/` | P2.2, P4.3, P6.1, P6.2, P6.3, P9.2, P13.3, P14.1, P14.2, P14.3, P17.3, P20.2 |
| 3 | Merrimack Valley High School and CRTC from Boscawen: welding and auto at CRTC, MVHS against Concord High, AP and honors, dual enrollment, trades and financial literacy, adult education, counseling, the alternative program, fees, civics, college credit, scholarships, graduation and FAFSA, STEM, test scores, CRTC culinary and computer programs, late buses | `merrimack-valley-from-boscawen.md` | `raw/high/` | P2.3, P5.1, P5.2, P5.3, P7.2, P7.3, P10.1, P10.2, P10.3, P12.3, P15.1, P15.2, P15.3, P17.1, P17.2, P20.1, P20.3 |
| 4 | Money and governance: consolidation, the school tax against enrollment, the surplus, tax caps, renters and school taxes, technology spending, the five-town district, senior exemptions, the budget breakdown, value for money, Boscawen Elementary's building, the SAU budget, Boscawen's enrollment against Loudon's | `money-and-governance.md` | `raw/money/` | P2.1, P3.1, P3.2, P3.3, P7.1, P9.1, P9.3, P12.1, P12.2, P16.1, P16.2, P18.1, P18.2, P18.3 |
