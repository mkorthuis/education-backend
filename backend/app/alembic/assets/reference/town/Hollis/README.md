# Hollis: Research for Ask NH Education Facts

Cited facts and figures for answering Hollis, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the third wave of the ToLoad towns. Hollis is in SAU 41 with Brookline:
- **The Hollis School District** runs Hollis Primary School (preschool to grade 3) and Hollis Upper Elementary School (grades 4–6).
- **The Hollis-Brookline Cooperative** runs Hollis-Brookline Middle School (grades 7–8) and High School (grades 9–12).

Both districts decide their budgets at annual meetings. Facts about the cooperative are placed `district Hollis-Brookline Cooperative` and serve both towns. Brookline's own research is in `../Brookline/` and cites these files.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `primary-and-upper-elementary.md` | Bell times (8:23 and 8:30, shared buses), after-school care ($125–$130 a week, first come, first served), the preschool ($270 a month, a January sign-up and waitlist, no busing), full-day kindergarten, the entry cutoff (policy JEB, read in Chrome), class sizes (19–23 at HUES; policy IIB adopted November 4, 2026), enrollment since 2011, screening tiers, scores against Chelmsford and the state, a pre-K research topic | 14 | 80 | 3 | 35 MB |
| `middle-and-high-school.md` | The 7:35 start and shared bus runs, Latin Honors (30% of the Class of 2026), AP waitlists, 712 students, career programs (72 students; Nashua and Palmer seats), AI under teacher guidance, Algebra in grade 7 and Geometry in grade 8, work-study for credit, no late bus, a class rank research topic | 12 | 98 | 6 | 47 MB |
| `support-choices-and-daily-life.md` | Special education transport contacts, the bus contract, gravel roads and turnarounds, religious holidays and chronic absence, early-release Wednesdays and the career-center calendar law (a new topic), renters' residency, snow decisions and blizzard bags, homeschool, charter and EFA access (newer JJJ policies), AP Calculus at ASD | 11 | 86 | 0 | 25 MB |
| `money-and-governance.md` | The failed $19.4 million HPS bond (285–590, needing 525), the renovation committee's options ($8.95 million "Option 1" kept), debt rolling off by FY2031, the cooperative's FY2028 cap-fitting draft (18 job reductions), out-of-district tuition, the cost split (Hollis 57% of taxes, 54% of students), the tax cap vote (59.3%, recount pending), annual meetings, support staff contracts, a current use topic | 8 | 103 | 5 | 49 MB |
| **Total** | | **45** | **367** | **14** | **156 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.29 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Hollis`). All 14 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 29 full, 29 partial, 2 from the site's data.
- **Topics:** four new topics, added to `../shared-topics.md`:
  - `current-use-taxation`;
  - `research-college-admission-factors`;
  - `research-prekindergarten-effects`;
  - `school-calendar-rules`.
- **Places:** `district Hollis-Brookline Cooperative` 157, `district Hollis` 141, `sau 41` 37, `town Hollis` 22, no place 10.
- **Pending facts:** 17, citing draft minutes and the FY2028 drafts.
- **Raw folders:** each under 100 MB.
- **Quotes:** 746 of 871 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, matched):

  | Fact | Checked against |
  |---|---|
  | The HPS bond, 285 yes to 590 no (525 needed) | The Hollis School District's 2026 annual meeting minutes |
  | The cooperative's ballot petition, 216 to 234 | The cooperative's 2026 annual meeting minutes |
  | The preschool, $270 a month | The HPS preschool page |
  | 712 high school students | The 2026-27 HBHS school profile |
  | Option 1, about $8.95 million | The renovation committee's November 16 agenda (cited in the fact) |
  | The tax cap vote, 2,878 to 1,974 | The town's results (cited in the fact; 59.3% derived) |

## Premises checked

| Question says | What the sources show |
|---|---|
| A Hollis Primary renovation voted down in March | Right: 285–590 on March 17, 2026, needing 525 |
| HPS at 8:23, HUES at 8:30 | Right; the same buses serve both |
| Guaranteed after-school spots | None: first come, first served, reapply yearly |
| A preschool lottery | No: a January sign-up, then a waitlist |
| A 3:05 pickup | Classes end at 2:57; pickups after 3:15 go through the office |
| A 7:35 middle school start | Right |
| Latin Honors instead of class rank | Right |
| AP waitlists | They exist; no counts published |
| About 675 high school students | Too low: 712 |
| The AI policy tabled | Right; no reason recorded |
| A late bus | None posted |
| Buses not turning on some roads | No record |
| Hollis Primary at 400 in a building for 340 | 340 was 2011-12 enrollment, not capacity; HPS has 370 (peak 394 in 2023) |
| Extra adequacy aid | No new disparity aid for Hollis; it went to Brookline |
| Brookline growing faster | Its cooperative enrollment has fallen |
| Both districts vote by official ballot | No: annual meetings; a 2026 petition to switch the cooperative failed |
| Support staff contracts through 2028 | Right |

## Corrections and additions to earlier files

- **`questions.md`:** its intro said both districts vote by official ballot; corrected.
- **Hudson and Merrimack:** their counts of Hollis-Brookline students at Palmer and its programs are consistent with this research.


## Browser pass (November 21, 2026)

SAU 41's policy book and minutes load only by script.
- **Read in Chrome:**
  - policy JEB (kindergarten at five by September 30), added as kindergarten-entry-cutoff 1;
  - policy IIB (adopted November 4, 2026), which updates district-classrooms-and-staff 3.
- **The athletic fee** appears only inside Arbiter's registration flow, so it wasn't read.
- **Still not retrieved:**
  - board minutes;
  - Beaver Brook's camps (HTTP 403);
  - Hollis Recreation's program list;
  - NH DRA's 2026 tax rates;
  - NH DOT road miles (HTTP 403).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 11 saved bus and transportation copies (383 in all; schools, child care centers, businesses and other public places keep theirs).
- 5 original route sheets (PDFs, spreadsheets or page images) deleted, with citations pointed to the redacted text copies.
