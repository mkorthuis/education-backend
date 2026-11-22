# Henniker Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Henniker and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Henniker/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Henniker

- **Henniker** is a town in Merrimack County on the Contoocook River, home of New England College. Site town id 245.
- **Two districts serve Henniker, both in SAU 24:**
-   - **The Henniker School District** (site district id 245): Henniker Community School (20935), preschool to grade 8.
-   - **The John Stark Regional School District** (site district id 275): John Stark Regional High in Weare, researched in `../Weare/`.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 560 (2014-15), 545 (2019-20), 563 (2025-26); cost per pupil FY2025 Henniker $21,870, John Stark $22,488, state $22,699; 2025 tax rates per $1,000 (Henniker): total $24.13, local school $13.97, municipal $7.15; Question 2: Henniker 50.9% yes, not adopted (unofficial); math proficiency 2026: Henniker 48%, John Stark 18%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Henniker's and John Stark's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Henniker|John Stark Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **HCS:** pre-K spots (P1.1); a September 30 cutoff (P1.2); care (P1.3); scores (P2.1); dirt-road bus stops (P2.3); a $300 ski club (P3.2); an 8th-grade math track (P5.3); a speech therapist (P8.1); middle schoolers with preschoolers (P13.1); a sensory room (P17.2); phones and smartwatches (P19.2); instruments (P20.2).
- **John Stark:** CRTC admission and buses (P4.1, P4.2); New England College courses (P5.1); AP and honors (P5.2); credit recovery and an alternative program (P10.1, P10.2); driving to school and late buses (P14.2, P14.3); low math scores (P16.1).
- **Money:** the local school share near 60% (P6.1); Weare's and Henniker's control of John Stark (P6.2); town meeting (P13.2); yearly tax changes (P15.2); two budgets (P18.2); the elderly exemption (P18.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Weare/` (all four files) | John Stark Regional High, the CRTC seat cap, the 1985 cost split, SAU 24, Hillsboro-Deering talks. |
| `town/Concord/high-school-and-pathways.md` | The Concord Regional Technical Center. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Danville, Sandown, Lee and Brookline (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Henniker` for HCS, the Henniker budget and board.
- `district John Stark Regional` only for John Stark facts Weare's files lack.
- `sau 24` for SAU-wide facts.
- `town Henniker` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Henniker/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money for both districts belongs to agent 4; John Stark to agent 3; HCS's upper grades, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Henniker Community School's early grades and families: pre-K, the cutoff, care, scores, advanced math, dirt-road bus stops, after-school clubs, delays, vacation camps, meals, the parent portal, summer programs, drop-off and pickup, bus changes, staying informed, infant care, preschool evaluations, Montessori and private preschools | `hcs-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P2.3, P3.3, P9.1, P9.2, P9.3, P11.1, P11.3, P12.1, P12.2, P12.3, P15.3, P17.1, P17.3 |
| 2 | HCS's middle grades, support and choices: the move to the middle side, fee help, the 8th-grade math track, homeschool access, EFAs, co-ops, speech therapy, IEP progress and the move to John Stark, counseling, a K–8 building, sensory spaces, screen time, phones, outdoor learning, instruments | `hcs-middle-support-and-choices.md` | `raw/middle/` | P3.1, P3.2, P5.3, P7.1, P7.2, P7.3, P8.1, P8.2, P8.3, P11.2, P13.1, P17.2, P19.1, P19.2, P19.3, P20.2 |
| 3 | John Stark from Henniker: CRTC admission and buses, apprenticeships, New England College courses, AP and honors, credit recovery, alternative programs, minimum graduation requirements, sports, early buses from Henniker, driving and parking, late buses, math scores, FAFSA help | `john-stark-from-henniker.md` | `raw/high/` | P4.1, P4.2, P4.3, P5.1, P5.2, P10.1, P10.2, P10.3, P13.3, P14.1, P14.2, P14.3, P16.1, P16.3 |
| 4 | Money and governance: the local school share of taxes, control of John Stark, the March meeting, town meeting voting, whether families stay, yearly tax changes, how the board cuts, the elderly exemption, two budgets, watching meetings, calendars, running for the board | `money-and-governance.md` | `raw/money/` | P6.1, P6.2, P6.3, P13.2, P15.1, P15.2, P16.2, P18.1, P18.2, P18.3, P20.1, P20.3 |
