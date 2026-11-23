# Dunbarton: Research for Ask NH Education Facts

Cited facts and figures for answering Dunbarton, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the four files below, in the reference library's format.

Gathered November 22, 2026, in the fourth ToLoad batch. Dunbarton is in SAU 67 (with Bow):
- **Dunbarton Elementary School** (kindergarten to grade 6; 225 students on October 1, 2026), run by the Dunbarton School District;
- grades 7–12 go to **Bow Memorial School** (grades 7–8 for Dunbarton) and **Bow High School** under the Bow–Dunbarton AREA agreement (July 1, 2024 to June 30, 2039, renewed by Dunbarton's voters 128 to 8 in 2022), with the Concord Regional Technical Center for career programs.

Bow's research (Bow Elementary, Bow Memorial, Bow High, the CRTC and the AREA's terms) was already done; these files cite it and write Dunbarton's side. There is no `town/sau67/` folder, so the SAU 67 facts are in these files.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `dunbarton-elementary-and-families.md` | Kindergarten 7:55 to 2:20 (grades 1–6 to 2:25), after-school care run on site by New Morning School of Bedford to 6:00 (no before-school care; families waitlisted in 2025), no public pre-K, delay calls by 5:30 a.m. and early dismissal between 10:15 and 10:30, ParentSquare taking over from other tools with Alma kept for records, the SAU 67 residency declaration and school-meals application, class sizes, town soccer and basketball, foster-care enrollment | 15 | 68 | 2 | 2.5 MB |
| `dunbarton-grades-3-6-support-and-choices.md` | DES at or above the state in every grade and subject and below Bedford, 0.64 grade levels above the 2019 national average (Bow 1.70, Bedford 2.70), a school-wide "WINN" block instead of a gifted program, speech and OT bought in DES's own budget (OT contracted from 2026-27), how an IEP move to Bow Memorial is handled, homeschoolers' and EFA students' access to Bow sports and band (policy AB, AREA section 3.I), the PTO paying for field trips, Dunbarton's own policy JJJ (same access, same fees, appeal to the Superintendent then the Board), no school resource officer at DES | 14 | 67 | 6 | 13 MB |
| `bow-from-dunbarton.md` | Dunbarton students join Bow Memorial in grade 7 (about 24% of grade 7–8 and Bow High students are Dunbarton's, derived), welding added at the CRTC for 2026-27 but no heavy equipment, Dunbarton's contracted buses with no posted routes and no late bus, returning from homeschooling, AP and dual enrollment, Bow High parking ($40 sticker; sophomores wait until February 1, 2027), the phone law, arts next to Concord High, sports eligibility worded differently at Bow Memorial and Bow High | 12 | 63 | 2 | 1 MB |
| `money-and-governance.md` | The tax year 2026 rate ($16.99; local education $11.46; 73.5% of the rate), a 57.7% rise in local school taxes from 2020 to 2026 while DES enrollment fell from 241 to 225, the $11,608,626 budget (passed 147 to 59 at the Saturday district meeting), $4,550,290 budgeted for Bow tuition (39.2%), the HB 1300 cap adopted 1,093 to 639, the AREA's 15-year term and exit steps, the November 2026 capital assessment ($81,285 needed in 2027, $940,074 over 10 years), teacher pay against Bow's, absentee voting for the March 10 officer ballot | 10 | 51 | 7 | 11 MB |
| **Total** | | **51** | **249** | **17** | **28 MB** |

`brief.md` is the brief the research agents worked from. Four agents used about 2.5 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all four files pass the backend's loader, run against the loaded towns plus Dunbarton. All 17 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 30 full, 29 partial, 1 none (P18.2: no source describes trauma-informed training at DES; the files give MTSS, Responsive Classroom and the SAU's crisis-prevention train-the-trainer model, and say no source uses the words "trauma-informed").
- **Topics:** one new topic, added to `../shared-topics.md`: `high-school-student-parking`.
- **Places:** `district Dunbarton` 146, `district Bow` 53, `town Dunbarton` 20, `sau 67` 16, no place 8, `district Concord` 4, `town Bow` 1.
- **Pending facts:** 2, citing draft minutes.
- **Raw folders:** each under 100 MB. The 25 saved PDFs are handbooks, the AREA agreement, budget packets, a teachers' contract, the state's required postings, forms and state data sheets (several are scans with no text layer; the agents transcribed them). None is a route sheet or a roster. DES and SAU 67 post no bus routes.
- **Privacy:** the address scan finds only Bow Elementary, DES, Bow High and USDA's civil rights address in the SAU meals form. Minutes copies have residents', volunteers' and students' names removed. A July 23, 2025 special meeting on after-school care was not saved because its comments name families.
- **Quotes:** 613 of 718 quoted passages found word for word in the raw copies. Of the misses I looked at, the figures and phrases I searched for (the cost per student, the teacher wage schedule, the 2026 rate, the withdrawal vote wording in RSA 195-A:14) are in the raw copies, in OCR or table form.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Tax year 2026 rate of $16.99 (municipal $2.89, county $1.61, local education $11.46, state education $1.03) and a commitment of $12,771,226 | The Department of Revenue's rate sheet, read as an image (page 1 of 4) |
  | Local school taxes of $5,508,832 (2020), $7,449,370 (2024) and $7,932,117 (2025), and the 2024 and 2025 rates of $17.51 and $10.61 | The site's `town_property_tax` table |
  | Dunbarton's HB 1300 cap vote, 1,093 to 639 (63.1%) | The site's `town_question_two` table |
  | $4,550,290 for Bow tuition ($1,464,110 for grades 7–8 and $3,086,180 for grades 9–12) and 39.2% of the $11,608,626 budget | The 2026-27 budget hearing packet; the sum and percentage recomputed |
  | The AREA's 15-year term (July 1, 2024 to June 30, 2039) and the withdrawal question's wording | The AREA agreement text and the saved RSA 195-A:14 |
  | Bow High's $40 parking sticker | The Bow High parking information and sticker form |

## Premises checked

| Question says | What the sources show |
|---|---|
| A "March school ballot" (P7.2, P14.1) | Dunbarton votes its budget at a traditional meeting on a Saturday (March 7, 2026; 147 to 59 on the budget), with a separate March 10 ballot for school officers; voters rejected SB2 (152 to 46). The 2027 meeting is Saturday, March 6 at 9 a.m. Sources show no absentee ballot for the budget vote. |
| Kindergarten at DES may not be full-day (P1.1) | It is a full school day (7:55 to 2:20); one undated parking page still lists morning and afternoon sessions and looks out of date |
| Care "right at DES" (P1.2, P8.3) | After-school care only, on site, run by New Morning School of Bedford to 6:00 p.m.; no before-school care and no supervision before about 7:40 |
| No public pre-K because Bow High has the special-ed preschool (P12.3) | Out of date: SAU 67's special education preschool moved to Bow Elementary for 2026-27; Dunbarton runs no preschool and New Hampshire funds none |
| Buses on dirt roads (P8.1) | Stops are set by the board case by case (two road-end neighborhoods approved in 2025-26); no source says buses enter dirt roads, and no routes are posted |
| Welding and heavy equipment for a 10th grader (P2.2) | Welding yes (new for 2026-27); heavy equipment no, and federal rules bar most such work under 18 |
| A "back-roads" bus and a late bus (P2.3, P16.3) | Dunbarton contracts its buses and posts no routes or times; no late or activity bus at Bow |
| Bow "charges" a rate and Dunbarton has a "say" (P3.3) | A formula, not a negotiated price; Dunbarton voters don't vote on Bow's budget; the agreement gives its board an audit right, a committee invitation, an accreditation trigger and joint meetings |
| The AREA is "locked in for good" (P7.3, P14.2) | A 15-year term; changing it needs both districts' voters; ending it takes a study, plan, State Board review and a majority in the withdrawing district, at least 2 years out; a Bow vote can start but not end it |
| DES enrollment rising with new houses (P10.2) | Not now: 255 in 2022, 225 in 2026; new-home permits fell from 22 (2024) to 4 (2025) |
| A big DES renovation coming (P12.1) | None found; the bond ends August 15, 2028 |
| Accelerated math at Bow Memorial (grades 3–6 file) | A 7th-grade Accelerated Math course is listed on BMS's Dunbarton slides; placement criteria not found |
| DES's speech and occupational therapists may be split with Bow (P5.1) | DES buys its own in its own budget (a speech aide plus contracted services; OT contracted from 2026-27 and in the building one day a week); no document shows Bow's therapists at DES |
| EFA students trying out for Bow middle school sports or band (P6.1) | Allowed: since August 18, 2026 EFA students share the public-school access right (Dunbarton's policy AB lists it), and the AREA says Dunbarton's home schooled students take part at Bow on the same terms with no home-school-only charge; Bow's own practice of a participation fee is in Bow's file |
| Trauma-informed training at DES (P18.2) | Not found under that name |

## Corrections and additions to earlier files

Applied:
- **Bow `money-and-governance.md`, district-tax-and-state-aid 10 and the P7.3 premises row:** these gave Dunbarton's February estimate of its 2026-27 local rate ($11.50). The fact's note and the row now add the rate DRA set on October 16, 2026: $11.46 local education, $12.49 with the state education tax.
- **Bow `memorial-and-high-school.md`, district-enrichment-and-advanced-learners 2 and the P3.2 rows:** they said no accelerated math track was found posted for Bow Memorial. Bow Memorial's "Dunbarton Open House" slides list Accelerated Math, 7th Math and Structured Math for grade 7 and Integrated Algebra I for grade 8; the fact, note and rows now say so and that no placement rule is posted. The slides are in Dunbarton's `raw/middle/`.

Not applied (additions for Bow's files):
- **`support-choices-and-daily-life.md`, district-transportation 4:** it quotes Bow's October 2026 minutes ("First Student handles Dunbarton's school buses"), while SAU 67's Dunbarton Routes page names STA New Hampshire and Dunbarton's April 2026 minutes name "Goffstown Trucking"; the three sources aren't reconciled.
- **`district-technology-and-phones` 3:** it gives Bow Memorial's phones-away hours as 8:30 to 2:58; the 2026-27 handbook gives the school day as 8:30 to 3:10 (the later source).
- **`district-homeschool-access` 1:** it reports Bow's practice of charging home-educated and EFA students to take part; the AREA agreement's section 3.I says Dunbarton's home schooled students take part in athletics and co-curricular activities with no home-school-only charge.
- **School resource officer:** Bow Police's page says one officer covers Bow High, Bow Middle School and Bow Elementary. Bow's files give no SRO information for Bow Memorial.
- **Concord `buildings-staff-and-comparisons.md`:** its Zillow table reads Bow's September 2026 value at $624,907; the page read November 22 gives $620,116 (Zillow revises past months).

## Library notes (for review, not applied)

- **Site data:** the town gives Dunbarton's 2025 equalization ratio as 95.3% and the site's DRA-based table has 95.71. The site's count for Dunbarton Elementary (234 in 2024-25) differs from the district's October 1 count (236).
- **`high-school-student-parking`:** a new topic here (Bow High's rules); other towns' parents ask about parking passes, so other high schools' facts could be added to it.

## Browser pass

Partly done (November 22, 2026, in Chrome): the Simbli policy manual opened and policy JJJ (access to public school programs for home educated, charter and nonpublic students; adopted December 6, 2023) is now fact 3 of `district-homeschool-access` in the grades 3–6 file (raw copy in `raw/browser/`). Policy JICJ (phones, October 2025) was read but not added: it applies to Dunbarton's own PreK–12 students, and P17.3 asks about Bow High. Not retrieved:
- the rest of the policy manual (IMBC, IHBH, JFABD, EBCD and IHBG were not opened), SAU 67's Canva data dashboard (no text), Bow's Suicide Prevention and Response Plan (Drive 404), Bow High's performing and visual arts department pages (course lists in embedded blocks);
- the Drive files for the September 2026 minutes, the November 2026 DES report and the July 23, 2025 meeting;
- bus routes and times for Bow Memorial and Bow High, a kindergarten sign-up window for fall 2027, New Morning's tuition for Dunbarton, Dunbarton's own benchmark percentages (Acadience and STAR), how Bow Memorial places students in math levels, and any teacher turnover rate (not found).
