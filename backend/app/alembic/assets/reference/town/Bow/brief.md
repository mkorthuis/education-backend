# Bow Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Bow and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Bow/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Bow

- **Bow** is a town in Merrimack County just south of Concord, along I-89 and I-93. Site town id 57.
- **The Bow School District** (site district id 57) is in **SAU 67** with Dunbarton. It votes by official ballot. Its schools:
-   - the Bow preschool (29264), at Bow High;
-   - Bow Elementary (20680), K–4;
-   - Bow Memorial (20675), grades 5–8;
-   - Bow High (27375), grades 9–12.
- **Dunbarton** sends grades 9–12 to Bow under a tuition contract; check `places.yaml` and the contract's terms (P4.2). Hooksett also has a Bow tuition contract.
- **Career and technical education:** Bow High students attend the Concord Regional Technical Center (CRTC). Concord's research may cover it (check `town/Concord/buildings-staff-and-comparisons.md` and `getting-to-school-and-safety.md`); write Bow's side.
- **Starting pages:** SAU 67, https://www.bownet.org; the town, https://www.bow-nh.gov (Bow Rec Center, tax rate).
- **Site figures:**
-   - Resident students: 1,359 (2014-15), 1,449 (2019-20), 1,432 (2026-27).
-   - Cost per pupil, FY2025: Bow $18,864, state $22,699.
-   - 2025 tax rates per $1,000: total $20.05, local school $12.58, municipal $4.62.
-   - Question 2: Bow 49.7%, so no cap (unofficial).
-   - Math proficiency, 2026: Bow 56% (district), state 44%. P3.1 says the low 40s at Bow High; the site has school-level results.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Bow's kindergarten, registration, preschool and SB2 facts. Read them: `grep -n -B2 -A10 -E "place: district (Bow)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:**
-   - full-day kindergarten (P1.1);
-   - the Rec Center's before- and after-school program, its waitlist and its hours on delays and early releases (P1.2, P10.2, P20.1);
-   - kindergartners on big buses (P1.3);
-   - CRTC and CRTC+ (P2.1, P2.2);
-   - math in the low 40s at Bow High (P3.1);
-   - accelerated math at BMS (P3.2);
-   - phones at BMS (P6.1);
-   - no-cut teams (P6.2);
-   - AP and online classes (P9.1);
-   - counselor caseloads (P9.3);
-   - the special education preschool at Bow High (P15.1);
-   - BES and BMS calendars (P20.3).
- **Money:**
-   - Dunbarton's tuition (P4.2);
-   - a building bond at Bow Elementary (P7.2);
-   - tax rates against Concord, Hooksett and Dunbarton (P7.3);
-   - capital projects and reserves (P19.1, P19.2);
-   - enrollment projections and EFAs (P16.2, P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Concord/` | Concord's schools and the Concord Regional Technical Center, for P2.1, P3.3 and P18.2 (check which file has CRTC). |
| `town/Bedford/` | Bedford High for comparison (P3.3). |
| Hooksett's research (this wave) | Hooksett's Bow tuition contract; Hooksett's agents write Hooksett's side. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Amherst, Hollis, Litchfield, Hooksett (this wave), and Stratham, Epping, Newmarket, Raymond and Durham (running). Don't write facts about those towns.

## Where facts go

- `district Bow` for the Bow School District, its schools, the preschool, its budget, board and the Dunbarton contract.
- `district Dunbarton` for Dunbarton's side of its tuition contract.
- `sau 67` for SAU-wide facts.
- `town Bow` for town government and services (the Rec Center, tax rate).
- No place for general NH rules.

All agents write in `town/Bow/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; BMS and BHS to agent 2; Bow Elementary and the preschool to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Bow Elementary and the preschool: kindergarten, the Rec Center's care and waitlist, buses for kindergartners, special education aides and minutes, the Rec Center with an IEP, pickup paperwork, delays and the Rec Center, lunch costs and accounts, comparison with Massachusetts, the special education preschool, its busing and transition, early reading | `elementary-and-preschool.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P10.1, P10.2, P10.3, P12.1, P15.1, P15.2, P15.3, P16.3 |
| 2 | Bow Memorial and Bow High: CRTC and CRTC+, internships and apprenticeships, math proficiency, accelerated math, comparison with Bedford and Concord for engineering, the move to 9th grade, AP and online classes, Early College, counselors, world languages, enrichment, NCAA help, senior privileges, preparation for work and NHTI, graduate surveys | `memorial-and-high-school.md` | `raw/high/` | P2.1, P2.2, P2.3, P3.1, P3.2, P3.3, P6.3, P9.1, P9.2, P9.3, P12.2, P12.3, P13.2, P13.3, P18.1, P18.2, P18.3 |
| 3 | Support, choices and daily life: BMS phones, no-cut teams, EFAs, homeschoolers in band and sports, bell times, late buses, bullying in 5th grade, private schools against BHS, EFAs for Bishop Brady, busing to private schools, the Rec Center on early-release days, late-bus notices, calendars | `support-choices-and-daily-life.md` | `raw/support/` | P6.1, P6.2, P8.1, P8.2, P8.3, P14.1, P14.2, P14.3, P17.1, P17.2, P17.3, P20.1, P20.2, P20.3 |
| 4 | Money and governance: the school tax and enrollment, Dunbarton's tuition, board meetings and the budget, schools and home values, a building bond at BES, tax rates against neighbors, where the tax goes, spending against the state, budget hearings and warrant articles, fields, teacher retention, vouchers and enrollment, capital projects, reserves, enrollment projections | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P7.1, P7.2, P7.3, P11.1, P11.2, P11.3, P13.1, P16.1, P16.2, P19.1, P19.2, P19.3 |
