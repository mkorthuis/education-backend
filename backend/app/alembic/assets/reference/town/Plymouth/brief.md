# Plymouth Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Plymouth and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Plymouth/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Plymouth

- **Plymouth** is a town in Grafton County on the Pemigewasset River, home to Plymouth State University. Site town id 447.
- **Two districts serve Plymouth, both in SAU 48** (which serves several Pemi-Baker towns):
-   - **The Plymouth School District** (site district id 447): Plymouth Elementary (22355), preschool to grade 8.
-   - **The Pemi-Baker Regional School District** (site district id 428): Plymouth Regional High (22350), grades 9–12, with its career and technical center. `places.yaml` lists tuition students from Ashland, Campton, Ellsworth, Holderness, Rumney, Thornton, Warren, Waterville Valley and Wentworth; check which towns are members and which pay tuition.
- **Choices:** Mountain Village Charter School (site district id 704) and Holderness School (1043) are in the area.
- **Starting pages:** SAU 48, https://www.sau48.org (check); PRHS, https://prhs.sau48.org (check); the town, https://www.plymouth-nh.org (check).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 589 (2014-15), 600 (2019-20), 579 (2025-26); cost per pupil FY2025 Plymouth $26,555, Pemi-Baker $21,937, state $22,699; 2025 tax rates per $1,000: total $23.77, local school $11.55, municipal $9.97; Question 2: Plymouth 44.6%, Pemi-Baker 51.6%, so no cap in either (unofficial); math proficiency 2026: Plymouth 52%, Pemi-Baker 36%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Plymouth's and Pemi-Baker's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Plymouth|Pemi-Baker Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** PES doors in the morning (P1.1); Parks & Rec after-school (P1.2); pre-K open to everyone (P3.1); 30 to 55 a grade (P3.2); PSU student teachers (P3.3); kindergarten cutoff (P9.1); lunch time (P16.2); Chromebooks home (P13.2); about half proficient in math (P6.1); Algebra I or Spanish in 8th grade (P17.3).
- **PRHS:** automotive, culinary, outdoor recreation leadership, health science and TV & media (P2.1, P8.2, P12.2, P15.1); AP and PSU courses (P6.3, P15.2); reading around 72% (P14.2); graduation rate (P10.3); late buses (P12.3); work-study and fire/EMT credit (P20.1); phones (P20.3).
- **Choices:** Mountain Village's lottery and Montessori approach (P7.1, P7.2); EFAs and single classes (P7.3, P11.1, P11.2); a homeschooled student at PRHS (P11.3); Holderness School aid (P17.2).
- **Money:** a high tax bill and PRHS's tuition students (P2.3); budget and enrollment (P4.1); the split between PES and PRHS (P4.2); vote dates (P4.3); crossing guards and sidewalks (P16.1); teacher pay against Laconia and Inter-Lakes (P18.1); different calendars (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Laconia/` | Laconia's schools, for teacher pay comparisons (P18.1). Meredith's (Inter-Lakes) research runs in this wave. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Belmont, Gilford, Meredith and Franklin (this wave), and Pembroke, Weare, Barrington, Farmington and Somersworth (running or queued). Don't write facts about those towns.

## Where facts go

- `district Plymouth` for the Plymouth School District, PES, its preschool, budget and board.
- `district Pemi-Baker Regional` for PRHS, its career center, budget and board, and its tuition contracts.
- `sau 48` for SAU-wide facts.
- `district Mountain Village Charter School` and `district Holderness School` for their own facts.
- `town Plymouth` for town government, recreation and roads.
- No place for general NH rules.

All agents write in `town/Plymouth/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budgets, taxes and governance for both districts belong to agent 4; PRHS and its career center to agent 3; PES's upper grades, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Plymouth Elementary and families: door times, Parks & Rec after-school, delay notices, pre-K, class sizes, PSU student teachers, meals, bus stops downtown, reading specialists, the kindergarten cutoff, preschools, guardianship papers, Chromebooks, counselors, ski and outdoor programs, lunch time, bullying | `pes-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.2, P3.3, P5.1, P5.2, P5.3, P9.1, P9.2, P13.1, P13.2, P13.3, P14.3, P16.2, P16.3 |
| 2 | PES's upper grades, support and choices: math results, the move to PRHS, Mountain Village's lottery and Montessori approach, homeschool and EFAs, paras at PRHS, single classes at PES, homeschoolers at PRHS, translation, Holderness School aid, Algebra I and Spanish in 8th grade, speech evaluations, pull-outs, parent support groups | `pes-support-and-choices.md` | `raw/support/` | P6.1, P6.2, P7.1, P7.2, P7.3, P8.1, P11.1, P11.2, P11.3, P12.1, P17.2, P17.3, P19.1, P19.2, P19.3 |
| 3 | Plymouth Regional High and its career center: automotive, culinary, outdoor recreation, health science and TV & media, hiring graduates, AP and PSU courses and costs, transition planning, work skills, business partners, graduation and college rates, late buses, test scores, college and aid advising, honors and AP, work-study and fire/EMT credit, phones | `prhs-and-career-center.md` | `raw/high/` | P2.1, P2.2, P6.3, P8.2, P8.3, P10.1, P10.2, P10.3, P12.2, P12.3, P14.2, P15.1, P15.2, P15.3, P17.1, P20.1, P20.3 |
| 4 | Money and governance: the tax bill and PRHS tuition, budget and enrollment, the split between PES and PRHS, vote dates, buying in Holderness or Campton, schools for home buyers, crossing guards and sidewalks, teacher pay, shared services, board meetings online, the two calendars | `money-and-governance.md` | `raw/money/` | P2.3, P4.1, P4.2, P4.3, P9.3, P14.1, P16.1, P18.1, P18.2, P18.3, P20.2 |
