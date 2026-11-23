# Dunbarton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Dunbarton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Dunbarton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Dunbarton

- **Dunbarton** is a town in Merrimack County southwest of Concord, with Gorham Pond, Page's Corner and Robert Rogers Road. Site town id 149.
- **The Dunbarton School District** (site district id 149) is in **SAU 67**, which it shares with Bow. It runs Dunbarton Elementary School (DES; 20685; kindergarten to grade 6; 234 students in 2024-25). Grades 7–12 go to **Bow** under the Bow–Dunbarton area agreement (the places file has it from 2024-07-01 to 2039-06-30; first signed 2012-13; the 2021 renewal was approved by the State Board and by Dunbarton voters in March 2022): Bow Memorial (the places file says grades 7–8 for Dunbarton) and Bow High. Check how Bow's grades are organized.
- **Bow's research is done** (`town/Bow/`: Bow Elementary and preschool, Bow Memorial and Bow High and the Concord Regional Technical Center, support, and money and governance including Dunbarton's AREA terms). Cite it and write Dunbarton's side only: Dunbarton Elementary, Dunbarton's taxes and its share.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 387 (2014-15), 455 (2019-20), 465 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Dunbarton Elementary 234; cost per pupil FY2025 Dunbarton $19,675, state $22,699; 2025 tax rates per $1,000 (Dunbarton): total $16.34 (it was $26.38 in 2024; check for a revaluation), local school $10.61, state education $1.00, municipal $3.16, county $1.57; Question 2: Dunbarton 63.1% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Dunbarton's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Dunbarton)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Dunbarton Elementary:** full-day kindergarten and the sign-up date (P1.1); before- or after-school care at DES (P1.2, P8.3); preschool options (P1.3, P12.3); a dirt road and the bus (P8.1); the snow delay call (P8.2); proof of residency for a renter (P9.1); free or reduced lunch (P9.2); ParentSquare (P4.3); class sizes (P12.2); whether DES has its own speech and OT therapists (P5.1); SROs at DES and Bow Memorial (P19.1); a foster child's mid-year start and transport to the old school (P18.1, P18.3).
- **Bow Memorial and Bow High from Dunbarton:** switching to Bow Memorial in 7th grade "when the Bow kids have been together since 5th" (P2.1; check Bow's grade structure); honors placement for Dunbarton 7th graders (P13.2); the IEP transfer (P5.2); the morning bus on the back roads and a late bus (P2.3, P16.3); Bow High's AP and dual enrollment (P11.1); student parking passes (P11.3); the CRTC options kids learn about "almost too late" (P16.1); shop and tech labs (P16.2); whether Dunbarton kids feel like outsiders (P17.1); sports eligibility and shuttles (P19.2, P19.3); the phone rule (P17.3).
- **Money and governance:** the school tax climbing (P3.1); HB 1300 (P3.2); what Dunbarton pays Bow each year and a say in Bow's spending (P3.3); cost per student at DES against Bow's charge (P7.1); which March ballot articles raise taxes (P7.2); whether the AREA is locked in and if a Bow vote could end it (P7.3, P14.2); "more than half" of the tax bill going to education (P10.1; the site shows $11.61 of $16.34); whether DES enrollment is rising with new houses (P10.2); home values and Bow High (P10.3); a renovation or addition at DES (P12.1, P20.3); absentee ballots for the school meeting (P14.1); Bow High's building upkeep in the tuition (P14.3); teacher pay and the contract against Bow's (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Bow/` | Bow Elementary and preschool, Bow Memorial and Bow High (CRTC bus, grade 11 math, Algebra I in grade 8, AP, counselors, closed lunch), support and daily life (phones, no late buses, the shared SAU 67 calendar, homeschool and EFA access), and money and governance (Dunbarton's 2024–2039 AREA terms, the FY27 school tax, the tax cap: Bow rejected it and Dunbarton adopted it). |
| `town/Concord/` | The Concord Regional Technical Center and Concord High. |
| `town/Chichester/`, `town/Pembroke/` | Nearby K–8 towns with area agreements (Chichester runs now in this batch; don't write its facts). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 22, 2026): Antrim, Bethlehem, Bristol, Campton, Canaan, Chesterfield, Chichester, Gorham, Grantham, Lancaster, Mont Vernon, New Durham, Plainfield, Rollinsford, Sanbornton, Sunapee, Thornton, Tuftonboro, Walpole, Warner and Whitefield (this batch, all running now). Don't write facts about those towns.

## Where facts go

- `district Dunbarton` for Dunbarton Elementary and Dunbarton's budget and board.
- `district Bow` for Bow Memorial, Bow High and the area agreement (cite Bow's files; add only what Dunbarton's questions need).
- `sau 67` for SAU-wide facts (the shared office, the calendar).
- `town Dunbarton` for town government, recreation, exemptions and taxes.
- No place for general NH rules.

All agents write in `town/Dunbarton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Bow's files already cover Bow Memorial, Bow High, the CRTC and the AREA's terms; cite them and write Dunbarton's side only. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Dunbarton Elementary early grades and families: full-day kindergarten and sign-up, before- and after-school care, preschool options and public pre-K, the bus on dirt roads, snow delays, town rec and clubs at DES, residency proof for renters, free and reduced lunch, ParentSquare, class sizes, foster enrollment and transport, trauma-informed practice | `dunbarton-elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P4.3, P8.1, P8.2, P8.3, P9.1, P9.2, P12.2, P12.3, P18.1, P18.3 |
| 2 | Dunbarton Elementary grades 3–6, support and choices: reading and math against Bow and Bedford, challenge for a student ahead in math, speech and OT staffing, the IEP move to Bow Memorial and who to call at the SAU, EFAs, homeschool paperwork and testing, sports and band for homeschoolers at Bow, welcoming a Hispanic student, preparing sixth graders for Bow Memorial, PTO fundraising and what the budget covers, art, music and PE, trauma training, SROs, third and fourth grade reading | `dunbarton-grades-3-6-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P5.1, P5.2, P5.3, P6.1, P6.2, P9.3, P13.1, P13.2, P15.1, P15.2, P18.2, P19.1, P20.1 |
| 3 | Bow Memorial and Bow High, from Dunbarton: switching to Bow Memorial in 7th grade, welding and heavy equipment and the CRTC, the bus and a late bus, returning from homeschooling to Bow High, AP and dual enrollment, counseling, student parking, how Bow grads do, feeling like outsiders, arts and theater against Concord High, the phone rule, shop and robotics labs, sports shuttles and eligibility, bus home after clubs | `bow-from-dunbarton.md` | `raw/high/` | P2.1, P2.2, P2.3, P6.3, P11.1, P11.2, P11.3, P13.3, P16.1, P16.2, P16.3, P17.1, P17.2, P17.3, P19.2, P19.3 |
| 4 | Money and governance: why the school tax climbs, HB 1300, what Dunbarton pays Bow and a say in Bow's spending, cost per student at DES against Bow's charge, March ballot articles, whether the AREA is locked in or could end by a Bow vote, the education share of the tax bill, enrollment and new houses, home values, the DES building and a renovation, absentee ballots, Bow High's upkeep in the tuition, teacher turnover, pay and contract against Bow | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P7.1, P7.2, P7.3, P10.1, P10.2, P10.3, P12.1, P14.1, P14.2, P14.3, P15.3, P20.2, P20.3 |
