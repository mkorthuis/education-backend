# Newton: Research for Ask NH Education Facts

Cited facts and figures for answering Newton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the second ToLoad batch. Newton's students attend the Sanborn Regional School District (SAU 17), shared with Kingston:
- Daniel J. Bakie School, in Kingston: preschool to grade 2;
- Memorial School, in Newton: grades 3–5;
- Sanborn Regional Middle and High School, in Kingston. High schoolers may take career programs at the Seacoast School of Technology in Exeter.

The district votes by official ballot. Sanborn was researched first in `../Kingston/`; these files cite Kingston's facts and add Newton's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-and-families.md` | Bus rides from Newton to Bakie (11–46 minutes in the morning; six stops over policy EEA's 45-minute limit), Bakie and Memorial buses rarely lining up, why the schools split by grade (a two-thirds vote in March 2019, from 2020-21), no care inside Memorial (the YMCA program at Bakie; buses to three centers), full-day kindergarten, delays, ESL, preschool referral and the Region 10 agreement | 11 | 27 | 3 | 6 MB |
| `support-and-choices.md` | Therapy set by each IEP (not automatically pull-out), residency papers (a lease; no deed needed), the calendar against Haverhill's, foster children staying at Memorial while in care, bus and online harassment, Memorial's counselor (social worker and psychologist shared with Bakie), bus video kept up to 10 school days, Newton's mental health center (Derry) | 7 | 41 | 0 | 6 MB |
| `middle-high-and-sst.md` | Phones banned bell to bell (kept off, not locked), a Newton late run at 4:10, two AP courses and 20 honors levels (Exeter 15 AP), class sizes (no official figure), SST and its schedule, renting the track ($200–$800), scholarships ($65,000 to 25 students in 2026), FAFSA help, early graduation and VLACS | 9 | 25 | 1 | 3 MB |
| `money-and-governance.md` | Newton's share of the two towns' school tax (43.5–47.8% since 2011; 45.5% in 2025), its school tax up 31.7% from 2021 to 2025, assessments lagging market value, Question 2 (1,510 to 565), the ballot's cost-per-pupil line, no empty classrooms shown, the October 2026 bidding policy (a new topic), the 2027-28 default only $23,456 above the proposal | 10 | 32 | 1 | 29 MB |
| **Total** | | **37** | **125** | **5** | **44 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.82 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Newton`). All 5 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 44 full, 15 partial, 1 from the site's data. Fifteen questions were answered wholly or mostly by Kingston's files and the library.
- **Topics:** one new topic, added to `../shared-topics.md`: `district-purchasing-and-bidding` (how a district buys goods and services and posts bids).
- **Places:** `district Sanborn Regional` 96, `town Newton` 21, no place 8.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB.
- **Privacy:** the bus sheets list stops by house number. To sort stops by town, the elementary agent sent the posted stop addresses (no names) to the Census Bureau's geocoder. Afterward: Later, the main session also removed residents' births, marriages and deaths from the saved 2025 town report text.
  - the main session removed house numbers from the raw copies, the derived files and the shared-stops table, keeping street names and intersections;
  - the PDF and HTML route sheets and the geocoder results were deleted;
  - agent prompts now forbid sending house-number addresses to outside services.
- **Quotes:** 368 of 478 quoted passages found word for word in the raw copies. Many notes quote Kingston's raw copies, which the facts cite.
- **Spot checks** (main session, all matched): Question 2, 1,510 to 565, against the town's results sheet and the site's data.

## Premises checked

| Question says | What the sources show |
|---|---|
| Half-day kindergarten (P1.2) | Full-day |
| Two schools in two towns (P2.1) | Right: by grade since 2020-21 |
| Bakie and Memorial buses line up (P2.2) | Mostly not: 9 of 49 shared stops within 5 minutes |
| Care at Memorial (P3.1) | None inside; the YMCA program is at Bakie |
| Therapy means pull-out (P4.1) | Set by each IEP |
| A deed to enroll (P10.1) | A lease or closing papers, plus a utility bill |
| A foster child only to the year's end (P15.2) | May stay while in foster care |
| Phones locked up (P6.1) | Banned bell to bell, kept off |
| Fewer AP classes (P7.1) | Right: 2 AP courses running |
| Newton's share keeps rising (P11.1) | Mixed: 43.5–47.8% since 2011 |
| The state's tax cap (P11.3) | A local option Newton voted for |
| No per-pupil breakdown (P12.1) | Partly wrong: the ballot prints it |
| Empty classrooms (P12.2) | None shown |
| Default budget increases (P19.3) | Out of date: $23,456 above the proposal |

## Corrections and additions to earlier files

- **Kingston** (`../Kingston/`):
  - Memorial's 2026-27 routes, which Kingston's research couldn't download, are here.
  - Kingston's note that the enrollment sheet's columns are shifted is wrong: read cell by cell, the columns are aligned.
  - JICK appeals go to policy ACA, which isn't in the district's posted listing.
  - Memorial had 2.0 counselors in 2023-24 and has 1.0 now, a change over time rather than a contradiction.
  - Policy BEDH gives speakers 5 minutes, while the board page says 3.

## Browser pass

Not needed for the answers. sau17.net shows automated requests a bot check, but it loads in Chrome (see Kingston's README). Still not retrieved:
- NH DOE's special education monitoring pages (HTTP 403);
- the state's apportionment file (HTTP 403);
- Sanborn's bid and RFP page (a bot check).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 1 saved bus and transportation copy (20 in all; schools, child care centers, businesses and other public places keep theirs).
- 3 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
- House numbers of home stops removed from quotes in the research files.
- The state's resident birth, marriage and death lists removed from 1 saved town report copy (headings and record counts kept).
