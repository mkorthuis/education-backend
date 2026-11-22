# Danville Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Danville and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Danville/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Danville

- **Danville** is a town in Rockingham County north of Plaistow and Hampstead. Site town id 125.
- **The Timberlane Regional School District** (site district id 534) is **SAU 106**, for Atkinson, Danville, Plaistow and Sandown. In Danville: Danville Elementary (22745), preschool to grade 5. Grades 6–8 attend Timberlane Regional Middle and grades 9–12 Timberlane Regional High, both in Plaistow.
- **Reuse first.** Much of this town's shared district is already researched (see "Already researched"). Read those files before searching; cite their facts in your question table instead of rewriting them, and write new facts only for what they lack or for this town's own side.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 713 (2014-15), 573 (2019-20), 559 (2025-26); cost per pupil FY2025 Timberlane $23,256, state $22,699; 2025 tax rates per $1,000 (Danville): total $22.84, local school $15.54, municipal $4.83; Question 2: Danville 80.1% yes, Timberlane adopted it district-wide (about 72%, unofficial); math proficiency 2026: Timberlane 42%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Timberlane's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Timberlane Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Danville Elementary:** full-day pre-K and kindergarten (P1.1); care at the school (P1.2); class sizes (P2.1); early bus pickups (P2.2); under 300 students (P4.1); First Student's reliability (P14.1); gifted or accelerated math (P16.1).
- **Timberlane:** special education hiring (P3.1); the Performing Arts Center's funding (P12.1); wrestling (P13.1); pay-to-play (P13.2); phones (P19.1); buses to Pinkerton or Seacoast School of Technology (P6.2).
- **Money:** taxes and the budget with falling enrollment (P9.1, P10.1); a budget committee cutting millions (P11.1); other towns outvoting Danville (P10.3); the SAU office in Plaistow (P20.3); the tax cap (P9.3).

## Already researched

| File | What it covers |
|---|---|
| `town/timberlane/` (timberlane-high-school.md, timberlane-middle-school-and-student-life.md, timberlane-money-and-governance.md) | Timberlane's middle and high schools, student life, budget, votes and cost formula. |
| `town/Atkinson/`, `town/Plaistow/` | Their elementary schools and their side of Timberlane, for comparisons and district-wide policies. |
| `town/Hampstead/` | A neighboring district, for comparisons (P16.3). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Sandown, Lee, Brookline and Henniker (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Timberlane Regional` for Danville Elementary and any new district-wide fact.
- `sau 106` for SAU-wide facts.
- `town Danville` for town government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Danville/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Sandown's research runs at the same time and also uses Timberlane; put only Danville's own facts and new district-wide facts in these files. Money and the four-town formula belong to agent 4; the middle and high school to agent 3; special education, support, arts and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Danville Elementary and families: pre-K and kindergarten, care, registration, class sizes, bus times and reliability, reading help, meals and the income cutoff, delays and notices, early drop-off, tech help, guardianship papers, a child behind after many absences, gifted or accelerated math, security | `danville-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P2.3, P8.1, P8.3, P14.1, P14.2, P14.3, P15.1, P15.2, P16.1, P19.2 |
| 2 | Special education, support, arts and choices: special education hiring and contacts, IEP moves to the middle school, homeschool access, residency, evaluations for homeschoolers, school costs, the Performing Arts Center, music lessons, activity costs, wrestling and sports fees and eligibility, catching up after absences, mental health support | `support-arts-and-choices.md` | `raw/support/` | P3.1, P3.2, P3.3, P7.1, P7.2, P7.3, P8.2, P12.1, P12.2, P12.3, P13.1, P13.2, P13.3, P15.3, P19.3 |
| 3 | Timberlane Middle and High from Danville: the move from a small school, the bus ride to Plaistow, bullying and discipline, AP and dual enrollment, counselors, scores, CTE and buses to other centers, shop classes, advanced courses in middle school, comparisons with nearby towns, college and work readiness, financial literacy, phones | `middle-and-high-school.md` | `raw/high/` | P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P6.1, P6.2, P6.3, P16.2, P16.3, P18.1, P18.2, P19.1 |
| 4 | Money and governance from Danville: taxes and the budget, Danville's share, the tax cap, the default budget, the four-town vote, budget cuts, teacher pay, equal upgrades for Danville Elementary, home values, central office costs, grant transparency, taxes and young families, the building's condition, community use, Danville's voice in the SAU | `money-and-governance.md` | `raw/money/` | P9.1, P9.2, P9.3, P10.1, P10.2, P10.3, P11.1, P11.2, P11.3, P17.1, P17.2, P17.3, P18.3, P20.1, P20.2, P20.3 |
