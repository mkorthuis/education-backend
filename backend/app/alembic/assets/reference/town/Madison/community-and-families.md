# Madison Community and Families: Town Profile, Housing, Child Care, School Options, Broadband, Family Help, History and Civic Life

Part of the Madison research (town/Madison). Gathered November 13, 2026.

## Summary

This file covers the community side of the Madison residents' questions: Madison's population, ages, births, income and poverty; housing, seasonal homes, the Village District of Eidelweiss and home prices; licensed child care in and near Madison with derived drive times; private, charter and EFA options within about 25 minutes; home internet and broadband grants; the town's police, fire and alerts; food help, charitable funds and scholarships for Madison graduates; town recreation, the library and summer camp; local history (the Madison Boulder, the Madison Corner School and the Historical Society); and where town meeting, the school deliberative session and community events are held.

- **10 topics, 93 facts and 11 number tables.** On November 14, 2026, three facts and the table rows and columns that only repeated the Census Bureau's survey (ACS) measures now in the site's Census data (income, poverty, home values, broadband and others) were taken out. Raw copies are in `raw/community/` (about 62 MB): Census JSON, OPD reports, NH DHHS child care data, the CSF EFA feed, Nominatim and OSRM routes, NH REALTORS reports, NH BEAD files, the Madison town reports for 2020–2024, the 2025 and 2026 town meeting minutes, the 2026 Madison School District annual report, Recreation Committee minutes and town, library, Historical Society, Eidelweiss and Kennett scholarship pages.
- **Main findings:**
  - **Child care:** NH DHHS lists two licensed programs in Madison, Family Child Care of Madison and Madison Preschool at The Madison Church; their places, ages and openings are in the site's data. **Derived:** six licensed programs taking infants are within about 25 minutes of Madison Elementary by car; no provider publishes how long its waitlist is.
  - **School options:** no private school with full-time students is within 25 minutes by car (derived). The nearest are New Life Christian Academy (about 32 minutes), Cornerstone Christian Academy in Ossipee (33) and Fryeburg Academy (34). Within 25 minutes, the EFA marketplace lists homeschool programs (HomeSweet HomeSchool in Madison, Tamworth Village Homeschool, Tamworth Learning Circles) and an early-childhood school; it flags no micro-schools. CSF counted 11 Madison students eligible for an EFA for 2026-27.
  - **Broadband:** Fidium finished fiber in the Madison wire center in 2024 (1,979 "passings", 82 miles). The state's final list of locations eligible for federal BEAD grants (unserved or underserved) has 21 in Madison, all awarded to SpaceX satellite service in a project the state labeled non-priority.
  - **People and homes:** 2,565 residents in 2020 (OPD estimate 2,664 for 2025). Children under 18 fell from 500 (2010) to 410 (2020). Resident births were 5 to 12 a year in 2020–2024. 36.8% of homes were seasonal in the 2020 Census (derived). The median single-family sale price was $500,000 through October 2026.
  - **Civic space:** the Madison Elementary gym (James Noyes Hall) is the polling place and holds the town meeting business session and the school district's deliberative session (premise confirmed for 2026).
  - **Scholarships:** the Madison Scholarship Fund (since 1987), a town-held Edward Granville Scholarship trust ($11,909.56 at the end of 2024, with no spending recorded 2020–2024) and six awards on Kennett's scholarship lists that name Madison or Madison Elementary. Some allow two-year and trade study; none is limited to it.
  - **Family help:** the Madison Church Food Pantry served 971 people in 2024 and opened a new building in June 2025; all Madison Elementary students can get weekend food bags through End 68 Hours of Hunger. The Ossipee Children's Fund, which paid toward Madison children's camp and child care, has announced its closure.
- **Main gaps:** the FCC broadband map (blocked); an NH nonpublic school list (blocked); how long infant care waitlists are (none published); a Madison coat drive (none found); Silver Lake's railroad history in any local source; the 2025 Madison town report (not posted).
- **Premises checked:**
  - "Only two licensed childcare facilities in Madison" (P7.1): **correct.** DHHS lists two Madison programs, a licensed family program and Madison Preschool (from 33 months), both with active licenses. The SAU 13 public preschool at Madison Elementary is not a DHHS-licensed program. (Corrected November 14, 2026: this check first called Madison Preschool inactive, misreading DHHS's scholarship-enrollment field.)
  - The gym as the site of Town Meeting and the Deliberative Session (P20.3): **correct for 2026.** Both the March 14, 2026 town meeting and the February 2, 2026 school deliberative session were in James Noyes Hall at Madison Elementary.
  - "Micro-school options" within 25 minutes (P19.1): **none flagged.** The EFA marketplace marks no entry as a micro-school; nearby options describe themselves as homeschool programs.
  - "Town broadband committee" (P19.2): **not found.** Madison has no broadband committee on its boards list; the selectmen appoint representatives to the county's Communications District.
  - Scholarships "dedicated to Madison graduates pursuing trade schools or two-year degrees" (P8.3): **partly.** No Madison award is limited to trades or two-year study, but several allow them.
- **Proposed shared topics** (used here; please review): `town-broadband` (local, local_practice): "Home internet in a town: subscription rates, fiber and other buildout, state and federal broadband grants, and regional broadband districts"; `town-government-and-civic-spaces` (local, governance_money): "How a town is governed (select board, town meeting, village districts) and where elections, town meeting, school sessions and community events are held"; `town-history-and-heritage` (local, local_practice): "Local history resources for families and schools: historical societies, museums, historic school buildings and natural landmarks". Scholarships sit under `town-family-help`, as in the Conway file; I second Conway's proposed `local-scholarships` topic.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.2 (community side) After-school care or enrichment in Madison or Silver Lake | town-recreation-and-summer facts 1–9; site data: child_care (Madison district, and Freedom and Tamworth by town: school-age programs and weekday hours); town-child-care fact 3; madison_area_child_care_drive_distance | partial | Town Rec (sports, open gym, chess, teen nights, summer camp at $700 for 8 weeks), library programs and local EFA-listed providers are covered. No town-run daily after-school care was found. School-run before- and after-school care is in the school-day file (agent 2). Whether licensed school-age programs pick up at Madison Elementary is not stated. |
| P7.1 Licensed child care in Madison; infant and toddler waitlists | site data: child_care (Madison district, and Freedom and Tamworth by town); town-child-care facts 1–7; madison_area_child_care_drive_distance; library: nh-child-care-search, child-care-aware-nh, child-care-scholarship-eligibility, head-start-eligibility | partial | **Premise checked** (see Summary). Places, ages, wait-list status and reported openings are in the site's data; derived drive times are here. **No provider publishes how long its waitlist is**, so "how early" cannot be answered from public sources. The SAU 13 preschool is in district-practices.md and the school file. |
| P8.3 Local scholarships or trust funds for Madison graduates, including trade and two-year | town-family-help facts 10–16; Conway file: town-family-help facts 8–15, kennett_local_scholarships_trades_two_year; library: ccsnh-tuition-and-aid, granite-edvance | partial | Madison Scholarship Fund, the Granville trust, four Madison-specific awards on Kennett's standard list and two on its non-standard list. Award amounts are not posted. No award limited to trades or two-year study was found. |
| P15.1 (community side) Weekend food bags and food help | town-family-help facts 1–5; site data: free and reduced lunch (district 333) | full | End 68 Hours of Hunger serves all Madison Elementary students; the Madison Food Pantry supplies classroom snacks. How the school hands out bags day to day is not described. |
| P15.3 (community side) Church and civic partnerships with the school; coat drives | town-family-help facts 2, 3, 16, 17; town-government-and-civic-spaces fact 6; town-history-and-heritage fact 6 | partial | Partnerships named by the school, the pantry, SLAM and Rec are covered. **No coat drive was found.** The school's volunteer process is in the Madison Elementary file (agent 1). |
| P18.3 (town side) SRO or town patrol coverage | town-emergency-services facts 1–4 | partial | **No source mentions a school resource officer** for Madison, Freedom or Tamworth. The department has a chief, a sergeant and two officers listed, with overnight on-call coverage. School security is in the school file. |
| P19.1 EFA private or micro-school options within 25 minutes | town-school-options-nearby facts 1–8; site data: census (Madison district: private or home school share, K–12); madison_area_school_options_drive; madison_area_efa_marketplace_by_town; library: efa-eligibility-and-cap, efa-uses-and-requirements, efa-provider-list; Conway file: town-school-options-nearby (charters); Jackson file: town-school-options-nearby 1–10; district-fees 1 in `Jackson/community-and-families.md` (tuition) | full | Drive times are **derived** (OSRM, normal conditions). No full-time private school is within 25 minutes. No micro-school is flagged. Northeast Woodland could not be routed. |
| P19.2 Broadband reliability on back roads | site data: census (Madison district: households with broadband, children with a computer and broadband); town-broadband facts 1–7; madison_area_internet_subscriptions | partial | Subscription rates (site data and fact 1), Fidium buildout, the county district and BEAD awards are covered. **The FCC map could not be opened**, so no address-level coverage or reliability data. Satellite limits under tree canopy are as the state describes them. |
| P20.1 (community side) Madison Boulder, Silver Lake history, one-room schoolhouses | town-history-and-heritage facts 1–8 | partial | Boulder, Madison Corner School and Historical Society programs are covered. **No source on Silver Lake's railroad era** was found. What the 4th-grade curriculum covers is in the school file (agent 1). |
| P20.3 The gym as civic gathering space | town-government-and-civic-spaces facts 3–7 | full | **Premise confirmed.** The polling place, town meeting, school deliberative session and many Rec and community events use James Noyes Hall. |
| Also: population, ages, income, school-age children | site data: census (Madison district: population, median age, children, income, poverty, households with children); town-community-profile facts 1–10; madison_population_census_and_opd; madison_children_by_age_census; madison_resident_births; madison_area_income_poverty (Ossipee); site data: enrollment by town and school | full | ACS margins for Madison's children are wide; 2010 and 2020 Census counts are used for ages. |
| Also: housing, seasonal homes, Eidelweiss, values and rents | site data: census (Madison district: housing units, seasonal share, owners, home value, rent, cost burden); town-housing facts 1–8; town-government-and-civic-spaces facts 8–9; madison_housing_units_occupancy; madison_area_housing_profile (Ossipee); madison_area_median_sale_price | full | No count of short-term rentals was found. |
| Also: town government, fire and rescue, dispatch and alerts | town-government-and-civic-spaces facts 1–2; town-emergency-services facts 5–10 | full | |

## town-community-profile: Madison's Population, Ages, Births, Income and Poverty

- kind: local
- question_type: local_practice
- description: A town's people beyond the site's Census estimates: decennial Census counts and ages, births, population projections, the enrollment outlook and civic life

1. The Census counted 2,502 Madison residents in 2010 and 2,565 in 2020, a rise of 63 people (2.5%, derived). NH's Office of Planning and Development (OPD) estimated 2,664 residents in 2025, including 16 living in group quarters, at 69.19 people per square mile.
   - citation: 2020 Census Redistricting Data (PL 94-171), table P1; OPD, 2025 Population Estimates of New Hampshire Cities and Towns (published July 17, 2026)
   - source: https://www.nheconomy.com/getmedia/62b7f54e-dced-456c-9bbf-cac23ea1f7d5/2025-Population-Estimates.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Census P1_001N 2565 (raw/community/census/DECENNIALPL2020.P1-madison.json). OPD table row: "Madison 2,502 2,565 2,664 16 69.19" under columns 2010 Census, 2020 Census, OPD estimate 2025, group quarters population, persons per square mile. OPD "strongly recommends that these estimates not be compared on a year-to-year basis." Raw: raw/community/population/opd-2025-population-estimates.pdf (.txt)
2. OPD projects Madison's population at 2,677 in 2025, 2,765 in 2030, 2,812 in 2035 and 2040, 2,778 in 2045 and 2,728 in 2050. OPD's town projections give total population only, not ages.
   - citation: OPD, State, County, and Municipal Population Projections: 2020-2050 (September 2022), Table 2, Carroll County
   - source: https://www.nheconomy.com/getmedia/0205c62d-9c30-4b00-9c9e-d81d8f17b8b3/NH-Population-Projections-2020-2050-Final-Report-092022.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report row (text layer): "Madison town 2,565 2,677 2,765 2,812 2,812" for 2020–2040, then separate 2045 and 2050 columns listing the towns in the same order ("2045 54,273 822 3,466 ... 1,113 2,778 ..." and "2050 53,293 807 3,403 ... 1,093 2,728 ..."), where Madison follows Jackson; read by position. See table madison_population_census_and_opd. Raw: raw/community/population/opd-population-projections-2020-2050.pdf (.txt)
3. The Census counted 71 Madison children under 5 and 339 aged 5 to 17 in 2020 (410 under 18, or 16.0% of residents, derived), down from 110 under 5 and 390 aged 5 to 17 in 2010 (500 under 18, or 20.0%).
   - citation: 2020 Census DHC table P12; 2010 Census SF1 table P12 (Sex by Age)
   - source: https://data.census.gov/table/DECENNIALDHC2020.P12?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Derived sums. 2020: under 5 = 32 (male) + 39 (female); 5–17 = (68 + 60) + (64 + 59) + (43 + 45) = 339 (P12_003N–P12_006N, P12_027N–P12_030N). 2010: under 5 = 55 + 55; 5–17 = (77 + 62) + (97 + 66) + (48 + 40) = 390 (P012003–P012006, P012027–P012030). Downloaded from the data.census.gov table API with identifier nhfacts-research. See table madison_children_by_age_census. Raw: raw/community/census/DECENNIALDHC2020.P12-madison.json, DECENNIALSF12010.P12-madison.json, labels-2020-P12.json, labels-2010-P12.json
4. The state's Resident Birth Reports printed in Madison's annual town reports list 6 births to Madison residents in 2020, 8 in 2021, 12 in 2022, 5 in 2023 and 7 in 2024. The 2024 report also lists one birth that took place in Madison to a family whose residence is given as Silver Lake, on a separate "Madison Town Births" report.
   - citation: NH Division of Vital Records Administration, Resident Birth Report, as printed in the Town of Madison Annual Reports 2020–2024
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: "Total number of records" on each Resident Birth Report: 2020 = 6 (2020 report p. 42), 2021 = 8 (2021 report p. 30), 2022 = 12 (2022 report p. 41, checked against the page image), 2023 = 5 (2023 report p. 43), 2024 = 7 (2024 report p. 56, checked against the page image); "MADISON Town Births ... Total number of records 1 ... City Of Residence SILVER LAKE" (2024 report p. 57). Reports are dated in early January, so a late-registered birth could be missing. Children's and parents' names are not repeated. Scanned reports; transcribed from OCR and page images. See table madison_resident_births. Raw: raw/community/town/2020-TOWN-REPORT-WEB.ocr.txt, 2021-Madison-TownReport-web.ocr.txt, 2022-Madison-Town-Report.ocr.txt, 2023-Town-Report-Web.ocr.txt, 0000-2024-Town-Report.ocr.txt
5. The American Community Survey (ACS) for 2020-2024 estimates that 23.1% (±5.2) of Madison residents were 65 or older. Its estimate of 20 children under 5 (±30) is too uncertain to use; the 2020 Census counted 71.
   - citation: ACS 5-year 2020-2024, table DP05 (Demographic and Housing Estimates), Madison town; 2020 Census DHC table P12
   - source: https://data.census.gov/table/ACSDP5Y2024.DP05?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: DP05_0024PE 23.1 ±5.2; DP05_0005E 20 ±30. The site's database (ACS 2020-2024, table B01001) agrees: 619 residents 65 or older (±139, derived) of 2,680, and 20 under 5 (sum of the male and female under-5 cells, ±22 and ±16). The 2020 Census count of 71 under 5 is in fact 3. Median age, children under 6 and under 18, and the other Census survey measures for Madison are in the site's Census data. The ACS is a sample survey; for a town of about 2,600 its margins are wide. Raw: raw/community/census/ACSDP5Y2024.DP05-madison.json, labels-DP05.json
6. The ACS for 2020-2024 estimates that 16.7% (±6.7) of Madison households had incomes of $200,000 or more and 16.4% had incomes under $50,000 (derived sum: 164 households, ±61).
   - citation: ACS 5-year 2020-2024, tables S1901 and B19001 (Household Income in the Past 12 Months)
   - source: https://data.census.gov/table/ACSST5Y2024.S1901?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: S1901_C01_011E 16.7 ±6.7. Under $50,000 derived: 3.3 + 1.9 + 2.7 + 4.7 + 3.8 = 16.4. The site's database (B19001, ACS 2020-2024) agrees: 168 (±70) of 1,003 households at $200,000 or more; 164 under $50,000 (sum of the first nine brackets; margin ±61, derived as the square root of the sum of squared bracket margins). Madison's and the state's median income and poverty rates are in the site's Census data; Ossipee's are in table madison_area_income_poverty. Raw: raw/community/census/ACSST5Y2024.S1901-madison.json, ACSDT5Y2024.B19013-madison.json
7. The Madison School District's 2026 annual report gives Madison Elementary's free or reduced-price lunch rate as 43% on October 31, 2025, against a rounded state average of 23%. Free and reduced-price meal counts by year are also in the site's data.
   - citation: Madison School District Annual Report (2026), School Report Card, Tenet #1
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Report text: "As of Oct. 31 2025 2024 2023 2022 2021 2020 / Enrollment 102 110 113 125 127 127 / Free/Reduced Lunch Rate 43% 30% 35% 35% 39% 41% / State Avg. F/R Rate (Rounded) 23% 24% 24% 24% 21% 21%". Free or reduced-price meals use household income up to 185% of the poverty line, a wider group than the ACS poverty measure. Linked from https://www.sau13.org/school-board/annual-reports. Raw: raw/community/school-district/madison-sd-annual-report-2026.pdf (.txt), PDF p. 28
8. The ACS for 2020-2024 estimates 630 Madison residents (±175) enrolled in kindergarten to grade 12, far above the 2020 Census count of 339 residents aged 5 to 17, which shows how uncertain ACS figures are for Madison.
   - citation: ACS 5-year 2020-2024, table S1401 (School Enrollment); 2020 Census DHC table P12
   - source: https://data.census.gov/table/ACSST5Y2024.S1401?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: S1401_C01_003E 630 ±175. The site's database (B14001, ACS 2020-2024) agrees: kindergarten 64 plus grades 1 to 12 sum to 630. The 2020 Census count is in fact 3. Households with children and the share of K–12 students in private school or home school are in the site's Census data; public school counts by town are in the site's data. Raw: raw/community/census/ACSST5Y2024.S1401-madison.json
9. The ACS for 2020-2024 estimates that Madison workers' average commute was 22.2 minutes (±2.3) and that 88.3% (±5.0) drove alone.
   - citation: ACS 5-year 2020-2024, table DP03 (Selected Economic Characteristics), Commuting to Work
   - source: https://data.census.gov/table/ACSDP5Y2024.DP03?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: DP03_0025E 22.2 ±2.3; DP03_0019PE 88.3 ±5.0. The site's database (B08301, ACS 2020-2024) agrees on driving alone: 1,052 (±160) of 1,192 workers, 88.3% (derived). It holds travel-time bands (B08303) but not the mean, so the 22.2 minutes could not be checked there. The share working from home is in the site's Census data. Raw: raw/community/census/ACSDP5Y2024.DP03-madison.json, labels-DP03.json
10. Madison's public school enrollment by grade for students living in Madison, and Madison Elementary's enrollment by grade, are in the site's data (town 333, school 20360).
   - citation: NH Education Facts database, town_enrollment (town 333) and school enrollment
   - source: https://nhfacts.com
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Pointer only, so the Ask uses its own tools. A read-only check on 2026-11-13 showed resident totals for 2014–2026 (320 in 2014, 218 in 2026). The OPD projection (fact 2) is for total population, not children.

## madison_population_census_and_opd: Madison Total Population, Census, OPD Estimate and Projections

- unit: count
- period: 2010 and 2020 Census; OPD projections 2025–2050 (published September 2022); OPD estimate for 2025 (published July 17, 2026); year: 2020–2050
- source: NH Office of Planning and Development, Municipal Population Projections 2020-2050, Table 2 — https://www.nheconomy.com/getmedia/0205c62d-9c30-4b00-9c9e-d81d8f17b8b3/NH-Population-Projections-2020-2050-Final-Report-092022.pdf ; OPD 2025 Population Estimates — https://www.nheconomy.com/getmedia/62b7f54e-dced-456c-9bbf-cac23ea1f7d5/2025-Population-Estimates.pdf
- as_of: 2026-11-13
- raw: raw/community/population/opd-population-projections-2020-2050.pdf (.txt); raw/community/population/opd-2025-population-estimates.pdf (.txt)
- note: Total population only; OPD does not project ages for towns. The 2025 estimate and the 2025 projection are separate OPD products.

| Place | town_id | Year | Value | Note |
|---|---|---|---|---|
| Madison | 333 | 2010 | 2,502 | Census |
| Madison | 333 | 2020 | 2,565 | Census |
| Madison | 333 | 2025 | 2,664 | OPD estimate (July 2026) |
| Madison | 333 | 2025 | 2,677 | OPD projection (2022) |
| Madison | 333 | 2030 | 2,765 | OPD projection |
| Madison | 333 | 2035 | 2,812 | OPD projection |
| Madison | 333 | 2040 | 2,812 | OPD projection |
| Madison | 333 | 2045 | 2,778 | OPD projection |
| Madison | 333 | 2050 | 2,728 | OPD projection |

## madison_children_by_age_census: Madison Residents Under 5 and Ages 5 to 17, 2010 and 2020 Census

- unit: count
- period: 2010 Census (SF1) and 2020 Census (DHC); year: 2020
- source: Census Bureau, table P12 (Sex by Age) — https://data.census.gov/table/DECENNIALDHC2020.P12?g=060XX00US3300345060
- as_of: 2026-11-13
- raw: raw/community/census/DECENNIALDHC2020.P12-madison.json; raw/community/census/DECENNIALSF12010.P12-madison.json
- note: **Derived** sums of the male and female age groups (see town-community-profile fact 3). Share of residents is derived from the total population.

| Place | town_id | Year | Under 5 | Ages 5–17 | Under 18 | Under 18 as share of residents (derived) |
|---|---|---|---|---|---|---|
| Madison | 333 | 2010 | 110 | 390 | 500 | 20.0% |
| Madison | 333 | 2020 | 71 | 339 | 410 | 16.0% |

## madison_resident_births: Births to Madison Residents, From the State's Resident Birth Reports

- unit: count
- period: Calendar years 2020–2024; year: 2024
- source: NH Division of Vital Records Administration, Resident Birth Report, printed in the Town of Madison Annual Reports — https://www.madison-nh.org/ (2020–2024 annual reports)
- as_of: 2026-11-13
- raw: raw/community/town/2020-TOWN-REPORT-WEB.ocr.txt; 2021-Madison-TownReport-web.ocr.txt; 2022-Madison-Town-Report.ocr.txt; 2023-Town-Report-Web.ocr.txt; 0000-2024-Town-Report.ocr.txt
- note: "Total number of records" on each year's Resident Birth Report. Reports were run in early January of the next year. The 2024 report also has a separate "Madison Town Births" report with 1 birth in Madison to a Silver Lake family, not counted here. State vital records sites refused automated access in earlier research, so the counts could not be checked against state data.

| Place | town_id | Year | Value | Note |
|---|---|---|---|---|
| Madison | 333 | 2020 | 6 | 2020 annual report |
| Madison | 333 | 2021 | 8 | 2021 annual report |
| Madison | 333 | 2022 | 12 | 2022 annual report; includes births in Silver Lake and Madison |
| Madison | 333 | 2023 | 5 | 2023 annual report |
| Madison | 333 | 2024 | 7 | 2024 annual report; plus 1 on the separate Town Births report |

## madison_area_income_poverty: Median Household Income and Poverty, Ossipee

- unit: dollars (income); percent (poverty)
- period: ACS 5-year 2020-2024; year: 2024
- source: Census Bureau, ACS 5-year tables B19013 and S1701 — https://data.census.gov/table/ACSDT5Y2024.B19013?g=060XX00US3300358740
- as_of: 2026-11-13
- raw: raw/community/census/ACSDT5Y2024.B19013-ossipee.json; raw/community/census/ACSST5Y2024.S1701-ossipee.json
- note: Ossipee is in the Governor Wentworth Regional School District with five other towns, so its town figures are not in the site's Census data, which covers school districts and the state. Madison, Freedom, Tamworth, Eaton and Conway are each their own school district, so their figures, and New Hampshire's, are in the site's Census data. Margins of error are large for small towns. The site's database (ACS 2020-2024) agrees with these values; it derives the under-18 poverty margin from table B17001 as ±9.2, where S1701 publishes ±12.1.

| Place | town_id | Median household income | Margin | Poverty rate, all ages (%) | Margin | Poverty rate, under 18 (%) | Margin |
|---|---|---|---|---|---|---|---|
| Ossipee | 419 | 90,521 | ±22,451 | 8.1 | ±3.7 | 9.4 | ±12.1 |

## town-housing: Madison's Housing: Seasonal Homes, Owners and Renters, Values, Sales and Rules

- kind: local
- question_type: local_practice
- description: A town's housing beyond the site's Census estimates: home sales and assessments, short-term rentals, workforce housing, and housing plans and studies

1. The 2020 Census counted 1,881 housing units in Madison, 693 of them (36.8%, derived) held for seasonal, recreational or occasional use, and the 2010 Census 1,877 units with 726 seasonal (38.7%, derived).
   - citation: 2020 Census DHC tables H3 and H5; 2010 Census SF1 tables H3 and H5
   - source: https://data.census.gov/table/DECENNIALDHC2020.H5?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: 2020: H3_001N 1881, H3_002N 1132 occupied, H5_006N 693 seasonal. 2010: H003001 1877, H003002 1075 occupied, H005006 726 seasonal. The Census does not report Silver Lake or Eidelweiss separately. The ACS 2020-2024 estimates for Madison (housing units, seasonal share, owner-occupied share, home value and rent) are in the site's Census data; Ossipee's, which are not, are in table madison_area_housing_profile. See table madison_housing_units_occupancy. Raw: raw/community/census/DECENNIALDHC2020.H3-madison.json, DECENNIALDHC2020.H5-madison.json, DECENNIALSF12010.H3-madison.json, DECENNIALSF12010.H5-madison.json
2. Among Madison's year-round households, the 2020 Census counted 993 owners and 139 renters (12.3% renters, derived), against 897 owners and 178 renters (16.6%) in 2010.
   - citation: 2020 Census DHC table H4 and 2010 SF1 table H4 (Tenure)
   - source: https://data.census.gov/table/DECENNIALDHC2020.H4?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: 2020: H4_002N 603 (owned with mortgage) + H4_003N 390 (free and clear) = 993; H4_004N 139 renters. 2010: H004002 577 + H004003 320 = 897; H004004 178. The ACS 2020-2024 owner-occupied share is in the site's Census data. Raw: raw/community/census/DECENNIALDHC2020.H4-madison.json, DECENNIALSF12010.H4-madison.json
3. The ACS for 2020-2024 estimates that 1,763 (±169) of Madison's housing units are single detached houses, 51 (±36) are mobile homes and none (±12) are in buildings with five or more units, and that 1,122 (60.6% of all units, derived) were built between 1970 and 1999.
   - citation: ACS 5-year 2020-2024, table DP04 (Units in Structure; Year Structure Built)
   - source: https://data.census.gov/table/ACSDP5Y2024.DP04?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: DP04_0007E 1763 ±169; DP04_0014E 51 ±36; DP04_0011E–DP04_0013E 0 ±12 each. Built 1970–79: 385 ±121; 1980–89: 546 ±150; 1990–99: 191 ±75 (sum 1,122, derived; 1,122 ÷ 1,851 units = 60.6%). The site's database (tables B25024 and B25034, ACS 2020-2024) agrees. Raw: raw/community/census/ACSDP5Y2024.DP04-madison.json
4. New Hampshire REALTORS® report a median single-family sale price in Madison of $500,000 for January through October 2026 (43 sales), up from $465,000 (48 sales) in the same months of 2025; for the same 2026 period the median was $539,000 in Freedom (23 sales), $427,500 in Ossipee (64) and $535,000 in Conway (115).
   - citation: NH REALTORS®, Local Market Update – October 2026 (Madison, Freedom, Ossipee, Conway)
   - source: https://nhar-public.stats.showingtime.com/docs/lmu/x/Madison?src=page
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Madison report: "Median Sales Price* ... Thru 10-2025 $465,000 Thru 10-2026 $500,000 + 7.5%"; "Closed Sales ... 48 43"; "Current as of November 5, 2026. All data from New Hampshire REALTORS®, Inc. and PrimeMLS". Small sample; the report warns that percent changes "can sometimes look extreme due to small sample size." No report exists for Tamworth or Eaton. See table madison_area_median_sale_price. Raw: raw/community/housing/nhar-lmu-madison-2026-11-13.pdf (.txt), nhar-lmu-freedom-2026-11-13.pdf, nhar-lmu-ossipee-2026-11-13.pdf, nhar-lmu-conway-2026-11-13.pdf
5. Madison voters adopted a zoning amendment on accessory dwelling units (ADUs) on March 10, 2026 by 385 to 168: one ADU is allowed per detached single-family house on a legal lot, up to 950 square feet and two bedrooms, with a building permit and certificate of occupancy, and RVs, campers and mobile homes may not be used as ADUs.
   - citation: Minutes of the Madison Town Meeting, March 10, 2026 Town Election, Article 3 (Zoning Amendment No. 2)
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_Town-Meeting-Minutes_Madison_signed.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes text: "A) One ADU is permitted per detached single-family dwelling, provided the lot is an existing legal lot of record ... H) The maximum size of an ADU shall not exceed 950 sq. ft. area. There shall be no more than two bedrooms in an ADU"; "M) RVS, campers or mobile homes are not allowed for use as an ADU"; result "Yes: 385 No: 168". Voters also adopted a new RV article (358 to 193). Scanned; transcribed from OCR. Raw: raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.pdf (.ocr.txt)
6. Madison's Zoning Board reported that a March 2022 zoning change redefined residential use to exclude stays of 30 days or less, "making STRs [short-term rentals] illegal in Madison"; 13 short-term rental appeals carried into 2024, and the Superior Court reversed a Zoning Board decision that had treated short-term rentals in Eidelweiss as illegal since 1987.
   - citation: Town of Madison 2024 Annual Report, Zoning Board of Adjustment report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "the March 2022 changes to the Zoning Ordinance. This change redefined the residential usage of a dwelling unit to exclude transient usage of 30 days or less, making STRs illegal in Madison. The ZBA decision on case 23-13 which considered short-term rentals in Eidelweiss to be illegal beginning with the enactment of the Zoning Ordinance in 1987 was reversed by the Superior Court"; "The remaining 9 continued short-term rental cases will also be heard in 2025." The town's STR Legal Expense trust held $66,998.59 at the end of 2024 (Trustees of Trust Funds report, p. 147). Outcomes after 2024 were not checked; the 2025 town report is not posted. No count of short-term rentals was found. Scanned; transcribed from OCR. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 119–120
7. Madison is writing a new master plan with North Country Council; in 2025 its steering committee planned a vision survey under RSA 674:3, a student version with the Madison Elementary principal, and a housing section with the Mount Washington Valley Housing Coalition.
   - citation: Madison Master Plan Steering Committee, approved minutes of June 4, 2025; Town of Madison home page (photo request)
   - source: https://www.madison-nh.org/wp-content/uploads/2025/09/June-4-2025-MPSC-approved-minutes.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes text: "In accordance with RSA 674:3, a Master Plan survey will be conducted"; "Student Version: Heather Woodward and Tia Gagnon will collaborate on the student version of the survey to tailor it to different age groups and to involve children (roughly 25% of the population of Madison)"; later minutes list "Evelyn - Housing section, MWVHC". The home page asks for photos "to feature in the plan" via North Country Council (submissions closed November 1, 2026). The town's posted master plan is the 2002 plan with 2010 revisions. Survey results were not found. Raw: raw/community/town/June-4-2025-MPSC-approved-minutes.pdf (.txt); raw/community/town/town-home.txt
8. A Madison owner who rents out a home, short-term or long-term, may be required by state law to file a Landlord's Agent Designated Respondent Affidavit with the Town Clerk, according to the town's website.
   - citation: Town of Madison, home page notice
   - source: https://www.madison-nh.org/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "If you own a home in Madison that you rent out, short-term or long-term, you may be required under State Law to file a Landlord's Agent Designated Respondent Affidavit form with the Town Clerk's Office." Raw: raw/community/town/town-home.txt

## madison_housing_units_occupancy: Madison Housing Units, Seasonal Homes and Tenure

- unit: count
- period: 2010 Census; 2020 Census; year: 2020
- source: Census Bureau tables H3, H4, H5 (2010, 2020) — https://data.census.gov/table/DECENNIALDHC2020.H5?g=060XX00US3300345060
- as_of: 2026-11-13
- raw: raw/community/census/DECENNIALSF12010.H3-madison.json, .H4-, .H5-; DECENNIALDHC2020.H3-madison.json, .H4-, .H5-
- note: Seasonal share is **derived** (seasonal units ÷ all units). The ACS 2020-2024 estimates (housing units, seasonal share, owner-occupied share) are in the site's Census data.

| Place | town_id | Source | Housing units | Occupied | Seasonal | Seasonal share (derived) | Owners | Renters |
|---|---|---|---|---|---|---|---|---|
| Madison | 333 | 2010 Census | 1,877 | 1,075 | 726 | 38.7% | 897 | 178 |
| Madison | 333 | 2020 Census | 1,881 | 1,132 | 693 | 36.8% | 993 | 139 |

## madison_area_housing_profile: Seasonal Homes, Renters, Home Values and Rents, Ossipee

- unit: percent; dollars
- period: ACS 5-year 2020-2024; year: 2024
- source: Census Bureau, ACS 5-year tables DP04 and B25004 — https://data.census.gov/table/ACSDP5Y2024.DP04?g=060XX00US3300358740
- as_of: 2026-11-13
- raw: raw/community/census/ACSDP5Y2024.DP04-ossipee.json; raw/community/census/ACSDT5Y2024.B25004-ossipee.json
- note: Ossipee is in the Governor Wentworth Regional School District with five other towns, so its town figures are not in the site's Census data, which covers school districts and the state. Madison, Freedom, Tamworth, Eaton and Conway are each their own school district, so their figures, and New Hampshire's, are in the site's Census data. Seasonal share is **derived** (B25004_006E 959 ±215 ÷ DP04_0001E 2,749); the site's database gives it as 34.9% ±7.4. The database (ACS 2020-2024) agrees with every value here. Margins are large for small towns.

| Place | town_id | Housing units | Seasonal share (derived) | Renter households (%) | Median home value | Value margin | Median gross rent | Rent margin |
|---|---|---|---|---|---|---|---|---|
| Ossipee | 419 | 2,749 (±207) | 34.9% (±7.4) | 18.0 (±7.1) | $325,500 | ±$23,271 | $1,601 | ±$245 |

## madison_area_median_sale_price: Median Single-Family Sale Price, January–October, Madison and Neighboring Towns

- unit: dollars
- period: Year to date through October 2025 and October 2026; year: 2026
- source: New Hampshire REALTORS®, Local Market Update – October 2026 — https://nhar-public.stats.showingtime.com/docs/lmu/x/Madison?src=page
- as_of: 2026-11-13
- raw: raw/community/housing/nhar-lmu-madison-2026-11-13.pdf; nhar-lmu-freedom-2026-11-13.pdf; nhar-lmu-ossipee-2026-11-13.pdf; nhar-lmu-conway-2026-11-13.pdf (each with .txt)
- note: Single-family homes only; "current as of November 5, 2026". Small numbers of sales make the medians swing. No report was available for Tamworth or Eaton.

| Place | town_id | Median price Jan–Oct 2025 | Sales | Median price Jan–Oct 2026 | Sales |
|---|---|---|---|---|---|
| Madison | 333 | $465,000 | 48 | $500,000 | 43 |
| Freedom | 187 | $475,000 | 22 | $539,000 | 23 |
| Ossipee | 419 | $400,000 | 76 | $427,500 | 64 |
| Conway | 113 | $470,000 | 113 | $535,000 | 115 |

## town-government-and-civic-spaces: How Madison Is Governed and Where Town Meeting, School Sessions and Community Events Are Held

- kind: local
- question_type: governance_money
- description: How a town is governed (select board, town meeting, town offices, village districts, town funding of local programs) and where elections, town meeting, school sessions and community events are held

1. Madison has a town meeting form of government with a five-member Board of Selectmen elected to alternating three-year terms and a Town Administrator; the selectmen meet every other Tuesday in the Town Hall's lower-level meeting room at 1923 Village Road.
   - citation: Town of Madison, Selectmen page; Welcome Packet (March 19, 2025)
   - source: https://www.madison-nh.org/selectmen/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "The Madison Board of Selectmen consists of five elected individuals who serve alternating three-year terms. The Board meets every other Tuesday evening beginning at 5:00 pm in the Town Hall Meeting Room (lower level) unless otherwise noted" (the page also says "every other Tuesday at 4:30"). Welcome packet: "Madison has a 'town meeting' form of government ... the town residents as the legislative body"; its "three elected Selectmen" is out of date, since the same packet lists five selectmen. Raw: raw/community/town/selectmen.txt; raw/community/town/Welcome-Packet-03-19-25.pdf (.ocr.txt)
2. Madison residents elect town officers on the second Tuesday of March and act on the town budget at a business meeting the following Saturday, while the school budget is decided by official ballot under SB2; Madison has about 41 square miles and was incorporated in 1852.
   - citation: Town of Madison Welcome Packet (March 19, 2025), letter from the Board of Selectmen
   - source: https://www.madison-nh.org/wp-content/uploads/2025/03/Welcome-Packet-03-19-25.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Packet text: "Residents vote for elected officials on the second Tuesday of March each year and deliberate and approve the proposed budget on the following Saturday"; "The school budget is voted in its entirety by ballot ('SB2' type of government)"; "The Town of Madison, incorporated in 1852 ... comprises approximately 41 square miles, including the village of Silver Lake." Scanned; transcribed from OCR. Raw: raw/community/town/Welcome-Packet-03-19-25.pdf (.ocr.txt)
3. In 2026 Madison's town and school election was held on March 10 in James Noyes Hall at Madison Elementary School (polls 8:00 a.m. to 7:00 p.m.), and the town meeting reconvened there on Saturday, March 14 to vote on the budget and other articles; 626 ballots were cast on election day and 151 voters took part in the Saturday session, of 2,109 registered voters.
   - citation: Minutes of the Madison Town Meeting, March 10, 2026 Town Election and March 14, 2026 Town Meeting
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_Town-Meeting-Minutes_Madison_signed.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes text: "You are hereby notified to meet at the James Noyes Hall at the Madison Elementary School in Madison on Tuesday, March 10, 2026 at eight o'clock in the forenoon ... to reconvene at nine o'clock in the forenoon of Saturday, March 14, 2026 in the James Noyes Hall at the Madison Elementary School"; "TOTAL VOTES CAST ON ELECTION DAY: 626 TOTAL REGISTERED VOTERS AT END OF ELECTION DAY: 2,109"; "One hundred fifty-one (151) voters signed and received paper ballots"; results "were posted in three places in the entry-way to the gymnasium." The 2024 and 2025 meetings were in the same hall (2024 report p. 12; raw/community/town/2025_Town-Meeting-Minutes_Madison.ocr.txt). The town clerk's election page lists the voting place as "Madison Elementary School James Noyes Hall (Gym) 2069 Village Rd (Rte 113)" (raw/community/town/departments-town-clerk-elections-voting.txt). Raw: raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.pdf (.ocr.txt)
4. The Madison School District's 2026 first (deliberative) session under SB2 was held in the James Noyes Memorial Hall at Madison Elementary School on Monday, February 2, 2026 at 7:00 p.m., and voting by official ballot was held with the town election on March 10, 2026 at the school.
   - citation: Madison School District Annual Report (2026), School Warrant Articles 2026
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Warrant text: "In accordance with SB2 (RSA 40:13), you are hereby notified to meet in the James Noyes Memorial Hall at Madison Elementary School on Route 113 in Madison. The first session for the transaction of all business other than voting by official ballot shall be held on Monday, February 2, 2026 at 7:00 PM"; "Voting on warrant articles 1 through 8 shall be conducted by official ballot and will occur in conjunction with the Town meeting to be held on Tuesday, the 10th day of March 2026 at the Madison Elementary School." Fills the gap in additional-data/district-practices.md (Madison fact 78). Raw: raw/community/school-district/madison-sd-annual-report-2026.pdf (.txt), PDF p. 5
5. Besides elections and meetings, the Madison Elementary gym and grounds host community events: Madison Recreation's Sunday open gyms and a Halloween dance (October 17, 2026), the Old Home Week talent show in James Noyes Hall, the Fire Department's children's Christmas party, the food pantry's 2024 Thanksgiving distribution, and Rec summer camp in the school's classrooms.
   - citation: Town of Madison 2024 Annual Report (Recreation, Fire-Rescue and Food Pantry reports); Madison Recreation website; 2026 Old Home Week schedule
   - source: https://www.madisonrecnh.com/madison-recreation-programs/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Texts: "the return of weekly Open Gyms on Sundays at Madison Elementary School" and "we utilized Burke Field, Silver Lake, and the classrooms at Madison Elementary daily" (2024 report pp. 143–144); "Madison Rec Halloween Dance on Saturday, October 17 at the Madison Elementary School Gym" (Rec site); "Talent Show - James Noyes Hall" (2026 OHW schedule); "We held our third annual children's Christmas Party at the Elementary School" (2024 report p. 113); "This year's food distribution was held at the Madison Elementary School" (p. 139). The school report says a new gym floor gives "a better experience for students, the Recreation Department, and the community" (school report PDF p. 18). Raw: raw/community/recreation/madisonrecnh-madison-recreation-programs.txt; raw/community/town/0000-2024-Town-Report.ocr.txt; raw/community/town/2026-Old-Home-Week-Schedule-Draft-6.txt; raw/community/school-district/madison-sd-annual-report-2026.txt
6. The Silver Lake Association of Madison holds its annual meeting each year on the second Saturday in July at Madison Elementary School, and it sponsors the school's 5th grade Lake Ecology curriculum.
   - citation: Silver Lake Association of Madison (SLAM), welcome letter and brochure in the Town of Madison Welcome Packet (March 19, 2025)
   - source: https://www.madison-nh.org/wp-content/uploads/2025/03/Welcome-Packet-03-19-25.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Text: "our annual meeting which is held each year on the second Saturday in July at 9am at the Madison Elementary School"; brochure: "Sponsors Madison Elementary School's 5th grade Lake Ecology curriculum." The association says it has "over 200 member families." Scanned; transcribed from OCR. Raw: raw/community/town/Welcome-Packet-03-19-25.pdf (.ocr.txt), pp. 16–17
7. Madison TV, the town's public-access channel, records town meetings and community events, and in 2024 it worked with a sound engineer on audio for large meetings held in the school gymnasium.
   - citation: Town of Madison 2024 Annual Report, Madison TV report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "In addition to recording all town meetings and many community activities"; "consulted with sound engineer Dan Parkhurst who advised us on ways to improve the audio quality at large meetings held in the school gymnasium. We used different microphones for February and March town meetings." Videos are on YouTube ("madTV603"). The 2026 PEG TV budget line was $53,800 (2026 minutes, Article 7). Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, p. 134
8. The Village District of Eidelweiss, formed in 1979 in the northeast corner of Madison, is a New Hampshire municipality (not a homeowners' association) governed by three elected commissioners; it maintains 16 miles of road and a public water system, while the Town of Madison handles building permits, police and fire, and the district has no authority over property rentals.
   - citation: Village District of Eidelweiss, District Map and Fact Sheet; Town of Madison Welcome Packet (2025)
   - source: https://vdoe-nh.org/street-map/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "The VDOE is not a homeowner's association. The VDOE is a New Hampshire municipality, called a Village District under New Hampshire law. It is governed by 3 elected Commissioners each serving a 3-year term. The VDOE's primary function is the maintenance of the 16 miles of road and the municipal drinking water system"; "in order to vote at the VDOE annual meeting, Eidelweiss must be your primary residence and you must be a registered voter with the Town of Madison"; "Hook-up to the VDOE municipal water system requires ... an $18,000 fee"; "VDOE has no regulations or authority over any type of property rental within Eidelweiss"; the Eidelweiss Property Owners Association is a separate volunteer group. Commissioners meet Wednesdays at 9:00 a.m., usually at the Madison Town Hall (raw/community/housing/vdoe-home.txt). Raw: raw/community/housing/vdoe-street-map.txt, vdoe-administration.txt
9. Eidelweiss property owners pay Madison's tax rate plus a village district rate: for 2024 the state set Eidelweiss's rate at $5.63 per $1,000 on $137,672,161 of value, about 22.5% of Madison's total valuation of $611,867,353 (derived), on top of Madison's 2024 total rate of $15.77.
   - citation: NH Department of Revenue Administration, 2024 Tax Rate Calculation for Madison, printed in the Town of Madison 2024 Annual Report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "Village Tax Rate Calculation ... Eidelweiss Village $775,094 $137,672,161 $5.63"; "Total Assessment Valuation with Utilities $611,867,353"; "Total 2024 Tax Rate $15.77." Share derived: 137,672,161 ÷ 611,867,353 = 22.5%. Madison revalued in 2025. Madison's DRA rates and valuations for 2014–2025 are in the site's data (property_tax, Madison district), and its 2024 rate and valuation match these (checked November 15, 2026); village district rates are not. The 2025 Eidelweiss rate was not checked here; the money file's district-tax-and-state-aid fact 2 gives $3.27 from the town's tax rate history. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 70–72

## town-history-and-heritage: The Madison Boulder, the Madison Corner School and the Historical Society

- kind: local
- question_type: local_practice
- description: Local history resources for families and schools: historical societies, museums, historic school buildings and natural landmarks

1. The Madison Boulder Natural Area, a 17-acre state park at 473 Boulder Road, holds a granite glacial erratic 83 feet long, 37 feet wide and 23 feet high above the ground that weighs more than 5,000 tons; the state acquired the site in 1946, and the U.S. Department of the Interior named the boulder a National Natural Landmark in 1970.
   - citation: NH State Parks, Madison Boulder Natural Area
   - source: https://www.nhstateparks.org/visit/state-parks/madison-boulder-natural-area
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "Madison Boulder Natural Area is home to one of the largest glacial erratic boulders in North America. Madison Boulder is a huge granite rock measuring 83 feet in length, 23 feet in height above the ground, 37 feet in width, and weighs upwards of 5,000 tons! The 17-acre site was acquired by the state of N.H. in 1946. In 1970 Madison Boulder was designated a National Natural Landmark"; "deposited ... around 14,000 years ago"; "always open for recreation." **Derived:** 3.9 road miles and about 13 minutes by car from Madison Elementary School (OSRM, raw/community/distances/osrm-routes-from-mes-2026-11-13.json). Raw: raw/community/history/nhstateparks.org-visit-state-parks-madison-boulder-natural-area.html (.txt)
2. The Madison Corner School, which stands in front of Madison Elementary School, was one of nine one-room schoolhouses in Madison; it was built in 1835 on Route 113, moved in 1873 to land given by James J. Burke (today's school property) and moved again in 1979, and it is on the National Register of Historic Places (1980) and the State Register (2006).
   - citation: Madison Historical Society, Madison Corner School page
   - source: https://www.madisonnhhistoricalsociety.org/madison-corner-school.html
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "The Madison Corner School was one of nine one room schoolhouses in Madison. It was built in 1835 on Rt. 113 across from Mooney Hill Road. It was first moved in 1873 to property given by James J. Burke which is the current school property ... In 1979 the building was moved to its current location in front of the Madison Elementary School"; "accepted onto the National Register of Historic Places in 1980 and the New Hampshire State Register of Historic places in 2006." Raw: raw/community/history/mhs-madison-corner-school.html (.txt)
3. The Madison Corner School served as a one-room school for grades 1 to 12 (its 1860 registry lists 25 boys and 28 girls aged 4 to 18); Madison High School was built in 1922 and closed in 1949, and from 1950 Madison sent high school students to Kennett in Conway, while the Corner School served as the town and school library until 1994 and 2000.
   - citation: Madison Historical Society, Madison Corner School page; Madison School District Annual Report (2026), Madison Corner School Preservation Committee Report 2025
   - source: https://www.madisonnhhistoricalsociety.org/madison-corner-school.html
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "The Madison Corner School served as a 1st - 12th grade one room school. The 1860 school registry lists 25 boys and 28 girls ranging in age from 4-18"; "In 1922 the Madison High School was built. It closed in 1949"; "The Madison Corner School served elementary students until 1950 when Madison began sending high school students to Kennett in Conway and all elementary students moved to the old high school building"; "served as the Town and School Library until the town library was built in 1994 and the elementary school library in 2000." The committee report: "Built in 1835, it served as a school for 114 years and then as town and school library for 49 years." Raw: raw/community/history/mhs-madison-corner-school.txt; raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 36
4. Madison School District voters have placed $25,000 a year in a Madison Corner Schoolhouse Capital Reserve Fund three times, in March 2024 (308 to 126), March 2025 (354 to 223) and March 2026 (380 to 206), and a volunteer preservation committee had raised $14,261.61 in private donations by December 31, 2025.
   - citation: Madison Historical Society, Madison Corner School page; Madison School District 2026 ballot results (March 10, 2026), Article 6
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_SCHOOL-BALLOT_RESULTS_03_10_2026-2.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page text: "Mar 2024 The Madison School District voted 308 to 126 in favor of raising & appropriating $25,000"; "Mar 2025 Madison School District voted 354 to 223 to raise & appropriate another $25,000"; "AS OF 12/31/25 THE COMMITTEE HAS RAISED $14,261.61 THROUGH PRIVATE DONATIONS & FUNDRAISERS." Ballot: "ARTICLE 6 ... $25,000 ... Madison Corner Schoolhouse Capital Reserve Fund ... (The current Madison Corner Schoolhouse CRF balance excluding interest earned from 6/30/25 is $50,394.37.) ... 380 YES 206". Capital planning details are in the money file. Raw: raw/community/history/mhs-madison-corner-school.txt; raw/community/school-district/2026_SCHOOL-BALLOT_RESULTS_03_10_2026-2.pdf (.ocr.txt)
5. The Corner School was named to the NH Preservation Alliance's "Seven to Save" list in October 2025; its committee held open houses in August and September 2025 with more than 100 visitors, opened the building again during Old Home Week on August 1, 2026, and partners with the Madison Historical Society to accept donations.
   - citation: Madison School District Annual Report (2026), Madison Corner School Preservation Committee Report 2025; 2026 Old Home Week schedule
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "In October, the Corner School was added to the prestigious New Hampshire Preservation Alliance's (NHPA) Seven to Save list"; "The committee held two successful open houses (August and September) welcoming over 100 visitors"; "the Committee was invited by NHPA to apply for a matching grant towards a Building Assessment Plan where we were successful in securing a request for $4,250" (the Historical Society page says "awarded $4200"); a $23,000 LCHIP grant was not awarded in 2025. OHW schedule: "Madison Corner School Open House ... Step inside this one room schoolhouse and imagine a class of 35 children ages 5 – 21." Raw: raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 36; raw/community/town/2026-Old-Home-Week-Schedule-Draft-6.txt
6. The Madison Historical Society, organized in 1958, runs a museum in the town's 1884 Town House at 19 East Madison Road, with summer exhibits, "Listening by the Lake" concerts and house tours; in 2024 it used space at the elementary school "where students can learn about their town's history," and during Old Home Week 2026 it offered weekday heritage activities.
   - citation: Madison Historical Society, About and Programs pages; Town of Madison 2024 Annual Report, Historical Society report; 2026 Old Home Week schedule
   - source: https://www.madisonnhhistoricalsociety.org/programs.html
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: About page: "The Madison Historical Society was first organized on September 3, 1958"; "1884 - A Town House was built by Nathaniel Nason." 2024 report: "We were pleased to be able to use space at the elementary school where students can learn about their town's history" and the summer exhibit "TIMELINE OF MADISON." OHW 2026: "Museum will be open to tour Sun. through Fri., 10-1 ... Heritage Activities Mon. through Fri. including Vintage Band Instruments, Old Tools, Laundry Day, Homemade Essentials and Cooking with Wood." The town owns the building; the Historical Society Building Improvement trust held $31,092.84 at the end of 2024. Raw: raw/community/history/mhs-about.txt, mhs-programs.txt, mhs-exhibits.txt; raw/community/town/0000-2024-Town-Report.ocr.txt, p. 130; raw/community/town/2026-Old-Home-Week-Schedule-Draft-6.txt
7. The Madison Library keeps a local history collection, and in 2024 the Friends of Madison Library offered talks including "From Ancient Rome to the Silver Lake Lead Mine: Rethinking History" and a NH Humanities program co-sponsored with the Historical Society.
   - citation: Town of Madison 2024 Annual Report, Madison Library report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "a bountiful local history collection"; "'From Ancient Rome to the Silver Lake Lead Mine: Rethinking History,' presentation by Ann and David Wilkins"; "'Granite State Stories: Benjamin Champney, Mount Washington, and Concord Coach,' a New Hampshire Humanities presentation ... co-sponsored with the Madison Historical Society." No local source on Silver Lake's railroad era was found. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 121–124
8. Madison's 124th annual Old Home Week ran August 1 to 9, 2026, with events at Burke Field, the Foot of the Lake beach on Silver Lake, the Historical Society museum and James Noyes Hall.
   - citation: Town of Madison, 2026 Old Home Week Schedule (draft 6)
   - source: https://www.madison-nh.org/wp-content/uploads/2026/07/2026-Schedule-Draft-6.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Schedule text: "124th Annual Madison Old Home Week August 1st—9th, 2026"; events include "Community Fair -Burke Field", "Pancake Breakfast - Foot of Silver Lake", "Talent Show - James Noyes Hall", "Fireworks Display—Burke Field." The Old Home Week invitation is attributed to the Historical Society (raw/community/town/boards-old-home-week.txt). Raw: raw/community/town/2026-Old-Home-Week-Schedule-Draft-6.pdf (.txt)

## town-recreation-and-summer: Madison Recreation, Summer Camp, the Library and Local Enrichment

- kind: local
- question_type: help
- description: Town recreation, after-school and summer programs, youth sports and camps, and their costs and scholarships

1. Madison Recreation, a town department with a part-time Recreation Director and a volunteer Recreation Committee set up in 2022, lists fall soccer, field hockey and flag football (with Freedom), weekly open gym (November–February), monthly teen nights, winter basketball, a chess club (February–June), spring softball and T-ball, and a summer camp (June–August).
   - citation: Madison Recreation, Programs and About pages
   - source: https://www.madisonrecnh.com/madison-recreation-programs/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Programs table: "Fall Soccer September – October; Open Gym November – February, Weekly; Teen Night Open Gym November – February, Monthly; Winter Basketball December – February; Chess Club February – June; Spring Softball May – June; Spring T-Ball May – June; Summer Recreation Camp June – August; Fall Field Hockey ...; Fall Flag Football." About: "The committee was established in 2022"; it "meets monthly on the first Thursday of each month at the Madison Town Hall lower level meeting room." The 2024 payroll lists a "PT Recreation Director" (2024 report pp. 83–84). Raw: raw/community/recreation/madisonrecnh-madison-recreation-programs.txt, madisonrecnh-about-madison-nh-rec.txt
2. For winter 2026-27, Madison Recreation basketball practices run Tuesdays and Thursdays 3:30–4:30 p.m. for grades 1–3, Wednesdays and Fridays 5:15–6:45 p.m. for girls in grades 4–6 and Tuesdays and Thursdays 5:00–6:30 p.m. for boys in grades 4–6, with registration through a new RecDesk system.
   - citation: Madison Recreation, home page (updated November 3, 2026)
   - source: https://www.madisonrecnh.com/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "Madison Recreation is opening up registration for Basketball this winter for kids in grades 1–6. Girls Basketball grades 4-6 will practice Wednesday & Fridays from 5:15-6:45, Boys Basketball grades 4-6 will practice Tuesdays & Thursday 5:00-6:30 and Basketball for all kids grades 1-3 will practice Tuesdays and Thursdays 3:30-4:30"; "transitioning to a NEW registration and payment system called RecDesk." Where practices are held is not stated. Raw: raw/community/recreation/madisonrecnh-home.txt
3. Madison Recreation's 2026 summer camp cost $700 for eight weeks or $100 a week, with field trips and bus transportation arranged through Eldridge.
   - citation: Town of Madison Recreation Committee minutes, February 19 and June 8, 2026
   - source: https://www.madison-nh.org/wp-content/uploads/2026/05/Rec-2-19-26.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes text (February 19): "Summer Camp: Heather said registration is open for Summer Camp. The cost of summer camp is $700 for 8 weeks or $100 a week. The field trips are mostly the same with a couple changes." June 8: "Summer Camp: All set with bussing through Eldridge. We will try to keep the pricing low"; a committee member said to tell him "if there are any kids that are struggling to cover the cost of the field trips." Camp dates and daily hours were not found. Scanned; transcribed from OCR. Raw: raw/community/recreation/Rec-2-19-26.pdf (.ocr.txt), REC-6-8-26.pdf (.ocr.txt)
4. In 2024 Madison Recreation's summer camp had more than 60 campers registered and 28 to 35 a day, used Burke Field, Silver Lake beaches and Madison Elementary classrooms, was staffed by eight counselors including current and former Madison Elementary teachers and paraprofessionals, and was open to Madison residents including home-schooled students.
   - citation: Town of Madison 2024 Annual Report, Madison Recreation Year in Review
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "Our Summer Camp Program grew tremendously this year for the residents of Madison, including students of Madison Elementary and any home school students that wished to participate. With a total registration of over 60 campers, and attendance numbers between 28-35 kids on a daily basis"; "We had 8 counselors ... all current and former teachers and paraprofessionals from Madison Elementary School"; "We also added a Counselors-in-Training (CIT) program ... Madison students entering 8th Grade"; swim lessons were taught at the Foot of the Lake beach. Scanned; transcribed from OCR. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 141–145
5. Since spring 2024 Madison Recreation has charged sports participation fees of $35 per sport for Madison residents and $45 for non-residents; in 2024 its programs and fundraising brought in about $32,000, including $23,200 for summer camp, of which $5,950 came from the Ossipee Children's Fund.
   - citation: Town of Madison 2024 Annual Report, Madison Recreation report (financials)
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "In the spring, Madison Rec began accepting sports participation fees to continue our goal of being self-sustaining: $35 per sport for Madison residents, and $45 for non-resident players"; "In total, Madison Recreation brought in approximately $32,000 ... $23,200 for Summer Camp"; table row "Summer Camp $5,300.00 $5,950.00 $11,950.00 $23,200.00" under "Cash & Check / Ossipee Children's Fund / Square / Gross Revenue." The Ossipee Children's Fund has since announced its closure (town-family-help fact 9). Whether 2026 fees changed was not found. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 141–142
6. Madison voters approved $77,190 for the town's Recreation Program in 2026, up from $69,390 approved for 2025 (of which $68,804.20 was spent), plus $19,201 for parks and recreation upkeep in the Public Works budget.
   - citation: Minutes of the Madison Town Meeting, March 14, 2026, Articles 7 and 8
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_Town-Meeting-Minutes_Madison_signed.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes table rows: "Rec Program 69,390.00 $ 68,804.20 $ 77,190.00" (2025 approved, 2025 expended, 2026 proposed; passed as amended for other lines) and "Parks & Rec $ 20,050.00 14,255.03 $ 19,201.00" (Public Works). Library: $119,838 for 2026. Raw: raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.ocr.txt, pp. 10–12
7. The Madison Library at 1895 Village Road held 339 programs in 2024, including weekly story times, children's book groups, seven weeks of summer reading and a "1000 books before Kindergarten" program; library cards are free to Madison residents, seasonal property owners and Madison School District employees.
   - citation: Town of Madison 2024 Annual Report, Madison Library report; Madison Library website (hours)
   - source: https://madisonlibrary-nh.org/WP/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "The Madison Library held 339 programs in 2024, with a total attendance of 2,385. Recurring programs included monthly book group discussions for adults, and kids, weekly story times"; "1000 books before Kindergarten program for children 5 and under"; "All Madison residents and seasonal property owners may receive a library card for no fee. In addition, employees of the Town of Madison, the Madison School District, and businesses in Madison"; a shared catalog with Tamworth, Jackson, Conway and Ossipee libraries. Hours (website): "Mon 9-5 | Tues 12-5 | Wed 2-6 | Thurs 2-6 | Fri 9-5 | Sat 9-1". Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 121–124; raw/community/library/library-home.txt
8. Other enrichment providers with Madison addresses on the EFA marketplace include HomeSweet HomeSchool on Village Road (tutoring, small groups and clubs for homeschooling families), Windcroft Stables (riding and pony-driving lessons and summer programs in horsemanship, farming and wilderness) and Rockin' Fitness (fitness classes tagged for after-school programs).
   - citation: CSF New Hampshire EFA marketplace feed (provider ids 12116, 2797, 14786)
   - source: https://app.nh.scholarshipfund.org/marketplace
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Feed descriptions: HomeSweet HomeSchool, "We specialize in individual tutoring ... In addition, we host small group activities ... Our diverse selection of clubs and enrichment programs"; Windcroft Stables, "Horseback riding lessons, pony driving lessons, summer programs including horsemanship, farming and wilderness"; Rockin' Fitness, tags include "Afterschool programs." Listing shows CSF approval, not price, schedule or quality; families without an EFA can also pay these providers directly where they accept it (not stated in the feed). Raw: raw/community/efa/efa-marketplace-vendors-2026-11-13.json; efa-providers-near-madison-2026-11-13.csv
9. No town-run daily after-school care was found in Madison: Madison Recreation's program list has sports, open gym, chess club, teen nights and summer camp but no daily after-school program; the nearest licensed school-age care is at Family Child Care of Madison and at programs in Conway, Tamworth and North Conway.
   - citation: Madison Recreation, Programs page; NH Child Care Search provider list (NH DHHS); Madison School District Annual Report (2026), school report card
   - source: https://www.madisonrecnh.com/madison-recreation-programs/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Documented absence: the Rec program table, 2026 Rec minutes and town pages list no daily after-school care. The school's report card lists "Before and After School Care Enrichment Programs" among school activities (raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 30); hours and fees are in the school-day file (agent 2). Whether any licensed program picks up at Madison Elementary is not stated in the DHHS data. The programs' ages and weekday hours are in the site's data (child_care); drive times are in table madison_area_child_care_drive_distance. Raw: raw/community/recreation/madisonrecnh-madison-recreation-programs.txt; raw/community/childcare/childcare-providers-madison-area-2026-11-13.csv

## town-child-care: Licensed Child Care in and Near Madison

- kind: local
- question_type: help
- description: Child care for a town beyond the site's child care data: where the nearest licensed programs are, drive times, Head Start, costs programs post, waitlists and local child care efforts

1. Madison Preschool, a licensed group program that NH DHHS's Child Care Search lists at 53 Conway Road in Madison, is at The Madison Church.
   - citation: NH Child Care Search (NH DHHS), provider list download; OpenStreetMap Nominatim (geocode)
   - source: https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Downloaded with the page's "fetchProviderList" function (735 providers statewide). 53 Conway Road geocodes to The Madison Church (raw/community/distances/nominatim-madison-preschool.json); the food pantry's 2024 report thanks the "Madison Church Pre-School." Madison's two licensed programs (Madison Preschool and Family Child Care of Madison), with their places, ages and openings, are in the site's data (child_care), so they are not repeated. Rewritten November 14, 2026: the earlier statement called Madison Preschool "marked inactive", reading Provider_Enrollment_Status_Formula__c ("Inactive"), which is about NH Child Care Scholarship enrollment; DHHS lists its license as active. Raw: raw/community/childcare/nhccis-provider-list-2026-11-13.json; childcare-providers-madison-area-2026-11-13.csv
2. The SAU 13 public preschool at Madison Elementary School, for 3- and 4-year-olds from Freedom, Madison and Tamworth, is a public school program and does not appear in the DHHS child care list; it had 18 children in 2025-26 (8 from Madison).
   - citation: Madison School District Annual Report (2026), principal's report; additional-data/district-practices.md (SAU 13 preschool)
   - source: https://www.sau13.org/preschool
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Report text: "For the 2025–2026 school year, the program continues to serve 18 students, with 8 from Madison, 7 from Tamworth, and 3 from Freedom." Eligibility, sessions and daily tuition are in district-practices.md (Madison fact 61) and the Madison Elementary file. No DHHS record names the SAU 13 preschool. Raw: raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 19
3. **Derived:** six licensed programs that take infants are within about 25 minutes of Madison Elementary School by car: Family Child Care of Madison (5 minutes), Children Unlimited (13), Explorations for the Young Child (15), Small Connections (16) and Tamworth Village Homeschool (16) in Conway and Tamworth, and The Lilliputian School in North Conway (24); Vaughan Learning Center and Wildflowers in North Conway are about 26 and 27 minutes away.
   - citation: NH Child Care Search provider list (NH DHHS); OSRM driving routes from Madison Elementary School (derived)
   - source: https://router.project-osrm.org/route/v1/driving/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Derived. Origin: Madison Elementary School (OpenStreetMap way 1216044221; 43.8982398, -71.1530970) from Nominatim. Program addresses geocoded with OpenStreetMap Nominatim (identifier nhfacts-research, contact webmaster@nhfacts.com) and routed with the public OSRM "driving" profile: a car with no traffic, snow or stops. The Lilliputian School geocoded only to the street. Two Center Conway programs (Adventures In Learning, Little Hands, Big Dreams) could not be geocoded. The programs' places and ages are in the site's data. See table madison_area_child_care_drive_distance. Raw: raw/community/distances/nominatim-*.json; osrm-routes-from-mes-2026-11-13.json; raw/community/childcare/childcare-providers-madison-area-2026-11-13.csv
4. **Derived:** Tamworth Preschool and Children's Center in Tamworth (formerly Bearcamp Valley School and Children's Center) is about 20 minutes by car from Madison Elementary School, and Ossipee Concerned Citizens Child Care Center in Center Ossipee about 25 minutes; the Ossipee center is the only program near Madison that NH DHHS's Child Care Search rates "Licensed Plus."
   - citation: NH Child Care Search provider list (NH DHHS); OSRM routes (derived)
   - source: https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Records: "Tamworth Preschool and Children's Center", 27 Durrell Road; "Ossipee Concerned Citizens Child Care Center", 3 Dore Street, QRIS_Rating__c "Licensed Plus"; every other program in table madison_area_child_care_drive_distance shows "Licensed". The Tamworth Community Nurse Association lists 27 Durrell Road as "Bearcamp Valley School & Children's Center" (raw/community/private-schools/tamworthnurses.org-schools-childcare.txt); the center's renaming is in the Tamworth file (town-child-care 1). Both programs' places and ages are in the site's data. Drive times: 19.6 and 25.0 minutes (OSRM). Raw: raw/community/childcare/childcare-providers-madison-area-2026-11-13.csv; raw/community/distances/osrm-routes-from-mes-2026-11-13.json
5. No child care program in or near Madison publishes how long its waitlist is on the pages found, so public sources cannot say how early families need to apply for infant or toddler care.
   - citation: Provider websites (documented absence); NH Child Care Search (fields shown)
   - source: https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: NH DHHS's Child Care Search shows each program's wait-list status and reported openings, which are in the site's data (child_care), but not wait lengths; the provider download read on November 13 had no such fields. The Lilliputian School's site has no waitlist statement; the Children Unlimited, Vaughan, Bearcamp Valley and Ossipee Concerned Citizens sites tried did not respond. The Bartlett and Jackson research also found no published infant waitlist (town/Bartlett/daily-life-and-community.md, town-child-care fact 3). Child Care Aware of NH gives referrals (library topic child-care-aware-nh). Raw: raw/community/childcare/nhccis-provider-list-2026-11-13.json
6. Tamworth Village Homeschool at 101 Main Street in Tamworth, a licensed group program, describes itself as offering preschool for ages 3 to 5, homeschool enrichment for ages 6 to 10 and a hybrid homeschool class for ages 5 and 6, two, three or five days a week.
   - citation: Tamworth Village Homeschool website; NH Child Care Search provider list
   - source: https://www.tamworthvillagehomeschool.com/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Site text: "We offer small and friendly home-based programs: Preschool for children ages 3 to 5; Homeschool enrichment programs for children from ages 6-10; Hybrid Homeschool K1 Class"; "Enrollment Options: Two Day Three Day or Five Day." Its places and ages as listed with NH DHHS are in the site's data (child_care). It is also on the EFA marketplace (provider 3843). Prices are not posted. **Derived:** 6.8 road miles, about 16 minutes from Madison Elementary. Raw: raw/community/private-schools/tamworthvillagehomeschool.com.html (.txt); raw/community/childcare/childcare-providers-madison-area-2026-11-13.csv
7. At the March 2026 town meeting, Madison voters gave $5,771 to Tri-County Community Action Program for services in Madison that include Head Start; Tri-County CAP runs Head Start centers in Tamworth and Conway.
   - citation: Minutes of the Madison Town Meeting, March 14, 2026, Article 26; Tri-County CAP, Head Start (Jackson file, town-child-care 3)
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_Town-Meeting-Minutes_Madison_signed.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: NH DHHS's Child Care Search lists Tamworth Area Head Start (448 White Mountain Highway) and Conway Head Start (73 Main Street) with active licenses; their places are in the site's data. Rewritten November 14, 2026: the earlier statement said DHHS "marks both inactive", reading the scholarship-enrollment field (Provider_Enrollment_Status_Formula__c), which is about NH Child Care Scholarship enrollment, not the program or its license. Minutes: "Tri-County Community Action Program, Inc. services in Madison include Fuel and Energy Assistance, Transportation Services, Community Action Resource Coordinators, the Free Diaper Distribution Program, Tamworth Dental Services, Head Start and USDA TEFAP Food Distribution pantries." Tri-County CAP's Head Start rules and its Conway center are in the Jackson file (town-child-care 3 in `Jackson/community-and-families.md`) and library topic head-start-eligibility. Raw: raw/community/childcare/childcare-providers-madison-area-2026-11-13.csv; raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.ocr.txt, p. 18

## madison_area_child_care_drive_distance: Road Distance From Madison Elementary to Licensed Child Care (derived)

- unit: number (miles; minutes)
- period: Programs as listed in NH DHHS data downloaded November 13, 2026; routes computed November 13, 2026; year: 2027
- source: NH Child Care Search (NH DHHS), provider list download — https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch ; OSRM public router — https://router.project-osrm.org/
- as_of: 2026-11-13
- raw: raw/community/childcare/childcare-providers-madison-area-2026-11-13.csv (from nhccis-provider-list-2026-11-13.json); raw/community/distances/osrm-routes-from-mes-2026-11-13.json; raw/community/distances/nominatim-*.json
- note: Licensed programs whose address is in Madison, Conway villages, Tamworth, Ossipee, Effingham or Sandwich. Their places, ages, openings and hours are in the site's data (child_care), so they are not repeated. Miles and minutes are **derived**: fastest OSRM car route from Madison Elementary School in normal conditions (no snow or traffic). "Street only" means the address geocoded only to the street. Not in the table: Adventures In Learning and Little Hands, Big Dreams (Center Conway), which could not be geocoded, and Little Busy Bodies Educational Child Care (Center Conway), Conway Head Start and Tamworth Area Head Start, which were not routed. Until November 14, 2026 this table had another name and also listed capacity, ages and a "Status" column that read DHHS's scholarship-enrollment field as active or inactive.

| Program | Town | Road miles (derived) | Minutes (derived) | Note |
|---|---|---|---|---|
| Madison Preschool | Madison | 0.6 | 2 | At The Madison Church, 53 Conway Road |
| Family Child Care of Madison | Madison | 1.6 | 5 | Licensed family program |
| Children Unlimited | Conway | 6.3 | 13 | |
| Explorations for the Young Child | Conway | 7.0 | 15 | |
| Small Connections | Conway | 7.4 | 16 | |
| Tamworth Village Homeschool | Tamworth | 6.8 | 16 | Also EFA provider |
| Tamworth Preschool and Children's Center | Tamworth | 8.4 | 20 | 27 Durrell Road |
| The Lilliputian School - White Mountain Highway Campus | North Conway | 11.3 | 24 | Street only |
| Ossipee Concerned Citizens Child Care Center | Center Ossipee | 12.5 | 25 | Rated "Licensed Plus" |
| Vaughan Learning Center | North Conway | 12.3 | 26 | |
| Wildflowers Early Learning Center | North Conway | 12.6 | 27 | |
| JJ's Playland | Effingham | 13.0 | 30 | Street only |
| Sandwich Children's Center | Center Sandwich | 20.8 | 37 | |

## town-school-options-nearby: Private, Charter, Homeschool and EFA Options Within About 25 Minutes of Madison

- kind: local
- question_type: help
- description: Private, charter and other schools families in a town use, with distance and tuition, and EFA use

1. The federal Private School Universe Survey (PSS) lists nine private schools within 25 miles (straight line) of Madison's ZIP code, 03849, for 2023-24, none of them in Madison, Conway or Tamworth: Fryeburg Academy (654 students, grades 9–12), New Life Christian Academy (27, grades 1–11) and Summit Achievement (11, grades 10–12) in or near Fryeburg, Maine; Shepherds River Mennonite School in Brownfield, Maine (30, grades 1–10); Cornerstone Christian Academy in Ossipee (74, PK–8); and four farther away.
   - citation: NCES Search for Private Schools, ZIP 03849 within 25 miles (PSS 2023-24)
   - source: https://nces.ed.gov/surveys/pss/privateschoolsearch/school_list.asp?Search=1&Zip=03849&Miles=25&NumOfStudentsRange=more&IncGrade=-1&LoGrade=-1&HiGrade=-1
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "Search Results: 9"; "Source: PSS Private School Universe Survey data for the 2023-24 school year." The other four: Waterville Valley Academy (22, grades 9–12), Bridge Crossing Academy and NFI North Bridge Crossing Academy in Bridgton, Maine (14 each, grades 2–7) and Maplestone in Acton, Maine (24, grades 7–12). PSS misses schools that did not respond, and the NH DOE nonpublic school list could not be opened (Not retrieved). Raw: raw/community/private-schools/nces-pss-03849-25mi.html (.txt)
2. **Derived:** no private school with full-time students is within 25 minutes of Madison Elementary School by car; the nearest are New Life Christian Academy (15.1 miles, about 32 minutes), Cornerstone Christian Academy in Ossipee (18.5 miles, 33 minutes) and Fryeburg Academy (15.7 miles, 34 minutes), and Brewster Academy in Wolfeboro is about 47 minutes away.
   - citation: OSRM driving routes from Madison Elementary School (derived); school addresses from NCES PSS and the EFA marketplace
   - source: https://router.project-osrm.org/route/v1/driving/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Derived, same method as town-child-care fact 3: origin Madison Elementary (43.8982398, -71.1530970); destinations geocoded with Nominatim (identifier nhfacts-research) except Cornerstone, which Nominatim placed only on "Old Route 28" and which uses the EFA feed's coordinates (43.681071, -71.115862). Normal conditions; winter driving and the Route 16/113 roads in snow are not modeled. Fryeburg Academy's commuter day tuition ($22,500 for 2027-28) and other schools' tuition are in the Jackson file (town-school-options-nearby 1–10; district-fees 1 in `Jackson/community-and-families.md`). See table madison_area_school_options_drive. Raw: raw/community/distances/osrm-routes-from-mes-2026-11-13.json; nominatim-new-life-christian.json, nominatim-fryeburg-academy.json, nominatim-brewster.json
3. Within 25 minutes, the EFA marketplace lists homeschool and early-childhood programs rather than full-time schools: HomeSweet HomeSchool in Madison (about 3 minutes), Tamworth Village Homeschool (16), Tamworth Learning Circles (21, listed as a "school" with no description) and The Lilliputian School in North Conway (24, a nonprofit Montessori-inspired early childhood center) (derived drive times).
   - citation: CSF New Hampshire EFA marketplace feed (provider ids 12116, 3843, 13886, 21176); OSRM routes (derived)
   - source: https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Feed descriptions: HomeSweet HomeSchool, "a nurturing, community-focused educational program ... Designed to support homeschooling families" with tags "K-5; 6-8; Certified Teachers"; The Lilliputian School, "a nonprofit early childhood education center ... Montessori-inspired, nature-based program" (grades 0–7 in the feed). Tamworth Village Homeschool's own site: town-child-care fact 6. Drive minutes: 3.3, 16.1, 21.3, 23.5 (Lilliputian street-level). Listing shows CSF approval, not price, quality or openings. Raw: raw/community/efa/efa-marketplace-vendors-2026-11-13.json; efa-providers-near-madison-2026-11-13.csv; raw/community/distances/osrm-routes-from-mes-2026-11-13.json
4. The EFA marketplace marks no provider as a micro-school: its "is_microschool" flag was false for all 3,608 entries statewide on November 13, 2026, so the feed cannot identify micro-schools near Madison; nearby programs describe themselves as homeschool programs, co-ops or tutoring.
   - citation: CSF New Hampshire EFA marketplace feed (field is_microschool)
   - source: https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Derived count: 0 of 3,608 records with "is_microschool": true. The CSF handbook lets EFA money pay for "Co-op / Microschool classes" (Conway file, town-school-options-nearby fact 29). Nearby co-op-style programs include We Can Be Heroes in Tamworth (a role-playing program for ages 9–15) and The Aletheia School in Wolfeboro (a homeschool learning and resource center for grades 7–12, about 47 minutes away). **Premise check (P19.1):** no micro-school is flagged. Raw: raw/community/efa/efa-marketplace-vendors-2026-11-13.json
5. **Derived:** on November 13, 2026 the EFA marketplace listed 3 entries in Madison, 7 in Tamworth (including Chocorua and South Tamworth), 7 in Ossipee (including Center Ossipee), 1 in Freedom and 1 in Eaton, adding to the 31 Mount Washington Valley entries counted in the Conway and Bartlett research.
   - citation: CSF EFA marketplace feed, filtered by city (derived)
   - source: https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Derived by the feed's city field. A "Madison, NH" entry with a North Carolina ZIP (House of Humane Letters, 27025) was dropped, as Conway and Bartlett did. Cornerstone Christian Academy appears twice in Ossipee. Tamworth Village Homeschool's feed coordinates are wrong (a far-away point), so straight-line counts miss it. The full list within 25 straight-line miles (92 rows) is in the CSV. See table madison_area_efa_marketplace_by_town. Raw: raw/community/efa/efa-marketplace-vendors-2026-11-13.json; efa-providers-near-madison-2026-11-13.csv
6. Two tuition-free public charter schools are in Conway: Robert Frost Charter School at 110 Main Street (K–12, about 14 minutes from Madison Elementary by car, derived) and Northeast Woodland Chartered Public School on Technology Lane (K–8, not routed); EFA money cannot be used by a student enrolled full time in a charter school.
   - citation: Conway file, town-school-options-nearby facts 1–23; OSRM route (derived)
   - source: https://router.project-osrm.org/route/v1/driving/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Pointer for the charter schools' admission, lotteries and transportation (town/Conway/community-and-choice.md). Robert Frost: 6.9 miles, 14.3 minutes (OSRM). Northeast Woodland's address could not be geocoded in OpenStreetMap, as in the Jackson research. Each charter says students from other districts arrange their own transportation (Conway file facts 12 and 19). Raw: raw/community/distances/osrm-routes-from-mes-2026-11-13.json; nominatim-robert-frost.json
7. The CSF public statistics feed showed 11 Madison students eligible for an Education Freedom Account for 2026-27 on November 13, 2026, all in a priority group, with 11 counted in its income field, 3 with special needs and none on the waitlist; NH Department of Education EFA counts by town are in the site's data.
   - citation: CSF NH EFA statistics feed, town "Madison"
   - source: https://nhefa.scholarshipfund.org/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Feed https://nhefa.scholarshipfund.org/api/admin/stats (undocumented): {"count": 11, "frl_count": 11, "priority_count": 11, "non_priority_count": 0, "sped_count": 3, "waitlist_count": 0, "town": "Madison"}. Same day: Freedom 5, Tamworth 15, Eaton 7, Ossipee 37, Conway 23. Counts change daily; the feed and NH DOE count differently. The site's education_freedom_account_entry table (town 333) holds NH DOE counts. Statewide EFA rules: library topics efa-eligibility-and-cap, efa-uses-and-requirements, efa-how-to-apply. Raw: raw/community/efa/efa-stats-2026-11-13.json
8. Madison students attend Kennett Middle School (about 15 minutes from Madison Elementary by car) and Kennett High School (about 25 minutes) in Conway, by the same derived method, for comparison with the drive times above.
   - citation: OSRM driving routes from Madison Elementary School (derived)
   - source: https://router.project-osrm.org/route/v1/driving/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Derived: Kennett Middle (176 Main Street, Conway) 6.8 miles, 14.6 minutes; Kennett High (409 Eagles Way, North Conway) 11.5 miles, 25.4 minutes. Bus times are in the transportation file. Raw: raw/community/distances/osrm-routes-from-mes-2026-11-13.json; nominatim-kennett-middle.json, nominatim-kennett-high.json

## madison_area_school_options_drive: School and EFA Options Near Madison, by Road Distance From Madison Elementary (derived)

- unit: miles; minutes (derived)
- period: Routes computed November 13, 2026; EFA feed and PSS as of November 13, 2026; year: 2027
- source: OSRM public router — https://router.project-osrm.org/ ; CSF EFA marketplace feed — https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors ; NCES PSS 2023-24
- as_of: 2026-11-13
- raw: raw/community/distances/osrm-routes-from-mes-2026-11-13.json; raw/community/distances/nominatim-*.json; raw/community/efa/efa-providers-near-madison-2026-11-13.csv; raw/community/private-schools/nces-pss-03849-25mi.txt
- note: **Derived**: fastest OSRM car route from Madison Elementary School in normal conditions (no snow or traffic). Sorted by minutes. "EFA" means the school or program is listed on the CSF marketplace. Grades and students from PSS 2023-24 where given. Not a ranking, and not a complete list of programs.

| Option | Town | Type | Grades or ages | EFA marketplace | Road miles | Minutes | Note |
|---|---|---|---|---|---|---|---|
| HomeSweet HomeSchool | Madison (Silver Lake) | Homeschool program | K–8 tags | Yes | 1.1 | 3 | Tutoring, small groups, clubs |
| Robert Frost Charter School | Conway | Public charter | K–12 | No (public) | 6.9 | 14 | Tuition-free |
| Kennett Middle School | Conway | Public (receiving school) | 7–8 | — | 6.8 | 15 | For comparison |
| Tamworth Village Homeschool | Tamworth | Licensed child care; homeschool enrichment | 6 weeks–14 | Yes | 6.8 | 16 | Hybrid class for ages 5–6 |
| Tamworth Learning Circles | Tamworth | Listed as "school" | not stated | Yes | 9.0 | 21 | No description in feed |
| The Lilliputian School | North Conway | Early childhood center | grades 0–7 (feed) | Yes | 11.3 | 24 | Street-level location |
| Kennett High School | North Conway | Public (receiving school) | 9–12 | — | 11.5 | 25 | For comparison |
| New Life Christian Academy | Fryeburg, ME | Private religious | 1–11 (27 students) | Yes | 15.1 | 32 | |
| Cornerstone Christian Academy | Ossipee | Private religious | PK–8 (74 students) | Yes | 18.5 | 33 | EFA feed coordinates |
| Fryeburg Academy | Fryeburg, ME | Private academy | 9–12 (654 students) | Yes | 15.7 | 34 | |
| Brewster Academy | Wolfeboro | Private | not stated | Yes | 27.5 | 47 | |
| The Aletheia School | Wolfeboro | Homeschool learning center | 7–12 | Yes | 27.6 | 47 | |
| Northeast Woodland Chartered Public School | Conway | Public charter | K–8 | No (public) | | | Address not geocoded |

## madison_area_efa_marketplace_by_town: EFA Marketplace Entries in Madison and Neighboring Towns, by Type (derived)

- unit: count
- period: CSF EFA marketplace feed as downloaded November 13, 2026; year: 2027
- source: Children's Scholarship Fund NH EFA marketplace feed — https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors
- as_of: 2026-11-13
- raw: raw/community/efa/efa-marketplace-vendors-2026-11-13.json; raw/community/efa/efa-providers-near-madison-2026-11-13.csv
- note: **Derived** by the feed's city field. Madison includes Silver Lake; Tamworth includes Chocorua and South Tamworth; Ossipee includes Center Ossipee. One "Madison, NH" entry with a North Carolina ZIP was dropped. The feed is undocumented and changes daily; listing shows CSF approval, not price, quality or openings. Conway's villages and the other valley towns are in the Conway file (conway_area_efa_marketplace_by_type).

| Place | town_id | Total | Provider | School | Tutor | Vendor | Entries |
|---|---|---|---|---|---|---|---|
| Madison | 333 | 3 | 2 | 0 | 1 | 0 | HomeSweet HomeSchool; Windcroft Stables; Rockin' Fitness |
| Tamworth | 525 | 7 | 4 | 1 | 1 | 1 | Tamworth Learning Circles (school); Tamworth Village Homeschool; We Can Be Heroes; Pianoforte; SAU #49 Carroll County Adult Education; Booska Engaging Brainwork (tutor); The Bearcamp Center (vendor) |
| Ossipee | 419 | 7 | 4 | 1 | 2 | 0 | Cornerstone Christian Academy (2 entries); Somersworth, NH Catholic Schoolhouse; Trail Life NH0109; Town of Ossipee Parks and Recreation (school); two tutors |
| Freedom | 187 | 1 | 0 | 0 | 0 | 1 | Outdoor School for Youth by Outdoor ESCAPES |
| Eaton | 159 | 1 | 1 | 0 | 0 | 0 | Sullivan Mathematics - Eaton |

## town-broadband: Home Internet in Madison: Subscriptions, Fiber Buildout and Broadband Grants

- kind: local
- question_type: local_practice
- description: Home internet and cell coverage in a town beyond the site's Census estimates: fiber and other buildout, cell coverage, state and federal broadband grants, and regional broadband districts

1. The ACS for 2020-2024 estimates that 87.1% (±5.2) of Madison's households have a cable, fiber optic or DSL internet subscription, 6.7% (±4.3) have only a cellular data plan and 4.2% (±4.1) have satellite service, while 2.2% (±2.2) have no internet subscription.
   - citation: ACS 5-year 2020-2024, table S2801 (Types of Computers and Internet Subscriptions)
   - source: https://data.census.gov/table/ACSST5Y2024.S2801?g=060XX00US3300345060
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: S2801_C02_017E 87.1 ±5.2 (cable, fiber optic or DSL); _016E 6.7 ±4.3 (cellular data plan with no other subscription); _018E 4.2 ±4.1 (satellite); _019E 2.2 ±2.2 (without a subscription). The site's database (table B28002, ACS 2020-2024) agrees: 874, 67, 42 and 22 of 1,003 households (derived shares). The share with broadband of any type, for Madison and the state, is in the site's Census data. The survey measures subscriptions, not speed or reliability. See table madison_area_internet_subscriptions. Raw: raw/community/census/ACSST5Y2024.S2801-madison.json, labels-S2801.json
2. Consolidated Communications (Fidium) completed fiber in its Madison wire center between May and July 2024, with 1,979 "passings" (homes or sites the fiber line runs past) and 82 miles of fiber optic cable in Madison, according to the town's representatives to the Carroll County Communications District.
   - citation: Town of Madison 2024 Annual Report, "NH Broadband Expansion Update for Madison Residents - 2024"
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "CCI/Fidium reports the Madison Wire Center was completed this year (May to July) and included a total of 1979 'passings' - the term used for service adjacent to a home site. A total of 82 miles of fiber optic cable has been installed in Madison by CCI/Fidium. Data was not provided by NHEC on progress for their customers in Madison." For scale, the 2020 Census counted 1,881 housing units (town-housing fact 1); a passing does not mean a home has subscribed. Scanned; transcribed from OCR. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, p. 138
3. Madison is one of 16 member towns of the Carroll County Communications District, formed in 2023 under RSA 53-G to promote "symmetrical high speed broadband" to every home and business in the county; Madison's selectmen appoint its representatives, and the town's boards list has no separate broadband committee.
   - citation: Carroll County Communications District, 2025 Annual Report; Town of Madison, Boards & Committees menu
   - source: https://cccdnh.org/wp-content/uploads/2025/09/2025-Carroll-County-Communications-District-Annual-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "The CCCD was organized in 2023 as provided by NH RSA 53-G ... The District members are the 16 Towns of Albany, Bartlett, Brookfield, Chatham, Conway, Eaton, Effingham, Freedom, Hale's Location, Hart's Location, Jackson, Madison, Moultonborough, Ossipee, Tamworth, and Tuftonboro. The CCCD Governing Board is composed of unpaid Representatives appointed by the Select Boards"; the representative list names a Madison representative and alternate. The town site's Boards & Committees menu lists no broadband committee (raw/community/town/town-home.txt). **Premise check (P19.2):** no town broadband committee. Raw: raw/community/broadband/cccd-annual-report-2025.pdf (.txt); cccd-home.txt
4. The Communications District reported that, as of September 2025, NH Broadband (the New Hampshire Electric Cooperative's service) was available to 11,318 homes across Carroll County with 925 left in its build plan and an estimated completion in June 2026, and that Fidium had passed 6,889 addresses under its grant, with more than 28,900 Carroll County addresses having access to fiber.
   - citation: Carroll County Communications District, 2025 Annual Report, Chairman's Letter
   - source: https://cccdnh.org/wp-content/uploads/2025/09/2025-Carroll-County-Communications-District-Annual-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: County-wide figures, not Madison's. Text: "NH Broadband states that 'as of September 2025, NH Broadband is available to 11,318 homes across Carroll County, with 925 remaining in our build plan ... estimated completion date of June 2026'"; "CCI/Fidium reports they have completed wire passings to 6,889 fiber addresses as part of the grant and a total of 28,900+ addresses in Carroll County have access to fiber." Whether the June 2026 completion happened was not found. Raw: raw/community/broadband/cccd-annual-report-2025.txt
5. New Hampshire's final list of locations eligible for federal BEAD broadband grants (June 16, 2025) includes 21 locations in Madison, out of 5,250 statewide; all 21 were awarded to SpaceX for low-earth-orbit satellite service, in a project the state labeled "non-priority," with planned speeds of 120 Mbps down and 20 Mbps up.
   - citation: NH Department of Business and Economic Affairs, Final BEAD Eligible BSLs (6-16-2025); NH BEAD Final Proposal files fp_locations (11-20-2025) and fp_deployment_projects (11-19-2025)
   - source: https://www.nheconomy.com/Office-of-Broadband-Initiatives/BEAD
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Spreadsheet "PSA Summary" row "Madison,21" (5,250 total, derived sum of 227 rows); the 21 Madison location IDs all match project "CM61-BEAD-NH-0014-0" in fp_locations (technology 61, download 120, upload 20), which fp_deployment_projects names "Lakes_SpaceX_Non_Priority ... A project awarded to SpaceX to deploy LEO to 228 locations" (derived match). Neighboring towns: Conway 29, Eaton 48, Freedom 5, Ossipee 40, Tamworth 45. The state's BEAD page says NTIA approved the Final Proposal on November 18, 2025, and subgrants were to go to the Governor and Council in early 2026. Raw: raw/community/broadband/Final-BEAD-Eligible-BSLs-6-16-2025_2.xlsx (sheet CSVs), fp_locations_11-20-2025.csv, fp_deployment_projects_Regions_11-19-2025.csv, nheconomy.com-Office-of-Broadband-Initiatives-BEAD.txt
6. New Hampshire's BEAD Final Proposal says satellite (LEO) service needs an unobstructed view of the sky, that tree canopy, terrain, rain, snow and fog can disrupt it, and that LEO applications were deemed non-priority in service areas where many eligible locations were under tree canopy.
   - citation: NH BEAD Final Proposal (November 19, 2025), Priority Broadband Projects, "Physical Limitations"
   - source: https://www.nheconomy.com/getmedia/ca8525eb-e4cb-41ae-8c76-1e336ba6803e/NH-BEAD-Final-Proposal_11-19-2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Text: "LEO satellite systems require an unobstructed view of the sky ... Even minor obstructions like tree branches or rooftops can cause service disruptions. Rain, snow, and fog further degrade performance"; "If a significant number of the BSLs in a project service area were indicated as covered by the tree canopy ... LEO applications were deemed to be non-priority for that project service area." The proposal also weighed scalability and customer density; it does not give Madison's own canopy figure. Raw: raw/community/broadband/nh-bead-final-proposal.pdf (.txt), PDF pp. 23–24
7. No address-level coverage or reliability data for Madison's roads was retrieved: the FCC National Broadband Map refused automated access, and the town, school district and county district documents read give no outage or reliability figures.
   - citation: FCC National Broadband Map (not retrieved); documented absence in town and CCCD reports
   - source: https://broadbandmap.fcc.gov/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Statement of a gap, so the Ask can say so plainly. The FCC map returned HTTP 403 (also in the Jackson research). In November 2026 the town's home page asked callers to use a temporary number because of "issues with Consolidated Communications (Fidium)" with Town Hall phones (raw/community/town/town-home.txt); that notice concerns phone lines, not home internet.

## madison_area_internet_subscriptions: Internet Subscriptions by Household, Madison and Neighboring Towns

- unit: percent of households
- period: ACS 5-year 2020-2024; year: 2024
- source: Census Bureau, ACS 5-year table S2801 — https://data.census.gov/table/ACSST5Y2024.S2801?g=060XX00US3300345060
- as_of: 2026-11-13
- raw: raw/community/census/ACSST5Y2024.S2801-<town>.json (madison, freedom, tamworth, eaton, conway, ossipee, nh)
- note: Categories overlap (a home can have several). Households and the share with broadband of any type are in the site's Census data for each district and the state. Ossipee's are not, as it is part of the multi-town Governor Wentworth Regional district: S2801 gives it 1,529 households (±173), 86.7% (±7.0) with broadband of any type (the site's database agrees on the share and derives its margin as ±13.8). The site's database (table B28002, ACS 2020-2024) agrees with every share here. Margins are large for small towns. Subscriptions do not measure speed or reliability.

| Place | town_id | Cable, fiber or DSL | Cellular only | Satellite | No subscription |
|---|---|---|---|---|---|
| Madison | 333 | 87.1 (±5.2) | 6.7 (±4.3) | 4.2 (±4.1) | 2.2 (±2.2) |
| Freedom | 187 | 78.7 (±6.7) | 5.7 (±3.0) | 0.6 (±0.8) | 10.4 (±6.0) |
| Tamworth | 525 | 73.2 (±10.4) | 5.1 (±4.9) | 8.1 (±6.7) | 14.5 (±8.6) |
| Eaton | 159 | 81.7 (±9.0) | 4.7 (±4.8) | 6.8 (±5.9) | 8.4 (±7.5) |
| Conway | 113 | 76.9 (±6.0) | 10.4 (±4.7) | 1.1 (±1.0) | 12.0 (±4.2) |
| Ossipee | 419 | 77.4 (±7.4) | 4.1 (±2.7) | 2.1 (±2.0) | 13.3 (±7.0) |
| NH | | 83.1 (±0.4) | 7.8 (±0.3) | 3.4 (±0.2) | 6.9 (±0.3) |

## town-emergency-services: Madison's Police, Fire and Rescue, Dispatch and Alerts

- kind: local
- question_type: local_practice
- description: A town's police, fire and emergency management, dispatch, mutual aid, emergency alerts and cell coverage

1. The Madison Police Department, in the lower level of the Town Hall at 1923 Village Road, lists a chief, a sergeant and two officers on its web page; its non-emergency number (603-367-8334) is forwarded to a dispatch center when the office is unattended.
   - citation: Town of Madison, Police page
   - source: https://www.madison-nh.org/departments/police/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "Police Chief ... Sergeant ... Officer ... Officer"; "1923 Village Road Town Hall lower level"; "This number is forwarded to our dispatch center when the office is unattended." The page posts monthly calls-for-service logs (latest November 2025). Names are not repeated. The 2024 town report also lists three part-time officers (p. 8). Raw: raw/community/town/departments-police.html (.txt)
2. In 2024 the Madison Police Department hired a third full-time officer, leaving one full-time position vacant; its chief reported 2,789 calls for service (up 14%), 442 motor vehicle stops and 26 arrests, and said county and state police gave "very little, to no assistance with overnight coverage while our officers are on call," with officers called out after hours 31 times.
   - citation: Town of Madison 2024 Annual Report, Madison Police Department report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "I'm thrilled to have hired Officer Tessa Llewellyn to fill our third full-time officer position ... This leaves the department with 1 vacant full-time position that I aim to fill in 2025"; "This has led to very little, to no assistance with overnight coverage while our officers are on call. For 2024, officers were called out afterhours 31 times. Officers have taken a combined total of approximately 4,938 hours of on call time (41% increase)"; "In 2024 we received 2,789 calls for service (14% increase), investigated 26 motor vehicle crashes (27% decrease), made 26 arrests (49% decrease), and conducted 442 motor vehicle stops." Scanned; transcribed from OCR. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 109–110
3. No source read says Madison has a school resource officer or shares one with Freedom or Tamworth: the police reports for 2021–2024, the 2025 and 2026 town meeting minutes and budgets, and the Madison School District's 2026 annual report do not mention a school resource officer or police assigned to Madison Elementary.
   - citation: Town of Madison Annual Reports 2021–2024 (police reports); 2025 and 2026 Town Meeting minutes; Madison School District Annual Report (2026) (documented absence)
   - source: https://www.madison-nh.org/departments/police/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Searched the OCR text of each document for "resource officer", "SRO" and "school" near police items; no match. **Premise check (P18.3):** no shared SRO was found. School building security, drills and police coordination are in the Madison Elementary file (agent 1). Raw: raw/community/town/2021-Madison-TownReport-web.ocr.txt, 2022-Madison-Town-Report.ocr.txt, 2023-Town-Report-Web.ocr.txt, 0000-2024-Town-Report.ocr.txt, 2025_Town-Meeting-Minutes_Madison.ocr.txt, 2026_Town-Meeting-Minutes_Madison_signed.ocr.txt; raw/community/school-district/madison-sd-annual-report-2026.txt
4. Madison voters approved $380,662 for police in 2026 (the 2025 budget was $372,547, of which $345,476.71 was spent) and set up a Police Cruiser Expendable Trust Fund with $25,000.
   - citation: Minutes of the Madison Town Meeting, March 14, 2026, Articles 9 and 15
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_Town-Meeting-Minutes_Madison_signed.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes table: "Police 372,547.00 345,476.71 380,662.00"; Article 15: "establish a Police Cruiser Expendable Trust Fund ... and appropriate twenty-five thousand dollars ($25,000.00)" PASSED. Raw: raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.ocr.txt, pp. 12–15
5. Madison Fire/Rescue is a volunteer department at 1917 Village Road (Route 113); at the start of 2025 it had 11 active members (4 certified firefighters, 5 Basic EMTs and 1 Advanced EMT among them) and 2 student members, and it answered 367 calls in 2024, 194 of them (52.86%) medical calls.
   - citation: Town of Madison, Fire/Rescue page; Town of Madison 2024 Annual Report, Madison Fire-Rescue report
   - source: https://www.madison-nh.org/departments/firerescue-department/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "Madison Fire/Rescue Department is a volunteer organization located at 1917 Village Road (Route 113)"; "Fire Commissioners are the Board of Selectmen." Report: "Throughout 2024, the department answered 367 calls for emergency response"; "Presently, we have 11 active members on our roster and 2 student members. Of the 11 active members: 4 are certified firefighters; 5 are Basic EMTS; 1 is an Advanced EMT"; "EMS Call (non MVA) 194 52.86%"; it belongs to the Ossipee Valley and Mount Washington Valley Mutual Aid Associations. The fire budget for 2026 was cut by $15,000 at town meeting, to $150,750. Raw: raw/community/town/departments-firerescue-department.txt; raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 113–114
6. Madison Fire/Rescue runs a Student Firefighter Program with the Career and Technical Center at Kennett High School, which had two active student members in 2024.
   - citation: Town of Madison 2024 Annual Report, Madison Fire-Rescue report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "The Student Firefighter Program, in conjunction with the Career Technical Center at Kennett High School, is continuing with 2 active student members. This program allows the students to participate to their level of comfort in our training and enables them to gain experience in the field." Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, p. 113
7. Madison pays a private ambulance service for emergency medical transport: its 2024 payments list $115,911.69 to Action Ambulance, and voters approved $134,442 for ambulance service in 2026.
   - citation: Town of Madison 2024 Annual Report, vendor payments and budget detail; Minutes of the Madison Town Meeting, March 14, 2026, Article 9
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "Action Ambulance 115,911.69" (vendor list, p. 96) and "Ambulance 115,911.69 133,044.00" (2024 actual and budget, p. 85). 2026 minutes: "Ambulance $ 120,104.00 $ 119,910.69 134,442.00" (2025 approved, 2025 expended, 2026). The contract terms were not found. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt; raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.ocr.txt, p. 12
8. Madison's emergency warning system is the "Madison Alert System," run through Genasys, which residents join by creating an account online; the fire department asks people with burn permits to notify Carroll County Dispatch (603-539-2263) before burning.
   - citation: Town of Madison home page; Fire/Rescue page
   - source: https://www.madison-nh.org/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Home page: "Sign up for the Madison Alert System!! Create an account here: https://madisonnh.genasys.com/portal/en". Fire page: "All permittees are asked to notify Carroll County Dispatch at 603-539-2263 before starting their burn." Which center dispatches Madison police, fire and ambulance calls is not stated on the pages read. Raw: raw/community/town/town-home.txt; departments-firerescue-department.txt
9. Madison's Emergency Management Director, who is also the fire chief, reported that 2024 brought no declared disasters, after federal disaster declarations for storms on July 16 and December 18, 2023 damaged town roads and culverts, including Colby Hill Road.
   - citation: Town of Madison 2024 Annual Report, Emergency Management report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "2024 was uneventful with regard to declared disaster events, a welcome change from 2023. The administrative processes surrounding the two declared disasters on July 16 and December 18, 2023, seeking reimbursement from the Federal Emergency Management Agency (FEMA) were time-consuming"; "The first was the reconstruction of Colby Hill Road." In November 2026 the town's home page warned that "previously closed roads may not be fully repaired." Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, p. 111; raw/community/town/town-home.txt
10. Madison's Highway Safety Committee includes the police chief, the fire chief, the public works foreman, the Madison Elementary school nurse and residents.
   - citation: Town of Madison 2024 Annual Report, Town Officials
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "HIGHWAY SAFETY COMMITTEE James Hayford, Police Chief Selectmen's Rep Justin Chick, Foreman DPW Sara Rodriguez, School Nurse Michael R. Brooks, Fire Chief Paul R. Jean, Resident." Its meetings and work were not found. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, p. 7

## town-family-help: Food Help, Charitable Funds and Scholarships for Madison Families

- kind: local
- question_type: help
- description: Local programs and funds that help families with costs

1. The Madison Church Food Pantry reported serving 971 individuals in 253 households in 2024 (all visits), including 338 visits by children under 18, and providing 18,102 meals; it is open Wednesdays and Thursdays by appointment and as needed for emergencies, and it delivers food twice a month to Silver Lake Landing.
   - citation: Town of Madison 2024 Annual Report, Madison Church Food Pantry 2024 Annual Report
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "In 2024, 971 individuals were served, and 18,102 meals were provided"; "We are open on Wednesdays and Thursdays by appointment and on an 'as needed' basis for emergency assistance"; "Households served (all visits): 253"; "Children (under18): 338 (34.81%)"; "Twice a month, we deliver food to Silver Lake Landing"; over 17 volunteers. The town's 2025 welcome packet says "Open: Wednesdays by appointment; Emergencies only on other days" (raw/community/town/Welcome-Packet-03-19-25.ocr.txt, p. 3). Scanned; transcribed from OCR. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 139–140
2. The Madison Food Pantry opened a new 480-square-foot building behind The Madison Church at 53 Conway Road in June 2025; it serves Madison and surrounding towns by appointment (603-733-6323), and its board also gives Madison Elementary School students free snacks.
   - citation: Conway Daily Sun, "Madison Food Pantry celebrates new building," June 19, 2025; Madison School District Annual Report (2026)
   - source: https://www.conwaydailysun.com/business/local/madison-food-pantry-celebrates-new-building/article_414920de-b858-44b7-8cdb-b6583068a354.html
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: News is the only source for the opening (the church's website had expired). Article text: "the new building is 480 square feet in size (16 by 30 feet) which, he said, is 'about four times as large as our previous pantry space'"; "The pantry board also provides free snacks for school children at Madison Elementary School, as well as Thanksgiving baskets, Christmas gifts and certificates"; "The food pantry currently serves approximately 25 families per month"; "serves individuals and families from Madison and the surrounding towns, with no person being turned away. To make an appointment to shop, call (603) 733-6323"; founded in 1979. The school report: "The Madison Food Pantry generously supplies our school with snacks for students to access in the classroom." The article text was stored encoded and decoded locally. Raw: raw/community/family-help/conwaydailysun.com-business-local-madison-food-pantry-celebrates-new-b.html (.decoded.txt); raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 28
3. The Madison Church Food Pantry gets food and money from the NH Food Bank, Tri-County Community Action (USDA surplus food), a FEMA food and shelter grant, grocery stores, Vaughan Community Services, the Ossipee Valley Rotary, the Madison Fire Department, the Conway Lions, the Knights of Columbus, the Boy Scouts and the Town of Madison, which gave $2,500 for 2024 and $5,000 in ARPA funds toward the new building.
   - citation: Town of Madison 2024 Annual Report, Madison Church Food Pantry report and Direct Assistance budget detail
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "Food Pantry Partnerships: NH Food Bank ... Tri-County Community Action Program. US Department of Agriculture (USDA) Surplus Food Program ... FEMA Emergency Food and Shelter Program (EFSP) ... Town of Madison. ARPA grant and an annual cash donation. Madison Fire Department. Christmas food drive collection. Madison Church Pre-School. Thanksgiving food collection. Conway Lions Club ..."; "In December, the Town of Madison donated $5,000.00 in American Rescue Plan Act (ARPA) funds"; budget detail "Direct Assistance Food Pantry 2,500.00 2,500.00". The vendor list shows "Food Pantry 7,500.00" (2,500 + 5,000, derived). The Thanksgiving distribution for 82 families was held at Madison Elementary on November 23, 2024. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, pp. 85, 97, 139–140 (vendor list p. 97)
4. All Madison Elementary School students can get weekend food bags through End 68 Hours of Hunger, whose Conway-based chapter packs bags each week and delivers them to Madison Elementary among other valley schools; each Friday bag holds food for three dinners and two breakfasts and lunches.
   - citation: Madison School District Annual Report (2026), School Report Card Tenet #1; Conway Daily Sun, "$25,000 challenge grant issued for End 68 Hours," January 22, 2025
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: School report: "While fulfilling a need for those who have food insecurity, we make food available to all students so no one feels targeted or singled out"; "All students have access to weekend food bags through End 68 Hours of Hunger." Article (news is the only source for the chapter): "Conway delivers to Lakeside Primary School. Mountainside Intermediate, Josiah Bartlett Elementary, Jackson Grammar School, Freedom Elementary; Madison Elementary ..."; "Every Friday, children in the program receive a bag to take home. It includes food for three dinners (Friday, Saturday and Sunday), along with two breakfasts and two lunches"; about 180 students a week valley-wide and about $2,000 a week to run (January 2025). How bags are handed out at Madison Elementary is not described. Raw: raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 28; raw/community/family-help/conwaydailysun.com-news-local-25-000-challenge-grant-issued-for-end-68.html (.decoded.txt)
5. Madison Elementary School's counselor also serves as the family liaison, connecting families with food, clothing and community support services, and as the district's homeless liaison, and the school says students facing housing instability increased significantly in 2025-26.
   - citation: Madison School District Annual Report (2026), School Report Card, School Counselor
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Report text: "The counselor serves as a family liaison, connecting families with essential resources such as food, clothing, and community support services. She is also the district's homeless liaison, coordinating services for students experiencing housing instability—a population that has increased significantly during the 2025–26 school year." Counseling details are in the Madison Elementary file (P15.2). Raw: raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 24
6. The Town of Madison gives direct (welfare) assistance to residents in need through an application picked up at Town Hall with proof of qualification; voters set the 2026 Direct Assistance budget at $17,000, up from $9,700 approved for 2025, of which $7,770.02 was spent.
   - citation: Town of Madison Welcome Packet (2025); Minutes of the Madison Town Meeting, March 14, 2026, Article 7
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_Town-Meeting-Minutes_Madison_signed.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Packet: "WELFARE ASSISTANCE Pick up application during Town Hall hours 603-367-4332 Must provide proof of qualification with guidelines." Minutes: "Direct Assistance S 9,700.00 7,770.02 $ 17,000.00." The 2024 budget detail splits Direct Assistance into the food pantry gift, welfare and a part-time welfare administrator. Raw: raw/community/town/Welcome-Packet-03-19-25.ocr.txt, p. 3; raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.ocr.txt, p. 10
7. At the March 2026 town meeting Madison voters gave $36,140 to seven regional agencies: Tri-County Community Action ($5,771, for fuel and energy aid, transportation, diapers, dental care, Head Start and food pantries), Starting Point ($5,329), the Gibson Center ($6,000), White Mountain Community Health Center ($9,440), the Way Station ($3,000), the Ossipee Children's Fund ($3,500) and the Family Resource Center at Children Unlimited ($3,100).
   - citation: Minutes of the Madison Town Meeting, March 14, 2026, Articles 26–32
   - source: https://www.madison-nh.org/wp-content/uploads/2026/03/2026_Town-Meeting-Minutes_Madison_signed.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes text: "Selectman Price moved that the charitable articles be voted as a group (Articles 26-32) in the aggregate amount of $36,140.00"; Starting Point provides "advocacy and support to victims of domestic and sexual violence and their children"; White Mountain Community Health Center serves "uninsured and underinsured residents"; the Way Station serves "the homeless & housing insecure of the Mount Washington Valley"; "The Moderator declared Articles 26-32 PASSED." In 2025 the Way Station and Ossipee Children's Fund were "new requests" (2025 minutes p. 30). Raw: raw/community/town/2026_Town-Meeting-Minutes_Madison_signed.ocr.txt, pp. 18–19; raw/community/town/2025_Town-Meeting-Minutes_Madison.ocr.txt
8. Madison's Trustees of Trust Funds held a "Gould Town Poor/Community Pantry" fund of $2,977.89 at the end of 2024, a fund dating to 1934 that was renamed in 2018.
   - citation: Town of Madison 2024 Annual Report, Trustees of Trust Funds Report for the year 2024
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report row: "Gould Town Poor/Community Pantry 2018 1,000.00 0.00 1,000.00 1,886.83 91.06 1,977.89 2,977.89" with the note "Fund 1934 before name change." Who decides its use is not stated beyond the trustees' general duty to follow donors' wishes (raw/community/town/boards-trustees-of-trust-funds.txt). Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, p. 147
9. The Ossipee Children's Fund, which for 36 years paid toward child care, enrichment, education and recreation for children in Effingham, Freedom, Madison and Ossipee, has announced on its website that it has ceased operations and accepts no new applications.
   - citation: Ossipee Children's Fund, home page ("Ossipee Children's Fund Announces Closure")
   - source: https://www.ocfnh.org/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Page text: "The Ossipee Children's Fund has made the difficult decision to cease operations. Effective immediately, the organization will no longer be accepting applications for financial assistance"; "established to provide equal access to childcare, enrichment, education, and recreation programs for children residing in Effingham, Freedom, Madison, and Ossipee." The notice is undated; Madison voters appropriated $3,500 for the fund in March 2026 (fact 7), and it paid $5,950 toward Madison Rec summer camp in 2024 (town-recreation-and-summer fact 5). What happens to the 2026 town appropriation was not found. Raw: raw/community/family-help/ocfnh-home.html (.txt)
10. The Madison Scholarship Fund, a 501(c)(3) started in 1987 by a former school board member, had given scholarships to 279 students by 2020, who used them at "colleges and universities, community colleges and tech schools"; recipients must send first-semester grades and reach at least a 2.0 average, and the fund is raised through an Old Home Week golf tournament and other events.
   - citation: Town of Madison 2020 Annual Report, Madison Scholarship Committee 2020 Annual Report; 2026 Old Home Week schedule
   - source: https://www.madison-nh.org/wp-content/uploads/2021/04/2020-TOWN-REPORT-WEB.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Report text: "in 1987 the first Madison Scholarship was awarded. In 2003, the Percy/Charlotte Hill Award was created. This is a four-year scholarship given to one student each year planning to major in ... (STEM)"; "Since 1987, 279 students have been awarded scholarships ... to help defray some costs of attending colleges and universities, community colleges and tech schools"; "In June 2020, 11 KHS seniors from Madison were each awarded a scholarship"; "they must submit a transcript of their first semester grades ... at least a 2.0 grade average"; "Madison Scholarship Fund, P.O. Box 355, Madison, NH 03849." 2026 OHW schedule: "Madison Scramble - Golf Tournament at Indian Mound. Benefit Madison Scholarship Fund" (August 3, 2026) and a Beano night "Sponsored by Madison Scholarship Fund." Award amounts are not published. No later committee report was found in the 2021–2024 town reports. Raw: raw/community/town/2020-TOWN-REPORT-WEB.ocr.txt, p. 114; raw/community/town/2026-Old-Home-Week-Schedule-Draft-6.txt
11. Kennett High School's Standard Scholarship List for the Class of 2026 includes four awards for Madison students: the Madison Local & Percy/Charlotte Hill Scholarship (Madison residents), the M.E.S. Arts Scholarship (at least one year at Madison Elementary, studying the arts), the Nancy Spaulding Madison Elementary School award (Madison residents attending a two- or four-year college) and the NH Retired Troopers Association Award in Memory of Sgt. James Noyes (priority to Madison residents).
   - citation: Kennett High School, Standard Scholarship List – Class of 2026
   - source: https://files.smartsites.parentsquare.com/10275/standard_scholarship_list_2025_26_1.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: List text: "M.E.S Arts Scholarship Current seniors. Applicant must have attended Madison Elementary for at least one year and be pursuing a degree in the arts"; "Madison Local & Percy/Charlotte Hill Scholarship Current seniors. Applicant must be a resident of Madison"; "Nancy Spaulding Madison Elementary School Current seniors. Applicant must be attending a 2 or 4 year college. Must be a resident of Madison"; "NH Retired Troopers Association Award in Memory of Sgt. James Noyes Priority given to Madison, NH residents Applicant must show courage." Amounts are not posted. The application process is in the Conway file (town-family-help fact 9). Raw: raw/community/scholarships/khs-standard-scholarship-list-2025-26.pdf (.txt)
12. Kennett's non-standard scholarship sheet (separate applications) lists the Edward Granville Scholarship, for applicants from Madison who attended Madison Elementary for at least three years, with preference for aviation, engineering, mechanics or transportation, and the Greater Ossipee Area Chamber of Commerce Scholarships, for post-secondary education or training by residents of Effingham, Freedom, Madison, Ossipee, Sandwich and Tamworth.
   - citation: Kennett High School, Non-Standard Local Scholarship Information sheet ("Available to the Class of 2027")
   - source: https://docs.google.com/spreadsheets/d/1zs_JVWFOlf1ylZExZN2exWB_6F4umQbuHx-HKBRHe5U/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Sheet text: "Edward Granville Scholarship, Applicant must be from Madison and have attended Madison Elementary for at least three years; preference given to those studying aviation, or fields aligned with engineering, mechanics or transportation, CLOSED"; "Greater Ossipee Area Chamber of Commerce Scholarships, Applicants must be pursuing post-secondary education or training to students who reside in the towns of Effingham, Freedom, Madison, Ossipee, Sandwich and Tamworth., CLOSED, Application." "CLOSED" means the last cycle's deadline had passed on November 13, 2026. Raw: raw/community/scholarships/khs-nonstandard-local-scholarships.csv
13. The Town of Madison's Trustees of Trust Funds hold an Edward Granville Scholarship fund created in 1991, worth $11,909.56 at the end of 2024 ($10,412.79 principal and $1,496.77 in income), and the trust reports for 2020–2024 show no withdrawals or spending from it (derived).
   - citation: Town of Madison Annual Reports 2020, 2022, 2023 and 2024, Trustees of Trust Funds reports
   - source: https://www.madison-nh.org/wp-content/uploads/2025/02/0000-2024-Town-Report.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: 2024 row: "Edward Granville Scholarship 1991 10,412.79 0.00 10,412.79 1,132.59 364.18 1,496.77 11,909.56" (income at start 1,132.59 + income 364.18 = 1,496.77 at year end, so nothing expended, derived). Year-end totals: $11,107.97 (2020), $11,205.51 (2022), $11,545.38 (2023), $11,909.56 (2024); the 2020–2023 reports print the name as "East Granville Scholarship." The trust reports list no other scholarship fund (derived). How or whether awards are paid from the fund is not stated; Kennett's sheet lists the award (fact 12). Scanned; transcribed from OCR. Raw: raw/community/town/0000-2024-Town-Report.ocr.txt, p. 147; 2023-Town-Report-Web.ocr.txt; 2022-Madison-Town-Report.ocr.txt; 2020-TOWN-REPORT-WEB.ocr.txt
14. **Derived:** none of the Madison-specific scholarships found is limited to trade school or two-year study, but several allow it: the Greater Ossipee Area Chamber awards cover "post-secondary education or training," the Nancy Spaulding award covers two- or four-year colleges, the Madison Scholarship Fund has been used at community colleges and tech schools, and the Granville award prefers mechanics and transportation fields without naming a level of study.
   - citation: Kennett Standard Scholarship List (Class of 2026); Kennett non-standard sheet; Madison Scholarship Committee 2020 report (derived comparison)
   - source: https://khs.sau9.org/scholarship
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Derived from facts 10–12. **Premise check (P8.3):** scholarships for Madison graduates exist, but none is dedicated to trades or two-year degrees. Kennett's general trade and two-year awards open to all its seniors (Career & Technical Center Scholarship, Karry Holland Trade School Award, Conway Area Lions and others) are in the Conway file (town-family-help facts 8–15; table kennett_local_scholarships_trades_two_year). Statewide aid: library topics ccsnh-tuition-and-aid, granite-edvance. Raw: raw/community/scholarships/khs-standard-scholarship-list-2025-26.txt; khs-nonstandard-local-scholarships.csv; raw/community/town/2020-TOWN-REPORT-WEB.ocr.txt
15. At the March 2025 town meeting Madison voters approved $500 "to offer the youth of Madison conservation training and instructive opportunities," available until spent or December 31, 2027; the warrant had first proposed a Conservation Scholarship and Educational trust fund.
   - citation: Minutes of the Madison Town Meeting, March 15, 2025, Article 21; 2025 Town Warrant (printed in the 2024 Annual Report)
   - source: https://www.madison-nh.org/wp-content/uploads/2025/04/2025_Town-Meeting-Minutes_Madison.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Minutes text: "Article 21. To see if the Town will vote to raise and appropriate the sum of five hundred dollars ($500.00) to offer the youth of Madison conservation training and instructive opportunities. This special article will be non-lapsing ... December 31, 2027 ... The Moderator declared Article 21 PASSED." Warrant text: "establish a Conservation Scholarship and Educational Expendable Trust Fund ... naming the Conservation Commission as agents to expend" (2024 report p. 160). How youth apply was not found. Raw: raw/community/town/2025_Town-Meeting-Minutes_Madison.pdf (.ocr.txt), p. 25; raw/community/town/0000-2024-Town-Report.ocr.txt
16. Madison's Old Home Week road race raises money for Madison Church camp scholarships, and the Madison Church also sponsors water bottles for the town's recreation summer camp.
   - citation: 2026 Old Home Week schedule; Town of Madison Recreation Committee minutes, April 13 and May 11, 2026
   - source: https://www.madison-nh.org/wp-content/uploads/2026/07/2026-Schedule-Draft-6.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Madison
   - note: Schedule text: "James Wellinghurst Memorial Road Race - 3.1 miles. Start at Madison Church, end at Silver Lake P.O. ... Benefit Madison Church Camp Scholarships." Rec minutes (May 11): "The Madison Church has committed to sponsoring water bottles for camp." How to apply for the camp scholarships was not found. Raw: raw/community/town/2026-Old-Home-Week-Schedule-Draft-6.txt; raw/community/recreation/REC-5-11-26.ocr.txt
17. Madison Elementary School's 2026 report card lists community connections including Madison Recreation, Tin Mountain and Green Mountain Conservation Group school programs, OASIS intergenerational tutoring, Believe in Books, a Kiwanis book giveaway, and fall and spring community lunches with a play; no Madison coat drive was found in town, school or news sources.
   - citation: Madison School District Annual Report (2026), School Report Card Tenet #3 (documented absence for coat drives)
   - source: https://drive.google.com/file/d/1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Report text: "Integrated Arts- Connecting Students with the Greater Community ... Believe in Books; Fall & Spring Community Lunch & a Play Performance; Green Mt. Conservation Integrated School Programs; Kiwanis Book Giveaway; Madison Recreation Department; OASIS Intergenerational Tutoring; Student Led Veterans Day Assemblies; Tin Mountain School Programs." The school also had Children's Literacy Foundation grants (2024-25 and 2025-26). Other partners named elsewhere: the Madison Church food pantry (fact 2), SLAM's Lake Ecology curriculum (town-government-and-civic-spaces fact 6), the Historical Society (town-history-and-heritage fact 6) and the Madison PTO's Holiday Fair and Trunk or Treat (2024 report p. 145). How a church or civic group arranges a partnership, summer reading program or supply drive is not described in the documents read; volunteer rules are in the Madison Elementary file. Coat drive searches: town site, 2020–2024 town reports, school report and one web search. Raw: raw/community/school-district/madison-sd-annual-report-2026.txt, PDF p. 30

## For another file

- **Madison Elementary agent (1):**
  - The 2026 Madison School District annual report (Drive id 1E5cBiDRGgIpK2cmOMRYvmznA25VifTjN, linked from https://www.sau13.org/school-board/annual-reports; copy at raw/community/school-district/madison-sd-annual-report-2026.pdf) gives Madison Elementary enrollment as of October 31: 127 (2020), 127 (2021), 125 (2022), 113 (2023), 110 (2024) and 102 (2025). This bears on the "~125 students" and "120–130 students" premises (P3.1, P7.2). Also: free/reduced lunch rate 43% (2025); reading proficiency up from 42% to 52% over five years, "exceeding the state average in both 2023 and 2024" (P2.2 premise); math 22% to 29%; the House system (2023-24); counselor as family and homeless liaison; full-time counselor and nurse; SAU 13 preschool 18 students in 2024-25 and 2025-26.
  - The Historical Society used school space so "students can learn about their town's history" (2024 town report p. 130), and SLAM sponsors a 5th grade Lake Ecology curriculum (welcome packet p. 17). Useful for P20.1's curriculum side.
  - The town Highway Safety Committee includes the school nurse (2024 report p. 7); no SRO was found (town-emergency-services fact 3).
- **School-day and policies agent (2):** the report card lists "Before and After School Care Enrichment Programs" (PDF p. 30) and "billing for before- and after-school programming" in the SAU business office (PDF p. 22). Rec summer camp in 2024 used Madison Elementary classrooms and included home-schooled students.
- **Kennett agent (3):** Madison Fire/Rescue's Student Firefighter Program with the Kennett Career and Technical Center (2024 report p. 113).
- **Money agent (4):**
  - 2026 school ballot results (raw/community/school-district/2026_SCHOOL-BALLOT_RESULTS_03_10_2026-2.pdf, .ocr.txt) and the 2026 SB2 warrant with the deliberative session date (February 2, 2026).
  - The 2024 tax rate computation (Eidelweiss $5.63 on $137.7 million; town $15.77), trust fund balances (School Building CRF $253,363.62; Special Education CRF $222,369.22 at end of 2024) and the Madison Corner Schoolhouse CRF ($50,394.37 at June 30, 2025) are in raw/community/town/0000-2024-Town-Report.ocr.txt and the school report.
  - The 2025 town meeting minutes are posted (raw/community/town/2025_Town-Meeting-Minutes_Madison.pdf); the 2025 annual town report is not.
- **Library (`additional-data/district-practices.md`), Madison fact 78:** says the deliberative session date was not found; the 2026 school warrant gives Monday, February 2, 2026 at 7:00 p.m. in James Noyes Memorial Hall (town-government-and-civic-spaces fact 4).
- **Earlier town files:**
  - Bartlett `daily-life-and-community.md`, town-child-care fact 2 and table bartlett_area_infant_care_drive_distance: Family Child Care of Madison is in Madison's DHHS data too (license to 2027-09-30); its places and ages are in the site's data.
  - Conway `community-and-choice.md`, kennett_local_scholarships_trades_two_year: the Greater Ossipee Area Chamber of Commerce Scholarships ("post-secondary education or training") could be added as open to training programs for residents of six towns.
  - Jackson `community-and-families.md`, town-child-care 1–5 in `Jackson/community-and-families.md`: Tamworth and Ossipee programs (table madison_area_child_care_drive_distance) were outside that file's area.
- **Shared topics:** proposals in the Summary (`town-broadband`, `town-government-and-civic-spaces`, `town-history-and-heritage`); support for Conway's proposed `local-scholarships`.

## Not retrieved

- FCC National Broadband Map (https://broadbandmap.fcc.gov/area-summary/fixed?...geoid=3300345060...): HTTP 403 to curl, as in the Jackson research. No location-level coverage, provider or technology data for Madison's roads.
- NH Broadband Mapping or a state coverage map by address: not found on the BEA BEAD pages read; only the BEAD eligible-location files were used.
- NH DOE nonpublic school list (education.nh.gov): blocked in earlier research; NCES PSS was used instead.
- Northeast Woodland Chartered Public School (53 Technology Lane, Conway): Nominatim returned no match for the address or the school name, so no drive time.
- Two Center Conway child care addresses (230 East Conway Road; 90 Odell Hill Road): Nominatim returned no match.
- How long child care waitlists are: no provider page found (NH DHHS's Child Care Search, now in the site's data, shows wait-list status and reported openings, not wait lengths). Sites for Children Unlimited (childrenunlimitednh.org), Vaughan Learning Center, Bearcamp Valley School and Ossipee Concerned Citizens did not respond to the domains tried. Directory sites (Winnie, Care.com, carelookup) were not used.
- Madison Preschool (53 Conway Road): The Madison Church's website (madisonchurch.squarespace.com) has expired. Whether it operates was first left open because DHHS's scholarship-enrollment field reads "Inactive"; NH DHHS's Child Care Search lists its license as active and its openings updated November 9, 2026 (site data).
- Madison Church Food Pantry's own page: expired site; the June 2025 news article and the 2024 town report were used.
- Town of Madison 2025 Annual Report: not posted on madison-nh.org (WordPress media search for "report" found reports through 2024). The 2025 police, fire, scholarship and trust fund reports are therefore missing.
- Madison Scholarship Committee reports after 2020: none in the 2021–2024 town reports; award amounts and recent recipient counts not found.
- Ossipee Children's Fund closure date: not on its home page; its Facebook page was not opened.
- Coat drives for Madison families: none found (town site, town reports 2020–2024, school report, one web search).
- Silver Lake's railroad era: no local source found on the Historical Society site, the library site or the town reports; the Old Home Week schedule only mentions "the Train Station" as a place.
- Madison's master plan survey results and the "Community Meeting Summary" (the Master Plan Steering Committee page names a link but none is attached).
- Which dispatch center handles Madison police, fire and ambulance calls: the police page says "our dispatch center"; the fire page names Carroll County Dispatch only for burn notices.
- Ambulance contract terms with Action Ambulance: not posted.
- Census data were taken from the data.census.gov table API (api.census.gov requires a key) and labels from api.census.gov group metadata; no Silver Lake or Eidelweiss geography exists in the Census tables used.
- Tamworth and Eaton NH REALTORS® market reports: "not available" (no PDF returned).
- No personal information was sent to any outside service. Census, Nominatim, OSRM, CSF, NH DHHS, NCES, NH REALTORS, nheconomy.com, Google Drive and the town, school and organization sites were called with the identifier nhfacts-research (webmaster@nhfacts.com) or a generic browser string.
