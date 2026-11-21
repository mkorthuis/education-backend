# Franklin Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Franklin and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Franklin/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Franklin

- **Franklin** is a small city in Merrimack County where the Pemigewasset and Winnipesaukee rivers form the Merrimack, north of Concord. Site town id 185.
- **The Franklin School District** (site district id 185) is **SAU 18**, a one-district SAU. Its schools: Paul A. Smith (20650), preschool to grade 4; Franklin Middle (26755), grades 5–8; Franklin High (20660), grades 9–12. The city council sets the school budget under the city's tax cap (check how).
- **Career and technical education:** the Huot Technical Center at Laconia High School, researched in `town/Laconia/high-school-and-huot.md` (programs, admission, sending schools, transport). Write this town's side.
- **Starting pages:** SAU 18, https://www.sau18.org (check); the city, https://www.franklinnh.org (check).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,186 (2014-15), 1,022 (2019-20), 896 (2025-26); cost per pupil FY2025 Franklin $23,098, state $22,699; 2025 tax rates per $1,000: total $17.63, local school $5.01, municipal $9.42; Question 2: Franklin 62.5% (check whether it applies to a city district); math proficiency 2026: Franklin 13%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Franklin's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Franklin)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** after-school care at Paul Smith (P1.1); free full-day pre-K (P4.1); drop-off before a 7:00 shift (P11.3); free meals for everyone (P11.2); the reading curriculum (P16.1); nurses and speech therapists (P14.3); AP and honors at FHS (P2.3); Huot in 9th or 10th grade (P6.2); free LRCC courses and how many (P10.1, P18.1); college-going (P18.2); graduation rates (P20.2); Franklin Continuing Education (P19.1–P19.3).
- **Money:** very low scores (P2.1); families leaving for Winnisquam or private schools (P2.2); taxes and the budget with falling enrollment (P3.1, P3.2, P20.1); buildings (P3.3); a federal safety and mental health grant pulled (P9.2); the city and school board's budget fights (P9.3); teacher and principal turnover (P13.1); merging or sharing services (P13.3).
- **Choices:** EFAs, homeschooling and returning for 9th grade (P12.1–P12.3); Tilton School (P18.3); backup options (P5.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Laconia/high-school-and-huot.md` | The Huot Center's programs, admission and sending schools. |
| `town/Concord/` | Concord's schools, for comparisons (P5.1). Bow's research runs now. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Belmont, Gilford, Meredith and Plymouth (this wave), and Pembroke, Weare, Barrington, Farmington and Somersworth (running or queued). Don't write facts about those towns.

## Where facts go

- `district Franklin` for SAU 18, its three schools, the preschool, policies, staff, budget and board.
- `district Tilton School` for Tilton School's own facts.
- `district Winnisquam Regional` only for its own side of any transfer.
- `district Laconia` only for a Huot fact that Laconia's files lack.
- `town Franklin` for city government, the tax cap and recreation.
- No place for general NH rules.

All agents write in `town/Franklin/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, the tax cap and governance belong to agent 4; Franklin High, Huot and adult education to agent 3; Franklin Middle and support to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Paul Smith and families: after-school care, reading help, late buses, pre-K, kindergarten registration and shots, welcoming new students, after-school activities, the calendar and alerts, volunteering, English learners, meals, early drop-off, daycares, nurses and speech, the reading curriculum, substitutes and volunteers | `paul-smith-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P14.1, P14.2, P14.3, P16.1, P16.3 |
| 2 | Franklin Middle and support: climate and bullying, IEPs for ADHD and anxiety, who to call, counselors, homeschoolers in sports, EFAs, returning for 9th grade, grades and the portal, attendance, summer school, enrollment without a birth certificate, math testing, food help, class sizes | `middle-school-and-support.md` | `raw/middle/` | P5.2, P7.1, P7.2, P7.3, P12.1, P12.2, P12.3, P15.1, P15.2, P15.3, P16.2, P17.1, P17.2, P17.3 |
| 3 | Franklin High, Huot and adult education: AP and honors, Huot admission, buses and programs, competency grading, work skills, LRCC courses and transfer, sports with college classes, dual enrollment, college-going, Tilton School, Continuing Education costs and links to LRCC and apprenticeships, graduation rates, what's working | `franklin-high-and-pathways.md` | `raw/high/` | P2.3, P6.1, P6.2, P6.3, P9.1, P10.1, P10.2, P10.3, P18.1, P18.2, P18.3, P19.1, P19.2, P19.3, P20.2, P20.3 |
| 4 | Money and governance: scores, families leaving, the tax share, the budget and enrollment, buildings, buying in Franklin, backup options, the federal grant, the city's tax cap and budget process, turnover, speaking at meetings, sharing services, spending and taxes | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P3.1, P3.2, P3.3, P5.1, P5.3, P9.2, P9.3, P13.1, P13.2, P13.3, P20.1 |
