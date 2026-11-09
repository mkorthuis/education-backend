# Town Money Figures: Tax Rates, School Taxes and State Adequacy Aid

Strategy type 6 ("How schools are run and paid for"), the numbers part. Gathered November 8, 2026.

## Summary

**What's covered**

| File (in `raw/town/`) | What it is | Years | Rows | Towns |
|---|---|---|---|---|
| `dra-tax-rates.csv` | NH Department of Revenue Administration (DRA) tax rates per $1,000 by town: municipal, county, local education, state education and total. Also the equalization ratio, the full value tax rate, DRA's school tax dollars (2018–2025), and a **derived** school share of the total rate | Tax years 2014–2025 (final), plus 36 towns already set for 2026 | 2,879 | 237 |
| `school-tax-by-town.csv` | NH DOE "Valuations, Property Tax Assessments and Tax Rates of School Districts": one row per town per year, with local education tax dollars, state education tax dollars, valuations, and assessed and equalized rates. Each row is cross-checked against DRA | Tax years 2010–2025 | 3,792 | 237 |
| `adequacy-aid.csv` | NH DOE adequacy aid calculation by municipality. One row per town, fiscal year and component, with each component as the DOE gives it (resident pupils, base and differentiated aid, statewide education tax, extraordinary need, fiscal capacity disparity aid, hold harmless and stabilization, total grant) | FY2020–FY2027 | 46,335 | 237, plus a "State Total" row |
| `sources.csv` | Every raw file in `raw/town/dra/` and `raw/town/doe/`, with source URL, how it was retrieved (live site or Wayback snapshot), as-of date and checksum | — | 82 files | — |

**How the DOE valuations report was read (item 3).** The report has one row per school district. Cooperative districts get a total row (town number 0) plus one row per member town. Towns are counted once by keeping:
- each single-town school district row, and
- each member-town row of a cooperative that shows rates.

The rows dropped are:
- cooperative and county total rows, and
- "reference only" member rows, which show XXXX for rates. These are the coops in footnotes B and C: Exeter Region, Hollis/Brookline, John Stark, Pemi-Baker, Profile, Souhegan, Winnacunnet and Dresden. Footnote C says those towns' full figures are on their own town district rows.

With this rule, the kept rows (245 a year) add up **exactly** to the report's TOTALS row in all 16 years (2010–2025), for all seven dollar and valuation columns. Adding every row instead overstates the total by about 30%, which explains the earlier mismatch. For 2014–2025 the per-town rates match DRA in all but 12 of 2,843 town-years. Local and state school tax dollars match DRA's tax-rate calculation data for every town in 2018–2025. Concord is the one exception, and only because DRA reports all of Concord while DOE splits off Penacook.

**Main gaps**
- **2025 rates** come from the final xlsx (DRA, January 2026). **2026** is partial: 36 towns had rates set as of October 30, 2026.
- **DRA full value tax rate** is missing for 2014–2017. No DRA file for those years was found in the archive or on the live site. The DOE report's equalized rates (computed a little differently) cover those years.
- **The 2015 DRA final PDF** prints some rows with components in the wrong columns. Seven rows (Concord, Penacook and five others) were fixed from DRA's 2015 xlsx or the DOE report; each fix is noted on the row.
- **The FY2027 adequacy file** is the October 1, 2026 calculation. DOE says the final calculation comes in April 2027.
- **Equalized valuation per pupil** is published by NH DOE only for 2020-21, as a separate district-level report (file kept, not converted). Town-level figures used for aid are in the adequacy file instead: EV per pupil for FY2027, and EV per free/reduced-meal pupil for FY2023–FY2027.
- **Unincorporated places** (Bean's Grant, Dixville and others) and the four non-town rows in the site's town table (Gonic, Coe-Brown Academy, Pinkerton Academy, Prospect Mountain) have no town_id match, so they are not in the CSVs (see *Name matching*).

---

## dra_tax_rates: Property Tax Rates by Town (DRA)

- unit: dollars per $1,000 of assessed value (rates); dollars (valuations, commitments, tax dollars); percent (equalization ratio, derived school share)
- period: tax years 2014–2026 (`tax_year` is the property tax year, which is set in the fall; NH DOE's matching school year is the one that starts that fall)
- source: NH DRA, Municipal and Property Division, "Municipal and Village District Tax Rates and Other Data" (https://www.revenue.nh.gov/about-dra/municipal-and-property-division/municipal-and-property-reports/municipal-and-village) and "Equalization" reports (https://www.revenue.nh.gov/about-dra/municipal-and-property-division/property-bureau/equalization)
- as_of: 2026-11-08 for 2025–2026 files, the 2025 comparison and the 2016–2025 ratio history, all from the live site. The 2014–2024 files are Wayback snapshots from 2015-11-12 to 2025-06-20; each file's snapshot is in `sources.csv`
- raw: `raw/town/dra/` (41 files)
- review_by: 2027-11-08

**Files used per year**

| Tax year | Rates file | DRA school tax dollars | Equalization ratio | Full value tax rate |
|---|---|---|---|---|
| 2014 | `2014-tax-rates.xlsx` | — | `ratio-median-ratio-cod-prd-history-2018-2009.xlsx` | — |
| 2015 | `15-final-tax-rates.pdf` ("FINAL 2015", printed 12/30/2015), with fixes from `15-tax-rate-information.xlsx` | — | `…history-2024-2015.xlsx` | — |
| 2016–2022 | `16-final-tax-rates.xlsx`, `17-final-tax-rates.xlsx`, `18-tax-rates.xlsx` … `22-tax-rates.xlsx` ("Completed Public Tax Rates") | 2018–2022 `…tax-rate-calculation-data.xlsx` | `ratio-median-ratio-cod-prd-ten-year-history.xlsx` (2025–2016) | 2018, 2019, 2020, 2022 comparison PDFs; 2021 `comp-of-full-value-tax-rates.xlsx` |
| 2023 | `2023-municipal-and-village-tax-rates-final.xlsx` | `2023-tax-rate-calculation-data.xlsx` | ten-year history | `2023-comparison-of-full-value-tax-rates-ranking-order.pdf` |
| 2024 | `2024-municipal-and-village-tax-rates.xlsx` | `2024-tax-rate-calculation-data.xlsx` | ten-year history | `2024-comparison-…pdf` |
| 2025 | `2025-municipal-and-village-district-tax-rates.xlsx` (Last-Modified 2026-01-26) | `2025-tax-rate-calculation-data.xlsx` | ten-year history (Last-Modified 2026-06-09) | `2025-comparison-of-full-value-tax-rate.pdf` |
| 2026 (partial) | `2026-municipal-tax-rates.pdf`, "Completed Public Tax Rates (As of October 30, 2026)" | — | — | — |

**Columns**
- `town`, `town_id`: from the site's `town` table.
- `tax_year`, `dra_name`: the name as DRA prints it.
- `municipal_rate`, `county_rate`, `local_education_rate`, `state_education_rate`, `total_rate`: per $1,000 of assessed value, copied exactly.
- `school_share_of_total_rate_pct_derived`: **derived**, = (local education rate + state education rate) ÷ total rate × 100, rounded to 0.1. DRA's own tax-rate comparison files publish the two "% of total tax rate" parts that this sum adds up.
- `equalization_ratio`: DRA's weighted-mean ratio of assessed to market value (percent).
- `full_value_tax_rate`: DRA's published full value rate.
- `assessed_valuation`, `assessed_valuation_with_utilities`, `total_tax_commitment`.
- `local_school_tax_effort`, `state_education_tax_effort`: dollars to be raised by local school taxes and the state education tax, from DRA's tax-rate calculation data (2018–2025).
- `date_rate_set`, `status`.
- `rate_source_file`, `ratio_source_file`, `full_value_source_file`, `calc_source_file`.
- `note`.

**Rows:** 2,879. That is 236 towns in 2014, 237 a year in 2015–2025, and 36 in 2026. The four municipal, county, state and local rates add up to the total rate (within 1 cent) on every 2016–2025 row.

**Caveats**
- **Penacook** (town_id 429) is the part of Concord in the Merrimack Valley School District. DRA lists it as its own line with Concord's municipal and county rates, its own school rates, and zero valuation. It has no ratio or full value rate.
- **2015 fixes.** In DRA's final 2015 PDF, the Concord and Penacook lines print the local and state education rates in each other's columns. They were assigned as local 12.15 / state 2.61 (Concord) and local 17.25 / state 2.43 (Penacook), the values in the NH DOE 2015 valuations report. For five more towns (Green's Grant, Hanover, Livermore, Salem, Surry), the PDF puts the components in the wrong columns. Their components come from `15-tax-rate-information.xlsx`, where they add up to the PDF total. The 2015 xlsx itself is incomplete for Concord and Loudon, so it is not used for those two, and its dollar columns are not used at all.
- **Hale's Location** has no 2014 row in DRA's 2014 file.
- **Full value rate vs. DOE equalized rate.** DRA computes the full value tax rate from "gross local property taxes … divided by the total equalized valuation including utility values and equalized railroad taxes" (DRA 2020 Comparison of Full Value Tax Rates, page II). This can differ from the DOE report's equalized total rate, sometimes by a lot. For example, Littleton 2025 is 13.44 (DRA) vs 10.92 (DOE), and Berlin 2024 is 23.42 vs 20.51.
- **Assessed rates aren't comparable across towns.** Equalization ratios move a lot when a town revalues: Acworth was 53.8 in 2024 and 99.46 in 2025. For comparisons between towns, DRA's full value rate or the DOE equalized rates are the comparable figures.

**Example: Hampton, 2014–2025** (rates per $1,000 of assessed value; DRA)

| Tax year | Municipal | County | Local education | State education | Total | School share (derived) | Equalization ratio | Full value rate |
|---|---|---|---|---|---|---|---|---|
| 2014 | 7.24 | 1.10 | 7.45 | 2.52 | 18.31 | 54.5% | 95.6 | |
| 2015 | 7.91 | 1.12 | 7.64 | 2.49 | 19.16 | 52.9% | 87.8 | |
| 2016 | 6.41 | 0.98 | 6.53 | 2.16 | 16.08 | 54.0% | 98.6 | |
| 2017 | 6.32 | 1.00 | 6.85 | 2.20 | 16.37 | 55.3% | 92.9 | |
| 2018 | 6.27 | 1.02 | 7.53 | 2.20 | 17.02 | 57.2% | 86.4 | 14.56 |
| 2019 | 5.92 | 0.94 | 7.16 | 1.99 | 16.01 | 57.2% | 93.9 | 14.79 |
| 2020 | 5.92 | 0.89 | 7.12 | 2.00 | 15.93 | 57.3% | 88.4 | 13.86 |
| 2021 | 5.91 | 0.89 | 7.10 | 1.94 | 15.84 | 57.1% | 75.4 | 11.80 |
| 2022 | 5.95 | 0.89 | 7.62 | 1.38 | 15.84 | 56.8% | 67.5 | 10.57 |
| 2023 | 5.98 | 0.89 | 7.99 | 1.89 | 16.75 | 59.0% | 62.6 | 10.36 |
| 2024 | 4.43 | 0.60 | 6.13 | 1.16 | 12.32 | 59.2% | 91.9 | 11.22 |
| 2025 | 4.71 | 0.61 | 6.13 | 1.16 | 12.61 | 57.8% | 89.68 | 11.20 |

In dollars (NH DOE valuations report), Hampton's local education tax was $21,317,805 in 2015 and $37,350,019 in 2025. Its state education tax was $6,769,141 and $6,813,213. The 2025 local figure includes $12,796,162.27 apportioned to the Winnacunnet Cooperative (DOE reference row; footnote C).

---

## school_tax_by_town: School Taxes by Town (NH DOE Valuations Report)

- unit: dollars (valuations and taxes); dollars per $1,000 (rates); percent (derived share)
- period: report years "2010-2011" through "2025-2026", which use tax years 2010–2025 (`tax_year`). `school_year` = 2010-11 … 2025-26
- source: NH DOE, Bureau of School Finance (Division of Education Analytics and Resources), "Valuations, Property Tax Assessments and Tax Rates of School Districts", read from the repo copies at `education-backend/backend/app/alembic/assets/equalized-value/equalized-value-2010.xls` … `equalized-value-2025.xlsx` (not modified). The 2019 repo file is byte-identical (same MD5) to `equalized-values-2019.xlsx` on the DOE "Financial Reports" page (https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/financial-reports), checked 2026-11-08
- as_of: repo files dated 2025-04-06 (2010–2023) and 2025-11-01 (2024–2025); read 2026-11-08
- raw: repo files above (not copied)
- review_by: 2027-11-08

**Report structure** (from the sheet and its Footnotes tab)

There are 15 numbered columns:
- (1) and (2): net assessed valuation, with and without utilities.
- (3) and (4): equalized valuation, with and without utilities.
- (5): local education tax assessment for schools.
- (6): other local property tax assessments (municipality and county).
- (7): state education tax assessment.
- (8)–(11): rates per $1,000 of assessed value (local education, other, state education, total).
- (12)–(15): the same rates per $1,000 of equalized value.

Each row has a district number ("Dist") and a town number ("Loc"); 2011–2016 also have county and SAU codes, and 2010 has no codes. Rows come in five kinds:

| Row kind | How to recognize it | Kept? | Rows per year (2025) |
|---|---|---|---|
| Single-town school district | Dist = Loc; name in the district column | Yes | 145 |
| Member town of a K-12 or regional cooperative | Loc = the town; name indented; rates shown | Yes | 100 |
| Cooperative or county total | Loc = 0 (or no codes, followed by member rows). The note on the sheet says coop rates "are not actual tax rates. They are weighted averages for the towns within that Cooperative." | No | 35 |
| "Reference only" member row | XXXX instead of rates, state tax and other-local tax. Coops marked "C" (footnote C) and Dresden "B" (footnote B, Hanover's share) | No; the coop's local education tax for that town is kept in column `reference_only_coop_rows` | 29 |
| TOTALS row and statistics | Below the table | Used for the reconciliation | — |

Footnote C (2025): "All figures for Exeter Region Coop, Hollis/Brookline Coop, John Stark Regional, Pemi-Baker Coop, Profile, Souhegan Coop and Winnacunnet Coop school districts are shown for reference only. The total Tax Assessments and Valuations for these towns are shown under …" their own districts. So for a town like Amherst, the town's own row already includes its Souhegan share: $13,720,641 of Amherst's $39,680,488 in 2025.

**Reconciliation with the TOTALS row** (kept rows vs the report's own total; the same holds for all seven columns, max difference $0.0004)

| Tax year | Kept rows | Local education tax, TOTALS row | Sum of kept rows | Sum of all rows (overcount) | State education tax, TOTALS row | Sum of kept rows |
|---|---|---|---|---|---|---|
| 2010 | 245 | 1,518,781,038 | 1,518,781,038 | 2,007,109,307 | 363,562,542 | 363,562,542 |
| 2011 | 245 | 1,570,851,682 | 1,570,851,682 | 2,077,117,005 | 363,086,707 | 363,086,707 |
| 2012 | 245 | 1,613,889,822 | 1,613,889,822 | 2,117,831,962 | 363,639,896 | 363,639,896 |
| 2013 | 245 | 1,689,930,090 | 1,689,930,090 | 2,216,948,160 | 363,563,724 | 363,563,724 |
| 2014 | 245 | 1,736,453,667 | 1,736,453,667 | 2,275,233,713 | 363,318,165 | 363,318,165 |
| 2015 | 245 | 1,786,530,618 | 1,786,530,618 | 2,334,055,733 | 363,109,425 | 363,109,425 |
| 2016 | 245 | 1,856,629,480 | 1,856,629,480 | 2,426,268,797 | 363,398,238 | 363,398,238 |
| 2017 | 245 | 1,941,848,847 | 1,941,848,847 | 2,543,695,896 | 363,116,484 | 363,116,484 |
| 2018 | 245 | 2,009,961,640 | 2,009,961,640 | 2,645,970,662 | 363,066,905 | 363,066,905 |
| 2019 | 245 | 2,092,961,123 | 2,092,961,123 | 2,746,580,818 | 363,214,190 | 363,214,190 |
| 2020 | 245 | 2,151,364,728 | 2,151,364,728 | 2,816,891,286 | 363,037,034 | 363,037,034 |
| 2021 | 245 | 2,188,550,415 | 2,188,550,415 | 2,858,453,982 | 363,245,325 | 363,245,325 |
| 2022 | 245 | 2,335,456,441 | 2,335,456,441 | 3,051,593,054 | 263,072,855 | 263,072,855 |
| 2023 | 245 | 2,464,297,405 | 2,464,297,405 | 3,232,792,140 | 363,753,627 | 363,753,627 |
| 2024 | 245 | 2,642,218,186 | 2,642,218,186 | 3,454,302,865 | 364,317,917 | 364,317,917 |
| 2025 | 245 | 2,790,227,910 | 2,790,227,910 | 3,643,421,419 | 363,492,715 | 363,492,715 |

Of the 245 kept rows, 237 match a site town each year. The other 8 are unincorporated places in the "Coos County" district: Cambridge, Dix Grant, Dixville, Martin's Location, Odell, Pinkham's Grant, Success and Wentworth Location.

**Cross-check with DRA** (column `matches_dra`; tolerance 1 cent on rates, $1 on dollars)
- **Local education rate:** matches DRA on every town-year 2014–2025 except Loudon 2020, which the DOE report prints as 0.00 for all rates even though its dollar figures are present.
- **State education rate:** 10 town-years differ by 1–2 cents (Merrimack 2014–2017; Portsmouth, Loudon and Springfield 2015–2017). Column 10's footnote says DOE's rates "may differ from actual tax rates, by a penny or so", because of property set-offs and rounding.
- **Total rate:** 1 other difference (Springfield 2018: 22.67 vs DRA 22.65).
- **Dollars, 2018–2025:** local education tax and state education tax equal DRA's "Local School Tax Effort" and "State Education Tax Effort" for every town. Concord matches once its DOE Concord and Penacook rows are added together, because DRA reports the whole city.
- **2010–2013:** no DRA comparison (`no DRA row`), and also Hale's Location in 2014.

**Columns**
- `town`, `town_id`, `tax_year`, `school_year`.
- `doe_row_name`, `doe_district_number`, `doe_row_type`, `cooperative_district`.
- The 15 report columns: `assessed_val_with_util` … `eq_rate_total`.
- `school_share_of_total_assessed_rate_pct_derived`: **derived**, (rate_local_educ + rate_state_educ) ÷ rate_total × 100.
- `reference_only_coop_rows`.
- `dra_*` comparison values, `matches_dra`, `source_file`.

**Caveats**
- **Concord and Penacook** are separate rows, following the DOE's school districts (Concord SD; Penacook in Merrimack Valley). Footnote K (2025): Penacook's school assessment was reduced by a $148,180 payment in lieu of taxes.
- **Hanover** is in the interstate Dresden district (footnote B) and **Orford** in Rivendell. Their own rows carry the totals.
- **Statewide state education tax** was about $263 million in tax year 2022 and about $363–364 million in the other years. The FY2023 adequacy file shows the statewide amount "If No $100 Million Reduction Occurred" as $363,632,069.
- **2010 rows** were matched by name, since that year has no town codes. "HAVERHILL COOP" was mapped to Haverhill, "MARLBORO" to Marlborough, and "ORFORD-Rivendell SD,VT" to Orford.

---

## adequacy_aid: State Adequacy Aid by Municipality (NH DOE)

- unit: as given per component (`unit` column: count of pupils (ADM), dollars, dollars per pupil, or fraction)
- period: fiscal years 2020–2027 (`fiscal_year` = the year the school year ends; FY2026 = 2025-26)
- source: NH DOE, "State Adequate Education Aid", https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/state-adequate-education-aid ("Data on Adequate Education Grants 2004-present"), Microsoft Excel files, plus each year's "How State Aid Was Determined" PDF
- as_of: 2026-11-08 (all files downloaded from the live page; server Last-Modified dates are in `sources.csv`)
- raw: `raw/town/doe/` (41 files: adequacy xlsx and pdf files, coop-split files, "explained" PDFs, the 2020-21 EVPP report)
- review_by: 2027-11-08

**Status of each year's file** (the page's own labels)

| FY | File | Page label |
|---|---|---|
| 2020 | `ad_ed_aid_fy2020_final.xlsx` | "FY 2020" (sheet title "FY2020 Final Grants", "as of 3-13-2020") |
| 2021 | `ad_ed_aid_fy2021.xlsx` | "FY 2021 (revised April 1, 2021)"; final grants column "as of 4-1-2021" |
| 2022 | `adequacy-fy-22-muni-summary.xlsx` | "FY 2022 Adequacy Aid (Revised April 1, 2022)" |
| 2023 | `adequacy-fy23-muni-estimate-summary.xlsx` | "FY 2023 Adequacy Aid (April 1, 2023)" |
| 2024 | `adequacy-fy-24-muni-summary-4.1.24_0.xlsx` | "FY 2024 Adequacy Aid (April 1, 2024)" |
| 2025 | `adequacy-fy-25-muni-summary-4.1.25.xlsx` | "FY 2025 Adequacy Aid- Final (April 1, 2025)" |
| 2026 | `adequacy-fy-26-muni-summary-4.1.26.xlsx` | "FY 2026 Adequacy Aid - Final (April 1, 2026)" |
| 2027 | `fy-27-adequacy-muni-summary.xlsx` | "FY 2027 Adequacy Aid - October 1, 2026". DOE's FY2027 explanation: "For the final calculation in April 2027, the total grant will be no less than 95% of the November 15, 2025 estimate." |

**Columns**
- `town`, `town_id`: from DOE's "Loc #", which is the site's town id.
- `fiscal_year`, `component`, `value` (copied exactly), `unit`.
- `source_label`: the DOE column heading, joined from the header rows.
- `doe_name`, `status`, `source_file`.

**Components** (names standardized across years; `source_label` keeps the DOE wording)
- **Pupils:** `resident_adm_base` (average daily membership in residence of the prior school year), `frl_adm`, `sped_adm`, `ell_adm`, `grade3_reading_adm` (FY2020–23), `home_education_adm` (FY2021, FY2025–27). FY2022 and FY2023 also give the separate years the DOE compared.
- **Cost of an adequate education:** `base_adequacy_aid`, `frl_differentiated_aid`, `sped_differentiated_aid`, `ell_differentiated_aid`, `grade3_reading_differentiated_aid`, `home_education_aid`, `total_cost_adequate_education`.
- **Statewide education property tax raised in the town:** `swept`.
- **Targeted aid:**
  - FY2021: `frl_pct_eligible`, `frl_additional_aid`, `fiscal_capacity_disparity_aid`.
  - FY2022–23: `relief_aid_frl_pct`, `relief_aid_unprorated`, `relief_aid_grant`.
  - FY2023–27: `extraordinary_need_grant`, plus `equalized_valuation`, `ev_per_frl_pupil` and `extraordinary_need_aid_per_frl_adm` (FY2024–27).
  - FY2027: `ev_per_pupil`, `fiscal_capacity_disparity_aid`.
- **Grant steps:** `preliminary_grant`.
- **Stabilization (FY2020–23):** `fy2012_stabilization_grant`, `stabilization_grant`.
- **Hold harmless:** `prior_estimate_*`, `hold_harmless_*`; FY2023 also has `swept_hold_harmless_grant`.
- **Totals:** `adequacy_grant` (the grant paid). From FY2022 on, also `final_total_state_grant`, which DOE labels "Final Total State Grant | Adequacy Grant & SWEPT Grant", that is, the adequacy grant plus the SWEPT.

**Reconciliation:** each year has 237 town rows plus 15 unincorporated places without numbers. Summed, they equal the file's "State Total" row for the cost of adequacy, the adequacy grant, the final total state grant, extraordinary need and fiscal capacity disparity aid, to the cent. SWEPT sums differ from the State Total by up to $6 (FY2020, FY2022, FY2023), where the State Total carries fractions.

**Cross-check with the valuations report:** for every town and every FY2020–FY2026, the adequacy file's SWEPT equals the state education tax in the DOE valuations report for the prior tax year (237 of 237 each year). For example, FY2026 SWEPT for Berlin is $665,317, which is Berlin's tax-year 2025 state education tax.

**Statewide figures** (per-pupil amounts from the file headers; totals from the "State Total" row)

| FY | Base per pupil | + F&R | + SPED | + ELL | Resident ADM | Cost of adequate education | SWEPT | Extraordinary need | Fiscal capacity disparity | Adequacy grant | Final total state grant |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2020 | 3,708.78 | 1,854.38 | 1,995.21 | 725.63 | 168,724 | 779,389,670 | 363,246,023 | — | — | 599,249,581 | — |
| 2021 | 3,708.78 | 1,854.38 | 1,995.21 | 725.63 | 167,284 | 769,142,374 | 363,068,238 | — | 47,505,897 | 649,510,186 | — |
| 2022 | 3,786.66 | 1,893.32 | 2,037.11 | 740.87 | 167,499 | 788,588,331 | 363,283,230 | — | — | 624,823,445 | 988,106,670 |
| 2023 | 3,786.66 | 1,893.32 | 2,037.11 | 740.87 | 159,397 | 753,439,489 | 263,098,498 | 14,318,854 | — | 707,519,581 | 970,618,080 |
| 2024 | 4,100 | 2,300 | 2,100 | 800 | 157,397 | 810,282,624 | 363,786,975 | 178,655,457 | — | 701,480,825 | 1,065,267,800 |
| 2025 | 4,182 | 2,346 | 2,142 | 816 | 154,925 | 817,869,206 | 364,350,537 | 158,650,596 | — | 700,016,284 | 1,064,366,821 |
| 2026 | 4,265.64 | 2,392.92 | 2,184.84 | 832.32 | 152,140 | 819,756,298 | 363,516,836 | 180,866,781 | — | 716,082,728 | 1,079,599,564 |
| 2027 | 4,351 | 2,441 | 2,229 | 849 | 149,043 | 815,557,326 | 364,075,715 | 148,081,489 | 10,277,616 | 690,800,747 | 1,054,876,462 |

Dollars are rounded to the nearest dollar in this table; the CSV has the exact values. FY2020–21 also paid a grade 3 reading amount of $725.63, and FY2022–23 $740.87. FY2020 and FY2021 files have no "Final Total State Grant" column; adequacy grant + SWEPT would be a **derived** equivalent. The SWEPT equalized rates DOE shows are $2.06 (FY2020), $1.925 (FY2021), $1.220 (FY2025), $1.120 (FY2026) and $1.030 (FY2027).

**Caveats**
- **Which column is the "state share".** DOE's "Final Total State Grant" counts the statewide education property tax (raised locally, kept by the district) together with the adequacy grant. DOE's FY2027 explanation says SWEPT "is a State tax, not a local tax". For "how much of Littleton's school money comes from the state", report the two parts separately. Littleton FY2026 final: adequacy grant $4,291,544.24 plus SWEPT $1,225,747, a final total state grant of $5,517,291.24.
- **The formula changes from year to year.** Stabilization ended after FY2023, extraordinary need began in FY2023, and fiscal capacity disparity aid was paid in FY2021 and again from FY2027. Hold harmless rules differ by year, so component lists differ.
- **Coop splits.** The "Co-op Splits" files show how a town's grant is divided among its school districts. They are saved in `raw/town/doe/` but not converted.

---

## Equalized Valuation per Pupil (item 4)

- **FY2027:** `adequacy-aid.csv`, component `ev_per_pupil`. DOE label: "Fiscal Capacity Disparity Aid | Based on EV Per Pupil (EVPP) / Sliding Scale Grant with $1,250 per ADM-R for EVPP Under $1.0 million and $0 for EVPP over $1.6 million. | EV Per ADM". Examples: Berlin $1,153,001.55, which gives fiscal capacity disparity aid of $846,043.32. Amherst $1,967,680.81, Hampton $4,908,634.08, Littleton $2,881,391.80, Lyme $2,340,737.70 (no such aid for these four).
- **FY2023–FY2027:** `ev_per_frl_pupil` (equalized valuation per free/reduced-price-meal pupil, used for extraordinary need). `equalized_valuation` for FY2024–FY2027.
- **2020-21 standalone report:** "EQUALIZED VALUATION PER PUPIL, 2020-2021" (`raw/town/doe/EVPP-FY-2021-Excel_0.xlsx`, from the DOE Financial Reports page). It is the only EVPP report posted there. It is organized by school district, with member towns in parentheses, and notes that towns in two districts need their two amounts added. It was not converted to a town table, because its rows did not reconcile to its state total in a first pass. Printed statistics: state average $1,346,793, median $1,274,149.5, low $523,285, high $120,861,443.

---

## Spot Checks: Amherst, Berlin, Hampton, Littleton, Lyme

**Tax year 2025: DRA vs the NH DOE valuations report vs the FY2026 adequacy file**

| Town | Local ed. rate DRA / DOE | State ed. rate DRA / DOE | Total rate DRA / DOE | Local school tax $ DRA / DOE | State ed. tax $ DRA / DOE / FY2026 SWEPT | Result |
|---|---|---|---|---|---|---|
| Amherst | 16.24 / 16.24 | 1.49 / 1.49 | 23.98 / 23.98 | 39,680,488 / 39,680,488 | 3,511,304 / 3,511,304 / 3,511,304 | agree |
| Berlin | 12.66 / 12.66 | 1.24 / 1.24 | 33.60 / 33.6 | 9,496,005 / 9,496,005 | 665,317 / 665,317 / 665,317 | agree |
| Hampton | 6.13 / 6.13 | 1.16 / 1.16 | 12.61 / 12.61 | 37,350,019 / 37,350,019 | 6,813,213 / 6,813,213 / 6,813,213 | agree |
| Littleton | 8.53 / 8.53 | 1.01 / 1.01 | 14.10 / 14.1 | 11,387,024 / 11,387,024 | 1,225,747 / 1,225,747 / 1,225,747 | agree |
| Lyme | 18.60 / 18.6 | 1.69 / 1.69 | 28.19 / 28.19 | 7,752,478 / 7,752,478 | 697,467 / 697,467 / 697,467 | agree |

Lyme's 2025 DRA row (6.41 municipal, 1.49 county, 18.60 local education, 1.69 state education, 28.19 total) also matches the town's DRA-approved final rate sheet (https://www.lymenh.gov/uploads/2025_final-taxrate_40.pdf), cited in the test answers.

**Ten-year view (DRA rates; derived school share; DOE dollars)**

| Town | 2015 total / local / state (school share) | 2025 total / local / state (school share) | Local education tax $ 2015 → 2025 | State education tax $ 2015 → 2025 |
|---|---|---|---|---|
| Amherst | 26.48 / 17.39 / 2.41 (74.8%) | 23.98 / 16.24 / 1.49 (73.9%) | 27,426,323 → 39,680,488 | 3,701,716 → 3,511,304 |
| Berlin | 39.19 / 13.76 / 2.92 (42.6%) | 33.60 / 12.66 / 1.24 (41.4%) | 5,459,593 → 9,496,005 | 734,425 → 665,317 |
| Hampton | 19.16 / 7.64 / 2.49 (52.9%) | 12.61 / 6.13 / 1.16 (57.8%) | 21,317,805 → 37,350,019 | 6,769,141 → 6,813,213 |
| Littleton | 23.32 / 11.55 / 2.58 (60.6%) | 14.10 / 8.53 / 1.01 (67.7%) | 8,728,736 → 11,387,024 | 1,257,813 → 1,225,747 |
| Lyme | 24.63 / 13.97 / 2.45 (66.7%) | 28.19 / 18.60 / 1.69 (72.0%) | 4,616,513 → 7,752,478 | 794,962 → 697,467 |

Rates are per $1,000 of *assessed* value, so a fall in a rate can reflect a revaluation. Littleton's equalization ratio was 55.9 in 2024 and 96.14 in 2025. Read rates over time together with the ratio, or use the dollar amounts.

**FY2026 adequacy aid (final, April 1, 2026)**

| Town | Resident ADM | Cost of adequate education | SWEPT | Extraordinary need | Hold harmless (80% of FY2025) | 95% hold harmless | Adequacy grant | Final total state grant |
|---|---|---|---|---|---|---|---|---|
| Amherst | 1,790.7205 | 8,735,717.09 | 3,511,304 | 0 | 0 | 0 | 5,224,413.09 | 8,735,717.09 |
| Berlin | 909.6057 | 5,567,227.43 | 665,317 | 5,971,482.22 | 1,163,967.53 | 0 | 12,037,360.18 | 12,702,677.18 |
| Hampton | 1,366.1962 | 6,972,333.51 | 6,813,213 | 0 | 0 | 35,858.67 | 194,979.18 | 7,008,192.18 |
| Littleton | 565.8282 | 3,476,322.80 | 1,225,747 | 1,518,428.60 | 522,539.84 | 0 | 4,291,544.24 | 5,517,291.24 |
| Lyme | 269.8006 | 1,266,459.09 | 697,467 | 0 | 0 | 0 | 568,992.09 | 1,266,459.09 |

Cents are rounded in this table where the file carries more digits (e.g. cost of adequacy 8,735,717.091).

FY2027 (October 1, 2026 calculation) adequacy grants:
- Amherst $5,257,753.93
- Berlin $12,320,878.17, including $5,427,978.18 extraordinary need and $846,043.32 fiscal capacity disparity aid
- Hampton $428,980
- Littleton $4,099,570
- Lyme $637,048.37

---

## How the Taxes and Aid Work (reference facts for these figures)

- kind: how_it_works
- question_type: governance_money

1. The Commissioner of Revenue Administration sets the statewide education property tax rate to raise $363,000,000 a year statewide.
   - citation: RSA 76:3
   - source: https://gc.nh.gov/rsa/html/V/76/76-3.htm
   - as_of: 2026-11-08 (checked in the test-answer research)
   - review_by: 2027-08-15
2. Each town assesses its share of the statewide education tax and pays it to the town's school district or districts; local property taxes fund school appropriations not covered by the education tax, state education trust fund money or other revenue.
   - citation: RSA 76:8, II and III
   - source: https://gc.nh.gov/rsa/html/V/76/76-8.htm
   - as_of: 2026-11-08
   - review_by: 2027-08-15
3. A municipality's education grant is the total adequacy cost for its pupils, minus its statewide education property tax warrant, plus its extraordinary need grant and fiscal capacity disparity aid grant.
   - citation: RSA 198:41, I
   - source: https://gc.nh.gov/rsa/html/XV/198/198-41.htm
   - as_of: 2026-11-08
   - review_by: 2027-08-15
4. For FY2027, NH DOE says the base per-pupil rate is $4,351 per ADM, plus $2,441 per free or reduced-price meal eligible student, $2,229 per special education student with an IEP, and $849 per English learner receiving English language instruction; the previous school year's (2025-26) ADM is used.
   - citation: NH DOE, "FY 2027 Adequate Education Aid" explanation
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/adequacy-explained-fy-2027.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
5. NH DOE says the FY2027 SWEPT uses a tax rate of $1.03 per thousand applied to April 1, 2024 equalized values, and that municipalities collect the SWEPT and send it directly to their school districts.
   - citation: NH DOE FY2027 explanation (citing RSA 76:3 and 76:8)
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/adequacy-explained-fy-2027.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
6. Extraordinary need grants (FY2027) go to municipalities whose equalized valuation per free/reduced-meal pupil is under $7,003,972, at $11,730 per such pupil below $1,697,933 and on a sliding scale in between. Fiscal capacity disparity aid goes to municipalities with equalized valuation per pupil under $1,600,000, at $1,250 per pupil below $1,000,000 and on a sliding scale in between.
   - citation: NH DOE FY2027 explanation; RSA 198:40-f and 198:40-g
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/adequacy-explained-fy-2027.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
7. NH DOE publishes a first adequacy estimate on November 15 before the fiscal year, a second calculation on September 1 used by DRA to set school tax rates, and adequacy figures used to set taxes must reach DRA by October 1; grants are paid 20% September 1, 20% November 1, 30% January 1 and 30% April 1.
   - citation: NH DOE FY2027 explanation (citing RSA 198:41, V)
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/2026/adequacy-explained-fy-2027.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
8. DRA's full value tax rate "represents the estimated tax rate for a municipality if all the taxable property was assessed at 100%", and DRA notes it "can only be used to make a limited comparison" between municipalities.
   - citation: DRA, 2020 Comparison of Full Value Tax Rates, page II
   - source: https://www.revenue.nh.gov/mun-prop/property/equalization-2020/documents/20-comp-of-full-value-tax-rates-ranking-order.pdf
   - as_of: Wayback snapshot 2024-06-22
   - review_by: 2027-11-08

---

## Name Matching

- **DRA:** names were matched to the site's `town` table after normalizing case, punctuation, "(P)", "(U)" and "Loc." ("Concord (Penacook)" and "Penacook" map to Penacook). Not matched, and left out: the unincorporated places Atkinson & Gilmanton Academy Grant, Bean's Grant, Bean's Purchase, Cambridge, Chandler's Purchase, Crawford's Purchase, Cutt's Grant, Dix Grant, Dixville, Erving's Grant, Green's Grant, Hadley's Purchase, Kilkenny, Livermore, Low & Burbank's Grant, Martin's Location, Odell, Pinkham's Grant, Sargent's Purchase, Second College Grant, Success, Thomson & Meserve's Purchase and Wentworth's Location.
- **NH DOE (valuations and adequacy):** matched by DOE town number ("Loc"), which equals the site's town id. Not in the site table: 73 Cambridge, 133 Dix Grant, 134 Dixville, 344 Martin's Location, 414 Odell, 436 Pinkham's Grant, 514 Success and 561 Wentworth Location. The adequacy files also list 15 more unincorporated places with letter codes instead of numbers.
- **Site towns with no tax or aid rows:** Gonic (462, part of Rochester), Coe-Brown Academy (998), Pinkerton Academy (999) and Prospect Mountain (970) are not municipalities in these sources. Hale's Location (222) has no DRA row for 2014.

## Not Retrieved

- **DRA full value tax rates for 2014–2017.** No file was found in the Wayback CDX listings for `revenue.nh.gov/mun-prop/property/equalization-2016/*` and `-2017/*`, and the live equalization page links only 2020–2025. The 2015 "Tax Rate Comparison" PDF (`dra/tax-rate-comparison-alpha.pdf`) has ratio, equalized valuation and component rates but no single full value rate, so it was not used for that column.
- **DRA 2016–2017 tax-rate calculation data** (school tax dollars). Not found in the archive. The DOE valuations report covers those dollars.
- **DRA 2026 rates** for the towns not yet set as of October 30, 2026. Check https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/2026-municipal-tax-rates.pdf again after December.
- **The original NH DOE URLs for the repo's equalized-value files**, other than 2019. Only `equalized-values-2019` (and older `valuation07_08`/`valuation08_09`) are linked on the DOE Financial Reports page today.
- **A town-level EVPP table** from the 2020-21 report: not converted (see item 4 above).
