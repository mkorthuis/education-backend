# Wakefield: Research for Ask NH Education Facts

Cited facts and figures for answering Wakefield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the seventh wave of the second ToLoad batch. Wakefield is SAU 101, a one-district SAU:
- **Paul School** in Sanbornville serves preschool to grade 8.
- **High school:** Spaulding High in Rochester, under an AREA plan, which lets Wakefield pay for up to 10% of its high schoolers elsewhere (22 were at Kingswood in 2025-26).

The district votes by official ballot. Spaulding and Creteau were researched in `../Rochester/`, Kingswood and LRTC in `../Wolfeboro/`. Milton's research (`../Milton/`) ran alongside.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `paul-school-early-grades-and-families.md` | The 8:30–3:00 day and the paid Morning Program (from 7:15; $25 a week), Pre-K 3 and Pre-K 4 (the lottery for typical peers not settled; no hours posted), bus rides (up to 77 minutes on the Blue bus), Alma, the carline and Pick Up Patrol, Fresh Picks Café meals and allergies, indoor recess below a 15°F "real feel" | 14 | 77 | 1 | 28 MB |
| `paul-school-upper-grades-support-and-choices.md` | Policy JJJ (equal access for homeschool and EFA students), contracted special education specialists ($522,000 proposed), Paul School's ATSI status (not "Good Standing" on the fall 2025 list), the interim principal, a new world language teacher, the 2026-27 middle school redesign, sports fees, snow make-up days | 14 | 111 | 0 | 53 MB |
| `high-school-from-wakefield.md` | The AREA plan's 10% allowance (no lottery found), 22 Wakefield students at Kingswood, mid-high school moves, no late bus from Spaulding, no electrical program at Creteau (Dover has one), Spaulding's LNA option, local scholarships for trades | 10 | 52 | 4 | 33 MB |
| `money-and-governance.md` | Question 2 (70.07% yes) and the 2027-28 draft under the cap ($11,550,178), Spaulding tuition ($15,508.91 billed for 2025-26; $20,043 for 2026-27), the Area Agreement Committee (a withdrawal study under RSA 195-A:14), trust fund deposits, health insurance up 28.5%, special education busing ($687,693 against $125,000 budgeted), contracts | 9 | 90 | 5 | 82 MB |
| **Total** | | **47** | **330** | **10** | **196 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.27 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Wakefield`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 34 full, 24 partial, 2 from the site's data.
- **Topics:** no new topics. RSA 195-A rules are added to the library's `gov-area-agreements`.
- **Places:** `district Wakefield` 296, `town Wakefield` 23, `district Rochester` 5, statewide 4 (RSA 195-A), `district Governor Wentworth Regional` 2.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB. The bus route sheets list stops by house number, so only a derived file of streets and times was kept. Only the cited pages of the annual report were kept, since it lists staff pay and graduates by name.
- **Privacy:** the address scans find only Paul School and the district office on Taylor Way. Later, the main session also removed graduates' names (Paul School 8th grade) from the saved 2025-26 annual report texts, and deleted those PDFs.
- **Quotes:** 547 of 647 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Question 2, 1,791 of 2,556 votes (70.07%) | The district's post of the results |
  | The 2027-28 levy cap, $11,550,178 (**derived**: $11,095,272 × 1.041) | The superintendent's November 2026 FY28 budget sheets |
  | Special education, $2,895,270 of a $14,280,558 general fund (20.3%, **derived**) | The FY2027 budget book and MS-27 |
  | Spaulding's 2025-26 rate, $15,508.91 | The June 2, 2026 board minutes |

## Premises checked

| Question says | What the sources show |
|---|---|
| An 8:30 start (P1.1) | Correct; a paid Morning Program from 7:15 |
| A pre-K lottery (P1.2) | Not settled; hours and tuition not posted |
| Long rides from East Wakefield (P4.1) | About 30 minutes from Pine River Pond; up to 77 on one route |
| A weekend food bag program (P9.2) | None found |
| Indoor recess below freezing (P19.3) | No: below a 15°F "real feel" |
| Yearly homeschool paperwork (P6.2) | Out of date since July 1, 2026 |
| A big special education share (P7.1) | About 20% of the general fund |
| "Good Standing" with the state (P10.2) | Not on the fall 2025 list: still ATSI |
| An interim principal (P16.3) | Confirmed |
| World languages (P20.2) | Yes, from 2026-27 |
| A "Wakefield lottery" for Kingswood (P2.1) | No lottery found; the board approves up to 10% |
| A late bus from Spaulding (P2.3, P5.3) | None found |
| A move to Kingswood mid-high school (P14.1) | Possible, case by case |
| Lions scholarships only for four-year colleges (P14.3) | No; trades and technical schools too |
| Cornerstone Christian as a high school (P15.2) | It ends at grade 8 |
| The tax cap passed (P3.1, P17.2) | Right: 70.07% |
| An Area Agreement Committee for a better rate (P3.3) | No: it studies withdrawal |
| $200,000+ into trust funds yearly (P13.3) | Right for the years found; none in the 2027-28 draft |
| Board members against teacher contracts (P17.1) | One of five, in 2025 |

## Corrections and additions to earlier files

- **Rochester** (`../Rochester/`):
  - Its money file's fact 4 says the 2025-26 rate wasn't found. Wakefield's June 2, 2026 minutes say Rochester billed the 2024-25 rate ($15,508.91) because its notice came late.
  - Its fact 6 ("Area Agreement Committee") is the RSA 195-A:14 withdrawal study committee Wakefield's March 2026 ballot asked for; Wakefield named its two members on September 1, 2026.
  - Its Creteau file lacks the LNA option's clinical hours, nursing-home site and limited seats. The class of 2027's local scholarship deadline is February 17, 2027.
- **Wolfeboro** (`../Wolfeboro/`): its money file lists one Wakefield admission to Kingswood in 2026 (April). Governor Wentworth's March 9, 2026 minutes admitted another, and its August 27, 2025 minutes admitted two.

## Library notes (for review, not applied)

- **`district-preschool` 112 (Wakefield)** says the district doesn't describe its program. Its news now describes Pre-K 3 and Pre-K 4 and registration in Alma, though not hours or tuition.
- **`kindergarten-registration` 88 (Wakefield)** says no registration dates were posted. SAU 101 posted "Kindergarten Registration is Now Open" on April 9, 2026.
- **`students-2026-state-test-results` 12:** its note says the release doesn't say whether Wakefield's gains are percentage points. The site's data show 14 points in reading (24% to 38%) and 13 in math (17% to 30%), 2024 to 2026.
- **`students-hb-131-bullying-law`:** Wakefield's policy committee minutes quote NHSBA tying the 2026 bullying policy revision to HB 1817; the library ties the changes to HB 131. Worth a check.

## Browser pass

SAU 101's site shows a bot check to automated requests. The main session listed its document library in Chrome (`raw/browser/`); the files download directly, and agents used them.

Not retrieved:
- the Town of Wakefield's website (a bot check), for the March 2026 results, the town report and trust fund reports;
- SAU 101's web pages beyond the first few;
- NH DOE's fall 2026 accountability designations (HTTP 403);
- the 2005 Rochester–Wakefield agreement, whose blog host is gone.
