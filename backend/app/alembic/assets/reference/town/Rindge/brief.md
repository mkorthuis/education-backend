# Rindge Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Rindge and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Rindge/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Rindge

- **Rindge** is a town in Cheshire County on the Massachusetts border, home of Franklin Pierce University and Lake Monomonac. Site town id 459.
- **The Jaffrey-Rindge Cooperative School District** (site district id 274) is **SAU 47**, for Jaffrey and Rindge. Its schools: Rindge Memorial (22320) in Rindge; Jaffrey Grade School (22275); Conant Middle High (22280 middle, 22265 high) in Jaffrey. Check Rindge Memorial's grades.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 688 (2014-15), 679 (2019-20), 594 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Rindge Memorial 323, Jaffrey Grade 250, Conant middle 240, Conant high 336; cost per pupil FY2025 Jaffrey-Rindge $23,397, state $22,699; 2025 tax rates per $1,000 (Rindge): total $13.79, local school $8.36, municipal $2.44; Question 2: Rindge 66.5% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Jaffrey-Rindge's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Jaffrey-Rindge Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Rindge Memorial:** the pre-K lottery (P1.1); bus times (P1.2); class sizes near 17 (P1.3); care in town (P4.2); scores near 41% and 42% (P10.1); reading help (P13.2); a district preschool mid-year (P20.3); Franklin Pierce student teachers (P20.2).
- **Support:** an unfilled K–2 special education position and one psychologist (P2.1, P15.2); para pay of $17 an hour (P2.2, P11.1); homeschool paperwork with SAU 47 (P7.3; repealed July 1, 2026); Massachusetts schools (P18.2).
- **Conant:** early buses to Jaffrey (P4.1); the 2025 award against low math proficiency (P5.1); CTE and trades (P6.1, P6.2); a late bus (P19.2); sports cuts (P19.1).
- **Money:** Rindge's share (P3.1, P12.3); 83% of special education on local taxes (P3.2); the default budget (P3.3); the Little Orioles center (P8.2); enrollment (P8.3); charter school costs (P12.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Jaffrey/` (jaffrey-grade-school-and-families.md, support-and-choices.md, conant-and-cte.md, money-and-governance.md) | The cooperative's schools, policies, open enrollment, Conant, career programs, the budget, the Jaffrey–Rindge cost split and votes. |
| `town/Keene/`, `town/Swanzey/` | The Cheshire Career Center and nearby districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newton, Rindge, Boscawen, Barnstead and Northfield (this wave); Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (running). Don't write facts about those towns.

## Where facts go

- `district Jaffrey-Rindge Cooperative` for Rindge Memorial and any new district-wide fact.
- `sau 47` for SAU-wide facts.
- `town Rindge` for town government, recreation, taxes and community programs.
- No place for general NH rules.

All agents write in `town/Rindge/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the middle and high school and career programs to agent 3; support and choices to agent 2; the elementary school and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Rindge Memorial and young families: the pre-K lottery, bus times, class sizes, care in town, delays, meals, bus changes, fee help, scores, communication apps, reading help, guardianship papers, summer programs, absences, residency, child care waitlists, Franklin Pierce student teachers, preschool mid-year | `rindge-memorial-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.2, P4.3, P9.1, P9.2, P9.3, P10.1, P10.3, P13.2, P14.1, P14.3, P17.3, P18.1, P20.1, P20.2, P20.3 |
| 2 | Support and choices: special education staffing, paras, out-of-district placements, EFAs and homeschool access, the move to the middle school, bullying and phones, sensory breaks and counselors, private schools such as Hampshire Country School, the psychologist's wait, vouchers, security, military families, Massachusetts schools | `support-and-choices.md` | `raw/support/` | P2.1, P2.2, P2.3, P7.1, P7.2, P7.3, P13.1, P13.3, P14.2, P15.1, P15.2, P15.3, P17.1, P17.2, P18.2 |
| 3 | Conant Middle High and career programs from Rindge: bus times to Jaffrey, the award and math results, AP and dual enrollment, library and elective cuts, CTE and trades, apprenticeships, math readiness, STEM clubs, job readiness, career counseling, young people leaving, graduation and college outcomes, sports cuts, the late bus, eligibility | `conant-from-rindge.md` | `raw/high/` | P4.1, P5.1, P5.2, P5.3, P6.1, P6.2, P6.3, P10.2, P12.1, P16.2, P16.3, P18.3, P19.1, P19.2, P19.3 |
| 4 | Money and governance: Rindge's share of the school tax, special education costs, the default budget, the budget breakdown, the Little Orioles center, enrollment, staff turnover and pay, cuts, public comment, charter school costs, leveling Rindge's share, rents | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P12.2, P12.3, P16.1 |
