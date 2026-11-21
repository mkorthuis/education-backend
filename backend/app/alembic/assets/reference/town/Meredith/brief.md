# Meredith Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Meredith and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Meredith/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Meredith

- **Meredith** is a town in Belknap County on Lake Winnipesaukee and Lake Waukewan, with many seasonal homes. Site town id 347.
- **The Inter-Lakes Cooperative School District** (site district id 269) serves Meredith, Center Harbor and Sandwich, and is in **SAU 2** (which also serves Ashland). Its schools: Inter-Lakes Elementary (29200), preschool to grade 6; Sandwich Central (20040), K–6; Inter-Lakes Middle (29201), grades 7–8 in the site's data (check whether the middle tier now starts earlier, P12.2); Inter-Lakes High (20035), grades 9–12.
- **Career and technical education:** the Huot Technical Center at Laconia High School, researched in `town/Laconia/high-school-and-huot.md` (programs, admission, sending schools, transport). Write this town's side.
- **Starting pages:** SAU 2, https://www.interlakes.org (check); the town, https://www.meredithnh.gov (check).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 797 (2014-15), 743 (2019-20), 621 (2025-26); cost per pupil FY2025 Inter-Lakes $33,271, state $22,699; 2025 tax rates per $1,000: total $10.62, local school $4.95, municipal $3.44, equalization ratio 77%; Question 2: Inter-Lakes 57.7%, so no cap (unofficial); math proficiency 2026: Inter-Lakes 44%, state 44%.
- **Shared district:** Center Harbor and Sandwich have no research. Facts about Inter-Lakes serve all three towns; write them with `district Inter-Lakes Cooperative`.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Inter-Lakes' kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Inter-Lakes Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** pre-K half or full day (P1.1); a 7-Upps waitlist (P1.2); drop-off before 7:30 (P7.3); a 5th grader moving to the middle/high school (P12.2); the reading program (P13.1); phones (P8.1); hockey and lacrosse (P8.2); competencies (P8.3); LRCC courses (P6.2); boat building and diesel (P2.2); about 45% in math (P15.1); a late bus (P17.3); field lights for middle schoolers (P20.1).
- **Support:** two paraeducators and an inclusion specialist cut (P5.1, P19.1); an SRO at the Laker Lane campus (P14.2); grandparents in the parent portal (P14.3).
- **Money:** Meredith paying over 70% (P3.1); a budget up with under 1,000 students (P3.2); robotics camp teachers cut (P2.3); $359,000 for field lights (P6.3); "Meredith Bay" addresses (P4.3); a lake house taxed the same (P10.1); sending money to the state (P10.2); a 10-to-1 ratio (P15.2); votes on a Wednesday (P16.3).
- **Home education:** a "yearly homeschool portfolio or evaluation" sent to SAU 2 (P11.3; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Laconia/high-school-and-huot.md` | The Huot Center's programs, admission and sending schools. |
| `town/Laconia/` | Laconia's schools, for moves and comparisons (P9.3, P4.3). Gilford's research runs in this wave. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Belmont, Gilford, Franklin and Plymouth (this wave), and Pembroke, Weare, Barrington, Farmington and Somersworth (running or queued). Don't write facts about those towns.

## Where facts go

- `district Inter-Lakes Cooperative` for the district, its schools, the preschool, policies, staff, budget and board.
- `sau 2` for SAU-wide facts (SAU 2 also serves Ashland).
- `district Laconia` only for a Huot fact that Laconia's files lack.
- `town Meredith` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Meredith/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, the cost formula and governance belong to agent 4; the middle and high school to agent 2; support, special education and choices to agent 3. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Inter-Lakes Elementary and families: pre-K, after-school care, nurses and medication, snow days, kindergarten, class sizes, early drop-off, preschool costs, buses into apartment complexes, the calendar, meals, the reading program, enrichment, early buses on back roads, ice-storm notices, Sandwich Central | `inter-lakes-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.3, P7.1, P7.2, P7.3, P9.1, P9.2, P12.1, P12.3, P13.1, P13.3, P17.1, P17.2, P18.3 |
| 2 | Inter-Lakes Middle and High: Huot access, boat building and diesel, test scores, AP and honors, business and math, LRCC courses, phones, hockey and lacrosse, competency grading, the move to the middle school, math results against private schools, adult education, late buses, where seniors go, field lights, physicals and concussion baselines, eligibility | `middle-and-high-school.md` | `raw/high/` | P2.1, P2.2, P4.1, P4.2, P6.1, P6.2, P8.1, P8.2, P8.3, P12.2, P15.1, P16.2, P17.3, P18.2, P20.1, P20.2, P20.3 |
| 3 | Support, choices and safety: paraeducator and inclusion cuts, IEP contacts at SAU 2, moving to Laconia mid-year, homeschoolers in sports, EFAs, home education paperwork, teacher planning time and paras, anxiety and crowds, an SRO, grandparents in the portal, returning from private school, training after the inclusion cut, speech and OT, 504 summer support | `support-choices-and-safety.md` | `raw/support/` | P5.1, P5.2, P9.3, P11.1, P11.2, P11.3, P13.2, P14.1, P14.2, P14.3, P15.3, P19.1, P19.2, P19.3 |
| 4 | Money and governance: the robotics camp cut, Meredith's share of the bill, the budget and enrollment, property values, Meredith Bay addresses, the field lights, lake houses and part-time residents, the state education tax, the staffing ratio, rents, the voting day, home buyers from Massachusetts | `money-and-governance.md` | `raw/money/` | P2.3, P3.1, P3.2, P3.3, P4.3, P6.3, P10.1, P10.2, P10.3, P15.2, P16.1, P16.3, P18.1 |
