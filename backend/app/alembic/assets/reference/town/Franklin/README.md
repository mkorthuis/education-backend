# Franklin: Research for Ask NH Education Facts

Cited facts and figures for answering Franklin, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fifth wave of the ToLoad towns. Franklin is a city and SAU 18. The Franklin School District runs:
- Paul A. Smith School: preschool to grade 4; grade 4 moved there in 2025-26;
- Franklin Middle School: grades 5–8;
- Franklin High School: grades 9–12.

Students may take career programs at the Huot Technical Center in Laconia or the Winnisquam Career Center in Tilton. The City Council adopts the school budget under the city's tax cap. The district's site is now sau18.nh.gov; it showed a bot check to the agents, so the main session read its pages in Chrome.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `paul-smith-and-families.md` | The city's after-school program (bused from the school), bus times (arrive 7:15, leave 2:00; no late bus), the special education preschool (four days, ages 3–4) and Head Start, meals ($3.25 lunch; apply yearly), registration in Alma, schoolwide Title I, staffing under the tax-cap budget | 10 | 54 | 0 | 25 MB |
| `middle-school-and-support.md` | The handbook's conduct and tiered behavior system, who to contact, the counselor and assistance program, the Alma portal and report cards, attendance and retention rules, staffing under the cap (no social worker), policy JJJ for home-educated and EFA students, relatives enrolling children, weekend food | 12 | 76 | 3 | 10 MB |
| `franklin-high-and-pathways.md` | Huot (Franklin-only application) and the Winnisquam center, no electrical program, LRCC courses (four free a year; funding may run out in spring 2027), extra grade points for Early College, honors and AP, competency credit at 2.5, the Adult Diploma Program (online with in-person support 3:30–6:30), the HiSET test site, Tilton School, the High School of Excellence award | 9 | 46 | 2 | 11 MB |
| `money-and-governance.md` | The city charter's tax cap (two-thirds to exceed; every 2026 motion failed), the adopted $19,351,084 budget against the board's $21.55 million (49.75 positions cut), special education at 34.8%, the ended $486,386 federal grant, teacher pay against Laconia and Concord, roofs in 2030–2040, sharing services | 11 | 83 | 4 | 64 MB |
| **Total** | | **42** | **259** | **9** | **110 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.0 million tokens, including three follow-ups from the browser pass.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Franklin`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 31 full, 28 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:**
  - `district Franklin` 204, `town Franklin` 40, no place 7.
  - `district Winnisquam Regional` 4, `district Tilton School` 3, `district Laconia` 1.
- **Pending facts:** 9, citing the draft November 6 minutes and the draft capital plan.
- **Raw folders:** the four total 110 MB; each is under 100 MB. Bus routes are kept only as a times-and-streets summary.
- **Quotes:** 585 of 721 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The adopted budget, $19,351,084 | Council minutes, July 21, 2026, and Resolution 11-27 |
  | The ended grant, $486,386 | The Concord Monitor's September 15, 2025 report |
  | Lunch at $3.25 | SAU 18's food services page (read in Chrome) |
  | Average teacher pay, $54,933 | The site's own salary data |

## Premises checked

| Question says | What the sources show |
|---|---|
| Free full-day pre-K (P4.1) | No: a special education preschool, four days a week; Head Start is the free option for eligible families |
| Free meals for everyone (P11.2) | No: $3.25 lunch from July 1, 2026; apply each year |
| Drop-off for a 7:00 shift (P11.3) | Buses arrive 7:15; the city's before-school care opens at 6:30 |
| Very low scores (P2.1) | Right: 13% math, 23% reading in 2026 |
| Families leaving for Winnisquam or private schools (P2.2) | Not shown by any count |
| Homeschoolers in FMS sports and band (P12.1) | Right, under policy JJJ |
| Automatic retention for absences (P15.2) | No |
| No birth certificate blocking enrollment (P17.1) | A relative can enroll a child; state law covers DHHS and court placements |
| AP or honors at FHS (P2.3) | Extra grade points and honors contracts exist; no course list is posted |
| Huot in 9th or 10th grade (P6.2) | Not in 9th grade |
| Free LRCC classes (P10.1) | Four a year, though a CCSNH article still says two |
| Night classes at Franklin Continuing Education (P19.1) | Online courses with in-person support, Monday–Thursday 3:30–6:30 |
| A school safety and mental health grant pulled (P9.2) | Right: $486,386 ended July 21, 2025 |
| Budget fights every spring (P9.3) | In 2026 they ran into August and November |
| The budget keeps rising (P3.2) | The adopted budget is 1.9% below 2025-26 |
| A big bond coming (P3.3) | None; roofs are planned for 2030–2040 |
| Lower pay than Laconia or Concord (P13.1) | Right: averages of $54,933, $64,499 and $88,176 |
| Merging with neighbors (P13.3) | Talk of sharing services, not with Tilton |

## Corrections and additions to earlier files

- **Brief:** sau18.org now redirects to sau18.nh.gov, and the city's site is franklinnh.gov.
- **SAU 18:** the high school's 2022-23 profile says SAU 18 served Franklin and Hill. When Hill left is worth checking.
- **Laconia** (`../Laconia/student-support-and-choices.md`, adult-education-and-workforce-training 6): it quotes Laconia Adult Education's "$125" HiSET fee. hiset.org now gives $140 for the full exam. Not changed.

## Library notes (for review, not applied)

- **`district-preschool` 31** says Franklin's site doesn't describe the preschool. It's a special education program four days a week (district-preschool 1–4 here).
- **`budget-form-and-vote-dates` summary** lists Franklin's budget form as not found. The City Council adopts it inside the city budget.
- **`21cclc-sites.csv`** labels Paul Smith K–3 and FMS 4–8. Grade 4 moved to Paul Smith in 2025-26.
- **`early-college-at-your-high-school` 5 and `dual-enrollment-rules` 7:** CCSNH's May 2026 article says two free courses a year; LRCC and the FHS handbook say four.

## Browser pass (November 21, 2026)

SAU 18's site loads in Chrome.
- **Read and saved:**
  - the preschool, food services, registration and Title I pages;
  - the FHS counseling page and the Adult Diploma page;
  - the FMS counselors page;
  - the 2026-27 FHS handbook and FMS handbook, and the bus route PDF (summarized).

  The three agents added facts from them.
- **Still unread:**
  - board policies other than the J series;
  - a current FHS course catalog (none is posted);
  - DRA's 2026 tax rates.
