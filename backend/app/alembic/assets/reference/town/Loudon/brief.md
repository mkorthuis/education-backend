# Loudon Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Loudon and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Loudon/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Loudon

- **Loudon** is a town in Merrimack County east of Concord, home of New Hampshire Motor Speedway. Site town id 321.
- **The Merrimack Valley School District** (site district id 352) is **SAU 46**, for Boscawen, Loudon, Penacook (Concord), Salisbury and Webster. Its schools: Loudon Elementary (22180), K–5; Boscawen (22155), Penacook (22185), Salisbury (22200) and Webster (22205) elementaries; Merrimack Valley Middle (26585), grades 6–8; Merrimack Valley High (22195), grades 9–12. Check the preschool.
- **Shared district, first town.** Boscawen shares this district and is researched in the next wave; it will cite these files. So cover district-wide facts (the middle and high school, the budget, the cost formula, policies) fully, placed with the district, and keep town-only facts placed with the town.
- **Career and technical education:** check where MVHS students take career programs (the Concord Regional Technical Center, researched in `town/Concord/high-school-and-pathways.md`, is likely).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 779 (2014-15), 684 (2019-20), 593 (2025-26); cost per pupil FY2025 Merrimack Valley $19,767, state $22,699; 2025 tax rates per $1,000 (Loudon): total $22.75, local school $14.06, municipal $4.46; Question 2: Loudon 70.0%, Merrimack Valley adopted it (63.0%, unofficial); math proficiency 2026: Merrimack Valley 41%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Merrimack Valley's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Merrimack Valley)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **LES:** a 9:00 start (P1.1, P12.1); kindergarten class sizes (P1.2); scores (P5.1); gifted programs (P5.2); paras (P7.1); bus changes (P12.2); library funding (P13.3); public pre-K (P15.1); combined classes (P17.2).
- **Middle and high school:** welding and auto (P2.1); internships (P2.2); a late bus to Loudon (P4.2); long bus rides (P8.1); a bell-to-bell phone ban (P8.2); AP and NHTI (P5.3); pushing four-year college (P10.1); financial aid help (P11.1); parking and traffic (P11.3); the Learning Center (P19.3).
- **Money:** Loudon's school tax (P3.1); the five-town split (P3.2, P20.3); closing a small elementary (P3.3); ESSER money (P14.2); out-of-district costs (P14.3); bus drivers (P16.1); senior tax relief (P16.3); race weekends (P19.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Concord/` | The Concord Regional Technical Center and Concord's schools, for comparisons. |
| `town/Pembroke/` | A neighboring district, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Kingston, Jaffrey, Alton and Tilton (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Merrimack Valley` for all its schools, policies, budget and board.
- `sau 46` for SAU-wide facts.
- `town Loudon` for town government, recreation, taxes and the Speedway.
- No place for general NH rules.

All agents write in `town/Loudon/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school to agent 3; support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Loudon Elementary and families: the 9:00 start and care, kindergarten size and registration, meals, scores, gifted programs, paras, its reputation, bus changes, snow notices, the library and reading, pre-K, security, after-school programs, combined classes, reading help, summer programs | `loudon-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.3, P5.1, P5.2, P7.1, P9.1, P12.1, P12.2, P13.2, P13.3, P15.1, P15.2, P15.3, P17.2, P18.1, P18.3 |
| 2 | Support and choices: EFAs, returning to LES, state aid when families leave, IEPs into the middle school, who to call at SAU 46, long bus rides, the phone ban, charter schools, diversity and inclusion, counseling, moving within the district, the Learning Center | `support-and-choices.md` | `raw/support/` | P6.1, P6.2, P6.3, P7.2, P7.3, P8.1, P8.2, P9.2, P13.1, P16.2, P18.2, P19.3 |
| 3 | Merrimack Valley Middle and High: welding and auto, internships, trades spending, the move from LES, late buses, AP and NHTI, tutoring, four-year college or not, work readiness, financial aid help, Loudon graduates' outcomes, activity costs, science curriculum, graduation and readiness | `middle-and-high-school.md` | `raw/high/` | P2.1, P2.2, P2.3, P4.1, P4.2, P5.3, P8.3, P10.1, P10.2, P11.1, P11.2, P12.3, P17.3, P19.1 |
| 4 | Money and governance: Loudon's school tax, the five-town split, closing a small elementary, taxes and enrollment, budget hearings in Penacook, parking and traffic, spending per student, ESSER money, out-of-district costs, bus drivers, senior tax relief, teacher turnover, race weekends, communication, volunteers, Loudon's voice | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P9.3, P10.3, P11.3, P14.1, P14.2, P14.3, P16.1, P16.3, P17.1, P19.2, P20.1, P20.2, P20.3 |
