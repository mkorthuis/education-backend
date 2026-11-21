# Weare Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Weare and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Weare/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Weare

- **Weare** is a rural town in Hillsborough County west of Manchester and Goffstown, along Routes 77, 114 and 149. Site town id 555.
- **Two school districts serve Weare, both in SAU 24** (check the SAU's other districts, such as Henniker):
-   - **The Weare School District** (site district id 555): Center Woods (26810), preschool to grade 3, and Weare Middle (20720), grades 4–8.
-   - **The John Stark Regional School District** (site district id 275): John Stark Regional High (26380), grades 9–12, for Weare and Henniker.
- **Career and technical education:** CRTC in Concord, researched in `town/Concord/high-school-and-pathways.md`; write John Stark's side.
- **Starting pages:** SAU 24, https://www.sau24.org; John Stark, https://www.jsrhs.net; the town, https://www.weare.nh.gov.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,512 (2014-15), 1,399 (2019-20), 1,241 (2025-26); cost per pupil FY2025 Weare $20,525, John Stark $22,488, state $22,699; 2025 tax rates per $1,000: total $21.64, local school $15.00, municipal $3.90, equalization ratio 67%; Question 2: Weare 61.5%, John Stark 57.9% (unofficial); math proficiency 2026: Weare 38%, John Stark 18%, state 44%.
- **Shared district:** John Stark and SAU 24 serve Henniker too. Write their facts here with `district John Stark Regional` or `sau 24`; Henniker has no research yet.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Weare's and John Stark's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Weare|John Stark Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** 4th graders at Weare Middle (P2.1); preschool for everyone (P11.1); kindergarten cutoff and day (P11.2); delay times (P11.3); phones at lunch (P2.3, P10.2); the 40-minute rule for competencies (P10.1); CRTC and the schedule (P6.1, P6.2, P10.3); shop at John Stark (P6.3); a Tuesday late bus (P19.3); unplowed roads (P14.2).
- **Money:** taxes rising with enrollment falling (P4.1); the default budget (P4.2); the split between the two districts (P4.3); an open enrollment warrant article (P9.1); two boards (P9.2); talk of Hillsboro-Deering (P9.3); coach and tech-ed turnover (P12.2); fields and bleachers (P12.3); the SAU office in Henniker (P14.3); rejected contracts (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Concord/high-school-and-pathways.md` | CRTC: programs, admission, sending schools. |
| `town/Goffstown/`, `town/Bedford/` | Comparisons (P3.1, P18.2). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Pembroke, Barrington, Farmington and Somersworth (this wave), and Amherst, Hollis, Litchfield and Hooksett (running). Don't write facts about those towns.

## Where facts go

- `district Weare` for the Weare School District, Center Woods and Weare Middle, its budget and board.
- `district John Stark Regional` for John Stark High and its budget and board.
- `sau 24` for SAU-wide facts.
- `town Weare` for town government and services.
- No place for general NH rules.

All agents write in `town/Weare/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budgets, taxes and governance for both districts belong to agent 4; John Stark's programs to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Center Woods and Weare Middle (grades K–5): care, early buses on dirt roads, class sizes, 4th graders at the middle school, reading help, preschool, kindergarten, delays, advanced math, homework, early finishers, unplowed roads, meals, medication, different calendars | `center-woods-and-early-grades.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P11.1, P11.2, P11.3, P13.1, P13.2, P13.3, P14.2, P17.2, P17.3, P20.1 |
| 2 | Weare Middle and John Stark: phones, AP against Goffstown and Bow, VLACS and Running Start, CRTC and the schedule, shop, after-school help and late buses at WMS, the move to high school, the 40-minute rule, phone rules, electives against CRTC, practical courses, FAFSA help, trades connections, the Tuesday late bus | `middle-and-high-school.md` | `raw/high/` | P2.3, P3.1, P3.2, P6.1, P6.2, P6.3, P8.1, P8.2, P10.1, P10.2, P10.3, P14.1, P19.1, P19.2, P19.3 |
| 3 | Support, choices and safety: paras, therapy pull-outs, IEP moves, homeschool access, EFAs, homeschoolers in sports, fees, gym priority, bullying and group chats, counselors and social workers, harassment, security, drills, military families, PowerSchool help | `support-choices-and-safety.md` | `raw/support/` | P5.1, P5.2, P5.3, P7.1, P7.2, P7.3, P8.3, P12.1, P15.1, P15.2, P15.3, P16.1, P16.2, P16.3, P17.1 |
| 4 | Money and governance: scores and turnover, taxes and enrollment, the default budget, the split between districts, open enrollment, two boards, Hillsboro-Deering talks, coach turnover, fields, the SAU office, schools and home buying, taxes against Goffstown and New Boston, home values, rejected contracts, watching meetings | `money-and-governance.md` | `raw/money/` | P3.3, P4.1, P4.2, P4.3, P9.1, P9.2, P9.3, P12.2, P12.3, P14.3, P18.1, P18.2, P18.3, P20.2, P20.3 |
