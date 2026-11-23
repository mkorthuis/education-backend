# Plainfield: Research for Ask NH Education Facts

Cited facts and figures for answering Plainfield, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch, after Lebanon's and Grantham's research on the same AREA agreement. Plainfield is in SAU 32, which it shares with the separate Cornish district (Cornish's SAU 100 buys superintendent, business and technology services from it):
- **Plainfield Elementary School** (kindergarten to grade 8, in Meriden; 181 students in 2025-26 and 164 in November 2026, down from 220 in 2020-21), run by the Plainfield School District;
- grades 9–12 go to **Lebanon High School** under the Grantham–Lebanon–Plainfield AREA agreement ($19,344 a student for 2026-27; 81 students budgeted), with the Hartford Area Career and Technology Center for trades; **Kimball Union Academy** (KUA), a private academy in Meriden, is the town's largest taxpayer and its tax-exempt educational property is about 77% of the town's exempt value.

Lebanon's and Grantham's files cover the AREA's terms and Lebanon High; these files cite them and write Plainfield's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `plainfield-elementary-and-families.md` | No preschool at the school (the nearest licensed programs are in Lebanon, about 20 minutes away, derived), a kindergarten cutoff of October 1 ("early admission is not an option"; the registration page says September 30), no before-school program (limited supervision from 7:30), a full-day kindergarten 8:05 to 2:50, lunch $3.80 with paper-only applications, Route 12A and the Lebanon High bus (first pickup 6:15, Lebanon High at 7:00), snow-day coordination with Lebanon that "may" differ, route P6's Meriden Village stops, KUA's rink and theater in set events | 22 | 57 | 5 | 2.5 MB |
| `plainfield-elementary-grades-4-8-and-choices.md` | 181 students against "around 200," one Algebra I class in grade 8 (11 students, all passed; federal 2023-24 data), a math team and an "Extending" math level, three special education teachers, a shared Director of Student Services with Cornish, 17.1% of students with IEPs, the 2026-27 budget moving English learner services to a contractor, the Friday FAST program with Whaleback skiing, devices in advisor caddies until 2:50, Cornish voters rejecting a grades 6–8 tuition deal 91 to 25 | 13 | 82 | 3 | 14 MB |
| `lebanon-high-and-kua-from-plainfield.md` | KUA's $52,500 day tuition with no town discount (the optional tax exemption ended in 2018; "considering" a Plainfield rate), enrolling at Lebanon High by contacting the SAU 32 office first, Hanover High at Dresden's $26,061 tuition with the parent paying it all and no "pay the difference" option, "equal access" to the Hartford center with an undefined "sending school ratios" factor, no late or activity bus, a library Friends scholarship and a dozen awards Plainfield seniors received, Plainfield's own policies JJJ (August 2025: same access and fees for homeschooled students, curricular access limited to half a school day) and IHBG (2021: still describes the repealed notice and annual evaluation steps and a placement evaluation by the principal on re-enrollment) | 16 | 55 | 3 | 2.9 MB |
| `money-and-governance.md` | The 2026-27 budget of $8,761,921 (+0.08%, passed 209 to 66) with the local property tax need up 7.24% because surplus and Cornish revenue shrank, health premiums up 25.4%, 6.5 positions cut, Lebanon tuition of $1,566,864 (17.9% of the budget), Question 2 failing (41.7% yes), the superintendent shared with Cornish since 2017 and extended one year "at the same salary and benefits," the Plainfield-Cornish cooperative study (one K–8 school at Plainfield; first vote March 2027), KUA's exempt property, SAU positions shared 55/45 and 60/40 | 14 | 77 | 7 | 0.5 MB |
| **Total** | | **65** | **271** | **18** | **20 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.3 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Plainfield. All 18 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 26 full, 33 partial, 1 from the site's data (P12.2). One question (P6.3 in the grades 4–8 file) is answered wholly by earlier files.
- **Topics:** two new topics, added to `../shared-topics.md`: `tax-exempt-property-rules` and `seasonal-road-posting-rules`.
- **Places:** `district Plainfield` 196, `district Lebanon` 30, `town Plainfield` 25, `sau 32` 10, no place 7, `district Kimball Union Academy` 3.
- **Pending facts:** 21: the loader counts any note that contains "draft" or "pending"; most cite the November 2026 board packet's draft items, unapproved minutes and draft budgets, and say so in the note. Check them before loading.
- **Raw folders:** each under 100 MB. The 12 saved PDFs are handbooks, an English learner plan and state sheets; four are scans with no text layer, which the agents transcribed. None is a roster. Bus sheets are kept as cleaned text. One image is saved: page 127 of the town report (the principal's enrollment table; it names three staff and no students). Pages of the town report with student names were not saved.
- **Privacy:** the address scan, including the `--raw` pass, finds only the school (92 Bonner Road) and agency addresses. Student, teacher and private resident names are removed from the saved minutes and newsletters.
- **Quotes:** 568 of 669 quoted passages found word for word in the raw copies (the misses are page breaks, hyphenation and OCR errors in the town report, per the agents' own check of 221 quoted strings, and table text read from images).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Question 2: Plainfield 549 to 768 (41.7% yes) | The site's `town_question_two` table |
  | Lebanon tuition: 81 students at $19,344 is $1,566,864, 17.9% of $8,761,921; $19,344 is 2.84% above $18,810 | Arithmetic from the town report's figures |
  | The 2026-27 budget of $8,761,921 as "a 0.08% increase in the expense budget" (and "a decrease of $1,492,677" from the total voted budget with warrants) | The town report's school pages (printed pp. 134–137) |
  | Cornish's vote on the Plainfield tuition deal, 91 to 25 | The Valley News report saved from March 8, 2026 |
  | Enrollment of 220, 211, 207, 198, 183 and 181 for 2020-21 to 2025-26 | The principal's table, read as an image (page 127) |

## Premises checked

| Question says | What the sources show |
|---|---|
| A September 30 kindergarten cutoff with some flexibility (P1.2) | Partly: the registration page says "before September 30th," the 2026-27 handbook "prior to October 1" and "Early admission is not an option" |
| Care for a 7:00 a.m. shift (P1.3) | No before-school program; limited supervision at 7:30 and full at 7:45; the first scheduled bus pickup is 7:02; the principal wrote in September 2026 of the "lack of an afterschool program" |
| The bus up a dirt road in mud season (P5.3) | No PES or SAU 32 mud-season rule found; the sheets show turnarounds, not road surfaces |
| Split classrooms (P7.1) | Partly: grades 3 and 4 share two mixed-grade homerooms; kindergarten, 1, 2 and 5 have their own; grade 5 drops from two classrooms to one |
| Five full days of public kindergarten (P7.3) | Yes, 8:05 to 2:50, with no fee posted |
| School lunches cost money now; an easy way to apply (P10.2) | $3.80 in 2026-27 ($0.40 reduced-price); applications are paper only |
| The bus stops in Meriden Village (P11.1) | Yes: route P6 on Main Street and at KUA Hill |
| PES kids use KUA's fields, rink or theater (P11.2) | Rink and theater, in set events; no source mentions fields |
| A full-time speech therapist and special education on site (P4.1) | Partly: three special education teachers (two also reading specialists), an intervention teacher, a behavior technician and ten educational assistants; speech days on site aren't published |
| Special education run by "someone we share with Cornish" (P4.3) | Yes: the Director of Student Services is on both districts' staff pages |
| "Share a superintendent now" and may combine middle schools (P6.1) | The superintendent yes (since 2017; a new one began November 9, 2026); middle schools no: Cornish voters rejected the tuition deal; the cooperative study recommends one K–8 school at Plainfield |
| A full-time guidance counselor every day (P9.3) | One counselor listed (1.0 FTE federally, about 181 students per counselor, derived); days in the building not published |
| PES may have an ESL teacher (P10.1) | An "ELL Teacher" is on the staff list, but the 2026-27 budget returns to a contracted model (a 0.6 FTE reduction) |
| Trades spots go first to Lebanon kids (P5.1) | No such rule found; the AREA promises "equal access" |
| A late bus for FFA or football (P5.2) | None: athletes provide their own transportation to practice sites |
| Homeschool paperwork goes to the SAU or the state (P13.2) | Since July 1, 2026 no declaration is required except to use public classes or when leaving public school |
| Choose Hanover High "if we pay the difference" (P16.3) | No such option: the parent assumes the whole tuition ($26,061) and Dresden must approve a non-resident |
| The HB 1300 cap and a board override (P3.3) | The cap wasn't adopted (41.7% yes against 60% needed), so there is nothing to override |
| "SAU #32 versus Cornish" costs (P8.1) | Cornish is in SAU 100 and buys services from SAU 32; the superintendent's extension is "at the same salary and benefits" |
| KUA's property is tax-exempt (P8.2) | True: $71.3 million of educational property plus $150,000 of dorm and dining property |
| Lebanon tuition is "fixed" (P8.3) | Partly: a formula with a cap, but the cost depends on how many students attend (72 in 2025-26, 81 budgeted) |
| About 200 students (the brief) | High: 181 in 2025-26, 164 in November 2026 |

## Corrections and additions to earlier files

Applied:
- **Lebanon `money-and-governance.md`, district-tuition-contracts 7:** its note said it wasn't clear whether the "2027" rate row means 2026-27. Plainfield's own 2026-27 budget carries the same $19,344 for 81 students, and Grantham's March 2026 slide calls it the current AREA rate; the note now says so.

Not applied (additions for other files):
- **Lebanon `money-and-governance.md`, table `lebanon_area_enrollment`:** its note says the slide labels years with a single number. The Plainfield annual report's list of 72 Plainfield students at LHS in 2024-25 equals the slide's "2025" value, which suggests the slide's year is the year the school year ends.
- **Lebanon `high-school-and-pathways.md`, district-fees 5:** the handbook's "approximately $90" AP exam fee is below the College Board's $99 fee for 2027 (Bedford's ap-and-ib-exam-fees-and-deadlines 2).
- **Lebanon `elementary-and-families.md`, district-transportation 7 note:** the line on Grantham and Plainfield closing separately is now confirmed from the source (December 2025 newsletter).
- **Grantham `lebanon-high-from-grantham.md`, town-school-options-nearby 3:** it derives 79 KUA day students (339 − 260); KUA's campus life page says "about 75" and the town report puts maximum capacity at 90 day students.

## Library notes (for review, not applied)

- **`district-practices.md` kindergarten-entry-cutoff 88** reports only the registration page's "before September 30th" and notes policy JEB wasn't checked; the 2026-27 handbook says "prior to October 1" and "Early admission is not an option."
- **The library's SAU contact table and the handbook** name www.sau32.nh.gov, which didn't resolve on November 22, 2026; the district's working address is www.plainfieldschool.org. The handbook gives the SAU office as 603-469-3442 and the registration page as 603-469-3250 ext. 263.

## Browser pass

Partly done (November 22, 2026, in Chrome): the district's Policies folder on Google Drive opened, and policies JJJ (August 27, 2025) and IHBG (June 17, 2021) were read through their `/mobilebasic` views and added as facts 4 and 5 of `district-homeschool-access` in the Lebanon High and KUA file (raw copies in `raw/browser/`). That answers P13.1 and P13.3 for Plainfield Elementary and shows P13.2's policy is out of date. Not retrieved:
- the district's board minutes (a Drive folder), the other policies in the folder (JEB, JH and the rest of sections I and J were listed but not opened), the Town of Plainfield's site (plainfieldnh.gov, HTTP 403: the final 2026 tax rate), the NH DOE page and plainfieldschool.org's bus pages (a bot check, "Client Challenge");
- Plainfield's bus routes and Route 12A times beyond the 2026-27 sheets read, the FAST "Step 2" form with transportation details, counselor and therapist days per week, application rules for the Philip Read library scholarships, KUA's and Estabrook Christian School's EFA acceptance and Estabrook's tuition, the building's age, roof and boiler, the superintendent's contract, the 2027-28 budget and AREA rate, teacher turnover counts, winter drive times and snow-day counts (not found).
