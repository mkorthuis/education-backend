# Windham: Research for Ask NH Education Facts

Cited facts and figures for answering Windham, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format, ready to load but not loaded.

Gathered November 20–21, 2026. Windham is SAU 95, a one-district SAU, with four schools:
- Golden Brook School: preschool to grade 4, with the Early Childhood Program;
- Windham Center School: grades 5–6;
- Windham Middle School: grades 7–8;
- Windham High School: grades 9–12.

High school students may take career programs at Salem High's CTE center or at Pinkerton Academy. The district votes by official ballot.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `elementary-schools-and-families.md` | The preschool lottery, the YMCA's before- and after-school care ($70 a week mornings; a waitlist after school), kindergarten supplies and the full day, reading (Wit & Wisdom since 2024-25, Fundations, Heggerty, Lexia, UFLI), the new math programs (Illustrative Math K–4, Open Up 5–8), IEPs and summer help, drop-off and pickup, Tutor.com for grades 4–6, ESL, the move to Windham Center (recess kept), Golden Brook's class sizes, specials, STEAM, meals | 12 | 74 | 1 | 57 MB |
| `middle-and-high-school.md` | U.S. News ranks (Windham Middle 4th, Windham High 8th; read in Chrome), Algebra I in 8th grade against neighbors, homework by course level, AP results and dual enrollment, UMass and UNH credit rules, graduation moving to the Tsongas Center in 2028 (weather, not the turf), robotics team 3467, laptops (not Chromebooks) at WHS, the phone rule, sports (58 teams in 30 sports), no participation fee, FAFSA help, the 7:52 start, ELOs | 12 | 84 | 4 | 61 MB |
| `student-support-and-getting-to-school.md` | Salem and Pinkerton CTE for Windham students (no plumbing; engineering at Salem only; a 6:45 a.m. bus), Windham Woods School ($54,500, not on the state's approved list), finishing the year after a move (policy JFAB), translated notices, home education access and the outdated policy IHBG, bell times, snow procedures, no late bus, counselors and the 504 coordinators, the 2026-27 calendar | 10 | 62 | 3 | 32 MB |
| `money-buildings-and-staff.md` | The FY2027 budget ($72,503,095) and the FY2028 proposal (+3.57%), HB 1300 (58.66% after the recount; the district's own cap analysis), the 2026 tax rate ($14.57, about 79% schools), the 2017 renovation bond ($38,907,102, to 2038), Windham Center's repairs and the failed track bond, special education costs (92% local), spending against neighbors, the Parental Bill of Rights, the teachers' contract and the 2027 vote, paras and counselors, resignations, one SRO and two marshals, substitute and volunteer rules, home values and zoning | 13 | 84 | 8 | 40 MB |
| **Total** | | **47** | **304** | **16** | **190 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.31 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Windham`). All 16 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 31 full, 29 partial. None was answered wholly by earlier files.
- **Topics:** one new topic was added to `../shared-topics.md`, `college-credit-for-ap-and-dual-enrollment` (credit at colleges outside New Hampshire, such as UMass Amherst). Its title was widened from UMass alone to match its description. It doesn't overlap `college-admission-requirements-nh` or `ap-and-ib-exam-fees-and-deadlines`.
- **Places:** `district Windham` 278, `town Windham` 18, `district Windham Woods School` 5, no place 3 (the UMass credit rules).
- **Places for the backend:** none needed. Windham runs every grade, and its CTE options are career-program arrangements, not tuition rows (like Laconia's).
- **Pending facts:** none cite draft minutes.
- **Raw folders:** all under 100 MB.
- **Quotes:** 539 of 759 quoted passages found word for word in the raw copies. Most misses are tables and PDF layout text.
- **Text copies:** on November 21 a mistake in my review script overwrote the agents' text copies of their PDFs. They were restored:
  - the 8 that survived in the agents' scratch folders were copied back;
  - the rest were regenerated from the saved PDFs with each agent's own tools (pypdf, PDFKit, and Apple Vision OCR for scanned pages);
  - the agents' OCR of three handbooks and plans was appended.

  Quote matches went from 532 before the mistake to 539 after.
- **Reconciled in review:**
  - **High school enrollment:** the support file's 873 is the 2026-27 profile's count; the money file's 863 is the district's October 1, 2026 count. The support file now gives both.
  - **The 2027 vote date:** the district's slides and minutes say March 10, 2027, a Wednesday. Its own calendar closes school for the local election on Tuesday, March 9, the second Tuesday, and the 2026 vote was on March 10, 2026, so the slides likely carried last year's date. The money file's fact now says so.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | FY2027 budget $72,503,095 | The district's HB 1300 hearing slides, October 20, 2026 |
  | The 2017 renovation article, $38,907,102 | The 2017 school district report |
  | Question 2 recount, 4,460 to 3,143, still short of 60% | The moderator's and clerk's signed tally sheet, November 14, 2026 (read as an image) |
  | 2026 tax rate $14.57, local school $10.46 | The town's press release and rate sheet, November 17, 2026 |
  | Windham Woods tuition $54,500 | The school's tuition page |
  | Policy JFAB: K–8 families moving in the last 60 school days may finish the year | The policy text (revised October 21, 2025) |
  | YMCA before-school care at Golden Brook, $70 a week for members | The YMCA's program listing |

## Premises checked

| Question says | What the sources show |
|---|---|
| A Golden Brook preschool lottery (P1.1) | Right; no applicant or waitlist numbers are published |
| A 2:50 dismissal; a YMCA waitlist (P1.2) | Right: 2:50, car pickup from 2:55; the state's child care data show the after-school program taking a waitlist |
| Extra fees for full-day kindergarten (P1.3) | No: kindergarten is the full day at no charge; only preschool has tuition |
| A budget "over $72 million," enrollment "around 2,900" (P2.1) | Right: $72,503,095; the district's own count fell from 3,049 (2021-22) to 2,786 (October 2026) |
| The HB 1300 tax cap (P2.2) | Not adopted: 58.66% after the recount; the district calculates it would have exceeded a cap in each of FY2023–FY2027 |
| Electrical or plumbing at Salem or Pinkerton (P2.3) | Electrical is offered to Windham students; plumbing isn't; seats are limited and waitlists aren't published |
| Windham Middle "near the top" (P3.1) | Right: U.S. News ranks it 4th of 140 (2027 rankings) |
| Nearly $39 million for Golden Brook and the middle school (P4.2) | Right: $38,907,102, approved in 2017, bond to 2038; Windham Center needs about $6.0 million, no bond proposed |
| Windham Woods School (P5.2) | A private school for students with learning disabilities, $54,500; not on the state's June 2025 approved list, and the state's reports page has no Windham Woods report (a newer September 2026 list couldn't be read) |
| Tutor.com for 4th graders (P6.2) | Right: free for grades 4–6 |
| Finishing the year after a move (P6.3) | Only if the family moves in the last 60 school days (90 for high school); otherwise the board decides |
| Graduation moving off-site in 2028 (P7.2) | Right: to the Tsongas Center in Lowell, for weather; the turf is being replaced because it's worn out |
| $19,690 per pupil (P8.1) | Right (FY2025); Salem $19,752, Pelham $20,212, Londonderry $21,196 |
| Recess and buses after the move to Windham Center (P9.3) | Recess continues (15 minutes daily); the day starts earlier |
| 1:1 Chromebooks (P11.2) | Chromebooks in grades 1–8; Windham High uses Apple laptops |
| 30 varsity teams (P12.1) | Sources differ: 30 varsity teams (profile), 58 teams in 30 sports (plan) |
| Athletic fees (P12.2) | No participation fee found |
| Annual homeschool paperwork (P13.2) | Repealed in state law from July 1, 2026, though policy IHBG still describes it |
| Tiered busing (P14.1) | Start times differ; no document calls the buses tiered |
| A late bus (P14.3) | None found |
| An early start (P15.3) | 7:52 a.m.; no board discussion of changing it since July 2023 |
| A nearly 900-student high school (P16.1) | Right: 873 (profile) or 863 (October 1, 2026) |
| SROs and marshals full-time at Golden Brook (P17.2) | One police SRO for all four schools and two district-wide marshals |
| About 65% proficient in math (P18.1) | Right: 65% (2025), 66% (2026) |
| A recent change in reading (P18.2) | Right: Wit & Wisdom replaced Lucy Calkins in 2024-25, with Fundations and other phonics programs |
| $730K+ homes (P19.1) | Right: Zillow's typical value is about $787,000 |
| The same four schools for every address (P19.2) | Right |
| School tax jumps (P19.3) | The 2025 revaluation cut the rate from $22.64 to $14.15; 2026 is $14.57 (+3%) |

## Corrections and additions to earlier files

- **Salem** (`high-school-and-cte.md`):
  - school-programs-after-grade-6 13 now notes that Windham High's 2026-27 Program of Studies lists five dual enrollment courses, without Biotechnology I.
  - high-school-outcomes 8 notes that the improvement plan's AP 3+ shares (72, 85, 85) differ slightly from the profile's.
- **Londonderry** (`buildings-and-staff.md`, town-housing 1) now notes that Zillow revised Windham's September 2026 value to $786,762.

Salem and Londonderry are loaded locally, so the folders were re-synced.

## The site's data

- `recommended-improvements.md` A8, item 8: Windham's Question 2 rows still have election night's 4,461 to 3,144. The recount gave 4,460 to 3,143. The outcome is the same.

## Library notes (for review, not applied)

- The kindergarten table in `district-practices.md` lists Windham's kindergarten day length as "not found." The elementary file has it (kindergarten-day-length 1).

## Browser pass (November 21, 2026)

- **Read in Chrome and added:**
  - U.S. News's pages for Windham Middle (4th of 140) and Windham High (8th of 84);
  - NH DOE's approved private special education programs page and its reports page.
- **Still not retrieved:**
  - NH DOE's September 17, 2026 approved programs list and its tuition and transportation report (PDFs on a site that refuses automated requests; Chrome can't read PDFs);
  - bus routes (behind the MyPowerHub login);
  - menus (a JavaScript app);
  - individual job postings;
  - the YMCA's waitlist length;
  - the FY2028 default budget and 2027 warrant (not posted yet).
