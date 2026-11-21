# Belmont Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Belmont and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Belmont/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Belmont

- **Belmont** is a town in Belknap County south of Laconia, along Routes 106 and 140. Site town id 43.
- **The Shaker Regional School District** (site district id 486) is **SAU 80**, a one-district SAU for Belmont and Canterbury. Its schools: Belmont Elementary (22135), preschool to grade 4; Canterbury Elementary (22165), K–5; Belmont Middle (22150), grades 5–8; Belmont High (22145), grades 9–12. Check how Canterbury's students move to Belmont Middle and High, and the budget form (SB 2 or meeting).
- **Career and technical education:** the Huot Technical Center at Laconia High School, researched in `town/Laconia/high-school-and-huot.md` (programs, admission, sending schools, transport). Write this town's side.
- **Starting pages:** Shaker Regional, https://www.sau80.org (check); the town, https://www.belmontnh.gov (check).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,038 (2014-15), 1,017 (2019-20), 829 (2025-26); cost per pupil FY2025 Shaker $23,031, state $22,699; 2025 tax rates per $1,000: total $17.39, local school $9.98, municipal $5.39; Question 2: Shaker 63.1%, so the cap is adopted (unofficial); math proficiency 2026: Shaker 40%, state 44%.
- **Shared district:** Canterbury has no research. Facts about Shaker serve both towns; write them with `district Shaker Regional`.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Shaker's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Shaker Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** care at Belmont Elementary (P1.1); about 43% proficient in math (P1.2); phones at the middle school (P2.1); testing up in math (P5.1); a foster child's enrollment (P12.1); Huot nursing and trades (P3.1, P19.1); Running Start (P3.3); JV teams (P7.1); the NH Scholar cord (P19.3); work-based learning (P19.2); adult education (P20.3).
- **Money:** the tax rate jumping, a bill up over 10% with nearly two-thirds to schools (P10.3, P13.1); a tax cap's cuts (P13.2); the Belmont–Canterbury cost split (P13.3); a separate ballot or a Saturday session (P18.1); the local and state education taxes (P18.2); buildings (P16.2); teacher turnover (P14.1).
- **Home education:** "homeschool paperwork with SAU 80" (P9.3; the yearly evaluation was repealed July 1, 2026); EFAs open to anyone (P9.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Laconia/high-school-and-huot.md` | The Huot Center's programs, admission and sending schools. |
| `town/Laconia/` | Laconia's schools and private schools around Laconia, for comparisons (P5.3, P11.3). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Gilford, Meredith, Franklin and Plymouth (this wave), and Pembroke, Weare, Barrington, Farmington and Somersworth (running or queued). Don't write facts about those towns.

## Where facts go

- `district Shaker Regional` for SAU 80, its four schools, the preschool, policies, staff, budget and board.
- `district Laconia` only for a Huot fact that Laconia's files lack.
- `town Belmont` for town government and services.
- No place for general NH rules.

All agents write in `town/Belmont/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, buildings and governance belong to agent 4; Belmont High and Huot to agent 3; Belmont Middle and home education to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Belmont Elementary and families: care, bus times and delays, speech staff and paras, English learners, preschool papers, messaging, who to call, meals, counselors, reviews, foster and McKinney-Vento enrollment, trauma-informed support, volunteers, tenants' residency papers, bus stops downtown | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.3, P4.2, P6.1, P6.2, P6.3, P8.1, P8.2, P8.3, P10.1, P12.1, P12.2, P12.3, P14.3, P15.1, P15.3 |
| 2 | Belmont Middle and choices: math results and help, phones, clubs and sports, IEP timing and the move to middle school, testing up in math, arts, EFAs, homeschool access and paperwork, private school students in sports, returning for 9th grade, EFAs at Laconia private schools, substance-use prevention | `middle-school-and-choices.md` | `raw/middle/` | P1.2, P2.1, P2.2, P2.3, P4.1, P4.3, P5.1, P5.2, P9.1, P9.2, P9.3, P11.1, P11.2, P11.3, P18.3 |
| 3 | Belmont High and Huot: health science and trades at Huot, competency grading and college, Running Start, JV teams, away games, trades scholarships, computer science, apprentices, job skills, scholarships and donations, work-based learning, the NH Scholar cord, dual-enrollment awareness, transcripts and records, adult education | `belmont-high-and-huot.md` | `raw/high/` | P3.1, P3.2, P3.3, P7.1, P7.2, P7.3, P16.3, P17.1, P17.2, P17.3, P19.1, P19.2, P19.3, P20.1, P20.2, P20.3 |
| 4 | Money and governance: comparisons with Gilford and Laconia, the Belmont–Canterbury district, the tax rate and bill, a tax cap, the cost split, teacher turnover, the budget documents, rents, board postings, buildings, the voting form, local and state education taxes | `money-and-governance.md` | `raw/money/` | P5.3, P10.2, P10.3, P13.1, P13.2, P13.3, P14.1, P14.2, P15.2, P16.1, P16.2, P18.1, P18.2 |
