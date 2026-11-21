# Somersworth Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Somersworth and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Somersworth/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Somersworth

- **Somersworth** is a city in Strafford County on the Salmon Falls River across from Berwick, Maine, next to Dover and Rollinsford. Site town id 491.
- **The Somersworth School District** (site district id 491) is in **SAU 56** with Rollinsford. Its schools:
-   - Idlehurst (29202), preschool to grade 2;
-   - Maple Wood (29203), grades 3–5;
-   - Somersworth Middle (22830), grades 6–8;
-   - Somersworth High (22845), grades 9–12, with the Somersworth Career Technical Center (CTC), a regional center.
- **Starting pages:** SAU 56, https://www.sau56.org; the city, https://www.somersworth.com (the city council adopts the school budget; check).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,614 (2014-15), 1,506 (2019-20), 1,278 (2025-26); cost per pupil FY2025 Somersworth $21,989, state $22,699; 2025 tax rates per $1,000: total $19.27, local school $10.70, municipal $5.59; Question 2: Somersworth 59.0%, so no cap (unofficial); math proficiency 2026: Somersworth 20%, state 44%.
- **SAU 56 is shared with Rollinsford.** Write SAU-wide facts with `sau 56`.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Somersworth's kindergarten, registration, preschool and budget facts. Read them: `grep -n -B2 -A10 -E "place: district (Somersworth)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** Pre-K and Head Start at Idlehurst (P1.1); care by 7:30 (P1.2); buses downtown (P1.3); translated notices (P2.1); cafeteria options (P2.3); class sizes (P4.2); Maple Wood at 7:30 and Idlehurst at 8:55 (P8.1); late buses (P10.2); the CTC and apprenticeships (P5.1–P5.3); AP and honors (P12.3); vaping (P12.1); arts (P11.2); Running Start (P19.2).
- **Money:** taxes with enrollment around 1,000 (P3.1); over a third of the budget on special education (P3.2); the Mayor's Commission (P3.3, P20.3); low scores (P4.1); a big health care bill (P7.2, P14.2); buildings (P11.1); teachers leaving for Dover and Portsmouth (P14.1); SAU 56 with Rollinsford (P17.3); the tax rate against other towns (P20.2).
- **Choices:** Seacoast Charter (P9.2; Dover's research covers it); a school across the river or a charter (P8.3); homeschool paperwork (P18.2; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Dover/choices-and-adult-learning.md`, `town/Dover/high-school-and-ctc.md` | Seacoast Charter School and Dover's career center, for comparisons and choices. |
| `town/Rochester/` | Rochester, for comparisons. |
| Barrington's and Farmington's research (this wave) | Nearby towns; use the site's data for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Pembroke, Weare, Barrington, Farmington (this wave), and Amherst, Hollis, Litchfield and Hooksett (running). Don't write facts about those towns.

## Where facts go

- `district Somersworth` for the district, its schools, the CTC, its budget and board.
- `sau 56` for SAU-wide facts.
- `town Somersworth` for city government and services (the city council, tax rate, recreation).
- No place for general NH rules.

All agents write in `town/Somersworth/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; the middle and high school and CTC to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Idlehurst and Maple Wood: Pre-K and Head Start, care, buses downtown, translation, cafeteria options, class sizes, reading help, meals and food programs, after-school programs, start times, early releases, late buses at Maple Wood, screens, preschool and daycare | `elementary-schools-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.3, P4.2, P6.1, P6.2, P6.3, P8.1, P10.1, P10.2, P13.3, P16.3 |
| 2 | Somersworth Middle and High and the CTC: the move to middle school, CTC carpentry and apprenticeships, credits, dual enrollment, paths besides college, arts, sports turnout, vaping, counseling, AP and honors, STEM clubs, math acceleration, 6th-grade sports, tutoring, FAFSA help, Running Start, UNH admissions | `middle-high-and-ctc.md` | `raw/high/` | P2.2, P5.1, P5.2, P5.3, P8.2, P11.2, P11.3, P12.1, P12.2, P12.3, P13.1, P13.2, P15.1, P15.2, P19.1, P19.2, P19.3 |
| 3 | Support and choices: families choosing other schools, IEP moves, special education support after the health care bill, out-of-district options, charter schools across the river, Seacoast Charter, fees, behavior support, PowerSchool, EFAs, homeschool access, paperwork and 9th-grade placement | `support-and-choices.md` | `raw/support/` | P4.3, P7.1, P7.2, P7.3, P8.3, P9.2, P10.3, P14.3, P15.3, P17.2, P18.1, P18.2, P18.3 |
| 4 | Money and governance: taxes and enrollment, special education's share, the Mayor's Commission, scores, schools and home buying, the school share of a mortgage, buildings, teacher retention, surprise costs, how fast taxes rise, the tax split, SAU 56 with Rollinsford, ratings and workers, how high rates can go, plans for the schools | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P4.1, P9.1, P9.3, P11.1, P14.1, P14.2, P16.1, P16.2, P17.1, P17.3, P20.1, P20.2, P20.3 |
