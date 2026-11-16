# Hart's Location Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hart's Location and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hart's Location/questions.md` (P1.1 to P20.3). The folder name has an apostrophe and a space: quote paths in the shell.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

## What you need to know about Hart's Location

- **Hart's Location** is one of New Hampshire's smallest towns, in Carroll County along Route 302 through Crawford Notch, between Bartlett and the Coos County line (Carroll and Bethlehem beyond). Much of its land is White Mountain National Forest and Crawford Notch State Park. Site town id 236. It is missing from the Census file in `additional-data/programs-and-help.md`.
- **Hart's Location School District** (site district id 236) runs no schools. It holds a traditional annual meeting (2026: polls at the Notchland Inn from 8 am, business meeting at the Town Hall at 4:30 pm, March 10). Its board page is https://www.sau9.org/harts-location: it "meets on the second Tuesday of every other month at 8:00 a.m. at the Josiah Bartlett Elementary School." Policies, agendas, minutes and annual reports are in a Google Drive folder linked there.
- **Where students go:**
  - K–8: Josiah Bartlett Elementary School (JBES, Bartlett School District, site district 35, school 20325) under a contract. The Bartlett research found the contract covers **K–8**, although SAU 9's tuition page labels it K–6. Saved scan: `additional-data/raw/districts/batch-1/sau9-contract-k-6-harts-bartlett-current.pdf`.
  - 9–12: no posted contract. The Bartlett research found a $21,650 high school tuition line in the 2026-27 budget, mileage paid for a family's trips to Fryeburg Academy, and minutes discussing an MOU with Fryeburg or Conway. Kennett High (Conway, site district 113, school 20345) is the SAU 9 high school.
- **Site data:** the site has adequacy aid rows, EFA counts and Question 2 votes for Hart's Location, and everything for JBES and Kennett.
- **SAU 9** (https://www.sau9.org/) serves Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location and Jackson.

## Several questions contain premises: check them

Questions assume high schoolers go to Kennett, a board meeting at "8:00 AM in Bartlett", a "Thursday afternoon Ski & Ride program" at JBES, "three seats" on the board, "under 50 voters", "90%+" federal and state land, federal PILT offsetting the school budget, "SAU #9 Joint Board" weighted votes, a 2027–28 renegotiation cycle for Hart's Location's contracts, a choice of Kennett Middle School for grades 6–8, Bethlehem/Profile as a possible receiving school, and "donor-town or SWEPT retention rules". Treat each as something to verify. If a premise is wrong or out of date, state the correct fact plainly and neutrally, and list it under "Premises checked" in your summary.

## Already researched: read before you search

Hart's Location's K–8 students attend JBES, which the Bartlett research covered in depth, and the Bartlett research also gathered 11 facts placed in Hart's Location. **Map each assigned question to existing facts first, by file, slug and number; gather new facts only for gaps or Hart's Location-specific angles.**

| File | What it has |
|---|---|
| `town/Bartlett/jbes.md` | JBES programs, staff, class sizes, special education, enrichment, outdoor learning and ski program, counseling, test results context |
| `town/Bartlett/daily-life-and-community.md` | JBES hours and care, Bartlett's own buses (no stop in Hart's Location), attendance, meals, fees, homeschool rules, EFA tutors, infant care, Bartlett Recreation (serves Hart's Location), late buses, Hart's Location storms |
| `town/Bartlett/money-and-governance.md` | Hart's Location's contract with Bartlett and its voice as a tuition town, the high school tuition line and Fryeburg mileage, Bartlett's cost per pupil, Kennett contracts, the SAU 9 study committee |
| `town/sau9/kennett-and-sau9.md`, `town/sau9/kennett-pathways.md` | Kennett AP, STEM, outcomes, career center programs and capacity, dual enrollment and Running Start, the Alternative Program, counseling, ski and outdoor programs |
| `town/Jackson/money-and-governance.md` | SAU 9 cost shares, board seats and weighted votes for every district (Hart's Location included), where to inspect budgets, Fryeburg Academy agreement, valley tax rates |
| `town/Jackson/*.md`, `town/Conway/*.md` | SAU 9 storm closings and remote days, policies, meals, English learners, family notices, security, home education in SAU 9 and the July 2026 law change, early supports and therapy, child care near Conway |
| `town/maine/` (being written now) | Fryeburg Academy research from the Chatham study. Don't redo the academy; point to it. |

Also in the library (`additional-data/`): statewide NH rules on residency, tuition, special education, home education, EFAs, open enrollment, adequacy and the statewide education property tax. Grep the topic list before writing a rule. `additional-data/raw/town/*.csv` has Hart's Location's tax rates and adequacy aid.

## Where facts go

- `district Hart's Location` for its contracts, budget, board, enrollment and choices.
- `town Hart's Location` for town government and community facts.
- `district Bartlett` for new JBES facts; `district Conway` for new Kennett facts; `sau 9` for SAU-wide.
- No place for general NH rules.

All three agents write in `town/Hart's Location/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Contradictions:** report anything that contradicts or fills a gap in the Jackson, Bartlett, Conway or SAU 9 files in your "For another file" section.

## Agent split

| Agent | Area | Output file | Raw folder |
|---|---|---|---|
| 1 | Schools and getting there: JBES and Kennett for Hart's Location students, buses through Crawford Notch, storms, care, programs, special education services, outcomes | `town/Hart's Location/schools-and-getting-there.md` | `town/Hart's Location/raw/schools/` |
| 2 | Money and governance: contracts, budget, taxes, state aid, PILT, SAU share and votes, board, residency and custody, special education responsibility, other schools | `town/Hart's Location/money-and-governance.md` | `town/Hart's Location/raw/money/` |
| 3 | Community and families: town profile, land, housing, child care, early intervention, home education and EFAs, emergency services, roads, connectivity | `town/Hart's Location/community-and-families.md` | `town/Hart's Location/raw/community/` |
