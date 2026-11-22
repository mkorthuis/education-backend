# Danville: Research for Ask NH Education Facts

Cited facts and figures for answering Danville, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the second ToLoad batch. Danville is in the Timberlane Regional School District (SAU 106) with Atkinson, Plaistow and Sandown:
- Danville Elementary School: preschool to grade 5, in Danville;
- Timberlane Regional Middle School (6–8) and High School (9–12), both in Plaistow. High schoolers may take career programs at Salem (bused) or Pinkerton Academy (no bus).

The district decides its budget by official ballot. Its shared facts are in `../timberlane/`, `../Atkinson/` and `../Plaistow/`; these files cite them by topic and number and add Danville's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `danville-elementary-and-families.md` | Half-day preschool and kindergarten options (full-day kindergarten $4,500), the YMCA's care in the school (7:00–8:30 and 3:00–6:00), class averages of 18.5–22.5, bus stops 20–46 minutes before the bell, First Student's record and contract, reading help, no gifted program, building security | 13 | 41 | 3 | 49 MB |
| `middle-and-high-school.md` | Danville students moving up to TRMS, the buses to Plaistow and the late route, distances to the Salem and Pinkerton centers, no grade 7–8 Algebra I in the 2023-24 federal data, TRMS math staffing, when TRHS courses open, phones locked in lockers, test results against Hampstead and Windham | 7 | 23 | 3 | 9 MB |
| `money-and-governance.md` | The 2026 rate ($18.50 after a 54.79% revaluation; the school tax Danville raises up 28.4% to $11,961,362; the December bill carries the rise), Danville's votes against the district result, the 2026 district-wide budget result (4,095 to 1,323), the Budget Committee's cuts, central office costs (5.1%), Danville's 95.8% residential tax base, the 1963 building's roof and HVAC | 8 | 53 | 6 | 18 MB |
| `support-arts-and-choices.md` | $1,759,577 moved from vacant special education positions to contractors, Danville's special education and counseling staff, the PAC (no separate budget), music lessons, wrestling and other teams, no pay-to-play or Chromebook fee, counselors per grade at TRMS | 9 | 26 | 3 | 22 MB |
| **Total** | | **37** | **143** | **15** | **98 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.95 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Danville`). All 15 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial.
- **Topics:** no new topics.
- **Places:** `district Timberlane Regional` 105, `town Danville` 37, `sau 106` 1.
- **Pending facts:** 7, citing draft fall 2026 minutes.
- **Raw folders:** each under 100 MB. Bus stops are kept by street only.
- **Quotes:** 258 of 389 quoted passages found word for word in Danville's raw copies. Most misses are quotes from the shared `../timberlane/`, `../Plaistow/` and `../Sandown/` raw folders, which the facts cite (five sampled misses were all found there), or excerpts joined with "...".
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $18.50, and the 54.79% revaluation | The September 28, 2026 selectmen's minutes and the town's rate transcription |
  | The school tax, $11,961,362 | Timberlane's October 2026 financial data |
  | The 2026 budget vote, 4,095 to 1,323 | The district's signed 2026 results sheet (image) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day pre-K at Danville, or a drive to TLC in Sandown (P1.1) | Partly wrong: half-day preschool at Danville; full-day kindergarten costs $4,500 |
| Care at the school (P1.2) | Yes: the YMCA, 7:00–8:30 and 3:00–6:00 |
| Teachers stretched thin (P2.1) | Class averages 18.5–22.5, within policy caps |
| Early pickups for a school ten minutes away (P2.2) | Borne out: stops 20–46 minutes before the bell |
| Bus driver shortages (P14.1) | Each fall from 2023 to 2025; none reported in 2026-27 |
| A gifted program (P16.1) | None found |
| Danville Elementary "under 300" (P4.1) | Right: 283 in 2024-25 |
| A bus to Pinkerton or Salem (P6.2) | Salem yes, Pinkerton no |
| Welding or electrical at Pinkerton or Salem (P6.1) | Only at Pinkerton |
| Algebra in 7th or 8th grade (P16.2) | Possible in grade 8 by the district's account; not in the 2023-24 federal data |
| Phones locked away in class (P19.1) | Locked in lockers all day |
| Taxes jump every March (P9.3) | No: the rate is set in the fall, and the December bill carries the rise |
| Millions in surplus (P10.1) | Out of date: large surpluses ended in FY2026 |
| Danville outvoted (P10.3) | Sometimes: Danville matched the result on 14 of 17 operating budgets since 2010 |
| The Budget Committee cutting millions (P11.1) | Partly: the $6.6 million FY2026 cut was made by voters at the deliberative session |
| Hard to hire special education staff (P3.1) | Right: $1.76 million moved to contracted services |
| A Chromebook fee (P8.2) | None |

## Corrections and additions to earlier files

- **Timberlane** (`../timberlane/`):
  - **Year labels:** the site's school enrollment figures were labeled 2025-26 but are the October 1, 2024 count. They are corrected to 2024-25 in the Timberlane, Atkinson and Plaistow files (`../timberlane/README.md`).
  - **Algebra I:** the middle school file's premise ("Algebra I by 8th grade: yes, for selected students") now notes the 2023-24 federal data.
  - **Additions:**
    - the 2026 district-wide budget result, and Danville's 2026 tallies;
    - the late route's streets;
    - TRMS's Math Enrichment teacher, now listed;
    - 27 of 29 contracted buses in use.
  - **Counselors' extension:** 4920 on the Counseling page, 4900 in the 2026-27 handbook. Not reconciled.
- **Plaistow** (`../Plaistow/families-choices-and-town.md`): it found no middle or high school special education coordinator. The November 19, 2026 administrative map shows one at each.

## Browser pass

- **Danville's 2025 town report** is listed on UNH's repository in Chrome, but it's a PDF that would have to be downloaded. All 60 questions are covered without it, so it wasn't read.
- **Not retrieved** (none essential):
  - NH DOE's gifted and special education pages (HTTP 403);
  - Governor and Council grant items;
  - the athletics site, which loads by script.
