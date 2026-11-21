# Claremont Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Claremont and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Claremont/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Claremont

- **Claremont** is a small city in Sullivan County on the Connecticut River; New Hampshire's school funding lawsuits (the Claremont decisions of 1993 and 1997) are named for it. Site town id 101.
- **The Claremont School District** (site district id 101) is in **SAU 6** (the site lists only Claremont there now; check whether Cornish and Unity left, P18.2). Its schools: Disnard (20165), K–2, and Maple Avenue (20160), grades 2–5, in the site's data (check the grades since Bluff closed); Claremont Middle (20115), grades 6–8; Stevens High (20140), grades 9–12.
- **Tuition:** Cornish (site district id 115) and Unity (539) send grades 9–12 to Claremont, and Croydon has a contract too (`places.yaml`).
- **Career and technical education:** the Sugar River Valley Regional Technical Center (check its campuses and sending schools).
- **Private school:** Claremont Christian School (site district id 1018); the questions call it "CCA" (check the name).
- **Starting pages:** SAU 6, https://www.sau6.org (check); the city, https://www.claremontnh.com (check).
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 1,788 (2014-15), 1,649 (2019-20), 1,403 (2025-26); cost per pupil FY2025 Claremont $26,012, state $22,699; 2025 tax rates per $1,000: total $30.54, local school $16.22, municipal $10.64; Question 2: Claremont 60.8% (check whether it applies to a city district); math proficiency 2026: Claremont 24%, state 44%.
- **Library:** search `additional-data/` for the Claremont decisions and the state's school funding cases before writing facts on P2.2 and P20.3.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Claremont's kindergarten, registration, preschool and budget-form facts, and the school funding cases. Read them: `grep -n -B2 -A10 -E "place: district (Claremont)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Schools:** the move from Bluff to Maple Avenue (P1.1, P16.3); before-school care by 7:00 (P1.2); bus routes cut (P1.3); free meals for everyone (P6.1); crossing guards (P6.3); overloaded classrooms (P11.2); how children are assigned to Disnard or Maple Avenue (P13.2, P20.1); a 7:30 middle school start (P17.1); outside-of-hours special education staff (P5.2).
- **Stevens and the tech center:** trades cut (P3.1); accreditation (P7.3); sports, band and club cuts (P7.2); athletic fees (P15.3).
- **Money:** a $5 million deficit and a state loan (P2.1, P11.1, P18.1, P20.3); the state trying to overturn the Claremont rulings (P2.2); the Bluff building (P2.3, P14.3); families moving to Cornish or Unity (P14.2); Cornish and Unity pulling back from SAU 6 (P18.2).
- **Choices:** Claremont Christian School (P10.1–P10.3); EFAs and homeschooling (P9.1–P9.3).

## Already researched

| File | What it covers |
|---|---|
| Lebanon's research (this wave) | A nearby district, for comparisons (P20.2). |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Berlin, Lebanon, Hanover and Swanzey (this wave), and Belmont, Gilford, Meredith, Franklin and Plymouth (queued). Don't write facts about those towns.

## Where facts go

- `district Claremont` for SAU 6, its schools, the technical center, policies, staff, budget, board and tuition contracts.
- `district Cornish` and `district Unity` only for their own sides of the contracts and SAU changes.
- `district Claremont Christian School` for its own facts.
- `town Claremont` for city government, recreation and taxes.
- No place for general NH rules.

All agents write in `town/Claremont/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Budget, taxes, the deficit, Bluff and governance belong to agent 4; Stevens and the technical center to agent 3; the middle school, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Disnard, Maple Avenue and families: the move from Bluff, before-school care, scores, advanced math, comparing the two schools, meals, Title I reading, crossing guards, English learners, translation, sign-ups, preschool, assignment between the schools, reading retention, summer reading, the Community Center's program, zones | `elementary-and-families.md` | `raw/elementary/` | P1.1, P1.2, P4.1, P4.2, P4.3, P6.1, P6.2, P6.3, P12.1, P12.2, P12.3, P13.1, P13.2, P16.1, P16.2, P17.2, P20.1 |
| 2 | Claremont Middle, support and choices: bus routes, special education staffing and outside-of-hours staff, bullying, homeschoolers in sports, EFAs, returning for 6th grade, Claremont Christian School and services for private school students, substitutes and staffing, start times, snow calls, counselors, phones, alternatives to the middle school | `middle-support-and-choices.md` | `raw/middle/` | P1.3, P5.1, P5.2, P5.3, P9.1, P9.2, P9.3, P10.1, P10.2, P10.3, P11.3, P17.1, P17.3, P19.1, P19.2, P19.3 |
| 3 | Stevens High and the technical center: trades programs and cuts, certifications and apprenticeships, trades or college, AP and online courses, sports and arts cuts, accreditation, work-study, safety, honors and sports, fees, comparisons with nearby towns | `stevens-high-and-tech-center.md` | `raw/high/` | P3.1, P3.2, P3.3, P7.1, P7.2, P7.3, P8.2, P15.1, P15.2, P15.3, P20.2 |
| 4 | Money and governance: the state loan and tax bill, the Claremont rulings, the Bluff building, workers and housing, downtown businesses and rents, the deficit and accountability, classroom loads, the schools' outlook, the school tax share, families moving, combined classes, Cornish and Unity and SAU 6, spending priorities, whether the budget crisis is fixed | `money-and-governance.md` | `raw/money/` | P2.1, P2.2, P2.3, P8.1, P8.3, P11.1, P11.2, P13.3, P14.1, P14.2, P14.3, P16.3, P18.1, P18.2, P18.3, P20.3 |
