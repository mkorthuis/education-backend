# Candia: Research for Ask NH Education Facts

Cited facts and figures for answering Candia, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the second ToLoad batch. Candia is in SAU 15 with Auburn and Hooksett:
- **Henry W. Moore School** serves kindergarten to grade 8 (290 students on October 27, 2026).
- **High school:** students attend Pinkerton Academy in Derry under a 2018–2038 agreement.

The district votes by official ballot, with a deliberative session. Pinkerton was researched in `../pinkerton/`, and the rest of SAU 15 in `../Hooksett/` and `../Auburn/`. These files add Candia's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `moore-early-grades-and-families.md` | Full-day kindergarten (8:40–3:15), New Morning after school only ($22 a day; no morning care), the cutoff (5 by September 30), spring 2026 scores (52% math) against Auburn and Hooksett, specials kept, the CYAA ski bus ($125), lunch prices ($4.00; reduced $0.40), no public preschool posted, M and C's stop on Bus C1, First Student's late-pickup charge | 18 | 69 | 3 | 30 MB |
| `moore-upper-grades-support-and-choices.md` | The homeschool evaluation repeal (Candia's policy still describes it), policy JJJ revised for EFA students (November 2, 2026), no honors math or Algebra I found, Jesse Remington (an EFA provider; cap reached), private school busing and evaluations (Candia's duty), the bullying and phone rules, Title IV before- and after-school help, band (no drama advisor), the para line over budget, the 21-day IEP rule | 13 | 83 | 3 | 31 MB |
| `pinkerton-from-candia.md` | The transcribed agreement, two Pinkerton buses (first pickups 5:55 and 5:58; rides up to 86 minutes), the November 2026 decision to keep the routes, no late bus, IEPs (Pinkerton's coordinator, Candia's responsibility), CTE seats not published, no AP for freshmen, 658 diplomas in 2026, marching band without audition, JROTC | 8 | 41 | 3 | 5.4 MB |
| `money-and-governance.md` | The Budget Committee–School Board split (2025 rejected 472 to 488; 2026 passed 408 to 355 at $11,833,313), Pinkerton at 18.5% of the budget (32.1% for all high school costs), two Candia trustees on Pinkerton's board, the tax cap's estimated effect, the 2026 rate ($14.84), the 2022 energy lease ($191,645 a year), the building's open needs, SchoolCare, the elderly exemption | 7 | 52 | 4 | 60 MB |
| **Total** | | **46** | **245** | **13** | **126 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.11 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Candia`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 36 full, 22 partial, 2 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Candia` 203, `town Candia` 29, `district Pinkerton Academy` 8, `sau 15` 2, no place 3.
- **Pending facts:** 5, citing draft minutes and the 2027-28 draft budget.
- **Raw folders:** each under 100 MB. The route sheets were saved with street names only, and the original PDFs deleted. The address scan finds only the bus contractor's and Pinkerton's own addresses.
- **Quotes:** 625 of 728 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $14.84 | The selectmen's November 2, 2026 minutes |
  | The 2026 budget, $11,833,313, passed 408 to 355 | The March 2026 election results and the February 5 minutes |
  | The energy lease, $191,644.60 a year (**derived**) | The principal and interest lines in the November 2 packet |
  | First Pinkerton pickup, 5:55 | The 2026-27 route sheet (street names only) |

## Premises checked

| Question says | What the sources show |
|---|---|
| No full-day kindergarten (P1.1) | Full day, 8:40–3:15 |
| New Morning at Moore (P1.2) | After school only |
| Free lunch now (P11.2) | No: $4.00, or $0.40 reduced |
| A public preschool (P16.1) | None posted |
| Specials cut (P6.2) | No cuts found |
| An annual homeschool assessment (P7.2) | Repealed July 1, 2026 |
| Honors math in grades 7–8 (P9.1) | None found |
| Paras and speech cut under the cap (P4.2) | Not so far: the draft adds two paras |
| Under 300 at Moore, over 3,000 at Pinkerton (P3.1) | Right |
| Pickup at the end of the driveway (P3.2) | Mostly not: many stops are at intersections |
| A late bus (P3.3) | None |
| A graduating class of 800 (P15.2) | High: 658 diplomas in 2026 |
| AP as a freshman (P9.3) | None in practice |
| Marching band auditions (P20.2) | None |
| Health insurance up 23% (P2.1, P10.2) | Not shown: Candia's draft assumes 12% |
| The board has picked its cuts (P2.1, P4.2, P20.3) | Not yet |
| One seat on Pinkerton's board (P10.3) | Two Candia trustees |
| A building bond coming (P17.1) | None in the records |

## Corrections and additions to earlier files

- **Auburn** (`../Auburn/`): its Algebra I table's note said Candia's students don't attend Pinkerton under a contract. The main session corrected it to point to Candia's own agreement, and reloaded Auburn.
- **Auburn's SAU figures** match Candia's: Candia paid SAU 15 $186,966 in 2024-25, the same 13.66% share.
- **Pinkerton** (`../pinkerton/`):
  - Its README calls Candia's agreement "scanned and untranscribed"; an OCR text is now in `raw/high/`.
  - Pinkerton's "cte-programs" page now returns HTTP 404; the CTE home page lists the same programs.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 16 (Candia):** the 2026 budget was amended to $11,833,313 and passed 408 to 355.
- **`high-school-tuition-options` 15 (Candia)** can now cite the transcribed agreement.
- **Coverage table:** Candia's preschool is "not found". These files confirm no program is posted.

## Site caution

Moore School's home page and some other Moore pages carry unrelated online-casino text, planted on the school's site; Hooksett's research saw it too. No fact relies on those passages. The district may want to know.

## Browser pass

Not needed for the answers. Not retrieved:
- NH DOE's 2024 approval letter for Candia (HTTP 403);
- the December 2025 Budget Committee minutes (HTTP 404);
- Pinkerton's Purple Star page (HTTP 404).
