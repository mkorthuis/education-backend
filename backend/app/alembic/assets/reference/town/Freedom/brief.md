# Freedom Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Freedom and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Freedom/questions.md` (P1.1 to P20.3).

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

## What you need to know about Freedom

- **Freedom** is in Carroll County, on Ossipee Lake (Danforth Bay), Loon Lake and the Maine border (Porter and Parsonsfield), off Routes 153 and 25. Site town id 187.
- **Freedom School District** (site district id 187) runs **Freedom Elementary School** (site school 20350), grades K–6, at 40 Loon Lake Road. Its students in grades 7–12 attend Conway's A. Crosby Kennett Middle School (KMS, site school 27010) and Kennett High School (20345), with the Mount Washington Valley Career and Technical Center. The Conway research found Freedom and Madison students join KMS in grade 7, and that Freedom, Madison and Tamworth had no Kennett contract for 2027 yet.
- **High school options study:** `additional-data/raw/districts/batch-7/freedom-middle-high-options-comparisons.pdf` (text in `.txt`) is the administration's "High School Options Preliminary Comparisons" for the Freedom board. It compares Kennett, Moultonborough Academy, Kingswood Regional, Fryeburg Academy, Inter-Lakes and Sacopee Valley, and says "The current tuition agreement is due to expire in 2027 with notification to exit the agreement in 2024. Each town approved the article and developed their own committee of three." Find out what happened next.
- **SAU 13** (https://www.sau13.org/) serves Freedom, Madison and Tamworth. Its preschool is at Madison Elementary.
- **Site data:** Freedom's cost per pupil was $41,267 in FY2025 ($35,274 in FY2024). The site has Freedom Elementary's enrollment, test scores, class sizes, staff, salaries, free and reduced meals and safety counts, and everything for KMS and Kennett. DRA's 2025 rates for Freedom (`additional-data/raw/town/dra-tax-rates.csv`) are 7.39 per $1,000 actual and 7.20 equalized.
- **Saved pages:** `additional-data/raw/districts/batch-7/` has `freedom-home`, `freedom-agendas`, `freedom-registration`, `freedom-kindergarten-packet` and the SAU 13 pages. `additional-data/district-practices.md` has Freedom's registration and preschool facts.

## Several questions contain premises: check them

Questions mention Freedom Elementary "under 60 students", "multi-grade" and "multi-age" classrooms, a "class of 8–10 kids", Freedom "6th graders" merging at KMS (check whether they join in grade 7), a KMS grade "of over 100 students", Freedom's "volunteer fire/EMS", a "King Pine" ski program, band instrument rentals at Freedom Elementary, Fryeburg Academy eligibility, the "current long-term agreement with the Conway School District", Freedom's buses carrying grades 7–12 to Conway ("bus fuel and fleet"), and the school's use as an emergency shelter. Treat each as something to verify. If a premise is wrong or out of date, state the correct fact plainly and neutrally, and list it under "Premises checked" in your summary.

## Already researched, or being researched now

**Kennett, KMS and the career center** were covered today. Map those questions to existing facts first; gather new facts only for Freedom angles and gaps.

| File | What it has |
|---|---|
| `town/Conway/schools-k-8.md` | KMS grade 6 and the students who join in grade 7 (Freedom and Madison), KMS accelerated math, special education and IEP moves to KMS, counseling, bullying policy, homeschoolers at KMS and Kennett |
| `town/Conway/money-and-governance.md`, `town/Conway/daily-life.md` | Tuition from sending towns seen from Conway's side (Freedom included), students by home district (March 2026), Kennett late buses, storm days |
| `town/sau9/kennett-and-sau9.md`, `town/sau9/kennett-pathways.md` | Kennett AP, STEM, outcomes, college persistence, ELOs, career center programs, capacity, credentials and co-ops, dual enrollment and Running Start, the Alternative Program and credit recovery, counseling and the student assistance program |
| `town/Jackson/after-jackson-grammar.md`, `town/Jackson/policies-safety-meals-and-support.md` | Kennett AP courses and scores, SAT, ninth-grade transition, Kennett phone procedure, sports fees |
| `town/maine/fryeburg-academy.md` (being written now) | Fryeburg Academy, from the Chatham research |

**SAU 13-wide facts are being gathered now by the Madison research** (`town/Madison/`). Don't research these; in your question table, write "SAU 13 fact: see Madison research" and move on:
- SAU 13's home education notice and evaluation process;
- SAU 13's free and reduced meal application process and McKinney-Vento and foster-care contacts;
- SAU 13's special education office and how therapists and counselors are shared across the three districts;
- the SAU 13 preschool;
- SAU 13's budget, apportionment, history and how the three boards work together.

**Tamworth** is also being researched now (`town/Tamworth/`), including the Moultonborough Academy option. Do research the Freedom side of each item (for example, which specialists are at Freedom Elementary, or Freedom's share of the SAU budget).

## Where facts go

- `district Freedom` for Freedom Elementary, the district's budget, contracts, board and enrollment.
- `town Freedom` for town government and community facts.
- `sau 13` for SAU-wide facts you can't avoid (keep these few; see above).
- `district Conway` for new KMS and Kennett facts.
- No place for general NH rules.

All four agents write in `town/Freedom/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Contradictions:** report anything that contradicts or fills a gap in the Jackson, Bartlett, Conway or SAU 9 files in your "For another file" section.

## Agent split

| Agent | Area | Output file | Raw folder |
|---|---|---|---|
| 1 | Freedom Elementary: classes and multi-grade grouping, curriculum and reading, enrichment, special education staffing, counseling, outdoor learning, devices, fees, safety, partnerships | `town/Freedom/freedom-elementary.md` | `town/Freedom/raw/school/` |
| 2 | Getting to school and the move to Kennett: buses and late buses, storms, care, summer programs and meals, the grade 7 move and IEP transfer, Kennett programs and supports for Freedom students | `town/Freedom/getting-to-school-and-kennett.md` | `town/Freedom/raw/daily/` |
| 3 | Money and governance: budget, cost per pupil, Kennett agreement and its 2027 renewal, high school options study, taxes, adequacy, special education costs, capital, transport costs, salaries, SAU and consolidation, public input | `town/Freedom/money-and-governance.md` | `town/Freedom/raw/money/` |
| 4 | Community and families: town profile and enrollment outlook, housing, child care, EFAs, PTO and community groups, food help, scholarships, police, fire and EMS, the school as a civic space and shelter, broadband | `town/Freedom/community-and-families.md` | `town/Freedom/raw/community/` |
