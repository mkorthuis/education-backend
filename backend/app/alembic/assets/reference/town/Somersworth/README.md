# Somersworth: Research for Ask NH Education Facts

Cited facts and figures for answering Somersworth, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the ToLoad towns. Somersworth is a city in SAU 56. Rollinsford, which the brief placed in SAU 56, now runs its own SAU 104. The Somersworth School District runs:
- Idlehurst Elementary: preschool to grade 2, with a Head Start classroom;
- Maple Wood Elementary: grades 3–5;
- Somersworth Middle School: grades 6–8;
- Somersworth High School: grades 9–12, with the Somersworth Career Technical Center.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools-and-families.md` | Start times (Maple Wood 8:20, Idlehurst 8:55), YMCA care from 7:00 ($70 a week; Maple Wood after-care wait-listed), the district preschool (31 of 48 with IEPs) and free Head Start (18 places, 8:00–2:00), busing rules, class-size policy (18 in K–2, 23 in grades 3–5), aide openings, summer meals, no early-release days | 13 | 75 | 3 | 22 MB |
| `middle-high-and-ctc.md` | Building Trades as year 1 of the carpenters' apprenticeship, the CTC's 80-minute blocks, college credit, 376 students and three counselors, four AP courses (French dropped), the health center, band, chorus and theater, robotics, no Algebra I in middle school (2023-24), sports participation, Early College, no late bus | 14 | 92 | 4 | 16 MB |
| `support-and-choices.md` | Special education programs and outside placements, the 2026-27 paraprofessional and social worker cuts under the city's tax cap, open enrollment (none out, two in), policy JJJ for home-educated and EFA students, homeschool credit, Seacoast Charter (lottery, no bus), Berwick Academy's tuition | 11 | 55 | 1 | 18 MB |
| `money-and-governance.md` | SchoolCare's $672,467.32 bill, the 2026-27 budget ($2,180,527 over the city tax cap; $34,622,278 approved), special education (about a third of the budget; 296 of 1,334 students with IEPs), Rollinsford's exit, the Mayor's Commission, debt ending after FY2030, the tax rate's rank | 7 | 58 | 5 | 31 MB |
| **Total** | | **45** | **280** | **13** | **87 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.12 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Somersworth`). All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 32 full, 25 partial, 3 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Somersworth` 245, `town Somersworth` 29, no place 5, `district Seacoast Charter School` 1.
- **Pending facts:** 6.
- **Raw folders:** each under 100 MB.
- **Quotes:** 626 of 752 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | SchoolCare's bill, $672,467.32 | Board minutes, October 28, 2025 |
  | The 2026-27 budget, $34,622,278 | Board minutes, April 7, 2026 |
  | $2,180,527 over the tax cap | The February 2026 budget committee minutes and reduction list |
  | Rollinsford's $238,410 payment | SAU 56's FY25 and FY26 budget presentations |

## Premises checked

| Question says | What the sources show |
|---|---|
| Maple Wood at 7:30, Idlehurst at 8:55 (P8.1) | Maple Wood starts at 8:20 (buses from 7:32); Idlehurst's 8:55 is right |
| Pre-K and Head Start at Idlehurst (P1.1) | Right: two programs |
| A bus downtown (P1.3) | Kindergartners always ride; grades 1–2 over a mile; routes stop downtown |
| Translated notices (P2.1) | Nothing found |
| Early releases and a late bus (P10.1, P10.2) | No early-release days; no late bus |
| A paid apprenticeship after CTC carpentry (P5.1) | Year 1 of the union apprenticeship counts; students still apply |
| Half the day at the CTC (P5.2) | One 80-minute block of four |
| Free college credit (P5.3) | Partly: Building Trades credit at NEIT and Keene State; Early College $150 a course |
| Arts cut (P11.2) | No: band, chorus and theater continue |
| Cuts after the health care bill (P7.2) | The bill was real; the cuts came from the city's tax cap |
| Seacoast Charter (P9.2) | A lottery; no bus |
| Yearly homeschool paperwork (P18.2) | Out of date since July 1, 2026 |
| Enrollment around 1,000 (P3.1) | 1,263–1,334 |
| Over a third on special education (P3.2) | About right: 33.8% proposed for 2026-27 |
| The Mayor's Commission (P3.3) | Real; a plan is due by May 2027 |
| SAU 56 shared with Rollinsford (P17.3) | Out of date: Rollinsford is SAU 104 |
| Teachers leaving for Dover and Portsmouth (P14.1) | No data; starting pay is close to Dover's |
| Low scores (P4.1) | The district's own slide puts it at the 16th percentile |

## Corrections and additions to earlier files

- **Brief:** "SAU 56 with Rollinsford" is out of date.
- **Rochester and Dover:** consistent. Dover's research could add the SchoolCare dispute details (in `money-and-governance.md`'s notes).

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 125 (Somersworth)** says the council's adoption date wasn't found. The council passed ordinance 8-26 between April 6 and 7, 2026, and the board approved $34,622,278 on April 7.

## Browser pass

The agents' blocked pages were:
- both city sites (somersworth.com and somersworthnh.gov, HTTP 403), so the charter's tax cap text, the council's votes, recreation and youth sports pages are missing;
- the health center's page (HTTP 520).

None is essential to the answers.

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 5 saved bus and transportation copies (577 in all; schools, child care centers, businesses and other public places keep theirs).
- 2 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- House numbers of home stops removed from quotes in the research files.
