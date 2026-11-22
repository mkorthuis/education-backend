# Swanzey: Research for Ask NH Education Facts

Cited facts and figures for answering Swanzey, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the sixth wave of the ToLoad towns. Swanzey's students attend the Monadnock Regional School District (SAU 93) with Fitzwilliam, Gilsum, Richmond, Roxbury and Troy. In Swanzey it runs:
- Mount Caesar Elementary School: preschool to grade 6, since Cutler closed in June 2026;
- Monadnock Regional Middle and High School: grades 7–12, sharing a building.

Students may take career programs at the Cheshire Career Center at Keene High. The other five towns have no research of their own; facts about Monadnock serve all six. The town's site is now swanzeynh.gov.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `mount-caesar-and-families.md` | Cutler's closing (grades 3–6 to Mount Caesar; 575 students in September 2026), the addition and security work, 6th graders staying, preschool (tuition for children without IEPs), the cutoff and early entry, Beyond the Bell (free; no before-school program), bus rides, Spanish materials, teachers' prep time, Keene's summer camps for non-residents | 13 | 64 | 1 | 29 MB |
| `high-school-and-career-center.md` | The Cheshire Career Center (2027-28 form due March 31; SAU 93 gets 20% of seats; blocks of 2 to 2½ hours), welding taught at MRHS, Early College through River Valley and Keene State's program, $300 a year toward college courses, summer school and VLACS, work-habits scores, graduates' plans (57% further schooling) | 7 | 42 | 2 | 25 MB |
| `support-daily-life-and-choices.md` | The support staff contract (1:1 paras not pulled to substitute), speech staffing, athletic trainers from Cheshire Medical Center, no pay-to-play fee, hall monitors (quoted, not added), the 7:30 start (70 minutes before Keene High), phones, high school hockey with other towns, home education and EFAs, out-of-district IEP placements | 13 | 75 | 1 | 31 MB |
| `money-and-governance.md` | The six-town split (half pupils, half value; Swanzey 51.5%), local school tax per pupil by town, the Cutler sale (two appraisals; a charitable-trust court petition; a March 2027 article), the rate after Cutler ($10.63), the tax cap (61.2% district-wide; Swanzey 57.0%) and the planned $600,000–$800,000 in cuts, the 2025 default budget, aide pay | 6 | 79 | 7 | 20 MB |
| **Total** | | **39** | **260** | **11** | **105 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.94 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Swanzey`). All 11 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 36 partial.
- **Topics:** no new topics.
- **Places:** `district Monadnock Regional` 230, `town Swanzey` 19, `town Keene` 7, `district Keene` 3, no place 1.
- **Pending facts:** none.
- **Raw folders:** the four total 105 MB; each is under 100 MB.
- **Quotes:** 537 of 638 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Swanzey's 2026 local school rate, $10.63 | The town tax collector's page |
  | The cap's allowed increase, $884,572 | Board minutes, November 10, 2026 |
  | The support staff contract vote, 1,399 to 677 | The 2026 annual report |
  | Swanzey's 51.5% share | The apportionment table (transcribed from the image) |

## Premises checked

| Question says | What the sources show |
|---|---|
| Cutler closed (P1.1) | Right: June 2026; grades 3–6 moved to Mount Caesar |
| Crowding at Mount Caesar (P1.2, P15.2) | Can't be confirmed: 575 students against 585 in both schools in 2024-25, with a new addition |
| 6th graders moved (P19.1) | No: they stay at Mount Caesar |
| Free preschool (P5.1) | Not for every child: tuition without an IEP, and families drive |
| A late-September birthday (P5.3) | Can start; October 1–November 1 birthdays rarely get early entry |
| Spanish notices (P10.1) | Only the meal application and the enrollment site |
| Welding at the Career Center (P2.1) | Not offered there; MRHS teaches it |
| Half a day at the Career Center (P2.2, P12.1) | 2 to 2½ hours of a 7-hour day |
| Low scores (P6.3) | Right: 17% of juniors proficient in math in 2026, against 30% statewide |
| Super early start times (P13.1) | Right: 7:30, 70 minutes before Keene High |
| Locked bathrooms (P12.2) | Not found |
| Contract staff replacing hires (P7.1) | Partly supported |
| Pay-to-play (P19.3) | No fee listed |
| Yearly homeschool filing (P9.2) | Out of date since July 1, 2026 |
| Selling Cutler (P1.3) | Under way, with a court petition and a March 2027 article |
| Taxes going down after Cutler (P3.2) | The rate fell from $11.03 to $10.63; no staff savings expected |
| The tax cap (P3.3) | Passed district-wide; cuts of $600,000–$800,000 planned, not yet listed |
| The six-town formula (P8.3) | Half pupils, half value; whether it's fair is a judgment |
| Aides and bus drivers (P15.1) | The district ranked itself lowest of eight for first-year aides |
| The default budget rising (P17.2) | Right: up 23.6% with flat enrollment |

## Corrections and additions to earlier files

- **Keene** (`../Keene/middle-high-and-career-center.md`): this research adds the Career Center's 2027-28 form (March 31 deadline, possible lottery, seat shares 58% SAU 29, 22% SAU 60, 20% SAU 93). Not a correction.
- **Conway** (`../Conway/money-and-governance.md`, district-facilities-and-capital 7): a statewide rule (RSA 194:61) is placed `district Conway`. Not changed.

## Library notes (for review, not applied)

- **`cte-centers.csv`:** the Career Center's note ("most students apply in February of their sophomore year") predates the March 31 deadline.
- **`kindergarten-entry-cutoff` 67 (Monadnock)** lacks the early-entrance rule. The coverage table's kindergarten day and registration, and `district-preschool` 73, are filled here.
- **`21cclc-sites.csv`** lists Beyond the Bell at "Mt. Caesar PreK-2" and "Cutler Elementary 3-6", both out of date since July 2026.

## Browser pass

The district's BoardDocs policies and minutes refused the agents.
- **Agent rule:** one agent read a single policy through a headless browser before BoardDocs blocked it. The brief tells agents not to route around a block.
- **Main session:** the main session opened BoardDocs in Chrome, but its policy search returned nothing. Policy IK (earning credit) and minutes since March 2025 remain unread.
- **Also unread:**
  - NH DOE's foster care page;
  - NHIAA's co-op lists;
  - the town site;
  - mrsdproject.com (a configuration error).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 3 saved bus and transportation copies (279 in all; schools, child care centers, businesses and other public places keep theirs).
- 3 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- House numbers of home stops removed from quotes in the research files.
