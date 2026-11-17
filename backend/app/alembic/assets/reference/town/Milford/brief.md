# Milford Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Milford and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Milford/questions.md`: 20 profiles and 60 questions, shared by four agents. (They arrived labeled "Milton NH," but every profile describes Milford.)

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Milford

- **Milford** is a town in Hillsborough County on the Souhegan River, west of Nashua and Amherst, with the Oval downtown and Routes 101, 101A and 13. Site town id 357. It has a Board of Selectmen, a town administrator and a Budget Advisory Committee; the school district is separate.
- **Milford School District** (site district id 357) is **SAU 40**, a one-district SAU. Use `district Milford` for SAU-level facts. It votes by official ballot (SB2); the library has its 2026 deliberative session date.
- **Its schools** (site school ids): Milford Early Education Experiences (29234, preschool, run by the Office of Special Services); Jacques Memorial Elementary (26580, kindergarten and grade 1); Heron Pond Elementary (27895, grades 2–5); Milford Middle School (21760, grades 6–8); Milford High School (21765, grades 9–12) with the **Applied Technology Center**, a regional career center (the library's list names Milford, Souhegan and Wilton-Lyndeborough as sending schools). Find what the Bales School building holds now (the questions name a "Sage School at Bales" and an alternative program).
- **Mason** sends its grades 6–12 to Milford under a tuition contract (`places.yaml`; check its terms and dates). Milford students also attend the Nashua Technology Center and Hudson's Palmer Center (15 Milford students at Palmer in 2025-26, `town/Hudson/alvirne-and-palmer-cte.md`, `cte-center-programs` 13).
- **Starting pages:** the district, https://www.milford.k12.nh.us (schools, the board, the budget, policies, the ATC, special services); the town, https://www.milford.nh.gov (selectmen, the Budget Advisory Committee, the tax rate, elections and warrants, planning, recreation).
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 2,413 in 2014-15, 2,188 in 2019-20, 1,837 in 2025-26 (P8.2).
  - Milford High's enrollment: 825 in 2015-16, 811 in 2019-20, 655 in 2024-25.
  - Cost per pupil, FY2025: Milford $22,084 (P2.3 says "over $22,000"); state $22,699; Amherst $23,894; Hollis $23,370; Souhegan Cooperative $25,841; Mont Vernon $18,635.
  - Tax rates per $1,000 (NH DRA, 2025): total $25.93, local school $16.98, municipal $6.06 (P7.2 asks why the school rate is high: equalized value per pupil and state aid explain rates; use the site's adequacy aid and the town's valuation).
  - Question 2 (November 2026): Milford voted 4,036 to 2,817, 58.9% yes, short of the 60% needed (the site's data; P2.2).
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/*/milford-*`: budget documents, the 2026 deliberative session and its packet, the enrollment page, the FY27 warrant, home page, policy JEBA, Jacques Memorial and its kindergarten pages, MEEE, policies, registration, rising kindergarten pages, special services, and town voter pages.
- **Library facts already loaded** (don't repeat them): the kindergarten cutoff (policy JEBA), online registration, the MEEE preschool and the SB2 dates. Read them: `grep -n -B2 -A10 "place: district Milford" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** a school budget "over $52 million" and next year's tax increase (P2.1); the 6% tax cap question in November 2026 (P2.2; it failed in Milford at 58.9%); "over $22,000 a kid" and "about a third" proficient in math (P2.3; the site's data); a high school tax rate against towns with similar budgets (P7.2); the default budget higher than the proposed budget (P8.1); sending districts' share of the ATC building (P8.3); the School Board and Budget Advisory Committee disagreeing (P15.1); another roof or HVAC bond (P15.2); "a CTE renovation bond" and when the new shops open (P4.2); losing teachers to Amherst and Bedford (P12.2).
- **Schools and programs:** MEEE's waitlist (P1.1); full- or half-day kindergarten at Jacques (P1.2); why grades split across Jacques and Heron Pond (P3.1); a gifted program (P3.2); "the Sage School at Bales" and the alternative program (P5.2, P16.3); bus routes canceled for driver shortages (P5.3); different bell times (P13.1); full-time nurses in every building (P14.3); no-cut teams (P18.2); a full-time SRO (P18.3); a Boys & Girls Club or recreation bus from Heron Pond (P19.2).

## Already researched, or being researched now

- **Being researched at the same time** (November 16, 2026): **Hampton** and **Exeter**. Don't write facts about them.
- **Comparisons:** `town/Bedford/` (Bedford's pay and programs, for P12.2), `town/Merrimack/` (the Nashua Technology Center and Palmer for Merrimack students), `town/Hudson/` (Palmer's programs and Milford's 15 students), `town/Nashua/` (charter and private options near Nashua). Amherst, Hollis and Souhegan aren't researched; use the site's data for comparisons with them.
- **State rules already written:** the library and earlier towns cover EFAs and school funding, home education access to classes, activities and CTE (`district-homeschool-access`, `cte-admission-and-cost-rules`) and the end of the yearly evaluation (July 1, 2026), special education, 504 plans, English learner services and translation, free and reduced-price meals, guardianship, bullying (the library's new `students-hb-131-bullying-law`), phones, default budgets, tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`), housing and enrollment research (`research-housing-and-school-enrollment`) and gifted education (`gifted-and-talented-rules`). Read Manchester's `student-support.md`, Nashua's `special-education.md`, Concord's `families-and-support.md` and Dover's `money-buildings-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place.

## Where facts go

- `district Milford` for SAU 40, its schools, MEEE, the ATC, the Bales School programs, policies, staff, budget and board.
- `district Mason` for Mason's side of its tuition contract; another sending district's name only for its own side of an ATC agreement.
- `town Milford` for town government and services: selectmen, the Budget Advisory Committee, the town's tax rate and budget, planning and housing, police and SROs, recreation and after-school programs, the library.
- Private schools and charters near Milford: their own district record if the site has one, otherwise `town Milford` with the school named. No place for general NH rules.

All four agents write in `town/Milford/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** budgets, taxes, bonds (including the CTE bond's money side), buildings, contracts and pay belong to agent 4; the ATC's programs and the shop project's timing to agent 2; special education and the Bales programs to agent 3. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Early years, elementary schools and daily life: MEEE enrollment and waitlist, kindergarten's day and after-school care, class sizes at Jacques, the move to Heron Pond and the two-building split, gifted programs, elementary results against Amherst and Hollis, phonics and screens, bell times, delayed openings, fees and help, registration paperwork, nurses, free and reduced-price meals, after-school buses from Heron Pond, reading help | `elementary-schools-and-daily-life.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.2, P3.3, P12.1, P13.1, P13.2, P13.3, P14.1, P14.3, P19.1, P19.2, P19.3 |
| 2 | Milford Middle, Milford High and the Applied Technology Center: trades programs, the shop renovation's timing, CTE and graduation, AP and dual enrollment, guidance and scholarships, graduates' plans, ATC classes for homeschool and EFA students, bullying and phones at the middle school, athletics and fundraising, the move to high school, arts programs, ATC digital media and culinary, the move to middle school, team cuts, employer internships | `middle-high-and-atc.md` | `raw/high/` | P4.1, P4.2, P4.3, P9.1, P9.2, P9.3, P10.2, P11.1, P11.2, P11.3, P17.1, P17.2, P18.1, P18.2, P20.1 |
| 3 | Special education, student support, choices and safety: the Office of Special Services and paras, the Sage School at Bales, special transportation, communication with Spanish-speaking families, English learners at the middle school, after-school clubs and tutoring, home education access and returning in grade 9, diversity and mid-year arrivals, credit recovery, mental health support, the alternative program, late buses, SROs and locked doors | `student-support-and-choices.md` | `raw/support/` | P5.1, P5.2, P5.3, P6.1, P6.2, P6.3, P10.1, P10.3, P14.2, P16.1, P16.2, P16.3, P17.3, P18.3 |
| 4 | Money, governance, buildings and staff: the budget and next year's tax, the tax cap, spending per pupil and results, Milford against Amherst, the school tax rate, room for growth, the default budget, enrollment trends, ATC sending districts' payments, teacher pay and turnover, administration against classrooms, the board and Budget Advisory Committee, maintenance and bonds, apartments and enrollment, morale, where to find results | `money-buildings-and-staff.md` | `raw/money/` | P2.1, P2.2, P2.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P12.2, P12.3, P15.1, P15.2, P15.3, P20.2, P20.3 |
