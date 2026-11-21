# Barrington Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Barrington and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Barrington/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Barrington

- **Barrington** is a town in Strafford County between Dover, Durham and Northwood, along Routes 4, 9, 125 and 202, with Swain's Lake. Site town id 33.
- **The Barrington School District** (site district id 33) is **SAU 74**, a one-district SAU. Its schools:
-   - the Early Childhood Learning Center (29010), preschool and kindergarten;
-   - Barrington Elementary (22045), grades 1–4;
-   - Barrington Middle (22030), grades 5–8.
- **High school:** `places.yaml` lists tuition contracts for grades 9–12 with Dover, Oyster River and Coe-Brown Northwood Academy. Dover's high school and career center are researched (`town/Dover/high-school-and-ctc.md`), and Oyster River in `town/Durham/` (loaded), which notes 182 Barrington students at Oyster River High. Coe-Brown hasn't been researched: place its facts `district Coe-Brown Northwood Academy`. Write Barrington's side: the choice process and deadlines, contracts and tuition, buses, students' counts and outcomes.
- **Starting pages:** SAU 74, https://www.sau74.org; Coe-Brown, https://www.coebrown.org; the town, https://www.barrington.nh.gov.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,343 (2014-15), 1,381 (2019-20), 1,354 (2025-26); cost per pupil FY2025 Barrington $20,308, state $22,699; 2025 tax rates per $1,000: total $19.56, local school $13.13, municipal $3.39; Question 2: Barrington 58.7%, so no cap (unofficial); math proficiency 2026: Barrington 49%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Barrington's kindergarten, registration, preschool, high school options and budget-form facts (high school options fact 9). Read them: `grep -n -B2 -A10 -E "place: district (Barrington)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** a preschool lottery (P1.1); 2nd-grade class sizes (P1.2); kindergarten (P6.1); bus stops on Route 125 (P8.1); algebra in middle school (P9.2); a gifted program (P16.1); high school credit in 8th grade (P16.2); updated tech and shop classes (P20.2).
- **High school choice:** the choice deadline (P3.1); Coe-Brown's deposit (P3.2); guaranteed seats at Oyster River (P9.1); late sports buses (P14.2); late registration (P13.2); Dover's career center (P2.1, P2.2, P20.3).
- **Money:** the new Dover contract (P4.2); budgets with flat enrollment (P4.1); a three-year teachers' contract (P7.2); new houses and space (P7.1); paying three schools (P12.2); taxes against Durham and Lee (P19.1); capital reserves (P20.1).
- **Home education:** "paperwork each year" with SAU 74 (P10.2; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Dover/high-school-and-ctc.md` | Dover High and its career center: programs, admission, sending towns. |
| `town/Durham/` (Oyster River) | Oyster River High: AP, counseling, letter-grade transcripts, Barrington's 182 students and its special education billing. |
| `town/Dover/choices-and-adult-learning.md` | Seacoast Charter and other choices. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Pembroke, Weare, Farmington and Somersworth (this wave), and Amherst, Hollis, Litchfield and Hooksett (running). Don't write facts about those towns.

## Where facts go

- `district Barrington` for SAU 74, its three schools, the preschool, its budget, board and tuition contracts.
- `district Coe-Brown Northwood Academy` for Coe-Brown's own programs, deposit and rules.
- `district Dover` or `district Oyster River Coop` only for a fact their files lack.
- `town Barrington` for town government and services.
- No place for general NH rules.

All agents write in `town/Barrington/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, contracts and governance belong to agent 4; the high school choice to agent 3. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | The Early Childhood Learning Center, Barrington Elementary and young families: the preschool, class sizes, care, therapy scheduling, kindergarten, waitlists, bus stops, meals, registration on closing, Chromebooks and supplies, getting to tutoring, guardianship papers, counselors, reading help and Title I, summer programs | `early-childhood-and-elementary.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.3, P6.1, P6.2, P8.1, P8.3, P13.1, P15.2, P15.3, P17.1, P17.2, P17.3, P18.1, P18.2, P18.3 |
| 2 | Barrington Middle and home education: hands-on and career classes, IEPs moving to BMS, costs of trips and sports, algebra, EFAs and home education paperwork, returning in 9th grade, the move to 5th grade, bullying and phones, scores, work habits, eligibility, gifted and honors, high school credit, updated tech and shop | `middle-school-and-home-education.md` | `raw/middle/` | P2.3, P5.1, P8.2, P9.2, P10.1, P10.2, P10.3, P11.1, P11.2, P11.3, P12.1, P14.3, P16.1, P16.2, P20.2 |
| 3 | High school choice: Dover's career center and its buses, the choice deadline, Coe-Brown's deposit, nursing and health, special education at Oyster River and Coe-Brown, where students go, seats at Oyster River, AP and college placement, late registration, credit transfer, coaching, late sports buses, robotics and coding, fitting in at Oyster River, bus rides, awareness of Dover's career center | `high-school-choice.md` | `raw/high/` | P2.1, P2.2, P3.1, P3.2, P3.3, P5.2, P7.3, P9.1, P9.3, P13.2, P13.3, P14.1, P14.2, P16.3, P19.2, P19.3, P20.3 |
| 4 | Money and governance: the budget and enrollment, the Dover contract, the tax split, staying for the schools, space and new houses, the teachers' contract, paying three high schools, the deliberative session, residency with utilities in a landlord's name, taxes against Durham and Lee, capital reserves | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P6.3, P7.1, P7.2, P12.2, P12.3, P15.1, P19.1, P20.1 |
