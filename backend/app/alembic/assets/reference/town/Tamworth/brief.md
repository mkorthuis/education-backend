# Tamworth Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Tamworth and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Tamworth/questions.md` (P1.1 to P20.3).

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

## What you need to know about Tamworth

- **Tamworth** is in Carroll County, with the villages of Tamworth, Chocorua, South Tamworth, Whittier and Wonalancet, along Routes 16, 25 and 113. Site town id 525.
- **Tamworth School District** (site district id 525) runs the **Kenneth A. Brett School** (site school 20365), grades K–8. School site: https://sites.google.com/tamworth.k12.nh.us/welcome-ka-brett-school/home (pages for bus schedules, guidance, Kennett information, the High School Options Committee, staff, athletics, newsletters). The district holds a traditional annual meeting in the Brett School gym.
- **High school:** Kennett High School in Conway (site district 113, school 20345; SAU 9), with the Mount Washington Valley Career and Technical Center. A contract signed in 2024 lets **up to 6 Tamworth students** attend **Moultonborough Academy** (Moultonborough School District, site district 369, school 22120; SAU 45) starting September 2024. The Conway research found Tamworth had no Kennett contract for 2027 yet. Check both contracts' terms and dates.
- **SAU 13** (https://www.sau13.org/) serves Freedom, Madison and Tamworth. Its office is in Tamworth. Its preschool is at Madison Elementary.
- **Site data:** Tamworth's cost per pupil was $37,750 in FY2025 ($34,172 in FY2024). The site has Brett School's enrollment, test scores, class sizes, staff, salaries, free and reduced meals and safety counts, and everything for Kennett and Moultonborough Academy. DRA's 2025 rates for Tamworth (`additional-data/raw/town/dra-tax-rates.csv`) are 14.78 per $1,000 actual and 13.33 equalized.
- **Saved pages:** `additional-data/raw/districts/batch-7/` has `tamworth-brett-home`, `tamworth-hs-options-committee`, `tamworth-kennett-info` and the SAU 13 pages. `additional-data/district-practices.md` has Tamworth's registration, preschool and meeting facts.

## Several questions contain premises: check them

Questions mention Brett School enrollment of "around 165", an "8:1 student-teacher ratio", a "$13.33" tax rate, a "winter Friday ski/snowboard program at King Pine or Cranmore", an "Orton-Gillingham reading specialist", "a town that is over 90% white", Brett grades 6–8 band and chorus, an IEP handoff "in 8th grade" to Kennett, Moultonborough Academy as a choice with a "boundary and eligibility rule", "Carroll County Adult Education" classes in Tamworth, "Tamworth Learning Circles", The Community School's high school, Bearcamp Valley School's early childhood programs, and "remote-learning days". Treat each as something to verify. If a premise is wrong or out of date, state the correct fact plainly and neutrally, and list it under "Premises checked" in your summary.

## Already researched, or being researched now

**Kennett and the career center** were covered today. Map Kennett questions to existing facts first; gather new facts only for Tamworth angles and gaps.

| File | What it has |
|---|---|
| `town/sau9/kennett-and-sau9.md`, `town/sau9/kennett-pathways.md` | Kennett AP, STEM, outcomes, college persistence, ELOs, career center programs, capacity, credentials and co-ops, dual enrollment and Running Start, the Alternative Program, counseling, ski and outdoor programs |
| `town/Conway/schools-k-8.md`, `town/Conway/money-and-governance.md`, `town/Conway/daily-life.md` | Homeschoolers at KMS and Kennett, IEP moves, tuition from sending towns seen from Conway's side (Tamworth included), students by home district, Kennett late buses |
| `town/Jackson/after-jackson-grammar.md`, `town/Jackson/policies-safety-meals-and-support.md` | Kennett AP courses and scores, SAT, ninth-grade transition, counseling, Kennett phone procedure, sports fees |
| `town/Conway/community-and-choice.md`, `town/Jackson/community-and-families.md` | Private and charter options near Conway, EFA rules and valley providers, the July 2026 homeschool law change, Kennett local scholarships |

**SAU 13-wide facts are being gathered right now by the Madison research** (`town/Madison/`, five agents running at the same time as you). Don't research these; in your question table, write "SAU 13 fact: see Madison research" and move on:
- SAU 13's home education notice and evaluation process;
- SAU 13's free and reduced meal application process and McKinney-Vento and foster-care contacts;
- SAU 13's special education office and how therapists are shared across the three districts;
- the SAU 13 preschool;
- SAU 13's budget, apportionment, history and how the three boards work together;
- the NH law on voter approval of SAU administrator pay, if one exists.

Do research the Tamworth and Brett School side of each (for example, which Brett staff handle meal forms, or Tamworth's share of the SAU budget).

## Where facts go

- `district Tamworth` for the Brett School, the district's budget, contracts, board and enrollment.
- `town Tamworth` for town government and community facts.
- `sau 13` for SAU-wide facts you can't avoid (keep these few; see above).
- `district Conway` for new Kennett facts; `district Moultonborough` for Moultonborough Academy facts.
- No place for general NH rules.

All five agents write in `town/Tamworth/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Contradictions:** report anything that contradicts or fills a gap in the Jackson, Bartlett, Conway or SAU 9 files in your "For another file" section.

## Agent split

| Agent | Area | Output file | Raw folder |
|---|---|---|---|
| 1 | The Brett School: classes, reading and math support, special education staffing, arts and music, outdoor learning and ski program, counseling, bullying, phones, paras, behavior training, communication, partnerships | `town/Tamworth/brett-school.md` | `town/Tamworth/raw/school/` |
| 2 | Getting to school, the school day and family support: buses, storm days, after-school care, meals and backpacks, fees, moves and McKinney-Vento, late buses from Kennett | `town/Tamworth/getting-to-school-and-the-day.md` | `town/Tamworth/raw/daily/` |
| 3 | High school for Tamworth students: Kennett and Moultonborough Academy compared, the Brett-to-Kennett transition, career center, dual enrollment, guidance, ELOs, outcomes compared | `town/Tamworth/high-school.md` | `town/Tamworth/raw/high-school/` |
| 4 | Money and governance: budget, cost per pupil, tuition contracts and rates, Moultonborough eligibility, taxes, state and federal aid, capital plan, support staff pay, consolidation | `town/Tamworth/money-and-governance.md` | `town/Tamworth/raw/money/` |
| 5 | Community and families: town profile, housing, child care, private schools and co-ops, EFAs, recreation and summer, arts, adult education and workforce training, mental health access, food and church partnerships | `town/Tamworth/community-and-families.md` | `town/Tamworth/raw/community/` |
