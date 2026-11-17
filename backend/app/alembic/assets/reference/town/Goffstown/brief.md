# Goffstown Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Goffstown and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Goffstown/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Goffstown

- **Goffstown** is a town in Hillsborough County, west of Manchester, with the village, Pinardville (next to Manchester) and Grasmere; Saint Anselm College is in town and the Uncanoonuc Mountains overlook it. Site town id 199. It has a Board of Selectmen, a town administrator and a Budget Committee; the school district is separate.
- **Goffstown School District** (site district id 199) is in **SAU 19** with New Boston, sharing a superintendent. It votes by official ballot; the 2026 school election and warrant are in the library and the saved pages.
- **Its schools** (site school ids):
  - **Glen Lake School** (28525): the Glen Lake Preschool Program, a developmental preschool for three- and four-year-olds, and kindergarten, which the library says is half-day (morning and afternoon sessions) for 2026-27. Check for any change.
  - **Grades 1–4:** Bartlett Elementary (20695, in Pinardville) and Maple Avenue (20690, in the village).
  - **Mountain View Middle School** (26820, grades 5–8) and **Goffstown High School** (20700, grades 9–12).
- **Sending districts** (`places.yaml`): **New Boston** sends grades 7–12 to Mountain View and Goffstown High under an AREA agreement from July 1, 2024 to June 30, 2034 (renewed by both districts' voters in March 2022; saved, below). **Hooksett** students may attend Goffstown High by petition, under a 2023–2028 memorandum, with Hooksett paying Pinkerton's rate.
- **Career and technical education:** Goffstown students attend the Manchester School of Technology's CTE programs (Manchester's research covers MST, its application for students from Bedford, Goffstown and other districts, and its programs).
- **Starting pages:** SAU 19 and the district, https://www.sau19.org (schools, the board, the budget and finance documents, policies); the town, https://goffstownnh.gov (selectmen, the Budget Committee, the tax rate, recreation, the library, police).
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 2,222 in 2014-15, 2,301 in 2019-20, 2,242 in 2025-26.
  - Goffstown High's enrollment: 1,107 in 2015-16, 1,071 in 2019-20, 1,003 in 2024-25 (including New Boston's students).
  - Cost per pupil, FY2025: Goffstown $17,811; state $22,699; New Boston $20,442; Bedford $19,650; Hooksett $17,848; Manchester $18,020 (P3.2 says Goffstown spends less than most towns: the site's data can rank it).
  - Tax rates per $1,000 (NH DRA): 2025 total $20.88, local school $11.59, municipal $7.02 (2024: $20.44). P3.1 says the rate "just jumped to $21.75": check whether that is the 2026 rate.
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Question 2 results, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/batch-7/goffstown-*`: the 2026 sample school ballot, both AREA agreement copies (2024–2034), finance documents, Glen Lake's pages and principal's message, the home page, kindergarten registration (district and SAU pages), the preschool pages and the 2026 town meeting guide.
- **Library facts already loaded** (don't repeat them): half-day kindergarten at Glen Lake, the kindergarten cutoff, kindergarten registration, the Glen Lake Preschool Program, and the official ballot vote. Read them: `grep -n -B2 -A10 "place: district Goffstown" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** a $21.75 tax rate and how much of the increase is the schools' (P3.1); a tax cap on the schools (P3.2, P8.3; the site's Question 2 data and the district's ballot); "the new superintendent coming in" (P3.3); the budget rising while enrollment "isn't exploding" (P8.1); building bonds coming (P12.3); New Boston's "fair share" and when the AREA agreement comes up (P15.3; it runs to 2034); losing teachers to Bedford and Londonderry for pay (P15.1; the site's salary schedules).
- **Schools and programs:** full-day kindergarten at Glen Lake (P1.1; the library says half-day); Bartlett's test scores "so much lower" than Maple Avenue's (P2.1, P12.2; the site's data); New Boston students crowding Mountain View and GHS (P7.1); a daily bus to MST and "two-year" MST programs (P5.1, P5.2); "28 to a room" in grades 5–8 (P19.2; the site's class sizes); locked entryways and resource officers in every elementary school (P15.2); a 3:30 pickup and a late bus for 5th graders (P17.3); combined bus routes for a driver shortage (P18.3); Glen Lake's preschool being "mostly for kids with delays" (P16.1); a gifted program (P16.3).

## Already researched, or being researched now

No earlier town is in SAU 19.
- **The Manchester School of Technology:** `town/Manchester/mst-and-pathways.md` has MST's programs, its application (with a form for Goffstown and other districts' students), credentials and schedule. Cite it, and add only Goffstown's side: transportation, credits at GHS, how many Goffstown students attend, and how homeschoolers apply through Goffstown.
- **Hooksett's petition to Goffstown High:** in `places.yaml`; `town/Londonderry/` and `town/Derry/` cover Hooksett's other options.
- **Manchester's charters, Catholic schools and the Derryfield School:** `town/Manchester/charter-schools.md` and `enrollment-and-choices.md`.
- **Statewide rules already written.** Earlier towns and the library cover EFAs and school funding (including EFA students and sports), home education access to classes and activities and the end of the yearly evaluation (July 1, 2026), special education, 504 plans and out-of-district placements, English learner services and translation, free and reduced-price meals, guardianship and custody paperwork, student records, phones, bullying, transportation to private schools (RSA 189:9), CTE admission (`cte-admission-and-cost-rules`), Early College and dual enrollment (formerly Running Start), default budgets and tax caps. Read Manchester's `student-support.md` and `enrollment-and-choices.md`, Nashua's `special-education.md` and `families-and-support.md`, Concord's `families-and-support.md` and `special-education-and-health.md`, Dover's `money-buildings-and-governance.md` (tax cap mechanics) and Londonderry's `student-support-and-health.md` and `budget-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place. Spend your time on Goffstown's own schools, policies and programs.
- **Researched at the same time** (November 16, 2026): Hudson, Bedford, Keene, Portsmouth, Goffstown and Laconia. Don't write facts about the other five districts; where a question compares Goffstown with Bedford, use the site's data.

## Where facts go

- `district Goffstown` for the Goffstown School District, its schools, Glen Lake, programs, policies, staff, budget and board.
- `sau 19` for facts that apply to both SAU 19 districts: SAU-wide policies, the superintendent's office and its cost, shared staff and services. Write them in your own file in `town/Goffstown/`; a later New Boston study will read them there.
- `district New Boston` for New Boston's side of the AREA agreement and its tuition payments; `district Hooksett` for Hooksett's petition terms.
- `town Goffstown` for town government and services: selectmen, the Budget Committee, the town's tax rate and budget, housing, police and SROs, recreation, the library.
- `district Manchester` only for an MST fact Manchester's research doesn't have. Private schools (the Derryfield School has a site record: `district The Derryfield School`; Catholic schools in Manchester: `town Manchester` with the school named). No place for general NH rules.

All four agents write in `town/Goffstown/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** the budget, taxes, tax cap, AREA tuition, bonds, contract, teacher pay and building security belong to agent 4; buses and bell times to agent 3; MST to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Glen Lake, the elementary schools, special education and family support: kindergarten's day length, registration and care, Bartlett against Maple Avenue and reading help, after-school tutoring at Bartlett, paraprofessionals and IEP support, the move to Mountain View for students with IEPs, out-of-district placements, Spanish-speaking staff, the preschool and who qualifies, English learner support, the Pinardville schools' reputation, meals without stigma, nurses, public pre-K for typically developing children, gifted programs | `elementary-and-special-education.md` | `raw/elementary/` | P1.1, P1.2, P2.1, P2.3, P6.1, P6.2, P6.3, P9.1, P9.2, P9.3, P12.2, P13.3, P14.3, P16.1, P16.3 |
| 2 | Mountain View, Goffstown High and MST: AP and honors, math tracks at Mountain View, college admissions against Bedford, MST transportation, credits and credentials, personal finance and trades, hockey and booster costs, academic eligibility, dual enrollment with Manchester Community College, FAFSA and scholarship help, mid-year placement, class sizes in grades 5–8, help for students not going to a four-year college, career center and counselors for recent graduates | `mountain-view-high-school-and-mst.md` | `raw/high/` | P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P8.2, P10.1, P10.2, P18.1, P18.2, P19.1, P19.2, P20.1, P20.2 |
| 3 | Getting to school, safety, climate and choices: the bus to Glen Lake, moving within Pinardville, phones, part-time classes and activities for homeschoolers, EFAs and sports, homeschoolers and MST, guardianship paperwork, counselors and social workers at Mountain View, bus times and middle school start times, mental health and bullying, school boundaries, two-hour delays and early drop-off, notice of early release, the late bus, bus driver shortages, transportation to private schools | `getting-to-school-and-choices.md` | `raw/daily/` | P1.3, P2.2, P7.2, P11.1, P11.2, P11.3, P13.1, P13.2, P14.1, P14.2, P16.2, P17.1, P17.2, P17.3, P18.3, P19.3 |
| 4 | Money, governance, buildings and staff: the tax rate and the school share, the tax cap and spending, the superintendent and central office, New Boston and space, parents' say in an SAU shared with New Boston, budget growth, what a cap would cut, the high school's fields and gym, schools and home values, bonds, the teachers' contract and turnover, building security and SROs, the AREA agreement's terms, how to see the board's votes | `money-buildings-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P7.1, P7.3, P8.1, P8.3, P10.3, P12.1, P12.3, P15.1, P15.2, P15.3, P20.3 |
