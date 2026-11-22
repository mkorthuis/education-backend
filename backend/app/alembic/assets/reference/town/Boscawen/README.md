# Boscawen: Research for Ask NH Education Facts

Cited facts and figures for answering Boscawen, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the second ToLoad batch. Boscawen's students attend the Merrimack Valley School District (SAU 46), shared with Loudon, Penacook (Concord), Salisbury and Webster:
- Boscawen Elementary School (BES): preschool to grade 5;
- Merrimack Valley Middle School (6–8) and High School (9–12), both in Penacook. High schoolers may take career programs at the Concord Regional Technical Center (CRTC).

The district decides its budget at an annual meeting. It was researched first in `../Loudon/`; these files cite Loudon's facts and add Boscawen's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `boscawen-elementary-and-families.md` | The YMCA's care at BES (7:00–8:45, 3:00–6:00), full-day kindergarten, the district preschool at BES (16 children), first grade (27 children, two teachers), the 2022 water letter (outlets replaced; all 2024 samples under 5 ppb), the schoolwide Title I program, BES's four bus routes (20–57 minutes), summer reading restored ($15,000), infant care in town | 14 | 49 | 6 | 8 MB |
| `support-and-choices.md` | Middle school buses (45–69 riders per route; 15–24 minutes early), two-trip buses, out-of-district transport, the June 2026 EFA charges ($2,779 per class) against the handbook's "no fees", homeschoolers at CRTC (free), district buses within the district only, phones and vaping, start times (pickups 6:49–7:20 for a 7:45 start), the contracting bid proposal | 14 | 38 | 2 | 40 MB |
| `merrimack-valley-from-boscawen.md` | MVHS against Concord High (math 19% each; science 27% against 42%; graduation 91.3% against 73.1%), test participation, the CRTC bus and senior seats, NEC courses for seniors, evening trades training nearby, the Learning Center, civics, four Boscawen-only scholarships, FAFSA policy, graduation June 12, 2027, no late bus | 10 | 39 | 2 | 5 MB |
| `money-and-governance.md` | Boscawen's share of pupils (19.1% to 22.2% since 2014-15), the 2026 rate ($21.80; school $13.42), the $2.3 million surplus (with $500,000 kept), consolidation talk (no school named), the tax caps, technology spending ($1.26 million), BES's building (1996; $1.3 million of planned work), the SAU budget ($1,748,615), the elderly exemption | 8 | 37 | 6 | 37 MB |
| **Total** | | **46** | **163** | **16** | **90 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.87 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Boscawen`). All 16 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 36 full, 23 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Merrimack Valley` 123, `town Boscawen` 30, `district Concord` 5, `sau 46` 2, no place 3.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB. Bus sheets with student and driver names stayed out of the raw copies. The address scan finds no home stops.
- **Quotes:** 373 of 471 quoted passages found word for word in the raw copies.
- **Search:** the elementary agent ran out of web searches partway through ("SEARCH BLOCKED"). It finished from pages reached directly.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 rate, $21.80 | The town's tax rate history |
  | The SAU budget, $1,748,615 | The SAU board's December 3, 2025 packet |

## Premises checked

| Question says | What the sources show |
|---|---|
| Care in the building (P1.1) | Right: the YMCA, 7:00–8:45 and 3:00–6:00 |
| Full-day kindergarten (P1.2) | Right |
| A pre-K spot (P1.3) | The district preschool is at BES, mainly special education |
| The water letter (P8.2) | From 2022; outlets replaced and retested |
| 25 children with one teacher (P19.2) | Not supported: 9.5 to 17.5 per teacher |
| Packed, late middle school buses (P2.2) | Neither confirmed nor ruled out |
| A town bus to Bishop Brady (P14.1) | District buses run within the district only |
| A 7:00 start (P20.2) | Pickups 6:49–7:20; classes start at 7:45 |
| AP cancellations (P5.2) | Possible; none documented |
| NEC courses (P5.3) | Seniors only, at NEC's campus |
| Night welding or electrical training (P7.3) | None through the district |
| Consolidation talk (P2.1) | Real, but no school named |
| A $2.3 million surplus (P3.2) | Right; $500,000 kept |
| Five towns (P9.3) | Penacook is a village of Concord |
| A senior break on the school portion (P12.1) | The exemption lowers the whole bill |
| A new-school bond (P16.2) | None planned |
| Fewer students than Loudon (P18.3) | Right: 464 against 593 |

## Corrections and additions to earlier files

- **Loudon** (`../Loudon/support-and-choices.md`): its EFA fact said no later minutes mention EFA fees. On June 1, 2026 the board accepted 2026-27 EFA rates. The fact now says so and cites this research.
- **Loudon's other files:**
  - BES now links a 2026-27 handbook;
  - the food service page's milk price ($0.65) differs from BES's handbook ($0.60);
  - BES's dyslexia screening notice repeats Loudon Elementary's text, school name included.
- **Bow** (`../Bow/`): it lists 13 Bishop Brady AP courses from the Program of Studies. Brady's 2026-27 profile lists 11 offered.

## Library notes (for review, not applied)

- **`granite-edvance` 1** gives 603-225-6612. Granite Edvance's "Get Our Help" page gives 603-227-5444 for FAFSA and college questions.

## Browser pass

Not needed for the answers. Not retrieved:
- the Town of Boscawen's 2025 report on UNH's repository (a download);
- the town's income relief page (HTTP 403);
- the NHDES results page (HTTP 403; the state's GIS data was used instead);
- the MVHS course catalog (district sign-in).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- The state's resident birth, marriage and death lists removed from 1 saved town report copy (headings and record counts kept); 1 report PDF deleted.
