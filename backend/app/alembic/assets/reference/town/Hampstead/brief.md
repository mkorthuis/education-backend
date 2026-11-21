# Hampstead Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hampstead and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hampstead/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links. If a search is refused, don't keep retrying it.

## What you need to know about Hampstead

- **Hampstead** is a town in Rockingham County along Routes 111 and 121, with Wash Pond and Sunset Lake. Site town id 223.
- **The Hampstead School District** (site district id 223) is **SAU 55**: one K–8 district with its own SAU office (P11.1). It votes by official ballot. Its schools:
  - Hampstead Central School (22755): preschool to grade 4; 470 students in 2025-26.
  - Hampstead Middle School (22750): grades 5–8; 352 students.
- **High school:** Hampstead's high school students attend **Pinkerton Academy** in Derry under a tuition contract. `places.yaml` records it, with 356 Hampstead students there in October 2024. Pinkerton is researched in the shared folder `town/pinkerton/`, and Derry's research covers the Derry side. Write only Hampstead's side: its contract and tuition, the bus from Hampstead, its students' counts and the move from HMS. Cite the Pinkerton files for Pinkerton's own programs.
- **Starting pages:** the district, https://www.hampsteadschools.net (schools, board, budget, policies, SAU 55); the town, https://www.hampsteadnh.us (tax rate, assessing, elections, recreation).
- **Site figures:**
  - Resident public students: 1,304 (2014-15), 1,232 (2019-20), 1,129 (2026-27).
  - Cost per pupil, FY2025: Hampstead $29,374 (K–8 district with Pinkerton tuition); state $22,699; Timberlane $23,256; Windham $19,690.
  - 2025 tax rates per $1,000: total $19.09, local school $13.83, state education $1.14, municipal $3.51.
  - Question 2: Hampstead 64.8% yes, so the cap is adopted for the Hampstead School District (unofficial).
  - Math proficiency, 2026: Hampstead 50% (district), against Windham 66%, Timberlane 42% and the state 44% (P7.1 says "under 50%" at HMS; the site has school-level results).
  - The site also has every school's enrollment, scores, class sizes, staff, salary schedules, meals, English learners, safety, EFAs, Census estimates, adequacy aid, special education aid and taxes. Point to these.
- **Saved pages:** `additional-data/raw/districts/*/hampstead-*`: the 2026-27 and 2027-28 budgets, the full-day kindergarten pilot, policy JEB, kindergarten interest, menus, the Pinkerton page, policies, registration, the 2026 sample ballot.
- **Library facts already loaded** (don't repeat them): kindergarten (a one-year universal full-day pilot), the cutoff, registration and SB2. Read them: `grep -n -B2 -A10 "place: district Hampstead" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.
- **The schools:**
  - full-day kindergarten for every child (P1.1; the library says a pilot);
  - care on site at HCS (P1.2);
  - class sizes (P1.3);
  - PickUp Patrol changes (P4.1);
  - Title I reading help (P4.3);
  - Orton-Gillingham staff (P6.2);
  - the preschool and non-IEP spots (P9.3);
  - SROs (P16.1);
  - one bus stop or two for shared custody (P18.1);
  - attending HCS from a Derry address (P18.3).
- **The move to Pinkerton:**
  - "350 kids at HMS to over 3,200 at Pinkerton" (P2.1);
  - the Pinkerton bus and a late bus (P2.2, P2.3);
  - a freshman academy (P20.2);
  - counselor handoffs (P20.3).
- **Choices:**
  - Hampstead Academy, a private school (P17.1, P17.3);
  - "yearly homeschool notification or evaluation" (P8.3; repealed July 1, 2026, `choice-hb-1268-home-education-history`).
- **Money:**
  - the budget rising while enrollment doesn't (P3.1);
  - the new tax cap (P3.2);
  - Pinkerton tuition per student and Hampstead's say (P3.3);
  - a separate SAU office for one K–8 district (P11.1);
  - the "funding gap" (P11.2);
  - cost per student against Chester, Danville and Sandown (P11.3);
  - teacher pay against Derry, Londonderry and Salem (P13.2);
  - building needs (P9.2);
  - absentee voting (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/pinkerton/pinkerton-academics-and-pathways.md`, `pinkerton-student-life.md` | Pinkerton's counselors, honors, CTE programs and applications, dual enrollment, AP, special education with sending districts, the 7:15 start, phones, parking permits, clubs, the freshman transition. |
| `town/Derry/` | Derry's side of Pinkerton, Derry's schools for comparisons, home sale prices (`town-housing` 2). |
| `town/Windham/`, `town/Londonderry/`, `town/Salem/`, Atkinson's and Plaistow's research (running now, in `town/timberlane/`) | Comparisons. |
| Library and earlier towns | State rules: EFAs and home education access, special education and out-of-district placements (Nashua's `special-education.md`), 504 plans, English learners, meals, shared custody and records (`student-records-ferpa`), bullying (`students-hb-131-bullying-law`), phones, dual enrollment, absentee voting (`voting-in-local-elections`), default budgets and tax caps. Cite them; don't write them again. |

**Being researched at the same time** (November 21, 2026): Atkinson and Plaistow (Timberlane), Pelham and Seabrook. Don't write facts about them.

## Where facts go

- `district Hampstead` for SAU 55, its two schools, the preschool, its policies, staff, budget and board. Use `sau 55` only if the loader's places list has it and the fact applies to the SAU itself.
- `district Pinkerton Academy` only for a Pinkerton fact Hampstead's side needs that the Pinkerton files lack (say so in "For another file").
- `town Hampstead` for town government and services.
- Private schools: Hampstead Academy under its own district record if the loader has one, otherwise `town Hampstead` with the school named.
- No place for general NH rules.
- **Raw copies:** under `town/Hampstead/raw/<area>/`, each under about 100 MB, holding only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** budget, pay, staffing, buildings and governance belong to H4. Put what you find for another area in "For another file."
- **Blocked pages:** list them under "Not retrieved" and move on.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Hampstead Central and the school day: kindergarten registration and readiness, care on site, class sizes, PickUp Patrol, after-school and summer help, Title I reading, Orton-Gillingham, the preschool, security and SROs, phones and bullying, delays and emergencies, two bus stops for shared custody, two households' records, attending from a Derry address | `central-school-and-daily-life.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P6.2, P9.3, P16.1, P16.2, P16.3, P18.1, P18.2, P18.3 |
| 2 | Hampstead Middle and the move to Pinkerton: the freshman transition, the Pinkerton bus and late bus, Pinkerton's trades programs and apprenticeships, HMS tech classes, HMS math and acceleration, enrichment, high school credit in 8th grade, AP and dual enrollment at Pinkerton, counselors, parking, scholarships and Running Start, science, art and music | `middle-school-and-pinkerton.md` | `raw/middle/` | P2.1, P2.2, P2.3, P5.1, P5.2, P5.3, P7.1, P7.2, P12.1, P12.2, P12.3, P14.1, P14.2, P14.3, P17.2 |
| 3 | Student support and choices: IEP moves to HMS, out-of-district placements, EFAs, homeschoolers in HMS activities, home education notices, tech help for grandparents, counseling at HMS, homework help, Hampstead Academy students moving to HMS or Pinkerton, 504 plans and counselors at Pinkerton, a freshman academy, comparisons with neighbors, ratings and home values | `student-support-and-choices.md` | `raw/support/` | P6.1, P6.3, P7.3, P8.1, P8.2, P8.3, P9.1, P10.1, P10.2, P10.3, P17.1, P17.3, P19.2, P20.1, P20.2, P20.3 |
| 4 | Money, staff and governance: the budget and enrollment, the tax cap, Pinkerton tuition and Hampstead's say, buildings and bonds, SAU 55's central office, the funding gap and line items, cost per student against neighbors, paras, teacher pay, substitutes, spending and scores over time, staffing and enrollment, the default budget, the tax bill split, vote dates and absentee ballots | `money-staff-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P9.2, P11.1, P11.2, P11.3, P13.1, P13.2, P13.3, P15.1, P15.2, P15.3, P19.1, P19.3 |
