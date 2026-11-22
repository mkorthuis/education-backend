# Hanover: Research for Ask NH Education Facts

Cited facts and figures for answering Hanover, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the sixth wave of the ToLoad towns. Hanover is in SAU 70, an interstate SAU with Norwich, Vermont:
- **The Hanover School District** runs the Bernice A. Ray School (K–5).
- **The Dresden School District**, an interstate district of Hanover and Norwich, runs Richmond Middle School (grades 6–8; Norwich students join in grade 7) and Hanover High School (grades 9–12). It also takes tuition students from Lyme and Cornish.

Juniors and seniors may take career programs at the Hartford Area Career and Technology Center in White River Junction, Vermont.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `ray-school-and-families.md` | KAST after-school care (to 5:30; $88–$400 a month; May waitlist), late fees, bus routes from Etna (first stops 6:45; rides up to 55 minutes), the K–1/K–2 adult-at-the-stop rule, Wednesday 1:55 dismissals, class plans for 2026-27, Advance Transit, no Hanover preschool (Marion Cross pre-K puts Hanover children last), no federal lunch program at Ray | 16 | 66 | 2 | 17 MB |
| `richmond-support-and-choices.md` | Norwich joining in grade 7, Richmond sports since 2026-27 ($65, waived for free/reduced lunch; homeschooled residents may play), phones banned all day (policy JICJ), SAU 70's 2026 parent survey, registration and residency papers, guardianship and records access, Ray's counselors, EFA applicants in the Upper Valley | 17 | 73 | 1 | 5.2 MB |
| `hanover-high-school.md` | HACTC (half-day; Dresden pays tuition), Dartmouth courses (free, up to four), no AP and unlimited honors, five math entry levels, sports fee ($150, waived), parking by lottery, the late-game rule for athletes, college counseling, AI by teacher, the Vermont youth survey (HHS takes Vermont's) | 14 | 111 | 4 | 16 MB |
| `money-and-governance.md` | Hanover's 2026-27 school tax ($9.09, +7.48%; health premiums +25.8%), the Dresden assessment and the FY2023 6th-grade move, the per-pupil split with Norwich (about $33,384 and $33,363), the 6.74 FTE cut at Ray, Lyme's tuition ($23,420), no bond planned, tax relief, the 2010 budget failures, workforce housing | 11 | 92 | 6 | 66 MB |
| **Total** | | **58** | **342** | **13** | **104 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.87 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Hanover`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 28 partial.
- **Topics:** no new topics.
- **Places:** `district Dresden` 202, `district Hanover` 77, `town Hanover` 45, `sau 70` 16, `district Lyme` 2. The Hartford center and Norwich's Marion Cross are in Vermont, which the site has no place type for. Their facts are placed with the district they bear on.
- **Pending facts:** none.
- **Raw folders:** the four total 104 MB; each is under 100 MB. A town sales report listing private buyers was deleted rather than kept.
- **Quotes:** 724 of 860 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Hanover's projected school tax, $9.09 | SAU 70's budget table (read from the image) |
  | Lyme's tuition, $23,420 | Dresden's FY25 budget book |
  | The Richmond sports fee, $65 | Richmond's athletics page and fee waiver form |

## Premises checked

| Question says | What the sources show |
|---|---|
| After-school care until 5:00 (P1.1) | KAST runs to 5:30 |
| Pre-K at Marion Cross but not Ray (P3.1) | Right: Hanover runs no preschool; Marion Cross puts Hanover children last |
| Long bus rides from Etna (P8.1) | Right: first stops at 6:45; rides up to about 55 minutes |
| An adult at the stop for K–2 (P8.3) | SAU 70's page says K–2; its guidelines and Ray's handbook say K–1 |
| The lunch application (P17.1) | Ray isn't in the federal program; the form is New Hampshire's voluntary one |
| Norwich students merging in 6th grade (P1.2) | No: they join in grade 7 |
| A late bus from Richmond (P17.3) | None listed |
| A counselor at Ray (P20.3) | A counselor and a counselor/psychologist; no social worker |
| Trades at Hanover High (P4.1) | At HACTC in Vermont |
| A rigid freshman schedule (P7.2) | Structured, with five math entry levels and placement |
| Parking for a junior (P13.3) | Hard: permits go to hardship cases, then seniors by lottery |
| College counseling left to parents (P18.2) | Not as stated |
| AI banned or taught (P19.2) | Neither: teachers decide case by case |
| The Dresden assessment always climbing (P2.1) | Mostly right; the FY2023 jump came from Hanover's 6th grade moving into Dresden |
| Hanover paying more than Norwich (P2.2) | Not shown: per-pupil costs are nearly equal |
| About 6.7 FTE cut (P15.1) | Right: 6.74 at Ray, mostly long-unfilled aide posts |
| Lyme paying tuition (P15.2) | Right: $23,420 a student for 2024-25 |
| A big building bond (P15.3) | None in either 2026 warrant |

## Corrections and additions to earlier files

None needed. Hanover's own low and moderate income tax relief page still shows pre-2023 limits; Hart's Location's `property-tax-relief` fact 3 has the current ones.

## Library notes (for review, not applied)

- **The coverage table** lists Hanover's kindergarten day, cutoff, registration and preschool as not found. All are here now.
- **`budget-form-and-vote-dates` 52 (Hanover):** the legal basis it lacks is Chapter 160 of the 2004 session laws.
- **`graduation-requirements` 10:** HHS's counseling page says the FAFSA is a graduation requirement; the library's rule says schools must give students the opportunity to complete it.
- **The Marion Cross pre-K FAQ copy:** SAU 70's page now gives a capacity of 36 rising to 54.

## Browser pass

The agents' blocked pages were:
- SAU 70's Simbli policies (bot check);
- the Dresden parking policy on BoardDocs (HTTP 403);
- Dartmouth Real Estate's page (HTTP 403).

The board policies would add the bullying, residency and alternative-credit texts. The facts already cite the handbooks' versions.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 19 saved bus and transportation copies (1,667 in all; schools, child care centers, businesses and other public places keep theirs).
- Graduates' names removed from 3 saved annual report copies; 3 PDFs deleted.
