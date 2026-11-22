# Allenstown Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Allenstown and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Allenstown/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Allenstown

- **Allenstown** is a town in Merrimack County. Site town id 9.
- **The Allenstown School District** (site district id 9) is in **SAU 53** with Pembroke, Chichester, Deerfield and Epsom (the SAU office is in Pembroke). It runs Allenstown Community School (29267), kindergarten to grade 8; 348 students in 2024-25. It decides its budget by official ballot (SB2).
- **Closed schools:** Allenstown Elementary (22580) and the Armand R. Dupont School (22575) closed when Allenstown Community School opened; check what became of each building (P3.3).
- **High school:** Pembroke Academy under an AREA agreement (`places.yaml`; Allenstown and Epsom raised reopening it in 2026). Strong Foundations Charter School is in Pembroke (P11.1–P11.3).
- **SAU 53 and Pembroke Academy are already researched** in `town/Pembroke/` (SAU 53's cost split and budget, Pembroke Academy's courses, CRTC access, buses, counselors and outcomes). Cite those facts by file, topic and number; write only this town's side. Allenstown, Epsom and Deerfield (all SAU 53) are being researched at the same time, so don't write facts about each other's schools.
- **Career and technical education:** the Concord Regional Technical Center (CRTC), researched in `town/Concord/high-school-and-pathways.md` and from Pembroke Academy's side in `town/Pembroke/pembroke-academy.md`.
- **Starting pages:** SAU 53, https://www.sau53.org (district pages, board agendas and minutes, budgets, policies); the town's own site for taxes and town reports; NH DOE profiles.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 546 (2014-15), 543 (2019-20), 529 (2025-26); school enrollment (the site's "2025" row is the October 1, 2024 count, i.e. 2024-25): Allenstown Community School 348 students in 2024-25; cost per pupil FY2025 Allenstown $25,289, state $22,699; 2025 tax rates per $1,000: total $24.88, local school $14.09, municipal $7.61; Question 2: Allenstown 69.2% yes (unofficial), adopted by the district.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Allenstown's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Allenstown)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **ACS:** public pre-K (P1.1); after-school care and a 2:30 dismissal (P1.2); test scores since the move to one building (P2.2); class sizes (P8.1); a gifted program (P17.1); band and chorus in 5th grade (P17.3); drop-off before 7:30 (P18.3); remote snow days (P18.2).
- **Support:** the paraprofessional contract voted down in an August special election (P4.1, P13.1); a new principal (P4.2); ESL staff (P14.1); math intervention (P15.2); summer bridge programs (P15.3).
- **Pembroke Academy:** a dedicated bus (P6.1); treated differently as tuition students (P6.2); an SAT average near 1180 and math proficiency near 23% (P12.2, P15.1); JROTC (P20.3).
- **Money:** about 350 students (P3.1); the default budget (P3.2); the old elementary school as Town Hall and Dupont bought back by the Diocese (P3.3); the mill tax break ending (P2.3); per-pupil spending against Pembroke and Hooksett (P19.2).
- **Home education:** filing with SAU 53 and end-of-year evaluations (P9.2; repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Pembroke/` | SAU 53 (cost split, budget, policies), Pembroke Academy (courses, CRTC, buses, counselors, outcomes) and the Academy's tuition and AREA terms. |
| `town/Concord/high-school-and-pathways.md` | CRTC's programs and admission. |
| `town/Hooksett/` | A neighboring district, for comparisons (P2.1, P19.2). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Allenstown, Epsom, Deerfield, Auburn and Wolfeboro (this wave); Kingston, Jaffrey, Loudon, Alton and Tilton (finishing); Newton, Rindge, Boscawen, Barnstead and Northfield (starting soon). Don't write facts about those towns.

## Where facts go

- `district Allenstown` for Allenstown Community School, the district's budget, board, policies and its side of the AREA agreement.
- `sau 53` only for SAU-wide facts not already in Pembroke's files.
- `town Allenstown` for town government, recreation, the buildings the town took over, and taxes.
- No place for general NH rules.

All agents write in `town/Allenstown/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money, taxes and governance belong to agent 4; Pembroke Academy and CRTC to agent 3; ACS's upper grades, support and choices to agent 2; ACS's early grades and families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Allenstown Community School's early grades and families: public pre-K, after-school care, walking and sidewalks, school quality and scores, homework help, bus stops on Route 3, notices, class sizes, meals, paper report cards, gifted learners, hands-on science in the new building, delays and snow days, early drop-off | `acs-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P7.1, P7.2, P7.3, P8.1, P8.2, P10.1, P10.3, P17.1, P17.2, P18.1, P18.2, P18.3 |
| 2 | ACS's upper grades, support and choices: paraprofessionals and IEPs, a new principal, shop and tech classes, middle school sports and clubs, EFA and homeschool access, fees, Strong Foundations Charter School, ESL and translation, welcoming new students, math in grades 7–8 and interventionists, band and chorus, bullying, counselors | `acs-upper-grades-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P5.3, P8.3, P9.1, P9.2, P10.2, P11.1, P11.2, P11.3, P14.1, P14.2, P14.3, P15.1, P15.2, P17.3, P20.1, P20.2 |
| 3 | Pembroke Academy and CRTC from Allenstown: the IEP move to the Academy, trades and welding, the CRTC bus, the Academy bus and pickup times, tuition students' standing, who to contact, homeschoolers taking classes, AP, honors and college credit, SAT and math results, college counseling, summer bridge before 9th grade, teams, JROTC and military families | `pembroke-academy-from-allenstown.md` | `raw/high/` | P4.3, P5.1, P5.2, P6.1, P6.2, P6.3, P9.3, P12.1, P12.2, P12.3, P15.3, P16.2, P20.3 |
| 4 | Money and governance: where the school tax goes, the budget against enrollment, the default budget, the old school buildings, the August special election, the school share of the tax bill, serving on the board or budget committee, the new gym's use by town leagues, field upkeep, home values, per-pupil spending, budget fights | `money-and-governance.md` | `raw/money/` | P2.3, P3.1, P3.2, P3.3, P13.1, P13.2, P13.3, P16.1, P16.3, P19.1, P19.2, P19.3 |
