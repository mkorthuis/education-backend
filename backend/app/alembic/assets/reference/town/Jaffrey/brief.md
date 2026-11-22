# Jaffrey Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Jaffrey and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Jaffrey/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Jaffrey

- **Jaffrey** is a town in Cheshire County at the foot of Mount Monadnock. Site town id 273.
- **The Jaffrey-Rindge Cooperative School District** (site district id 274) is **SAU 47**, for Jaffrey and Rindge. Its schools: Jaffrey Grade School (22275), preschool to grade 5; Rindge Memorial (22320), preschool to grade 5; Conant Middle High (22280 and 22265), grades 6–12.
- **Shared district, first town.** Rindge shares this district and is researched in the next wave; it will cite these files. So cover district-wide facts (the middle and high school, the budget, the cost formula, policies) fully, placed with the district, and keep town-only facts placed with the town.
- **Career and technical education:** the Region 14 Applied Technology Center (check whether it is at ConVal in Peterborough and how Conant students get there). Keene's Cheshire Career Center is researched in `town/Keene/` and `town/Swanzey/`.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 715 (2014-15), 661 (2019-20), 577 (2025-26); cost per pupil FY2025 Jaffrey-Rindge $23,397, state $22,699; 2025 tax rates per $1,000 (Jaffrey): total $18.95, local school $9.35, municipal $6.24; Question 2: Jaffrey 53.0%, the cooperative 60.2% (check whether it passed at 60%, unofficial); math proficiency 2026: Jaffrey-Rindge 34%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Jaffrey-Rindge's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Jaffrey-Rindge Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **JGS:** Little Orioles and pre-K cuts (P1.1); 2nd-grade class sizes (P1.2); care (P1.3); paras (P4.2); speech and reading minutes (P4.3); a preschool lottery (P7.1); full-day kindergarten (P7.3); combined bus routes (P11.1); remote days (P11.2); a 17-to-1 ratio (P13.3); ESL (P16.1).
- **Conant:** sports cuts and user fees (P3.1, P3.2); Region 14 and a CTE wing (P5.1, P5.2); about 30% proficient (P6.1); AP and honors (P6.2); Running Start (P10.1); elective, library and arts cuts (P10.2, P10.3, P19.1–P19.3); 6th graders apart from high schoolers (P14.1).
- **Support and money:** one school psychologist (P4.1); open enrollment (P15.2); half the tax bill to schools (P2.1); Jaffrey's share against Rindge's (P2.2); the default budget again (P2.3, P18.3); central office costs (P12.2); teacher pay and turnover (P13.1, P13.2); state mandates and special education aid (P20.1, P20.3).
- **Home education:** an annual portfolio review with SAU 47 (P9.3; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Keene/`, `town/Swanzey/` | Neighboring districts and the Cheshire Career Center, for comparisons. |
| Peterborough's research (later in this batch) | ConVal, which may host Region 14. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Kingston, Loudon, Alton and Tilton (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Jaffrey-Rindge Cooperative` for all its schools, policies, budget and board.
- `sau 47` for SAU-wide facts.
- `district Contoocook Valley` only for Region 14 center facts, if it is at ConVal.
- `town Jaffrey` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Jaffrey/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; Conant and CTE to agent 3; support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Jaffrey Grade School and families: Little Orioles and pre-K, class sizes, care, paras, speech and reading minutes, the preschool lottery and alternatives, kindergarten, meals, portal help, reading help, bus routes, remote days, notices, class-size ratios, ESL, translation, reading progress | `jaffrey-grade-school-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.2, P4.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P13.3, P16.1, P16.2, P16.3 |
| 2 | Support and choices: school psychologist waits, homeschool access, EFAs, home education paperwork, 6th graders in a 6–12 building, phones and bullying, the move to Conant, security, open enrollment, panic attacks and counseling, flexible and online schedules, 504 plans moving with a student | `support-and-choices.md` | `raw/support/` | P4.1, P9.1, P9.2, P9.3, P14.1, P14.2, P14.3, P15.1, P15.2, P17.1, P17.2, P17.3 |
| 3 | Conant Middle High and CTE: sports cuts and user fees, Region 14 admission, a CTE wing, certifications, scores, AP and honors, high school classes for middle schoolers, Running Start, library and elective cuts, work readiness, business partners, comparisons with nearby schools, band, chorus, art, clubs and drama | `conant-and-cte.md` | `raw/high/` | P3.1, P3.2, P5.1, P5.2, P5.3, P6.1, P6.2, P6.3, P10.1, P10.2, P10.3, P12.1, P12.3, P15.3, P19.1, P19.2, P19.3 |
| 4 | Money and governance: the school share of taxes, Jaffrey's share against Rindge's, the default budget, why athletics gets cut first, central office costs, teacher pay and turnover, budgets voted down, home values, state mandates, a plain breakdown, special education aid | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P3.3, P12.2, P13.1, P13.2, P18.1, P18.2, P18.3, P20.1, P20.2, P20.3 |
