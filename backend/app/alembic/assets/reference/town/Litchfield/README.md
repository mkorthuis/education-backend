# Litchfield: Research for Ask NH Education Facts

Cited facts and figures for answering Litchfield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the ToLoad towns. Litchfield is SAU 27, a one-district SAU:
- Griffin Memorial School: preschool to grade 4;
- Litchfield Middle School: grades 5–8;
- Campbell High School: grades 9–12.

Campbell students may take career programs at Hudson's Palmer Center at Alvirne. The district votes by official ballot.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `griffin-memorial-and-families.md` | Full-day kindergarten (67 children in four rooms; policy aims at 18), the September 30 cutoff (policy JEB), dismissal (2:45–3:00), care in the school 6:30 a.m.–6:00 p.m. ($95–$200 a week), First Student drop-offs (five-day requests only), UFLI phonics, IEPs from other New Hampshire districts, grade 3–4 results against the state, aide vacancies, the state improvement designation | 14 | 57 | 2 | 39 MB |
| `middle-and-high-school.md` | Drop-off 7:15 and a 7:22 late bell at LMS, Campbell at 7:35, phones banned bell to bell, buses to Palmer (welding, no electrical), the late bus ($32,850, left out of the 2027-28 proposal), AP (Calculus BC, no Chemistry; sciences every other year), SNHU courses, VLACS, Sophomore and Senior Projects, grade weights, the maker space | 9 | 77 | 1 | 15 MB |
| `support-daily-life-and-choices.md` | Why LMS starts early (combined bus runs since 2021), bus times, Route 3A traffic, cooling (Griffin heating only), GreatSchools against Bedford and Hollis-Brookline, policy JJJ for EFA and home-educated students (the 50% rule), Bishop Guertin, lunch participation, Griffin's missing secure vestibule, enrollment by race | 14 | 83 | 3 | 59 MB |
| `money-and-governance.md` | The $38.9 million Griffin renovation and addition for March 2027 (about $297, then $755 a year on a $618,000 home), the 2027-28 budget ($28,073,982, +2.69%; 19 positions cut, self-insured health plan), the school rate ($9.73), special education ($5,367,067; 14 students out of district), starting pay ($47,848, $3,152 below Hudson), default-budget cuts, meetings at 5:30 | 5 | 62 | 8 | 48 MB |
| **Total** | | **42** | **279** | **14** | **161 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.15 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Litchfield`). All 14 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 37 full, 23 partial.
- **Topics:** no new topics.
- **Places:** `district Litchfield` 270, `town Litchfield` 8, no place 1.
- **Pending facts:** 5, citing the board's November 10 summary of draft minutes.
- **Raw folders:** each under 100 MB.
- **Quotes:** 613 of 734 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2027-28 budget, $28,073,982 | The board's November 10, 2026 snapshot |
  | The late bus, $32,850 | The same snapshot |
  | Starting pay, $47,848 | The 2026–2028 tentative agreement |
  | Special education, $5,367,067 | The 2025 annual report |
  | The $38.9 million project | Board minutes |
  | The school rate, $9.73 | Board minutes, December 3, 2025 |

## Premises checked

| Question says | What the sources show |
|---|---|
| Free kindergarten (P1.1) | Right as far as sources show: full day, no tuition posted |
| A 2:50 dismissal (P1.2) | Pages say 2:50, the handbook 2:45; pickup 2:45–3:00 |
| A late-September cutoff (P1.3) | Five on or before September 30 |
| Bus drop-offs at a sitter's only on work days (P5.1) | Requests must cover five days a week |
| Balanced literacy (P11.1) | No: UFLI, a systematic phonics program |
| About 60% proficient in math at Griffin (P15.1) | That was 2024-25; 71% in 2025-26 |
| Before-school band (P15.2) | None; band starts in grade 5 |
| A 7:00 middle school start | Close: drop-off 7:15, late bell 7:22 |
| Griffin and Campbell at 8:25 on Route 3A | Campbell starts at 7:35 and is reached from Albuquerque Avenue |
| About 340 students at Campbell | Right |
| No bus to a tech center | Wrong: buses run to Palmer, moving to district vans |
| Phones up to each teacher | Wrong: banned bell to bell at every school |
| A late bus | Runs in 2026-27; left out of the 2027-28 proposal |
| A low online rating for Campbell | Right for GreatSchools; the gap comes from 2021 AP and dual-enrollment figures |
| Air conditioning | Griffin heating only; LMS and Campbell cooled |
| A rising school tax bill (P2.3) | The amount raised rose; the rate held at $9.73 |
| Losing teachers to Hudson and Bedford over pay (P7.3) | Partly: Hudson pays more; Bedford's starting pay was lower; no turnover data |
| A February deliberative session (P7.1) | The board calendar says Saturday, February 6, 2027 |
| 5:30 meetings and online video | Right; no reason given for the time |
| A new school soon (P20.1) | A $38.9 million renovation and addition goes to voters in March 2027 |

## Corrections and additions to earlier files

None needed. Merrimack's Litchfield 2026 rate matches the town's sheet.

## Library notes (for review, not applied)

- `district-preschool` 59 says no Litchfield preschool page was found. This research has the program and eligibility (district-preschool 1–2); current tuition isn't posted.
- The library's coverage table lists Litchfield's kindergarten day and cutoff as not found. Both are now here.
- `money-school-building-aid-2026-27` 7 ranks a $45,412,700 Litchfield new school second for building aid. The board now puts that project at about $48,017,000 and isn't proposing it; the March 2027 proposal is the $38.9 million renovation and addition.

## Browser pass

The agents' blocked pages were:
- Niche (HTTP 403) and U.S. News (connection reset);
- NH DOT traffic counts (the planning commission's were used);
- NH DOE's special education determinations and 2026 enrollment;
- the 2026-27 budget folder (Google sign-in).

None is essential to the answers.
