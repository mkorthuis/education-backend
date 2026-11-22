# Pittsfield Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Pittsfield and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Pittsfield/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Pittsfield

- **Pittsfield** is a town in Merrimack County between Barnstead and Epsom. Site town id 439.
- **The Pittsfield School District** (site district id 439) is **SAU 51** and runs Pittsfield Elementary School (26595; preschool to grade 5) and Pittsfield Middle High School (Pittsfield Middle 26550, grades 6–8; Pittsfield High 22500, grades 9–12). It votes by official ballot (SB2).
- **Neighbors already researched:** Barnstead and Prospect Mountain (`town/Barnstead/`, `town/Alton/`; Prospect Mountain's open enrollment program and the 2025 "Appeal of Pittsfield School District" ruling on open enrollment tuition, cited in `town/Gilmanton/`), Epsom (`town/Epsom/`) and Concord (`town/Concord/`, including the Concord Regional Technical Center). Cite them.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 572 (2014-15), 576 (2019-20), 468 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Pittsfield Elementary 215, Pittsfield Middle 103, Pittsfield High 161; cost per pupil FY2025 Pittsfield $24,039, state $22,699; 2025 tax rates per $1,000 (Pittsfield): total $17.82, local school $10.57, municipal $4.82; Question 2: Pittsfield 65.6% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Pittsfield's preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Pittsfield)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** Wednesday 12:35 dismissals and after-school care (P1.1); open aide and teacher spots (P1.2, P5.1); public preschool (P3.1); kindergarten numbers way down (P3.2); the Bow Street crosswalk (P3.3); bus ride length (P15.2); full-time nurses (P15.3).
- **Middle High:** a middle school flagged for low scores (P4.1); advanced math and science (P4.3); police for absences (P7.3); 6th grade moved to the Middle High (P16.1); about 60 chronically absent students (P18.1); phones and behavior (P18.2); new door locks (P11.3).
- **High school and CTE:** a trades program and CRTC transport (P6.1, P19.2); a sportsmanship award and co-op teams (P12.1); late buses (P12.3); AP and dual enrollment (P13.1); the Foss Family scholarship (P13.3); open enrollment (P10.2).
- **Money:** closing the high school and tuitioning out (P4.2, P6.2, P8.1, P14.2, P17.1); a budget deficit a few years ago (P2.3); the tax cap on the ballot (P2.2); a superintendent shared with Concord (P10.3); para pay (P11.1); default budget cuts (P11.2); a Saturday deliberative session (P14.3); a bond for a roof or boiler (P17.2); the board not answering during public comment (P18.3); sharing staff and buses with Barnstead or Epsom (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Barnstead/`, `town/Alton/` | Prospect Mountain High and its open enrollment program. |
| `town/Epsom/` | A neighbor sending high schoolers to Pembroke Academy. |
| `town/Concord/` | Concord High and the Concord Regional Technical Center. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (this wave); Wakefield, Milton, Moultonborough, Nottingham, Northwood, Rye, Chester and Fremont (running). Don't write facts about those towns.

## Where facts go

- `district Pittsfield` for both schools and the district's budget and board.
- `sau 51` for SAU-wide facts.
- `town Pittsfield` for town government, recreation, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Pittsfield/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Pittsfield Elementary and families: early-release Wednesdays and after-school care, staff vacancies and para pay, lunch accounts, preschool, kindergarten size, drop-off safety, IEP support and missed sessions, who to call, online grades for grandparents, snow alerts, bus rides, nurses, reading tutoring | `pittsfield-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.1, P3.2, P3.3, P5.1, P5.2, P5.3, P7.1, P11.1, P15.1, P15.2, P15.3, P16.2 |
| 2 | Pittsfield Middle High, support and choices: middle school scores and help, advanced math and science, counseling, truancy rules, homeschool access and returning, comparisons with neighbors, building security, 6th graders with high schoolers, bullying, teacher turnover, chronic absence, phones and behavior, Chromebooks | `middle-high-support-and-choices.md` | `raw/middle/` | P4.1, P4.3, P7.2, P7.3, P9.1, P9.3, P10.1, P11.3, P16.1, P16.3, P17.3, P18.1, P18.2, P19.3 |
| 3 | Pittsfield High and career programs: trades and CRTC, vocational seats if tuitioned out, equipment, sports and theater, open enrollment, co-op teams, varsity at a bigger school, late buses, AP and dual enrollment, guidance and FAFSA, local scholarships, science labs and health careers, transport to a tech center, graduates' outcomes | `high-school-and-career-programs.md` | `raw/high/` | P6.1, P6.2, P6.3, P8.2, P10.2, P12.1, P12.2, P12.3, P13.1, P13.2, P13.3, P19.1, P19.2, P20.3 |
| 4 | Money and governance: tax bills, the tax cap, the past deficit, closing the high school and the building, home values, EFAs and the budget, the shared superintendent, default budgets, cost per student, keeping the high school against tuitioning, the deliberative session, the district's future, bonds, public comment, renters, sharing with Barnstead or Epsom | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P4.2, P8.1, P8.3, P9.2, P10.3, P11.2, P14.1, P14.2, P14.3, P17.1, P17.2, P18.3, P20.1, P20.2 |
