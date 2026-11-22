# Wolfeboro: Research for Ask NH Education Facts

Cited facts and figures for answering Wolfeboro, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the second ToLoad batch. Wolfeboro's students attend the Governor Wentworth Regional School District (SAU 49), shared with Brookfield, Effingham, New Durham, Ossipee and Tuftonboro:
- **Carpenter School** (K–2) and **Crescent Lake School** (3–6), both in Wolfeboro. Third grade moved to Crescent Lake in 2025-26.
- **Kingswood Regional Middle School** (7–8) and **High School** (9–12), in Wolfeboro, with the Lakes Region Technology Center (LRTC) joined to the high school.

The district votes by official ballot, counted town by town. These files are the district's first research; Ossipee's research, which follows, cites them.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | Carpenter's 3:25 dismissal and the Children's Center's care ($95 a week or $20 a day), third grade moved to Crescent Lake after a 2025 ceiling collapse (kept there by a 9–0 vote), no public preschool now (one planned at Carpenter for 2027-28), the report card scale (no letter grades), contracted speech therapy, volunteer fingerprinting, the 2026 playground reserve (2,687 to 2,453), Wolfeboro's falling K–6 count | 13 | 65 | 1 | 21 MB |
| `middle-school-support-and-choices.md` | Free meals to 300% of poverty (voted 2025 and 2026), storm delays by town instead of district-wide closings (calls by 5:30 a.m.), the late bus (Monday–Thursday), a district-run fleet (38 vehicles; 3–4 leased a year), homeschool and EFA access (policy JJJ, November 2026), counselors (2 at KRMS, 4 at KRHS), the handbook's outdated bullying definition, French and Spanish from grade 7, the rejected wellness coordinator | 16 | 102 | 3 | 46 MB |
| `kingswood-high-and-lrtc.md` | LRTC inside the school day on the high school's bell schedule (7:25–2:20), Kingswood High's size (712 in October 2025; 703 in the 2026-27 profile), SAU 13 students so far (a handful), LRTC enrollment (244; 173 from Kingswood), 15 Early College courses and 7 AP subjects, the pre-Labor Day start, the AI and phone policies, Brewster's aid | 12 | 61 | 4 | 48 MB |
| `money-and-governance.md` | The 2026 default ($236,502 above the proposed budget), the 2025 failure by 9 votes, the cost formula (75% students, 25% property value; Wolfeboro 34.7%, no adequacy grant), school taxes up 48% from 2014 to 2025 with 22.5% fewer resident students, cost drivers (health insurance up 21.3%), contract votes (53–66% yes), bus driver pay ($20.85–$22.35), staff children's tuition | 7 | 63 | 5 | 73 MB |
| **Total** | | **48** | **291** | **13** | **188 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.12 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Wolfeboro`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 31 full, 28 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Governor Wentworth Regional` 256, `town Wolfeboro` 32, no place 3.
- **Pending facts:** 3, citing draft minutes.
- **Raw folders:** each under 100 MB. The address scan finds no home stops; the routing apps that hold bus stops need a sign-in, and nothing was saved from them.
- **Quotes:** 638 of 753 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026-27 default, $70,792,454, and its $236,502 gap | The 2026 deliberative session presentation |
  | The playground reserve vote, 2,687 to 2,453 | The district's 2026 voting results, by town |
  | Kingswood High's 712 students | The 2026-27 program of studies |
  | Bus drivers' $20.85 | The district's 2026 annual report |

## Premises checked

| Question says | What the sources show |
|---|---|
| Carpenter lets out at 3:25 (P1.1) | Right |
| Switching schools in 3rd grade (P1.2) | Right since 2025-26 |
| A gifted group before middle school (P4.2) | None found |
| Pre-K only in private daycares (P15.1) | Right for now; a public preschool is planned |
| A "3" as a B or C (P16.1) | No letter grades: 3.0–3.5 means "consistently meets" |
| Petition after petition for playgrounds (P18.1) | One, in March 2026 |
| Just over the free-lunch cutoff (P6.3) | Covered: free meals to 300% of poverty |
| No late bus (P13.2) | There is one, Monday–Thursday |
| Hour-long rides (P14.1) | Can't be confirmed; no ride times published |
| District-wide snow days (P14.2) | Partly wrong: delays by town |
| An aging fleet (P14.3) | Partly: leased replacements each year |
| Homeschoolers shut out (P9.1–P9.3) | No |
| A 900-student high school (P12.3) | Wrong: 712 |
| More students from SAU 13 (P2.3, P5.2) | Not yet in the numbers |
| A local discount at Brewster (P12.2) | None listed; need-based aid |
| Budget cuts after a "no" vote (P3.3) | Not in 2026: the default was higher |
| A new SAU 13 tuition agreement (P10.1, P20.2) | Not confirmed; on the November 2 agenda |
| A surprise bond (P10.2) | None on the 2023–2026 ballots |
| Contracts a battle every time (P15.3) | Mixed: all passed with 53–66% yes |

## Corrections and additions to earlier files

- **Freedom** (`../Freedom/`): its tuition agreement fact is consistent. The district board accepted the five-year agreement on August 4, 2025. Its fact that Freedom doesn't bus to Kingswood fits the August 2026 condition that sending districts pay for their own transport.
- **Library `district-preschool` 35** says children with special needs are served in public or private preschools or day care. In Wolfeboro those are the Children's Center and Magic Moments.

## Library notes (for review, not applied)

- **places.yaml, Middleton → Governor Wentworth:** the note says Middleton's tuition "is being phased up to Governor Wentworth's per-pupil cost over five years starting in 2026-27". Its own source, Middleton's 2025 warrant, gives only grades 7–12 and the ten-year term (checked by the main session from the scanned warrant), and no source read here mentions a phase-in.

## Browser pass

Not needed for the answers. Not retrieved:
- **Pay rates:** the support staff contract and para pay rates. The state labor board's library refused requests.
- **NH DRA:** the 2026 tax rate and the cooperative apportionment file.
- **Not posted:** Middleton's tuition rate and the November 2 board minutes.
- **Needing a sign-in:** the routing apps (bus times) and the local scholarship list (a Google Sheet).
- **NH DOE:** the gifted report and grants pages.
