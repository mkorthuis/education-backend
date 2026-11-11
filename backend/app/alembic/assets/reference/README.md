# Additional Data for Ask NH Education Facts

Data gathered from public sources to answer the general questions in *Ask NH Facts - General Questions and Data Strategy.md* (Desktop): the facts and figures the site's database doesn't have yet. Everything here is cited, so it can be checked and later loaded into the database.

Gathered starting November 8, 2026.

## Files

| File | Strategy type | What's in it |
|---|---|---|
| `national-comparisons.md` | 2. How NH compares | State-by-state figures: NAEP, graduation, students, spending, teacher pay, preschool, higher education, absenteeism, youth health |
| `facts-rules-and-rights.md` | 3. Rules and rights | What NH and federal law require: special education, attendance, bullying, discipline, records, kindergarten, homeschooling, EFAs, charter schools, graduation |
| `facts-terms-and-how-schools-work.md` | 5. What the numbers mean; 6. How schools are run and paid for | Definitions of the site's measures and terms; governance, budgets, taxes and state aid |
| `programs-and-help.md` (+ CSVs in `raw/programs/`) | 4. Finding help and programs | Head Start, EFA providers, career centers, dual enrollment, family support organizations, who to call |
| `town-figures.md` (+ CSVs in `raw/town/`) | 6. How schools are paid for (numbers) | Tax rates and the school share by town; state adequacy aid by town |
| `state-issues.md` | 3. Rules and rights; 6. How schools are run and paid for | The state laws, court cases, budgets, elections and trends affecting public schools in 2025-26: the school tax cap and Question 2, the school funding cases, special education aid, EFAs and other school choice bills, rights laws and lawsuits, safety and health, teachers |
| `district-practices.md` | 1. Local practices | Kindergarten, preschool, budget votes and high school tuition options, district by district |
| `research-briefs.md` | 7. What the research says | Short, neutral summaries of strong studies on recurring "does it work?" questions |
| `outcomes-after-high-school.md` | 8. Life after high school | College-going, persistence, career and technical education, apprenticeships, students with disabilities after school |

Raw downloads (API responses, spreadsheets, PDFs) are kept in `raw/<area>/` so every figure can be traced back.

## Rules for every file

1. **Only what a source says.** Every fact and number comes from a page or file that was actually read or downloaded, never from memory. Numbers are copied exactly. A figure we calculated (a share, a sum) is marked **derived**, with how it was calculated.
2. **Primary sources first:** the statute or rule text (gc.nh.gov), federal regulations (ecfr.gov), and the agency's own data. News and advocacy sites are used only to find a primary source, not cited in its place.
3. **Plain and neutral.** Short sentences and everyday words, explaining any term. No opinions, no advice on how to vote or what to choose, and no loaded words on contested topics (EFAs, funding, taxes).
4. **Dated.** `as_of` is the date the source was checked, or "Wayback snapshot YYYY-MM-DD" when only an archived copy could be reached.
5. **Gaps are written down.** Anything that couldn't be retrieved goes in the file's *Not retrieved* section, with the URL and what was tried.

## Formats

### Facts (topics and statements)

```markdown
## bullying-school-duties: What Schools Must Do About Bullying

- kind: rule            (rule | term | how_it_works | research | local | programs)
- question_type: rules  (local_practice | comparison | rules | help | meaning | governance_money | research | after_high_school)
- description: What NH law requires of a school after a bullying report, including deadlines.

1. The parents of the student who was bullied, and of the student accused, must be told within 48 hours of the report.
   - citation: RSA 193-F:4, II(i)
   - source: https://gc.nh.gov/rsa/html/XV/193-F/193-F-4.htm
   - as_of: 2026-11-08
   - review_by: 2027-08-15
   - place: district Rochester        (only when the fact is about one district or town)
   - note: for reviewers only; never shown
```

- **Topic slugs** are lower-case words joined by hyphens, and unique across all files.
- **Statements** stand alone: each names its subject ("New Hampshire law…", "In Rochester…"), so it reads right when quoted by itself.
- **`review_by`:** facts from state law use the August 15 after the next legislative session (2027-08-15). Everything else is reviewed one year after `as_of`.

### Numbers (one table per measure)

```markdown
## naep_g4_math_score: NAEP Average Score, Grade 4 Math

- unit: score               (percent | dollars | count | number | score)
- period: 2024 (tested January–March 2024); year: 2024
- source: NAEP Data Service, NAEP 2024 — https://www.nationsreportcard.gov/Dataservice/...
- as_of: 2026-11-08
- raw: raw/national/naep-2024-math-g4.json
- note: Public schools. "US" is the national public average.

| Place | Value | Rank | Note |
|---|---|---|---|
| US | 237 | | |
| AL | … | | |
| NH | 242 | | |
```

- **Places:**
  - State codes are two letters, with `US` for the nation.
  - Towns use the name exactly as in the site's `town` table (with the id in a column).
  - Districts use the `district` table's name and id.
- **Year convention:** `year` is the year the school or fiscal year ends (2025 = 2024-25 or FY2025). `period` keeps the source's own label ("Fall 2022", "Class of 2022", "Tax year 2025").
- **Rank:** only the source's own published rank, never one we computed.

### Long lists

Long lists (hundreds of rows, such as EFA providers or Head Start sites) go in a CSV in `raw/<area>/`. The Markdown file describes each one: source, date, columns, row count and caveats, plus a short summary.

## Status (November 8, 2026)

All eight files are complete. Each starts with its own summary and ends with a *Not retrieved* list.

| File | Contents |
|---|---|
| `facts-rules-and-rights.md` | 42 topics, 320 facts; 17 unresolved items listed |
| `facts-terms-and-how-schools-work.md` | 65 topics, 379 facts |
| `programs-and-help.md` | 31 topics, 106 facts, plus 16 CSVs in `raw/programs/` (Head Start 45 sites; EFA providers 3,606, 1,788 in NH; EFA stats for 229 towns; 33 career centers with 292 programs; 53 after-school sites; family-support directories with the towns each serves) |
| `town-figures.md` | Department of Revenue tax rates by town, 2014–2025 (2,879 rows); school taxes by town from NH DOE's valuation report, 2010–2025 (3,792 rows); adequacy aid by town and component, FY2020–FY2027 (46,335 rows); all in `raw/town/` |
| `state-issues.md` (added November 11, 2026) | 50 topics, 450 facts in eight sections; each section's sources and the gaps not retrieved are listed in the file. Raw copies in `raw/state-issues/` (553 files, 377 MB) |
| `district-practices.md` | All 183 districts, 607 facts. Coverage: kindergarten cutoff 117, registration 97, full or half day 36; preschool 121; budget form and vote dates 148; high school options 86 of 105 districts without one. The table is in `raw/districts/coverage.csv` |
| `national-comparisons.md` | 38 state-by-state tables and 2 fact topics |
| `outcomes-after-high-school.md` | 23 tables and 13 fact topics |
| `research-briefs.md` | 10 briefs, 95 findings from 84 studies and federal guides |

In all, about 2,030 cited facts and 64 number tables, backed by about 4,150 raw files (1.3 GB) in `raw/`.

**One format difference:** facts in `programs-and-help.md` have a `source` link but no `citation` line, because they come from organization web pages with no section numbers. A loader should use the source as the citation.

## Spot checks

Random facts were re-checked against their sources after each file was finished:

| File | Checked | Result |
|---|---|---|
| Terms and how schools work | 5 statute facts (RSA 194:23, 194-C:2, 40:13, 76:5, 198:4-d) | All match the current text |
| Rules and rights | 4 statute facts (RSA 186:11 IX-e, 194-F:3, 189:1-a, 193-A:1) | 3 matched. RSA 186:11, IX-e said information may be withheld "only" where disclosure could lead to abuse or neglect, and left out "abandonment" and "sexuality"; corrected to match the statute |
| National comparisons | NAEP grade 4 math (NH, MA, US, 2019–2024) and Census spending per pupil | Match the raw downloads and the verified test sources |
| Town figures | Lyme, Amherst and Hampton, 2025 | Match the Lyme tax-rate sheet verified for the tests. Revenue and NH DOE figures agree for Amherst |
| Outcomes after high school | ACS college enrollment of 18–24-year-olds, 2019 | Matches the raw Census file |
| Programs and help | Parent Information Center contact; CSV row counts | Match |
| District practices | Raymond, Windham, Lebanon and Merrimack | All four match the district pages or the saved copies |

## Corrections to earlier documents

These came out of the research and affect the Desktop test answers and the strategy document:

1. **NAEP "significantly higher":** the test sources said Massachusetts's 2024 average was significantly higher than New Hampshire's in grade 4 math, grade 8 math and grade 8 reading. That used a two-state comparison. Against all states, which is how NAEP's own New Hampshire reports compare, Massachusetts is not significantly higher in grade 8 math or reading. `national-comparisons.md` uses the all-states comparison.
2. **School spending study:** test #3's sources quote the 2021 working-paper version of the Jackson and Mackevicius meta-analysis. The published 2024 version reports 0.0316 standard deviations on test scores and 2.8 percentage points on college-going (`research-briefs.md`).
3. **Town school taxes:** the strategy and schema notes said NH DOE's valuation report is hard to turn into one figure per town. `town-figures.md` shows how. Keep each single-town district row and each cooperative member row that shows rates, and drop the total rows and the "XXXX" reference rows. The kept rows then add up exactly to the report's totals in all 16 years and agree with the Department of Revenue's rates.
