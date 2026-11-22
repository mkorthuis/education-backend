# Charlestown: Research for Ask NH Education Facts

Cited facts and figures for answering Charlestown, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the ninth wave of the second ToLoad batch. Charlestown is one of five towns in the Fall Mountain Regional School District, SAU 60:
- **Charlestown Primary** serves preschool to grade 4, and **Charlestown Middle** grades 5–8.
- **Fall Mountain Regional High** in Langdon serves the five towns. Its fuller trades programs are at Keene's Cheshire Career Center.

The district votes by official ballot in each member town. Claremont's Sugar River Valley center was researched in `../Claremont/`, Keene's in `../Keene/`.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `charlestown-primary-and-families.md` | Half-day pre-K for 4-year-olds (fills fast, waiting list), no after-school program found at the school, the district's own buses (a high school run first; 46–74 minute rides), meals by application, summer meals at the library, child care in town (Green Mountain Children's Center moved here), private school options | 18 | 65 | 1 | 27 MB |
| `charlestown-middle-support-and-choices.md` | Paraprofessional cuts at the middle school (two vacant positions; FY27 cut 6 special education positions district-wide), Algebra I Honors possible in grade 8, the 2015 bullying policy, absences (fair week only partly excused), teams for grades 7–8 only, no sports fee found | 12 | 76 | 3 | 23 MB |
| `fall-mountain-high.md` | Woodworking, metals (welding) and ag mechanics at the school, 40 students at the Cheshire Career Center (1 at Claremont), the end of new placements at River Valley in Vermont, 17 college-credit courses taught at the school, AP by demand (2 in 2023-24), Article 12 (no residents out by open enrollment), FFA, the 4:05 late bus (Monday to Thursday) | 8 | 44 | 2 | 7 MB |
| `money-and-governance.md` | Why Charlestown's rate is highest (45.7% of pupils, 29.1% of property value, 36.9% of school taxes; **derived**), the failed 2026 budget (Charlestown 241–631) and $37,218,637 default, the 2020 withdrawal plan Charlestown rejected (905–509), North Charlestown's closing (276–269), the Senior Educational Official in place of a superintendent, the Cooperative Review Committee | 7 | 92 | 7 | 9 MB |
| **Total** | | **45** | **277** | **13** | **66 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 1.96 million tokens.

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Charlestown. All 13 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 29 full, 30 partial, 1 from the site's data. P12.3 (the late bus) was filled by the browser pass.
- **Topics:** no new topics.
- **Places:** `district Fall Mountain Regional` 247, `town Charlestown` 20, `sau 60` 8, statewide 1.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB. The bus route copy has house numbers removed.
- **Privacy:** the main session removed graduates' names from five saved copies of the district's annual reports (2024–2026) and deleted the reports' PDFs and the town report's PDF, whose births, marriages and deaths pages are images. Citations to deleted PDFs now point to the text copies. The address scans find only schools, offices and agencies.
- **Quotes:** 440 of 577 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 default budget, $37,218,637 | The 2026 annual report and deliberative session slides |
  | Charlestown's 2026 vote, 241–631 | The district's 2026 voting results |
  | Charlestown's 2026-27 school tax, $8,922,517 | The October 26, 2026 FY28 budget presentation |

## Premises checked

| Question says | What the sources show |
|---|---|
| Free meals for all | No: families apply every year |
| A bus company | No: the district runs its own buses |
| After-school care at the school | None found |
| A Niche C+ | Not checked: Niche blocked the request |
| A drop-off bottleneck and fix | Not found |
| Paras short at the middle school | Partly: vacant posts were cut |
| Yearly homeschool paperwork | Not found; state law no longer requires it |
| Fair week excused | Only partly |
| Algebra I in grade 8 | Possible, not assured |
| Shop and welding gone, trades only in Claremont | Partly wrong: shop and metals remain; trades at Keene |
| RVCC classes only at the college | Wrong: 17 college-credit courses at the school |
| Few AP courses | Correct |
| Charlestown pays far more | Partly: lowest local cost per pupil of the five towns |
| A default budget | Happened in 2026 |
| North Charlestown closed | Right, for good |
| Leaving Fall Mountain "just talk" | Wrong: studied and voted down in 2019–2020 |

## Corrections and additions to earlier files

- **Claremont** (`../Claremont/`): its preschool fact 7 lists Green Mountain Children's Center at 90 Charlestown Road, Claremont, as SAU 6's page still does. The center says it moved to 509 River Road, Charlestown in fall 2026.

## Library notes (for review, not applied)

- **`district-preschool` 29 (Fall Mountain)** says no preschool page was found; Charlestown Primary's pre-K details are here.
- **`budget-form-and-vote-dates` 39 (Fall Mountain):** its 2026 warrant note ("a scan with no text") can be filled: the 2026 deliberative session was February 2, 2026.
- **Coverage table:** it lists Fall Mountain's kindergarten day, cutoff and registration as not found; this research fills them.

## Browser pass

www.sau60.org shows a bot check to automated requests. The district's own linked home page on its hosting service (sau60nh.sites.thrillshare.com) loaded normally, and agent 4 read board minutes, policies and news posts there.

A second pass in Chrome reached www.sau60.org's Documents page. Its document list (26 documents) is saved at `raw/browser/sau60-documents-index.tsv`, and the late run schedule, a Google Doc linked from the Transportation folder, at `raw/browser/fmrhs-late-run-schedule.txt`. Agent 3 added it as `fall-mountain-high.md` district-transportation 3, which fills P12.3. The route documents list home stops and weren't saved.

Not retrieved:
- the home education page, the counseling pages, board minutes and the handbook on www.sau60.org;
- Niche and NH DOE pages (HTTP 403);
- the district's 2026 annual report on Google Drive (downloads off); the copy on the Town of Acworth's site was used.
