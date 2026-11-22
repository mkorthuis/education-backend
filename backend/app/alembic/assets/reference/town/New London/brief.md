# New London Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for New London and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/New London/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about New London

- **New London** is a town in Merrimack County near Lake Sunapee, home of Colby-Sawyer College and New London Hospital. Site town id 395.
- **The Kearsarge Regional School District** (site district id 276) is **SAU 65** and runs Kearsarge Regional Elementary School at New London (21980; kindergarten to grade 5), the Kearsarge Regional Preschool in New London (26565), Kearsarge Regional Middle (26535; grades 6–8) and High (22015; grades 9–12) in North Sutton, and elementary schools in Bradford, Sutton and Warner. It holds a two-session annual meeting (deliberative session, then ballot). Check how costs are split among the seven towns.
- **Career programs:** check which center serves Kearsarge students (the Concord Regional Technical Center, researched in `town/Concord/`, or another) and how they get there. **Hopkinton's research is running now** and compares itself with Kearsarge; don't write Hopkinton facts.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 322 (2014-15), 340 (2019-20), 314 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Kearsarge Elementary at New London 330 (plus 22 in its preschool), Kearsarge Middle 410, Kearsarge High 481; cost per pupil FY2025 Kearsarge $27,691, state $22,699; 2025 tax rates per $1,000 (New London): total $11.86, local school $5.03, municipal $3.71; Question 2: New London 43.0% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Kearsarge's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Kearsarge Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** after-school care for a 2:55 pickup (P1.1); kindergarten size and paras (P1.2); full-day kindergarten and the cutoff (P1.3); remote snow days (P2.3); James House Preschool, speech evaluations, hours and wraparound care (P3.1, P3.2); the Springfield and Wilmot lines (P8.1); early-release Wednesdays and town rec (P13.3); diversity and halal meals (P19.1, P19.2).
- **Middle school and support:** the bus to North Sutton (P2.1); phones (P7.1); 7th-grade accelerated math (P7.2); Orton-Gillingham or Wilson (P9.1); out-of-district placements (P9.3); homeschool sports, band and co-ops (P11.1, P11.3); Proctor Academy's cost (P12.1); 8th graders in high school shows (P15.2).
- **High school:** Colby-Sawyer and Running Start (P5.1, P10.1); AP science and math (P5.2); a late bus (P5.3); career programs and their buses (P6.1); work credit (P6.3); AP and dual enrollment fees (P10.2); credits from Proctor (P12.2); arts (P15.1); a hockey co-op (P18.1); athletic fees (P18.3); a culinary pathway (P20.2).
- **Money:** New London's share against the other six towns (P4.1, P14.1); bonds (P4.2); about 1,680 students (P4.3); scores against Sunapee (P8.2); the tax on a $600,000 home (P8.3); the deliberative session (P14.2); why New London keeps its own elementary school (P14.3); staff retention and pay (P17.1); Live & Learn Local (P16.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Concord/` | Concord and the Concord Regional Technical Center. |
| `town/Hopkinton/` (running) | A neighbor that compares itself with Kearsarge. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newport, New London, Enfield, Haverhill and Littleton (this wave); Peterborough, New Ipswich, Hinsdale, Winchester, Charlestown, Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (running). Don't write facts about those towns.

## Where facts go

- `district Kearsarge Regional` for the schools and the district's budget, meeting and board.
- `sau 65` for SAU-wide facts.
- `town New London` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/New London/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Kearsarge Elementary at New London and young families: after-school care, kindergarten size and the cutoff, math help, snow days, James House Preschool and speech evaluations, private preschools, attendance lines, bus times and before-school care, meals, early-release Wednesdays, summer programs, volunteers, diversity and languages, menus, the PTO | `kres-new-london-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.2, P2.3, P3.1, P3.2, P3.3, P8.1, P13.1, P13.2, P13.3, P16.3, P17.2, P19.1, P19.2, P19.3 |
| 2 | Kearsarge Middle School, support and choices: the bus to North Sutton, phones, accelerated math, social climate, reading help for dyslexia, IEP evaluations and out-of-district placements, homeschool access, EFAs and co-ops, Proctor Academy, high school music for 8th graders, local music and theater, the move to 6th grade | `kearsarge-middle-support-and-choices.md` | `raw/middle/` | P2.1, P7.1, P7.2, P7.3, P9.1, P9.2, P9.3, P11.1, P11.2, P11.3, P12.1, P15.2, P15.3, P16.2 |
| 3 | Kearsarge High and career programs: Colby-Sawyer and Running Start, AP math and science, the late bus, career programs and buses, apprenticeships, work credit, transferring credits, AP and dual enrollment fees, senior projects, returning from Proctor, honors class sizes, theater and band, hockey, eligibility, athletic fees, a culinary pathway | `kearsarge-high-and-career-programs.md` | `raw/high/` | P5.1, P5.2, P5.3, P6.1, P6.2, P6.3, P10.1, P10.2, P10.3, P12.2, P12.3, P15.1, P18.1, P18.2, P18.3, P20.2 |
| 4 | Money and governance: New London's share, bonds, costs and enrollment, scores against Sunapee, the tax on a home, the school share of the tax bill, the deliberative session, why New London has its own elementary school, Colby-Sawyer's employee benefit, staff retention and pay, score trends, the calendar, sponsoring and donating | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P8.2, P8.3, P14.1, P14.2, P14.3, P16.1, P17.1, P17.3, P20.1, P20.3 |
