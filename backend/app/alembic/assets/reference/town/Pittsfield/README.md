# Pittsfield: Research for Ask NH Education Facts

Cited facts and figures for answering Pittsfield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the eighth wave of the second ToLoad batch. Pittsfield is SAU 51, a one-district SAU whose superintendent and business office have been provided by Concord's SAU 8 under contract since July 2026:
- **Pittsfield Elementary School (PES)** serves kindergarten to grade 6 from 2026-27. Its preschool moved to Head Start.
- **Pittsfield Middle High School (PMHS)** serves grades 7–12.
- **Career programs:** the Concord Regional Technical Center (CRTC).

The district votes by official ballot. In March 2026 voters told the board to pursue closing the high school after 2026-27; a study committee reports in December 2026. Neighbors were researched in `../Barnstead/`, `../Epsom/` and `../Concord/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `pittsfield-elementary-and-families.md` | Every Wednesday an early release in 2026-27 (the 12:35 time not found), Boys & Girls Club care at PES (6:30 to 5:30; $60 a week before, up to $85 after, with aid), staff shortages, the preschool's move to Head Start, kindergarten (37 children in 2025-26), bus spans of 75 minutes, missed IEP services under review, meals | 13 | 57 | 2 | 11 MB |
| `middle-high-support-and-choices.md` | The middle school's ATSI designation (one student group), no Pre-Calculus or AP taught at PMHS (advanced courses in Concord from September 2026), the May 2026 attendance rules and police agreement, 57 of 193 chronically absent, grade 6 back at PES, the phone ban, door security, homeschool access | 11 | 69 | 2 | 13 MB |
| `high-school-and-career-programs.md` | No shop courses (trades at the CRTC; 16 of 23 applicants accepted for 2025-26), the CRTC bus ($288.75 a day), five NHTI Early College courses, no co-op teams in 2026-27, the sportsmanship award, open enrollment (0% may leave), a late bus with no posted schedule, one counselor, the Foss scholarship ($880,000 over 411 awards), the class of 2026's plans | 13 | 52 | 4 | 23 MB |
| `money-and-governance.md` | The high school closure petition (395–239) and study committee (483–148), Concord's SAU contract ($260,000 a year, to 2029; "not a merger"), the FY2024 overspending and FY2025 deficit ($633,362, unaudited), the operating budget passing every year 2019–2026, Question 2 (65.6% yes), state aid down, no bond debt | 7 | 73 | 2 | 40 MB |
| **Total** | | **44** | **251** | **10** | **87 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.87 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Pittsfield`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 28 full, 32 partial.
- **Topics:** no new topics. The NHIAA transfer rule is added to `school-sports-rules`, and facts are added to the library's `district-preschool`, `special-ed-disputes` and `title-i-school-programs`.
- **Places:** `district Pittsfield` 237, `town Pittsfield` 8, statewide 6.
- **Pending facts:** 68. Most 2026 board and committee minutes are posted only as drafts, and several earlier 2026 minutes links are broken, so many facts cite drafts. Their figures should be rechecked when approved minutes are posted.
- **Raw folders:** each under 100 MB. The bus sheet copy keeps only street names; the original wasn't saved.
- **Privacy:** the October 27, 2026 tax-cap hearing minutes are kept only as a redacted text copy. The main session read the text of every saved PDF, and ran OCR on the scanned minutes: no residents' addresses. The address scans find only the schools and state offices.
- **Quotes:** 579 of 701 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | March 2026 votes: open enrollment 411–213, the study committee 483–148, the closure petition 395–239 | The town's March 10, 2026 results report (OCR) |
  | The FY2025 deficit, $633,362 | The 2026 warrant and deliberative session minutes |
  | Concord's SAU contract, $260,000 | The signed services agreement |

## Premises checked

| Question says | What the sources show |
|---|---|
| A 12:35 Wednesday release (P1.1) | Every Wednesday; the time isn't posted |
| No affordable after-school care (P1.1) | Boys & Girls Club at PES, with aid |
| Unfilled aide and teacher jobs (P1.2, P5.1) | Correct, by the district's account |
| A public preschool (P3.1) | Moved to Head Start for 2026-27 |
| Kindergarten way down (P3.2) | Not in 2025-26 |
| Long bus rides (P15.2) | Up to 75 minutes before and after school |
| Flagged for low scores (P4.1) | Partly: one student group |
| No advanced math (P4.3) | No Pre-Calculus or AP at PMHS; Concord courses from 2026 |
| Police for a few absences (P7.3) | No; only after a missed meeting at 15 absences |
| 6th grade at PMHS (P16.1) | Out of date: back at PES in 2026-27 |
| About 60 chronically absent (P18.1) | Confirmed: 57 of 193 |
| Trades through the CRTC (P6.1, P19.2) | Right; no shop at PMHS |
| High schoolers sent elsewhere (P6.2, P8.2) | Not decided; a study reports in December |
| Co-op teams (P12.1) | None in 2026-27 |
| A late bus (P12.3) | Exists; no schedule found |
| One counselor (P13.2) | Right: about 194 students |
| A deficit a few years back (P2.3) | Yes: $633,362 confirmed for FY2025 |
| A local vote to put the tax cap on the ballot (P2.2) | Not needed; state law put it there |
| Budgets voted down to default (P11.2) | The operating budget passed every year 2019–2026 |
| A roof or boiler bond (P17.2) | None; no bond debt |
| No answers during public comment (P18.3) | The board's own policy, not state law |

## Corrections and additions to earlier files

- **Northfield** (`../Northfield/`): its table lists Pittsfield Middle as grades 6–8, right for 2025-26; grade 6 moved to PES in 2026-27.
- **Barnstead** (`../Barnstead/`): its files say Pittsfield's study findings were due "by early December". Pittsfield's minutes now give December 1 (committee) and December 3, 2026 (board).
- **Alton** (`../Alton/`): its food program fact places End 68 Hours of Hunger's Pittsfield program at 7 Fayette Street. It moved to the SAU 51 building on Oneida Street, with weekly distributions from September 10, 2026.

## Library notes (for review, not applied)

None beyond the additions above.

## Browser pass

Not needed for the answers. Not retrieved:
- board minutes for February to May 2026, whose links on sau51.org return "not found" (HTTP 404);
- the PMHS bell schedule and CRTC bus schedule, and the PES early-release time;
- the High School Options Study Committee's report (due December 3) and the 2022 feasibility study;
- the NH Supreme Court's 2025 *Appeal of Pittsfield School District* opinion (HTTP 403);
- NH DOE's 2026 accountability lists and school-level absence data.
