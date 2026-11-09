# National Comparisons: How New Hampshire Compares

Strategy type 2 (*Ask NH Facts - General Questions and Data Strategy.md*). State-by-state figures for all 50 states, DC and the U.S. wherever the source has them. Gathered November 8, 2026; every figure below was read from a file or page downloaded that day (copies in `raw/national/`).

## Summary

**38 number tables and 2 fact topics.**

| Area | Tables | Source and edition | Latest year |
|---|---|---|---|
| NAEP test scores | 12: grades 4 and 8, math and reading; average score, % at/above NAEP Proficient, % at/above NAEP Basic; 2024 with 2022 and 2019; NAEP's own "vs NH" and "change since 2019 / 2022" significance flags | NAEP Data Service (NCES), NAEP 2024 | 2024 (tested Jan–Mar 2024) |
| NAEP science | 1 (national only) | NAEP Data Service, NAEP 2024 | 2024; NAEP published no state science results |
| State "proficient" bar on the NAEP scale | 4 (grade 4/8 reading/math) | NCES 2026-014 (Yee & Cramer, Feb. 2026) and its Technical Notes | 2021-22 state tests, NAEP 2022 |
| Graduation rate (ACGR) | 2: class of 2023 by group (ED Data Express); class of 2022 by group (Digest 219.46) | ED Data Express SY2022-23; NCES Digest 2023 | Class of 2023 |
| Students by race/ethnicity | 1 | NCES Digest 2023, Table 203.70 | Fall 2022 |
| Pupils per teacher | 2: NCES (Digest 208.40) and NEA | Digest 2023; NEA Aug. 2026 | Fall 2022 (NCES); 2024-25 (NEA) |
| School spending and revenue mix | 2: current spending per pupil (with instruction and support services) and Census rank; revenue shares | Census Annual Survey of School System Finances, FY2024 (released May 2026) | FY2024 |
| NEA Rankings & Estimates | 3: average teacher salary (2024-25, rank, 2025-26 estimate); current expenditure per student; state/local/federal revenue shares | NEA, August 2026 update | 2024-25 (2025-26 estimates) |
| Starting teacher salary | 1 | NEA Teacher Salary Benchmark 2024-25 (April 2026) | 2024-25 |
| State-funded preschool | 1 (% of 4- and 3-year-olds, enrollment, state $ per child, no-program states) | NIEER State of Preschool 2025 (April 2026) | 2024-25 |
| Public college funding | 1 (education appropriations per FTE) | SHEEO SHEF FY2025 (April 2026) | FY2025 |
| Public college tuition | 1 (4-year in-state and out-of-state, 2-year in-district) | College Board, Trends in College Pricing **2026** (Nov. 2026) | 2026-27 |
| Where new college students go | 1 | NCES Digest 2023, Table 309.20 | Fall 2022 |
| Chronic absenteeism | 1 | AEI Return to Learn tracker / AEI report (June 2026) | 2024-25 (NH: 2022-23 only) |
| Youth health (YRBS) | 5: sad or hopeless; considered suicide; bullied at school; bullied electronically; missed school because unsafe — NH vs U.S. | CDC YRBS Explorer | **2025** (with 2023, 2021, 2019) |

Fact topics: `naep-vs-state-tests` (how to read NAEP next to state test results, and why "significantly different" depends on the comparison) and `chronic-absenteeism-nh-data` (why NH's absenteeism figures are thin).

**Biggest gaps** (details in *Not retrieved*):
- **Chronic absenteeism:** no New Hampshire rate after 2022-23 anywhere we found. NH's figures come from AEI's estimates built on federal counts; ED Data Express's newest state file is 2021-22 and has counts, not rates. The AEI tracker is research, not an official statistic.
- **NCES Digest tables** for race/ethnicity, pupils per teacher, graduation by group and college migration are still the 2023 edition (fall 2022 or class of 2022). NCES's "current tables" list confirms no newer version. Graduation by group is newer in ED Data Express (class of 2023), but no 2023-24 state file is listed.
- **NAEP 2024 science** has national results only, no states.
- **NH YRBS from NH DHHS** (regional reports) was not reachable (403); CDC's YRBS Explorer has NH statewide results through 2025, used here.
- **No published rank** for SHEEO, College Board, NAEP, YRBS, AEI, NCES Digest tables, Census revenue shares or Census support-services spending. Those Rank cells are blank on purpose.

## How to read the tables

- One table per measure. `Value` is the main figure for the year on the `year` line; when a table carries more years, those are in extra columns labeled with their year. Other extra columns hold related figures from the same source and edition (for example, the NAEP "2024 vs NH" flag or NEA's 2025-26 estimate).
- **Places:** two-letter state codes, `DC`, and `US`. What `US` means differs by source and is stated in each table's note (for example, NAEP's national public average, NIEER's "50 states + DC" total, or SHEEO's U.S. figure without DC).
- **Rank:** only the source's own published rank. Blank means the source publishes none.
- **Numbers** are copied as published. Where a source file holds more digits than it displays (NAEP API, Census and NCES Excel files), the table shows the publisher's displayed rounding and says so in the note. Any figure we calculated is marked **derived**.
- **Year convention:** `year` is the year the school or fiscal year ends (2025 = 2024-25 or FY2025); `period` keeps the source's own label.
- All `as_of` dates are 2026-11-08; review one year later (2027-11-08), or sooner when the source publishes a new edition (NAEP: early 2027 for the 2026 assessment; Census FY2025: spring 2027; NEA: April and August; NIEER: spring; SHEEO: spring; College Board: each fall).

---

## naep-vs-state-tests: Reading NAEP Results Next to State Test Results

- kind: term
- question_type: comparison
- description: What NAEP "Proficient" means, how state "proficient" bars compare with it (including New Hampshire's), and why NAEP comparisons between states can differ depending on how many states are compared. (What NH SAS "proficient" means is in `measure-state-vs-naep-proficient`, facts-terms-and-how-schools-work.md.)

1. NCES says NAEP Proficient is not the same as grade-level proficiency on a state test: "NAEP Proficient does not represent grade-level proficiency as determined by other assessment standards (e.g., state or district assessments)."
   - citation: NCES 2026-014, Table 3 note (report p. 5)
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. NCES describes students at or above NAEP Proficient as demonstrating "solid academic performance and competency over challenging subject matter."
   - citation: NCES 2026-014, Table 3 note (report p. 5)
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. By law, NAEP's achievement levels (NAEP Basic, NAEP Proficient, NAEP Advanced) "are to be used on a trial basis and should be interpreted with caution," NCES notes.
   - citation: NCES 2026-014, p. 1 (also the note on each 2024 NAEP state snapshot report)
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. A state test's "proficient" and NAEP Proficient are different bars. NCES placed each state's 2021-22 standard for proficient performance on the NAEP scale and found that "in 2022, state standards for proficient performance mapped at the NAEP Basic achievement level for most states in both grades and subjects."
   - citation: NCES 2026-014 (Yee & Cramer, February 2026), p. 1
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
5. In that NCES study, New Hampshire's 2021-22 standards for proficient performance were equivalent to NAEP scores of 228 in grade 4 reading, 243 in grade 4 math, 269 in grade 8 reading and 295 in grade 8 math. Each is below the NAEP Proficient cut score (238, 249, 281 and 299) and above the NAEP Basic cut score (208, 214, 243 and 262), and New Hampshire is not among the states NCES lists as having standards at the NAEP Proficient level in any of the four.
   - citation: NCES 2026-014-A, Tables A-1 and A-2; NCES 2026-014, Table 3 and pp. 6, 8, 10, 12
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014a.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: The comparison with cut scores is ours (derived); NCES's own classification adds a margin of error (score + 2 standard errors), which still leaves NH at NAEP Basic in all four (NH standard errors 1.3, 0.8, 1.5, 0.8).
6. NCES's study lists Massachusetts among the states whose standards were at the NAEP Proficient level in all four: grade 4 reading, grade 4 math, grade 8 reading and grade 8 math.
   - citation: NCES 2026-014, pp. 6, 8, 10 and 12 (report pages; PDF pages 10, 12, 14, 16)
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
7. NCES says the mapping study "is not an evaluation of the various state assessments or of the quality of the states' achievement standards," and that it "does not imply that the NAEP achievement levels are more valid than the state standards or that states should emulate NAEP standards."
   - citation: NCES 2026-014, p. 1
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
8. NCES adds a caveat for New Hampshire's grade 8 math result: New Hampshire and Missouri "administered end-of-course assessments and had student participation rates of less than 95% on their end-of-grade assessments but were included because their assessment data files contained only end-of-grade results."
   - citation: NCES 2026-014, Figure 10 note (report p. 12)
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
9. NCES's mapping study has no 2019 result for New Hampshire, so New Hampshire is left out of the study's comparisons across 2013, 2019 and 2022.
   - citation: NCES 2026-014, Appendix A, Table 4 (NH row) and the notes to Figures 2–3, 5–6, 8–9 and 11–12, which list New Hampshire among the states "excluded from the counts" "for comparability"
   - source: https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
10. NAEP's 2024 snapshot reports for New Hampshire compare its average score with those of 51 other states and jurisdictions (the other states, DC and the Department of Defense schools, DoDEA) instead of giving a rank. Grade 4 math: New Hampshire's average was lower than 2, higher than 28 and not significantly different from 21. Grade 8 math: lower than 1, higher than 32, not significantly different from 18. Grade 4 reading: lower than 1, higher than 40, not significantly different from 10. Grade 8 reading: lower than 1, higher than 38, not significantly different from 12.
    - citation: NAEP 2024 Mathematics and Reading State Snapshot Reports, New Hampshire, grades 4 and 8, public schools
    - source: https://nces.ed.gov/nationsreportcard/subject/publications/stt2024/pdf/2024219NH4.pdf
    - as_of: 2026-11-08
    - review_by: 2027-11-08
    - note: The places in each group are listed in the `naep_g*_*_score` tables ("2024 vs NH" column), which reproduce these counts exactly; the one jurisdiction above NH in grade 8 math and in both reading grades is DoDEA, and in grade 4 math DoDEA and Massachusetts. The source is the grade 4 math report; the others are https://nces.ed.gov/nationsreportcard/subject/publications/stt2024/pdf/2024219NH8.pdf (math grade 8), https://nces.ed.gov/nationsreportcard/subject/publications/stt2024/pdf/2024220NH4.pdf and https://nces.ed.gov/nationsreportcard/subject/publications/stt2024/pdf/2024220NH8.pdf (reading).
11. In each 2024 snapshot report, New Hampshire's average score was higher than the national public average in grade 4 math (242 vs 237), grade 8 math (280 vs 272), grade 4 reading (221 vs 214) and grade 8 reading (264 vs 257).
    - citation: NAEP 2024 State Snapshot Reports, New Hampshire, "Overall results"
    - source: https://nces.ed.gov/nationsreportcard/subject/publications/stt2024/pdf/2024219NH8.pdf
    - as_of: 2026-11-08
    - review_by: 2027-11-08
12. Whether NAEP calls a difference "significant" can depend on how many places are compared at once. When many groups are compared, NAEP adjusts its tests with a multiple comparison procedure, the Benjamini–Hochberg false discovery rate (FDR) procedure, which NAEP says it has used since 1998. For example, in NAEP's comparison of New Hampshire with all states (the snapshot set), Massachusetts's 2024 grade 8 math and grade 8 reading averages were not significantly different from New Hampshire's; when the NAEP Data Service compares only New Hampshire and Massachusetts, it reports Massachusetts significantly higher in both.
    - citation: NAEP Technical Documentation, "The False Discovery Rate (FDR) Procedure"; NAEP Data Service sigacrossjuris queries for 2024 (all states + DC + DoDEA vs. jurisdiction=NH,MA)
    - source: https://nces.ed.gov/nationsreportcard/tdw/analysis/2000_2001/infer_multiplecompare_fdr.aspx
    - as_of: 2026-11-08
    - review_by: 2027-11-08
    - note: Raw: raw/national/naep-*-2024-sigacrossjuris-NH-MA-only.json vs raw/national/naep-*-2024-sigacrossjuris-score-states-DoDEA.json. The technical documentation page reached is the 2000–2001 edition; the newer edition's URL returned 404. The NH–MA two-state result also differs in the earlier test answers file (which used a 4-place query). For "is NH different from state X," the tables here use NAEP's snapshot comparison set. The NAEP Data Service query: https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=mathematics&grade=8&subscale=MRPCM&variable=TOTAL&jurisdiction=NH,MA&stattype=MN:MN,ALC:AP&Year=2024
13. NAEP results come from samples of students, so NAEP reports whether differences are statistically significant (p < .05), and its "significance tests were performed using unrounded numbers."
    - citation: NAEP 2024 State Snapshot Reports, New Hampshire, note to the achievement-level chart
    - source: https://nces.ed.gov/nationsreportcard/subject/publications/stt2024/pdf/2024219NH4.pdf
    - as_of: 2026-11-08
    - review_by: 2027-11-08

## chronic-absenteeism-nh-data: Why New Hampshire's Chronic Absenteeism Figures Are Limited

- kind: how_it_works
- question_type: comparison
- description: Where state chronic absenteeism rates come from, and why New Hampshire has no recent rate to compare.

1. Federal EdFacts data define chronic absenteeism as "Students absent 10% or more school days."
   - citation: ED Data Express, EDFacts file spec 195, data group 814, data description
   - source: https://eddataexpress.ed.gov/sites/default/files/data_download/EID_11092/SY2122_FS195_DG814_SEA_data_files.zip
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. In its federal EdFacts report for 2021-22, New Hampshire counted 56,427 chronically absent students statewide and added this state note: "Due to the pandemic, and students being out, these numbers will continue to fluctuate. In addition, districts are allowed to change between an hour vs a day calendar. There is currently no good way to calculate chronic absenteeism."
   - citation: ED Data Express, SY2021-22 FS195 DG814 SEA file and its data notes (New Hampshire rows)
   - source: https://eddataexpress.ed.gov/sites/default/files/data_download/EID_11092/SY2122_FS195_DG814_SEA_data_files.zip
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. The newest state-level chronic absenteeism file in the ED Data Express Data Library on November 8, 2026 was for 2021-22, and it gives counts of chronically absent students, not rates.
   - citation: ED Data Express Data Library listing (all 25 pages), checked 2026-11-08
   - source: https://eddataexpress.ed.gov/download/data-library
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: Listing saved as raw/national/eddataexpress-data-library-listing-2026-11-08.txt (read in a browser; the site blocks plain downloads).
4. AEI's Return to Learn tracker has no state-reported chronic absenteeism data for New Hampshire: New Hampshire has no row in AEI's table of state-reported rates, and AEI's New Hampshire estimates (2017-18 through 2022-23) come from federal EdFacts counts, which AEI pairs with NCES enrollment counts.
   - citation: AEI, "From Attendance Crisis to Chronic Condition?" (Nat Malkus, June 2026), Appendix Tables A2 and A3 and their notes
   - source: https://www.aei.org/wp-content/uploads/2026/06/From-Attendance-Crisis-to-Chronic-Condition-Tracking-Post-Pandemic-Chronic-Absenteeism-into-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: AEI is a research organization; its rates are estimates, not official statistics. AEI writes that EdFacts-based denominators "are imperfect and are subject to error" (Return to Learn tracker methods text, raw/national/aei-returntolearntracker-home-2026-11-08.html).
5. In AEI's estimates, New Hampshire's chronic absenteeism rate was 14% in 2018-19, 35% in 2021-22 and 25% in 2022-23; AEI has no New Hampshire figure for 2023-24 or 2024-25.
   - citation: AEI, June 2026 report, Appendix Table A2
   - source: https://www.aei.org/wp-content/uploads/2026/06/From-Attendance-Crisis-to-Chronic-Condition-Tracking-Post-Pandemic-Chronic-Absenteeism-into-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08

---

# Test scores (NAEP)

## naep_g4_math_score: NAEP Average Scale Score, Grade 4 Math

- unit: score
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Math 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=mathematics&grade=4&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=mathematics&grade=4&subscale=MRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=MN:MN&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- source (change): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossyear&subject=mathematics&grade=4&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-math-g4-2019-2022-2024.json; raw/national/naep-math-g4-2024-sigacrossjuris-score-states-DoDEA.json, raw/national/naep-math-g4-2024-sigacrossjuris-NH-vs-nationalpublic.json; raw/national/naep-math-g4-sigacrossyear-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH. "2024 vs 2019" and "2024 vs 2022" are NAEP's test of whether the place's own 2024 score differs significantly from that earlier year.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | 2024 vs 2019 | 2024 vs 2022 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 237 |  | lower | 235 | 240 | lower | higher |  |
| AL | 236 |  | lower | 230 | 230 | higher | higher |  |
| AK | 226 |  | lower | 226 | 232 | lower | not sig. different |  |
| AZ | 232 |  | lower | 232 | 238 | lower | not sig. different |  |
| AR | 230 |  | lower | 228 | 233 | not sig. different | not sig. different |  |
| CA | 233 |  | lower | 230 | 235 | not sig. different | not sig. different |  |
| CO | 239 |  | not sig. different | 236 | 242 | not sig. different | not sig. different |  |
| CT | 239 |  | not sig. different | 236 | 243 | lower | not sig. different |  |
| DE | 233 |  | lower | 226 | 239 | lower | higher |  |
| DC | 231 |  | lower | 223 | 235 | lower | higher |  |
| FL | 243 |  | not sig. different | 241 | 246 | not sig. different | not sig. different |  |
| GA | 236 |  | lower | 235 | 238 | not sig. different | not sig. different |  |
| HI | 239 |  | not sig. different | 237 | 239 | not sig. different | higher |  |
| ID | 238 |  | not sig. different | 236 | 242 | lower | not sig. different |  |
| IL | 236 |  | lower | 237 | 237 | not sig. different | not sig. different |  |
| IN | 240 |  | not sig. different | 239 | 245 | lower | not sig. different |  |
| IA | 237 |  | lower | 240 | 241 | lower | not sig. different |  |
| KS | 237 |  | lower | 235 | 239 | not sig. different | not sig. different |  |
| KY | 238 |  | lower | 234 | 239 | not sig. different | higher |  |
| LA | 235 |  | lower | 229 | 231 | not sig. different | higher |  |
| ME | 233 |  | lower | 233 | 241 | lower | not sig. different |  |
| MD | 234 |  | lower | 229 | 239 | lower | higher |  |
| MA | 246 |  | higher | 242 | 247 | not sig. different | higher |  |
| MI | 235 |  | lower | 232 | 236 | not sig. different | not sig. different |  |
| MN | 241 |  | not sig. different | 239 | 248 | lower | not sig. different |  |
| MS | 239 |  | not sig. different | 234 | 241 | not sig. different | higher |  |
| MO | 235 |  | lower | 232 | 238 | lower | not sig. different |  |
| MT | 238 |  | not sig. different | 239 | 241 | not sig. different | not sig. different |  |
| NE | 238 |  | lower | 242 | 244 | lower | lower |  |
| NV | 233 |  | lower | 229 | 236 | not sig. different | higher |  |
| NH | 242 |  | — | 239 | 245 | lower | not sig. different |  |
| NJ | 240 |  | not sig. different | 239 | 246 | lower | not sig. different |  |
| NM | 224 |  | lower | 221 | 231 | lower | not sig. different |  |
| NY | 234 |  | lower | 227 | 237 | not sig. different | higher |  |
| NC | 239 |  | not sig. different | 236 | 241 | not sig. different | not sig. different |  |
| ND | 241 |  | not sig. different | 240 | 243 | not sig. different | not sig. different |  |
| OH | 239 |  | not sig. different | 238 | 241 | not sig. different | not sig. different |  |
| OK | 233 |  | lower | 229 | 237 | lower | not sig. different |  |
| OR | 229 |  | lower | 228 | 236 | lower | not sig. different |  |
| PA | 238 |  | not sig. different | 238 | 244 | lower | not sig. different |  |
| RI | 237 |  | lower | 234 | 239 | not sig. different | higher |  |
| SC | 238 |  | lower | 234 | 237 | not sig. different | higher |  |
| SD | 240 |  | not sig. different | 239 | 241 | not sig. different | not sig. different |  |
| TN | 240 |  | not sig. different | 236 | 240 | not sig. different | not sig. different |  |
| TX | 241 |  | not sig. different | 239 | 244 | not sig. different | not sig. different |  |
| UT | 242 |  | not sig. different | 240 | 244 | not sig. different | not sig. different |  |
| VT | 235 |  | lower | 234 | 239 | lower | not sig. different |  |
| VA | 238 |  | not sig. different | 236 | 247 | lower | not sig. different |  |
| WA | 238 |  | lower | 235 | 240 | not sig. different | not sig. different |  |
| WV | 232 |  | lower | 226 | 231 | not sig. different | higher |  |
| WI | 239 |  | not sig. different | 240 | 242 | not sig. different | not sig. different |  |
| WY | 243 |  | not sig. different | 243 | 246 | lower | not sig. different |  |

## naep_g4_math_proficient: NAEP Percent at or above NAEP Proficient, Grade 4 Math

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Math 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=mathematics&grade=4&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AP&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=mathematics&grade=4&subscale=MRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=ALC:AP&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- as_of: 2026-11-08
- raw: raw/national/naep-math-g4-2019-2022-2024.json; raw/national/naep-math-g4-2024-sigacrossjuris-proficient-states-DoDEA.json, raw/national/naep-math-g4-2024-sigacrossjuris-NH-vs-nationalpublic.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|---|
| US | 39 |  | lower | 35 | 40 |  |
| AL | 37 |  | not sig. different | 27 | 28 |  |
| AK | 30 |  | lower | 28 | 33 |  |
| AZ | 34 |  | lower | 32 | 37 |  |
| AR | 31 |  | lower | 28 | 33 |  |
| CA | 35 |  | lower | 30 | 34 |  |
| CO | 42 |  | not sig. different | 36 | 44 |  |
| CT | 42 |  | not sig. different | 37 | 45 |  |
| DE | 35 |  | lower | 26 | 39 |  |
| DC | 33 |  | lower | 24 | 34 |  |
| FL | 45 |  | not sig. different | 41 | 48 |  |
| GA | 38 |  | not sig. different | 34 | 36 |  |
| HI | 42 |  | not sig. different | 37 | 40 |  |
| ID | 41 |  | not sig. different | 36 | 43 |  |
| IL | 38 |  | not sig. different | 38 | 38 |  |
| IN | 43 |  | not sig. different | 40 | 47 |  |
| IA | 39 |  | not sig. different | 40 | 42 |  |
| KS | 40 |  | not sig. different | 35 | 40 |  |
| KY | 38 |  | not sig. different | 33 | 40 |  |
| LA | 35 |  | lower | 27 | 29 |  |
| ME | 33 |  | lower | 32 | 42 |  |
| MD | 37 |  | not sig. different | 31 | 39 |  |
| MA | 51 |  | higher | 43 | 50 |  |
| MI | 37 |  | lower | 32 | 36 |  |
| MN | 45 |  | not sig. different | 41 | 53 |  |
| MS | 38 |  | not sig. different | 32 | 39 |  |
| MO | 36 |  | lower | 34 | 39 |  |
| MT | 40 |  | not sig. different | 38 | 43 |  |
| NE | 40 |  | not sig. different | 43 | 45 |  |
| NV | 36 |  | lower | 28 | 34 |  |
| NH | 43 |  | — | 40 | 46 |  |
| NJ | 44 |  | not sig. different | 39 | 48 |  |
| NM | 23 |  | lower | 19 | 29 |  |
| NY | 37 |  | lower | 28 | 37 |  |
| NC | 41 |  | not sig. different | 35 | 41 |  |
| ND | 43 |  | not sig. different | 40 | 44 |  |
| OH | 43 |  | not sig. different | 40 | 41 |  |
| OK | 31 |  | lower | 27 | 35 |  |
| OR | 31 |  | lower | 29 | 37 |  |
| PA | 41 |  | not sig. different | 40 | 47 |  |
| RI | 38 |  | not sig. different | 34 | 40 |  |
| SC | 40 |  | not sig. different | 34 | 36 |  |
| SD | 42 |  | not sig. different | 40 | 43 |  |
| TN | 42 |  | not sig. different | 36 | 40 |  |
| TX | 43 |  | not sig. different | 38 | 44 |  |
| UT | 45 |  | not sig. different | 42 | 46 |  |
| VT | 36 |  | lower | 34 | 39 |  |
| VA | 40 |  | not sig. different | 38 | 48 |  |
| WA | 40 |  | not sig. different | 35 | 39 |  |
| WV | 31 |  | lower | 23 | 30 |  |
| WI | 42 |  | not sig. different | 43 | 45 |  |
| WY | 46 |  | not sig. different | 44 | 48 |  |

## naep_g4_math_basic: NAEP Percent at or above NAEP Basic, Grade 4 Math

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Math 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=mathematics&grade=4&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AB&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-math-g4-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file).

| Place | Value 2024 | Rank | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|
| US | 76 |  | 74 | 80 |  |
| AL | 76 |  | 71 | 71 |  |
| AK | 64 |  | 65 | 73 |  |
| AZ | 70 |  | 70 | 77 |  |
| AR | 70 |  | 69 | 75 |  |
| CA | 70 |  | 67 | 75 |  |
| CO | 77 |  | 75 | 80 |  |
| CT | 76 |  | 74 | 82 |  |
| DE | 71 |  | 64 | 79 |  |
| DC | 65 |  | 57 | 73 |  |
| FL | 82 |  | 81 | 87 |  |
| GA | 75 |  | 75 | 77 |  |
| HI | 77 |  | 77 | 78 |  |
| ID | 76 |  | 76 | 82 |  |
| IL | 74 |  | 76 | 77 |  |
| IN | 79 |  | 78 | 84 |  |
| IA | 77 |  | 80 | 81 |  |
| KS | 76 |  | 75 | 79 |  |
| KY | 78 |  | 75 | 81 |  |
| LA | 75 |  | 69 | 73 |  |
| ME | 73 |  | 75 | 81 |  |
| MD | 70 |  | 65 | 76 |  |
| MA | 82 |  | 79 | 85 |  |
| MI | 74 |  | 71 | 76 |  |
| MN | 78 |  | 78 | 85 |  |
| MS | 81 |  | 74 | 84 |  |
| MO | 75 |  | 72 | 80 |  |
| MT | 78 |  | 80 | 82 |  |
| NE | 78 |  | 80 | 84 |  |
| NV | 72 |  | 69 | 77 |  |
| NH | 81 |  | 80 | 86 |  |
| NJ | 77 |  | 77 | 85 |  |
| NM | 62 |  | 60 | 72 |  |
| NY | 72 |  | 66 | 76 |  |
| NC | 77 |  | 75 | 82 |  |
| ND | 81 |  | 81 | 84 |  |
| OH | 77 |  | 76 | 82 |  |
| OK | 74 |  | 71 | 80 |  |
| OR | 67 |  | 66 | 75 |  |
| PA | 75 |  | 76 | 81 |  |
| RI | 76 |  | 74 | 81 |  |
| SC | 76 |  | 74 | 77 |  |
| SD | 79 |  | 80 | 83 |  |
| TN | 78 |  | 76 | 79 |  |
| TX | 79 |  | 78 | 84 |  |
| UT | 79 |  | 78 | 82 |  |
| VT | 75 |  | 74 | 81 |  |
| VA | 76 |  | 75 | 87 |  |
| WA | 75 |  | 74 | 79 |  |
| WV | 72 |  | 67 | 74 |  |
| WI | 77 |  | 79 | 80 |  |
| WY | 83 |  | 84 | 87 |  |

## naep_g8_math_score: NAEP Average Scale Score, Grade 8 Math

- unit: score
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Math 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=mathematics&grade=8&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=mathematics&grade=8&subscale=MRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=MN:MN&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- source (change): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossyear&subject=mathematics&grade=8&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-math-g8-2019-2022-2024.json; raw/national/naep-math-g8-2024-sigacrossjuris-score-states-DoDEA.json, raw/national/naep-math-g8-2024-sigacrossjuris-NH-vs-nationalpublic.json; raw/national/naep-math-g8-sigacrossyear-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH. "2024 vs 2019" and "2024 vs 2022" are NAEP's test of whether the place's own 2024 score differs significantly from that earlier year.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | 2024 vs 2019 | 2024 vs 2022 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 272 |  | lower | 273 | 281 | lower | not sig. different |  |
| AL | 262 |  | lower | 264 | 269 | lower | not sig. different |  |
| AK | 264 |  | lower | 270 | 274 | lower | lower |  |
| AZ | 270 |  | lower | 271 | 280 | lower | not sig. different |  |
| AR | 266 |  | lower | 267 | 274 | lower | not sig. different |  |
| CA | 269 |  | lower | 270 | 276 | lower | not sig. different |  |
| CO | 278 |  | not sig. different | 275 | 285 | lower | not sig. different |  |
| CT | 277 |  | not sig. different | 276 | 286 | lower | not sig. different |  |
| DE | 263 |  | lower | 264 | 277 | lower | not sig. different |  |
| DC | 262 |  | lower | 260 | 269 | lower | not sig. different |  |
| FL | 267 |  | lower | 271 | 279 | lower | lower |  |
| GA | 269 |  | lower | 271 | 279 | lower | not sig. different |  |
| HI | 270 |  | lower | 270 | 275 | lower | not sig. different |  |
| ID | 278 |  | not sig. different | 282 | 286 | lower | lower |  |
| IL | 277 |  | not sig. different | 275 | 283 | lower | not sig. different |  |
| IN | 278 |  | not sig. different | 279 | 286 | lower | not sig. different |  |
| IA | 275 |  | lower | 277 | 282 | lower | not sig. different |  |
| KS | 274 |  | lower | 272 | 282 | lower | not sig. different |  |
| KY | 271 |  | lower | 269 | 278 | lower | not sig. different |  |
| LA | 267 |  | lower | 266 | 272 | lower | not sig. different |  |
| ME | 273 |  | lower | 273 | 282 | lower | not sig. different |  |
| MD | 268 |  | lower | 269 | 280 | lower | not sig. different |  |
| MA | 283 |  | not sig. different | 284 | 294 | lower | not sig. different |  |
| MI | 270 |  | lower | 273 | 280 | lower | not sig. different |  |
| MN | 282 |  | not sig. different | 280 | 291 | lower | not sig. different |  |
| MS | 269 |  | lower | 266 | 274 | lower | not sig. different |  |
| MO | 270 |  | lower | 272 | 281 | lower | not sig. different |  |
| MT | 279 |  | not sig. different | 277 | 284 | lower | not sig. different |  |
| NE | 280 |  | not sig. different | 279 | 285 | lower | not sig. different |  |
| NV | 265 |  | lower | 269 | 274 | lower | lower |  |
| NH | 280 |  | — | 279 | 287 | lower | not sig. different |  |
| NJ | 282 |  | not sig. different | 281 | 292 | lower | not sig. different |  |
| NM | 256 |  | lower | 259 | 269 | lower | not sig. different |  |
| NY | 271 |  | lower | 274 | 280 | lower | not sig. different |  |
| NC | 276 |  | lower | 274 | 284 | lower | not sig. different |  |
| ND | 280 |  | not sig. different | 278 | 286 | lower | not sig. different |  |
| OH | 279 |  | not sig. different | 276 | 286 | lower | not sig. different |  |
| OK | 264 |  | lower | 264 | 276 | lower | not sig. different |  |
| OR | 268 |  | lower | 270 | 280 | lower | not sig. different |  |
| PA | 276 |  | not sig. different | 274 | 285 | lower | not sig. different |  |
| RI | 270 |  | lower | 270 | 276 | lower | not sig. different |  |
| SC | 268 |  | lower | 269 | 276 | lower | not sig. different |  |
| SD | 281 |  | not sig. different | 281 | 287 | lower | not sig. different |  |
| TN | 276 |  | not sig. different | 272 | 280 | not sig. different | not sig. different |  |
| TX | 269 |  | lower | 273 | 280 | lower | not sig. different |  |
| UT | 282 |  | not sig. different | 282 | 285 | lower | not sig. different |  |
| VT | 276 |  | lower | 276 | 287 | lower | not sig. different |  |
| VA | 275 |  | lower | 279 | 287 | lower | not sig. different |  |
| WA | 274 |  | lower | 276 | 286 | lower | not sig. different |  |
| WV | 261 |  | lower | 260 | 272 | lower | not sig. different |  |
| WI | 283 |  | not sig. different | 281 | 289 | lower | not sig. different |  |
| WY | 278 |  | not sig. different | 281 | 286 | lower | not sig. different |  |

## naep_g8_math_proficient: NAEP Percent at or above NAEP Proficient, Grade 8 Math

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Math 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=mathematics&grade=8&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AP&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=mathematics&grade=8&subscale=MRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=ALC:AP&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- as_of: 2026-11-08
- raw: raw/national/naep-math-g8-2019-2022-2024.json; raw/national/naep-math-g8-2024-sigacrossjuris-proficient-states-DoDEA.json, raw/national/naep-math-g8-2024-sigacrossjuris-NH-vs-nationalpublic.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|---|
| US | 27 |  | lower | 26 | 33 |  |
| AL | 18 |  | lower | 19 | 21 |  |
| AK | 22 |  | lower | 23 | 29 |  |
| AZ | 26 |  | lower | 24 | 31 |  |
| AR | 20 |  | lower | 19 | 27 |  |
| CA | 25 |  | lower | 23 | 29 |  |
| CO | 32 |  | not sig. different | 28 | 37 |  |
| CT | 32 |  | not sig. different | 30 | 39 |  |
| DE | 19 |  | lower | 18 | 29 |  |
| DC | 20 |  | lower | 16 | 23 |  |
| FL | 21 |  | lower | 23 | 31 |  |
| GA | 24 |  | lower | 24 | 31 |  |
| HI | 23 |  | lower | 22 | 28 |  |
| ID | 31 |  | not sig. different | 32 | 37 |  |
| IL | 32 |  | not sig. different | 27 | 34 |  |
| IN | 31 |  | not sig. different | 30 | 37 |  |
| IA | 27 |  | lower | 28 | 33 |  |
| KS | 26 |  | lower | 23 | 33 |  |
| KY | 24 |  | lower | 21 | 29 |  |
| LA | 21 |  | lower | 19 | 23 |  |
| ME | 25 |  | lower | 24 | 34 |  |
| MD | 25 |  | lower | 25 | 33 |  |
| MA | 37 |  | higher | 35 | 47 |  |
| MI | 24 |  | lower | 25 | 31 |  |
| MN | 34 |  | not sig. different | 32 | 44 |  |
| MS | 22 |  | lower | 18 | 24 |  |
| MO | 23 |  | lower | 24 | 32 |  |
| MT | 32 |  | not sig. different | 29 | 36 |  |
| NE | 32 |  | not sig. different | 31 | 37 |  |
| NV | 20 |  | lower | 21 | 26 |  |
| NH | 32 |  | — | 29 | 38 |  |
| NJ | 37 |  | higher | 33 | 44 |  |
| NM | 14 |  | lower | 13 | 21 |  |
| NY | 26 |  | lower | 28 | 34 |  |
| NC | 31 |  | not sig. different | 25 | 37 |  |
| ND | 29 |  | not sig. different | 28 | 37 |  |
| OH | 32 |  | not sig. different | 29 | 38 |  |
| OK | 17 |  | lower | 16 | 26 |  |
| OR | 24 |  | lower | 22 | 31 |  |
| PA | 31 |  | not sig. different | 27 | 39 |  |
| RI | 26 |  | lower | 24 | 29 |  |
| SC | 24 |  | lower | 22 | 29 |  |
| SD | 33 |  | not sig. different | 32 | 39 |  |
| TN | 31 |  | not sig. different | 25 | 31 |  |
| TX | 24 |  | lower | 24 | 30 |  |
| UT | 35 |  | not sig. different | 35 | 37 |  |
| VT | 29 |  | not sig. different | 27 | 38 |  |
| VA | 29 |  | not sig. different | 31 | 38 |  |
| WA | 30 |  | not sig. different | 28 | 40 |  |
| WV | 18 |  | lower | 15 | 24 |  |
| WI | 37 |  | not sig. different | 33 | 41 |  |
| WY | 30 |  | not sig. different | 31 | 37 |  |

## naep_g8_math_basic: NAEP Percent at or above NAEP Basic, Grade 8 Math

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Math 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=mathematics&grade=8&subscale=MRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AB&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-math-g8-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file).

| Place | Value 2024 | Rank | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|
| US | 59 |  | 60 | 68 |  |
| AL | 50 |  | 53 | 57 |  |
| AK | 54 |  | 59 | 63 |  |
| AZ | 57 |  | 58 | 68 |  |
| AR | 54 |  | 55 | 63 |  |
| CA | 54 |  | 56 | 61 |  |
| CO | 65 |  | 63 | 73 |  |
| CT | 63 |  | 63 | 72 |  |
| DE | 51 |  | 51 | 65 |  |
| DC | 46 |  | 46 | 55 |  |
| FL | 55 |  | 58 | 66 |  |
| GA | 56 |  | 59 | 67 |  |
| HI | 58 |  | 58 | 65 |  |
| ID | 67 |  | 71 | 74 |  |
| IL | 62 |  | 62 | 69 |  |
| IN | 67 |  | 66 | 73 |  |
| IA | 65 |  | 67 | 72 |  |
| KS | 63 |  | 61 | 71 |  |
| KY | 58 |  | 57 | 67 |  |
| LA | 54 |  | 53 | 61 |  |
| ME | 61 |  | 61 | 71 |  |
| MD | 54 |  | 54 | 65 |  |
| MA | 68 |  | 70 | 78 |  |
| MI | 57 |  | 60 | 68 |  |
| MN | 71 |  | 69 | 77 |  |
| MS | 57 |  | 54 | 62 |  |
| MO | 59 |  | 61 | 70 |  |
| MT | 68 |  | 68 | 73 |  |
| NE | 69 |  | 68 | 74 |  |
| NV | 52 |  | 56 | 62 |  |
| NH | 69 |  | 70 | 77 |  |
| NJ | 65 |  | 67 | 76 |  |
| NM | 42 |  | 45 | 56 |  |
| NY | 58 |  | 60 | 66 |  |
| NC | 62 |  | 61 | 71 |  |
| ND | 71 |  | 69 | 75 |  |
| OH | 65 |  | 64 | 73 |  |
| OK | 53 |  | 52 | 66 |  |
| OR | 55 |  | 57 | 67 |  |
| PA | 63 |  | 62 | 70 |  |
| RI | 57 |  | 58 | 64 |  |
| SC | 55 |  | 56 | 64 |  |
| SD | 71 |  | 72 | 76 |  |
| TN | 62 |  | 60 | 68 |  |
| TX | 56 |  | 61 | 68 |  |
| UT | 70 |  | 70 | 72 |  |
| VT | 64 |  | 66 | 75 |  |
| VA | 63 |  | 65 | 75 |  |
| WA | 59 |  | 64 | 72 |  |
| WV | 48 |  | 48 | 62 |  |
| WI | 69 |  | 70 | 76 |  |
| WY | 68 |  | 72 | 76 |  |

## naep_g4_reading_score: NAEP Average Scale Score, Grade 4 Reading

- unit: score
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Reading 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=reading&grade=4&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=reading&grade=4&subscale=RRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=MN:MN&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- source (change): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossyear&subject=reading&grade=4&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-reading-g4-2019-2022-2024.json; raw/national/naep-reading-g4-2024-sigacrossjuris-score-states-DoDEA.json, raw/national/naep-reading-g4-2024-sigacrossjuris-NH-vs-nationalpublic.json; raw/national/naep-reading-g4-sigacrossyear-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH. "2024 vs 2019" and "2024 vs 2022" are NAEP's test of whether the place's own 2024 score differs significantly from that earlier year.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | 2024 vs 2019 | 2024 vs 2022 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 214 |  | lower | 216 | 219 | lower | lower |  |
| AL | 213 |  | lower | 213 | 212 | not sig. different | not sig. different |  |
| AK | 202 |  | lower | 204 | 204 | not sig. different | not sig. different |  |
| AZ | 208 |  | lower | 215 | 216 | lower | lower |  |
| AR | 210 |  | lower | 212 | 215 | lower | not sig. different |  |
| CA | 212 |  | lower | 214 | 216 | lower | not sig. different |  |
| CO | 221 |  | not sig. different | 223 | 225 | lower | not sig. different |  |
| CT | 219 |  | not sig. different | 219 | 224 | lower | not sig. different |  |
| DE | 210 |  | lower | 208 | 218 | lower | not sig. different |  |
| DC | 209 |  | lower | 207 | 214 | lower | not sig. different |  |
| FL | 218 |  | not sig. different | 225 | 225 | lower | lower |  |
| GA | 214 |  | lower | 216 | 218 | not sig. different | not sig. different |  |
| HI | 216 |  | lower | 219 | 218 | not sig. different | not sig. different |  |
| ID | 216 |  | lower | 215 | 223 | lower | not sig. different |  |
| IL | 214 |  | lower | 218 | 218 | not sig. different | not sig. different |  |
| IN | 220 |  | not sig. different | 217 | 222 | not sig. different | not sig. different |  |
| IA | 215 |  | lower | 218 | 221 | lower | not sig. different |  |
| KS | 213 |  | lower | 215 | 219 | lower | not sig. different |  |
| KY | 218 |  | not sig. different | 217 | 221 | not sig. different | not sig. different |  |
| LA | 216 |  | lower | 212 | 210 | higher | not sig. different |  |
| ME | 210 |  | lower | 213 | 221 | lower | not sig. different |  |
| MD | 216 |  | lower | 212 | 220 | lower | not sig. different |  |
| MA | 225 |  | not sig. different | 227 | 231 | lower | not sig. different |  |
| MI | 209 |  | lower | 212 | 218 | lower | not sig. different |  |
| MN | 214 |  | lower | 215 | 222 | lower | not sig. different |  |
| MS | 219 |  | not sig. different | 217 | 219 | not sig. different | not sig. different |  |
| MO | 212 |  | lower | 213 | 218 | lower | not sig. different |  |
| MT | 217 |  | lower | 219 | 222 | lower | not sig. different |  |
| NE | 212 |  | lower | 219 | 222 | lower | lower |  |
| NV | 213 |  | lower | 212 | 218 | lower | not sig. different |  |
| NH | 221 |  | — | 223 | 224 | not sig. different | not sig. different |  |
| NJ | 222 |  | not sig. different | 223 | 227 | not sig. different | not sig. different |  |
| NM | 201 |  | lower | 202 | 208 | lower | not sig. different |  |
| NY | 215 |  | lower | 214 | 220 | lower | not sig. different |  |
| NC | 213 |  | lower | 216 | 221 | lower | not sig. different |  |
| ND | 216 |  | lower | 218 | 221 | lower | not sig. different |  |
| OH | 216 |  | lower | 219 | 222 | lower | not sig. different |  |
| OK | 207 |  | lower | 208 | 216 | lower | not sig. different |  |
| OR | 207 |  | lower | 210 | 218 | lower | not sig. different |  |
| PA | 216 |  | lower | 219 | 223 | lower | not sig. different |  |
| RI | 216 |  | lower | 217 | 220 | lower | not sig. different |  |
| SC | 215 |  | lower | 216 | 216 | not sig. different | not sig. different |  |
| SD | 214 |  | lower | 218 | 222 | lower | lower |  |
| TN | 215 |  | lower | 214 | 219 | lower | not sig. different |  |
| TX | 212 |  | lower | 214 | 216 | lower | not sig. different |  |
| UT | 219 |  | not sig. different | 221 | 225 | lower | not sig. different |  |
| VT | 213 |  | lower | 217 | 222 | lower | lower |  |
| VA | 214 |  | lower | 214 | 224 | lower | not sig. different |  |
| WA | 216 |  | lower | 217 | 220 | lower | not sig. different |  |
| WV | 206 |  | lower | 205 | 213 | lower | not sig. different |  |
| WI | 215 |  | lower | 217 | 220 | lower | not sig. different |  |
| WY | 222 |  | not sig. different | 225 | 227 | lower | not sig. different |  |

## naep_g4_reading_proficient: NAEP Percent at or above NAEP Proficient, Grade 4 Reading

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Reading 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=reading&grade=4&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AP&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=reading&grade=4&subscale=RRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=ALC:AP&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- as_of: 2026-11-08
- raw: raw/national/naep-reading-g4-2019-2022-2024.json; raw/national/naep-reading-g4-2024-sigacrossjuris-proficient-states-DoDEA.json, raw/national/naep-reading-g4-2024-sigacrossjuris-NH-vs-nationalpublic.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|---|
| US | 30 |  | lower | 32 | 34 |  |
| AL | 28 |  | lower | 28 | 28 |  |
| AK | 22 |  | lower | 24 | 25 |  |
| AZ | 26 |  | lower | 31 | 31 |  |
| AR | 28 |  | lower | 30 | 31 |  |
| CA | 29 |  | lower | 31 | 32 |  |
| CO | 36 |  | not sig. different | 38 | 40 |  |
| CT | 36 |  | not sig. different | 35 | 40 |  |
| DE | 26 |  | lower | 25 | 33 |  |
| DC | 30 |  | lower | 26 | 30 |  |
| FL | 33 |  | not sig. different | 39 | 38 |  |
| GA | 30 |  | not sig. different | 32 | 32 |  |
| HI | 32 |  | not sig. different | 35 | 34 |  |
| ID | 32 |  | not sig. different | 32 | 37 |  |
| IL | 30 |  | not sig. different | 33 | 34 |  |
| IN | 34 |  | not sig. different | 33 | 37 |  |
| IA | 29 |  | lower | 33 | 35 |  |
| KS | 28 |  | lower | 31 | 34 |  |
| KY | 33 |  | not sig. different | 31 | 35 |  |
| LA | 32 |  | not sig. different | 28 | 26 |  |
| ME | 26 |  | lower | 29 | 36 |  |
| MD | 34 |  | not sig. different | 31 | 35 |  |
| MA | 40 |  | not sig. different | 43 | 45 |  |
| MI | 25 |  | lower | 28 | 32 |  |
| MN | 31 |  | lower | 32 | 38 |  |
| MS | 32 |  | not sig. different | 31 | 32 |  |
| MO | 27 |  | lower | 30 | 34 |  |
| MT | 32 |  | not sig. different | 34 | 36 |  |
| NE | 28 |  | lower | 34 | 37 |  |
| NV | 30 |  | lower | 27 | 31 |  |
| NH | 36 |  | — | 37 | 38 |  |
| NJ | 38 |  | not sig. different | 38 | 42 |  |
| NM | 20 |  | lower | 21 | 24 |  |
| NY | 31 |  | not sig. different | 30 | 34 |  |
| NC | 30 |  | lower | 32 | 36 |  |
| ND | 29 |  | lower | 31 | 34 |  |
| OH | 32 |  | not sig. different | 35 | 36 |  |
| OK | 23 |  | lower | 24 | 29 |  |
| OR | 27 |  | lower | 28 | 34 |  |
| PA | 33 |  | not sig. different | 34 | 40 |  |
| RI | 33 |  | not sig. different | 34 | 35 |  |
| SC | 32 |  | not sig. different | 32 | 32 |  |
| SD | 28 |  | lower | 32 | 36 |  |
| TN | 32 |  | not sig. different | 30 | 35 |  |
| TX | 28 |  | lower | 30 | 30 |  |
| UT | 36 |  | not sig. different | 37 | 40 |  |
| VT | 31 |  | lower | 34 | 37 |  |
| VA | 31 |  | not sig. different | 32 | 38 |  |
| WA | 32 |  | not sig. different | 34 | 35 |  |
| WV | 25 |  | lower | 22 | 30 |  |
| WI | 31 |  | not sig. different | 33 | 36 |  |
| WY | 36 |  | not sig. different | 38 | 41 |  |

## naep_g4_reading_basic: NAEP Percent at or above NAEP Basic, Grade 4 Reading

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Reading 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=reading&grade=4&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AB&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-reading-g4-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file).

| Place | Value 2024 | Rank | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|
| US | 59 |  | 61 | 65 |  |
| AL | 58 |  | 59 | 58 |  |
| AK | 47 |  | 51 | 53 |  |
| AZ | 53 |  | 61 | 61 |  |
| AR | 56 |  | 58 | 62 |  |
| CA | 56 |  | 58 | 63 |  |
| CO | 65 |  | 68 | 71 |  |
| CT | 63 |  | 64 | 70 |  |
| DE | 55 |  | 53 | 62 |  |
| DC | 52 |  | 50 | 57 |  |
| FL | 62 |  | 71 | 70 |  |
| GA | 59 |  | 61 | 63 |  |
| HI | 61 |  | 64 | 63 |  |
| ID | 61 |  | 61 | 69 |  |
| IL | 59 |  | 62 | 64 |  |
| IN | 65 |  | 63 | 67 |  |
| IA | 61 |  | 64 | 68 |  |
| KS | 60 |  | 60 | 66 |  |
| KY | 62 |  | 62 | 67 |  |
| LA | 60 |  | 57 | 55 |  |
| ME | 56 |  | 60 | 67 |  |
| MD | 59 |  | 56 | 64 |  |
| MA | 68 |  | 70 | 76 |  |
| MI | 55 |  | 58 | 64 |  |
| MN | 61 |  | 61 | 69 |  |
| MS | 65 |  | 63 | 65 |  |
| MO | 58 |  | 60 | 64 |  |
| MT | 62 |  | 65 | 69 |  |
| NE | 58 |  | 65 | 69 |  |
| NV | 59 |  | 57 | 64 |  |
| NH | 67 |  | 67 | 71 |  |
| NJ | 66 |  | 67 | 72 |  |
| NM | 47 |  | 48 | 53 |  |
| NY | 59 |  | 58 | 66 |  |
| NC | 58 |  | 61 | 67 |  |
| ND | 62 |  | 65 | 69 |  |
| OH | 62 |  | 65 | 68 |  |
| OK | 54 |  | 55 | 63 |  |
| OR | 52 |  | 56 | 64 |  |
| PA | 62 |  | 64 | 68 |  |
| RI | 61 |  | 62 | 66 |  |
| SC | 60 |  | 61 | 61 |  |
| SD | 60 |  | 65 | 69 |  |
| TN | 61 |  | 59 | 66 |  |
| TX | 57 |  | 58 | 61 |  |
| UT | 64 |  | 67 | 72 |  |
| VT | 58 |  | 62 | 68 |  |
| VA | 58 |  | 60 | 69 |  |
| WA | 61 |  | 61 | 65 |  |
| WV | 53 |  | 52 | 60 |  |
| WI | 61 |  | 63 | 66 |  |
| WY | 68 |  | 71 | 73 |  |

## naep_g8_reading_score: NAEP Average Scale Score, Grade 8 Reading

- unit: score
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Reading 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=reading&grade=8&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=reading&grade=8&subscale=RRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=MN:MN&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- source (change): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossyear&subject=reading&grade=8&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-reading-g8-2019-2022-2024.json; raw/national/naep-reading-g8-2024-sigacrossjuris-score-states-DoDEA.json, raw/national/naep-reading-g8-2024-sigacrossjuris-NH-vs-nationalpublic.json; raw/national/naep-reading-g8-sigacrossyear-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH. "2024 vs 2019" and "2024 vs 2022" are NAEP's test of whether the place's own 2024 score differs significantly from that earlier year.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | 2024 vs 2019 | 2024 vs 2022 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 257 |  | lower | 259 | 262 | lower | lower |  |
| AL | 250 |  | lower | 251 | 253 | not sig. different | not sig. different |  |
| AK | 246 |  | lower | 253 | 252 | lower | lower |  |
| AZ | 254 |  | lower | 259 | 259 | lower | lower |  |
| AR | 255 |  | lower | 255 | 259 | lower | not sig. different |  |
| CA | 254 |  | lower | 259 | 259 | not sig. different | not sig. different |  |
| CO | 265 |  | not sig. different | 263 | 267 | not sig. different | not sig. different |  |
| CT | 263 |  | not sig. different | 264 | 270 | lower | not sig. different |  |
| DE | 249 |  | lower | 253 | 260 | lower | lower |  |
| DC | 251 |  | lower | 250 | 250 | not sig. different | not sig. different |  |
| FL | 253 |  | lower | 260 | 263 | lower | lower |  |
| GA | 259 |  | lower | 260 | 262 | not sig. different | not sig. different |  |
| HI | 257 |  | lower | 259 | 258 | not sig. different | not sig. different |  |
| ID | 261 |  | not sig. different | 264 | 266 | lower | not sig. different |  |
| IL | 262 |  | not sig. different | 262 | 265 | not sig. different | not sig. different |  |
| IN | 262 |  | not sig. different | 261 | 266 | lower | not sig. different |  |
| IA | 261 |  | not sig. different | 260 | 262 | not sig. different | not sig. different |  |
| KS | 255 |  | lower | 256 | 263 | lower | not sig. different |  |
| KY | 258 |  | lower | 258 | 263 | lower | not sig. different |  |
| LA | 257 |  | lower | 257 | 257 | not sig. different | not sig. different |  |
| ME | 255 |  | lower | 257 | 265 | lower | not sig. different |  |
| MD | 258 |  | lower | 259 | 264 | lower | not sig. different |  |
| MA | 268 |  | not sig. different | 269 | 273 | lower | not sig. different |  |
| MI | 255 |  | lower | 259 | 263 | lower | not sig. different |  |
| MN | 260 |  | lower | 260 | 264 | lower | not sig. different |  |
| MS | 253 |  | lower | 253 | 256 | not sig. different | not sig. different |  |
| MO | 255 |  | lower | 258 | 263 | lower | not sig. different |  |
| MT | 261 |  | not sig. different | 261 | 265 | lower | not sig. different |  |
| NE | 256 |  | lower | 259 | 264 | lower | lower |  |
| NV | 253 |  | lower | 259 | 258 | lower | lower |  |
| NH | 264 |  | — | 263 | 268 | lower | not sig. different |  |
| NJ | 266 |  | not sig. different | 270 | 270 | lower | not sig. different |  |
| NM | 245 |  | lower | 248 | 252 | lower | not sig. different |  |
| NY | 257 |  | lower | 262 | 262 | not sig. different | not sig. different |  |
| NC | 255 |  | lower | 256 | 263 | lower | not sig. different |  |
| ND | 257 |  | lower | 258 | 263 | lower | not sig. different |  |
| OH | 260 |  | not sig. different | 262 | 267 | lower | not sig. different |  |
| OK | 249 |  | lower | 251 | 258 | lower | not sig. different |  |
| OR | 255 |  | lower | 257 | 264 | lower | not sig. different |  |
| PA | 259 |  | lower | 259 | 264 | lower | not sig. different |  |
| RI | 258 |  | lower | 259 | 262 | lower | not sig. different |  |
| SC | 254 |  | lower | 254 | 259 | lower | not sig. different |  |
| SD | 260 |  | lower | 262 | 263 | lower | not sig. different |  |
| TN | 259 |  | lower | 258 | 262 | not sig. different | not sig. different |  |
| TX | 252 |  | lower | 255 | 256 | not sig. different | not sig. different |  |
| UT | 261 |  | not sig. different | 265 | 267 | lower | lower |  |
| VT | 257 |  | lower | 264 | 268 | lower | lower |  |
| VA | 256 |  | lower | 260 | 262 | lower | not sig. different |  |
| WA | 259 |  | lower | 262 | 266 | lower | not sig. different |  |
| WV | 247 |  | lower | 249 | 256 | lower | not sig. different |  |
| WI | 260 |  | not sig. different | 262 | 267 | lower | not sig. different |  |
| WY | 260 |  | lower | 261 | 265 | lower | not sig. different |  |

## naep_g8_reading_proficient: NAEP Percent at or above NAEP Proficient, Grade 8 Reading

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Reading 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=reading&grade=8&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AP&Year=2019,2022,2024
- source (vs NH): https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=sigacrossjuris&subject=reading&grade=8&subscale=RRPCM&variable=TOTAL&jurisdiction=DS,AL,...,WY&stattype=ALC:AP&Year=2024 (states, DC and DoDEA; the US row uses jurisdiction=NH,NP)
- as_of: 2026-11-08
- raw: raw/national/naep-reading-g8-2019-2022-2024.json; raw/national/naep-reading-g8-2024-sigacrossjuris-proficient-states-DoDEA.json, raw/national/naep-reading-g8-2024-sigacrossjuris-NH-vs-nationalpublic.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file). "2024 vs NH" is NAEP's own significance test of each place against New Hampshire (p < .05, with NAEP's adjustment for comparing many states), run against the same set NAEP's state snapshot reports use (50 states, DC and DoDEA); "higher" means the place is significantly higher than NH.

| Place | Value 2024 | Rank | 2024 vs NH | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|---|
| US | 29 |  | lower | 29 | 32 |  |
| AL | 21 |  | lower | 22 | 24 |  |
| AK | 22 |  | lower | 26 | 23 |  |
| AZ | 25 |  | lower | 28 | 28 |  |
| AR | 25 |  | lower | 26 | 30 |  |
| CA | 28 |  | lower | 30 | 30 |  |
| CO | 35 |  | not sig. different | 34 | 38 |  |
| CT | 35 |  | not sig. different | 35 | 41 |  |
| DE | 23 |  | lower | 24 | 31 |  |
| DC | 25 |  | lower | 22 | 23 |  |
| FL | 25 |  | lower | 29 | 34 |  |
| GA | 31 |  | not sig. different | 31 | 32 |  |
| HI | 29 |  | lower | 31 | 29 |  |
| ID | 32 |  | not sig. different | 32 | 37 |  |
| IL | 33 |  | not sig. different | 32 | 35 |  |
| IN | 33 |  | not sig. different | 31 | 37 |  |
| IA | 31 |  | not sig. different | 29 | 33 |  |
| KS | 25 |  | lower | 26 | 32 |  |
| KY | 29 |  | lower | 29 | 33 |  |
| LA | 27 |  | lower | 27 | 27 |  |
| ME | 26 |  | lower | 29 | 36 |  |
| MD | 33 |  | not sig. different | 33 | 36 |  |
| MA | 40 |  | higher | 40 | 45 |  |
| MI | 24 |  | lower | 28 | 31 |  |
| MN | 28 |  | lower | 30 | 34 |  |
| MS | 23 |  | lower | 22 | 25 |  |
| MO | 26 |  | lower | 28 | 33 |  |
| MT | 31 |  | not sig. different | 29 | 34 |  |
| NE | 27 |  | lower | 29 | 34 |  |
| NV | 26 |  | lower | 29 | 29 |  |
| NH | 34 |  | — | 33 | 38 |  |
| NJ | 38 |  | not sig. different | 42 | 43 |  |
| NM | 19 |  | lower | 18 | 23 |  |
| NY | 31 |  | not sig. different | 32 | 32 |  |
| NC | 27 |  | lower | 26 | 33 |  |
| ND | 25 |  | lower | 27 | 32 |  |
| OH | 32 |  | not sig. different | 33 | 38 |  |
| OK | 20 |  | lower | 21 | 26 |  |
| OR | 27 |  | lower | 28 | 34 |  |
| PA | 31 |  | not sig. different | 31 | 35 |  |
| RI | 30 |  | not sig. different | 31 | 35 |  |
| SC | 26 |  | lower | 27 | 29 |  |
| SD | 29 |  | lower | 31 | 32 |  |
| TN | 31 |  | not sig. different | 28 | 32 |  |
| TX | 25 |  | lower | 23 | 25 |  |
| UT | 31 |  | not sig. different | 36 | 38 |  |
| VT | 29 |  | not sig. different | 34 | 40 |  |
| VA | 29 |  | lower | 31 | 33 |  |
| WA | 31 |  | not sig. different | 32 | 38 |  |
| WV | 21 |  | lower | 22 | 25 |  |
| WI | 31 |  | not sig. different | 32 | 39 |  |
| WY | 29 |  | not sig. different | 30 | 34 |  |

## naep_g8_reading_basic: NAEP Percent at or above NAEP Basic, Grade 8 Reading

- unit: percent
- period: 2024, 2022 and 2019 (each tested January–March of that year); year: 2024
- source: NAEP Data Service (NCES), NAEP Reading 2024, 2022, 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=reading&grade=8&subscale=RRPCM&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=ALC:AB&Year=2019,2022,2024
- as_of: 2026-11-08
- raw: raw/national/naep-reading-g8-2019-2022-2024.json
- note: Public schools. "US" is the national public average. Values are rounded to whole numbers, as NAEP reports them (unrounded values are in the raw file).

| Place | Value 2024 | Rank | Value 2022 | Value 2019 | Note |
|---|---|---|---|---|---|
| US | 66 |  | 68 | 72 |  |
| AL | 59 |  | 61 | 64 |  |
| AK | 57 |  | 63 | 63 |  |
| AZ | 65 |  | 68 | 70 |  |
| AR | 65 |  | 64 | 68 |  |
| CA | 63 |  | 67 | 68 |  |
| CO | 74 |  | 73 | 77 |  |
| CT | 70 |  | 72 | 78 |  |
| DE | 59 |  | 62 | 69 |  |
| DC | 58 |  | 57 | 58 |  |
| FL | 63 |  | 69 | 72 |  |
| GA | 68 |  | 69 | 72 |  |
| HI | 67 |  | 68 | 68 |  |
| ID | 71 |  | 74 | 77 |  |
| IL | 70 |  | 71 | 74 |  |
| IN | 69 |  | 70 | 75 |  |
| IA | 72 |  | 71 | 73 |  |
| KS | 66 |  | 67 | 74 |  |
| KY | 67 |  | 68 | 73 |  |
| LA | 66 |  | 66 | 68 |  |
| ME | 65 |  | 66 | 75 |  |
| MD | 66 |  | 67 | 73 |  |
| MA | 75 |  | 77 | 81 |  |
| MI | 65 |  | 68 | 73 |  |
| MN | 71 |  | 72 | 74 |  |
| MS | 64 |  | 63 | 67 |  |
| MO | 65 |  | 67 | 74 |  |
| MT | 70 |  | 72 | 76 |  |
| NE | 67 |  | 70 | 74 |  |
| NV | 62 |  | 68 | 69 |  |
| NH | 74 |  | 73 | 78 |  |
| NJ | 73 |  | 77 | 77 |  |
| NM | 54 |  | 57 | 61 |  |
| NY | 65 |  | 70 | 70 |  |
| NC | 65 |  | 66 | 72 |  |
| ND | 68 |  | 69 | 75 |  |
| OH | 69 |  | 71 | 75 |  |
| OK | 59 |  | 62 | 71 |  |
| OR | 65 |  | 67 | 73 |  |
| PA | 69 |  | 68 | 73 |  |
| RI | 66 |  | 68 | 71 |  |
| SC | 64 |  | 63 | 69 |  |
| SD | 70 |  | 73 | 74 |  |
| TN | 68 |  | 67 | 73 |  |
| TX | 61 |  | 66 | 67 |  |
| UT | 72 |  | 75 | 77 |  |
| VT | 67 |  | 73 | 77 |  |
| VA | 66 |  | 69 | 71 |  |
| WA | 69 |  | 71 | 74 |  |
| WV | 58 |  | 60 | 67 |  |
| WI | 70 |  | 72 | 76 |  |
| WY | 70 |  | 71 | 75 |  |

## naep_g8_science: NAEP Grade 8 Science (National Only)

- unit: score
- period: 2024 and 2019; year: 2024
- source: NAEP Data Service (NCES), NAEP Science 2024 and 2019 — https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=science&grade=8&subscale=SRPUV&variable=TOTAL&jurisdiction=NP,AL,...,WY&stattype=MN:MN,ALC:AB,ALC:AP&Year=2019,2024
- as_of: 2026-11-08
- raw: raw/national/naep-science-g8-2019-2024.json
- note: Public schools; "US" = national public. NAEP 2024 grade 8 science reported national results only: the Data Service returns no state values (error flag 320) for NH or any state in 2024 or 2019, and NCES titled the report "2024 NAEP Science Assessment: Grade 8 Results for the Nation" (NCES 2024222, September 2025; https://ies.ed.gov/use-work/resource-library/report/statistical-analysis-report/2024-naep-science-assessment-grade-8-results-nation). Rounded to whole numbers as NAEP reports them.

| Place | Value 2024 (average score) | Rank | 2024 % at/above Proficient | 2024 % at/above Basic | 2019 average score | 2019 % at/above Proficient | 2019 % at/above Basic | Note |
|---|---|---|---|---|---|---|---|---|
| US | 149 |  | 30 | 61 | 153 | 33 | 66 |  |
| NH | n/a |  | n/a | n/a | n/a | n/a | n/a | No state results in 2024 or 2019 |

# How each state's "proficient" bar maps onto NAEP

## naep_equivalent_state_standard_g4r: Where Each State's "Proficient" Bar Falls on the NAEP Scale, Grade 4 Reading

- unit: score
- period: 2021-22 state tests mapped onto NAEP 2022; year: 2022
- source: NCES, Mapping State Proficiency Standards Onto the NAEP Scales: Results From the 2022 NAEP Reading and Mathematics Assessments (NCES 2026-014, Yee & Cramer, February 2026) — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf ; values from its Technical Notes (NCES 2026-014-A), Tables A-1 and A-2 — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014a.pdf
- as_of: 2026-11-08
- raw: raw/national/nces-2026014-state-mapping.pdf; raw/national/nces-2026014a-state-mapping-technical-notes.pdf
- note: Value = the "NAEP equivalent score" of the state's standard for proficient performance on its own 2021-22 test: the NAEP score that the same share of the state's students reached in 2022. NAEP cut scores for grade 4 reading: NAEP Basic 208, NAEP Proficient 238 (NCES 2026-014 Table 3). "Level" comes from the lists in NCES's report text (states named at NAEP Proficient or below NAEP Basic; every other state included is at NAEP Basic; this column is **derived** from those lists). NCES classifies a standard at the highest level whose cut score is within the upper bound of the margin of error (score + 2 standard errors). For states in the Smarter Balanced consortium (SBAC), the report classifies SBAC as a whole (NAEP Basic in all four); the state's own estimate is shown. "Caution" = NCES flags relative error greater than 0.5. "—" = not included in this grade/subject (Maine in all four; 11 more states in grade 8 math, mostly because of end-of-course testing). The study covers public schools; there is no "US" value.

| Place | Value | Rank | Standard error | Level (derived from NCES lists) | Testing program | Note |
|---|---|---|---|---|---|---|
| AL | 213 |  | 1.4 | NAEP Basic | State test |  |
| AK | 236 |  | 2.1 | NAEP Proficient | State test |  |
| AZ | 225 |  | 1.5 | NAEP Basic | State test |  |
| AR | 229 |  | 1.0 | NAEP Basic | State test |  |
| CA | 224 |  | 1.3 | NAEP Basic (SBAC as a whole) | SBAC |  |
| CO | 233 |  | 1.0 | NAEP Basic | State test |  |
| CT | 222 |  | 1.2 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DE | 223 |  | 1.4 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DC | 233 |  | 2.7 | NAEP Proficient | State test |  |
| FL | 221 |  | 1.0 | NAEP Basic | State test |  |
| GA | 232 |  | 0.9 | NAEP Basic | State test |  |
| HI | 221 |  | 1.2 | NAEP Basic | State test |  |
| ID | 221 |  | 2.1 | NAEP Basic (SBAC as a whole) | SBAC |  |
| IL | 237 |  | 2.1 | NAEP Proficient | State test |  |
| IN | 232 |  | 1.1 | NAEP Basic | State test |  |
| IA | 197 |  | 2.1 | Below NAEP Basic | State test |  |
| KS | 226 |  | 1.2 | NAEP Basic | State test |  |
| KY | 223 |  | 1.0 | NAEP Basic | State test |  |
| LA | 220 |  | 1.4 | NAEP Basic | State test |  |
| ME | — |  |  |  |  | Not included in this grade/subject |
| MD | 223 |  | 1.2 | NAEP Basic | State test |  |
| MA | 242 |  | 1.6 | NAEP Proficient | State test |  |
| MI | 225 |  | 1.7 | NAEP Basic | State test |  |
| MN | 223 |  | 1.5 | NAEP Basic | State test |  |
| MS | 226 |  | 1.2 | NAEP Basic | State test |  |
| MO | 224 |  | 1.8 | NAEP Basic | State test |  |
| MT | 228 |  | 1.0 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NE | 222 |  | 1.2 | NAEP Basic | State test |  |
| NV | 222 |  | 1.5 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NH | 228 |  | 1.3 | NAEP Basic | State test |  |
| NJ | 229 |  | 1.4 | NAEP Basic | State test |  |
| NM | 222 |  | 2.0 | NAEP Basic | State test |  |
| NY | 227 |  | 1.7 | NAEP Basic | State test |  |
| NC | 233 |  | 1.4 | NAEP Basic | State test |  |
| ND | 230 |  | 1.0 | NAEP Basic | State test |  |
| OH | 208 |  | 2.1 | NAEP Basic | State test |  |
| OK | 240 |  | 1.7 | NAEP Proficient | State test |  |
| OR | 223 |  | 2.0 | NAEP Basic (SBAC as a whole) | SBAC |  |
| PA | 220 |  | 1.4 | NAEP Basic | State test |  |
| RI | 242 |  | 1.5 | NAEP Proficient | State test |  |
| SC | 218 |  | 2.1 | NAEP Basic | State test |  |
| SD | 222 |  | 1.1 | NAEP Basic (SBAC as a whole) | SBAC |  |
| TN | 228 |  | 1.9 | NAEP Basic | State test |  |
| TX | 215 |  | 1.2 | NAEP Basic | State test |  |
| UT | 233 |  | 1.2 | NAEP Basic | State test |  |
| VT | 228 |  | 1.9 | NAEP Basic (SBAC as a whole) | SBAC |  |
| VA | 193 |  | 1.7 | Below NAEP Basic | State test |  |
| WA | 222 |  | 1.9 | NAEP Basic (SBAC as a whole) | SBAC |  |
| WV | 218 |  | 1.4 | NAEP Basic | State test |  |
| WI | 228 |  | 1.5 | NAEP Basic | State test |  |
| WY | 231 |  | 1.4 | NAEP Basic | State test |  |

## naep_equivalent_state_standard_g4m: Where Each State's "Proficient" Bar Falls on the NAEP Scale, Grade 4 Math

- unit: score
- period: 2021-22 state tests mapped onto NAEP 2022; year: 2022
- source: NCES, Mapping State Proficiency Standards Onto the NAEP Scales: Results From the 2022 NAEP Reading and Mathematics Assessments (NCES 2026-014, Yee & Cramer, February 2026) — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf ; values from its Technical Notes (NCES 2026-014-A), Tables A-1 and A-2 — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014a.pdf
- as_of: 2026-11-08
- raw: raw/national/nces-2026014-state-mapping.pdf; raw/national/nces-2026014a-state-mapping-technical-notes.pdf
- note: Value = the "NAEP equivalent score" of the state's standard for proficient performance on its own 2021-22 test: the NAEP score that the same share of the state's students reached in 2022. NAEP cut scores for grade 4 math: NAEP Basic 214, NAEP Proficient 249 (NCES 2026-014 Table 3). "Level" comes from the lists in NCES's report text (states named at NAEP Proficient or below NAEP Basic; every other state included is at NAEP Basic; this column is **derived** from those lists). NCES classifies a standard at the highest level whose cut score is within the upper bound of the margin of error (score + 2 standard errors). For states in the Smarter Balanced consortium (SBAC), the report classifies SBAC as a whole (NAEP Basic in all four); the state's own estimate is shown. "Caution" = NCES flags relative error greater than 0.5. "—" = not included in this grade/subject (Maine in all four; 11 more states in grade 8 math, mostly because of end-of-course testing). The study covers public schools; there is no "US" value.

| Place | Value | Rank | Standard error | Level (derived from NCES lists) | Testing program | Note |
|---|---|---|---|---|---|---|
| AL | 245 |  | 0.7 | NAEP Basic | State test |  |
| AK | 254 |  | 1.7 | NAEP Proficient | State test |  |
| AZ | 240 |  | 1.3 | NAEP Basic | State test |  |
| AR | 237 |  | 1.1 | NAEP Basic | State test |  |
| CA | 241 |  | 0.8 | NAEP Basic (SBAC as a whole) | SBAC |  |
| CO | 253 |  | 1.5 | NAEP Proficient | State test |  |
| CT | 240 |  | 1.1 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DE | 241 |  | 1.0 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DC | 252 |  | 1.4 | NAEP Proficient | State test |  |
| FL | 232 |  | 1.0 | NAEP Basic | State test |  |
| GA | 242 |  | 1.4 | NAEP Basic | State test |  |
| HI | 242 |  | 0.9 | NAEP Basic | State test |  |
| ID | 241 |  | 1.0 | NAEP Basic (SBAC as a whole) | SBAC |  |
| IL | 257 |  | 1.8 | NAEP Proficient | State test |  |
| IN | 244 |  | 1.4 | NAEP Basic | State test |  |
| IA | 226 |  | 1.4 | NAEP Basic | State test |  |
| KS | 249 |  | 1.2 | NAEP Proficient | State test |  |
| KY | 241 |  | 1.2 | NAEP Basic | State test |  |
| LA | 241 |  | 0.9 | NAEP Basic | State test |  |
| ME | — |  |  |  |  | Not included in this grade/subject |
| MD | 254 |  | 1.3 | NAEP Proficient | State test |  |
| MA | 249 |  | 1.4 | NAEP Proficient | State test |  |
| MI | 246 |  | 1.2 | NAEP Basic | State test |  |
| MN | 239 |  | 1.3 | NAEP Basic | State test |  |
| MS | 237 |  | 1.0 | NAEP Basic | State test |  |
| MO | 242 |  | 1.0 | NAEP Basic | State test |  |
| MT | 246 |  | 1.3 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NE | 247 |  | 1.2 | NAEP Proficient | State test |  |
| NV | 244 |  | 1.8 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NH | 243 |  | 0.8 | NAEP Basic | State test |  |
| NJ | 249 |  | 1.9 | NAEP Proficient | State test |  |
| NM | 245 |  | 1.4 | NAEP Basic | State test |  |
| NY | 236 |  | 1.8 | NAEP Basic | State test |  |
| NC | 249 |  | 1.4 | NAEP Proficient | State test |  |
| ND | 252 |  | 1.0 | NAEP Proficient | State test |  |
| OH | 225 |  | 1.6 | NAEP Basic | State test |  |
| OK | 245 |  | 0.9 | NAEP Basic | State test |  |
| OR | 242 |  | 1.3 | NAEP Basic (SBAC as a whole) | SBAC |  |
| PA | 247 |  | 1.2 | NAEP Proficient | State test |  |
| RI | 250 |  | 0.9 | NAEP Proficient | State test |  |
| SC | 241 |  | 1.8 | NAEP Basic | State test |  |
| SD | 243 |  | 0.9 | NAEP Basic (SBAC as a whole) | SBAC |  |
| TN | 245 |  | 0.9 | NAEP Basic | State test |  |
| TX | 246 |  | 1.3 | NAEP Basic | State test |  |
| UT | 244 |  | 1.7 | NAEP Basic | State test |  |
| VT | 247 |  | 1.1 | NAEP Basic (SBAC as a whole) | SBAC |  |
| VA | 224 |  | 1.5 | NAEP Basic | State test |  |
| WA | 240 |  | 1.2 | NAEP Basic (SBAC as a whole) | SBAC |  |
| WV | 236 |  | 1.0 | NAEP Basic | State test |  |
| WI | 246 |  | 1.1 | NAEP Basic | State test |  |
| WY | 242 |  | 1.2 | NAEP Basic | State test |  |

## naep_equivalent_state_standard_g8r: Where Each State's "Proficient" Bar Falls on the NAEP Scale, Grade 8 Reading

- unit: score
- period: 2021-22 state tests mapped onto NAEP 2022; year: 2022
- source: NCES, Mapping State Proficiency Standards Onto the NAEP Scales: Results From the 2022 NAEP Reading and Mathematics Assessments (NCES 2026-014, Yee & Cramer, February 2026) — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf ; values from its Technical Notes (NCES 2026-014-A), Tables A-1 and A-2 — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014a.pdf
- as_of: 2026-11-08
- raw: raw/national/nces-2026014-state-mapping.pdf; raw/national/nces-2026014a-state-mapping-technical-notes.pdf
- note: Value = the "NAEP equivalent score" of the state's standard for proficient performance on its own 2021-22 test: the NAEP score that the same share of the state's students reached in 2022. NAEP cut scores for grade 8 reading: NAEP Basic 243, NAEP Proficient 281 (NCES 2026-014 Table 3). "Level" comes from the lists in NCES's report text (states named at NAEP Proficient or below NAEP Basic; every other state included is at NAEP Basic; this column is **derived** from those lists). NCES classifies a standard at the highest level whose cut score is within the upper bound of the margin of error (score + 2 standard errors). For states in the Smarter Balanced consortium (SBAC), the report classifies SBAC as a whole (NAEP Basic in all four); the state's own estimate is shown. "Caution" = NCES flags relative error greater than 0.5. "—" = not included in this grade/subject (Maine in all four; 11 more states in grade 8 math, mostly because of end-of-course testing). The study covers public schools; there is no "US" value.

| Place | Value | Rank | Standard error | Level (derived from NCES lists) | Testing program | Note |
|---|---|---|---|---|---|---|
| AL | 251 |  | 1.8 | NAEP Basic | State test |  |
| AK | 279 |  | 0.9 | NAEP Basic | State test |  |
| AZ | 276 |  | 1.6 | NAEP Basic | State test |  |
| AR | 261 |  | 1.6 | NAEP Basic | State test |  |
| CA | 265 |  | 1.5 | NAEP Basic (SBAC as a whole) | SBAC |  |
| CO | 271 |  | 2.1 | NAEP Basic | State test |  |
| CT | 265 |  | 1.3 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DE | 264 |  | 1.9 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DC | 269 |  | 1.1 | NAEP Basic | State test |  |
| FL | 265 |  | 1.4 | NAEP Basic | State test |  |
| GA | 271 |  | 1.3 | NAEP Basic | State test |  |
| HI | 263 |  | 1.9 | NAEP Basic | State test |  |
| ID | 262 |  | 1.5 | NAEP Basic (SBAC as a whole) | SBAC |  |
| IL | 285 |  | 1.3 | NAEP Proficient | State test |  |
| IN | 271 |  | 1.3 | NAEP Basic | State test |  |
| IA | 238 |  | 2.2 | Below NAEP Basic | State test |  |
| KS | 287 |  | 1.3 | NAEP Proficient | State test |  |
| KY | 267 |  | 1.4 | NAEP Basic | State test |  |
| LA | 262 |  | 1.4 | NAEP Basic | State test |  |
| ME | — |  |  |  |  | Not included in this grade/subject |
| MD | 272 |  | 1.0 | NAEP Basic | State test |  |
| MA | 279 |  | 1.3 | NAEP Proficient | State test |  |
| MI | 251 |  | 1.6 | NAEP Basic | State test |  |
| MN | 266 |  | 1.1 | NAEP Basic | State test |  |
| MS | 269 |  | 1.7 | NAEP Basic | State test |  |
| MO | 268 |  | 1.7 | NAEP Basic | State test |  |
| MT | 269 |  | 1.0 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NE | 266 |  | 1.2 | NAEP Basic | State test |  |
| NV | 267 |  | 1.0 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NH | 269 |  | 1.5 | NAEP Basic | State test |  |
| NJ | 271 |  | 1.5 | NAEP Basic | State test |  |
| NM | 266 |  | 1.1 | NAEP Basic | State test |  |
| NY | 263 |  | 1.8 | NAEP Basic | State test |  |
| NC | 277 |  | 1.4 | NAEP Basic | State test |  |
| ND | 266 |  | 1.3 | NAEP Basic | State test | Caution (relative error > 0.5) |
| OH | 262 |  | 1.5 | NAEP Basic | State test |  |
| OK | 276 |  | 1.3 | NAEP Basic | State test |  |
| OR | 268 |  | 0.9 | NAEP Basic (SBAC as a whole) | SBAC |  |
| PA | 256 |  | 1.3 | NAEP Basic | State test |  |
| RI | 283 |  | 1.2 | NAEP Proficient | State test |  |
| SC | 261 |  | 1.5 | NAEP Basic | State test |  |
| SD | 266 |  | 1.3 | NAEP Basic (SBAC as a whole) | SBAC |  |
| TN | 283 |  | 1.2 | NAEP Proficient | State test |  |
| TX | 251 |  | 1.3 | NAEP Basic | State test |  |
| UT | 273 |  | 2.2 | NAEP Basic | State test |  |
| VT | 273 |  | 1.1 | NAEP Basic (SBAC as a whole) | SBAC |  |
| VA | 238 |  | 1.8 | Below NAEP Basic | State test |  |
| WA | 263 |  | 1.7 | NAEP Basic (SBAC as a whole) | SBAC |  |
| WV | 264 |  | 2.4 | NAEP Basic | State test |  |
| WI | 281 |  | 0.9 | NAEP Proficient | State test |  |
| WY | 256 |  | 1.2 | NAEP Basic | State test |  |

## naep_equivalent_state_standard_g8m: Where Each State's "Proficient" Bar Falls on the NAEP Scale, Grade 8 Math

- unit: score
- period: 2021-22 state tests mapped onto NAEP 2022; year: 2022
- source: NCES, Mapping State Proficiency Standards Onto the NAEP Scales: Results From the 2022 NAEP Reading and Mathematics Assessments (NCES 2026-014, Yee & Cramer, February 2026) — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014.pdf ; values from its Technical Notes (NCES 2026-014-A), Tables A-1 and A-2 — https://nces.ed.gov/nationsreportcard/subject/publications/studies/pdf/2026014a.pdf
- as_of: 2026-11-08
- raw: raw/national/nces-2026014-state-mapping.pdf; raw/national/nces-2026014a-state-mapping-technical-notes.pdf
- note: Value = the "NAEP equivalent score" of the state's standard for proficient performance on its own 2021-22 test: the NAEP score that the same share of the state's students reached in 2022. NAEP cut scores for grade 8 math: NAEP Basic 262, NAEP Proficient 299 (NCES 2026-014 Table 3). "Level" comes from the lists in NCES's report text (states named at NAEP Proficient or below NAEP Basic; every other state included is at NAEP Basic; this column is **derived** from those lists). NCES classifies a standard at the highest level whose cut score is within the upper bound of the margin of error (score + 2 standard errors). For states in the Smarter Balanced consortium (SBAC), the report classifies SBAC as a whole (NAEP Basic in all four); the state's own estimate is shown. "Caution" = NCES flags relative error greater than 0.5. "—" = not included in this grade/subject (Maine in all four; 11 more states in grade 8 math, mostly because of end-of-course testing). The study covers public schools; there is no "US" value.

| Place | Value | Rank | Standard error | Level (derived from NCES lists) | Testing program | Note |
|---|---|---|---|---|---|---|
| AL | 297 |  | 1.1 | NAEP Basic | State test |  |
| AK | 315 |  | 1.3 | NAEP Proficient | State test |  |
| AZ | 296 |  | 1.7 | NAEP Proficient | State test |  |
| AR | 278 |  | 1.0 | NAEP Basic | State test |  |
| CA | 289 |  | 1.4 | NAEP Basic (SBAC as a whole) | SBAC |  |
| CO | 292 |  | 2.4 | NAEP Basic | State test |  |
| CT | 293 |  | 1.5 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DE | 292 |  | 1.1 | NAEP Basic (SBAC as a whole) | SBAC |  |
| DC | — |  |  |  |  | Not included in this grade/subject |
| FL | — |  |  |  |  | Not included in this grade/subject |
| GA | 283 |  | 1.1 | NAEP Basic | State test |  |
| HI | 289 |  | 2.0 | NAEP Basic | State test |  |
| ID | 296 |  | 1.2 | NAEP Basic (SBAC as a whole) | SBAC | Caution (relative error > 0.5) |
| IL | 304 |  | 1.4 | NAEP Proficient | State test |  |
| IN | 302 |  | 1.6 | NAEP Proficient | State test |  |
| IA | 262 |  | 1.6 | NAEP Basic | State test |  |
| KS | 302 |  | 1.6 | NAEP Proficient | State test |  |
| KY | 282 |  | 1.4 | NAEP Basic | State test |  |
| LA | — |  |  |  |  | Not included in this grade/subject |
| ME | — |  |  |  |  | Not included in this grade/subject |
| MD | — |  |  |  |  | Not included in this grade/subject |
| MA | 297 |  | 1.1 | NAEP Proficient | State test |  |
| MI | 287 |  | 1.0 | NAEP Basic | State test |  |
| MN | 290 |  | 1.2 | NAEP Basic | State test |  |
| MS | 272 |  | 1.8 | NAEP Basic | State test |  |
| MO | 283 |  | 1.1 | NAEP Basic | State test | End-of-course tests; under 95% took the end-of-grade test (NCES Fig. 10 note) |
| MT | 299 |  | 1.4 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NE | 289 |  | 1.2 | NAEP Basic | State test |  |
| NV | 297 |  | 1.7 | NAEP Basic (SBAC as a whole) | SBAC |  |
| NH | 295 |  | 0.8 | NAEP Basic | State test | End-of-course tests; under 95% took the end-of-grade test (NCES Fig. 10 note) |
| NJ | — |  |  |  |  | Not included in this grade/subject |
| NM | 289 |  | 2.2 | NAEP Basic | State test |  |
| NY | — |  |  |  |  | Not included in this grade/subject |
| NC | — |  |  |  |  | Not included in this grade/subject |
| ND | 293 |  | 1.4 | NAEP Basic | State test | Caution (relative error > 0.5) |
| OH | — |  |  |  |  | Not included in this grade/subject |
| OK | 298 |  | 1.8 | NAEP Proficient | State test |  |
| OR | 297 |  | 2.0 | NAEP Basic (SBAC as a whole) | SBAC |  |
| PA | 304 |  | 1.3 | NAEP Proficient | State test |  |
| RI | 303 |  | 1.0 | NAEP Proficient | State test |  |
| SC | 289 |  | 1.3 | NAEP Basic | State test |  |
| SD | 295 |  | 1.6 | NAEP Basic (SBAC as a whole) | SBAC |  |
| TN | — |  |  |  |  | Not included in this grade/subject |
| TX | — |  |  |  |  | Not included in this grade/subject |
| UT | 293 |  | 2.1 | NAEP Basic | State test |  |
| VT | 298 |  | 1.9 | NAEP Basic (SBAC as a whole) | SBAC |  |
| VA | — |  |  |  |  | Not included in this grade/subject |
| WA | 292 |  | 1.1 | NAEP Basic (SBAC as a whole) | SBAC |  |
| WV | 283 |  | 1.2 | NAEP Basic | State test |  |
| WI | 302 |  | 1.2 | NAEP Proficient | State test |  |
| WY | 283 |  | 1.3 | NAEP Basic | State test |  |

# Graduation

## acgr_2023_by_group: Four-Year Graduation Rate (ACGR), Class of 2023, by Student Group

- unit: percent
- period: School year 2022-23 (class of 2023); year: 2023
- source: U.S. Department of Education, ED Data Express, EDFacts file specs 150/151, data groups 695/696 (SEA level), SY 2022-23 — https://eddataexpress.ed.gov/sites/default/files/data_download/EID_15488/SY2223_FS150_FS151_DG695_DG696_SEA_data_files.zip (listed in the ED Data Express Data Library, https://eddataexpress.ed.gov/download/data-library)
- as_of: 2026-11-08
- raw: raw/national/eddataexpress-SY2223_FS150_FS151_DG695_DG696_SEA_data_files.zip
- note: Public high schools. This is the newest state-level ACGR file in the ED Data Express Data Library as of 2026-11-08 (the NCES Digest table stops at 2021-22). Values are copied as the file gives them; values with ">=" or "<=" were blurred (rounded) by ED to protect privacy, and small groups are reported as whole numbers. "Cohort" is the adjusted cohort count (the denominator) for all students. Groups are as the file names them: "Students with disabilities" = Children with disabilities (IDEA); "Two or more races" = Multicultural/Multiethnic/Multiracial/other. "N/A" = reported as not available in the file; "—" = the file has no row for that group in that state. The file also has foster care and homeless rates (in the raw file).

| Place | Value (all students) | Rank | Cohort | Students with disabilities | English learners | Economically disadvantaged | American Indian/Alaska Native | Asian/Pacific Islander | Black | Hispanic | White | Two or more races | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 86.70 |  | 3838338 | 72.60 | 73.10 | 81.90 | 74.60 | 93.40 | 82.00 | 82.90 | 90.00 | N/A |  |
| AL | 90 |  | 52928 | 77.70 | 72 | 86.50 | 92 | 93 | 87.70 | 86.40 | 91.80 | 90 |  |
| AK | 77.90 |  | 9629 | 57 | 65 | 72.40 | 67 | 83 | 65 | 77 | 83.90 | 74 |  |
| AZ | 77.80 |  | 93470 | 73.40 | 62.10 | 76.90 | 67.50 | 91.30 | 72.20 | 74.90 | 84.10 | 82 |  |
| AR | 89.90 |  | 35156 | 86.10 | 84.40 | 87.30 | 87 | 91 | 87 | 88.50 | 91.30 | 88 |  |
| CA | 86.20 |  | 495492 | 71.90 | 72.50 | 83.30 | 79 | 94.10 | 77.90 | 83.90 | 89.70 | 86.70 |  |
| CO | 82.70 |  | 68390 | 65.70 | 68.70 | 72.80 | 67 | 91 | 77.90 | 75.60 | 87.60 | 83 |  |
| CT | 88.20 |  | 40732 | 70.90 | 72 | 81.90 | 87 | 96 | 81.10 | 80.80 | 93.30 | 88 |  |
| DE | 88.90 |  | 10914 | 74 | 74 | 82 | 86 | 95 | 87.80 | 83 | 91.50 | 93 |  |
| DC | 76.50 |  | 4759 | 63 | 58 | 69 | >=50 | 93 | 74.70 | 71 | 98 | 94 |  |
| FL | 88 |  | 208274 | 85.60 | 76.20 | 83.90 | 85 | 96.30 | 83.30 | 86.90 | 91 | 88.50 |  |
| GA | 84.40 |  | 134822 | 73.20 | 66 | 80.80 | 82 | 94 | 83.70 | 77.60 | 87.10 | 82.50 |  |
| HI | 85.50 |  | 12943 | 64 | 69 | 80.40 | — | 85.60 | 86 | 80 | 86 | — |  |
| ID | 81.10 |  | 25525 | 56 | 67 | 70.80 | 70 | 86 | 72 | 73.50 | 83.50 | 77 |  |
| IL | 87.60 |  | 149998 | 72.30 | 77.30 | 81.20 | 82 | 94.60 | 80.20 | 85.60 | 90.80 | 84.30 |  |
| IN | 88.10 |  | 77216 | 82.90 | 87 | 88.60 | 78 | 96 | 81 | 86.60 | 90.30 | 83 |  |
| IA | 87.50 |  | 38026 | 67.90 | 74 | 78.60 | 74 | 85 | 75 | 79.60 | 90.30 | 80 |  |
| KS | 88 |  | 36783 | 81.90 | 85.30 | 83.10 | 85 | 93 | 82 | 84.30 | 89.90 | 85 |  |
| KY | 91.40 |  | 49023 | 81 | 78 | 90 | >=95 | 96 | 87 | 85.90 | 92.60 | 90 |  |
| LA | 82.60 |  | 50762 | 78.10 | 44 | 77.20 | 82 | 92 | 79.40 | 67.80 | 88.30 | 84 |  |
| ME | 87.30 |  | 13941 | 74 | 71 | 78.80 | 69 | 90 | 81 | 78 | 88.20 | 82 |  |
| MD | 85.80 |  | 67829 | 69.50 | 55.80 | 79.80 | 86 | 96 | 84.70 | 71.40 | 93.40 | 89 |  |
| MA | 89.20 |  | 72602 | 76.40 | 67.30 | 82.20 | 83 | 95.10 | 85.60 | 78.90 | 93 | 89 |  |
| MI | 81.80 |  | 115301 | 59.60 | 75.10 | 71.30 | 72 | 93.20 | 71.30 | 76.80 | 85 | 75.30 |  |
| MN | 83.30 |  | 69945 | 65.60 | 63.30 | 71.90 | 55 | 85.10 | 72.10 | 68.90 | 88.70 | 78.10 |  |
| MS | 89.40 |  | 31998 | 70 | 64 | 87 | 80 | 96 | 88.20 | 85 | 91.10 | 88 |  |
| MO | 89.30 |  | 67017 | 78.40 | 76 | 82.70 | 86 | 93 | 79.50 | 86.10 | 91.70 | 89 |  |
| MT | 85.50 |  | 10838 | 75 | 65 | 75 | 66 | 94 | 77 | 79 | 89.20 | 79 |  |
| NE | 87.30 |  | 24336 | 67 | 53 | 79.10 | 74 | 88 | 76 | 76.70 | 92.40 | 81 |  |
| NV | 81.40 |  | 38348 | 66.80 | 72.80 | 81.40 | 65 | 90.60 | 70.50 | 80 | 85.60 | 82 |  |
| NH | 88.10 |  | 13202 | 75 | 74 | 75.30 | 84 | 95 | 82 | 78 | 88.90 | 88 |  |
| NJ | 90.50 |  | 106157 | 77.40 | 73.40 | 85.90 | 90 | 96.50 | 85.90 | 85.30 | 94.40 | 92 |  |
| NM | 76.50 |  | 25411 | 67.50 | 75.90 | 66.10 | 72 | 89 | 70 | 76.20 | 79.60 | 75 |  |
| NY | 87.20 |  | 202009 | 68.60 | 65 | 82.60 | 82 | 93.30 | 82.10 | 81 | 91.60 | 86.30 |  |
| NC | 86.50 |  | 120822 | 71.60 | 66.10 | 83.60 | 80 | 94.70 | 84 | 81.10 | 89.80 | 83.50 |  |
| ND | 83.20 |  | 8249 | 64 | 70 | 70 | 65 | 80 | 70 | 70 | 88.20 | — |  |
| OH | 86.20 |  | 132008 | 64.80 | 70.30 | 77 | 76 | 94.30 | 75.80 | 77.10 | 89.30 | 82.50 |  |
| OK | 81.20 |  | 52179 | 71.80 | 64.60 | 74.80 | 82.90 | 86 | 77 | 77.70 | 82.50 | 80.70 |  |
| OR | 81.30 |  | 46371 | 68.60 | 68.10 | 80.70 | 68 | 89 | 73 | 78.60 | 82.60 | 79.80 |  |
| PA | 87.50 |  | 136045 | 75.50 | 68.60 | 82 | 81 | 94 | 79.80 | 76.70 | 91.40 | 82 |  |
| RI | 84.10 |  | 11062 | 66 | 69 | 76.50 | 74 | 90 | 82 | 77.20 | 88.30 | 78 |  |
| SC | 83.80 |  | 59540 | 58.10 | 76.60 | 76.40 | 80 | 93 | 79.70 | 79.80 | 87.20 | — |  |
| SD | 84 |  | 9963 | 65 | 89 | 66 | 48 | 94 | 82 | 70 | 90.50 | 79 |  |
| TN | 87.30 |  | 71510 | 51.90 | 63.50 | 80.10 | 87 | 95 | 84.30 | 80 | 89.70 | — |  |
| TX | 90.30 |  | 403301 | 80.70 | 82.40 | 87.40 | 89 | 96.60 | 86.70 | 88.60 | 94.20 | 91.70 |  |
| UT | 88.30 |  | 52066 | 73.80 | 77.30 | 78.70 | 77 | 86 | 81 | 81 | 90.70 | 87 |  |
| VT | 82 |  | 5828 | 71 | 69 | 72 | >=50 | 88 | 73 | 80 | 82.30 | 80 |  |
| VA | 88.80 |  | 99059 | 69.80 | 66.40 | 82.60 | — | 95.80 | 86.60 | 77.50 | 92.60 | 90.80 |  |
| WA | 83.80 |  | 85003 | 66.90 | 70.70 | 77 | 71 | 90.40 | 81.50 | 78.80 | 85.20 | 84.90 |  |
| WV | 92.60 |  | 18443 | 85.50 | 84 | 88 | >=80 | >=95 | 90 | 92 | 92.80 | 90 |  |
| WI | 90.50 |  | 65638 | 73.50 | 76.70 | 82.50 | 74 | 92 | 71.10 | 83.50 | 94.70 | 88 |  |
| WY | 81.40 |  | 7475 | 60 | 70 | 69.40 | 52 | 88 | 73 | 76 | 83.80 | 75 |  |

## acgr_2022_by_group: Four-Year Graduation Rate (ACGR), Class of 2022, by Student Group

- unit: percent
- period: School year 2021-22 (class of 2022); all-students rates also for 2020-21 and 2018-19; year: 2022
- source: NCES, Digest of Education Statistics 2023, Table 219.46 (prepared January 2024; still the current version per the Digest "current tables" list on 2026-11-08) — https://nces.ed.gov/programs/digest/d23/tables/dt23_219.46.asp
- as_of: 2026-11-08
- raw: raw/national/nces-digest-d23-219.46.xlsx (values), raw/national/nces-digest-d23-219.46.html (web page)
- note: Public high schools. Values are the cells of NCES's Excel file for the table (one decimal where NCES stored one; the web page shows the same values rounded to whole numbers). "---" = not available; "‡" = reporting standards not met; ">=" values were blurred (rounded) for privacy. Race groups exclude Hispanic students; "Asian/Pacific Islander" is the table's Total column for that group. The Digest notes that in 2019-20 some states changed diploma requirements because of the pandemic.

| Place | Value 2021-22 (all) | Rank | Value 2020-21 (all) | Value 2018-19 (all) | Students with disabilities | English learners | Economically disadvantaged | American Indian/Alaska Native | Asian/Pacific Islander | Black | Hispanic | White | Two or more races | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 86.6 |  | 86.1 | 85.8 | 71.4 | 72.1 | 81.3 | 73.9 | 93.7 | 81 | 82.8 | 89.8 | --- |  |
| AL | 88.2 |  | 90.7 | 91.7 | 73.5 | 68 | 82.6 | 88 | 94 | 85.2 | 83.8 | 90.4 | 90 |  |
| AK | 77.8 |  | 78.2 | 80.4 | 61 | 65 | 70.2 | 64 | 84 | 74 | 77 | 83.6 | 75 |  |
| AZ | 77.3 |  | 76.4 | 77.8 | 67.3 | 60.4 | 73.3 | 64.9 | 89.3 | 71.9 | 73.4 | 83.3 | 78 |  |
| AR | 88.2 |  | 88.4 | 87.6 | 82.9 | 82 | 85.4 | 84 | 88 | 84.7 | 86.7 | 89.8 | 86 |  |
| CA | 87 |  | 83.6 | 84.5 | 73.8 | 71.8 | 84.6 | 79 | 94.9 | 78.6 | 84.7 | 90.6 | 86.8 |  |
| CO | 82.3 |  | 81.7 | 81.1 | 67.9 | 69.4 | 71.9 | 65 | 90 | 77 | 75.1 | 87.3 | 81 |  |
| CT | 88.9 |  | 89.6 | 88.5 | 69.9 | 70 | 82.1 | 84 | 95 | 82 | 81.3 | 93.6 | 89 |  |
| DE | 87.8 |  | 80.5 | 89 | 72 | 69 | 81 | 84 | 96 | 85.2 | 82 | 91.5 | 88 |  |
| DC | 76.4 |  | 74.8 | 68.9 | 63 | 55 | 65 | ‡ | ‡ | 75.6 | 69 | 96 | 89 |  |
| FL | 87.3 |  | 90.2 | 87.2 | 83.6 | 73.1 | 83.2 | 86 | 95.7 | 82.1 | 85.9 | 90.6 | 88.5 |  |
| GA | 84.1 |  | 83.7 | 82 | 72.5 | 66.2 | 78.6 | 77 | 93.8 | 82.2 | 77.8 | 87.4 | 83.4 |  |
| HI | 86 |  | 86 | 85.2 | --- | --- | --- | --- | 85.9 | 85 | 83 | 87 | --- |  |
| ID | 79.9 |  | 80.1 | 80.8 | 57 | 65 | 69.6 | 74 | 82 | 69 | 73.1 | 81.9 | 77 |  |
| IL | 87.3 |  | ‡ | 86.2 | 71.9 | 76.8 | 80 | 80 | 95.5 | 79.5 | 85.1 | 90.5 | 84.6 |  |
| IN | 87.7 |  | 88.2 | 87.2 | 77.2 | 88 | 85.2 | 87 | 94 | 80.1 | 84.7 | 89.4 | 84.9 |  |
| IA | 89.9 |  | 90.2 | 91.6 | 72.8 | 73 | 82.3 | 81 | 90 | 77 | 80.2 | 92.7 | 83 |  |
| KS | 89.1 |  | 87.9 | 87.2 | 83.2 | 84.4 | 82.2 | 88 | 94 | 82 | 85.2 | 91 | 87 |  |
| KY | 90.1 |  | 90.2 | 90.6 | 79.7 | 77 | 88.4 | 89 | 94 | 84.9 | 83.3 | 91.4 | 89 |  |
| LA | 83.1 |  | 82.1 | 80.1 | 57 | 46 | 77.5 | 83 | 91 | 80.3 | 69.2 | 88 | 82 |  |
| ME | 86.1 |  | 86.1 | 87.4 | 73 | 76 | 76.6 | 71 | 92 | 76 | 77 | 86.9 | 82 |  |
| MD | 86.3 |  | 87.2 | 86.9 | 69.3 | 56.6 | 77.9 | 79 | 96.4 | 84 | 72.3 | 93.5 | 90 |  |
| MA | 90.1 |  | 89.8 | 88 | 78 | 73.1 | 83.2 | 82 | 96 | 86.2 | 81.2 | 93.2 | 89 |  |
| MI | 81 |  | 80.5 | 81.4 | 58.1 | 72.5 | 69.6 | 71 | 91.9 | 70.1 | 74.3 | 84.4 | 74.6 |  |
| MN | 83.6 |  | 83.3 | 83.7 | 65.6 | 65 | 71.1 | 55 | 86.9 | 73.5 | 69 | 88.5 | 77.5 |  |
| MS | 88.9 |  | 88.4 | 85 | 67.1 | 67 | 90.3 | 91 | 93 | 87.9 | 85 | 90.3 | 87 |  |
| MO | 89.8 |  | 89.2 | 89.7 | 78.1 | 73 | 81.7 | 85 | 94 | 80.1 | 85.5 | 92.2 | 88 |  |
| MT | 85.8 |  | 86.1 | 86.6 | 76 | 67 | 76.4 | 69 | 89 | 84 | 80 | 88.8 | 82 |  |
| NE | 87.1 |  | 87.6 | 88.4 | 65.8 | 53 | 79 | 70 | 90 | 74 | 77 | 92 | 82 |  |
| NV | 81.7 |  | 81.3 | 84.1 | 65.9 | 72.6 | 81.5 | 69 | 91 | 68.4 | 80.7 | 86.1 | 82 |  |
| NH | 87.7 |  | 87.1 | 88.4 | 73 | 68 | 73.3 | 72 | 95 | 79 | 76 | 88.6 | 85 |  |
| NJ | 85.2 |  | 88.5 | 90.6 | 48.5 | 70.3 | 78.7 | 85 | 95.9 | 77.8 | 79.3 | 89.1 | 84 |  |
| NM | --- |  | 76.6 | 75.1 | --- | --- | --- | --- | --- | --- | --- | --- | --- |  |
| NY | 86.7 |  | 84.9 | 82.8 | 66.2 | 60.7 | 81.6 | 82 | 92.3 | 80.5 | 80.4 | 91.5 | 86.7 |  |
| NC | 86.4 |  | 87 | 86.5 | 71 | 66.9 | 79.5 | 85 | 95.6 | 83.4 | 80.2 | 89.9 | 83.5 |  |
| ND | 85.1 |  | 87 | 88.3 | 66 | 73 | 69 | 65 | 85 | 72 | 74 | 89.7 | --- |  |
| OH | 86.2 |  | 85.3 | 82 | 68.2 | 71 | 76.8 | 76 | 94.2 | 75.4 | 76.3 | 89.5 | 82.2 |  |
| OK | --- |  | 80 | 84.9 | --- | --- | --- | --- | --- | --- | --- | --- | --- |  |
| OR | 81.3 |  | 80.6 | 80 | 67.5 | 65 | 80.7 | 69 | 89 | 74 | 78.7 | 82.5 | 79.7 |  |
| PA | 87 |  | 86.7 | 86.5 | 73.6 | 67.5 | 80.1 | 78 | 94.2 | 77 | 76 | 91.1 | 81.1 |  |
| RI | 83.3 |  | 83.7 | 83.9 | 66 | 67 | 75.7 | 69 | 93 | 80 | 76.9 | 87.2 | 78 |  |
| SC | 83.8 |  | 83.3 | 81.1 | 57.9 | 78 | 76.4 | 77 | 94 | 79.8 | 80.1 | 86.9 | --- |  |
| SD | 82.1 |  | 82.9 | 84.1 | 63 | 75 | 60 | 46 | 86 | 76 | 69 | 89.5 | 73 |  |
| TN | 90.4 |  | 89.3 | 90.5 | 79 | 68 | 83.6 | 89 | 96 | 85.7 | 82.1 | 93.5 | --- |  |
| TX | 89.7 |  | 90 | 90 | 79.1 | 80.1 | 86.4 | 88 | 96.6 | 85.6 | 88 | 93.8 | 90.6 |  |
| UT | 88.2 |  | 88.1 | 87.4 | 73.5 | 76.3 | 77.5 | 78 | 86 | 79 | 81 | 90.6 | 87 |  |
| VT | 82.8 |  | 83.2 | 84.5 | 70 | 63 | 75 | 74 | 78 | 73 | 83 | 83.4 | 80 |  |
| VA | 89.1 |  | 89.8 | 87.5 | 70.2 | 69.2 | 82.4 | 86 | 96.4 | 86.1 | 77.9 | 92.8 | 91 |  |
| WA | 83.6 |  | --- | 81.1 | 66.4 | 70.5 | 76.5 | 68 | 90.7 | 82.1 | 79 | 84.7 | 84.7 |  |
| WV | 91.2 |  | 91.1 | 91.3 | 83 | 81 | 85.3 | >=80 | >=95 | 87 | 86 | 91.5 | 89 |  |
| WI | 90.3 |  | 89.6 | 90.1 | 72.8 | 76 | 81.4 | 80 | 92 | 70.9 | 82.4 | 94.2 | 87 |  |
| WY | 81.8 |  | 82.5 | 82.1 | 63 | 63 | 68 | 49 | >=95 | 80 | 76 | 84.1 | 78 |  |

# Students and class size

## students_race_ethnicity_share: Public School Students by Race/Ethnicity (Share of Enrollment)

- unit: percent
- period: Fall 2022 (school year 2022-23); year: 2023
- source: NCES, Digest of Education Statistics 2023, Table 203.70 (current version per the Digest "current tables" list on 2026-11-08) — https://nces.ed.gov/programs/digest/d23/tables/dt23_203.70.asp
- as_of: 2026-11-08
- raw: raw/national/nces-digest-d23-203.70.xlsx, raw/national/nces-digest-d23-203.70.html
- note: Public elementary and secondary schools. Percentage distribution of enrollment, shown to one decimal as NCES formats it. Value = White share; the other columns are the other groups' shares. Race categories exclude persons of Hispanic ethnicity. Rows sum to about 100 (rounding).

| Place | Value: White | Rank | Hispanic | Black | Asian | Two or more races | American Indian/Alaska Native | Pacific Islander | Note |
|---|---|---|---|---|---|---|---|---|---|
| US | 44.7 |  | 28.7 | 14.9 | 5.5 | 4.9 | 0.9 | 0.4 |  |
| AL | 51.9 |  | 10.5 | 31.7 | 1.5 | 3.5 | 0.8 | 0.1 |  |
| AK | 47.2 |  | 7.5 | 2.3 | 5.0 | 13.4 | 21.6 | 3.1 |  |
| AZ | 34.9 |  | 47.6 | 5.7 | 3.1 | 4.2 | 4.2 | 0.4 |  |
| AR | 58.8 |  | 14.2 | 19.4 | 1.8 | 4.2 | 0.6 | 1.0 |  |
| CA | 20.5 |  | 56.2 | 5.0 | 11.9 | 5.5 | 0.4 | 0.4 |  |
| CO | 50.8 |  | 35.3 | 4.6 | 3.3 | 5.1 | 0.6 | 0.3 |  |
| CT | 47.4 |  | 30.0 | 12.6 | 5.2 | 4.5 | 0.3 | 0.1 |  |
| DE | 40.5 |  | 19.0 | 30.5 | 4.3 | 5.2 | 0.4 | 0.2 |  |
| DC | 13.2 |  | 17.8 | 64.1 | 1.5 | 3.3 | 0.1 | 0.1 |  |
| FL | 35.3 |  | 36.4 | 20.9 | 2.8 | 4.1 | 0.2 | 0.2 |  |
| GA | 35.9 |  | 18.1 | 36.4 | 4.7 | 4.6 | 0.2 | 0.1 |  |
| HI | 11.2 |  | 18.3 | 1.3 | 24.6 | 18.8 | 0.1 | 25.6 |  |
| ID | 73.8 |  | 19.3 | 1.1 | 1.1 | 3.4 | 1.0 | 0.3 |  |
| IL | 46.0 |  | 27.5 | 16.5 | 5.5 | 4.2 | 0.2 | 0.1 |  |
| IN | 64.3 |  | 14.0 | 13.1 | 2.9 | 5.5 | 0.2 | 0.1 |  |
| IA | 72.5 |  | 12.5 | 6.8 | 2.5 | 4.9 | 0.3 | 0.6 |  |
| KS | 61.9 |  | 21.5 | 6.7 | 2.8 | 6.1 | 0.7 | 0.2 |  |
| KY | 73.1 |  | 8.8 | 10.7 | 2.0 | 5.1 | 0.1 | 0.2 |  |
| LA | 42.0 |  | 10.6 | 41.6 | 1.6 | 3.5 | 0.6 | 0.1 |  |
| ME | 86.7 |  | 3.2 | 4.4 | 1.4 | 3.4 | 0.8 | 0.1 |  |
| MD | 32.9 |  | 22.0 | 32.8 | 6.7 | 5.2 | 0.3 | 0.1 |  |
| MA | 54.4 |  | 24.2 | 9.4 | 7.3 | 4.4 | 0.2 | 0.1 |  |
| MI | 63.6 |  | 8.9 | 18.1 | 3.5 | 5.1 | 0.6 | 0.1 |  |
| MN | 62.3 |  | 10.9 | 11.7 | 7.0 | 6.2 | 1.7 | 0.1 |  |
| MS | 42.6 |  | 4.8 | 47.0 | 1.1 | 4.3 | 0.2 | 0.1 |  |
| MO | 68.5 |  | 8.0 | 15.2 | 2.1 | 5.5 | 0.4 | 0.4 |  |
| MT | 77.4 |  | 5.9 | 0.7 | 0.7 | 4.7 | 10.4 | 0.2 |  |
| NE | 63.3 |  | 21.1 | 6.6 | 3.0 | 4.6 | 1.3 | 0.2 |  |
| NV | 28.4 |  | 44.2 | 12.2 | 5.5 | 7.5 | 0.8 | 1.5 |  |
| NH | 82.9 |  | 6.9 | 2.1 | 3.0 | 4.7 | 0.2 | 0.1 |  |
| NJ | 38.6 |  | 33.1 | 14.7 | 10.2 | 3.0 | 0.2 | 0.2 |  |
| NM | 20.8 |  | 63.4 | 1.8 | 1.2 | 2.4 | 10.3 | 0.1 |  |
| NY | 40.4 |  | 29.2 | 15.8 | 10.0 | 3.6 | 0.7 | 0.2 |  |
| NC | 44.0 |  | 20.4 | 24.8 | 4.0 | 5.6 | 1.1 | 0.1 |  |
| ND | 73.7 |  | 6.5 | 5.3 | 1.4 | 4.6 | 8.2 | 0.3 |  |
| OH | 66.6 |  | 7.3 | 16.8 | 2.8 | 6.2 | 0.1 | 0.1 |  |
| OK | 45.5 |  | 19.8 | 7.9 | 2.3 | 12.9 | 11.2 | 0.4 |  |
| OR | 58.8 |  | 25.5 | 2.4 | 4.0 | 7.2 | 1.2 | 0.8 |  |
| PA | 61.4 |  | 14.3 | 14.5 | 4.5 | 5.1 | 0.2 | 0.1 |  |
| RI | 52.3 |  | 29.4 | 9.0 | 3.3 | 5.1 | 0.7 | 0.1 |  |
| SC | 47.8 |  | 12.7 | 31.6 | 1.7 | 5.8 | 0.3 | 0.1 |  |
| SD | 70.8 |  | 8.0 | 3.3 | 1.6 | 5.7 | 10.4 | 0.1 |  |
| TN | 58.7 |  | 13.9 | 20.6 | 2.0 | 4.5 | 0.2 | 0.1 |  |
| TX | 25.7 |  | 52.9 | 12.8 | 5.1 | 3.0 | 0.3 | 0.2 |  |
| UT | 71.3 |  | 19.6 | 1.3 | 1.7 | 3.4 | 1.0 | 1.7 |  |
| VT | 88.1 |  | 3.1 | 2.6 | 2.1 | 3.8 | 0.3 | 0.1 |  |
| VA | 45.0 |  | 18.7 | 21.6 | 7.5 | 6.7 | 0.3 | 0.2 |  |
| WA | 49.3 |  | 25.7 | 4.8 | 8.7 | 8.9 | 1.1 | 1.4 |  |
| WV | 88.6 |  | 2.2 | 4.1 | 0.7 | 4.3 | 0.1 | 0.0 |  |
| WI | 67.2 |  | 13.6 | 8.7 | 4.2 | 5.1 | 1.0 | 0.1 |  |
| WY | 76.8 |  | 14.7 | 0.8 | 0.7 | 3.8 | 3.1 | 0.2 |  |

## pupils_per_teacher: Pupils per Teacher in Public Schools

- unit: number
- period: Fall 2022 (school year 2022-23); also fall 2019; year: 2023
- source: NCES, Digest of Education Statistics 2023, Table 208.40 (current version per the Digest "current tables" list on 2026-11-08) — https://nces.ed.gov/programs/digest/d23/tables/dt23_208.40.asp
- as_of: 2026-11-08
- raw: raw/national/nces-digest-d23-208.40.xlsx, raw/national/nces-digest-d23-208.40.html
- note: Public elementary and secondary schools. Pupil/teacher ratio = enrollment divided by full-time-equivalent (FTE) teachers; it is not average class size. Teachers are FTE counts, shown to whole numbers as NCES formats them.

| Place | Value fall 2022 | Rank | Teachers (FTE) fall 2022 | Enrollment fall 2022 | Value fall 2019 | Note |
|---|---|---|---|---|---|---|
| US | 15.4 |  | 3,228,895 | 49,618,464 | 15.9 |  |
| AL | 17.9 |  | 42,022 | 750,923 | 17.7 |  |
| AK | 18.3 |  | 7,160 | 130,723 | 17.6 |  |
| AZ | 22.8 |  | 49,566 | 1,132,223 | 23.6 |  |
| AR | 12.7 |  | 38,815 | 493,130 | 12.9 |  |
| CA | 21.8 |  | 271,586 | 5,930,473 | 23.0 |  |
| CO | 16.3 |  | 53,553 | 870,871 | 16.9 |  |
| CT | 11.7 |  | 44,007 | 513,513 | 12.4 |  |
| DE | 14.2 |  | 9,991 | 141,465 | 14.4 |  |
| DC | 11.3 |  | 8,052 | 91,001 | 12.1 |  |
| FL | 18.3 |  | 156,787 | 2,870,527 | 17.2 |  |
| GA | 14.4 |  | 121,301 | 1,750,972 | 15.0 |  |
| HI | 14.2 |  | 11,984 | 170,209 | 14.8 |  |
| ID | 17.5 |  | 18,121 | 317,555 | 18.1 |  |
| IL | 13.7 |  | 135,363 | 1,852,242 | 14.6 |  |
| IN | 15.8 |  | 65,597 | 1,036,108 | 17.0 |  |
| IA | 14.1 |  | 36,138 | 511,297 | 14.5 |  |
| KS | 12.9 |  | 37,885 | 487,978 | 13.6 |  |
| KY | 15.3 |  | 43,023 | 660,029 | 16.4 |  |
| LA | 17.5 |  | 41,110 | 718,145 | 18.4 |  |
| ME | 11.4 |  | 15,192 | 173,853 | 12.2 |  |
| MD | 14.3 |  | 62,236 | 889,960 | 14.8 |  |
| MA | 12.0 |  | 76,978 | 923,349 | 12.8 |  |
| MI | 16.7 |  | 85,880 | 1,433,914 | 17.6 |  |
| MN | 15.5 |  | 56,124 | 870,019 | 16.1 |  |
| MS | 13.0 |  | 33,768 | 440,285 | 14.8 |  |
| MO | 12.8 |  | 69,838 | 892,246 | 13.2 |  |
| MT | 13.7 |  | 11,036 | 150,733 | 14.0 |  |
| NE | 13.8 |  | 23,911 | 329,234 | 13.7 |  |
| NV | 21.0 |  | 23,076 | 484,192 | 19.5 |  |
| NH | 11.5 |  | 14,731 | 168,909 | 12.1 |  |
| NJ | 11.8 |  | 117,661 | 1,383,830 | 12.1 |  |
| NM | 14.6 |  | 21,572 | 315,023 | 15.2 |  |
| NY | 11.7 |  | 215,761 | 2,532,888 | 12.4 |  |
| NC | 15.4 |  | 99,980 | 1,541,722 | 15.5 |  |
| ND | 12.4 |  | 9,581 | 118,513 | 12.5 |  |
| OH | 16.4 |  | 102,323 | 1,680,639 | 15.9 |  |
| OK | 16.6 |  | 42,124 | 701,301 | 16.2 |  |
| OR | 18.7 |  | 30,906 | 577,335 | 20.2 |  |
| PA | 13.3 |  | 127,037 | 1,693,347 | 13.9 |  |
| RI | 12.7 |  | 10,786 | 137,449 | 13.4 |  |
| SC | 14.1 |  | 55,947 | 789,231 | 14.7 |  |
| SD | 13.8 |  | 10,261 | 141,888 | 14.1 |  |
| TN | 15.3 |  | 65,781 | 1,006,752 | 15.7 |  |
| TX | 14.8 |  | 373,332 | 5,519,599 | 15.1 |  |
| UT | 22.2 |  | 31,164 | 691,906 | 22.6 |  |
| VT | 10.5 |  | 7,934 | 83,654 | 10.8 |  |
| VA | 13.6 |  | 92,651 | 1,260,351 | 14.9 |  |
| WA | 17.2 |  | 63,272 | 1,090,227 | 18.4 |  |
| WV | 13.5 |  | 18,670 | 251,224 | 14.0 |  |
| WI | 13.7 |  | 60,011 | 823,040 | 14.3 |  |
| WY | 12.6 |  | 7,312 | 92,467 | 12.8 |  |

## nea_students_per_teacher: Students Enrolled per Teacher (NEA)

- unit: number
- period: School year 2024-25; year: 2025
- source: National Education Association, Rankings of the States 2025 and Estimates of School Statistics 2026 (August 2026 update), Table B-3 — https://www.nea.org/sites/default/files/2026-08/2026-rankings-and-estimates-report-august-update.pdf
- as_of: 2026-11-08
- raw: raw/national/nea-2026-rankings-and-estimates-august-update.pdf
- note: Rank is NEA's own, 1 = most students per teacher, among the 50 states and DC. This is a ratio of enrollment to teachers, not average class size. "NEA estimate" = NEA marked the 2024-25 figure with *.

| Place | Value 2024-25 | Rank | Value 2023-24 (revised) | Rank 2023-24 | Note |
|---|---|---|---|---|---|
| US | 15.1 |  | 15.1 |  |  |
| AL | 15.1 | 18 | 16.1 | 16 |  |
| AK | 19.4 | 5 | 18.6 | 5 |  |
| AZ | 22.3 | 1 | 22.6 | 2 |  |
| AR | 14.9 | 20 | 14.9 | 20 |  |
| CA | 21.5 | 4 | 21.7 | 4 |  |
| CO | 16.4 | 14 | 16.4 | 14 |  |
| CT | 12.1 | 42 | 12.1 | 42 |  |
| DE | 14.6 | 23 | 14.4 | 24 |  |
| DC | 10.9 | 49 | 11.1 | 48 |  |
| FL | 16.6 | 11 | 16.6 | 11 |  |
| GA | 14.2 | 28 | 14.3 | 26 |  |
| HI | 14.9 | 21 | 15.2 | 18 | NEA estimate |
| ID | 17.7 | 6 | 17.8 | 6 |  |
| IL | 13.4 | 33 | 13.5 | 35 |  |
| IN | 16.6 | 12 | 16.5 | 12 |  |
| IA | 13.3 | 37 | 13.3 | 36 |  |
| KS | 13.9 | 30 | 13.8 | 29 |  |
| KY | 16.5 | 13 | 16.5 | 13 |  |
| LA | 14.3 | 25 | 14.8 | 21 |  |
| ME | 11.6 | 46 | 11.6 | 47 |  |
| MD | 14.0 | 29 | 14.1 | 28 |  |
| MA | 11.8 | 44 | 11.8 | 45 |  |
| MI | 17.2 | 9 | 17.3 | 9 |  |
| MN | 15.5 | 16 | 15.2 | 17 |  |
| MS | 13.4 | 34 | 13.6 | 32 |  |
| MO | 12.0 | 43 | 12.1 | 43 |  |
| MT | 13.4 | 35 | 13.7 | 31 |  |
| NE | 12.3 | 40 | 12.4 | 40 |  |
| NV | 22.2 | 2 | 25.0 | 1 |  |
| NH | 11.1 | 48 | 10.5 | 50 |  |
| NJ | 11.8 | 45 | 11.8 | 44 |  |
| NM | 14.2 | 27 | 14.3 | 25 | NEA estimate |
| NY | 10.8 | 50 | 11.1 | 49 |  |
| NC | 15.2 | 17 | 14.9 | 19 |  |
| ND | 12.5 | 39 | 12.4 | 39 |  |
| OH | 17.3 | 8 | 17.4 | 7 |  |
| OK | 16.3 | 15 | 16.3 | 15 |  |
| OR | 17.4 | 7 | 17.3 | 8 |  |
| PA | 13.7 | 32 | 13.6 | 33 |  |
| RI | 12.9 | 38 | 12.7 | 38 |  |
| SC | 14.2 | 26 | 14.2 | 27 |  |
| SD | 13.7 | 31 | 13.8 | 30 |  |
| TN | 14.9 | 22 | 13.6 | 34 |  |
| TX | 15.0 | 19 | 14.8 | 22 |  |
| UT | 21.9 | 3 | 22.1 | 3 |  |
| VT | 10.3 | 51 | 10.4 | 51 |  |
| VA | 11.5 | 47 | 11.7 | 46 |  |
| WA | 17.1 | 10 | 16.8 | 10 |  |
| WV | 13.3 | 36 | 13.1 | 37 |  |
| WI | 14.4 | 24 | 14.6 | 23 |  |
| WY | 12.2 | 41 | 12.3 | 41 |  |

# School spending and revenue

## census_current_spending_per_pupil: Current Spending per Pupil (Census)

- unit: dollars
- period: Fiscal year 2024 (school year 2023-24); year: 2024
- source: U.S. Census Bureau, 2024 Annual Survey of School System Finances, summary tables (released May 2026) — https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24_sumtables.xlsx (Table 8 values; Table 11 ranks)
- as_of: 2026-11-08
- raw: raw/national/census-elsec24_sumtables.xlsx
- note: Public elementary-secondary school systems. Current spending excludes capital outlay and debt payments. Whole dollars, as Census formats them. Rank is Census's own (Table 11), 1 = highest, among the 50 states and DC. "Instruction" and "Support services" are per-pupil current spending by function (Table 8); Census ranks instruction (Table 11) but not support services. Census computes per-pupil amounts with fall enrollment from the NCES Common Core of Data (see Table 11 note in the raw file).

| Place | Value | Rank | Instruction per pupil | Instruction rank | Support services per pupil | Note |
|---|---|---|---|---|---|---|
| US | 17,619 |  | 10,346 |  | 6,582 |  |
| AL | 13,627 | 40 | 7,452 | 44 | 5,319 |  |
| AK | 21,004 | 13 | 10,742 | 18 | 9,504 |  |
| AZ | 12,003 | 49 | 6,191 | 51 | 5,213 |  |
| AR | 13,873 | 38 | 7,547 | 41 | 5,565 |  |
| CA | 20,791 | 14 | 11,959 | 13 | 8,031 |  |
| CO | 15,908 | 28 | 8,497 | 32 | 6,788 |  |
| CT | 26,316 | 5 | 15,165 | 5 | 10,243 |  |
| DE | 22,201 | 9 | 11,858 | 15 | 9,608 |  |
| DC | 31,529 | 2 | 15,764 | 4 | 14,706 |  |
| FL | 12,693 | 46 | 7,574 | 40 | 4,484 |  |
| GA | 15,833 | 29 | 9,380 | 27 | 5,643 |  |
| HI | 23,878 | 7 | 13,872 | 8 | 8,960 |  |
| ID | 11,060 | 51 | 6,588 | 49 | 4,020 |  |
| IL | 21,776 | 11 | 12,761 | 9 | 8,413 |  |
| IN | 13,622 | 41 | 7,487 | 43 | 5,469 |  |
| IA | 14,369 | 36 | 8,308 | 35 | 5,416 |  |
| KS | 15,558 | 32 | 9,236 | 28 | 5,637 |  |
| KY | 14,596 | 35 | 8,355 | 34 | 5,343 |  |
| LA | 15,581 | 31 | 8,495 | 33 | 6,222 |  |
| ME | 19,962 | 17 | 10,993 | 16 | 8,199 |  |
| MD | 20,208 | 16 | 12,513 | 11 | 7,131 |  |
| MA | 24,429 | 6 | 14,724 | 6 | 9,279 |  |
| MI | 18,314 | 19 | 9,993 | 22 | 7,611 |  |
| MN | 17,098 | 25 | 10,887 | 17 | 5,432 |  |
| MS | 12,324 | 47 | 6,937 | 48 | 4,661 |  |
| MO | 14,241 | 37 | 7,820 | 39 | 5,830 |  |
| MT | 13,656 | 39 | 6,191 | 38 | 5,162 |  |
| NE | 16,147 | 26 | 9,919 | 26 | 5,511 |  |
| NV | 14,812 | 34 | 8,937 | 30 | 5,474 |  |
| NH | 22,978 | 8 | 13,888 | 7 | 8,541 |  |
| NJ | 27,234 | 4 | 15,858 | 3 | 10,540 |  |
| NM | 17,664 | 21 | 10,068 | 21 | 6,814 |  |
| NY | 31,918 | 1 | 21,571 | 1 | 9,695 |  |
| NC | 12,995 | 42 | 8,017 | 37 | 4,330 |  |
| ND | 17,102 | 24 | 10,118 | 20 | 5,614 |  |
| OH | 17,257 | 22 | 9,940 | 25 | 6,761 |  |
| OK | 12,162 | 48 | 6,513 | 50 | 4,917 |  |
| OR | 18,083 | 20 | 9,951 | 24 | 7,573 |  |
| PA | 21,091 | 12 | 12,628 | 10 | 7,672 |  |
| RI | 22,110 | 10 | 12,368 | 12 | 9,153 |  |
| SC | 15,060 | 33 | 8,171 | 36 | 6,123 |  |
| SD | 12,828 | 45 | 7,418 | 46 | 4,681 |  |
| TN | 12,882 | 44 | 7,535 | 42 | 4,688 |  |
| TX | 12,895 | 43 | 7,421 | 45 | 4,831 |  |
| UT | 11,347 | 50 | 7,108 | 47 | 3,739 |  |
| VT | 28,818 | 3 | 15,895 | 2 | 11,877 |  |
| VA | 17,104 | 23 | 9,983 | 23 | 6,447 |  |
| WA | 18,564 | 18 | 10,740 | 19 | 7,197 |  |
| WV | 15,640 | 30 | 8,871 | 31 | 5,780 |  |
| WI | 15,952 | 27 | 9,157 | 29 | 6,161 |  |
| WY | 20,521 | 15 | 11,951 | 14 | 7,930 |  |

## census_revenue_share_by_source: School Revenue by Source: Federal, State and Local Shares (Census)

- unit: percent
- period: Fiscal year 2024 (school year 2023-24); year: 2024
- source: U.S. Census Bureau, 2024 Annual Survey of School System Finances, summary tables (released May 2026) — https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24_sumtables.xlsx (Table 5; per-pupil ranks from Table 11)
- as_of: 2026-11-08
- raw: raw/national/census-elsec24_sumtables.xlsx
- note: Percent of each state's public school system revenue, one decimal as Census formats it. "Local: taxes and parent government contributions" is the part of local revenue from local taxes (including property taxes) and appropriations from a parent government such as a city or county; Census does not separate property taxes in this table. Census publishes no rank for these shares; the rank columns are Census's Table 11 ranks of revenue **per pupil** from each source (1 = highest). Revenue from other school systems is excluded.

| Place | Value: local share | Rank | State share | Federal share | Local: taxes and parent government contributions | Local revenue per pupil rank | State revenue per pupil rank | Federal revenue per pupil rank | Note |
|---|---|---|---|---|---|---|---|---|---|
| US | 43.2 |  | 45.2 | 11.6 | 36.0 |  |  |  |  |
| AL | 31.3 |  | 52.5 | 16.1 | 15.4 | 40 | 26 | 18 |  |
| AK | 23.8 |  | 55.2 | 21.0 | 20.2 | 42 | 12 | 3 |  |
| AZ | 34.7 |  | 47.3 | 18.1 | 29.2 | 41 | 35 | 17 |  |
| AR | 16.0 |  | 69.3 | 14.7 | 9.5 | 49 | 16 | 31 |  |
| CA | 35.0 |  | 53.4 | 11.6 | 25.1 | 18 | 7 | 14 |  |
| CO | 54.8 |  | 36.8 | 8.4 | 46.7 | 13 | 38 | 48 |  |
| CT | 56.1 |  | 35.8 | 8.1 | 51.5 | 3 | 17 | 27 |  |
| DE | 31.8 |  | 57.4 | 10.7 | 28.7 | 28 | 8 | 22 |  |
| DC | 86.1 |  | (X) | 13.9 | 85.4 | 1 | 51 | 1 |  |
| FL | 55.4 |  | 29.3 | 15.3 | 47.6 | 21 | 50 | 28 |  |
| GA | 48.6 |  | 39.4 | 12.0 | 40.4 | 20 | 37 | 34 |  |
| HI | 1.5 |  | 85.3 | 13.1 | 0.0 | 51 | 2 | 13 |  |
| ID | 20.9 |  | 67.4 | 11.7 | 13.3 | 48 | 29 | 50 |  |
| IL | 51.1 |  | 38.6 | 10.3 | 45.2 | 7 | 23 | 20 |  |
| IN | 32.7 |  | 55.9 | 11.4 | 24.4 | 39 | 24 | 41 |  |
| IA | 39.9 |  | 50.9 | 9.2 | 33.8 | 31 | 30 | 49 |  |
| KS | 26.5 |  | 61.7 | 11.8 | 17.1 | 44 | 15 | 37 |  |
| KY | 37.0 |  | 45.9 | 17.1 | 31.3 | 34 | 34 | 15 |  |
| LA | 47.1 |  | 33.7 | 19.2 | 40.5 | 17 | 43 | 4 |  |
| ME | 51.0 |  | 40.6 | 8.4 | 49.0 | 10 | 27 | 45 |  |
| MD | 46.5 |  | 44.1 | 9.4 | 43.7 | 11 | 19 | 33 |  |
| MA | 48.1 |  | 43.6 | 8.2 | 37.9 | 8 | 13 | 35 |  |
| MI | 32.4 |  | 56.7 | 10.9 | 25.9 | 27 | 10 | 21 |  |
| MN | 30.2 |  | 61.7 | 8.1 | 19.7 | 33 | 9 | 47 |  |
| MS | 32.5 |  | 44.8 | 22.7 | 26.6 | 43 | 41 | 7 |  |
| MO | 53.7 |  | 55.2 | 11.4 | 46.0 | 16 | 47 | 40 |  |
| MT | 43.2 |  | 39.0 | 17.8 | 27.7 | 30 | 45 | 16 |  |
| NE | 55.9 |  | 33.6 | 10.5 | 49.6 | 14 | 46 | 43 |  |
| NV | 16.3 |  | 70.1 | 13.6 | 11.4 | 47 | 11 | 25 |  |
| NH | 63.4 |  | 28.3 | 8.3 | 60.6 | 4 | 36 | 38 |  |
| NJ | 47.4 |  | 46.3 | 6.3 | 43.3 | 5 | 5 | 42 |  |
| NM | 16.7 |  | 63.6 | 19.7 | 13.3 | 45 | 4 | 2 |  |
| NY | 50.9 |  | 40.8 | 8.4 | 44.1 | 2 | 3 | 9 |  |
| NC | 25.5 |  | 57.1 | 17.4 | 21.5 | 46 | 32 | 24 |  |
| ND | 38.4 |  | 46.2 | 15.4 | 25.2 | 26 | 25 | 11 |  |
| OH | 53.6 |  | 34.6 | 11.8 | 43.9 | 12 | 40 | 29 |  |
| OK | 41.5 |  | 44.6 | 13.9 | 31.2 | 36 | 44 | 39 |  |
| OR | 37.7 |  | 51.8 | 10.5 | 30.3 | 23 | 14 | 30 |  |
| PA | 52.4 |  | 37.5 | 10.1 | 47.2 | 6 | 20 | 19 |  |
| RI | 47.1 |  | 40.3 | 12.7 | 45.2 | 9 | 21 | 10 |  |
| SC | 44.6 |  | 42.5 | 12.9 | 36.3 | 22 | 31 | 23 |  |
| SD | 49.9 |  | 30.7 | 19.4 | 43.1 | 25 | 49 | 12 |  |
| TN | 39.8 |  | 44.3 | 15.9 | 30.2 | 35 | 42 | 26 |  |
| TX | 50.8 |  | 35.8 | 13.4 | 42.8 | 24 | 48 | 36 |  |
| UT | 41.5 |  | 50.6 | 7.9 | 33.3 | 37 | 39 | 51 |  |
| VT | 2.6 |  | 87.0 | 10.4 | 0.0 | 50 | 1 | 8 |  |
| VA | 48.9 |  | 41.3 | 9.8 | 46.7 | 15 | 33 | 44 |  |
| WA | 26.1 |  | 65.6 | 8.3 | 21.8 | 38 | 6 | 46 |  |
| WV | 35.6 |  | 46.0 | 18.4 | 31.2 | 32 | 28 | 6 |  |
| WI | 36.0 |  | 52.1 | 11.9 | 29.4 | 29 | 22 | 32 |  |
| WY | 39.1 |  | 45.3 | 15.5 | 23.9 | 19 | 18 | 5 |  |

## nea_current_expenditure_per_student: Current Expenditure per Student in Fall Enrollment (NEA)

- unit: dollars
- period: School year 2024-25; year: 2025
- source: National Education Association, Rankings of the States 2025 and Estimates of School Statistics 2026 (August 2026 update), Table D-1 — https://www.nea.org/sites/default/files/2026-08/2026-rankings-and-estimates-report-august-update.pdf
- as_of: 2026-11-08
- raw: raw/national/nea-2026-rankings-and-estimates-august-update.pdf
- note: Rank is NEA's own, 1 = highest, among the 50 states and DC. "NEA estimate" = NEA marked the 2024-25 figure with *. NEA's figures differ from Census's (census_current_spending_per_pupil) because of different years, definitions and enrollment counts.

| Place | Value 2024-25 | Rank | Value 2023-24 (revised) | Rank 2023-24 | Note |
|---|---|---|---|---|---|
| US | 17,873 |  | 17,250 |  |  |
| AL | 13,269 | 44 | 13,176 | 42 | NEA estimate |
| AK | 21,344 | 13 | 21,000 | 11 | NEA estimate |
| AZ | 11,987 | 50 | 11,808 | 49 |  |
| AR | 13,090 | 45 | 13,061 | 43 |  |
| CA | 20,898 | 16 | 19,591 | 16 | NEA estimate |
| CO | 17,130 | 24 | 16,705 | 23 |  |
| CT | 27,481 | 6 | 26,070 | 6 | NEA estimate |
| DE | 22,128 | 10 | 21,082 | 10 | NEA estimate |
| DC | 30,564 | 2 | 30,203 | 2 | NEA estimate |
| FL | 13,487 | 41 | 12,555 | 46 | NEA estimate |
| GA | 16,113 | 29 | 15,178 | 30 | NEA estimate |
| HI | 19,728 | 17 | 18,943 | 18 | NEA estimate |
| ID | 11,578 | 51 | 10,739 | 51 | NEA estimate |
| IL | 21,385 | 12 | 20,913 | 12 | NEA estimate |
| IN | 13,604 | 40 | 13,374 | 40 | NEA estimate |
| IA | 14,353 | 37 | 13,931 | 37 |  |
| KS | 15,398 | 32 | 14,901 | 31 |  |
| KY | 15,056 | 33 | 14,516 | 32 |  |
| LA | 18,021 | 20 | 16,342 | 27 |  |
| ME | 23,290 | 9 | 22,461 | 8 | NEA estimate |
| MD | 19,412 | 18 | 19,345 | 17 |  |
| MA | 27,587 | 5 | 27,077 | 5 | NEA estimate |
| MI | 14,779 | 36 | 14,489 | 33 |  |
| MN | 17,114 | 25 | 16,593 | 24 | NEA estimate |
| MS | 13,049 | 46 | 12,490 | 47 | NEA estimate |
| MO | 14,005 | 38 | 13,595 | 39 | NEA estimate |
| MT | 15,431 | 31 | 14,480 | 34 | NEA estimate |
| NE | 16,788 | 28 | 16,487 | 26 | NEA estimate |
| NV | 15,056 | 33 | 14,247 | 36 | NEA estimate |
| NH | 23,619 | 7 | 22,252 | 9 |  |
| NJ | 28,779 | 4 | 27,941 | 4 | NEA estimate |
| NM | 15,985 | 30 | 15,183 | 29 | NEA estimate |
| NY | 32,370 | 1 | 30,967 | 1 | NEA estimate |
| NC | 13,640 | 39 | 13,796 | 38 |  |
| ND | 18,118 | 19 | 17,492 | 19 | NEA estimate |
| OH | 16,856 | 27 | 16,171 | 28 | NEA estimate |
| OK | 12,758 | 48 | 12,136 | 48 | NEA estimate |
| OR | 17,533 | 22 | 16,760 | 22 | NEA estimate |
| PA | 21,522 | 11 | 20,779 | 14 | NEA estimate |
| RI | 23,552 | 8 | 22,538 | 7 | NEA estimate |
| SC | 14,944 | 35 | 14,306 | 35 | NEA estimate |
| SD | 13,485 | 42 | 13,337 | 41 | NEA estimate |
| TN | 13,294 | 43 | 13,027 | 44 |  |
| TX | 12,815 | 47 | 13,010 | 45 |  |
| UT | 12,029 | 49 | 11,289 | 50 |  |
| VT | 29,534 | 3 | 28,697 | 3 | NEA estimate |
| VA | 17,674 | 21 | 16,832 | 20 |  |
| WA | 20,948 | 15 | 19,955 | 15 | NEA estimate |
| WV | 17,372 | 23 | 16,780 | 21 | NEA estimate |
| WI | 17,003 | 26 | 16,524 | 25 | NEA estimate |
| WY | 21,150 | 14 | 20,874 | 13 |  |

## nea_revenue_share_by_source: School Revenue by Source: State, Local and Federal Shares (NEA)

- unit: percent
- period: School year 2024-25; year: 2025
- source: National Education Association, Rankings of the States 2025 and Estimates of School Statistics 2026 (August 2026 update), Tables C-3, C-4 and C-5 — https://www.nea.org/sites/default/files/2026-08/2026-rankings-and-estimates-report-august-update.pdf
- as_of: 2026-11-08
- raw: raw/national/nea-2026-rankings-and-estimates-august-update.pdf
- note: Value is the state share. Ranks are NEA's own, 1 = highest share, among the 50 states and DC. "est." marks figures NEA flagged with * as NEA estimates.

| Place | Value (state share) | Rank | Local share | Local rank | Federal share | Federal rank | Note |
|---|---|---|---|---|---|---|---|
| US | 47.2 |  | 45.0 |  | 7.8 |  |  |
| AL | 56.5 (est.) | 14 | 33.5 (est.) | 38 | 10.0 (est.) | 18 |  |
| AK | 58.3 (est.) | 13 | 25.8 (est.) | 46 | 16.0 (est.) | 3 |  |
| AZ | 54.8 | 16 | 30.7 | 41 | 14.5 | 4 |  |
| AR | 43.9 | 32 | 43.0 | 25 | 13.1 | 8 |  |
| CA | 61.0 (est.) | 10 | 33.0 (est.) | 39 | 6.0 (est.) | 42 |  |
| CO | 37.7 | 40 | 53.9 | 12 | 8.4 | 23 |  |
| CT | 37.5 (est.) | 41 | 57.6 (est.) | 7 | 4.8 (est.) | 49 |  |
| DE | 64.1 | 9 | 30.5 | 42 | 5.5 | 46 |  |
| DC | 0.0 | 51 | 92.0 (est.) | 1 | 8.0 (est.) | 25 |  |
| FL | 30.9 (est.) | 47 | 57.3 (est.) | 8 | 11.8 (est.) | 11 |  |
| GA | 41.2 (est.) | 37 | 51.8 (est.) | 13 | 7.0 (est.) | 35 |  |
| HI | 91.4 (est.) | 1 | 0.9 (est.) | 51 | 7.7 (est.) | 26 |  |
| ID | 71.9 (est.) | 4 | 20.6 (est.) | 48 | 7.4 (est.) | 30 |  |
| IL | 35.6 (est.) | 44 | 58.6 (est.) | 5 | 5.8 (est.) | 43 |  |
| IN | 59.5 (est.) | 12 | 33.7 (est.) | 37 | 6.8 (est.) | 36 |  |
| IA | 53.3 | 19 | 39.0 | 28 | 7.7 | 27 |  |
| KS | 59.8 | 11 | 31.1 | 40 | 9.2 | 20 |  |
| KY | 45.7 | 30 | 36.8 | 32 | 17.5 | 1 |  |
| LA | 35.5 | 45 | 50.2 | 16 | 14.3 | 5 |  |
| ME | 45.8 (est.) | 29 | 47.9 (est.) | 18 | 6.3 (est.) | 40 |  |
| MD | 42.6 | 34 | 47.0 | 19 | 10.4 | 16 |  |
| MA | 42.5 | 35 | 49.1 | 17 | 8.3 | 24 |  |
| MI | 64.7 | 8 | 27.9 | 44 | 7.4 | 31 |  |
| MN | 65.7 (est.) | 7 | 28.9 (est.) | 43 | 5.4 (est.) | 48 |  |
| MS | 48.9 | 25 | 34.0 | 36 | 17.1 | 2 |  |
| MO | 30.6 (est.) | 49 | 61.7 (est.) | 4 | 7.7 (est.) | 28 |  |
| MT | 44.2 (est.) | 31 | 44.3 (est.) | 23 | 11.5 (est.) | 13 |  |
| NE | 30.8 (est.) | 48 | 62.0 (est.) | 3 | 7.2 (est.) | 32 |  |
| NV | 72.1 (est.) | 3 | 22.1 (est.) | 47 | 5.8 (est.) | 44 |  |
| NH | 28.2 | 50 | 65.7 | 2 | 6.0 | 41 |  |
| NJ | 50.1 (est.) | 23 | 46.3 (est.) | 20 | 3.6 (est.) | 51 |  |
| NM | 70.5 (est.) | 5 | 16.1 (est.) | 49 | 13.4 (est.) | 6 |  |
| NY | 37.2 (est.) | 43 | 58.5 (est.) | 6 | 4.3 (est.) | 50 |  |
| NC | 54.3 | 18 | 34.3 | 35 | 11.4 | 14 |  |
| ND | 51.9 (est.) | 21 | 38.3 (est.) | 30 | 9.8 (est.) | 19 |  |
| OH | 37.9 (est.) | 39 | 55.0 (est.) | 10 | 7.1 (est.) | 34 |  |
| OK | 48.1 (est.) | 26 | 42.9 (est.) | 26 | 9.0 (est.) | 22 |  |
| OR | 56.4 (est.) | 15 | 37.0 (est.) | 31 | 6.7 (est.) | 37 |  |
| PA | 37.3 (est.) | 42 | 56.3 (est.) | 9 | 6.4 (est.) | 38 |  |
| RI | 47.3 (est.) | 27 | 45.6 (est.) | 21 | 7.1 (est.) | 33 |  |
| SC | 43.7 | 33 | 44.6 | 22 | 11.8 | 12 |  |
| SD | 33.1 (est.) | 46 | 54.7 (est.) | 11 | 12.2 (est.) | 9 |  |
| TN | 49.1 | 24 | 39.0 | 29 | 12.0 | 10 |  |
| TX | 40.0 | 38 | 50.9 | 14 | 9.1 | 21 |  |
| UT | 54.4 | 17 | 40.2 | 27 | 5.4 | 47 |  |
| VT | 90.6 (est.) | 2 | 3.2 (est.) | 50 | 6.3 (est.) | 39 |  |
| VA | 42.3 | 36 | 50.2 | 15 | 7.5 | 29 |  |
| WA | 68.6 (est.) | 6 | 25.9 (est.) | 45 | 5.5 (est.) | 45 |  |
| WV | 52.2 (est.) | 20 | 36.6 (est.) | 33 | 11.2 (est.) | 15 |  |
| WI | 51.2 | 22 | 35.7 | 34 | 13.1 | 7 |  |
| WY | 45.8 | 28 | 44.1 | 24 | 10.1 | 17 |  |

# Teacher pay

## nea_avg_teacher_salary: Average Public School Teacher Salary (NEA)

- unit: dollars
- period: School year 2024-25 (with NEA's 2025-26 estimate); year: 2025
- source: National Education Association, Rankings of the States 2025 and Estimates of School Statistics 2026 (August 2026 update), Tables B-6 (2024-25) and E-6 (2025-26 estimates) — https://www.nea.org/sites/default/files/2026-08/2026-rankings-and-estimates-report-august-update.pdf
- as_of: 2026-11-08
- raw: raw/national/nea-2026-rankings-and-estimates-august-update.pdf
- note: Rank is NEA's own, 1 = highest, among the 50 states and DC. "NEA estimate" in the Note column means NEA marked the 2024-25 figure with * (an NEA estimate rather than a state-reported figure). 2025-26 values are NEA estimates; NEA does not rank them. "Change 2017–2026" columns are NEA's estimated percent change in current dollars and in constant (inflation-adjusted) dollars (Table E-6).

| Place | Value 2024-25 | Rank | Value 2023-24 (revised) | Rank 2023-24 | Estimate 2025-26 | Change 2017–2026, current $ (%) | Change 2017–2026, constant $ (%) | Note |
|---|---|---|---|---|---|---|---|---|
| US | 74,495 |  | 71,985 |  | 76,552 | 28.18 | -4.63 |  |
| AL | 62,985 | 35 | 61,912 | 33 | 64,466 | 27.93 | -4.81 |  |
| AK | 81,450 | 11 | 78,256 | 10 | 82,629 | 20.15 | -10.60 |  |
| AZ | 64,291 | 31 | 62,714 | 29 | 66,748 | 41.03 | 4.94 |  |
| AR | 59,193 | 45 | 58,337 | 41 | 60,120 | 24.46 | -7.39 |  |
| CA | 103,552 | 1 | 101,084 | 1 | 105,726 | 33.61 | -0.58 |  |
| CO | 72,781 | 19 | 68,647 | 20 | 74,790 | 44.35 | 7.41 |  |
| CT | 89,593 | 6 | 86,511 | 6 | 91,081 | 24.52 | -7.35 | NEA estimate |
| DE | 76,570 | 14 | 71,186 | 16 | 78,614 | 27.89 | -4.84 |  |
| DC | 95,077 | 4 | 86,663 | 5 | 96,971 | 28.11 | -4.68 | NEA estimate |
| FL | 56,663 | 50 | 54,875 | 50 | 58,069 | 21.34 | -9.72 |  |
| GA | 71,524 | 21 | 67,641 | 23 | 72,758 | 31.02 | -2.51 |  |
| HI | 75,860 | 16 | 74,222 | 14 | 77,812 | 37.35 | 2.20 |  |
| ID | 62,786 | 36 | 61,516 | 34 | 66,085 | 39.14 | 3.53 |  |
| IL | 78,495 | 13 | 75,978 | 13 | 80,077 | 24.12 | -7.65 |  |
| IN | 61,661 | 38 | 58,620 | 38 | 63,116 | 25.68 | -6.48 |  |
| IA | 65,312 | 30 | 62,399 | 32 | 67,041 | 20.48 | -10.36 |  |
| KS | 61,470 | 39 | 58,276 | 44 | 63,411 | 28.31 | -4.53 |  |
| KY | 60,594 | 42 | 58,325 | 42 | 62,457 | 19.33 | -11.21 |  |
| LA | 56,785 | 49 | 55,911 | 47 | 57,660 | 15.78 | -13.85 |  |
| ME | 65,621 | 29 | 62,569 | 30 | 68,820 | 30.15 | -3.16 |  |
| MD | 87,409 | 7 | 84,338 | 7 | 90,741 | 32.75 | -1.23 |  |
| MA | 93,554 | 5 | 91,014 | 4 | 96,165 | 22.24 | -9.05 |  |
| MI | 71,023 | 22 | 69,068 | 19 | 73,088 | 17.34 | -12.69 |  |
| MN | 76,234 | 15 | 72,430 | 15 | 78,007 | 31.40 | -2.23 |  |
| MS | 54,975 | 51 | 53,704 | 51 | 56,504 | 26.52 | -5.86 |  |
| MO | 57,366 | 48 | 55,132 | 49 | 59,534 | 22.45 | -8.89 |  |
| MT | 59,305 | 44 | 57,556 | 45 | 60,392 | 21.29 | -9.75 | NEA estimate |
| NE | 63,326 | 34 | 60,239 | 37 | 64,854 | 23.91 | -7.80 |  |
| NV | 74,812 | 17 | 66,930 | 25 | 75,074 | 37.31 | 2.17 |  |
| NH | 69,432 | 25 | 67,170 | 24 | 71,857 | 24.92 | -7.05 |  |
| NJ | 84,974 | 9 | 82,877 | 8 | 86,096 | 20.24 | -10.54 |  |
| NM | 69,736 | 24 | 68,440 | 21 | 71,057 | 50.79 | 12.20 |  |
| NY | 98,655 | 2 | 95,615 | 2 | 100,367 | 22.55 | -8.82 |  |
| NC | 60,323 | 43 | 58,292 | 43 | 59,971 | 21.44 | -9.64 |  |
| ND | 60,704 | 41 | 58,581 | 40 | 62,325 | 19.83 | -10.84 |  |
| OH | 70,586 | 23 | 68,236 | 22 | 71,868 | 23.48 | -8.12 |  |
| OK | 61,931 | 37 | 61,330 | 35 | 62,055 | 37.01 | 1.95 |  |
| OR | 81,657 | 10 | 77,130 | 11 | 83,727 | 35.35 | 0.71 |  |
| PA | 79,078 | 12 | 76,961 | 12 | 81,142 | 22.45 | -8.89 |  |
| RI | 85,772 | 8 | 82,189 | 9 | 88,120 | 21.18 | -9.83 | NEA estimate |
| SC | 64,050 | 32 | 60,763 | 36 | 67,107 | 34.21 | -0.14 |  |
| SD | 58,486 | 46 | 56,328 | 46 | 60,451 | 28.68 | -4.26 |  |
| TN | 61,222 | 40 | 58,610 | 39 | 62,941 | 25.63 | -6.52 |  |
| TX | 63,749 | 33 | 62,463 | 31 | 68,001 | 29.46 | -3.67 |  |
| UT | 72,882 | 18 | 69,161 | 18 | 75,306 | 55.03 | 15.35 |  |
| VT | 71,871 | 20 | 69,555 | 17 | 73,694 | 24.40 | -7.44 |  |
| VA | 69,254 | 26 | 66,327 | 26 | 72,014 | 37.59 | 2.38 |  |
| WA | 96,589 | 3 | 91,720 | 3 | 99,649 | 83.07 | 36.21 |  |
| WV | 58,099 | 47 | 55,300 | 48 | 58,281 | 27.94 | -4.81 |  |
| WI | 67,794 | 27 | 65,762 | 27 | 68,943 | 22.04 | -9.19 |  |
| WY | 65,668 | 28 | 63,669 | 28 | 67,914 | 16.72 | -13.16 |  |

## nea_starting_teacher_salary: Average Starting Teacher Salary (NEA)

- unit: dollars
- period: School year 2024-25; year: 2025
- source: National Education Association, Teacher Salary Benchmark Report 2024-2025 (posted April 2026), Table ST-2 — https://www.nea.org/sites/default/files/2026-04/2024-2025-teacher-salary-benchmark-report-final-new.pdf (summary page: https://www.nea.org/resource-library/educator-pay-and-student-spending-how-does-your-state-rank/starting-teacher)
- as_of: 2026-11-08
- raw: raw/national/nea-2024-2025-teacher-salary-benchmark-report.pdf; raw/national/nea-starting-teacher-salary-page-2026-11-08.html
- note: Rank is NEA's own, 1 = highest, among the 50 states and DC. NEA's benchmark covers nearly 12,000 school districts; its report lists the NH data source as "NEA State Affiliate and State Department of Education". The report also lists a "Federal" (DoDEA) figure, not shown here.

| Place | Value 2024-25 | Rank | Value 2023-24 | Rank 2023-24 | Change (%) | Note |
|---|---|---|---|---|---|---|
| US | 48,112 |  | 46,526 |  | 3.4% |  |
| AL | 47,955 | 25 | 44,632 | 31 | 7.4% |  |
| AK | 53,650 | 9 | 52,451 | 9 | 2.3% |  |
| AZ | 44,869 | 39 | 46,128 | 23 | -2.7% |  |
| AR | 50,076 | 16 | 50,031 | 14 | 0.1% |  |
| CA | 59,424 | 3 | 58,409 | 2 | 1.7% |  |
| CO | 45,489 | 35 | 42,421 | 41 | 7.2% |  |
| CT | 51,053 | 14 | 49,860 | 15 | 2.4% |  |
| DE | 49,344 | 20 | 48,407 | 19 | 1.9% |  |
| DC | 64,640 | 1 | 63,373 | 1 | 2.0% |  |
| FL | 49,435 | 19 | 48,639 | 17 | 1.6% |  |
| GA | 48,722 | 21 | 43,654 | 35 | 11.6% |  |
| HI | 51,835 | 11 | 51,835 | 10 | 0.0% |  |
| ID | 46,253 | 33 | 45,732 | 24 | 1.1% |  |
| IL | 46,655 | 31 | 45,061 | 26 | 3.5% |  |
| IN | 45,958 | 34 | 45,007 | 27 | 2.1% |  |
| IA | 48,139 | 24 | 40,997 | 46 | 17.4% |  |
| KS | 44,163 | 40 | 42,800 | 36 | 3.2% |  |
| KY | 41,901 | 47 | 40,161 | 48 | 4.3% |  |
| LA | 46,850 | 30 | 46,682 | 22 | 0.4% |  |
| ME | 44,152 | 41 | 42,380 | 42 | 4.2% |  |
| MD | 57,293 | 6 | 54,439 | 6 | 5.2% |  |
| MA | 54,216 | 8 | 52,616 | 8 | 3.0% |  |
| MI | 43,093 | 45 | 41,645 | 44 | 3.5% |  |
| MN | 46,477 | 32 | 44,993 | 28 | 3.3% |  |
| MS | 43,814 | 43 | 42,492 | 40 | 3.1% |  |
| MO | 40,682 | 49 | 38,871 | 49 | 4.7% |  |
| MT | 36,682 | 51 | 35,674 | 51 | 2.8% |  |
| NE | 39,561 | 50 | 38,811 | 50 | 1.9% |  |
| NV | 49,731 | 17 | 47,355 | 20 | 5.0% |  |
| NH | 44,010 | 42 | 42,588 | 38 | 3.3% |  |
| NJ | 58,727 | 4 | 57,597 | 4 | 2.0% |  |
| NM | 54,372 | 7 | 53,400 | 7 | 1.8% |  |
| NY | 51,612 | 13 | 50,063 | 13 | 3.1% |  |
| NC | 44,952 | 38 | 42,542 | 39 | 5.7% |  |
| ND | 45,252 | 37 | 43,734 | 34 | 3.5% |  |
| OH | 42,222 | 46 | 40,982 | 47 | 3.0% |  |
| OK | 41,294 | 48 | 41,152 | 45 | 0.3% |  |
| OR | 46,854 | 29 | 44,446 | 33 | 5.4% |  |
| PA | 52,198 | 10 | 50,470 | 11 | 3.4% |  |
| RI | 48,242 | 23 | 47,205 | 21 | 2.2% |  |
| SC | 48,426 | 22 | 44,693 | 30 | 8.4% |  |
| SD | 47,196 | 27 | 45,530 | 25 | 3.7% |  |
| TN | 47,230 | 26 | 44,897 | 29 | 5.2% |  |
| TX | 49,465 | 18 | 48,526 | 18 | 1.9% |  |
| UT | 57,849 | 5 | 55,711 | 5 | 3.8% |  |
| VT | 46,963 | 28 | 44,533 | 32 | 5.5% |  |
| VA | 50,448 | 15 | 48,666 | 16 | 3.7% |  |
| WA | 60,658 | 2 | 57,912 | 3 | 4.7% |  |
| WV | 45,294 | 36 | 42,708 | 37 | 6.1% |  |
| WI | 43,288 | 44 | 42,259 | 43 | 2.4% |  |
| WY | 51,776 | 12 | 50,214 | 12 | 3.1% |  |

# Preschool

## nieer_state_preschool_access: Children in State-Funded Preschool (NIEER)

- unit: percent
- period: School year 2024-25; year: 2025
- source: National Institute for Early Education Research (NIEER), The State of Preschool 2025 (State Preschool Yearbook), Executive Summary, Table 2 (access) and Table 6 (resources), released April 2026 — https://nieer.org/sites/default/files/2026-04/2025%20NIEER%20Yearbook-ExecutiveSummary.pdf
- as_of: 2026-11-08
- raw: raw/national/nieer-2025-yearbook-executive-summary.pdf; raw/national/nieer-2026-04-22-press-release-nh.pdf
- note: Value = percent of the state's 4-year-olds enrolled in state-funded preschool. Rank is NIEER's own access rank for 4-year-olds (1 = highest). "US" is NIEER's "50 states + DC" total. "No program" = the state had no program meeting NIEER's definition of state-funded preschool. Indiana's program and Virginia's Mixed Delivery/CCSP have a parent work or school requirement, so NIEER profiles them but leaves them out of rankings and totals (shown as "Work requirement"). Virginia's ranked row is its VPI program. Spending per child is state dollars only (Table 6); NIEER's resource rank is also its own. Preschool special education and Head Start enrollment are not included here.

| Place | Value (% of 4-year-olds) | Rank | % of 3-year-olds | 4-year-olds enrolled | 3-year-olds enrolled | State $ per child enrolled | Resource rank (state $ per child) | Total state preschool spending | Note |
|---|---|---|---|---|---|---|---|---|---|
| US | 37 |  | 9 | 1,424,670 | 315,293 | $8,124 |  | $14,387,269,279 |  |
| AL | 40 | 18 | 0 | 24,238 | 0 | $7,651 | 18 | $185,448,382 |  |
| AK | 11 | 39 | 0.2 | 1,053 | 22 | $7,150 | 20 | $8,158,561 |  |
| AZ | 2 | 45 | 1 | 1,674 | 1,117 | $8,723 | 14 | $26,875,278 |  |
| AR | 33 | 24 | 19 | 12,197 | 6,723 | $6,278 | 26 | $127,617,130 |  |
| CA | 46 | 14 | 11 | 198,998 | 46,352 | $14,907 | 4 | $4,148,114,798 |  |
| CO | 70 | 3 | 24 | 43,398 | 14,709 | $5,817 | 29 | $338,023,799 |  |
| CT | 16 | 37 | 14 | 5,862 | 5,312 | $10,464 | 9 | $133,143,028 |  |
| DE | 9 | 42 | 4 | 999 | 419 | $12,052 | 8 | $17,090,424 |  |
| DC | 94 | 1 | 76 | 7,056 | 5,963 | $27,354 | 1 | $356,697,970 |  |
| FL | 63 | 7 | 0 | 149,100 | 0 | $2,946 | 44 | $443,714,085 |  |
| GA | 53 | 10 | 0 | 69,314 | 0 | $7,630 | 19 | $538,431,295 |  |
| HI | 7 | 43 | 4 | 1,060 | 577 | $8,109 | 16 | $13,273,747 |  |
| ID | 0 |  | 0 | 0 | 0 | $0 |  | $0 | No program |
| IL | 35 | 20 | 26 | 49,026 | 34,562 | $6,641 | 22 | $555,609,751 |  |
| IN | 7 |  | 0 | 6,018 | 0 | $601 |  | $3,616,054 | Work requirement (not ranked) |
| IA | 65 | 6 | 6 | 25,065 | 2,337 | $3,885 | 40 | $97,813,323 |  |
| KS | 45 | 16 | 22 | 16,116 | 7,745 | $4,815 | 36 | $119,446,934 |  |
| KY | 26 | 28 | 8 | 14,030 | 4,072 | $5,080 | 33 | $95,692,076 |  |
| LA | 35 | 22 | 1 | 19,403 | 481 | $5,584 | 31 | $111,023,907 |  |
| ME | 47 | 13 | 1 | 6,116 | 80 | $6,363 | 24 | $41,012,213 |  |
| MD | 38 | 19 | 8 | 27,947 | 5,799 | $7,933 | 17 | $269,734,230 |  |
| MA | 30 | 25 | 16 | 21,038 | 11,182 | $3,046 | 43 | $105,715,076 |  |
| MI | 43 | 17 | 0 | 47,981 | 0 | $13,604 | 6 | $652,720,000 |  |
| MN | 18 | 35 | 0.5 | 12,304 | 311 | $6,283 | 25 | $79,260,540 |  |
| MS | 23 | 29 | 0 | 8,076 | 0 | $4,832 | 35 | $39,022,295 |  |
| MO | 22 | 30 | 3 | 16,367 | 1,814 | $3,095 | 42 | $56,524,225 |  |
| MT | 0 |  | 0 | 0 | 0 | $0 |  | $0 | No program |
| NE | 34 | 23 | 16 | 8,560 | 4,034 | $2,008 | 45 | $26,532,334 |  |
| NV | 10 | 41 | 2 | 3,670 | 618 | $9,226 | 12 | $39,560,895 |  |
| NH | 0 |  | 0 | 0 | 0 | $0 |  | $0 | No program |
| NJ | 35 | 21 | 27 | 37,692 | 27,673 | $18,848 | 2 | $1,231,974,000 |  |
| NM | 53 | 11 | 22 | 11,633 | 4,796 | $13,761 | 5 | $226,084,608 |  |
| NY | 56 | 9 | 17 | 118,427 | 34,577 | $6,719 | 21 | $1,028,061,297 |  |
| NC | 21 | 32 | 0 | 26,707 | 0 | $6,254 | 27 | $167,027,011 |  |
| ND | 11 | 40 | 0 | 1,076 | 0 | $6,510 | 23 | $7,005,089 |  |
| OH | 13 | 38 | 5 | 17,432 | 6,162 | $5,110 | 32 | $120,573,483 |  |
| OK | 65 | 5 | 3 | 32,794 | 1,370 | $5,749 | 30 | $207,632,498 |  |
| OR | 17 | 36 | 13 | 7,200 | 5,137 | $17,072 | 3 | $216,587,540 |  |
| PA | 26 | 27 | 14 | 36,377 | 18,348 | $8,474 | 15 | $479,719,969 |  |
| RI | 26 | 26 | 0 | 2,864 | 0 | $9,858 | 10 | $28,232,929 |  |
| SC | 45 | 15 | 6 | 26,940 | 3,549 | $3,947 | 38 | $120,727,185 |  |
| SD | 0 |  | 0 | 0 | 0 | $0 |  | $0 | No program |
| TN | 20 | 33 | 1 | 16,627 | 874 | $4,886 | 34 | $85,505,733 |  |
| TX | 52 | 12 | 11 | 204,754 | 43,729 | $4,395 | 37 | $996,609,407 |  |
| UT | 2 | 44 | 1 | 1,189 | 464 | $3,917 | 39 | $6,474,481 |  |
| VT | 72 | 2 | 56 | 4,131 | 2,998 | $9,591 | 11 | $73,025,082 |  |
| VA | 22 | 31 | 3 | 21,596 | 2,829 | $6,120 | 28 | $149,480,336 |  |
| WA | 19 | 34 | 9 | 16,282 | 7,256 | $13,484 | 7 | $329,963,994 |  |
| WV | 66 | 4 | 7 | 11,904 | 1,279 | $8,810 | 13 | $120,466,591 |  |
| WI | 59 | 8 | 0.04 | 38,397 | 23 | $3,882 | 41 | $165,861,752 |  |
| WY | 0 |  | 0 | 0 | 0 | $0 |  | $0 | No program |

# Higher education

## sheeo_education_appropriations_per_fte: State and Local Education Appropriations per Full-Time-Equivalent Student, Public Colleges (SHEEO)

- unit: dollars
- period: Fiscal year 2025; year: 2025
- source: State Higher Education Executive Officers Association (SHEEO), State Higher Education Finance (SHEF): FY 2025, Table 3.2 (released April 2026) — https://shef.sheeo.org/wp-content/uploads/2026/04/SHEF_FY25_Report.pdf
- as_of: 2026-11-08
- raw: raw/national/sheeo-SHEF_FY25_Report.pdf
- note: Constant adjusted dollars: SHEEO adjusts for inflation (HECA), cost of living (COLI) and enrollment mix (EMI). Education appropriations are state and local support for public college operating expenses and student aid, excluding research, hospitals and medical education, and include federal stimulus funds. SHEEO publishes no numeric rank; its report says FY2025 values "ranged from $4,557 in New Hampshire to $25,468 in Illinois" (Figure 3.2 orders states from lowest to highest). The U.S. figure excludes DC.

| Place | Value FY2025 | Rank | FY2024 | FY2020 | FY2015 | % change since 2024 | % change since 2020 | Note |
|---|---|---|---|---|---|---|---|---|
| US | $12,082 |  | $12,205 | $10,801 | $9,423 | -1.0% | 11.9% |  |
| AL | $11,210 |  | $12,117 | $9,635 | $7,999 | -7.5% | 16.3% |  |
| AK | $22,141 |  | $20,894 | $19,832 | $20,278 | 6.0% | 11.6% |  |
| AZ | $6,064 |  | $6,874 | $7,085 | $7,503 | -11.8% | -14.4% |  |
| AR | $9,557 |  | $10,840 | $10,320 | $10,616 | -11.8% | -7.4% |  |
| CA | $12,773 |  | $12,342 | $10,954 | $9,537 | 3.5% | 16.6% |  |
| CO | $7,933 |  | $7,687 | $6,272 | $4,942 | 3.2% | 26.5% |  |
| CT | $15,096 |  | $16,627 | $11,382 | $11,230 | -9.2% | 32.6% |  |
| DE | $7,322 |  | $7,033 | $8,262 | $7,218 | 4.1% | -11.4% |  |
| DC | $21,848 |  | $22,583 | $29,319 | $19,878 | -3.3% | -25.5% |  |
| FL | $11,503 |  | $11,625 | $9,690 | $8,075 | -1.0% | 18.7% |  |
| GA | $12,727 |  | $13,379 | $12,588 | $10,963 | -4.9% | 1.1% |  |
| HI | $15,837 |  | $16,188 | $15,995 | $11,333 | -2.2% | -1.0% |  |
| ID | $12,100 |  | $12,783 | $12,045 | $10,524 | -5.3% | 0.5% |  |
| IL | $25,468 |  | $25,062 | $21,482 | $19,319 | 1.6% | 18.6% | Highest (SHEEO) |
| IN | $6,716 |  | $7,198 | $7,979 | $7,842 | -6.7% | -15.8% |  |
| IA | $7,296 |  | $7,221 | $7,394 | $8,493 | 1.0% | -1.3% |  |
| KS | $13,121 |  | $11,316 | $9,080 | $8,488 | 15.9% | 44.5% |  |
| KY | $10,608 |  | $10,494 | $9,346 | $9,467 | 1.1% | 13.5% |  |
| LA | $7,402 |  | $8,704 | $7,365 | $7,521 | -15.0% | 0.5% |  |
| ME | $9,028 |  | $9,729 | $8,826 | $8,186 | -7.2% | 2.3% |  |
| MD | $13,674 |  | $13,997 | $10,677 | $8,819 | -2.3% | 28.1% |  |
| MA | $14,644 |  | $14,835 | $10,238 | $8,803 | -1.3% | 43.0% |  |
| MI | $10,640 |  | $11,737 | $9,273 | $8,537 | -9.3% | 14.7% |  |
| MN | $11,191 |  | $11,849 | $10,664 | $8,423 | -5.6% | 4.9% |  |
| MS | $8,764 |  | $9,289 | $7,977 | $9,002 | -5.7% | 9.9% |  |
| MO | $10,972 |  | $10,767 | $10,567 | $9,734 | 1.9% | 3.8% |  |
| MT | $7,839 |  | $7,658 | $7,535 | $7,051 | 2.4% | 4.0% |  |
| NE | $13,760 |  | $13,628 | $12,995 | $12,058 | 1.0% | 5.9% |  |
| NV | $10,407 |  | $10,740 | $9,952 | $8,410 | -3.1% | 4.6% |  |
| NH | $4,557 |  | $4,673 | $4,041 | $4,488 | -2.5% | 12.8% | Lowest of the 50 states (SHEEO) |
| NJ | $10,194 |  | $10,729 | $9,770 | $9,248 | -5.0% | 4.3% |  |
| NM | $23,020 |  | $24,041 | $22,495 | $14,192 | -4.2% | 2.3% |  |
| NY | $16,047 |  | $15,995 | $14,549 | $12,777 | 0.3% | 10.3% |  |
| NC | $12,271 |  | $13,903 | $12,814 | $12,308 | -11.7% | -4.2% |  |
| ND | $10,066 |  | $10,804 | $10,315 | $11,324 | -6.8% | -2.4% |  |
| OH | $8,352 |  | $8,391 | $7,728 | $7,721 | -0.5% | 8.1% |  |
| OK | $9,379 |  | $9,877 | $8,995 | $10,075 | -5.0% | 4.3% |  |
| OR | $8,580 |  | $8,886 | $7,684 | $5,192 | -3.4% | 11.7% |  |
| PA | $7,227 |  | $7,070 | $6,746 | $5,708 | 2.2% | 7.1% |  |
| RI | $7,966 |  | $8,164 | $6,241 | $6,014 | -2.4% | 27.6% |  |
| SC | $10,049 |  | $9,607 | $8,052 | $6,663 | 4.6% | 24.8% |  |
| SD | $10,711 |  | $10,493 | $9,479 | $7,660 | 2.1% | 13.0% |  |
| TN | $14,955 |  | $14,997 | $13,125 | $10,397 | -0.3% | 13.9% |  |
| TX | $14,879 |  | $14,811 | $13,471 | $9,740 | 0.5% | 10.4% |  |
| UT | $12,153 |  | $13,347 | $10,525 | $9,016 | -8.9% | 15.5% |  |
| VT | $5,470 |  | $5,568 | $4,396 | $3,513 | -1.8% | 24.4% |  |
| VA | $11,547 |  | $10,252 | $8,753 | $6,633 | 12.6% | 31.9% |  |
| WA | $14,409 |  | $13,434 | $10,069 | $7,365 | 7.3% | 43.1% |  |
| WV | $8,432 |  | $7,640 | $7,566 | $7,042 | 10.4% | 11.4% |  |
| WI | $9,955 |  | $10,306 | $10,127 | $10,211 | -3.4% | -1.7% |  |
| WY | $18,689 |  | $22,090 | $22,727 | $21,539 | -15.4% | -17.8% |  |

## college_tuition_public_in_state: Published Tuition and Fees at Public Colleges, In-State (College Board)

- unit: dollars
- period: Academic year 2026-27; year: 2027
- source: College Board, Trends in College Pricing 2026 (November 2026), Figures CP-5 and CP-6, from the report's Excel data file — https://research.collegeboard.org/media/xlsx/trends-in-college-pricing-2026-excel-data.xlsx (report: https://research.collegeboard.org/media/pdf/trends-in-college-pricing-and-student-aid-2026.pdf)
- as_of: 2026-11-08
- raw: raw/national/collegeboard-trends-in-college-pricing-2026-excel-data.xlsx; raw/national/collegeboard-trends-in-college-pricing-and-student-aid-2026.pdf
- note: Enrollment-weighted averages for full-time undergraduates, rounded by College Board to the nearest $10. Value = public four-year, in-state tuition and fees. Two-year = public two-year, in-district. College Board publishes no rank; its report says 2026-27 four-year in-state prices "range from $6,360 in Florida and $7,690 in North Carolina to $18,350 in New Hampshire, $18,570 in Vermont, and $18,710 in New Jersey." "5-year change" is College Board's inflation-adjusted percent change from 2021-22 to 2026-27, shown to one decimal (**derived** by multiplying College Board's fraction by 100 and rounding). Published ("sticker") prices are before grant aid. The figures have no DC row, and no Alaska row for two-year colleges ("—"). The Excel sheets note they were prepared in October 2026.

| Place | Value: 4-year in-state | Rank | 4-year out-of-state | 4-year 5-year change, inflation-adjusted (%) | 2-year in-district | 2-year 5-year change, inflation-adjusted (%) | Note |
|---|---|---|---|---|---|---|---|
| US | 12,290 |  | 32,730 | -6.8 | 4,210 | -9.7 |  |
| AL | 12,790 |  | 32,390 | -7.9 | 6,000 | -0.8 |  |
| AK | 10,090 |  | 27,650 | -6.6 | — | — |  |
| AZ | 13,660 |  | 39,500 | -5.7 | 2,950 | -7.0 |  |
| AR | 10,830 |  | 29,180 | -4.5 | 5,040 | 5.9 |  |
| CA | 12,560 |  | 44,070 | 3.1 | 1,440 | -17.7 |  |
| CO | 14,130 |  | 38,110 | -2.0 | 5,720 | -2.7 |  |
| CT | 17,470 |  | 36,310 | -4.4 | 5,220 | -5.7 |  |
| DE | 17,150 |  | 41,350 | 0.6 | 5,070 | -16.3 |  |
| DC | — |  | — | — | — | — |  |
| FL | 6,360 |  | 26,310 | -18.4 | 3,240 | -18.5 |  |
| GA | 8,540 |  | 28,550 | -21.6 | 4,250 | -13.8 |  |
| HI | 11,740 |  | 32,980 | -12.9 | 4,020 | -18.4 |  |
| ID | 9,590 |  | 28,990 | -2.2 | 4,870 | -4.9 |  |
| IL | 16,070 |  | 31,270 | -10.6 | 4,950 | -8.7 |  |
| IN | 10,610 |  | 33,060 | -12.9 | 5,510 | -10.1 |  |
| IA | 11,510 |  | 32,300 | -2.8 | 6,900 | -2.7 |  |
| KS | 11,010 |  | 27,280 | -4.1 | 4,040 | -2.7 |  |
| KY | 12,720 |  | 27,440 | -7.1 | 6,180 | -10.1 |  |
| LA | 11,010 |  | 23,660 | -10.6 | 5,330 | 3.6 |  |
| ME | 13,260 |  | 33,620 | -1.9 | 4,160 | -11.6 |  |
| MD | 11,850 |  | 28,250 | -6.3 | 5,160 | -13.3 |  |
| MA | 16,440 |  | 36,600 | -4.1 | 7,780 | -7.2 |  |
| MI | 17,320 |  | 47,590 | -1.5 | 4,780 | -5.4 |  |
| MN | 15,390 |  | 31,840 | 0.9 | 6,800 | -5.9 |  |
| MS | 10,450 |  | 25,830 | -3.9 | 4,280 | -2.4 |  |
| MO | 13,720 |  | 29,880 | 14.2 | 5,000 | -1.2 |  |
| MT | 9,270 |  | 33,180 | 4.1 | 4,700 | -2.6 |  |
| NE | 10,490 |  | 25,160 | -4.6 | 3,830 | -8.2 |  |
| NV | 10,630 |  | 30,770 | 3.5 | 4,850 | 4.1 |  |
| NH | 18,350 |  | 36,560 | -11.9 | 7,890 | -9.3 |  |
| NJ | 18,710 |  | 35,950 | 2.0 | 6,920 | 2.9 |  |
| NM | 9,290 |  | 26,230 | -5.0 | 2,350 | -2.3 |  |
| NY | 8,750 |  | 24,130 | -16.6 | 6,250 | -11.3 |  |
| NC | 7,690 |  | 26,140 | -15.0 | 2,580 | -15.1 |  |
| ND | 11,680 |  | 16,350 | -5.5 | 6,740 | 0.5 |  |
| OH | 14,240 |  | 33,260 | -3.7 | 6,230 | 0.1 |  |
| OK | 10,610 |  | 26,330 | -5.1 | 4,890 | -13.0 |  |
| OR | 15,560 |  | 42,370 | 3.6 | 7,120 | -3.7 |  |
| PA | 17,520 |  | 35,340 | -6.6 | 6,560 | -5.0 |  |
| RI | 16,570 |  | 37,920 | -4.1 | 6,080 | -0.4 |  |
| SC | 13,330 |  | 37,430 | -17.5 | 6,410 | -11.5 |  |
| SD | 9,680 |  | 13,430 | -15.0 | 7,710 | -13.1 |  |
| TN | 12,190 |  | 27,580 | -5.9 | 5,350 | -5.8 |  |
| TX | 11,330 |  | 30,380 | -16.7 | 3,300 | -6.7 |  |
| UT | 8,400 |  | 27,400 | -7.2 | 4,630 | -6.9 |  |
| VT | 18,570 |  | 46,240 | -14.6 | 8,950 | -15.1 |  |
| VA | 16,600 |  | 40,920 | -4.1 | 5,910 | -7.8 |  |
| WA | 12,700 |  | 39,800 | -4.7 | 5,620 | -4.4 |  |
| WV | 10,270 |  | 27,610 | -4.0 | 5,600 | 3.6 |  |
| WI | 10,880 |  | 33,930 | -3.1 | 5,270 | -7.7 |  |
| WY | 7,710 |  | 24,570 | 3.2 | 4,990 | -10.6 |  |

## college_freshmen_stay_in_state: New College Students Who Enrolled in Their Home State

- unit: number
- period: Fall 2022 (first-time students who finished high school in the previous 12 months); year: 2023
- source: NCES, Digest of Education Statistics 2023, Table 309.20 (current version per the Digest "current tables" list on 2026-11-08) — https://nces.ed.gov/programs/digest/d23/tables/dt23_309.20.asp
- as_of: 2026-11-08
- raw: raw/national/nces-digest-d23-309.20.xlsx, raw/national/nces-digest-d23-309.20.html
- note: Degree-granting colleges. "Value" is NCES's ratio of a state's residents enrolled in their home state to its residents enrolled in any state (two decimals, as NCES shows it). "Share staying, %" is **derived**: residents enrolled in home state ÷ residents enrolled in any state × 100, from the counts in the same table, rounded to one decimal. "Left the state" and "Came from other states" are NCES's out-of-state and into-state migration counts.

| Place | Value | Rank | Share staying, % (derived) | Residents enrolled anywhere | Enrolled in home state | Left the state | Came from other states | Net migration | Note |
|---|---|---|---|---|---|---|---|---|---|
| US | 0.78 |  | 77.7 | 2,085,459 | 1,619,747 | 465,712 | 520,137 | 54,425 |  |
| AL | 0.87 |  | 87.3 | 30,421 | 26,559 | 3,862 | 13,229 | 9,367 |  |
| AK | 0.45 |  | 44.6 | 2,589 | 1,155 | 1,434 | 195 | -1,239 |  |
| AZ | 0.85 |  | 84.7 | 37,140 | 31,453 | 5,687 | 19,235 | 13,548 |  |
| AR | 0.86 |  | 85.7 | 17,626 | 15,111 | 2,515 | 7,275 | 4,760 |  |
| CA | 0.86 |  | 85.7 | 271,020 | 232,338 | 38,682 | 26,403 | -12,279 |  |
| CO | 0.64 |  | 64.0 | 32,989 | 21,115 | 11,874 | 8,409 | -3,465 |  |
| CT | 0.54 |  | 53.7 | 28,405 | 15,250 | 13,155 | 10,069 | -3,086 |  |
| DE | 0.60 |  | 60.3 | 5,813 | 3,505 | 2,308 | 3,905 | 1,597 |  |
| DC | 0.16 |  | 16.4 | 2,625 | 430 | 2,195 | 9,291 | 7,096 |  |
| FL | 0.86 |  | 85.5 | 112,207 | 95,992 | 16,215 | 20,233 | 4,018 |  |
| GA | 0.78 |  | 77.8 | 68,797 | 53,532 | 15,265 | 13,710 | -1,555 |  |
| HI | 0.55 |  | 55.3 | 7,921 | 4,383 | 3,538 | 2,227 | -1,311 |  |
| ID | 0.73 |  | 72.6 | 9,854 | 7,155 | 2,699 | 5,052 | 2,353 |  |
| IL | 0.63 |  | 63.3 | 86,970 | 55,056 | 31,914 | 13,714 | -18,200 |  |
| IN | 0.84 |  | 84.3 | 40,313 | 33,991 | 6,322 | 17,169 | 10,847 |  |
| IA | 0.85 |  | 85.1 | 21,679 | 18,448 | 3,231 | 10,953 | 7,722 |  |
| KS | 0.81 |  | 81.2 | 20,440 | 16,600 | 3,840 | 7,292 | 3,452 |  |
| KY | 0.86 |  | 85.6 | 26,813 | 22,963 | 3,850 | 7,462 | 3,612 |  |
| LA | 0.86 |  | 85.6 | 28,281 | 24,208 | 4,073 | 7,007 | 2,934 |  |
| ME | 0.69 |  | 68.7 | 7,755 | 5,324 | 2,431 | 3,597 | 1,166 |  |
| MD | 0.61 |  | 61.4 | 41,292 | 25,342 | 15,950 | 7,819 | -8,131 |  |
| MA | 0.61 |  | 60.7 | 50,516 | 30,664 | 19,852 | 26,635 | 6,783 |  |
| MI | 0.87 |  | 86.5 | 57,475 | 49,720 | 7,755 | 10,206 | 2,451 |  |
| MN | 0.63 |  | 63.5 | 40,172 | 25,496 | 14,676 | 7,283 | -7,393 |  |
| MS | 0.91 |  | 90.6 | 19,461 | 17,638 | 1,823 | 6,886 | 5,063 |  |
| MO | 0.77 |  | 77.0 | 37,470 | 28,868 | 8,602 | 9,122 | 520 |  |
| MT | 0.72 |  | 71.6 | 5,117 | 3,666 | 1,451 | 3,534 | 2,083 |  |
| NE | 0.76 |  | 75.8 | 15,704 | 11,909 | 3,795 | 3,734 | -61 |  |
| NV | 0.75 |  | 74.8 | 14,432 | 10,791 | 3,641 | 854 | -2,787 |  |
| NH | 0.46 |  | 45.8 | 8,223 | 3,768 | 4,455 | 4,626 | 171 |  |
| NJ | 0.57 |  | 57.3 | 73,273 | 41,979 | 31,294 | 5,420 | -25,874 |  |
| NM | 0.82 |  | 81.6 | 12,409 | 10,120 | 2,289 | 2,152 | -137 |  |
| NY | 0.76 |  | 76.4 | 136,516 | 104,347 | 32,169 | 36,487 | 4,318 |  |
| NC | 0.86 |  | 85.6 | 60,314 | 51,610 | 8,704 | 15,617 | 6,913 |  |
| ND | 0.75 |  | 74.8 | 4,636 | 3,470 | 1,166 | 3,600 | 2,434 |  |
| OH | 0.84 |  | 83.8 | 70,741 | 59,310 | 11,431 | 17,743 | 6,312 |  |
| OK | 0.84 |  | 84.3 | 20,980 | 17,683 | 3,297 | 6,349 | 3,052 |  |
| OR | 0.74 |  | 74.2 | 20,474 | 15,199 | 5,275 | 8,469 | 3,194 |  |
| PA | 0.73 |  | 72.8 | 69,509 | 50,633 | 18,876 | 27,881 | 9,005 |  |
| RI | 0.66 |  | 66.1 | 7,687 | 5,082 | 2,605 | 8,401 | 5,796 |  |
| SC | 0.85 |  | 84.8 | 30,142 | 25,573 | 4,569 | 11,890 | 7,321 |  |
| SD | 0.74 |  | 74.4 | 5,843 | 4,345 | 1,498 | 3,277 | 1,779 |  |
| TN | 0.81 |  | 81.0 | 42,591 | 34,492 | 8,099 | 13,489 | 5,390 |  |
| TX | 0.86 |  | 85.7 | 204,641 | 175,476 | 29,165 | 14,772 | -14,393 |  |
| UT | 0.89 |  | 88.7 | 18,806 | 16,682 | 2,124 | 8,995 | 6,871 |  |
| VT | 0.41 |  | 41.1 | 3,042 | 1,249 | 1,793 | 4,543 | 2,750 |  |
| VA | 0.79 |  | 78.5 | 61,475 | 48,275 | 13,200 | 15,704 | 2,504 |  |
| WA | 0.67 |  | 67.0 | 36,735 | 24,629 | 12,106 | 7,091 | -5,015 |  |
| WV | 0.86 |  | 86.2 | 8,781 | 7,571 | 1,210 | 4,589 | 3,379 |  |
| WI | 0.77 |  | 76.9 | 35,151 | 27,042 | 8,109 | 12,333 | 4,224 |  |
| WY | 0.73 |  | 73.0 | 3,208 | 2,342 | 866 | 1,422 | 556 |  |

# Attendance

## chronic_absenteeism_rate: Chronic Absenteeism Rate (AEI Return to Learn Tracker)

- unit: percent
- period: School years 2018-19 through 2024-25 (AEI labels years by the spring: 2025 = 2024-25); year: 2025
- source: American Enterprise Institute (AEI), Nat Malkus, "From Attendance Crisis to Chronic Condition? Tracking Post-Pandemic Chronic Absenteeism into 2025" (June 2026), Appendix Table A2 "Complete Chronic Absenteeism Data by State, School Years 2017–25"; data from the Return to Learn Tracker — https://www.aei.org/wp-content/uploads/2026/06/From-Attendance-Crisis-to-Chronic-Condition-Tracking-Post-Pandemic-Chronic-Absenteeism-into-2025.pdf (tracker: https://www.returntolearntracker.net/, updated Oct 30, 2026)
- as_of: 2026-11-08
- raw: raw/national/aei-2026-06-chronic-absenteeism-into-2025.pdf; raw/national/aei-r2l-state-chronic-absenteeism-2018-2025.csv (tracker chart data, 45 states + DC); raw/national/aei-returntolearntracker-home-2026-11-08.html
- note: Share of students missing 10% or more of school days, for any reason. This is a research tracker, not an official federal statistic: AEI builds state rates from state-reported district data, "backfilled with EdFacts data when state data are unavailable" (Table A2 note), weighting districts by student counts. New Hampshire does not publish its own rate; NH is absent from AEI's state-reported-only Table A3, so NH figures here come from federal EdFacts counts of chronically absent students, which AEI pairs with NCES enrollment counts (an imperfect denominator, per AEI's methods). AEI's "Total" (US row) covers different numbers of states each year and "are not comparable over years" (Table A2 note); for 2025 it covers 45 states. "—" = no data. AEI cautions that what counts as an absence differs by state. AEI shows whole percents in Table A2.

| Place | Value 2024-25 | Rank | 2023-24 | 2022-23 | 2021-22 | 2020-21 | 2019-20 | 2018-19 | Note |
|---|---|---|---|---|---|---|---|---|---|
| US | 22.7 |  | 23.1 | 25.4 | 28.5 | 18.9 | 13.3 | 15.1 | AEI "Total" (not comparable across years) |
| AL | 12 |  | 15 | 18 | 18 | 8 | 9 | 11 |  |
| AK | 41 |  | 41 | 43 | 46 | 22 | 17 | 28 |  |
| AZ | — |  | — | 42 | 48 | 25 | 16 | 25 |  |
| AR | 29 |  | 27 | 22 | 26 | 17 | 22 | 22 |  |
| CA | 20 |  | 21 | 25 | 30 | 14 | 0 | 13 |  |
| CO | 29 |  | 28 | 31 | 35 | 26 | 23 | 22 |  |
| CT | 17 |  | 18 | 20 | 24 | 19 | 12 | 10 |  |
| DE | 17 |  | 20 | 23 | 25 | 22 | 17 | 15 |  |
| DC | 40 |  | 40 | 44 | 48 | 31 | 29 | 33 |  |
| FL | 29 |  | 31 | 31 | 32 | 25 | 17 | 20 |  |
| GA | 20 |  | 22 | 23 | 25 | 21 | 9 | 13 |  |
| HI | 24 |  | 25 | 27 | 34 | 18 | 8 | 14 |  |
| ID | 15 |  | 16 | 17 | 21 | 16 | 8 | 3 |  |
| IL | 25 |  | 26 | 28 | 30 | 21 | 11 | 18 |  |
| IN | 18 |  | 19 | 21 | 23 | 20 | 11 | 12 |  |
| IA | 16 |  | 22 | 21 | 26 | 21 | 17 | 12 |  |
| KS | 20 |  | 21 | 23 | 26 | 18 | 14 | 14 |  |
| KY | 25 |  | 28 | 30 | 28 | 22 | 12 | 18 |  |
| LA | 23 |  | 25 | 22 | 21 | 29 | 12 | 18 |  |
| ME | 23 |  | 23 | 26 | 30 | 21 | 18 | 17 |  |
| MD | 25 |  | 27 | 30 | 31 | 18 | 18 | 20 |  |
| MA | 19 |  | 20 | 22 | 28 | 18 | 13 | 13 |  |
| MI | 29 |  | 30 | 31 | 39 | 20 | 21 | 20 |  |
| MN | — |  | 24 | 25 | 30 | 17 | 15 | 14 |  |
| MS | 28 |  | 25 | 24 | 28 | 21 | 9 | 14 |  |
| MO | 21 |  | 22 | 23 | 24 | 17 | 15 | 13 |  |
| MT | — |  | — | 37 | 38 | 27 | 14 | 23 |  |
| NE | 21 |  | 22 | 22 | 24 | 21 | 15 | 15 |  |
| NV | 25 |  | 29 | 35 | 36 | 31 | 20 | 19 |  |
| NH | — |  | — | 25 | 35 | 18 | 13 | 14 |  |
| NJ | 14 |  | 15 | 17 | 18 | 13 | 8 | 11 |  |
| NM | 33 |  | 30 | 39 | 41 | 30 | 16 | 18 |  |
| NY | 27 |  | 27 | 29 | 32 | 24 | 21 | 19 |  |
| NC | 25 |  | 26 | 27 | 32 | 27 | 10 | 16 |  |
| ND | 22 |  | 20 | 20 | 22 | 16 | 11 | 12 |  |
| OH | 24 |  | 24 | 26 | 29 | 23 | 10 | 16 |  |
| OK | 22 |  | 21 | 23 | 23 | 14 | 19 | 17 |  |
| OR | 34 |  | 34 | 38 | 36 | 28 | 22 | 20 |  |
| PA | 21 |  | 21 | 22 | 26 | 18 | 15 | 15 |  |
| RI | 22 |  | 25 | 29 | 34 | 28 | 18 | 19 |  |
| SC | 22 |  | 22 | 25 | 20 | 8 | 14 | 13 |  |
| SD | 20 |  | 21 | 21 | 22 | 18 | 11 | 14 |  |
| TN | 18 |  | 18 | 20 | 20 | 15 | 13 | 13 |  |
| TX | — |  | 19 | 20 | 26 | 15 | 7 | 11 |  |
| UT | 23 |  | 23 | 25 | 29 | 19 | 9 | 14 |  |
| VT | 25 |  | 26 | 29 | 40 | 26 | 19 | 17 |  |
| VA | 14 |  | 15 | 19 | 20 | 11 | 12 | 11 |  |
| WA | 27 |  | 27 | 30 | 33 | 19 | 9 | 15 |  |
| WV | 23 |  | 24 | 28 | 29 | 13 | 19 | 20 |  |
| WI | 17 |  | 18 | 19 | 22 | 16 | 13 | 13 |  |
| WY | — |  | — | 35 | 37 | 2 | 2 | 2 |  |

# Youth health (YRBS)

## yrbs_sad_hopeless: High School Students Who Felt Sad or Hopeless (YRBS)

- unit: percent
- period: Spring of 2019, 2021, 2023 and 2025 survey years; year: 2025
- source: CDC, Youth Risk Behavior Surveillance System (YRBS), YRBS Explorer, question H26 — https://yrbs-explorer.services.cdc.gov/ (data via https://yrbs-explorer.services.cdc.gov/api/TableData?QuestionId=H26&Yr=<year>&LocationId=<NH or XX>)
- as_of: 2026-11-08
- raw: raw/national/yrbs-explorer/tabledata-H26-NH-<year>.json, tabledata-H26-XX-<year>.json, footnotes-H26-NH.json
- note: Public high school students (grades 9-12). CDC's definition: felt sad or hopeless, almost every day for >=2 weeks in a row so that they stopped doing some usual activities, during the 12 months before the survey. "US" is CDC's national YRBS (a separate national sample); NH is New Hampshire's state YRBS. Values are weighted percents with 95% confidence intervals (CI) as CDC shows them; overlapping intervals mean a difference may not be statistically meaningful, and CDC's Explorer does not test NH against the US. The 2023 values match CDC's open-data file "YRBSS – Mental Health Indicators" (data.cdc.gov nu3s-3dwd) where that file covers the question.

| Place | Value 2025 | Rank | 95% CI 2025 | Value 2023 | 95% CI 2023 | Value 2021 | Value 2019 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 33.3 |  | 31.2–35.5 | 39.7 | 37.7–41.7 | 42.3 | 36.7 |  |
| NH | 34.2 |  | 33.1–35.3 | 39.6 | 38.5–40.7 | 44.2 | 33.6 |  |

## yrbs_considered_suicide: High School Students Who Seriously Considered Attempting Suicide (YRBS)

- unit: percent
- period: Spring of 2019, 2021, 2023 and 2025 survey years; year: 2025
- source: CDC, Youth Risk Behavior Surveillance System (YRBS), YRBS Explorer, question H27 — https://yrbs-explorer.services.cdc.gov/ (data via https://yrbs-explorer.services.cdc.gov/api/TableData?QuestionId=H27&Yr=<year>&LocationId=<NH or XX>)
- as_of: 2026-11-08
- raw: raw/national/yrbs-explorer/tabledata-H27-NH-<year>.json, tabledata-H27-XX-<year>.json, footnotes-H27-NH.json
- note: Public high school students (grades 9-12). CDC's definition: seriously considered attempting suicide, during the 12 months before the survey. "US" is CDC's national YRBS (a separate national sample); NH is New Hampshire's state YRBS. Values are weighted percents with 95% confidence intervals (CI) as CDC shows them; overlapping intervals mean a difference may not be statistically meaningful, and CDC's Explorer does not test NH against the US. The 2023 values match CDC's open-data file "YRBSS – Mental Health Indicators" (data.cdc.gov nu3s-3dwd) where that file covers the question.

| Place | Value 2025 | Rank | 95% CI 2025 | Value 2023 | 95% CI 2023 | Value 2021 | Value 2019 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 14.5 |  | 13.4–15.6 | 20.4 | 18.7–22.3 | 22.2 | 18.8 |  |
| NH | 15.9 |  | 15.1–16.7 | 21.3 | 20.4–22.3 | 24.7 | 18.4 |  |

## yrbs_bullied_at_school: High School Students Who Were Bullied on School Property (YRBS)

- unit: percent
- period: Spring of 2019, 2021, 2023 and 2025 survey years; year: 2025
- source: CDC, Youth Risk Behavior Surveillance System (YRBS), YRBS Explorer, question H23 — https://yrbs-explorer.services.cdc.gov/ (data via https://yrbs-explorer.services.cdc.gov/api/TableData?QuestionId=H23&Yr=<year>&LocationId=<NH or XX>)
- as_of: 2026-11-08
- raw: raw/national/yrbs-explorer/tabledata-H23-NH-<year>.json, tabledata-H23-XX-<year>.json, footnotes-H23-NH.json
- note: Public high school students (grades 9-12). CDC's definition: were bullied on school property, during the 12 months before the survey. "US" is CDC's national YRBS (a separate national sample); NH is New Hampshire's state YRBS. Values are weighted percents with 95% confidence intervals (CI) as CDC shows them; overlapping intervals mean a difference may not be statistically meaningful, and CDC's Explorer does not test NH against the US. The 2023 values match CDC's open-data file "YRBSS – Mental Health Indicators" (data.cdc.gov nu3s-3dwd) where that file covers the question.

| Place | Value 2025 | Rank | 95% CI 2025 | Value 2023 | 95% CI 2023 | Value 2021 | Value 2019 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 19.7 |  | 18.3–21.2 | 19.2 | 17.3–21.4 | 15.0 | 19.5 |  |
| NH | 23.1 |  | 22.2–24.1 | 24.2 | 23.2–25.3 | 20.0 | 23.0 |  |

## yrbs_electronically_bullied: High School Students Who Were Electronically Bullied (YRBS)

- unit: percent
- period: Spring of 2019, 2021, 2023 and 2025 survey years; year: 2025
- source: CDC, Youth Risk Behavior Surveillance System (YRBS), YRBS Explorer, question H24 — https://yrbs-explorer.services.cdc.gov/ (data via https://yrbs-explorer.services.cdc.gov/api/TableData?QuestionId=H24&Yr=<year>&LocationId=<NH or XX>)
- as_of: 2026-11-08
- raw: raw/national/yrbs-explorer/tabledata-H24-NH-<year>.json, tabledata-H24-XX-<year>.json, footnotes-H24-NH.json
- note: Public high school students (grades 9-12). CDC's definition: were electronically bullied, counting being bullied through texting, Instagram, Facebook, or other social media, during the 12 months before the survey. "US" is CDC's national YRBS (a separate national sample); NH is New Hampshire's state YRBS. Values are weighted percents with 95% confidence intervals (CI) as CDC shows them; overlapping intervals mean a difference may not be statistically meaningful, and CDC's Explorer does not test NH against the US. The 2023 values match CDC's open-data file "YRBSS – Mental Health Indicators" (data.cdc.gov nu3s-3dwd) where that file covers the question.

| Place | Value 2025 | Rank | 95% CI 2025 | Value 2023 | 95% CI 2023 | Value 2021 | Value 2019 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 14.6 |  | 13.5–15.8 | 16.3 | 14.2–18.5 | 15.9 | 15.7 |  |
| NH | 18.2 |  | 17.3–19.1 | 21.5 | 20.7–22.4 | 21.8 | 20.1 |  |

## yrbs_missed_school_unsafe: High School Students Who Missed School Because They Felt Unsafe (YRBS)

- unit: percent
- period: Spring of 2019, 2021, 2023 and 2025 survey years; year: 2025
- source: CDC, Youth Risk Behavior Surveillance System (YRBS), YRBS Explorer, question H13 — https://yrbs-explorer.services.cdc.gov/ (data via https://yrbs-explorer.services.cdc.gov/api/TableData?QuestionId=H13&Yr=<year>&LocationId=<NH or XX>)
- as_of: 2026-11-08
- raw: raw/national/yrbs-explorer/tabledata-H13-NH-<year>.json, tabledata-H13-XX-<year>.json, footnotes-H13-NH.json
- note: Public high school students (grades 9-12). CDC's definition: did not go to school because they felt unsafe at school or on their way to or from school, on at least 1 day during the 30 days before the survey. "US" is CDC's national YRBS (a separate national sample); NH is New Hampshire's state YRBS. Values are weighted percents with 95% confidence intervals (CI) as CDC shows them; overlapping intervals mean a difference may not be statistically meaningful, and CDC's Explorer does not test NH against the US. The 2023 values match CDC's open-data file "YRBSS – Mental Health Indicators" (data.cdc.gov nu3s-3dwd) where that file covers the question.

| Place | Value 2025 | Rank | 95% CI 2025 | Value 2023 | 95% CI 2023 | Value 2021 | Value 2019 | Note |
|---|---|---|---|---|---|---|---|---|
| US | 10.6 |  | 9.3–12.0 | 12.8 | 10.4–15.6 | 8.6 | 8.7 |  |
| NH | 8.1 |  | 7.6–8.7 | 10.3 | 9.7–11.0 | 9.6 | 6.9 |  |

---

## Not retrieved

| What | URL | What was tried / result |
|---|---|---|
| NAEP 2024 grade 8 science by state | https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&subject=science&grade=8&subscale=SRPUV&... | Not collected by NAEP: the Data Service returns error flag 320 (no data) for every state in 2024 and 2019; NCES's report is "Grade 8 Results for the Nation." National values are in `naep_g8_science`. |
| Newer NCES Digest editions of Tables 219.46, 203.70, 208.40, 309.20 | https://nces.ed.gov/programs/digest/d24/tables/dt24_219.46.asp (and d24/d25 for the others) | 404 for the 2024 and 2025 editions; the Digest "current tables" list (https://nces.ed.gov/programs/digest/current_tables.asp) points to the 2023 edition for all four. The 2025 Digest has only selected tables, none of these. |
| Graduation rate (ACGR) by state for the class of 2024 | https://eddataexpress.ed.gov/download/data-library | All 25 pages of the Data Library were read in a browser (plain downloads get an empty 202 response). Newest state-level ACGR file listed: 2022-23 (used). |
| Chronic absenteeism by state, 2022-23 and later, from ED Data Express | https://eddataexpress.ed.gov/download/data-library | Same listing: newest state-level file is 2021-22 (counts only, no rates). The earlier research note of a 2022-23 school-level file could not be confirmed in today's listing. AEI's tracker used instead. |
| New Hampshire chronic absenteeism rate, 2023-24 and 2024-25 | https://www.returntolearntracker.net/ ; AEI June 2026 report | Not in AEI's data (NH "—" for 2024 and 2025); NH has no row in AEI's state-reported table. No other source found. |
| Attendance Works state chronic absence files | https://www.attendanceworks.org/tools/state-data/ | Page read; it offers 2021-22 per-state zip files built from federal data. Not downloaded, because AEI's table covers more recent years from the same federal counts plus state data. |
| NH DHHS Youth Risk Behavior Survey pages (regional 2023 reports, NH 2025 reports) | https://www.dhhs.nh.gov/programs-services/population-health/health-statistics-informatics/youth-risk-behavior-survey | curl returned 403 (the site blocks automated requests). NH statewide results for 2019–2025 came from CDC's YRBS Explorer instead; regional figures were not collected. |
| YRBS for other states | https://yrbs-explorer.services.cdc.gov/ | Not collected beyond NH and the U.S. (the task asked for NH vs U.S.). CDC's mental-health file in `raw/national/cdc-yrbss-mental-health-indicators-nu3s-3dwd-total.csv` has about 40 states for sadness/hopelessness and suicide questions, 2019–2023, if a state table is wanted later. |
| Census school finance FY2025 | https://www2.census.gov/programs-surveys/school-finances/tables/2025/secondary-education-finance/elsec25_sumtables.xlsx | 404; the tables directory lists years through 2024. FY2024 used. |
| Census rank for support-services spending per pupil; ranks for revenue shares | elsec24_sumtables.xlsx, Tables 5, 8 and 11 | Not published: Table 11 ranks per-pupil amounts (total, instruction, salaries, benefits, administration; revenue per pupil by source) but not support services or percentage shares. |
| Current-edition NAEP technical documentation on multiple comparisons | https://nces.ed.gov/nationsreportcard/tdw/analysis/2004_2005/infer_multiplecompare_fdr.aspx | 404; the 2000–2001 edition of the same page loads and is cited. |
| SHEEO numeric state ranks | https://shef.sheeo.org/wp-content/uploads/2026/04/SHEF_FY25_Report.pdf | SHEEO publishes an ordered chart (Figure 3.2) and the low/high states, not numeric ranks. |
| College Board values for DC (both sectors) and Alaska (two-year) | trends-in-college-pricing-2026-excel-data.xlsx, Figures CP-5 and CP-6 | Not in College Board's figures. |
| Individual NAEP-equivalent classification for Smarter Balanced (SBAC) states | NCES 2026-014 | The report classifies SBAC as a whole (NAEP Basic in all four) and gives each SBAC state's own score in the Technical Notes without a level; the tables show the state score and the SBAC-wide level. |
