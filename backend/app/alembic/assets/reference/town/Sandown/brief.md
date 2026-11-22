# Sandown Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Sandown and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Sandown/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Sandown

- **Sandown** is a town in Rockingham County west of Danville and north of Hampstead. Site town id 479.
- **The Timberlane Regional School District** (site district id 534) is **SAU 106**. In Sandown: Sandown Central (22775), preschool and kindergarten, and Sandown North Elementary (27910), grades 1–5. Grades 6–8 attend Timberlane Regional Middle and grades 9–12 Timberlane Regional High, both in Plaistow.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 991 (2014-15), 970 (2019-20), 911 (2025-26); cost per pupil FY2025 Timberlane $23,256, state $22,699; 2025 tax rates per $1,000 (Sandown): total $17.80, local school $12.43, municipal $3.56; Question 2: Sandown 74.3% yes, Timberlane adopted it district-wide (about 72%, unofficial); math proficiency 2026: Timberlane 42%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Timberlane's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Timberlane Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Sandown's schools:** the Timberlane Learning Center preschool (P1.1); kindergarten alone at Sandown Central (P1.2); care (P1.3); advanced learners (P4.3); late pickup (P5.2); automatic free meals (P5.3); kindergarten class sizes and screen time (P11.1, P11.2); Sandown Central's size (P19.1); ESL (P17.2).
- **Timberlane:** over a million dollars to outside placements (P7.1); a late bus to Sandown (P10.3); paras and special education staffing (P15.1); the Performing Arts Center (P13.1); AP and dual enrollment (P13.2).
- **Money:** a 2.5% tax cap (P3.2); spending with falling enrollment (P3.3); the four-town formula (P6.2); leaving the district (P6.1, P6.3); a $2 million budget committee cut (P12.1); a $25 million lease-purchase (P12.2); meetings turning into arguments (P8.3); SAU meetings in Plaistow (P20.3).

## Already researched

| File | What it covers |
|---|---|
| `town/timberlane/` (timberlane-high-school.md, timberlane-middle-school-and-student-life.md, timberlane-money-and-governance.md) | Timberlane's middle and high schools, student life, budget, votes and cost formula. |
| `town/Atkinson/`, `town/Plaistow/` | Their elementary schools and their side of Timberlane. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Danville, Lee, Brookline and Henniker (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Timberlane Regional` for Sandown Central, Sandown North and any new district-wide fact.
- `sau 106` for SAU-wide facts.
- `town Sandown` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Sandown/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Danville's research runs at the same time and also uses Timberlane; put only Sandown's own facts and new district-wide facts in these files. Money and the formula belong to agent 4; the middle and high school to agent 3; special education and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Sandown Central, Sandown North and families: the preschool, kindergarten at Sandown Central, care, advanced learners, reading help, late pickup, meals, kindergarten class sizes, screen time, delays, grandparents at pickup, security, the math curriculum, ESL, finding school news, space for growth, security, preschools | `sandown-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.3, P5.1, P5.2, P5.3, P11.1, P11.2, P11.3, P16.1, P16.2, P16.3, P17.2, P17.3, P19.1, P19.2 |
| 2 | Special education, support and choices: outside placements, IEPs at the middle school, out-of-district placements, homeschool access, EFAs, returning to Sandown North, the move to the middle school, bullying and phones, a late bus, staffing of paras and teachers, moving between Timberlane towns | `support-and-choices.md` | `raw/support/` | P7.1, P7.2, P7.3, P9.1, P9.2, P9.3, P10.1, P10.2, P10.3, P15.1, P15.2, P17.1 |
| 3 | Timberlane Middle and High from Sandown: welding and electrical, the bus to a career center, shop classes, comparisons with Massachusetts schools, the bus ride to Plaistow, the Performing Arts Center, AP and dual enrollment, counselors, readiness after graduation, alternatives to regular high school, young people leaving, sports and booster costs | `middle-and-high-school.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.1, P4.2, P13.1, P13.2, P13.3, P14.1, P14.2, P14.3, P18.1, P18.2 |
| 4 | Money and governance from Sandown: Sandown's tax bill, the tax cap, spending and enrollment, the four-town formula, leaving the district, voting without children, home values, meetings, budget committee cuts, the lease-purchase, per-pupil cost, mid-year freezes, facility costs, district stability, the school share of taxes, default and proposed budgets, SAU meetings in Plaistow | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.1, P6.2, P6.3, P8.1, P8.2, P8.3, P12.1, P12.2, P12.3, P15.3, P18.3, P19.3, P20.1, P20.2, P20.3 |
