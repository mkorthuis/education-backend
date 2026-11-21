# Pembroke: Research for Ask NH Education Facts

Cited facts and figures for answering Pembroke, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the ToLoad towns. Pembroke is in SAU 53, and the Pembroke School District runs:
- Pembroke Hill School: K–4;
- Three Rivers School: grades 5–8;
- Pembroke Academy: grades 9–12. The Academy also takes Allenstown's, Chichester's and Epsom's high school students as their AREA school, and its students may take career programs at the Concord Regional Technical Center (CRTC).

The district decides its budget at a traditional annual meeting.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `pembroke-hill-and-families.md` | Kindergarten (the school's 8:00–2:20 day, no fee posted), no care at the school (doors at 7:40; the Boys & Girls Club bus to Allenstown, up to $105 a week), bus rides from Buck Street (18–45 minutes), Butler Bus replacing Dail, delay calls, pickup rules, class sizes (20.6 in grades 3–4 against a recommended 17), the special education preschool, infant care costs | 13 | 57 | 3 | 13 MB |
| `three-rivers-and-support.md` | Combined Three Rivers–Pembroke Hill bus routes (Main Street 7:17), Panther Prep orientation, one counselor for about 290 students, the August 2026 bullying policy (parents told within 48 hours), IEP moves and out-of-district placements (the district pays transport), homeschool and EFA access (policy JJJ; no annual filing since July 2026), board meetings and the budget calendar | 13 | 96 | 1 | 16 MB |
| `pembroke-academy.md` | CRTC programs (welding new, missing from the 2026-27 course book), 7 AP and 11 dual-credit courses, 20 honors courses, Early College ($150 at the Academy), four counselors (about 186 students each), the 2025 SAT mean (991), graduates' plans, Latin honors from the Class of 2030, no late bus, phone and parking rules, nearby private schools' tuition | 13 | 71 | 3 | 16 MB |
| `money-and-governance.md` | The 2026 rate ($22.74; local school $14.23, up $0.48), no default budget (a traditional meeting; $3 million cut in 2024), Academy tuition ($18,434.70; 44% of revenue; 373 sending-town students), SAU 53's cost split, no bonded debt and the $300,000 roof request, the Village School (closed 2019, sold, apartments), the tax cap recount (2,114 to 1,231) | 9 | 88 | 2 | 48 MB |
| **Total** | | **48** | **312** | **9** | **93 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.06 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Pembroke`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions are listed: 41 full, 17 partial, 1 from the site's data and 1 with none (P18.1, a late bus: none found).
- **Topics:** no new topics.
- **Places:** `district Pembroke` 269, `town Pembroke` 23, `sau 53` 12, `town Concord` 5, and one each for `district Allenstown`, `district Chichester` and `district Epsom`.
- **Pending facts:** 17, citing unapproved fall 2026 minutes and the FY2028 draft.
- **Raw folders:** each under 100 MB. The bus sheets list stops by house number, so only times and street names are kept.
- **Quotes:** 598 of 692 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $22.74, and local school $14.23 | The 2026 tax rate breakdown (OCR) |
  | Academy tuition, $18,434.70 | Allenstown's 2026 deliberative packet |
  | The tax cap recount, 2,114 to 1,231 | The recount results (OCR) |
  | The Village School sale, $151,000 | The broker's report |
  | Special education transportation, $959,500 | The FY2028 proposed budget packet |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day kindergarten, maybe with a fee (P1.1) | The school's full day, no fee posted |
| Care at the school by 8:00 (P1.2) | None; doors open at 7:40 |
| A 45-minute ride from Buck Street (P1.3) | 18–42 minutes in the morning, 26–45 in the afternoon |
| Texts on delay days (P5.1) | The handbook describes phone calls |
| Special education staffing short (P7.1) | "Fully staffed" in September; no openings posted |
| No public pre-K (P9.1) | Mostly right: a special education preschool only |
| Annual homeschool paperwork (P11.3) | None since July 1, 2026 |
| A middle school bus in Suncook Village (P14.2) | No separate one; routes are shared with Pembroke Hill |
| The budget "locked in" (P18.3) | Residents can amend it at the March meeting |
| Welding at the CRTC (P2.2) | New this year, but not in the Academy's course book |
| About 800 students at the Academy | 744 in 2024-25 |
| Running Start (P12.2) | Renamed Early College |
| Sports or JV cuts (P8.2) | None found; the board warned the next cut would reach extracurriculars |
| Average class rank (P17.3) | Not published; Latin honors from the Class of 2030 |
| A school tax up almost $2 (P2.1) | That was 2025 ($1.87); 2026 rose $0.48 |
| A default budget (P4.3) | None: Pembroke votes at a traditional meeting |
| Tuition students crowding the Academy (P10.2) | Not shown by the data |
| Paying SAU 53 to run Pembroke's schools (P10.3) | Pembroke runs all three of its schools |
| Rates set in spring (P4.1) | Set in the fall |
| The old Village School (P15.2) | Closed in June 2019, sold, being turned into apartments |

## Corrections and additions to earlier files

- **Concord** (`../Concord/high-school-and-pathways.md`): nothing contradicts it. The Academy's course book lists 12 CRTC programs and omits the new ones.
- **Brief:** its address www.pembrokeacademy.com is a parked domain; the Academy's site is https://pa.sau53.org.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 108 (Pembroke)** said the meeting's time and place weren't given. The warrant says March 7, 2026, 9:00 a.m., at Pembroke Academy.
- **Allenstown fact 2 and Epsom fact 28** said the Academy arrangement "may be an AREA agreement; not confirmed." Allenstown's and Chichester's 2026 articles call Pembroke Academy their AREA high school.
- **The coverage table** still marks Pembroke's kindergarten day as not found; it's here now.

## Site data issue

The site's Question 2 row for Pembroke has election night's 2,104 to 1,224. The recount gives 2,114 to 1,231, still adopted. Logged as item 11 in `../recommended-improvements.md` (A8).

## Browser pass

The agents' blocked pages were:
- the library's summer reading page and NH DOE's iPlatform (HTTP 403);
- town reports for 2016–2024 (server errors);
- the home education form (SharePoint sign-in).

None is essential to the answers.
