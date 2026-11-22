# Hopkinton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hopkinton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hopkinton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hopkinton

- **Hopkinton** is a town in Merrimack County west of Concord; its villages include Contoocook and Hopkinton Village. Site town id 263.
- **The Hopkinton School District** (site district id 263) is **SAU 66** and runs Harold Martin School (20975; preschool to grade 3), Maple Street School (20965; grades 4–6), Hopkinton Middle School (27000; grades 7–8) and Hopkinton High School (20970; grades 9–12). It decides its budget at an annual meeting (March 14, 2026).
- **Career programs:** the Concord Regional Technical Center (CRTC) at Concord High, researched in `town/Concord/`. Cite it; write Hopkinton's side (access, transport, fees, how many students attend).
- **Comparisons** with Bow (`town/Bow/`), Concord (`town/Concord/`) and John Stark (`town/Henniker/`, `town/Weare/`) can use those files and the site's data.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 849 (2014-15), 958 (2019-20), 877 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Harold Martin 269, Maple Street 219, Hopkinton Middle 165, Hopkinton High 283; cost per pupil FY2025 Hopkinton $24,040, state $22,699; 2025 tax rates per $1,000 (Hopkinton): total $23.35, local school $15.36, municipal $5.34; Question 2: Hopkinton 51.8% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Hopkinton's preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Hopkinton)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** full-day public pre-K for everyone (P1.1); waitlists at 'tween school 'n home and the Boys & Girls Club (P1.3); dismissals at 2:30 and 2:40 (P2.1); a late bus at Maple Street (P2.2); PickUp Patrol (P14.2); full-day kindergarten without tuition (P18.1); classroom space (P20.3); class visits to the town library (P20.1).
- **Upper grades and support:** the move from Harold Martin to Maple Street (P1.2); EFAs after the income cap (P7.1); part-time homeschool access (P7.2, P7.3); grades 7–12 in one building (P11.1); 6th-grade orientation (P11.3); ESL on site (P16.1); high school math for 8th graders (P17.2).
- **High school and CRTC:** AP and honors against Concord and Bow (P4.1); VLACS and NHTI (P4.2); the CRTC bus and fees (P5.1, P5.2); a ban on driving to CRTC (P12.2); dual enrollment credits transferring (P12.3); letter grades and class rank (P19.2); Division III/IV and cuts (P19.3); an AI policy (P19.1).
- **Money:** taxes rising with under 1,000 students (P3.1); roofs and boilers in the capital plan (P3.2); CRTC and out-of-district costs (P3.3); Niche reviews (P9.1); 56% math proficiency (P9.2); SWEPT and adequacy (P15.1); spending against Bow, Kearsarge and John Stark (P15.2); seniors at concerts and luncheons (P20.2).

## Already researched

| File | What it covers |
|---|---|
| `town/Concord/` | Concord High and the Concord Regional Technical Center. |
| `town/Bow/`, `town/Henniker/`, `town/Weare/` | Neighbors with their own high schools, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Strafford, Pittsfield, Hopkinton, Hillsborough and Wilton (this wave); Wakefield, Milton, Moultonborough, Nottingham, Northwood, Rye, Chester and Fremont (running). Don't write facts about those towns.

## Where facts go

- `district Hopkinton` for the four schools and the district's budget, meeting and board.
- `district Concord` only for CRTC facts Concord's files lack.
- `sau 66` for SAU-wide facts.
- `town Hopkinton` for town government, recreation, the town library, scholarships and taxes.
- No place for general NH rules.

All agents write in `town/Hopkinton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Harold Martin School and young families: pre-K, after-school care and waitlists, dismissal times and buses, snow and early-release rules, screens in K–3, the reading program, volunteers, bus pickup times, PickUp Patrol, lunch, kindergarten registration and cost, a temporary bus change, help with boots and meals, library visits | `harold-martin-and-families.md` | `raw/elementary/` | P1.1, P1.3, P2.1, P2.3, P10.1, P10.2, P10.3, P14.1, P14.2, P14.3, P18.1, P18.2, P18.3, P20.1 |
| 2 | Maple Street, the middle school, support and choices: the move to Maple Street, late buses, 504 plans and IEPs, paras, moving up with an IEP, EFAs and homeschool access, middle school sports for homeschoolers, grades 7–12 in one building, inclusion and bullying, 6th-grade orientation, phones, ESL, translation, fee waivers, high school math for 8th graders | `maple-street-middle-school-support-and-choices.md` | `raw/middle/` | P1.2, P2.2, P6.1, P6.2, P6.3, P7.1, P7.2, P7.3, P11.1, P11.2, P11.3, P13.3, P16.1, P16.2, P16.3, P17.2 |
| 3 | Hopkinton High and CRTC: AP and honors, VLACS and NHTI, college destinations, the CRTC bus, fees and schedule, gap years and apprenticeships, driving to CRTC, dual enrollment credits, mental health support, medical absences, music and theater, labs and art rooms, AI policy, grading and rank, varsity cuts | `hopkinton-high-and-crtc.md` | `raw/high/` | P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P12.1, P12.2, P12.3, P13.1, P13.2, P17.1, P17.3, P19.1, P19.2, P19.3 |
| 4 | Money and governance: taxes and enrollment, the capital plan, CRTC and out-of-district costs, board meetings online, teacher turnover, calendars, ratings, test scores, class sizes over time, state funding and SWEPT, spending against neighbors, contracts and health insurance, seniors at school events, classroom space | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P8.1, P8.2, P8.3, P9.1, P9.2, P9.3, P15.1, P15.2, P15.3, P20.2, P20.3 |
