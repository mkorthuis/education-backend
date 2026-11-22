# Seabrook: Research for Ask NH Education Facts

Cited facts and figures for answering Seabrook, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the first wave of the ToLoad towns (with Atkinson, Plaistow, Hampstead and Pelham). Seabrook is in SAU 21:
- **The Seabrook School District,** with Seabrook Elementary (preschool to grade 4) and Seabrook Middle (grades 5–8) on Walton Road.
- **The Winnacunnet Cooperative,** with Hampton, Hampton Falls and North Hampton, for grades 9–12.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-middle-school.md` | The 8:00–2:30 day and two after-school programs to 6 p.m., Niche grades (both C, read in Chrome), the 2024 growth jump and the 2026 reading drop, compressed math and Algebra I, Spanish-speaking families, the preschool, kindergarten (about 11 per teacher), reading help in a daily intervention block, phones and Chromebooks, the 1–4 report card | 15 | 68 | 1 | 69 MB |
| `winnacunnet-and-sst-for-seabrook.md` | Winnacunnet facts the shared file lacks (placed `district Winnacunnet Cooperative`): the Seabrook bus routes (first pickups 6:54, arrival 7:25), SST in 9th grade (engineering only), the trimester schedule, Early College, 33% math explained, class rank, the Evening Program, vaping and fighting rules, Seabrook-only scholarships, Sea to Summit | 8 | 42 | 2 | 19 MB |
| `student-support-and-choices.md` | Moving within town, EFAs (46 Seabrook students), grades on a phone, summer programs, IEP and 504 help, bus bullying, counselors, open enrollment (bills failed), IEPs into Winnacunnet, homeschoolers in activities, snow calls by SAU 21's superintendent, Sacred Heart services votes | 12 | 63 | 1 | 19 MB |
| `money-and-governance.md` | Winnacunnet's cost per pupil and formula (Seabrook pays 32.59% with 30.68% of students because the plant's value counts), the nuclear plant's $45 million three-year agreements, budget failures 2024–2026 and the default, the 2024 SAU 21 withdrawal study and vote (722–579 to stay), the elderly exemption from 65, Winnacunnet votes by town, building plans, teacher pay | 8 | 54 | 5 | 46 MB |
| **Total** | | **43** | **227** | **9** | **153 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.91 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Seabrook`). All 9 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 29 full, 30 partial, 1 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Seabrook` 144, `district Winnacunnet Cooperative` 46, `town Seabrook` 22, `sau 21` 15.
- **Places for the backend:** `places.yaml` already has Seabrook's Winnacunnet row. No change.
- **Raw folders:** all under 100 MB.
- **Quotes:** 598 of 680 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The plant's three-year agreement, $45 million for 2024–2026 | Seabrook's 2025 town report (OCR) |
  | The FY2027 default budget, $19,040,759 | The Seabrook School District 2025-26 annual report's warrant |
  | The SAU 21 withdrawal article, 722 to 579 | The district clerk's March 11, 2025 results (scanned page, read as an image) |
  | The Child Benefit Services petition failing 531–741 in 2025 | The same page |
  | Winnacunnet bus pickups from 6:52–6:54 a.m. | The 2026-27 WHS route sheet |

## Premises checked

| Question says | What the sources show |
|---|---|
| An 8:00–2:30 elementary day (P1.1) | Right; two after-school programs run to 6 p.m. |
| C- and D+ ratings online (P3.1) | Niche gives both schools an overall C (read in Chrome); proficiency rose in 2024 and elementary reading fell to 23% in 2026 |
| Honors or accelerated math (P3.2) | A compressed 7th/8th-grade course and Algebra I in grade 8 |
| About a third proficient in math (P7.1) | Right: 34% at the middle school in 2026 |
| Kindergarten classes of 15 or 25 (P18.1) | About 11 per teacher (44 children, 4 teachers, 2025-26) |
| A 280-student middle school (P14.2) | About right: 277 in 2024-25, 259 in 2025-26 |
| A jump in growth in 2024 (P20.1) | Right: math 51 to 59, reading 47 to 61 |
| A state competency report card (P20.3) | The 1–4 card is SAU 21's own choice |
| Almost $29,000 a pupil at Winnacunnet (P2.1) | Right: $28,650.51 |
| Half struggling in math (P2.1) | About two-thirds below proficient in 2025 |
| The nuclear plant's cushion (P2.3) | Partly: the plant's share of value fell from 54.5% (2011) to 35.3% (2025) |
| A school tax break at 70 (P10.3) | The elderly exemption starts at 65 |
| SAU 21 serves four towns (P17.1) | It serves five districts |
| Separate K–8 and high school management (P17.2) | Partly: two districts, one SAU office |
| 33% math at Winnacunnet (P9.1) | The spring 2025 result on the ballot; 44% for grade 11 in 2026 |
| SST trades in 9th grade (P7.2) | Only Engineering takes rising freshmen |
| Running Start (P4.3) | Renamed Early College; two courses a year free |
| The Evening Program (P13.2) | Exists and is free |
| Open enrollment (P12.3) | The 2026 bills failed; no local article |
| Seabrook following Hampton's weather calls (P18.2) | SAU 21's superintendent decides for its schools; Hampton's K–8 is SAU 90 |
| Teachers leaving for pay (P20.2) | Not shown: Seabrook's average salary is above Hampton's |

## Corrections and additions to earlier files

- **Winnacunnet** (`../winnacunnet/README.md`): now points to this research's 41 Winnacunnet facts. The shared file itself is unchanged.
- Hampton's and Exeter's files agree with this research (Seabrook's 2026 budget vote, 507–614; its 2025 full-value rate; SST counts).

## The site's data

- `recommended-improvements.md` A8, item 9: Seabrook Middle's class size of 6.3 (2025-26), and the district's 0.00 (2024-25), look like reporting artifacts.
- The brief's school counts (302 and 277) were October 2024 counts; October 2025 counts are 282 and 259.

## Browser pass (November 21, 2026)

- **Read in Chrome and added:** Niche's pages for Seabrook Elementary and Seabrook Middle (`elementary-and-middle-school.md`, school-rating-sites 1).
- **Still not retrieved:**
  - the town and library websites (HTTP 403);
  - SAU 21's Simbli board portal (minutes, the capital plan, Winnacunnet's homeschool policy);
  - winnacunnet.org (booster dues, AP results);
  - the Adventure Zone's current fees (its site is down).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 4 saved bus and transportation copies (76 in all; schools, child care centers, businesses and other public places keep theirs).
- 4 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- The state's resident birth, marriage and death lists removed from 2 saved town report copies (headings and record counts kept); 1 report PDF deleted.
