# Tamworth: Research for Ask NH Education Facts

Cited facts and figures for answering Tamworth, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`; the people are invented. The research is in the reference library's format (`../../additional-data/README.md`) and uses the shared topics in `../shared-topics.md`. It isn't loaded into the Ask yet; see `../recommended-improvements.md`.

Gathered November 13, 2026. Tamworth is the second SAU 13 town, after Madison. It runs the Kenneth A. Brett School (K–8) and sends high schoolers to Kennett High in Conway (SAU 9) and, since 2024, Moultonborough Academy. SAU 13-wide facts were left to the Madison research, which ran at the same time.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `brett-school.md` | Enrollment and the ratio, one class per grade, reading (Wilson-based programs, LETRS, Acadience) and the new enVision math, specialists, paraprofessional vacancies, the music vacancy, the King Pine Friday program, counseling, CPI training, the phone policy, volunteers, family communication | 11 | 103 | 2 | `raw/school/` |
| `getting-to-school-and-the-day.md` | First Student's buses, Tamworth's own Kennett buses (6:00 a.m. first pickup, derived ride times), the late-bus policy, free meals and weekend bags, moving mid-year, snow days, homeless students | 7 | 67 | 2 | `raw/daily/` |
| `high-school.md` | Kennett and Moultonborough Academy side by side (AP, honors, weighting, computer science, career-tech in Wolfeboro), no agriculture, forestry or diesel at Kennett, IEP handoff and counts, transition events, Running Start, ELOs, Seacoast comparison | 10 | 65 | 4 | `raw/high-school/` |
| `money-and-governance.md` | Cost per pupil and falling enrollment, tuition per pupil ($20,221 at both schools), the 2024 notice ending the Kennett contract, Moultonborough seats and selection, tax-rate shares, state aid's fall, HVAC phases, support staff pay, middle school ideas, board transparency | 8 | 99 | 8 | `raw/money/` |
| `community-and-families.md` | Census profile, child care near Tamworth, Tamworth Preschool and Children's Center (formerly Bearcamp Valley), The Community School's closing, recreation and camps, adult education and CDL aid, teen mental health access, food help, EFA use | 9 | 84 | 6 | `raw/community/` |
| **Total** | | **45** | **418** | **22** | **234 MB** |

`brief.md` is the brief the research agents worked from. Five agents used about 2.7 million tokens; two started late, when slots freed up under the 20-agent limit.

## Checks

- **Parser:** all five files pass the backend's parser. One table note that ran onto list lines was joined into one line. Eight list lines remain in a "For another file" note, which the loader doesn't read.
- **Topics:** every topic matches `../shared-topics.md`, after the proposals below were reviewed and added (three Tamworth sections renamed to match).
- **Places:** `district Tamworth` 264, `town Tamworth` 85, `district Moultonborough` 22, `district Conway` 17, `district Governor Wentworth Regional` 2, `district Madison` 1, `town Albany` 1.
- **Census update (November 14, 2026):** the site's database now holds the American Community Survey. Four community facts that only restated its measures (median age, children, income, poverty, home value and rent) were removed, and the ACS housing figures were cut from two housing facts and a table. The kept ACS figures (ages, race, income brackets, internet, units in structure) were checked against the database and match.
- **Adequacy aid update (November 14, 2026):** the site's database now holds NH DOE's adequacy aid calculation for FY2020–FY2027. One fact and the table of state education aid by year, which only restated it, were removed, and one fact was cut to why the extraordinary need grant fell. The district's budget estimates of adequacy aid were kept; they differ from DOE's grants, as each note says.
- **Tax rates update (November 15, 2026):** the site's database now holds NH DRA's tax rates by town (tax years 2014–2025) and NH DOE's school taxes by town (2011–2025). The fact giving Tamworth's 2025 rates and full value rate, which only restated them, was removed, and the fact on the school share and school tax dollars was cut to the district's "current appropriation," which equals them. The per-$1,000 shares of budget lines and the district's tax-impact sheet were kept; the $735,906,312 valuation they use matches the database.
- **Spot checks:** each agent checked 3 to 6 quotes against its raw copies. These were checked again independently, and all matched:

  | Fact | Checked against |
  |---|---|
  | Conway's 2026-27 charge of $1,549,098 for 76.61 Tamworth students | Budget line and Conway's apportionment page |
  | The February 2024 motion to cancel the Conway contract | Board minutes |
  | Moultonborough's "up to ten students per grade level ... a total of 40" | The 2026-27 agreement |
  | The six-Friday ski program | Brett student handbook |
  | Tamworth Preschool and Children's Center, and The Community School "closing" | Local news pages saved in `raw/community/` |

## Premises checked

| Question says | What the sources show |
|---|---|
| Brett enrollment "around 165" (P2.1, P8.1, P16.2) | Out of date: 165 was 2024-25; 154 in October 2025 and 126–127 in fall 2026 |
| An "8:1" student-teacher ratio (P13.3) | Roughly right for 2024-25 when every teacher is counted; average class sizes run 11.7 to 19 |
| A "$13.33" tax rate (P2.2) | That's DRA's 2025 full value (equalized) rate; the rate on bills is $14.78 (both in the site's data) |
| A winter Friday program at "King Pine or Cranmore" (P12.1) | Six Fridays at King Pine; Cranmore is only where families pick up ski club rentals |
| An Orton-Gillingham reading specialist (P7.1) | Not in any record; Brett uses Wilson-based programs with LETRS training and Acadience screening |
| Band and chorus in grades 6–8 (P8.1) | Planned, but the music teacher job is unfilled |
| Agriculture, forestry and diesel at Kennett and the career center (P2.3) | None is offered; Moultonborough Academy students can take agricultural science (with forestry) in Wolfeboro |
| "Up to 6" Moultonborough seats and a "boundary" (P14.2) | No boundary: students apply, with a lottery if needed. The limit grew from 10% (2024) to 10 per grade (2026-27); every applicant has been funded so far |
| An IEP handoff "in 8th grade" (P7.2) | Correct in outline; 9 Tamworth students with IEPs were at Kennett and 3 at Moultonborough in August 2026; no written procedure |
| "Shadow days" for 8th graders (P16.2) | None by that name; Brett's Kennett page lists only a December 2024 information night |
| Bearcamp Valley School's early childhood programs (P1.1) | Renamed Tamworth Preschool and Children's Center in August 2025: child care for 18 months to 12 years, 7 a.m. to 5 p.m. |
| The Community School's farm-based high school (P10.1, P20.1) | It announced its closing in 2020; the nonprofit is now The Bearcamp Center, with meals and K–8 camps, and no high school |
| Tamworth Learning Circles (P5.3) | Couldn't be confirmed active |
| Carroll County Adult Education in Tamworth (P18.1) | Correct: its office is in Tamworth; its one evening class is in Conway |
| "Over 90% white" (P8.3) | Correct: 93.7% non-Hispanic White in the 2020 Census |
| A 45-minute drive for mental health care (P19.2) | About 25 minutes to Conway's mental health center (derived) |
| Ski leagues through the Recreation Department (P12.3) | Skiing is a Brett School program |
| "Remote-learning days" (P12.2) | Allowed by SAU 13 policy; none found in use |

## Corrections and additions to earlier files

Each was checked against the raw copy before it was made:
- **SAU 9, `kennett-pathways.md` "Not retrieved":** Kennett's September and October 2026 principal's reports are in Tamworth's board packets.
- **SAU 9, `school-programs-after-grade-6` 8 (note):** Lakes Region Community College allows up to four tuition-free Early College classes a year.
- **Conway, `district-tuition-contracts` 8 (note):** adds Tamworth's February 15, 2024 notice and its 2026-27 charge, and the Madison and Freedom notice dates.
- **Conway, `town-school-options-nearby` 31 (note):** Tamworth Learning Circles couldn't be confirmed active.
- **Jackson, community "Not retrieved":** the "(Closed 2024)" label for The Community School is Private School Review's; the closing was reported in 2020.

**For the library (not edited here):** `additional-data/district-practices.md` gives Tamworth's Moultonborough limit as "up to 6" and its most recent meeting as 2024; the 2026-27 agreement allows 10 per grade, and the 2026 meeting was March 4, 2026.

## Topics added to the shared list

Reviewed with the other towns' proposals on November 13, 2026 and added to `../shared-topics.md`, with Tamworth's sections renamed to match: `district-volunteers-and-partners` (was `district-volunteers-and-donations`), `dyslexia-screening-and-intervention`, `school-residency-rules` (was `school-residency-and-moves`), `adult-education-and-workforce-training`, and `town-government-and-civic-spaces` (was `town-government`).

## Coverage

27 questions are answered **fully** and 33 **partly**; none has nothing.

| Profile | Q1 | Q2 | Q3 |
|---|---|---|---|
| P1 Young parents | partial (renamed center vs SAU 13 preschool) | partial (one class per grade; K–2 average 11.7) | partial (center open to 5; Brett's program seasonal) |
| P2 Dairy farmer | **full** (falling enrollment and cost drivers) | **full** (per-$1,000 shares, derived) | **full** (none of the three offered) |
| P3 Product manager | partial (grade 8 Algebra I not stated) | partial (side by side; "rigor" not measured) | partial (no CS at Kennett; VLACS and MA options) |
| P4 Line cook | **full** (Whittier bus times) | **full** (free meals, Friday bags) | partial (residency rules; Ossipee steps) |
| P5 Homesteaders | **full** (no notice since July 2026) | partial (policies cover own residents) | partial (Community School closed; Circles unconfirmed) |
| P6 Retired principal | **full** (interventions) | partial (staff vs shared) | partial (HVAC phases; no roof plan) |
| P7 Nursing assistant | **full** (no Orton-Gillingham; state law) | partial (counts; no written handoff) | partial (2 of 12 para jobs vacant) |
| P8 Innkeepers | **full** (music vacancy; art) | partial (arts partners; no Barnstormers link) | partial (NCES counts; supports) |
| P9 Electrician | **full** (construction from grade 9) | partial (ELOs, co-ops) | partial (late-bus policy; no drop points published) |
| P10 Forester | **full** (no Community School high school) | **full** (no outdoor classroom yet; trail proposed) | partial (ELO science credit; Tin Mountain partner) |
| P11 Grandmother | **full** (Brett counseling) | partial (meal forms; no Chromebook or trip waivers found) | partial (Rec camp weeks; fees not posted) |
| P12 Ski patroller | **full** (six Fridays at King Pine) | partial (delays and policy; no remote days used) | **full** (skiing is a school program) |
| P13 Bus driver and para | partial (para ranges, derived) | **full** (CPI and PBIS) | partial (contract not posted) |
| P14 Commuting couple | partial (places and wait-list status in the site's data; no wait lengths) | **full** (application and lottery) | **full** (2003 contract ends June 2027) |
| P15 Fiscal watchdog | **full** ($20,221 at both) | partial (2025 middle school idea; no study) | **full** (state grant down to $1.46 million) |
| P16 Telehealth therapist | partial (combined classes; bullying policy) | partial (information night; no shadow day) | **full** (bell-to-bell locked cases) |
| P17 Market gardeners | **full** (schedule arithmetic, derived) | **full** (earlier files) | partial (35–80-minute rides; transfer at Brett) |
| P18 Young worker | **full** (adult education office in Tamworth) | partial (one evening class, in Conway) | partial (WIOA; CDL costs) |
| P19 Pastor | partial (policy JFABD; counselor and nurse) | partial (about 25 minutes, derived) | **full** (volunteer and privacy rules) |
| P20 Short-term rental owners | **full** (neither school in the EFA marketplace) | **full** (ClassDojo, conferences) | partial (Portsmouth and Oyster River from the site's data) |

## Notable findings

- **Kennett's contract ends June 30, 2027:** the board voted on February 15, 2024 to give notice. As of November 13, 2026 there is no new contract; the board says it is still negotiating.
- **The same rate at both high schools for 2026-27:** about $20,221 per pupil at Kennett (derived) and at Moultonborough Academy, whose rate is capped at Kennett's.
- **Enrollment is falling fast:** 204 on October 1, 2016, 154 in 2025 and 126 in September 2026.
- **State aid fell** from $2.15 million (FY2024) to $1.46 million (FY2027), mostly the loss of the extraordinary need grant.
- **Long rides:** the earliest Kennett pickup is 6:00 a.m. on Route 25, an 80-minute ride; afternoon riders from Route 25 change buses at Brett.

## Gaps to retry

- Whether grade 8 includes Algebra I (residents asked three times; no answer recorded).
- The teachers' and support staff contracts; Governor Wentworth's para pay.
- Late-bus drop points and the Moultonborough route sheet (folder link returns 404).
- The March 2026 annual meeting results, the October 7, 2026 tuition presentation and the Governor Wentworth contract terms.
- Recreation and camp fees; NH Works Conway office (refused access).
