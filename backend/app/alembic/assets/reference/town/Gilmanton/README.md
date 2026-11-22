# Gilmanton: Research for Ask NH Education Facts

Cited facts and figures for answering Gilmanton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the second ToLoad batch. Gilmanton is its own SAU (SAU 79):
- **Gilmanton School** serves kindergarten to grade 8 (308 students in November 2026).
- **High school:** students attend Gilford High under an AREA plan that runs to 2035. Career programs are at the Huot Center in Laconia and the Winnisquam Career Center.

The district votes by official ballot, with a deliberative session in January. Gilford High was researched in `../Gilford/`. These files add Gilmanton's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `gilmanton-school-early-grades-and-families.md` | No district preschool (Child Find screening only), BASE before-care in the school (from 7:00; $12 a morning), two classes per grade K–6, Route 107 runs (7:49–8:22; rides of 33–47 minutes), 10 early-release days (six Wednesdays), a reading specialist and two tutors, no resource officer, ALMA calls and emails (no texts), drop-off from 8:25 | 18 | 79 | 1 | 12 MB |
| `gilmanton-school-upper-grades-support-and-choices.md` | One K–8 building with its own middle school routines, the bell-to-bell device ban (JICJ), music and art kept (no band), Spanish for grades 7–8 now online through VLACS, homeschool access (JJJ, July 2026), the counselors as 504 coordinators, contracted therapists, the bullying policy rewritten November 10, 2026, Algebra I in grade 8 (17 students, all passed), NH DOE compliance findings | 14 | 88 | 2 | 15 MB |
| `gilford-high-from-gilmanton.md` | Huot and WiCC access (a morning Huot bus; van trips to WiCC), IEPs under the AREA plan (Gilmanton stays responsible), seven technology and engineering electives, the late bus in doubt for 2026-27, first high school pickups at 5:58–6:06, no GHS driver education course found, best-interest reassignments (policy JCA), open enrollment, state driver education rules | 10 | 31 | 2 | 3.5 MB |
| `money-and-governance.md` | Gilford tuition and the bond charge (30–32.5% of the budget; about 43% of the local school tax), $25,435 per student budgeted for 2026-27 against Gilford's $28,190 projection, the AREA renegotiation (no agreement; the subcommittee dissolved), the 2025-26 default budget, enrollment down to 308, the roof out to bid (a $560,733 roof fund), the tax cap adopted, the deliberative session's role | 10 | 54 | 3 | 28 MB |
| **Total** | | **52** | **252** | **8** | **58 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.07 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Gilmanton`). All 8 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 27 full, 30 partial, 3 from the site's data.
- **Topics:** one new topic, added to `../shared-topics.md`: `driver-education-rules` (New Hampshire's driver education requirement for license applicants under 18).
- **Places:** `district Gilmanton` 211, `town Gilmanton` 29, `district Gilford` 6, `sau 79` 2, no place 4.
- **Pending facts:** 19, citing draft minutes (mostly November 10, 2026) and the proposed 2027-28 budget.
- **Raw folders:** each under 100 MB. House numbers were stripped from the saved bus routes, and the original route document wasn't kept. The address scan finds only Gilmanton Academy, the polling place.
- **Quotes:** 562 of 739 quoted passages found word for word in the raw copies.
- **Main session fix:** the trust fund facts used the report's beginning-balance column. They now give the September 30, 2026 ending balances: the roof fund $560,732.63, the boiler fund $107,425.36, all accounts $1,608,405.84.
- **Spot checks** (main session, all matched after that fix):

  | Fact | Checked against |
  |---|---|
  | $25,435 budgeted per student | The January 31, 2026 deliberative session minutes |
  | Gilford's $28,190 projection | The November 9, 2026 work session minutes |
  | Enrollment of 308 | The November 10, 2026 minutes and packet |
  | The trust fund balances | The trustees' September 30, 2026 report (a scan) |

## Premises checked

| Question says | What the sources show |
|---|---|
| No preschool (P1.1) | Right: screening only |
| No before-care (P1.2) | It exists: BASE, from 7:00 |
| Early release every Wednesday (P4.3) | 10 days a year, six of them Wednesdays |
| Reading tutors during the day (P11.2) | Yes |
| A resource officer (P13.2) | None |
| A text alert (P20.3) | Calls and emails; no texts mentioned |
| Kindergartners in the same building (P14.1) | Right: one K–8 building |
| Music, art or band cut (P14.3) | Music and art kept; no band program |
| Languages only from 9th grade (P19.3) | No: Spanish in grades 7–8 |
| About 350 students (P2.2, P5.2) | Out of date: 308 |
| IEPs rebuilt at Gilford High (P6.2) | Not under the AREA plan |
| Everything geared to college (P8.2) | Not supported: seven technology electives |
| No late bus (P10.1) | Unclear for 2026-27 |
| Driver's ed at Gilford High (P12.1) | Not found |
| A bus before 6:30 (P16.2) | Right: first stops 5:58–6:06 |
| Locked into Gilford (P16.3) | Not entirely: reassignments are possible |
| Half the budget to Gilford (P2.3, P5.1) | About 31–32% of the budget, 43% of the local tax |
| Rising enrollment (P5.2) | No |
| A Blue Ribbon award (P9.2) | Right, in 2015 |
| Calendars that don't match (P12.3) | Right: 5 weekdays differ |
| Roof and boiler costs coming (P15.2) | Roof from the reserve; boilers working |

## Corrections and additions to earlier files

- **Gilford** (`../Gilford/`):
  - **Late bus:** its fact says GHS's handbook offers a late bus for Gilmanton students. Gilmanton's November 10, 2026 draft minutes say it isn't paying for one this year. The main session added that to the Gilford fact's note (`gilford-high-and-huot.md`, district-transportation 3).
  - **Career centers:** its file found only the morning Huot bus; the joint minutes add van trips to WiCC.
  - **The AREA renegotiation:** its money file left the outcome open. The subcommittee reached no agreement and was dissolved, which confirms the places.yaml note.
- **Alton** (`../Alton/`): its open enrollment facts are consistent. Gilmanton's side, who pays Prospect Mountain and how much, is here.

## Library notes (for review, not applied)

- **`district-practices.md`** says sau79.org and gilmantonschool.org need a Google sign-in (November 8, 2026). On November 21 both opened without one.
- **Coverage table:** it lists Gilmanton's kindergarten cutoff, registration, day length, preschool and high school options as not found. These files fill them.
- **`budget-form-and-vote-dates` 43:** the 2026 deliberative session was January 31 and the ballot March 10.
- **`open-enrollment-status`:** Gilmanton began paying Prospect Mountain tuition after the 2025 Pittsfield ruling, which supports adding the ruling from the opinion itself.

## Browser pass

Not needed for the answers. Not retrieved:
- **Gilmanton's 2025 town report** on UNH's repository (HTTP 403). It may list graduates' plans.
- **NH DMV's driver education pages** (HTTP 403).
- **The NH Supreme Court's Pittsfield opinion** (HTTP 403).
- **Gilford High's class information pages**, which need scripts to load.
