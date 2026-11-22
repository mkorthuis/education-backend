# Epsom: Research for Ask NH Education Facts

Cited facts and figures for answering Epsom, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 21, 2026, in the fourth wave of the second ToLoad batch. Epsom is in SAU 53 with Pembroke, Allenstown, Chichester and Deerfield:
- **Epsom Central School** serves kindergarten to grade 8.
- **High school:** students attend Pembroke Academy as an AREA town (a few attend Prospect Mountain), and may take career programs at the Concord Regional Technical Center (CRTC).

The district votes by official ballot. SAU 53 and Pembroke Academy were researched in `../Pembroke/`; these files cite them and add Epsom's side.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `epsom-central-early-grades-and-families.md` | Full-day kindergarten (8:20–3:05, no fee posted), the Boys & Girls Club's care at the school (from 6:00 a.m. and to 5:30 p.m.; $60 and up to $85 a week; open on snow days), math scores (29–31% in 2022-24, 43% in 2025-26; named for gains in 2026), UFLI phonics and Wonders, seven Dail routes (26–32 minutes), class sizes, no public pre-K, storm calls | 13 | 62 | 2 | 65 MB |
| `epsom-central-upper-grades-support-and-choices.md` | No shop class (VEX robotics and engineering labs instead), contracted part-time speech services, two counselors and a psychologist, no late bus, JJJ (October 2026) for home-educated and EFA students, 12 students taking VLACS algebra or languages, no private school in Epsom, open enrollment elsewhere (Epsom pays up to 80%), how EFAs affect state aid | 12 | 81 | 1 | 66 MB |
| `pembroke-academy-from-epsom.md` | No Epsom bus to Pembroke Academy (a $1 budget line; bus articles failed three times), Coe-Brown only by private tuition or a hardship or best-interest placement, PA's size (744), NHTI courses at $150 each, welding at the CRTC (no diesel), the NHIAA rule on travel teams, Epsom scholarships | 12 | 45 | 2 | 6 MB |
| `money-and-governance.md` | The local school levy ($5.19 million in 2014, $11.20 million in 2025), about 540 resident students (378 at the school), SAU costs about 2.2% of the budget, the AREA agreement (state withdrawal process; a case at the NH Supreme Court), the 2026 budget (567 to 341; the default took effect four of five years before), PA tuition ($21,159.22 for 2027-28), the roof ($124,000 from surplus; no debt), para pay ($17.55–$22.53) | 8 | 82 | 1 | 31 MB |
| **Total** | | **45** | **270** | **6** | **168 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.11 million tokens.

## Checks

- **Parser:** all four files pass the backend's parser (`tools/check_town.sh Epsom`). All 6 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 38 full, 22 partial.
- **Topics:** no new topics.
- **Places:** `district Epsom` 223, `district Pembroke` 20, `town Epsom` 15, `sau 53` 7, `district Coe-Brown Northwood Academy` 2, `district Concord` 1, no place 2.
- **Pending facts:** 45, citing the draft minutes of June 25 and November 10, 2026 (the board posts minutes as drafts until approved).
- **Raw folders:** each under 100 MB.
- **Quotes:** 597 of 681 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | The 2026 budget, 567 to 341 | The 2026 election results (scanned) |
  | PA tuition, $21,159.22 | The November 10, 2026 budget packet |
  | The roof, $124,000 | The June 25, 2026 draft minutes |
  | Para pay from $17.55 | The support staff contract (transcribed) |

## Premises checked

| Question says | What the sources show |
|---|---|
| No care before or after school (P1.1) | Wrong: the Boys & Girls Club runs care at the school |
| Low math scores (P2.3) | True for 2022-24; 43% in 2025-26, near the state's 44% |
| No public pre-K in Epsom (P8.3) | Mostly right: none at the school |
| Special education short-staffed (P3.1) | Speech is contracted part-time; no missed services reported |
| A late bus (P6.1) | None |
| A full-time counselor (P14.3) | Two counselors and a psychologist |
| Cornerstone Christian on Black Hall Road (P15.1) | No private school operates in Epsom |
| Vouchers cost the town (P13.1) | EFAs come from the state's trust fund; aid drops only when a student leaves the school |
| Coe-Brown instead of PA (P5.1) | Only by private tuition or a hardship or best-interest placement |
| An 850-student PA (P5.2) | 744 in 2024-25 |
| An early bus to PA (P7.1, P16.1) | Epsom runs no high school bus |
| Dual enrollment free (P7.2) | NHTI charges $150 a course, with waivers |
| Diesel at the CRTC (P19.1) | Welding yes, diesel no |
| About 380 students (P4.1) | 378 at the school; the district pays for about 540 |
| Locked in to PA forever (P4.3) | No: the state's AREA withdrawal process applies |
| A roof or HVAC bond (P10.2) | None; no debt |

## Corrections and additions to earlier files

- **Pembroke** (`../Pembroke/`):
  - SAU 53's costs are split half by pupils and half by property value.
  - PA's AP results (95% at 3 or higher) appear in its October 2025 AREA presentation.
  - Pembroke Hill posts cancellations "prior to 7:00 am," while Epsom's handbook says 6:30 a.m.

## Library notes (for review, not applied)

- **Epsom fact 28** says the PA arrangement "may be an AREA agreement; not confirmed." Epsom's 2026 Article 3 calls Pembroke Academy "its AREA High School."
- **`kindergarten-day-length` and `kindergarten-registration`:** this research fills their "not found" entries for Epsom.

## Browser pass

Not needed for the answers. The agents' blocked pages were:
- the Epsom library and the town's files (HTTP 403 or "Access denied");
- the NH Supreme Court opinion;
- Coe-Brown's admissions page.

The Supreme Court ruling is expected in December.
