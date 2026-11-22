# Loudon: Research for Ask NH Education Facts

Cited facts and figures for answering Loudon, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the second wave of the second ToLoad batch. Loudon's students attend the Merrimack Valley School District (SAU 46), shared with Boscawen, Penacook (Concord), Salisbury and Webster:
- Loudon Elementary School (LES), in Loudon: K–5;
- Merrimack Valley Middle School (6–8) and High School (9–12), both in Penacook. High schoolers may take career programs at the Concord Regional Technical Center (CRTC) or the Winnisquam Career Center.

The district decides its budget at an annual meeting; an SB2 petition failed in March 2026. These files are the first research on Merrimack Valley; Boscawen's research follows and cites them. District facts are placed `district Merrimack Valley` and serve all five towns.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `loudon-elementary-and-families.md` | The 9:00–3:30 day and why (the same five buses run middle and high school first), the YMCA's care at LES (7:00–8:45 and to 6:00), kindergarten (45 children), no gifted program, paras and contracted aides, DonorsChoose, no public pre-K in Loudon (Boscawen and Penacook only), 2026 scores against Concord, the special education audit | 17 | 68 | 4 | 26 MB |
| `support-and-choices.md` | Middle and high school buses (pickups 6:20–6:29; two routes at 65 minutes), the phone ban (off and out of view; three-day confiscation), EFA and homeschool access (the handbook's free access against the board's fee vote), Benjamin Franklin Academy and Strong Foundations, open enrollment with none paid out, IEPs into 6th grade, the Learning Center | 10 | 76 | 2 | 19 MB |
| `middle-and-high-school.md` | CRTC seats (no Concord priority found; new welding), internships for credit, no middle school late bus, ten AP courses (88% scored 3 or higher), NHTI's six free credits for 2026 graduates, six diploma pathways, the Class of 2026's plans (42.5% four-year college), CRTC tuition ($407,179) | 8 | 75 | 3 | 13 MB |
| `money-and-governance.md` | The 1965 Articles (operating costs by students; capital by value; Loudon 28.66% and 36.12%), Loudon's $10,931,254 assessment, K–5 to stay in Loudon (two-thirds vote to change), the 2026 votes (budget 352–104; SB2 158–310), buses kept in-house (6–5), out-of-district costs, no bonds, the elderly exemption, NASCAR weekend dates | 13 | 100 | 6 | 42 MB |
| **Total** | | **48** | **319** | **15** | **100 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.18 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Loudon`). All 15 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 28 full, 30 partial, 2 from the site's data.
- **Topics:** no new topics.
- **Places:** `district Merrimack Valley` 285, `town Loudon` 25, `sau 46` 3, `district Strong Foundations Charter School` 3, `district Benjamin Franklin Academy Chartered Public School` 2, `district Concord` 1.
- **Pending facts:** none.
- **Raw folders:** each under 100 MB. The bus route sheets name drivers, home addresses and some students, so only summaries without them are kept; one saved route file was deleted.
- **Quotes:** 704 of 860 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The SB2 petition, 158 to 310 | The March 5, 2026 annual meeting minutes |
  | Loudon's shares, 28.66% and 36.12%, and $10,931,254 | The district's tax rate slides and 2026 annual report |
  | CRTC tuition, $407,179 | The 2026 annual report |
  | Pickups from 6:20 | The bus route summaries and the November 2, 2026 board packet |

## Premises checked

| Question says | What the sources show |
|---|---|
| A 9:00 start (P1.1, P12.1) | Right: doors at 8:45, school 9:00–3:30 |
| No care at the school | Wrong: the YMCA runs care at LES |
| High school at 7:30 (P12.1) | First period is 7:45 |
| Gifted pull-out groups (P5.2) | None |
| Public pre-K in Loudon (P15.1) | None; the preschool is at Boscawen and Penacook |
| Combined classes (P17.2) | None found |
| Concord students get "first dibs" at CRTC (P2.1) | No priority found |
| Study halls instead of internships (P2.2) | Both exist |
| A late bus (P4.2) | None at the middle school |
| MVHS pushes four-year college (P10.1) | 42.5% planned four-year college; 36.1% planned to work |
| About 250 at LES (P3.1) | 243 (240 in October 2026) |
| Paying more because of property values (P3.2) | Mostly not: about 98.5% is split by students |
| Closing a small school (P3.3) | For Salisbury and Webster, discussed; not Loudon |
| ESSER-funded staff (P14.2) | No source shows it |
| No school tax break for seniors (P16.3) | The elderly exemption lowers the whole bill |
| A parking and traffic mess in Penacook (P11.3) | No source describes one |
| Phones "locked up" (P8.2) | Banned, but kept off and out of view |
| Losing EFA students' state money (P6.3) | Partly: aid follows enrolled resident students |
| EFA students barred from sports or band (P6.1) | No: HB 1817 and the handbook allow them |

## Corrections and additions to earlier files

- **Concord** (`../Concord/`): consistent with its Merrimack Valley facts. Concord's and Belmont's files list Merrimack Valley as a CRTC and WiCC sending school, which MVHS's profile confirms.
- **The district's budget page** has an explainer whose figures conflict with the official documents (a "$98,450,000" budget; "We contract with First Student"). No fact uses it, and Boscawen's brief warns against it.

## Library notes (for review, not applied)

- **`budget-form-and-vote-dates` 86 (Merrimack Valley)** and its "To recheck next cycle" line say the 2026 SB2 petition's result wasn't found. It was defeated 158 to 310 on March 5, 2026.

## Browser pass

Not needed for the answers. The agents' blocked pages were:
- Niche, NH DOE's charter and ESSER pages, and Governor and Council items (HTTP 403);
- the 2026-27 Program of Studies and science curriculum (sign-in only).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- The state's resident birth, marriage and death lists removed from 1 saved town report copy (headings and record counts kept); 1 report PDF deleted.
