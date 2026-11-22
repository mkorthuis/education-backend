# Milton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Milton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Milton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Milton

- **Milton** is a town in Strafford County on the Maine border north of Rochester; its villages include Milton Mills and Three Ponds. Site town id 359.
- **The Milton School District** (site district id 359) is **SAU 64** and runs Milton Elementary School (22075; preschool to grade 5), Nute Junior High (26540; grades 6–8) and Nute High (22070; grades 9–12), the last two in one building. It votes by official ballot (SB2).
- **Career programs:** check which center serves Nute students (Rochester's Creteau Technology Center at Spaulding, or another) and how they get there. Rochester is researched in `town/Rochester/` (high-school-and-creteau.md). **Wakefield's research is running now** (`town/Wakefield/`); its agent 3 owns new Spaulding and Creteau facts, so put Creteau program findings in "For another file" and write Milton's side (access, transport, how many Milton students attend).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 551 (2014-15), 500 (2019-20), 499 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Milton Elementary 239, Nute Junior High 105, Nute High 166; cost per pupil FY2025 Milton $22,365, state $22,699; 2025 tax rates per $1,000 (Milton): total $14.76, local school $7.08, municipal $5.00; Question 2: Milton 67.3% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Milton's preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Milton)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Milton Elementary:** full-day pre-K and a pre-K bus (P1.1, P1.2); after-school care (P1.3); reading specialists (P4.2); full-day kindergarten (P17.1); a crossing guard on Elm and Dawson streets (P17.3).
- **Nute:** math scores around 23% (P2.3); 6th graders in the same building as seniors (P15.1); about 160 high schoolers and in-person AP or honors (P6.1); VLACS (P6.2); a graduation rate around 75% (P8.1); Great Bay courses for free (P12.2); JV and varsity numbers (P13.1); JROTC (P18.1); band, chorus, art and theater (P19.1, P19.2); a shared library (P19.3); shop classes (P2.2); CTE transport (P2.1).
- **Money:** a default budget higher than the proposed budget (P3.1, P14.2); over $22,000 a student with about 500 students (P3.2); adequacy aid falling (P3.3); a feasibility study with Dr. Dolloff (P11.1); a board and budget committee split (P14.1); SAU 64's central office (P14.3); an open enrollment warrant article (P9.2, P16.3); teacher turnover (P20.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Rochester/` | Spaulding High and the Creteau Technology Center. |
| `town/Farmington/` | A neighboring one-district SAU with its own high school, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Wakefield, Milton, Moultonborough, Nottingham and Northwood (this wave); Greenland, Rye, Brentwood, Fremont, Chester, Ossipee and New Boston (running). Don't write facts about those towns.

## Where facts go

- `district Milton` for Milton Elementary, Nute and the district's budget and board.
- `sau 64` for SAU-wide facts.
- `town Milton` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/Milton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Milton Elementary and families: pre-K and its bus, after-school care, drop-off times, reading specialists, snow days, free and reduced lunch, paper notices, help for grandparents, homework help, a missed bus, who to email, kindergarten and first grade class sizes, full-day kindergarten, speech screening, walking and a crossing guard | `milton-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.1, P4.2, P4.3, P7.1, P7.2, P7.3, P10.1, P10.2, P10.3, P11.2, P17.1, P17.2, P17.3 |
| 2 | Nute Junior High, support and choices: math scores, paras and special education, IEPs and who to call, homeschool access, the open enrollment article and other schools, returning mid-year, sports eligibility, 6th graders in a 6–12 building, bullying and phones, 6th-grade math help, EFAs and private schools, absences, the library | `nute-junior-high-support-and-choices.md` | `raw/middle/` | P2.3, P5.1, P5.2, P5.3, P9.1, P9.2, P9.3, P13.3, P15.1, P15.2, P15.3, P16.2, P18.3, P19.3 |
| 3 | Nute High School: CTE and its bus, shop classes, AP and honors, VLACS, college admissions, the graduation rate, work credit and internships, job readiness, FAFSA help, Great Bay courses, credit recovery, team numbers and co-ops, JROTC, computer and IT electives, band, chorus, art and theater, trades and apprenticeships | `nute-high-school.md` | `raw/high/` | P2.1, P2.2, P6.1, P6.2, P6.3, P8.1, P8.2, P8.3, P12.1, P12.2, P12.3, P13.1, P18.1, P18.2, P19.1, P19.2, P20.2 |
| 4 | Money and governance: the default budget, spending per student, adequacy aid, the feasibility study, home values, the gym and fields, the board and budget committee split, SAU 64's costs, comparisons with Farmington and Rochester, open enrollment's money, teacher turnover, the town's commitment | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P11.1, P11.3, P13.2, P14.1, P14.2, P14.3, P16.1, P16.3, P20.1, P20.3 |
