# Chatham Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Chatham and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Chatham/questions.md` (P1.1 to P20.3).

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for New Hampshire law. For Maine law, use 2027-08-15 too.

## What you need to know about Chatham

- **Chatham** is a small town in Carroll County on the Maine border, east of Jackson and north of Conway, with North Chatham, Chatham Center and South Chatham along Route 113 (Main Road). Route 113 continues north through Evans Notch into Maine. Site town id 91.
- **Chatham School District** (site district id 91) runs no schools. It holds a traditional annual district meeting (March 10, 2026, 6 pm, Town Hall). Its board is listed at https://www.sau9.org/chatham: it "meets on the first Tuesday of every other month at 9:00 a.m. at the SAU #9 Office" in Conway. Its warrants, minutes and annual reports are in Google Drive folders linked from that page. The saved 2026 warrant (`additional-data/raw/districts/batch-1/chatham-warrant-2026.pdf`, with page images `-p1.png`, `-p2.png`) is a scan.
- **Where students go:** to schools in Fryeburg, Maine, as far as is known:
  - **Maine School Administrative District 72 (MSAD 72)**, a Maine public district serving Fryeburg, Lovell, Brownfield, Denmark, Stow, Stoneham and others. Its schools include C.A. Snow School, Molly Ockett Middle School, New Suncook School (Lovell) and Brownfield-Denmark Elementary. The questions assume Chatham children go to "Molly Ockett School" from kindergarten. Check which school and grades Chatham children actually attend.
  - **Fryeburg Academy**, a private academy that takes town-tuitioned day students, plus boarding and international students, for grades 9–12.
  - Check whether these are written contracts, what they cost, and whether Chatham families have any other choice (Kennett High, NH open enrollment).
- **Site data:** the site has no cost per pupil for Chatham (the rows are empty). It has adequacy aid rows, EFA counts by town and Question 2 votes. Test scores, class sizes and graduation for MSAD 72 and Fryeburg Academy are not in the site's database; they come from the Maine DOE.
- **SAU 9** (https://www.sau9.org/) serves Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location and Jackson.

## Several questions contain premises: check them

Questions mention Molly Ockett School for kindergarten and 4th grade, universal pre-K in MSAD 72, early-release Wednesdays at 12:30 p.m., Maine's universal school meals, MSAD 72 talk of shutting or reconfiguring schools, New Suncook and Brownfield-Denmark, a Pleasant Mountain Locals Pass through MSAD 72, the Clarence E. Mulford Trust, "fewer than 400 residents", a board meeting at 9:00 a.m. in Conway, Region 9 and Lake Region Vocational Center, Running Start at White Mountains Community College, NH open enrollment in Bartlett or Conway, a school bus on Evans Notch Road, and a "large international boarding population". Treat each as something to verify. If a premise is wrong or out of date, state the correct fact plainly and neutrally, and list it under "Premises checked" in your summary.

## Already researched: read before you search

Three SAU 9 towns are done. Read the files for your area first; don't redo what they hold. Where an earlier fact answers a Chatham question, name it in your question table (for example "Jackson file: district-classrooms-and-staff 5 in `Jackson/after-jackson-grammar.md`").

| File | What it already has that Chatham questions need |
|---|---|
| `town/Jackson/after-jackson-grammar.md` | Fryeburg Academy: Maine DOE graduation rate (class of 2023, 94.74%) and chronic absenteeism, behavior reports, the 2026-27 school profile (704 students: 420 district, 220 boarding, 64 private day; 205 international; 18 AP courses; SAT means), Maine's test standards against NAEP |
| `town/Jackson/money-and-governance.md` | Jackson's Fryeburg Academy agreement for 2027-28 to 2036-37 (terms, cost, reports to the board), high school choice, transport under the agreement, SAU 9 cost shares, seats and votes for every member district (Chatham included), valley tax rates |
| `town/Jackson/getting-to-school-and-the-school-day.md`, `town/Jackson/community-and-families.md` | Transport under the Fryeburg agreement; EFA use at Fryeburg Academy and valley EFA providers; licensed child care near Jackson and Conway; home education in SAU 9 and the July 2026 homeschool law change; scholarships for Jackson students |
| `town/Bartlett/money-and-governance.md` | Bartlett's talks with Fryeburg Academy ("cannot take all of our students"); Hart's Location's high school tuition line and a family's mileage to Fryeburg |
| `town/sau9/kennett-and-sau9.md`, `town/sau9/kennett-pathways.md` | Kennett High and the career center (MWVCTC): AP, STEM, credentials, dual enrollment, Running Start, sending-town access |
| `town/Conway/community-and-choice.md` | EFA marketplace providers in the valley, including Fryeburg Academy; therapy providers in Conway and Fryeburg (NPI search) |

Also in the library (`additional-data/`): statewide NH rules on residency, tuition, special education, home education, EFAs, open enrollment and adequacy. Grep the topic list before writing a rule. `additional-data/raw/town/*.csv` has Chatham's tax rates and adequacy aid (Chatham is missing from the Census file in `programs-and-help.md`).

## Where facts go

Maine schools are not in the site's district table, so this research adds a new place form:

- `maine MSAD 72` for facts about MSAD 72 and its schools (programs, staff, calendar, meals, policies, Maine test results).
- `maine Fryeburg Academy` for facts about Fryeburg Academy itself.
- `district Chatham` for Chatham's own contracts, budget, board, buses, choices and enrollment.
- `town Chatham` for town government and community facts.
- `sau 9` for SAU-wide facts.
- No place for general Maine or NH rules (Maine's truancy law, Maine's diploma requirements, NH's residency law), with `kind: rule`.

Facts about MSAD 72 and Fryeburg Academy matter to more than Chatham (Jackson students may attend Fryeburg Academy from 2027-28, and Hart's Location pays for one student there), so they go in a shared folder, `town/maine/`, like `town/sau9/`. Two agents write there; the other three write in `town/Chatham/`. Any file may use any of the places above.

Topics: use the shared slugs. Rules that are Maine's (truancy, diploma requirements, Maine's tuition rate for private academies) can go under a new general topic if none fits; propose it in your summary.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Contradictions:** report anything that contradicts or fills a gap in the Jackson, Bartlett, Conway or SAU 9 files in your "For another file" section.

## Agent split

| Agent | Area | Output file | Raw folder |
|---|---|---|---|
| 1 | MSAD 72 schools (K–8): which schools and grades, registration, pre-K, programs, staff, special education services, enrichment, outdoor learning, counseling, Maine test results and comparisons, reconfiguration talks | `town/maine/msad72-schools.md` | `town/maine/raw/msad72/` |
| 2 | Getting to school and the school day: Chatham's buses and ride times, roads, storm closings, calendars, early release, after-school care, meals, attendance and truancy, summer and ESY transport | `town/Chatham/getting-to-school-and-the-day.md` | `town/Chatham/raw/daily/` |
| 3 | Fryeburg Academy: day and boarding students, admission for town-tuitioned students, academics, arts, world languages, career and technical education, fees, counseling, graduation requirements, credits and transcripts, outcomes | `town/maine/fryeburg-academy.md` | `town/maine/raw/fryeburg-academy/` |
| 4 | Money and governance: Chatham's budget, tuition agreements, tax share and rates, adequacy aid and the statewide education tax, enrollment counts, residency and tuition liability, special education responsibility across states, SAU 9 role, board and public input, other high school options and open enrollment | `town/Chatham/money-and-governance.md` | `town/Chatham/raw/money/` |
| 5 | Community and families: town profile and housing, child care, home education and EFAs, scholarships, guardianship papers, recreation and music programs, ski passes, emergency services | `town/Chatham/community-and-families.md` | `town/Chatham/raw/community/` |
