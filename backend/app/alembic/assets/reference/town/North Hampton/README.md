# North Hampton: Research for Ask NH Education Facts

Cited facts and figures for answering North Hampton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the second ToLoad batch. North Hampton is in SAU 21 with Hampton Falls, Seabrook, South Hampton and the Winnacunnet Cooperative. Hampton's own K–8 district is SAU 90, not SAU 21.
- **North Hampton School (NHS)** serves preschool to grade 8 (272 students on October 1, 2025).
- **High school:** Winnacunnet High School in Hampton. Career programs are at the Seacoast School of Technology (SST) in Exeter.

The district votes by official ballot. Winnacunnet was researched in `../winnacunnet/`, `../Hampton/` and `../Seabrook/`. These files add North Hampton's side and some new Winnacunnet facts.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `nhs-early-grades-and-families.md` | Recreation department care at the school (from 7:00; until 5:30; $12 a day), Route 111 (the school's own road; rides of 2–38 minutes), the specialized preschool (at least 51% with IEPs; no lottery), full-day kindergarten, the cutoff (5 by September 30), 11–17 students per teacher in K–5, starting within 24–48 hours, PickUp Patrol and ParentSquare, iPads to grade 3 | 13 | 69 | 2 | 51 MB |
| `nhs-upper-grades-support-and-choices.md` | Optional Algebra I inside grade 8 math, no branded reading method named, each board's own phone policy, volunteer fingerprinting ($23; 3–4 weeks), homeschool access (JJJ), EFAs and IEP services, one counselor and a psychologist, the secured building, the $90,000 SRO line ($24,666 spent), out-of-district tuition | 15 | 71 | 1 | 26 MB |
| `winnacunnet-from-north-hampton.md` | Winnacunnet's size (970, not 1,100), three Winnacunnet bus routes (first pickup 6:39; all arrive 7:25), SST Electrical (new, full) and no HVAC, SST classes of 90 minutes, 13 AP courses (79.6% scoring 3 or higher in 2024), the transition program to the 22nd birthday, the athletic trainer, Personal Finance, grade 8 math (72% in 2025, 35% in 2026) | 13 | 41 | 2 | 65 MB |
| `money-and-governance.md` | Cost per pupil ($34,105.89 in 2024-25), the 85.26-acre campus, the 3.2% raise (non-union staff only), no school bond, falling enrollment and a 0.14% budget cut for 2026-27, the tax split (30.2% to Winnacunnet), SAU 21's share (about 3.1%), the default budget ($74,364 lower), the elderly exemption (56 owners), the SRO split (75% school) | 9 | 66 | 4 | 42 MB |
| **Total** | | **50** | **247** | **9** | **184 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.13 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh "North Hampton"`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 25 full, 35 partial.
- **Topics:** no new topics.
- **Places:** `district North Hampton` 179, `town North Hampton` 27, `district Winnacunnet Cooperative` 27, `sau 21` 7, no place 7.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB. The saved bus files keep only times and street names. The address scan finds only the school's own address (201 Atlantic Avenue).
- **Privacy:** two residents' street addresses were removed from the text copy of the deliberative minutes. The official PDFs kept beside it (the minutes and the 2025-26 annual report) still show them. Raw folders stay local and aren't loaded. Later, the main session also removed residents' deaths, marriages and births from the saved FY25 town report text.
- **Quotes:** 606 of 685 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Cost per pupil, $34,105.89, and the $74,364 default gap | The 2026-27 budget presentation |
  | The 85.26-acre parcel | The town's assessing record |
  | 79.6% of AP exams scored 3 or higher (2024) | Winnacunnet's 2024-25 annual report |
  | First Winnacunnet pickup, 6:39 | The 2026 route sheet (street names only) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Care on site (P1.1) | Yes, run by the town's recreation department |
| A pre-K lottery (P7.1) | None found; a specialized program |
| Full-day kindergarten (P10.1) | Right |
| Six weeks to enroll (P14.1) | Usually 24–48 hours |
| An ESOL teacher in the building (P18.1) | Not settled; one at SAU 21 |
| Algebra or Geometry in grade 7 or 8 (P3.1) | Partly: optional Algebra I in grade 8 |
| One SAU-wide phone ban (P8.3) | Each board has its own policy |
| Background-check hoops (P9.3) | Partly: fingerprints for regular volunteers |
| Talk of cutting sports, band or art (P19.1) | None found; the budget passed 489 to 163 |
| Locked doors and an SRO (P19.2) | Partly |
| A 30-student class and a 1,100-student WHS (P8.1) | 30 is the whole grade; WHS has 970 |
| HVAC at SST (P4.1) | No; Electrical is new and full |
| Half-day CTE (P4.3) | No: 90 minutes a day |
| Transition to 21 or 22 (P16.1–P16.2) | To the 22nd birthday, unless a regular diploma ends it |
| About $34,000 and 270 students (P2.1, P6.1) | Right |
| A 3.2% raise (P6.2) | Non-union staff only |
| Taxes jump with bonds (P9.1) | No bond outstanding or proposed |
| Flat enrollment, rising budgets (P15.1) | Enrollment falling; the 2026-27 budget fell |
| No plain-English breakdown (P17.2) | Partly wrong |

## Corrections and additions to earlier files

- **The brief** said SAU 21 includes Hampton. It doesn't.
- **Hampton** (`../Hampton/`): its Winnacunnet cost share row for North Hampton (13.35%, $4,322,482) matches Winnacunnet's annual report.
- **Seabrook** (`../Seabrook/`):
  - **Policies:** its file says SAU 21's policies are on Simbli. North Hampton's handbook points to SAU 21's BoardDocs, which holds every member board's manual.
  - **ESOL:** the SAU 21 budget's ESOL line for 2026-27 is $172,113.
- **Winnacunnet** (`../winnacunnet/`): this file adds facts that folder lacks, placed `district Winnacunnet Cooperative`. They cover AP results (2019 and 2024), college applications, SAT benchmarks and special education programs.

## Library notes (for review, not applied)

- **Coverage table:** it lists North Hampton's kindergarten cutoff as missing. It is 5 by September 30, from the principal's January 2025 note.
- **`district-preschool` 84:** it says eligibility wasn't posted. The 2026-27 preschool slides describe a specialized program with at least 51% of children on IEPs.

## Browser pass

Not needed for the answers. Not retrieved:
- **SAU 21's BoardDocs** refused requests after the first 32 policies, so no board minutes or Winnacunnet policies were read.
- **winnacunnet.org** blocked automated requests, so its athletic trainer, transitions and youth survey pages weren't read.
- **NH DOE's** vocational rehabilitation pages.
- **The town's recreation program list.**
