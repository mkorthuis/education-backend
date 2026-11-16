# Concord Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Concord and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Concord/questions.md`: 40 profiles and 120 questions, twice the usual, so nine agents share them.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

## What you need to know about Concord

- **Concord** is the state capital, in Merrimack County. Site town id 111. The city has a mayor and city council; the school district is separate, under its own charter.
- **Concord School District** (site district id 111) is **SAU 8** (https://www.sau8.org/). Its **Board of Education** adopts the budget after public hearings, with no district meeting or ballot vote. Use `district Concord` for SAU-level facts too.
- **Its schools** (site school ids):
  - **Elementary:** Abbot-Downing (20240, preschool to grade 5), Beaver Meadow (26490, preschool to grade 5), Christa McAuliffe (20305, K–5), and the paired Mill Brook (20250, preschool to grade 2) and Broken Ground (20260, grades 3–5) in East Concord.
  - **Middle:** Rundlett Middle School (20270, grades 6–8).
  - **High:** Concord High School (20285), with the Concord Regional Technical Center (CRTC; the library's fact calls it the Concord Regional Technology Center, so check the name). Its sending high schools include Bishop Brady, Bow, Hopkinton, John Stark, Kearsarge, Merrimack Valley, Pembroke Academy and Pittsfield.
  - **Closed:** Eastman, Rumford and Walker schools aren't on NH DOE's current list.
- **Penacook** is a village of the city, but the state's district/town list puts it in the **Merrimack Valley School District** (SAU 46, site district id 352), with Boscawen, Loudon, Salisbury and Webster. Three profiles live in Penacook (P2, P14, P30). Check which schools Penacook students attend and whether any part of Penacook is in the Concord School District. Place those facts in `district Merrimack Valley`.
- **Deerfield** sends high school students to Concord High under a tuition contract (July 2024 to June 2027, in `places.yaml`).
- **Site figures that frame the questions:**
  - Enrollment: 4,674 in 2015-16, 3,933 in 2023-24 and 3,832 in 2024-25 (NH DOE October counts).
  - Cost per pupil, FY2025: Concord $24,351; state $22,699; Hopkinton $24,040; Pembroke $20,240; Merrimack Valley $19,767; Bedford $19,650; Bow $18,864.
  - The site also has every school's enrollment by grade, test scores (with growth where NH DOE reports it), class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety and discipline counts, graduation and plans, licensed child care in the city, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/batch-5/concord-*`: the business office, budgets and the FY2027 budget, the district charter (PDF and text), registration, school hours, preschool and contacts.
- **Library facts already loaded about Concord** (don't repeat them; cite them as existing): kindergarten on the same hours as grades 1–5 (7:45 a.m. to 2:30 p.m.); the kindergarten cutoff (5 by September 30, no exceptions, Policy 512) and registration; the Concord Developmental Preschool (ages 3–5 at Abbot-Downing, Beaver Meadow and Mill Brook); how the budget is adopted (FY27 hearings March 23 and 25, 2026); the Capital City 21st Century Community Learning Centers at Mill Brook, Broken Ground and Rundlett; CRTC's sending schools; and **the new middle school on NH DOE's school building aid list** (below). State rules on special education, 504 plans, English learners, EFAs, home education, McKinney-Vento, foster care, Running Start and truancy are in the library's rule topics.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **The new middle school's site.** About 15 questions assume it is being built at **Broken Ground** (P1.3, P2.1, P3.1, P3.3, P13.1, P18.1, P18.3, P26.1, P29.1, P29.3, P33.1, P34.1, P39.1). The board chose Broken Ground in December 2023. But the library's 2026-27 building aid fact calls the project "Concord's new Rundlett Middle School", a 900-student, 214,105-square-foot school replacing the 1957 building, at an estimated $164,623,927 with a maximum state award of $65,849,571 at Concord's 40% rate. $164,623,927 is the January 2025 projection for the Rundlett site; the Broken Ground projection was $156,551,477. A January 2025 Concord Monitor article reported the board leaning back toward Rundlett. **Find the current site, design, cost, schedule and status first**, and answer each question from that. If the school is going at Rundlett, say so plainly; many questions then change.
- **The cost:** "$152 million" (P4.1, P24.1): the board set a $152 million cap in 2024; earlier estimates ran to $176 million. "Nashua built a similar school for far less" (P4.1): see the Nashua note below.
- **The building's age:** "the 1955 Rundlett building" (P29.2); the library says 1957.
- **Penacook:** whether Penacook students go to Rundlett or Concord High at all (P2.1, P14.2, P30.1).
- **Walk zones:** "the 1.5-mile walk zone" (P3.3, P15.2): check Concord's policy.
- **Comparisons:** St. Paul's School's AP offerings (P8.1; check whether it offers AP courses); gifted enrollment "compared to national averages" (P1.1); suspension rates by race in state data (P4.3); remedial math placement of Concord High graduates at NHTI (P32.1).
- **Daily life:** a 20-minute lunch at Rundlett (P20.3); locked or vandalized bathrooms (P19.3); half-day or early-release days for kindergarten (P36.3); a referendum on the site (P24.2; the district has no voter meeting).

## Already researched, or being researched now

No earlier town is in SAU 8. Start from the library facts above and the site's data.

**Manchester** (`town/Manchester/`, finished) and **Nashua** (`town/Nashua/`, being researched now) have many of the same statewide questions: EFAs, home education, special education rights and evaluations, 504 plans, English learner services and interpreters, foster care and McKinney-Vento, Running Start, guardianship and custody papers. Read Manchester's `student-support.md`, `enrollment-and-choices.md` and `mst-and-pathways.md` for state rules already written there, and don't write them again. Where the library and those files lack a state rule you need, write it with no place. Spend your time on Concord's own schools, policies and programs.

**Nashua's new middle school (McCarthy):** Nashua's research is gathering its cost and bond (`town/Nashua/money-and-governance.md` and `middle-schools.md`, when written). For P4.1, use those if they exist when you get there; otherwise gather only McCarthy's cost, size and year from a cited source.

## Where facts go

- `district Concord` for the district's schools, programs, policies, staff, budget, the new middle school, the Board of Education and the superintendent's office.
- `town Concord` for city government and services: the city council, the master plan, planning board and traffic studies, police and SROs, snow removal, tax relief, conservation lands, and the city's role in the school project.
- `district Merrimack Valley` for Penacook's schools.
- Another district (Bow, Hopkinton, Pembroke, Bedford, Nashua) only for a fact about that district itself.
- No place for general NH rules.

All nine agents write in `town/Concord/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** the middle school project touches several areas. Agent 1 owns the project itself (site, cost, design, schedule, process, outreach, environment, the old Rundlett site); agent 8 owns its tax impact and state aid; agent 2 owns buses, walk zones and traffic around it; agent 9 owns repairs to the current Rundlett building. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | The new middle school: current site, design, cost and schedule; the site decision and comparisons; outreach and translation; construction effects at Broken Ground; wetlands, energy and walkability; the old Rundlett building's future | `new-middle-school.md` | `raw/middle-school-project/` | P1.3, P3.1, P4.1, P13.1, P16.1, P20.1, P24.2, P25.1, P26.1, P29.1, P29.2, P29.3, P33.1, P39.1, P39.2 |
| 2 | Getting to school, traffic and safety: buses and winter delays, walk zones and split custody, Penacook's schools and routes, traffic studies and drop-off corridors, snow removal, bus monitors, SROs and tip lines | `getting-to-school-and-safety.md` | `raw/daily/` | P2.1, P2.3, P3.3, P15.2, P18.1, P18.2, P18.3, P30.1, P35.1, P35.2, P35.3 |
| 3 | Elementary schools and the early years: gifted and math acceleration, after-school care at Mill Brook, reading benchmarks, phones and watches, kindergarten class sizes, devices and hotspots, pre-K, preschool handoffs, early-release days, outdoor education | `elementary-schools.md` | `raw/elementary/` | P1.1, P1.2, P6.2, P6.3, P7.1, P7.2, P9.2, P36.1, P36.2, P36.3, P39.3 |
| 4 | Concord High academics and pathways: CTE and CRTC, AP and honors, NHTI dual enrollment and articulation, AP gaps, the Seal of Biliteracy, computer science, internships, remedial math, civics and life skills, adult education | `high-school-and-pathways.md` | `raw/high/` | P2.2, P8.1, P8.2, P11.2, P19.1, P21.1, P30.3, P31.1, P31.2, P32.1, P32.2, P32.3, P37.1, P37.2 |
| 5 | Student life, climate and discipline at Rundlett and Concord High: suspensions and disparities, bullying, the move to high school, intramurals, behavior support, student voice, bathrooms, band, lunch, ELL students and honors, halal food; homeschool access to classes and activities, and EFA students returning | `student-life-and-climate.md` | `raw/climate/` | P4.3, P7.3, P10.1, P10.2, P10.3, P11.3, P15.3, P16.2, P19.2, P19.3, P20.2, P20.3, P21.2, P21.3, P33.3 |
| 6 | Special education, 504 plans and health: 504 accommodations, counselor ratios, evaluation delays and appeals, structured literacy, transition planning, IEP paperwork, social-emotional supports, Riverbend, threat assessment, nurses, therapy backlogs, AAC, language disorders | `special-education-and-health.md` | `raw/sped/` | P5.1, P5.2, P9.3, P12.1, P12.2, P12.3, P17.3, P23.1, P23.2, P23.3, P26.2, P38.1, P38.2, P38.3 |
| 7 | Families, English learners and community support: ELL classes, food and summer meals, interpreters and translated report cards, foster care counseling and transportation, sensitive assignments, two-household notices, volunteering, homelessness, vacation meals, coats, family liaisons, domestic violence confidentiality, custody orders and pick-up, crisis stabilization | `families-and-support.md` | `raw/support/` | P3.2, P9.1, P13.3, P14.1, P14.2, P14.3, P15.1, P26.3, P27.1, P27.2, P27.3, P33.2, P40.1, P40.2, P40.3 |
| 8 | Money, taxes and governance: the budget's growth as enrollment falls, the bond's tax impact, state building aid, senior tax relief, commercial and residential taxes, administrative cost per pupil, rents, the adequacy formula, public comment and board summaries, alumni's say | `money-and-governance.md` | `raw/money/` | P5.3, P6.1, P13.2, P24.1, P24.3, P25.2, P25.3, P28.1, P28.3, P30.2, P31.3, P37.3 |
| 9 | Buildings, staff and how Concord compares: repairs at Rundlett, deferred maintenance, custodial budgets, boilers and air filtration, teacher absenteeism, staff diversity, para vacancies, starting pay and mentoring, school quality and home values, catchment turnover, comparisons with Bow, Hopkinton and Pembroke | `buildings-staff-and-comparisons.md` | `raw/staff/` | P4.2, P8.3, P11.1, P16.3, P17.1, P17.2, P22.1, P22.2, P22.3, P28.2, P34.1, P34.2, P34.3 |
