# Stratham Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Stratham and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Stratham/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Stratham

- **Stratham** is a town in Rockingham County between Exeter, Greenland and North Hampton, along Routes 33, 108 and 101, with Stratham Hill Park. Site town id 511.
- **Two school districts serve Stratham, both in SAU 16:** the Stratham School District (site district id 511): Stratham Memorial School (20615), preschool to grade 5; and the **Exeter Region Cooperative** (site district id 172): Cooperative Middle School (20590, grades 6–8, in Stratham) and Exeter High School (20600), with SST.
- **The cooperative, SAU 16 and SST are already researched** in `town/Exeter/` (see below). Read those files first and write only Stratham's side: Stratham Memorial, Stratham's share and votes, Stratham's buses and students.
- **Starting pages:** SAU 16, https://www.sau16.org (Stratham Memorial, the boards, budgets, policies); the town, https://www.strathamnh.gov (tax rate, assessing, exemptions).
- **Site figures:** resident students 1,320 (2014-15), 1,252 (2019-20), 991 (2026-27); cost per pupil FY2025 Stratham $29,303 (K–5), the cooperative $24,141, state $22,699; 2025 tax rates per $1,000: total $13.52, local school $9.72, municipal $2.15; Question 2: Stratham 47.8% yes and the cooperative 48.6%, so neither cap is adopted (unofficial); math proficiency 2026: Stratham 71%, the cooperative 53%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Stratham's kindergarten cutoff, registration, preschool and SB2 facts, and the cooperative's. Read them: `grep -n -B2 -A10 -E "place: district (Stratham|Exeter Region Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Stratham Memorial:** an 8:25 to 3:05 day and care (P1.1); First Student buses late or combined (P1.2); the Infinite Campus portal (P1.3, P7.3); a new special services wing (P3.1); a summer 2027 window and flooring work left (P4.1); Responsive Classroom (P4.3); a 500-student school (P6.1); capacity (P15.3); public preschool for 3- and 4-year-olds (P19.1).
- **The cooperative for Stratham students:** a 7:25 start at CMS and the Stratham bus time (P6.2); the late bus to Stratham (P7.1); a vaping parent night (P7.2); math placement into EHS (P8.1); Canvas observer accounts (P9.1); SST's new Electrical Technologies (P10.1); tryouts with six towns (P12.1). Exeter's files answer much of this; add Stratham's side.
- **Money:** a 2026 tax rate of $14.50 and an $11.96 million bond for Stratham Memorial (P13.1); leftover bond money spent on windows and flooring (P13.2); the split between Stratham and the cooperative (P13.3); HB 1300 (P14.2); two budget votes (P14.3); SAU 16 central office costs for Stratham (P20.1); state aid (P20.2); which board controls what (P20.3).
- **Home education:** "paperwork each year" (P16.1; the yearly evaluation was repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Exeter/cms-sst-and-getting-to-school.md` | Cooperative Middle School (electives, the late buses at 4:10–4:15, the move from the elementary schools, mixing across towns, phones, vaping, bullying, substitutes), home education policies, and SST (programs including Electrical Technologies, sessions, credits, certifications, enrollment by sending school). |
| `town/Exeter/exeter-high-school.md` | Exeter High: AP and honors, the Commons, counselors (about 193 students each), the 7:30 start, relearning, extended learning, Infinite Campus portals for two households, clubs. |
| `town/Exeter/money-governance-and-community.md` | The cooperative's budget and each town's share (table `ercsd_town_shares_2025`), the FY2027 increase by town, open enrollment, SAU 16 community programs. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Epping, Newmarket, Raymond and Durham (this wave), and from the first wave Atkinson, Plaistow (shared `town/timberlane/`), Hampstead, Pelham and Seabrook. Don't write facts about those towns.

## Where facts go

- `district Stratham` for the Stratham School District, Stratham Memorial, its preschool, budget and board.
- `district Exeter Region Cooperative` for a cooperative fact Exeter's files lack (say so in "For another file").
- `sau 16` for SAU-wide facts.
- `town Stratham` for town government and services.
- No place for general NH rules.

All agents write in `town/Stratham/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Stratham Memorial belongs to agent 1, the cooperative's schools for Stratham students to agents 2 and 3, money and governance to agent 4. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Stratham Memorial and families: care, buses, the portal, curriculum, school updates, special services and reading help, IEP contacts at SAU 16, biking, Responsive Classroom, meals and quiet help, missed bus stops, paper notices, homework help and check-ins, bus changes, preschool, kindergarten cutoff and registration | `stratham-memorial-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.3, P3.1, P3.2, P3.3, P4.2, P4.3, P5.1, P5.2, P5.3, P18.1, P18.2, P18.3, P19.1, P19.3 |
| 2 | Cooperative Middle School for Stratham students: preparation for the six-town school, the move to 6th grade, the start time and Stratham buses, mixing, the late bus, vaping and phones, missing assignments, math placement into EHS, career prep, counselors, home education and activities | `cms-for-stratham.md` | `raw/middle/` | P2.2, P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P16.1, P16.2, P16.3 |
| 3 | Exeter High and SST for Stratham students: Canvas, freshman classes, calling out, SST and Electrical, sports at EHS, apprenticeships, counselors, dual enrollment, AP and college results against Portsmouth and Winnacunnet, tryouts, eligibility, booster costs, internships, the calendar for employers, workplace skills | `exeter-high-and-sst-for-stratham.md` | `raw/high/` | P9.1, P9.2, P9.3, P10.1, P10.2, P10.3, P11.1, P11.2, P11.3, P12.1, P12.2, P12.3, P17.1, P17.2, P17.3 |
| 4 | Money and governance: the SMS renovation and bond, leftover bond money, the tax split, senior exemptions, HB 1300, two budgets, schools and property values, public or private, capacity, renters' access, SAU 16 central office costs, state aid, which board decides | `money-and-governance.md` | `raw/money/` | P4.1, P13.1, P13.2, P13.3, P14.1, P14.2, P14.3, P15.1, P15.2, P15.3, P19.2, P20.1, P20.2, P20.3 |
