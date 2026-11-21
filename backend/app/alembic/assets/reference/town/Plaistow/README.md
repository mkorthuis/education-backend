# Plaistow: Research for Ask NH Education Facts

Cited facts and figures for answering Plaistow, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the two files below and the shared Timberlane folder (`../timberlane/`), in the reference library's format.

Gathered November 21, 2026, in the first wave of the ToLoad towns, with Atkinson. Plaistow's students attend the Timberlane Regional School District (SAU 106): Pollard Elementary (preschool to grade 5), then Timberlane Regional Middle and High, both in Plaistow.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `pollard-and-families.md` | Pre-K (half day, $2,200, free with free lunch), Child Find and speech timing, kindergarten (cap of 20; a full-day room added), care inside Pollard (YMCA) and no daycare bus stops, early releases and delays, the 2025 driver shortage (fixed), the PTA, enrichment in class (no pull-outs), English learners, translation (none beyond Google Translate), students by race | 14 | 66 | 2 | 11 MB |
| `families-choices-and-town.md` | Comparison with Haverhill, registration at the school (two proofs of residency), mid-year placement (policy JG), meals (one application any time of year), IEP contacts, EFAs (31 Plaistow students) and Massachusetts private schools, Child Find for homeschoolers, grandparent guardianship, PickUp Patrol, counselors, private school busing, home values | 11 | 50 | 3 | 10 MB |
| Shared `../timberlane/` (3 files) | Timberlane High, Timberlane Middle and student life, money and governance | 30 | 243 | 7 | 80 MB |
| **Total** | | **55** | **359** | **12** | **101 MB** |

`brief.md` is the brief the research agents worked from. Plaistow's own two agents used about 0.92 million tokens; the three shared Timberlane agents are counted in `../Atkinson/README.md`.

## Checks

- **Parser:** both files and the shared folder pass the backend's parser (`tools/check_town.sh Plaistow`).
- **Coverage:** 59 of 60 questions have facts: 32 full, 26 partial, 1 from the site's data. P11.3 (help with middle school supply lists) has none. This counts shared rows only where they name Plaistow.
- **Topics:** no new topics.
- **Places:** `district Timberlane Regional` 97, `town Plaistow` 18, no place 1, plus the shared folder.
- **Raw folders:** all under 100 MB.
- **Quotes:** 202 of 244 quoted passages found word for word in Plaistow's raw copies.
- **Spot checks:** the shared figures are checked in `../Atkinson/README.md`. Plaistow's own share, 30.66% of costs with 30.65% of students, comes from the same budget package page.

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day pre-K at Pollard (P1.1) | No: half day, $2,200 a year, free for families who qualify for free lunch |
| Kindergarten with 24 children (P1.3) | Policy caps it at 20 |
| Daycare bus stops from Pollard (P2.1) | No district rule allows them; the YMCA's care is inside Pollard |
| Bus routes changing for driver shortages (P2.3) | True in fall 2025, fixed by November 2025 |
| A PTO (P9.3) | It's a PTA, and active |
| Gifted pull-outs (P15.1) | None; enrichment in regular classes |
| Spanish notices (P17.2) | No translation practice found beyond Google Translate |
| Residency paperwork at the SAU office (P9.2) | At the child's school |
| EFA money from the town (P12.2) | EFAs are state accounts; Massachusetts private schools are listed |
| Private school busing from the town (P18.3) | First Student runs the district's buses; how RSA 189:9 is applied isn't stated |
| About 50 open positions (P3.1, P16.1) | Right: 49.5 vacant positions, paying for contracted staff |
| The local school rate from $8.38 to $10.54 (P10.1) | $8.38 is right for 2025; the 2026 rate isn't posted |
| A 2.5% tax cap (P10.3) | The petition was amended to 25%; Question 2's cap applies |
| A 5% fund balance (P16.2) | Repealed by petition in 2025 |
| A 94% graduation rate (P7.3) | 92.5% in 2025 |
| An SAT average near 1180 (P18.2) | Mean 951 for the class of 2027 |
| Plaistow subsidizing the others (P20.2) | No: 30.66% of costs with 30.65% of students |
| A withdrawal study (P20.3) | Only Sandown's, in 2015 |
| About 40% of middle schoolers proficient in math (P8.1) | Right: 42% in 2026 |
| Middle schoolers in high school productions (P4.3) | Not without the superintendent's exception |

## Corrections and additions to earlier files

None needed.

## Browser pass

The agents' blocked pages were:
- NH DOE's timely-evaluation results and enrollment reports;
- NH DRA's tax files;
- Niche.

The NH DOE and NH DRA pages are PDFs or report tools Chrome can't read. The Niche grades aren't needed for these questions.
