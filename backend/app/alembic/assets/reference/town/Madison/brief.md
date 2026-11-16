# Madison Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Madison and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Madison/questions.md` (P1.1 to P20.3).

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

## What you need to know about Madison

- **Madison** is in Carroll County, south of Conway on Routes 16 and 113, with Silver Lake, the Eidelweiss lake community, Madison Corner and the Madison Boulder. Site town id 333.
- **Madison School District** (site district id 333) runs **Madison Elementary School** (site school 20360), grades K–6, which also hosts the **SAU 13 preschool** for children from Freedom, Madison and Tamworth. School site: https://sites.google.com/a/mes-nh.com/madison-elementary-school/ (check for a newer one). The district votes by official ballot (SB2), with a deliberative session and a March ballot.
- **Grades 7–12** attend Conway's A. Crosby Kennett Middle School (KMS, site school 27010) and Kennett High School (site school 20345), with the Mount Washington Valley Career and Technical Center. Check the contract: its term, formula and dates. The Conway research found that Madison and Freedom students join KMS in grade 7 and that Madison, Freedom and Tamworth had no Kennett contract for 2027 yet. Check that.
- **SAU 13** (https://www.sau13.org/) serves Freedom (Freedom Elementary, school 20350), Madison and Tamworth (Kenneth A. Brett School, 20365), with a central office in Tamworth. Kennett and KMS are in **SAU 9**, a different SAU, so Madison families deal with two SAUs.
- **Site data:** Madison's cost per pupil was $35,063 in FY2025 ($33,750 in FY2024). The site also has Madison Elementary's enrollment, test scores, class sizes, staff, salaries, free and reduced meals and safety counts, and everything for KMS and Kennett. DRA's 2025 rates for Madison are in `additional-data/raw/town/dra-tax-rates.csv`: total 8.98 per $1,000, equalized 9.02, after a 2025 revaluation.
- **Saved SAU 13 pages:** `additional-data/raw/districts/batch-7/` has `sau13-home`, `sau13-annual-reports`, `sau13-preschool`, `sau13-student-registration`, `madison-home`, `madison-agendas`, `madison-kindergarten-packet`, Freedom's middle and high school options comparison, and Tamworth's high school options committee and Kennett info. `additional-data/district-practices.md` has Madison's kindergarten registration, SB2 status, preschool and its residency form.

## Several questions contain premises: check them

Questions mention an "~11:1 student-teacher ratio", grade cohorts of "11 to 26", "~125 students" and "120–130 students", "lottery odds" for an "integrated Pre-K", Madison's SAS scores trailing the state, "only two licensed childcare facilities in Madison", a "$9.02/thousand tax rate", a "~$250k+ share of the SAU #13 central office budget", "New Hampshire's recent law allowing voters to veto SAU administrator pay increases", a "10-year tuition contract with Conway", Madison students joining KMS "in 7th grade", "elementary enrollment is half what it was a generation ago", "joint board meetings", "Lakes Region Community College" Running Start, and the gym as the site of Town Meeting and the Deliberative Session. Treat each as something to verify. If a premise is wrong or out of date, state the correct fact plainly and neutrally, and list it under "Premises checked" in your summary.

## Already researched: read before you search

Madison's grades 7–12 attend Conway's schools, which today's research covered. **Map each Kennett and KMS question to existing facts first; gather new facts only for Madison angles and gaps.**

| File | What it has |
|---|---|
| `town/Conway/schools-k-8.md` | KMS grade 6 and the students who join in grade 7 (Madison and Freedom), KMS accelerated math and no gifted program, special education and IEP moves to KMS, English learners, counseling, bullying policy, homeschoolers at KMS and Kennett |
| `town/Conway/money-and-governance.md`, `town/Conway/daily-life.md` | Tuition from sending towns seen from Conway's side, students by home district (March 2026), Conway's buses and late buses, calendar, storm days |
| `town/sau9/kennett-and-sau9.md`, `town/sau9/kennett-pathways.md` | Kennett AP, STEM, outcomes, college persistence, ELOs, career center programs, capacity, credentials and co-ops, dual enrollment and Running Start, the Alternative Program, counseling, ski and outdoor programs |
| `town/Jackson/after-jackson-grammar.md`, `town/Jackson/money-and-governance.md` | Kennett's AP courses and scores, SAT, college plans, early credit, the 2021–22 cooperative study, Kennett contract formulas from the sending towns' side |
| `town/Conway/community-and-choice.md`, `town/Jackson/community-and-families.md` | Private and charter options near Conway, EFA rules and valley providers, the July 2026 homeschool law change, child care near Conway, Kennett local scholarships |
| `town/maine/` (being written now) | Fryeburg Academy research from the Chatham study; point to it |

Also in the library (`additional-data/`): statewide NH rules on residency, tuition, special education, home education, EFAs, default budgets, SAU budgets, adequacy and the statewide education property tax. Grep the topic list before writing a rule.

## Where facts go

- `district Madison` for Madison Elementary, the district's budget, contracts, board and enrollment.
- `town Madison` for town government and community facts.
- `sau 13` for SAU-wide facts: SAU 13 policies, special education office, preschool rules, central office budget, calendar, homeschool process. Freedom and Tamworth will use them later.
- `district Conway` for new facts about KMS and Kennett that earlier files lack.
- No place for general NH rules.

All five agents write in `town/Madison/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Contradictions:** report anything that contradicts or fills a gap in the Jackson, Bartlett, Conway or SAU 9 files in your "For another file" section.

## Agent split

| Agent | Area | Output file | Raw folder |
|---|---|---|---|
| 1 | Madison Elementary School: programs, staff, class sizes, enrichment, special education, English learners, counseling, preschool, test results, curriculum, safety, volunteers | `town/Madison/madison-elementary.md` | `town/Madison/raw/school/` |
| 2 | Getting to school, the school day and SAU 13 policies: buses, late buses, calendars, care, ESY, meals and fee waivers, homeschool process, foster and homeless students, enrollment | `town/Madison/getting-to-school-and-policies.md` | `town/Madison/raw/daily/` |
| 3 | Kennett Middle and High for Madison students: the grade 7 move, IEP transfer between SAUs, KMS programs, career center access, dual enrollment, outcomes, counseling, ELOs, private comparisons | `town/Madison/kennett-for-madison.md` | `town/Madison/raw/kennett/` |
| 4 | Money and governance: budget, default budget, Kennett contract, special education costs, cost per pupil, taxes, SWEPT, exemptions, SAU 13 budget and history, capital, salaries and para pay, public input | `town/Madison/money-and-governance.md` | `town/Madison/raw/money/` |
| 5 | Community and families: town profile, housing, child care, EFA options, broadband, scholarships, food and church partnerships, local history, civic spaces, police and fire | `town/Madison/community-and-families.md` | `town/Madison/raw/community/` |
