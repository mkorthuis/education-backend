# Sandown: Research for Ask NH Education Facts

Cited facts and figures for answering Sandown, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the second ToLoad batch. Sandown is in the Timberlane Regional School District (SAU 106) with Atkinson, Danville and Plaistow:
- The Learning Center at Sandown Central: preschool and kindergarten;
- Sandown North Elementary School: grades 1–5;
- Timberlane Regional Middle School (6–8) and High School (9–12), both in Plaistow. High schoolers may take career programs at Salem (bused) or Pinkerton Academy (no bus).

The district decides its budget by official ballot. Its shared facts are in `../timberlane/`, `../Atkinson/` and `../Plaistow/`; these files cite them by topic and number and add Sandown's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `sandown-elementary-and-families.md` | Why children change buildings after kindergarten (the 2015 consolidation), Sandown North at capacity and the new subcommittee, kindergarten sizes (about 18 per teacher), no care in either building, reading and math help (no single math program since 2014), no gifted program, ESL at Sandown Central only, the May 2026 screen-time survey, D.A.R.E., meals, private preschool rates | 17 | 52 | 1 | 41 MB |
| `support-and-choices.md` | $1,759,577 moved to special education contractors, the state's 2026 IEP review (18 findings), special education staff, paraeducator pay and vacancies, teacher turnover at Sandown North (61% stayed in 2023-24), the late bus to Sandown, moving out mid-year (JFAB), EFAs, co-ops nearby | 9 | 38 | 2 | 39 MB |
| `middle-and-high-school.md` | Bus times from two Sandown stops (6:14 and 6:39 for a 7:20 bell), CTE at Salem and Pinkerton (drivers repaid by the mile), CTE, athletics and activities budgets FY2022–FY2027, engineering cut from seven courses to two, music (0.1% of the budget; 41% in an ensemble), counselors, Next Charter (90% Derry seats), young adults leaving, the 2026 wrestling title, no booster fee | 13 | 38 | 8 | 18 MB |
| `money-and-governance.md` | The 2026 rate ($20.89; school $15.50, up $3.07), the district-wide votes for 2023–2026 (the 25% cap failed 1,939 to 3,220), Sandown against the result on 20 of 53 articles, the $25 million lease (55.5%; RSA 33:7-e allows a simple majority), building costs by property value (Sandown 22% of value, 29% of students), the 2016 withdrawal vote, the elderly exemption | 8 | 57 | 4 | 11 MB |
| **Total** | | **47** | **185** | **15** | **109 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.05 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Sandown`). All 15 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 33 full, 26 partial, 1 from the site's data.
- **Topics:** one new topic, added to `../shared-topics.md`: `lease-purchase-financing-rules` (RSA 33:7-e's simple-majority votes for lease-purchase agreements, and how they differ from bonds).
- **Places:** `district Timberlane Regional` 141, `town Sandown` 42, no place 2.
- **Pending facts:** 7, citing draft committee and board minutes.
- **Raw folders:** each under 100 MB. Three district pages that now return 404 were read from Internet Archive copies; their facts say so.
- **Quotes:** 351 of 467 quoted passages found word for word in Sandown's raw copies; many of the rest are in the shared Timberlane raw folder.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $20.89 (school $15.50; 2025 $17.80) | The town's 2026 tax rate history |
  | The 25% cap, 1,939 to 3,220 (Sandown 572 to 648) | The district's 2026 results by town (transcription checked against the signed image) |
  | The 2025 study committee article, 3,597 to 2,131 | The district's 2025 results by town |

## Premises checked

| Question says | What the sources show |
|---|---|
| A "Timberlane Learning Center" preschool (P1.1) | The 2016 name; it is now The Learning Center at Sandown Central |
| Sandown Central just for kindergarten (P1.2) | Preschool and kindergarten |
| Care in the buildings (P1.3) | None in either building |
| Reading specialists cut (P5.1) | Not borne out |
| Automatic free meals (P5.3) | Only for children approved through state records |
| Large kindergarten classes (P11.1) | About 18 per teacher; the cap is 20 |
| Heavy screen time for young children (P11.2) | Staff report minimal screen use |
| ESL at both schools (P17.2) | Sandown Central only |
| Sandown Central "packed" (P19.1) | No: Sandown North is the full building |
| A CTE bus (P2.2) | Salem yes; Pinkerton students drive and are repaid |
| Shop budgets "gutted" (P2.3) | Mixed: an engineering teacher cut, but CTE tuition spending doubled |
| A long bus ride (P4.2) | Borne out: pickups from 6:14 |
| Counselors stretched thin (P13.3) | About 186 students each at TRHS, under the state's 300 |
| Booster fees (P18.2) | None found |
| A 2.5% tax cap (P3.2) | Never took effect; the 25% version failed |
| Outvoted on half the articles (P6.1) | 20 of 53 since 2023 |
| Subsidizing Plaistow's buildings (P6.2) | Not supported: building costs are split by property value |
| A $2 million Budget Committee cut (P12.1) | None found |
| A $25 million lease "without a bond vote" (P12.2) | It was voted, by simple majority (55.5%) |
| Meetings always shouting matches (P8.3) | Not supported |
| Moving to Danville or Kingston means switching right away (P17.1) | No: JFAB lets a student finish the year |
| A late bus to Sandown (P10.3) | Tuesday–Thursday, about 3:45–4:00 |

## Corrections and additions to earlier files

- **Timberlane** (`../timberlane/`): the 2026 district-wide results fill its "Not retrieved" gap. Sandown's files also add:
  - the 2026 wrestling title (31 since 1987);
  - SNHU's dual enrollment fee ($100 a course);
  - Atlantic Orthopedics taking over athletic training in January 2027;
  - 17 special education and 2 regular education paraeducator positions cut in FY2026;
  - the IEP review's 18 findings out of 792 possible.
- **Plaistow** (`../Plaistow/families-choices-and-town.md`): it found no co-op within about 15 miles except one in Windham. The marketplace feed tags two (in Hampstead and Kingston).

- **Teacher retention (corrected after Alton's research):** the statewide comparison was 91% of elementary teachers (89.3% overall), sums that included 31 schools reporting more retained than current teachers. It is now 83.8% at the 440 schools with usable counts.

## Library notes (for review, not applied)

- **`district-practices.md`, Timberlane's kindergarten item** says the March 2026 Article 14 result wasn't posted. It failed, 2,530 to 2,790.

## Browser pass

- **Sandown's Tax Assistance page** didn't load: the browser extension has no permission to read sandown.us. The facts use the town's Assessing pages instead.
- **Not retrieved** (none essential): NH DOE's gifted report and turnover data, and NH DRA's 2026 files (HTTP 403).
