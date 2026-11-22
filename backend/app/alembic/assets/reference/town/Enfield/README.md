# Enfield: Research for Ask NH Education Facts

Cited facts and figures for answering Enfield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the tenth wave of the second ToLoad batch. Enfield is one of five towns in the Mascoma Valley Regional School District, SAU 62:
- **Enfield Village School** serves preschool to grade 4 (Canaan Elementary serves the other side of the district).
- **Indian River School** serves grades 5–8, and **Mascoma Valley Regional High** grades 9–12, both in Canaan.
- **Career programs:** the Hartford Area Career & Technology Center (HACTC) in White River Junction, Vermont.

The district votes by official ballot. Lebanon and Hanover were researched in `../Lebanon/` and `../Hanover/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `enfield-village-and-families.md` | Bus rides (the first Route 4A stops ride about an hour; all grades share buses while three drivers short), bus stop changes (a year, half year or quarter only), meals ($1.75 breakfast, $3.00 lunch, by application), the inclusive preschool (tuition and a $30 fee), the Grafton line, Alma and folders, home internet grants | 12 | 46 | 1 | 10 MB |
| `indian-river-support-and-choices.md` | 5th grade at Indian River, math (44% in 2026, the state average), NWEA results by grade, MAPs (alternative pathways), policy JJJ (October 2026) for EFA students, the out-of-date homeschool policy, absences (hunting week only with approval), phones, bullying on buses, one Algebra I class in 2023-24, 504 plans | 16 | 125 | 1 | 36 MB |
| `mascoma-high-and-hartford-center.md` | The HACTC bus (about 28 minutes; paid by the district; about $598,000 a year of tuition), AP courses in alternate years (93% scoring 3+ in 2026), exam fees paid, PE credit for sports, ELOs, credit recovery during the year, no late bus, 8th graders on JV only with a waiver | 7 | 70 | 3 | 16 MB |
| `money-and-governance.md` | The $32,974,071 budget (passed 1,305–502) against a higher default, school tax dollars up 33.7% while students fell 16.1% (2015–2025), Enfield's share (the most dollars, not the highest rate), the 2026 rate ($18.89; schools 59.2%), the tax cap (55.42%; not adopted), board seats, the FY28 proposal, spending against Lebanon and Hanover | 6 | 59 | 4 | 38 MB |
| **Total** | | **41** | **300** | **9** | **100 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.95 million tokens.

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Enfield. All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 39 full, 21 partial.
- **Topics:** no new topics. Three federal facts are added to the library's `section-504-plans`.
- **Places:** `district Mascoma Valley Regional` 280, `town Enfield` 15, statewide 5.
- **Pending facts:** 20, citing draft minutes (most 2026-27 minutes are still drafts) and a tabled draft EFA policy.
- **Raw folders:** each under 100 MB (the four together about 100 MB). Bus copies keep only street names and times, without drivers' names; minutes copies have residents' names and addresses removed.
- **Privacy:** the address scans, including the text of every saved PDF, find only schools, the food service office and agencies; no name lists were found.
- **Quotes:** 529 of 621 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The budget, $32,974,071, passed 1,305–502 | The 2026 MS-27 and the transcribed March 10, 2026 results |
  | The default budget, $33,209,497 | The 2026 warrant |
  | The 2026 tax rate, $18.89 | The 2026 annual report |

## Premises checked

| Question says | What the sources show |
|---|---|
| Hour-long rides on the Route 4A side (P1.2) | True for the first stops |
| Free meals for all (P5.2) | Wrong |
| Pre-K only for children with delays (P8.1) | Wrong: inclusive, with tuition |
| PlusPortals (P12.2) | Not used: Alma, email and folders |
| About 40% in math (P3.2) | Right for 2023–2025; 44% in 2026 |
| An annual homeschool portfolio (P10.2) | Out of date since July 1, 2026 |
| A late bus to Enfield (P12.3, P17.3) | None found |
| Hunting week off (P11.3) | Only with advance approval |
| Phones locked up all day (P16.2) | Partly: off and away |
| AP Biology and Chemistry alternate (P7.1) | Correct |
| Homeschool work as transfer credit (P10.3) | No: competencies instead |
| Running Start only online (P15.3) | No: taught at the school |
| Summer credit recovery (P17.1) | No: during the year |
| The budget vote (P4.3) | Already passed, 1,305–502 |
| Taxes up as enrollment falls (P2.3) | Partly: dollars up, the rate down after revaluation |
| Enfield pays the most (P4.2) | Most dollars, not the highest rate |
| The tax cap (P9.2) | Not adopted: 55.42% |
| Locked into the cooperative (P9.3) | No; no withdrawal study found |

## Corrections and additions to earlier files

- **Lebanon and Hanover:** consistent; their HACTC facts list Mascoma among the sending schools.

## Library notes (for review, not applied)

- **`kindergarten-entry-cutoff` 61 (Mascoma):** its note says policy JEB's link returned 404. The policy table now links it, and it downloads (https://drive.google.com/file/d/1UEsuPFETsTkG6DOZMTm9UiZcikAUvrCU/view).
- **`budget-form-and-vote-dates` 83 (Mascoma)** says the 2026 dates weren't found: the deliberative session was January 31, 2026 and the vote March 10, 2026.

## Browser pass

Not needed for the answers. Not retrieved:
- the Town of Enfield's website, NH DRA's cooperative apportionment file and NH DOE's apportionment page (HTTP 403), so the cost-sharing inputs come from the district's documents;
- the FY2025 audit (an encrypted PDF);
- NH DOE's gifted-and-talented reports (HTTP 403).
