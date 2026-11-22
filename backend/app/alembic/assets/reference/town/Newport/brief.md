# Newport Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Newport and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Newport/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Newport

- **Newport** is a town in Sullivan County, east of Claremont; Sturm, Ruger & Co. is a major employer. Site town id 401.
- **The Newport School District** (site district id 401) is **SAU 43** and runs Richards Elementary (21995; preschool to grade 5), Newport Middle (26970; grades 6–8), Newport Middle High (21985; grades 9–12) and Newport SOAR High School (29258). It votes by official ballot (SB2). Check which towns send tuition students (Croydon, Goshen, Unity).
- **Career programs:** the Sugar River Valley Regional Technical Center, with campuses in Claremont and Newport, is researched in `town/Claremont/`. Cite it; write Newport's side (the Newport campus, its renovation, access and how many Newport students attend).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 813 (2014-15), 780 (2019-20), 595 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Richards Elementary 272, Newport Middle 137, Newport High 291, SOAR 7; cost per pupil FY2025 Newport $29,290, state $22,699; 2025 tax rates per $1,000 (Newport): total $25.09, local school $13.61, municipal $7.97; Question 2: Newport 61.7% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Newport's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Newport)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Richards:** early drop-off before a 6:00 a.m. shift (P1.1); kindergarten size and paras (P2.1); bus times from Guild and riding with 5th graders (P2.2); after-school care (P2.3); free meals (P4.1); Title I pull-outs (P4.2); help with Alma (P8.1); Richards Free Library programs (P8.2); a driver shortage (P13.3); walking from downtown (P19.2).
- **Middle school and support:** Newport Montessori or Mount Royal Academy (P5.2); para postings and IEP aides (P6.1); a middle school attached to the high school (P6.3, P14.1); returning from homeschool and the Alma Start deadline (P11.1, P11.3); phones (P14.3); gifted programs and early Algebra I (P18.1, P18.2); volunteer background checks (P17.2).
- **High school and SRVRTC:** welding or machining as a freshman after the $15.4 million renovation (P1.2); hiring by local shops (P1.3); advanced classes (P5.3); credits with a CTE program (P7.1); driver's ed (P7.2); apprenticeships (P7.3); AP and dual enrollment (P9.1); an LNA license and clinical rides (P20.1, P20.3); RVCC or Colby-Sawyer credit (P20.2).
- **Money:** the renovation's tax effect (P3.1); the default budget (P3.2); spending with about 900 students (P3.3); low scores (P5.1); turnover (P10.1); tuition from Croydon or Goshen (P10.3); who uses the new center (P12.1); building bonds (P12.3); supply money and DonorsChoose (P17.1).

## Already researched

| File | What it covers |
|---|---|
| `town/Claremont/` | Claremont and the Sugar River Valley Regional Technical Center. |
| `town/Lebanon/` | Lebanon, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Newport, New London, Enfield, Haverhill and Littleton (this wave); Peterborough, New Ipswich, Hinsdale, Winchester, Charlestown, Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (running). Don't write facts about those towns.

## Where facts go

- `district Newport` for the schools, the Newport campus of the career center and the district's budget and board.
- `sau 43` for SAU-wide facts.
- `town Newport` for town government, recreation, the Richards Free Library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Newport/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Richards Elementary and young families: early drop-off, kindergarten size and paras, bus times, after-school care, free meals, Title I help, fee waivers, Alma help, the library, storm alerts, conferences by phone or Zoom, bus reliability, enrolling a foster child mid-year, records, updating meal forms, coats and supplies, walking to school | `richards-and-families.md` | `raw/elementary/` | P1.1, P2.1, P2.2, P2.3, P4.1, P4.2, P4.3, P8.1, P8.2, P13.1, P13.2, P13.3, P15.1, P15.2, P16.1, P16.2, P19.2 |
| 2 | Newport Middle School, support and choices: private school options, IEP aides and services, a middle school beside the high school, emotional support, returning from homeschool, sports and band for homeschoolers, Alma Start, mixing with older students, bullying, phones, a counselor for new arrivals, moving out mid-year, volunteers, gifted and Algebra I | `middle-school-support-and-choices.md` | `raw/middle/` | P5.2, P6.1, P6.2, P6.3, P8.3, P11.1, P11.2, P11.3, P14.1, P14.2, P14.3, P15.3, P16.3, P17.2, P18.1, P18.2, P18.3 |
| 3 | Newport High and SRVRTC: CTE as a freshman, local hiring, advanced classes, credits with CTE, driver's ed, apprenticeships, AP and dual enrollment, small-school transcripts, counseling and FAFSA, internships, sports rosters, Health Science and the LNA, RVCC and Colby-Sawyer credit, clinical transportation | `newport-high-and-srvrtc.md` | `raw/high/` | P1.2, P1.3, P5.3, P7.1, P7.2, P7.3, P9.1, P9.2, P9.3, P10.2, P12.2, P20.1, P20.2, P20.3 |
| 4 | Money and governance: the career center renovation's cost, the default budget, spending per student, test scores, turnover, tuition students, who uses the new center, building bonds, classroom supplies, PTO and board meetings, what renters hear, state funding | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P5.1, P10.1, P10.3, P12.1, P12.3, P17.1, P17.3, P19.1, P19.3 |
