# Strafford: Research for Ask NH Education Facts

Cited facts and figures for answering Strafford, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the eighth wave of the second ToLoad batch. Strafford is SAU 105, a one-district SAU since it left SAU 44 on July 1, 2021:
- **Strafford School** serves preschool (Little Spartans) to grade 8.
- **High school:** Coe-Brown Northwood Academy, under an agreement running to 2033.

The district decides its budget at a traditional annual meeting (an SB2 petition failed 17–75 in 2021). Coe-Brown was researched in `../Barrington/`, `../Deerfield/` and `../Northwood/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `strafford-school-early-grades-and-families.md` | Seven bus routes (30–40 minute morning runs; a route cut only on a draft list), buses shared with Coe-Brown's runs, Little Spartans (half-day, $125 or $175 a month), KinderCampus care at the school (7:00 to 5:30), the 8:40–3:10 day, kindergarten homerooms of 14, 15 and 14, the nurse, PickUp Patrol | 9 | 56 | 2 | 5 MB |
| `strafford-school-upper-grades-support-and-choices.md` | Scores (45% math, 48% reading in 2025–26; grade 7–8 opt-outs), the November 10 draft cut list (tutoring, summer school, athletics, a case manager), three counselors (2 full-time equivalents), no world language (a new Spanish Club), Coe-Brown's survey of Strafford freshmen, sports (no track team), homeschool access under policies JJJ and IHBG-R (IHBG still describes the pre-2026 rules) | 10 | 100 | 2 | 4 MB |
| `coe-brown-from-strafford.md` | The 2023–2033 agreement (automatic admission, special education, career programs, the Education Committee seat), three bus runs ($91.20 a bus a day; no late bus), Coe-Brown's shop courses and Career Ed program, Assisted Study, the Math Lab | 11 | 52 | 4 | 3 MB |
| `money-and-governance.md` | The FY28 proposal ($15,841,849, up 9.6%) against the tax cap (61.8% yes; about $1.25 million to close), the 2026 rate ($14.12 after revaluation; schools about 70%), the 1966 building and its bond (paid off in 2030), the $67,210 boiler from the capital reserve, the playground audit, SAU 105's costs since leaving SAU 44, policy KF's facility-use fees (gym $110 a day) | 9 | 66 | 2 | 4 MB |
| **Total** | | **39** | **274** | **10** | **15 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.75 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Strafford`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 37 full, 23 partial.
- **Topics:** no new topics.
- **Places:** `district Strafford` 227, `town Strafford` 19, `district Coe-Brown Northwood Academy` 10, statewide 3 (NHIAA rules).
- **Pending facts:** 33, mostly citing the draft 2026-27 Pre-K–5 handbook (the board approved it with changes; the published version loads only by script) and the draft FY2025 audit.
- **Raw folders:** each under 100 MB. The bus route copy has house numbers removed. Minutes, the 2025 town report and the November 18 board packet are kept only as cleaned text or excerpts, without residents' names, emails or addresses.
- **Privacy:** the address scans find only the school, the SAU office and the town hall.
- **Quotes:** 584 of 685 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The FY28 proposal, $15,841,849, up $1,389,109 | The November 18, 2026 budget planning snapshot |
  | The boiler and water heater, $67,210 from the capital reserve | The November 18, 2026 board packet |
  | The 2026 tax rate, $14.12 | The town's tax rate page |

## Premises checked

| Question says | What the sources show |
|---|---|
| A bus route cut for the tax cap (P1.1, P11.1) | Only on a draft list |
| Hour-long rides (P1.1) | 30–40 minutes on today's routes |
| Half-day preschool with a waitlist (P1.2, P7.3) | Half-day; no waitlist posted |
| An 8:45 start, 3:10 dismissal (P11.1, P1.3) | 8:40 and 3:10 |
| A plan for the car line (P8.2) | None found |
| A nurse all day (P15.3) | One full-time nurse budgeted |
| Cuts to 4th and 7th grade teachers (P8.3) | The draft names grades 2 and 3 |
| Under half proficient (P3.2) | True for 2025–26 |
| Tutoring, summer school, sports cut (P3.3, P8.1, P19.3) | On the draft list; nothing decided |
| A full-time counselor (P13.2) | Three counselors, 2 full-time equivalents |
| An Intent to Homeschool with SAU 105 (P9.1) | No SAU form; NH DOE's site. Policy JJJ and IHBG-R give equal access by written request to the principal |
| No world language (P17.1) | Right; a Spanish Club began in November 2026 |
| A dedicated Northwood bus (P4.3) | Shared with elementary runs |
| A late bus (P12.3) | None found |
| Automatic admission at Coe-Brown (P14.1) | Correct |
| $1.25 million in cuts, under 400 students (P2.1) | A gap from the proposal; 349 students plus 13 preschoolers |
| A $67,000 boiler (P2.2) | $67,210, from a reserve, not new taxes |
| A December hearing (P13.3) | December 2, 6:00 p.m.; the legal hearing is January 27 |
| SAU 105 added a superintendent's salary (P10.2) | Partly; the 2019 plan projected a slight saving |

## Corrections and additions to earlier files

- **Northwood** (`../Northwood/`):
  - Its money file gives Strafford's share of SAU 44's fund balance as about $82,189. Strafford's 2019 report gave $68,830.36 and its 2020 minutes "$68,000" (different dates).
  - Its early grades file lists Little Blessings Learning Center's site as not found. Little Blessings is Strafford KinderCampus's Northwood location (straffordkindercampus.com).
- **Barrington and Deerfield:** their Coe-Brown agreements give the sending district the final say on special education; Strafford's agreement has no such clause.

## Library notes (for review, not applied)

- **`district-preschool` 105 (Strafford)** says no tuition is posted and gives only 9:00–11:30. The board set 2026-27 tuition at $125 a month (two days) and $175 (three days) on February 11, 2026, and the sessions are 9:00–11:30 and 12:15–2:45.
- **`places.yaml` (Strafford–Coe-Brown)** says 151 of Strafford's 157 high schoolers attended in 2025-26. Strafford's September 2026 report gives 157 of 165.

## Browser pass

Strafford's policy manual, handbooks, staff directory and athletics pages load only by script. The main session opened the policy manual in Chrome and saved four policies from their Google Drive files (`raw/middle/browser/`): JJJ, IHBG and IHBG-R (home education access), folded into the upper grades file, and KF (facility use and fees), folded into the money file.

Not retrieved:
- the published 2026-27 handbooks, and policies DB, BEDH, IHBB, IKE and JJLC;
- coebrown.org's driver education page (HTTP 403);
- the State Board's 2023 approval materials (HTTP 403);
- afternoon bus times, which aren't printed.
