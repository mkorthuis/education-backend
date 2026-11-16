# Getting to School, Choices and Communication in Londonderry

Part of the Londonderry research (town/Londonderry). Gathered November 15, 2026.

## Summary

This file covers how Londonderry students get to school and how the district reaches families: the 2026-27 bus routes after full-day kindergarten ended the midday Moose Hill runs, school hours and drop-off windows at each school, how elementary schools are assigned by address and what happens when a family moves, kindergarten registration paperwork, homeschooled students' access to sports and band, the district's home education pages after the 2026 change in state law, snow-day and delay alerts, lockdown and emergency notices, Chromebook and laptop privacy, and watching school board meetings.

- **9 topics, 77 facts, 2 number tables.** Places: `district Londonderry` for SAU 12, its schools, policies, buses and board; no place for two state privacy rules added to the library topic `nh-student-records-and-privacy`.
- **New data concepts:** scheduled morning pickup windows for all 74 posted 2026-27 routes (derived; table `londonderry_morning_bus_pickup_span_2026_27`); the lengths of the board's 2026 meeting videos (table `londonderry_school_board_video_length_2026`); the times closing and delay notices were posted in 2025-26; the district's false-alarm reports and safety updates; its data-privacy agreement system and breach plan; the in-district kindergarten class cap of 18 and involuntary placements.
- **Main sources:** londonderry.org pages (transportation, closings and delays, registration, home education, board schedule), school board policies EEA, EEA-R, EBCD, EB, JCA, JFA, JFABD, JJJ, IHBG, IGDJ, JICL, JICL-R and BEDH, the 2026-27 handbooks of North, Matthew Thornton, South, the middle school and the high school, the 2026-27 bus route sheets, board minutes (May 2025 to October 2026), the district news blog, the district's technology, ed-tech privacy and digital-tools sites, the LHS program of studies, the district YouTube channel, and RSA 189:66.
- **Premises checked:**
  - "They cut out the midday kindergarten runs" (P1.3): **correct.** The midday Moose Hill buses ended with full-day kindergarten in 2026-27; the superintendent had estimated about $280,000 a year in savings, and the five full-day Moose Hill buses were moved to the elementary routes. **No on-time figures are published**; principals called the start of the year "tremendous" on September 1, 2026.
  - Getting on I-93 south "by 7:30 AM" after a before-school drop-off (P2.3): elementary drop-off opens at 8:30 and school starts at 8:42, so a school drop-off cannot happen before 7:30. The YMCA runs before-school programs inside each elementary school (the site's child care data lists 7:00 to 8:30 a.m.).
  - "Two completely different drop-offs" (P17.1): **correct.** Middle school students enter at 7:34 and start at 7:44; elementary drop-off is 8:30 to 8:42, in different buildings.
  - "Annual homeschool evaluations and testing" (P15.3): **out of date.** State law dropped the annual evaluation on July 1, 2026 (library `home-education-rules` 1–2). Londonderry's posted home education page and policy IHBG (adopted November 12, 2024) still describe a required notice letter, annual evaluations and district testing.
  - "Sitting through three hours of procedural stuff" (P29.3): the 15 regular board meetings streamed in 2026 ran from 31 minutes to 2 hours 26 minutes (median 1 hour 33 minutes, derived); the December 2025 budget workshops ran about four hours each (3 hours 49 minutes and 4 hours 7 minutes).
  - "Close on our house in July" (P9.3): 2027-28 kindergarten registration dates are still not posted (rechecked November 15, 2026). The district asks for proof of residency "satisfactory to the Superintendent"; no source says whether a purchase agreement counts before closing.
- **Questions answered wholly by earlier files:** 1 of 13 (P15.2, EFAs: library `efa-uses-and-requirements`, `efa-eligibility-and-cap`, `efa-how-to-apply`, `choice-hb-1817-efa-public-school-courses`, plus the site's EFA counts). One local fact was added (Londonderry's access policy predates the EFA change).
- **Main gaps:** measured bus on-time or ride-time data (the take-in sheets give stop times but no school arrival time); the school-by-street lookup itself (a Looker Studio report that needs a browser); whether the district has an annual data and privacy governance plan before the board (not found in the 2025–2026 minutes read); any written district rule on finishing the year at the old school after a move within town; what translation SchoolMessenger alerts offer; the cable channel 8 listing (the district's LACTV link returns "page not found").
- **Privacy:** the route sheets list stops by house number. They were read only for times and kept out of `raw/`; a derived CSV with times only is saved (`raw/daily/derived-bus-route-times-2026-27.csv`). Three image-only route pages were read from rendered images for times only. Board minutes name residents who spoke; no facts use those names. Nothing with personal information was sent to any outside service.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.3 Are morning bus routes on time now that the midday kindergarten runs were cut | district-transportation 1–9; table londonderry_morning_bus_pickup_span_2026_27; district-school-day-and-calendar 1 | partial | **Premise correct** (midday runs ended; about $280,000 a year estimated). Policy goal: arrive at least 5 minutes before school starts and home by 4:10 p.m. Elementary pickups are scheduled 7:56 to 8:28 a.m. for an 8:42 start. Principals reported a good start in September 2026. **No on-time data is published.** |
| P2.3 Before-school drop-off cutoff if leaving for I-93 by 7:30 a.m. | district-school-day-and-calendar 1–3, 8; district-transportation 8; site data: child_care (YMCA of Greater Londonderry School's Out programs at Matthew Thornton, North and South, listed 7:00–8:30 a.m. and 3:00–6:00 p.m.) | partial | North's drop-off is 8:30–8:42 at the back entrance; teachers aren't available before 8:30. The district says the YMCA runs before- and after-school programs inside the schools and takes kindergartners. Rates and openings: see agent 1's file (P1.2) and the site's child care data. |
| P3.3 Which elementary school a new house is zoned for | district-attendance-zones-and-transfers 1–3 | full | The registration page links a "Londonderry Elementary Schools by Street" lookup; students are assigned by home address. Kindergarten classes are capped at 18, so a kindergartner may be placed at another school for a year. |
| P9.3 Kindergarten registration and paperwork if closing on a house in July | district-attendance-zones-and-transfers 4–6; library: kindergarten-registration (district-practices fact 45: 2027-28 dates not posted; 2026-27 opened November 5, 2025), kindergarten-entry-cutoff (fact 56: five by September 30) | partial | Online preliminary form, then the registrar's instructions within 5 business days. Needed: birth certificate, proof of residency satisfactory to the superintendent, parenting plan if any, a physical within 12 months, immunizations. **Rechecked:** Moose Hill's page still says "Stay tuned for 2027-2028 Kindergarten Registration." Whether a purchase agreement counts as proof of residency is not stated. |
| P11.1 Moving across town mid-year: finish the year at the same elementary school | district-attendance-zones-and-transfers 7–11; district-transportation 10; library: change-of-school-assignment 1–3, 8; homeless-student-school-stability (Albany `getting-to-school-and-the-day.md` facts 1–5) | partial | Handbooks ask families to tell the office about a move; policy JCA lets a parent ask the superintendent for a different school assignment, and state law says an in-district transfer is approved if the school has room. **No written rule on finishing the year after a move within town was found**; busing from the new address to the old school isn't promised. If a family loses housing, McKinney-Vento lets the child stay in the school of origin. |
| P15.1 Homeschooled kids in LHS sports or marching band | district-homeschool-access 1–5; Nashua `charter-private-and-home.md` district-pe-outdoor-and-athletics 6 (NHIAA by-law for home-educated students); library: home-education-rules 8 | full | Yes, on the same terms as enrolled students: a written request to the principal, the same eligibility, tryouts and fees, and NHIAA rules for sports. The Lancer Marching Band is part of a full-year, one-credit band course, so a homeschooler would ask to take that course. |
| P15.2 How the EFA program works for tutoring or curriculum | library: efa-uses-and-requirements 1–8, efa-eligibility-and-cap 1–6, efa-how-to-apply 1–6, choice-hb-1817-efa-public-school-courses 1–3; site data: EFA counts by town; district-homeschool-access 3 | full | **Answered by earlier files.** EFA money may pay for tutoring, curriculum and textbooks among other costs. Londonderry's access policy JJJ predates the 2026 law that added EFA students to the district-access rule. |
| P15.3 Does the district make annual homeschool evaluations and testing easy | district-homeschool-access 6–8; library: home-education-rules 1–2, 8, choice-hb-1817-efa-public-school-courses 3 | full | **Premise out of date.** No annual evaluation has been required since July 1, 2026. The district's posted page and policy still describe the old notice and evaluation rules, including free district testing. State law now lets home-educated students take the state test and the PSAT through the district. |
| P16.3 Getting snow-day and delay texts early enough before a shift | district-family-communication 1–6; district-transportation 11–12; district-school-day-and-calendar 4–6 | full | Text YES to 67587 to get SchoolMessenger texts. Calls, texts and emails go out at about 5 a.m. (policy says about 5:30), and some decisions are posted the evening or afternoon before. A cancellation after a delay comes by 6 a.m. (blog) or 7:45 a.m. (LHS handbook). Delays are two hours. |
| P17.1 How elementary and middle school times line up; two drop-offs? | district-school-day-and-calendar 1–6, 9; district-transportation 7 | full | **Premise correct.** LMS: enter 7:34, start 7:44, end 2:30. Elementary: drop-off 8:30–8:42, end 3:13. LHS: 7:20–2:14. LMS starts 46 minutes before elementary drop-off opens (derived). Middle and high school students share buses; elementary buses run later. |
| P22.3 How the district tells parents about a medical emergency or lockdown drill | district-safety-and-security 1–8; district-family-communication 3, 7–8 | partial | The district uses ALICE. Families are told of incidents by blog and SchoolMessenger; after a false alarm at Matthew Thornton on September 2, 2026 the district posted a same-day account. During drills and emergencies parents are asked not to call the school or text their child. Injured students get first aid and parents are notified. **No written rule on how fast families are told was found.** |
| P28.3 Cybersecurity and student data privacy on school Chromebooks | district-technology-and-phones 1–9; nh-student-records-and-privacy 1–2 (this file); library: nh-student-records-and-privacy 4, 7 | partial | Chromebooks run web filtering and antivirus; policy says students have no expectation of privacy and the district may monitor all activity. Every digital tool needs a data privacy agreement; a breach plan and NH DOE's minimum standards are posted. **No annual data and privacy governance plan (RSA 189:66, V) was found in the board minutes read.** |
| P29.3 Watching board meetings online without three hours of procedure | district-board-and-public-input 1–9; table londonderry_school_board_video_length_2026 | full | Meetings stream live on YouTube (@londonderryschooldistrict) and cable channel 8, and recordings stay posted; 2026 regular meetings ran a median 1 hour 33 minutes (derived). Recordings have no chapters. Shorter options: the minutes (PDF summaries, usually posted 2–4 weeks later), the agendas, topic-only clips and 3–6 minute video newsletters. |

## district-transportation: Londonderry's Buses, the End of Midday Kindergarten Runs, and Storm Delays

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. In the Londonderry School District, all regular education students in kindergarten through grade 12 are automatically assigned a bus route from their home address; the 2026-27 routes were posted (and updated) on August 27, 2026 as "take in" and "take home" sheets for each school, and questions go through a Transportation Inquiry form.
   - citation: Londonderry School District, Transportation page
   - source: https://www.londonderry.org/departments/transportation
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "8/27: UPDATED 2026/27 REGULAR (grades K-12) Transportation Bus Routes are posted below. All REGULAR EDUCATION students in grades K-12 are automatically signed up for bussing to/from their home address." The Drive folder holds eight sheets (LHS-LMS, Matthew Thornton, North, South; Take In and Take Home), updated August 27 to September 15. Raw: raw/daily/lsd-transportation.txt
2. Londonderry's school buses are run under contract by Student Transportation of America (STA); the business administrator told the board in December 2025 that the contract carried a 3% increase for 2026-27.
   - citation: Londonderry School Board minutes, December 18, 2025, item 5.4 District Office
   - source: https://drive.google.com/file/d/19Yfoocebr70u8d2_yxR6upXWQKx31AVa/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "Our student transportation is with STA which includes a 3% contract increase. There is a breakdown of all the bus usage." The district's news blog also carries STA driver-hiring posts (2023–2024). Raw: raw/daily/minutes/sb-2025-12-18.txt
3. With full-day kindergarten in 2026-27, Londonderry ended its midday kindergarten bus runs to and from Moose Hill School; the business administrator told the board in May 2026 that the five full-day buses that had served Moose Hill would be moved to the elementary routes.
   - citation: Londonderry School Board minutes, May 19, 2026, item 5.3 Bus Presentation
   - source: https://drive.google.com/file/d/1PPfNBpcpDRZ5FxCPL8RXRbNn8rMqWm0L/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "The midday buses were eliminated from Moose Hill, but five full day buses were used at Moose as well and they will be redeployed to the elementary schools." Confirms the P1.3 premise. Before 2026-27, two-hour delays cancelled morning kindergarten (posts titled "2 hr Delay ... No AM K or LEEP"). Raw: raw/daily/minutes/sb-2026-05-19.txt
4. When the Londonderry superintendent laid out the full-day kindergarten plan in August 2025, he estimated it would save about $280,000 in midday bus runs, besides at least $400,000 in staff costs and about $2,100 more in state aid per kindergartner.
   - citation: Londonderry School Board minutes, August 5, 2025
   - source: https://drive.google.com/file/d/1NMtfzH7OwICWdTHo2js7xvH4jGGC24J-/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "Current estimation, we would save at least $400k in staff costs. We learned that we would gain about $2100 per student in state aid by having full day kindergarten. We would also save about $280k in mid-day bus runs." An estimate made before the plan began; no later source read reports the actual savings. Raw: raw/daily/minutes/sb-2025-08-05.txt
5. Since 2026-27, Londonderry kindergartners ride the same buses as other students at Matthew Thornton, North and South; kindergarten and first-grade students have assigned seats at the front, and stops are set around where the youngest riders live.
   - citation: Londonderry School Board minutes, May 19, 2026; Full Day Kindergarten in Neighborhood Schools 2026, FAQ 1–2
   - source: https://www.londonderry.org/community/full-day-k-2026-project
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "The elementary bus routes for next school year will include K-5 students from the same geographical areas. Stops will be designed around where the younger students reside. Kindergarten and first grade students will be assigned seats at the front of each bus." FAQ: "Bus routes will no longer exist for Moose Hill ... Overall Kindergarten routes will get much shorter especially for North and South School." Raw: raw/daily/minutes/sb-2026-05-19.txt; additional-data/raw/districts/batch-4/londonderry-full-day-k-2026-project.txt
6. Londonderry's bus regulations (EEA-R, amended July 14, 2026) set the goals that students arrive at school at least five minutes before school starts and are all home by 4:10 p.m., with exceptions for accidents, bad weather, breakdowns and road closures; students should be at their stop five minutes before the bus, which cannot wait for late students.
   - citation: Londonderry School Board policy EEA-R, Student Transportation Services Regulations for Students Riding School Busses, section A.2 and rules 3
   - source: https://drive.google.com/file/d/1QAhZD0kNBVPsRr1KmkbG5FOcmuILeM2_/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "The goals of the district are that students will arrive at school no less than five (5) minutes before the start of school and that all students will be delivered home no later than 4:10 PM. Exceptions to this rule could be such things as accidents, bad weather, breakdowns, road closures etc." and "The bus cannot wait for those who are not on time." No on-time statistics are published. Raw: raw/daily/lsd-policy-eea-r-bus-regulations.txt
7. Londonderry has run combined buses for the middle and high schools since 2025-26, when the board voted 5–0 for a two-tier system: routing software brought the routes down to 38 buses carrying about 25 to 30 riders each, dropping one bus saved about $70,000, and middle schoolers sit in front; in May 2026 the business administrator reported "very few issues," and the combined routes continue in 2026-27.
   - citation: Londonderry School Board minutes, May 20, 2025 (item 8.1) and May 19, 2026 (item 5.3); Transportation page
   - source: https://drive.google.com/file/d/1SWB6-_ZcVzOVSaC3SIQAsILPILLCieZA/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: 2025 minutes: "Traversa is the routing software ... they could get the routes down to 38 busses ... ridership per bus which is roughly 25-30 students ... LMS students would sit in the front of the bus and LHS to the back. They confirm they could drop a bus in this model and save the district about $70,000 ... approve going to the 2-tier bus routes for the 2025/2026 school year ... 5-0." 2026 minutes: "There were very few issues with combining LHS and LMS bus routes." Transportation page: "We will be continuing with a combined bus route system." Raw: raw/daily/minutes/sb-2025-05-20.txt; raw/daily/minutes/sb-2026-05-19.txt
8. On Londonderry's 2026-27 morning route sheets, the 37 elementary routes (10 at South, 12 at North, 15 at Matthew Thornton) make their first scheduled pickups between 7:56 and 8:15 a.m. and their last between 8:12 and 8:28 a.m., for an 8:42 start; the 37 combined middle and high school routes pick up between 6:35 and 7:08 a.m. (derived; see table londonderry_morning_bus_pickup_span_2026_27).
   - citation: Londonderry School District, 2026-2027 Regular Ed Bus Routes (Take In sheets), derived
   - source: https://drive.google.com/drive/folders/14coaZZnz7gGFFlqdX_zb5jRGZ-zLo9v6
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: **Derived** from the scheduled stop times on each "Take In" page. The sheets give no school arrival time, so ride time to school can't be computed. Three pages had no text layer (Matthew Thornton routes 26 and 30, LHS/LMS route 19) and were read from rendered images. Scheduled, not measured, times. The sheets list stops by house number, so only times were kept. Raw: raw/daily/derived-bus-route-times-2026-27.csv
9. Londonderry's afternoon route sheets for 2026-27 show dismissal at 2:13 p.m. for the high school, 2:30 p.m. for the middle school (both on the same combined buses) and 3:13 p.m. for the three elementary schools.
   - citation: Londonderry School District, 2026-2027 Regular Ed Bus Routes (Take Home sheets)
   - source: https://drive.google.com/drive/folders/14coaZZnz7gGFFlqdX_zb5jRGZ-zLo9v6
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Sheet text: "2:13PM Dismissal LHS/2:30PM Dismissal LMS" (36 LHS-LMS sheets, updated 09/11/2026); "3:13PM Dismissal" (Matthew Thornton, North and South sheets). Sheets read in the scratchpad only (they list home addresses); times only. See raw/daily/derived-bus-route-times-2026-27.csv for the morning times.
10. In Londonderry, the longest walk to a bus stop is set at a quarter mile for elementary students and half a mile for middle and high school students; stops are grouped at corners, buses don't run on private or Class VI roads, winter stops (Thanksgiving to February vacation) are reviewed on request, each student gets one address "unless there is a family situation," and a request for an alternate address "does not guarantee transportation."
   - citation: Londonderry School District, Transportation page; policy EEA-R, section A.1 and E–F
   - source: https://www.londonderry.org/departments/transportation
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "Kindergarten students shall be picked-up at their driveway whenever possible; maximum walking distance ... Elementary grade students .25 (1/4) of a mile; Middle school grades .5 (1/2) of a mile"; "Winter stops run from Thanksgiving break to February vacation"; "Each student is allowed one address unless there is a family situation"; "this request does not guarantee transportation." The amended EEA-R says instead that stops will be placed "closest to the residence of younger students, especially kindergarten students." Bus assignment changes must be in writing, need space, and last at least a quarter; appeals go to the business administrator, then the superintendent and the board, each within five days. Raw: raw/daily/lsd-transportation.txt; raw/daily/lsd-policy-eea-r-bus-regulations.txt
11. Londonderry's delayed openings are two hours at every school, and buses run their routes two hours later; under policy EBCD (amended August 5, 2025), after-school activities go on after a delay, while a full-day closing or an emergency early release cancels all afternoon and evening programs.
   - citation: North Elementary School Parent and Student Handbook 2026-2027, "Delayed Opening / School Cancellations"; Londonderry School Board policy EBCD, Emergency Closings
   - source: https://drive.google.com/file/d/1sHFDtjwvxd3CDwt1oDDbdVPb9csxoavH/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Handbook text: "Delayed openings result in a 2 hour delay at all schools. All school buses will begin their routes 2 hours later than usual." Policy text: "After-school activities and events will not be affected by a delayed opening"; "If school is closed for the entire day, all afternoon and evening programs shall also be canceled"; "If there is an emergency early release, all afternoon and evening programs shall also be canceled." EBCD still mentions "the cancellation of morning kindergarten, if necessary," written before full-day kindergarten. Raw: raw/daily/lsd-policy-ebcd-emergency-closings.txt; raw/daily/north-student-handbook.txt
12. In the 2025-26 school year, Londonderry's news blog posted three full-day closings (December 2, 2025, January 26, 2026 and March 6, 2026) and three two-hour delays (January 7, January 27 and March 4, 2026); the delay announced for March 6 was changed to a closing that morning (derived from the posts found).
   - citation: Londonderry School News (news.londonderry.org), closing and delay posts, 2025-26
   - source: https://news.londonderry.org/2026/03/06/no-school-activities-3-6-2026/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: **Derived** from the blog's search results for "No School" and "Delay" (posts dated September 2025 to November 2026); a post could have been missed. March 5 post: "There will be a 2 hour delay tomorrow, Friday, 3/6/2026 ... if we need to cancel the whole school day, we will send out a follow up message by 6am." March 6 post: "the Londonderry School District has made the decision to cancel school & activities 3/6/2026." No closing or delay was posted for 2026-27 by November 15, 2026. Raw: raw/daily/news-2026-03-05-delay-no-am-k.txt; raw/daily/news-2026-03-06-no-school.txt; raw/daily/news-2026-01-25-no-school.txt
13. Londonderry's high school bus for Hooksett students who attend Londonderry High School picks up at the Delta Dental Ice Arena (formerly Tri Town) at 6:20 a.m., Hooksett Town Hall at 6:25 and Cawley Middle School at 6:40 in 2026-27.
   - citation: Londonderry School District, Transportation page, "Hooksett Information"; LHS Route 38 Hooksett Take In sheet
   - source: https://www.londonderry.org/departments/transportation
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "Pick Up 6:20AM - Delta Dental Ice Arena (formerly Tri Town) ... 6:25AM - Town Hall ... 6:40AM - Cawley Middle School." The same route sheet adds a morning shuttle that takes CTE students from LHS to Alvirne (Hudson) and a midday return bus from Manchester School of Technology (see "For another file"). Raw: raw/daily/lsd-transportation.txt

## district-school-day-and-calendar: Londonderry's School Hours, Drop-Off Windows and Delayed Openings

- kind: local
- question_type: local_practice
- description: School hours, before- and after-school care, the school calendar and vacations, and attendance and absence rules

1. Londonderry's three elementary schools (Matthew Thornton, North and South) run from 8:42 a.m. to 3:13 p.m. in 2026-27; students may arrive from 8:30, when staff supervision begins.
   - citation: North Elementary School Parent and Student Handbook 2026-2027, "School Day"; Matthew Thornton School Profile
   - source: https://north.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: North handbook text: "Students arrive starting at 8:30 reporting directly to their classrooms. School starts at 8:42 and ends at 3:13." Matthew Thornton profile: "Hours: 8:42 AM – 3:13 PM." The Matthew Thornton and South 2026-27 handbooks give the same 8:30–8:42 drop-off and "Dismissal Time is 3:13." Raw: raw/daily/north-student-handbook.txt; raw/daily/mt-school-profile.txt; raw/daily/mt-student-handbook.txt; raw/daily/south-student-handbook.txt
2. Each Londonderry elementary school has its own parent drop-off spot, open 8:30 to 8:42 a.m.: North uses the back entrance (entering from Clark Road along Sanborn Road, with a new two-lane setup: left lane grades 1–5, right lane kindergarten and siblings), Matthew Thornton the front of the building, and South the back of the building, each away from bus traffic.
   - citation: 2026-27 handbooks of North ("Parents Dropping Off in the AM"), Matthew Thornton and South ("Parents Transporting Students To and From School")
   - source: https://north.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: North: "Students may be dropped off at the back entrance of North School between 8:30 and 8:42 a.m. ... two lanes of traffic (new this year)." Matthew Thornton: "Parents/guardians are asked not to drop off students before 8:30 AM, as teachers are not available prior to that time for supervision, and the doors are locked. A drop off area has been established ... between 8:30 and 8:42 AM at the front of the building. PLEASE DO NOT DROP OFF STUDENTS IN THE BACK." South: "between 8:30 and 8:42 AM at the back of the building. PLEASE DO NOT DROP OFF STUDENTS IN THE FRONT." Raw: raw/daily/north-student-handbook.txt; raw/daily/mt-student-handbook.txt; raw/daily/south-student-handbook.txt
3. The Londonderry School District says the YMCA runs before- and after-school programs inside its elementary schools and can take kindergartners now that kindergarten is full-day; the district refers families to the YMCA for details.
   - citation: Londonderry School District, Full Day Kindergarten in Neighborhood Schools 2026, FAQ 4
   - source: https://www.londonderry.org/community/full-day-k-2026-project
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: FAQ text: "Can Kindergarten students attend the before and after-school programs within our schools? Yes. The YMCA is aware of this plan for the 2026-27 school year and can accommodate Kindergarten students. Please reach out to them for more information: https://www.graniteymca.org/programs/child-care/school-age-child-care/." Hours, licensed places and openings are in the site's child care data (YMCA of Greater Londonderry School's Out programs at each school); not restated. The 2026-27 handbooks describe no district-run before-school care. Raw: additional-data/raw/districts/batch-4/londonderry-full-day-k-2026-project.txt
4. Londonderry Middle School students enter at 7:34 a.m. and the day starts at 7:44 and ends at 2:30 p.m. in 2026-27; the handbook says a student not in the building by 7:40 is marked tardy, and on a two-hour delay homeroom starts at 9:44.
   - citation: Londonderry Middle School Student Handbook 2026-2027; LMS Daily Schedule 2026-2027; LMS Delayed Opening Schedule 2026-2027
   - source: https://lms.londonderry.org/information/daily-schedule
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Handbook text: "STUDENTS ENTER 7:34 STARTING TIME 7:44"; "students are expected to go directly to homeroom after the 7:35 AM bell. Any student not in the building by 7:40 AM will be marked/recorded as tardy"; "Homeroom will begin at 9:44 a.m." Schedule PDF (scanned with a text layer): "STUDENT DAY: 7:44 a.m. _ 2:JO p.m." (read as 2:30; the bus sheets say "2:30PM Dismissal LMS"). Delayed schedule: "STUDENT DAY: 9:44 a.m. - 2:30 p.m." Raw: raw/daily/lms-student-handbook.txt; raw/daily/lms-daily-schedule-2026-27.txt; raw/daily/lms-delayed-opening-2026-27.txt
5. Londonderry High School's regular day runs from 7:20 a.m. (A period) to 2:14 p.m. (H period); on a two-hour delay it starts at 9:20 and still ends at 2:14, with every period shortened.
   - citation: Londonderry High School, Schedules page (Regular and 2 Hour Delay Bell Schedules); LHS Student Handbook
   - source: https://lhs.londonderry.org/information/schedules
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "A 7:20 - 8:07 ... H 1:27 - 2:14"; "2 Hour Delay Bell Schedule ... A 9:20 - 9:52 ... H 1:42 - 2:14." Handbook: "Delayed openings of school shall be for 2 hours (school starts at 9:20 AM)"; "A student is late to school if he/she arrives after 7:20 a.m." Raw: raw/daily/lhs-schedules-page.txt; raw/daily/lhs-student-handbook.txt
6. On a two-hour delay, Londonderry's elementary school day begins at 10:42 a.m., and the North handbook asks parents not to call the school about delays or early dismissals.
   - citation: North Elementary School Parent and Student Handbook 2026-2027, "Delayed Opening / School Cancellations"
   - source: https://north.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Handbook text: "The school day will begin at 10:42 AM on Delayed Opening school days. Please avoid calling the school to inquire about delay or early dismissals." Raw: raw/daily/north-student-handbook.txt
7. At Londonderry's elementary schools, parents enter changes to a child's dismissal plan in the PickUp Patrol app by 2:00 p.m. (after that only emergency changes by phone), report absences there by 8:45 a.m. (North), and are asked to pick up children for appointments before 2:45 p.m. so they don't board the bus.
   - citation: 2026-27 handbooks of North ("Absences – Tardiness – Dismissals"), Matthew Thornton and South ("Dismissal")
   - source: https://north.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: North: "Changes can be entered ... at any time up until 2:00pm on the day of the change. After 2:00pm, changes will not be accepted except in the case of an emergency"; "report the absence using PickUp Patrol by 8:45 on the day of the absence." Matthew Thornton and South: "Students who have appointments or need to be dismissed prior to the 3:13 dismissal time, should be dismissed prior to 2:45." Raw: raw/daily/north-student-handbook.txt; raw/daily/mt-student-handbook.txt
8. A Londonderry family with a middle schooler and an elementary student has two separate morning drop-offs in 2026-27: the middle school day starts at 7:44 a.m., 46 minutes before elementary drop-off opens at 8:30, and ends at 2:30 p.m., 43 minutes before elementary dismissal at 3:13 (derived).
   - citation: Londonderry Middle School Student Handbook 2026-2027; North Elementary School Parent and Student Handbook 2026-2027 (derived comparison)
   - source: https://lms.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: **Derived** by subtracting the published times (7:44 to 8:30; 2:30 to 3:13). The middle school is at 313 Mammoth Road; the elementary schools are separate buildings. Answers the P17.1 premise. Raw: raw/daily/lms-student-handbook.txt; raw/daily/north-student-handbook.txt
9. When Londonderry closes schools early in an emergency, the high school is released first, followed separately by the middle school and the elementary schools at about 40-minute intervals; elementary handbooks ask families to arrange care in advance, and in some evacuations students may be moved to the high school gymnasium.
   - citation: LHS Student Handbook, "School Cancellations, Delays, Emergency Closings"; Matthew Thornton and South 2026-27 handbooks, "Cancellation of School"
   - source: https://docs.google.com/document/d/1nafKoNciyLSTgXMhYMPekj5QpyX9h8KXZs9YobQw84c/edit
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: LHS text: "High school students will be released first, followed separately by the middle school and the elementary schools in approximately forty (40) minute intervals." Matthew Thornton text: "In some emergency evacuation situations students may be relocated to the high school gymnasium for safety reasons whereupon we will attempt to contact parents. An attempt will be made to contact all parents to notify them of the early dismissal and approximate arrival time home." Raw: raw/daily/lhs-student-handbook.txt; raw/daily/mt-student-handbook.txt

## district-attendance-zones-and-transfers: Londonderry's Elementary School Assignments, Registration Papers and Moves Within Town

- kind: local
- question_type: local_practice
- description: How a district assigns students to schools by home address, its feeder pattern from elementary to middle to high school, redistricting history and plans, proof of residency, and requests to attend a different school (added from the Manchester research)

1. Londonderry assigns elementary students (including full-day kindergartners) to Matthew Thornton, North or South by home address, and its Student Registration page links a lookup titled "Londonderry Elementary Schools by Street" for finding a school by street address.
   - citation: Londonderry School District, Student Registration page and New Student Registration form
   - source: https://www.londonderry.org/family/student-registration
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "Elementary School by Address ... Click Here to lookup elementary school assignments by street address" (link: https://lookerstudio.google.com/reporting/34fc43e3-ec08-43fa-805f-d419c5c09558, page title "Londonderry Elementary Schools by Street"; the report itself needs a browser and was not read). Form text: "If full day kindergarten is available your student will be assigned to an elementary school based on home address." All three elementary schools feed Londonderry Middle School and Londonderry High School. Raw: raw/daily/lsd-student-registration.txt; raw/daily/lsd-preliminary-registration-form.html; raw/daily/lsd-looker-elementary-schools-by-street.html
2. Londonderry caps kindergarten classes at 18; under procedures shared with the board in July 2026, if a neighborhood school's kindergarten is full the district may place a child at another elementary school, provide a transportation plan, and aim to return the child to the neighborhood school the next year; families may also ask for a different school.
   - citation: Londonderry School Board minutes, July 27, 2026, item 8.2 Administrative Procedures with Kindergarten Registration
   - source: https://drive.google.com/file/d/1HVaslF5D-4gjsKwcBKRC8eaS2eTzow60/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "The kindergarten classrooms are capped at 18 students and if the number goes above that then students would be placed in neighborhood schools. Families can also request going to a different school voluntarily. The district may place students out of their neighborhood school involuntarily to keep class size at 18. A transportation plan will be determined by the district and provided. The goal would be to return these involuntary transfers back to their neighborhood school by the following school year." Raw: raw/daily/minutes/sb-2026-07-27.txt
3. On the first days of 2026-27, Londonderry had 274 kindergartners (106 at Matthew Thornton, 86 at North and 82 at South), 64 more than expected, with room for 2, 4 and 8 more children at those schools.
   - citation: Londonderry School Board minutes, September 1, 2026, item 10.2 Opening Day Enrollment Report
   - source: https://drive.google.com/file/d/1LiN8AturKtjnoGrv0toAO4045nVApuA7/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "In regard to kindergarten, there are 106 at MT, 86 at NS and 82 at SS. There is a total of 274. MT has room for two more, NS 4 more and SS eight more. Kindergarten enrollment was much larger than anticipated with a 64 jump." The October 31, 2026 enrollment report (library raw) later lists 106, 88 and 86. Raw: raw/daily/minutes/sb-2026-09-01.txt
4. Londonderry registers new students in two steps: a family fills out an online preliminary registration form for each child and then gets instructions from the district registrar by email within about five business days; children already in the LEEP preschool don't need a new form, and on November 15, 2026 the form offered only the 2026-27 school year.
   - citation: Londonderry School District, Student Registration page; New Student Registration form
   - source: https://www.londonderry.org/family/student-registration
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "please complete the preliminary registration form below. After completing the form you will receive further registration instructions from the Registrar within 5 business days. If you need immediate registration assistance please contact the Registrar at registrar@londonderry.org." Form: "School year you are registering your student for. 2026-2027." Moose Hill's page still reads "Stay tuned for 2027-2028 Kindergarten Registration" (library district-practices fact 45 has the 2026-27 dates). Raw: raw/daily/lsd-student-registration.txt; raw/daily/lsd-preliminary-registration-form.html; raw/daily/moose-home.txt
5. Londonderry's admission policy JFAA (adopted January 28, 2025) asks new students to register with a parent before opening day, bringing a copy of the birth certificate, any court-ordered parenting plan and proof of residency "satisfactory to the Superintendent," plus proof of a physical exam within the 12 months before registration and the required immunizations (or a documented medical or religious exemption).
   - citation: Londonderry School Board policy JFAA, Admission of Resident Students
   - source: https://drive.google.com/file/d/1t8uiONuZ6tbq_ZpW32NI4Y5wLlbCusCn/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "Upon registration, all children must have proof of a copy of the child's birth certificate, court ordered parenting plan (if applicable), and proof of residency satisfactory to the Superintendent or his/her designee"; "Physical examination must have been within 12 months prior to the date of registration"; "Any student not meeting the physical examination requirement required under RSA: 200 shall be excluded from school." The policy does not list which documents count as proof of residency, or say whether a purchase agreement is accepted before closing. Raw: additional-data/raw/districts/batch-4/londonderry-policy-jfaa.txt
6. Under Londonderry's policy JFAA, students covered by the federal McKinney-Vento Act (homeless students) and children in state foster custody are enrolled immediately, with physical and immunization records supplied as soon as practical.
   - citation: Londonderry School Board policy JFAA, Admission of Resident Students
   - source: https://drive.google.com/file/d/1t8uiONuZ6tbq_ZpW32NI4Y5wLlbCusCn/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "Students eligible under the McKinney Vento Act or in the custody of the State as a foster child, following a best determination meeting, shall be granted immediate enrollment. Proof of physical and immunizations records should be furnished as soon as practical after enrollment." Raw: additional-data/raw/districts/batch-4/londonderry-policy-jfaa.txt
7. Londonderry's elementary handbooks ask families to tell the school office before moving: a move within the same school's area only needs the new address and phone number, while for a move out of the area the office sends the child's records to the new school (South asks the family to sign a release form there and a records request at the new school).
   - citation: 2026-27 handbooks of Matthew Thornton, North and South, "Transfers"
   - source: https://south.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Matthew Thornton text: "Please notify the school office if you are planning to move. If you are moving to another home within the Matthew Thornton district, the school will need to be aware of your new address ... If you are moving from the Matthew Thornton district, the office will assist you with the transfer of student information to the new school that your child will be attending." South adds: "You will need to sign a Release of Information form here at South School and a Request for Records form at your new school." None of the handbooks says whether a child who moves to another school's area in town may finish the year at the old school. Raw: raw/daily/mt-student-handbook.txt; raw/daily/south-student-handbook.txt; raw/daily/north-student-handbook.txt
8. Londonderry's policy JCA (adopted August 5, 2025) lets a parent ask the superintendent in writing to move a child to another class or school; the superintendent meets the parent within 10 business days and decides in writing within five more; a denial can go to a school board hearing on "manifest educational hardship," and any reassignment lasts no longer than the end of the following school year before review.
   - citation: Londonderry School Board policy JCA, Change of Class or School Assignment: Best Interests and Manifest Hardship
   - source: https://drive.google.com/file/d/1xw7Vj_ZU-O78tiCfXnqoXHmKo_o05llZ/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "the Superintendent is authorized to reassign a student residing in the District to a another class within the school, to another public elementary school within the District"; "the Superintendent shall schedule a meeting ... within 10 business days"; "Within five business days of the reassignment meeting, the Superintendent shall deliver to the parent/guardian a written determination"; "A reassignment based on best interest of the student shall be limited to no longer than the end of the ensuing school year." The policy also says it "does not limit the Superintendent's discretion to make other in-District assignments." State rules on in-district transfers are in library topic change-of-school-assignment. Raw: raw/daily/lsd-policy-jca-school-assignment.txt
9. Londonderry's policy JCA makes parents responsible for transportation only when a child is reassigned to a school in another district; it says nothing about busing for a child reassigned to another Londonderry school, and the district's bus page says a request to be bused from an alternate address "does not guarantee transportation."
   - citation: Londonderry School Board policy JCA, sections A.4 and B.6; Transportation page
   - source: https://drive.google.com/file/d/1xw7Vj_ZU-O78tiCfXnqoXHmKo_o05llZ/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "Transportation for a student reassigned to a school in another district under this Section A (best interest) shall be the responsibility of the parent/guardian." Transportation page: "Please note that this request does not guarantee transportation." Raw: raw/daily/lsd-policy-jca-school-assignment.txt; raw/daily/lsd-transportation.txt
10. Londonderry's policy on homeless students (JFABD, adopted August 26, 2014) says that, to the extent feasible, a homeless student keeps attending the school last attended before becoming homeless unless the parents prefer otherwise, and that the superintendent names a liaison for homeless children and youth to identify and enroll them.
   - citation: Londonderry School Board policy JFABD, Education of Homeless Children and Youth
   - source: https://drive.google.com/file/d/1I26MwNwP398XlchY3-A-3KIIMHyJupJb/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "to the extent feasible, the student's education shall continue in the school the student last attended before becoming homeless, unless doing so is contrary to the wishes of the student's parents or guardian. The Superintendent will designate a Liaison for Homeless Children and Youth." Federal rules (staying in the school of origin, transportation) are in Albany's getting-to-school-and-the-day.md, homeless-student-school-stability 1–5. Raw: raw/daily/lsd-policy-jfabd-homeless.txt
11. Londonderry's residency policy JFA (adopted January 28, 2025) defines residency for enrollment only by reference to state law, RSA 193:12.
   - citation: Londonderry School Board policy JFA, Residency
   - source: https://drive.google.com/file/d/18kZc9zE6PePsoGcirIZ5RUyQ45CDcsJ9/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "Residency for the purpose of enrollment in a District school shall be defined by RSA 193:12." State residency rules are in Tamworth's getting-to-school-and-the-day.md (school-residency-rules 1–3). Raw: raw/daily/lsd-policy-jfa-residency.txt

## district-homeschool-access: Homeschooled and EFA Students in Londonderry's Classes, Sports and Band

- kind: local
- question_type: local_practice
- description: How homeschooled and EFA students can take part in a district's classes, activities and sports, and the district's homeschool notice and evaluation process

1. Londonderry's policy JJJ (adopted November 12, 2024) gives students who live in the district and are home educated or attend a charter or private school the same access as enrolled students to the district's courses and co- and extracurricular programs under RSA 193:1-c, with the same eligibility rules (registration deadlines, academic standing, parent permission, NHIAA rules, physicals) and, when a program is full, the same selection rules, then a random draw.
   - citation: Londonderry School Board policy JJJ, Access to Public School Programs by Non-Public, Charter School, and Home Educated Students, section A
   - source: https://drive.google.com/file/d/1Z40F-y73ogquvsJlRBcM-3uCzdZQHQmI/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "Non-enrolled district students will have the same access as do enrolled students to the District's courses and programs ... provided they meet the eligibility requirements for participation (e.g., deadlines for registration, academic progress/performance, parental permission, third party (e.g., NHIAA) requirements, physical exams/health requirements, etc.)"; "If, after applying such criteria the course/program remains overenrolled, the determination should be made randomly." Raw: raw/daily/lsd-policy-jjj-access-nonpublic-home-educated.txt
2. Under Londonderry's policy JJJ, a parent asks the building principal in writing for a class or activity; for activities such as sports the student must meet the enrolled students' eligibility rules "with the exception of school attendance," pass the same tryouts, follow the governing body's rules and pay the same fees; a denial can be appealed to the principal (meeting within 5 school days, decision within 3) and then the superintendent, whose decision is final.
   - citation: Londonderry School Board policy JJJ, sections B, D and E
   - source: https://drive.google.com/file/d/1Z40F-y73ogquvsJlRBcM-3uCzdZQHQmI/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "Requests by non-enrolled district students for participation in District co-curricular/extra-curricular activities or programs ('activities') shall be made in writing by the parent/guardian to the building Principal"; "Meet the eligibility criteria ... with the exception of school attendance; Meet any tryout criteria"; "subject to the same fees charged enrolled students"; "Within five (5) school days the Principal will convene a meeting"; "a final decision within three (3) school days." Requests for therapies or special education services go to the Student Services Director. Raw: raw/daily/lsd-policy-jjj-access-nonpublic-home-educated.txt
3. Londonderry's policy JJJ names home-educated, public charter and nonpublic school students but not Education Freedom Account (EFA) students, whom state law added to the district-access law (RSA 193:1-c) effective August 18, 2026; it also tells principals to consider "home education evaluation materials" under RSA 193-A:6, a section repealed on July 1, 2026.
   - citation: Londonderry School Board policy JJJ (adopted November 12, 2024); library topics choice-hb-1817-efa-public-school-courses 1–2 and home-education-rules 2
   - source: https://drive.google.com/file/d/1Z40F-y73ogquvsJlRBcM-3uCzdZQHQmI/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "All students residing in the District, whether they are home educated, or are attending public chartered school or nonpublic schools (collectively, 'non-enrolled district students')"; "the Principal should consider home education evaluation materials (see RSA 193-A:6, III)". No 2025 or 2026 board minutes read show a revision of JJJ. Comparison with the state law changes is from the library. Raw: raw/daily/lsd-policy-jjj-access-nonpublic-home-educated.txt
4. Londonderry High School is a member of the NHIAA, which sets athletic eligibility; under board policy IGDJ no student below grade 9 plays on high school teams, a student must pass a medical exam and have written parent consent before practice, and parents provide accident insurance.
   - citation: Londonderry School Board policy IGDJ, Interscholastic Athletics (adopted January 23, 1984)
   - source: https://drive.google.com/file/d/1YvktT842E8iKnkKV3brfouJ2fX4BvTEq/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "The Londonderry High School is a member of the New Hampshire Interscholastic Athletic Association (NHIAA) ... The eligibility of students to participate in the athletic program is determined in accordance with NHIAA regulations"; "No student below grade 9 shall participate in high school athletic programs"; "No student may start practice ... until he or she has been examined and approved by a medical doctor and until written consent has been obtained from the parent"; "Insurance against accident or injury shall be provided by the parents." NHIAA's home-educated rule: Nashua charter-private-and-home.md, district-pe-outdoor-and-athletics 6. Raw: raw/daily/lsd-policy-igdj-interscholastic-athletics.txt
5. At Londonderry High School, the Lancer Marching Band (about 180 students) is part of a full-year, one-credit band course, "Band - Concert and Marching," whose requirements include marching band and color guard, rehearsals and performances outside school hours, and "full eligibility"; so a homeschooled student who wants to march would ask to take that course under policy JJJ.
   - citation: Londonderry High School Program of Studies 2026-2027 (course H0100); LHS Music page
   - source: https://docs.google.com/document/d/1xhfCtRh-RYT1-wNp1cB7SpkY2LMxTtZjYb0A5GF46to/edit
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Program text: "Band - Concert and Marching H0100 09-12 FY credits: 1.0 ... Out of school time is required for both rehearsals and performances including football halftime shows ... Participation in the World Famous Lancer Marching Band and Color Guard is a course requirement ... Full eligibility (academic and otherwise) required." Music page: "the world-famous Lancer Marching Band ... which currently has 180 students." The link to JJJ's course-request process is our reading; no source addresses homeschoolers in the band. Raw: raw/daily/lhs-program-of-studies-2026-27.txt; raw/daily/lhs-music.txt
6. Londonderry's Home Education page (a PDF dated August 2024, still posted on November 15, 2026) tells parents planning a home school program that they "must provide a letter" to the district, using forms to start, end or complete a program, sent to the superintendent's office at 6A Kitty Hawk Landing; since July 1, 2026, state law requires no declaration except to use district programs or when withdrawing from a public school.
   - citation: Londonderry School District, Home Education page ("Home Education for LSD.pdf"); library topic home-education-rules 1
   - source: https://www.londonderry.org/family/home-education
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: PDF text: "Any parent(s) / legal guardian(s) planning on establishing a home school program must provide a letter to the appropriate school district. Please select the link below for the appropriate document. Starting a Home Education Program; Termination of a Home Education Program; Completion of a Home Education Program." PDF metadata: created 2024-08-12. Answers the P15.3 premise; the state rule is the library's. Raw: raw/daily/lsd-home-education.txt; raw/daily/lsd-home-education-for-lsd.txt
7. Londonderry's posted home education policy IHBG (adopted November 12, 2024) still describes the rules in force before July 1, 2026: written notice within 5 days to a chosen "participating agency," an annual evaluation, a free state or local test given by the district (passing at the 40th percentile) when the superintendent is the participating agency, and a portfolio review for which the district may charge a fee.
   - citation: Londonderry School Board policy IHBG, Home Education Instruction, sections A–C
   - source: https://drive.google.com/file/d/1Xgp4pzpP3ZqPQLhu5XYCz3X4R2WN7Mt9/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "parents/guardians are required to provide for an annual educational evaluation"; "If the evaluation method is a state or local assessment provided by the District ... the District will not charge a fee for providing or administering the test. Reasonable academic proficiency is deemed demonstrated if the composite results place the child at or above the fortieth percentile"; "the parent/guardian may request the District to perform a portfolio review, for which the District may charge a fee." RSA 193-A:6 (evaluations) was repealed July 1, 2026 (library home-education-rules 2); home-educated students may now take the statewide assessment and PSAT through their district (library home-education-rules 8). No 2026 revision of IHBG was found in the minutes read. Raw: raw/daily/lsd-policy-ihbg-home-education.txt
8. Londonderry's October 31, 2026 enrollment report counts 129 home-educated students, up from 109 a year earlier; the superintendent told the board in October 2025 that this number includes only families who report to the district.
   - citation: Londonderry School District Enrollment Report, 10/31/2026; Londonderry School Board minutes, October 7, 2025, item 7.1
   - source: https://drive.google.com/file/d/116qs3ppaVWUuaXWMdq9KRP-wVLPSH3Sv/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Report text: "Home Education 129 109." Minutes text: "Mr. Slater asks for clarification about the home educated. Mr. Black states that the number is the only ones that self-report to us." Raw: additional-data/raw/districts/batch-4/londonderry-enrollment-2026-10-31.txt; raw/daily/minutes/sb-2025-10-07.txt

## district-family-communication: How Londonderry Sends Closing, Delay and Emergency Notices

- kind: local
- question_type: local_practice
- description: How schools reach families: parent portals, grade tracking, emergency notices, and translation and interpreting

1. Londonderry announces school closings and delays through SchoolMessenger calls, texts and emails, WMUR-TV (Channel 9), the district and school websites, and a recorded message on the district's "School Announcement Line" (603-432-6920, then 9).
   - citation: Londonderry School District, Closings & Delays page
   - source: https://www.londonderry.org/family/closings-delays
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "WMUR TV Channel 9 ... School Messenger Notification System (email, text and voice message) ... District and School Websites ... Call the District Office at 432-6920 and select 9 which is the 'School Announcement Line'." Raw: raw/daily/lsd-closings-delays.txt
2. To get Londonderry's SchoolMessenger alerts by text, a parent must opt in by texting YES to the short code 67587 (STOP opts out); the SchoolMessenger app or website lets families update phone numbers and email using the email address on file, and carrier charges are not reimbursed.
   - citation: Londonderry School District, Closings & Delays page, "Signing up for SMS (text) Alerts"
   - source: https://www.londonderry.org/family/closings-delays
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "you must 'opt-in' to receive important information from the district via our SMS text messaging service. Messages you receive will come from our 'short code', 67587. To opt-in simply text YES to 67587"; "You will need to register using the email address we have on file for you." Messages cover "school closings and delays, attendance alerts, and other general time sensitive information." Raw: raw/daily/lsd-closings-delays.txt
3. In January 2026 Londonderry said it sends closing and delay alerts by SchoolMessenger text, email and call to all families and staff at about 5 a.m., using contacts synced from its student information system, and at the same time posts them to its news blog (which anyone can subscribe to by email), its website, its official Facebook page, WMUR and its school Facebook groups.
   - citation: Londonderry School News, "Where to Find Londonderry Schools Cancellation/Delay Alerts," January 7, 2026
   - source: https://news.londonderry.org/2026/01/07/where-to-find-londonderry-schools-cancellation-delay-alerts/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Post text: "We use the School Messenger system to text, email, and call all student families and staff at about 5am. Active family contacts are synced through our Student Management System"; "Anyone in the community can subscribe to the blog to get the email notifications"; "We replicate this information in these four areas ... in the event that one of the areas has a glitch ... we did have a glitch with WMUR this morning ... If you suspect a glitch in the future, it is worth checking out the other areas." Raw: raw/daily/news-2026-01-07-where-to-find-alerts.txt
4. Londonderry's bus regulations say storm closing and delay announcements begin at about 5:30 a.m.; the high school handbook says that if school is cancelled after a delay has been announced, a second notice comes by 7:45 a.m.
   - citation: Londonderry School Board policy EEA-R, "The Role of Students and Parents," item 6; LHS Student Handbook, "School Cancellations, Delays, Emergency Closings"
   - source: https://drive.google.com/file/d/1QAhZD0kNBVPsRr1KmkbG5FOcmuILeM2_/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "In inclement weather announcements regarding the closing of schools or delayed opening begin at approximately 5:30 a.m." LHS text: "if school is canceled after a delayed opening announcement, a second notice will be given by 7:45 AM via the same media." The January 2026 blog post says about 5 a.m. (fact 3). Raw: raw/daily/lsd-policy-eea-r-bus-regulations.txt; raw/daily/lhs-student-handbook.txt
5. In 2025-26, Londonderry sometimes announced storm decisions well before morning: the January 26, 2026 closing was posted about 2:30 p.m. the day before, the March 6 delay about 8:20 p.m. the night before (promising any cancellation "by 6am"), and the March 6 closing that replaced it at about 5:50 a.m. (derived from post times).
   - citation: Londonderry School News posts of January 25, March 5 and March 6, 2026
   - source: https://news.londonderry.org/2026/03/05/2-hr-delay-friday-3-6-no-am-k-or-leep/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: **Derived:** publication times in the pages' metadata (UTC) converted to Eastern Standard Time: 2026-01-25T19:29:25Z = 2:29 p.m.; 2026-03-06T01:19:45Z = 8:19 p.m. March 5; 2026-03-06T10:51:22Z = 5:51 a.m. These are blog post times; SchoolMessenger messages may have gone out at slightly different times. March 5 text: "if we need to cancel the whole school day, we will send out a follow up message by 6am." Raw: raw/daily/news-2026-01-25-no-school.html; raw/daily/news-2026-03-05-delay-no-am-k.html; raw/daily/news-2026-03-06-no-school.html
6. Londonderry's 2026-27 Matthew Thornton and South handbooks also list radio stations (WLLO 102.9 AM, WBZ 1030 AM, WGIR 610 AM, WDER 1320 AM), the district's education channel LEO-21 and a school Twitter account for closings, and say email "blasts" can go to a single classroom, grade or bus route when buses are delayed; families keep their email current in the Aspen parent portal.
   - citation: Matthew Thornton Handbook 2026-27, "Cancellation of School" and "Communication"; South Student/Parent Handbook 2026-2027
   - source: https://mt.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Handbook text: "Emails can be sent by classroom or grade level when applicable, or by bus route in the event of delays ... If you would like to receive these communications, please update Aspen with your current email address"; "Radio Stations WLLO (Londonderry) 102.9 AM WBZ (Boston) – 1030 AM WGIR (Manchester) – 610 AM WDER (Derry) – 1320 AM; TV Stations LEO-21 (Londonderry) – Channel 21 WMUR-TV (Manchester) – Channel 9." The LHS handbook names WZID (95.7 FM). The district's own closings page lists only WMUR, SchoolMessenger, the websites and the phone line. Raw: raw/daily/mt-student-handbook.txt; raw/daily/south-student-handbook.txt
7. Each year Londonderry elementary families get an emergency card to check and return, with contacts, cell phone numbers and health information; changes go into the Aspen parent portal or on the card, and custody restrictions must be given to the office in writing.
   - citation: Matthew Thornton Handbook 2026-27, "Health: Emergency Cards" and "Parent/Guardian Transporting Student(s)"
   - source: https://mt.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Handbook text: "At the start of each school year, each child will bring home a copy of the emergency information that is on file with the school ... Contact information is especially important. Be sure to include cell phone numbers"; "The office must be informed in writing of situations of legal custody restricting individuals from dismissing or seeing your child." The LHS handbook: "Emergency cards are sent home the first day of school." Raw: raw/daily/mt-student-handbook.txt; raw/daily/lhs-student-handbook.txt
8. In September 2026 Londonderry's superintendent said the district's "multi-tool approach" to family communication was working but that its Communication Committee was surveying staff after seeing vendors combine all communication in one app; the district does not yet have a "virtual phone" that lets staff call and text parents without a personal phone, and no decision had been made.
   - citation: Londonderry School Board minutes, September 1, 2026 (item 10.4) and September 15, 2026 (item 8.3); Communication Committee page
   - source: https://drive.google.com/file/d/1LiN8AturKtjnoGrv0toAO4045nVApuA7/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "The Communication Committee went to a conference in the Spring and realized school and vendors were attempting to streamline all communication into a single application. We have not made any decisions ... One capability we do not have right now is a 'virtual phone' ... He believes our multi-tool approach is working but wants to gather more feedback." Committee page: "Anyone is welcome to attend." Raw: raw/daily/minutes/sb-2026-09-01.txt; raw/daily/minutes/sb-2026-09-15.txt; raw/daily/lsd-communication-committee.txt

## district-safety-and-security: Londonderry's ALICE Drills, Alarms and Emergency Notices

- kind: local
- question_type: local_practice
- description: Building security, visitor rules, drills and emergency plans, and school security grants

1. The Londonderry School District calls itself an ALICE-certified district: in a threat it uses the Alert, Lockdown, Inform, Counter, Evacuate (ALICE) protocol, and its staff have been trained in ALICE since 2022-23; schools also practice drills such as lockdown, shelter in place, reverse evacuation, fire, controlled evacuation and (at South) drop, cover and hold.
   - citation: LHS Student Handbook, "ALICE Protocol"; Matthew Thornton Handbook 2026-27 and South Handbook 2026-2027, "Security"
   - source: https://docs.google.com/document/d/1nafKoNciyLSTgXMhYMPekj5QpyX9h8KXZs9YobQw84c/edit
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: LHS text: "The Londonderry School District is an ALICE certified district. In the event of a threat to the safety of the school community, we will initiate the Alert, Lockdown, Inform, Counter, Evacuate (ALICE) protocol." Matthew Thornton: "Shelter in Place, Clear Hallways, Reverse Evacuation, Fire Drills, Controlled Evacuations, and ALICE drills ... Starting in the 2022-23 School Year, our District staff is trained in the ALICE response to a Violent Critical Incident." South: "ALICE/Lockdown, Reverse Evacuation, Fire Drills, Controlled Evacuations, and Drop Cover & Hold." Raw: raw/daily/lhs-student-handbook.txt; raw/daily/mt-student-handbook.txt; raw/daily/south-student-handbook.txt
2. Londonderry Middle School's handbook asks parents not to call the school, and not to call or text their child's cell phone, during ALICE drills and emergencies, because staff need the lines for police and fire and calls could interfere; students are told to turn off their devices.
   - citation: Londonderry Middle School Student Handbook 2026-2027, emergency drills
   - source: https://lms.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Handbook text: "Because school personnel need access to the appropriate agencies (police, fire, etc), parents are asked to please refrain from calling the school. Additionally, we request parents do not call/text their child's cell phone during emergencies and/or drills, as this could interfere with emergency procedures. To ensure student safety, students will be asked to shut off all electronic devices." The LHS handbook says "School leadership will work to communicate timely information in clear and direct language and with specific guidance as soon as possible." No time limit for telling families was found. Raw: raw/daily/lms-student-handbook.txt; raw/daily/lhs-student-handbook.txt
3. On September 2, 2026 a student set off an Alertus alarm button at Matthew Thornton School at about 10:25 a.m.; staff and students followed ALICE, Londonderry police arrived within minutes and confirmed a false alarm, every student and staff member was accounted for within 30 minutes, and the district posted an account for families the same day.
   - citation: Londonderry School News, "False Alarm: Alertus Button Activated at Matthew Thornton," September 2, 2026
   - source: https://news.londonderry.org/2026/09/02/false-alarm-alertus-button-activated-at-matthew-thornton/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Post text: "At approximately 10:25 am this morning, a student falsely activated an ALERTUS button at Matthew Thornton School. All of the staff and students relied on their ALICE training ... Within minutes, the Londonderry Police Department was on campus ... Within 30 minutes, full accountability of all students and staff was achieved ... Counselors and administrators will continue to be available." Alertus is a panic-button and alert-beacon system. Raw: raw/daily/news-2026-09-02-false-alarm-mt.txt
4. Londonderry's Emergency Operations Planning committee of school administrators, police and fire debriefs every incident; after the September 2, 2026 false alarm it met on September 3, and the superintendent told the board police had praised the response.
   - citation: Londonderry School Board minutes, September 15, 2026, item 8.1; Joint Press Release, Londonderry Police Department and Londonderry School District, September 4, 2025
   - source: https://drive.google.com/file/d/1YDWjPE_x7r4VJRecGVWRbAo2rgMauzek/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "Mr. Black talks the meeting the EOP committee had on 9/3 to debrief the false alarm event at MT ... LPD was at the meeting and praised what how things were handled." Press release: "It is customary for our Emergency Operations Committee (a partnership of School Administrators, the Londonderry Police Department, and the Londonderry Fire Department) to debrief all incidents after they occur." Raw: raw/daily/minutes/sb-2026-09-15.txt; raw/daily/news-2025-09-04-joint-press-release-lpd-pdf.txt
5. After a water leak set off an Alertus button at Londonderry High School on August 27, 2025, the police chief and superintendent issued a joint press release describing backup communication with police (direct calls to dispatch, shared radios and an Alertus app) and a police-station alarm beacon that failed to sound that day but worked when retested.
   - citation: Joint Press Release on August 27th Alertus False Alarm at Londonderry High School, September 4, 2025
   - source: https://news.londonderry.org/wp-content/uploads/2025/09/Joint_Press_Release_9_4_2025.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Release text: "Within seconds of the water leak tripping one of our Alertus buttons at LHS, school staff were able to identify it was a false alarm. Two phone calls from LHS went directly to dispatch ... our School Resource Officers also received direct communication from the school system through shared radios and an Alertus App"; "the Alertus beacon at the Londonderry Police Department did not trigger an alarm at dispatch ... Yesterday afternoon we tested the beacon at the LPD from two separate schools, and it did work successfully." Raw: raw/daily/news-2025-09-04-joint-press-release-lpd-pdf.txt
6. In September 2026 Londonderry's superintendent reported that an outside vendor had certified every Alertus beacon and button as working (including at the police department), reunification plans had been updated, ALICE training now included advisors and head coaches for after-school hours, doors, windows and stairwells would be numbered outside for responders, and a state grant would pay to 3D-map every school.
   - citation: Londonderry School Board minutes, September 1, 2026, item 10.1 Safety Updates
   - source: https://drive.google.com/file/d/1LiN8AturKtjnoGrv0toAO4045nVApuA7/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "In August, our staff worked with an outside vendor to certify and check that all beacons and Alertus buttons are functional within all of our schools. All are working as well as LPD. The reunification plans have been updated and reorganized ... We have expanded ALICE training this year to include advisors and head coaches ... We will be numbering our doors, windows and stairwells from the outside for first responders. There is a state grant to 3D Map all our schools this year." Raw: raw/daily/minutes/sb-2026-09-01.txt
7. At Londonderry High School all injuries are reported to the school nurses, who give first aid and notify parents; the board's safety policy EB assigns first aid for accidents or sudden illness to the school nurse and makes each principal responsible for a school safety program, including emergency procedures.
   - citation: LHS Student Handbook, "Health Services"; Londonderry School Board policy EB, Safety Program (amended August 25, 2015)
   - source: https://drive.google.com/file/d/16HtLMM-M2XoTSSqV_9gtg1ih5Gsf0SI9/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Handbook text: "All injuries must be reported to the nurses. First aid treatment will be administered and parents notified." Policy text: "Providing, through the services of the school nurse, first aid care for students in case of accident or sudden illness"; "Each principal shall be responsible for the supervision of a safety program for his/her school." Nurse staffing is agent 4's area. Raw: raw/daily/lhs-student-handbook.txt; raw/daily/lsd-policy-eb-safety-program.txt
8. Londonderry elementary visitors enter through a buzzer at the main entrance, give their name and the reason for the visit, and wear a badge; cameras watch the entrances, and doors are locked through the school day (7:00 a.m. to 3:30 p.m. at North).
   - citation: 2026-27 handbooks of North, Matthew Thornton and South, "Security / School Safety / Visitations"
   - source: https://north.londonderry.org/information/student-handbook
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: North text: "All school doors will be locked daily from 7:00am – 3:30pm. Visitors will be allowed to enter the main entrance via a buzzer system ... Surveillance cameras are placed near the entrances ... Visitor badges or passes will be provided." Matthew Thornton: "locked daily from 8:42 to 3:13." South: "All doors to the school will be locked throughout the school day." Raw: raw/daily/north-student-handbook.txt; raw/daily/mt-student-handbook.txt; raw/daily/south-student-handbook.txt

## district-technology-and-phones: Londonderry's Chromebooks, Laptops and Student Data Privacy

- kind: local
- question_type: local_practice
- description: Devices students use, screen time, technology rules, and phone and personal device policies

1. Londonderry students' devices vary by school: North classrooms share Chromebook carts and iPads, Matthew Thornton gives each student in grades 2–5 a Chromebook in class, every middle schooler is issued a Chromebook to carry home daily and return in June, and Londonderry High School is a one-to-one laptop school whose laptop lasts all four years and is used for standardized tests.
   - citation: North and Matthew Thornton 2026-27 handbooks, "Computer Education & Technology"; Londonderry Technology, Chromebook Program (LMS); LHS Student Handbook, "School Laptops"
   - source: https://tech.londonderry.org/middle-school-services/chromebook-program
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: North: "Each classroom has access to Chromebook carts as needed ... have access to iPads." Matthew Thornton: "Each classroom, in grades 2-5, has one-to-one Chromebooks to use with the curriculum." LMS page: "At the beginning of each year all LMS students are issued a Chromebook ... bringing it home at the end of the day ... required to turn them in at the close of the school year." LHS: "Londonderry High School is a 1:1 Laptop school ... The laptop will need to last for the entirety of your high school career and must be used for all standardized tests." Raw: raw/daily/north-student-handbook.txt; raw/daily/mt-student-handbook.txt; raw/daily/tech-lms-chromebook-program.txt; raw/daily/lhs-student-handbook.txt
2. Londonderry's middle school Chromebooks are managed by district IT staff, get software and updates from the district's cloud, come with antivirus and website-blocking software, are set up for the digital SAT, PSAT and state tests, and may connect only to the school's designated wireless network, not a private network or cellular hotspot, at school.
   - citation: Londonderry Technology, Chromebook Program; Londonderry Middle School Student Handbook 2026-2027, technology section
   - source: https://tech.londonderry.org/middle-school-services/chromebook-program
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "Receive necessary software and updates over the network & Internet from the School District's Cloud. Include an anti-virus program & software that blocks school-inappropriate websites"; "Are set up to participate in digital SATs, PSATs, & State Assessment testing." Handbook: "Students are permitted to access only the school's wireless network designated for use with a chromebook. Students may not use any private network or cellular connection." Raw: raw/daily/tech-lms-chromebook-program.txt; raw/daily/lms-student-handbook.txt
3. Londonderry middle school families pay a $15 annual Chromebook insurance fee (online, by check, or waived with an approved fee waiver for families eligible for free or reduced-price meals) and complete the Chromebook acceptable use forms in the Aspen parent portal before school starts.
   - citation: Londonderry Technology, Chromebook Program, "Requirements for Chromebooks"
   - source: https://tech.londonderry.org/middle-school-services/chromebook-program
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "An annual Chromebook Insurance Fee of $15 must be paid using one of the three options"; "A laptop Fee Waiver form ... is available for families eligible for the USDA's Free/Reduced Meals program"; "Chromebook acceptable use forms are part of a students back to school forms that must be completed in the Aspen Parent Portal prior to the start of school." Raw: raw/daily/tech-lms-chromebook-program.txt
4. Londonderry's internet policy JICL (adopted May 13, 2025) tells students they have no expectation of privacy on district computers, files, email, internet logs and other electronic data, requires a filter on every district computer that blocks obscene or pornographic images, and requires students to sign an acceptable use agreement; its regulation JICL-R reserves the district's right to "monitor all activity."
   - citation: Londonderry School Board policy JICL, School District Internet Access for Students; JICL-R, Acceptable Internet Use Procedures
   - source: https://drive.google.com/file/d/1U7XAH-cQIo1Q7_Jv2EwGwodFpKB4bY0Y/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: JICL text: "Students are hereby notified that there is no expectation of privacy on district computers, computer files, email, internet usage logs, and other electronic data. The Superintendent or designee shall ensure that all District computers with Internet access have a technology protection measure that prevents access to visual depictions that are obscene or pornographic." JICL-R: "The District reserves the right to: 1. Monitor all activity. Notwithstanding FERPA and other related laws, students have no expectation of privacy regarding their use on the school district computer network." State limits on surveillance software and on app makers' use of student data are in library nh-student-records-and-privacy 4 and 7. Raw: raw/daily/lsd-policy-jicl-internet-access.txt; raw/daily/lsd-policy-jicl-r-acceptable-use.txt
5. Londonderry requires a signed data privacy agreement (DPA) before any digital tool is used with students, and its "LSD Digital Tools" website lists approved, recommended and prohibited apps by grade and subject, with a DPA lookup and a digital learning specialist for each level.
   - citation: LSD Digital Tools website, home page; Ed Tech, Privacy & Security page
   - source: https://digitaltools.londonderry.org
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "Our district utilizes many digital tools. When using digital tools, a data privacy agreement (DPA) is required. This website lists all of our district approved, recommended, and prohibited applications." Privacy page: "Approval status for applications that collected personal identifiable information. Data Privacy Agreement Lookup." The lists themselves load in a browser and were not read. Raw: raw/daily/digitaltools-home.txt; raw/daily/edtech-privacy-security.txt
6. Londonderry's Ed Tech "Privacy & Security" page says the district manages students' personally identifiable information under FERPA and COPPA, links the federal and state privacy laws (including RSA 189:65 to 189:68-a and the breach-notice law RSA 359-C:20), and posts its acceptable use policy, student records policies, a data breach response plan and the NH Department of Education's minimum privacy and security standards.
   - citation: Londonderry School District, Ed Tech – Privacy & Security
   - source: https://edtech.londonderry.org/privacy-security
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "The Londonderry School District oversees a wide range of information about students. The district manages personally identifiable information (PII) about students in accordance with the federal laws known as FERPA and COPPA"; "Londonderry School District Policies and Guidelines for Student Data and Security: Acceptable Use Policy; Student Education Records Information; ... Data Breach Response Plan; Minimum Standards for Privacy and Security." Raw: raw/daily/edtech-privacy-security.txt
7. Londonderry's posted data breach response plan calls for a yearly updated directory of district devices, installed software and staff with access; review of any new software or device by the superintendent; a prompt investigation of any breach; notice to affected New Hampshire residents "as soon as possible and without unreasonable delay"; and simultaneous notice to the state Attorney General.
   - citation: Londonderry School District, Data Breach Response (linked from the Privacy & Security page)
   - source: https://drive.google.com/file/d/166nruyK1HfAsTY7egKGmBCknjTH0UaWo/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Plan text: "The superintendent, or their designee, will create an annually updated data directory that will include: i. Computing devices purchased by the district, ii. Software that is installed on district devices, iii. Staff members with access to district devices"; "Notice shall be made as soon as possible and without unreasonable delay"; "notice of the breach will be simultaneously sent to the New Hampshire Attorney General's office." The plan is undated. Raw: raw/daily/lsd-data-breach-response-plan.txt
8. In May 2026 the Londonderry School Board approved buying 375 student laptops at $659.00 each, 375 Chromebooks at $336.90 each, 145 teacher laptops at $879.00 each and 11 interactive whiteboards at $1,389.90 each.
   - citation: Londonderry School Board minutes, May 19, 2026, item 7.2 Purchase Request
   - source: https://drive.google.com/file/d/1PPfNBpcpDRZ5FxCPL8RXRbNn8rMqWm0L/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Minutes text: "approve the purchase of 11 Interactive white boards from Insight at $1389.90, 375 Student Laptops from Y&S at $659.00, 145 Teacher laptops from Connections at $879.00 and 375 Chromebooks from Y&S at $336.90 ... The motion passed by a vote of 5-0." Raw: raw/daily/minutes/sb-2026-05-19.txt
9. No annual data and privacy governance plan (required of every New Hampshire district by RSA 189:66, V) was found on Londonderry's privacy pages or in the 25 board minutes from 2025 and 13 from 2026 that were searched; the posted breach plan and NH DOE standards cover two of the plan's required parts.
   - citation: Londonderry School Board minutes, 2025 and January–October 2026 (searched); Ed Tech – Privacy & Security page
   - source: https://www.londonderry.org/school-board/minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: **Derived** from a search of the minutes' text for "governance," "data privacy," "privacy plan" and "cyber," which found nothing; a plan may exist without being in these sources. The plan's required contents are in this file's nh-student-records-and-privacy 1 below. Raw: raw/daily/edtech-privacy-security.txt; minutes searched in the scratchpad (cited ones in raw/daily/minutes/)

## district-board-and-public-input: Watching Londonderry School Board Meetings

- kind: local
- question_type: governance_money
- description: School board elections and meetings, how residents and tuition towns can give input, and remote or recorded meetings

1. The Londonderry School Board usually meets at 7:00 p.m. in the Londonderry High School cafeteria or library; meetings are shown live on local Cable Access Channel 8 and streamed on the district's YouTube channel.
   - citation: Londonderry School District, School Board Schedule page; 11-10-2026 Londonderry School Board Agenda post
   - source: https://www.londonderry.org/school-board/schedule
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "School Board Meetings are at 7:00 PM at the Londonderry High School in the LHS Cafeteria unless otherwise stated. Public meetings are televised LIVE on Cable Access Ch. 8 and streamed on our YouTube Channel." Agenda post: "The meeting will also be broadcast on local Cable Access Ch. 8 as well as the District's YouTube Channel." Every 2026 minutes file read says the same. Raw: raw/daily/lsd-board-schedule.txt; raw/daily/news-2026-11-06-board-agenda.txt
2. The Londonderry School District's working YouTube channel is @londonderryschooldistrict ("Londonderry SAU12"), linked from the district site's "School Board Videos" menu and its agendas; the Schedule page instead links @londonderryschools, which returned "404 Not Found" on November 15, 2026.
   - citation: YouTube, Londonderry School District channel; Londonderry Media – YouTube page; School Board Schedule page
   - source: https://www.youtube.com/@londonderryschooldistrict/streams
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: The district's media page lists separate channels for Moose Hill, North, Matthew Thornton, South, the middle school, the high school and Londonderry Athletics. The Schedule page link https://www.youtube.com/@londonderryschools gave HTTP 404. Raw: raw/daily/youtube-lsd-streams-tab.html; raw/daily/youtube-lsd-channel-lists.txt; raw/daily/lsd-media-youtube.txt; raw/daily/lsd-board-schedule.txt
3. Recordings of Londonderry School Board meetings stay on the district's YouTube channel; the 15 regular meetings streamed from January 27 to November 10, 2026 ran from 31 minutes to 2 hours 26 minutes, with a median of 1 hour 33 minutes, while the December 9 and 18, 2025 budget workshops ran 3 hours 49 minutes and 4 hours 7 minutes (derived; see table londonderry_school_board_video_length_2026).
   - citation: YouTube, Londonderry School District channel, Live (streams) tab
   - source: https://www.youtube.com/@londonderryschooldistrict/streams
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: **Derived** from the video lengths shown on the channel's Live tab (includes the April 7 board meeting and public hearing; excludes the 2-minute non-public opening, candidates night, the deliberative session, workshops and hearings). None of the 15 ran over 3 hours; two ran over 2 hours (October 6 and February 17). Video length includes any time before the meeting opens. Raw: raw/daily/youtube-lsd-channel-lists.txt; raw/daily/youtube-lsd-streams-tab.html
4. The Londonderry School Board's meeting videos have no chapter markers or written summary to jump to items; the November 10, 2026 recording (1 hour 51 minutes) has a blank description.
   - citation: YouTube, "School Board Meeting 11-10-26" watch page
   - source: https://www.youtube.com/watch?v=M9w5Bby0R5A
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page data: "shortDescription" empty; no chapter or marker data; "lengthSeconds":"6705". Only this one video was checked for chapters. Raw: raw/daily/youtube-lsd-watch-2026-11-10-board-meeting.html
5. Londonderry also posts short videos on single topics: segment-only recordings of the board's tax cap discussions (45 minutes from September 15 and 1 hour 7 minutes from October 6, 2026) and superintendent video newsletters of about 3 to 6 minutes, such as the fall 2026 Academic Update (3:31), Attendance (3:40) and Tax Cap (5:47) videos.
   - citation: YouTube, Londonderry School District channel, Videos tab
   - source: https://www.youtube.com/@londonderryschooldistrict/videos
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Channel listing: "School Board Tax Cap Discussion only from 10-6-26 | 1:07:15"; "School Board Tax Cap Discussion on 9-15-26 | 45:14"; "TAX CAP: PART ONE | 4:11"; "TAX CAP; PART TWO | 4:34"; "Fall video newsletter: Academic Update 2026 | 3:31"; "Fall Video Newsletter: Attendance 2026 | 3:40"; "Fall Video Newsletter: Tax Cap 2026 | 5:47". Raw: raw/daily/youtube-lsd-channel-lists.txt; raw/daily/youtube-lsd-videos-tab.html
6. Londonderry posts each board agenda on its news blog a few days before the meeting (the November 10, 2026 agenda went up November 6), and anyone may subscribe to the blog by email; written minutes, which summarize each agenda item in four to seven pages, are posted to the board's Minutes folder about two to four weeks after a meeting (the October 20 minutes on November 12, the September 15 minutes on October 14).
   - citation: Londonderry School News, "11-10-2026 Londonderry School Board Agenda"; School Board Minutes folder listing
   - source: https://www.londonderry.org/school-board/minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: **Derived** lag from the dates in the Drive folder listing ("10-20-2026 Minutes.pdf | Nov 12"; "9-15-2026 Minutes.pdf | Oct 14"; "9-1-2026 Minutes.pdf | Sep 18"). Agenda post dated November 6, 2026. The 13 sets of 2026 minutes read run 4 to 7 pages (the last page often only the signature). Raw: raw/daily/news-2026-11-06-board-agenda.txt; raw/daily/lsd-board-minutes.txt; raw/daily/minutes/sb-2026-09-15.txt
7. The Londonderry School Board's 2026-27 calendar (dated November 12, 2026) has regular meetings about twice a month, the budget presented to the board on November 24 at 6 p.m., budget workshops on December 3, 10 and 17 and January 7 at 6 p.m., the budget and bond hearing on January 14, the deliberative session on February 5 and the election on March 9, 2027.
   - citation: Londonderry School District, 2026-2027 School Board Meeting Calendar
   - source: https://www.londonderry.org/school-board/schedule
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Calendar text: "November 10 Regular Meeting; 24 Budget Presented to the Board - 6PM; December 3 Budget Workshop - 6PM; 10 Budget Workshop - 6PM; 17 Budget Workshop and Regular Meeting - 6PM; January 7 Budget Workshop and Regular Meeting - 6PM; 14 Budget Hearing/Bond Hearing; ... February 5 Deliberative Session ... March ... 9 Election Day; 16 School Board Reorganization"; "Meetings are at 7:00 PM in the LHS Cafe unless otherwise noted." Raw: raw/daily/lsd-board-calendar-2026-27.txt
8. Under Londonderry's policy BEDH (adopted March 25, 2026), the board holds a public comment period of at least 30 minutes at every meeting except emergency or non-public-only meetings, usually in the first half, with five minutes per speaker; people who can't attend may send one signed written comment, which is attached to the minutes.
   - citation: Londonderry School Board policy BEDH, Public Comment and Participation at Board Meetings
   - source: https://drive.google.com/file/d/1jVW2jNePSiqKUOG-aOZ3hnqnNuuiaQ3L/view
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Policy text: "The Board will generally schedule the public comment period in the first half of its meetings. The Board will provide a minimum of thirty minutes to hear public comments"; "Individual speakers will be allotted five minutes per person"; "The Board will provide opportunity for written public comments for people unable to attend the meeting. Written comments ... will be attached to the minutes. Anonymous written comments will not be accepted." Raw: raw/daily/lsd-policy-bedh-public-comment.txt
9. The district's link for Londonderry's local access television (LACTV) page returned "page not found" on November 15, 2026; the town's "Watch" page lists live streams and on-demand pages for its cable channels CTV-20, LEO-21 and GOV-22 and a town YouTube channel.
   - citation: Town of Londonderry, Watch page
   - source: https://www.londonderrynh.gov/577/Watch
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Londonderry
   - note: Page text: "Stream CTV-20; Stream LEO-21; Stream GOV-22; Stream DIG-170; CTV-20 OnDemand; LEO-21 OnDemand; GOV-22 OnDemand; YouTube - Government; YouTube - Cable Access." The district's link https://www.londonderrynh.gov/cable/pages/local-access-television-lactv gave the town site's 404 page. No source read ties the board's "Channel 8" to one of these channel names. Raw: raw/daily/town-lactv-watch.txt

## nh-student-records-and-privacy: New Hampshire Student Records and Privacy Law

- kind: rule
- question_type: rules
- description: NH's own student privacy rules: records access, directory information, tracking and surveillance limits, online services and record retention.

1. New Hampshire law requires every school district to have a data and privacy governance plan, updated and presented to the school board each year, that inventories all software, digital tools and extensions (with their provider, purpose, privacy statement and terms of use), checks them against the Department of Education's standards, sets access and acceptable use policies, includes a breach response plan and requires service providers to meet the standards.
   - citation: RSA 189:66, V
   - source: https://gc.nh.gov/rsa/html/XV/189/189-66.htm
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Statute text: "Each local education agency shall develop a data and privacy governance plan which shall be presented to the school board for review and approval by June 30, 2019. The plan shall be updated annually and presented to the school board. The plan shall include: (a) An inventory of all software applications, digital tools, and extensions ... (d) A response plan for any breach of information. (e) A requirement for a service provider to meet or exceed standards for data protection and privacy." Adds to the library topic of the same slug. Raw: raw/daily/rsa-189-66.txt
2. The NH Department of Education's "Minimum Standards for Privacy and Security of Student and Employee Data," which every district must follow under RSA 189:66, V, are drawn from the federal NIST SP 800-171 security controls and cover access control, staff training, audit logs, configuration, sign-in and passwords, incident response, maintenance, media protection, personnel and physical security, risk and security assessment, and system protection.
   - citation: NH Department of Education, Minimum Standards for Privacy and Security of Student and Employee Data (as posted by the Londonderry School District)
   - source: https://drive.google.com/file/d/1d7pGEjxniDePvKdNxhG-dTpnB3QRFesq/view
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Document text: "This document defines minimum standards ('Standards') for the privacy and security of student and employee information for Local Education Agencies ('LEA') that the Department is required to establish according to ... RSA 189:66, V"; "All LEAs under the purview of the New Hampshire Department of Education are required to implement these Standards"; "These Standards have been developed from a subset of basic and derived security requirements from National Institute of Standards and Technology Special Publication 800-171 Revision 1." Copy from Londonderry's privacy page; undated. Raw: raw/daily/lsd-minimum-standards-privacy-security.txt

## londonderry_morning_bus_pickup_span_2026_27: Scheduled Morning Pickup Windows on Londonderry's 2026-27 Bus Routes (minutes, derived)

- unit: number (minutes)
- period: 2026-27 school year route sheets (updated August 25 to September 14, 2026); year: 2027
- source: Londonderry School District, 2026-2027 Regular Ed Bus Transportation Bus Routes (Take In sheets) — https://drive.google.com/drive/folders/14coaZZnz7gGFFlqdX_zb5jRGZ-zLo9v6
- as_of: 2026-11-15
- raw: raw/daily/derived-bus-route-times-2026-27.csv
- topic: district-transportation
- place: district Londonderry
- note: **Derived.** Value = minutes from a route's first scheduled pickup to its last, for the route with the longest window at that school; the Note gives the number of routes, the range of first and last pickup times and the median window. The sheets give no arrival time at school, so these are not full ride times; a child picked up first rides at least this long. Scheduled, not measured. Three pages were image-only and read from rendered images. Stops (house numbers) were not kept.

| Place | Trip | Value | Note |
|---|---|---|---|
| Londonderry | South Londonderry Elementary, morning (school starts 8:42) | 27 | 10 routes (13–22); first pickups 7:56–8:10, last pickups 8:18–8:28; median 18 |
| Londonderry | North Londonderry Elementary, morning (school starts 8:42) | 27 | 12 routes (1–12); first pickups 7:56–8:15, last pickups 8:12–8:27; median 18 |
| Londonderry | Matthew Thornton Elementary, morning (school starts 8:42) | 23 | 15 routes (23–37); first pickups 7:56–8:15, last pickups 8:16–8:26; median 13 |
| Londonderry | Londonderry Middle and High School combined, morning (LHS starts 7:20, LMS 7:44) | 27 | 37 routes (1–37); first pickups 6:35–6:52, last pickups 6:49–7:08; median 17. Hooksett route 38 not included |

## londonderry_school_board_video_length_2026: Length of Londonderry School Board Meeting Videos, 2025-26 and 2026 (minutes)

- unit: number (minutes)
- period: Meetings streamed December 9, 2025 to November 10, 2026; year: 2027
- source: YouTube, Londonderry School District channel (@londonderryschooldistrict), Live tab — https://www.youtube.com/@londonderryschooldistrict/streams
- as_of: 2026-11-15
- raw: raw/daily/youtube-lsd-channel-lists.txt
- topic: district-board-and-public-input
- place: district Londonderry
- note: Value = video length shown on the channel, rounded down to whole minutes (the Note gives the exact length). Lengths include any time before the meeting is called to order. Regular meetings in 2026: median 93 minutes (derived from the 15 regular meetings listed, January 27 to November 10, 2026).

| Place | Meeting | Value | Note |
|---|---|---|---|
| Londonderry | School Board Budget Workshop, December 9, 2025 | 228 | 3:48:46 |
| Londonderry | School Board Budget Workshop, December 18, 2025 | 246 | 4:06:51 |
| Londonderry | School Board Budget Workshop, January 8, 2026 | 98 | 1:38:11 |
| Londonderry | Budget Hearing/Bond Hearing, January 15, 2026 | 96 | 1:36:56 |
| Londonderry | School Board Meeting, January 27, 2026 | 55 | 55:56 |
| Londonderry | School Deliberative Session, February 7, 2026 (video title date) | 91 | 1:31:41 |
| Londonderry | School Board Meeting, February 17, 2026 | 122 | 2:02:31 |
| Londonderry | School Board Meeting, March 25, 2026 | 103 | 1:43:46 |
| Londonderry | School Board and Public Hearing Meeting, April 7, 2026 | 99 | 1:39:16 |
| Londonderry | School Board Meeting, April 21, 2026 | 71 | 1:11:46 |
| Londonderry | School Board Meeting, May 5, 2026 | 73 | 1:13:16 |
| Londonderry | School Board Meeting, May 19, 2026 | 80 | 1:20:51 |
| Londonderry | School Board Meeting, June 23, 2026 | 67 | 1:07:36 |
| Londonderry | School Board Meeting, July 14, 2026 | 117 | 1:57:21 |
| Londonderry | School Board Meeting, July 27, 2026 | 30 | 30:41 |
| Londonderry | School Board Meeting, September 1, 2026 | 93 | 1:33:11 |
| Londonderry | School Board Meeting, September 15, 2026 | 98 | 1:38:50 |
| Londonderry | School Board Meeting, October 6, 2026 | 145 | 2:25:55 |
| Londonderry | School Board Meeting, October 20, 2026 | 85 | 1:25:56 |
| Londonderry | School Board Meeting, November 10, 2026 | 111 | 1:51:45 |

## For another file

- **Agent 1 (elementary) and agent 7 (buildings), P1.1 and P19.3, "new modular classrooms" at South:** the full-day kindergarten FAQ says the portables were moved from Moose Hill to **Matthew Thornton**, with three new classroom spaces created inside Matthew Thornton by August 10, 2026 (FAQ 6, additional-data/raw/districts/batch-4/londonderry-full-day-k-2026-project.txt). On August 5, 2025 the superintendent said "We could cancel the leases on the two modulars" (raw/daily/minutes/sb-2025-08-05.txt).
- **Agent 7, P6.3, P7.3 and P23.1 (district offices at Moose Hill):** January 27, 2026 minutes: "The District office is not going to Moose Hill that will remain LEEP and 3 and 4 year olds ... the district office is a joint venture with the town that is totally separate" (https://drive.google.com/file/d/1r95d7wf12Gge8AhWMx3gn5yJ6kv-9u-2/view). April 7, 2026 minutes: met "with the landlord at Kitty Hawk to discuss the move out plan ... The architect contract has been signed. A few small projects need to be completed the existing Town Hall" (https://drive.google.com/file/d/1n47pIQ-ccaOxv7ssQFln9c9Z7h1qGVOv/view). September 15, 2026 minutes: 3 and then 8 more paraprofessionals moved from Moose Hill to Matthew Thornton for K–1 needs through November (raw/daily/minutes/sb-2026-09-15.txt, item 8.2).
- **Agent 1, P3.2 and P22.2:** September 1, 2026 minutes: "At SS, 1st and 2nd grade are larger than we wanted, and we will take a look at this during the budget season" (raw/daily/minutes/sb-2026-09-01.txt). Kindergarten cap of 18 (this file, district-attendance-zones-and-transfers 2).
- **Agent 3 (CTE, P8.2):** LHS route 38 runs a morning shuttle picking up CTE students at LHS at 7:10 and dropping them at Alvirne (Hudson) at 7:30, and an "MST cte return bus" with Manchester School of Technology dismissal at 1:55 p.m. (route sheets, Drive folder above). The district accepted a state CTE transportation grant of up to $326,000 on March 25, 2025; June 3, 2025 minutes discuss Alvirne welding, Salem auto and Nashua biotech (2025 minutes folder, https://drive.google.com/drive/folders/1Cu0UYOUtBgDN0-enSgpxeLL42hVDdZe6).
- **Agent 6 (budget):** October 6, 2026 minutes: a tax cap would force cuts in discretionary programs "such as transportation, academics and athletics," a projected $2.0 million shortfall (raw/daily/minutes/sb-2026-10-06.txt). September 15, 2026: obligations exceeding the cap formula include the bus contract. December 18, 2025: STA contract up 3%; Hooksett tuition about $1,307,430, "in line with Pinkerton's tuition" (raw/daily/minutes/sb-2025-12-18.txt). The 2026-27 board calendar, workshop video lengths and policy BEDH (this file, district-board-and-public-input 3, 7–8) bear on P10.2 and P24.3.
- **Agent 2 (bus conduct, P4.3; phones, P17.2):** policy EEA (amended July 27, 2026) bans photographing or videoing students or drivers on buses; a first offense usually gets a warning and later ones 1 to 20 days off the bus; every bus records video and audio (raw/daily/lsd-policy-eea-transportation.txt). LMS handbook: phones may be used before 7:30 a.m. and after 2:30 p.m. outside the building (raw/daily/lms-student-handbook.txt).
- **Agent 4 (P11.2 meals):** the Chromebook fee waiver uses the free and reduced-price meal application (district-technology-and-phones 3).
- **Earlier towns:** nothing here contradicts an earlier town file. Like Nashua's and Concord's, Londonderry's IHBG and JJJ predate the 2026 home education and EFA access changes.

## Not retrieved

- https://lookerstudio.google.com/reporting/34fc43e3-ec08-43fa-805f-d419c5c09558 ("Londonderry Elementary Schools by Street"): the report is drawn by JavaScript; a plain request returned only the page title. A browser is needed to read street assignments.
- https://www.youtube.com/@londonderryschools (linked from the board Schedule page): HTTP 404 Not Found.
- https://www.londonderrynh.gov/cable/pages/local-access-television-lactv (linked from the district menu): the town site's 404 page. Which town channel carries "Cable Access Ch. 8" was not found.
- https://www.youtube.com/feeds/videos.xml?channel_id=UCvjc7DDgC4Q5Yrr14JUIdbg (channel feed): HTTP 404; the channel pages were used instead.
- digitaltools.londonderry.org lists of approved and prohibited tools and the DPA lookup: loaded by script; the static pages showed only headings.
- The SharePoint links in the Home Education PDF (forms to start and complete a home education program) and the November 10, 2026 agenda PDF: not opened (SharePoint personal links usually need a sign-in).
- Any measured bus on-time or ride-time data, or complaints about late buses in 2026-27: none found in the minutes read (May 2025 to October 2026) or on the news blog; web search was not used.
- The 2026-27 board minutes after October 20, 2026 (November 10 minutes not yet posted).
- A district statement on which documents count as proof of residency, or whether a purchase and sale agreement is accepted before closing: not found on the registration pages, form or policy JFAA.
- Whether SchoolMessenger alerts are sent in languages other than English: not stated on the closings page or in the handbooks read.
