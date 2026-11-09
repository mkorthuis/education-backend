# Programs and Help (Type 4: Finding help and programs)

Where families can find preschool (Head Start), EFA schools and providers, career and technical education (CTE) centers, college courses in high school, after-school programs, help paying for college, and who to call for help. This file covers **where and who**: locations, contacts, what each organization does and how to apply. Eligibility *rules* (Head Start, child care scholarship, EFA, dual enrollment law) are in `facts-rules-and-rights.md`.

Gathered November 8, 2026. Format and rules: see `README.md`.

## Summary

**Directories (CSV files in `raw/programs/`)**

| File | What it lists | Rows | Source and date |
|---|---|---|---|
| `head-start-sites-nh.csv` | Head Start and Early Head Start sites in NH | 45 rows (35 addresses; 28 towns) | HHS Office of Head Start locations file, downloaded 2026-11-08 (file dated 2026-11-08) |
| `efa-providers.csv` | Every school, tutor, therapist, vendor and other provider in the EFA marketplace | 3,606 (1,788 in NH, including 347 schools) | Children's Scholarship Fund NH marketplace feed (**undocumented**), 2026-11-08 |
| `efa-stats-by-town-2026-27.csv` | EFA students, priority, income, special needs and waitlist by town, 2026-27 | 229 towns | CSF NH stats feed (**undocumented**), 2026-11-08 |
| `cte-centers.csv` | CTE centers with host SAU and district, region, website | 33 (28 NH, 5 VT) | NH DOE CTE page and center lists (2022-23 list, updated 8/23/2022), checked 2026-11-08 |
| `cte-programs-2025.csv` | Which centers offer each of 17 program areas (CIP codes) | 292 center-program rows | NH DOE "CTE Program Grid - 2025" (PDF dated 2025-04-29), checked 2026-11-08 |
| `community-colleges-early-college.csv` | The 7 NH community colleges: address, phones, Early College coordinator, high schools each coordinator serves | 7 | CCSNH Locations and Early College contacts pages, 2026-11-08 |
| `21cclc-sites.csv` | Federally funded after-school programs (21st Century Community Learning Centers) by school | 53 school sites, 17 grantees | NH DOE 21st CCLC contact list "updated 9-2026", checked 2026-11-08 |
| `area-agencies.csv` (+ `-towns-served`) | The 10 area agencies for developmental services and the towns each serves | 10 (243 town rows) | NH DHHS BDS PDF, contacts "Effective 9/29/25" (Wayback 2025-12-07) |
| `fcess-programs.csv` (+ `-towns-served`) | Early Supports and Services (birth to 3) programs by region, with intake numbers | 14 (274 town rows) | NH DHHS FCESS directories, September and March 2025 (Wayback 2025-10-31) |
| `family-resource-centers.csv` | Family Resource Centers | 27 (23 cities) | NH DHHS FRC map data (Wayback 2025-10-31) |
| `community-mental-health-centers.csv` (+ `-towns-served`) | The 10 community mental health centers, 32 other offices, the statewide crisis line | 43 (238 town rows) | NH DHHS list "Updated 1/18/22" and 2025 location data (Wayback 2025-10-31) |
| `vocational-rehabilitation-offices.csv` (+ `-towns-served`) | VR New Hampshire offices and the towns each covers | 9 (293 town rows) | NH DOE VR pages (Wayback 2025-08-31) |

All CSVs have `town_id` and `town` columns matched to the site's `town` table (241 towns); the `*-towns-served.csv` files give one row per organization per town served, for a `find_programs(kind, town)` lookup. Matching is by exact town name first; when the name doesn't match (usually a village or a typo) the row was matched from its latitude/longitude or street address with the U.S. Census Geocoder's county subdivision (NH towns and cities), shown in `town_match` as `name`, `census_latlong` or `census_address`. Unmatched rows are left blank and listed under each file.

**Facts (topics below):** Head Start; EFA applications and the provider list; CTE centers; Early College (Running Start) and other college courses in high school; the community colleges; Parent Information Center; Child Care Aware, NH Child Care Search and the Child Care Scholarship; 211 NH; NAMI NH; kinship caregivers; military families; refugee and immigrant families; NH DOE special education help; after-school programs; paying for college (NH Promise, CCSNH tuition, Granite Edvance, NH 529 plans, Orphans of Veterans scholarship, FAFSA); area agencies; Early Supports and Services (birth to 3); Family Resource Centers; community mental health centers and the crisis line; VR New Hampshire. 32 topics, 106 statements.

**As-of dates.** Live pages and feeds were checked 2026-11-08. dhhs.nh.gov and education.nh.gov block scripts: the Head Start, child care, CTE and 21st CCLC pages were opened in a visible browser on 2026-11-08, while the area agency, FCESS, Family Resource Center, mental health, VR and some NH DOE contact pages come from Wayback copies dated August 2025 to October 2026 (each statement gives its snapshot date).

**Main gaps** (details in *Not retrieved*):
- CTE sending schools are found for 17 of 26 NH centers, and the CTE grid lists broad program areas, not specific trades such as welding.
- The mental health town lists date from 2022, and the current FCESS directory isn't archived.
- No list says which towns each Family Resource Center covers.
- No current Purple Star schools list, and no school liaison is listed for Pease.
- The UNH First Step page is blocked (a 2024 copy was used), and 211nh.org didn't resolve (an archived copy was used).
- No state-funded college grant was found; the web-search budget ran out before a full search.
- The EFA feeds are undocumented and could change without notice.

---

## Directories

### head-start-sites-nh.csv: Head Start and Early Head Start Sites

- source: HHS Office of Head Start, Head Start Service Location Dataset, national CSV — https://s3foa.s3.us-east-1.amazonaws.com/HS_Service_Locations.csv (linked from https://www.headstart.gov/about-us/article/head-start-service-location-datasets)
- as_of: 2026-11-08 (file Last-Modified 2026-11-08 05:01 GMT); data dictionary read from the datasets page, Wayback snapshot 2026-10-26
- rows: 45 NH rows out of 19,507 national rows. One row per site per program type, so a site with both Head Start and Early Head Start has two rows (35 distinct addresses in 28 towns).
- columns: `town_id`, `town`, `town_match`, `service_location_name`, `program_type` (code), `program_type_label`, `status`, `funded_slots`, `address_line_one`, `address_line_two`, `city`, `state`, `zip`, `county`, `latitude`, `longitude`, `service_location_phone_number`, `registration_phone_number`, `recipient_name`, `grant_number`, `program_admin_name`, `program_admin_id`, `program_admin_address_line_one`, `program_admin_city`. Values are as given in the file.
- program types (from the data dictionary): 1 = Head Start Preschool, 2 = Early Head Start, 3 + 4 = Migrant and Seasonal Head Start, 5 = American Indian and Alaska Native Head Start, 6 = American Indian and Alaska Native Early Head Start. NH has only types 1 and 2.
- status (from the data dictionary): "Open: Currently, children/pregnant women are receiving services at the designated location. Closed: Currently, children/pregnant women are not receiving services at the designated location. … Scheduled holidays, summer breaks, and short term closures (ex. snow days) are not represented in this status."
- counts: Head Start Preschool 25 Open, 1 Closed, 8 "Not Reported"; Early Head Start 10 Open, 1 Closed. Funded slots total 879 Head Start and 260 Early Head Start; at Open rows, 698 and 244 (**derived**: sums of `funded_slots`).
- grantees (5 grants): Southern New Hampshire Services, Inc. (15 rows; several sites are named "CAPHR Head Start…"), Belknap-Merrimack Counties Community Action Program (9), Community Action Partnership of Strafford County (8), Tri County CAP Head Start (8), Southwestern Community Services, Inc. (5).
- caveats:
  - The data dictionary says: "Location data is self-reported and kept up-to-date by each grant recipient." The file "refreshes once a day" and "Daily archives of this data are not available."
  - Funded slots "may be funded by the Office of Head Start (OHS), state funds, tribal funds, other federal programs, or additional non-OHS sources." They are not open seats.
  - All 8 Tri County CAP sites (North Country and Lakes Region) show status "Not Reported", not Open.
  - Closed rows: Early Head Start Nashua (88 Temple St) and Milton Children's Center (55 Industrial Way, Milton).
  - Registration phone numbers are written as the file gives them, e.g. "(603)668-8010 - 6034".
  - The NH DHHS Head Start Collaboration Office page lists 34 NH locations (checked 2026-11-08) and names the Hillsborough/Rockingham grantee "Community Action Partnership Hillsborough and Rockingham Counties". Addresses there are close to, but not always identical with, the HHS file (e.g. "67 Old Louson Road" vs "67 Old Loudon Rd" in Concord). Use the HHS file as the directory and the DHHS page as a cross-check.
- town matching: 44 by name; Groveton Area Head Start (Groveton is a village) matched to Northumberland from its latitude/longitude. None unmatched.

### efa-providers.csv: EFA Schools and Providers

- source: Children's Scholarship Fund NH (CSF) marketplace feed — https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors. This is the data behind the EFA marketplace page (https://app.nh.scholarshipfund.org/marketplace, which needs JavaScript).
- **undocumented:** the endpoint isn't published or documented and could change or disappear without notice. Field meanings below are inferred from the data, not from documentation.
- as_of: 2026-11-08
- rows: 3,606 providers. 1,788 are in New Hampshire (state field "NH", "New Hampshire" or "US-0-NH", or NH in the address); the rest are out-of-state or online-only.
- by `organization_type` (as given): provider 1,731 (NH 1,001), vendor 772 (NH 108), school 545 (NH 347), tutor 474 (NH 258), therapy 84 (NH 74).
- columns: `provider_id`, `name`, `organization_type`, `low_grade`, `high_grade`, `street`, `city`, `state`, `address`, `latitude`, `longitude`, `in_nh` (**derived**, see above), `town_id`, `town`, `town_match`, `tags` (provider-chosen labels, joined with "; ").
- caveats:
  - Grades are numbers as given; 0 appears to mean kindergarten, but the feed doesn't say. 858 providers have no grades.
  - 781 providers (383 in NH) have no latitude/longitude.
  - The feed's yes/no flags (`is_private`, `is_charter`, `is_public`, `is_virtual`, `is_microschool`, `has_vouchers`, `has_sgo`) are false for every provider, so they were left out. The free-text `description` and `logo` fields were also left out (the provider's own marketing text).
  - Being listed means the provider is in the marketplace; the feed says nothing about quality, accreditation or openings. List providers without ranking them.
  - City names are typed by providers and include villages and typos.
- town matching (NH rows): 1,692 by name, 66 from latitude/longitude, 30 unmatched. Unmatched city values (count): Jaffery 4, North Haverhill 2, Center Barnstead 2, North Conway 2, and one each of Ringe, Gilmanton Iron Works, Ctr. Tuftonboro, Merrmiack, Lochmere, Woodsville, "Newport, NH", Porstmouth, Manchster, Center Conway, Georges Mills, Somerset, Alton Bay, Suncook, New Hampston, Lebenon, Haverhill Corner, Somersowrth, Cornish Flat, and one blank city. These have no coordinates; they were left blank rather than corrected by hand.
- summary: NH providers are in 199 of the site's towns; NH schools in 119 (**derived**: distinct matched towns).

### efa-stats-by-town-2026-27.csv: EFA Students and Waitlist by Town

- source: CSF NH stats feed — https://nhefa.scholarshipfund.org/api/admin/stats, the data shown under "View Stats" on https://nhefa.scholarshipfund.org/ (page title "ScholaVia - NH Education Freedom Accounts")
- **undocumented:** no published documentation. Column meanings come from the labels on the public page that displays this feed.
- as_of: 2026-11-08; school year as given: "2026-2027"
- rows: 229 towns. All 229 match the site's town table by name. Site towns with no row: Chatham, Clarksville, Dorchester, Ellsworth, Groton, Hale's Location, Hart's Location, Millsfield, plus the site's non-town rows (Coe-Brown Academy, Gonic, Pinkerton Academy, Prospect Mountain).
- columns (page label in brackets): `source_town`, `eligible_count` [Eligible Students], `priority_count` / `non_priority_count` [Priority vs Non-Priority], `frl_count`, `frl_percent` [Qualified by Income], `sped_count`, `sped_percent` [Students with Special Needs], `waitlist_count` [Waitlist], `est_total_j15`, `est_priority_j15`, `est_non_priority_j15` [Estimated by July 15; blank in this pull, so the page hides them].
- statewide values in the same feed (2026-2027): eligible students 13,757; priority 13,275; non-priority 482; qualified by income 10,409 (75.7%); students with special needs 1,559 (11.3%); `max_students` 12,500; `funded_count` 13,159; waitlist 476. When `funded_count` is above zero the page shows the larger of `max_students` and `funded_count` under the label "Enrolled" (13,159); otherwise it shows `max_students` as "EFA Cap".
- check: town counts sum to 13,757, the statewide eligible figure; town waitlists sum to 476 (**derived**).
- caveat: these are counts of applicants in CSF's system as of the download date and change daily during the application year. The site's existing EFA tables (from NH DOE) are the official counts.

### cte-centers.csv: Career and Technical Education Centers

- sources:
  - NH DOE, "CTE Programs in New Hampshire" — https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-of-career-development/cte-programs-in-new-hampshire (31 centers with website links; viewed in a browser 2026-11-08; Wayback snapshot 2025-11-27 identical list)
  - NH DOE, "NH CTE Centers for the 2022-2023 School Year (Updated 8/23/2022)" — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/cte-centers-info-22-23.pdf (33 centers; base of the CSV)
  - NH DOE, "CTE Centers by District, SAU, and Region" (the file the CTE page links today; created 2021-02-03; 32 centers, no North Point) — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/cte-center-region-sau-dist.pdf
  - NH DOE, "NH MAP 2023" (CTE regional centers and satellites, region numbers 01–20) — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/nh_map_satellites_regions.pdf
- as_of: 2026-11-08. The PDFs downloaded in a browser from education.nh.gov on 2026-11-08 were byte-for-byte identical to the Wayback copies (2025-08-31 and 2026-09-16).
- rows: 33 (28 in NH, 5 in Vermont).
- columns: `center_id` (NH DOE school ID), `center_name` (2022-23 list), `center_town_as_given`, `state`, `town_id`, `town`, `sau_number`, `sau_name`, `district_id` (the NH DOE district number, which is also the site's `district.id`), `district_name`, `region_name` (2022-23 list), `map_region_number` (2023 map), `doe_page_name` and `website` (CTE page), `in_2021_list`, then `sending_schools` (names exactly as the center lists them, joined with "; "), `sending_wording` (the heading or sentence the list appears under), `sending_source`, `sending_as_of`, `phone`, `address`, `how_to_apply` from the centers' own websites where found (see caveats).
- caveats:
  - Conant High School CATE (Jaffrey) and Mascenic Regional High School CATE (New Ipswich) are in both center lists but not on the current CTE page or in the 2025 program grid.
  - The region names differ between files for one center: River Bend (Bradford, VT) is "Southwest" in the 2021 list and "Out of State" in the 2022-23 list.
  - The map region number was matched by the center's town as printed on the map (e.g. "08 LACONIA", "08 TILTON").
  - Vermont centers have no `town_id` (not NH towns).
  - Sending schools: not in any NH DOE file. They come from each center's own site (or, for Creteau and Manchester School of Technology, Wayback copies from April and May 2026, because those sites block scripts). Found for 17 of the 26 NH centers on the current NH DOE list, and for 4 of the 5 Vermont centers (NH schools only). Blank means not found (see *Not retrieved*). Most pages are undated.
  - The lists differ in kind: some name high schools, some districts or towns (Region 14, Dover, Palmer, whose list ends "and others"), and Creteau's is its partnership with Dover and Somersworth rather than a list labeled "sending schools". Typos are kept as shown (e.g. "Northwoord" on Dover's list).
  - Canaan Career Center's one NH school (Colebrook Academy) comes from a Colebrook Academy course guide, not Canaan's own site.

### cte-programs-2025.csv: CTE Programs by Center

- source: NH DOE, "CTE Program Grid - 2025" — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/cip-code-cte-program-grid_0.pdf (21 pages, PDF created 2025-04-29), linked from the CTE page
- as_of: 2026-11-08
- rows: 292 (one per program area per center); 17 program areas; 31 centers.
- columns: `cip_code_as_given`, `cip_code` (**derived**: "120401" written as "12.0401" and "46.000" as "46.0000"; the grid has no CIP code for JROTC), `program_name` (as given), `grid_school_town_as_given`, `center_id`, `center_name`, `center_town`, `center_state`, `town_id`, `town`, `grid_pages`.
- program areas (centers offering): Agriculture, General 01.0000 (17); Aeronautics/Aviation/Aerospace Science and Technology, General 49.0101 (4); Business/Commerce, General 52.0101 (23); Computer and Information Sciences, General 11.0101 (23); Cosmetology/Cosmetologist, General 12.0401 (11); Restaurant, Culinary and Catering Management/Manager 12.0504 (24); Digital Communication and Media/Multimedia 09.0702 (19); Drafting and Design Technology, General 15.1301 (13); Education, General 13.0101 (19); Manufacturing Technology/Technician 15.0613 (21); Construction Trades 46.0000 (24); Engineering Technology, General 15.0000 (20); Biotechnology 26.1201 (5); JROTC (4); Law and Protective Services 43.9999 (13); Transportation and Materials Moving 49.0000 (24); Health Services/Allied Health/Health Sciences, General 51.0000 (28).
- caveats:
  - The grid names centers by short names ("MST", "CRTC", "Arthur Paradice"). Each was linked to `cte-centers.csv` by its town (**derived**); "Cannan, VT" was read as Canaan and "North Conway" as the Conway center (the centers list gives the Mt. Washington Valley center's town as Conway).
  - The grid lists broad program areas only. It doesn't say whether a center teaches welding, machining or another specific trade (those fall under areas like Manufacturing Technology but the grid doesn't break them out). Specific programs are on each center's website.
  - Parsed from the PDF by position and checked: the count of each town in the PDF text matches the CSV.

### community-colleges-early-college.csv: Community Colleges and Early College Coordinators

- sources: CCSNH "Locations" — https://www.ccsnh.edu/locations/ ; "Early College At Your High School Contacts" — https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/running-start-contacts/
- as_of: 2026-11-08
- rows: 7 (Great Bay, Lakes Region, Manchester, Nashua, NHTI, River Valley, White Mountains).
- columns: `college`, `abbreviation`, `street`, `city_state_zip`, `town_id`, `town`, `main_phone`, `admissions_phone`, `college_contact_page`, `early_college_coordinator`, `coordinator_phone`, `coordinator_email`, `high_schools_served_as_listed`.
- caveats: phone numbers as shown (formats differ). The high-school lists are copied as written on the contacts page, including its punctuation (e.g. "White, Mountains Regional", "John Stark, Regional"). Emails were shown on the page through Cloudflare's email protection and were decoded from the page itself. Coordinator names change; review yearly.

### 21cclc-sites.csv: After-School Programs (21st Century Community Learning Centers)

- source: NH DOE, "21st CCLC Program Contact Information" (PDF "21-cclc-program-contact-information-updated-9-2026", created 2026-09-11) — https://www.education.nh.gov/sites/g/files/ehbemt326/files/media/media_document/21-cclc-program-contact-information-updated-9-2026_0.pdf, linked from https://www.education.nh.gov/21cclc (both opened in a browser 2026-11-08)
- as_of: 2026-11-08
- rows: 53 school sites under 17 grantees (15 school districts and 2 community-based organizations). The NH DOE page says "42 Grants, 52 Sites, 17 School Districts and Community Based Organizations".
- columns: `grant_row`, `subgrantee`, `district_id` (from "(Distr N)"; for the two community organizations, the district of the school served, **derived**), `school_site_as_given`, `school_name`, `grades`, `school_id` and `school_match` (match to the site's `school` table; `manual` = matched by hand from a clearly similar name), `program_name`, `program_director`, `phone`, `email`, `address` (the program's office), `town_id`, `town`, `town_match` (of the office address), `grant_cohort`, `school_town_id`, `school_town` (the school's town in the site's database).
- grantees and towns: Berlin, Concord, Conway, Franklin, Friends of Seabrook Community, Haverhill, Hinsdale, Laconia, Manchester (14 schools), Monadnock Regional (Fitzwilliam, Swanzey, Troy), Nashua (7), Newfound Regional (Bristol), Governor Wentworth (Ossipee), Portsmouth, Raymond, Rumney, Dover Housing Authority (Woodman Park School, Dover).
- caveats:
  - These are the federally funded programs only, not every after-school or summer program. There is no 21st CCLC site in Claremont in this list.
  - Merged cells in the PDF were filled down (each school row repeats its grantee's contact).
  - The January 2025 version of the list (34 grant rows, 54 sites; Wayback 2026-01-08) also included Winchester ACCESS; it isn't in the September 2026 list.
  - "Jewett Street Elementary School" was matched by hand to the site's "Jewett School" (marked "check").

### Family support directories

Five directories, each with a matching `*-towns-served.csv` (one row per organization per town it serves, with `town_id`) where the source gives a town list. dhhs.nh.gov and education.nh.gov returned 403 to scripts, so these come from Wayback copies of the agencies' own pages and files (dates below). All phone numbers were checked against the saved source files. Common columns: `town_id`, `town`, `town_match` (of the office address), `name`, `region`, `address`, `city`, `phone`, `website`, `towns_served` (as written, joined with "; "), `source_url`, `as_of`, `note`.

Town-list spellings are kept as the source writes them, so some don't match the site's town names and have a blank `town_id` in the towns-served files (e.g. "Hillsboro" for Hillsborough, "Mt. Vernon" for Mont Vernon, "Kinston", "Whitfield", "Moultonboro"), and villages (Groveton, Sanbornville, Woodsville) appear as their own entries. Each file's unmatched values are listed below.

#### area-agencies.csv (+ area-agencies-towns-served.csv): Area Agencies for Developmental Services

- source: NH DHHS Bureau of Developmental Services, "Area Agencies" PDF — https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents/2021-11/bds-area-agencies-map.pdf (page 1 contacts "Effective 9/29/25"; page 2 "Towns and Cities by Region", "Updated 5/2025"); websites from https://www.dhhs.nh.gov/programs-services/disability-care/area-agencies
- as_of: Wayback snapshot 2025-12-07 (PDF); 2025-10-31 (page)
- rows: 10 agencies (Regions I–X); 243 town rows. Extra column `region_name`. The note column gives each agency's BDS liaison and any phone difference from the DHHS location data.
- agencies: Northern Human Services (I, Conway), PathWays of the River Valley (II, Claremont), Lakes Region Community Services (III, Laconia), Community Bridges (IV, Concord), Monadnock Developmental Services (V, Keene), Gateways Community Services (VI, Nashua), Moore Center Services (VII, Manchester), One Sky Community Services (VIII, Portsmouth), Community Partners (IX, Dover), Community Crossroads (X, Atkinson).
- town coverage: 231 of the site's towns matched. Unmatched town-list values: Dixville, Glencliff, Groveton, Livermore, Sanbornville, Union, Wentworth Location, Whitfield, Hillsboro, Spofford, Mt. Vernon, Kinston. Site towns with no agency (because of those spellings or not listed): Hale's Location, Hillsborough, Kingston, Mont Vernon, Penacook, Whitefield (and the site's non-town rows).

#### fcess-programs.csv (+ fcess-programs-towns-served.csv): Early Supports and Services (Birth to 3)

- sources: NH DHHS FCESS Program Directory ("September 2025", published under the file name fcess-directory-dec24.pdf) — https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/fcess-directory-dec24.pdf ; FCESS Intake Directory ("March 2025") — https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/fcess-intake.pdf ; FCESS Family Page — https://www.dhhs.nh.gov/programs-services/disability-care/developmental-services/birth-3-family-centered-early-supports-1
- as_of: Wayback snapshot 2025-10-31 (PDFs); 2025-12-31 (Family Page); 2026-10-30 (FCESS main page)
- rows: 14 (13 regional programs plus 1 statewide DHHS row); 274 town rows. Regions 6, 7 and 10 each have two programs, and The Children's Pyramid (Nashua) serves Regions 6 and 10. Extra columns `area_agency`, `referral_phone` (each region's intake contact from the March 2025 intake directory).
- caveats: the directory DHHS links today (fcess-directory.pdf) has no archived copy; the two directories disagree on intake contacts for Regions 8 and 10 (the September 2025 numbers are in the notes). Unmatched town-list values: Barlett, Dixville, Groveton, Intervale, Livermore, Moultonboro, Sanbornville, Union, Wentworth Location, Woodsville, Meriden, Alton Bay, Ctr. Harbor, Hillsboro, Ashuelot, Spofford, Westermoreland, Mt. Vernon.

#### family-resource-centers.csv: Family Resource Centers

- source: the DHHS location data behind the "Family Resource Centers in NH" map on the FRC Family Page — https://www.dhhs.nh.gov/content/api/locations (filtered to the "FRC Families" tag), page https://www.dhhs.nh.gov/programs-services/population-health/family-community-health/family-resource-centers-family-page
- as_of: Wayback snapshot 2025-10-31 (data); 2025-11-02 (page)
- rows: 27 entries in 23 cities. Extra columns `zip`, `email`. The note column gives each entry's other DHHS tags; 23 entries are tagged "Kinship Navigation" (**derived** count).
- caveats: no source says which towns each FRC covers, so `towns_served` and `region` are blank. Two Concord entries share one address (both kept as listed). No phone is listed for Waypoint's Nashua FRC. Gorham isn't in the city list of the DHHS FRC providers page (Wayback 2026-03-03). The River Center's city is written "Peterbourgh" and has no `town_id`. familysupportnh.org doesn't resolve, so no Family Support NH list was available.

#### community-mental-health-centers.csv (+ community-mental-health-centers-towns-served.csv): Community Mental Health Centers

- sources: NH DHHS "New Hampshire Mental Health Services" sheet — https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/bmhs-list-map.pdf (main contacts and "Cities & Towns by Geographic Region"; **"Updated 1/18/22"**); office locations and emergency numbers from the DHHS location data (tag BMHS); DHHS Mental Health page — https://www.dhhs.nh.gov/programs-services/mental-health ; cross-check with NH Community Behavioral Health Association, https://nhcbha.org/emergency-key-services/
- as_of: Wayback snapshot 2025-10-31 (PDF and data); 2026-10-26 (page); 2026-11-08 (NHCBHA)
- rows: 43 (10 main centers, 32 other offices, 1 statewide crisis line); 238 town rows. Extra columns `office_type`, `zip`, `intake_phone`, `crisis_phone`.
- centers (region, main office town): Northern Human Services (1, Conway), West Central Behavioral Health (2, Lebanon), Lakes Region Mental Health Center (3, Laconia), Riverbend Community Mental Health (4, Concord), Monadnock Family Services (5, Keene), Greater Nashua Mental Health (6, Nashua), The Mental Health Center of Greater Manchester (7, Manchester), Seacoast Mental Health Center (8, Portsmouth), Community Partners of Strafford County (9, Dover), Center for Life Management (10, Derry).
- caveats: the town lists and main addresses date from 2022. Two 2022 main addresses (Regions 2 and 6) don't match the 2025 location data. Riverbend's emergency number differs between DHHS (844-743-5748) and NHCBHA (844-753-5748), unresolved; the statewide NH Rapid Response line (833-710-6477) is the safer number to give. Unmatched town-list values: Dixville, Intervale, Shelbourne, Waterville, Wentworth Location, West Lebanon, Hillsboro, Spofford.

#### vocational-rehabilitation-offices.csv (+ vocational-rehabilitation-offices-towns-served.csv): NH Vocational Rehabilitation Offices

- sources: VR New Hampshire (NH DOE Bureau of Vocational Rehabilitation) "Find Your Regional Office" — https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation/about-vr/find-your-regional-office ; "VR Offices by Town" PDF (modified 2024-01-11) — https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/vr-by-town.pdf ; apply, FAQ and school transition pages under https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation
- as_of: Wayback snapshot 2025-08-31 (offices, town list, FAQ, transition); 2025-09-29 (apply); 2026-09-22 (home page)
- rows: 9 (6 regional offices: Berlin, Concord, Keene, Manchester, Nashua, Portsmouth; Services for the Blind & Vision Impaired; the statewide contact; the Pre-ETS transition coordinator); 293 town rows. Extra column `coverage_detail` for towns shared by two offices (Danville, Northwood, Pelham, Raymond) and Keene's "(Lebanon)"/"(Claremont)" sub-areas.
- caveats: the office page prints the Nashua office at the Manchester address (1 Sundial Avenue, Manchester); the FAQ says "seven regional offices" but the office page lists six plus the blind services office. The town list includes villages and non-town entries ("Prison", "YDC (Youth Development)", "Nashua Area", "Concord Area", "Laconia (Region 3)"), so Concord, Laconia, Nashua and Peterborough ("Peterbrough") have no plain town row. Many unmatched values; see the towns-served file.

---

## Facts

## head-start-where-to-find: Finding a Head Start Program in New Hampshire

- kind: programs
- question_type: help
- description: Where Head Start and Early Head Start sites are in NH, who runs them, and how to find one.

1. The federal Head Start Center Locator at headstart.gov lets families search for Head Start Preschool and Early Head Start centers by address, city, ZIP code or state.
   - source: https://headstart.gov/center-locator
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: page showed "Last Updated: November 7, 2026"; Office of Head Start contact on the page: 1-866-763-6481, HeadStart@eclkc.info
2. Five organizations run Head Start in New Hampshire: Community Action Program Belknap-Merrimack Counties, Community Action Partnership Hillsborough and Rockingham Counties, Community Action Partnership of Strafford County, Southwestern Community Services, and Tri-County Community Action Program.
   - source: https://www.dhhs.nh.gov/programs-services/childcare-parenting-childbirth/child-development-and-head-start/new-hampshire
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: viewed in a browser (dhhs.nh.gov blocks scripts). In the HHS file the Hillsborough/Rockingham grant is under "Southern New Hampshire Services, Inc."
3. The New Hampshire Head Start Collaboration Office, in the NH Department of Health and Human Services, works to "foster collaboration and teamwork between Head Start and state and local partners" and "improve access to comprehensive services for income-eligible families of young children."
   - source: https://www.dhhs.nh.gov/programs-services/childcare-parenting-childbirth/child-development-and-head-start/new-hampshire
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. The federal Head Start locations file listed 45 New Hampshire entries at 35 addresses in 28 towns on November 8, 2026; 35 entries were open (25 Head Start Preschool and 10 Early Head Start), 8 Head Start entries run by Tri County CAP in northern NH had status "Not Reported", and 2 were closed.
   - source: https://s3foa.s3.us-east-1.amazonaws.com/HS_Service_Locations.csv
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: derived counts from `raw/programs/head-start-sites-nh.csv`. The file is self-reported by grantees and refreshed daily.

## efa-how-to-apply: Applying for an Education Freedom Account

- kind: programs
- question_type: help
- description: Where and when families apply for an EFA, and who to contact. Eligibility rules are in facts-rules-and-rights.md.

1. Families apply for a New Hampshire Education Freedom Account (EFA) online at nhefa.scholarshipfund.org, the EFA website run by the Children's Scholarship Fund (CSF). The 2026-27 application uses a new website called Schola Via.
   - source: https://nhefa.scholarshipfund.org/faq
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. The NH EFA phone number is (603) 755-6751, and the contact email is csfnh@scholarshipfund.org.
   - source: https://nhefa.scholarshipfund.org/faq
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. According to the EFA program's FAQ, applications for the next school year open in March and are accepted on a rolling basis until February 15; to be eligible for the full (base) grant, an application must be complete and verified by CSF by July 15.
   - source: https://nhefa.scholarshipfund.org/faq
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. The EFA FAQ says the enrollment cap for 2026-27 is 12,500 students and will increase to 15,625 for the 2027-28 school year.
   - source: https://nhefa.scholarshipfund.org/faq
   - as_of: 2026-11-08
   - review_by: 2027-11-08
5. EFA funds are paid through an online platform called ClassWallet, which families can use to shop in its marketplace, pay a provider directly (if the provider has signed up for ClassWallet), or get reimbursed for approved expenses.
   - source: https://nhefa.scholarshipfund.org/faq
   - as_of: 2026-11-08
   - review_by: 2027-11-08
6. The EFA application website's public stats for the 2026-2027 school year showed 13,757 eligible students, 476 on the waitlist, and 13,159 labeled "Enrolled", on November 8, 2026.
   - source: https://nhefa.scholarshipfund.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: figures from the site's feed https://nhefa.scholarshipfund.org/api/admin/stats (undocumented); counts change daily. Town detail in `raw/programs/efa-stats-by-town-2026-27.csv`.

## efa-provider-list: The EFA Marketplace of Schools and Providers

- kind: programs
- question_type: help
- description: What the list of EFA-approved schools and providers contains, and its limits.

1. The EFA marketplace run by the Children's Scholarship Fund listed 3,606 schools, tutors, therapists, vendors and other providers on November 8, 2026, of which 1,788 were located in New Hampshire, including 347 schools.
   - source: https://app.nh.scholarshipfund.org/marketplace
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: figures from the marketplace's feed https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors (undocumented). NH location is derived from the state and address fields. Full list in `raw/programs/efa-providers.csv`.
2. Many EFA marketplace providers are outside New Hampshire or online-only; the list records each provider's type, grades, address and labels, but not tuition, openings or quality.
   - source: https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## cte-centers-overview: Career and Technical Education Centers

- kind: programs
- question_type: help
- description: Where NH's CTE centers are, what program areas they offer, and where to look for details.

1. The NH Department of Education lists 31 career and technical education (CTE) centers on its CTE page, including five in Vermont (Canaan, White River Junction, Bradford, Springfield and Brattleboro).
   - source: https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-of-career-development/cte-programs-in-new-hampshire
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: viewed in a browser. Full list with host districts in `raw/programs/cte-centers.csv`.
2. Most NH CTE centers are part of a host high school and school district; for example, the Manchester School of Technology is in the Manchester district (SAU 37) and the Wilbur H. Palmer center is in Hudson (SAU 81).
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/cte-centers-info-22-23.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. The NH DOE "CTE Program Grid - 2025" lists which centers offer each of 17 broad program areas. The most widely offered are Health Services/Allied Health (28 centers), Restaurant, Culinary and Catering (24), Construction Trades (24) and Transportation and Materials Moving (24). Manufacturing Technology is offered at 21 centers and Aeronautics/Aviation at 4.
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/cip-code-cte-program-grid_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: derived counts from `raw/programs/cte-programs-2025.csv`. The grid doesn't list specific trades such as welding or machining.
4. In the 2025 program grid, Berlin Regional CTC (Berlin) offers 7 of the 17 program areas: Drafting and Design Technology, Education, Manufacturing Technology, Construction Trades, Engineering Technology, Transportation and Materials Moving, and Health Services.
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/cip-code-cte-program-grid_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Berlin
5. Berlin Regional Career & Technical Center's website says it "welcomes students from Gorham Middle High School as well as from Berlin High School"; phone (603) 752-4122 x 4, 550 Willard Street, Berlin, NH 03570.
   - source: https://sites.google.com/sau3.org/bhscte/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Berlin
   - note: page undated.
6. The Concord Regional Technology Center lists ten "CRTC Sending High Schools": Bishop Brady, Bow, Concord, Hillsboro-Deering, Hopkinton, John Stark Regional, Kearsarge Regional, Merrimack Valley, Pembroke Academy and Pittsfield; phone 603-717-7654.
   - source: https://thecrtc.org/sending-schools/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Concord
   - note: page undated. Sending-school lists were found on the sites of 17 of the 26 NH centers on the current NH DOE list (in `raw/programs/cte-centers.csv`); some name districts or towns rather than schools.

## early-college-at-your-high-school: Early College at Your High School (formerly Running Start)

- kind: programs
- question_type: help
- description: CCSNH's program of college courses taught in NH high schools: what it is, how to sign up, cost and contacts.

1. The Community College System of New Hampshire (CCSNH) web address for Running Start, ccsnh.edu/running-start, now opens the page for "Early College At Your High School."
   - source: https://www.ccsnh.edu/running-start/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: redirects to https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/
2. In CCSNH's Early College at Your High School, college courses are taught at high schools by teachers credentialed to teach college-level courses, partnered with community college faculty and using the college syllabus, as part of the daily high school schedule.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. CCSNH says Early College at Your High School courses are offered to eligible sophomores, juniors and seniors, and ninth graders may take a college course with permission.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/running-start-faqs/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. To find out which college courses their high school offers, CCSNH tells students and families to talk to their school counselor; to get college credit, students must register with the sponsoring college during the fall or spring registration period, and can't be registered after a course has ended.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/running-start-faqs/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
5. CCSNH says the tuition for an Early College at Your High School course is $150, and NH students in grades 10-12 can receive two Early College scholarships a year that cover tuition, applied automatically to their first two courses; students may have to pay for books and materials.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/running-start-faqs/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: the program page says the scholarships are "subject to available funding"; the tuition page says the $150 is "prorated for courses fewer than three credit hours."
6. Each of the seven community colleges has an Early College coordinator for the high schools in its area; CCSNH publishes the coordinators' names, phone numbers and the high schools each serves.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/running-start-contacts/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: in `raw/programs/community-colleges-early-college.csv`. E.g. Concord High is served by NHTI's coordinator; Alvirne by Nashua Community College's.
7. CCSNH says acceptance of the college credit is always at the discretion of the receiving college or university, and a course that doesn't fit a student's program may transfer as an elective.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
8. CCSNH says IEPs and 504 plans are not applied to college-credit courses; students who need college-level accommodations should contact the Coordinator of Disability Services at the college offering the course.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/running-start/running-start-faqs/
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## early-college-on-campus: Early College Courses at the Community Colleges

- kind: programs
- question_type: help
- description: Taking classes directly at (or online from) a NH community college while in high school.

1. CCSNH's Early College program lets high school students aged 15 and older take classes directly with one of the community colleges, in person, online, hybrid or flex.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. CCSNH says tuition for Early College courses taken at the community colleges is half price, with up to two Early College scholarships a year that, pending availability, cover tuition and fees; some course fees and books may still cost money.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. To sign up for an Early College online class, CCSNH says to search the CCSNH course look-up site for the attribute "Early College on Campus" and then contact the Early College coordinator at the college offering it; students should work with their high school so the course counts toward high school requirements.
   - source: https://www.ccsnh.edu/colleges-and-programs/programs-for-high-school-students-to-earn-college-credit/
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## community-colleges-nh: New Hampshire's Community Colleges

- kind: programs
- question_type: help
- description: The seven CCSNH colleges, where they are and their main numbers.

1. The Community College System of New Hampshire has seven colleges: Great Bay (Portsmouth), Lakes Region (Laconia), Manchester, Nashua, NHTI – Concord's Community College, River Valley (Claremont) and White Mountains (Berlin).
   - source: https://www.ccsnh.edu/locations/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. NHTI – Concord's Community College is at 31 College Drive, Concord, NH 03301; main phone (603) 230-4000, admissions (603) 230-4011.
   - source: https://www.ccsnh.edu/locations/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Concord
   - note: all seven in `raw/programs/community-colleges-early-college.csv`

## unh-early-college-online: UNH Early College Online (with VLACS)

- kind: programs
- question_type: help
- description: UNH college courses for high school students, taken online through VLACS.

1. Through UNH Early College Online, a partnership of the University of New Hampshire's College of Professional Studies and the Virtual Learning Academy Charter School (VLACS), high school students take fully online UNH courses that count toward high school graduation and earn four UNH credits per course, up to 28 credits.
   - source: https://cps.unh.edu/online/academics/early-college-online
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. UNH says students in UNH Early College Online pay $150 per course, including instructional materials, and must enroll through VLACS; students who don't create a VLACS account won't get high school credit and are charged full UNH tuition.
   - source: https://cps.unh.edu/online/academics/early-college-online
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: VLACS's page calls the $150 an "administrative fee" per course: https://vlacs.org/programs/unh-early-college/
3. UNH's page says sophomores who have completed sophomore English, juniors and seniors are eligible, as are homeschooled students aged 15 or older; VLACS's page says students must be a junior or senior. Families should confirm with VLACS.
   - source: https://cps.unh.edu/online/academics/early-college-online
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: the two pages disagree on grade 10; both quoted as written. VLACS's page: https://vlacs.org/programs/unh-early-college/
4. VLACS's page gives the Spring 2027 enrollment deadline for UNH Early College courses as February 19, 2027 at noon EST.
   - source: https://vlacs.org/programs/unh-early-college/
   - as_of: 2026-11-08
   - review_by: 2027-03-01

## unh-first-step: UNH First Step (UNH Credit at the High School)

- kind: programs
- question_type: help
- description: UNH Manchester's concurrent-credit courses taught in a few NH high schools. Only an older archived page could be read.

1. UNH First Step, a UNH Manchester concurrent credit program, lets New Hampshire high school students earn UNH credit at their high schools; it began at Pinkerton Academy in fall 2019 as a pilot and expanded to Bow High School, in communication arts and computer science.
   - source: https://manchester.unh.edu/academics/unh-first-step-concurrent-credit-program
   - as_of: Wayback snapshot 2024-04-14
   - review_by: 2027-11-08
   - note: the live page returned 403 to scripts and in a browser on 2026-11-08, so this is two and a half years old. The page then said participants must be juniors or seniors with an overall "B" average, and the $150 per 4-credit course fee was waived during the pilot. Contact then: Mary Young, mary.young@unh.edu, 603-641-4119. Confirm before use.

## keene-state-accelerated-high-school: Keene State Accelerated High School Program

- kind: programs
- question_type: help
- description: Keene State College courses for high school juniors and seniors.

1. Keene State College's Accelerated High School Program lets high school juniors and seniors with at least a B average take one course each fall, spring and summer semester on campus at half-price tuition, up to 6 courses (24 credits).
   - source: https://www.keene.edu/academics/conted/accelerated/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Keene
2. For information about applying to Keene State's Accelerated High School Program, the page says to call the Admissions Office at 603-358-2276.
   - source: https://www.keene.edu/academics/conted/accelerated/
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## parent-information-center: Parent Information Center (Special Education Help)

- kind: programs
- question_type: help
- description: NH's parent center for special education and family engagement: what it does and how to reach it.

1. The Parent Information Center (PIC), at 54 Old Suncook Road, Concord, NH 03301, can be reached at 603.224.7005, 1.800.947.7005 (NH only), or admin@picnh.org.
   - source: https://picnh.org/contact-us/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. The Parent Information Center helps parents understand their child's special needs and the laws that govern early intervention and the special education process; since 1995 it has also worked with all parents, schools and communities on family engagement.
   - source: https://picnh.org/about-us/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. The Parent Information Center says it is not a legal services agency and cannot provide legal advice or legal representation.
   - source: https://picnh.org/about-us/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. The Parent Information Center on Special Education is funded, in part or whole, by the U.S. Department of Education, Office of Special Education Programs.
   - source: https://picnh.org/contact-us/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
5. PIC's free Volunteer Advocate Training Program is an 8-week hybrid series that teaches parents to navigate the NH special education process and support other families; it uses an application process, gives preference to parents of children with disabilities or special health care needs, and doesn't accept professional advocates who charge fees. Applications for the 2027 series opened November 2, 2026.
   - source: https://picnh.org/volunteer-advocate-training-program/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
6. New Hampshire Family Voices, PIC's partner organization, provides free, confidential help to families and professionals caring for children with chronic conditions or disabilities, including help navigating health care and its financing.
   - source: https://picnh.org/our-organizations/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: NH Family Voices phone on its own site: 603-271-4525 (https://nhfv.org/resources/kinship-navigator-program/)

## child-care-aware-nh: Child Care Aware of New Hampshire (Child Care Referrals)

- kind: programs
- question_type: help
- description: Free child care referrals statewide, and how to reach them.

1. Child Care Aware of New Hampshire gives free, confidential child care referrals to anyone looking for child care in NH: call toll free (855) 393-1731 ext. 2531 or email ccrr@caphr.org.
   - source: https://www.caphr.org/services/child-care-aware
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: the older address snhs.org/services/child-care-aware redirected here on 2026-11-08
2. Child Care Aware of NH gives each family a list of three to fifteen programs that meet its search, and families can ask for programs enrolled to accept the NH Child Care Scholarship.
   - source: https://www.caphr.org/services/child-care-aware
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. Child Care Aware of NH provides its services under a contract with the NH Department of Health and Human Services and says it gives information, not recommendations, and does not endorse any program or provider.
   - source: https://www.caphr.org/services/child-care-aware
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## nh-child-care-search: NH Child Care Search

- kind: programs
- question_type: help
- description: The state's free online search of child care programs.

1. NH Child Care Search is a free state service for finding child care, where families can look up providers' quality rating, licensing history and services: https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch
   - source: https://www.dhhs.nh.gov/programs-services/childcare-parenting-childbirth/child-development-and-head-start
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: link out to it rather than copy it (the plan's recommendation); viewed in a browser.

## child-care-scholarship-how-to-apply: Applying for the NH Child Care Scholarship

- kind: programs
- question_type: help
- description: Where to apply and who to call. Income limits and eligibility rules are in facts-rules-and-rights.md.

1. Families apply for the NH Child Care Scholarship online at nheasy.nh.gov (NH EASY, the application site for DHHS services), or in person or by mail with a paper application at DHHS District Offices.
   - source: https://www.dhhs.nh.gov/programs-services/childcare-parenting-childbirth/child-development-and-head-start
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. To schedule a follow-up appointment about a Child Care Scholarship application, DHHS says to call 1-844-ASK-DHHS (1-844-275-3447).
   - source: https://www.dhhs.nh.gov/programs-services/childcare-parenting-childbirth/child-development-and-head-start
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. DHHS says Child Care Scholarship eligibility is redetermined every 12 months and families must reapply each year; current income levels are posted at https://nheasy.nh.gov/forms/E/2532.pdf.
   - source: https://www.dhhs.nh.gov/programs-services/childcare-parenting-childbirth/child-development-and-head-start
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## nh-211: 211 NH

- kind: programs
- question_type: help
- description: The statewide information and referral line.

1. 211 NH connects New Hampshire residents with specially trained Information and Referral Specialists 24 hours a day, 365 days a year; dial 211, or call 1-866-444-4211.
   - source: https://211nh.org/
   - as_of: Wayback snapshot 2026-10-07
   - review_by: 2027-11-08
   - note: 211nh.org did not resolve (DNS) on 2026-11-08; archived copy used. 1-866-444-4211 is printed in the site footer.
2. 211 NH helps by phone, email or text with non-emergency needs such as housing, utilities, food, mental health and health care.
   - source: https://211nh.org/
   - as_of: Wayback snapshot 2026-10-07
   - review_by: 2027-11-08

## nami-nh: NAMI New Hampshire

- kind: programs
- question_type: help
- description: Mental health information and family support from NAMI NH.

1. NAMI New Hampshire's Information & Resource Line, 1-800-242-6264 (press 4) or info@naminh.org, connects families and individuals affected by mental health conditions with NAMI NH programs and local resources; it is not a hotline or crisis service.
   - source: https://www.naminh.org/ir/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. NAMI NH offers free Family Peer Support for parents and caregivers of a child or youth waiting in a hospital emergency department for mental health services (call/text 603-568-5771, weekdays 9 to 5).
   - source: https://www.naminh.org/ir/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. NAMI New Hampshire is at 85 North State Street, Concord, NH 03301; phone 603-225-5359.
   - source: https://www.naminh.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## kinship-caregiver-support: Help for Grandparents and Relatives Raising Children

- kind: programs
- question_type: help
- description: NH's Kinship Navigator Program for relative caregivers, and how to reach it.

1. New Hampshire law requires the Department of Health and Human Services to establish a kinship navigator program offering information, referral and follow-up services to grandparents and other relatives raising children.
   - citation: RSA 170-G:4-g
   - source: https://gc.nh.gov/rsa/html/XII/170-G/170-G-4-g.htm
   - as_of: 2026-11-08
   - review_by: 2027-08-15
2. New Hampshire's Kinship Navigator Program works through the state's Family Resource Centers; it is free and voluntary and open to grandparents and other relatives raising a child in the absence of the child's parents.
   - source: https://nhfv.org/resources/kinship-navigator-program/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. To reach a Kinship Navigator, NH Children's Trust says to contact the local Family Resource Center or email kinship@nhchildrenstrust.org; services are free and confidential, and the child must live with the caregiver full-time.
   - source: https://www.nhchildrenstrust.org/_files/ugd/38c037_918939ab160b41709a166ff4fe791654.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: the Kinship Caregiver Guide, linked from https://www.nhchildrenstrust.org/kinship-guide; guide PDF created 2023-09-29. NH Children's Trust: 105B Loudon Road, Suite 201, Concord, NH 03301, (603) 224-1279 (from the kinship-guide page).

## military-families-nh: Support for Military Families

- kind: programs
- question_type: help
- description: Who to call about school and family support for National Guard and military families in NH.

1. The New Hampshire National Guard's State Family Program can be reached at 603-225-1889; its Service Member and Family Support Resource and Referral Line is 1 877 598 0666.
   - source: https://nh.ng.mil/Family-Services/State-Family-Program/
   - as_of: Wayback snapshot 2026-06-17
   - review_by: 2027-11-08
   - note: the site blocks scripts. The same page elsewhere gives the Family Program number as "1-800-598-0666"; the 877 number is the one in the contact block. Child and Youth Program contractor: 603-225-1269.
2. The NH National Guard's Child and Youth Program offers free summer and vacation camps, teen leadership opportunities and other support for military youth and families.
   - source: https://nh.ng.mil/Family-Services/State-Family-Program/
   - as_of: Wayback snapshot 2026-06-17
   - review_by: 2027-11-08
3. Military OneSource lists the 157th Air Refueling Wing at Pease Air National Guard Base, 302 Newmarket St, Pease ANGB, NH 03803-0157, phone 603-430-3577; it lists no school liaison for Pease.
   - source: https://installations.militaryonesource.mil/military-installation/157-arw
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. The NH DOE's page for the Military Interstate Children's Compact Commission names Kathleen A. Murphy, Commissioner, as primary point of contact (kmurphy@sau8.org or 603-717-0121).
   - source: https://www.education.nh.gov/partners/military-interstate-childrens-compact-commission
   - as_of: Wayback snapshot 2025-10-24
   - review_by: 2027-11-08
5. In November 2021 the NH Department of Education announced that fourteen schools had been designated Purple Star Schools, committed to supporting military children, including schools in Bow, Concord, Dover, Henniker, Hudson, Londonderry, Portsmouth and Salem; no current list was found.
   - source: https://www.education.nh.gov/news/purple-star-schools-meeting-unique-needs-military-children
   - as_of: Wayback snapshot 2025-12-12
   - review_by: 2027-11-08
   - note: release dated November 05, 2021. It named Staff Sgt. Rick Frost of the NH National Guard as contact; that may be out of date.

## refugee-immigrant-family-support: Refugee and Immigrant Family Support

- kind: programs
- question_type: help
- description: The two resettlement agencies with NH offices.

1. The International Institute of New England's Manchester office is at 470 Pine Street, Lower Level, Manchester, NH 03104, phone 603.647.1500.
   - source: https://iine.org/contact
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Manchester
2. The International Institute of New England's Manchester site serves refugee families with initial resettlement and support services including job placement, cultural adjustment programming, English language instruction, case management and citizenship application services.
   - source: https://iine.org/contact
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. Ascentria Care Alliance's Services for New Americans program serves refugees, asylum seekers and other immigrants in Southern New Hampshire (and Central and Western Massachusetts); its NH office is at 261 Sheep Davis Road, A-1, Concord, NH 03301, phone 603.224.8111.
   - source: https://www.ascentria.org/service/services-for-new-americans/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Concord

## nhdoe-special-education-help: NH Department of Education Contacts for Families

- kind: programs
- question_type: help
- description: Who to call at NH DOE about special education, complaints and appeals.

1. The NH Department of Education's Bureau of Special Education Support main line for questions about the special education process is (603) 271-3741, email specialeducation@doe.nh.gov.
   - source: https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-of-student-support
   - as_of: Wayback snapshot 2025-06-01
   - review_by: 2027-11-08
2. A special education complaint to the NH Department of Education must be in writing, signed, and mailed (email isn't accepted) to: New Hampshire Department of Education, Attention: Special Education Complaint Office, 25 Hall Street, Concord, NH 03301; the complainant must also send a copy to the school district.
   - source: https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-of-student-support/special-education/complaints
   - as_of: Wayback snapshot 2026-02-28
   - review_by: 2027-11-08
3. The NH Department of Education and State Board of Education offer mediation and, for special education, neutral conferences to settle disagreements, and appeal routes including special education due process hearings and State Board hearings.
   - source: https://www.education.nh.gov/parents-and-students/appeals-and-mediation
   - as_of: Wayback snapshot 2025-05-24
   - review_by: 2027-11-08
4. The NH Department of Education's general contact is 25 Hall Street, Concord, NH 03301-3860, (603) 271-3494, info@doe.nh.gov.
   - source: https://www.education.nh.gov/parents-and-students/services-my-child
   - as_of: Wayback snapshot 2026-09-15
   - review_by: 2027-11-08
   - note: no NH DOE education ombudsman page was found in the archive index of education.nh.gov.

## after-school-21st-cclc: Federally Funded After-School Programs (21st CCLC)

- kind: programs
- question_type: help
- description: Where NH's 21st Century Community Learning Centers are and who runs them.

1. The federal 21st Century Community Learning Centers program pays for before-school, after-school and summer programs for children attending high-poverty schools, including tutoring, homework help and enrichment.
   - source: https://www.education.nh.gov/21cclc
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. The NH Department of Education's 21st CCLC page reported 42 grants at 52 sites, run by 17 school districts and community-based organizations.
   - source: https://www.education.nh.gov/21cclc
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: viewed in a browser. Site list in `raw/programs/21cclc-sites.csv`.
3. In Concord, the Capital City 21st Century Community Learning Centers run at Mill Brook, Broken Ground and Rundlett Middle schools; the program director's phone is 603-230-1760.
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/media/media_document/21-cclc-program-contact-information-updated-9-2026_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Concord
4. The September 2026 NH DOE list of 21st CCLC programs includes no program in Claremont.
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/media/media_document/21-cclc-program-contact-information-updated-9-2026_0.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: town Claremont
   - note: absence of a federally funded program, not of all after-school programs.

## nh-promise-usnh: New Hampshire Promise (UNH, Keene State, Plymouth State)

- kind: programs
- question_type: help
- description: USNH's tuition program for NH students from families earning up to $100,000; replaces the Granite Guarantee for new students from fall 2027.

1. Beginning in fall 2027, under the University System of New Hampshire's New Hampshire Promise, incoming first-year students who are NH residents with a total family income of up to $100,000 a year can pay no tuition at any USNH institution (UNH Durham, UNH Manchester, UNH College of Professional Studies Online, Keene State College and Plymouth State University), with tuition covered by federal, state and institutional grant aid.
   - source: https://www.unh.edu/admissions-aid/new-hampshire-promise
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: the old Granite Guarantee address (unh.edu/financialaid/granite-guarantee) redirects to this page.
2. There is no separate application for the New Hampshire Promise: students apply for admission to a USNH institution and submit the FAFSA, and admitted students who qualify are considered automatically.
   - source: https://www.unh.edu/admissions-aid/new-hampshire-promise
   - as_of: 2026-11-08
   - review_by: 2027-11-08
3. The New Hampshire Promise covers standard tuition, not fees, books, housing or meals; it also requires full-time enrollment and, for new first-year students, a cumulative high school GPA of 2.7 or above.
   - source: https://www.unh.edu/admissions-aid/new-hampshire-promise
   - as_of: 2026-11-08
   - review_by: 2027-11-08
4. Students with a community college associate degree from CCSNH who transfer to a USNH institution are also eligible for the New Hampshire Promise, and current Granite Guarantee students keep their Granite Guarantee awards.
   - source: https://www.unh.edu/admissions-aid/new-hampshire-promise
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## ccsnh-tuition-and-aid: Community College Tuition and Aid

- kind: programs
- question_type: help
- description: CCSNH's 2026-27 tuition rates and discounts.

1. For 2026-27, CCSNH's in-state tuition is $238 per credit; the New England Regional rate is $357 and the out-of-state rate $523 per credit.
   - source: https://www.ccsnh.edu/paying-for-college-new/tuition-fees-new/
   - as_of: 2026-11-08
   - review_by: 2027-08-01
2. CCSNH says it offers federal grants and loans, scholarships and special program grants, and that dual credit high school students taking courses at a community college pay half tuition with academic, comprehensive and lab fees waived.
   - source: https://www.ccsnh.edu/paying-for-college-new/tuition-fees-new/
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## granite-edvance: Granite Edvance (College Planning and Scholarships)

- kind: programs
- question_type: help
- description: The NH nonprofit the state education department lists for grants and scholarships.

1. Granite Edvance (formerly The NHHEAF Network) is a New Hampshire nonprofit that helps students and families with college and career planning through scholarships, private student loan options and guidance, without charge for its support services; phone 603-225-6612.
   - source: https://graniteedvance.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: NH DOE's higher education page lists Granite Edvance and the NH Charitable Foundation under "Grants and Scholarships - Financial Resources" (https://www.education.nh.gov/pathways-education/higher-education-new-hampshire, Wayback snapshot 2025-12-05).
2. Granite Edvance offers scholarships for two-year and trade-school students several times a year and for four-year students once a year; its spring two-year and trade-school scholarship offers up to $1,500.
   - source: https://graniteedvance.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## nh-529-plans: New Hampshire's 529 College Savings Plans

- kind: programs
- question_type: help
- description: The state's two 529 plans.

1. The State of New Hampshire offers two 529 college savings plans, both managed by Fidelity Investments: the UNIQUE College Investing Plan, open to anyone in the U.S., and the Fidelity Advisor 529 Plan, sold through financial advisors.
   - source: https://www.treasury.nh.gov/residents/529-college-savings-program
   - as_of: Wayback snapshot 2026-01-06
   - review_by: 2027-11-08
2. The NH Treasury says NH 529 funds can be used for college expenses, K-12 tuition, apprenticeships and student loan repayments, and education withdrawals are tax-free.
   - source: https://www.treasury.nh.gov/residents/529-college-savings-program
   - as_of: Wayback snapshot 2026-01-06
   - review_by: 2027-11-08

## orphans-of-veterans-scholarship: Scholarships for Orphans of Veterans

- kind: programs
- question_type: help
- description: NH's scholarship for children of service members who died on duty or of service-connected disabilities.

1. New Hampshire's Scholarships for Orphans of Veterans program provides $2,500 scholarships to children of NH service members who died on active duty or of service-connected disabilities, for room, board, books and supplies at NH colleges; such students may also receive free tuition at USNH and CCSNH.
   - citation: RSA 193:19
   - source: https://www.education.nh.gov/who-we-are/division-of-educator-support-and-higher-education/higher-education/higher-education-scholarships-for-orphans-of-veterans
   - as_of: Wayback snapshot 2026-04-01
   - review_by: 2027-11-08
   - note: contact on page 603-271-8508

## fafsa: The FAFSA (Federal Student Aid Application)

- kind: programs
- question_type: help
- description: Where to file the federal aid form.

1. Students apply for federal financial aid for college or career school with the Free Application for Federal Student Aid (FAFSA) at studentaid.gov; the 2027–28 FAFSA form was available as of November 8, 2026.
   - source: https://studentaid.gov/h/apply-for-aid/fafsa
   - as_of: 2026-11-08
   - review_by: 2027-11-08
2. Federal Student Aid says students must apply every year, and that missing a state deadline doesn't affect eligibility for federal student aid.
   - source: https://studentaid.gov/h/apply-for-aid/fafsa
   - as_of: 2026-11-08
   - review_by: 2027-11-08

## area-agencies-developmental-services: Area Agencies for Developmental Services

- kind: programs
- question_type: help
- description: The 10 regional agencies for people with developmental disabilities or acquired brain disorders, including help after a young adult leaves school.

1. New Hampshire has 10 area agencies, non-profit corporations working under NH Department of Health and Human Services rules, that provide services, directly or through subcontractors, to people with a developmental disability or acquired brain disorder.
   - source: https://www.dhhs.nh.gov/programs-services/disability-care/area-agencies
   - as_of: Wayback snapshot 2025-10-31
   - review_by: 2027-11-08
2. To be eligible for area agency services, DHHS says a person must meet the disability definition and be of a specific age depending on the service, and "Funding availability is critical to receiving all of the services you may need."
   - source: https://www.dhhs.nh.gov/programs-services/disability-care/area-agencies
   - as_of: Wayback snapshot 2025-10-31
   - review_by: 2027-11-08
3. The DHHS list of towns by region assigns each New Hampshire town to one of the 10 area agency regions; the agencies and their main numbers are Northern Human Services (Region I, Conway, (603) 447-3347), PathWays of the River Valley (II, Claremont, (603) 542-8706), Lakes Region Community Services (III, Laconia, (603) 524-8811), Community Bridges (IV, Concord, (603) 225-4153), Monadnock Developmental Services (V, Keene, (603) 352-1304), Gateways Community Services (VI, Nashua, (603) 882-6333), Moore Center Services (VII, Manchester, (603) 206-2700), One Sky Community Services (VIII, Portsmouth, (603) 436-6111), Community Partners (IX, Dover, (603) 749-4015) and Community Crossroads (X, Atkinson, (603) 893-1299).
   - source: https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents/2021-11/bds-area-agencies-map.pdf
   - as_of: Wayback snapshot 2025-12-07
   - review_by: 2027-11-08
   - note: contacts "Effective 9/29/25"; towns "Updated 5/2025". Several agencies also list an 800 number (see CSV). Town lookup in `raw/programs/area-agencies-towns-served.csv`.

## fcess-early-supports: Family Centered Early Supports and Services (Birth to 3)

- kind: programs
- question_type: help
- description: NH's early intervention for babies and toddlers: how to make a referral and who runs it in each region.

1. NH Birth to 3: Family Centered Early Supports and Services serves young children who have, or are at risk for, developmental delay, or who have an established condition, through the 10 area agencies, with no out-of-pocket cost to families and no primary care provider referral required.
   - source: https://www.dhhs.nh.gov/programs-services/disability-care/developmental-services/birth-3-family-centered-early-supports
   - as_of: Wayback snapshot 2026-10-30
   - review_by: 2027-11-08
2. DHHS says anyone can make a referral to NH Birth to 3, without a doctor's referral; families can contact their local area agency or call 603-271-3770.
   - source: https://www.dhhs.nh.gov/programs-services/disability-care/developmental-services/birth-3-family-centered-early-supports-1
   - as_of: Wayback snapshot 2025-12-31
   - review_by: 2027-11-08
   - note: each region's intake number is in `raw/programs/fcess-programs.csv` (`referral_phone`).
3. Family Centered Early Supports and Services support a child until the child is no longer eligible or the day before the child's 3rd birthday; some children then transition to preschool special education.
   - source: https://www.dhhs.nh.gov/programs-services/disability-care/developmental-services/birth-3-family-centered-early-supports-1
   - as_of: Wayback snapshot 2025-12-31
   - review_by: 2027-11-08

## family-resource-centers: Family Resource Centers

- kind: programs
- question_type: help
- description: Free, voluntary local family support centers, and where they are.

1. New Hampshire's Family Resource Centers are open to every family, and all their services are voluntary, confidential and free of charge; they are not Child Protective Services or DCYF.
   - source: https://www.dhhs.nh.gov/programs-services/population-health/family-community-health/family-resource-centers-family-page
   - as_of: Wayback snapshot 2025-11-02
   - review_by: 2027-11-08
2. DHHS says families don't need an appointment at a Family Resource Center, but hours vary by location, so calling first is recommended.
   - source: https://www.dhhs.nh.gov/programs-services/population-health/family-community-health/family-resource-centers-family-page
   - as_of: Wayback snapshot 2025-11-02
   - review_by: 2027-11-08
3. The DHHS map of Family Resource Centers listed 27 locations in 23 cities and towns, from Colebrook and Berlin to Nashua, Salem and Portsmouth; 23 of them were also tagged by DHHS as offering Kinship Navigation.
   - source: https://www.dhhs.nh.gov/programs-services/population-health/family-community-health/family-resource-centers-family-page
   - as_of: Wayback snapshot 2025-10-31
   - review_by: 2027-11-08
   - note: derived counts from the location data behind the page's map, https://www.dhhs.nh.gov/content/api/locations (filtered to the "FRC Families" tag); list in `raw/programs/family-resource-centers.csv`.

## community-mental-health-centers: Community Mental Health Centers and Crisis Help

- kind: programs
- question_type: help
- description: NH's 10 regional community mental health centers and the statewide crisis line.

1. New Hampshire's community mental health centers are private, full-service clinics; their services include 24-hour emergency services, assessment, individual, family and group therapy, case management and psychiatric services, and all have specialized programs for children and families.
   - source: https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/bmhs-list-map.pdf
   - as_of: Wayback snapshot 2025-10-31
   - review_by: 2027-11-08
   - note: the sheet says "Updated 1/18/22".
2. DHHS says mental health services in NH are available to everyone, regardless of age or ability to pay, and people in a mental health or substance use crisis can call or text the NH Rapid Response Access Point at 833-710-6477 (24/7) or visit nh988.com.
   - source: https://www.dhhs.nh.gov/programs-services/mental-health
   - as_of: Wayback snapshot 2026-10-26
   - review_by: 2027-11-08
3. A DHHS flyer explains that calls and texts to 988 are routed by area code, so a call from a phone with an out-of-state area code reaches a call center in that state; for a local response every time, it says to call NH Rapid Response.
   - source: https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/988-rapid-response.pdf
   - as_of: Wayback snapshot 2025-10-31
   - review_by: 2027-11-08
4. DHHS's list of cities and towns by region assigns each NH town to one of 10 community mental health centers: Northern Human Services (Region 1), West Central Behavioral Health (2), Lakes Region Mental Health Center (3), Riverbend Community Mental Health (4), Monadnock Family Services (5), Greater Nashua Mental Health (6), The Mental Health Center of Greater Manchester (7), Seacoast Mental Health Center (8), Community Partners of Strafford County (9) and Center for Life Management (10).
   - source: https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/bmhs-list-map.pdf
   - as_of: Wayback snapshot 2025-10-31
   - review_by: 2027-11-08
   - note: town lookup in `raw/programs/community-mental-health-centers-towns-served.csv`; town lists date from 2022.

## vocational-rehabilitation-nh: VR New Hampshire (Vocational Rehabilitation)

- kind: programs
- question_type: help
- description: Job and career help for people with disabilities, including students still in high school.

1. VR New Hampshire, the NH Department of Education's Bureau of Vocational Rehabilitation, helps Granite Staters with disabilities prepare for, get and keep jobs; its statewide number is 603-271-3471.
   - source: https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation
   - as_of: Wayback snapshot 2026-09-22
   - review_by: 2027-11-08
2. To start with VR New Hampshire, a person can refer themselves or someone else by contacting VR or a regional office, or through the online referral portal (https://nhdoeconsumer.awareportals.com); a Rehabilitation Counselor then meets with them before the application and eligibility steps.
   - source: https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation/apply-vr-services
   - as_of: Wayback snapshot 2025-09-29
   - review_by: 2027-11-08
3. VR New Hampshire says its services have no charge, though customers may be asked to pay toward certain services in their Individualized Plan for Employment, and that there is currently no order of selection (waiting list by priority) for VR services in NH.
   - source: https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation/about-vr/faqs
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
4. Through School Transition Services, also called pre-employment transition services (Pre-ETS), VR New Hampshire works with school districts on job exploration counseling, work readiness skills, work-based learning, self-advocacy and counseling on post-secondary education; students can get Pre-ETS before applying for VR. The transition coordinator's number is 603-271-3993.
   - source: https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation/programs-and-services/school-transition-services
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
   - note: the list of five services is from the VR Students page (https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation/who-we-serve/students-disabilities); "before applying" is from the school transition fact sheet. No Pre-ETS age range was stated on any page opened.
5. VR New Hampshire has regional offices in Berlin, Concord, Keene, Manchester, Nashua and Portsmouth, plus Services for the Blind & Vision Impaired in Concord; its "VR Offices by Town" list assigns towns to offices, with a few towns shared by two offices.
   - source: https://www.education.nh.gov/who-we-are/deputy-commissioner/bureau-vocational-rehabilitation/about-vr/find-your-regional-office
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-08
   - note: the town list PDF was last modified 2024-01-11. Office lookup in `raw/programs/vocational-rehabilitation-offices-towns-served.csv`.

---

## Not retrieved

| Item | URL | What was tried |
|---|---|---|
| CTE sending schools for 9 NH centers: Fall Mountain, Mt. Washington Valley, North Point, Plymouth, Portsmouth, Somersworth, Sugar River Valley (Claremont and Newport), White Mountains | each center's site (in `cte-centers.csv`) | Home and about/admissions pages read; no list found. NH DOE publishes no sending-school list. An NH DOE research brief by RMC Research (January 2021, 2018-19 data) has regional high-school lists, but they're old and were not used. Ask NH DOE's Bureau of Career Development or each center. |
| Specific CTE programs (welding, machining, etc.) | center websites | The NH DOE grid lists only 17 broad program areas. Specific programs would have to be collected from each center's program-of-studies page. |
| CTE enrollment, completers and credentials by center | NH DOE | Not published by center; already on the data request list in `personas/data-gap-research.md`. |
| Current Purple Star schools list | https://www.education.nh.gov/news/purple-star-schools-meeting-unique-needs-military-children | Only the November 2021 release (14 schools, some towns named). Ask the NH National Guard or NH DOE. |
| Military school liaison for Pease | https://installations.militaryonesource.mil/military-installation/157-arw | Military OneSource lists no school liaison; nh.ng.mil returns 403 to scripts, so its pages were read from Wayback (June/July 2026). |
| UNH First Step (current page) | https://manchester.unh.edu/academics/unh-first-step-concurrent-credit-program | 403 to curl, WebFetch and a visible browser; only a Wayback copy from 2024-04-14. |
| 211 NH (live site) | https://211nh.org/ | Domain didn't resolve on 2026-11-08 (local DNS and 8.8.8.8); Wayback snapshot 2026-10-07 used. |
| NH Child Care Search program data | https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch | Not copied, by design: the plan says to link out to it. |
| A state-funded NH college grant (e.g. a Governor's Scholarship) | — | Not found. NH DOE's higher education page lists only Granite Edvance and the NH Charitable Foundation under grants and scholarships. The session's web-search budget ran out before a fuller search; don't state that no such program exists. |
| Plymouth State or other USNH high-school credit programs | — | Not found in one search; not checked further after the search budget ran out. |
| NH DOE education ombudsman | education.nh.gov | No ombudsman page in the Wayback index of education.nh.gov (about 54,000 archived URLs searched for "ombuds"). |
| Field documentation for the EFA feeds | app.nh.scholarshipfund.org, nhefa.scholarshipfund.org | None published. Stats labels come from the public page; provider grade codes are unexplained. Ask CSF NH before loading these into the database. |
| Current FCESS program directory | https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/fcess-directory.pdf | Not archived; the September 2025 version under an older file name was used. Intake numbers for Regions 8 and 10 differ between directories. |
| Family Support NH list of Family Resource Centers | familysupportnh.org | Domain doesn't resolve; Wayback has only 2003-2005 copies. The DHHS map data was used. No source gives the towns each FRC covers. |
| Current community mental health center town lists and addresses | https://www.dhhs.nh.gov/sites/g/files/ehbemt476/files/documents2/bmhs-list-map.pdf | Newest DHHS sheet is "Updated 1/18/22". NHCBHA's town lookup runs in JavaScript and wasn't extracted. Riverbend's emergency number conflicts between sources (844-743-5748 vs 844-753-5748). |
| VR 2026 pages and brochure | education.nh.gov VR pages | 2026 captures are 403s or redirects; 2025 copies used. Nashua office address printed as Manchester's; no Pre-ETS age range found. |
| Live dhhs.nh.gov and education.nh.gov pages for the family-support directories | — | 403 to scripts. The DHHS and DOE pages for Head Start, child care, the CTE list and the 21st CCLC list were opened in a visible browser; the area agency, FCESS, FRC, mental health and VR material came from Wayback (2025-08 to 2026-10). Re-check in a browser before publishing. |
| Kinship Navigator sites | https://www.nhchildrenstrust.org/kinship-guide | The guide's location page is a multi-column layout that doesn't extract cleanly; the navigators work out of Family Resource Centers, so use that directory. |

**Raw downloads.** The raw downloads are kept in `raw/programs/source/`:
- `dl/`: the national Head Start CSV, the two EFA JSON responses (`esa_vendors.json`, `efa_stats.json`), the NH DOE CTE PDFs (`dl/cte/`) and the September 2026 21st CCLC list (`dl/live/`)
- `agentA/`: the career centers' sending-school documents
- `agentB/`: the family-support sources
- `browser/`: pages saved from a browser

They were copied from the session scratch folder on 2026-11-08. The build scripts weren't kept.
