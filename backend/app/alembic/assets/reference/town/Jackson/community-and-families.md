# Jackson Community, Families, Early Childhood and School Alternatives

Part of the Jackson research (town/Jackson). Gathered November 13, 2026.

## Summary

This file covers the Jackson community side of the residents' questions: private day schools within driving distance, household incomes by bracket, Education Freedom Accounts (EFAs) for Jackson families, home education in SAU 9, licensed child care near Jackson, the school-age population trend, workforce housing, local scholarships and camp aid, the town's emergency services, and home sale prices near Jackson. The Census Bureau's American Community Survey estimates for Jackson (incomes, poverty, children, housing, home values and rents) are in the site's Census data and are not repeated here.

It has 10 shared-topic sections (13 topics before the November 13, 2026 fold) with 76 facts and 9 number tables. Raw copies are in `raw/community/` (Census JSON, NH DHHS child care data, the EFA marketplace feed, OSRM routes, Jackson School District annual reports 2017–2026, the town's 2025 hazard mitigation plan, housing commission papers and school web pages).

Main findings:
- No licensed child care program is located in Jackson, Glen, Intervale or Bartlett in the state's child care data; the nearest are in the town of Conway (North Conway, Conway and Center Conway). The programs themselves are in the site's child care data.
- White Mountain Waldorf School closed in June 2020. Northeast Woodland Chartered Public School in Conway, a Waldorf-inspired public charter school, is tuition-free for NH residents. Fryeburg Academy is on the EFA marketplace, and the EFA handbook allows tuition at a private school approved by the education department of the state where it is located.
- Jackson School District annual reports count 30 K–6, 10 grade 7–8 and 20 grade 9–12 students in February 2026, against 38, 16 and 28 in December 2016. The district's own "anticipated kindergarten" counts (2017–2024 reports) ranged from 0 to 10 a year, most often 2 to 5.
- The 2010 and 2020 Censuses counted 56% and 48% of Jackson's housing units as held for seasonal use (derived). Home values, rents, incomes and poverty for Jackson, Bartlett and Conway are in the site's Census data.
- Jackson's police department has a full-time chief and one sergeant and is dispatched by Carroll County. The town's 2025 hazard mitigation plan says cell access is "limited in places" and the town's warning system (Genasys) holds only landline numbers unless residents add others.

Main gaps: births by year for Jackson (state vital records and NH Health WISDOM refused automated access, and the town reports on the UNH archive were blocked); the NH DOE nonpublic school list and teacher turnover data (education.nh.gov refused access); the FCC broadband map; a NHAR sale-price report for Jackson (none is published); several small private schools' tuition.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.3 Private day schools within a reasonable winter drive | town-school-options-nearby 1–10; district-fees 1; jackson_private_school_drive_distance_tuition | partial | 17 schools with derived road distances; day tuition from 8 schools' own sites (Burke posts no day rate). NH DOE nonpublic list could not be opened; tuition for 8 small schools not found. "Reasonable" is not defined; the table gives miles and normal-conditions minutes |
| P2.3 How lower-income local kids fit in | site data: census (Jackson district); town-community-profile 1–3; jackson_household_income_distribution; town-family-help 1–8; district-pe-outdoor-and-athletics 1; site data: free and reduced lunch counts | partial | The site's Census data gives incomes and poverty; facts add incomes by bracket and the programs. No public data measures social fit |
| P9.2 EFAs for Fryeburg Academy or White Mountain Waldorf | town-school-options-nearby 11–20; library: efa-eligibility-and-cap, efa-uses-and-requirements, efa-how-to-apply, efa-provider-list, choice-efa-enrollment-growth; site data: EFA counts by town | full | White Mountain Waldorf School closed in 2020; Fryeburg Academy is an EFA provider |
| P9.3 What SAU 9 requires of homeschoolers | district-homeschool-access 1–6; library: home-education-rules, choice-hb-1268-home-education-history | partial | SAU 9 posts no home education page or forms; Jackson's policy IGBJ predates the 2026 law; the board is drafting a new policy |
| P10.1 Licensed infant, toddler and preschool care in or near Jackson | site data: child_care (Jackson district, and the other SAU 9 districts by town); town-child-care 1–5; library: head-start-eligibility, nh-child-care-search, child-care-scholarship-eligibility | full | The Conway programs' places, ages, openings, hours and rates are in the site's data. JGS preschool details are in another file |
| P10.3 School-age population trend, 5 to 10 years out | town-community-profile 4–12; jackson_children_by_age_census; jackson_district_students_by_level; jackson_anticipated_kindergarten; jackson_population_projection_opd; jackson_carroll_county_age_projection; site data: census (Jackson district); site data: JGS enrollment by grade | partial | No births-by-year data from the state; no NESDEC projection found; OPD projects total population only |
| P12.1 Workforce housing, enrollment and teacher retention | town-housing 1–13; jackson_housing_units_occupancy; site data: census (Jackson district); district-classrooms-and-staff 1–2 | partial | NH DOE teacher turnover data not retrieved; derived teacher continuity from staff lists; no data shows cause and effect |
| P17.2 Local scholarships and enrichment funds | town-family-help 1–8; district-pe-outdoor-and-athletics 1 | partial | NHCF Carroll County funds and town recreation eligibility not found |
| P8.3 / P19.2 (town side) Emergency response and communication | town-emergency-services 1–8 | partial | FCC coverage map not retrieved; school notification and security are in another file |
| P20.1 (housing cost side) Home prices in Jackson, Bartlett and Conway | site data: census (Jackson, Bartlett and Conway districts); town-housing 1–4; jackson_area_median_sale_price | partial | Home values and rents are in the site's Census data. No town-level sale-price report exists for Jackson; tax rates are in the site's data (property_tax) |

## town-school-options-nearby: Private, Charter and EFA Options for Jackson Families

- kind: local
- question_type: help
- description: Private, charter and other schools families in a town use, with distance and tuition, and EFA use

1. The federal Private School Universe Survey (PSS) search lists 40 private schools within 60 miles (straight line) of Jackson's ZIP code, 03846, for the 2023-24 school year. Only one of them, Cornerstone Christian Academy in Ossipee, is in Carroll County.
   - citation: NCES Search for Private Schools, ZIP 03846 within 60 miles; and Carroll County, NH search
   - source: https://nces.ed.gov/surveys/pss/privateschoolsearch/school_list.asp?Search=1&Zip=03846&Miles=60&NumOfStudentsRange=more&IncGrade=-1&LoGrade=-1&HiGrade=-1
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "Search Results: 40" and "Source: PSS Private School Universe Survey data for the 2023-24 school year." The PSS is a survey and misses schools that did not respond: Brewster Academy (Wolfeboro, Carroll County) and Holderness School are not in it. Parsed list in raw/community/private-schools/nces-pss-03846-60mi.txt; pages raw/community/private-schools/nces-pss-03846-60mi-p1.html to -p3.html; Carroll search raw/community/private-schools/nces-pss-carroll-nh.html.
2. The nearest private day schools to Jackson by road are in Fryeburg, Maine (New Life Christian Academy, 19.1 miles, and Fryeburg Academy, 19.8 miles) and Gorham, NH (Salve Regina Academy, 20.7 miles). Of the schools that post a day tuition, the nearest by road are Fryeburg Academy, Gould Academy in Bethel, Maine (42.0 miles) and Brewster Academy in Wolfeboro (50.2 miles) (derived).
   - citation: OSRM driving routes from Jackson village (derived); school addresses from NCES PSS and school sites
   - source: https://router.project-osrm.org/route/v1/driving/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Derived. Origin: the OpenStreetMap place node for Jackson village (44.1442760, -71.1811070) from Nominatim, raw/community/distances/nominatim-jackson.json. School addresses geocoded with Nominatim (raw/community/distances/nominatim-schools.json) and routed with the public OSRM demo server (raw/community/distances/osrm-routes-from-jackson.json). Distances are the fastest route in normal conditions; they do not account for snow, closures or traffic. See table jackson_private_school_drive_distance_tuition.
3. For comparison, by the same method Josiah Bartlett Elementary School is 8.8 road miles (about 16 minutes) and Kennett High School 12.2 road miles (about 26 minutes) from Jackson village (derived).
   - citation: OSRM driving routes from Jackson village (derived)
   - source: https://router.project-osrm.org/route/v1/driving/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Derived, same method as fact 2. Destinations geocoded by Nominatim: "Josiah Bartlett Elementary School, 1313, School Street, Bartlett" and "Kennett High School, 409, Eagles Way, Redstone, Conway". Bus ride times are in another file. Raw: raw/community/distances/osrm-routes-from-jackson.json.
4. Gould Academy in Bethel, Maine posts 2026-2027 tuition of $57,057 for day students and says its board sets tuition each year. It offers "Flexible Tuition" based on a family's assets, income, expenses and debts.
   - citation: Gould Academy, Affording Gould Academy
   - source: https://www.gouldacademy.org/admissions/affording-gould
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "2026-2027 Tuition ... Boarding Students: $79,921 Day Students: $57,057" and "Flexible Tuition amounts are generated based on an evaluation of assets, income, expenses, and debts". A search-engine summary quoted an older figure ($55,396); the live page was used. Raw: raw/community/private-schools/gould-affording.txt
5. Brewster Academy in Wolfeboro posts 2026-27 day tuition of $44,700, which includes academic, athletic and community programs and lunch in the dining hall.
   - citation: Brewster Academy, Tuition and Financial Aid
   - source: https://www.brewsteracademy.org/admissions/tuition
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "2026-27 Tuition ... Boarding: $80,800 Day: $44,700" and "Day student tuition includes academic, athletic, and community programs and lunch in the dining hall." Grades not stated on the pages read. Raw: raw/community/private-schools/brewster-tuition.txt
6. Holderness School, a grade 9 to postgraduate school, posts 2026-2027 day tuition of $55,900; New Hampton School (grades 9-12 and postgraduate) posts $46,350; and Hebron Academy in Maine (grades 6-12 and postgraduate) posts $20,900 for day students.
   - citation: Holderness School, Tuition & Financial Aid; New Hampton School, Tuition & Financial Aid; Hebron Academy, Tuition Reset
   - source: https://www.holderness.org/admission/tuition-financial-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: Holderness "2026-2027 Tuition BOARDING $82,400 DAY $55,900" and "A grade 9-PG boarding and day, coeducational college-preparatory school"; New Hampton (https://www.newhampton.org/admission/tuition-financial-aid) "2026-2027 Tuition Boarding Tuition: $$77,480 Day Tuition: $$46,350"; Hebron (https://www.hebronacademy.org/admissions/affording-hebron/tuition-reset) "2026-2027 Tuition Rates For Grades 6-12 & Postgraduate ... Day Student $20,900" and "Tuition rates do not include optional or required fees such as ESOL, Academic Support, International Health Insurance, or the Winter Recreational Sports Fee". Raw: raw/community/private-schools/holderness-tuition.txt, newhampton-tuition.txt, hebron-tuition.txt
7. Waterville Valley Academy, a ski and snowboard academy, runs a grades 6-8 day program (late November to March) at $31,000 and a grades 9-12 winter term (early November to March) at $39,538 for grades 9-10 day students and $41,000 for grades 11-12 day students. Its students keep following their home school's curriculum, with academy support.
   - citation: Waterville Valley Academy, WVA Middle School and WVA Winter Term pages
   - source: https://www.register.wvbbts.org/about/wva-winter-term/88479
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "Term Dates: Early November – March ... Grades: 9–12 | Day and Boarding Options Available"; "9th - 10th Grade Day Student: $39,538 ... 11th - 12th Grade Day Student: $41,000"; "Students continue with their home school curriculum during their time at WVA." Middle school page (https://www.register.wvbbts.org/about/wva-middle-school/88488): "Term Dates: Late November – March Grades: 6–8 | Day Program" and "Middle School Day: $31,000". The pages do not state the school year of these prices; they link a 2025-2026 handbook. Raw: raw/community/private-schools/wva-winter-term.txt, wva-middle-school.txt
8. Carrabassett Valley Academy, a ski academy in Maine, posts 2026/2027 full-year day tuition of $52,500 for grades 7-8 and $57,500 for grades 9-12, and winter-term day tuition of $36,000 and $41,000. Burke Mountain Academy in Vermont posts no day rate; its full-term academy boarding rate is $72,000 for 2026-27.
   - citation: Carrabassett Valley Academy, Tuition & Financial Aid; Burke Mountain Academy, Tuition & Financial Aid
   - source: https://www.gocva.com/admissions/tuition-and-financial-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: CVA page lists each price before its label: "7th-8th Grade $70,400 FULL YEAR BOARDING $52,500 FULL YEAR DAY $48,550 WINTER TERM BOARDING $36,000 WINTER TERM DAY 9th-12th Grade $75,400 FULL YEAR BOARDING $57,500 FULL YEAR DAY $53,550 WINTER TERM BOARDING $41,000 WINTER TERM DAY". Burke (https://www.burkemtnacademy.org/admissions/tuition-and-financial-aid): "2026-27 Tuition Rates Academy - Full Term Boarding - $72,000 ... U14 Academic + Athletic - $24,000". Both are more than 80 road miles from Jackson (table). Raw: raw/community/private-schools/cva-tuition.txt, burke-tuition.txt
9. Several small religious or community private schools near Jackson do not post tuition on a website that could be read: New Life Christian Academy (Fryeburg, Maine, grades 1-11), Salve Regina Academy (Gorham, PK-8), Shepherds River Mennonite School (Brownfield, Maine, grades 1-10), Unity Christian School (Berlin, K-12), Cornerstone Christian Academy (Ossipee, PK-8) and Mount Royal Academy North (Lancaster, PK-7).
   - citation: NCES PSS 2023-24 search results (grades); school web searches
   - source: https://nces.ed.gov/surveys/pss/privateschoolsearch/school_list.asp?Search=1&Zip=03846&Miles=60&NumOfStudentsRange=more&IncGrade=-1&LoGrade=-1&HiGrade=-1
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Grades and enrollments as listed by PSS 2023-24. Salve Regina's listed web address (srca.org) redirected to an unrelated site and was not followed. Third-party directories quote tuition for some of these schools; they were not used. See Not retrieved. Raw: raw/community/private-schools/nces-pss-03846-60mi.txt
10. Northeast Woodland Chartered Public School in Conway is a public charter school, not a private school. It is tuition-free for New Hampshire residents, admits K-8 students by lottery when applications exceed seats, and said in May 2026 that most classrooms for 2026-27 were full.
   - citation: Northeast Woodland Chartered Public School, Enrollment & Lottery and FAQ
   - source: https://www.northeastwoodland.org/enrollment-lottery
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Northeast Woodland Chartered Public School
   - note: Page text: "There is no tuition fee for New Hampshire residents." (FAQ, https://www.northeastwoodland.org/faq) and "As of May 2026, space for the 2026–2027 school year is very limited, and most classrooms are currently full." Address "53 Technology Lane Conway, NH 03818". Its address could not be geocoded in OpenStreetMap, so no road distance is given. Charter school rules: library topic charter-schools. Raw: raw/community/private-schools/nwcs-enrollment-lottery.txt, nwcs-faq.txt
11. Fryeburg Academy (745 Main St, Fryeburg, Maine) is listed in the EFA marketplace of the Children's Scholarship Fund (CSF), the organization that runs New Hampshire's EFA program, so families can pay it with EFA funds. White Mountain Waldorf School is not listed.
   - citation: CSF New Hampshire EFA marketplace feed (provider 3312)
   - source: https://app.nh.scholarshipfund.org/marketplace
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Feed https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors (undocumented) listed 3,608 providers on 2026-11-13; entry: id 3312, "Fryeburg Academy", organization_type "provider", grades 0-12, "745 Main St, Fryeburg, ME 04037". No name containing "White Mountain Waldorf" appears; the school closed in 2020 (topic town-school-options-nearby 18–20). The library's 2026-11-08 copy (additional-data/raw/programs/efa-providers.csv) agrees. Raw: raw/community/efa/efa-marketplace-vendors-2026-11-13.json
12. The CSF EFA parent handbook (August 2026) defines a private school, for EFA tuition, as a nonpublic school approved at least for attendance purposes by the NH Department of Education or by the education department of the state where the school is located. Out-of-state schools are therefore not excluded by that definition.
   - citation: CSF New Hampshire, EFA Parent Handbook (8-2026), "Private school tuition and student fees"
   - source: https://nh.scholarshipfund.org/wp-content/uploads/2026/09/Parent-Handbook-CSF-8-2026.pdf
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Handbook text: "A private school is a nonpublic school approved for (at a minimum) attendance purposes by the NH Department of Education or by the Department of Education of the respective state in which the school is located." RSA 194-F:2, II(a) lists "Tuition and fees at a private school" with no in-state limit, and RSA 194-F:6 lets the scholarship organization approve providers (raw/community/efa/rsa-194-F-2.txt, rsa-194-F-6.txt). The marketplace includes other out-of-state schools such as Gould Academy, Hebron Academy, Kents Hill School and Burke Mountain Academy. Raw: raw/community/efa/csf-efa-parent-handbook-2026-08.txt
13. The Maine Department of Education lists Fryeburg Academy among the "Private Secondary (9-12) Schools Approved for Public Tuition Funds" for 2026-2027, under Maine law Title 20-A, §5806, with its 2026-27 rate "to be calculated December 2026."
   - citation: Maine DOE, Fiscal Reports: Tuition
   - source: https://www.maine.gov/doe/funding/reports/tuition
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Page text under "2026-2027 Private Secondary (9-12) Schools Approved for Public Tuition Funds ... Approved Secondary (9-12) Private Schools in Maine per Title 20-A, §5806": "Fryeburg Fryeburg Academy To be calculated December 2026". Gould Academy and Hebron Academy are on the same list. This is Maine's approval to receive public tuition money; the Maine page for attendance-only approval was not opened. Raw: raw/community/efa/maine-doe-tuition-reports.txt; earlier rates in maine-doe-private-tuition-rates-fy21-fy26.txt
14. Jackson Grammar School itself is listed in the EFA marketplace as "SAU #9 Jackson Grammar School," and New Hampshire law lets EFA money pay for classes and programs a district public school provides.
   - citation: CSF EFA marketplace feed (provider 2889); RSA 194-F:2, II(d)
   - source: https://app.nh.scholarshipfund.org/marketplace
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Feed entry id 2889 "SAU #9 Jackson Grammar School", organization_type "provider". RSA 194-F:2, II(d): "Services contracted for and provided by a district public school, chartered public school, public academy, or independent school, including, but not limited to, individual classes and curricular activities and programs." EFA students' access to their district's courses is in library topic choice-hb-1817-efa-public-school-courses. Raw: raw/community/efa/efa-marketplace-vendors-2026-11-13.json; raw/community/efa/rsa-194-F-2.txt
15. The EFA marketplace listed 48 providers with map locations within 25 miles (straight line) of Jackson village on November 13, 2026 (derived). They include Fryeburg Academy, New Life Christian Academy and Salve Regina Academy; Tin Mountain Conservation Center in Albany; Living Shores Aquarium in Bartlett; a reading specialist on Dundee Road in Jackson (Intervale mailing address); and the Mount Washington Observatory, Arts in Motion Theater Camp and the Mount Washington Valley Skating Club in the Conway area.
   - citation: CSF EFA marketplace feed, filtered by distance (derived)
   - source: https://app.nh.scholarshipfund.org/api/marketplace/esa_vendors
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Derived: great-circle distance from Jackson village (44.1442760, -71.1811070) to each provider's listed latitude/longitude; 30 "provider", 10 "school", 4 "tutor" and 4 "vendor" entries. 783 marketplace entries statewide have no coordinates, so nearby providers without them (for example The Lilliputian School, North Conway, and Saco River Swimming, Center Conway) are missing from the count. Mountain Top Music Center (Conway) also has no coordinates. Full list: raw/community/efa/efa-providers-within-25mi-of-jackson-2026-11-13.csv
16. The CSF public statistics feed showed 2 Jackson students eligible for an EFA for 2026-27 on November 13, 2026, both in a priority group. NH Department of Education EFA counts by town are in the site's data.
   - citation: CSF NH EFA statistics feed, town "Jackson"
   - source: https://nhefa.scholarshipfund.org/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Feed https://nhefa.scholarshipfund.org/api/admin/stats (undocumented): {"town": "Jackson", "count": 2, "priority_count": 2, "non_priority_count": 0, "frl_count": 1, "waitlist_count": 0}. Counts change daily. The site's education_freedom_account_entry table (town 271) holds NH DOE counts; it showed "Base Aid" 4.00 for 2027 on 2026-11-13, and the two sources count differently. Raw: raw/community/efa/efa-stats-2026-11-13.json
17. New Hampshire's EFA law covers fee-for-service transportation to an education service provider, but the CSF handbook says ride services such as Uber or Lyft are not eligible.
   - citation: RSA 194-F:2, II(n); CSF EFA Parent Handbook (8-2026)
   - source: https://gc.nh.gov/rsa/html/XV/194-F/194-F-2.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Statute: "(n) Fees for transportation paid to a fee-for-service transportation provider for the student to travel to and from an education service provider." Handbook: "An example of a fee-for-service transportation provider is a bus company that transports a child ... Ride services such as Uber or Lyft are not eligible expenses." Bears on a Jackson family driving to Fryeburg (19.8 road miles). Raw: raw/community/efa/rsa-194-F-2.txt; raw/community/efa/csf-efa-parent-handbook-2026-08.txt
18. White Mountain Waldorf School, a private school in Albany in the Mount Washington Valley, closed at the end of June 2020 after 35 years. Its trustees decided on May 4, 2020 to close it.
   - citation: Conway Daily Sun, "White Mountain Waldorf School closing after 35 years," June 2, 2020
   - source: https://www.conwaydailysun.com/business/local/white-mountain-waldorf-school-closing-after-35-years/article_99697104-a4e7-11ea-8c4f-ff536a6acf78.html
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: News is the only source found. Article text: "ALBANY — After 35 years of serving families in the Mount Washington Valley, the White Mountain Waldorf School will close its doors at the end of the month." and "The decision to close was made May 4 by the school's trustees". The NH DOE nonpublic school list could not be opened to confirm. A directory lists it as "Closed 2024" (raw/community/efa/psr-wmws.txt); the 2020 news report is the primary account. Raw: raw/community/efa/cds-wmws-closing-2020.html (.txt)
19. Northeast Woodland Chartered Public School, at 53 Technology Lane in Conway, is a Waldorf-model, nature-based public charter school for kindergarten through grade 8. New Hampshire residents pay no tuition; out-of-state students pay $11,227 for 2026-27.
   - citation: Northeast Woodland Chartered Public School, About Us, FAQ and Enrollment & Lottery
   - source: https://www.northeastwoodland.org/faq
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Northeast Woodland Chartered Public School
   - note: About page: "Our vision at Northeast Woodland is to create an environment of nature-based learning focused on a Waldorf education model"; FAQ: "As a State of NH chartered public school, Northeast Woodland is tuition-free for New Hampshire residents" and "Tuition for K-8th out-of-state students is $11,227". Because it is a public school, EFA rules do not apply to its K-8 program. Raw: raw/community/private-schools/nwcs-about.txt, nwcs-faq.txt, nwcs-enrollment-lottery.txt
20. Northeast Woodland's school day runs 8:00 am to 2:40 pm Monday through Thursday and 8:00 am to 1:10 pm on Fridays. Its 2026 open enrollment ran January 30 to March 6, 2026, with a lottery the second week of March. Under the school's lottery policy (March 11, 2026), children of faculty, staff and founding board members are placed first, then siblings of current students, before the lottery is held.
   - citation: Northeast Woodland, Family Information and Enrollment & Lottery; NWCPS Enrollment Lottery Rankings policy (approved March 11, 2026)
   - source: https://www.northeastwoodland.org/enrollment-lottery
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Northeast Woodland Chartered Public School
   - note: Corrected November 13, 2026 from the Conway research: this fact first said siblings are placed first, as the enrollment page still says. The board's March 11, 2026 policy puts staff and founding-board children ahead of siblings (town/Conway/raw/community/charters/nwcs-policy-enrollment-lottery-rankings-2026-03-11.txt: "Children of faculty, staff, and founding Northeast Waldorf Education Foundation Board members ... Siblings of existing students ... will be placed prior to holding the lottery after staff children are"). Text: "Applications open on January 30, 2026 ... runs through March 6, 2026"; "The lottery ... will be held the second week of March 2026"; "All siblings of existing students who have completed applications by the close of open enrollment, will be placed prior to holding the lottery." Family Information: "Our school day runs from 8am-2:40pm on Monday, Tuesday, Wednesday and Thursday, and from 8:00am-1:10pm on Fridays." Transportation is not described on the pages read; charter transportation rules are in library topic charter-schools. Raw: raw/community/private-schools/nwcs-family-info.txt, nwcs-enrollment-lottery.txt

## district-fees: Fryeburg Academy's Posted Tuition and Deposits

- kind: local
- question_type: local_practice
- description: Costs families may pay: sports, field trips, supplies, technology, instruments and other fees, and help with them

1. Fryeburg Academy, a private academy in Fryeburg, Maine, posts a commuter day tuition of $22,500 for 2027-28. It also posts a $500 refundable security deposit for boarding and commuter day students and an optional $1,500 recreational ski program.
   - citation: Fryeburg Academy, Tuition + Financial Aid
   - source: https://www.fryeburgacademy.org/admissions/tuition-financial-aid
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Page text: "Tuition 2027-28 ... Commuter Day Tuition: $22,500" and "$500 Refundable Security Deposit: This mandatory fee for boarding and commuter day students" and "Recreational Ski Program: $1,500. Optional for boarding and commuter day students." This is the price for a family paying privately. Jackson's district tuition agreement with Fryeburg Academy from 2027-28 is in additional-data/district-practices.md (high school options). Raw: raw/community/private-schools/fryeburg-tuition.txt

## town-community-profile: Jackson's Household Incomes, Children and School-Age Population

- kind: local
- question_type: local_practice
- description: A town's people beyond the site's Census estimates: decennial Census counts and ages, births, population projections, the enrollment outlook and civic life

1. The Census Bureau's American Community Survey (ACS) for 2020-2024 estimates that 31.8% (±12.4) of Jackson households had incomes of $200,000 or more and that 27.5% had incomes under $50,000 (derived sum of brackets, ±16.1). For New Hampshire the shares are 16.8% (±0.4) and 23.8% (±0.5).
   - citation: ACS 5-year 2020-2024, table S1901 (Income in the Past 12 Months); table B19001 (Household Income)
   - source: https://data.census.gov/table/ACSST5Y2024.S1901?g=060XX00US3300338260
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: S1901_C01_011E 31.8 (±12.4) for $200,000 or more; NH 16.8 (±0.4). Under $50,000 is derived by adding the first five brackets (7.9 + 1.8 + 7.7 + 4.5 + 5.6 = 27.5); NH: 3.2 + 2.3 + 4.9 + 5.3 + 8.1 = 23.8. Counts in B19001: 141 (±54) of 443 households at $200,000 or more; 122 (±76, derived) under $50,000; NH 132,209 (±2,903, derived) of 555,822. The margins for the under-$50,000 shares are derived from the B19001 count margins with the Census Bureau's formula for a proportion. Checked November 14, 2026 against the site's Census data (B19001, 2020-2024): the counts match. Median household income, poverty rates and the number of children are in the site's Census data, so they are not repeated here. See table jackson_household_income_distribution. Raw: raw/community/census/ACSST5Y2024.S1901-jackson.json, ACSDT5Y2024.B19001-jackson.json
2. The share of Jackson Grammar School students eligible for free or reduced-price meals is in the site's data (free and reduced lunch counts by district and school).
   - citation: NH Education Facts database, district_reduced_lunch (district 271)
   - source: https://nhfacts.com
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Pointer only, so the Ask uses its own tools. A read-only check on 2026-11-13 showed counts for 2012-2026. Meals policies are in another file.
3. No public data source measures how children from lower-income families fit in socially at Jackson Grammar School, Josiah Bartlett Elementary or Kennett High School. The facts available are the site's Census income and poverty estimates, incomes by bracket (fact 1), meal eligibility counts, class and cohort sizes, and the programs that lower costs (topic town-family-help 1–8; district-pe-outdoor-and-athletics 1).
   - citation: Research note (no source measures this)
   - source: https://data.census.gov/table/ACSST5Y2024.S1901?g=060XX00US3300338260
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Searched the Jackson School District annual reports (2017-2026), the JGS site and SAU 9 site for any survey of student belonging by income; none was found. Statement of a gap, written so the Ask can say so plainly.
4. The Census counted 19 Jackson residents under age 5 and 87 aged 5 to 17 in 2010, and 18 under 5 and 93 aged 5 to 17 in 2020 (derived sums), while Jackson's total population grew from 816 to 1,028.
   - citation: 2010 Census SF1 table P12; 2020 Census DHC table P12 (Sex by Age), Jackson town
   - source: https://data.census.gov/table/DECENNIALDHC2020.P12?g=060XX00US3300338260
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Derived by adding male and female age groups. 2010: under 5 = 12 + 7; 5-17 = (14 + 23 + 8) + (12 + 19 + 11). 2020: under 5 = 13 + 5; 5-17 = (15 + 14 + 12) + (23 + 15 + 14). See table jackson_children_by_age_census. Raw: raw/community/census/DECENNIALSF12010.P12-jackson.json, DECENNIALDHC2020.P12-jackson.json; labels in labels-dec-*.json
5. The Jackson School District's annual reports count the district's students by level each winter. The count fell from 38 in grades K-6, 16 in grades 7-8 and 28 in grades 9-12 on December 31, 2016 to 30, 10 and 20 on February 5, 2026, after a peak of 49 in grades K-6 in December 2018 and January 2021.
   - citation: Annual Reports of the School District of Jackson, 2017-2026, Enrollment pages
   - source: https://drive.google.com/drive/folders/1LP1rwzxaO8TST7NY9MI0lD7ihtpLyekv
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Scanned PDFs; transcribed from images raw/community/school-district/jackson-sd-annual-report-YYYY-enrollment-page.png (2017 report: "(as of December 31, 2016) Total K-6 = 38 Total 7-8 = 16 Total 9-12 .... 28"; 2026 report: "(as of February 5, 2026) Total K-6 = 30 Total 7-8 = 10 Total 9-12 = 20"). The reports do not say whether the K-6 count includes non-resident pupils, but the March 2, 2023 district meeting minutes say 43 of the 47 students then at JGS were residents, two were teachers' children and two were tuition students; NH DOE's October counts for Jackson Grammar School are in the site's data and differ. Table: jackson_district_students_by_level.
6. From 2017 to 2024 the district's annual reports also listed "anticipated enrollment" of kindergartners for the next five years, which ranged from 0 to 10 a year and most often 2 to 5. The last list, in the 2024 report, expected 6 in 2024, 5 in 2025, 4 in 2026, 5 in 2027 and 2 in 2028.
   - citation: Annual Reports of the School District of Jackson, 2017-2024, "Anticipated Enrollment"
   - source: https://drive.google.com/file/d/1cPtbQOSy3H-df9W9N-nc3RxwWCR9GbDt/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Transcribed from image raw/community/school-district/jackson-sd-annual-report-2024-enrollment-page.png: "Entering Kindergarten in 2024 6 ... 2025 5 ... 2026 4 ... 2027 5 ... 2028 2". The 2025 and 2026 reports have no anticipated-enrollment section. The reports do not say how the counts were made. Actual kindergarten counts the next winter sometimes differed (table jackson_anticipated_kindergarten).
7. Jackson Grammar School's enrollment by grade (2015-16 to 2024-25) is in the site's data.
   - citation: NH Education Facts database, school_enrollment (school 20355)
   - source: https://nhfacts.com
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Pointer only. A read-only check on 2026-11-13 showed totals for 2016-2025.
8. NH's Office of Planning and Development (OPD) projects Jackson's total population at 1,108 in 2030, 1,127 in 2035 and 2040, and 1,093 in 2050, from 1,028 in the 2020 Census. OPD's municipal projections give total population only, not ages. OPD's estimate for 2025 is 1,049.
   - citation: OPD, State, County, and Municipal Population Projections: 2020-2050 (September 2022), Appendix B Table 2; OPD 2025 Population Estimates (July 17, 2026)
   - source: https://www.nheconomy.com/getmedia/0205c62d-9c30-4b00-9c9e-d81d8f17b8b3/NH-Population-Projections-2020-2050-Final-Report-092022.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Report text: "Jackson town 1,028 1,073 1,108 1,127 1,127 1,113 1,093" under "2020 Census 2025 2030 2035 2040 2045 2050". Method: "OPD projects the 10 counties, then the respective (within counties) municipalities"; for Carroll County, municipal shares were adjusted for planned housing in 2020-2025 and then held constant. 2025 estimate: "Jackson 816 1,028 1,049" (https://www.nheconomy.com/getmedia/62b7f54e-dced-456c-9bbf-cac23ea1f7d5/2025-Population-Estimates.pdf). See table jackson_population_projection_opd. Raw: raw/community/opd-population-projections-2020-2050.txt, opd-2025-population-estimates.txt
9. For Carroll County as a whole, OPD projects school-age children (ages 5 to 19) at 6,187 in 2025, 6,272 in 2030, 6,443 in 2035 and 6,702 in 2040, and children under 5 at 2,058 in 2025 falling to 1,853 in 2040 (derived sums of age groups).
   - citation: OPD, Population Projections 2020-2050, Table 8: Projected Populations for Carroll County by Age Groups and Sex
   - source: https://www.nheconomy.com/getmedia/0205c62d-9c30-4b00-9c9e-d81d8f17b8b3/NH-Population-Projections-2020-2050-Final-Report-092022.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Derived: 5-9 + 10-14 + 15-19 totals (2025: 1,919 + 2,220 + 2,048; 2030: 2,245 + 2,013 + 2,014; 2035: 2,235 + 2,369 + 1,839; 2040: 2,147 + 2,374 + 2,181). County figures, not Jackson. Table: jackson_carroll_county_age_projection. Raw: raw/community/opd-population-projections-2020-2050.txt
10. The Jackson Housing Commission's June 2025 presentation said Jackson had "only 1 birth in 2023, projected 5 births in 2024" and that Jackson Grammar School was "at just 60% enrollment." It did not give a source for the birth figures.
   - citation: Jackson Housing Commission, "Jackson Housing Happy Hour" slides, June 13, 2025
   - source: https://docs.jacksonhousingcommission.org/documents/publications/jhc_hhh_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Slide text: "EDUCATIONAL AND COMMUNITY IMPACT ➔ Jackson Grammar School at just 60% enrollment ➔ Projected to be lower next year ➔ Immediate demographic concerns: Only 1 birth in 2023, projected 5 births in 2024". This is the only Jackson birth figure found; state vital records were not reachable (see Not retrieved). Raw: raw/community/housing/jhc-hhh-2025-slides.txt
11. At the March 5, 2026 district meeting, Jackson voters adopted RSA 194-D open enrollment for Jackson Grammar School (grades K-6), which lets nonresident students apply to attend under admission criteria and class-size limits set by the school board. In March 2026 the board's policy committee was writing the policies.
   - citation: Jackson School District Warrant 2026, Article 6 (in the 2026 annual report); Jackson School Board Minutes, March 16, 2026
   - source: https://drive.google.com/file/d/1T7p75Vh1QrxEkyb5IClUT3j1jjZNyRkJ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Warrant (scanned, transcribed from raw/community/school-district/jackson-sd-annual-report-2026.ocr.txt): "ARTICLE 6. Shall the Jackson School District adopt the provisions of NH RSA Chapter 194-D to designate the Jackson Grammar School grades Kindergarten through six as an Open Enrollment Elementary School ... and further to allow nonresident students to apply for admission and enroll in Jackson Grammar School, subject to the School Board approving admission criteria, limiting each grade enrollment to a maximum class size". Minutes: "a. Open Enrollment – Town passed this. Policy Committee is working on policies." Open enrollment law: library topic open-enrollment-status. Raw: raw/community/school-district/jackson-board-minutes-2026-03-16.txt
12. A letter from three residents read at the March 6, 2025 Jackson School District meeting, and printed in the district's 2026 annual report, said the 2025/26 census showed a Jackson Grammar School population of 29 Jackson students plus five children of non-resident staff, and voiced "growing concern regarding the declining JGS student population."
   - citation: "Address to Jackson School Board, Annual Meeting March 6th, 2025," in the Annual Report of the School District of Jackson (2026), pages 24-25
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Scanned; OCR text: "in recent years we have also voiced growing concern regarding the declining JGS student population. According to the 2025/26 census, the school population will be 29 Jackson students, plus five non-resident staff member children." Signed by three residents. This is the residents' statement, not a district count. Raw: raw/community/school-district/jackson-sd-annual-report-2026.ocr.txt

## town-family-help: Local Scholarships, Camp Aid and Programs That Lower Costs for Jackson Families

- kind: local
- question_type: help
- description: Local programs and funds that help families with costs

1. Jackson Grammar School's website has a "Local Programs & Scholarships" section. In fall 2026 it linked a summer camp scholarship application, a JGS PTO event, Friends of the Whitney Community Center events and the Jackson Community Association's scholarship for high school graduates.
   - citation: Jackson Grammar School, Newsletters, Local Programs, Scholarships
   - source: https://jgs.sau9.org/newsletters
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "Local Programming for Kids, Summer Camps & Scholarships, Scholarships for High School Graduates ... JGS PTO's Halloween Hollow Treat Trail ... Friends of the WCC present Spooky Stories ... Camp Scholarships Application for Summer Camps ... Jackson Community Association Scholarship Application". The PTO flyer link returned an access error. Raw: raw/community/programs/jgs-newsletters.txt
2. The camp scholarship form posted by Jackson Grammar School is from the Bushee Thorn Mountain Trust for 2026. It gives priority to Christian camps, then special-needs camps, then YMCA/YWCA, Scout and Tin Mountain camps, for which the award limit is $350. Applications were due April 6 to the trustee, minister or counselor who gave out the form.
   - citation: Bushee Thorn Mountain Trust, Application for Camp Scholarship – 2026 (linked from the JGS site)
   - source: https://files.smartsites.parentsquare.com/10273/camp_scholarship_application_2026.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Page text: "Priorities for awarding camperships are as follows: 1. Christian camps 2. Special needs camps 3. YMCA/YWCA, Girl/Boy Scout camps, Tin Mountain camps: ***Award Limit $350***" and "Please return application to the Trustee, Minister or Counselor from whom you received it by April 6." The form asks for estimated annual family income. A private mailing contact on the form is not repeated here. Raw: raw/community/programs/jgs-camp-scholarship-application-2026.txt
3. Tin Mountain Conservation Center in Albany offers summer camp scholarships covering 90%, 50% or 25% of camp costs. Camp places and scholarships are first come, first served, and families are asked to register first and then apply.
   - citation: Tin Mountain Conservation Center, Summer Camp Scholarship Application Form
   - source: https://tinmountain.org/file_download/4189723e-6c2e-4d70-a678-5de367f5421e
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Form text: "Enrollment in Tin Mountain Camps and scholarships are on a first come, first served basis ... Full Scholarship (90% funds covered) ... Half Scholarship (50% of funds covered) ... Quarter Scholarship (25% of funds covered)". Undated Word form; year not stated. Tin Mountain is also an EFA marketplace provider (topic town-school-options-nearby 11–17). Raw: raw/community/programs/tinmountain-camp-scholarship-form.docx (.txt)
4. The Eastern Slope Ski Club's Winter Snow Sports Fund gives need-based awards toward program fees for Carroll County residents in grades 3-12 who ski or ride in Alpine, Nordic or snowboard programs: up to 20% for season-long skill programs, up to 30% for local youth race programs and up to 40% for scored racing at U16 and up. Applicants send tax returns, a letter, proof of registration and two recommendations.
   - citation: Eastern Slope Ski Club, ESSC Winter Snow Sports Fund
   - source: https://easternslopeskiclub.org/essc-scholarship-program/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "scholarship funds are limited and allocated on financial needs ... Skill development season long programs, up to 20%; USSA racing, up to 30% for local mountain race programs, basically U10-U14 ... is up to 40%, USSA and FIS racing for MWVST athletes U16 and up" and "Recipients must abide by the ESSC Code of Conduct, be a resident of Carroll County and currently in grades three through twelve." Recipients also volunteer at the club's ski sale. Raw: raw/community/programs/essc-scholarship-program.txt
5. Jackson XC (the Jackson Ski Touring Foundation) runs "Speed Camp," a no-charge coaching program for skiers in grades K-6 with some experience, on non-holiday Mondays after school, and gives free tickets and rentals on non-holiday Tuesdays to up to two adults who bring children under 5. Middle school, high school and college ski team members may ski at no charge with pre-registration.
   - citation: Jackson XC, Youth Instruction & Programs
   - source: https://www.jacksonxc.org/youth-instruction-programs/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "A no-charge coaching program for grades K-6 who already have some ski experience. Non-holidays Mondays 3:15 to 4:00"; "Tuesdays, non-holiday, JacksonXC offers free tickets and rentals ... to skiers (up to two adults) who bring a child or children under the age of 5"; "High/Middle School and College Ski Teams (team members) may ski at no charge with pre-registration." The page also says Jackson XC is the site of JGS's weekly early-release ski program. Raw: raw/community/programs/jacksonxc-youth.txt
6. The Friends of the Whitney Community Center, which runs community programs at the center on the Jackson Grammar School campus, says its mission is to offer "diverse, affordable programs." In 2026 it published four program catalogs a year with 15-20 programs each and ran three summer camps.
   - citation: Jackson School Board Minutes (DRAFT), October 19, 2026, attachment "The Future of WCC Community Programming"
   - source: https://drive.google.com/file/d/1B9DSqRrrnOyvR3lbMnycQaxBs8GBMxoH/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Slide text: "The Friends of the Whitney Community Center support a vibrant and connected community by offering diverse, affordable programs"; "Four sessions/catalogs a year with 15-20 programs per catalog ... Summer Camps – 3 in 2026"; "FWCC utilizes the WCC for programming at no charge". The slides do not describe scholarships or fee waivers. Draft minutes. Raw: raw/community/school-district/jackson-board-minutes-2026-10-19-draft.txt
7. The Jackson Community Association, founded with an endowment from summer resident Bertha Rogers in 1961, gives the Bertha F. Rogers scholarships to Jackson high school graduates. Seniors apply in the spring (deadline May 10), and funds are sent to the student's college after a first semester with at least a 2.0 grade point average. The association has also funded projects at Jackson Grammar School.
   - citation: Jackson Community Association, "A History of the Jackson Community Association" (linked from the JGS site)
   - source: https://files.smartsites.parentsquare.com/10273/a_history_of_the_jackson_community_associationdocx.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Text: "In the summer of 1961 Miss Rogers wrote ... asking ... to form the Jackson Community Association"; "The deadline for applications to be submitted is May 10th. Scholarship funds are sent directly to the student's college after successful completion of the fall semester with a minimum grade point average of 2.0"; "the JCA has supplied the Jackson Grammar School with funding for a weather station, a photography project, classroom books and a nature trail." Application: https://files.smartsites.parentsquare.com/10273/jcaapplicationupdate26docx.pdf. Raw: raw/community/programs/jca-history-scholarship.txt, jca-scholarship-application-2026.txt
8. The Town of Jackson's welfare administrator provides general assistance to residents in financial need. Help with basic needs such as shelter, food, medications, rent and utilities is given as vouchers paid to vendors, and the office refers families to other programs.
   - citation: Town of Jackson, General Assistance
   - source: https://www.jackson-nh.gov/boards-committees/select-board/general-assistance/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "Interim, emergency assistance with basic needs is provided for those unable to provide for themselves. Basic needs include, but are not limited to, shelter, food, medications, rent, and utilities. Assistance is issued in the form of vouchers for these items paid directly to a vendor." Contact: Welfare Administrator, 603-383-4223 x 101. Raw: raw/community/town-general-assistance.txt

## district-pe-outdoor-and-athletics: Eastern Slope Ski Club Programs for SAU 9 and SAU 13 Children

- kind: local
- question_type: local_practice
- description: PE, recess, outdoor and environmental learning, ski programs, partnerships with outdoor organizations, and school sports teams

1. The Eastern Slope Ski Club runs junior ski and snowboard programs for children in SAU 9 and SAU 13 (Alpine and Nordic for grades 1-6, snowboarding for grades 5-6), with inexpensive equipment rentals available at registration.
   - citation: Eastern Slope Ski Club, Junior Programs
   - source: https://easternslopeskiclub.org/junior-programs/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Page text: "The Junior Programs are for all children in SAU 9 & 13 ... Alpine Skiing: Grades 1-6 Nordic (Cross Country) Skiing: Grades 1-6 Snowboarding: Grades 5-6" and "We can help with inexpensive equipment rentals for the duration of the program." Fees are paid in a portal and are not listed. How JGS schedules skiing is in another file. Raw: raw/community/programs/essc-junior-programs.txt

## district-homeschool-access: Home Education in Jackson and SAU 9

- kind: local
- question_type: local_practice
- description: How homeschooled and EFA students can take part in a district's classes, activities and sports, and the district's homeschool notice and evaluation process

1. SAU 9's website has no page, form or guidance on home education. The superintendent's office is at 176A Main Street, Conway (603-447-8368).
   - citation: SAU 9 website: home page, site map, Forms, Student Services, Students & Families, FAQs
   - source: https://www.sau9.org/site_map
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Searched all six pages for "home educ", "homeschool", "home school", "193-A" and "participating agency"; no matches. Home page text: "176A Main Street Conway, NH 03818 ... 603-447-8368". Raw: raw/community/homeschool/sau9-home.txt, sau9-site-map.txt, sau9-forms.txt, sau9-student-services.txt, sau9-students-families.txt, sau9-faqs.txt
2. The Jackson School Board's policy IGBJ, "Home Education Instruction & Access to Curricular and Cocurricular Programs," was last revised November 21, 2022. It describes the earlier law: parents chose a "participating agency" (the Commissioner, the superintendent or a nonpublic school head), sent it written notice, kept a portfolio and arranged an annual evaluation, and the district gave a state or local test free or a portfolio review for a fee when the superintendent was the participating agency.
   - citation: Jackson School District Policy IGBJ (adopted June 10, 1994; revised November 21, 2022)
   - source: https://drive.google.com/file/d/1uYef2bm7sLNfOhNjXWcUknc6JbxoLRu0/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Policy text: "The parent/guardian decides which participating agency to select ... a. the Commissioner ... b. the resident district Superintendent ... c. the head of a nonpublic school"; "Under RSA 193-A:6, II, parents/guardians are required to provide for an annual educational evaluation"; "the District will not charge a fee for providing or administering the test ... at or above the fortieth percentile"; "the parent/guardian may request the District to perform a portfolio review, for which the District may charge a fee." From the Jackson policy folder (Section I). Raw: raw/community/homeschool/jackson-policy-igbj-home-education.txt
3. Since July 1, 2026, New Hampshire law no longer requires a notice, a portfolio or an annual evaluation for most home-educated children, and it bars school boards and superintendents from enforcing policies on home-educated students except for access to public school courses and programs. Jackson's policy IGBJ was written before that change.
   - citation: RSA 193-A:3 and 193-A:4, II (as amended by 2026, 297:3, effective July 1, 2026); library topic home-education-rules; Jackson Policy IGBJ (revised November 21, 2022)
   - source: https://gc.nh.gov/rsa/html/XV/193-A/193-A-4.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Jackson
   - note: RSA 193-A:3: "A declaration of home education shall not be required, except to obtain access to public school programs pursuant to RSA 193:1-c or upon withdrawal from a public school." RSA 193-A:4, II: "No superintendent, school board, school principal, other school district official, local official, or state official shall propose, adopt, or enforce any policy or procedure governing home educated students except for policies related to the courses and programs described in RSA 193:1-c." Repeal of the former evaluation section (RSA 193-A:6) is in library topic home-education-rules, fact 2. Raw: raw/community/homeschool/rsa-193-A-3.txt, rsa-193-A-4.txt, jackson-policy-igbj-home-education.txt
4. Jackson's policy JJJ (adopted November 21, 2022) gives resident nonpublic, charter and home-educated students access to the Jackson School District's courses and co-curricular programs if they meet the same performance, age and prerequisite requirements as enrolled students and follow school rules.
   - citation: Jackson School District Policy JJJ, Access to Public School Programs by Nonpublic, Charter School, and Home-Educated Pupils
   - source: https://drive.google.com/file/d/1PDsnQUeWIwZ6_u_A9d8nEg3I_P-_W-Aa/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Policy text: "Nonpublic, public chartered school, and home-educated pupils who are residents of Jackson shall have access to curricular courses and co-curricular programs offered by the Jackson School District. These students must meet the same performance, age, and prerequisite requirements as Jackson School District students." Part-time enrollment at JGS (P9.1) is covered in another file. Raw: raw/community/homeschool/jackson-policy-jjj-access-public-school-programs.txt
5. At its October 19, 2026 meeting, the Jackson School Board discussed a "Framework & Policy for Home-Educated/Part-Time Student Support." A family letter said Jackson and SAU 9 lack "clear and consistent support for homeschooled students," and a board member said a new policy was in progress and needed more discussion.
   - citation: Jackson School Board Minutes (DRAFT), October 19, 2026, item g
   - source: https://drive.google.com/file/d/1B9DSqRrrnOyvR3lbMnycQaxBs8GBMxoH/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Minutes text: "g. Discussion: Framework & Policy for Home-Educated/Part-Time Student Support ... They feel that Jackson and SAU #9 do not have a clear and consistent support for homeschooled students in the District. ... Ms. Auth spoke about a new policy that is in progress. It was discussed at the policy meeting tonight, but it needs more discussion at another meeting. The family liaison position support is available at Jackson, as well." Draft minutes, not yet approved. Raw: raw/community/school-district/jackson-board-minutes-2026-10-19-draft.txt
6. The Jackson School District's annual report counted 4 reported home-educated students in grades K-6 and none in grades 7-12 as of February 5, 2026. Earlier reports counted 3 to 8 a year between December 2016 and January 2024.
   - citation: Annual Report of the School District of Jackson (for the March 5, 2026 meeting), Enrollment page 31; earlier annual reports 2017-2025
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Scanned PDF; transcribed from image raw/community/school-district/jackson-sd-annual-report-2026-enrollment-page.png: "Number of Reported Home Educated Students Grade K-6 = 4 Grade 7-12 = 0". Totals by year are in table jackson_district_students_by_level. Since July 1, 2026 most home-educating families no longer file a notice, so later counts may not be comparable.

## town-child-care: Licensed Child Care and Preschool in and Near Jackson

- kind: local
- question_type: help
- description: Child care for a town beyond the site's child care data: where the nearest licensed programs are, drive times, Head Start, costs programs post, waitlists and local child care efforts

1. NH DHHS's Child Care Search lists no licensed child care program in Jackson or in Bartlett (including Glen and Intervale); the nearest are in the town of Conway (North Conway, Conway and Center Conway), and the Town of Jackson's 2025 hazard mitigation plan also says the town has no licensed child care facilities.
   - citation: NH Child Care Search (NH DHHS), provider list download; Jackson Hazard Mitigation Plan Update 2025, Table 2.1
   - source: https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: The search page's "download provider results" function (fetchProviderList) returned 734 providers statewide, 25 in Carroll County. Filtered on city = Jackson, Glen, Intervale, Bartlett, North Conway, Conway, Center Conway, Kearsarge or Redstone. The site's database copy of the search (735 programs, downloaded the same day) also has none in Jackson or Bartlett; the Conway programs' places, ages, openings, hours and rates are in the site's data (child_care), so they are not repeated here. Public school preschools such as JGS's (details in another file) do not appear in this list. HMP Table 2.1: "Licensed Child Care Facilities No" and page 25: "The town has no private schools, childcare facilities, or colleges/universities." Raw: raw/community/childcare/nhccis-provider-list-2026-11-13.json; childcare-providers-jackson-area-2026-11-13.csv; raw/community/emergency/jackson-hmp-2025.txt
2. In NH DHHS's Child Care Search, every licensed program in the town of Conway (North Conway, Conway and Center Conway), the nearest to Jackson, shows a quality rating of "Licensed."
   - citation: NH Child Care Search (NH DHHS), provider list download
   - source: https://new-hampshire.my.site.com/nhccis/NH_ChildCareSearch
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: All 10 rows in the CSV have "Licensed" in QRIS_Rating__c; the site's database copy agrees. The search also has a separate Granite Steps for Quality field, filled in for some programs; it is not used here. Rewritten November 14, 2026: the earlier statement listed names, capacities and scholarship enrollment, which the site's data now holds, and read the scholarship-enrollment field (Provider_Enrollment_Status_Formula__c, "Active" or "Inactive") as whether a program was active; that field is about NH Child Care Scholarship enrollment, not the program or its license. Raw: raw/community/childcare/childcare-providers-jackson-area-2026-11-13.csv
3. Tri-County Community Action Program runs Head Start for children ages 3 to 5 in Coös, Carroll and Grafton counties, including a center in Conway (603-447-5161). It is free to eligible families, with income at or below 100% of the federal poverty guidelines and limited slots for over-income families, and classes run 4 hours a day, 5 days a week, with breakfast and lunch in Conway.
   - citation: Tri-County CAP, Head Start
   - source: https://tccap.org/head-start/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "Ages Served 3-5 years ... Areas Served Coös, Carroll, and Grafton Counties ... Income Guidelines 100% of Federal poverty guidelines, limited slots available for over-income families ... No cost to eligible families"; "A center-based classroom program, 4 hours per day (6 hours in Berlin and Littleton), 5 days a week"; "Colebrook, Conway, Groveton, Plymouth, Tamworth, and Whitefield provide breakfast and lunch"; "Conway (603) 447-5161". The federal locations file lists "Conway Area Head Start, 73 Main St" with 15 funded slots (additional-data/raw/programs/head-start-sites-nh.csv); DHHS lists "Conway Head Start" with capacity 20, ages 3-6. Statewide eligibility: library topic head-start-eligibility. Raw: raw/community/childcare/tccap-head-start.txt
4. Northeast Woodland Chartered Public School in Conway runs a private, tuition-based pre-K for children who turn 3 by August 31, separate from its charter. For 2026/2027 it costs $11,330 a year for five days, $7,725 for three days and $5,819.50 for two days, and in May 2026 the program was full with a waitlist.
   - citation: Northeast Woodland, Enrollment & Lottery (Pre-K)
   - source: https://www.northeastwoodland.org/enrollment-lottery
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Text: "Our Pre-K program is a private program and is not a part of our charter."; "A pupil may enter pre-k if their chronological age will be three years on or before August 31"; "Five Day Early Childhood Program: Monday - Friday (8am-2:20pm) $11,330/year ... Three Day ... $7,725/year ... Two Day ... $5,819.50/year"; "As of May 2026, our Pre-K program for the 2026/27 school year is full." Raw: raw/community/private-schools/nwcs-enrollment-lottery.txt
5. Jackson Grammar School has a public preschool, and Josiah Bartlett Elementary School serves children from early childhood education; their details are in the library and another Jackson file.
   - citation: additional-data/district-practices.md (Jackson preschool; Bartlett early childhood)
   - source: https://jgs.sau9.org/kindergartenregistration
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Pointer only. district-practices.md coverage table lists Jackson "K day, Preschool"; Bartlett fact 7 (early childhood). The NH Child Care Scholarship rules are in library topic child-care-scholarship-eligibility.

## town-housing: Jackson's Housing, Plans and Rules, Valley Housing Needs, and What the Data Can Show

- kind: local
- question_type: local_practice
- description: A town's housing beyond the site's Census estimates: home sales and assessments, short-term rentals, workforce housing, and housing plans and studies

1. The 2020 Census counted 1,052 housing units in Jackson, 500 of them (48%, derived) held for seasonal, recreational or occasional use; the 2010 Census counted 1,009 units, 570 of them seasonal (56%, derived).
   - citation: 2020 Census DHC tables H3 and H5; 2010 Census SF1 tables H3 and H5
   - source: https://data.census.gov/table/DECENNIALDHC2020.H5?g=060XX00US3300338260
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: 2020: H3_001N 1052, H3_002N 500 occupied, H5_006N 500 seasonal. 2010: H003001 1009, H003002 399 occupied, H005006 570 seasonal. Shares derived (500/1052; 570/1009). Rewritten November 14, 2026: the ACS 2020-2024 housing units, households and seasonal share (1,006 units, 54.4% seasonal) are in the site's Census data, so they were removed here. Table jackson_housing_units_occupancy. Raw: raw/community/census/DECENNIALDHC2020.H3-jackson.json, DECENNIALDHC2020.H5-jackson.json, DECENNIALSF12010.H3-jackson.json, DECENNIALSF12010.H5-jackson.json
2. Among Jackson's year-round households, the 2020 Census counted 397 owners and 103 renters (21% renters, derived).
   - citation: 2020 Census DHC table H4 (Tenure); 2010 Census SF1 H4
   - source: https://data.census.gov/table/DECENNIALDHC2020.H4?g=060XX00US3300338260
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: 2020: H4_002N (owned with mortgage) 197 + H4_003N (owned free and clear) 200 = 397 owners; H4_004N 103 renters (103/500 = 20.6%). 2010: 152 + 157 = 309 owners, 90 renters of 399. Rewritten November 14, 2026: the ACS 2020-2024 owner and renter estimates are in the site's Census data (owner-occupied homes), so they were removed here. Raw: raw/community/census/DECENNIALDHC2020.H4-jackson.json, DECENNIALSF12010.H4-jackson.json
3. New Hampshire REALTORS® data show a year-to-date median single-family sale price through October 2026 of $610,000 in Bartlett (72 sales) and $535,000 in Conway (115 sales). The REALTORS® publish no town report for Jackson; their Carroll County median for 2025 was $500,500 (940 sales).
   - citation: New Hampshire REALTORS®, Local Market Update – October 2026 (Bartlett; Conway); Carroll County single-family residential home sales, 1998 to present
   - source: https://nhar-public.stats.showingtime.com/docs/lmu/x/Bartlett?src=page
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Bartlett: "Median Sales Price* ... Thru 10-2025 $620,000 Thru 10-2026 $610,000"; "Closed Sales ... 55 72". Conway (https://nhar-public.stats.showingtime.com/docs/lmu/x/Conway?src=page): "$470,000 $535,000"; closed sales "113 115". Jackson: "Report is not available", and Jackson is not in the site's list of areas. Carroll County (https://nhar-public.stats.showingtime.com/docs/ann/x/CarrollCounty?src=page): "2025 940 +11.8 $500,500". Sale prices of the homes that sold differ from the owners' own estimates of value in the site's Census data. Table jackson_area_median_sale_price. Raw: raw/community/housing/nhar-lmu-bartlett.txt, nhar-lmu-conway.txt, nhar-annual-carroll-county.txt
4. The Town of Jackson's 2025 hazard mitigation plan says the average cost per new single-family home in Jackson rose from $291,700 in 2012 to $817,300 in 2022, and that Jackson's net valuation rose 57.5% from $486,711,781 in 2023 to $846,196,787 in 2024, the year of a town revaluation.
   - citation: Jackson, NH Hazard Mitigation Plan Update 2025 (Final, May 19, 2025), Chapter 2
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Plan text: "from 2012 to 2022, the average cost per new single-family housing unit went from $291,700 to $817,300 in Jackson. The net valuation in Jackson rose 57.5% from a 2023 valuation of $486,711,781 to $846,196,787 in 2024." Valuation footnote: "Town of Jackson, email, 1/31/25". The town's site has a "Revaluation Process 2024 FAQ" page (not opened). The plan's valuations equal NH DOE's assessed valuation with utilities for Jackson in 2023 and 2024; Jackson's tax rates and valuations are in the site's data (property_tax, Jackson district). Raw: raw/community/emergency/jackson-hmp-2025.txt
5. Jackson's 2016 master plan background chapter says the high cost of housing makes it hard for younger families to live in Jackson and "affects the school population." It asks whether the grammar school will "have enough children to remain open, or will the town need to tuition grammar school students to another town?"
   - citation: Town of Jackson Master Plan 2016 Update, Background, Housing (pages 15-18)
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/01/2016_master_plan_updatebackgroundfinal.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Text: "This trend has implications on Jackson's ability to attract younger families, and affects the school population"; "fewer young families with children will move to town and put their children into local schools"; "rental rates may range between $800 and $2500 per month, especially given costs for short-term rentals"; "Will the local grammar school have enough children to remain open, or will the town need to tuition grammar school students to another town?" These are the plan's statements, not measured effects. Raw: raw/community/housing/jackson-master-plan-2016-background.txt
6. At town meeting on March 12, 2024, Jackson voted to establish a housing commission under RSA 674:44-h to promote "a balanced and diverse supply of housing." It meets the third Tuesday of each month at 6 pm at the Town Office.
   - citation: Town of Jackson, Housing Commission page; Jackson Housing Commission slides (June 13, 2025)
   - source: https://www.jackson-nh.gov/boards-committees/housing-commission/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "At Town Meeting on March 12, 2024, the Town of Jackson voted to establish a Housing Commission pursuant to RSA 674:44-h for the proper recognition, promotion, enhancement, encouragement, and development of a balanced and diverse supply of housing". Meeting time from slides: "Attend meetings the 3rd Tuesday of every month at 6:00pm in the Jackson Town Office". Contact jacksonhousingcommission@gmail.com. Raw: raw/community/town-housing-commission.txt; raw/community/housing/jhc-hhh-2025-slides.txt
7. The housing commission's brochure says rental vacancies in Jackson are 0.5% and that home prices rose 50% since 2019. It does not give sources; the ACS for 2020-2024 estimates Jackson's rental vacancy rate at 17.4% with a margin of ±27.9 points.
   - citation: Jackson Housing Commission brochure (trifold); ACS 5-year 2020-2024 DP04
   - source: https://docs.jacksonhousingcommission.org/documents/publications/jhc_trifold.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Brochure text: "Availability and Vacancy Rates: Rental vacancies are at 0.5%, with fewer homes available than in 2010. Housing Affordability: Home prices rose 50% since 2019". ACS DP04_0005E rental vacancy rate 17.4 ±27.9 (raw/community/census/ACSDP5Y2024.DP04-jackson.json). Checked November 14, 2026 against the site's Census data (B25004 and B25003, 2020-2024): 8 units vacant for rent (±13), none rented but not yet occupied (±12) and 38 renter households (±34) give the same 17.4%. Neither figure is reliable for a town this small. Raw: raw/community/housing/jhc-trifold.txt
8. In October 2026 the housing commission reported that the donated Baker's Field parcel was planned for five homes of two to three bedrooms through the New Hampshire Rural Community Land Trust, and that a new town master plan survey had at least 200 responses.
   - citation: Jackson Housing Commission, Regular Meeting Minutes, October 20, 2026
   - source: https://docs.jacksonhousingcommission.org/documents/minutes/2026.10.20%20Jackson%20Housing%20Commission%20Minutes.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Minutes text: "The Baker's Field development remains planned for five homes"; "The development plan continues to propose five homes, conceptually containing two to three bedrooms each"; "The Town Master Plan survey received at least 200 responses before the mailed survey was distributed"; the commission discussed requesting "$25,000 in the 2027 budget for a Housing & Conservation Opportunities Plan". Raw: raw/community/housing/jhc-minutes-2026-10-20.txt
9. Since March 2020, Jackson's zoning ordinance (Section 4.4, last amended March 10, 2026) requires every short-term rental (stays of 1 to 30 nights in a dwelling) to have a conditional use permit from the Select Board, with a $150 application fee. One stated purpose is "to help preserve the quality and quantity of the housing stock for year-round residential use."
   - citation: Town of Jackson Zoning Ordinance Section 4.4, Short Term Rentals (rev. 3/10/2026); Short Term Rental Information & Forms page
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/10/SECTION-4.4-rev-3.10.2026.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Ordinance text: "SECTION 4.4: SHORT TERM RENTALS (added 3/10/2020, amended 5/15/2021, 3/10/2022, 3/7/2024, 3/11/2025, 3/10/2026)"; "4.4.2.2 To help preserve the quality and quantity of the housing stock for year-round residential use."; "(with a $150 application fee)". Raw: raw/community/housing/jackson-str-ordinance-section-4-4-rev-2026.txt; raw/community/town-str-forms.txt
10. No public count of short-term rentals in Jackson was found. The town's 2025 hazard mitigation plan quotes the Planning Board's 2023 report that it reviewed "one or two Conditional Use Permits each month (total 20) for Short Term Rentals" in 2023.
   - citation: Jackson Hazard Mitigation Plan Update 2025, Chapter 2, quoting the 2023 Jackson Annual Report, Planning Board, page 76
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Plan text: "the Jackson Planning Board stated, '…as a land use board, we had a handful of subdivision/boundary line (4) and lot merger (1) approvals throughout the year and one or two Conditional Use Permits each month (total 20) for Short Term Rentals.'" This counts permit reviews in one year, not all short-term rentals. The town annual reports could not be downloaded (see Not retrieved). Raw: raw/community/emergency/jackson-hmp-2025.txt
11. The Mount Washington Valley Housing Coalition cites North Country Council's Regional Housing Needs Assessment (January 2023) as finding that Carroll County needed 336 rental units and 804 ownership units by 2025.
   - citation: Mount Washington Valley Housing Coalition, 2024 Membership page
   - source: https://mwvhc.networkforgood.com/projects/228449-2024-membership
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Page text: "By 2025 Carroll County needs 336 Rental Units and 804 Ownership Units (North Country Council, Regional Housing Needs Assessment, January, 2023)". The North Country Council report itself was not found on nccouncil.org; the statewide 2023 RHNA does not mention Jackson. Raw: raw/community/housing/mwvhc-membership-2024.txt
12. Jackson's 2016 master plan quotes the Mount Washington Valley Housing Coalition (2012) that the valley "has a housing affordability problem" and that retail and hospitality employers had "struggled to recruit and retain an adequate workforce."
   - citation: Town of Jackson Master Plan 2016 Update, Background, Housing, quoting MWV Housing Coalition, Housing Matters (August 2012)
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/01/2016_master_plan_updatebackgroundfinal.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - note: Text: "In Housing Matters, August 2012, the Mount Washington Valley Housing Coalition pointed out that 'MWV has a housing affordability problem. The trend toward second home ownership and upscale single-family development is at odds with the housing demand of working families ... Retail and hospitality employers report that ... they have, at times, struggled to recruit and retain an adequate workforce.'" Raw: raw/community/housing/jackson-master-plan-2016-background.txt
13. No public data shows whether housing costs cause changes in Jackson's school enrollment or in teacher turnover. The records show the trends side by side: a seasonal share of housing near half of all units (2010-2024), fewer students in the district's counts in February 2026 than in December 2016, and the town's and housing commission's stated concern, but not cause and effect.
   - citation: Research note
   - source: https://data.census.gov/table/ACSDT5Y2024.B25004?g=060XX00US3300338260
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Statement of what the data cannot show. The seasonal share for 2010 and 2020 is in fact 1; the 2020-2024 estimate is in the site's Census data. NH DOE's teacher turnover or attrition data could not be opened (see Not retrieved). Teacher salaries and the salary schedule are in the site's data.

## district-classrooms-and-staff: Teacher Tenure at JGS and SAU 9 Staffing Shortages

- kind: local
- question_type: local_practice
- description: How a district's schools group classes and grades, their staff and roles, staffing changes, substitutes and aides, and how the schools describe themselves

1. Two of the four grade-level classroom teachers listed at Jackson Grammar School for 2025-26 were also listed in 2016-17, and the principal changed between the 2022-23 and 2023-24 staff lists (derived from the district's annual report staff pages).
   - citation: Annual Reports of the School District of Jackson, 2017 and 2023-2026, "Jackson Grammar School Staff" pages
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Jackson
   - note: Derived by comparing the names on the staff pages (OCR, checked against the page images): 2016-17 (2017 report, page 4) lists four grade-level teachers (K/1, 2/3, 4/5, 6) and a teaching principal; 2025-26 (2026 report, page 30) lists four (K/1, 3/4, 4/5, 5/6), two of whom appear in 2016-17. The 2023 report's principal differs from the 2024 report's. Names are not repeated here. The reports do not give reasons for any change. Raw: raw/community/school-district/jackson-sd-annual-report-2017.ocr.txt, jackson-sd-annual-report-2026.ocr.txt (and 2023-2025)
2. SAU 9's superintendent wrote in the 2026 annual report that, like districts across the state, SAU 9 faces staffing shortages, "particularly in special education, nursing, and paraprofessional roles," and that recruitment and retention are strategic priorities. This is SAU-wide, not specific to Jackson.
   - citation: Annual Report of the School District of Jackson (2026), Superintendent's Report
   - source: https://drive.google.com/file/d/1D0hValK7yd9WP7SPuc3smY0tq72Y08Bk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Scanned; OCR text: "Like districts across the state, SAU 9 continues to navigate staffing shortages, particularly in special education, nursing, and paraprofessional roles. Recruitment and retention remain strategic priorities". The report does not mention housing. Raw: raw/community/school-district/jackson-sd-annual-report-2026.ocr.txt

## town-emergency-services: Jackson's Police, Dispatch, Mutual Aid and Emergency Alerts

- kind: local
- question_type: local_practice
- description: A town's police, fire and emergency management, dispatch, mutual aid, emergency alerts and cell coverage

1. The Jackson Police Department is a full-time department with a full-time chief and one full-time sergeant, according to the town's 2025 hazard mitigation plan. The police department also handles animal control.
   - citation: Jackson, NH Hazard Mitigation Plan Update 2025, Chapter 2 and Table 2.1
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Plan text: "The Jackson Police Department is a full-time department ... The department staffs a full-time Chief and Sergeant." Table 2.1: "Police Department Yes, full-time Chief, one full-time Sergeant"; "Animal Control Officer No, the Police Department handles animals". Plan dated May 19, 2025, prepared for the Town and NH Homeland Security & Emergency Management. The police chief listed on the town website is Michael Mosher (raw/community/town-police.txt). Raw: raw/community/emergency/jackson-hmp-2025.txt
2. Carroll County Dispatch (the Carroll County Sheriff's Office in Ossipee) dispatches Jackson's police, fire and ambulance calls.
   - citation: Jackson Hazard Mitigation Plan Update 2025, Table 2.1 and critical facilities list
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Table 2.1: "Police Dispatch Carroll County Dispatch ... Fire Dispatch Carroll County Dispatch ... EMS Dispatch Carroll County Dispatch". Critical facilities: "Carroll County Sheriff's Office (Ossipee) Dispatch". Raw: raw/community/emergency/jackson-hmp-2025.txt
3. The Jackson Police Department has mutual aid agreements with surrounding towns, NH State Police (Troop E), the Carroll County Sheriff's Office and NH Fish & Game. The fire department (a full-time chief and 25-28 paid on-call firefighters) belongs to Mount Washington Valley Mutual Aid, and Bartlett-Jackson Ambulance provides emergency medical services. The plan rates these mutual aid systems as working well.
   - citation: Jackson Hazard Mitigation Plan Update 2025, Chapter 2 and Table 6.1
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Table 6.1: "Mutual Aid Agreements ... Excellent No Improvements Needed: The Jackson Fire Department has a mutual aid agreement with Mount Washington Valley Mutual Aid. The Jackson Police Department has mutual aid agreements with surrounding towns, the NH State Police (Troop E), the Carroll County Sheriff's Office, and NH Fish & Game. ... All mutual aid systems in Jackson work well." Chapter 2: "The department staffs a full-time Chief and 25-28 paid-on-call firefighters". The plan does not name Bartlett or Conway police specifically. Raw: raw/community/emergency/jackson-hmp-2025.txt
4. Jackson's town warning system is Genasys (formerly CodeRED, the NH Emergency Notification System), plus a fire siren where three blasts mean an emergency. The 2025 plan says Genasys holds only residents' landline numbers unless residents add cell numbers and email addresses, and keeps outreach to residents as an action item. The Jackson School District uses SchoolMessenger for school notices.
   - citation: Jackson Hazard Mitigation Plan Update 2025, Table 2.1, Table 6.1 and Table 7.1
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Table 2.1: "Town Emergency Warning Systems Genasys (formerly CodeRED) & fire siren (3 blasts means emergency) School Emergency Warning System SchoolMessenger". Table 6.1: "Genasys is a reverse calling system that uses residents' landline phone numbers. Genasys does not include cell and unlisted numbers or email addresses. The Jackson School District uses School Messenger"; "deferred to continue to provide public outreach to encourage residents to contact Genasys to add cell numbers, emails, and unlisted numbers ... Action Item #9". The plan also lists Facebook pages of the police, fire department and JGS, and the private Jackson E-News list. Raw: raw/community/emergency/jackson-hmp-2025.txt
5. The 2025 plan lists cellular telephone access in Jackson as "limited in places," notes radio "dead spots" in parts of town, and names mobile and portable radio upgrades as the town's greatest emergency communications need.
   - citation: Jackson Hazard Mitigation Plan Update 2025, Table 2.1 and Table 6.1 (Radio Communications)
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Table 2.1: "Cellular Telephone Access Limited in places"; "High-Speed Internet Yes". Table 6.1: "All three emergency departments in Jackson (Police/Fire/Highway Departments) have radio interoperability. ... There are areas of the Town that have 'dead spots'. Mobile radios and portable radio upgrades are Jackson's greatest need." Critical facilities include "Radio & cell towers (Black Mountain Knoll)" and a solar "Communications Tower (Thorn Mountain)". FCC coverage maps were not retrieved. Raw: raw/community/emergency/jackson-hmp-2025.txt
6. Jackson's Emergency Operations Plan was last updated in 2023 (dated April 11, 2023) and is due for its next update in 2028. The fire station is the primary emergency operations center, and the Whitney Community Center, on the Jackson Grammar School campus, is the primary emergency shelter.
   - citation: Jackson Hazard Mitigation Plan Update 2025, Table 2.1 and Table 6.1; Town of Jackson, Emergency Management page
   - source: https://www.jackson-nh.gov/departments/emergency-management/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: HMP Table 2.1: "Emergency Operation Plan (EOP) Yes, April 11, 2023"; "Primary EOC Fire Station (generator)"; "Primary Shelter Whitney Community Center (generator)". Table 6.1: "The Jackson Emergency Operations Plan (EOP) was last updated in 2023 ... deferred to update the EOP again in 2028." The town page says the plan "will be available for review at the Town offices pending it's final revisions"; the EOP itself is not online. The plan lists Jackson Grammar School among "Facilities & People to Protect." Raw: raw/community/town-emergency-management.txt; raw/community/emergency/jackson-hmp-2025.txt
7. The 2025 plan says a mass-casualty incident is most likely on NH Route 16, which it calls "twisty, steep, busy," and that students traveling to Bartlett for middle school and Conway for high school increase that potential; it reports no mass-casualty incident since the previous plan.
   - citation: Jackson Hazard Mitigation Plan Update 2025, Chapter 4 (Mass Casualty Incident)
   - source: https://www.jackson-nh.gov/wp-content/uploads/2026/03/Jack_HMP_Final_May19_2025.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Plan text: "An MCI could happen anywhere in Jackson but is more likely on NH Route 16. Route 16 is a twisty, steep, busy road ... In addition, students traveling to Bartlett for middle school and Conway for high school increase the potential. Fortunately, there have been no reported MCIs since the last hazard mitigation plan." Raw: raw/community/emergency/jackson-hmp-2025.txt
8. Through "Project Good Morning," offered with the Carroll County Sheriff's Office, Jackson residents who live alone call Carroll County Dispatch each morning, and if a person does not call, dispatch asks the Jackson Police Department to do a well-check.
   - citation: Town of Jackson, Jackson Neighbor Care Program
   - source: https://www.jackson-nh.gov/departments/emergency-management/jackson-neighbor-care-program/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Jackson
   - note: Page text: "Each morning an individual must call into Carroll County Dispatch to inform them that they are safe and doing well. In the event a person does not call in, Dispatch will contact the Jackson Police Department and ask them to do a well-check". Shows the dispatch and police link. Raw: raw/community/town-neighbor-care.txt

## jackson_private_school_drive_distance_tuition: Private Day Schools Near Jackson: Grades, Day Tuition and Road Distance

- unit: dollars (tuition); miles and minutes (distance)
- period: Tuition as posted on November 13, 2026 (year shown per row); distances computed November 13, 2026; year: 2027
- source: Each school's own tuition page (see facts); OSRM driving routes from Jackson village — https://router.project-osrm.org/ ; grades from NCES PSS 2023-24 where the school's page did not state them
- as_of: 2026-11-13
- raw: raw/community/distances/osrm-routes-from-jackson.json; raw/community/distances/nominatim-schools.json; raw/community/private-schools/
- note: Distances and minutes are **derived**: fastest OSRM car route from Jackson village (OSM node 44.1442760, -71.1811070) to each school's geocoded address, in normal conditions; winter weather is not modeled. Cornerstone Christian Academy and Holy Trinity School geocoded only to the street, so their distances are approximate. "Not found" means no tuition was found on a school website that could be read (third-party directory figures were not used). The list is sorted by distance; it is not a ranking and not a complete list of schools.

| School | Town | State | Grades | Day tuition (school's site) | Road miles from Jackson (derived) | Drive minutes, normal conditions (derived) | Note |
|---|---|---|---|---|---|---|---|
| New Life Christian Academy | Fryeburg | ME | 1-11 (PSS) | not found | 19.1 | 38 | Religious school |
| Fryeburg Academy | Fryeburg | ME | 9-12 (PSS) | $22,500 (2027-28, commuter day) | 19.8 | 40 | Jackson district agreement from 2027-28 |
| Salve Regina Academy | Gorham | NH | PK-8 (PSS) | not found | 20.7 | 32 | Catholic school |
| Shepherds River Mennonite School | Brownfield | ME | 1-10 (PSS) | not found | 23.6 | 56 | Religious school |
| Unity Christian School | Berlin | NH | K-12 (PSS) | not found | 27.2 | 47 | Religious school |
| Mount Royal Academy North | Lancaster | NH | PK-7 (PSS) | not found | 40.1 | 73 | |
| Cornerstone Christian Academy | Ossipee | NH | PK-8 (PSS) | not found | 41.0 | 71 | Distance approximate (street-level geocode) |
| Gould Academy | Bethel | ME | 8-12 (PSS) | $57,057 (2026-27) | 42.0 | 66 | |
| Brewster Academy | Wolfeboro | NH | not stated on pages read | $44,700 (2026-27) | 50.2 | 86 | |
| Waterville Valley Academy | Waterville Valley | NH | 6-8 day program; 9-12 winter term | $31,000 (grades 6-8); $39,538 (9-10) and $41,000 (11-12) winter-term day; year not stated | 54.8 | 108 | Ski academy, November–March |
| Laconia Christian Academy | Laconia | NH | PK-12 (PSS) | not found | 55.0 | 103 | Religious school |
| Hebron Academy | Hebron | ME | 6-12 and postgraduate | $20,900 (2026-27) | 59.3 | 98 | |
| New Hampton School | New Hampton | NH | 9-12 and postgraduate | $46,350 (2026-27) | 59.5 | 108 | |
| Holy Trinity School | Laconia | NH | PK-8 (PSS) | $7,900 (2026-27, full time PreK–grade 6) | 59.9 | 111 | Catholic school; full time only through grade 6 in 2026-27 (Laconia research, `town/Laconia/student-support-and-choices.md`, town-school-options-nearby 1); distance approximate |
| Holderness School | Holderness | NH | 9 to postgraduate | $55,900 (2026-27) | 62.5 | 98 | |
| Burke Mountain Academy | East Burke | VT | 8-12 (PSS) | no day rate posted ($72,000 full-term boarding, 2026-27) | 82.4 | 122 | Ski academy |
| Carrabassett Valley Academy | Carrabassett Valley | ME | 7-12 | $52,500 (7-8) and $57,500 (9-12) full-year day; $36,000 and $41,000 winter-term day (2026/2027) | 127.4 | 203 | Ski academy |

## jackson_household_income_distribution: Household Income Distribution, Jackson and New Hampshire

- unit: percent
- period: ACS 5-year 2020-2024; year: 2024
- source: Census Bureau, ACS 5-year table S1901 — https://data.census.gov/table/ACSST5Y2024.S1901?g=060XX00US3300338260
- as_of: 2026-11-13
- raw: raw/community/census/ACSST5Y2024.S1901-jackson.json; raw/community/census/ACSST5Y2024.S1901-nh.json
- note: Percent of households. The margins of error for Jackson are large; a difference of a few points is not meaningful. Checked November 14, 2026 against the site's Census data (B19001 counts, 2020-2024): every bracket matches for Jackson and New Hampshire. Median household income is in the site's Census data.

| Place | town_id | Income bracket | Value | Margin of error |
|---|---|---|---|---|
| Jackson | 271 | Less than $10,000 | 7.9 | ±11.7 |
| Jackson | 271 | $10,000 to $14,999 | 1.8 | ±2.7 |
| Jackson | 271 | $15,000 to $24,999 | 7.7 | ±6.0 |
| Jackson | 271 | $25,000 to $34,999 | 4.5 | ±5.0 |
| Jackson | 271 | $35,000 to $49,999 | 5.6 | ±7.1 |
| Jackson | 271 | $50,000 to $74,999 | 14.4 | ±8.3 |
| Jackson | 271 | $75,000 to $99,999 | 2.9 | ±3.2 |
| Jackson | 271 | $100,000 to $149,999 | 14.7 | ±9.3 |
| Jackson | 271 | $150,000 to $199,999 | 8.6 | ±5.9 |
| Jackson | 271 | $200,000 or more | 31.8 | ±12.4 |
| NH | | Less than $10,000 | 3.2 | ±0.1 |
| NH | | $10,000 to $14,999 | 2.3 | ±0.1 |
| NH | | $15,000 to $24,999 | 4.9 | ±0.2 |
| NH | | $25,000 to $34,999 | 5.3 | ±0.3 |
| NH | | $35,000 to $49,999 | 8.1 | ±0.3 |
| NH | | $50,000 to $74,999 | 14.3 | ±0.4 |
| NH | | $75,000 to $99,999 | 12.4 | ±0.3 |
| NH | | $100,000 to $149,999 | 20.0 | ±0.5 |
| NH | | $150,000 to $199,999 | 12.7 | ±0.3 |
| NH | | $200,000 or more | 16.8 | ±0.4 |

## jackson_children_by_age_census: Jackson Residents Under 5 and Ages 5 to 17

- unit: count
- period: 2010 Census (April 1, 2010); 2020 Census (April 1, 2020); ACS 5-year 2020-2024; year: 2010, 2020, 2024
- source: Census Bureau, 2010 SF1 P12; 2020 DHC P12; ACS 5-year B01001 — https://data.census.gov/table/DECENNIALDHC2020.P12?g=060XX00US3300338260
- as_of: 2026-11-13
- raw: raw/community/census/DECENNIALSF12010.P12-jackson.json; raw/community/census/DECENNIALDHC2020.P12-jackson.json; raw/community/census/ACSDT5Y2024.B01001-jackson.json
- note: Age-group totals are **derived** by adding male and female counts. Census counts are full counts; the ACS row is a sample estimate with very wide margins (under 5: 11 ±18; ages 5-17: 26 ±31, the margin derived from the B01001 margins) and should not be read as a drop from 2020. Checked November 14, 2026 against the site's Census data (B01001, 2020-2024): the counts match. The ACS total population and children under 18 are in the site's Census data, so the ACS row leaves the total blank.

| Place | town_id | Source | Under 5 | Ages 5-17 | Total population | Note |
|---|---|---|---|---|---|---|
| Jackson | 271 | 2010 Census | 19 | 87 | 816 | |
| Jackson | 271 | 2020 Census | 18 | 93 | 1,028 | |
| Jackson | 271 | ACS 2020-2024 | 11 | 26 | | Sample estimate; margins (±18 and ±31) larger than the values |

## jackson_district_students_by_level: Jackson School District Students by Level, From District Annual Reports

- unit: count
- period: Count dates December 31, 2016 to February 5, 2026 (as printed); year: 2017–2026
- source: Annual Reports of the School District of Jackson, 2017–2026, Enrollment page — https://drive.google.com/drive/folders/1LP1rwzxaO8TST7NY9MI0lD7ihtpLyekv
- as_of: 2026-11-13
- raw: raw/community/school-district/jackson-sd-annual-report-2017.pdf … 2026.pdf; enrollment page images jackson-sd-annual-report-YYYY-enrollment-page.png
- note: Scanned; transcribed from images. "Year" is the annual report year (the school year ends that June). Grades 7-8 attend Josiah Bartlett Elementary and 9-12 Kennett High under tuition contracts. "Home educated" and "private/charter" are the reports' "Jackson Students Not Attending Local Schools" totals; from 2025 the reports list only home-educated students. The 2024 report also counts 1 special education placement. The reports do not say whether K-6 includes non-resident pupils. The 2025 report printed 27 in grades K-6; the March 6, 2025 district meeting corrected it to 37 ("pg 30 - students total should be 37"), which the report's grade counts add to. The K-6 count is Jackson Grammar School's enrollment and can include non-resident pupils: the March 2, 2023 meeting minutes say two of the 47 then enrolled were teachers' children and two were tuition students.

| Place | Year | Count date | Grades K-6 | Grades 7-8 | Grades 9-12 | Home educated | Private/charter |
|---|---|---|---|---|---|---|---|
| Jackson | 2017 | 2016-12-31 | 38 | 16 | 28 | 3 | 3 |
| Jackson | 2018 | 2017-12-31 | 41 | 14 | 27 | 3 | 3 |
| Jackson | 2019 | 2018-12-31 | 49 | 13 | 26 | 3 | 3 |
| Jackson | 2020 | 2020-01-13 | 43 | 12 | 31 | 5 | 1 |
| Jackson | 2021 | 2021-01-11 | 49 | 15 | 24 | 8 | 0 |
| Jackson | 2022 | 2022-01-18 | 44 | 15 | 24 | 5 | 3 |
| Jackson | 2023 | 2023-01-06 | 47 | 11 | 25 | 3 | 0 |
| Jackson | 2024 | 2024-01-17 | 36 | 9 | 23 | 5 | 5 |
| Jackson | 2025 | 2025-02-14 | 37 | 7 | 24 | 3 | not reported |
| Jackson | 2026 | 2026-02-05 | 30 | 10 | 20 | 4 | not reported |

## jackson_anticipated_kindergarten: Jackson's Anticipated Kindergartners, by Annual Report

- unit: count
- period: Annual reports 2017–2024 (prepared each winter for the March district meeting); year: 2017–2028
- source: Annual Reports of the School District of Jackson, 2017–2024, "Anticipated Enrollment"; kindergarten counts from the next year's Enrollment page — https://drive.google.com/drive/folders/1LP1rwzxaO8TST7NY9MI0lD7ihtpLyekv
- as_of: 2026-11-13
- raw: raw/community/school-district/jackson-sd-annual-report-2017-enrollment-page.png … 2026-enrollment-page.png
- note: Transcribed from images. Each report column gives the number of children it expected to enter kindergarten in that fall. "Counted" is the kindergarten count in the following winter's report. Blank means the report did not cover that year. The reports do not say how the anticipated counts were made.

| Entering kindergarten in fall | 2017 report | 2018 report | 2019 report | 2020 report | 2021 report | 2022 report | 2023 report | 2024 report | Kindergartners counted the next winter |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 5 | | | | | | | | 3 |
| 2018 | 5 | 10 | | | | | | | 10 |
| 2019 | 5 | 2 | 1 | | | | | | 5 |
| 2020 | 5 | 6 | 7 | 6 | | | | | 6 |
| 2021 | 4 | 4 | 5 | 5 | 5 | | | | 2 |
| 2022 | | 2 | 0 | 1 | 1 | 2 | | | 3 |
| 2023 | | | 3 | 4 | 4 | 2 | 2 | | 1 |
| 2024 | | | | 4 | 4 | 4 | 4 | 6 | 6 |
| 2025 | | | | | 3 | 4 | 5 | 5 | 4 |
| 2026 | | | | | | 2 | 3 | 4 | |
| 2027 | | | | | | | 3 | 5 | |
| 2028 | | | | | | | | 2 | |

## jackson_population_projection_opd: Jackson Total Population, Census and OPD Projections

- unit: count
- period: 2020 Census; OPD projections 2025–2050 (published September 2022); OPD estimate 2025 (published July 17, 2026); year: 2020–2050
- source: NH Office of Planning and Development, State, County, and Municipal Population Projections: 2020-2050, Appendix B Table 2 — https://www.nheconomy.com/getmedia/0205c62d-9c30-4b00-9c9e-d81d8f17b8b3/NH-Population-Projections-2020-2050-Final-Report-092022.pdf
- as_of: 2026-11-13
- raw: raw/community/opd-population-projections-2020-2050.pdf (.txt); raw/community/opd-2025-population-estimates.pdf (.txt)
- note: Total population only; OPD does not project ages for towns. The 2025 estimate is a separate OPD product (https://www.nheconomy.com/getmedia/62b7f54e-dced-456c-9bbf-cac23ea1f7d5/2025-Population-Estimates.pdf). The Town's web page quotes a 2024 Census estimate of 1,070.

| Place | town_id | Year | Value | Note |
|---|---|---|---|---|
| Jackson | 271 | 2010 | 816 | Census |
| Jackson | 271 | 2020 | 1,028 | Census |
| Jackson | 271 | 2025 | 1,049 | OPD estimate (July 2026) |
| Jackson | 271 | 2025 | 1,073 | OPD projection (2022) |
| Jackson | 271 | 2030 | 1,108 | OPD projection |
| Jackson | 271 | 2035 | 1,127 | OPD projection |
| Jackson | 271 | 2040 | 1,127 | OPD projection |
| Jackson | 271 | 2045 | 1,113 | OPD projection |
| Jackson | 271 | 2050 | 1,093 | OPD projection |

## jackson_carroll_county_age_projection: Carroll County Children by Age, OPD Projections

- unit: count
- period: 2020 base and projections 2025–2050; year: 2020–2050
- source: NH OPD, Population Projections 2020-2050, Table 8: Projected Populations for Carroll County by Age Groups and Sex — https://www.nheconomy.com/getmedia/0205c62d-9c30-4b00-9c9e-d81d8f17b8b3/NH-Population-Projections-2020-2050-Final-Report-092022.pdf
- as_of: 2026-11-13
- raw: raw/community/opd-population-projections-2020-2050.txt
- note: County-wide, used because OPD does not project ages for Jackson. Ages 5-19 total is **derived**. 2020 column is the report's base year.

| Place | Year | Ages 0-4 | Ages 5-9 | Ages 10-14 | Ages 15-19 | Ages 5-19 (derived) |
|---|---|---|---|---|---|---|
| Carroll County | 2020 | 1,765 | 2,124 | 2,264 | 2,201 | 6,589 |
| Carroll County | 2025 | 2,058 | 1,919 | 2,220 | 2,048 | 6,187 |
| Carroll County | 2030 | 2,038 | 2,245 | 2,013 | 2,014 | 6,272 |
| Carroll County | 2035 | 1,945 | 2,235 | 2,369 | 1,839 | 6,443 |
| Carroll County | 2040 | 1,853 | 2,147 | 2,374 | 2,181 | 6,702 |
| Carroll County | 2045 | 1,824 | 2,053 | 2,289 | 2,195 | 6,537 |
| Carroll County | 2050 | 1,859 | 2,023 | 2,190 | 2,117 | 6,330 |

## jackson_housing_units_occupancy: Jackson Housing Units, Seasonal Homes and Tenure

- unit: count
- period: 2010 Census; 2020 Census; year: 2010, 2020
- source: Census Bureau, SF1 2010 H3/H4/H5; DHC 2020 H3/H4/H5 — https://data.census.gov/table/DECENNIALDHC2020.H5?g=060XX00US3300338260
- as_of: 2026-11-13
- raw: raw/community/census/ (files named DECENNIALSF12010.H*, DECENNIALDHC2020.H*)
- note: Seasonal share and renter share are **derived**. The Town's 2025 hazard mitigation plan quotes the 2022 ACS: 1,065 units, 500 occupied, 565 vacant. The ACS 2020-2024 rows for Jackson, Bartlett, Conway and New Hampshire were removed on November 14, 2026: housing units, households, the seasonal share and owner-occupied homes are in the site's Census data.

| Place | town_id | Source | Housing units | Occupied year-round | Seasonal, recreational or occasional | Seasonal share (derived) | Owner-occupied | Renter-occupied | Renter share (derived) |
|---|---|---|---|---|---|---|---|---|---|
| Jackson | 271 | 2010 Census | 1,009 | 399 | 570 | 56.5% | 309 | 90 | 22.6% |
| Jackson | 271 | 2020 Census | 1,052 | 500 | 500 | 47.5% | 397 | 103 | 20.6% |

## jackson_area_median_sale_price: Median Single-Family Sale Price, Bartlett, Conway and Carroll County

- unit: dollars
- period: Year to date through October 2025 and 2026 (towns); calendar 2025 (county and state); year: 2026, 2025
- source: New Hampshire REALTORS® (ShowingTime), Local Market Update – October 2026, and annual single-family sales report — https://nhar-public.stats.showingtime.com/docs/lmu/x/Bartlett?src=page
- as_of: 2026-11-13
- raw: raw/community/housing/nhar-lmu-bartlett.pdf (.txt); nhar-lmu-conway.pdf (.txt); nhar-annual-carroll-county.pdf (.txt)
- note: Single-family homes sold through the MLS. No report is published for Jackson. "Report current as of November 5, 2026." Small numbers of sales make town medians move a lot from year to year.

| Place | town_id | Period | Median sale price | Number of sales |
|---|---|---|---|---|
| Bartlett | 35 | Jan–Oct 2025 | 620,000 | 55 |
| Bartlett | 35 | Jan–Oct 2026 | 610,000 | 72 |
| Conway | 113 | Jan–Oct 2025 | 470,000 | 113 |
| Conway | 113 | Jan–Oct 2026 | 535,000 | 115 |
| Carroll County | | 2025 | 500,500 | 940 |
| NH | | 2025 | 535,000 | 12,542 |
| Jackson | 271 | — | not published | |

## Not retrieved

- NH DHHS / NH Health WISDOM (https://wisdom.dhhs.nh.gov/wisdom/) and NH Vital Records NHVRINweb (https://nhvrinweb.sos.nh.gov/Default.aspx, nhivs_quickfacts.aspx): curl and the web fetch tool both got "Access Denied" (HTTP 403). No births-by-year data for Jackson residents were retrieved. Saved refusals: raw/community/births/.
- Town of Jackson annual reports 2015–2025 on the UNH archive (https://scholars.unh.edu/cgi/viewcontent.cgi?article=1131&context=jackson_nh_reports and earlier articles): the item pages load, but every PDF download returned a Cloudflare challenge (HTTP 403), with and without cookies; the Wayback Machine refused automated requests (HTTP 429); the old town copy (https://www.jackson-nh.org/sites/g/files/vyhlif3296/f/uploads/2023_town_report.pdf) returns 404. These reports hold the Resident Birth Report, police and planning board reports and the Bartlett/Jackson recreation report.
- NH DOE (education.nh.gov), including the nonpublic schools lists on https://www.education.nh.gov/who-we-are/division-of-educator-and-analytic-resources/bureau-of-education-statistics/schools-and-sau-information and my.doe.nh.gov: HTTP 403 to curl and the web fetch tool. Not retrieved: the official nonpublic school list (used NCES PSS instead), teacher turnover/attrition data for JGS or SAU 9, and the 2020 DOE release on Northeast Woodland.
- nh.gov and readynh.gov (NH Alerts / ReadyNH): HTTP 403. The town's warning system was taken from the hazard mitigation plan instead.
- FCC National Broadband Map (https://broadbandmap.fcc.gov/): HTTP 403. No mobile coverage data for Jackson retrieved; the hazard mitigation plan's "limited in places" is the only coverage statement.
- Census API (https://api.census.gov/data/2024/acs/acs5): redirects to "missing_key". Data were taken from the data.census.gov table API instead; labels from api.census.gov group metadata.
- NH REALTORS® Local Market Update for Jackson (https://nhar-public.stats.showingtime.com/docs/lmu/x/Jackson?src=page): "Report is not available"; Jackson is not in the site's area list. NH Housing's downloadable sales data (https://www.nhhousing.org/resources/housing-demographic-data/) is by county and region only (raw/community/housing/nhh-historical-monthly-solds-2009-present.xlsx). The NHHFA town purchase price database was not found on the new site.
- NESDEC or other enrollment projections for SAU 9 or Jackson: none found on https://www.sau9.org/ (including SAU#9 Reports), in the Jackson School District annual reports 2017-2026 (OCR text searched for "projection", "NESDEC" and "census") or by web search.
- North Country Council Regional Housing Needs Assessment (January 2023): not found on https://www.nccouncil.org/ or by search; cited only through the MWV Housing Coalition. The MWV Housing Coalition website (https://www.mwvhousing.org/) did not respond.
- Private school tuition not found on the school's own site: Salve Regina Academy (srca.org redirected to an unrelated site; not followed), New Life Christian Academy, Unity Christian School, Cornerstone Christian Academy (cornerstonechristian.com is a different school in Illinois), Mount Royal Academy North, Laconia Christian Academy, Holy Trinity School (found later by the Laconia research: $7,900 for 2026-27, https://www.holytrinitycatholicnh.org/tuition-financial-aid), Shepherds River Mennonite School. Waterville Valley Academy's main site (https://www.wvbbts.org/) did not connect; its register.wvbbts.org pages were used. Brewster Academy's grades were not on the pages read.
- The Community School (South Tamworth) and The White Mountain School (Bethlehem) were left out of the table: directories and the EFA marketplace label both as closed ("The White Mountain School (closed)"; "The Community School (Closed 2024)"), but no primary closure notice was read. Added November 13, 2026: "(Closed 2024)" is Private School Review's label, and the current EFA feed has no Community School entry; a 2020 Conway Daily Sun column reports the closing, and the nonprofit is now The Bearcamp Center for Sustainable Community (town/Tamworth/community-and-families.md, town-school-options-nearby 1–2). Added November 13, 2026: The White Mountain School's own announcement (Wayback copy of June 1, 2024) says its 138th year "will be the final year" (town/Madison/raw/kennett/).
- Northeast Woodland Chartered Public School's address (53 Technology Lane, Conway) could not be geocoded in OpenStreetMap, so no road distance was computed.
- NH Charitable Foundation funds for Carroll County children (Bill and Esther Levy Scholarship Fund; Mount Washington Valley Community Assistance Fund): seen only in search results, not opened.
- Whether Jackson children may join Bartlett or Conway recreation programs, and at what fee: the Bartlett Recreation (MyRec) pages read do not say; Conway Parks & Recreation fees not found. Jackson has no recreation department page on the town site. Added November 13, 2026: Conway's 2026 camp handbook limits its day camp to Conway and Albany residents and its teen center to Conway, Albany and Eaton (town/Albany/community-and-families.md).
- JGS PTO: no PTO page on the current JGS site; the PTO flyer link (https://files.smartsites.parentsquare.com/10273/2026_halloween_hollow_flyer.pdf) returned HTTP 403. Jackson churches' children's funds other than the Bushee Thorn Mountain Trust form were not found.
- Jackson Housing Commission website (https://jacksonhousingcommission.org/) is a script-only page; documents were found through links in its code and downloaded from docs.jacksonhousingcommission.org.
- For another file: Bartlett Recreation's Adventure Kids after-school program ($8 a day, K-5) and PLC-day care (raw/school-day/bartlett-myrec-adventure-kids.txt, gathered by the school-day agent); Northeast Woodland's aftercare; Kennett/JBES bus times; the 2026 open enrollment policy details for JGS; Robert Frost Charter School in Conway (seen in search results only).
