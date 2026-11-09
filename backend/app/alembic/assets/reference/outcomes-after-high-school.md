# Outcomes After High School (Strategy Type 8)

What New Hampshire graduates do after high school: college enrollment, college completion, career and technical education (CTE) results, registered apprenticeships, students with disabilities after school, young adults' schooling and work, and migration. New Hampshire statewide unless a table says otherwise. Gathered 2026-11-08.

## Summary

**Measures and years (23 number tables, 13 fact topics)**

- **College enrollment of NH high school completers (NH DOE, National Student Clearinghouse data):** statewide rate for 2017–2019 (old iReport), plus 2019 by student group, institution type and location; 2019 and 2020 from NH DOE's 2021–2023 postsecondary report. The definition of the iExplore rate already in the site's database was confirmed in NH DOE's iGlossary.
- **College completion:** six-year completion rates for students who *started at* NH colleges (NSC Completing College report, December 2020), by sector. Also NSC follow-up of 34,617 CCSNH early college (dual enrollment) students from 2016–2022: 83.0% later enrolled in college, and 64.7% of the 2016–2019 groups earned a credential.
- **Young adults (Census ACS 1-year):** share of 18–24-year-olds living in NH who are enrolled in college, 2015–2025 (no 2020); education level of 18–24 and 25–34-year-olds; employment rates for ages 16–19 and 20–24 (2015, 2019, 2024, 2025).
- **CTE (Perkins V, NH DOE):** CTE concentrators' graduation rate, placement after high school, work-based learning and other indicators. Actual results for 2023–24 and 2024–25; earlier "FY22/FY23" values; targets.
- **Registered apprenticeships (U.S. DOL data, via NH Employment Security):** active, new and completed apprentices and programs, FY2020–FY2025; age of new apprentices, top occupations and wages.
- **Students with IEPs after school (IDEA):** how students with disabilities left school, 2018–19 to 2023–24 (federal Section 618 counts); Indicator 14 post-school outcomes, FFY2018–FFY2024; Indicator 13 transition-plan compliance, FFY2018–FFY2024.
- **Jobs ahead:** NH Employment Security 2024–2034 projected yearly job openings, grouped by the education an occupation usually needs (derived).
- **Migration:** Carsey School (UNH) estimate of net migration of 18–29-year-olds into NH, 2015–2019.

**Main gaps (see *Not retrieved*)**

- No NH DOE report on college **persistence or completion of NH high school graduates** could be found. NSC completion figures here are for colleges located in NH, not for NH graduates wherever they enroll.
- The iExplore statewide rate after 2020 could not be read reliably (Tableau dashboard). The site's database has school and district values only.
- **CTE credentials:** NH's Perkins high school measures do not include a credential count. NH chose work-based learning instead of credentials, and NH DOE publishes no industry-credential counts. CTE results by career center are not published.
- **Apprenticeships:** no count of NH high school graduates or youth apprentices. The FY2024 column of the 2026 NHES fact sheet repeats FY2022 values (see note).
- **Indicator 14** rests on a survey with a 4.9–6.1% response rate, which NH DOE says is not representative. It is statewide only.
- **PSEO** (earnings by college program) does not include any NH college.
- No NHES report focused on young workers was found; ACS tables are used instead.

**Format note:** for measures with several years, tables add a *Year* column (the `year` convention in the README: the year a school or fiscal year ends). The *Rank* column is omitted where no source rank exists.

---

## Numbers

### College enrollment after high school

## nh_postsec_enrollment_rate_ireport: NH DOE Post-Secondary Enrollment Rate (Statewide), 2017–2019

- unit: percent
- period: Report years 2016-17 to 2018-19; year: 2017–2019
- source: NH DOE iReport (old school report card), State of New Hampshire, College & Career Readiness tab — https://ireport.education.nh.gov/state/NH/grad-ccr
- as_of: Wayback snapshot 2022-05-29 (http://web.archive.org/web/20220529042238/https://ireport.education.nh.gov/state/NH/grad-ccr)
- raw: raw/outcomes/nhdoe-ireport-state-grad-ccr-wayback-20220529.html
- note: The page calls it "Post-Secondary Enrollment Rate" and says it "shows how many of our students that completed high school move on to enroll in either a 2-year or a 4-year higher Education Institution", using "National Student Clearinghouse services as well as data obtained from the university System of NH". The page's "Over Time" table labels the years 2017, 2018 and 2019.

| Place | Year | Value | Note |
|---|---|---|---|
| NH | 2017 | 59.82 | |
| NH | 2018 | 57.83 | |
| NH | 2019 | 57.72 | |

## nh_postsec_enrollment_rate_2019_by_group: NH DOE Post-Secondary Enrollment Rate by Student Group, 2019

- unit: percent
- period: Report year 2018-2019; year: 2019
- source: NH DOE iReport, State of New Hampshire, College & Career Readiness — https://ireport.education.nh.gov/state/NH/grad-ccr
- as_of: Wayback snapshot 2022-05-29
- raw: raw/outcomes/nhdoe-ireport-state-grad-ccr-wayback-20220529.html
- note: "N*" for migrant students is shown as on the page (not reported).

| Place | Group | Value |
|---|---|---|
| NH | All students | 57.72 |
| NH | Economically disadvantaged | 37.02 |
| NH | English language learners | 44.03 |
| NH | Students with disabilities | 34.02 |
| NH | Students in foster care | 9.41 |
| NH | Homeless | 31.07 |
| NH | Migrant | N* |
| NH | Military connected | 59.26 |
| NH | American Indian or Alaskan | 36.00 |
| NH | Asian or Pacific Islander | 74.02 |
| NH | Black or African American | 47.43 |
| NH | Hispanic or Latino | 46.07 |
| NH | White | 57.58 |
| NH | Multiple races | 50.96 |

## nh_postsec_enrollees_by_institution_2019: NH College Enrollees by Type and Location of College, 2019

- unit: percent
- period: Report year 2018-2019; year: 2019
- source: NH DOE iReport, State of New Hampshire, College & Career Readiness (Post-Secondary Enrollment Rate details) — https://ireport.education.nh.gov/state/NH/grad-ccr
- as_of: Wayback snapshot 2022-05-29
- raw: raw/outcomes/nhdoe-ireport-state-grad-ccr-wayback-20220529.html
- note: The page lists these under "Institution Type" and "Institution Location" without saying what they are a share of. Each pair adds to about 100% (public + private = 100.13; in-state + out-of-state = 100.08), so they appear to be shares of the students who enrolled, not of all completers. This is our reading, not the page's wording.

| Place | Category | Value |
|---|---|---|
| NH | Public institution | 59.72 |
| NH | Private institution | 40.41 |
| NH | In-state institution | 52.40 |
| NH | Out-of-state institution | 47.68 |

## nh_postsec_enrollment_rate_2019_2020: NH DOE Postsecondary Enrollment (Statewide), 2019 and 2020

- unit: percent
- period: 2019, 2020 (as labeled in the report); year: 2019, 2020
- source: NH DOE, *The Status of Postsecondary Education in New Hampshire, 2021–2023*, page 12 — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2021-12/nhedreport-2021-final-digital.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nhdoe-status-of-postsecondary-education-2021-2023.pdf
- note: The report says the data "show how many students who completed high school move on to enroll in either a two-year or four-year college", obtained "through the National Student Clearinghouse, CCSNH, and USNH data", and that 2020 "slipped, most likely due to the pandemic". The 2019 value (58.5) differs from the iReport value for 2019 (57.72). Neither source explains the difference.

| Place | Year | Value |
|---|---|---|
| NH | 2019 | 58.5 |
| NH | 2020 | 54.7 |

## ccsnh_early_college_later_enrollment: CCSNH Early College Students Who Later Enrolled in College, by Last Early College Year

- unit: count (with percent)
- period: Academic years 2016–2022 (the last year a student took a CCSNH early college course); year: 2016–2022
- source: Mark Rubinstein, "Postsecondary Matriculation and Completion for New Hampshire Early College Students, 2016-2022" (15 July 2024), Appendix B of the CCSNH–USNH first annual alignment report to the Governor and Council (October 28, 2024), Tables I–III — https://media.sos.nh.gov/govcouncil/2024/1113/111%20GC%20Agenda%20111324.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nh-gc-2024-11-13-item111-ccsnh-usnh-alignment-report.pdf
- note: Covers only students who took CCSNH early college (dual enrollment) courses, not all NH graduates. Matched through the National Student Clearinghouse. The PDF is a scan, and figures were read from extracted text. The column sums were checked: they add to 28,715 enrolled out of 34,617. The report says the later groups had less time to enroll.

| Place | Year | Early college students | Later enrolled in college | Percent enrolled |
|---|---|---|---|---|
| NH | 2016 | 4,342 | 3,735 | 86.0 |
| NH | 2017 | 4,284 | 3,710 | 86.6 |
| NH | 2018 | 4,242 | 3,635 | 85.7 |
| NH | 2019 | 5,736 | 4,809 | 83.8 |
| NH | 2020 | 6,342 | 5,136 | 81.0 |
| NH | 2021 | 4,571 | 3,796 | 83.0 |
| NH | 2022 | 5,100 | 3,894 | 76.4 |
| NH | 2016–2022 | 34,617 | 28,715 | 83.0 |

## ccsnh_early_college_where_enrolled: Where CCSNH Early College Students Enrolled and Whether They Finished

- unit: count (with percent)
- period: Academic years 2016–2022; year: 2016–2022
- source: same report as above, Tables IV, VIII, IX, X, XI, XII — https://media.sos.nh.gov/govcouncil/2024/1113/111%20GC%20Agenda%20111324.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nh-gc-2024-11-13-item111-ccsnh-usnh-alignment-report.pdf
- note: Percentages are the report's own, except where marked derived.

| Place | Measure | Value | Note |
|---|---|---|---|
| NH | Later enrolled in college (of 34,617) | 28,715 | 83.0% |
| NH | Of those, enrolled at a CCSNH college | 6,065 | 21.1% |
| NH | Of those, first enrolled at a four-year college | 24,525 | 85.4% |
| NH | Of four-year enrollees, enrolled at a NH four-year college | 10,929 | report says "~44.5%" |
| NH | Of NH four-year enrollees, chose a USNH institution | 6,624 | 60.6% |
| NH | Of NH four-year enrollees, chose SNHU | 2,621 | report says "~24%" |
| NH | Earned a college credential, 2016–2022 groups (of 28,715 enrolled) | 11,425 | ~39.8%; the report says many had too little time to finish |
| NH | Earned a college credential, 2016–2019 groups (of 15,889 enrolled) | 10,274 | ~64.7%; the report says it "exceeds 73%" for the 2016 and 2017 groups |

### College completion

## nsc_six_year_completion_nh_colleges: Six-Year College Completion Rate at New Hampshire Colleges, by Sector

- unit: percent
- period: Six-year outcomes as reported in NSC Signature Report No. 19 (December 2020); the starting year is not stated in the NH DOE report; year: 2020
- source: NH DOE, *The Status of Postsecondary Education in New Hampshire, 2021–2023*, page 16, citing "Completing College: A State-Level View of Student Attainment Rates (Signature Report No. 19)", National Student Clearinghouse Research Center, December 2020 — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2021-12/nhedreport-2021-final-digital.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nhdoe-status-of-postsecondary-education-2021-2023.pdf
- note: Counts students by the college where they started (in NH), whether or not they are NH graduates. It does not measure how many NH high school graduates finish college. The report says the NH private nonprofit figures include "SNHU online students".

| Place | Group | USNH | CCSNH | NH private nonprofits | US: public 4-year | US: public 2-year | US: private nonprofit 4-year |
|---|---|---|---|---|---|---|---|
| NH | Total completion rate | 79.4 | 42.9 | 56.9 | 67.4 | 40.4 | 76.9 |
| NH | Exclusively full-time | 89.7 | 68.4 | 80.1 | 83.7 | 63.5 | 87.7 |
| NH | Exclusively part-time | 20 | 24.1 | 16.8 | 21.6 | 17.8 | 39.1 |
| NH | Started at age 20 or younger | 82.1 | 44.5 | 77.8 | 70.5 | 43.48 | 79.96 |
| NH | Started over age 24 | 57.2 | 41.6 | 37.6 | 56.3 | 34.9 | 67.9 |
| NH | Women | 82.7 | 46.3 | 56.6 | 71.3 | 43.5 | 80.2 |
| NH | Men | 76.7 | 41.3 | 57.1 | 63.9 | 38.5 | 74.2 |

### Young adults living in New Hampshire (Census)

## acs_18_24_enrolled_college: Share of 18–24-Year-Olds in NH Enrolled in College or Graduate School

- unit: percent (with count)
- period: ACS 1-year estimates, 2015–2025 (no standard 1-year release for 2020); year: 2015–2025
- source: U.S. Census Bureau, American Community Survey 1-year, Table S1401 (School Enrollment), New Hampshire — https://data.census.gov/table/ACSST1Y2025.S1401?g=040XX00US33 (retrieved through https://data.census.gov/api/access/data/table?id=ACSST1Y{year}.S1401&g=040XX00US33)
- as_of: 2026-11-08
- raw: raw/outcomes/census/census-acs1-{year}-S1401-NH.json
- note: Variables S1401_C01_029E (population 18 to 24), S1401_C01_030E (enrolled in college or graduate school) and S1401_C02_030E (percent). Labels were checked for 2015, 2017, 2019 and 2021–2025; 2016 and 2018 use the same variable codes. The counts cover people living in NH, so this is not a measure of NH graduates. "±" is the 90% margin of error.

| Place | Year | Population 18–24 | Enrolled in college or grad school | Percent | ± (percent) |
|---|---|---|---|---|---|
| NH | 2015 | 130,063 | 58,439 | 44.9 | 2.3 |
| NH | 2016 | 127,368 | 57,305 | 45.0 | 2.3 |
| NH | 2017 | 126,595 | 58,411 | 46.1 | 2.4 |
| NH | 2018 | 127,582 | 55,560 | 43.5 | 2.2 |
| NH | 2019 | 123,941 | 54,827 | 44.2 | 2.4 |
| NH | 2021 | 124,420 | 54,597 | 43.9 | 2.2 |
| NH | 2022 | 118,758 | 43,565 | 36.7 | 2.5 |
| NH | 2023 | 120,374 | 51,154 | 42.5 | 2.7 |
| NH | 2024 | 122,828 | 52,784 | 43.0 | 2.5 |
| NH | 2025 | 120,561 | 48,604 | 40.3 | 2.8 |

## acs_18_24_education_level: Highest Education of 18–24-Year-Olds in NH

- unit: percent
- period: ACS 1-year 2015, 2019, 2024, 2025; year: 2015, 2019, 2024, 2025
- source: U.S. Census Bureau, ACS 1-year, Table S1501 (Educational Attainment), New Hampshire — https://data.census.gov/table/ACSST1Y2025.S1501?g=040XX00US33
- as_of: 2026-11-08
- raw: raw/outcomes/census/census-acs1-{year}-S1501-NH.json
- note: Variables S1501_C02_002E to S1501_C02_005E. "Some college or associate's" includes people currently in college. 2025 margins of error: ±1.8, ±2.9, ±2.8, ±2.4.

| Place | Year | Less than high school graduate | High school graduate (incl. equivalency) | Some college or associate's | Bachelor's or higher |
|---|---|---|---|---|---|
| NH | 2015 | 11.1 | 31.8 | 44.9 | 12.2 |
| NH | 2019 | 11.3 | 32.1 | 44.2 | 12.5 |
| NH | 2024 | 8.8 | 40.0 | 37.0 | 14.2 |
| NH | 2025 | 10.7 | 39.8 | 35.0 | 14.6 |

## acs_25_34_bachelors: Share of 25–34-Year-Olds in NH With a Bachelor's Degree or Higher

- unit: percent
- period: ACS 1-year 2015, 2019, 2024, 2025; year: 2015, 2019, 2024, 2025
- source: U.S. Census Bureau, ACS 1-year, Table S1501, New Hampshire — https://data.census.gov/table/ACSST1Y2025.S1501?g=040XX00US33
- as_of: 2026-11-08
- raw: raw/outcomes/census/census-acs1-{year}-S1501-NH.json
- note: Variables S1501_C02_017E and S1501_C02_018E. Counts people living in NH, including people who moved to NH after college.

| Place | Year | High school graduate or higher | Bachelor's or higher | ± (bachelor's) |
|---|---|---|---|---|
| NH | 2015 | 94.8 | 40.7 | 2.5 |
| NH | 2019 | 94.9 | 40.4 | 2.1 |
| NH | 2024 | 95.3 | 43.8 | 2.1 |
| NH | 2025 | 96.3 | 46.9 | 2.7 |

## acs_youth_employment: Work Rates of NH Teens and Young Adults

- unit: percent
- period: ACS 1-year 2015, 2019, 2024, 2025; year: 2015, 2019, 2024, 2025
- source: U.S. Census Bureau, ACS 1-year, Table S2301 (Employment Status), New Hampshire — https://data.census.gov/table/ACSST1Y2025.S2301?g=040XX00US33
- as_of: 2026-11-08
- raw: raw/outcomes/census/census-acs1-{year}-S2301-NH.json
- note: Variables S2301_C02_002E/003E (labor force participation), C03 (employment/population ratio), C04 (unemployment rate). Includes students. 2025 margins of error: ages 16–19 ±4.0, ±3.7, ±2.2; ages 20–24 ±2.7, ±2.7, ±1.4.

| Place | Year | Age | Population | In labor force | Employed (share of population) | Unemployment rate |
|---|---|---|---|---|---|---|
| NH | 2015 | 16–19 | 76,236 | 50.8 | 43.6 | 13.3 |
| NH | 2015 | 20–24 | 88,639 | 81.9 | 75.4 | 7.8 |
| NH | 2019 | 16–19 | 72,902 | 47.8 | 43.4 | 8.7 |
| NH | 2019 | 20–24 | 84,664 | 81.3 | 76.5 | 5.3 |
| NH | 2024 | 16–19 | 72,982 | 54.7 | 50.6 | 7.3 |
| NH | 2024 | 20–24 | 83,273 | 78.7 | 75.2 | 4.4 |
| NH | 2025 | 16–19 | 67,909 | 53.7 | 49.6 | 7.6 |
| NH | 2025 | 20–24 | 84,968 | 78.5 | 74.7 | 4.2 |

### Career and technical education (Perkins V)

## perkins_nh_performance_2024_2025: NH CTE Concentrators' Perkins V Results and Targets, 2023–24 to 2026–27

- unit: percent
- period: Program years 2023–24 and 2024–25 (actual); 2023–24 to 2026–27 (approved or proposed levels); year: 2024, 2025
- source: NH DOE Office of Career and Technical Education, "Perkins State Determined Levels of Performance (SDLPs), Program Year 2026–2027", Appendix A — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/perkins-state-determined-levels-of-performance-2026-2027_0.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nhdoe-perkins-sdlp-2026-2027.pdf
- note: S = high school, P = postsecondary (CCSNH). The document notes for 3S1: "NH RSA 189:68(I) limits reporting of employment outcomes". For 2P1 it notes "a change in data collection methodology beginning in 2023–24, making the prior approved level not directly comparable". **Check before use:** in this table the 5S3 actual values (52.52, 53.28) are identical to the 3S1 actual values, and the 3P1 2023–24 actual (24.86) is identical to the 4S1 value. These may be copying errors in the source.

| Place | Indicator | 2023–24 approved | 2023–24 actual | 2024–25 approved | 2024–25 actual | 2025–26 approved | 2026–27 proposed |
|---|---|---|---|---|---|---|---|
| NH | 1S1 Four-year graduation rate | 98 | 97.83 | 97.85 | 97.03 | 97.61 | 98 |
| NH | 2S1 Academic achievement, ELA (SAT) | 55 | 55.29 | 57.75 | 60.88 | 54.80 | 61 |
| NH | 2S2 Academic achievement, math (SAT) | 35 | 26.56 | 33.5 | 23.72 | 32.5 | 32.5 |
| NH | 2S3 Academic achievement, science (NH SAS) | 35 | 34.11 | 36.25 | 33.29 | 35.04 | 35.5 |
| NH | 3S1 Post-program placement | 58 | 52.52 | 55 | 53.28 | 55 | 55.75 |
| NH | 4S1 Non-traditional program concentration | 26 | 24.86 | 23.75 | 25.29 | 24.5 | 26 |
| NH | 5S3 Work-based learning | 58 | 52.52 | 55 | 53.28 | 65.91 | 68 |
| NH | 1P1 Postsecondary placement | 75 | 77.44 | 77.25 | 80.10 | 78 | 82 |
| NH | 2P1 Earned recognized postsecondary credential | 69 | 27.28 | 26.5 | 27.74 | 27.60 | 28 |
| NH | 3P1 Non-traditional concentration (postsecondary) | 26 | 24.86 | 21 | 21.62 | 21.5 | 23.5 |

## perkins_nh_performance_fy22_fy23: NH Perkins V Values Labeled FY22 and FY23 (with Proposed FY24)

- unit: percent
- period: As labeled "FY22", "FY23" and "Proposed FY24"; year: 2022, 2023
- source: NH DOE, "New Hampshire State Determined Performance Levels, Perkins Program Year FY24" — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/new-hampshire-state-determined-performance-levels-fy24.pdf
- as_of: Wayback snapshot 2025-08-31
- raw: raw/outcomes/nhdoe-perkins-sdpl-fy24-wayback-20250831.pdf
- note: The document doesn't call the FY22 and FY23 columns "actual". It says levels "must be higher than the average actual performance of the two most recently completed program years". Its "Proposed FY24" values match the 2024–25 approved levels above except science (36.5 vs 36.25), so FY23 likely means 2023–24. But the FY23 values differ from the 2023–24 actuals above for every indicator except 3S1. The indicator codes are shown as in the source (ELA labeled 2S2 and math 2S3 here).

| Place | Indicator (as labeled) | FY22 | FY23 | Proposed FY24 |
|---|---|---|---|---|
| NH | 1S1 4-year graduation rate | 97.77 | 97.37 | 97.85 |
| NH | 2S2 academic achievement E/LA | 58.33 | 54.29 | 57.75 |
| NH | 2S3 academic achievement Math | 35.9 | 30.61 | 33.5 |
| NH | 2S3 academic achievement Science | 36.59 | 35.94 | 36.5 |
| NH | 3S1 post program placement | 57.0 | 52.52 | 55.0 |
| NH | 4S1 non-traditional program concentration | 25.67 | 21.38 | 23.75 |
| NH | 5S3 work based learning | 42.06 | 66.54 | 55.0 |
| NH | 1P1 postsecondary placement | 75.92 | 78.55 | 77.25 |
| NH | 2P1 earned recognized postsecondary credential | 27.02 | 25.64 | 26.5 |
| NH | 3P1 non-traditional program concentration | 21.66 | 20.28 | 21.0 |

### Registered apprenticeships

## nh_registered_apprenticeships: Registered Apprenticeships in New Hampshire, FY2020–FY2025

- unit: count
- period: Federal fiscal years (FY2025 = October 1, 2024 – September 30, 2025); year: 2020–2025
- source: NH Employment Security, ELMI Bureau, "Apprenticeships in New Hampshire" fact sheets (November 2024, for FY20–FY24; April–May 2026, for FY25), data from the U.S. Department of Labor, Office of Apprenticeship — https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet.pdf and https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet-2026.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nhes-apprenticeship-factsheet-2024-11.pdf; raw/outcomes/nhes-apprenticeship-factsheet-2026.pdf
- note: Covers all registered apprentices in NH of any age, not only recent graduates. **Discrepancy:** the 2026 fact sheet's FY24 column (2,707 active; 1,275 new; 528 completed; 55 new programs; 434 total programs) repeats most of its FY22 column and differs from the November 2024 fact sheet's FY24 figures used below. Its "Change FY 24-25" (+563 active, 18.9%) is computed from those repeated values. Its text says FY2025 total programs were 514, with 403 having active apprentices.

| Place | Year | Active apprentices | New apprentices | Completed apprentices | New programs | Total programs | Source |
|---|---|---|---|---|---|---|---|
| NH | 2020 | 2,761 | 1,032 | 517 | 45 | 371 | Nov 2024 fact sheet |
| NH | 2021 | 2,679 | 1,130 | 688 | 75 | 436 | Nov 2024 fact sheet |
| NH | 2022 | 2,707 | 1,275 | 591 | 55 | 434 | Nov 2024 fact sheet |
| NH | 2023 | 2,981 | 1,492 | 536 | 39 | 449 | Nov 2024 fact sheet |
| NH | 2024 | 3,224 | 1,457 | 546 | 56 | 492 | Nov 2024 fact sheet |
| NH | 2025 | 3,270 | 1,272 | 569 | 65 | 514 | 2026 fact sheet |

## nh_new_apprentices_by_age_fy2024: Age of New Apprentices at Registration, FY2024

- unit: count
- period: Federal fiscal year 2024; year: 2024
- source: NHES, "Apprenticeships in New Hampshire" (November 2024), chart "Age of New Apprentices at Registration" — https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nhes-apprenticeship-factsheet-2024-11.pdf
- note: The chart's bars add to 658 (derived), fewer than the 1,457 new apprentices in the table above. The fact sheet doesn't explain the difference. Its text says "Forty-four percent of new apprentices ... were in their twenties", the median age at registration was 26, the most common age was 18 (64 apprentices), and "There were two apprentices under age 18 at registration." For FY2025, the 2026 fact sheet says 39% were in their twenties, the median age was 24, the most common age was 18 (97 apprentices), and 20 apprentices were under 18 at registration.

| Place | Age group | New apprentices |
|---|---|---|
| NH | 16–19 | 125 |
| NH | 20–24 | 175 |
| NH | 25–29 | 114 |
| NH | 30–34 | 75 |
| NH | 35–44 | 102 |
| NH | 45–54 | 43 |
| NH | 55–64 | 24 |

## nh_new_apprentices_top_occupations: Most Common Occupations for New Apprentices, FY2024 and FY2025

- unit: count
- period: Federal fiscal years 2024 and 2025; year: 2024, 2025
- source: NHES apprenticeship fact sheets (November 2024; April–May 2026), from U.S. DOL Office of Apprenticeship data — https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet.pdf; https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet-2026.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nhes-apprenticeship-factsheet-2024-11.pdf; raw/outcomes/nhes-apprenticeship-factsheet-2026.pdf
- note: Values were read from bar-chart labels in the extracted PDF text, in the order shown. The FY2024 chart has 10 bars; the occupation-to-value pairing assumes the labels and values are listed in the same order. In FY2024, 59% of active apprentices were in construction and extraction occupations; in FY2025, 54%.

| Place | Year | Occupation | New apprentices |
|---|---|---|---|
| NH | 2024 | Electricians | 104 |
| NH | 2024 | Elementary, middle and secondary school teachers | 88 |
| NH | 2024 | Plumbers, pipefitters and steamfitters | 87 |
| NH | 2024 | Industrial machinery mechanics | 46 |
| NH | 2024 | Painters, construction and maintenance | 45 |
| NH | 2024 | Welders, cutters, solderers and brazers | 44 |
| NH | 2024 | Machinists | 35 |
| NH | 2024 | CNC tool operators | 25 |
| NH | 2024 | Patternmakers, metal and plastic | 24 |
| NH | 2024 | Insulation workers, floor, ceiling and wall | 18 |
| NH | 2025 | Plumber | 200 |
| NH | 2025 | Electrician | 132 |
| NH | 2025 | Medical assistant | 64 |
| NH | 2025 | K-12 teacher | 62 |
| NH | 2025 | CNC operator, milling and turning | 27 |
| NH | 2025 | Marine machinery mechanic | 24 |

## nh_apprentice_wages: Average Starting and Journeyworker Wages of New Apprentices

- unit: dollars (per hour)
- period: Federal fiscal years 2024 and 2025; year: 2024, 2025
- source: NHES apprenticeship fact sheets (November 2024; April–May 2026) — https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet.pdf; https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet-2026.pdf
- as_of: 2026-11-08
- raw: raw/outcomes/nhes-apprenticeship-factsheet-2024-11.pdf; raw/outcomes/nhes-apprenticeship-factsheet-2026.pdf
- note: "Journeyworker wage" is the expected wage after completing the program. Both fact sheets say the median apprenticeship was expected to last 3.5 years.

| Place | Year | Average starting wage | Average journeyworker wage | Increase (source) |
|---|---|---|---|---|
| NH | 2024 | 22.46 | 27.32 | 22% |
| NH | 2025 | 20.06 | 25.58 | 28% |

### Students with disabilities after high school

## idea_exiting_nh_by_reason: How NH Students With Disabilities (Ages 14–21) Left School, 2018–19 to 2023–24

- unit: count (with derived percent)
- period: School years 2018-19 to 2023-24 (July 1 – June 30); year: 2019–2024
- source: U.S. Department of Education, OSEP, IDEA Section 618 State Part B Exiting data files (EDFacts file specification 009), data.ed.gov — e.g. https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/3705d2cb-29ba-4d2b-9cd3-2268d2ca835b/download/bexiting2023-24-1.csv; 2023-24 Static Table bexiting_1 — https://data.ed.gov/dataset/ca86ef17-cf38-44f0-863e-1137f069fe80/resource/1e02717f-41dc-49d5-8298-4154e62b1dc1/download/2324-bexiting-1.xlsx
- as_of: 2026-11-08
- raw: raw/outcomes/idea618-bexiting2018-19-4.csv … idea618-bexiting2023-24-1.csv; raw/outcomes/idea618-2324-bexiting-1.xlsx
- note: "All Disabilities", ages 14 to 21 total. "Total exiting school" = regular diploma + certificate + reached maximum age + dropped out + died (the sum was checked for every year). **Derived:** "% diploma" = regular diploma ÷ total exiting school. NH reports no alternate diploma ("-"). Students who transferred to regular education or moved (known to be continuing) left special education but not school.

| Place | Year | Regular diploma | Certificate | Reached maximum age | Dropped out | Died | Total exiting school | % diploma (derived) | % dropped out (derived) | Transferred to regular education | Moved, known to be continuing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NH | 2019 | 1,348 | 128 | 38 | 129 | 4 | 1,647 | 81.8 | 7.8 | 926 | 420 |
| NH | 2020 | 1,311 | 124 | 34 | 112 | 10 | 1,591 | 82.4 | 7.0 | 717 | 413 |
| NH | 2021 | 1,234 | 150 | 39 | 150 | 2 | 1,575 | 78.3 | 9.5 | 582 | 420 |
| NH | 2022 | 1,348 | 152 | 30 | 148 | 8 | 1,686 | 80.0 | 8.8 | 771 | 488 |
| NH | 2023 | 1,532 | 63 | 5 | 143 | 7 | 1,750 | 87.5 | 8.2 | 636 | 357 |
| NH | 2024 | 1,450 | 89 | 11 | 145 | 4 | 1,699 | 85.3 | 8.5 | 729 | 335 |

## idea_ind14_nh_post_school_outcomes: Students With IEPs One Year After Leaving High School (Indicator 14), FFY2018–FFY2024

- unit: percent
- period: Federal fiscal years 2018–2024. FFY2024 = youth who left school during 2023-24, surveyed by September 2025; FFY2023 = left in 2022-23. year: 2019–2024 (school year left, FFY2018–FFY2023 inferred as one year earlier each)
- source: NH DOE, Part B SPP/APR for FFY2024 (Indicator 14, historical data and FFY 2024 data) — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/nh-01-spp-part-b-ffy-2024-25-final_0.pdf; FFY2018 value from the FFY2023 SPP/APR — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/nh-01-spp-part-b-ffy-2023-24-3354-20250623073648-and-determination.pdf
- as_of: 2026-11-08 (FFY2024 APR); Wayback snapshot 2025-08-31 (FFY2023 APR)
- raw: raw/outcomes/nhdoe-nh-01-spp-part-b-ffy-2024-25-final.pdf; raw/outcomes/nhdoe-nh-01-spp-part-b-ffy-2023-24-3354-20250623073648-and-determination.pdf
- note: A = enrolled in higher education; B = higher education or competitively employed; C = higher education, other postsecondary education or training, or any employment. Based on a survey with low response (see next table). NH DOE reported FFY2023 and FFY2024 responses as not representative.

| Place | FFY | A: higher education | B: higher education or competitive job | C: any education, training or job | Target A | Target B | Target C |
|---|---|---|---|---|---|---|---|
| NH | 2018 | 48.18 | 79.09 | 84.55 | 40.40 | 64.00 | 78.20 |
| NH | 2019 | 41.80 | 68.85 | 83.61 | 40.40 | 64.00 | 78.20 |
| NH | 2020 | 45.45 | 80.30 | 93.94 | 45.45 | 80.30 | 93.94 |
| NH | 2021 | 35.59 | 71.19 | 84.75 | 45.45 | 80.30 | 95.00 |
| NH | 2022 | 23.44 | 70.31 | 81.25 | 50.50 | 85.30 | 96.00 |
| NH | 2023 | 25.88 | 55.29 | 72.94 | 50.50 | 85.30 | 97.00 |
| NH | 2024 | 22.33 | 48.54 | 71.84 | 50.50 | 90.30 | 98.00 |

## idea_ind14_nh_survey_counts: Indicator 14 Survey Counts, FFY2023 and FFY2024

- unit: count
- period: FFY2023 (left school 2022-23) and FFY2024 (left school 2023-24); year: 2023, 2024
- source: NH DOE, Part B SPP/APR FFY2023 and FFY2024, Indicator 14 "SPP/APR Data" — URLs as above
- as_of: Wayback snapshot 2025-08-31 (FFY2023); 2026-11-08 (FFY2024)
- raw: raw/outcomes/nhdoe-nh-01-spp-part-b-ffy-2023-24-3354-20250623073648-and-determination.pdf; raw/outcomes/nhdoe-nh-01-spp-part-b-ffy-2024-25-final.pdf
- note: Each category counts a respondent once: 2 = competitively employed but not in higher education; 3 and 4 = neither of those. The FFY2023 APR says 30 more youth started the survey without finishing enough to count; the FFY2024 APR says 55. Response rate for FFY2022 was 3.81%.

| Place | FFY | Targeted youth | Respondents | Response rate | 1. Higher education | 2. Competitively employed | 3. Other postsecondary education or training | 4. Other employment |
|---|---|---|---|---|---|---|---|---|
| NH | 2023 | 1,750 | 85 | 4.86% | 22 | 25 | 10 | 5 |
| NH | 2024 | 1,695 | 103 | 6.08% | 23 | 27 | 20 | 4 |

## idea_ind13_nh_transition_iep_compliance: IEPs of Students 16+ With All Required Transition Parts (Indicator 13), FFY2018–FFY2024

- unit: percent
- period: Federal fiscal years 2018–2024 (FFY2024 records reviewed July 1, 2024 – June 30, 2025); year: 2018–2024 as FFY
- source: NH DOE, Part B SPP/APR FFY2024 (Indicator 13) — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/nh-01-spp-part-b-ffy-2024-25-final_0.pdf; FFY2018 and FFY2023 counts from the FFY2023 SPP/APR — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/nh-01-spp-part-b-ffy-2023-24-3354-20250623073648-and-determination.pdf
- as_of: 2026-11-08; Wayback snapshot 2025-08-31
- raw: raw/outcomes/nhdoe-nh-01-spp-part-b-ffy-2024-25-final.pdf; raw/outcomes/nhdoe-nh-01-spp-part-b-ffy-2023-24-3354-20250623073648-and-determination.pdf
- note: A compliance measure (the target is always 100%), based on a desk audit of about 11% of eligible student files. FFY2022 is the baseline year.

| Place | FFY | Compliant files | Files reviewed | Percent | Target |
|---|---|---|---|---|---|
| NH | 2018 | | | 33.33 | 100 |
| NH | 2019 | | | 90.22 | 100 |
| NH | 2020 | | | 64.29 | 100 |
| NH | 2021 | | | 79.07 | 100 |
| NH | 2022 | | | 54.20 | 100 |
| NH | 2023 | 457 | 615 | 74.31 | 100 |
| NH | 2024 | 460 | 614 | 74.92 | 100 |

### Jobs ahead and migration

## nhes_projected_openings_by_education: Projected Yearly Job Openings in NH by Usual Entry Education, 2024–2034

- unit: count (with derived percent)
- period: Long-term projections, base year 2024 to 2034; year: 2034
- source: NH Employment Security, ELMI Bureau, "Long-Term Employment Projections, 2024-2034", Occupational Projections Statewide (xlsx) — https://mm.nh.gov/files/uploads/nhes/documents/occ-projections-lt-2024-2034.xlsx (linked from https://www.nhes.nh.gov/elmi/products-and-services/employment-projections)
- as_of: 2026-11-08
- raw: raw/outcomes/nhes-occ-projections-lt-2024-2034.xlsx
- note: **Derived.** We summed "Total Annual Openings" (exits + transfers + growth) for the 659 detailed occupations with published figures, grouped by the first part of the "Education/Experience/Training" column. 112 occupations were not published ("Employment data do not meet disclosure standards") and are left out. The file's own all-occupations total is 82,298 openings a year; the detailed sum is 80,838. Total NH employment: 737,947 (2024 estimate), projected 764,713 in 2034 (+3.6%). "Postsecondary" means a postsecondary non-degree award, such as a certificate. "None" means no formal credential.

| Place | Usual entry education | Yearly openings (derived sum) | Detailed occupations | % of summed openings (derived) |
|---|---|---|---|---|
| NH | High school diploma or equivalent | 28,257 | 257 | 35.0 |
| NH | No formal credential | 27,952 | 77 | 34.6 |
| NH | Bachelor's degree | 12,370 | 149 | 15.3 |
| NH | Postsecondary non-degree award | 5,249 | 44 | 6.5 |
| NH | Associate's degree | 2,604 | 41 | 3.2 |
| NH | Some college, no degree | 2,204 | 6 | 2.7 |
| NH | Master's degree | 1,572 | 32 | 1.9 |
| NH | Doctoral or professional degree | 630 | 53 | 0.8 |
| NH | (Of all: occupations whose usual training is an apprenticeship) | 1,164 | 11 | 1.4 |

The 11 apprenticeship-training occupations (yearly openings): carpenters 418; electricians 371; plumbers, pipefitters and steamfitters 236; sheet metal workers 69; structural iron and steel workers 25; glaziers 19; brickmasons and blockmasons 11; stonemasons 5; millwrights 5; boilermakers 4; musical instrument repairers and tuners 1.

## carsey_nh_net_migration_young_adults: Net Migration of Young Adults Into NH From Other States, 2015–2019

- unit: number (people per year)
- period: Average per year, 2015–2019 vs 2010–2014 (ACS 5-year samples); year: 2019
- source: Kenneth M. Johnson, Carsey School of Public Policy, University of New Hampshire, "Migration Gains to New Hampshire From Other U.S. States Are Growing, With the Largest Gains Among Young Adults" (December 10, 2020) — https://carsey.unh.edu/publication/snapshot/migration-gains-to-NH-are-growing
- as_of: 2026-11-08
- raw: raw/outcomes/carsey-2020-12-10-migration-gains-young-adults.html
- note: Covers people moving between NH and other U.S. states, not just NH graduates. The brief says it "uses sample estimates and should be interpreted with caution." For where NH's new college students go, see NCES Digest Table 309.20 in `national-comparisons.md`.

| Place | Measure | Value |
|---|---|---|
| NH | Average yearly net domestic migration gain, ages 18–29, 2015–2019 | 3,800 |
| NH | Same, ages 18–29, 2010–2014 | "no gain at all" |
| NH | Average yearly net domestic migration gain, all ages, 2015–2019 | 8,300 |
| NH | Same, all ages, 2010–2014 | about 1,000 |

---

## Facts (definitions and caveats)

## postsecondary-enrollment-rate-meaning: What NH's "Post-secondary Enrollment Rate" Counts

- kind: term
- question_type: after_high_school
- description: The definition and data source of the college enrollment rate NH DOE publishes for schools, districts and the state (the iExplore measure in the site's database).

1. New Hampshire's Department of Education defines its Post-secondary Enrollment Rate as the "Percent of Students enrolling in a Higher Institution (2 or 4 years) after immediately completing their high school diploma. College enrollment must be within the year following graduation."
   - citation: NH DOE iGlossary, term "Post-secondary Enrollment Rate" (category College and Career Readiness)
   - source: https://jwt.nh.gov/?src_route=/iGlossary/Glossary
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: raw/outcomes/nhdoe-iglossary-postsecondary-enrollment-rate-2026-11-08.json (read through the Tableau dashboard).
2. NH DOE says its post-secondary enrollment data come from National Student Clearinghouse services and from the University System of New Hampshire.
   - citation: NH DOE iReport, State of New Hampshire, College & Career Readiness
   - source: https://ireport.education.nh.gov/state/NH/grad-ccr
   - as_of: Wayback snapshot 2022-05-29
   - review_by: 2027-11-08
3. NH DOE's 2021–2023 postsecondary report describes the same data as coming from the National Student Clearinghouse, CCSNH and USNH.
   - citation: NH DOE, The Status of Postsecondary Education in New Hampshire, 2021–2023, p. 12
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2021-12/nhedreport-2021-final-digital.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. In New Hampshire, the post-secondary enrollment rate counts students found enrolled in college records. That is different from graduates' self-reported plans at the end of senior year, the other measure on the site. The two should not be read as the same thing.
   - citation: NH DOE iGlossary and iReport definitions (above)
   - source: https://jwt.nh.gov/?src_route=/iGlossary/Glossary
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: Contrast drawn by us from the definitions; the plans data's own definition is in the site's database, not re-checked here.
5. NH DOE's published statewide values for 2019 differ by source: 57.72% on the old iReport and 58.5% in the 2021–2023 postsecondary report.
   - citation: iReport (Wayback 2022-05-29); Status of Postsecondary Education 2021–2023, p. 12
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2021-12/nhedreport-2021-final-digital.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## national-student-clearinghouse-coverage: What National Student Clearinghouse Data Cover

- kind: term
- question_type: after_high_school
- description: How much of college enrollment the Clearinghouse captures, and what NH's NSC-based completion figures do and don't measure.

1. The Community College System of New Hampshire says the National Student Clearinghouse "typically captures ~97% of US postsecondary enrollment."
   - citation: Rubinstein, "Postsecondary Matriculation and Completion for New Hampshire Early College Students, 2016-2022" (July 15, 2024), p. 10 of the alignment report
   - source: https://media.sos.nh.gov/govcouncil/2024/1113/111%20GC%20Agenda%20111324.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. The six-year completion rates NH DOE reports for USNH, CCSNH and NH private colleges come from the Clearinghouse's "Completing College" state report and count students by the college where they started, not by where they went to high school.
   - citation: NH DOE, Status of Postsecondary Education 2021–2023, p. 16 (source line)
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2021-12/nhedreport-2021-final-digital.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: "By the college where they started" is our reading of the sector tables (USNH, CCSNH, NH private nonprofits).
3. The CCSNH early college study counts only students who took CCSNH dual enrollment courses. Each year's group includes only students whose last early college course was that year, so the report calls it "an imprecise proxy for high school seniors."
   - citation: Rubinstein (2024), p. 10
   - source: https://media.sos.nh.gov/govcouncil/2024/1113/111%20GC%20Agenda%20111324.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## perkins-cte-concentrator: What a CTE "Concentrator" Is in New Hampshire

- kind: term
- question_type: after_high_school
- description: Who is counted in NH's Perkins V career and technical education results.

1. For Perkins V, NH DOE defines a high school CTE concentrator as "a student who has completed at least two semester-long courses within the same CTE program."
   - citation: NH DOE, Perkins SDLPs Program Year 2026–2027, p. 1 (citing Perkins V Section 3(12), 20 U.S.C. § 2302)
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/perkins-state-determined-levels-of-performance-2026-2027_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. NH DOE defines a postsecondary CTE concentrator as a student who has earned at least 12 credits in a CTE program, or who has completed a program requiring fewer than 12 credits.
   - citation: same, p. 1
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/perkins-state-determined-levels-of-performance-2026-2027_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. NH DOE's Perkins V page gave an earlier version: a student who has completed two CTE courses, where a course is a semester-length CTE learning experience (including classroom, lab or shop time, and work-based learning such as internships, apprenticeships or student-run enterprises).
   - citation: NH DOE, "Perkins V: Strengthening Career and Technical Education for the 21st Century Act" page
   - source: https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-of-career-development/perkins-v
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
4. Perkins V results are percentages of CTE concentrators: the number of concentrators meeting the measure divided by all CTE concentrators.
   - citation: NH DOE, State Determined Performance Levels, Perkins Program Year FY24, Background
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/new-hampshire-state-determined-performance-levels-fy24.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08

## perkins-nh-indicators: What NH's Perkins V Results Measure (and Don't)

- kind: how_it_works
- question_type: after_high_school
- description: The meaning of NH's high school CTE measures, including placement after high school and why there is no credential count.

1. New Hampshire's Perkins "post-program placement" measure (3S1) is the percentage of CTE concentrators who, in the second quarter after leaving high school, are in postsecondary education, advanced training, military service, a service program, or are employed.
   - citation: NH DOE, State Determined Performance Levels (SDPL) Form, p. 1
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sdpl-form.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
2. NH DOE notes that "NH RSA 189:68(I) limits reporting of employment outcomes" for the placement measure.
   - citation: NH DOE, Perkins SDLPs 2026–2027, p. 1
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/perkins-state-determined-levels-of-performance-2026-2027_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. Perkins V lets each state choose a high school "program quality" measure: credentials earned, college credits earned, or work-based learning. New Hampshire chose work-based learning, measured as concentrators who graduated having taken part in work-based learning, divided by all concentrators who graduated.
   - citation: NH Perkins V State Plan, Section D.1 (Accountability for Results)
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2020-04/perkins-v-state-plan.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
4. As a result, New Hampshire's Perkins high school results include no figure for credentials earned by CTE students. The state's performance form lists "5S1: Program Quality – Attained Recognized Postsecondary Credential" as N/A.
   - citation: NH DOE, SDPL Form, p. 2
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sdpl-form.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
5. The credential measure in NH's Perkins results (2P1) is for postsecondary (community college) CTE concentrators, not high school students.
   - citation: NH DOE, Perkins SDLPs 2026–2027, p. 2 and Appendix A
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/perkins-state-determined-levels-of-performance-2026-2027_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
6. Perkins program years run July 1 to June 30, and results are reported to the U.S. Department of Education in the Consolidated Annual Report on a delay.
   - citation: NH DOE, Perkins SDLPs 2026–2027, p. 2
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/perkins-state-determined-levels-of-performance-2026-2027_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## nh-industry-recognized-credential: What NH Counts as an "Industry Recognized Credential"

- kind: term
- question_type: after_high_school
- description: NH DOE's definition and rubric for industry credentials in CTE.

1. NH DOE defines an Industry Recognized Credential as "the culminating evidence of a learner's proficiency in competencies that equip them for a productive career in a specific industry domain."
   - citation: NH DOE, New Hampshire Industry Recognized Credential Rubric
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/nh-industry-recognized-credential-definition-and-rubric_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. NH DOE's rubric rates a credential on elements including its assessment (scored highest when accredited by a third party and including a performance task), how clearly it states the required competencies, and how well it lines up with in-demand New Hampshire occupations according to labor market data and employers.
   - citation: same rubric
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/nh-industry-recognized-credential-definition-and-rubric_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. NH DOE's career and technical education page links the credential rubric and Perkins targets but no counts of credentials earned by students.
   - citation: NH DOE, Office of Career Technical Education page
   - source: https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-career-development/office-career-technical-education
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: raw/outcomes/nhdoe-cte-office-page-2026-11-08.txt

## registered-apprenticeship-basics: How Registered Apprenticeships Work in New Hampshire

- kind: how_it_works
- question_type: after_high_school
- description: What a registered apprenticeship is, who can start one, and the youth option for high school students.

1. Registered apprenticeships combine job-related classroom instruction with on-the-job learning. Apprentices are paid from the first day, get wage increases as they gain skill, and on completion receive "an industry-issued, nationally recognized credential." Apprenticeships last one to six years.
   - citation: NH Employment Security, "Apprenticeships in New Hampshire" fact sheet (April–May 2026), p. 1
   - source: https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. NH Employment Security says most apprenticeships require 2,000 to 8,000 hours of on-the-job training, plus at least 144 hours of classroom training.
   - citation: NHES, Apprenticeships page
   - source: https://www.nhes.nh.gov/elmi/career-resources/apprenticeships
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. NH Employment Security lists these requirements to become an apprentice: at least 16 years old, a high school diploma or GED, U.S. citizenship or permanent residency, and the physical ability to do the work.
   - citation: NHES, Apprenticeships page, "How can I become an apprentice?"
   - source: https://www.nhes.nh.gov/elmi/career-resources/apprenticeships
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. A Registered Youth Apprenticeship lets students begin an apprenticeship in the final years of high school. NHES says to contact the school guidance counselor.
   - citation: NHES, Apprenticeships page, "What if I'm still in high school?"
   - source: https://www.nhes.nh.gov/elmi/career-resources/apprenticeships
   - as_of: 2026-11-08
   - review_by: 2027-11-08
5. New Hampshire's apprenticeship counts include apprentices of all ages. In FY2025, 20 new apprentices were under 18 at registration, and the most common age at registration was 18. No count of recent NH high school graduates or youth apprentices is published.
   - citation: NHES fact sheet (April–May 2026), p. 2
   - source: https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## indicator-14-post-school-outcomes: What "Indicator 14" Measures for Students With IEPs

- kind: term
- question_type: after_high_school
- description: The federal measure of what students with IEPs do in the year after leaving high school, and how NH collects it.

1. Indicator 14 reports the percent of youth who had IEPs when they left school and, within one year, were (A) enrolled in higher education; (B) enrolled in higher education or competitively employed; or (C) enrolled in higher education or other postsecondary education or training, or competitively employed or in some other employment.
   - citation: NH DOE, Indicator 14 IDEA Part B Data Fact Sheet (September 2022), p. 1
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/indicator-14-data-fact-sheet.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
2. For Indicator 14, "enrolled in higher education" means full- or part-time enrollment in a community college or a four-year college for at least one complete term in the year since leaving high school.
   - citation: same, p. 1
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/indicator-14-data-fact-sheet.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
3. For Indicator 14, "competitive employment" means working for pay at or above the minimum wage, in a setting with people who are not disabled, 20 hours a week for at least 90 days in the year since leaving high school. It includes the military. "Some other employment" means working for pay or self-employment for at least 90 days.
   - citation: same, p. 1
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/indicator-14-data-fact-sheet.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
4. New Hampshire measures Indicator 14 with a survey sent through districts to everyone who had an IEP when they left school the year before (graduates, certificate earners, dropouts and students who reached maximum age). Percentages are based on survey respondents only.
   - citation: same, p. 1–2
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/indicator-14-data-fact-sheet.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
5. For FFY2024, 103 of 1,695 youth responded (6.08%). NH DOE reported that the responses were not representative of youth who had IEPs when they left school (students with Other Health Impairments were under-represented by 16 points). It said the declines ("slippage") tie back to "the low response rate."
   - citation: NH DOE, Part B SPP/APR FFY2024, Indicator 14
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/nh-01-spp-part-b-ffy-2024-25-final_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
6. For FFY2023, NH DOE reported that responses under-represented students with Other Health Impairments by 18 percentage points. It found "nonresponse bias related to disability category had some impact" on the results.
   - citation: NH DOE, Part B SPP/APR FFY2023, Indicator 14
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/nh-01-spp-part-b-ffy-2023-24-3354-20250623073648-and-determination.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
7. NH DOE publishes Indicator 14 statewide only. Its fact sheet says district-level data are collected by the receiving district as entered on the survey, and are used for district determinations.
   - citation: Indicator 14 Data Fact Sheet, p. 2
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/indicator-14-data-fact-sheet.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08

## indicator-13-transition-iep: What "Indicator 13" Measures (Transition Plans in IEPs)

- kind: term
- question_type: after_high_school
- description: The federal compliance measure for transition planning in IEPs of students 16 and older, and how NH checks it.

1. Indicator 13 is the percent of youth with IEPs aged 16 and above whose IEP includes measurable postsecondary goals updated each year and based on a transition assessment, transition services including courses of study, and annual IEP goals related to transition needs. There must also be evidence that the student, and if appropriate a participating agency, was invited to the IEP meeting.
   - citation: NH DOE, Indicator 13 Data Fact Sheet (September 2022), p. 1
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/indicator-13-data-fact-sheet_0.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
2. New Hampshire monitors every district each year for Indicator 13 by a desk audit of about 11% of eligible student files. The federal target is 100%.
   - citation: NH DOE, Part B SPP/APR FFY2024, Indicator 13
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/nh-01-spp-part-b-ffy-2024-25-final_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. Indicator 13 checks whether IEP paperwork contains the required transition parts. It does not measure what students do after school; that is Indicator 14.
   - citation: Indicator 13 and Indicator 14 Data Fact Sheets
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/indicator-13-data-fact-sheet_0.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08

## idea-exiting-counts: What the Federal "Exiting" Counts for Students With Disabilities Mean

- kind: term
- question_type: after_high_school
- description: How the IDEA Section 618 counts of students with disabilities leaving school are defined.

1. The federal IDEA Part B exiting counts cover students ages 14 through 21 who received special education and left it during the reporting period of July 1 to June 30. Reasons include graduating with a regular diploma, receiving a certificate, reaching maximum age, dropping out, dying, moving (known to be continuing), and transferring to regular education.
   - citation: U.S. Department of Education, OSEP, IDEA Section 618 Static Table bexiting_1, 2023-24 (title and footnote 1)
   - source: https://data.ed.gov/dataset/ca86ef17-cf38-44f0-863e-1137f069fe80/resource/1e02717f-41dc-49d5-8298-4154e62b1dc1/download/2324-bexiting-1.xlsx
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. In these counts, "dropped out" means a student who was enrolled at some point in the reporting period, was not enrolled at the end, and did not leave for any of the other reasons. When OSEP calculates dropout percentages, it counts students who "moved, not known to continue" as dropouts.
   - citation: same table, footnote 3
   - source: https://data.ed.gov/dataset/ca86ef17-cf38-44f0-863e-1137f069fe80/resource/1e02717f-41dc-49d5-8298-4154e62b1dc1/download/2324-bexiting-1.xlsx
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. The IDEA exiting counts show how students with disabilities left school, not what they did afterward.
   - citation: same table (exit reasons only)
   - source: https://data.ed.gov/dataset/ca86ef17-cf38-44f0-863e-1137f069fe80/resource/1e02717f-41dc-49d5-8298-4154e62b1dc1/download/2324-bexiting-1.xlsx
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## acs-young-adult-measures: What the Census Young-Adult Figures Count

- kind: term
- question_type: after_high_school
- description: Caveats for using American Community Survey figures to answer questions about NH graduates.

1. The Census Bureau's American Community Survey figures for New Hampshire count 18–24-year-olds who live in New Hampshire, whether or not they went to high school in New Hampshire. They are not a measure of what NH graduates do.
   - citation: ACS 1-year Table S1401, universe "Population 18 to 24 years", New Hampshire
   - source: https://data.census.gov/table/ACSST1Y2025.S1401?g=040XX00US33
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. ACS figures are survey estimates with margins of error. For example, the 2025 share of NH 18–24-year-olds enrolled in college (40.3%) has a margin of error of ±2.8 points, so small year-to-year changes may not be real changes.
   - citation: ACS 1-year 2025, Table S1401, S1401_C02_030E and its margin of error
   - source: https://data.census.gov/table/ACSST1Y2025.S1401?g=040XX00US33
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: "May not be real changes" is a general reading of the margin of error, not a significance test.

## pseo-coverage-nh: Earnings by College Program (PSEO) Don't Cover NH Colleges

- kind: term
- question_type: after_high_school
- description: Whether the Census Bureau's Post-Secondary Employment Outcomes data can show earnings of UNH or CCSNH graduates.

1. The Census Bureau's Post-Secondary Employment Outcomes (PSEO) data, which show earnings and job locations of graduates by college and program, include no New Hampshire college. The latest release (version 4.14.1, 2026Q2) lists 1,117 institutions in 37 other states and DC.
   - citation: Census LEHD, PSEO latest release, pseo_all_institutions.csv and version_pseo.txt (files dated 2026-08-25)
   - source: https://lehd.ces.census.gov/data/pseo/latest_release/all/pseo_all_institutions.csv
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: raw/outcomes/census-pseo-all-institutions.csv; raw/outcomes/census-pseo-version_pseo.txt

## nh-young-adult-migration: Young Adults Moving Into and Out of New Hampshire

- kind: research
- question_type: after_high_school
- description: What NH-specific research says about young adults' migration, beyond college-going patterns.

1. A University of New Hampshire Carsey School analysis of Census data found that, between 2015 and 2019, about 3,800 more 18–29-year-olds moved to New Hampshire from other states each year than left for other states. Between 2010 and 2014 there was no net gain at that age.
   - citation: Johnson, K.M., "Migration Gains to New Hampshire From Other U.S. States Are Growing, With the Largest Gains Among Young Adults," Carsey School of Public Policy, December 10, 2020
   - source: https://carsey.unh.edu/publication/snapshot/migration-gains-to-NH-are-growing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. The Carsey analysis counts all people moving between states, not only NH high school graduates, and its author cautions that it "uses sample estimates and should be interpreted with caution."
   - citation: same
   - source: https://carsey.unh.edu/publication/snapshot/migration-gains-to-NH-are-growing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. In NH DOE's 2019 iReport data, 52.40% of NH completers who enrolled in college went to college in New Hampshire and 47.68% out of state.
   - citation: NH DOE iReport, State of New Hampshire, College & Career Readiness, 2018-2019 (Institution Location)
   - source: https://ireport.education.nh.gov/state/NH/grad-ccr
   - as_of: Wayback snapshot 2022-05-29
   - review_by: 2027-11-08
   - note: The denominator is inferred (the two values add to about 100%); see the nh_postsec_enrollees_by_institution_2019 table.

## data-sources-after-high-school: Where NH Data on Life After High School Come From

- kind: how_it_works
- question_type: after_high_school
- description: Which agency publishes each measure of what NH graduates do, and at what level.

1. New Hampshire's college-enrollment rate for high school completers is published by NH DOE for schools, districts and the state through iExplore, using National Student Clearinghouse and USNH data.
   - citation: NH DOE iGlossary; iReport
   - source: https://jwt.nh.gov/?src_route=/iGlossary/Glossary
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. CTE results under Perkins V are published by NH DOE statewide only, as percentages of CTE concentrators.
   - citation: NH DOE, Perkins SDLPs 2026–2027
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/perkins-state-determined-levels-of-performance-2026-2027_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. Registered apprenticeship counts for New Hampshire come from the U.S. Department of Labor, Office of Apprenticeship. NH Employment Security summarizes them in a yearly fact sheet.
   - citation: NHES apprenticeship fact sheet (April–May 2026), chart source lines
   - source: https://mm.nh.gov/files/uploads/nhes/documents/apprenticeship-factsheet-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. Post-school outcomes of students with IEPs (Indicator 14) and transition-plan compliance (Indicator 13) are published by NH DOE statewide each year in its federal State Performance Plan/Annual Performance Report.
   - citation: NH DOE, State Performance Plan, Annual Performance Report and Indicators page
   - source: https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-special-education-support/state-performance-plan-annual-performance-report-and-indicators
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: raw/outcomes/nhdoe-spp-apr-page-2026-11-08.txt

---

## Not retrieved

| Item | What was tried | Result |
|---|---|---|
| NH DOE National Student Clearinghouse reports on persistence and completion of NH high school graduates (statewide, 2017–21, mentioned in earlier research) | NH DOE site search in Chrome ("national student clearinghouse", "post-secondary enrollment"); NH DOE Postsecondary Education page; web searches; Wayback CDX search of education.nh.gov files (the archive's search service was "Temporarily Offline") | Not found. The 2021–2023 postsecondary report gives only enrollment rates (2019, 2020). Persistence and completion of NH graduates wherever they enroll: not retrieved. |
| iExplore statewide Post-secondary Enrollment Rate, 2016–2025 | Tableau embedding API on https://jwt.nh.gov/?src_route=/iExplore/Explore-Dashboard (worksheets listed; the default view is school-level class size) | Not extracted. An earlier extraction gave graduation-rate values near 36–38%, which can't be right, so its post-secondary values weren't used. The definition was confirmed in iGlossary. |
| National Student Clearinghouse Research Center current state tables (Completing College 2025, Persistence and Retention) for NH colleges | Web search | The 2025 state results are in an interactive dashboard; not retrieved. The NSC figures above (December 2020 report) come via NH DOE's 2021 report. |
| Federal Perkins V performance data (OCTAE "Perkins State Plans and Data Explorer", https://octae.ed.gov/pcrn/explorer) | curl (Angular app with no public API paths in the main bundle); perkins.ed.gov/pims/DataExplorer | The PIMS Data Explorer has Perkins IV data only, through 2018-19. The PCRN explorer was not extracted. NH DOE's own Perkins documents were used. |
| CTE enrollment, completers and credentials by career center | NH DOE CTE office page (2026-11-08); Perkins documents | Not published; NH DOE reports statewide Perkins percentages only (data request needed). |
| U.S. DOL Apprentices by State dashboard (https://www.apprenticeship.gov/data-and-statistics/apprentices-by-state-dashboard) | curl (page loads; data in an embedded Tableau view); an earlier attempt was refused (PermissionDenied) | Not extracted; NHES fact sheets (from DOL data) were used. Youth apprenticeship counts are not published. ApprenticeshipNH (https://apprenticeshipnh.com/) home page shows no counts. |
| NH Employment Security analyses of young workers | NHES ELMI pages (home, Employment Projections, Apprenticeships) in Chrome | No young-worker report found; ACS tables used instead. Projections were used for job openings. |
| Census API (api.census.gov) data queries | curl to api.census.gov/data/2024 and /2025 acs1/subject | Redirected to "missing_key". Data were taken from the data.census.gov table API; variable labels from api.census.gov group metadata (2016 and 2018 labels not checked). |
| Indicator 14 and 13 by district | NH DOE SPP/APR page and fact sheets | Statewide only; district results are not public. |
| Carsey 2018 brief on 20-somethings (2013–2017 net gain) | Seen only in search results | Not opened, so not used. |
