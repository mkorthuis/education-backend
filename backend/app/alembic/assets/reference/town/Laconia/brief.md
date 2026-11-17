# Laconia Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Laconia and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Laconia/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Laconia

- **Laconia** is a city in Belknap County in the Lakes Region, between Lake Winnipesaukee (Weirs Beach, Paugus Bay) and Lake Winnisquam, with Lakeport and the South End; it hosts Laconia Motorcycle Week each June. Site town id 285. It has a mayor and City Council and a city manager; the school board is elected, and the City Council adopts the school budget within the city budget under the city's tax cap.
- **Laconia School District** (site district id 285) is **SAU 30**, a one-district SAU. Use `district Laconia` for SAU-level facts too. Its office is at 39 Harvard Street.
- **Its schools** (site school ids):
  - **Preschool to grade 5:** Elm Street School (21290), Pleasant Street School (21260) and Woodland Heights Elementary (21285), each with preschool in the site's data. For 2026-27 families pick up a preschool registration packet at the SAU office (library fact).
  - **Laconia Middle School** (21275, grades 6–8) and **Laconia High School** (21255, grades 9–12) with the **Huot Technical Center**, a regional career and technical center for Laconia and nearby districts (Tamworth's research lists the sending schools).
- **Families register** through Alma Start (library fact); find what Alma is used for now (grades, forms).
- **Starting pages:** the district, https://www.laconiaschools.org (also https://www.sau30.org): schools, the board, the budget, policies, the Huot Center; the city, https://www.laconianh.gov (the City Council, the budget, the tax cap and tax rate, recreation, the library, police).
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 2,021 in 2014-15, 1,877 in 2019-20, 1,735 in 2025-26.
  - Laconia High's enrollment: 586 in 2015-16, 539 in 2019-20, 562 in 2024-25.
  - Cost per pupil, FY2025: Laconia $23,275; state $22,699; Gilford $25,908; Concord $24,351.
  - Tax rates per $1,000 (NH DRA): 2025 total $12.98, local school $5.72, state education $1.12, municipal $5.21 (2024: $13.63). The question about "richer lake towns" paying a lower rate (P20.3) can be answered from the site's rates and NH DOE's school taxes, with how equalized valuation and the state education tax work.
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Question 2 results, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/batch-2/laconia-*`: the city's finance page, the 2026-27 elementary handbook, the three elementary schools' pages, the home page and a flyer, policy JEB and section J, the 2026-27 new student page, the preschool page and the SAU 30 home page.
- **Library facts already loaded** (don't repeat them): the kindergarten and grade 1 cutoffs, Alma Start registration, and the preschool packet at the SAU office. Read them: `grep -n -B2 -A10 "place: district Laconia" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** a 4.4% school budget increase "this year" (P3.1); the City Council granting exemptions to the tax cap (P3.2); "five teaching spots" cut through attrition (P4.1, P15.2); health insurance "jumping nearly 17%" (P15.1); the state's share of special education costs (P15.3; the site has catastrophic aid); "richer lake towns" paying a lower rate (P20.3).
- **Schools and programs:** a preschool packet picked up at Harvard Street while everything else is in Alma (P1.1); meals on half-days and delayed openings (P1.3); SAU 30 buses to Holy Trinity (P7.1; RSA 189:9 and the district's practice); an LNA license through Huot's Health Sciences II before graduation (P10.1); Running Start (P10.2; renamed Early College); plumbing and HVAC hours counting toward an apprenticeship (P2.1); the Huot block schedule (P2.3); Huot's Protective Services (P17.2) and Automotive (P20.1) programs; Bike Week in June and bus routes (P12.1); full-day kindergarten everywhere (P19.1); a dedicated SRO every day (P17.1).

## Already researched, or being researched now

No earlier town is in SAU 30, and no earlier town sends students to Laconia.
- **The Huot Technical Center** is named in `town/Tamworth/high-school.md` (a list of Lakes Region schools); no earlier town researched it. Read `town/sau9/kennett-pathways.md` and `town/Dover/high-school-and-ctc.md` for how other regional centers' credentials and schedules were written.
- **Lakes Region Community College** may appear in `town/sau9/`, `town/Madison/` or `town/Tamworth/` files; grep before writing it again.
- **Statewide rules already written.** Earlier towns and the library cover EFAs and school funding (including EFA students' special education evaluations), home education access to classes and activities and the end of the yearly evaluation (July 1, 2026), special education, 504 plans, English learner services and translation, free and reduced-price meals, guardianship and custody paperwork, student records, phones, bullying, transportation to private schools (RSA 189:9), CTE admission (`cte-admission-and-cost-rules`), Early College (formerly Running Start), the LNA license rules, default budgets and tax caps. Read Manchester's `student-support.md` and `enrollment-and-choices.md`, Nashua's `special-education.md` and `families-and-support.md`, Concord's `families-and-support.md` and `special-education-and-health.md`, Dover's `money-buildings-and-governance.md` (tax cap mechanics; Dover is also a city with a tax cap) and Londonderry's `student-support-and-health.md` and `budget-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place. Spend your time on Laconia's own schools, policies and programs.
- **Researched at the same time** (November 16, 2026): Hudson, Bedford, Keene, Portsmouth, Goffstown and Laconia. Don't write facts about the other five districts.

## Where facts go

- `district Laconia` for SAU 30, its schools, the Huot Technical Center, programs, policies, staff, budget and board.
- `town Laconia` for city government and services: the City Council, the city's tax cap, tax rate and budget, housing, police and SROs, Motorcycle Week traffic, recreation and summer programs, the library, the Boys & Girls Club.
- `district Gilford` and other sending districts only for their own side of the Huot agreements. Private schools (Holy Trinity, Laconia Christian): `town Laconia` with the school named. Lakes Region Community College: `town Laconia` with the college named. No place for general NH rules.

All four agents write in `town/Laconia/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** the budget, the tax cap, staffing cuts, insurance, buildings and fields belong to agent 4; Huot's programs to agent 2, and Huot's access for homeschoolers and adults to agent 3. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Elementary schools, the early years and daily life: the preschool packet and Alma, before- and after-school care at Elm Street, meals on half-days and delays, buses and pickup after 3:30, nurses, getting to the Boys & Girls Club, buses to Holy Trinity, counselors at Pleasant Street, paper copies, summer programs, Motorcycle Week and buses, elementary zones and their reputations, who to talk to and volunteering, full-day kindergarten and class size, screens in kindergarten, choosing a school at registration | `elementary-schools-and-daily-life.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.2, P4.3, P6.2, P7.1, P11.1, P11.2, P11.3, P12.1, P13.1, P14.3, P19.1, P19.2, P19.3 |
| 2 | Laconia Middle, Laconia High and the Huot Technical Center: plumbing and HVAC and apprenticeship hours, the push to four-year college, the block schedule and credits, AP and honors and college admissions, middle school bullying and phones, dual enrollment at Lakes Region Community College, truancy, the LNA license through Health Sciences, Early College credits, guidance counselor access, summer credit recovery, Protective Services, financial literacy, Automotive, phones in class | `high-school-and-huot.md` | `raw/high/` | P2.1, P2.2, P2.3, P5.1, P5.3, P8.3, P9.2, P10.1, P10.2, P10.3, P12.2, P17.2, P18.2, P20.1, P20.2 |
| 3 | Special education, student support, choices and adult learning: tuition and private options, para and speech therapist openings, IEP contacts and disputes, Holy Trinity to Laconia schools, EFAs and special education evaluations, homeschoolers at Huot and in LHS sports and band, mental health and substance use support, English learner teachers, translated alerts, 504 plans at the middle school, accelerated math, mid-quarter progress reports, SROs and building security, evening classes for adults, financial aid help for adults | `student-support-and-choices.md` | `raw/support/` | P5.2, P6.1, P6.3, P7.2, P7.3, P8.1, P8.2, P12.3, P14.1, P14.2, P16.1, P16.2, P16.3, P17.1, P18.1, P18.3 |
| 4 | Money, taxes, governance, staff and buildings: the budget increase, the tax cap and its exemptions, teachers against central office and insurance, positions cut through attrition and class sizes, what the spending buys, ratings and renters, test scores against Gilford, the school share of a tax bill, insurance costs and teacher retention, workload after cuts, state special education aid, fields and locker rooms and the capital plan, the lake towns' tax rates | `money-staff-and-buildings.md` | `raw/money/` | P3.1, P3.2, P3.3, P4.1, P9.1, P9.3, P13.2, P13.3, P15.1, P15.2, P15.3, P17.3, P20.3 |
