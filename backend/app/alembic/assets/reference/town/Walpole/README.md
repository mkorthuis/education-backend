# Walpole: Research for Ask NH Education Facts

Cited facts and figures for answering Walpole, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch, after Charlestown's research on the same cooperative. Walpole is in the Fall Mountain Regional School District (SAU 60), a five-town cooperative (Acworth, Alstead, Charlestown, Langdon and Walpole) whose board meets in Langdon:
- **Walpole Elementary School** (pre-K to grade 8 in the Walpole attendance area; grades 2–8 at 8 Bemis Lane from 2026-27 after North Walpole School's grades 2–4 moved in on a March 23, 2026 vote; 277 students pre-K to grade 8), and **Walpole Primary School** (pre-K to grade 1);
- **Fall Mountain Regional High School** (Langdon; built for about 700 students and running at about 50% capacity), with career programs at the River Valley center in Springfield, Vermont and the Keene center nearby.

Walpole voters rejected leaving the cooperative on March 10, 2026 (336 to 440). Charlestown's files cover the district's shared schools and money; these files cite them and write Walpole's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `walpole-primary-and-families.md` | North Walpole School's grades 2–4 already in Walpole Elementary (the building is "not formally closed"; the October 26, 2026 forum was real), Route 4 mornings up to 35 minutes (derived), Drewsville in the Walpole attendance area (Route 3, scheduled at 40 minutes), no school-run care (Walpole Village School's 7:30–4:00 day is for ages 2–5; Home Away From Home posts no hours), a morning Preschool (age 3) and Pre-K (age 4) new for 2026-27 with no lottery or first-come rule posted, the library's weekly Wiggle Time and Story Time, Hooper Institute as a Town of Walpole program, 2026 summer meal sites in Alstead and Charlestown only | 17 | 58 | 1 | 9.8 MB |
| `walpole-elementary-support-and-choices.md` | "Walpole Middle School" not being a school, grade 8 math at 41% in spring 2026 (Keene Middle 32%, Hanover's Richmond School 68%, state 40%) and all-grade math falling from 45% (2024) to 35% (2026), 1.5 FTE special education teachers and 6 paraprofessionals in the FY28 proposal, a 1.0 FTE counselor plus 0.5 FTE shared with the Primary School, the 2026-27 EFA cap reached, homeschoolers' access allowed by law, a link still to the 2021 notification form | 16 | 81 | 9 | 23 MB |
| `fall-mountain-high-from-walpole.md` | Keene's career center closer to Walpole (15.8 miles, 24 minutes) than the high school (23.4 miles, 39 minutes), agriculture and shop classes continuing (animal science expanded in June 2026), River Valley's seats limited to current juniors and a $143,436 amendment passed 116 to 71, a derived table of graduates' plans, teacher pay against Keene and River Valley, policies on credit for returning homeschoolers, tuition students and advanced courses, Walpole's capital reserve ($305,246) and a FY27 tax estimate of +$74.02 per $100,000 | 13 | 43 | 4 | 0.3 MB |
| `money-and-governance.md` | The North Walpole building costing $66,828 for FY27 and $72,156 for FY28 (draft), the withdrawal plan's table that doesn't add up (lines $8,577,839, printed total $7,947,217), local school tax up 58% from 2014 to 2025 while resident students fell 15% (derived), adequacy aid of $3,213 a pupil against Charlestown's $8,571, the Cooperative Review Committee with no plan yet (up to 18 months), board meetings all in Langdon, the school budget voted by ballot | 8 | 66 | 10 | 5.3 MB |
| **Total** | | **54** | **248** | **24** | **38 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.4 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Walpole. All 24 tables are linked to a topic.
- **Coverage:** 57 of 60 questions have facts: 16 full, 41 partial, 3 none (P10.3, P11.1 and P11.2: no source on what buyers say about the schools). Two questions (P6.2 and P14.1 in the high school file) lean on Charlestown's file.
- **Topics:** no new topics.
- **Places:** `district Fall Mountain Regional` 219, `town Walpole` 25, `sau 60` 3, no place 1.
- **Pending facts:** none flagged (the agents reworded notes that merely quoted "draft").
- **Raw folders:** each under 100 MB (middle is 23 MB). The 21 saved PDFs are handbooks, supply lists, a summer newsletter, a budget and state sheets; several are scans the agents transcribed. None is a roster. Bus sheets are saved without house numbers; minutes are excerpts with resident and student names removed. Five page images are saved: the FY27 budget by location, three library flyers and the Hooper Camp flyer.
- **Privacy:** the address scan, including the `--raw` pass, finds only the food shelf in Charlestown and the high school's address.
- **Quotes:** 511 of 653 quoted passages found word for word in the raw copies (the misses are mostly budget and minutes tables read from images and the agents' own wording).
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Local school tax of $4,766,290 (2014) and $7,513,728 (2025), up 58%; resident students from 419 to 355 | The site's `town_school_tax` table |
  | Walpole voters rejecting withdrawal 336 to 440, and the district 580 to 1,929 | The saved 2026 voting results (the YES row with 336 and 580 and 23.12%) |
  | Question 2 in Walpole at 54.5% (Charlestown 68.0%) | The site's `town_question_two` table |
  | Adequacy aid of $3,213 a pupil against $8,571 | The district's proposed 2026-27 apportionment as described in the file's notes |

## Premises checked

| Question says | What the sources show |
|---|---|
| A North Walpole School closing (P4.1) | The October 26 forum was real, but grades 2–4 already moved to Walpole Elementary (board vote March 23, 2026); the building is "not formally closed" and a district-wide vote is expected in March 2027; North Walpole School is at 17 Cray Road, not Bemis Lane |
| Walpole leaving the cooperative (P6.3) | Hypothetical: the withdrawal article failed March 10, 2026 (336 to 440 in Walpole); a new withdrawal would need a three-fifths vote in Walpole only since October 8, 2026 |
| Ag and shop classes are being cut (P6.2) | Wrong: they continue and the board reported expanded animal science in June 2026 |
| A River Valley or Keene center (P20.1) | River Valley is in Springfield, Vermont and the Keene center is a different school; River Valley enrollment was limited to current juniors and the FY28 version dated November 9 lists $0 |
| "Walpole Middle School" | Not a school: Walpole Elementary has grades 2–8 in 2026-27; the brief's "grades 2–8, 123 students" was grades 5–8 in 2024-25 |
| Free meals | Need a yearly application |
| Weather early-release notices | They came the evening or afternoon before |
| EFAs | Open to more families but the 2026-27 cap was reached |
| Homeschoolers at soccer and band | Allowed by law |
| A late bus | Not found |
| The Cooperative Review Committee has a plan (P20.2) | No plan yet; it expects up to 18 months and no article for March 2027 |
| Superintendent turnover (P6.1) | Partly right: churn since 2023, but a long run before |
| Board meetings in Walpole (P19.2) | All in Langdon |
| The school budget is voted at Town Hall (P12.3) | By ballot |
| Drewsville is a separate zone | It is part of the Walpole attendance area (Route 3 serves it) |

## Corrections and additions to earlier files

None applied; nothing found contradicts earlier files. Additions for other files:
- **Charlestown `charlestown-primary-and-families.md`, district-transportation 15:** says child care stops need to be more than 2 miles from the school; Walpole's Route 2 sheet lists a stop at Walpole Village School, about 0.7 miles from Walpole Primary.
- **Charlestown `charlestown-middle-support-and-choices.md`:** district-homeschool-access 1–2 says the SAU's Home Education page wasn't retrieved and whether IHBG was revised was not found; Walpole's file reads the page (it links NH DOE's 2021 sample notification form). IHBG-R is still not retrieved. Its district-special-education-services 12 gives STEPS and FOCUS; Walpole's file adds that LEAP is housed at Walpole Elementary.
- **Charlestown `fall-mountain-high.md`, cte-center-programs 9 and 10:** its FY27 slide "8 FMRSD residents, 3 outside" plus 8 equals the 11 juniors in the January 5, 2026 minutes; the January 2026 minutes count 19 in 2025-26 with 11 juniors, which Charlestown's file did not find.
- **Keene `middle-high-and-career-center.md` and Swanzey `high-school-and-career-center.md`:** the center's seat shares (22% for SAU 60) and March 31 deadline are in Swanzey cte-center-programs 6; Keene's says students apply in February of sophomore year.
- **Charlestown `money-and-governance.md`, district-sau-governance 8:** the March 23, 2026 vote is the same vote as Walpole's district-classrooms-and-staff 1.

## Library notes (for review, not applied)

- **`district-practices.md` district-preschool 29** says no Fall Mountain preschool page was found; Walpole's 2026-27 Preschool and Pre-K notice (district-preschool 1–2 in Walpole's primary file) fills it. The library's `school-staffing-and-class-size` 1 and `kindergarten-rules` 4 apply to Walpole.
- **`additional-data/raw/districts/batch-3/fallmtn-policies.txt`** records only that the district's policy page lists sections A to L; the policies are in a Drive folder, with sections I and J listing 54 and 60 documents (including IHBG, IK, IMBC, IHCD, JFAB, JJIC, JLD and JJC used here).

## Browser pass

Not done. Not retrieved:
- walpolenh.us (HTTP 403: the town report, exemptions, North Walpole Village District rates and the Recreation and police pages), the NH DOE gifted-report page (403), the Walpole old Google Site (sign-in), a UNH-hosted Walpole town report (403), the Walpole Enrollment Trends PDF (Drive download disabled), the counseling scholarship page (sign-in), and the withdrawal committee's reports on SAU 60's Drive (read only for their high school parts);
- the November 9 board decision on the North Walpole building (not posted), kindergarten and grade 1 class counts, a coat or boot closet, Home Away From Home's and Cheshire Medical Center's child care hours and rates, school bell times and a Walpole-specific lockout procedure, Hooper Camp prices, how students travel to career centers, Fall Mountain's bell and departure times, lab equipment age, teacher turnover data, Fall Mountain's tuition rate for non-member towns, what LEAP is, whether Walpole offers Algebra I or any gifted program, the 2026-27 handbook (only an August 2024 scan was found), what buyers say about the schools, and reasons for leader turnover (not found).
