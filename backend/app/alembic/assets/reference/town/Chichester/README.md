# Chichester: Research for Ask NH Education Facts

Cited facts and figures for answering Chichester, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch. Chichester is in SAU 53 (with Epsom, Allenstown and Pembroke):
- **Chichester Central School** (kindergarten to grade 8; 238 students in August 2026, 35 of them kindergartners), run by the Chichester School District, which has no deliberative session and votes at a traditional March meeting;
- grades 9–12 go to **Pembroke Academy** under the Pembroke Academy AREA agreement (the agreement's text isn't posted), with the Concord Regional Technical Center (CRTC) for career programs.

Pembroke's, Epsom's, Allenstown's and Concord's research was already done; these files cite it and write Chichester's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `chichester-early-grades-and-families.md` | The Learning Tree (Epsom) as the only listed after-school care (its page still says 2025-26), four bus routes of 31 to 45 minutes from the first stop with no separate kindergarten bus, PickUp Patrol's 1:00 p.m. cutoff for bus changes, delay times not posted, lunch $2.70 or $2.90 with free or reduced meals by application, no public pre-K, a library media specialist (certification not stated), kindergarten registration (17 enrolled in a week, 35 in August) | 12 | 55 | 3 | 7.2 MB |
| `chichester-grades-5-8-support-and-choices.md` | Grade 8 math 50% and reading over 90% against 40% and 51% for the state, one science teacher and no world language, speech therapy on the roster and occupational therapy on the staff page only, $562,355 budgeted for out-of-district placements (2026-27), phones off bell to bell (JICJ), robotics from early 2026, homeschoolers under policy JJJ, Bishop Brady and St. John's with EFAs | 15 | 66 | 5 | 7.9 MB |
| `pembroke-academy-from-chichester.md` | Chichester's own morning bus to the Academy (24 stops, first at 6:02, arriving 7:15; no afternoon or late run posted; cut proposed December 2025), the CRTC's 13 programs with no heavy equipment, diesel, agriculture or forestry (the nearest are at White Mountains Community College and the Winnisquam center), Strong Foundations only K–8, the 2020 CRTC program book, scholarships for Chichester seniors, Concord Area Transit and Mid-State Transit | 10 | 41 | 3 | 1.4 MB |
| `money-and-governance.md` | FY2627 passed 57–24 at $8,504,806 (2.87% against a base that included trust transfers; 5.2% like for like, derived), the FY2728 draft of $9,134,065 (+5.4%), Pembroke tuition of $1,142,951 (13.4% of the operating budget; $18,434.70 a student against Concord High's $21,043.15 and Coe-Brown's $21,617), the school part of the rate ($11.57 in 2025; $12.54 estimated for 2026), Question 2 at 59.8% (three votes short of 60%; recount November 18), a $9.5 to $10 million five-year capital plan for March 2027, no budget committee formed | 13 | 62 | 8 | 0.5 MB |
| **Total** | | **50** | **224** | **19** | **17 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.5 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Chichester. All 19 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 23 full, 36 partial, 1 none (P19.3: the time children are expected at the bus stop on a two-hour delay isn't posted).
- **Topics:** no new topics.
- **Places:** `district Chichester` 186, `town Chichester` 17, no place 6, `district Pembroke` 6, `district Concord` 4, `district Winnisquam Regional` 2, `sau 53` 1, `town Concord` 1, `town Berlin` 1.
- **Pending facts:** 19. The loader counts any note that contains "draft" or "pending"; nearly all cite the board's unapproved October 21, 2026 minutes or June 18, 2026 draft minutes, or the draft MS-26, and say so in the note. Check them before loading.
- **Raw folders:** each under 100 MB. The 28 saved PDFs are handbooks, policies, a budget (a scan with a transcription of the pages used), the CRTC's 2020 program book and state sheets. None is a roster. The bus sheets are kept as cleaned copies with house numbers removed.
- **Privacy:** the address scan finds only schools and public buildings. The CRTC's 2020 program book had named student testimonials ("Class of 2021") and two named parents; the main session replaced those 8 names (6 students and 2 parents) with "[student]" and "[parent]" in `raw/high/crtc-program-book-2020.txt` (no fact quoted any of them). The board's staff roster pages with names were not saved. Minutes copies have names removed.
- **Quotes:** 609 of 684 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The school part of the rate in 2022–2025 ($15.61, $11.12, $11.35, and $11.57 in the district's figure; the site's rates add to $11.56 in 2025) | The site's `town_property_tax` table |
  | Question 2: 834 yes and 560 no (59.8%), three votes short of 60% (837 needed) | The site's `town_question_two` table |
  | FY2627 budget vote of 57–24 | The March 7, 2026 district meeting minutes |
  | Pembroke tuition line of $1,142,951 and the "62 students @ $17,434.70" note, whose rate is a misprint | The FY2627 voted budget scan, read as an image (62 × $18,434.70 = $1,142,951; the rate matches the hearing presentation) |
  | The FY2728 draft of $9,134,065, $464,259 (5.4%) above the voted $8,669,806, which included $165,000 of trust transfers | The November 18, 2026 budget packet |

## Premises checked

| Question says | What the sources show |
|---|---|
| A long kindergarten bus ride on back roads (P1.2) | No separate kindergarten bus; the first-stop rider rides 31 to 45 minutes in the morning (derived) |
| Every pickup change in PickUp Patrol by 1:00 p.m. (P1.2, P7.1) | Partly: 1:00 for a change of bus or early dismissal; the handbook gives 2:00 for other changes |
| Art, music and gym with small classes, not cut (P1.3) | All three are taught K–8; music went full time in 2025-26; a full-time art position was taken out of the 2026-27 proposal |
| Locked doors, key cards and cameras (P10.3) | Sign-in and badges; a 2015 camera policy; key cards not found |
| A public pre-K at Chichester Central (P12.1) | None; SAU 53's TLC Preschool in Allenstown serves children with disabilities and some classmates |
| Free lunch for everyone (P7.3) | No: $2.70 or $2.90, with free or reduced-price meals by application (18 of 203 students eligible in 2025-26) |
| A summer reading program (P7.2) | Not found; the minutes mention a "Pirates Camp" summer school in 2024 and 2025 |
| A certified librarian (P18.1) | A library media specialist is on staff (new in 2025-26); certification isn't stated |
| Lab science and a foreign language in grades 7–8 (P3.2) | Inquiry-based science with one teacher, no lab course described; no world language anywhere in the handbook, roster or budget |
| Speech and OT shared with other SAU 53 towns (P5.1) | The speech therapist is on Chichester's roster (1.00 FTE); the OT is on the staff page, not the roster |
| Homeschoolers at soccer and band without enrolling (P9.1) | Yes under JJJ; policy JJI still adds a rule limiting eligibility if a similar sport is offered at the child's own school |
| Yearly homeschool evaluations (P9.3) | None since July 1, 2026; policy IHBG still describes them |
| A late bus after sports at Pembroke Academy (P10.1) | None found; only a morning route is posted |
| The CRTC "still" has agriculture or forestry (P13.1) | Neither is in the 2026-27 list or the 2020 program book |
| Strong Foundations as an option after grade 8 (P10.2) | It serves kindergarten to grade 8 only |
| Chichester has no vote for the Pembroke board (P17.3) | Correct; seats on AREA meetings and an advisory board, and a vote on the tuition line in its own budget |
| The warrant "goes up every year" (P4.1) | The operating budget does ($7.78 million FY2425 to $9.13 million FY2728 draft); the school rate did not (it fell in 2023 after the revaluation) |
| A state school budget cap (P4.2) | HB 1300 was on the ballot: Chichester 59.8%, three votes short of 60%; a recount was scheduled for November 18 |
| Tuition "versus the school building's share" (P2.3) | The district's papers don't split taxes between the Academy and the K–8 building; tuition is 13.4% of the FY2627 operating budget |
| "Cut at the deliberative session" (P11.3) | Chichester has none; floor cuts failed in 2025 (a 9% cut, 55–84) and none was offered in 2026 |
| Leaving the AREA contract (P8.2) | It is an AREA agreement: a withdrawal vote after the third anniversary with a two-year lead time; no study found; text not posted |

## Corrections and additions to earlier files

None applied; nothing found contradicts them. Additions for other files:
- **Pembroke `money-and-governance.md`, district-tuition-contracts 4:** it says 62 students were budgeted for 2026-27, down from 77; Chichester's FY2728 draft budgets 76.
- **Deerfield `district-budget-and-cost` 12:** it lists $26,439 for Chichester's 2024-25 K–8 cost per pupil, a figure the SAU 53 data dashboard gives (as an iReport cost per pupil); the district's own posting says $25,916 and the site $25,210.
- **Allenstown `pembroke-academy-from-allenstown.md`, district-transportation 4:** the 2026-27 Chichester sheet has a 6:02 first stop (2022-23 had 6:04) and the same 7:15 arrival; its note that Chichester's budget lists one high school bus is confirmed.
- **Pembroke `pembroke-academy.md`:** its gap "whether any late or activity bus runs" agrees with Chichester's sources (none found).
- **Epsom's `pembroke-academy-from-epsom.md`:** its manifest hardship case (now at the Supreme Court) bears on Chichester's policy JCA.

## Library notes (for review, not applied)

- **`district-practices.md`:** the kindergarten registration entry for Chichester says "not active yet" for 2026-27; the January and February 2026 newsletter says registration opened with 17 students enrolled in a week, 31 registered by May and 35 kindergartners by August 19.
- **`budget-voter-information` fact 2** (cost per pupil and proficiency scores printed in the warrant from September 8, 2026) will apply to Chichester's March 2027 warrant; the 2026 warrant (posted February 12, 2026) predates it.
- **The RSA 32:10 fact** was added to the library topic `budget-traditional-district-meeting` as a no-place fact in `money-and-governance.md`.
- **Site data:** the account note on the voted budget's tuition line misprints the per-student rate ($17,434.70 for $18,434.70); the district's own posting ($25,916) and the site's NH DOE figure ($25,210) for 2024-25 cost per pupil are the same series 2.8% apart.

## Browser pass

Partly done (November 22, 2026, in Chrome): SAU 53's School Board Minutes folder on Google Drive opened; its 2026-2027 folder stops at the October 21, 2026 draft, and the district page and the town's pages say nothing of the recount, so the November 18 result is still not posted (a search found nothing either). Not retrieved:
- The recount result for Question 2 (held November 18, 2026), the 2026 tax rate (not set), the March 7, 2026 district meeting minutes beyond the Article 9 discussion (a scan), the EEI plan's slide decks, the AREA agreement's text, the SAU 53 data dashboard pages (Wix), the Learning Tree's 2026-27 arrangement and cost, Pittsfield High School's tuition rate (none found);
- bus times on a two-hour delay, a missed-stop procedure, whether the library media specialist holds a state license, what the summer "Pirates Camp" is, the town library's summer reading program, whether any key-card entry exists, and a Chichester student count at charter schools (not found).
