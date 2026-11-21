# Gilford Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Gilford and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Gilford/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Gilford

- **Gilford** is a town in Belknap County on Lake Winnipesaukee, east of Laconia, home to Gunstock Mountain. Site town id 191.
- **The Gilford School District** (site district id 191) is **SAU 73**, a one-district SAU. Its schools: Gilford Elementary (21245), K–4; Gilford Middle (26995), grades 5–8; Gilford High (21240), grades 9–12.
- **Gilmanton** sends grades 9–12 to Gilford High under a tuition contract (`places.yaml`). Gilmanton has no research; write the contract from both sides with `district Gilford` (and `district Gilmanton` for Gilmanton's own side, only if found).
- **Career and technical education:** the Huot Technical Center at Laconia High School, researched in `town/Laconia/high-school-and-huot.md` (programs, admission, sending schools, transport). Write this town's side.
- **Starting pages:** the district, https://www.gilfordschools.org (check); the town, https://www.gilfordnh.org; the Gilford Youth Center (Good Morning Club).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,029 (2014-15), 998 (2019-20), 857 (2025-26); cost per pupil FY2025 Gilford $25,908, state $22,699; 2025 tax rates per $1,000: total $11.85, local school $5.61, municipal $4.03; Question 2: Gilford 56.6%, so no cap (unofficial); math proficiency 2026: Gilford 52%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Gilford's kindergarten, registration and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Gilford)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** the Good Morning Club and GES Extended Day (P1.1, P1.2, P9.3); class sizes (P1.3); public pre-K (P9.1); full-day kindergarten and the cutoff (P9.2); lunch prices up (P5.1); Gilford Got Lunch (P5.3); a ski club to Gunstock (P10.2); Algebra 1 in grade 8 (P12.3); Huot programs, buses and college credit (P3.1–P3.3); AP and dual enrollment (P7.2); graduation tickets at the Bank of NH Pavilion (P11.3); co-op teams (P17.1); sports fees (P17.2); instrument rental (P18.2); more counselors (P20.1).
- **Money:** a budget up 2.8% with falling enrollment (P2.1, P15.1); what Gilmanton pays (P2.2); the superintendent retiring and the search (P2.3, P7.3, P15.3); cuts from falling enrollment (P14.2); arts cuts (P18.1); the deliberative session and elections (P19.2).
- **Home education:** "paperwork every year" with SAU 73 (P13.3; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Laconia/high-school-and-huot.md` | The Huot Center's programs, admission and sending schools. |
| `town/Laconia/` | Laconia's schools, for comparisons (P14.1). Meredith's research (Inter-Lakes) runs in this wave. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Belmont, Meredith, Franklin and Plymouth (this wave), and Pembroke, Weare, Barrington, Farmington and Somersworth (running or queued). Don't write facts about those towns.

## Where facts go

- `district Gilford` for SAU 73, its three schools, policies, staff, budget, board and the Gilmanton contract.
- `district Laconia` only for a Huot fact that Laconia's files lack.
- `town Gilford` for town government, the Youth Center and recreation.
- No place for general NH rules.

All agents write in `town/Gilford/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, the superintendent search and governance belong to agent 4; Gilford High and Huot to agent 3; Gilford Middle and home education to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Gilford Elementary and families: care before and after school and on early-release days, class sizes, lunch prices and eligibility, delay notices, Gilford Got Lunch, reading specialists, speech and OT waits, tech help, buses on hill roads, clubs for 4th graders, pre-K, kindergarten, care waitlists, Spanish speakers and translation | `gilford-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P6.1, P6.3, P8.1, P8.2, P8.3, P9.1, P9.2, P9.3, P16.1, P16.2 |
| 2 | Gilford Middle and home education: the move from GES, accelerated math, phones and Chromebooks, IEP handoffs, ski racing absences, a ski club, homework help, early buses, social climate and bullying, Algebra 1 in grade 8, homeschoolers in band and sports, returning from homeschool, homeschool paperwork | `gilford-middle-school.md` | `raw/middle/` | P4.1, P4.2, P4.3, P6.2, P10.1, P10.2, P10.3, P12.1, P12.2, P12.3, P13.1, P13.2, P13.3 |
| 3 | Gilford High and Huot: Huot admission, buses and college credit, moving from Gilmanton, AP and dual enrollment, internships, guidance, graduation tickets, choosing 9th-grade classes, co-op teams, sports fees, sports buses, instruments, performing arts, mental health counselors, non-college paths, community support | `gilford-high-and-huot.md` | `raw/high/` | P3.1, P3.2, P3.3, P7.1, P7.2, P11.1, P11.2, P11.3, P16.3, P17.1, P17.2, P17.3, P18.2, P18.3, P20.1, P20.2, P20.3 |
| 4 | Money and governance: the budget and enrollment, Gilmanton's tuition, taxes and the superintendent change, the superintendent search, comparisons with Laconia and Inter-Lakes, cuts from falling enrollment, the school share of a mortgage, what drives the 2.8% increase, teacher retention, arts cuts, spending breakdown, elections and the deliberative session, watching meetings | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P7.3, P14.1, P14.2, P14.3, P15.1, P15.2, P15.3, P18.1, P19.1, P19.2, P19.3 |
