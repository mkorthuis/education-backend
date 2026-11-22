# Brookline: Research for Ask NH Education Facts

Cited facts and figures for answering Brookline, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the second ToLoad batch. Brookline is in SAU 41 with Hollis:
- **The Brookline School District** runs Richard Maghakian Memorial School (RMMS, preschool to grade 3) and Captain Samuel Douglass Academy (CSDA, grades 4–6). It votes by official ballot.
- **The Hollis-Brookline Cooperative** runs Hollis-Brookline Middle School (grades 7–8) and High School (grades 9–12), both in Hollis. It votes at an annual meeting.

The cooperative was already researched in `../Hollis/`; these files cite Hollis's facts by topic and number and add Brookline's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `rmms-csda-and-families.md` | The 8:25 and 8:35 starts, the Brookline Afterschool Program (6:30 a.m. to 6:00 p.m.; $80, $115 or $180 a week), two-wave buses (high school rides of 32–49 minutes), the preschool (places by age, space and fit), kindergarten placement, class sizes against policy IIB (17, 20, 23), enrollment (564) and NESDEC projections, Star screening, Accelerated Grade 6 Math, the FY28 cuts | 14 | 78 | 4 | 75 MB |
| `hbms-support-and-choices.md` | Brookline students about 45% of HBMS's 7th grade, teams and homework, HBMS's special education staff, Brookline's own JJJ (adopted October 28, 2026), homeschool and EFA facts, no busing to ASD, para pay ($17.69–$26.19) and substitutes ($100 a day), team cuts, athletics against activities in the budget | 12 | 57 | 3 | 20 MB |
| `hbhs-and-pathways.md` | STEM courses beside Chelmsford High, seven college-credit courses, career programs at Nashua (welding at Alvirne), counseling, HBHS's enrollment (712), clubs and the late bus to Brookline, the fields, college costs and debt (a new topic) | 13 | 42 | 3 | 60 MB |
| `money-and-governance.md` | The 2026 rate ($25.56; school $17.52, down from $17.81), new disparity aid ($880,771 in FY2027, less in FY2028), the 8% cap (kept 459 to 513 in 2025) and HB 1300's tighter cap, the failed FY2027 budget and its default, the FY2028 draft ($14,452,291; four positions cut), health insurance (+15.1%), the 2026–2029 teachers' contract ($51,424 start), no school bond | 8 | 74 | 5 | 74 MB |
| **Total** | | **47** | **251** | **15** | **229 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.18 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Brookline`). All 15 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 34 full, 25 partial, 1 from the site's data.
- **Topics:** one new topic, added to `../shared-topics.md`: `college-costs-and-debt-nh` (state funding for New Hampshire's public colleges, tuition and graduates' borrowing).
- **Places:** `district Brookline` 153, `district Hollis-Brookline Cooperative` 62, `town Brookline` 14, `sau 41` 13, no place 9.
- **Pending facts:** 21, citing draft minutes and the FY2028 drafts.
- **Raw folders:** each under 100 MB. Bus-route house numbers are left out. Later, the main session also removed residents' births, marriages and deaths from the saved 2025 town report text, and deleted that PDF.
- **Quotes:** 558 of 621 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $25.56, and school $17.52 | The town's tax rate history |
  | The cap repeal vote, 459 to 513 | The town's 2025 annual report |
  | After-school care at $80, $115 and $180 a week | The program's 2026-27 payment schedule |
  | Policies JJJ and IIB | The adopted texts, read in Chrome |

## Premises checked

| Question says | What the sources show |
|---|---|
| An 8:25 start (P1.2) | RMMS; CSDA starts at 8:35 |
| A kindergarten lottery (P1.1) | None; the preschool fills by age, space and fit |
| A Route 130 drop-off line | Not supported by any source |
| Crowding at RMMS and CSDA (P9.2) | Mixed: 564 students, below the peak of 587, but grades 4–5 run 22–23 against a guideline of 23 |
| 5th graders skipping a math grade | No skip; Accelerated Grade 6 Math covers two years in one |
| Homeschool paperwork filed with SAU 41 (P6.1) | Out of date: none needed since July 1, 2026 unless using school programs |
| Busing to ASD (P13.1) | Brookline doesn't bus to ASD |
| A "voucher" (P13.2) | An Education Freedom Account; this year's cap was reached in August |
| SAU 41 sets para pay (P16.1) | Each district has its own contract |
| Most extra funding goes to sports (P17.3) | The budget lines bear it out |
| About 750 at HBHS (P10.1) | 745 in 2024-25; 712 now |
| Extra aid "next year" (P2.1) | It came in FY2027; the FY2028 estimate is $83,356 lower |
| A $33.11 million cooperative placeholder (P8.1) | Not found in any posted document |
| Health insurance jumping (P8.3) | Right: 15.1% for 2026-27 |
| The teachers' contract up for renewal (P19.2) | No: approved for 2026–2029 |
| Different calendars (P18.2) | The same, except one orientation day and graduation |
| A surprise bond later (P19.3) | Brookline has no school bond |

## Corrections and additions to earlier files

- **Hollis** (`../Hollis/`): nothing contradicts it. Brookline's files add:
  - Brookline's own bus list, confirming no late bus;
  - Brookline's JJJ, adopted October 28, 2026 (Hollis's file says Brookline's JJJ-R "is filed separately"; none was found);
  - HBMS's coaching vacancies by November;
  - Star screening adopted K–8 across SAU 41.
- **Hollis's IIB** uses 18 for kindergarten; Brookline's uses 17.
- **Transportation phone number:** the Brookline FAQ prints 603-465-7085, apparently a typo for 603-465-7805.
- **Brief:** "Cavanaugh" should read Cavalier Court.

## Browser pass (November 21, 2026)

- **Read in Chrome** from the SAU 41 policy book (which loads only by script):
  - **JJJ, as adopted October 28, 2026:** replaces the second-reading draft the facts first cited.
  - **IIB, class size:** added as district-classrooms-and-staff 7.
  - **No JEB:** the Brookline manual has no kindergarten entry-age policy.
  - The texts are in `raw/middle/policies/sau41-brookline-policies-jjj-iib-2026-11-21.txt`.
- **Not retrieved** (none essential):
  - the town's 2024 annual report on UNH's repository (a bot check);
  - Naviance (needs a student login);
  - NH DOE's iReport.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- 4 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
