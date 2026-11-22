# Tilton: Research for Ask NH Education Facts

Cited facts and figures for answering Tilton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the second ToLoad batch. Tilton's students attend the Winnisquam Regional School District (SAU 59), shared with Northfield and Sanbornton:
- the Winnisquam Early Learning Center, in Tilton: a special education preschool;
- Southwick School (K–4), in Northfield, for Tilton children west of I-93;
- Sanbornton Central School (K–4), for those east of I-93;
- Winnisquam Regional Middle School (5–8) and High School (9–12), both in Tilton. The Winnisquam Career Center (WiCC) opened beside the high school in fall 2025; students may also take programs at the Huot Center in Laconia.

The district has no elementary school in Tilton since Union-Sanborn closed in June 2022. It decides its budget at a traditional district meeting. These files are the first research on Winnisquam; Northfield's research follows and cites them. District facts are placed `district Winnisquam Regional` and serve all three towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `early-learning-and-southwick.md` | The Early Learning Center (IEP only; half days), Union-Sanborn's closing (June 2022) and the I-93 split, Southwick's class sizes (12 to 18; policy cap 23 in K–2), route 505 downtown (7:33–8:19; daycare drop-offs), unhired speech and OT positions, ParentSquare, Alma and other apps, the ELL coordinator, winter coats and the Christmas fund, the Hall Memorial Library | 15 | 85 | 2 | 34 MB |
| `middle-school-support-and-choices.md` | WRMS math (49% in 2026, between Belmont and Gilford), the rewritten bullying policy (parents told within 48 hours), aides (42.0 FTE, down from 47.0), Compass Classical Academy in the old Union-Sanborn building (Tilton preference; rides on existing routes), JJJ (re-approved November 16, 2026), Tilton School's aid, 504 plans and College Board tests (a new topic) | 13 | 80 | 0 | 16 MB |
| `high-school-and-wicc.md` | WiCC (172 students against 178 seats; 2.5 credits a full year), Huot's morning bus (8:15) and no electrical program anywhere, grade 11 math under 10%, Early College (renamed Running Start), the class of 2025's 90.2% graduation rate, two AP courses, one shared SRO, phones off (not locked), credit recovery and the Diploma Academy | 10 | 47 | 4 | 26 MB |
| `money-and-governance.md` | The cost split (72% students, 28% property value; Tilton 35.96% of costs, 38.8% of the local tax), Tilton's 2025 school tax up 24.8% and why, the outlets' share of value, the March 20, 2027 district meeting, the fire district rate the site's totals leave out, falling enrollment (1,343 to 1,126), a roof bond up to $7 million planned, 400–500 new housing units | 11 | 52 | 4 | 29 MB |
| **Total** | | **49** | **264** | **10** | **105 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.05 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Tilton`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial.
- **Topics:** one new topic, added to `../shared-topics.md`: `college-board-testing-accommodations` (how students with IEPs or 504 plans get SAT, PSAT and AP accommodations).
- **Places:** `district Winnisquam Regional` 224, `town Tilton` 23, `district Tilton School` 9, `district Compass Classical Academy Charter School` 2, no place 6.
- **Pending facts:** 27, citing draft fall 2026 minutes (the board's minutes stay drafts until approved).
- **Raw folders:** each under 100 MB. The district's ParentSquare feed names students, so only the three cited posts were kept. Later, the main session also removed graduates' names from the saved 2026 Winnisquam annual report text, and deleted that PDF.
- **Quotes:** 747 of 886 quoted passages found word for word in the raw copies.

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day pre-K at the Early Learning Center (P1.1) | No: a special education preschool, half days |
| Union-Sanborn closed in 2024; Southwick crowded (P2.1) | Closed June 2022; Southwick has 12 to 18 per class |
| Tilton children in Northfield (P14.2) | Partly: west of I-93 to Southwick, east to Sanbornton Central |
| Speech and OT on staff at Southwick (P7.1) | Not shown; the positions went unfilled |
| Three apps (P13.1) | More than three |
| WRMS math lags Belmont and Gilford (P3.3) | Not in 2026 |
| The town buses to the charter school (P9.2) | The district does, on existing routes |
| Annual homeschool notice and portfolio (P12.3) | Repealed July 1, 2026 |
| A 504 plan gives SAT time (P20.3) | Partly: College Board must approve it separately |
| A new career center on campus (P4.1) | Right |
| Electrical at Huot (P4.2) | Neither Huot nor WiCC has electrical |
| Career classes don't count (P4.3) | They count: 2.5 credits a year |
| Low math proficiency (P5.1) | Right: under 10% in 2026 |
| Running Start (P5.2) | Renamed Early College |
| An SRO at each school (P19.1) | One shared |
| Phones locked up (P19.2) | Banned, kept off; not locked |
| Outlets make Tilton pay more (P6.2) | Partly: the split is 28% by value |
| A budget ballot (P6.3) | A traditional meeting, March 20, 2027 |

## Corrections and additions to earlier files

- **Belmont** (`../Belmont/belmont-high-and-huot.md`): its WiCC program "Business Enterprise and Entrepreneurship through Agriculture" appears as "Plant Science & Agriculture" in WiCC's 2025-26 Program of Studies. Otherwise consistent.
- **Meredith:** its Winnisquam grade 11 math ("<10") matches.

## Library notes (for review, not applied)

- **`district-preschool` 121** says Winnisquam's site describes no preschool. The Early Learning Center's page and handbook now do.
- **`kindergarten-day-length`** has no Winnisquam entry.

## Browser pass

Not needed for the answers. The agents' blocked pages were:
- Compass Classical Academy's site (no response);
- NH DOE's charter pages and Tilton School's Form 990 (HTTP 403);
- Niche and U.S. News (blocked);
- a Laconia Daily Sun article (HTTP 429, a rate limit on that site, not a search block).
