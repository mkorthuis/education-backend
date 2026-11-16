# Albany Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Albany and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Albany/questions.md` (P1.1 to P20.3).

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

## What you need to know about Albany

- **Albany** is a rural Carroll County town west and south of Conway. Most of its land is White Mountain National Forest; the Kancamagus Highway (Route 112) runs through it to Passaconaway, and Route 16 crosses its eastern edge near the Conway line. Site town id 5.
- **Albany School District** (site district id 5) runs no schools. It holds a traditional annual district meeting (2026: officers elected March 10 at the Town Hall, business meeting 7 pm). Its board page is https://www.sau9.org/albany: it "meets on the second Tuesday of every other month at 5:30 p.m. at the Albany Town Hall" and lists three members, one of them in a one-year appointed term. Policies, agendas, minutes, annual reports and warrants are in Google Drive folders linked from that page.
- **Where students go:** SAU 9's tuition page (https://www.sau9.org/tuitions) lists Albany–Conway contracts for K–6, 7–8 and 9–12, with new 7–8 and 9–12 contracts starting in 2027-28. Saved copies are scans: `additional-data/raw/districts/batch-1/sau9-contract-k-6-albany-conway-current.pdf` and `sau9-contract-9-12-albany-conway-current.pdf` (no 7–8 copy saved). Conway's schools, with site school ids: Pine Tree Primary (K–2, 29272), Conway Intermediate (3–5, 29271), A. Crosby Kennett Middle (6–8, 27010), Kennett High (9–12, 20345), and the career center at Kennett.
- **Site data:** the site has no cost per pupil for Albany (the rows are empty). It has adequacy aid rows, EFA counts by town and Question 2 votes for Albany, and everything for Conway's schools.
- **SAU 9** (https://www.sau9.org/) serves Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location and Jackson.

## Several questions contain premises: check them

Questions mention "Pine Tree Elementary or Conway Elementary", a "K–6" contract (Conway's grade 6 is now at Kennett Middle), "5- and 8-year" agreements and an "8-year K–6 contract", annual tuition "true-up" bills and credits, an Albany "RSA 194-D open-enrollment policy capping town-funded transfers", Albany's "high poverty rate", a "phase-out of Hold Harmless grants and shift toward Equalized Valuation per Free & Reduced Meal student", "remote learning days" in storms, Albany having no Fryeburg Academy contract, and a "three-person board". Treat each as something to verify. If a premise is wrong or out of date, state the correct fact plainly and neutrally, and list it under "Premises checked" in your summary.

## Already researched: read before you search

Albany's students attend Conway's schools, and Conway was researched today. Most school-side questions are already answered. **Your first job is to map each assigned question to existing facts; gather new facts only for what is missing or Albany-specific.** Name existing facts in your question table (for example "Conway file: district-school-day-and-calendar #4" or "sau9 file: cte-center-programs #12").

| File | What it has |
|---|---|
| `town/Conway/schools-k-8.md` | Grade regrouping and school names, kindergarten, staffing and cuts, KMS grade 6 and students joining in grade 7, reading support, accelerated math and the absence of a gifted program, special education at K–8 and the move to KMS, English learners, counseling and family liaisons, bullying policy, recess and ski days, homeschoolers at KMS and Kennett, class size compared |
| `town/Conway/daily-life.md` | Buses and route times (derived ride-time table), school hours, Project SUCCEED care, conferences, storm days and absences, meals and applying when income drops, summer meals, family notices and interpreters, Chromebooks and device fees, foster care, weekend food |
| `town/Conway/money-and-governance.md` | Conway's budget and default budgets, special education spending, staffing cuts, tax and state aid, tuition from sending towns seen from Conway's side (Albany included), students by home district (March 2026), the KMS capital plan and trust funds, para pay |
| `town/Conway/community-and-choice.md` | Private and charter options, home education in SAU 9, independent evaluations and related services, homeless and foster contacts, outside therapy and early supports, Kennett local scholarships |
| `town/sau9/kennett-and-sau9.md`, `town/sau9/kennett-pathways.md` | Kennett transition, AP, STEM, dual enrollment and Running Start, college outcomes and persistence, ELOs earning credit, career center programs, credentials, capacity and co-ops, the Alternative Program and credit recovery, counseling and the student assistance program, ski and outdoor programs |
| `town/Jackson/*.md`, `town/Bartlett/*.md` | Kennett contracts and formulas from the sending towns' side, SAU 9 cost shares, seats and votes for every district (Albany included), the 2021–22 cooperative study, valley tax rates, SAU 9 policies (phones, meals, English learners, security grants), storm closings, EFA rules and valley providers, the July 2026 homeschool law change, child care near Conway, Fryeburg Academy data |

Also in the library (`additional-data/`): statewide NH rules on residency, tuition, special education, home education, EFAs, open enrollment, adequacy and the statewide education property tax. Grep the topic list before writing a rule. `district-practices.md` has an Albany high school options fact. `additional-data/raw/town/*.csv` has Albany's tax rates and adequacy aid.

## Where facts go

- `district Albany` for Albany's contracts, budget, board, enrollment and choices.
- `town Albany` for town government and community facts.
- `district Conway` for new facts about Conway's schools that earlier files lack.
- `sau 9` for SAU-wide facts.
- No place for general NH rules.

All four agents write in `town/Albany/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Contradictions:** report anything that contradicts or fills a gap in the Jackson, Bartlett, Conway or SAU 9 files in your "For another file" section.

## Agent split

| Agent | Area | Output file | Raw folder |
|---|---|---|---|
| 1 | Programs, outcomes and policies at Conway's schools for Albany students | `town/Albany/programs-and-outcomes.md` | `town/Albany/raw/programs/` |
| 2 | Getting to school, the school day and school-based family support | `town/Albany/getting-to-school-and-the-day.md` | `town/Albany/raw/daily/` |
| 3 | Money and governance | `town/Albany/money-and-governance.md` | `town/Albany/raw/money/` |
| 4 | Community and families | `town/Albany/community-and-families.md` | `town/Albany/raw/community/` |
