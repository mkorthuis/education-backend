# Atkinson: Research for Ask NH Education Facts

Cited facts and figures for answering Atkinson, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the two files below and the shared Timberlane folder (`../timberlane/`), in the reference library's format.

Gathered November 21, 2026, in the first wave of the ToLoad towns, with Plaistow. Atkinson's students attend the Timberlane Regional School District (SAU 106): Atkinson Academy (preschool to grade 5), then Timberlane Regional Middle and High in Plaistow.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `atkinson-academy-and-families.md` | Scores against Golden Brook, Hampstead and Windham Center (a derived table), no portables found, the 1803 building's renovation (FY2030), the preschool ($2,200, aid on request), kindergarten (half day free, full day $4,500), care, reading help and the interventionist, library aides cut June 2026, the paused unified arts rotation, PickUp Patrol and bus passes, the autism program, enrollment (342, down from 382) | 14 | 79 | 2 | 43 MB |
| `support-and-town.md` | Meals and fees, fields (the district's crew for school fields; the town's parks), EFA and home education (policies IHBG and JJJ out of date), state and town tax relief, the elderly exemption ($150,000–$300,000), the veterans' credit (raised to $2,750), the 2026 tax rate ($10.58 after revaluation, about 74.5% schools), the Kimball Library bus, guardianship enrollment, welcome | 10 | 60 | 0 | 37 MB |
| Shared `../timberlane/` (3 files) | Timberlane High, Timberlane Middle and student life, money and governance | 30 | 243 | 7 | 80 MB |
| **Total** | | **54** | **382** | **9** | **160 MB** |

`brief.md` is the brief the research agents worked from. Atkinson's own two agents used about 0.96 million tokens. The three shared Timberlane agents, which also answered Plaistow's questions, used about 1.63 million.

## Checks

- **Parser:** both files and the shared folder pass the backend's parser (`tools/check_town.sh Atkinson`, `tools/check_town.sh timberlane`).
- **Coverage:** all 60 questions have facts: 29 full, 30 partial, 1 from the site's data. This counts shared rows only where they name Atkinson.
- **Topics:** no new topics.
- **Places:** `district Timberlane Regional` 108, `town Atkinson` 30, no place 1, plus the shared folder.
- **Places for the backend:** none needed. Timberlane runs every grade.
- **Raw folders:** all under 100 MB.
- **Quotes:** 230 of 264 quoted passages found word for word in Atkinson's raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Atkinson's FY2026 share, $16,017,725 (22.78%) with 706 of 3,175 students | Timberlane's FY2027 supplemental budget package, page 57 |
  | The lease purchase agreement, $25,243,000 | The February 2025 deliberative session minutes |
  | 49.5 vacant positions | Budget Committee minutes, October 22, 2026 |
  | TRHS mean SAT 951 for the class of 2027 | The TRHS school profile |
  | The high school bathrooms, $625,033 | The facilities committee's November 10, 2026 estimate |
  | Full-day kindergarten tuition, $4,500 | The February 2025 deliberative session minutes |
  | Atkinson's 2026 tax rate, $10.58 | The town's 2026 tax bill notice |

## Premises checked

| Question says | What the sources show |
|---|---|
| Portables and an expansion warrant (P1.3) | No portables found; the only project is the 1803 building, for FY2030 |
| Atkinson's disproportionate share (P2.1) | No: costs follow resident students (22.78% of costs, 22.24% of students); Atkinson has the lowest school rate on equalized value |
| Enrollment around 3,200 (P2.2) | Right: 3,175–3,212 |
| Budget cap votes (P2.3) | Question 2 was adopted for Timberlane (72%) |
| The preschool lottery and peer tuition (P3.1) | Not published; everyone pays $2,200, with aid on request |
| Full-day kindergarten guaranteed (P3.2) | No: half day is free, full day $4,500 |
| A $25 million facilities contract (P4.2) | Right: up to $25,243,000, about $1.0 million a year to 2044 |
| Orton-Gillingham staff (P5.1) | No district document mentions it |
| The PAC over two decades old (P6.1) | Right: completed November 2002; roof and air handlers in progress |
| Pay-to-play fees (P9.3) | None found; buses are in the general budget |
| Annual homeschool evaluations (P10.2) | Repealed July 1, 2026; Timberlane's policy still describes them |
| Library and reading staff restored (P11.3) | Partly: an interventionist added in 2024; library aides cut in 2026 |
| AP and dual enrollment through VLACS (P13.1) | 19 AP courses in person, 6 SNHU courses at TRHS |
| 52% math, 60% reading at Atkinson Academy (P17.2) | Those were 2025; 2026 was 61% and 62% |
| SAU 55 (P10.2, P18.1, P19.3) | Timberlane has been SAU 106 since July 1, 2021 |
| A social worker at TRHS (P18.3) | None, by the student services director's account |

## Corrections and additions to earlier files

None needed.

## Library notes (for review, not applied)

None.

## Browser pass

The agents' blocked pages were NH DOE's assessment pages and NH DRA's tax files. Both are PDFs or reports Chrome can't read, so they remain gaps. The site's own data and the town's tax notice cover the figures used.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 2 saved bus and transportation copies (2 in all; schools, child care centers, businesses and other public places keep theirs).
- The state's resident birth, marriage and death lists removed from 1 saved town report copy (headings and record counts kept); 1 report PDF deleted.
