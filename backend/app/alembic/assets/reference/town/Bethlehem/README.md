# Bethlehem: Research for Ask NH Education Facts

Cited facts and figures for answering Bethlehem, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the five files below, in the reference library's format. These files are the first research on Profile School and SAU 35.

Gathered November 22, 2026, in the third ToLoad batch. Bethlehem is in SAU 35:
- **Bethlehem Elementary School** (preschool to grade 6), run by the Bethlehem School District;
- **Profile School** (junior high and senior high, grades 7–12, in Bethlehem), run by the Profile School District for Bethlehem, Easton, Franconia and Sugar Hill (Landaff and Littleton pay tuition for a few students);
- Lafayette Regional (Franconia and Sugar Hill) is the SAU's other elementary district; Lisbon Regional left SAU 35 for SAU 110 on July 1, 2026, so there are four boards now, not five;
- career programs at the Gallen center in Littleton and the Paradice center in Whitefield (Profile's vocational bus).

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `bethlehem-elementary-and-families.md` | The town Recreation after-school program (2:30–5:00, only on full school days, 30 places, 4 left on Nov 22), the Boys & Girls Club in Lisbon to 6:00, a "morning" pre-school (BES's page says its 2025-26 class was full), storm calls the evening before or by 5:30 a.m., the 7:20–7:50 drop-off window, earliest bus pickups (6:34 and 6:47, 2025-26), the paper-only meals packet, outdoor recess unless the wind chill is under 5°F | 14 | 77 | 2 | 0.4 MB |
| `bethlehem-elementary-learning-and-choices.md` | BES math proficiency up from 56% to 74% (2021-22 to 2025-26), Lafayette's gap shrinking from 29 points to 6, classrooms that "may contain students of two grades" and the June 2026 Exploratory Committee on growth, homework caps for K–3, homeschool rules after July 1, 2026, a proposed topic on internet safety rules | 15 | 76 | 1 | 47 MB |
| `profile-high-and-career.md` | About 193 students in September 2026 (about 130 in grades 9–12), 11 AP courses with math to AP Calculus AB and AP Statistics, VLACS only for courses Profile doesn't offer, the vocational bus (7:25 a.m.) to Gallen and Paradice, no Littleton co-op (only a possible golf team with Lisbon), 63% of 2021–2025 graduates to a four-year college (derived) | 11 | 75 | 3 | 4.4 MB |
| `profile-student-life-and-support.md` | Phones banned bell to bell, policy JJJ (October 15, 2026 revision) letting homeschoolers try out for soccer and join Concert Band, coaches driving athletes by written permission and no late bus, one counselor and a licensed clinical social worker, staff counts by school | 12 | 57 | 7 | 0.9 MB |
| `money-and-governance.md` | Four boards since July 1, 2026, Profile's four-town split (Bethlehem paid $2,557,123 of $4,944,616, 51.7%, against 59.6% of students and 36.7% of value, derived), Bethlehem's local education tax of $5,066,215 split about half and half between Profile and BES, taxes up about 18% while resident students fell about 20% (2014–2025, derived), the energy leases starting in FY28, The White Mountain School's closing (June 30, 2024) | 12 | 83 | 4 | 0.6 MB |
| **Total** | | **64** | **368** | **17** | **53 MB** |

`brief.md` is the brief the research agents worked from. Five agents used about 2.9 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all five files pass the backend's loader, run against the loaded towns plus Bethlehem. All 17 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 19 full, 41 partial.
- **Topics:** two new topics, added to `../shared-topics.md`: `school-internet-safety-rules` and `vlacs-online-courses`.
- **Places:** `district Profile` 152, `district Bethlehem` 139, `sau 35` 37, `town Bethlehem` 32, no place 5, `district Lafayette Regional` 2, `district Littleton` 1.
- **Pending facts:** 3, citing draft minutes.
- **Raw folders:** each under 100 MB. The 43 saved PDFs are policies, handbooks and seven SAU 35 superintendent's reports (checked for name lists and student recognitions: none). The bus route sheets are kept as street-name-only files.
- **Privacy:** the address scan finds only schools, the Recreation Department and the SAU office. The "college matriculation" list in Profile's school profile names colleges, not students. Staff and board member names are replaced with roles in the saved minutes.
- **Quotes:** 558 of 653 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Bethlehem's local education tax of $5,066,215, with $2,557,123 for Profile | The site's `town_school_tax` and `town_school_tax_coop_share` tables (tax year 2025) |
  | Profile's 2024-25 enrollment of 216 (83 in grades 7–8 and 133 in grades 9–12) | The site's `school_enrollment` data |
  | Lisbon's transition to SAU 110 | The June 2026 SAU 35 superintendent's report |
  | The Jason Somerville Trust for Bethlehem students | The saved Profile local scholarships page |

## Premises checked

| Question says | What the sources show |
|---|---|
| After-school care until 5:30 at BES | No: the town program ends at 5:00, runs only on full school days and holds 30 children; the Boys & Girls Club in Lisbon runs to 6:00 with buses |
| A full-day Pre-K at BES | Not found; an SAU 35 document calls it the "morning pre-school" |
| A nurse every day at BES | Not confirmed; the handbook plans for a "designated nurse substitute" |
| Profile has around 200 students in grades 7–12 | About right: 193 in September 2026, 216 in 2024-25 (about 130 in grades 9–12) |
| Counseling five days a week at Profile | No source says so; the handbook says counseling is as-needed; one counselor, one LICSW and a shared school psychologist |
| Late buses at Profile | None posted; every 2025-26 route ends by 3:20 p.m. |
| A co-op with Littleton for sports | Not found; no 2026-27 NHIAA team combines Profile with another school |
| Four separate school boards under SAU 35 | Correct since July 1, 2026 (five before Lisbon left) |
| Bethlehem's share of Profile against Franconia, Sugar Hill and Easton | Bethlehem paid 51.7% of the towns' $4,944,616 in 2025 against 59.6% of their students and 36.7% of their equalized value (derived) |
| The SAU 35 office as a line on the tax bill | Not a separate line; the dollar share by district wasn't found |
| The White Mountain School's closing and its effect | It closed June 30, 2024; no source ties it, or short-term rentals, to public school enrollment |
| Phone policy at Profile | Confirmed: banned bell to bell |
| An annual SAU 35 filing for homeschoolers | Wrong since July 1, 2026: nothing is required each year; EFA families send records to the EFA program |
| Combined grades at BES if enrollment drops | Partly right: some classrooms combine two grades; the 2026 worry was growth |

## Corrections and additions to earlier files

None. Littleton's, Berlin's and Plymouth's facts are cited where they apply; nothing found contradicts them.

## Library notes (for review, not applied)

- **Profile's articles of agreement** and the Special Education Policy and Procedures Manual aren't posted online; a request to SAU 35 would fill several gaps.

## Browser pass

Not done. Not retrieved:
- the Town of Bethlehem's website (annual report, planning board, zoning; HTTP 403), the Jason Somerville Trust page (403), NH DOE, FCC and National Blue Ribbon pages (403), NH DRA's 2026 tax rate files (403), and `desc.dos.nh.gov` (403);
- Google Drive minutes behind a sign-in (BES board minutes of March 17 and April 14, 2026, so the March open-enrollment vote is unknown);
- BES's preschool days, hours and tuition, nurse hours, the PE schedule, the 2026-27 bus sheet, a Profile science lab or technology renovation, counts of Profile students at Gallen and Paradice, and teacher turnover (not found).
