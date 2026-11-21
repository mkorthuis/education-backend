# Pembroke Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Pembroke and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Pembroke/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Pembroke

- **Pembroke** is a town in Merrimack County just south-east of Concord, with the Suncook Village area on the Suncook River. Site town id 427.
- **The Pembroke School District** (site district id 427) is in **SAU 53**, which also serves Allenstown, Chichester, Deerfield and Epsom. Check the SAU's districts and Pembroke's budget form (town meeting or ballot). Schools: Pembroke Hill (22615), K–4; Three Rivers (26925), grades 5–8; Pembroke Academy (22620), grades 9–12.
- **Pembroke Academy takes tuition students** from Allenstown, Chichester, Deerfield, Epsom and Hooksett (`places.yaml`). Hooksett's research is running now and writes Hooksett's side; write Pembroke Academy's.
- **Career and technical education:** CRTC in Concord, researched in `town/Concord/high-school-and-pathways.md`; write Pembroke Academy's side.
- **Starting pages:** SAU 53, https://www.sau53.org; Pembroke Academy, https://www.pembrokeacademy.com; the town, https://www.pembroke-nh.com.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,132 (2014-15), 1,034 (2019-20), 967 (2025-26); cost per pupil FY2025 Pembroke $20,240, state $22,699; 2025 tax rates per $1,000: total $21.84, local school $13.75, municipal $5.42; Question 2: Pembroke 63.2%, so the cap is adopted (unofficial); math proficiency 2026: Pembroke 37%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Pembroke's kindergarten, registration, preschool, high school options and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Pembroke)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** full-day kindergarten (P1.1); care by 8:00 (P1.2); public pre-K (P9.1); Spanish-speaking kindergartners (P9.2); Three Rivers' reputation (P3.1); a late bus (P18.1); shop and trades at the Academy (P8.1); cuts to sports and JV (P8.2); the Academy's AP and college outcomes (P17.1–P17.3); CRTC programs (P12.1); NHTI Running Start (P12.2); phones and parking (P12.3).
- **Money:** the school rate up almost $2 (P2.1); a state funding cut and phasing out (P2.3, P4.2, P19.2); the default budget (P4.3); tuition from the sending towns and crowding (P10.1, P10.2); paying for SAU 53 (P10.3, P19.1); the old Pembroke Village School (P15.2); buildings (P13.3); teacher pay against Concord and Hooksett (P13.2); enrollment (P13.1); the website (P18.2).
- **Home education:** "annual homeschool paperwork" with SAU 53 (P11.3; the yearly evaluation was repealed July 1, 2026).

## Already researched

| File | What it covers |
|---|---|
| `town/Concord/high-school-and-pathways.md` | CRTC's programs and admission; Concord's schools for comparison (P6.1). |
| Hooksett's research (running now) | Hooksett's side of its Pembroke Academy contract. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Weare, Barrington, Farmington and Somersworth (this wave), and Amherst, Hollis, Litchfield and Hooksett (running). Don't write facts about those towns.

## Where facts go

- `district Pembroke` for the district, its three schools, its budget, board and tuition contracts.
- `sau 53` for SAU-wide facts (the SAU's other districts have no research yet).
- Sending districts' own sides of their contracts: `district Allenstown`, `district Chichester`, `district Deerfield`, `district Epsom` (only for those contracts).
- `town Pembroke` for town government and services.
- No place for general NH rules.

All agents write in `town/Pembroke/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, tuition and governance belong to agent 4; Pembroke Academy to agent 3; Three Rivers to agent 2; Pembroke Hill to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Pembroke Hill and young families: kindergarten, care by 8:00, bus rides, delay notices, meals, the pickup list, class sizes, special education staffing, public pre-K, English learners, summer programs, infant and toddler care costs | `pembroke-hill-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.2, P5.3, P6.3, P7.1, P9.1, P9.2, P9.3, P20.1 |
| 2 | Three Rivers and support: its reputation, counselors and bullying, IEPs moving to 5th grade, out-of-district placements, homeschoolers in sports and band, EFAs, home education paperwork, the move to Three Rivers, bus times in Suncook Village, after-school help, emergency notices, the SAU website, school board meetings | `three-rivers-and-support.md` | `raw/middle/` | P3.1, P3.2, P7.2, P7.3, P11.1, P11.2, P11.3, P14.1, P14.2, P14.3, P16.3, P18.2, P18.3 |
| 3 | Pembroke Academy: welding and auto at CRTC, help for middle students, comparison with Concord and Bow, AP, advanced math and robotics, shop and trades, sports cuts, apprenticeships, CRTC culinary and health science, NHTI Running Start, phones and parking, counselors and alternatives for students who fall behind, AP and honors, college counseling, outcomes, late buses, other high school options | `pembroke-academy.md` | `raw/high/` | P2.2, P3.3, P6.1, P6.2, P8.1, P8.2, P8.3, P12.1, P12.2, P12.3, P16.1, P16.2, P17.1, P17.2, P17.3, P18.1, P20.2 |
| 4 | Money and governance: the school tax increase, state funding changes, help for seniors, the default budget, tuition from sending towns and crowding, SAU 53's costs, enrollment, teacher pay, buildings, ratings and home values, the old Village School, taxes for a new buyer, the budget breakdown, affordability for young families | `money-and-governance.md` | `raw/money/` | P2.1, P2.3, P4.1, P4.2, P4.3, P10.1, P10.2, P10.3, P13.1, P13.2, P13.3, P15.1, P15.2, P15.3, P19.1, P19.2, P19.3, P20.3 |
