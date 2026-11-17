# Keene Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Keene and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Keene/questions.md`: 20 profiles and 60 questions, shared by five agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Keene

- **Keene** is a city in Cheshire County in the Monadnock Region of southwestern New Hampshire, home of Keene State College and Cheshire Medical Center. Site town id 279. It has a mayor and city council; the school district is separate, with its own school board.
- **Keene School District** (site district id 279) is in **SAU 29**, which also serves Chesterfield, Harrisville, Marlborough, Marlow, Nelson and Westmoreland. It has used the official ballot (SB2) since 1997; its 2026 deliberative session was February 7 at Keene High.
- **Its schools** (site school ids):
  - **Jonathan Daniels School** (29180): the Jonathan Daniels Preschool, integrated and play-based, for ages 3 and 4, with morning and afternoon sessions (library fact).
  - **Kindergarten to grade 5:** Franklin (21190), Fuller (21165), Symonds (21170) and Wheelock (21200). The question says "Benjamin Franklin Elementary"; check the school's name.
  - **Keene Middle School** (21185, grades 6–8) and **Keene High School** (21195, grades 9–12) with the **Cheshire Career Center**, a regional career and technical center.
- **Sending towns** (`places.yaml`): Chesterfield, Harrisville, Marlborough, Marlow, Nelson, Westmoreland and Stoddard send students to Keene High under the Keene AREA (since 1966, amended in 2024-25 for a 20-year term), and several send grades 6–8 to Keene Middle (a grade 6 AREA since 2018, grades 7–8 since 1973).
- **Charter and private schools in Keene:** Gathering Waters Charter School (Waldorf-inspired; site district 750) and Making Community Connections Charter School (MC2; site district 733); St. Joseph Regional School (Catholic, K–8). Our Lady of Mercy Academy is named in a question; find where it is.
- **Keene Community Education** offers adult classes; find who runs it and what it offers now. Keene State College's Accelerated High School Program is in the library (`keene-state-accelerated-high-school`).
- **Starting pages:** the district, https://www.keeneschoolsnh.org (schools, the board, the budget, policies, SAU 29); the city, https://keenenh.gov (city council, tax rate, recreation, the library, police).
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 2,550 in 2014-15, 2,485 in 2019-20, 2,339 in 2025-26.
  - Keene High's enrollment: 1,363 in 2015-16, 1,364 in 2019-20, 1,280 in 2024-25 (including students from the sending towns).
  - Cost per pupil, FY2025: Keene $20,358; state $22,699; Chesterfield $23,686; Harrisville $36,960; Marlborough $24,942; Nelson $26,634; Westmoreland $22,218.
  - Tax rates per $1,000 (NH DRA): 2025 total $34.37, local school $15.93, municipal $13.61 (2024: $33.07, $15.16, $13.31).
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Question 2 results, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them. Check Keene's Question 2 result in the site's data before writing about P1.2 and P18.1.
- **Saved pages:** `additional-data/raw/districts/batch-4/keene-*`: the four elementary handbooks (Franklin, Fuller, Symonds, Wheelock), Jonathan Daniels' handbook, home and enrollment pages, kindergarten registration, Keene High's about page, the district home page, the official ballot page and the policies (with JEB).
- **Library facts already loaded** (don't repeat them): kindergarten hours (the Symonds handbook), the kindergarten cutoff, Jonathan Daniels Preschool, the SB2 vote and 2026 dates, and Keene State's Accelerated High School Program. Read them: `grep -n -B2 -A10 "place: district Keene" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** the Question 2 tax cap and "the 4% of the budget that isn't locked in" (P1.2, P18.1); the school tax rising while enrollment shrinks (P2.1); "safety renovations" at Keene High and their cost (P2.2, P14.3); tuition from the sending towns not covering the cost (P2.3); "cutting 'discretionary' spending" (P19.2); no plain-English budget dashboard (P18.3).
- **Schools and programs:** "Benjamin Franklin Elementary" and a 2:40 p.m. pickup (P3.1); "Cheshire Center Preschool" and an "SAU 29 preschool" waitlist (P1.3); full-day pre-K (P16.3); elementary Spanish down to "one teacher for 400 kids" (P10.2); a "remote evaluation idea" for special education evaluations taking months (P6.1); Career Center programs only from junior year (P5.1); a walking-distance cutoff for buses (P3.3); different early-release and snow-day rules for elementary and middle school (P16.2); an "annual homeschool portfolio" evaluation (P13.3; New Hampshire repealed the yearly evaluation on July 1, 2026); GreatSchools ratings (P7.2): report what the rating sites show and how they compute it, plainly and without judging.

## Already researched, or being researched now

No earlier town is in SAU 29, and no earlier town sends students to Keene.
- **Career and technical centers elsewhere:** Dover's (`town/Dover/high-school-and-ctc.md`), Concord's and Salem's research show how other regional centers admit students and which credentials they offer; use them for the format, not as Keene facts.
- **Charter school rules** (lotteries, transportation, special education responsibility for charter students): `town/Manchester/charter-schools.md` and `town/Nashua/charter-private-and-home.md` cover the state rules; cite them.
- **Statewide rules already written.** Earlier towns and the library cover EFAs and their eligibility, school funding, home education access to classes and activities and the end of the yearly evaluation (July 1, 2026), special education, 504 plans, English learner services and translation, free and reduced-price meals, guardianship and custody paperwork, student records, bullying notification (RSA 193-F), transfer credits, CTE admission (`cte-admission-and-cost-rules`), Early College (formerly Running Start), default budgets and tax caps. Read Manchester's `student-support.md` and `enrollment-and-choices.md`, Nashua's `special-education.md` and `families-and-support.md`, Concord's `families-and-support.md` and `special-education-and-health.md`, Dover's `money-buildings-and-governance.md` (tax cap mechanics) and Londonderry's `student-support-and-health.md` and `budget-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place. Spend your time on Keene's own schools, policies and programs.
- **Researched at the same time** (November 16, 2026): Hudson, Bedford, Keene, Portsmouth, Goffstown and Laconia. Don't write facts about the other five districts.

## Where facts go

- `district Keene` for the Keene School District, its schools, the Cheshire Career Center, programs, policies, staff, budget and board.
- `sau 29` for facts that apply to every SAU 29 district: SAU-wide policies, the superintendent's office, shared staff and services. Write them in your own file in `town/Keene/` (SAU 13's facts sit in `town/Madison/` the same way); a later SAU 29 town will read them there.
- `town Keene` for city government and services: the city council, the city's tax rate and budget, housing, police, recreation, the library.
- `district Chesterfield`, `district Marlborough`, `district Nelson` and the other sending districts for their own schools and their side of the AREA agreement (P7.1 compares their elementary schools).
- Charter schools: `district Gathering Waters Charter School`, `district Making Community Connections Charter School`. Private schools (St. Joseph Regional, Our Lady of Mercy): `town Keene` with the school named, or the town where the school is. Keene State College and Keene Community Education: `town Keene` unless the program is the school district's. No place for general NH rules.

All five agents write in `town/Keene/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** the budget, taxes, tax cap, tuition, building projects and SAU 29 comparisons belong to agent 5; staffing and pay to agent 3; the Cheshire Career Center's programs to agent 2, and its access for charter, private and home-educated students to agent 4. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Elementary schools, the early years and daily life: how the four elementary schools differ, preschool waitlists and Jonathan Daniels, after-school care at Franklin, reading intervention, meals and walking distance for buses, rating sites, elementary Spanish and world languages, guardianship paperwork, paper copies and phone contact, recess and outdoor time, early release and snow days, full-day pre-K, choosing an elementary zone | `elementary-schools-and-daily-life.md` | `raw/elementary/` | P1.1, P1.3, P3.1, P3.2, P3.3, P7.2, P10.2, P15.1, P15.2, P16.1, P16.2, P16.3, P20.1 |
| 2 | Keene Middle, Keene High and the Cheshire Career Center: AP and honors STEM, dual enrollment at Keene State and online, behavior at KMS, Career Center access in grade 9, credentials and local contractors, the trades and college prep, homework clubs and late buses, smaller programs inside KHS, financial aid and FAFSA help, homework load, day-to-day safety, computer science, welcoming new students, mid-year transfer credits and spring sports | `middle-high-and-career-center.md` | `raw/high/` | P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P10.3, P11.3, P14.1, P14.2, P14.3, P18.2, P20.2, P20.3 |
| 3 | Special education, student support and staff: evaluation timelines and remote evaluations, paraprofessionals at Wheelock, the move from Wheelock to KMS, starting teacher pay and mentoring, substitute and paraeducator shortages, collaboration time, translation of notices and IEP paperwork, bullying notification, para and bus driver hiring, support for teachers with behavior | `student-support-and-staff.md` | `raw/support/` | P6.1, P6.2, P6.3, P9.1, P9.2, P9.3, P10.1, P15.3, P19.1, P19.3 |
| 4 | Charters, private schools, home education and adult learning: special education at Gathering Waters, moving from Waldorf to KHS, charter lotteries and busing, how MC2 works and its diploma, MC2 students at KHS sports and the Career Center, EFA eligibility for St. Joseph's and Our Lady of Mercy, moving from St. Joe's to KHS, private school students on middle school teams, placing a homeschooled student, part-time classes for homeschoolers, homeschool evaluations, Keene Community Education's career classes, free English and computer classes for adults, whether certificates are recognized | `choices-and-adult-learning.md` | `raw/choices/` | P8.1, P8.2, P8.3, P11.1, P11.2, P12.1, P12.2, P12.3, P13.1, P13.2, P13.3, P17.1, P17.2, P17.3 |
| 5 | Money, taxes, SAU 29 and buildings: the tax cap and specials, the school tax with shrinking enrollment, Keene High's renovations and their cost, sending towns' tuition against the cost, the SAU 29 towns' elementary schools, Keene's taxes against nearby towns, tax caps and rents, a budget dashboard, discretionary cuts | `money-sau29-and-buildings.md` | `raw/money/` | P1.2, P2.1, P2.2, P2.3, P7.1, P7.3, P18.1, P18.3, P19.2 |
