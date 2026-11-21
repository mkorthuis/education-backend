# Swanzey Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Swanzey and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Swanzey/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Swanzey

- **Swanzey** is a town in Cheshire County just south of Keene, with the villages of West Swanzey, East Swanzey and Westport. Site town id 523.
- **The Monadnock Regional School District** (site district id 363) is **SAU 93**, a one-district SAU for six towns. Its schools: Mount Caesar (21695), preschool to grade 6, in Swanzey; Emerson (21665, Fitzwilliam), Troy Elementary (21725) and Gilsum STEAM Academy (21670); Monadnock Regional Middle (26980), grades 7–8, and High (21700), grades 9–12, in Swanzey. Check Cutler's closing and where 6th graders go (P1.1, P19.1).
- **Tuition:** Winchester (site district id 573) sends grades 9–12 to Monadnock (`places.yaml`).
- **Career and technical education:** the Cheshire Career Center at Keene High, researched in `town/Keene/middle-high-and-career-center.md`. Write Monadnock's side.
- **Starting pages:** the district, https://www.mrsd.org (check); the town, https://www.town.swanzey.nh.us (check).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 907 (2014-15), 847 (2019-20), 887 (2025-26); cost per pupil FY2025 Monadnock $21,795, state $22,699; 2025 tax rates per $1,000: total $20.18, local school $11.03, municipal $5.62; Question 2: Monadnock 61.2%, so the cap is adopted (unofficial); math proficiency 2026: Monadnock 33%, state 44%.
- **Shared district:** the other five towns have no research. Facts about Monadnock serve all six; write them with `district Monadnock Regional`.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Monadnock's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Monadnock Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** Cutler closed and West Swanzey merged into Mount Caesar (P1.1, P1.2, P15.2); renovations (P14.2); 6th graders at Mount Caesar (P19.1); after-school care (P4.1); First Student delays (P4.2); public preschool (P5.1); a late-September birthday (P5.3); Spanish and ESL (P10.1, P10.2).
- **Middle and high school:** CTE at Keene (P2.1, P2.2, P12.1); Running Start at Keene State (P6.2); low scores (P6.3); locked bathrooms (P12.2); very early start times (P13.1); vaping (P13.2); phones (P13.3); middle school teams (P19.2); athletic trainers and fees (P19.3).
- **Money:** the Cutler building (P1.3); taxes after Cutler (P3.2); a tax cap's cuts (P3.3); $11 per $1,000 (P8.1); the six-town formula (P8.3); contract staff (P7.1); aides and bus drivers (P15.1); the deliberative session (P17.1); the default budget rising (P17.2).
- **Home education:** "submit to the SAU 93 office each year" (P9.2; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Keene/middle-high-and-career-center.md` | The Cheshire Career Center: programs, admission, sending schools, schedule. |
| `town/Keene/choices-and-adult-learning.md` and other Keene files | Keene's private schools, adult education and recreation (P14.3, P18.3, P16.3). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Berlin, Claremont, Lebanon and Hanover (this wave), and Belmont, Gilford, Meredith, Franklin and Plymouth (queued). Don't write facts about those towns.

## Where facts go

- `district Monadnock Regional` for SAU 93, its schools, the preschool, policies, staff, budget, board and the Winchester contract.
- `district Keene` only for a Cheshire Career Center fact that Keene's files lack.
- `town Swanzey` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Swanzey/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, the cost formula, buildings and governance belong to agent 4; the high school's academics and CTE to agent 2; support, daily life and choices at the middle and high school to agent 3. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Mount Caesar and families: Cutler's closing and class sizes, after-school care, late buses, preschool, kindergarten registration and the cutoff, Spanish and ESL, meals, guardianship papers, counselors, the renovations, a crowded building, early drop-off, delays, summer camps in Keene, 6th graders' placement | `mount-caesar-and-families.md` | `raw/elementary/` | P1.1, P1.2, P4.1, P4.2, P5.1, P5.2, P5.3, P10.1, P10.2, P10.3, P11.1, P11.2, P14.2, P15.2, P16.1, P16.2, P16.3, P19.1 |
| 2 | Monadnock Regional High and the career center: welding and carpentry at the Cheshire Career Center, graduating on time, apprenticeships, AP and college prep, Running Start, scores, work habits, switching into a tech program, FAFSA help, credits for a senior, adult education, transferring credits | `high-school-and-career-center.md` | `raw/high/` | P2.1, P2.2, P2.3, P6.1, P6.2, P6.3, P8.2, P12.1, P12.3, P15.3, P18.3, P20.2 |
| 3 | Support, daily life and choices at the middle and high school: grades dropping in 7th grade, contract staff and paras, IEP disagreements, EFAs, homeschool paperwork and co-ops, locked bathrooms, start times, bullying and vaping, phones, private schools in Keene, sports, music and clubs, middle school teams, trainers and fees, foster children's school stability, trauma support | `support-daily-life-and-choices.md` | `raw/support/` | P4.3, P7.1, P7.2, P7.3, P9.1, P9.2, P9.3, P12.2, P13.1, P13.2, P13.3, P14.3, P18.2, P19.2, P19.3, P20.1, P20.3 |
| 4 | Money and governance: the Cutler building, the school share of taxes, taxes after Cutler, a tax cap's cuts, the local school rate, the six-town formula, watching meetings, how a regional district works, aides and bus drivers, the deliberative session, the default budget, the budget breakdown, buying a starter home | `money-and-governance.md` | `raw/money/` | P1.3, P3.1, P3.2, P3.3, P8.1, P8.3, P11.3, P14.1, P15.1, P17.1, P17.2, P17.3, P18.1 |
