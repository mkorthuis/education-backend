# Nottingham Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Nottingham and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Nottingham/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Nottingham

- **Nottingham** is a town in Rockingham County west of Lee and Durham, home to Pawtuckaway State Park. Site town id 413.
- **The Nottingham School District** (site district id 413) is **SAU 107** and runs Nottingham School (22095; listed in the site's data as Nottingham Elementary School), preschool to grade 8. It votes by official ballot (SB2). Check when and why it left SAU 44.
- **High school:** families choose Dover High or Coe-Brown Northwood Academy (`places.yaml`: Dover's contract runs 2025–2032 and takes up to 100% of Nottingham's high schoolers; a new 2026–2037 Coe-Brown contract was approved by voters in March 2026, subject to State Board approval). Dover High and its Regional Career Technical Center are researched in `town/Dover/`; Coe-Brown in `town/Barrington/` and `town/Deerfield/` (facts placed `district Coe-Brown Northwood Academy`).
- **Northwood's research is running now** (`town/Northwood/`): its agent 3 owns new Coe-Brown facts. Write Nottingham's side (its contracts, buses, numbers and costs), cite the Coe-Brown files, and put new Coe-Brown findings in "For another file".
- **Reuse first.** Much of this town's high school or shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 719 (2014-15), 791 (2019-20), 747 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Nottingham School 527, Coe-Brown 654; cost per pupil FY2025 Nottingham $18,527, state $22,699; 2025 tax rates per $1,000 (Nottingham): total $13.20, local school $9.37, municipal $2.30; Question 2: Nottingham 57.2% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Nottingham's kindergarten cutoff, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Nottingham)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Nottingham School:** a preschool lottery and waiting list (P1.1); bus rides from the lake (P1.3); class sizes (P3.1); after-school care on early-release days (P3.3); before-school care at 6:30 (P6.1); free meals (P11.1); buses on unpaved roads (P15.1); a full-time nurse and counselor (P7.2); ESL for Portuguese speakers (P19.1).
- **Upper grades and choices:** shop classes (P2.3); accelerated math (P3.2); homeschool access and annual portfolios (P9.1, P9.3); speech and OT in the building (P10.3); world languages (P14.1); middle school sports against Northwood, Deerfield and Strafford (P20.1).
- **High school:** whether the town pays all of Dover's tuition (P2.1); bus times (P2.2, P16.1); when to choose and switching (P5.1); twins at different schools (P5.3); Oyster River (P8.3); IEPs at Coe-Brown (P10.2); late buses (P13.2); calendars (P14.3); who pays AP, dual enrollment and sports fees (P16.2); private or charter tuition help (P20.2).
- **Money:** savings from leaving SAU 44 (P4.1, P18.2); about 520 students and rising taxes (P4.2); tuition swings between Dover and Coe-Brown (P4.3); separate warrant articles for repairs (P12.1); Wednesday board meetings (P12.2); about $18,500 per pupil (P15.2); caps on tuition increases (P18.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Dover/` | Dover High and the Dover Regional Career Technical Center. |
| `town/Barrington/`, `town/Deerfield/` | Coe-Brown Northwood Academy and those towns' contracts with Coe-Brown and Dover. |
| `town/Lee/`, `town/Durham/` | Mast Way and Oyster River, for comparisons and P8.3. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Wakefield, Milton, Moultonborough, Nottingham and Northwood (this wave); Greenland, Rye, Brentwood, Fremont, Chester, Ossipee and New Boston (running). Don't write facts about those towns.

## Where facts go

- `district Nottingham` for Nottingham School and the district's budget, board and its side of the two contracts.
- `district Dover` only for Dover High facts Dover's files lack.
- `sau 107` for SAU-wide facts.
- `town Nottingham` for town government, recreation, the Blaisdell Memorial Library and taxes.
- No place for general NH rules.

All agents write in `town/Nottingham/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Nottingham School's early grades and families: the preschool, kindergarten drop-off and pickup, bus rides, class sizes, after-school and before-school care, meals, snow days, reading help, paper notices, moving mid-year, unpaved roads, early reading, ESL, translation, summer programs | `nottingham-school-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.3, P6.1, P6.2, P6.3, P7.1, P7.3, P11.1, P11.2, P15.1, P17.1, P19.1, P19.2, P19.3 |
| 2 | Nottingham School's upper grades, support and choices: shop classes, accelerated math, the nurse and counselor, homeschool access and paperwork, special education, therapists, bullying, world languages, Chromebooks, EFAs, STEM clubs, civics, middle school sports, phones | `nottingham-school-upper-grades-support-and-choices.md` | `raw/middle/` | P2.3, P3.2, P7.2, P9.1, P9.2, P9.3, P10.1, P10.3, P11.3, P14.1, P14.2, P15.3, P17.3, P18.3, P20.1, P20.3 |
| 3 | High school choice from Nottingham: Dover High and Coe-Brown, Dover's career center, bus times and late buses, choosing and switching, preparation for honors, twins at different schools, Oyster River, IEPs at the high school, which school friends pick, arts, calendars, fees, private or charter tuition | `high-school-choice.md` | `raw/high/` | P2.1, P2.2, P5.1, P5.2, P5.3, P8.3, P10.2, P13.1, P13.2, P13.3, P14.3, P16.1, P16.2, P20.2 |
| 4 | Money and governance: leaving SAU 44, taxes against enrollment, tuition swings, scores against Lee and Barrington, crowding, warrant articles for repairs, watching board meetings, the school share of the tax bill, cost per pupil, budget input, teacher turnover, tuition caps, a one-school SAU | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P8.1, P8.2, P12.1, P12.2, P12.3, P15.2, P16.3, P17.2, P18.1, P18.2 |
