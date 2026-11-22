# Hillsborough Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hillsborough and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hillsborough/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hillsborough

- **Hillsborough** is a town in Hillsborough County west of Henniker; its villages include Hillsborough Bridge (downtown), Hillsborough Center, the Upper and Lower Villages and Emerald Lake. Site town id 249.
- **The Hillsboro-Deering Cooperative School District** (site district id 251) is **SAU 34** and runs Hillsboro-Deering Elementary (20955; preschool to grade 5), Middle (20960; grades 6–8) and High School (20950; grades 9–12, on Hillcat Drive). It votes by official ballot (SB2). Check whether Windsor sends students and how costs are shared with Deering.
- **Career programs:** the Concord Regional Technical Center, researched in `town/Concord/`. Comparisons with John Stark (`town/Henniker/`, `town/Weare/`) and Hopkinton (running in this wave) can use those files and the site's data.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 910 (2014-15), 819 (2019-20), 684 (2025-26); Deering 185 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Hillsboro-Deering Elementary 418, Middle 230, High 333; cost per pupil FY2025 Hillsboro-Deering $26,314, state $22,699; 2025 tax rates per $1,000 (Hillsborough): total $21.05, local school $10.98, municipal $7.95; Question 2: Hillsborough 69.2% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Hillsboro-Deering's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Hillsboro-Deering Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** the preschool lottery and after-care (P1.1, P1.2); Emerald Lake bus stops (P1.3); 37% math proficiency and challenge (P5.1, P5.2); translation (P8.1); free meals for all (P8.3); guardianship papers (P14.1); full-day kindergarten and the cutoff (P15.1); the town rec program on snow days (P14.3).
- **Middle school and support:** a reading specialist and special education staffing (P4.1); a late bus after homework club (P4.3); step-up visits (P8.2); homeschool sports and band, and annual notification and assessment (P9.1, P9.2); art, music and drama cuts (P13.1); phones (P17.2).
- **High school and CRTC:** CRTC busing and credits (P2.1, P2.2); varsity co-ops (P7.1); AP and Running Start (P7.2); the alternative program (P11.1); class cancellations and online options (P12.2); NHTI for higher math (P18.1); the school profile (P18.3); adult education and HiSET (P19.2).
- **Money:** a $24 million budget with under 1,000 students (P3.1); Deering's and Windsor's shares (P3.3); a separate SAU 34 office (P10.1); building ages and a bond (P10.3); low ratings (P16.1); community use of facilities (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Concord/` | The Concord Regional Technical Center. |
| `town/Henniker/`, `town/Weare/` | John Stark Regional, a neighbor, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (this wave); Wakefield, Milton, Moultonborough, Nottingham, Northwood, Rye, Chester and Fremont (running). Don't write facts about those towns.

## Where facts go

- `district Hillsboro-Deering Cooperative` for the three schools and the district's budget and board.
- `district Concord` only for CRTC facts Concord's files lack.
- `sau 34` for SAU-wide facts.
- `town Hillsborough` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Hillsborough/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Hillsboro-Deering Elementary and young families: the preschool lottery and after-care, Emerald Lake buses, math scores and challenge, enrichment, translation, free meals, guardianship and PowerSchool, Title I reading help, snow days and rec, full-day kindergarten and the cutoff, teacher turnover, bus ride lengths by neighborhood | `hdes-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P8.1, P8.3, P14.1, P14.2, P14.3, P15.1, P15.3, P16.3 |
| 2 | The middle school, support and choices: reading specialists and special education, who to call at SAU 34, the late bus, EFAs and private schools, the move to middle school, homeschool access and paperwork, bullying, counseling, arts, clubs, homework and the 9th-grade jump, buses, phones, start times, mental health and prevention | `middle-school-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P4.3, P5.3, P8.2, P9.1, P9.2, P11.2, P11.3, P13.1, P13.2, P13.3, P17.1, P17.2, P17.3, P20.1 |
| 3 | Hillsboro-Deering High and CRTC: the CRTC bus and credits, apprenticeships, graduation and placement against neighbors, varsity co-ops, AP and dual enrollment, guidance, homeschoolers taking classes, job readiness, the alternative program, ELO and work credit, cancelled classes, local scholarships, NHTI for advanced classes, college readiness, the school profile, adult education | `hdhs-and-crtc.md` | `raw/high/` | P2.1, P2.2, P2.3, P6.2, P7.1, P7.2, P7.3, P9.3, P10.2, P11.1, P12.1, P12.2, P12.3, P18.1, P18.2, P18.3, P19.2 |
| 4 | Money and governance: the budget and enrollment, the tax bill split, Deering's and Windsor's shares, the March vote in plain English, open enrollment, the SAU 34 office, buildings and bonds, nearby schools and ratings, taxes against neighbors, renters, community use of facilities, community partners, watching board meetings | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P6.1, P6.3, P10.1, P10.3, P15.2, P16.1, P16.2, P19.1, P19.3, P20.2, P20.3 |
