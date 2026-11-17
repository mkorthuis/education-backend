# Portsmouth Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Portsmouth and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Portsmouth/questions.md`: 20 profiles and 60 questions, shared by five agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Portsmouth

- **Portsmouth** is a city in Rockingham County on the Piscataqua River, across from Kittery, Maine, home of the Pease Tradeport and next to the Portsmouth Naval Shipyard (in Kittery). Site town id 449. It has a mayor and City Council and a city manager; the school board is elected, and the City Council adopts the school budget within the city budget.
- **The Portsmouth School Department** (site district id 449) is **SAU 52**, a one-district SAU. Use `district Portsmouth` for SAU-level facts too. On June 8, 2026, the City Council adopted the fiscal 2027 General Fund budget, which includes the schools (library fact).
- **Its schools** (site school ids):
  - **The Portsmouth Early Education Program (PEEP)** (22560): an inclusive preschool at Little Harbour School for children ages 3 to 5, with tuition (library fact). A saved page is named "Little Clipper"; find what it is (P10.2).
  - **Kindergarten to grade 5:** Little Harbour (22515), Mary C. Dondero (22545) and New Franklin (22525).
  - **Portsmouth Middle School** (22510, grades 6–8) and **Portsmouth High School** (22565, grades 9–12) with its **Career Technical Education Center** and the **Robert J. Lister Academy**, a small alternative high school.
- **Sending towns** (`places.yaml`): Greenland, New Castle, Newington and Rye (SAU 50) send their high school students to Portsmouth High under AREA agreements; New Castle and Newington also send grades 6–8 to Portsmouth Middle. Portsmouth's tuition policy (DEAA, revised 2016) is at https://files.portsmouthnh.gov/school/policies/DEAA.pdf; the agreements themselves weren't found online.
- **Starting pages:** the school department, https://www.cityofportsmouth.com/school (schools, the board, the budget, policies); the city, https://www.portsmouthnh.gov (the City Council, the budget and tax rate, recreation, the library, police); files at https://files.portsmouthnh.gov.
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 2,225 in 2014-15, 2,201 in 2019-20, 2,021 in 2025-26.
  - Portsmouth High's enrollment: 1,110 in 2015-16, 1,129 in 2019-20, 1,017 in 2024-25 (including students from the sending towns).
  - Cost per pupil, FY2025: Portsmouth $27,609; state $22,699; Rye $32,559; New Castle $36,955; Newington $40,353; Greenland $24,874; Dover is in the site's data too.
  - Tax rates per $1,000 (NH DRA): 2025 total $11.51, local school $4.57, municipal $5.26.
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Question 2 results, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/batch-8/portsmouth-*`: the FY2027 adopted budget, the home page, kindergarten registration, "Little Clipper", PEEP's pages, application, flyer and tuition, several site pages (node*), the policies (with section J) and registration.
- **Library facts already loaded** (don't repeat them): full-day kindergarten at New Franklin (a welcome letter), the kindergarten cutoff (from a 2017-18 page), Infinite Campus registration for 2026-27, PEEP, and the fiscal 2027 budget adoption. Read them: `grep -n -B2 -A10 "place: district Portsmouth" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** the budget "jumping by millions every year" (P2.2); rent and the school budget (P4.1; say plainly what the data can and can't show); the tax bill and health insurance and salaries (P5.1); "this local tax cap idea" and an override (P5.2; Portsmouth's charter and the site's Question 2 data); Rye and Newington's "fair share" (P5.3); per-pupil spending "way higher than the state average" (P9.1; the site's data agrees: $27,609 against $22,699); budget cuts to reading specialists, paras and arts (P8.2, P14.2); "a massive bond for a new roof or HVAC" (P16.2).
- **Schools and programs:** elementary redistricting (P1.1); free lunch for everyone (P4.3); "Little Clipper" preschool (P10.2); "random Wednesdays off" and many early-release days (P7.2); a high school bus before 8 a.m. and a start-time change (P7.3); a state ban on DEI programs and its effect on teaching and clubs (P15.2; state law and any court rulings, plainly); half-empty elementary schools in ten years (P13.3; enrollment projections, not opinion); what Coast Guard families do (P10.3; housing near Pease and the Coast Guard station).

## Already researched, or being researched now

No earlier town is in SAU 52, and no earlier town sends students to Portsmouth.
- **The Seacoast:** `town/Dover/` covers Dover's CTC and Great Bay Community College options (`high-school-and-ctc.md`), Seacoast Charter, Saint Mary Academy and Portsmouth Christian Academy (`choices-and-adult-learning.md`, topic `town-school-options-nearby`), and Dover's elementary schools. Cite what's there; add Portsmouth's own side.
- **Statewide rules already written.** Earlier towns and the library cover EFAs and school funding, home education, special education, 504 plans and transition services to age 21, English learner services and translation, free and reduced-price meals and community eligibility, guardianship and custody paperwork, student records, phones, bullying, military families (the Interstate Compact on Educational Opportunity for Military Children), CTE admission (`cte-admission-and-cost-rules`), Early College (formerly Running Start), the "divisive concepts" law, default budgets and tax caps. Read Manchester's `student-support.md` and `enrollment-and-choices.md`, Nashua's `special-education.md` and `families-and-support.md`, Concord's `families-and-support.md` and `special-education-and-health.md`, Dover's `money-buildings-and-governance.md` (tax cap mechanics) and Londonderry's `student-support-and-health.md` and `budget-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place. Spend your time on Portsmouth's own schools, policies and programs.
- **Researched at the same time** (November 16, 2026): Hudson, Bedford, Keene, Portsmouth, Goffstown and Laconia. Don't write facts about the other five districts.

## Where facts go

- `district Portsmouth` for SAU 52, its schools, PEEP, the CTE Center, Lister Academy, programs, policies, staff, budget and board.
- `town Portsmouth` for city government and services: the City Council, the city's tax rate and budget, housing, police and SROs, recreation and summer programs, the library.
- `district Rye`, `district Newington`, `district New Castle`, `district Greenland` for their side of the AREA agreements and tuition.
- Charter schools: their own district record (for example `district Seacoast Charter School`). Private schools (St. Patrick Academy, Portsmouth Christian Academy): `town Portsmouth` or the town where the school is, with the school named. No place for general NH rules.

All five agents write in `town/Portsmouth/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** the budget, taxes, tuition, cuts and buildings belong to agent 4; staffing and teacher pay to agent 5; the CTE Center and Lister to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Elementary schools, PEEP and the early years: redistricting, after-school care and waitlists, the kindergarten day, how the three schools compare, reading intervention, summer programs, military families arriving mid-year, PEEP, "Little Clipper" and speech services, art, music and outdoor time, volunteering and the PTA, getting from the bus or after-school program, elementary class sizes | `elementary-schools.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P6.1, P8.1, P8.3, P10.1, P10.2, P14.1, P14.3, P17.3, P18.2 |
| 2 | Portsmouth Middle, Portsmouth High, the CTE Center and Lister Academy: trades programs, hiring by the shipyard and local employers, the move to middle school, math grouping, AP and dual enrollment, phones, Great Bay classes for credit, financial literacy, hands-on programs and internships, Lister Academy, varsity cuts, the freshman transition, robotics and coding | `middle-high-and-cte.md` | `raw/high/` | P2.1, P2.3, P3.1, P3.2, P6.2, P6.3, P7.1, P9.2, P11.1, P11.2, P11.3, P12.2, P15.3 |
| 3 | Special education and student support: IEP follow-through, free and reduced-price meals, counselors and social workers at the middle school, bullying and social media, inclusion and belonging, the DEI law and clubs, English learner support, Spanish notices, the transition program to 21, special education funding and services, peer programs | `student-support.md` | `raw/support/` | P4.2, P4.3, P12.1, P12.3, P15.1, P15.2, P17.1, P17.2, P20.1, P20.2, P20.3 |
| 4 | Money, taxes, buildings and governance: budget growth, rent and school costs, health insurance and salaries, the tax cap and override, the sending towns' tuition, cuts to specialists, paras and the arts, per-pupil spending, state aid, judging the district beyond test scores, building condition and bonds, community use of the track and events | `money-buildings-and-governance.md` | `raw/money/` | P2.2, P4.1, P5.1, P5.2, P5.3, P8.2, P9.1, P9.3, P14.2, P16.1, P16.2, P16.3 |
| 5 | Getting to school, choices, community and staff: buses from Elwyn Park, early-release days, the high school start time, where Coast Guard families live, school community, private school enrollment and why families choose it, housing and enrollment projections, vouchers and EFAs for St. Patrick's, private and charter students returning to PHS, working for the district, paraprofessional and substitute openings, where teachers live | `getting-to-school-choices-and-staff.md` | `raw/daily/` | P3.3, P7.2, P7.3, P10.3, P13.1, P13.2, P13.3, P18.1, P18.3, P19.1, P19.2, P19.3 |
