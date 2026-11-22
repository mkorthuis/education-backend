# Wilton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Wilton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Wilton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Wilton

- **Wilton** is a town in Hillsborough County west of Milford; West Wilton is one of its villages. Site town id 571.
- **The Wilton-Lyndeborough Cooperative School District** (site district id 572) is **SAU 63** and runs Lyndeborough Central School (23035; preschool and kindergarten), Florence Rideout Elementary (23060; grades 1–5), Wilton-Lyndeborough Middle School (26955; grades 6–8) and Senior High School (23070; grades 9–12). It decides its budget at a traditional annual meeting. Check how costs are shared with Lyndeborough.
- **Career programs:** the Milford Applied Technology Center at Milford High, researched in `town/Milford/`. Comparisons with Milford and Souhegan (`town/Milford/`, `town/Amherst/`) can use those files and the site's data. **High Mowing School** (23025) is a private Waldorf day and boarding school in Wilton.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 444 (2014-15), 418 (2019-20), 385 (2025-26); Lyndeborough 152 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Lyndeborough Central 39, Florence Rideout 211, WLC Middle 130, WLC High 147; cost per pupil FY2025 Wilton-Lyndeborough $24,590, state $22,699; 2025 tax rates per $1,000 (Wilton): total $26.98, local school $15.60, municipal $8.65; Question 2: Wilton 59.2% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Wilton-Lyndeborough's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Wilton-Lyndeborough Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** public pre-K (P1.1); kindergarten in Lyndeborough, then Florence Rideout (P1.2, P20.2); before- and after-school care (P1.3); scores against Milford and Amherst (P3.2); accelerated math (P3.3); moving to Milford mid-year (P8.1); snow-day calls (P8.3); Spanish translation (P11.1).
- **Middle school and support:** coming from High Mowing (P6.1); private school students on WLC teams (P6.2); EFAs at High Mowing (P6.3); annual homeschool notification and part-time classes (P9.1, P9.2); VLACS and MATC for homeschoolers (P9.3); the 8th-to-9th move in one building (P18.1); phones (P18.2); 504 plans (P18.3); immunization exemptions (P19.2).
- **High school and MATC:** MATC busing and schedules (P2.1); shop classes at WLC (P2.2); apprenticeship credit (P2.3); enough students for teams (P3.1, P15.1); AP and dual enrollment (P7.1); a class under 40 or 50 (P7.2); tuitioning into Souhegan or Milford (P12.2); late buses (P15.3).
- **Money:** budgets rising with flat enrollment (P4.1); SAU 63's share of the tax bill (P4.2); a bond for roofs or heating (P4.3); the Wilton–Lyndeborough formula (P10.2); turnover (P10.3); para and substitute pay (P14.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Milford/` | Milford High and the Milford Applied Technology Center. |
| `town/Amherst/` | Souhegan High, for comparisons and P12.2. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (this wave); Wakefield, Milton, Moultonborough, Nottingham, Northwood, Rye, Chester and Fremont (running). Don't write facts about those towns.

## Where facts go

- `district Wilton-Lyndeborough Cooperative` for the four schools and the district's budget, meeting and board.
- `district Milford` only for MATC facts Milford's files lack.
- `sau 63` for SAU-wide facts.
- `town Wilton` for town government, recreation, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Wilton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Florence Rideout, Lyndeborough Central and young families: public pre-K, kindergarten in Lyndeborough, before- and after-school care, scores, accelerated math, IEPs and speech, specialists, special education communication, moving mid-year, meals, snow days, translation, reading help for bilingual children, help with forms, recess and nutrition, kindergarten class sizes, the library | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P3.2, P3.3, P5.1, P5.2, P5.3, P8.1, P8.2, P8.3, P11.1, P11.2, P11.3, P19.3, P20.2, P20.3 |
| 2 | WLC Middle School, support and choices: coming from High Mowing, private school students on teams, EFAs, homeschool notification and part-time classes, VLACS and MATC access, bullying and mental health, report cards and the portal, tutoring, bus rides, High Mowing aid and private high school scholarships, the 8th-to-9th move, phones, 504 plans, nurses and counseling, immunization | `middle-school-support-and-choices.md` | `raw/middle/` | P6.1, P6.2, P6.3, P9.1, P9.2, P9.3, P13.1, P13.2, P13.3, P15.2, P16.2, P16.3, P18.1, P18.2, P18.3, P19.1, P19.2 |
| 3 | WLC High and MATC: MATC busing and schedules, shop classes, apprenticeship credit, class and team sizes, AP and dual enrollment, college admissions from a small school, FAFSA and scholarships, tuitioning to Souhegan or Milford, sports co-ops, late buses, community college and trades, where graduates go, financial literacy | `wlc-high-and-matc.md` | `raw/high/` | P2.1, P2.2, P2.3, P3.1, P7.1, P7.2, P7.3, P12.2, P15.1, P15.3, P17.1, P17.2, P17.3 |
| 4 | Money and governance: budgets and enrollment, the tax bill split, buildings and bonds, spending against other co-ops, the Wilton–Lyndeborough formula, turnover, families staying public, home values, para and substitute pay and training, coordination with High Mowing, the elementary schools against Milford's | `money-and-governance.md` | `raw/money/` | P4.1, P4.2, P4.3, P10.1, P10.2, P10.3, P12.1, P12.3, P14.1, P14.2, P14.3, P16.1, P20.1 |
