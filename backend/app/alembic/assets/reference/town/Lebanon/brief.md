# Lebanon Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Lebanon and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Lebanon/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Lebanon

- **Lebanon** is a city in Grafton County on the Connecticut River, with West Lebanon, home of Dartmouth Health's medical center (DHMC). Site town id 295.
- **The Lebanon School District** (site district id 295) is **SAU 88**, a one-district SAU. Its schools: Mount Lebanon (21355), preschool to grade 4, in West Lebanon; Hanover Street (21335), K–4; Lebanon Middle (21370), grades 5–8; Lebanon High (21360), grades 9–12. Check the elementary zones (P3.1, P18.1).
- **Tuition:** Plainfield (site district id 441, grades 9–12), Grantham (211, grades 7–12), Lyme (327), Croydon and Cornish have contracts with Lebanon (`places.yaml`).
- **Career and technical education:** check where Lebanon High students take career programs (the Hartford Area Career and Technology Center in White River Junction, Vermont, is likely; P2.1–P2.3).
- **Choices:** Ledyard Charter School (site district id 719).
- **Starting pages:** SAU 88, https://www.sau88.net (check); the city, https://lebanonnh.gov (check); River Valley Community College.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,389 (2014-15), 1,330 (2019-20), 1,335 (2025-26); cost per pupil FY2025 Lebanon $29,144, state $22,699; 2025 tax rates per $1,000: total $21.53, local school $11.16, municipal $8.10; Question 2: Lebanon 45.4%, so no state-law cap (unofficial; check any city charter cap, P4.2); math proficiency 2026: Lebanon 59%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Lebanon's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Lebanon)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** the preschool at Mount Lebanon (P1.1, P14.3); drop-off by 7:00 for hospital shifts (P1.2); snow days for hospital staff (P1.3); zones (P3.1, P18.1); math enrichment (P3.2); after-school care until 5:30 (P5.2); West Lebanon buses (P5.3); free full-day kindergarten (P10.3); the reading program and dyslexia screening (P17.1, P17.2); 5th grade at the middle school (P5.1, P12.1).
- **High school:** the Hartford career center and its fees (P2.1–P2.3); RVCC courses (P6.2, P8.1, P16.1); Ledyard students at LHS sports and prom (P13.2); pay-to-play (P15.3); adult education (P16.3).
- **Money:** a 2026 rate of $22.16 (P4.1); a tax cap (P4.2, P15.2); budget and enrollment (P4.3); Plainfield's and Grantham's students (P14.2); building projects and bonds (P18.2, P20.2); central office costs (P20.1).

## Already researched

| File | What it covers |
|---|---|
| Hanover's research (this wave) | The neighboring Dresden district and Vermont career centers. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Berlin, Claremont, Hanover and Swanzey (this wave), and Belmont, Gilford, Meredith, Franklin and Plymouth (queued). Don't write facts about those towns.

## Where facts go

- `district Lebanon` for SAU 88, its schools, the preschool, policies, staff, budget, board and tuition contracts.
- `district Ledyard Charter School` for its own facts.
- `district Plainfield` and `district Grantham` only for their own sides of the contracts.
- `town Lebanon` for city government, the tax rate and any city tax cap.
- No place for general NH rules.

All agents write in `town/Lebanon/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, the tax cap, buildings and governance belong to agent 4; Lebanon High, career programs and college courses to agent 3; the middle school, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Mount Lebanon, Hanover Street and families: the preschool and its waitlist, drop-off times, snow days, zones, math enrichment, after-school care, West Lebanon buses, English learners, translation, meals, kindergarten, 4th-grade clubs, homework, the reading program, dyslexia screening, classroom visits | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.2, P5.2, P5.3, P7.1, P7.2, P7.3, P10.3, P12.2, P12.3, P14.3, P17.1, P17.2, P17.3 |
| 2 | Lebanon Middle, support and choices: the 5th-grade move, foster children's evaluations, paras, outside specialists, homeschool paperwork and returning, counselors and social workers, phones, quiet breaks, Ledyard Charter and its students in LHS activities, Chromebook help, bullying, Wi-Fi, diversity | `middle-support-and-choices.md` | `raw/middle/` | P5.1, P9.1, P9.2, P9.3, P10.1, P10.2, P11.1, P11.2, P11.3, P12.1, P13.1, P13.2, P13.3, P19.1, P19.2, P19.3 |
| 3 | Lebanon High and pathways: the Hartford career center, graduating with a half-day program, CTE fees, AP and honors, RVCC courses, college outcomes, alternatives for struggling students, FAFSA and trades counseling, test scores, pay-to-play, adult education and GED, the high school's reputation | `high-school-and-pathways.md` | `raw/high/` | P2.1, P2.2, P2.3, P6.1, P6.2, P6.3, P8.1, P8.2, P8.3, P15.1, P15.3, P16.1, P16.3, P18.3 |
| 4 | Money and governance: class sizes against other towns, the tax rate, a tax cap, budget and enrollment, buying in Lebanon, tuition students, cuts under a cap, renters, zones for new families, building projects, central office costs, buildings, speaking on the budget | `money-and-governance.md` | `raw/money/` | P3.3, P4.1, P4.2, P4.3, P14.1, P14.2, P15.2, P16.2, P18.1, P18.2, P20.1, P20.2, P20.3 |
