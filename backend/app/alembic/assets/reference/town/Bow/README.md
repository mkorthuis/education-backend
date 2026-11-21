# Bow: Research for Ask NH Education Facts

Cited facts and figures for answering Bow, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the ToLoad towns. Bow is in SAU 67 with Dunbarton, and the Bow School District runs:
- Bow Elementary School (BES), with the preschool back there for 2026-27;
- Bow Memorial School (BMS): grades 5–8;
- Bow High School (BHS): grades 9–12.

Dunbarton sends grades 7–12 to Bow under an AREA agreement. Bow students may take career programs at the Concord Regional Technical Center (CRTC). Bow decides its budget at a traditional annual meeting.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-preschool.md` | The preschool's move back to BES, kindergarten (8:00–2:15), kindergartners on shared buses (first riders 26–57 minutes), the Rec Center's care, waitlist and delay days, its rules for children with disabilities, aide postings, meals ($3 lunch), grades 3–8 results on a national scale, an after-school program rules topic | 14 | 56 | 3 | 21 MB |
| `memorial-and-high-school.md` | The CRTC bus (Bus 12) and CRTC+, CRTC payments ($441,401), grade 11 math (SAT cut scores explain the gap), Algebra I in grade 8, 12–13 AP courses, counselors (about 157 students each), languages, closed lunch from 2026-27, the gifted line at $0, an NCAA eligibility topic | 13 | 72 | 4 | 14 MB |
| `support-choices-and-daily-life.md` | Phones banned bell to bell (policy JICJ, October 2025), cut policies (not no-cut), no late buses, the shared SAU 67 calendar, Rec Center sign-ups on workshop and storm days, homeschool and EFA access before and after HB 1817, Bishop Brady ($15,950; EFA-eligible; no Bow busing) | 11 | 60 | 0 | 27 MB |
| `money-and-governance.md` | Dunbarton's 2024–2039 AREA terms (cost per student plus a capital fee; $4,550,290 budgeted, derived), the FY27 school tax (+$2,072,710, +8.26%; health insurance up about 20%), the finished BES addition ($12.4 million bond, 2023), enrollment (1,703, flat), capital reserves, the tax cap (Bow rejected it, Dunbarton adopted it) | 7 | 62 | 3 | 35 MB |
| **Total** | | **45** | **250** | **10** | **97 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.07 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Bow`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 37 full, 22 partial, 1 from the site's data.
- **Topics:** two new topics, added to `../shared-topics.md`:
  - `after-school-program-rules`;
  - `ncaa-initial-eligibility`.
- **Places:** `district Bow` 188, `town Bow` 27, `sau 67` 21, no place 10, `district Dunbarton` 4.
- **Pending facts:** 2. Both are intended: they cite a policy read in its packet draft and a list marked DRAFT.
- **Raw folders:** each under 100 MB.
- **Quotes:** 614 of 760 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The FY27 school tax increase, $2,072,710 | The 2026-27 revenue and tax rate estimate and the budget hearing packet |
  | CRTC payments, $441,401 | The FY2026-27 proposed budget |
  | Bishop Brady's tuition, $15,950 | Bishop Brady's tuition page |

## Premises checked

| Question says | What the sources show |
|---|---|
| The district votes by official ballot (brief) | No: a traditional annual meeting; the intro is corrected |
| The special education preschool at Bow High (P15.1, P15.2) | Out of date: it moved back to BES for 2026-27 |
| Full-day kindergarten (P1.1) | Effectively: the full 8:00–2:15 day, lunch at school |
| Kindergartners on big buses (P1.3) | Right: the same routes as grades 1–4, mostly with high schoolers |
| A Rec Center waitlist (P1.2) | One exists when space runs out; no size published |
| Aide shortages (P5.1) | Not shown either way; one posting open since September |
| One named reading curriculum (P16.3) | None found |
| A CRTC bus (P2.1) | Yes: Bus 12 leaves BHS at 7:30 |
| Math in the low 40s (P3.1) | 43% in 2025, 32% in 2026 (state 30%) |
| Accelerated math at BMS (P3.2) | No track posted; Algebra I in grade 8 for high school credit |
| No-cut teams | Not true: written cut policies |
| A late bus | None |
| A BES building bond (P7.2) | Already built: $12.4 million approved in 2023 |
| The school tax rising as enrollment falls (P4.1) | The levy rose 40.4% from 2020 to 2025; students fell 1.6% |
| Falling enrollment (P16.2, P19.3) | Not so far: 1,703, projected 1,716–1,721 through 2028-29 |
| Booster clubs paying for fields (P13.1) | Not shown: reserves, athletic fees and Dunbarton's capital fee |

## Corrections and additions to earlier files

- **`questions.md`:** its intro said Bow votes by official ballot; corrected.
- **`places.yaml`:** the Hooksett → Bow note said Hooksett pays Pinkerton's rate. Hooksett's memorandum sets Bow's base tuition at Dunbarton's AREA rate; Hooksett pays the contribution its board sets, and Bow may bill parents the rest. The Goffstown and Pembroke notes were corrected the same way. The Dunbarton → Bow row was already there.

## Library notes (for review, not applied)

- **`district-preschool` 11 (Bow)** places the special education preschool at Bow High. It moved back to BES for 2026-27, and the SAU 67 page now posts program details.
- **`budget-form-and-vote-dates` 12 (Bow):** consistent. This research adds the March 13, 2026 meeting's outcome.
- **`cte-centers-overview` 6:** Bow's Program of Studies calls the CRTC both "Concord Regional Technology Center" and "Concord Regional Technical Center".

## Browser pass

The agents' blocked pages were:
- Bow's Simbli policy manual (a bot check);
- the town's website pages (server errors), so the 2026 tax rate and the elderly exemption are missing;
- the 2026–2031 strategic plan PDF, whose text couldn't be read.

None is essential to the answers.
