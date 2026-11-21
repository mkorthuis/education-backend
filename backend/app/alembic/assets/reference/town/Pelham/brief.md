# Pelham Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Pelham and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Pelham/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links. If a search is refused, don't keep retrying it.

## What you need to know about Pelham

- **Pelham** is a town in Hillsborough County on the Massachusetts line (Dracut), along Route 38, between Hudson, Windham and Salem. Site town id 425.
- **The Pelham School District** (site district id 425) is **SAU 28**, a one-district SAU. It votes by official ballot. Its schools:
  - Pelham Elementary (27970): preschool to grade 5; 751 students in 2025-26.
  - Pelham Memorial School (21110): grades 6–8; 349 students.
  - Pelham High School (21105): grades 9–12; 508 students.
- **Career and technical education:** Pelham High students may apply to Salem High's CTE center, Hudson's Palmer Center at Alvirne, and Pinkerton Academy (13 programs, including Automotive and Welding). All three are researched (see below); write only Pelham's side.
- **Starting pages:** the district, https://www.pelhamsd.org (schools, board, budget, policies, calendar); the town, https://www.pelhamweb.com (tax rate, assessing, exemptions, recreation, the library, police).
- **Site figures:**
  - Resident public students: 2,020 (2014-15), 1,877 (2019-20), 1,588 (2026-27).
  - Cost per pupil, FY2025: Pelham $20,212; Windham $19,690; Salem $19,752; state $22,699.
  - 2025 tax rates per $1,000: total $19.09, local school $11.17, state education $1.30, municipal $5.44. Schools are about 65% of the total, so P3.1's "two-thirds" holds; check 2026.
  - Question 2: Pelham 71.4% yes, so the cap is adopted for Pelham (unofficial; P3.2).
  - Math proficiency, 2026: Pelham 44% (district); Windham 66%; state 44%. P4.3 says "around 30%" in the middle school; the site has school-level results.
  - The site also has enrollment, scores, class sizes, staff, salaries, meals, English learners, safety, graduation and plans, child care, EFAs, Census estimates, adequacy aid, special education aid and taxes. Point to these.
- **Saved pages:** `additional-data/raw/districts/*/pelham-*`: the 2026 deliberative posting, home, policies JEB and JEB-R, kindergarten pages, Pelham Elementary's home page, policies section J.
- **Library facts already loaded** (don't repeat them): kindergarten, the cutoff, registration, the preschool at Pelham Elementary and SB2. Read them: `grep -n -B2 -A10 "place: district Pelham" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.
- **The schools:**
  - all three schools on Marsh Road and drop-off traffic (P1.1);
  - kindergarten full or half day and its cost (P6.1);
  - a reading specialist added at Pelham Elementary (P6.3);
  - a renovated Pelham Memorial and class sizes (P2.3);
  - a 40-hour community service requirement (P7.1);
  - four years of math (P12.1);
  - summer online classes left out of the GPA (P12.3);
  - working papers through the school office (P17.1);
  - twins kept together or split (P18.2).
- **Choices and support:**
  - CTE at Salem, Alvirne and Pinkerton and who buses (P2.1, P2.2);
  - homeschoolers in single classes (P16.2);
  - out-of-district placements (P5.2).
- **Money:**
  - "two-thirds" of the tax bill and dropping enrollment (P3.1);
  - the new tax cap (P3.2);
  - SAU 28 central office costs (P3.3);
  - talk of cutting staff (P7.3, P20.3);
  - a "$400,000" special education capital reserve request (P10.2);
  - teacher, para and bus driver pay against neighbors (P10.3, P20.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Salem/high-school-and-cte.md` | Salem's CTE center: eligibility for Pelham students, applications, no tuition or transportation cost. |
| `town/Hudson/alvirne-and-palmer-cte.md` | The Palmer Center at Alvirne: sending towns including Pelham (6 students in 2025-26), charges to sending districts. |
| `town/pinkerton/pinkerton-academics-and-pathways.md` | Pinkerton's CTE programs open to Pelham students (cte-center-programs 5). |
| `town/Windham/` | Windham's schools, for the comparisons in P8.1 and P19.2, and Windham's middle-school math and SAT measures. |
| Library and earlier towns | State rules: EFAs and home education access, special education and out-of-district placements (Nashua's `special-education.md`), 504 plans, English learners and translation, meals, guardianship, bullying, phones, dual enrollment and college credit, youth employment certificates (search the library), default budgets and tax caps. Cite them; don't write them again. |

**Being researched at the same time** (November 21, 2026): Atkinson and Plaistow (Timberlane), Hampstead and Seabrook. Don't write facts about them.

## Where facts go

- `district Pelham` for SAU 28, its schools, the preschool, policies, staff, budget and board.
- `town Pelham` for town government and services.
- Salem's, Hudson's and Pinkerton's CTE programs belong to their own places; Pelham's side (students attending, buses, credit) is `district Pelham`.
- No place for general NH rules.
- **Raw copies:** under `town/Pelham/raw/<area>/`, each under about 100 MB, holding only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** budget, pay, staffing and governance belong to agent 4. Put what you find for another area in "For another file."
- **Blocked pages:** list them under "Not retrieved" and move on.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Pelham Elementary and the early years: Marsh Road drop-off, before- and after-school care, early scores, IEP and speech timing, kindergarten, class sizes, the reading specialist, public preschool, staying at one elementary school, bus times, summer reading, the pickup line, building security, recess, art and music, lunch and allergies | `elementary-and-early-years.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P6.1, P6.2, P6.3, P8.2, P8.3, P14.2, P14.3, P15.1, P15.3, P18.1, P18.3 |
| 2 | Pelham Memorial and Pelham High: the Memorial renovation and class sizes, AP and honors, dual enrollment, middle school math, community service, work-study and early release, sports teams and cuts, buses to away games, tutoring and eligibility, four years of math, counselors and scholarships, summer online courses and GPA, twins' classes, graduates' plans, SAT against Windham, science labs | `memorial-and-high-school.md` | `raw/high/` | P2.3, P4.1, P4.2, P4.3, P7.1, P7.2, P9.1, P9.2, P9.3, P12.1, P12.2, P12.3, P18.2, P19.1, P19.2, P19.3 |
| 3 | Support, buses and choices: CTE access and buses, out-of-district placements, late-bus alerts, Spanish-speaking families, English learners arriving mid-year, free and reduced lunch, bullying and counselors at Memorial, 504 plans into PHS, phones, grandparent paperwork, snow calls, homeschoolers in sports, band and classes, homeschool credits, working papers | `support-buses-and-choices.md` | `raw/support/` | P2.1, P2.2, P5.2, P5.3, P11.1, P11.2, P11.3, P13.1, P13.2, P13.3, P14.1, P15.2, P16.1, P16.2, P16.3, P17.1 |
| 4 | Money, staff and governance: the school share of taxes, the tax cap, SAU 28's central office, staff cuts as budgets rise, value against Windham and Salem, the default budget, the special education capital reserve, teacher, para and bus driver pay and retention, substitutes, graduates' work readiness, budgets and property values | `money-staff-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P7.3, P8.1, P10.1, P10.2, P10.3, P17.2, P17.3, P20.1, P20.2, P20.3 |
