# Chesterfield Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Chesterfield and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Chesterfield/questions.md`: 20 profiles and 60 questions, shared by 4 agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Chesterfield

- **Chesterfield** is a town in Cheshire County on Route 9 between Keene and Brattleboro, with Spofford Lake and West Chesterfield. Site town id 95.
- **The Chesterfield School District** (site district id 95) is in **SAU 29** and runs Chesterfield Central School (21140; kindergarten to grade 8; one building). Grades 9–12 go to **Keene High School** under the Keene AREA (the places file has it from 2026-07-01 to 2046-06-30, amended for a 20-year term). SAU 29's other districts are Harrisville, Keene, Marlborough, Marlow, Nelson and Westmoreland. Check the tuition formula, the Keene AREA's governance and the SAU's cost split.
- **Keene's research is done** (`town/Keene/`: elementary, middle and high schools, the Career Center, support, choices, and the budget and the AREA tuition formula). Cite it and write Chesterfield's side only.
- **Site figures:** Resident students (the site's town enrollment; its "2026" row is the October 1, 2025 count, i.e. 2025-26): 439 (2014-15), 441 (2019-20), 383 (2025-26); school enrollment in 2024-25 (the site's "2025" row, the October 1, 2024 count): Chesterfield Central 253; cost per pupil FY2025 Chesterfield $23,686, state $22,699; 2025 tax rates per $1,000 (Chesterfield): total $21.65, local school $12.05, state education $1.57, municipal $4.65, county $3.38; Question 2: Chesterfield 57.3% yes (unofficial).
- **The site's own data** has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes. Point to these; don't restate them.
- **Library facts already loaded** (don't repeat them): Chesterfield's kindergarten, preschool and budget-form facts. Read them: `grep -n -B2 -A10 -E "place: district (Chesterfield)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Premises to check

Report each in your "Premises checked" table.

- **Chesterfield School:** a public pre-K at the school (P1.1); a 2:20 dismissal (P1.2); a full-day kindergarten and drop-off windows (P7.1); a kindergarten class of 12 or 25 (P12.1); full-time math and reading specialists (P16.2); aides and speech therapists (P5.1); regular art, music and Spanish (P14.1); the front door locked all day with a buzzer (P17.3); SAU 29 closing together or Chesterfield deciding (P7.2); a "middle school" honors track and homerooms (P4.2, P4.3); a school theater, chorus or band (P14.3).
- **Keene High from Chesterfield:** Keene High at "1,400" students (P2.1); the high school bus in West Chesterfield (P2.2); Cheshire Career Center access in 9th or 10th grade (P2.3); sending-town kids' pick of classes and sports (P6.1); rides for clubs and practices (P6.2); a late activity bus (P20.1); AP and dual enrollment (P10.1); counselors' time for Chesterfield kids (P10.2); smaller or alternative high school options the district would pay for (P15.2).
- **Money and governance:** the tuition per student and who negotiates it (P11.1); a say in Keene High's spending (P11.2); vouchers' effect on the tuition bill (P11.3); a school tax cap (P3.3); budget creeping up with fewer than 300 students (P3.2); the school building's roof or HVAC bond (P16.1); the Budget Committee (P16.3); SAU 29 costs shared with six towns (P18.1); sharing a middle school with Westmoreland (P18.2); the next School Board meeting and public comment (P18.3).

## Already researched

| File | What it covers |
|---|---|
| `town/Keene/` | Keene's four elementary schools and daily life, Keene Middle and High and the Career Center (AP, dual enrollment, programs by grade), support and staff, choices (Gathering Waters, MC2, St. Joseph, Our Lady of Mercy, policy JJJ, home education), and money (FY2027 budget, AREA tuition formula and 2026-27 rates, SAU 29). |
| `town/Swanzey/`, `town/Winchester/` | Monadnock-area districts, for comparisons. |
| Library and earlier towns | State rules: EFAs and home education access (`district-homeschool-access`; the yearly evaluation was repealed July 1, 2026, `choice-hb-1268-home-education-history`); special education, out-of-district placements and 504 plans (Nashua's `special-education.md`); English learners and translation; free and reduced-price meals; guardianship, residency and records; bullying (`students-hb-131-bullying-law`); phones (`climate-phone-free-school-day`); dual enrollment and college credit (`dual-enrollment-rules`, `college-credit-for-ap-and-dual-enrollment`); open enrollment (`open-enrollment-status`); youth employment; default budgets, deliberative sessions and tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`); property tax relief (RSA 72:38-a and elderly exemptions in Concord's, Derry's and Hampton's files); voting (`voting-in-local-elections`). Cite these by file, topic and fact number; don't write them again. Where they lack a state rule you need, write it with no place. |

**Being researched at the same time** (November 22, 2026): Antrim, Bethlehem, Bristol, Campton, Canaan, Chichester, Dunbarton, Gorham, Grantham, Lancaster, Mont Vernon, New Durham, Plainfield, Rollinsford, Sanbornton, Sunapee, Thornton, Tuftonboro, Walpole, Warner and Whitefield (this batch, all running now). Don't write facts about those towns.

## Where facts go

- `district Chesterfield` for Chesterfield School and the district's budget and board.
- `district Keene` for Keene High and the AREA (cite Keene's files; add only what Chesterfield's questions need).
- `sau 29` for SAU-wide facts.
- `town Chesterfield` for town government, Parks & Rec, exemptions and taxes.
- No place for general NH rules.

All agents write in `town/Chesterfield/`. Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** Money belongs to agent 4; the high school and career programs to agent 3; the upper grades, support and choices to agent 2; the early grades and young families to agent 1. Keene's files already cover Keene High, the Career Center and the AREA tuition formula; cite them and write Chesterfield's side only. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Chesterfield School early grades and families: public pre-K, after-school care, the bus from the far side of Spofford Lake, speech and aides for a 1st grader, IEP goals followed, kindergarten days and windows, delay and snow-day calls, the lunch account, free and reduced meals, kindergarten class size, art, music and Spanish, recess and outdoor learning, buses to practices and town rec, the front door and security, daily updates | `chesterfield-early-grades-and-families.md` | `raw/elementary/` | P1.1, P1.2, P1.3, P5.1, P5.3, P7.1, P7.2, P7.3, P8.3, P12.1, P14.1, P14.2, P17.2, P17.3, P19.3 |
| 2 | Chesterfield School grades 5–8, support and choices: reading and math against SAU 29, honors and challenge, class size and homerooms, intensive support through 8th grade, local trades, cell phones, bullying, families who go private or homeschool, a middle school theater, chorus or band, math and reading specialists, school and Parks & Rec sports, welcoming new families, placing a new 6th grader, Keene Middle School tryouts, 8th grade preparation for honors at Keene High | `chesterfield-grades-5-8-support-and-choices.md` | `raw/middle/` | P4.1, P4.2, P4.3, P5.2, P6.3, P8.1, P8.2, P12.2, P14.3, P16.2, P17.1, P19.1, P19.2, P20.2, P20.3 |
| 3 | Keene High and the Cheshire Career Center, from Chesterfield: walking into a 1,400-student high school, the bus, the career center in 9th or 10th grade, sending-town students' classes and sports, rides for clubs, AP and dual enrollment, counselors and college help, where Chesterfield graduates go, the activity bus, counseling for a struggling freshman, smaller high school options, attendance rules, private school in Keene with an EFA, busing or reimbursement to a private school, rec sports for private-school kids | `keene-high-from-chesterfield.md` | `raw/high/` | P2.1, P2.2, P2.3, P6.1, P6.2, P10.1, P10.2, P10.3, P13.1, P13.2, P13.3, P15.1, P15.2, P15.3, P20.1 |
| 4 | Money and governance: the share of the bill going to the school, why the budget creeps up, a school tax cap, Chesterfield's tuition per student and who negotiates it, a say over Keene High's spending, vouchers and the tuition bill, EFAs and homeschooling at the district level (spending, assessments, SAU rules), teacher turnover, the school building and bonds, the Budget Committee, SAU 29's cost sharing, sharing a middle school with Westmoreland, School Board meetings and public comment | `money-and-governance.md` | `raw/money/` | P3.1, P3.2, P3.3, P9.1, P9.2, P9.3, P11.1, P11.2, P11.3, P12.3, P16.1, P16.3, P18.1, P18.2, P18.3 |
