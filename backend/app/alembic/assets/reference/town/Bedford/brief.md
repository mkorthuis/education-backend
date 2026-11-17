# Bedford Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Bedford and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Bedford/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Bedford

- **Bedford** is a town in Hillsborough County, west of Manchester across the Merrimack River, bordering Manchester, Merrimack, Amherst, New Boston and Goffstown; Route 3 and the F.E. Everett Turnpike run through it. Site town id 41. It has a town council and a town manager; the school district is separate.
- **Bedford School District** (site district id 41) is **SAU 25**, a one-district SAU. Use `district Bedford` for SAU-level facts too. It votes by official ballot (SB2): for 2026-27, Session I was February 3, 2026, with a default budget if the proposed one fails.
- **Its schools** (site school ids):
  - **Kindergarten to grade 4:** Memorial (20990), Peter Woodbury (21000) and Riddle Brook (27680, which the site also lists with preschool).
  - **The Bedford Early Education Program (BEEP):** an inclusive preschool for three- and four-year-olds with and without special needs, with tuition for typically developing children (library fact). Find which building it is in.
  - **McKelvie Intermediate School** (21005, grades 5–6), **Ross A. Lurgio Middle School** (28560, grades 7–8) and **Bedford High School** (28555, grades 9–12, with the IB Diploma Programme and AP). Lurgio and BHS share the Nashua Road campus.
- **Career and technical education:** Bedford students may apply to the Manchester School of Technology's CTE programs (Manchester's research has MST's programs and how students from other districts apply).
- **Before 2007** Bedford's high school students went to Manchester West; BHS opened then. Only use that history if a question needs it.
- **Starting pages:** the district, https://www.sau25.net (check; the district's site may be on Google Sites), its school board, budget and policy manual pages; the town, https://www.bedfordnh.org (town council, the tax rate, recreation, the library, police); the Bedford Citizen (https://thebedfordcitizen.org) for news, to find primary sources.
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 4,414 in 2014-15, 4,407 in 2019-20, 3,912 in 2025-26.
  - Bedford High's enrollment: 1,477 in 2015-16, 1,498 in 2019-20, 1,358 in 2024-25.
  - Cost per pupil, FY2025: Bedford $19,650; state $22,699; Merrimack $23,849; Londonderry $21,196; Manchester $18,020.
  - Tax rates per $1,000 (NH DRA): 2025 total $16.49, local school $10.45, municipal $3.87.
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Question 2 results, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/batch-3/bedford-*`: the 2025 annual report, BEEP's pages and 2026-27 tuition, the FY2027 budget handouts, superintendent's summary, election dates and final warrant, the policy manual and policy JEB, the info and reports pages, Memorial's traffic page, Peter Woodbury's and Riddle Brook's arrival pages, registration, and a Bedford Citizen article.
- **Library facts already loaded** (don't repeat them): full-day kindergarten (the FY2027 budget summary), the kindergarten cutoff (policy JEB), BEEP, and the SB2 vote and 2026 dates. Read them: `grep -n -B2 -A10 "place: district Bedford" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** "the budget keeps climbing when enrollment isn't exploding" and what a tax cap would do (P6.1); "aging tech and building repairs" and "another big bond" (P6.2, P20.1); a move away from commercial textbooks to save money (P6.3, P8.2); the teachers' contract driving costs (P8.1); a cut to the technology budget (P15.1); "modest savings" in the budget (P20.3).
- **Schools and programs:** free full-day kindergarten, or a paid second half (P1.2); McKelvie's "later morning schedule" and staggered start times (P2.3, P7.1); "every kid in town" merging at McKelvie in grade 5 (P2.1); "thousands of middle and high schoolers" on the Nashua Road campus (P17.2); AP and IB exam sign-ups early in the fall (P13.2); Memorial's pre-K "only for special ed" (P19.1; BEEP takes typically developing children for tuition); a PTG at the schools (P11.3); new houses raising K–4 class sizes (P16.3); Riddle Brook homes selling for more (P16.1); "so many outside tutors" (P18.1) and tutoring explaining test scores (P12.3), which the data can't settle: say so plainly.

## Already researched, or being researched now

- **The Manchester School of Technology** (programs, admission of students from other districts, transportation): `town/Manchester/mst-and-pathways.md`. Add only Bedford's side: how many Bedford students attend, transportation and Bedford's policy.
- **The Founders Academy and Manchester's charters and Catholic schools:** `town/Manchester/charter-schools.md` and `enrollment-and-choices.md`; `town/Nashua/charter-private-and-home.md`.
- **Comparisons with Bedford:** `town/Londonderry/high-school-and-pathways.md` and `buildings-and-staff.md` compare Londonderry with Bedford (college admissions, ratings and home values); cite them where useful.
- **Statewide rules already written.** Earlier towns and the library cover EFAs and school funding, home education access to classes and activities and the end of the yearly evaluation (July 1, 2026), special education, 504 plans and dispute options, English learner services and translation, free and reduced-price meals, guardianship and custody paperwork, student records, phones, bullying, drinking water testing in schools, CTE admission (`cte-admission-and-cost-rules`), Early College (formerly Running Start), default budgets and tax caps. Read Manchester's `student-support.md` and `enrollment-and-choices.md`, Nashua's `special-education.md` and `families-and-support.md`, Concord's `families-and-support.md` and `special-education-and-health.md`, Dover's `money-buildings-and-governance.md` (tax cap mechanics) and Londonderry's `student-support-and-health.md` and `budget-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place. Spend your time on Bedford's own schools, policies and programs.
- **Researched at the same time** (November 16, 2026): Hudson, Bedford, Keene, Portsmouth, Goffstown and Laconia. Don't write facts about the other five districts; where a question compares Bedford with one of them, use the site's data.

## Where facts go

- `district Bedford` for SAU 25, its schools, BEEP, programs, policies, staff, budget and board.
- `town Bedford` for town government and services: the town council, the town's tax rate and budget, development and housing, police and SROs, recreation and leagues, the library, the town pool if it's the town's.
- `district Manchester` only for an MST fact Manchester's research doesn't have. Charter schools: their own district record (for example `district The Founders Academy Charter School`). Private schools: `town Bedford` with the school named in the statement. No place for general NH rules.

All four agents write in `town/Bedford/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** the budget, taxes, contract, bonds, buildings, technology spending and staffing belong to agent 4; bell times and buses to agent 2; BEEP and kindergarten to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Elementary schools, BEEP and family life: checking an address's school, full-day kindergarten and its cost, before- and after-school care, home education access, paperwork and part-time classes, English learner support at Riddle Brook, the PTG, pickup lists, volunteering, PowerSchool and Google Classroom access, the town line with Manchester and Merrimack, K–4 class sizes, public preschool, kindergarten registration and after-school waitlists | `elementary-schools-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P10.1, P10.2, P10.3, P11.1, P11.3, P14.1, P14.2, P14.3, P16.2, P16.3, P19.1, P19.2 |
| 2 | McKelvie, Lurgio, getting to school and safety: the move to McKelvie, advanced math, buses and bell times, accommodations moving to McKelvie, bus reliability, Nashua Road traffic, phones at Lurgio, choosing grade 9 courses, translated notices and alerts, comparing McKelvie with Founders and Catholic schools, returning from a charter, AI, data and coding before high school, bullying at McKelvie, the emergency plan for the Nashua Road campus | `mckelvie-lurgio-and-getting-to-school.md` | `raw/middle/` | P2.1, P2.2, P2.3, P5.3, P7.1, P7.2, P9.1, P9.2, P9.3, P11.2, P12.1, P12.2, P15.2, P17.1, P17.2 |
| 3 | Bedford High School: IB and AP, how colleges read IB grades, workload, students not in the IB Diploma, trades and MST, dual enrollment and its cost, fees and waivers, test results and tutoring, AI rules, exam sign-up dates, mental health support, honors and IB math help, paths besides four-year college, exam and activity costs | `high-school-and-pathways.md` | `raw/high/` | P3.1, P3.2, P3.3, P4.1, P4.2, P4.3, P7.3, P12.3, P13.1, P13.2, P13.3, P18.1, P18.2, P18.3 |
| 4 | Money, buildings, staff and special education services: paraprofessional staffing and IEP minutes, who helps in a disagreement, budget growth and a tax cap, technology and building repairs and bonds, textbooks and curriculum review, the teachers' contract, SAU administration against classrooms, the technology budget and IT staff, home values by school zone, drinking water tests, elementary space, facilities and maintenance, community use of the pool and fields and adult enrichment, "modest savings" and the tax rate | `money-buildings-and-staff.md` | `raw/money/` | P5.1, P5.2, P6.1, P6.2, P6.3, P8.1, P8.2, P8.3, P15.1, P15.3, P16.1, P17.3, P19.3, P20.1, P20.2, P20.3 |
