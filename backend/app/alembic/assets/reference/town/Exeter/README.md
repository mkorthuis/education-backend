# Exeter: Research for Ask NH Education Facts

Cited facts and figures for answering Exeter, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format, ready to load but not loaded.

Gathered November 16–17, 2026, alongside Hampton and Milford. Two districts in SAU 16 serve Exeter:
- **The Exeter School District:** the Exeter Developmental Preschool, Main Street School (K–2) and Lincoln Street (3–5).
- **The Exeter Region Cooperative,** for six towns: Cooperative Middle School in Stratham (6–8) and Exeter High School (9–12), which hosts the Seacoast School of Technology (SST).

Both districts vote by official ballot.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools-and-families.md` | The preschool at 13 School Street ($2,000 a year, Exeter children only), full-day kindergarten since 2017-18, drop-off, advanced learners, special education and the move to Lincoln Street, Great Bay Kids and YMCA care and prices, free meals for every Main Street and Lincoln Street student in 2026-27, class sizes and reading results, Great Bay Charter's application and lottery dates, Stratham and Kensington, English learners, diversity, translated notices | 15 | 97 | 2 | 47 MB |
| `cms-sst-and-getting-to-school.md` | SST's 13 programs (no plumbing or HVAC), its sessions, credits and 1,159 industry certifications in 2025-26, enrollment by sending school (677 in 2026-27), CMS electives, the late buses (4:10–4:15), the drive to Stratham, home education and EFA access (the revised policies), bullying, vaping and phones, sixth graders' first year, substitutes, Exeter Adult Education's evening classes | 12 | 92 | 5 | 65 MB |
| `exeter-high-school.md` | 15 AP courses (3 in science, two for seniors only), the proposal to merge Academic and College Prep levels, portals for two households, clubs, the four Commons, seven counselors (about 193 students each), relearn-and-retake to 80%, PEA's public offerings, the 7:30 start, undecided juniors, placing homeschooled ninth graders, traffic at 2:30, extended learning | 12 | 78 | 4 | 21 MB |
| `money-governance-and-community.md` | The 2026 rate ($19.54; schools $12.79), the cooperative's FY2027 increase by town and Exeter's shares (43.0% of taxes, 44.8% of students, 41.3% of value), elderly exemptions, special education aid and paras, open enrollment (0 in, 0% out), Niche grades (read in Chrome), the Main Street bond paid off in 2026-27, weekend food and private help, public comment for residents without children | 9 | 80 | 4 | 16 MB |
| **Total** | | **48** | **347** | **15** | **149 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.04 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Exeter`). All 15 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 24 full, 35 partial, 1 from the site's data.
- **Topics:** no new topics. `school-rating-sites` (from Manchester) was added to the money file for Niche's grades.
- **Places:** `district Exeter Region Cooperative` 167, `district Exeter` 100, `town Exeter` 38, `sau 16` 27, `district Great Bay Charter School` 8, `district Stratham` 2, `town Stratham` 1, `district Kensington` 1, no place 3. The three no-place facts are UNH's transfer credit rules, which agree with Bedford's file.
- **Places for the backend:** `places.yaml` already has the cooperative's rows for all six towns. No change.
- **Pending facts:** 19 facts cite board minutes still posted as drafts (October 20, 2026 and others). Check them before loading.
- **Raw folders:** all under 100 MB.
- **Quotes:** 713 of 860 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 tax rate, $19.54, with $12.79 for schools | The town's Property Tax Info page |
  | The preschool's tuition, $2,000 a year | The preschool's About Us page |
  | SST enrollment, 677 in 2026-27 (346 from Exeter High, 79 from Winnacunnet) | SST's October 2026 report in the cooperative's board packet |
  | Open enrollment article, Exeter 1,472 to 513 | The town's 2026 cooperative results (scanned; OCR) |
  | The full-day kindergarten bond's last payment, $488,483, drops out in 2027-28 | School board minutes, November 4, 2025 |

## Premises checked

| Question says | What the sources show |
|---|---|
| Preschool at Main Street School and its waitlist (P1.1) | Run by Main Street but at 13 School Street; no waitlist posted |
| Full-day kindergarten for everyone (P1.2) | Yes, since 2017-18 |
| SST plumbing or HVAC (P2.1) | No such program; 13 programs, Electrical new this year |
| A 2026 rate of $19.54 (P4.1) | Right; school taxes rose 37% from 2019 to 2025 while resident students fell 13.4% (derived) |
| Exeter subsidized by, or subsidizing, the other towns (P4.2) | Not shown either way: Exeter pays 43.0% of the cooperative's school taxes, has 44.8% of its students and 41.3% of its property value (derived) |
| The state capping special education aid; para cuts (P6.3) | The aid is flat and prorated, not called a cap; no para cuts found |
| The bus ride to Stratham (P7.1) | About 3 road miles and a 10-minute drive (derived); no route times posted |
| A late bus at CMS (P7.2) | Yes: two buses at 4:10–4:15 with three Exeter stops |
| Routes combined for driver shortages (P9.3) | No record in a year of board minutes |
| Why PreK–2 and 3–5 are split (P10.2) | No source gives a reason |
| Great Bay Charter's lottery (P10.3) | Held only for an oversubscribed grade; seats now "space-available" |
| An open enrollment debate (P12.2) | Adopted in March 2026 with 0 students in and 0% out |
| A 7:30 start at Exeter High (P13.2) | Right: 7:30 to 2:30; no discussion of changing it since September 2025 |
| Niche against Oyster River and Portsmouth (P14.2) | Read in Chrome: the cooperative B+ (12th in NH), Exeter K–5 A, Portsmouth A, Oyster River C |
| Bonds for Main Street or Lincoln Street (P14.3) | None proposed; the only bond is paid off in 2026-27 |
| Annual homeschool paperwork (P16.2) | Out of date: notice only when a child withdraws or wants district programs; SAU 16's handout still cites a repealed rule |
| Traffic at 2:30 (P18.2) | The 2:30 dismissal is right; the town's traffic studies of the entrance now return 404 |
| SST evening classes for adults (P20.1) | None posted; Exeter Adult Education runs evening diploma courses |
| "Almost $13" for schools (P20.3) | Right: $12.79, plus $1.09 of state education tax |

## Corrections and additions to earlier files

- **Winnacunnet** (`../winnacunnet/winnacunnet-high-school.md`): its question rows and gap notes now point to SST's count of Winnacunnet students (79 in 2026-27), its session times, and its note that Winnacunnet sends no SST buses on weather-delay days.
- Portsmouth's and Dover's files agree with this research. No changes there.

## Library notes (for review, not applied)

- `cte-centers-overview` doesn't list SST. This research has its sending schools and 13 programs.
- `district-preschool` 28 says no tuition is posted for the Exeter Developmental Preschool. Its About Us page now says $2,000 a year.
- The library's kindergarten table says Exeter's day length was "not found." The elementary file has it.
- `home-education-rules` 10: SAU 16's policies and handout still cite the repealed Ed 315.

## Browser pass (November 17, 2026)

- **Read in Chrome and added:** Niche's district pages for both Exeter districts, Oyster River and Portsmouth (`money-governance-and-community.md`, school-rating-sites 1).
- **Still not retrieved:**
  - **The state's cooperative formulas,** which would explain how the cooperative's costs are split. NH DOE lists them on its Cooperative Apportionments page, but the file is a PDF, which Chrome can't read. The town shares above come from the cooperative's own figures.
  - **DRA's cooperative apportionment PDFs.**
  - **The YMCA's Exeter registration listing** (HTTP 429, not retried).
  - **The six-town totals of the March 2026 cooperative vote.**
  - **The image pages of the cooperative's FY2028 draft budget.**

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 4 saved bus and transportation copies (8 in all; schools, child care centers, businesses and other public places keep theirs).
