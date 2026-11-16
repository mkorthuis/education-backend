# Enrollment, School Zones and Choices in Manchester

Part of the Manchester research (town/Manchester). Gathered November 15, 2026.

## Summary

This file covers how Manchester assigns students to schools by address, the feeder pattern from elementary to high school, past redistricting, moving within the city, divided custody with Hooksett, paying tuition to attend Goffstown, private school tuition in the city and how far an Education Freedom Account (EFA) goes toward it, the share of North End children in private or home school, and homeschooled students returning to or using district schools.

- **Counts:** 4 topics, 42 facts, 2 number tables.
  - `district-attendance-zones-and-transfers` (17 facts): **proposed new shared topic**, see below.
  - `town-school-options-nearby` (21 facts).
  - `school-residency-rules` (1 fact) and `efa-eligibility-and-cap` (3 facts) add to existing rule topics.
  - Tables: `manchester_private_school_tuition` and `manchester_private_or_home_school_share`.
- **New data concepts:** the city's own attendance-zone map (GIS), the elementary-to-high-school feeder pattern worked out from it, which zones the city's named neighborhoods fall in, Census estimates of private or home schooling for the North End and each high school zone, and private school tuition set against the 2026-27 EFA amounts.
- **Main gaps:** the Manchester School District's website (mansd.org) answered every request with a bot check, so its policies (104.1 change of school, 106 non-resident students, 115 grade placement), home education page, facilities planning page and Board of School Committee minutes weren't read. Manchester Ink Link, the main local news source on transfers, open enrollment and redistricting, returned HTTP 403. Trinity High School doesn't post its tuition. Goffstown's non-resident tuition rate wasn't found. The web search budget ran out near the end.
- **Questions answered wholly by earlier files:** 1 (P28.2, by the library's `home-education-rules`). P25.1 and P27.2 are mostly answered by earlier files, with local facts added here.

**Proposed new shared topic:** `district-attendance-zones-and-transfers` | Attendance Zones, Feeder Patterns and School Transfers | local | local_practice | How a district assigns students to schools by home address, its feeder pattern from elementary to middle to high school, redistricting history and plans, proof of residency, and requests to attend a different school in the district. No existing shared topic covers school zones; `district-classrooms-and-staff` covers grade groupings and `district-transportation` covers buses.

### Premises checked

| Question | Premise | What the sources show |
|---|---|---|
| P3.2 | North End families go to Central High | Correct. On the city's map, the whole North End neighborhood area is in Central's high school zone, by way of Webster or Smyth Road and Hillside (zones facts 3, 5). |
| P11.1 | "Right on the Goffstown line" with a 1st grader at Northwest Elementary, near Mast Road | Partly. The city's "Northwest" neighborhood area is all in Northwest Elementary's zone, but its "Mast Road" area is almost all in Parker-Varney's zone (zones fact 7). An address lookup settles which school serves a home. |
| P11.1 | Paying tuition to attend Goffstown may not be allowed | Not correct. Goffstown's policy lets non-resident students attend with School Board approval and tuition, with no bus (options facts 1–2). Goffstown also adopted open enrollment for 5 out-of-district kindergarten seats in March 2026 (options facts 3–4). |
| P21.3 | Mount St. Mary is a choice for later school years like Trinity | Partly. Mount Saint Mary Academy serves preschool through grade 6; Trinity is a high school (options facts 9–10). |
| P22.2 | A 5th grader at Wilson | Out of date. There is no Wilson zone among the city's 12 elementary zones, and Manchester's grade 5 is in its middle schools (zones facts 2, 8, 11; the site's 2024-25 enrollment by grade). |
| P25.1 | One town "gets to decide" where a child with 50/50 custody attends | Not quite. New Hampshire law sets residence by the court order or a written parental agreement; if parents living apart can't agree, the two superintendents decide jointly, and the education commissioner decides if they can't (Hart's Location `school-residency-rules` 2–3). |
| P27.2 | Families paying private tuition can't use EFA funds or tax credits | Not correct since June 2025. Any New Hampshire resident eligible for public school can apply for an EFA, with no income limit, subject to an enrollment cap that was reached for 2026-27 and rises to 15,625 for 2027-28 (library `efa-eligibility-and-cap` 1–5; efa facts 1–2 here). Scholarship tax credits exist for lower-income families (library `choice-federal-tax-credit-scholarships`). |
| P28.2 | Homeschoolers send a yearly evaluation to the superintendent or the state | Out of date. Since July 1, 2026, New Hampshire no longer requires an annual evaluation; RSA 193-A:6 was repealed (library `home-education-rules` 1, 2, 10). |
| P28.3 | A 10-year-old returning for 6th grade | In Manchester, grade 6 is in the middle schools (grades 5–8), so the student would enter the middle school for the home's zone (zones facts 3, 11; site enrollment data). |

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P3.2 North End families: Central High, or Derryfield and Trinity? | `district-attendance-zones-and-transfers` 3, 5; `town-school-options-nearby` 5–6, 14–15, 19–21; table `manchester_private_or_home_school_share` | partial | Census estimates give the share of North End K–12 students in private or home school (about 15%, with a wide margin), not which schools they attend. No source counts North End students at Derryfield or Trinity. Central's enrollment is in the site's data. |
| P11.1 Tuitioning into Goffstown from the Goffstown line | `town-school-options-nearby` 1–4; library `change-of-school-assignment` 9 and `open-enrollment-status` 1–5; `district-attendance-zones-and-transfers` 7 | full | Goffstown's non-resident tuition rate wasn't found. Whether Manchester limits its residents' use of open enrollment wasn't found in a readable source (see Not retrieved). |
| P14.2 Would an EFA make a dent in private tuition? | `town-school-options-nearby` 6–18; table `manchester_private_school_tuition`; library `choice-efa-state-cost` 3, 5 and `efa-uses-and-requirements` 1–3; `efa-eligibility-and-cap` 1–3 here | full | The site's EFA data counts 1,297 Manchester students with base aid for 2026-27 (data only). Trinity doesn't post its tuition. |
| P15.1 Plans to redraw the Green Acres school lines? | `district-attendance-zones-and-transfers` 2–4, 6, 10–13 | partial | Current zones and the history of changes (2017, 2018, the 2020 study, closures) are covered. No current plan to redraw elementary lines was found, but the district's facilities planning page and board minutes couldn't be read. |
| P21.3 Cost of Trinity or Mount St. Mary | `town-school-options-nearby` 5–17; table `manchester_private_school_tuition` | partial | Mount Saint Mary Academy and seven other schools' tuition are covered; Trinity's tuition isn't posted (its discounts and aid are). |
| P22.2 Moving two streets over: switching schools mid-year? | `district-attendance-zones-and-transfers` 1, 9, 14–15; library `change-of-school-assignment` 1–3; `district-attendance-zones-and-transfers` 18 | partial | Manchester's policy 508 (July 1 request, August 1 answer, capacity limits, preference for overflow students returning home) is now covered; it doesn't address a mid-year move within the city. State law lets a parent ask to stay at the original school for the rest of the year (library change-of-school-assignment). |
| P25.1 50/50 custody between Manchester and Hooksett | Hart's Location `school-residency-rules` 2–3; Chatham `school-residency-rules` 1–5; `school-residency-rules` 1 here; `district-attendance-zones-and-transfers` 16–17 | full | Mostly answered by earlier town files' rule facts; Hooksett's own residency policy is added. |
| P27.2 Why not EFA funds or tax credits for private-school families? | library `efa-eligibility-and-cap` 1–6, `efa-uses-and-requirements`, `choice-federal-tax-credit-scholarships` 1–10; `efa-eligibility-and-cap` 1–3 here; `town-school-options-nearby` 6, 11–13, 18 | full | The "why" is a policy judgment; the facts show families paying tuition can apply for an EFA now, subject to the cap. |
| P28.1 Homeschooled children in Parkside sports or band | library `home-education-rules` 1, 5, 8 and `choice-hb-1817-efa-public-school-courses` 2–3; `district-attendance-zones-and-transfers` 7; `district-attendance-zones-and-transfers` 20 | full | Policy 562 (August 2026): written request to the principal, same deadlines and eligibility as enrolled students, generally no transportation; EFA students limited to half a schedule. |
| P28.2 Where to send the yearly homeschool evaluation | library `home-education-rules` 1, 2, 10 | full | Answered wholly by the library: no annual evaluation is required since July 1, 2026. |
| P28.3 Returning for 6th grade: tested or placed by age? | library `home-education-rules` 7; `district-attendance-zones-and-transfers` 1, 3, 11; `district-attendance-zones-and-transfers` 19 | partial | Policy 717 (formerly 115) covers high school placement (transcript, test scores, portfolio or an equal evaluation); placement in grades K–8 isn't described. |
| P38.1 Renting and moving: keeping a child in the same elementary school | library `change-of-school-assignment` 1–3, 6, 8; `district-attendance-zones-and-transfers` 1, 14–15; `district-attendance-zones-and-transfers` 18 | partial | Policy 508's capacity limits (20 per teacher in K–4, 25 in grades 5–12) and request deadlines now answer the oversubscribed-school question; a mid-year move isn't addressed. |
| P38.3 How early to look at school zones when buying | `district-attendance-zones-and-transfers` 1–3, 9–13; library district-practices (Manchester registration opened March 21, 2026) | partial | The facts cover how to look up a home's schools and how often zones have changed; "how early" is a judgment the data can't make. School results by school are in the site's data. |

## district-attendance-zones-and-transfers: Attendance Zones, Feeder Patterns and School Transfers

- kind: local
- question_type: local_practice
- description: How a district assigns students to schools by home address, its feeder pattern from elementary to middle to high school, redistricting history and plans, proof of residency, and requests to attend a different school in the district

1. The Manchester School District assigns students to schools by where they live, and its registration page sends families to the City of Manchester's School District Lookup, where entering an address shows the elementary, middle and high schools that serve it.
   - citation: Manchester School District, New Student Registration page; City of Manchester, School District Lookup
   - source: https://www.mansd.org/o/msd/page/register-a-student
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Manchester
   - note: Page text: "To look up your neighborhood schools enter an address in the search field in the link above and click "Go". The elementary, middle, and high schools that serve your neighborhood will be displayed.  Students in Manchester are assigned to schools geographically." The "Find Your School" button links to https://www.manchesternh.gov/Residents/School-District/School-District-Lookup. Raw: additional-data/raw/districts/batch-1/manchester-register-a-student.txt (saved 2026-11-08; mansd.org showed a bot check on 2026-11-15, so it wasn't rechecked). Lookup page: raw/choices/city-school-district-lookup.html.

2. The City of Manchester's map service "Manchester NH Public School Districts Elementary, Middle, High Schools" shows 12 elementary attendance zones (Bakersville, Beech Street, Gossler Park, Green Acres, Highland-Goffe's Falls, Jewett, McDonough, Northwest, Parker-Varney, Smyth Road, Webster and Weston), 4 middle school zones (Hillside, McLaughlin, Parkside and Southside) and 3 high school zones (Central, Memorial and West).
   - citation: City of Manchester GIS, SchoolDistricts map service, layers 1–3 (High, Middle and Elementary School Districts)
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/SchoolDistricts/MapServer
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Service description: "Manchester NH Public School Districts Elementary, Middle, High Schools"; copyright "City of Manchester, NH". The elementary layer has 12 polygons (object ids 1, 2, 4 and 6–14; ids 3 and 5 are absent). The service gives no edit date. Raw: raw/choices/gis/schooldistricts-service.json, schooldistricts-layer1-4326.json, -layer2-, -layer3-.

3. On the city's zone map, Manchester's feeder pattern runs: Webster, Smyth Road and McDonough to Hillside Middle and Central High; Beech Street to McLaughlin (about two-thirds of its zone's area) or Hillside (about one-third), then Central; Green Acres and Weston to McLaughlin and Memorial; Bakersville, Highland-Goffe's Falls and Jewett to Southside and Memorial; and Gossler Park, Northwest and Parker-Varney to the Middle School at Parkside and West High (**derived**).
   - citation: City of Manchester GIS, SchoolDistricts map service, layers 1–3; overlay worked out for this file
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/SchoolDistricts/MapServer
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: **Derived** by laying a grid of points about 100–130 m apart over each elementary zone and checking which middle and high zone each point falls in; shares are by land area, not by homes or students. Every elementary zone except Beech Street lies 100% in one middle and one high zone. McLaughlin's middle zone is 95% in Memorial's high zone and 5% in Central's. Method and output: raw/choices/gis/zones-overlay-method.py.txt, zones-overlay-output.txt. Raw: raw/choices/gis/schooldistricts-layer1-4326.json, -layer2-, -layer3-.

4. Manchester's middle school zones match its high school zones on the city's map: all of Hillside's zone is in Central's, all of Parkside's is in West's, all of Southside's is in Memorial's, and McLaughlin's is 95% in Memorial's and 5% in Central's, by area (**derived**).
   - citation: City of Manchester GIS, SchoolDistricts map service, layers 1–2
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/SchoolDistricts/MapServer
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: **Derived** by the grid overlay described in fact 3. Parkside's middle zone and West's high zone have the same area in the service (226,901,914 square feet). Raw: raw/choices/gis/schooldistricts-layer1-4326.json, -layer2-.

5. The city's "North End" neighborhood area lies about 92% in Webster's elementary zone and 8% in Smyth Road's, and all of it is in Hillside's middle school zone and Central's high school zone (**derived**).
   - citation: City of Manchester GIS, HealthNeighborhoodsMap ("Manchester Neighborhoods") and SchoolDistricts map services
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/HealthNeighborhoodsMap/MapServer
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: **Derived** by grid overlay (raw/choices/gis/zones-overlay-output.txt) of the city's 25 named neighborhood areas on the school zones; shares by land area. The neighborhood layer was last edited 2017-09-01 (last_edited_date 1504298613000). The city's lookup for 2519 Elm St (the Webster School address in the site's data) returned Webster, Hillside and Central (raw/choices/city-lookup-2519-elm-st-webster-school.txt). Raw: raw/choices/gis/neighborhoods-4326.json.

6. The city's "Green Acres" neighborhood area lies about 81% in Green Acres Elementary's zone, 17% in Weston's and 2% in Jewett's; about 98% of it is in McLaughlin's middle school zone, and all of it is in Memorial's high school zone (**derived**).
   - citation: City of Manchester GIS, HealthNeighborhoodsMap and SchoolDistricts map services
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/SchoolDistricts/MapServer
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: **Derived** by grid overlay (raw/choices/gis/zones-overlay-output.txt); shares by land area. The Green Acres elementary zone (about 200.6 million square feet) is the largest of the 12 elementary zones in the service's Shape.STArea field. Raw: raw/choices/gis/neighborhoods-4326.json, schooldistricts-layer3-4326.json.

7. On the city's map, the "Northwest" neighborhood area is all in Northwest Elementary's zone, the "Mast Road" area is about 99% in Parker-Varney's zone, and the "Rimmon Heights" area is about 93% in Northwest's and 7% in Gossler Park's; all three are in the Middle School at Parkside's and West High's zones (**derived**).
   - citation: City of Manchester GIS, HealthNeighborhoodsMap and SchoolDistricts map services
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/SchoolDistricts/MapServer
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: **Derived** by grid overlay (raw/choices/gis/zones-overlay-output.txt); shares by land area. The neighborhood areas are the city's planning neighborhoods, not school zones; a family's school comes from the address lookup. Raw: raw/choices/gis/neighborhoods-4326.json.

8. The city's zone map has no Hallsville or Wilson elementary zone, and its "Hallsville" neighborhood area now lies about 49% in Jewett's zone, 20% in Beech Street's, 19% in Weston's and 12% in McDonough's (**derived**).
   - citation: City of Manchester GIS, SchoolDistricts map service, layer 3, and HealthNeighborhoodsMap
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/SchoolDistricts/MapServer/3
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: **Derived** by grid overlay (raw/choices/gis/zones-overlay-output.txt). The 12 elementary zone names in layer 3 are listed in fact 2. Hallsville School and Henry Wilson Elementary School aren't on NH DOE's current school list (brief). Raw: raw/choices/gis/schooldistricts-layer3-4326.json, neighborhoods-4326.json.

9. On November 15, 2026, the city's School District Lookup returned McDonough Elementary, Hillside Middle School and Central High School for 1 City Hall Plaza, and Webster Elementary, Hillside and Central for 2519 Elm Street.
   - citation: City of Manchester, School District Lookup, results for two public addresses
   - source: https://www.manchesternh.gov/Residents/School-District/School-District-Lookup
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Page text: 'Your neighborhood schools for "1 CITY HALL PLZ" are: MCDONOUGH ELEMENTARY / HILLSIDE MIDDLE SCHOOL / CENTRAL HIGH SCHOOL'. Only public building addresses were entered. Both results agree with the zone map overlay (fact 3). Raw: raw/choices/city-lookup-1-city-hall-plaza.txt, city-lookup-2519-elm-st-webster-school.txt.

10. In April 2017, Manchester's school board approved a change to the feeder pattern, the path students follow from elementary to middle to high school, as the first step in a redistricting effort city officials had pursued for nearly a decade; the district's 2018 plan shows that "Phase 1" feeder pattern taking effect in September 2017.
   - citation: Superintendent's Redistricting Proposal, April 9, 2018, slide 3; NHPR, "After Almost a Decade, Manchester Takes First Step Toward School Redistricting," April 20, 2017
   - source: https://drive.google.com/file/d/187wQJDSb3qTaARR3N-9zo4U_nNggDAww/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Slide 3: "Phase 1: School Feeder Pattern Effective September 2017", with "Beech Street students are split between McLaughlin and Southside middle schools, then reunite at Central High School." NHPR: "Last night, the School Board took its first step. It approved a change to the feeder pattern ... The bigger challenge, says Girard, will come when the school board votes to redraw district lines." The plan is linked as "2018 Redistricting Plan" on the district's older Google Site. Raw: raw/choices/msd-2018-redistricting-plan.pdf/.txt; raw/choices/nhpr-2017-04-20-redistricting.txt.

11. In April 2018, Manchester's Board of School Committee approved a superintendent's redistricting plan that sent all Beech Street graduates to McLaughlin Middle and Central High from September 2018, and moved grade 5 into the middle schools (grades 5–8) with elementary schools becoming kindergarten to grade 4, starting on the West Side in September 2019 and planned for the rest of the city in September 2020.
   - citation: Manchester School District announcement, "Redistricting plan to be implemented in Manchester," April 2018; Superintendent's Redistricting Proposal, April 9, 2018, slides 9, 14–15
   - source: https://msdannouncements.blogspot.com/2018/04/redistricting-plan-to-be-implemented-in.html
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Announcement text: "the redistricting plan that was approved by the Board of School Committee this month ... incoming sixth graders from Beech Street Elementary School will attend McLaughlin Middle School ... They will all attend Central High ... Adoption of the grades 5-8 middle school model will start on the West Side of Manchester in September 2019. The Middle School at Parkside will include fifth graders from Gossler Park, Northwest, and Parker-Varney ... bringing in the fifth grade classes from the other 11 elementary schools beginning in September 2020." The site's 2024-25 enrollment shows grade 5 in the middle schools. Today's map splits the Beech Street zone between McLaughlin and Hillside (fact 3). Raw: raw/choices/msd-announcements-2018-04-redistricting.txt; raw/choices/msd-2018-redistricting-plan.txt.

12. The 2018 redistricting plan gave its reasons as all 14 elementary schools being near 100% capacity while Central High was at 66%, Memorial at 75% and West at 50%, and it aimed to reduce class sizes to 20 in kindergarten, 20–22 in grades 1–2, 22–25 in grades 3–5 and 25–27 in grades 6–8 as finances and space allowed.
   - citation: Superintendent's Redistricting Proposal, April 9, 2018, slides 4, 6, 7 and 13
   - source: https://drive.google.com/file/d/187wQJDSb3qTaARR3N-9zo4U_nNggDAww/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Text: "All 14 of our elementary schools are near 100% capacity." "Central HS is at 66% capacity / Memorial HS is at 75% capacity / West HS is at 50% capacity now…" and "Reduce class sizes beginning in 2018 to the extent finances and space allow: 20 students in kindergarten, 20-22 students in grades 1-2, 22-25 students in grades 3-5, 25-27 students in grades 6-8." Today the city has 12 elementary zones (fact 2). Raw: raw/choices/msd-2018-redistricting-plan.txt.

13. In 2020, the Manchester School District hired MGT Consulting Group for an independent audit of its school buildings, including their capacity and use, and the consultant presented a draft report to the Board of School Committee's Finance and Facilities Committee, followed by a special board meeting and community feedback sessions.
   - citation: Manchester School District (older Google Site), "District Facilities, Capacity and Utilization Study"
   - source: https://sites.google.com/a/mansd.org/manchestersd/for-families/district-facilities-capacity-and-utilization-study
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Page text: "In 2020, Manchester School District hired a consultant to complete an independent audit of school district facilities. In addition to assessing the condition of buildings, the intent was to get an independent assessment of the capacity and utilization of those buildings. The consultant, MGT Consulting Group, completed inspections of all school facilities and gathered feedback from families, staff and students through an online survey." The page goes on to describe the consultant's report to the Finance and Facilities Committee "at a special meeting on Dec. 16" and a board special meeting on "Wednesday, Jan. 6"; it gives no years for those dates. The page is on the district's older site, which still shows "Registration for the 2022-2023 school year is now open!"; the district's current facilities planning page (mansd.org) couldn't be read. Raw: raw/choices/gsite-district-facilities-capacity-and-utilization-study.txt.

14. Manchester's transportation guidelines make students in full-day kindergarten through grade 12 eligible for a bus if they live 1.4 miles or more from their "districted school," or in some cases must cross busy or dangerous streets, and tell families who have moved and need to change transportation to contact their child's school.
   - citation: Manchester School District Transportation site, Transportation Guidelines
   - source: https://sites.google.com/a/mansd.org/msd-transportation/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Page text: "Students in grades K (full day) -12 are eligible for bus transportation if they live 1.4 miles or more from their districted school, or in some cases, if they are required to cross busy or dangerous streets to get to school." and "Contact your child's school for the following ... You have moved and need to change transportation." Raw: raw/choices/gsite-transportation-home.txt.

15. Manchester's transportation guidelines say that students who become homeless during the school year need not transfer to another school and can receive transportation from the district, through the school's social worker or the district's homeless liaison.
   - citation: Manchester School District Transportation site, Homeless Students
   - source: https://sites.google.com/a/mansd.org/msd-transportation/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Page text: "Under the McKinney-Vinto act, students who become homeless during the school year need not transfer to another school and can receive transportation from the school district. Please contact your school's Social Worker or the District's Homeless Liaison ... at 665-6868." The page spells the federal McKinney-Vento Act "McKinney-Vinto." Who counts as homeless (including families sharing housing after losing theirs) is in RSA 193:12, IV. Raw: raw/choices/gsite-transportation-home.txt; raw/choices/rsa-193-12.txt.

16. The Hooksett School District defines residency for enrollment as RSA 193:12 does (Policy JFA), and its Policy JFAA asks parents enrolling a student for two proofs of residency and requires families who move within the district to notify the school and give new proof of residency within 30 days.
   - citation: Hooksett School Board Policies JFA (Residency) and JFAA (Enrollment and Admission of Resident Students, revised January 20, 2026)
   - source: https://hooksettschoolboard.sau15.net/policy-manual/enrollment-and-adminission-of-resident-studentscertification-of-residency-form/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Hooksett
   - note: JFA text: "Residency for the purpose of enrollment in the Hooksett School District is as defined by RSA 193:12." JFAA: "Parents or legal guardians will be required to provide two proofs of residency. Documents which demonstrate proof include a mortgage statement, rental/lease agreement, or deed ... Parents or legal guardians of students who move within the district will be required to notify school officials and to provide new proof of residency within 30 days." The site's data lists Hooksett's schools as Fred C. Underhill, Hooksett Memorial and David R. Cawley Middle. Raw: raw/choices/hooksett-policy-residency.txt, hooksett-policy-jfaa.txt.

17. When a child's parents live in two districts, such as Manchester and Hooksett, and can't agree on the child's school residence, New Hampshire law has the two superintendents decide jointly, and the child stays in the school of origin while the question is decided; in Manchester the superintendent is SAU 37's and in Hooksett SAU 15's (**derived** application).
   - citation: RSA 193:12, VI(a)–(b); SAU numbers from the site's data
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Statute text: "If more than one school district is involved in a residency dispute, or the parents who live apart cannot agree on the residence of a minor child, the respective superintendents shall jointly make such decision. In those instances when an agreement cannot be reached, the commissioner ... shall make a determination within 30 days" and "A pupil shall remain in attendance in the pupil's school of origin during the pendency of a determination of residency." **Derived**: applying the statute to the two districts named in P25.1. Hooksett's policies are on sau15.net. Raw: raw/choices/rsa-193-12.txt.
18. Under Manchester's policy 508 (revised March 23, 2026), a parent may ask in writing, by July 1 for the coming school year, to move a child to another Manchester school; the Superintendent grants it only if the target school has room under maximum ratios of 20 students per teacher in K–4 and 25 in grades 5–12 (24 in lab courses), may hold seats for families expected to move into that school's area, gives preference to an overflow student returning to their own neighborhood school, and answers by August 1, with appeal to the Board of School Committee.
   - citation: Manchester School District, Policy Students 508, Change of School or Assignment (formerly 104.1)
   - source: https://www.mansd.org/o/msd/page/msd-policy-students-508-change-of-school-or-assignment
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Text: "The request must be made no later than July 1st for the upcoming school year."; "K-4: 1 Teacher for Every 20 Students. Grades 5-12: 1 Teacher for Every 25 Students. Lab Courses: 1 Teacher for Every 24 Students."; "To the extent the student seeking reassignment is an overflow student seeking to return to their resident catchment area school, that request shall be given preference."; "The Superintendent shall notify the parent of the decision under this section no later than August 1st". For moves out of the district the policy requires Board approval and makes transportation the family's responsibility. The policy doesn't address a family that moves within the city mid-year. Read in Chrome in the browser pass (mansd.org refuses automated requests). Raw: raw/choices/mansd-policies-508-511-562-717-2026-11-15.txt
19. Manchester's grade-placement policy 717 (formerly 115) says a student transferring into a Manchester high school, including a home-schooled student, is placed using a transcript from an approved school, test scores or a portfolio of work, or, without them, an evaluation applied equally to all students, after which a graduation plan is set with the family; credits aren't transferred one for one, and students need three semesters at the school to be included in class rank.
   - citation: Manchester School District, Policy Instruction 717, Equity in Determining Grade Placement and Credit
   - source: https://www.mansd.org/o/msd/page/msd-policy-instruction-717-equity-in-determining-grade-placement-and-credit
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Text: "Students seeking to transfer into a high school administered by the Manchester School District must provide any of the following documentation or a combination thereof for the purposes of grade placement: A transcript from an approved school Test scores indicating competence A portfolio of student work"; "All transfer students, including home schooled students and students from other countries, shall be placed and a plan for graduation shall be developed."; "a minimum of three (3) cumulative semesters at the receiving high school". The policy addresses high school only; placement in grades K–8 isn't described. Raw: raw/choices/mansd-policies-508-511-562-717-2026-11-15.txt
20. Manchester's policy 562 (adopted August 24, 2026) gives resident home-educated, EFA, charter and private-school students access to district classes and activities, including athletics, intramurals, band, chorus and clubs, on terms no more restrictive than for enrolled students: families ask in writing (the principal for activities, the Superintendent for classes), meet the same deadlines and eligibility rules, and generally provide their own transportation; EFA students may not exceed half of a normal schedule without leaving the EFA program and must sign a waiver of the district's special education obligation (FAPE).
   - citation: Manchester School District, Policy Students 562, Participation in Public School Activities by Education Freedom Account, Home Educated, Charter and Non-Public Pupils (formerly 162)
   - source: https://www.mansd.org/o/msd/page/msd-policy-students-562-participation-in-public-school-activities-by-home-educated-charter-and-nonpublic-pupils
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Manchester
   - note: Text: "cannot be more restrictive for non-public, Education Freedom Account, public charter school, or home educated pupils than the policy governing the District's resident pupils"; "Co/extra-curricular activities include, but are not necessarily limited to field trips, excursions, athletics (including intramurals), band, chorus, clubs"; "Transportation to and from school generally shall not be provided."; "Education Freedom Account students may not enroll in more than 50% of a normal school schedule without disenrolling in the education freedom account program."; "they shall be required to acknowledge and execute a waiver of FAPE". Raw: raw/choices/mansd-policies-508-511-562-717-2026-11-15.txt

## town-school-options-nearby: Private, Charter and Other School Options Nearby

- kind: local
- question_type: help
- description: Private, charter and other schools families in a town use, with distance and tuition, and EFA use

1. The Goffstown School District's Policy JFAB lets students who aren't Goffstown residents attend its schools when the School Board approves, charging tuition at a rate the board sets each year from a per-pupil cost determined under state law, billed quarterly in advance to the sending district or the parent responsible for payment.
   - citation: Goffstown School District Policy JFAB, Admission of Nonresident Students (and tuition), adopted December 19, 2022
   - source: https://www.sau19.org/index.php/files/555/J-Students/5768/JFAB---Admission-of-Non-Resident-Students-Adopted-12-19-2022
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Goffstown
   - note: Policy text: "all nonresident day students ... will be charged tuition based on a per pupil cost determined in accordance with state law. This cost will be determined annually, and the tuition set by the School Board. A tuition student will not be admitted without School Board approval. ... Tuition will be charged at a rate set by the School Board and billed quarterly in advance to the sending School District or parent responsible for payment." State law allowing this: RSA 193:3, IV (library change-of-school-assignment fact 9). Goffstown's current tuition amount wasn't found. Raw: raw/choices/goffstown-jfab-nonresident.txt; policy list raw/choices/goffstown-policies-j-list.json.

2. Goffstown's Policy JFAB says there is no bus transportation for non-resident students who attend Goffstown schools, and that a sending district's own school board must approve when that district is responsible for the tuition.
   - citation: Goffstown School District Policy JFAB, adopted December 19, 2022
   - source: https://www.sau19.org/index.php/files/555/J-Students/5768/JFAB---Admission-of-Non-Resident-Students-Adopted-12-19-2022
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Goffstown
   - note: Policy text: "When a sending School District is responsible for tuition, approval must be received from the sending School District's School Board. There is no bus transportation provided to non-resident students who attend Goffstown schools." New Boston students, who attend under an AREA agreement, are excepted from the board-approval line. Raw: raw/choices/goffstown-jfab-nonresident.txt.

3. On March 10, 2026, Goffstown voters approved Article 6, 1,609 to 1,575, making Goffstown an open enrollment district under RSA 194-D that admits 5 students from outside the district into kindergarten at Glen Lake School and allows none of its own resident students to seek enrollment outside the district; under RSA 194-D:3, I(e) that took effect July 1, 2026 (**derived** date).
   - citation: Town of Goffstown, 2026 Town and School Election Results (March 10, 2026), School Article 06; 2026 sample ballot; RSA 194-D:3, I(e)
   - source: https://goffstownnh.gov/DocumentCenter/View/5681/2026-Town-and-School-Election-Results-03102026-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Goffstown
   - note: Results page 3, transcribed from image (raw/choices/goffstown-2026-election-results-p3.png; the PDF's text layer is garbled): "ARTICLE 06 Open Enrollment School District ... Ballots Cast 3,361 ... Yes 1,609 ... No 1,575". Article text (voters guide): "to admit 5 students from outside the Goffstown School District into Kindergarten at the Glen Lake School, and to establish that 0 (zero) of the resident student population are eligible to seek enrollment outside of the district". RSA 194-D:3, I(e): "Adoption and limitation actions shall become effective on July 1 immediately following the action." Goffstown's kindergarten is half-day (library district-practices). Raw: raw/choices/goffstown-2026-election-results.pdf/.txt; raw/choices/goffstown-2026-voters-guide.txt.

4. Goffstown's 2026 voters guide explained that open enrollment districts may charge the sending district 80% of the per-pupil cost, that the article would not restrict Goffstown students from charter schools, EFAs, home schooling or change-of-school requests, and that its main goal was to limit the district's possible costs while more is learned about open enrollment.
   - citation: Town of Goffstown, 2026 Voters Guide, School Article 6 explanation
   - source: https://goffstownnh.gov/DocumentCenter/View/5664/2026-Voters-Guide-PDF
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Goffstown
   - note: Guide text: "Open Enrollment districts can receive students from other districts and are allowed to charge the sending district 80% of the per pupil cost. ... This article would not restrict any Goffstown student from attending any charter school, accessing Educational Freedom Accounts, being Home Schooled, or requesting a change of school assignment under RSA 193:3. The main goal of the article is to limit the potential financial expenses to the district while more information about Open Enrollment Districts is learned, litigated in other districts, or changed by state law." The statute: RSA 194-D:5, I (sending district pays at least 80% of its average cost per pupil); no transportation either way, RSA 194-D:2, IX (library open-enrollment-status facts 4–5). Raw: raw/choices/goffstown-2026-voters-guide.txt.

5. Trinity High School's 2026-27 school profile lists about 343 students, says they come from over 44 New Hampshire communities with most from the greater Manchester area, and says about 65% are Catholic, with admission based on academic record, teacher recommendations and placement exams.
   - citation: Trinity High School, 2026-2027 Profile
   - source: https://www.trinity-hs.org/editoruploads/files/2026-2027/2026-20267%20Profile%20(1).pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Profile text: "Students come from over 44 communities in New Hampshire. The majority are from the greater Manchester area. While approximately 65% of our students are of the Catholic faith, students of other faiths are welcome. Acceptance and placement are based on demonstrated academic performance, teacher recommendations and placement exams." and "Student Enrollment: approx 343 / Average Class Size: 18". Sponsored by the Diocese of Manchester; 581 Bridge Street. Raw: raw/choices/trinity-2026-27-profile.txt.

6. Trinity High School's tuition page doesn't list a tuition amount; it says Trinity accepts EFA funding through the Children's Scholarship Fund, opens its financial aid application in late January, and gives a $500 per-student discount to families with two or more children at Trinity or St. Joseph Junior High, and military discounts of $2,500 (active duty) or $1,000 (veterans) per family.
   - citation: Trinity High School, Tuition & Aid
   - source: https://www.trinity-hs.org/admissions/tuition-aid.cfm
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Page text: "In addition to our Financial Aid Program, Trinity High School accepts EFA funding through the Children's Scholarship Fund." "Sibling Discount: Families with 2 or more siblings at either Trinity or St. Joe's are eligible to receive a $500 tuition discount per student." "Children of an Active Military member ... $2,500 tuition discount per THS family ... Children of our Military Veterans ... $1,000". Tuition questions go to the Tuition Manager (tuition@thsstj.org). Raw: raw/choices/trinity-tuition-aid.txt.

7. Saint Joseph Junior High School in Manchester lists 2026-27 tuition of $9,885, plus a $50 application fee, a new-student enrollment fee of $125 ($250 after February 1), a $250 book and material fee, a $150 graduation fee for 8th graders and $100 for Fair Share Calendars, with a $500 per-student discount for families with two or more children in Catholic schools.
   - citation: Saint Joseph Junior High School, Tuition & Assistance 2026-2027
   - source: https://www.stjoesjrhs.org/editoruploads/files/Admissions/STJ%202026_2027%20Tuition%20Rates%20.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Text: "2026-2027 Tuition Cost: $9,885 ... Non-Refundable $50 Application Fee ... Enrollment Fee (for new students): $125 through January 31st. $250 after February 1st ... Book & Material Fee: $250 per student ... Graduation Fee: $150 ... Fair Share Calendars: $100 per student ... Sibling Discount: Families with 2 or more siblings in Catholic schools are eligible to receive a $500 tuition discount per student." Payments may be yearly, quarterly, monthly, biweekly or weekly. Raw: raw/choices/stjoseph-jrhs-2026-27-tuition-rates.txt.

8. Holy Family Academy in Manchester lists 2026-27 tuition of $9,603 for grades 7 and 8 and $12,317 for grades 9 to 12, with uniforms, textbooks, supplies, fundraising, activity, sports and testing fees extra, and asks families seeking its financial aid to also apply for state funding through the Children's Scholarship Fund.
   - citation: Holy Family Academy, Admissions: Tuition and Financial Aid
   - source: https://www.holyfamilyacademy.org/admissions
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Page text: "2026-2027 TUITION / 7th & 8th Grade - $9,603* / 9th-12th Grade - $12,317* ... *Other costs/fees include: uniforms, textbooks, supplies, fundraising fee, activity fee, sports fees, and testing fees." "Families who apply for financial aid must also apply for state funding through the NH Children's Scholarship Fund. There is a $40 fee for the FACTS Grant and Aid Assessment". Priority aid deadline 3/1/2026. The site's data lists Holy Family Academy under the Diocese of Manchester. Raw: raw/choices/holy-family-admissions.txt.

9. Mount Saint Mary Academy, a preschool-through-grade-6 Catholic school at 2291 Elm Street, lists 2026-27 tuition of $9,475 for its three-year-old preschool, $7,725 for pre-K and $7,900 for kindergarten to grade 6, with the second child's tuition reduced by $500 and later children's by $300, and a $300 non-refundable deposit at registration.
   - citation: Mount Saint Mary Academy, Family Handbook 2026-2027
   - source: https://msm-nh.client.factsmgt.com/oa/client_files/msm-nh/uploads_enroll/MSMA%20FAMILY%20HANDBOOK%2026-27.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Handbook text: "TUITION RATE* PRE-SCHOOL – THREE-YEAR OLD PROGRAM $9475.00 PRE-K – FOUR-YEAR OLD PROGRAM $7725.00 GRADES K-6 $7900.00 *Discount in tuition for families with multiple students. *The second student's tuition will be reduced by $500.00, subsequent children will be reduced by $300.00"; "$300.00 non-refundable deposit at registration"; "We are dedicated to our preschool through 6th grade students". The school's own website (mtstmaryacademy.org) didn't connect; the handbook is posted on its FACTS enrollment site. Raw: raw/choices/mount-st-mary-family-handbook-2026-27.txt.

10. Mount Saint Mary Academy serves preschool through grade 6 and Trinity High School serves high school, so a family considering both would use them for different grades; Manchester's Catholic schools with grades 7 and 8 include Saint Joseph Junior High and Holy Family Academy.
   - citation: Mount Saint Mary Academy Family Handbook 2026-2027; Trinity High School 2026-2027 Profile; Holy Family Academy Admissions; Saint Joseph Junior High tuition sheet
   - source: https://msm-nh.client.factsmgt.com/oa/client_files/msm-nh/uploads_enroll/MSMA%20FAMILY%20HANDBOOK%2026-27.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Handbook: "Preschool through grade six." Holy Family lists 7th–8th and 9th–12th grade tuition; St. Joseph lists an 8th grade graduation fee; Trinity's profile describes a high school. Raw: raw/choices/mount-st-mary-family-handbook-2026-27.txt, trinity-2026-27-profile.txt, holy-family-admissions.txt, stjoseph-jrhs-2026-27-tuition-rates.txt.

11. Saint Benedict Academy in Manchester lists 2026-27 tuition of $6,550 per child for kindergarten to grade 6 and for full-time early childhood ($4,500 part-time), a $500 discount for second and later children, a $300 registration fee per family and a $250 family fundraising fee, and asks families seeking its aid to also apply for EFA and Education Tax Credit funds through the Children's Scholarship Fund.
   - citation: Saint Benedict Academy, Tuition & Financial Aid (Tuitions Rates 2026-2027)
   - source: https://www.stbenedictacademy.org/admissions/tuition-financial-aid.cfm
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Page text: "Tuitions Rates 2026-2027 ... Early Childhood Full Time 5 Days per Week $6,550 / Part Time M-F 7:30-11:30 $4,500 ... Grades K-6 Tuition $6,550 Per Child / $500 multi child discount for second and subsequent children ... non-refundable registration fee of $300 per family and $250 per Family Fundraising Fee". "All families applying for need-based financial aid for students in grades K-6 through FACTS Grant and Aid must also apply for ETC and EFA funds through Children's Scholarship Fund New Hampshire". Raw: raw/choices/st-benedict-tuition.txt.

12. Saint Catherine School in Manchester lists full-day tuition of $6,248 for pre-kindergarten and kindergarten and $6,588 for grades 1 to 6, with an $850 sibling discount in grades 1 to 6, and requires families seeking its aid to also apply for Education Tax Credit and EFA funds through the Children's Scholarship Fund; the page doesn't say which school year the rates are for.
   - citation: Saint Catherine School, Tuition & Financial Aid
   - source: https://www.scsnh.com/tuition
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Page text: "Pre-Kindergarten & Kindergarten | Full Day | $6,248 | Grades 1–6 | Full Day | $6,588 | Sibling Discount (Gr. 1-6 only) | $850" and "All families applying for need based financial aid through FACTS Grant and Aid must also apply for ETC and EFA funds through Children's Scholarship Fund New Hampshire (CSF)". Raw: raw/choices/st-catherine-tuition.txt.

13. Cardinal Lacroix Academy in Manchester lists tuition of $6,325 for preschool through grade 6 for 2025-26, not counting registration and fundraising fees, and says families receiving its financial aid should generally expect to pay at least 50% of tuition and must first apply through the Children's Scholarship Fund.
   - citation: Cardinal Lacroix Academy, Tuition Rates and Financial Aid
   - source: https://www.clanh.org/tuition-rates
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Diocese of Manchester
   - note: Page text: "2025-2026 School Year for Preschool through Grade 6 is $6,325 ... Tuition rates listed do not include registration fee and fundraising fee." "each family should generally expect to pay a minimum of 50% of the total tuition. All families applying for financial aid are first required to apply for grants available through the New Hampshire Children's Scholarship Fund and Education Freedom Act." The page still describes EFAs as for families at or below 300% of the poverty line; since June 2025 there is no income limit (library efa-eligibility-and-cap fact 1). No 2026-27 rate was posted. Raw: raw/choices/cardinal-lacroix-tuition-rates.txt, cardinal-lacroix-financial-aid.txt.

14. The Derryfield School, an independent day school for grades 6 to 12 in Manchester, lists 2026-27 tuition of $46,990, with round-trip bus transportation $2,520, books $75–$350, technology $625–$1,240 and activity fees $60–$300 extra, and lunch included.
   - citation: The Derryfield School, Tuition and Affordability
   - source: https://www.derryfield.org/admission/affording-derryfield/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district The Derryfield School
   - note: Page text: "2026-2027 Tuition | $46,990 ... Transportation (Round Trip) | $2,520 | Transportation (One-Way) | $1,700 | Books* | $75 - $350 | Technology** | $625 - $1,240 | Lunch & Snacks | Included in tuition! | Student Activity Fees* | $60 - $300". Tuition refund insurance is 0.65% of the tuition owed. Raw: raw/choices/derryfield-affording.txt.

15. The Derryfield School says 40% of its students receive need-based aid, its average need-based grant is $28,350 from a $4.5 million aid budget, merit scholarships go to 12% of students, and it offers places only to admitted students it can assist financially, placing others in a wait pool.
   - citation: The Derryfield School, Tuition and Affordability
   - source: https://www.derryfield.org/admission/affording-derryfield/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district The Derryfield School
   - note: Page text: "40% Students Receive Need-Based Financial Assistance / $28,350 Average Need-Based Grant / $4.5M Need-Based Equitable Tuition Budget" and "The Derryfield School will offer space only to those students we can financially assist. If we are unable to provide need-based financial assistance to an admissible student, that student will be placed in the wait pool". Aid applications (Clarity, $65 fee) are due January 15, with decisions March 1. Raw: raw/choices/derryfield-affording.txt.

16. The 2026-27 base EFA grant of $4,351 equals about 55% of Mount Saint Mary Academy's kindergarten-to-grade-6 tuition, 66% of Saint Benedict's, 44% of Saint Joseph Junior High's, 35% of Holy Family Academy's high school tuition and 9% of Derryfield's (**derived**).
   - citation: EFA amounts from the library (state-issues choice-efa-state-cost fact 3); tuition from facts 7–9, 11 and 14
   - source: https://www.derryfield.org/admission/affording-derryfield/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Manchester
   - note: **Derived**: $4,351 divided by $7,900 (Mount Saint Mary K–6), $6,550 (St. Benedict K–6), $9,885 (St. Joseph), $12,317 (Holy Family 9–12), $46,990 (Derryfield). What would remain after the base grant: $3,549, $2,199, $5,534, $7,966 and $42,639. Fees, discounts and school aid are not counted. Trinity's tuition isn't posted. See table manchester_private_school_tuition.

17. A 2026-27 EFA for a student whose household income qualifies for the extra free-or-reduced-price-meal amount is $6,792 ($4,351 plus $2,441), which equals about 86% of Mount Saint Mary's kindergarten-to-grade-6 tuition, 104% of Saint Benedict's, 69% of Saint Joseph Junior High's, 55% of Holy Family's high school tuition and 14% of Derryfield's (**derived**).
   - citation: EFA amounts from the library (choice-efa-state-cost fact 3); differentiated aid factors from Children's Scholarship Fund NH, EFA Parent Handbook (August 2026)
   - source: https://nh.scholarshipfund.org/wp-content/uploads/2026/09/Parent-Handbook-CSF-8-2026.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Manchester
   - note: **Derived**: $6,792 divided by each tuition in fact 16. Handbook text: "The factors that qualify a student as eligible for differentiated aid are: Verification of household income at or below 185% of the federal poverty line; ... English Language Learner; ... a qualifying disability." Special education adds $2,229 and English learner status $849 in 2026-27 (library). The average EFA in 2026-27 was about $5,169 (library choice-efa-state-cost fact 5). Raw: raw/choices/csf-efa-parent-handbook-2026-08.txt.

18. Five Manchester private schools' tuition pages (Trinity, Saint Benedict, Saint Catherine, Holy Family and Cardinal Lacroix) point families to EFA funds through the Children's Scholarship Fund, and three of them require families seeking the school's own aid to apply there first.
   - citation: Tuition pages of Trinity High School, Saint Benedict Academy, Saint Catherine School, Holy Family Academy and Cardinal Lacroix Academy
   - source: https://www.trinity-hs.org/admissions/tuition-aid.cfm
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Manchester
   - note: **Derived** count from facts 6, 8, 11, 12 and 13. Saint Benedict and Saint Catherine: "must also apply for ETC and EFA funds"; Cardinal Lacroix: "first required to apply for grants available through the New Hampshire Children's Scholarship Fund and Education Freedom Act"; Holy Family: "must also apply for state funding through the NH Children's Scholarship Fund"; Trinity: "accepts EFA funding through the Children's Scholarship Fund." Raw: raw/choices/trinity-tuition-aid.txt, st-benedict-tuition.txt, st-catherine-tuition.txt, holy-family-admissions.txt, cardinal-lacroix-financial-aid.txt.

19. Census Bureau estimates for 2020–2024 put about 15% (plus or minus 8 percentage points) of kindergarten-to-grade-12 students living in Manchester's two North End census tracts in a private school or home school, compared with about 11% (plus or minus 2 points) citywide and 13% statewide; the margins overlap, so the survey can't show a clear difference (**derived**).
   - citation: U.S. Census Bureau, American Community Survey 2020–2024 5-year estimates, table B14002 (School Enrollment by Level of School by Type of School), census tracts 1.03 and 1.04, Hillsborough County
   - source: https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b14002.dat
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Manchester
   - note: **Derived**: tracts 1.03 and 1.04 lie 94% and 99% inside the city's North End neighborhood area (tract 6, 37% inside, is left out). Private or home school, K–12: 139 (±85) of 927 (±240) = 15.0% (±8.3). Citywide 1,701 of 14,993 = 11.3% (±2.0), the same formula as the site's measure private_k12_pct. Margins combined by the Census Bureau's formulas for sums and proportions. Method and output: raw/choices/gis/acs-private-share-method.py.txt, acs-private-share-output.txt. See table manchester_private_or_home_school_share. Raw: raw/choices/gis/acsdt5y2024-b14002-nh-extract.dat (NH rows of the national file), tigerweb-2020-tracts-hillsborough-4326.json.

20. For high school grades alone, the same 2020–2024 Census estimates put about 22% (plus or minus 16 percentage points) of North End students in grades 9 to 12 in a private school or home school, about 51 of 232 students, compared with about 12% (plus or minus 4 points) citywide (**derived**).
   - citation: U.S. Census Bureau, American Community Survey 2020–2024 5-year estimates, table B14002, tracts 1.03 and 1.04
   - source: https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b14002.dat
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Manchester
   - note: **Derived**: 51 (±44) of 232 (±105) = 22.0% (±15.9); city 602 of 5,216 = 11.5% (±3.8). The North End sample is small, so the range is wide (about 6% to 38%). The survey doesn't say which private school, and it counts home schooling as private. Raw: raw/choices/gis/acsdt5y2024-b14002-nh-extract.dat.

21. Grouping Manchester's census tracts by the high school zone holding most of each tract's area, the 2020–2024 Census estimates put the share of K–12 students in private or home school at about 8% (plus or minus 3 points) in Central's zone, 14% (plus or minus 5) in West's and 13% (plus or minus 4) in Memorial's (**derived**).
   - citation: U.S. Census Bureau, ACS 2020–2024 5-year, table B14002; City of Manchester GIS high school zones; Census TIGERweb 2020 tracts
   - source: https://ags.manchesternh.gov/agsgis7/rest/services/Community/SchoolDistricts/MapServer/1
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Manchester
   - note: **Derived**: each of the 30 tracts with at least half its area in the city was assigned to the high school zone covering most of its area (most were 89–100% in one zone; tracts 17 and 19 were 69% and 65%). Central 412 of 5,205 (7.9% ±3.1; includes the two North End tracts); West 507 of 3,730 (13.6% ±5.3); Memorial 782 of 6,058 (12.9% ±3.9). The 30 tracts sum exactly to the city's totals. Zone of residence, not school attended. See table manchester_private_or_home_school_share.

## school-residency-rules: Which District Is Responsible for a Student

- kind: rule
- question_type: rules
- description: Which district is legally responsible for a student under New Hampshire law: domicile, guardians, divided homes and parenting plans, moves between districts, attending a district where a student doesn't live, and who decides disputes

1. New Hampshire's residency law says that, for children of divorced or separated parents, nothing in it requires a school district to transport a child to another school in the district, beyond the attendance area of the school the child is assigned to, or beyond the district's borders.
   - citation: RSA 193:12, II(a)(2)(B)
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Statute text: "(B) Nothing in this subparagraph shall require a school district to provide transportation for a child to another school in the school district in which the child resides, or beyond the designated attendance area for the school to which the child is assigned, or beyond the geographical limits of the school district in which the child resides." The section was last amended by 2026, 307:4, effective July 10, 2026. Divided-home residence rules are in Hart's Location money-and-governance.md school-residency-rules 2–3. Raw: raw/choices/rsa-193-12.txt.

## efa-eligibility-and-cap: Education Freedom Accounts: Who Qualifies, the Cap and Priority Groups

- kind: rule
- question_type: rules
- description: Who can get an Education Freedom Account (EFA) after SB 295 (2025), the enrollment cap, priority groups and who runs the program.

1. The Children's Scholarship Fund's EFA Parent Handbook (August 2026) says the enrollment cap is 12,500 students for 2026-27, and that because enrollment reached 90% of the cap, the cap rises to 15,625 students for 2027-28; current EFA students, their siblings, children with disabilities and families at or below 350% of the federal poverty guidelines are not held to the cap.
   - citation: Children's Scholarship Fund – New Hampshire, EFA Parent Handbook (8-2026), Enrollment Cap and Priority Groups; RSA 194-F
   - source: https://nh.scholarshipfund.org/wp-content/uploads/2026/09/Parent-Handbook-CSF-8-2026.pdf
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Handbook text: "The State legislature has set a maximum enrollment cap of 12,500 EFA students for the 2026-27 school year. The enrollment cap does not apply to students that meet the eligibility requirements of one or more priority groups ... In the event that the EFA program reaches 90% of the enrollment cap in any given year, the enrollment cap will be raised by 25% the following school year. In 2027-28 the cap will be raised to 15,625 students." Adds the 2027-28 figure to the library's fact 5. Raw: raw/choices/csf-efa-parent-handbook-2026-08.txt.

2. The Children's Scholarship Fund says EFA applications are rolling, that an application completed and verified by July 15 receives a full EFA for the coming school year, and that families may apply through February for a prorated EFA for the current year; students enrolled full time (more than 50% of instructional time) in their district's public school or a charter school, including VLACS, are not eligible.
   - citation: Children's Scholarship Fund – New Hampshire, "Everything You Need to Know about Education Freedom Accounts" and EFA Parent Handbook (8-2026)
   - source: https://nh.scholarshipfund.org/apply/nh-education-freedom-accounts/
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Page text: "Applications are rolling. Applications completed and verified by July 15 are eligible for a full EFA for the upcoming school year, or families may apply through February for a prorated EFA for the current school year." Handbook: "Students cannot participate in the EFA program if they are enrolled full-time (more than 50% of instructional time) in either: A local district public school; A chartered public school, (including VLACS)". Raw: raw/choices/csf-efa-everything-you-need.txt; raw/choices/csf-efa-parent-handbook-2026-08.txt.

3. The Children's Scholarship Fund says a student's EFA grows with differentiated aid when the household income is at or below 185% of the federal poverty line, the student is an English learner who scored below 4.5 on the public school English proficiency test, or the student has a qualifying disability, and that families must re-qualify for the income amount each year.
   - citation: Children's Scholarship Fund – New Hampshire, EFA Parent Handbook (8-2026), Differentiated Aid
   - source: https://nh.scholarshipfund.org/wp-content/uploads/2026/09/Parent-Handbook-CSF-8-2026.pdf
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Handbook text: "Household income at or below 185% of Federal Poverty Line ... Families must qualify annually by providing annual financial documentation for the additional grant funds." "English Learner Grant means eligible students who ... participated in the annual assessment of English language proficiency at a public school and score below 4.5." "the student shall meet the requirements of a child with a disabling condition, as defined in 34 CFR 300.8." Amounts for 2026-27 are in the library (choice-efa-state-cost fact 3). Raw: raw/choices/csf-efa-parent-handbook-2026-08.txt.

## manchester_private_school_tuition: Posted Tuition at Manchester Private Schools

- unit: dollars
- period: school year 2026-27 unless noted; year: 2027
- source: each school's own tuition page or handbook (URLs in town-school-options-nearby facts 7–9 and 11–14)
- as_of: 2026-11-15
- raw: raw/choices/stjoseph-jrhs-2026-27-tuition-rates.txt; holy-family-admissions.txt; mount-st-mary-family-handbook-2026-27.txt; st-benedict-tuition.txt; st-catherine-tuition.txt; cardinal-lacroix-tuition-rates.txt; derryfield-affording.txt
- topic: town-school-options-nearby
- place: town Manchester
- note: Tuition only; fees, discounts and aid are in the facts. Base EFA share is **derived** ($4,351 for 2026-27; $4,265.64 for 2025-26) and rounded. Trinity High School (grades 9–12) doesn't post its tuition. Mount Zion Christian Schools and North End Montessori couldn't be reached.

| Place | School | Grades | School year | Value | Base EFA as share of tuition |
|---|---|---|---|---|---|
| Manchester | Mount Saint Mary Academy | Preschool (age 3) | 2026-27 | 9475 | |
| Manchester | Mount Saint Mary Academy | Pre-K (age 4) | 2026-27 | 7725 | |
| Manchester | Mount Saint Mary Academy | K–6 | 2026-27 | 7900 | 55% |
| Manchester | Saint Benedict Academy | K–6 and full-time early childhood | 2026-27 | 6550 | 66% |
| Manchester | Saint Catherine School | Pre-K and K, full day | not stated | 6248 | |
| Manchester | Saint Catherine School | 1–6 | not stated | 6588 | 66% |
| Manchester | Cardinal Lacroix Academy | Preschool–6 | 2025-26 | 6325 | 67% (2025-26 base) |
| Manchester | Saint Joseph Junior High School | Junior high | 2026-27 | 9885 | 44% |
| Manchester | Holy Family Academy | 7–8 | 2026-27 | 9603 | 45% |
| Manchester | Holy Family Academy | 9–12 | 2026-27 | 12317 | 35% |
| Manchester | The Derryfield School | 6–12 | 2026-27 | 46990 | 9% |

## manchester_private_or_home_school_share: Share of K–12 Students in Private or Home School, Manchester Areas

- unit: percent
- period: American Community Survey 2020–2024 5-year estimates; year: 2024
- source: U.S. Census Bureau, ACS table B14002 (table-based summary file) — https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b14002.dat
- as_of: 2026-11-15
- raw: raw/choices/gis/acsdt5y2024-b14002-nh-extract.dat; tigerweb-2020-tracts-hillsborough-4326.json; neighborhoods-4326.json; schooldistricts-layer1-4326.json
- topic: town-school-options-nearby
- place: town Manchester
- note: **Derived.** Share of students enrolled in kindergarten through grade 12 who attend a private school or are home schooled (the ACS counts home schooling as private), by where they live. Areas are groups of census tracts: the North End tracts are 1.03 and 1.04; the zone rows assign each tract to the high school zone covering most of its area (the Central row includes the North End tracts). MOE is the 90% margin of error, in percentage points. The city and state rows match the site's private_k12_pct measure, which uses the same formula.

| Place | Area | Value | MOE | Grades 9–12 | MOE 9–12 | Note |
|---|---|---|---|---|---|---|
| Manchester | North End (tracts 1.03, 1.04) | 15.0 | 8.3 | 22.0 | 15.9 | 139 of 927; 51 of 232 |
| Manchester | Central High zone (12 tracts) | 7.9 | 3.1 | 8.0 | 5.8 | 412 of 5,205; 118 of 1,467 |
| Manchester | West High zone (8 tracts) | 13.6 | 5.3 | 12.7 | 7.7 | 507 of 3,730; 201 of 1,585 |
| Manchester | Memorial High zone (10 tracts) | 12.9 | 3.9 | 13.1 | 7.2 | 782 of 6,058; 283 of 2,164 |
| Manchester | Whole city | 11.3 | 2.0 | 11.5 | 3.8 | 1,701 of 14,993; 602 of 5,216 |
| NH | Statewide | 13.1 | 0.7 | 13.0 | 1.2 | 25,005 of 191,066; 8,447 of 65,029 |

## For another file

- **Agent 1 (elementary):** the city's elementary zone map has 12 zones and no Hallsville or Wilson zone; the "Hallsville" neighborhood now lies in Jewett, Beech Street, Weston and McDonough zones (`district-attendance-zones-and-transfers` 2, 8). The April 2018 plan set the K–4 and grades 5–8 timeline (West Side 2019, rest of city 2020) that explains the "5th grader at an elementary school" premises (facts 11–12; raw/choices/msd-announcements-2018-04-redistricting.txt).
- **Agent 5 (daily):** bus eligibility is 1.4 miles from the "districted school," and moves go through the school (zones fact 14); RSA 193:12, II(a)(2)(B) says districts needn't transport a divided-home child beyond the assigned school's attendance area (`school-residency-rules` 1 here), for P25.3.
- **Agent 3 (MST):** the 2018 announcement says MST then held a lottery for 9th graders when applicants exceeded openings and planned shared classes at Memorial (raw/choices/msd-announcements-2018-04-redistricting.txt). This is history, not current practice.
- **Agent 8 (money) and the library:** NHPR (May 29, 2026; raw/choices/nhpr-2026-05-29-open-enrollment.txt) reports that a 2025 New Hampshire Supreme Court ruling in a Pittsfield case "clarified that under existing law, a student's home district must send 80% of what it spends per student to the new district," and that districts can limit their students' use of open enrollment by local policy. The opinion (courts.nh.gov) returned 403. The library's `open-enrollment-status` doesn't mention this ruling; it should be added from the opinion itself. Manchester Ink Link reported that the Board of School Committee tabled an open enrollment policy in May 2026 (not retrieved).
- **Library `efa-eligibility-and-cap` fact 5:** the cap rises to 15,625 for 2027-28 (fact 1 here).
- **Library raw, private-schools:** `additional-data/raw/private-schools/sources/calendar_year_number_served_2025.pdf` is a list headed "DRAFT" of EFA students served by each provider in 2025 (Trinity High School 198; Saint Catherine 171; St. Benedict 102; Holy Family 94; Mount Zion 89; Cardinal Lacroix 88; St. Joseph Junior High 81; Mount Saint Mary 81; North End Montessori 17). Its source URL isn't recorded, so it isn't cited here.
- **Earlier town files:** Hart's Location `school-residency-rules` 2–3 and Chatham `school-residency-rules` 1–5 match RSA 193:12 as read on 2026-11-15. The statute's history line shows a 2026 amendment (ch. 307:4, effective July 10, 2026); those facts' quotations are unchanged.

## Not retrieved

- https://www.mansd.org/ (every page tried returned a "Client Challenge" bot check on 2026-11-15, so the site's other pages weren't tried): Policy Students 104.1 Change of School or Assignment (/o/msd/page/msd-policy-students-104-1-change-of-school-or-assignment), 104 Manifest Educational Hardship, 105 Admission of Resident Students, 106 Admission and Tuition of Nonresident Students, Instruction 115 Equity in Determining Grade Placement and Credit (/o/msd/page/msd-policy-instruction-115-equity-in-determining-grade-placement-and-credit), the district policies list (/page/district-policies), the facilities planning updates page (/o/msd/page/facilities-planning-updates), the home education page and Board of School Committee minutes. The same pages appear under school subdomains (beech.mansd.org, jewett.mansd.org); those weren't tried. These hold Manchester's rules for in-district transfers and oversubscribed schools (P22.2, P38.1), placement of students returning from home education (P28.3), and access for homeschooled students (P28.1).
- https://priorityone.mansd.org/?p=25 (Priority One facilities plan, Beech Street and Wilson): connection failed.
- https://manchester.inklink.news/ (HTTP 403): ?p=276993 (intra-district transfers policy), ?p=280329 (School Committee tables open enrollment policy, May 2026), ?p=272000 (high school realignment discussion, January 2026), ?p=139450 (temporary redistricting for Wilson students), ?p=234892 (four elementary schools may see student shifting).
- https://www.courts.nh.gov/sites/g/files/ehbemt471/files/documents/2025-10/2025046pittsfield.pdf (2025 Supreme Court open enrollment ruling): HTTP 403 "Access Denied".
- https://www.aol.com/news/henry-wilson-school-closes-goes-225000400.html (syndicated Union Leader article on Wilson's closure): HTTP 404.
- Trinity High School's tuition amount: not posted on https://www.trinity-hs.org/admissions/tuition-aid.cfm; families are referred to the Tuition Manager.
- https://mtstmaryacademy.org, https://www.mzcs.org (Mount Zion Christian Schools), http://northendmontessori.com: no connection. Mount Saint Mary's handbook was used instead; the other two schools' tuition wasn't found.
- Goffstown School District's current tuition rate for non-resident students: not on the policy or voters guide pages; searched the SAU 19 policy list and the 2026 election documents.
- https://api.census.gov/ (ACS tract data): now requires an API key and redirected to missing_key.html; the Census Bureau's table-based summary file was used instead.
- The session's web search budget ran out near the end, so Goffstown's tuition rate, Manchester middle school athletics rules for homeschoolers and a current redistricting plan weren't searched further.
