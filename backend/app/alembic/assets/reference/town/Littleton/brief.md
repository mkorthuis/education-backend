# Littleton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Littleton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Littleton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Littleton

- **Littleton** is a town in Grafton County, the commercial center of the North Country, home of Littleton Regional Healthcare. Site town id 317.
- **The Littleton School District** (site district id 317) is **SAU 84** and runs Mildred C. Lakeway School (21450; kindergarten to grade 6), Daisy Bronson Junior High (21440; grades 7–8) and Littleton High (21445; grades 9–12). It votes by official ballot (SB2). Check its preschool and Above the Notch.
- **Career programs:** the Hugh J. Gallen Career & Technical Center at Littleton High, which also serves neighboring districts. **Haverhill's research is running now**; don't write Haverhill facts.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 727 (2014-15), 668 (2019-20), 571 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Lakeway 309, Daisy Bronson 86, Littleton High 168; cost per pupil FY2025 Littleton $29,715, state $22,699; 2025 tax rates per $1,000 (Littleton): total $14.10, local school $8.53, municipal $3.37; Question 2: Littleton 66.2% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Littleton's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Littleton)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Lakeway:** before-school care (P1.1); the Parks & Rec program and snow days (P1.2); free lunch handled quietly (P6.2); walking along Route 302 (P6.3); speech therapists and paras (P7.1); crossing guards (P9.1); a counselor (P9.2); public pre-K and the kindergarten cutoff (P11.1, P11.3); ESL and translation (P14.1, P14.2, P14.3).
- **Daisy Bronson and support:** sharing a building with the high school (P4.1); honors or advanced classes (P4.2); IEPs into Daisy Bronson (P7.3); part-time access for homeschoolers and returning (P8.1, P8.2); phones (P13.3); team cuts and co-ops with Profile or Lisbon (P15.1, P15.2); Above the Notch (P16.1); credit recovery (P16.2); counselor wait times (P16.3).
- **Littleton High and the Gallen CTC:** money and customer-service skills (P2.2); getting into building trades or auto (P3.1); credits with CTE (P3.2); local hiring (P3.3); Running Start (P10.1); a personal finance class (P10.2); forestry or agriculture (P12.3); arts cuts and a late bus (P18.1, P18.2); about 170 students and AP (P20.1).
- **Money:** taxes with fewer students (P2.1); open enrollment (P2.3); a higher rate than Franconia or Portsmouth (P5.1); sharing busing and administration (P5.2); a voted-down budget (P5.3); an over-hour bus ride (P12.1); many snow and remote days (P12.2); turnover and supplies (P13.1, P13.2); facilities against other North Country schools (P15.3); comparisons with Bethlehem and Profile (P17.1); a bond (P17.2); enrollment and buildings (P19.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Berlin/`, `town/Plymouth/` | Other North Country and Grafton County districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newport, New London, Enfield, Haverhill and Littleton (this wave); Peterborough, New Ipswich, Hinsdale, Winchester, Charlestown, Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (running). Don't write facts about those towns.

## Where facts go

- `district Littleton` for the three schools, the Gallen CTC and the district's budget and board.
- `sau 84` for SAU-wide facts.
- `town Littleton` for town government, Parks & Rec, the library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Littleton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Lakeway and young families: before-school care, Parks & Rec after-school, reading help, homework help, free lunch, bus stops and walking, speech and paras, IEPs, crossing guards, a counselor, summer camps, public pre-K, child care waitlists, kindergarten and the cutoff, ESL and translation | `lakeway-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P6.1, P6.2, P6.3, P7.1, P7.2, P9.1, P9.2, P9.3, P11.1, P11.2, P11.3, P14.1, P14.2, P14.3 |
| 2 | Daisy Bronson, support and choices: the move from Lakeway and the shared building, advanced classes, IEPs into Daisy Bronson, homeschool part-time access and returning, co-ops and state funds, phones, team cuts and co-ops, Above the Notch, credit recovery, counseling waits, students arriving behind | `daisy-bronson-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P7.3, P8.1, P8.2, P8.3, P13.3, P15.1, P15.2, P16.1, P16.2, P16.3, P19.2 |
| 3 | Littleton High and the Gallen CTC: practical skills, building trades and auto, credits with CTE, local hiring, Running Start, personal finance, counseling for community college, forestry and agriculture, the arts, the late bus, digital design and art electives, AP with a small school, colleges' view, FAFSA and scholarships | `littleton-high-and-gallen-ctc.md` | `raw/high/` | P2.2, P3.1, P3.2, P3.3, P10.1, P10.2, P10.3, P12.3, P18.1, P18.2, P18.3, P20.1, P20.2, P20.3 |
| 4 | Money and governance: taxes and enrollment, open enrollment, scores and college placement against others, the tax rate against other towns, sharing costs, a voted-down budget, bus ride length, snow and remote days, turnover and supplies, facilities, Littleton against Bethlehem, bonds, class sizes, state funding, enrollment and buildings | `money-and-governance.md` | `raw/money/` | P2.1, P2.3, P4.3, P5.1, P5.2, P5.3, P12.1, P12.2, P13.1, P13.2, P15.3, P17.1, P17.2, P17.3, P19.1, P19.3 |
