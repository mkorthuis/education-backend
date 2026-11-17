# Hudson Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hudson and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hudson/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hudson

- **Hudson** is a town in Hillsborough County on the Merrimack River, across from Nashua, bordering Litchfield, Londonderry, Windham and Pelham and Massachusetts (Tyngsborough, Dracut). Site town id 267. It has a Board of Selectmen, a town administrator and a Budget Committee; the school district is separate.
- **Hudson School District** (site district id 267) is **SAU 81**, a one-district SAU. Use `district Hudson` for SAU-level facts too. It votes by official ballot (SB2): the 2026 deliberative session was Saturday, February 7, 2026, with a default budget if the proposed one fails.
- **Its schools** (site school ids):
  - **The Early Learning Center:** Library Street School (21075, kindergarten; full-day, 8:50 am start) and Dr. H. O. Smith Elementary (21045, grade 1).
  - **Preschool:** integrated classes at Nottingham West (29232).
  - **Grades 2–5:** Hills Garrison Elementary (27900) and Nottingham West Elementary (26765).
  - **Hudson Memorial School** (21060, grades 6–8).
  - **Alvirne High School** (21050, grades 9–12) with the **Wilbur H. Palmer Career and Technical Education Center**, which takes students from other districts (Merrimack's research has its admission terms), and the Alvirne Farm.
- **No other district sends Hudson students under contract** in `places.yaml`. Litchfield opened Campbell High School in the 2000s and stopped sending students to Alvirne; find when and why (P12.3).
- **Starting pages:** the district, https://www.sau81.org (board, budget, policies, schools, Palmer CTE); the town, https://www.hudsonnh.gov (elections, the Budget Committee, the tax rate, recreation, the library, police). Find where board and Budget Committee meetings are streamed (P9.3).
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 3,659 in 2014-15, 3,205 in 2019-20, 2,905 in 2025-26, a 21% drop (P1.1 says "roughly 25%").
  - Alvirne's enrollment (the site's school enrollment): 1,303 in 2015-16, 1,106 in 2019-20, 976 in 2024-25 (P12.1 says "under 1,000"; find a late-1990s figure from a district report).
  - Cost per pupil, FY2025: Hudson $19,704; state $22,699; Windham $19,690; Londonderry $21,196; Litchfield $21,147; Nashua $18,376.
  - Tax rates per $1,000 (NH DRA): 2025 total $17.11, local school $9.17, municipal $5.57 (2024: $16.45, $9.30, $4.97).
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Question 2 results, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/batch-5/hudson-*`: the district budget page, the Early Learning Center's pages, 2026 election information and results, the Library Street welcome for the class of 2036, the preschool and registration pages.
- **Library facts already loaded** (don't repeat them): full-day kindergarten at Library Street (`kindergarten-day-length`), the kindergarten cutoff, online registration, the integrated preschool at Nottingham West, and the SB2 vote and 2026 dates (`budget-form-and-vote-dates`). Read them: `grep -n -B2 -A10 "place: district Hudson" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** enrollment down "roughly 25%" while the budget rises every year (P1.1); voters rejecting the operating budget "again" (P1.3); "out-of-district special education placement costs eating up so much of the budget" (P2.3); "voters vote down warrant articles for teacher contracts" (P6.3); neighboring districts paying "significantly higher salaries" (P6.1); EFAs affecting Hudson's adequacy aid (P7.2).
- **Schools and programs:** the Palmer CTE Center renovations being complete (P3.1); block scheduling at Alvirne (P3.2); a competency-based grading system (P5.2); "Maroon and Gold days" (P16.2); before- and after-school care at the Early Learning Center (P4.1); Schoology for grades (P10.1); math scores lower than Windham's and Londonderry's (P4.2; the site's data); Alvirne's enrollment over 1,500 in the late 1990s (P12.1); Litchfield splitting off and "regional tuition agreements" (P12.3); bus routes consolidated for driver shortages (P13.3); paras pulled to cover substitute shortages (P15.2).

## Already researched, or being researched now

- **The Palmer CTE Center:** `town/Merrimack/high-school-and-pathways.md` (topic `cte-center-programs`) has six facts placed `district Hudson` on Palmer's programs and how Merrimack students are admitted. Read them, cite them, and add Hudson's own side: programs, credentials, the renovation, the advisory board and employer partners.
- **Comparisons:** `town/Londonderry/` has test-score and budget comparisons that include Hudson (`budget-and-governance.md`: tax rates against Hudson; `elementary-schools.md`); `town/Nashua/` has Nashua's schools, Bishop Guertin and the private and charter options near Nashua (`charter-private-and-home.md`).
- **Statewide rules already written.** Earlier towns and the library cover EFAs and school funding, home education access to classes and activities and the end of the yearly evaluation (July 1, 2026), special education, 504 plans and out-of-district placements, English learner services and translation, free and reduced-price meals, guardianship and custody paperwork, student records, phones, bullying, services owed to private school students, CTE admission (`cte-admission-and-cost-rules`), Early College (formerly Running Start), default budgets and tax caps. Read Manchester's `student-support.md` and `enrollment-and-choices.md`, Nashua's `special-education.md` and `families-and-support.md`, Concord's `families-and-support.md` and `special-education-and-health.md`, Dover's `money-buildings-and-governance.md` (tax cap mechanics) and Londonderry's `student-support-and-health.md` and `budget-and-governance.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place. Spend your time on Hudson's own schools, policies and programs.
- **Researched at the same time** (November 16, 2026): Hudson, Bedford, Keene, Portsmouth, Goffstown and Laconia. Don't write facts about the other five districts; where a question compares Hudson with one of them, use the site's data.

## Where facts go

- `district Hudson` for SAU 81, its schools, the Early Learning Center, Alvirne, the Palmer Center and the farm, programs, policies, staff, budget and board.
- `town Hudson` for town government and services: selectmen, the Budget Committee, the town's tax rate and budget, development and housing, police and SROs, recreation and youth leagues, the library.
- `district Litchfield` only for Litchfield's side of leaving Alvirne; another district's name only for that district's own side of an agreement.
- Private schools (Bishop Guertin and others): `town Hudson` with the school named in the statement, unless the site has a district record for it. No place for general NH rules.

All four agents write in `town/Hudson/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** the budget, taxes, warrants, contracts, default budget and capital reserves belong to agent 4; support staff pay and staffing to agent 3; Palmer and Alvirne programs to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | The Early Learning Center, the elementary schools and Hudson Memorial, daily life and choices: full-day kindergarten and before- and after-school care, math results and what the district is doing, elementary zones, home education access and returning, grandparents' authority and Schoology, homework help at Hudson Memorial, bullying that starts off campus, fees and waivers, bus consolidation, services and programs for private school students, inspecting curriculum, phones and smartwatches, Chromebook time | `schools-and-daily-life.md` | `raw/schools/` | P4.1, P4.2, P4.3, P7.1, P7.3, P10.1, P10.2, P10.3, P13.2, P13.3, P14.1, P14.3, P17.2, P20.1, P20.2 |
| 2 | Alvirne High School and the Palmer CTE Center: credentials and apprenticeships, the schedule and graduation requirements for CTE students, employer partners and co-ops, AP and Early College, grading and GPA, canceled electives, workplace and financial literacy, the advisory board, working papers and work-study, enrollment then and now and sports divisions, the Alvirne Farm, what keeps college-bound families, clubs, extracurricular funding, middle-to-high-school athletics | `alvirne-and-palmer-cte.md` | `raw/high/` | P3.1, P3.2, P3.3, P5.1, P5.2, P5.3, P11.1, P11.2, P11.3, P12.1, P12.2, P14.2, P16.3, P18.2, P18.3 |
| 3 | Special education, student support and support staff: special education staffing and IEP minutes, the move to Hudson Memorial, out-of-district placements and in-district programs, behavior and mental health support, ESOL at Nottingham West, translation, teacher training for multilingual learners, free and reduced-price meals, para, custodian and bus driver pay and vacancies, paras covering for substitutes, de-escalation training, sensory spaces at Alvirne, 504 plans, counselors, psychologists and social workers | `student-support-and-staff.md` | `raw/support/` | P2.1, P2.2, P2.3, P6.2, P8.1, P8.2, P8.3, P13.1, P15.1, P15.2, P15.3, P16.1, P16.2, P20.3 |
| 4 | Budget, taxes, governance and buildings: budget growth with falling enrollment, administration against instruction, the default budget, teacher pay against neighbors, failed contract articles and hiring, EFAs and adequacy aid, the school share of a tax increase, schools and home values, watching meetings, Litchfield's departure and tuition agreements, tax caps, vouchers, Alvirne's fields and facilities, the state funding formula, capital reserves and repairs, fund balance | `money-buildings-and-governance.md` | `raw/money/` | P1.1, P1.2, P1.3, P6.1, P6.3, P7.2, P9.1, P9.2, P9.3, P12.3, P17.1, P17.3, P18.1, P19.1, P19.2, P19.3 |
