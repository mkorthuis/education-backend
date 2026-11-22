# New Boston: Research for Ask NH Education Facts

Cited facts and figures for answering New Boston, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21–22, 2026, in the fifth wave of the second ToLoad batch. New Boston is in SAU 19 with Goffstown:
- **New Boston Central School (NBCS)** serves preschool to grade 6.
- **Grades 7–12** attend Goffstown's Mountain View Middle School and Goffstown High (GHS) under an AREA agreement renewed for 2024–2034.

The district votes by official ballot. Goffstown was researched in `../Goffstown/`. These files add New Boston's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `nbcs-and-families.md` | Full-day kindergarten (approved March 2026), the Rec program's waitlist ($275 a month, to 6 p.m.), the YMCA bus to Goffstown and Roots and Wings, scores against Bedford and Amherst, the preschool (role-model children with IEP children), meal prices ($4.00 lunch), one early release (June 16, 2027), three kindergarten sections planned | 16 | 79 | 5 | 23 MB |
| `support-and-choices.md` | The July 2026 lead tests (four outlets over 5 ppb, replaced and retested), one counselor and a nurse, no gifted program, aides and reading specialists in the FY28 request, Mountain View's size (880 in grades 5–8), New Boston's aide and life skills costs at Goffstown, the new access policy JJJ (EFA students) | 13 | 78 | 3 | 30 MB |
| `mountain-view-and-goffstown-high.md` | GHS's hands-on courses, the 6:30 a.m. high school runs, one late run home (5:30 p.m.), SafeStop tracking, no welding club found, 151 New Boston students at Mountain View and 283 at GHS (October 1, 2026) | 7 | 33 | 1 | 14 MB |
| `money-and-governance.md` | The tax cap vote (1,879 to 1,277; 59.5%, short of 60%), SAU 19's budget up 16.4% while NBCS fell from 477 to 407, a roughly $3 million lease for boilers, ventilation and windows (no bond), tuition to Goffstown ($8,178,779 proposed for FY28; payments under budget), the superintendent's retirement, deliberative sessions on weekday evenings | 9 | 68 | 3 | 29 MB |
| **Total** | | **45** | **258** | **12** | **96 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.06 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh "New Boston"`). All 12 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial.
- **Topics:** no new topics. The money file uses the library's `budget-deliberative-session`.
- **Places:** `district New Boston` 207, `district Goffstown` 24, `town New Boston` 19, `sau 19` 7, no place 1.
- **Pending facts:** 11, citing draft policies (EFAA, JJJ, JICK), the draft White Buildings lease and draft minutes.
- **Raw folders:** each under 100 MB. Bus copies keep only times and street names.
- **Privacy:** the main session removed 45 residents' and board members' house numbers from the saved minutes and packets, and deleted 11 PDFs of those documents.
- **Quotes:** 573 of 651 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The tax cap vote, 1,879 to 1,277 | The town's hand tally, and the site's own Question 2 data |
  | FY28 tuition, $8,178,779 (**derived**) | The two budget lines: $2,235,233 for Mountain View and $5,943,546 for GHS |
  | The lease quotes at 4.98% | Goffstown's May 11, 2026 board meeting file |

## Premises checked

| Question says | What the sources show |
|---|---|
| Full-day kindergarten (P1.1) | Right, from fall 2026 |
| A huge Rec waitlist (P1.2) | Right as last posted |
| A daycare van (P1.3) | Partly: the YMCA bus |
| Preschool only for special needs (P10.1) | Partly |
| Early release days (P20.2) | Only the last day |
| Pull-out enrichment (P4.2) | None |
| Starting over at Mountain View (P6.2) | Not by the rules |
| Cap-driven aide cuts (P6.3) | The FY28 request already cuts two aides |
| Several counselors (P13.2) | One counselor and a nurse |
| Clean water tests (P18.3) | No: four outlets over the limit, since fixed |
| Hands-on tracks gone at GHS (P2.1) | Not supported |
| A 6:30 bus (P2.2, P15.2) | About right |
| A late bus (P2.3) | Yes, one run |
| Taxes up every year (P3.1) | Not every year |
| The tax cap (P3.2) | Not adopted: 59.5% |
| A big bond (P5.2) | None; a lease instead |
| Half-empty buses (P12.1) | No ridership data |

## Corrections and additions to earlier files

- **Goffstown** (`../Goffstown/`):
  - New Boston's October 1, 2026 counts at Mountain View and GHS (151 and 283) fill a gap in its money file.
  - GHS's late run to New Boston is scheduled for 5:30, not the handbook's 5:00.
  - The YMCA's prices match.
- **This town's brief and questions:** both said SAU 19 includes Dunbarton. It serves only Goffstown and New Boston; Dunbarton is in SAU 67 with Bow. The main session corrected both.

## Library notes (for review, not applied)

- **New Boston fact 96:** it says the 2026 deliberative session date wasn't found. It was Tuesday, February 3, 2026, at 7 p.m.; the 2027 session is Tuesday, February 2.

## Browser pass

Not needed for the answers. Not retrieved:
- NH DOE's special education data and lead-results pages (HTTP 403);
- SAU 19's November 10 votes, which aren't posted.
