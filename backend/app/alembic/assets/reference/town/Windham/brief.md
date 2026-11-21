# Windham Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Windham and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Windham/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Windham

- **Windham** is a town in Rockingham County between Salem, Derry, Londonderry and Pelham, along I-93 and Route 111, with Cobbetts Pond, Canobie Lake and Searles Castle. Site town id 575. It has a Board of Selectmen and a town administrator; the school district is separate.
- **Windham School District** (site district id 575) is **SAU 95**, a one-district SAU. Use `district Windham` for SAU-level facts. It votes by official ballot (SB2); the library has its 2026 dates (`district-practices.md`, fact 146).
- **Its schools** (site school ids):
  - Golden Brook School (21130): preschool to grade 4, with the integrated Early Childhood Program;
  - Windham Center School (21135): grades 5–6;
  - Windham Middle School (21125): grades 7–8;
  - Windham High School (28640): grades 9–12.

  Every Windham address is in the same four schools.
- **Career and technical education:** Windham High students may apply to Salem High's CTE center (no tuition or transportation cost) and to some Pinkerton Academy programs (Architecture, Animal Science & Management, Electrical, Welding). Both are already researched (see below); write only Windham's side.
- **Starting pages:** the district, https://www.windhamsd.org (schools, the board, budgets and warrants, policies, calendar, registration, the preschool, special services, athletics); the town, https://www.windhamnh.gov (selectmen, the tax rate, assessing and exemptions, elections, recreation, the library and police).
- **Site figures that frame the questions:**
  - **Resident public school students** (the site's town enrollment): 2,854 in 2014-15, 3,051 at the peak in 2022-23, 2,847 in 2026-27 (P2.1 says "around 2,900"). School enrollment in 2025-26: Golden Brook 1,113, Windham Center 426, Windham Middle 414, Windham High 940 (down from 1,058 in 2022-23; P16.1 says "nearly 900").
  - **Cost per pupil, FY2025:** Windham $19,690 (P8.1); Salem $19,752; Pelham $20,212; Londonderry $21,196; Bedford $19,650; state $22,699.
  - **Tax rates per $1,000** (NH DRA): 2025 total $14.15, local school $10.07, state education $1.03, municipal $2.48. The 2024 total was $22.64; the equalization ratio went from 59.4% to 96.4%, so 2025 looks like a revaluation year (P4.1, P19.3; check).
  - **Question 2** (November 2026): Windham voted 4,461 to 3,144, 58.7% yes, short of the 60% needed. Results are unofficial (the site's data; P2.2).
  - **Math proficiency** (all grades): 65% in 2025 and 66% in 2026 (P18.1 says "around 65%"), against 55% in Londonderry, 48% in Salem, 44% in Pelham, 75% in Bedford and 44% statewide in 2026 (P19.1).
  - **Other data on the site:** every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/*/windham-*`: four budget PDFs and the budget folder, the budget voting page, the 2026 Voters' Guide, the town's 2026 notice, the home page, Golden Brook and its new-student page, kindergarten pages, the K–12 registration packet, policies, policy JEB, and the 2025-26 and 2026-27 preschool pages.
- **Library facts already loaded** (don't repeat them):
  - the kindergarten cutoff (policy JEB);
  - K–12 registration by emailed packet;
  - the preschool (a lottery, ages, sessions and tuition: $150 a month for two days, $300 for four);
  - the SB2 dates.

  Read them: `grep -n -B2 -A10 "place: district Windham" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:**
  - a budget "over $72 million" (P2.1);
  - what HB 1300 would mean (P2.2; Windham's 58.7% means the cap wasn't adopted);
  - the school and town shares of the tax bill (P4.1);
  - "nearly $39 million renovating Golden Brook and the middle school," and upcoming bonds (P4.2);
  - special education and out-of-district costs (P4.3; the site has special education aid);
  - the teachers' contract and the deliberative session (P8.3);
  - year-to-year school tax changes and the 2025 revaluation (P19.3).
- **Schools and programs:**
  - **Preschool and the early grades:**
    - the preschool lottery's odds (P1.1);
    - a 2:50 dismissal and the YMCA's care and waitlist (P1.2, P6.1);
    - kindergarten supplies and fees (P1.3);
    - Tutor.com for 4th graders (P6.2);
    - specials time (P17.3);
    - phonics (P18.2);
    - STEM or maker time at Windham Center (P20.1).
  - **Middle and high school:**
    - Windham Middle "ranked near the top" and advanced math (P3.1);
    - graduation moving off-site in 2028 and the turf field (P7.2);
    - "30 varsity sports teams," JV cuts and athletic fees (P12.1, P12.2);
    - an early high school start (P15.3).
  - **Choices:**
    - Windham Woods School: find what it is and how placement and tuition work (P5.2);
    - CTE waitlists at Salem and Pinkerton and the bus time (P2.3, P15.1);
    - "annual homeschool paperwork or portfolio reviews" (P13.2; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`).
  - **The school day:**
    - finishing the year after moving out of town (P6.3);
    - different bell times and tiered busing (P14.1);
    - a late bus (P14.3);
    - school resource officers "and marshals" at Golden Brook (P17.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Salem/high-school-and-cte.md` | Salem's CTE center: Windham students are eligible, with no tuition or transportation cost, and apply by February 20 (cte-center-programs 3, 5). Windham High's 2026-27 profile: 29 AP courses, 6 dual enrollment courses, 315 AP students with 85.71% scoring 3 or higher, and the class of 2026's plans (school-programs-after-grade-6 13, high-school-outcomes 8, both placed `district Windham`). CRDC AP comparisons (school-programs-after-grade-6 14). |
| `town/pinkerton/pinkerton-academics-and-pathways.md` | Pinkerton's CTE programs open to Windham students (cte-center-programs 5). |
| `town/Londonderry/` | Zillow home values including Windham's 03087 ZIP (`town-housing` 1); Londonderry's schools for comparison. |
| `town/Derry/`, `town/Bedford/`, `town/Hudson/` | Comparisons (Derry's home sale prices, `town-housing` 2; Bedford's class sizes and programs). |
| Library and earlier towns | State rules: EFAs, home education access and the end of the yearly evaluation (`district-homeschool-access`, `choice-hb-1268-home-education-history`); special education, extended school year and 504 plans (Nashua's `special-education.md`); English learner services and translation; free and reduced-price meals; residency and finishing the year after a move (Chatham's `school-residency-rules`); the Parental Bill of Rights (`parental-bill-of-rights`); bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and UNH transfer credit (Exeter's `college-admission-requirements-nh` 1–3, Bedford's `high-school-and-pathways.md`); default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

Nothing else is being researched at the same time.

## Where facts go

- `district Windham` for SAU 95, its four schools, the preschool, its policies, staff, budget and board.
- `town Windham` for town government and services: selectmen, the tax rate, assessing and exemptions, police and SROs, recreation and before- and after-school programs (the YMCA), the library.
- Salem's and Pinkerton's CTE programs belong to their own places, already researched. Windham's side (how many Windham students attend, transportation, credit, the schedule) is `district Windham`.
- Private schools (Windham Woods School and others): their own district record if the site has one, otherwise `town Windham` with the school named. No place for general NH rules.

All four agents write in `town/Windham/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** each topic belongs to one agent. Put what you find for another agent's area in your "For another file" section rather than writing it twice.
  - Budgets, taxes, bonds, buildings, contracts, staffing and pay: agent 4.
  - Windham High and Windham Middle's own programs: agent 2.
  - Golden Brook, Windham Center and the preschool: agent 1.
  - Buses, the calendar, CTE access, special education choices and student support: agent 3.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Golden Brook and Windham Center: the preschool lottery, before- and after-school care and costs, kindergarten fees and supplies, reading interventions and IEPs at Golden Brook, extended-year and summer help, morning drop-off, Tutor.com, ESL, the move to Windham Center, class sizes in K–4, specials time, help for middle-of-the-pack students in math, phonics, STEM and maker time, meals | `elementary-schools-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.3, P6.1, P6.2, P9.1, P9.3, P10.1, P17.3, P18.1, P18.2, P20.1, P20.3 |
| 2 | Windham Middle and Windham High: advanced math at WMS, the move from Windham Center, college results and counseling, AP and dual enrollment and credit transfer, graduation and the turf field, robotics and computer science, science labs, phones and Chromebooks, the social scene, sports and JV teams, athletic fees and boosters, financial aid help, dual enrollment against AP, the start time, ELOs and internships | `middle-and-high-school.md` | `raw/high/` | P3.1, P3.2, P3.3, P7.1, P7.2, P7.3, P11.1, P11.2, P11.3, P12.1, P12.2, P12.3, P15.2, P15.3, P20.2 |
| 3 | Student support, choices and getting to school: CTE access at Salem and Pinkerton and the bus time, Windham Woods School, finishing the year after a move, translated notices, home education access, paperwork and 9th-grade placement, bell times and tiered busing, snow delays, late buses, anxious 8th graders' move to WHS, counselor access, the 504 coordinator, the calendar's early releases and workshop days | `student-support-and-getting-to-school.md` | `raw/support/` | P2.3, P5.2, P6.3, P9.2, P13.1, P13.2, P13.3, P14.1, P14.2, P14.3, P15.1, P16.1, P16.2, P16.3, P17.1 |
| 4 | Money, governance, buildings and staff: the budget against enrollment, HB 1300, the school and town tax shares, renovations and bonds, special education and out-of-district costs, spending against Salem, Londonderry and Pelham, the Parental Bill of Rights in practice, the teachers' contract and the deliberative session, paras and counselors, teacher turnover, security staffing, substitute and volunteer clearance, scores and home values, school zoning, tax changes for a new owner | `money-buildings-and-staff.md` | `raw/money/` | P2.1, P2.2, P4.1, P4.2, P4.3, P8.1, P8.2, P8.3, P10.2, P10.3, P17.2, P18.3, P19.1, P19.2, P19.3 |
