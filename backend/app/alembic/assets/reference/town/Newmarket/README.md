# Newmarket: Research for Ask NH Education Facts

Cited facts and figures for answering Newmarket, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the ToLoad towns. Newmarket is SAU 31, a one-district SAU, with two schools:
- Newmarket Elementary: preschool to grade 5.
- Newmarket Junior-Senior High: grades 6–12.

Students may take career programs at the Seacoast School of Technology.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-school.md` | Care (Linked Together at NES; the town's Play & Stay, $16 a day, bused), walking from the mills (about 1.3 miles; K–3 with an adult), meals, the preschool ($206 a month), class sizes, earliest drop-off, enrollment papers, full-day kindergarten (8:40–3:05), dyslexia screening (i-Ready), Title I reading help and its criteria | 15 | 52 | 0 | 11 MB |
| `junior-senior-high.md` | Comparison with Oyster River (site data), UNH courses (family pays), the middle school's own schedule, college and FAFSA help, SST (52 students, 19%; bus at 7:05), AP (five in person), counselors (about 139 each), work-study credit, band after the music cut, credits (24 for the class of 2027), Early College, scholarships | 8 | 63 | 2 | 27 MB |
| `support-daily-life-and-choices.md` | Translation (none found), paras and their duties, the 5th-to-6th move, therapy scheduling, delays (about 6 a.m.), buses (First Student, renewed to 2031), EFA and homeschool access (JJJ-R, September 2026), the portal, phones ("Off and Away"), counselors, sports co-ops (football with Epping, hockey with Portsmouth, lacrosse with Oyster River), late buses, downtown traffic | 9 | 77 | 2 | 15 MB |
| `money-and-governance.md` | The $39 million bond (flat about $2.1 million a year to 2046), what drives increases (contracts, health insurance, special education at 27%), central office at 4.6%, the $100,000 building reserve (793–257), unfilled positions and lapsed money, enrollment (983), the FY2028 draft (+4.85%), HVAC and roof repairs, renters, community use of fields, tax relief, one tax rate for all property ($20.68) | 11 | 66 | 6 | 38 MB |
| **Total** | | **43** | **258** | **10** | **91 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.94 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Newmarket`). All 10 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 30 partial.
- **Topics:** no new topics.
- **Places:** `district Newmarket` 230, `town Newmarket` 25, no place 3.
- **Places for the backend:** none needed.
- **Raw folders:** all under 100 MB.
- **Quotes:** 576 of 716 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The building reserve article, 793 yes and 257 no | The district's March 10, 2026 election results |
  | The 2026 tax rate, $20.68 | The town's tax rate announcement |
  | Preschool tuition, $206 a month | The 2026-27 preschool application |

## Premises checked

| Question says | What the sources show |
|---|---|
| Walking from the downtown mills (P1.2) | About 1.3 miles; K–3 only with an adult; a bus stop on Main Street |
| No public preschool (P5.1) | There is one: $206 a month for typically developing children; free under an IEP |
| Full-day kindergarten and any cost (P16.1) | Full day, 8:40–3:05; no tuition posted |
| Dyslexia screening only if parents push (P18.1) | No: every child is screened |
| UNH courses (P2.2) | Possible, at the family's cost; also UNH's CATS program |
| A separate middle school wing (P2.3) | No wing, but a separate schedule, lunch and recess |
| AP in person (P12.1) | Five run in 2026-27; the catalog lists seven |
| Trimmed music time (P19.1) | A half-time position was cut; 7th/8th-grade band continues |
| A senior project (P20.1) | None found |
| A yearly homeschool filing with SAU 31 (P10.2) | Never required; policy IHBG still describes the repealed evaluation |
| Bus routes canceled for driver shortages (P9.3) | No record |
| Paraeducator jobs hard to fill (P6.1) | Two openings posted since August; no document calls it a shortage |
| A $39 million bond still being paid (P3.1) | Right, to 2046, but the payment is flat |
| A $100,000 building reserve (P8.1) | Right; the rate is higher than about 80% of towns |
| About a thousand students (P8.3) | Right: 983 |
| A separate commercial tax rate (P17.3) | New Hampshire has one rate for all property |

## Corrections and additions to earlier files

None needed.

## Library notes (for review, not applied)

- `district-preschool` 82 says no tuition or hours are posted. The 2026-27 application gives $206 a month and the session times.
- `kindergarten-day-length` 30 gives pickup "starting at 3:00 pm"; the 2026-27 handbook says 3:05 p.m.

## Browser pass

The agents' blocked pages were:
- NH DOE's enrollment by grade;
- NH DRA's commercial valuation;
- UNH's continuing education page;
- the district's script-only policy portal (BoardDocs copies used instead);
- four counseling Google Docs that need sign-in.

None is essential to the answers.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 9 saved bus and transportation copies (63 in all; schools, child care centers, businesses and other public places keep theirs).
- 3 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- Graduates' names removed from 1 saved annual report copy; 1 PDF deleted.
