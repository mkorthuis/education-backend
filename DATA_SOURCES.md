# Data Sources

Every dataset the backend loads, where it comes from, and how current it is.
All data is published by the New Hampshire Department of Education (NHED). Files are saved under
`backend/app/alembic/assets/` and loaded with `python -m app.etl load <dataset>` (see README,
"Loading a New Year of Data"). Each dataset's config is in `backend/app/alembic/config/`.

**Year convention:** a file labelled `YYYY` covers the school year (or state fiscal year) that
ends in `YYYY` — e.g. `2025` = 2024-2025 / FY2025.

Last checked against the NHED sites: **2026-11-01**.

## Where the files come from

| Source | URL | Access notes |
|---|---|---|
| iPlatform public reports | https://my.doe.nh.gov/iPlatform | Choose a year, Run Report, then Export → Excel. |
| Bureau of Education Statistics pages | https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics | Static `.csv`/`.xlsx` links under `/sites/g/files/ehbemt326/files/inline-documents/`. |
| DOE-25 reports (iPlatform) | https://my.doe.nh.gov/iPlatform/DOE25/DOE25Reports | One workbook per district per year, named `dNNNNNN.xlsx` (district id twice). Rename to `{district}-doe-25-YYYY.xlsx`. Cell B2 holds the district id. |
| myNHDOE public reports (lists) | https://my.doe.nh.gov/myNHDOE/Help/PublicReports.aspx?ReportName=… | `SchoolListCSV`, `SAUListCSV` download directly; `DistrictTown` renders an HTML table (save as CSV). The old `/Profiles/PublicReports/` URLs now error. |
| iExplore (Tableau) | https://jwt.nh.gov/?src_route=/iExplore/Explore-Dashboard | Moved from `dashboard.nh.gov`, which no longer resolves. Use Download → set every filter to (All) and Year → Download → "*Download Explore" → Excel. |

All of these sit behind Akamai bot protection: `curl`, `requests`, WebFetch and headless Chrome get
HTTP 403. A real (headed) Chrome session works. The 2026-11-01 refresh used Playwright driving
installed Chrome with `headless=False`.

## Datasets

| # | Dataset (ETL name) | NHED report / page | Asset path | Years loaded | Status (2026-11-01) |
|---|---|---|---|---|---|
| 1 | School, district & SAU lists (`location`) | myNHDOE `SchoolListCSV`, `SAUListCSV`, `DistrictTown` | `YYYY-school-list.xls`, `YYYY-sau-list.xls`, `YYYY-district-list.csv` | 2025, 2026 snapshots | ✅ 2026 loaded |
| 2 | Public school enrollment by grade (`enrollment`) | iPlatform › Enrollments by Grade › Public School Enrollments by Grade | `enrollments/YYYY-School Enrollments by Grade Public.xlsx` | 2016–2025 | ⚠️ 2026 report broken on NHED's side (HTTP 500) — see `DATA_NOT_LOADED.md` |
| 3 | Town enrollment by grade (`town-enrollment`) | iPlatform › Enrollments by Grade › Town Enrollment By Grade | `town-enrollments/YYYY-Town Level Enrollment By Grade.xlsx` | 2012–2026 | ✅ 2026 loaded (K–12; the new PS/PG columns are not loaded) |
| 4 | Average class size by district (`class-size`) | iPlatform › Average Class Size › By District | `average-class-size/district/YYYY-District-Average-Class-Size.xlsx` | 2012–2026 | ✅ 2026 loaded |
| 5 | Average class size by school (`class-size`) | iPlatform › Average Class Size › By School | `average-class-size/school/YYYY-School-Average-Class-Size.xlsx` | 2012–2026 | ✅ 2026 loaded |
| 5a | State average class size, all grades (`state-class-size`) | iExplore › COMPARE › Download › "Download Data on Compare", Indicator Name = Average Class Size, Entity A = State of New Hampshire | `average-class-size/state/YYYY-iExplore-Compare-Average-Class-Size.csv` (the Year ID and the 2 years before it; UTF-16, tab-separated) | 2016–2025 | ✅ Loaded 2026-11-06 into `state_class_size.all_grades`; 2026 not published yet |
| 6 | School metrics (`measurement`) | iExplore dashboard download | `YYYY-school-metrics.xlsx` (3 years per workbook) | 2016–2025 | ✅ 2025 loaded (exported by hand from iExplore) |
| 7 | State targets (`measurement-state-target`) | NH ESSA consolidated state plan, Table 1 (ELA/Math proficiency interim targets), shifted two years by the 2022 COVID-19 addendum | `state_targets.csv` (sources in `state-targets-source/`) | 2019–2027 | ✅ 2025–2027 added; 2027 is the final (long-term goal) year |
| 8 | Assessment results (`assessment`) | Assessment Data › Disaggregated Data File (Regular Denominator) | `assessments/assessments-YYYY.csv` | 2009–2026 (no 2020) | ✅ 2026 loaded |
| 9 | DOE-25 annual financial reports (`finance`) | iPlatform › DOE-25 Reports | `finance/YYYY/{district}-doe-25-YYYY.xlsx` | 2010–2025 | ✅ FY2025 loaded (176 districts); Newfound Area FY2024 added |
| 10 | Cost per pupil by district (`cost-per-pupil`) | Financial Reports › Cost Per Pupil By District | `cost-per-pupil/cost-per-pupil-YYYY.csv` | 2010–2025 | ✅ FY2025 loaded; FY2024 replaced with the 2025-12-23 revision |
| 11 | State average cost per pupil & total expenditures (`state-expenditure`; its enrollment rows are in `state_enrollment_level`) | Financial Reports › State Average Cost Per Pupil and Total Expenditures | `state-expenditure/state-expenditures-YYYY.csv` | 2010–2025 | ✅ FY2025 loaded; FY2024 replaced with the 2025-12-23 revision |
| 12 | Valuations, property tax assessments & school tax rates (`property-tax`) | Financial Reports › Valuations, Property Tax Assessments, and School Tax Rates | `equalized-value/equalized-value-YYYY.xls(x)`, read through `property-tax/school-tax-by-town.csv` | Tax years 2011–2025 (see *Property tax* below; the 2010 file has no district numbers, so it isn't loaded) | ✅ Loaded 2026-11-15 into `town_school_tax`: 237 towns a year, and the part of each town's local school tax that goes to a cooperative |
| 13 | Education Freedom Accounts (`education-freedom-account`) | Other State Aid Programs › Education Freedom Accounts by municipality | `education-freedom-account/education-freedom-account-YYYY.xlsx` | 2022–2027 | ✅ FY2026 loaded; FY2027 loaded (preliminary August 2026 count) |
| 14 | School safety (`safety`) | School Safety Data Collection | `safety/safety-YYYY.xlsx` | 2016–2025 | ✅ 2025 loaded |
| 15 | FTE staff by district (`staff`) | iPlatform › Staff Reports › Full Time Equivalent Staff Count by District | `staff/staff-count/YYYY-FTE-Staff.xlsx` | 2012–2026 | ✅ 2026 loaded |
| 16 | Teacher attainment (`teacher-education`) | iPlatform › Staff Reports › Teacher Attainment | `staff/teacher-attainment/YYYY-Teacher-Attainment.xlsx` | 2012–2026 | ✅ 2026 loaded |
| 17 | Teacher average salary (`teacher-salary`) | iPlatform › Staff Salary Reports › Teacher Average Salary | `staff/teacher-average-salary/YYYY-Teacher-Salary.xlsx` | 2008–2026 | ✅ 2026 loaded |
| 18 | Teacher salary schedule / bands (`teacher-salary-band`) | iPlatform › Staff Salary Reports › Teacher Salary Schedule | `staff/teacher-starting-salary/YYYY-Teacher-Starting.xlsx` | 2024–2026 | ✅ 2025, 2026 loaded, including the new `MA45` band |
| 19 | Cohort graduation (`graduation-cohort`) | iPlatform › Dropouts and Completers › Cohort Counts By School | `cohort-graduation/YYYY-Cohort Counts By School.xlsx` | 2012–2025 | ✅ 2025 loaded (*Preliminary*) |
| 20 | Post-graduation outcomes (`post-graduation`) | iPlatform › Dropouts and Completers › Completers By Status By School | `completers/YYYY-Completers.xlsx` | 2012–2025 | ✅ 2025 loaded (*Preliminary*) |
| 21 | Early exit & dropout rates (`early-exit`) | iPlatform › Dropouts and Completers › Early Exit and Dropout Rates for Grades 9-12 (2020 or later) | `early-exit-dropout/YYYY-early-exit-dropout-rates-HS.xlsx` | 2012–2024 | ⚠️ 2025 report broken on NHED's side (HTTP 500) — see `DATA_NOT_LOADED.md` |
| 22 | Free & reduced-price lunch eligibility (`reduced-lunch`) | iPlatform › Free and Reduced School Lunch Eligibility › Free Reduced K-12 School Lunch Eligibility Rates by School | `reduced-lunch/YYYY-Free Reduced K-12 School Lunch Eligibility.xlsx` | 2012–2026 | ✅ 2026 loaded (Final, as of October 1, 2025). Tables `school_reduced_lunch`, `district_reduced_lunch` (the district's schools added up), `state_reduced_lunch` (the "Total State Average" row) |
| 23 | English learners (`english-learner`) | iPlatform › Enrollments - Demographic Categories › Limited English Proficiency Enrollment | `english-learner/YYYY-Limited English Proficiency Enrollment.xlsx` | 2014–2026 | ✅ 2026 loaded (Final, as of October 1, 2025). By district only. Tables `district_english_learner`, `state_english_learner`. The 2012 and 2013 reports have no counts (every district is 0), so they aren't loaded |
| 24 | State enrollment by type of school (`enrollment-type`) | iPlatform › State Totals › State Totals Ten Years Public and Private Fall Enrollments | `state-enrollment-type/YYYY-State Totals Ten Years Public and Private Fall Enrollments.xlsx` (each export covers the ten years ending YYYY) | 2008–2027 | ✅ 2027 loaded (October 1, 2026; nonpublic counts for 2026-27 not yet reported). Tables `enrollment_type`, `state_enrollment_type`. Readiness is added to grade 1. Add each new export to the end of the config's `files` list |
| 25 | NAEP results by state (`naep`) | Not NHED: NCES's NAEP Data Service (https://www.nationsreportcard.gov/Dataservice/), saved by `python -m app.etl fetch naep` | `naep/results-<subject>-grade<g>.json`, `naep/compare-{states,nation,years}-<subject>-grade<g>.json` | 2003–2024, reading and math, grades 4 and 8 | ✅ Loaded 2026-11-09 (all states, DC, DoDEA, national public; NH's significance tests; student groups for NH and the nation: sex, economic status, disability, race/ethnicity, school location, English learners) |
| 26 | School system revenue by state (`census-finance`) | Not NHED: U.S. Census Bureau, Annual Survey of School System Finances (https://www2.census.gov/programs-surveys/school-finances/tables/), saved by `python -m app.etl fetch census-finance` | `census-finance/census-finance-YYYY.json` | FY2010–FY2024 | ✅ Loaded 2026-11-09 (every state, DC and the U.S.; 52 revenue items; Census's per-pupil enrollment) |
| 27 | Licensed child care programs (`child-care`) | Not NHED: NH DHHS Child Care Search (https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch), saved by `python -m app.etl fetch child-care`: the page's "Download Provider Results" list, its search results with no filters, and each program's own page | `child-care/child-care-YYYY-MM-DD.json` and `child-care-YYYY-MM-DD-pages.json.gz` (one pair per download; list each date under `downloads` in `child_care_config.yaml`) | Downloads from 2026-11-13 | ✅ Loaded 2026-11-13: 735 programs, capacity 48,501, with each program's page: vacancies, availability, hours, rates, Head Start, licensing visits, features |
| 28 | Census American Community Survey 5-year estimates (`acs`) | Not NHED: U.S. Census Bureau ACS summary files (https://www2.census.gov/programs-surveys/acs/summary_file/), saved by `python -m app.etl fetch acs`: New Hampshire's rows of 64 detailed tables | `acs/acs5-<year>.json.gz` (one per release) | 2015–2019 and 2020–2024 | ✅ Loaded 2026-11-14: 236 towns, 179 school districts and the state; 1,195 values per place with margins of error |
| 29 | Adequacy aid calculation (`adequacy-aid`) | NH DOE Bureau of School Finance, State Adequacy Aid Funding (https://www.education.nh.gov/who-we-are/division-of-education-and-analytic-resources/bureau-school-finance/state-adequacy-aid-funding): each year's municipal summary workbook and split of towns among cooperative districts, saved through a browser | `adequacy-aid/*.xlsx` (two per year, listed in `adequacy_aid_config.yaml`) | FY2020–FY2027 | ✅ Loaded 2026-11-14: 237 towns, every part of the calculation, each district's share; FY2027 is the October 1, 2026 calculation |
| 30 | Property tax rates by town (`property-tax`) | Not NHED: NH Department of Revenue Administration, Municipal and Village District Tax Rates (https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village) and Equalization reports; the files are listed under *Property tax* below | `property-tax/dra/*`, read through `property-tax/dra-tax-rates.csv` | Tax years 2014–2025 | ✅ Loaded 2026-11-15 into `town_property_tax`: 236–237 towns a year. 2026 waits for DRA's final file (36 towns had rates set by October 30, 2026) |
| 31 | NAEP equivalents of state proficiency standards (`naep-state-standard`) | Not NHED: NCES's state mapping study, Data Tables page (https://nces.ed.gov/nationsreportcard/studies/statemapping/data_tables.aspx): each per-year table's "Download Excel" file (https://nces.ed.gov/nationsreportcard/subject/studies/excel/state_mapping/YYYY/table_YYYYa.xlsx for 2017–2022; `.../excel/state mapping/YYYY/...`, with a space, for 2009–2015) and the 2005–2009 study's HTML tables (https://nces.ed.gov/nationsreportcard/studies/statemapping/findings_table1.aspx, 2 and 3), downloaded 2026-11-15 | `naep-state-mapping/table_YYYY{a,b}.xlsx`, `naep-state-mapping/findings_table{1,2,3}.html` | 2005, 2007 and 2009 (2005–2009 study, NCES 2011-458); 2009–2022 (per-year tables) | ✅ Loaded 2026-11-15 into `naep_state_standard`: every state and DC, reading and math, grades 4 and 8, as published (2009 twice: per-year and 2005–2009 study). NH has no estimate in 2005, 2017 or 2019; its 2015 grade 8 rows repeat the SBAC-wide estimate. Not loaded: the consortium rows (SBAC, PARCC, ACT), Puerto Rico, and the 2024 preliminary findings (levels only; the full 2024 report is due) |

## Property tax

Tax years count by the **starting** year, unlike the files above: rates are set in the fall, so tax year 2025 pays
for 2025-26 (FY2026). The two CSVs in `property-tax/` were built for the Ask's reference library
(`additional-data/town-figures.md` explains every step and fix) and name, on each row, the files it was read from.
Those files are in the repo, and the load stops if one is missing:

- **NH DOE's valuations report**, one per tax year: `equalized-value/equalized-value-YYYY.xls(x)`, from the DOE's
  Financial Reports page (https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports).
- **NH DRA's files**, in `property-tax/dra/`: each year's tax rates, the equalization ratio histories, the full value
  rate comparisons (2018 on) and the tax-rate calculation data (2018 on). DRA's site keeps only recent files, so the
  older ones were downloaded from the Wayback Machine's copy of DRA's address:

| File | DRA's address | Downloaded from |
|---|---|---|
| `15-final-tax-rates.pdf` | http://revenue.nh.gov:80/mun-prop/municipal/documents/15-final-tax-rates.pdf | [Wayback Machine, snapshot 2016-01-22](https://web.archive.org/web/20160122140241id_/http://revenue.nh.gov:80/mun-prop/municipal/documents/15-final-tax-rates.pdf) |
| `15-tax-rate-information.xlsx` | http://www.revenue.nh.gov/mun-prop/municipal/documents/15-tax-rate-information.xlsx | [Wayback Machine, snapshot 2016-06-30](https://web.archive.org/web/20160630145930id_/http://www.revenue.nh.gov/mun-prop/municipal/documents/15-tax-rate-information.xlsx) |
| `16-final-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/16-final-tax-rates.xlsx | [Wayback Machine, snapshot 2020-10-18](https://web.archive.org/web/20201018072850id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/16-final-tax-rates.xlsx) |
| `17-final-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/17-final-tax-rates.xlsx | [Wayback Machine, snapshot 2020-10-18](https://web.archive.org/web/20201018202802id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/17-final-tax-rates.xlsx) |
| `18-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/18-tax-rate-calculation-data.xlsx | [Wayback Machine, snapshot 2020-10-18](https://web.archive.org/web/20201018182348id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/18-tax-rate-calculation-data.xlsx) |
| `18-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/18-tax-rates.xlsx | [Wayback Machine, snapshot 2020-10-18](https://web.archive.org/web/20201018202803id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/18-tax-rates.xlsx) |
| `19-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/19-tax-rate-calculation-data.xlsx | [Wayback Machine, snapshot 2020-10-18](https://web.archive.org/web/20201018202746id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/19-tax-rate-calculation-data.xlsx) |
| `19-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/19-tax-rates.xlsx | [Wayback Machine, snapshot 2020-10-18](https://web.archive.org/web/20201018072844id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/19-tax-rates.xlsx) |
| `20-comp-of-full-value-tax-rates-ranking-order.pdf` | https://www.revenue.nh.gov/mun-prop/property/equalization-2020/documents/20-comp-of-full-value-tax-rates-ranking-order.pdf | [Wayback Machine, snapshot 2024-06-22](https://web.archive.org/web/20240622201842id_/https://www.revenue.nh.gov/mun-prop/property/equalization-2020/documents/20-comp-of-full-value-tax-rates-ranking-order.pdf) |
| `20-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/20-tax-rate-calculation-data.xlsx | [Wayback Machine, snapshot 2023-12-27](https://web.archive.org/web/20231227102609id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/20-tax-rate-calculation-data.xlsx) |
| `20-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/20-tax-rates.xlsx | [Wayback Machine, snapshot 2023-12-27](https://web.archive.org/web/20231227102526id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/20-tax-rates.xlsx) |
| `2014-tax-rates.xlsx` | http://revenue.nh.gov:80/mun-prop/municipal/documents/2014-tax-rates.xlsx | [Wayback Machine, snapshot 2015-11-12](https://web.archive.org/web/20151112080114id_/http://revenue.nh.gov:80/mun-prop/municipal/documents/2014-tax-rates.xlsx) |
| `2018-comparison-of-full-value-tax-rates-ranking-order.pdf` | https://www.revenue.nh.gov/mun-prop/property/equalization-2018/documents/2018-comparison-of-full-value-tax-rates-ranking-order.pdf | [Wayback Machine, snapshot 2024-06-22](https://web.archive.org/web/20240622201950id_/https://www.revenue.nh.gov/mun-prop/property/equalization-2018/documents/2018-comparison-of-full-value-tax-rates-ranking-order.pdf) |
| `2019-comparison-of-full-value-tax-rates-ranking-order.pdf` | https://www.revenue.nh.gov/mun-prop/property/equalization-2019/documents/2019-comparison-of-full-value-tax-rates-ranking-order.pdf | [Wayback Machine, snapshot 2024-06-22](https://web.archive.org/web/20240622201913id_/https://www.revenue.nh.gov/mun-prop/property/equalization-2019/documents/2019-comparison-of-full-value-tax-rates-ranking-order.pdf) |
| `2021-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/2021-tax-rate-calculation-data.xlsx | [Wayback Machine, snapshot 2023-12-27](https://web.archive.org/web/20231227102624id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/2021-tax-rate-calculation-data.xlsx) |
| `2022-comparison-of-full-value-tax-rates-ranking-order.pdf` | https://www.revenue.nh.gov/mun-prop/property/equalization-2022/documents/2022-comparison-of-full-value-tax-rates-ranking-order.pdf | [Wayback Machine, snapshot 2024-06-22](https://web.archive.org/web/20240622201738id_/https://www.revenue.nh.gov/mun-prop/property/equalization-2022/documents/2022-comparison-of-full-value-tax-rates-ranking-order.pdf) |
| `2022-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/2022-tax-rate-calculation-data.xlsx | [Wayback Machine, snapshot 2023-12-27](https://web.archive.org/web/20231227102533id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/2022-tax-rate-calculation-data.xlsx) |
| `2023-comparison-of-full-value-tax-rates-ranking-order.pdf` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2023-comparison-of-full-value-tax-rates-ranking-order.pdf | [Wayback Machine, snapshot 2025-06-20](https://web.archive.org/web/20250620013142id_/https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2023-comparison-of-full-value-tax-rates-ranking-order.pdf) |
| `2023-municipal-and-village-tax-rates-final.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/2023-municipal-and-village-tax-rates-final.xlsx | [Wayback Machine, snapshot 2024-03-15](https://web.archive.org/web/20240315003217id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/2023-municipal-and-village-tax-rates-final.xlsx) |
| `2023-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/2023-tax-rate-calculation-data.xlsx | [Wayback Machine, snapshot 2024-05-26](https://web.archive.org/web/20240526104929id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/2023-tax-rate-calculation-data.xlsx) |
| `2024-comparison-of-full-value-tax-rates-ranking-order.pdf` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2024-comparison-of-full-value-tax-rates-ranking-order.pdf | [Wayback Machine, snapshot 2025-06-20](https://web.archive.org/web/20250620013035id_/https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2024-comparison-of-full-value-tax-rates-ranking-order.pdf) |
| `2024-municipal-and-village-tax-rates.xlsx` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2024-municipal-and-village-tax-rates.xlsx | [Wayback Machine, snapshot 2025-03-07](https://web.archive.org/web/20250307042552id_/https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2024-municipal-and-village-tax-rates.xlsx) |
| `2024-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2024-tax-rate-calculation-data.xlsx | [Wayback Machine, snapshot 2025-03-06](https://web.archive.org/web/20250306034909id_/https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2024-tax-rate-calculation-data.xlsx) |
| `2025-comparison-of-full-value-tax-rate.pdf` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2025-comparison-of-full-value-tax-rate.pdf | DRA's site, 2026-11-08 |
| `2025-municipal-and-village-district-tax-rates.xlsx` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2025-municipal-and-village-district-tax-rates.xlsx | DRA's site, 2026-11-08 |
| `2025-tax-rate-calculation-data.xlsx` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2025-tax-rate-calculation-data.xlsx | DRA's site, 2026-11-08 |
| `21-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/21-tax-rates.xlsx | [Wayback Machine, snapshot 2022-03-27](https://web.archive.org/web/20220327213659id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/21-tax-rates.xlsx) |
| `22-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/municipal/documents/22-tax-rates.xlsx | [Wayback Machine, snapshot 2023-12-27](https://web.archive.org/web/20231227102539id_/https://www.revenue.nh.gov/mun-prop/municipal/documents/22-tax-rates.xlsx) |
| `comp-of-full-value-tax-rates.xlsx` | https://www.revenue.nh.gov/mun-prop/property/equalization-2021/documents/comp-of-full-value-tax-rates.xlsx | [Wayback Machine, snapshot 2023-03-27](https://web.archive.org/web/20230327112301id_/https://www.revenue.nh.gov/mun-prop/property/equalization-2021/documents/comp-of-full-value-tax-rates.xlsx) |
| `ratio-median-ratio-cod-prd-history-2018-2009.xlsx` | https://www.revenue.nh.gov/mun-prop/property/equalization-2018/documents/ratio-median-ratio-cod-prd-history-2018-2009.xlsx | [Wayback Machine, snapshot 2024-06-22](https://web.archive.org/web/20240622201937id_/https://www.revenue.nh.gov/mun-prop/property/equalization-2018/documents/ratio-median-ratio-cod-prd-history-2018-2009.xlsx) |
| `ratio-median-ratio-cod-prd-history-2024-2015.xlsx` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/ratio-median-ratio-cod-prd-history-2024-2015.xlsx | [Wayback Machine, snapshot 2025-06-20](https://web.archive.org/web/20250620013016id_/https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/ratio-median-ratio-cod-prd-history-2024-2015.xlsx) |
| `ratio-median-ratio-cod-prd-ten-year-history.xlsx` | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/ratio-median-ratio-cod-prd-ten-year-history.xlsx | DRA's site, 2026-11-08 |

## Notes

- **Statewide student groups.** The free and reduced-price lunch and English learner reports carry the state's own
  totals, which the statewide pages use. Students with disabilities have no statewide row in any loaded report; the
  `/measurement/state` endpoint weights the districts' "Students with Disability (%)" by their enrollment instead.
- **Exporting iPlatform reports by year.** Export → Excel requests
  `https://my.doe.nh.gov/iPlatform/Report/ExportReport/?reportPath=<report path>&format=ExcelOpenXml&ReportID=<id>&SchoolYear=<YYYY>`.
  Fetched from inside a browser session that has opened iPlatform, it returns the workbook for any year
  (reduced lunch is ReportID 26, English learners 27). On 2026-11-05 this worked from headless Chrome.

- **Preliminary data is used.** Every iPlatform export is marked "Type of Data: Final" or "Preliminary".
  Preliminary data is loaded when it is the newest available: the 2025 cohort and completers reports, and
  the FY2027 EFA count. Re-export and reload once NHED finalizes them.
- **Current districts and schools only.** The location lists are snapshots: closed schools stay in the
  database with their history, but `is_current` marks the ones in the latest list (`year_end` of
  `generate_schools_config.yaml`). The API's district and school lists return only current ones unless
  `include_former=true`; lookups by id still work for former ones.
- **Revised history.** On 2025-12-23 NHED reissued FY2024 cost per pupil and state expenditures. The
  revision adds Newfound Area, which the January 2025 file excluded, and adjusts the state averages.
  Newfound's FY2024 DOE-25 form, missing until now, was added too.
- **District changes in the 2026 list.**
  - New district Pasquaney (584) takes Bridgewater, Groton and Hebron from Newfound Area.
  - Lisbon moved to new SAU 110 and Unity to new SAU 109.
  - Gonic is no longer listed under Rochester.
  - A new "In-State Facility" district (838) appears.
  - Most grade spans changed from K-x to P-x.
  - The new school and SAU lists use upper-case addresses.
- **DOE-25 district numbers.** When cell B2 is blank or names a different district (16 forms carry a
  typo, e.g. Thornton's 531 as 53), the district in the file name is used, and the case is logged.
- **DOE-25 coverage.** FY2025 has forms for charter schools and Hill as well. Earlier years have none,
  so they are not loaded (see `DATA_NOT_LOADED.md`).
- **Renamed educator indicators (2025 school metrics).** iExplore replaced "Classes by Certified Educators in
  the Subject (%)" and "Classes by Experienced Educators (%)" with "Educators certified in the subject (%)" and
  "Experienced Educators (%)". The new workbook recomputes 2023–2024 under the new names and the values differ
  from the old ones, so they are loaded as new indicators rather than merged into the old series.
- **Teacher average salary, 2008–2022: district names.** These files name districts instead of numbering
  them.
  - A name must equal a district's name after cleanup (lowercase, without "school district", "schools"
    or "sd"), or be one of the other spellings in `legacy_district_aliases`
    (`district_teacher_salary_config.yaml`).
  - Names in `legacy_skipped_names` are skipped: only Franklin Career Academy, which no file gives an id for.
  - Any other name stops the load with an error naming it. After a new district list renames a district,
    add its old name to `legacy_district_aliases`, or the build fails.
- **Former districts and schools.** Districts and schools that closed before the 2025 list are added from
  `former_schools_config.yaml`: 12 districts and 56 schools, with the name and district they were last listed
  under, taken from the 2009–2018 assessment and 2016–2025 enrollment files. They are marked former.
  - `renumbered_schools` there maps the old ids of three schools the state renumbered in 2019 (Inter-Lakes
    Elementary, Idlehurst, Maple Wood) to their current ids; loaders matching schools by id use
    `core.known_school_ids`, so the old rows load under the current school.
  - Cost per pupil lists Gorham Randolph Shelburne Coop as 201 until 2022; `district_id_aliases` in
    `generate_cost_per_pupil_config.yaml` maps it to 203.
- **Assessment names (2019 on).**
  - Names are compared without outer spaces and with inner runs of spaces collapsed. The 2019, 2021 and 2022
    files spell "Newfound Area " with a trailing space.
  - `district_id_aliases` and `school_id_aliases` in `assessment_data_config.yaml` map the files' names of
    renamed districts and schools, and of Bridgewater-Hebron (listed under Newfound Area until 2024), to ids.
  - Any other name that matches nothing stops the load with an error naming it. After a new list renames a
    district or school, add the files' name to the aliases (or to `skipped_districts`/`skipped_schools`),
    or the build fails.
- **Outcome school names.** The early exit (2020 on) and graduation cohort files name schools.
  `outcome_school_name_aliases.yaml` maps the old names of renamed high schools (Colebrook Academy, Conant
  High School, Granite State Arts Academy, Great Bay eLearning, White Mountains Regional High School) to
  their ids. An alias whose id isn't in the school table stops the build.
- **Safety zeros.** Every safety table, including `school_safety`, stores zero counts, so a missing
  row means no data rather than no incidents.
- **Assessment student counts.** The 2009-2018 and 2024 files show "15-Oct", and 2019 shows 43753, where a
  spreadsheet turned the "10 - 15" range into a date; the loader reads both as 10-15.
- **Safety: schools that didn't report.** A school row with no number in any count cell ("Not Reported",
  "Data Not Yet Submitted", blank) is skipped and logged, rather than stored as zero incidents.
- **Salary band types** are defined in `district_teacher_salary_band_config.yaml` (`salary_band_types`)
  and upserted by the loader. `MA45` (Masters + 45) is type 7, first reported in 2024-25.
- **Town enrollment columns** are found by header (KG, G1–G12), not by position, since 2026 added PS
  and PG columns.
- **Child care.**
  - The portal shows only the present. Each saved download becomes a `child_care_program_snapshot` for trends;
    `child_care_program` keeps each program's latest details, with `is_current` for those in the latest download.
  - Every listed program holds a license (Active, or Permit Issued for a new one) or a license exemption. The
    export's "Provider Enrollment Status" is the program's enrollment as a Child Care Scholarship provider, not
    whether it's open: `accepts_scholarship` is true when it's Active. The export's "Enrolled in the NH Child Care
    Scholarship" agrees except for 4 programs that say Yes but are Inactive (2026-11-13).
  - Short fixed lists are lookup tables with ids set in the config (`quality_ratings`, `regions`, `counties`,
    `license_statuses`, `availabilities`, `feature_categories`, like `program_types`); a value that isn't listed stops
    the load. Licensing visit types (`child_care_review_type`) and list values (`child_care_feature`) are added as
    they appear. They're lookup tables rather than Postgres enums, as elsewhere in the backend: a lookup row can
    carry a display name, and a migration can add a value and load rows using it in the same run.
  - `child_care_feature_category` has each list's `code` for queries (`language`) and its `name`, the heading a
    program's page gives it ("Language Spoken by Staff"), which is how the loader finds the page's lists. A page
    list that's in neither `feature_categories` nor `skipped_page_lists` stops the load.
  - `child_care_region` is DHHS's 7 numbered child care regions, with DHHS's number as the id. They aren't the
    `region` table's 5 school regions. DHHS sets the region and county per program, not quite by town: Hillsborough's
    programs are in Regions 1 and 2, New Ipswich's in 1 and 3 (one has none), and one North Conway school is listed in
    Coos County. So they stay on the program. `county` isn't child-care specific, so towns can use it later.
  - `gsq_step` is the Granite Steps for Quality step as a number: 0 (Licensed) to 4. `quality_rating_id_fk` is the
    older QRIS rating (Licensed, Licensed Plus, Accreditation). The page's endorsement badge (a GSQ_Badge image on 47
    pages) isn't loaded; it doesn't line up with either.
  - `capacity` is the licensed total for all ages. `infant_capacity` and `toddler_capacity` come from the search's
    results; they never add up to more than the total and differ from the page's vacancies, so they look like the
    license's infant and toddler capacity. The page doesn't show them; confirm with DHHS before labelling them so.
  - The `infant`, `toddler`, `preschool` and `school_age` flags come from the age groups a program lists in the
    search, else its license's program types, else its age range by the portal's definitions (school age: a range
    reaching 6); `age_groups_source` says which (`listed`, `license`, `age_range`). 2026-11-13: 621 listed, 81 by
    license, 27 by age range; six license-exempt programs have none of these, so their flags are blank. A program's
    own list and its license disagree for 159 of the 529 that have both (26 licensed only for preschool list all four
    groups), so the license's program types are kept too, as features (below).
  - The license's types (`License_Type_From_Application__c`) mix the kind of license (Group child care center, Family
    Child Care Home, Friend and Neighbor, ...) and the ages it covers (Infant/Toddler, Preschool, School Age and Night
    Care Program). Each is a `child_care_feature` in the `license_type` category, linked to the program in
    `child_care_program_feature_xref`. The age range is in months at both ends (`min_age_months`, `max_age_months`).
  - Towns come from the program's city: `location.TownMatcher` (villages, then "North Conway" -> Conway), plus
    `town_aliases` in the config (Hillsboro, Lochmere, Etna, Spofford). A city that matches no town stops the load.
  - `district_child_care` counts a town's programs toward the district that teaches its kindergarten, so a town in
    an elementary and a cooperative district (Amherst and Souhegan) counts once. Totals add up to `state_child_care`.
  - Residential Child Care Programs (homes for youth) are in the search's results but not the export, and aren't loaded.
  - Each program's page shows a browser a reCAPTCHA once it has opened more than 5 of them. It's only enforced in the
    browser; the fetch reads every page anyway, one every 2 seconds (about 40 minutes), a deliberate choice made
    2026-11-13. Pages are saved trimmed to their content and parsed when loaded, so a parser fix needs no new fetch.
    An interrupted fetch keeps the pages read so far; fetching again the same day reads only the rest.
  - The pages give the snapshot's availability and vacancies (each with the program's own "Last Updated"), Head Start,
    the main contact, hours (`child_care_program_hours`), rates by age group and period (`child_care_program_rate`;
    a page without rates says only to contact the provider), Other Information's lists (`child_care_feature`, linked
    in `child_care_program_feature_xref`), and licensing visits with their compliance counts (`child_care_inspection`).
    A page shows three years of visits; every saved download's are kept. `is_current` marks the programs in the
    latest download; the snapshots' dates say when else a program was listed.
  - A page can have several schedules, each with its own days, hours and rates (a half-day and a full-day session).
    They have no names, so each different one is numbered (`schedule`), and one that repeats another's hours and rates
    is left out.
    Median weekly rates in the first schedule, 2026-11-13: infant $345, toddler $320, preschool $295, school age $183
    (322 of 735 programs list rates; the rest say to ask).
  - Vacancies are the program's own report, as of its `vacancies_updated` date, which can be a year or more old. The
    views add them up regardless; 2026-11-13: 700 infant, 1,259 toddler, 2,749 preschool and 3,266 school-age openings.
  - A program can hide its email on its page ("The provider has chosen not to display the email address");
    `email_hidden` records it. The bulk lists include the email anyway, so it's stored and the API
    (`/api/v1/child-care/program` and `/program/{id}`) returns it; a request with `hide_hidden_email=true` gets those
    programs' emails blank.
  - API: `/api/v1/child-care/state`, `/town` and `/district` give the views' totals for each download (`as_of`);
    `/program` lists programs with their latest snapshot (filters: town, district, type, age group, availability,
    vacancies, scholarship, current), and `/program/{id}` adds hours, rates, features, visits and every snapshot.
- **American Community Survey (ACS).**
  - 5-year estimates: a release is named by its last year and covers five (2024: 2020–2024). Census advises
    against comparing overlapping periods, so history skips ahead five years: 2015–2019, then 2020–2024. Dollars
    are in each release's last year's dollars; an inflation index (BLS's CPI-U-RS) isn't loaded yet.
  - Fetched from the table-based summary files (no API key): one file per table for the whole country, of which New
    Hampshire's state, county subdivision (060) and school district (950, 960, 970) rows are kept. 2015–2019 is in
    Census's "prototype" folder, in the same format, made before Census switched to it for 2021. 2010–2014 is only in
    the older sequence-based files.
  - 64 tables, 1,195 values, chosen by topic and marked core (likely to be used soon) or extended (kept for later) in
    `acs_config.yaml`; `acs_variables.csv` gives each value's column name in the views, unit and description. Race-
    by-race repeats of tables, data-quality tables and detailed occupation and commuting tables are left out. Citizens
    of voting age (B29001) isn't published for towns or school districts.
  - Every estimate has a margin of error at 90% confidence. Where Census gives a code instead of a number, the value
    is blank and `acs_annotation` says why; a controlled estimate's margin of error is 0.
  - Towns: 236 of Census's 260 county subdivisions; the other 24 (unincorporated grants, purchases, townships and
    locations, Livermore, and an undefined area) have no town row and are listed in `skip_towns`. Hale's Location and
    Millsfield match by alias; Wentworth location (Coos County) isn't the town Wentworth ("Wentworth town", Grafton
    County). Census gives no per capita income for Millsfield. School districts: all 179 of Census's (88 elementary, 9 secondary, 82 unified), 168 by name and
    11 by `district_aliases`. Census's districts overlap (Amherst's residents count in Amherst and in Souhegan), so
    don't add them up; elementary plus unified cover the state once. The state's figures are Census's own.
  - 2015–2019 has 1,155 of the 1,195 values. Household language (B16002) wasn't in its 5-year release, and two public
    transportation lines were reorganized. Three income medians are the same in 2019 dollars, and eight "year built"
    and "year moved in" brackets are the same lines with their years moved; `acs_variable_release` records each.
  - Read the materialized views: per level (town, district, state), one per topic with each value and its margin of
    error (`town_acs_housing`, …) and `{level}_acs_summary`: 40 measures (rates, shares, medians) with margins of error
    by Census's formulas and a reliability rating by coefficient of variation: high to 15%, caution to 30%, low above
    (`acs_reliability`). A load refreshes them.
- **Adequacy aid.**
  - NH DOE calculates aid for each town by where students live (RSA 198:40-a to 198:42): resident students and the
    extra rates for free or reduced-price meal, special education and English learner students make the cost of an
    adequate education; the statewide education property tax (SWEPT) the town keeps is subtracted; extraordinary need
    aid and (from FY2027) fiscal capacity disparity aid are added; hold-harmless grants limit drops. The grant is never
    below $0, and a town keeps all its SWEPT, even beyond its cost (38 towns in FY2027).
  - Values are stored as the DOE publishes them, one row per part (`town_adequacy_aid`), with each year's rates and
    thresholds (`adequacy_aid_parameter`) and steps (`adequacy_aid_step`), from the DOE's explanation of the year.
    Each step's formula is checked against every town's published figure on load: rates times students to the cent;
    extraordinary need and disparity aid within cents (the DOE rounds at steps the law doesn't spell out). Steps the
    DOE doesn't fully publish (FY2021's one-time F&R aid, relief aid before proration, FY2023's SWEPT hold-harmless,
    SWEPT itself) are explained but not checked.
  - The formula changed every year or two: third-grade reading aid and stabilization grants through FY2023; FY2021's
    one-time F&R and disparity aid; COVID-era student counts (FY2022: the greater of two years; FY2023: free and
    reduced counts rebuilt from the 2019-20 share) and relief aid prorated to $17.5 million (FY2022-FY2023); SWEPT
    cut to $263 million for FY2023 with a hold-harmless grant; extraordinary need grants from FY2023 ($650 per
    student in FY2023 by the workbook, though the DOE's explanation says $600; $11,730 by FY2027).
  - The DOE's files have errors the config corrects visibly: FY2020-FY2021's split gives Dresden (Hanover) town number
    0 (`town_fixes`). 23 unincorporated places (8 numbered, 15 lettered below the towns) have no town row or district;
    they count toward the state-total check but aren't stored. In FY2023 they got $34,284 of SWEPT hold-harmless
    grants.
  - Districts: 28 towns are split among two or more districts in the DOE's split file (56 shares, which add up to each
    town's grant and SWEPT); every other town's grant goes to its one current district (`town_district_xref`, with
    Concord set in `town_districts`). The links are current, so a district whose towns changed could be assigned
    wrongly in earlier years; `district_adequacy_aid.reported_difference` would show it.
  - The grant matches what districts report as "Adequacy Aid Grant" in their financial reports (DOE-25): 921 of 934
    district-years, FY2020-FY2025, to the dollar. Hanover reports Dresden's share of Hanover's grant as its own (the
    difference in FY2021 and FY2022 is exactly that share); Newfound Area and Dover differ in a few years.
  - Older years (FY2004-FY2019) are in the Wayback Machine in a different layout; they'd need their own column maps.
  - API (`/api/v1/finance/adequacy-aid`): `/years`, and `/formula?year=` for a year's parameters and steps;
    `/district` and `/town` for totals and each town's calculation as columns; `/district/{id}/calculation` (for the
    district financials page) and `/town/{id}/calculation` for each town's steps with the DOE's figure and, for a
    formula, its inputs (so the page can show "students x rate = aid"); `/state` for the DOE's totals. Every year by
    default, each with its status (FY2027 is an estimate).
  - API (`/api/v1/acs`): `/release`, `/topic`, `/variable` and `/measure` describe what's loaded; `/town/summary`,
    `/district/summary` and `/state/summary` give the 40 measures as `{value, moe, reliability}`, and with
    `compare_to=2019` each also gets the earlier value, the change and whether it's significant at 90% (the change is
    larger than the square root of the two margins squared; overlapping releases aren't compared; dollars are each
    release's own). `/town/{topic}`, `/district/{topic}` and `/state/{topic}` give a topic's values (`tier=core` by
    default, `tier=all`, or `variables=` by column name), with no filter required: every town's full poverty topic
    is 6.5 MB.
- The frontend's list of sources (`education-frontend/src/pages/DataSources.tsx`) still links the old
  `dashboard.nh.gov` and `/Profiles/PublicReports/` URLs.
