# Rindge: Research for Ask NH Education Facts

Cited facts and figures for answering Rindge, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the second ToLoad batch. Rindge's students attend the Jaffrey-Rindge Cooperative School District (SAU 47), shared with Jaffrey:
- Rindge Memorial School: preschool to grade 5;
- Conant Middle High School, in Jaffrey: grades 6–12. Students take career programs at the Region 14 center at ConVal in Peterborough.

The district votes by official ballot. It was researched first in `../Jaffrey/`; these files cite Jaffrey's facts and add Rindge's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `rindge-memorial-and-families.md` | The free pre-K lottery (full-day halved), RMS buses (7:44–8:28 after the Conant runs), classes of about 16, the town's Extended Day Program and Rec bus stop, the meal policy, scores (43% in 2025-26), guardianship papers, Franklin Pierce student teachers, one licensed child care program in town, enrollment by grade for 2025-26 | 14 | 49 | 3 | 32 MB |
| `support-and-choices.md` | The vacant K–2 special education teacher, one contracted psychologist and a diagnostician (3.0 positions in FY2022, 2.0 since), para pay ($17.00, then $17.25) and fast-food medians, 6 of 22 para lines vacant at RMS, 19 out-of-district placements ($90,000–$500,000), Fly-Up Day and WEB Crew, Hampshire Country School ($88,900; boarding only), Massachusetts schools (closed to NH residents) | 10 | 54 | 5 | 66 MB |
| `conant-from-rindge.md` | Conant buses from 6:23, the 2025 award against 19% grade 11 math, no Franklin Pierce arrangement, library and elective trims, no CTE of its own since 2025, math credits against proficiency, AP pass rates over 60%, graduation over 95%, the founding agreement's busing promise (a two-thirds vote to change), no late bus published, sports eligibility, young adults leaving | 12 | 39 | 2 | 27 MB |
| `money-and-governance.md` | Rindge's share (57.2% of the local tax with 48% of the pupils, 55.6–59.5% since 2018-19), special education on local taxes (84.0%), the default budget, Little Orioles kept and made tuition-funded, enrollment down 13.7%, the 2018 formula vote (47.82%; two-thirds needed), the 2019 dissolution study and the failed 2025 petition (803 to 854), the 2026-27 estimate ($13,433,509), charter school costs, public comment | 8 | 43 | 3 | 61 MB |
| **Total** | | **44** | **185** | **13** | **186 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.91 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Rindge`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 37 full, 22 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Jaffrey-Rindge Cooperative` 150, `town Rindge` 31, no place 4.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB.
- **Privacy:** home-stop house numbers were removed from the bus tables, notes and raw bus files by the main session, and the route PDFs were deleted.
- **Quotes:** 396 of 492 quoted passages found word for word in the raw copies.
- **Search:** three agents ran out of web searches partway through ("SEARCH BLOCKED"). They finished from pages reached directly.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026-27 estimate, $13,433,509 | The district's FY27 revenue and assessment estimate |
  | The 2018 formula vote, 47.82% | The district's staff position analysis |
  | Hampshire Country School, $88,900 | The school's FAQ |
  | Conant buses from 6:23 | The 2026-27 Rindge bus sheet (OCR) |

## Premises checked

| Question says | What the sources show |
|---|---|
| The pre-K lottery wiped out (P1.1) | Partly: still free and by lottery, but full-day was halved |
| Classes near 17 (P1.3) | Close: 16 |
| Scores near 41% and 42% (P10.1) | Right for 2024-25; 43% in 2025-26 |
| An unfilled K–2 special education job (P2.1) | Right |
| Only one psychologist (P2.1, P15.2) | Partly: one contracted psychologist and a diagnostician |
| Paras at $17 (P2.2) | Right for 2025-26 |
| Fast food pays more (P2.2) | Not by the area medians |
| Yearly homeschool paperwork (P7.3) | Repealed July 1, 2026 |
| Massachusetts schools (P18.2) | Closed to NH residents under Massachusetts school choice |
| Very early buses (P4.1) | Right: from 6:23 |
| Franklin Pierce courses (P5.2) | No set program |
| Busing to Peterborough or Keene for shop (P6.1) | Right |
| No late bus (P19.2) | Right as far as published |
| Rindge carries a big chunk (P3.1) | Right: 57.2% with 48% of pupils, steady since 2018-19 |
| 83% of special education on local taxes (P3.2) | About right: 84.0% in 2024-25 |
| Little Orioles on the chopping block (P8.2) | Discussed, kept, made tuition-funded |
| Paying twice for charter students (P12.2) | Not as tuition; state aid and special education costs differ |

## Corrections and additions to earlier files

- **Jaffrey** (`../Jaffrey/`):
  - **AP pass rates:** Jaffrey's file says they weren't published. The February 2026 annual report gives "over 60%" two years running.
  - **Formula history:** Jaffrey's file has none. This file adds the 2018 vote to split costs 100% by pupils (47.82%; two-thirds needed).
  - **Meals:** the JGS handbook says a child over the charging limit can't take part in meals, but policy EFAA (2024) serves a child who asks.
  - **Rindge buses:** there are six (40–45), not "five".

## Library notes (for review, not applied)

- **`district-preschool` 51** counts 33 RMS preschoolers. The district counted 64 in 2025-26, before full-day pre-K was halved.

## Browser pass

Not needed for the answers. Not retrieved:
- NH DOE's enrollment reports (a bot check);
- the town's program registration (needs a sign-in);
- Winchendon's tuition rules (a bot check);
- mass.gov (HTTP 403).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- The state's resident birth, marriage and death lists removed from 3 saved town report copies (headings and record counts kept); 3 report PDFs deleted.
