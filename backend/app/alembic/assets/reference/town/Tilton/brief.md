# Tilton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Tilton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Tilton/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Tilton

- **Tilton** is a town in Belknap County at the junction of I-93 and Route 3, home of the Tanger outlets and Tilton School (a private school). Site town id 532.
- **The Winnisquam Regional School District** (site district id 582) is **SAU 59**, for Northfield, Sanbornton and Tilton. Its schools: the Winnisquam Early Learning Center (29247), preschool; Southwick (27070), K–4; Sanbornton Central (22925), K–4; Winnisquam Regional Middle (22955), grades 5–8; Winnisquam Regional High (22950), grades 9–12. Check where Tilton's elementary children go since Union Sanborn closed (P2.1, P14.2).
- **Shared district, first town.** Northfield shares this district and is researched in the next wave; it will cite these files. So cover district-wide facts (the middle and high school, the budget, the cost formula, policies) fully, placed with the district, and keep town-only facts placed with the town.
- **Career and technical education:** the Winnisquam Career Center (WiCC) at WRHS; Belmont's research (`town/Belmont/belmont-high-and-huot.md`, cte-center-programs 9–10) already has its five programs. The Huot Center in Laconia is researched in `town/Laconia/`.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 465 (2014-15), 472 (2019-20), 413 (2025-26); cost per pupil FY2025 Winnisquam $23,715, state $22,699; 2025 tax rates per $1,000 (Tilton): total $11.29, local school $6.06, municipal $3.18; Question 2: Tilton 64.9%, Winnisquam adopted it (64.3%, unofficial); math proficiency 2026: Winnisquam 46%, state 44%.
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Winnisquam's kindergarten, registration, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Winnisquam Regional)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Elementary:** full-day pre-K (P1.1); crowding since Union Sanborn closed (P2.1); bus times (P2.2); speech and OT at Southwick (P7.1); Tilton children in Northfield (P14.2); ELL and translation (P16.1, P16.2); three apps (P13.1).
- **Middle and high school:** WRMS's reputation (P3.1); math (P3.3, P5.1); WiCC programs and credit (P4.1–P4.3); Huot for other programs (P4.2, P17.1); Running Start (P5.2); internships (P8.2); an SRO (P19.1); phones (P19.2); credit recovery and alternatives (P20.1, P20.2).
- **Choices:** Compass Classical Academy and charter busing (P9.1, P9.2); Tilton School's aid and sports (P10.1–P10.3); homeschool access and notification (P12.1–P12.3).
- **Money:** about $23,700 per student (P6.1); the outlets' commercial taxes (P6.2); the budget vote (P6.3); Tilton's tax bill (P8.1); enrollment (P8.3); taxes against Sanbornton and Northfield (P14.3); ratings and home values (P15.1, P15.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Belmont/belmont-high-and-huot.md` | WiCC's programs and terms. |
| `town/Laconia/` | The Huot Center. |
| `town/Franklin/` | Tilton School, Compass Classical Academy and WiCC from Franklin's side. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 21, 2026): Kingston, Jaffrey, Loudon and Alton (this wave of the second ToLoad batch). Don't write facts about those towns.

## Where facts go

- `district Winnisquam Regional` for all its schools, WiCC, policies, budget and board.
- `sau 59` for SAU-wide facts.
- `district Tilton School` for Tilton School's own facts.
- `town Tilton` for town government, recreation, the library and taxes.
- No place for general NH rules.

All agents write in `town/Tilton/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; WRHS and WiCC to agent 3; WRMS, support and choices to agent 2. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | The Early Learning Center, Southwick and families: pre-K, care, kindergarten registration, crowding, bus times, delays, speech and OT, meals, winter help, tutoring, apps, summer camps, late arrivals, why Tilton children go to Northfield, ELL support, registration without a computer, library partnerships, entrance security | `early-learning-and-southwick.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P2.1, P2.2, P2.3, P7.1, P11.1, P11.2, P11.3, P13.1, P13.2, P13.3, P14.2, P16.2, P16.3, P18.2, P19.3 |
| 2 | Winnisquam Middle, support and choices: the middle school's climate, sports and band, math, IEP aides, the move from Southwick, Compass Classical Academy, charter busing, class sizes and homework, Tilton School, homeschool access and notification, interpreters, 504 plans | `middle-school-support-and-choices.md` | `raw/middle/` | P3.1, P3.2, P3.3, P7.2, P7.3, P9.1, P9.2, P9.3, P10.1, P10.2, P10.3, P12.1, P12.2, P12.3, P16.1, P20.3 |
| 3 | Winnisquam High and WiCC: WiCC programs and credit, other programs at Huot, math scores, Running Start, college preparation, internships, fitting in, FAFSA help, electives, an SRO, phones, credit recovery, alternative programs | `high-school-and-wicc.md` | `raw/high/` | P4.1, P4.2, P4.3, P5.1, P5.2, P5.3, P8.2, P14.1, P17.1, P17.2, P17.3, P19.1, P19.2, P20.1, P20.2 |
| 4 | Money and governance: spending per student, the outlets' taxes, the budget vote, Tilton's tax bill, enrollment, taxes against Sanbornton and Northfield, ratings and home values, neighborhoods near the schools, the district's reputation, volunteers, the strategic plan | `money-and-governance.md` | `raw/money/` | P6.1, P6.2, P6.3, P8.1, P8.3, P14.3, P15.1, P15.2, P15.3, P18.1, P18.3 |
