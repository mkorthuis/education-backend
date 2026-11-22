# Deerfield: Research for Ask NH Education Facts

Cited facts and figures for answering Deerfield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the second ToLoad batch. Deerfield is in SAU 53 with Allenstown, Chichester, Epsom and Pembroke:
- **Deerfield Community School (DCS)** serves preschool to grade 8.
- **High school:** families choose Concord High, Coe-Brown Northwood Academy or Pembroke Academy, under three agreements that all end June 30, 2027.

The district votes by official ballot. SAU 53 and Pembroke Academy were researched in `../Pembroke/`, and Concord High in `../Concord/`. These files add Deerfield's side and place Coe-Brown facts for Northwood and Barrington to reuse.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `dcs-early-grades-and-families.md` | The preschool ($65 and $85 a month; limited spots, a waiting list), no school-run before- or after-school care, 43 incoming kindergartners for three teachers, bus rides (mornings 28–50 minutes; the last child off 42–61 minutes after 2:40), storm notices (no posted call time), Alma and the other parent systems, the policy on roads a bus can't use | 14 | 62 | 1 | 16 MB |
| `dcs-upper-grades-support-and-choices.md` | Scores (52% math, 59% reading in 2026), staffing on the draft 2027-28 roster, Grade 8 Algebra, VLACS, no shop class, no world language since about 2020, homeschool and EFA access (policy JJJ), Fair Day closing, the state's special education determinations, Deerfield graduates' first math grades at Concord High | 14 | 101 | 2 | 40 MB |
| `high-school-choice.md` | The three agreements side by side (admission, IEPs, 504s, career programs, buses), two high school buses (Concord and Coe-Brown; none to Pembroke; no late bus), 116 Deerfield students at Concord High, Coe-Brown's FFA and SNHU courses ($100 each), divisions, switching after 9th grade, the CRTC | 8 | 65 | 6 | 36 MB |
| `money-and-governance.md` | The budget failing every year since FY2022 (684 to 837 in 2026), the 2026 rate ($15.44; school $10.69), tuition by school (Coe-Brown $21,617; Concord $21,043.15; Pembroke $18,434.70), the 2026 advisory vote to keep choice (765 to 750), SAU 53's share (21.5%, $544,290) and the planning committee (812 to 648), the building study (446–496 students), $1.61 million in trusts, no debt | 9 | 67 | 10 | 46 MB |
| **Total** | | **45** | **295** | **19** | **138 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.16 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Deerfield`). All 19 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial.
- **Topics:** no new topics.
- **Places:** `district Deerfield` 272, `district Coe-Brown Northwood Academy` 8, `town Deerfield` 7, `district Concord` 5, `sau 53` 1, `district Pembroke` 1, no place 1.
- **Pending facts:** 23, citing draft minutes, the draft 2027-28 roster and the proposed 2027-28 budget.
- **Raw folders:** each under 100 MB. The route sheets list stops by house number, so only a derived file with times and street names was kept. The address scan finds only the school's own address. Later, the main session also removed graduates' names from the saved Concord High report to Deerfield, and deleted that PDF.
- **Quotes:** 708 of 827 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 budget vote, 684 to 837 | The posted 2026 ballot results |
  | The advisory vote on choice, 765 to 750 | The ballot's handwritten tally (the 7 is looped; 1,515 ballots in all, in line with the other articles) |
  | The school rate, $10.69 | The November 4, 2026 board packet |
  | SAU 53's share, $544,290 | The voted 2026-27 budget |

## Premises checked

| Question says | What the sources show |
|---|---|
| Hard-to-get preschool spots (P1.1) | Partly: limited, with a waiting list; $65 or $85 a month |
| Little care in town (P1.2) | No school-run care found |
| An hour's ride for a 3rd grader (P2.1) | Partly, in the afternoons |
| Everything in Alma (P8.1) | Mostly not: lunch money, messages and forms use other systems |
| About half proficient (P2.2) | Close: 52% math, 59% reading |
| Algebra before high school (P6.1) | Yes: Grade 8 Algebra |
| Spanish or French only from 9th grade (P18.3) | Right: none at DCS since about 2020 |
| All-or-nothing homeschooling (P9.1) | No: policy JJJ allows part-time access |
| Buses to all three high schools (P3.1) | Partly wrong: Concord and Coe-Brown only |
| A late bus (P11.1) | None found |
| A cap on Deerfield students at Coe-Brown (P3.2) | No numeric cap |
| The tax "creeping up" (P4.1) | The levy rose; the rate fell in 2025 and 2026 |
| Choice locked in (P10.1) | No: all three agreements end June 30, 2027 |
| SAU 53 saving money (P16.1) | No study exists |
| A building bond coming (P17.2) | None proposed; a $45.5 million bond failed in 2022 |

## Corrections and additions to earlier files

- **Concord** (`../Concord/`): Concord High's financial aid night, Apply NH and career resources page and its agriculture pathway aren't in Concord's files.
- **Pembroke** (`../Pembroke/`):
  - Pembroke Academy's greenhouse, botany, ecology and wildlife electives, and its lack of FFA, are new.
  - Its money file says Deerfield "also sends a few" to Pembroke Academy: Deerfield budgeted 5 in 2025-26, 3 in 2026-27 and 2 for 2027-28.
  - Its SAU 53 special education fact cites a presentation given to the Deerfield board. It uses only the presentation's statewide rule on court-ordered placements, and its note says so, so no change was made.

## Library notes (for review, not applied)

- **`district-preschool` 22** says no tuition is posted for Deerfield. The DCS Preschool's site posts $65 a month (two days) and $85 a month (three days).
- **`kindergarten-day-length`:** the coverage table still marks Deerfield's kindergarten day as not found. These files add it.
- **`high-school-tuition-options` 21 (Deerfield):** all three agreements end June 30, 2027 and were being renegotiated in November 2026.
- **`cte-centers-overview` 6** calls the center the "Concord Regional Technology Center". The center's own page says "Concord Regional Technical Center".

## Browser pass

Not needed for the answers. Not retrieved:
- **The town's listed website** (townofdeerfieldnh.com) redirects to an unrelated gambling site. The elementary agent's one request saw the redirect, and nothing from it was saved or used. So the town's reports, recreation pages and tax documents are missing.
- **Ratings:** Niche and SchoolDigger (bot checks), so the "B" in P10.2 wasn't checked.
- **Coe-Brown's own pages**, and its enrollment report for Deerfield, which is in the board's drive rather than posted.
- **Board minutes:** those for September 16, October 21 and November 18, 2026 aren't posted.
