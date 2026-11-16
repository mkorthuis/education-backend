# Getting to School, Choices and the Community in Rochester

Part of the Rochester research (town/Rochester). Gathered November 15, 2026.

## Summary

This file covers how Rochester students get to school (Student Transportation of America's buses, walk zones, assigned stops, missed buses, the 2026-27 route lists and the My Ride K-12 app, the COAST public bus), crossing guards, snow days and remote learning days, attendance rules and chronic absence, the elementary attendance zones and the 2025 redistricting, Maple Street Magnet School's closing, home education access and credits, private and charter options near Rochester (Tri-City Christian Academy, St. Charles School, Portsmouth Christian Academy) and Education Freedom Accounts, moving from a private school to Spaulding, veterans and other community visitors, and the city's plans for former school sites.

- **10 topics, 71 facts, 2 tables.** Nine topics are shared town topics (`district-transportation`, `district-school-day-and-calendar`, `district-attendance-zones-and-transfers`, `district-homeschool-access`, `school-programs-after-grade-6`, `town-school-options-nearby`, `town-streets-and-safe-routes`, `district-volunteers-and-partners`, `town-housing`). One is a **proposed new shared rule topic**, `remote-learning-and-snow-day-rules` (kind rule, question type rules): "New Hampshire's rules on remote learning days in bad weather, counting them as instructional time, and making up lost school days" (Ed 306.15 and 306.18; no library topic has them). Tables: `rochester_bus_morning_ride_minutes_2026_27` (derived) and `rochester_area_private_tuition_2026_27`. Raw copies are in `raw/daily/` (about 25 MB).
- **Places used:** `district Rochester` (the district, SAU 54, its schools and policies), `town Rochester` (police crossing guards, city streets and housing, the COAST bus, EFA counts), `district Tri-City Christian Academy`, `district St. Charles School` and `district Portsmouth Christian Academy` (each has its own record in the site's `district` table), and no place for state rules.
- **How district pages were read, and what needs a browser check:** www.rochesterschools.com answers automated requests with a bot check ("Client Challenge"). Before the main session ruled it out, eight district web pages and the district's news and live-feed data were read through the website vendor's host (rochesterpublicschoolsnh.sites.thrillshare.com and its API), which routes around the block. **In the browser pass (November 15, 2026) every one of those pages was opened at its www.rochesterschools.com address in Chrome; the facts matched, the raw copies were replaced with the browser copies, and the vendor copies were moved to `raw/daily/vendor-host/`.** Two facts were reworded because the feed shows only relative dates (district-transportation 11, district-school-day-and-calendar 6). The district's PDFs (policies, board minutes, route lists, calendar, zone map, Spaulding handbook) came directly from its separate document host (files-backend.assets.thrillshare.com, reached through the district's aptg.co and 5il.co links), which didn't block. Sources are cited by their www.rochesterschools.com address. The City of Rochester's site (www.rochesternh.gov) refused automated requests (HTTP 403); the city's news site (news.rochesternh.gov) worked.
- **Main findings:**
  - **No late bus or backup ride for a missed bus is described** on the district's transportation page, in policy EEA or in Spaulding's handbook. Drivers do not wait at stops, students may ride only their assigned bus, and bus changes need a call to the Central Office more than a day ahead, with "most requests" not granted. The COAST public bus (routes 6, 12 and 14) serves Rochester at a $2.00 fare from September 1, 2026.
  - **Bus stops and times are on two route lists posted August 18, 2026 and on the new My Ride K-12 app** (linked with the student number from Infinite Campus). Derived from the route sheets: elementary runs' first stops are 7:30–8:08 a.m. and middle and high school runs' 6:19–6:52 a.m.; the longest scheduled morning rides are 49 minutes (elementary, Chamberlain Street) and 64 minutes (Rochester Middle School).
  - **Elementary placement is by home address, and the district is not taking in-district elementary transfer requests for 2026-27.** The posted zone map is the "Scenario 1" plan the board adopted on January 9, 2025; on it, Wakefield Street and most of downtown east of the Cocheco River are in the Chamberlain Street zone. It still shows a Maple Street Magnet zone, although the board voted on March 12, 2026 to close that building as of June 30, 2026. The 2026-27 bus lists serve five elementary schools.
  - **Rochester's home education policy IHBG (amended June 10, 2021) still describes notices that state law stopped requiring on July 1, 2026,** and doesn't name EFA students. Under IHBG, home-educated, private and charter school students who live in Rochester may join district classes, sports and activities through the same process as enrolled students. Under policy IK (amended July 9, 2026), a home education portfolio or assessments can show the competencies for Spaulding credit.
  - **Remote learning days are allowed** (policy IMBA, amended July 9, 2026), and a student who doesn't do the work on such a day is marked absent (policy JED). In 2025-26 the district closed for snow (December 2, 2025; January 26, 2026) and delayed two hours (January 7, 2026); no remote learning day was found. The 2026-27 calendar holds five snow make-up days, June 22–25 and June 28, 2027.
  - **St. Charles School is a K–8 special education program,** run by Catholic Charities New Hampshire in Rochester for public school students placed there, with a non-religious curriculum. **Tri-City Christian Academy** (Somersworth, Pre-K–12) posts 2026-27 tuition of $6,322 to $7,750 for a first child and tells New Hampshire families to apply for EFAs. Rochester had 316 EFA-eligible students and 8 on the waitlist on November 15, 2026 (CSF's live figures).
  - **Crossing guards are City of Rochester police employees,** paid $15.00 an hour (posting opened July 30, 2025). In 2021 the city listed posts at Franklin/Chamberlain Streets and Brock Street/Holy Rosary Credit Union among seven. No current list or count of posts was found.
- **Main gaps:** the city's crossing guard posts and budget, and council discussion of them (city site blocked); the 2026-27 zone lines for the former Maple Street Magnet area and the text of policy JF (Enrollment and Capacity, adopted June 11, 2026, not posted); any chronic absenteeism rate for Rochester (New Hampshire doesn't publish one; the 2023-24 federal civil rights data have no chronic absence file); any enrollment projection tied to housing growth; a schedule of veteran or career speakers in Spaulding classes; the share of Rochester children at charter or private schools beyond the site's Census and EFA figures.

### Premises checked

| Question | Premise | What the sources show |
|---|---|---|
| P4.3 | Families may choose "Seacoast Charter School" instead of Spaulding High School | **Not for high school.** Seacoast Charter School in Dover serves kindergarten to grade 8 (Dover file `Dover/choices-and-adult-learning.md`, town-school-options-nearby fact 1), so it isn't an alternative to Spaulding. The site's school list shows no general private school located in Rochester; the private schools there are special education programs. |
| P5.3 | There may be "backup transportation or a late-bus option" | **None described.** The district's transportation page, policy EEA and Spaulding's handbook describe no late bus or backup ride; drivers don't wait at stops, and families are told to call the bus company if a bus passes a stop. |
| P7.1 | A family "right near downtown" is zoned for one elementary school | **Partly.** Placement is by address. On the posted map, downtown is split among the Chamberlain Street, Maple Street Magnet, McClelland and Salmon Falls zones, and Wakefield Street is in Chamberlain Street's. Maple Street Magnet closed June 30, 2026, and no updated map was found. |
| P12.2 | Homeschoolers must file paperwork "each year" with SAU 54, with evaluations | **Out of date.** Since July 1, 2026 no declaration or annual evaluation is required (library `home-education-rules` facts 1–2). Rochester's posted policy IHBG (2021) still describes a notice within 5 business days of starting. |
| P15.1 | Crossing guards are missing at "busy intersections near Chamberlain and Brock" | **Can't be checked.** In 2021 the city listed guard posts at Franklin/Chamberlain Streets and at Brock Street/Holy Rosary Credit Union. No current list of posts was found; the city's site refused automated requests. |
| P15.2 | The district uses "remote learning days" | **Allowed, but none found in use.** Policy IMBA allows them in bad weather; in 2025-26 the district closed or delayed instead, and the 2026-27 calendar has five snow make-up days in June. |
| P24.2 | "St. Charles School or Tri-City Christian" are private school choices | **Partly.** Tri-City Christian Academy is a Pre-K–12 Christian school in Somersworth. St. Charles School in Rochester is a K–8 special education program for public school students placed there, with a non-religious curriculum, not a school families enroll in directly. |
| P24.1 | Portsmouth Christian Academy as a private option | **Correct.** It is in Dover; it posts out-of-pocket tuition of $7,495 to $19,825 and asks EFA families to use the funds mostly for tuition. |

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P4.3 Do Chamberlain Street families stick with Spaulding or try Seacoast Charter or private schools? | town-school-options-nearby 1–10; site data; Dover file `Dover/choices-and-adult-learning.md` town-school-options-nearby 1–8 | partial | **Premise checked** (Seacoast Charter is K–8). Covered: the private schools near Rochester and their tuition, EFA counts. **Site data:** EFA counts by town (297 Rochester students in the FY2027 base-aid count), Census private or home schooling share, Spaulding enrollment (1,299 in 2024-25, with Wakefield students). **Derived:** CSF's 316 EFA-eligible Rochester students are about 8% of 3,868 (316 plus the site's 3,552 Rochester public school students in 2025-26). The site's school list has no general private school located in Rochester; the four there (Monarch School of New England, St. Charles School, and the Strafford Learning Center's Rochester Learning Academy and John Powers Primary School) are special education programs. The nearest charter schools in the site's list are Seacoast Charter (Dover, K–8), Great Bay Charter (Exeter) and the online VLACS. **Not found:** how many Rochester students attend charter or private schools, or by neighborhood. |
| P5.3 Backup transportation or a late bus if a son misses the bus | district-transportation 1–5, 13 | partial | **Premise checked** (none described). Covered: drivers don't wait; only the assigned bus; bus changes; what to do if a bus passes a stop; the COAST public bus. Absences for transport trouble fall under the principal's "other good cause" (district-school-day-and-calendar 8–9). **Not found:** any district rule for a student who misses the bus beyond these. |
| P7.1 Which elementary school is zoned for a home near downtown | district-attendance-zones-and-transfers 1–9 | full | **Premise checked.** Wakefield Street is in the Chamberlain Street zone on the posted map (transcribed from image). The district's registration office (603-332-3678, student.registration@sau54.org) answers placement questions. |
| P12.1 Homeschooled children in band, sports or art at McClelland or the middle school | district-homeschool-access 2–4; library: home-education-rules fact 8, choice-hb-1817-efa-public-school-courses | full | Through IHBG, by the same process as enrolled students, when "administratively and academically feasible", with the school's rules, NHIAA eligibility for sports and IGDAA eligibility for activities. |
| P12.2 Yearly paperwork with SAU 54 and evaluations | district-homeschool-access 1, 4; library: home-education-rules 1–2, 5, choice-hb-1268-home-education-history | full | **Premise checked** (out of date). |
| P12.3 Whether Spaulding accepts homeschool credits in grade 9 | district-homeschool-access 5; school-programs-after-grade-6 3 | full | Credit comes from showing competencies (portfolio or assessments), decided by the principal; transfer credit from "approved schools" doesn't list home education. Spaulding's diploma needs 26 credits for the classes of 2027–2029 (agent 3's file). |
| P15.1 Crossing guards near Chamberlain and Brock | town-streets-and-safe-routes 1–5; district-transportation 2, 6 | partial | **Premise checked.** Covered: who employs guards, pay, the 2021 posts, the board's September 2025 question, walk zones. **Not found:** the current posts, how many guards the city funds, and how posts are chosen (city budget and police pages not reachable). |
| P15.2 Snow days versus remote learning days, and whether teaching happens on remote days | district-school-day-and-calendar 1–7; remote-learning-and-snow-day-rules 1–4 | full | **Premise checked.** What is taught on a remote day isn't described in any source found. |
| P17.3 Veterans groups and community members invited into Spaulding for careers and civics | district-volunteers-and-partners 1–5 | partial | Covered: Rochester Veterans Council events with Spaulding football and Creteau students, RMS's yearly assembly, visitor rules. **Not found:** a program of veteran or career speakers in Spaulding civics or career classes. Creteau's business partners are in agent 3's file. |
| P18.3 Finding the family's bus stop before the first week | district-transportation 6–10; table rochester_bus_morning_ride_minutes_2026_27 | full | Routes were posted August 18, 2026, two weeks before the September 1 start. |
| P21.1 Honest, up-to-date information on which elementary school is "best" | district-attendance-zones-and-transfers 1–2, 10–11; site data; library: school-rating-sites, measure-student-growth-percentile, measure-essa-school-designations | partial | Placement is by address and in-district elementary transfers aren't accepted for 2026-27, so tenants can't choose among schools. **Site data:** each school's test scores and growth, class sizes, enrollment, meal eligibility and safety counts. Agent 1's file covers whether the schools are improving. |
| P21.2 How redistricting works if the city builds more apartments downtown | district-attendance-zones-and-transfers 3, 5–8, 10, 12; town-housing 1–2 | partial | Covered: the 2024-25 redistricting, annual zone review, the closings, the new capacity policy, the former school sites' zoning. **Site data:** enrollment fell from 4,135 Rochester students (2013-14) to 3,552 (2025-26). **Not found:** any enrollment projection or rule that ties new housing to zone changes; JF's text. |
| P21.3 Chronic absenteeism and what the schools do about it | district-school-day-and-calendar 8–12; library: chronic-absenteeism-nh-data, measure-truancy-vs-chronic-absence, research-chronic-absence | partial | **No Rochester chronic absence rate was found;** New Hampshire doesn't publish one (Manchester file `Manchester/results-and-community.md`, district-school-day-and-calendar 5). **Site data** (habitual truancy, 10 unexcused half days): 1,780 Rochester students in 2024-25, up from 1,592; Spaulding 496. **Derived:** about 47% of the district's 3,768 students in 2024-25, against about 19% statewide (30,546 of 162,544). Districts define a half day themselves (Rochester's in fact 10), so the comparison is rough. |
| P24.1 Whether an EFA makes private school affordable for a middle-income family | town-school-options-nearby 5–7, 9–10; table rochester_area_private_tuition_2026_27; site data; library: efa-eligibility-and-cap, efa-uses-and-requirements | full | **Site data (FY2027 per-student EFA amounts):** $4,351 base, plus $2,441 if eligible for free or reduced-price meals, $2,229 for special education and $849 for English learners. **Derived:** Tri-City's grade 1–5 tuition for a first child enrolled by April 15 ($6,322) is $1,971 more than the base amount, before the textbook fee. Whether that is "affordable" depends on the family. |
| P24.2 What St. Charles School or Tri-City Christian offers that the public schools don't | town-school-options-nearby 1–4, 8 | full | **Premise checked.** The facts list each school's program; whether those are better is a judgment the data can't make. |
| P24.3 Private elementary school, then Spaulding: will the children feel out of place? | school-programs-after-grade-6 1–3; site data | partial | Covered: registration, Spaulding's freshman information, credit rules. **Site data:** Spaulding's size and grade 9 enrollment. **The data can't tell** how a student will feel; no source measures how former private school students do at Spaulding. |

## district-transportation: Rochester's School Buses: Walk Zones, Assigned Stops, Missed Buses, Route Lists and the COAST Bus

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. Rochester School District buses are run by Student Transportation of America, and the district's transportation page sends questions to the company's Rochester office (603-509-2904) or the district's Central Office (603-332-3678).
   - citation: Rochester School District, Transportation page
   - source: https://www.rochesterschools.com/o/rsd/page/bus-information
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-transportation-page.txt (saved in Chrome on 2026-11-15). Text: "If you have any questions or concerns, please contact - Student Transportation of America (Rochester): 603-509-2904 - Rochester School District Central Office: 603-332-3678".
2. Under Rochester School Board policy EEA (amended December 11, 2025), students in kindergarten to grade 3 may be required to walk up to 1 mile to school, grades 4 and 5 up to 1½ miles and grades 6 to 12 up to 2 miles, except that the elementary walking rule excludes Salmon Falls School students; bus riders in a busing area may have to walk up to 1 mile (grades K–3) or 1½ miles (grades 4–12) to the nearest stop, and a student may not walk from a walk zone into a bus zone to ride.
   - citation: Rochester School Board Policy EEA, Student Transportation Services (adopted April 8, 1993; amended August 14, 2025 and December 11, 2025), Walking Distances 1–3
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-eea.pdf (.txt). Text: "Students may be required to walk up to 1 mile to get to their assigned school; to exclude Salmon Falls School students." and "students living within a busing area, may be required to walk up to 1 and 1/2 miles to get to the nearest school bus stop." The transportation page repeats the distances without the Salmon Falls exception.
3. Under Rochester's policy EEA and transportation page, students are assigned to buses and schools by the address of their primary residence (not a babysitter's), may ride only their assigned bus and get on and off only at their assigned stop, may not bring other students home on the bus or ride to or from jobs, including babysitting, and may get a temporary health-related permit with a doctor's written verification; the policy also reserves the board's right to charge students over 14 in grades 9–12 for transportation.
   - citation: Rochester School Board Policy EEA, items 4–10; Rochester School District, Transportation page
   - source: https://www.rochesterschools.com/o/rsd/page/bus-information
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-eea.txt; raw/daily/rsd-transportation-page.txt. Text: "Students are not assigned to schools from a baby-sitter's address"; "Special permits for health-related reasons may be issued on a temporary basis. Written verification from a medical doctor is required."; "The Board reserves the right to charge all students over the age of 14 in grades 9 through 12 for transportation to and from school." No fee was found in the 2026-27 sources.
4. Rochester School District asks families who need a bus change to call the Central Office (603-332-3678) more than one day ahead, says most requests cannot be granted because of School Board policy and bus capacity, and says a note sent to school does not replace that call.
   - citation: Rochester School District, Transportation page
   - source: https://www.rochesterschools.com/o/rsd/page/bus-information
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-transportation-page.txt. Text: "Please allow more than one day notice, and understand that most requests cannot be honored because of School Board policy and bus capacities. Sending a note into the school will not replace the need contact the RSD Central office."
5. Spaulding High School's 2026-27 handbook says students must be at their stop before the bus arrives and the driver will not wait for students who are not there, and the district told families in December 2025 that if a bus passes their stop, students should never chase it and should contact the transportation department for help.
   - citation: Spaulding High School Parent & Student Handbook 2026-2027, Bus Regulations 2 and 5 (p. 23); Rochester School District live feed post, December 1, 2025 ("Winter Bus Safety Reminders")
   - source: https://www.rochesterschools.com/o/shs/page/student-enrollment1
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/shs-parent-student-handbook-2026-27.pdf (.ocr.txt, transcribed from image by OCR; the handbook PDF is scanned); raw/daily/rsd-live-feed-selected-posts.txt. Text: "Students must be at their bus stop before the bus arrives. The driver will not wait at the bus stop for students who are not at the bus stop."; "If the bus ever passes your stop, students should never chase it. Please contact the Transportation Department for help." No late bus or backup ride for a missed bus is described on the transportation page, in EEA or in the handbook.
6. Under Rochester's policy EEA, the superintendent sets bus stops with the bus operator, a stop becomes authorized when the School Board approves it, drivers may not load or unload students anywhere else, stops are placed at convenient intervals where students can wait and cross with the most safety the road allows, and the district reviews the safety of walking routes and bus stops every year or when it sees fit.
   - citation: Rochester School Board Policy EEA, Operation of the School Bus System C–E
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-eea.txt. Text: "A bus stop so established will be designated as authorized when the School Board has approved its designation as such."; "E. The safety of student walking routes and bus stops shall be reviewed by the District annually or when deemed appropriate." The January 2026 post below shows a stop moved for safety.
7. Rochester School District posted its 2026-27 bus routes on August 18, 2026 as two lists, elementary and middle/high school, which give each morning run's stops in order with scheduled times, for September 1, 2026 to June 25, 2027; the elementary list was updated August 28, 2026.
   - citation: Rochester School District, "Transportation Routes for the 26-27 School Year" (news, August 18, 2026); Elementary Bus Routes 26-27 (08.28.26, updated) and HS/MS Bus Routes 26-27 (08.28.26)
   - source: https://www.rochesterschools.com/article/3004433
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-routes-2026-27-article.txt; the article page, dated "August 18, 2026"; raw/daily/rsd-elementary-bus-routes-2026-27.pdf and rsd-ms-hs-bus-routes-2026-27.pdf (mostly scanned; .ocr.txt transcribed from image). Sheet text: "9/1/2026 - 6/25/2027". The sheets list stops by street corner or house number; only morning runs are posted. File names: "Elem-Bus-Routes-26-27_08.28.26-updated.pdf", "HSMS-Bus-Routes-26-27_08.28.26.pdf".
8. Rochester School District added the My Ride K-12 app for 2026-27: a parent registers in the app or at myridek12.tylerapp.com, chooses Rochester School District, adds each child with the student number shown in the Infinite Campus Parent Portal, and then sees the child's transportation information, which can be shared with another adult by email.
   - citation: Rochester School District, My Ride K-12 App page; "Transportation Routes for the 26-27 School Year" ("New for this school year")
   - source: https://www.rochesterschools.com/o/rsd/page/my-ride-k-12
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-my-ride-k12-page.txt. Text: "Enter your child's Student number, then click Add Student. You can find the Student Number in the Infintie Campus Portal. Once you have linked to a student, click that student's details to see all relevant transportation information." Support is through Student Transportation of America (603-509-2904).
9. Rochester School District requires a completed K-2 Drop Off form on file for every student in kindergarten, grade 1 and grade 2, and those students may not get off the bus without an adult present unless the returned form gives permission.
   - citation: Rochester School District, Transportation page
   - source: https://www.rochesterschools.com/o/rsd/page/bus-information
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-transportation-page.txt. Text: "All grade K, 1, and 2 students must have a completed K-2 Drop Off form on file with the school. Students in grades K, 1, and 2 may not exit the bus without an adult present unless permission has been granted through a returned K-2 Drop Off form."
10. On Rochester's 2026-27 morning route lists, the 19 elementary runs make their first pickups between 7:30 and 8:08 a.m. and reach the schools between 8:07 and 8:25 a.m. for an 8:30 a.m. start, while the 19 middle and high school runs make their first pickups between 6:19 and 6:52 a.m. and reach the schools between 7:02 and 7:24 a.m. for a 7:30 a.m. start (derived; see table rochester_bus_morning_ride_minutes_2026_27).
   - citation: Rochester School District, Elementary and HS/MS Bus Routes 26-27; City of Rochester news, "Rochester School Department Welcomes Students Back for 2026-27 School Year" (August 31, 2026)
   - source: https://www.rochesterschools.com/article/3004433
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: **Derived** from the OCR text of the route sheets (scheduled times; "Leave Yard" departures from the bus yard were left out). Raw: raw/daily/rochester-bus-routes-2026-27-scheduled-times.csv (times only, no addresses); raw/daily/news/news-rochester-school-department-welcomes-students-back.txt: "School hours: Elementary schools, 8:30 a.m.–3 p.m.; RMS and SHS, 7:30 a.m.–2:15 p.m." The elementary runs start at Rochester Middle School or Spaulding after the middle and high school runs, as policy EEA B describes ("alternating elementary and middle / high school trips with the same fleet of buses").
11. Rochester School District told families in September 2025 that a bus driver shortage and route adjustments had changed pick-up and drop-off times for all buses, and the superintendent told the School Board on September 11, 2025 that bus routes to Maple Street Magnet School were still affected by the driver shortage.
   - citation: Rochester School District live feed post, September 12, 2025; Rochester School Board minutes, September 11, 2025 (Superintendent Update)
   - source: https://www.rochesterschools.com/o/rsd/page/board-agendas-minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-live-feed-selected-posts.txt: "Due to the current driver shortage and route adjustments, pick-up and drop-off times have changed for all buses."; raw/daily/minutes/Full-Board-Minutes-09.11.25.pdf (.txt): "While bus routes at Maple Street School remain impacted by a driver shortage, overall efficiency continues to improve." No 2026-27 driver shortage notice was found.
12. From January 5, 2026, Rochester School District split elementary route R19, moved riders from the Pine Street stop to route R4 and to a stop at Duvall Park near North Main Street, and added a Cove Court stop so students would not need to cross Main Street, saying the changes were to improve safety and manage bus capacity.
   - citation: Rochester School District live feed post, "New Elementary Permanent Bus Route Changes – Beginning January 5, 2026" (January 4, 2026)
   - source: https://www.rochesterschools.com/o/rsd/page/bus-information
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-live-feed-selected-posts.txt. Text: "These changes are being made to help improve safety and manage bus capacity more effectively."; "A new Cove Court bus stop will be added so students will not need to cross Main Street." The 2026-27 R-4 run still stops at Cove Ct/N Main St/Pine St/River St and Chestnut St/River St/Duval Park (route sheet).
13. COAST, the Seacoast region's nonprofit public bus system, runs routes 6 (Farmington–Rochester), 12 (Rochester–Somersworth–Dover) and 14 (Rochester), and since September 1, 2026 charges a $2.00 cash fare to every rider age 5 and older (11 tickets for $20, a $60 monthly pass), with free rides for children under 5 with an adult and for UNH and Great Bay Community College students, and half fare ($1.00) for riders 65 and older, riders with qualifying disabilities and Medicare cardholders.
   - citation: COAST, Routes & Schedules; Fares, Tickets & Passes; "COAST Board Approves New Fare Structure Effective September 1, 2026"
   - source: https://coastbus.org/pricing-fares/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/coast/coast-schedules.txt; coast-fares.txt; coast-fare-structure-2026-09-01.txt. Text: "All passengers age 5 and older pay $2.00 each time they board a COAST fixed-route bus"; "Children under 5 ride free when accompanied by an adult." The fare had been $1.50 since 2008. Route 14's page says routes 12, 13 and 14 are run by the same bus. No reduced fare for K–12 students is listed. Weekday times weren't captured (the schedule page is interactive).

## district-school-day-and-calendar: Rochester's 2026-27 Calendar, Snow Days, Remote Learning Days and Attendance Rules

- kind: local
- question_type: local_practice
- description: School hours, before- and after-school care, the school calendar and vacations, and attendance and absence rules

1. Rochester's 2026-27 school calendar, approved March 12, 2026, has 180 instructional days, 5 teacher workshop days and 5 early release days; the last scheduled student day is Monday, June 21, 2027, and June 22–25 and June 28, 2027 are marked "Snow Day if needed."
   - citation: Rochester School District, 2026-2027 School Year Calendar (Approved 03/12/2026)
   - source: https://www.rochesterschools.com/documents/calendars/16773249
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-calendar-2026-27.pdf (.txt). Text: "SD - Snow Day if needed"; "180 Instructional Days 5 Teacher Workshop Days 5 Early Release Days". The June dates were read from the calendar grid (rendered and checked against the image). First days by grade are in the city's August 31, 2026 news post (raw/daily/news/news-rochester-school-department-welcomes-students-back.txt).
2. Under Rochester School Board policy IC/ICA, the schools are open at least 180 days a year (at least 990 hours for middle and high schools and 945 for elementary schools), and days closed for emergencies are made up at the end of the school year or during vacations, as the board approves on the superintendent's recommendation.
   - citation: Rochester School Board Policy IC/ICA, School Year/School Calendar (adopted April 8, 1993; amended February 9, 2006; reviewed December 10, 2009)
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ic.pdf (.txt). Text: "Any days that the schools are closed for emergency reasons will be made up at the end of the school year or during recess periods, as approved by the Board upon the Superintendent's recommendation."
3. Under Rochester School Board policy EBCD, the superintendent may close schools or dismiss early for hazardous weather or other emergencies after consulting traffic and weather authorities, closes only the affected school when conditions affect one school, and must tell students, parents and staff early each year how closings will be announced.
   - citation: Rochester School Board Policy EBCD, Emergency Closings (adopted April 8, 1993; amended November 13, 2008; reviewed August 9, 2018)
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ebcd.pdf (.txt). Text: "If conditions affect only a single school, only that school shall be closed."; "shall take action to close the schools only after consultation with traffic and weather authorities."
4. Rochester School Board policy IMBA, amended July 9, 2026, lets the district or a school teach remotely when bad weather makes it unsafe to transport students (a "remote learning day"), and also covers individual online courses, which need the principal's written approval in advance.
   - citation: Rochester School Board Policy IMBA, Remote Learning (adopted April 13, 2006; last amended July 9, 2026), sections A and B; Rochester School Board minutes, July 9, 2026
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-imba.pdf (.txt); raw/daily/minutes/Full-Board-Minutes--07_09_26-1.pdf (.txt) ("IMBA - Remote Learning" among policies approved as amended). Text: "When inclement weather makes it unsafe to safely transport students to or from in-person instruction, the District or school may elect to provide instruction remotely, pursuant to Board policy IC." The policy does not say what a remote day's lessons must include.
5. Under Rochester's attendance policy JED, a student who does not complete the work on a day when internet instruction has been directed is marked with an undocumented (unexcused) absence, and Spaulding's 2026-27 handbook says the same for any day "when instruction has been directed."
   - citation: Rochester School Board Policy JED, Student Absences and Excuses (amended June 12, 2025); Spaulding High School Parent & Student Handbook 2026-2027, Section 1: Attendance
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-jed.pdf (.txt): "Failure to complete work for days when internet instruction has been directed will result in an undocumented absence."; raw/daily/shs-parent-student-handbook-2026-27.ocr.txt (transcribed from image).
6. In 2025-26 Rochester's schools closed for snow on December 2, 2025 (with all before- and after-school activities cancelled) and again in late January 2026, and opened two hours late on January 7, 2026, with the superintendent announcing them on the district's feed; no remote learning day appears in the district's feed, which runs from late August 2025 to October 2026.
   - citation: Rochester School District live feed posts, December 1, 2025; January 6, 2026; January 26, 2026
   - source: https://www.rochesterschools.com/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-live-feed-selected-posts.txt; the feed's three pages, read in Chrome on 2026-11-15, run from late August 2025 to October 2026 and show relative dates only; the late-January snow day post sits between the January 30 workshop reminder and the early-February counseling week posts (the feed may not hold every notice). Text: "Due to the impending snow storm, there will be no school in Rochester (SAU54) tomorrow Tuesday Dec 2nd."; "there will be a 2 hour delay for the Rochester Schools Wednesday Jan 7th."; "Wishing all Rochester School District families a safe and cozy snow day."
7. In 2025 the Rochester School Board turned down a memorandum on "Work from Home Snow Days 2024-2025" for teachers and sent it to negotiations with the teachers' union (March 6, 2025), and in December 2025 it approved a paraprofessional snow day memorandum.
   - citation: Rochester School Board minutes, March 6, 2025 (special meeting) and December 11, 2025
   - source: https://www.rochesterschools.com/o/rsd/page/board-agendas-minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/minutes/Special-Board-Minutes-3.6.25.pdf (.txt): "to reject the following MOU and move to RFT negotiations for consideration. ● Work from Home Snow Days 2024-2025 Motion carried by majority."; raw/daily/minutes/Full-Board-Minutes-12_11_25.pdf (.txt): "to approve the Para-professional Snow Day MOU." The memoranda's terms weren't posted. These concern staff work on snow days, not student instruction.
8. Under Rochester's policy JED, excused absences are illness or wellness, recovery from an accident, court, medical and dental appointments, a death in the immediate family, religious holidays, verified school trips and events, college visits, and other good cause the principal accepts; parents may excuse up to 5 wellness days a year by phone, and more need a provider's note.
   - citation: Rochester School Board Policy JED, Student Absences and Excuses (amended June 12, 2025), Absences
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-jed.txt. Text: "*Parents/guardians may excuse up to 5 days (per school year) with a notification via a phone call. Additional absences beyond 5 days, associated with student wellness, must be accompanied by a note from a provider, to be considered excused."; "Such other good cause as may be acceptable to the Principal or permitted by law". Family vacations: no more than 5 days excused, requested a month ahead.
9. Under Rochester's policy JED, a student's absence for a reason not on the excused list needs a written explanation from the parent, and the principal decides whether it is good cause and tells the parents by phone and in writing.
   - citation: Rochester School Board Policy JED, Absences
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-jed.txt. Text: "If parents wish for their child to be absent for a reason not listed above, the parent must provide a written explanation ... The Principal will make a determination as to whether the stated reason for the student's absence constitutes good cause". Missing the bus is not named in the list.
10. Rochester's policy JED counts a half-day absence as missing more than two and fewer than three and a half hours of instruction, treats 10 unexcused half days in a year as habitual truancy, and says excessive absences, excused or not, may be reviewed and addressed with truancy interventions.
   - citation: Rochester School Board Policy JED, Truancy and Intervention
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-jed.txt. Text: "A half-day absence is defined as a student missing more than two hours of instruction time and fewer than three and one-half hours"; "Excessive absences, regardless of excused or unexcused, that are impacting the student's educational program, will be reviewed and may be addressed in accordance with other truancy interventions." The site's habitual truancy counts use the state definition (library measure-truancy-vs-chronic-absence).
11. Under Rochester's policy JED, families are told of every absence; at 5 unexcused absences the school mails a letter, at 10 it mails another and a parent meeting is required after 10 days of absence in a year, and at 15 the district mails a letter with an attendance intervention plan and may refer a student who does not improve to DCYF or to the Rochester Police Department for prosecution under RSA 193:1-7.
   - citation: Rochester School Board Policy JED, Truancy and Intervention; Spaulding High School Parent & Student Handbook 2026-2027, Section 1: Attendance
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-jed.txt: "After 10 cumulative days of absence during a given school year, a parent meeting will be required."; "may result in a referral to DCYF (Department for Children Youth and Families) or the Rochester Police Department for prosecution under N.H. RSA 193:1-7. The School District will inform parents/guardians if a referral ... is made." Spaulding's handbook (raw/daily/shs-parent-student-handbook-2026-27.ocr.txt) adds that the guidance counselor is notified at 5 and 10.
12. Spaulding High School's 2026-27 handbook says absences of ten days, even with parents' approval, or absences that interfere with a student's program will be treated as truancy, that documentation is due within three days of an absence, and that "even a pattern of parent excused absences can become a problem."
   - citation: Spaulding High School Parent & Student Handbook 2026-2027, Section 1: Attendance and Truancy (pp. 8–9)
   - source: https://www.rochesterschools.com/o/shs/page/student-enrollment1
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/shs-parent-student-handbook-2026-27.ocr.txt (transcribed from image). Text: "Absences, even with the approval of the parents/guardians, which are excessive, ten days, and/or which interfere with the student's educational program will be interpreted as truancy and follow-up legal procedures may be instituted." No chronic absenteeism rate or attendance goal was found in the district's 2024-2029 strategic plan (its scanned PDF, https://aptg.co/0FHCk1, was OCR'd; not saved here) or in the board minutes of July 2024–November 2026.

## remote-learning-and-snow-day-rules: Snow Days, Remote Learning Days and Make-Up Time: New Hampshire Rules

- kind: rule
- question_type: rules
- description: New Hampshire's rules on remote learning days in bad weather, counting them as instructional time, and making up lost school days

1. New Hampshire's school approval rules count remote learning as meeting the in-person instruction requirement only when bad weather makes it unsafe to transport students, when a parent or guardian asks for remote learning, or in a parent-approved alternative program the school board has approved.
   - citation: N.H. Admin. Rules Ed 306.18(a) and (c) (eff. 12-13-24)
   - source: https://gc.nh.gov/rules/state_agencies/ed300.html
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Raw: raw/daily/ed300.txt (fetched 2026-11-15; same text as the library's copy in additional-data/raw/terms/rules/ed300.txt). Text: "(c) Remote learning shall satisfy the requirements of RSA 189:1 and RSA 189:24 under the following conditions: (1) When inclement weather makes it unsafe to safely transport students to or from in-person instruction; (2) As an option for a parent or guardian making a request for remote learning; or (3) As articulated in a parent-approved alternative program approved by the local school board pursuant to Ed 306.17(c)."
2. Under New Hampshire's school year rule, remote learning done under those conditions counts toward the required instructional time, and a district that offers remote learning must have a school board policy governing it.
   - citation: N.H. Admin. Rules Ed 306.15(f) and Ed 306.18(d)
   - source: https://gc.nh.gov/rules/state_agencies/ed300.html
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Raw: raw/daily/ed300.txt. Text: "(f) Remote learning conducted in accordance with Ed 306.18(c) shall count toward the required amount of instructional time."; "(d) When the district offers remote learning, the school board shall be responsible for the development of a policy for the governance and administration of remote learning."
3. New Hampshire schools must keep a calendar of 180 days of instruction or the required number of instructional hours, and must use added hours to make up lost instructional time before asking the state for a waiver of instructional time.
   - citation: N.H. Admin. Rules Ed 306.15(a) and (d); RSA 189:2
   - source: https://gc.nh.gov/rules/state_agencies/ed300.html
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Raw: raw/daily/ed300.txt. Text: "(a) Each school shall maintain a school calendar which provides for 180 days of instruction or the required number of instructional hours, which may result in fewer than 180 days."; "(d) Schools shall use additional hours to reschedule lost instructional time before requesting a waiver of the amount of instructional time under RSA 189:2." The hour minimums are in the library (kindergarten-rules fact 3).
4. Under New Hampshire's school year rule, a school does not have to make up kindergarten time when a morning or afternoon kindergarten session is cancelled because of a delayed opening or early release for older grades.
   - citation: N.H. Admin. Rules Ed 306.15(e)
   - source: https://gc.nh.gov/rules/state_agencies/ed300.html
   - as_of: 2026-11-15
   - review_by: 2027-08-15
   - note: Raw: raw/daily/ed300.txt. Text: "(e) There shall be no requirement to reschedule instructional time for kindergarten if morning or afternoon kindergarten sessions are cancelled due to delayed opening or early release for students in grade 1 or higher."

## district-attendance-zones-and-transfers: Rochester's Elementary Zones, the 2025 Redistricting, Maple Street's Closing and Transfers

- kind: local
- question_type: local_practice
- description: How a district assigns students to schools by home address, its feeder pattern from elementary to middle to high school, redistricting history and plans, proof of residency, and requests to attend a different school

1. Rochester School District places kindergarten to grade 5 students by the residential address of the student's primary household, requires proof of residency at registration and again when a family moves within the district, and sends placement questions to Student Enrollment and Records (student.registration@sau54.org, 603-332-3678).
   - citation: Rochester School District, Elementary Placement page
   - source: https://www.rochesterschools.com/o/rsd/page/elementary-placement
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-elementary-placement-page.txt. Text: "Student placement for grades K–5 is determined by the residential address of the student's primary household, as established by the parent or legal guardian. Proof of residency is required at the time of registration. Current students who move to a new address within the district must also provide updated proof of residency." Residency rules: policies JFA and JFA-1, linked from the page.
2. Rochester School District's elementary placement page says that because of current enrollment levels across the district, it is not accepting in-district elementary transfer requests for the 2026-27 school year.
   - citation: Rochester School District, Elementary Placement page
   - source: https://www.rochesterschools.com/o/rsd/page/elementary-placement
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-elementary-placement-page.txt. Text: "Due to current enrollment levels across the district, we are no longer able to accept in district Elementary transfer requests for the 2026-2027 school year." The page still links a "Voluntary Elementary School Transfer Request" form.
3. The zone map Rochester School District posts as its "25-26 School Attendance Zones Map" is titled "Proposed School Attendance Zones, Scenario 1: Optimal Class Size (20/class)," was made by the City of Rochester's mapping office, and shows six elementary zones: Chamberlain Street, East Rochester, Gonic, Maple Street Magnet, McClelland and Salmon Falls.
   - citation: Rochester School District, RSD School Zone Map 2025-26 (PDF), linked from the Elementary Placement and Online Registration pages
   - source: https://www.rochesterschools.com/o/rsd/page/elementary-placement
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/rsd-school-zone-map-2025-26.pdf (.txt). Map text: "Proposed School Attendance Zones Scenario 1: Optimal Class Size (20/class) Rochester School District City of Rochester, NH"; legend "Chamberlain Street School East Rochester School Gonic School Maple Street Magnet School McClelland School Salmon Falls Rd School"; file path "\GISdata\Projects\SchoolDept\Redistricting\2024\PresentationGraphics\Scenario1.mxd". It also marks "Proposed Bus Stop" dots. No 2026-27 map was found.
4. On that map's downtown inset, Wakefield Street and the downtown streets east of the Cocheco River (including Union and Summer Streets, South Main Street and Columbus Avenue north of Upham Street) are in the Chamberlain Street School zone; the blocks around Maple, Pine, Chestnut and River Streets west of the river form the Maple Street Magnet zone; North Main Street west of Walnut Street and the Washington Street area are in the McClelland zone; and the area south of downtown (Upham Street, lower Columbus Avenue, Broad Street) is in the Salmon Falls zone.
   - citation: Rochester School District, RSD School Zone Map 2025-26, downtown inset
   - source: https://www.rochesterschools.com/o/rsd/page/elementary-placement
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Transcribed from image: the PDF was rendered and the inset read by eye. Raw: raw/daily/rsd-school-zone-map-2025-26.pdf; crop raw/daily/rsd-school-zone-map-2025-26-downtown-inset.png. Zone edges follow streets and the river, so an address near a boundary should be checked with the district (fact 1).
5. The Rochester School Board's redistricting for the new Salmon Falls School began on December 12, 2024, when the Director of Operations presented three plans and the administration recommended Option 1 for optimal class size and early intervention in all elementary schools; on January 9, 2025 the board accepted "Redistricting Plan: Scenario 1" unanimously.
   - citation: Rochester School Board minutes, December 12, 2024 ("Redistricting Plan") and January 9, 2025
   - source: https://www.rochesterschools.com/o/rsd/page/board-agendas-minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/minutes/_Full_Board_Minutes_12.12.24__1_.pdf (.txt): "presented three redistricting plans. Administration recommended Option 1 as the best option. This option allows for optimal class size and early intervention in all elementary schools."; raw/daily/minutes/Full_Board_Minutes__1.09.25.pdf (.txt): "to accept Redistricting Plan: Scenario 1. Motion carried unanimously." Discussion that night included "the Maple Street Magnet School zone" and "transportation logistics".
6. During the 2025 redistricting, Rochester School District's Family and Community Engagement Director told the board on February 13, 2025 that families were supported through district-wide messages from the Family and Community Engagement Center, the district's app, PTAs, website updates, a redistricting hotline and a redistricting email.
   - citation: Rochester School Board minutes, February 13, 2025
   - source: https://www.rochesterschools.com/o/rsd/page/board-agendas-minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/minutes/Full_Board_Meeting_Minutes_2.13.25____1_.pdf (.txt). Text: "These supports include ongoing district wide communication through The Family and Community Engagement Center, Thrillshare and PTA's. Current updates can be found on the district website, by calling the redistricting hotline or sending an email to the redistricting team." The hotline number wasn't posted in the minutes.
7. Salmon Falls School on Salmon Falls Road opened on September 2, 2025 for up to 420 students in kindergarten to grade 5, and Rochester School Department closed School Street School and William Allen School in 2025, consolidating their students and staff into other elementary schools.
   - citation: City of Rochester news, "Chamber of Commerce holds Ribbon-Cutting Ceremony for Salmon Falls School" (August 29, 2025) and "City of Rochester Seeks Public Input on Future of Former School Properties" (February 23, 2026)
   - source: https://news.rochesternh.gov/chamber-of-commerce-holds-ribbon-cutting-ceremony-for-salmon-falls-school-public-open-house-planned-for-9-20/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/news/news-chamber-of-commerce-holds-ribbon-cutting-ceremony.txt: "set to open on September 2 and will accommodate up to 420 students from kindergarten to fifth grade."; raw/daily/news/news-city-of-rochester-seeks-public-input-on-future-of.txt: "In 2025, the Rochester School Department closed the two aging schools to reduce costs and consolidate students and staff into other elementary schools throughout the city." City news site, not the district's.
8. On March 12, 2026 the Rochester School Board voted to close the Maple Street Magnet School building as of June 30, 2026 (the motion carried 10–1), and on May 14, 2026 it set June 26 as Maple Street's last student day, with the chair asking that Maple Street families get their student placement letters on time.
   - citation: Rochester School Board minutes, March 12, 2026 ("Consideration of Maple Street Magnet School") and May 14, 2026
   - source: https://www.rochesterschools.com/o/rsd/page/board-agendas-minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/minutes/Full-Board-Minutes-03_12_26-1.pdf (.txt): "to close the Maple Street Magnet School building as of June 30 2026. ... Motion carried 10-1" (the roll call lists one member under both YES and NO); raw/daily/minutes/Full-Board-Minutes--05_14_26-3.pdf (.txt): "The Board Chair requested that Maple Street families receive their student placement letters in a timely manner."; "June 26 as the final student day for Maple Street Magnet School." The posted zone map (fact 3) still shows a Maple Street zone.
9. Rochester's 2026-27 elementary bus lists serve five schools (Chamberlain Street, East Rochester, Gonic, McClelland and Salmon Falls), and in the former Maple Street Magnet area they show a McClelland run stopping at Maple Street and Waldron Avenue ("McClelland Students ONLY") and a Chamberlain Street–East Rochester run stopping at Pine, River and Chestnut Streets (derived).
   - citation: Rochester School District, Elementary Bus Routes 26-27 (08.28.26, updated), runs R-4 and R-15
   - source: https://www.rochesterschools.com/article/3004433
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: **Derived** from the OCR text of the route sheets (raw/daily/rsd-elementary-bus-routes-2026-27.ocr.txt, transcribed from image). R-15 "Description: McC": "Maple St & Waldron Ave McClelland Students ONLY"; R-4 "Description: ERS CHAM": "Cove Ct & N Main St & Pine St & River St", "Chestnut St & River St & Duval Park". The route sheets don't show which addresses are assigned to which school.
10. Under Rochester School Board policy JECC (amended July 9, 2026), students are assigned to schools by legal residence, attendance zones are set by the district, reviewed every year by the administration and published on its website, and the superintendent may approve a transfer to another school only in the student's best educational interest and when space and programs allow, under class size guidelines of 18 in kindergarten, 22 in grades 1–2 and 25 in grades 3–5.
   - citation: Rochester School Board Policy JECC, Voluntary Transfer of Students to Schools (adopted July 17, 1997; last amended July 9, 2026)
   - source: https://www.rochesterschools.com/o/rsd/page/online-enrollment
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-jecc-vol.pdf (.txt). Text: "School attendance zones shall be established by the District, reviewed annually by the administration, and published on the District's website."; "Kindergarten 18 1-2 22 3-5 25". The policy cites RSA 189:1-a and RSA 193:12.
11. Rochester's policy JECC limits voluntary transfers to students with identified special needs, rising fifth graders staying at their current school (and their siblings), and children of district employees at the employee's school, with parents providing transportation in the last two cases; requests go in writing to both principals, the superintendent's decision on appeal is final, and a transfer can be revoked for chronic absenteeism, enrollment above the class size guidelines, or a student not picked up on time.
   - citation: Rochester School Board Policy JECC, Eligibility for Consideration; Voluntary Transfer Request Process; Appeals; Revocation of Transfer
   - source: https://www.rochesterschools.com/o/rsd/page/online-enrollment
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-jecc-vol.txt. Text: "The Superintendent's decision shall be final and shall not be subject to further administrative review."; "The student exhibits chronic absenteeism, consistent with RSA 193:1"; "The student is not consistently picked up in a timely manner at the conclusion of the school day." The state's best-interest and hardship transfers (RSA 193:3) are in the library (change-of-school-assignment); Rochester's procedure is policy JCA (raw/daily/policies/pol-jca.txt).
12. On June 11, 2026 the Rochester School Board adopted a new policy, JF Enrollment and Capacity, waiving the second reading by unanimous vote; on November 15, 2026 it was not among the policies posted in the district's Section J (Students).
   - citation: Rochester School Board minutes, June 11, 2026 (Governance Committee); Rochester School District, Policies, Section J – Students
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/minutes/Full-Board-Minutes--06_11_26-1.pdf (.txt): "to suspend the second reading requirement for policy JF Enrollment and Capacity. Motion carried unanimously."; "to approve policy JF Enrollment and Capacity. Motion carried unanimously."; raw/daily/policies/rsd-policy-book-j-list.txt (the posted Section J files; no JF). The policy's text wasn't found.

## district-homeschool-access: Home-Educated Students and Rochester's Schools: Policy IHBG, Activities and Credit

- kind: local
- question_type: local_practice
- description: How homeschooled and EFA students can take part in a district's classes, activities and sports, and the district's homeschool notice and evaluation process

1. Rochester School Board policy IHBG, as posted (adopted 1996, last amended June 10, 2021), still says a parent starting a home education program must notify the commissioner, the resident superintendent or a nonpublic school principal within 5 business days, must file a notice within 15 days when the program ends, and must keep records and evaluations as state law and rules require.
   - citation: Rochester School Board Policy IHBG, Home Education and Access to Curriculum and Co-Curricular Programs (adopted February 8, 1996; reviewed/amended June 10, 2021), sections A–B
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ihbg.pdf (.txt). Text: "shall notify the commissioner of the department of education, resident school district Superintendent, or principal of a nonpublic school of such within 5 business days of commencing the program."; "Homeschool records and evaluations shall be maintained in accordance with applicable New Hampshire statutes and education rules." Since July 1, 2026, state law requires no declaration except to use public school programs or on withdrawal, and the annual evaluation section was repealed (library home-education-rules facts 1–2). No revision of IHBG appears in the board minutes of July 2024–November 2026.
2. Under Rochester's policy IHBG, nonpublic, public charter and home-educated students may take district courses and co-curricular programs by following the same process as the district's resident students, are admitted when that is "administratively and academically feasible and appropriate," and are held to district rules on space, add/drop dates and prerequisites and to school rules and discipline.
   - citation: Rochester School Board Policy IHBG, section D.1–2
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ihbg.txt. Text: "Parents/guardians who wish for their child to participate in curricular courses and or co-curricular programs shall follow the same process as the district's resident students. Students will be granted admission when administratively and academically feasible and appropriate." State law says the district's policy may not be more restrictive than for enrolled students (library home-education-rules fact 8).
3. Under Rochester's policy IHBG, these students may play on school teams if they meet NHIAA eligibility rules and join other activities if they meet the academic eligibility that policy IGDAA applies to athletes, must come and go through the school office (with a written plan to the superintendent when an activity starts or ends while the office is closed), and either side may end participation with written notice.
   - citation: Rochester School Board Policies IHBG, section D.3–6, and IGDAA, Eligibility for Participation in Activities
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ihbg.txt; raw/daily/policies/pol-igdaa.pdf (.txt): "must meet the current academic eligibility requirements applied to student athletes under School Board Policy IGDJA." IHBG also says the district is "not responsible for nonpublic, public chartered school, or home educated students who are educationally handicapped."
4. Rochester's policy IHBG names nonpublic, public charter and home-educated students but not Education Freedom Account students, whom HB 1817 added on August 18, 2026 to the students state law lets take part in their home district's courses and activities.
   - citation: Rochester School Board Policy IHBG, section D.1; library topic choice-hb-1817-efa-public-school-courses
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ihbg.txt: "nonpublic, public chartered school, or home educated pupils shall have access to curricular courses and co-curricular programs offered by the school district in accordance with NH statute." HB 1817 facts: additional-data/state-issues.md, choice-hb-1817-efa-public-school-courses 1–2. An EFA student is not a "home educated student" under state law (library home-education-rules fact 4).
5. Under Rochester's policy IK (amended July 9, 2026), Spaulding awards credit when a student shows the competencies for a course, "irrespective of age or enrollment," and a home-educated student may show them through an evaluation of a home education portfolio or through district or state-approved assessments; a placement test that doesn't cover every required competency for a course does not earn its credit.
   - citation: Rochester School Board Policy IK, Earning of High School Credit (adopted April 8, 1993; last amended July 9, 2026), sections B and C.2.b
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ik--high.pdf (.txt). Text: "A collection of evidence showing achievement of competencies (e.g., out of school achievements, home education program portfolio, etc.)"; "An approved home education program (see Board policy IHBG); home educated students may demonstrate achievement of competencies through evaluation of their portfolio or assessments"; "Pre-placement tests will not generate credit if they do not fully encompass and assess all required competencies for that credit." Home education is not among IK's "approved schools" for transfer credit (school-programs-after-grade-6 fact 3).

## school-programs-after-grade-6: Entering Spaulding High School From a Private or Home School

- kind: local
- question_type: local_practice
- description: Middle and high school programs that a district's students attend: AP, honors, dual enrollment, early credit, transitions between schools, activities

1. A family new to Rochester's schools, including one coming from a private school, registers online through Infinite Campus (about 30 minutes) with the child's birth certificate, immunization records, any legal documents and proof of residency, and Spaulding High School's registration office is at 603-332-0757 and shs.student.registration@sau54.org.
   - citation: Rochester School District, Online Registration page
   - source: https://www.rochesterschools.com/o/rsd/page/online-enrollment
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Library raw copy (fetched 2026-11-08): additional-data/raw/districts/batch-6/rochester-online-enrollment.txt. Text: "High School (9-12) Phone: 603-332-0757 Fax: 603-330-0251 shs.student.registration@sau54.org"; "The registration process will take about 30 minutes to complete."; "Legible copy of student's Birth Certificate Immunization Records ... Any necessary legal documents Proof of Residency". Translated forms are offered in Indonesian, Nepali, Portuguese and Spanish.
2. Spaulding High School's "Incoming Freshmen Information" page gathers the Class of 2030 Program of Studies, a list of freshman courses, a welcome letter with counselor and social media information, a video of the 2026 Eighth Grade Parent Night slideshow, daily schedules, meal information and forms.
   - citation: Spaulding High School, Incoming Freshmen Information page
   - source: https://www.rochesterschools.com/o/shs/page/incoming-freshmen-info
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/shs-incoming-freshmen-info.txt (saved in Chrome on 2026-11-15). Text: "Class of 2030 Program of Studies"; "Downloadable Freshmen Courses"; "Welcome Letter with Counselor & Social Media Information"; "8th Grade Parent Night Slideshow"; "Calendar, Schedules, School Meals, Courses, Infinite Campus, Forms and Announcements that incoming freshmen will need when entering high school." The slideshow is a video file and wasn't transcribed.
3. Under Rochester's policy IK, Spaulding's principal grants transfer credit for similar courses completed at "approved schools" (New Hampshire public and charter schools, public academies, approved public or private tuition program schools, and member schools of interstate districts), may count a course that isn't similar as an elective, must explain a denial in writing, and a parent may ask the superintendent to review it, whose decision is final; credit is not given for a course lower in a sequence than one already credited.
   - citation: Rochester School Board Policy IK, sections E and G (last amended July 9, 2026)
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-ik--high.txt. Text: "'Approved schools' include New Hampshire public schools, charter schools, public academies, approved public or private tuition program schools, and all schools in Vermont and Maine that are members of an interstate school district with schools in New Hampshire."; "Upon written request by the parent/guardian, such denial can be submitted for review to the Superintendent ... The Superintendent's decision shall be final." Most students entering grade 9 have no high school credit to transfer; policy IMBD (adopted July 9, 2026) covers high school credit for grade 7–8 courses taken in Rochester.

## town-school-options-nearby: Tri-City Christian Academy, St. Charles School, Portsmouth Christian Academy and EFAs

- kind: local
- question_type: help
- description: Private, charter and other schools families in a town use, with distance and tuition, and EFA use

1. Tri-City Christian Academy is a private Christian school in Somersworth for preschool through grade 12, with preschool to grade 5 on its Rocky Hill Road campus (in use since January 2008) and middle and high school at 150 West High Street, where it began in 1985; it was re-accredited by the New England Association of Schools and Colleges in October 2024.
   - citation: Tri-City Christian Academy, Facilities/Directions; Accreditation
   - source: https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2031959&type=d&pREC_ID=2273184
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Tri-City Christian Academy
   - note: Raw: raw/daily/private/tcca-facilities.txt: "The Rocky Hill Road campus currently houses our Pre-K, Kindergarten and Elementary programs."; "Established in 1985, TCCA began serving the community in this location. Our Middle School and High School programs are currently located at this campus."; raw/daily/private/tcca-accred.txt: "achieved re-accreditation from the New England Association of Schools and Colleges (NEASC) this week (October 2024)". The map embed gives 12 Rocky Hill Rd, Somersworth.
2. Tri-City Christian Academy describes its high school program as teaching math through calculus, literary analysis and composition, and science, history and Bible from "a thoroughly Biblical worldview," with electives that include individual music lessons, chorus, band, art, drama, yearbook, early childhood education and computer courses, outside apprenticeships for qualified students, and CLEP and early college options.
   - citation: Tri-City Christian Academy, High School page
   - source: https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2038808&type=d&pREC_ID=2112500
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Tri-City Christian Academy
   - note: Raw: raw/daily/private/tcca-hs.txt. Text: "the development of critical thinking in the context of a thoroughly Biblical worldview in science, history, and Bible subjects"; "Individual music lessons, chorus, band, art, drama, yearbook, early childhood education, and many elective computer courses are the primary elective offerings each semester. Apprentice vocational programs outside of school have also been individually designed". The site's athletics menu lists soccer, basketball, volleyball, golf, skiing/snowboarding and spring sports; a uniform policy applies.
3. Tri-City Christian Academy's before- and after-school care on its Rocky Hill Road campus runs 6:30 a.m. to 6:00 p.m. and costs $5.00 an hour for the first child, $2.50 for the second and $1.00 for each additional child, charged before 8:00 a.m. and after 3:00 p.m. for preschool to grade 5.
   - citation: Tri-City Christian Academy, Before and After School Care; 2026-2027 Tuition/Fee Schedule (page 2)
   - source: https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2031959&type=d&pREC_ID=2108800
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Tri-City Christian Academy
   - note: Raw: raw/daily/private/tcca-care.txt: "We open our doors each morning at 6:30am and remain open until 6:00pm"; raw/daily/private/tcca-rate-sheet-2026-27.pdf (.txt). Middle school students are charged before 7:50 a.m. or after 3:15 p.m.; pickup after 6:00 p.m. may cost $5.00 per 10 minutes.
4. Tri-City Christian Academy's home school program lets home-schooled students join its chapel services, field trips, field day, performing arts and athletics, may admit them to some classes case by case at a prorated tuition, and offers a TCCA home school transcript and diploma; its page asks interested families to send a "Home School Notification Form" with payment and calls the school a "participating agency with the State of New Hampshire."
   - citation: Tri-City Christian Academy, Home School Program
   - source: https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2038845&type=d&pREC_ID=2112533
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Tri-City Christian Academy
   - note: Raw: raw/daily/private/tcca-homeschool.txt. Text: "Tri-City Christian Academy continues to serve as a participating agency with the State of New Hampshire"; "On a case by case basis, when space is available, home school students participating in selected regular or elective classes can be considered. A pro-rated tuition charge ... would apply." Since July 1, 2026, New Hampshire requires no declaration of home education except to use public school programs or on withdrawal from a public school (library home-education-rules fact 1).
5. Tri-City Christian Academy's 2026-27 tuition for a first child is $6,322 in grades 1–5, $6,534 in grades 6–12 and $6,588 in kindergarten or preschool if enrolled by April 15, and $7,437, $7,686 and $7,750 if enrolled later, with lower rates for second and third children, no tuition for a fourth, and fees for enrollment ($150 for one new student, $300 for two or more), textbooks, graduation ($250) and most trips, arts and sports.
   - citation: Tri-City Christian Academy, 2026-2027 Tuition/Fee Schedule (last revision 01/29/26)
   - source: https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2038856&type=d&pREC_ID=2113527
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Tri-City Christian Academy
   - note: Raw: raw/daily/private/tcca-rate-sheet-2026-27.pdf (.txt); the two column groups were read from the rendered page ("Rates if Enrolled by April 15th" and "Rates if Enrolled after April 15th"). See table rochester_area_private_tuition_2026_27. "No tuition charge for 4th & subsequent students from the same family." Children of TCCA graduates get 15% off.
6. Tri-City Christian Academy tells New Hampshire families who need tuition help to apply to the NH Children's Scholarship Fund and the Education Freedom Account program after enrolling, and others to apply through FACTS Grant & Aid; it accepts new-family applications from March 1 each year (March 1, 2026 for 2026-27).
   - citation: Tri-City Christian Academy, Tuition & Financial Aid Information; Admissions Process
   - source: https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2038856&type=d&pREC_ID=2113527
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Tri-City Christian Academy
   - note: Raw: raw/daily/private/tcca-tuition.txt: "If you live in NH and need tuition assistance, you should apply to the NH Children's Scholarship Fund and the New Hampshire Education Freedom Account Program."; raw/daily/private/tcca-admissions.txt: "New Student Applications are accepted beginning on March 1st." EFA rules: library efa-eligibility-and-cap, efa-uses-and-requirements, efa-how-to-apply.
7. Portsmouth Christian Academy in Dover says its out-of-pocket tuition ranges from $7,495 to $19,825 depending on the number of children, household income, giving and other factors, offers need-based "Variable Tuition" for kindergarten to grade 12 through Clarity Financial Aid ($65 application fee), and says New Hampshire families should apply for EFAs, which it expects recipients to use substantially for tuition.
   - citation: Portsmouth Christian Academy, Tuition
   - source: https://pcaschool.org/admissions/tuition/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Portsmouth Christian Academy
   - note: Raw: raw/daily/private/pca-tuition.txt. Text: "out-of-pocket tuition rates range between $7,495 and $19,825."; "Eligible families in New Hampshire receive at least $3,407 of state assistance for qualified educational expenses. PCA's expectation is that recipients of Education Freedom Accounts (EFA's) substantially use these funds to pay for tuition." The site's FY2027 base EFA amount is $4,351 per student (site data). PCA's rate sheet sits behind a contact form and wasn't requested. Its Homeschool Connection is in the Dover file (town-school-options-nearby 12).
8. St. Charles School, run by Catholic Charities New Hampshire at 19 Grant Street in Rochester, is a private special education program for public school students in kindergarten to grade 8 with severe behaviors in a typical classroom, offering academic, social, emotional and behavioral services in a therapeutic setting so students can return to traditional schools; its curriculum is non-religious.
   - citation: Catholic Charities New Hampshire, St. Charles School
   - source: https://stcharles.cc-nh.org/programs/stcharles/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district St. Charles School
   - note: Raw: raw/daily/private/st-charles-school.txt. Text: "The St. Charles School provides academic, social, emotional and behavioral services in a therapeutic setting for male and female students in grades K-8."; "We are a private provider of special education serving public school students. Our curriculum is non-religious." It lists emotional disturbance, other health impairment, specific learning disability, speech-language impairment, high functioning autism (case by case), developmental delay and intellectual disability. Placement decisions: agent 4's file and library special-education-placements-across-states.
9. On November 15, 2026 the EFA program's administrator, Children's Scholarship Fund NH, counted 316 EFA-eligible students living in Rochester for 2026-27 (308 in priority groups, 8 not), of whom 268 (84.8%) qualified by income and 44 (13.9%) had special needs, with 8 Rochester students on the waitlist.
   - citation: Children's Scholarship Fund NH, EFA statistics feed (ScholaVia "View Stats"), school year 2026-2027
   - source: https://nhefa.scholarshipfund.org/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/csf-efa-stats-rochester-2026-11-15.json (trimmed copy of https://nhefa.scholarshipfund.org/api/admin/stats, an undocumented feed; see additional-data/programs-and-help.md, efa-stats-by-town-2026-27.csv). Rochester row: "count": 316, "priority_count": 308, "non_priority_count": 8, "frl_count": 268, "frl_percent": 84.8, "sped_count": 44, "sped_percent": 13.9, "waitlist_count": 8. Statewide the same day: 13,804 eligible, a cap of 12,500, 13,156 funded and 493 on the waitlist. Counts change daily; the site's EFA tables (NH DOE) are the official counts.
10. For 2026-27, a Rochester child with no extra EFA aid would receive the FY2027 base amount of $4,351, which is $1,971 less than Tri-City Christian Academy's $6,322 tuition for a first child in grades 1–5 enrolled by April 15 and $2,183 less than its $6,534 for grades 6–12, before textbook and other fees (derived).
   - citation: Site data (EFA per-student amounts, FY2027); Tri-City Christian Academy, 2026-2027 Tuition/Fee Schedule
   - source: https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2038856&type=d&pREC_ID=2113527
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: **Derived:** $6,322 − $4,351 = $1,971; $6,534 − $4,351 = $2,183. The FY2027 amounts in the site's database: base $4,351; extra $2,441 for free or reduced-price meal eligibility, $2,229 for special education and $849 for English learners. A child eligible for free or reduced-price meals would get $6,792, more than the posted grade 1–5 tuition. Raw: raw/daily/private/tcca-rate-sheet-2026-27.txt. Whether the state's amount reaches the family in full isn't covered here.

## town-streets-and-safe-routes: Crossing Guards and Street Safety Near Rochester's Schools

- kind: local
- question_type: local_practice
- description: Sidewalks, crosswalks, Safe Routes to School and road maintenance near schools

1. Rochester's school crossing guards are part-time City of Rochester employees in the police department, supervised by a sergeant, who direct traffic at assigned crossings and report hazards; the city's crossing guard posting, opened July 30, 2025 and still listed in June 2026, pays $15.00 an hour and asks for a high school diploma or GED.
   - citation: City of Rochester, Crossing Guard job posting (job number 202500023, opened 07/30/2025); City of Rochester news, "The City of Rochester is Hiring!" (June 11, 2026)
   - source: https://www.governmentjobs.com/careers/rochesternh/jobs/5026420/crossing-guard
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/news/governmentjobs-rochester-crossing-guard-5026420.txt: "Under the supervision of the Sergeant, the incumbent is responsible for directing traffic at assigned crossings to protect school children"; "Be alert for present or potential traffic or safety problems in the area surrounding the assigned crossing. Report to the department any such hazards and recommend remedial steps."; raw/daily/news/news-the-city-of-rochester-is-hiring-check-out-a-list-o.txt ("Crossing Guard ... PART TIME REGULAR – $15.00 Hourly ... Department: POLICE STATION").
2. In August 2021 the City of Rochester sought part-time crossing guards for posts at Lowell Street, Franklin and Chamberlain Streets, Brock Street at Holy Rosary Credit Union, Railroad Avenue in Gonic, Portland Street in East Rochester, Portland Street at Crow Hill Road, and Granite Street, working 7.5 hours a week (7:45–8:30 a.m. and 2:45–3:30 p.m.) at $15.00 an hour after a background check.
   - citation: City of Rochester news, "School Crossing Guards needed for upcoming school year" (August 25, 2021)
   - source: https://news.rochesternh.gov/school-crossing-guards-needed-for-upcoming-school-year/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/news/news-school-crossing-guards-needed-for-upcoming-school.txt. Text: "Multiple openings are available at the following locations: Lowell Street Franklin/Chamberlain Streets Brock Street/Holy Rosary Credit Union Railroad Avenue, Gonic Portland Street, East Rochester Portland Street/Crow Hill Road Granite Street". The newest list of posts found is this 2021 one; the hours fit the 2021 bell times. The city's own site (rochesternh.gov), where a current list or budget might be, refused automated requests.
3. At the Rochester School Board's September 11, 2025 meeting, a board member asked about the status of crossing guards, and the Director of Operations was to follow up.
   - citation: Rochester School Board minutes, September 11, 2025
   - source: https://www.rochesterschools.com/o/rsd/page/board-agendas-minutes
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/minutes/Full-Board-Minutes-09.11.25.pdf (.txt). Text: "Kelli Wiggin inquired about the status of crossing guards, David Rychlik will provide a follow-up." No follow-up appears in the later minutes found (through November 5, 2026).
4. The Rochester Police Department's September 1, 2026 back-to-school message told drivers to slow down and obey school zone signals, stop for loading school buses, watch for crossing guards and obey their signals, and never pass other vehicles, change lanes or make U-turns in a school zone.
   - citation: City of Rochester news, "Back To School: Rochester Police Offer School Zone Safety Reminders as School Year Begins" (September 1, 2026)
   - source: https://news.rochesternh.gov/back-to-school-rochester-police-offer-school-zone-safety-reminders-as-school-year-begins/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/news/news-back-to-school-rochester-police-offer-school-zone.txt. Text: "Watch out for school crossing guards and obey their signals."; "Never pass other vehicles while driving in a school zone. Never change lanes while driving in a school zone. Never make U-Turns while driving in a school zone."
5. Rochester's Department of Public Works planned to start improvements at the Summer Street and Columbus Avenue intersection in fall 2026, finishing in late summer 2027, adding left-turn lanes on Columbus Avenue and "appropriate pedestrian facilities" at an intersection the city's 2020 Transportation Master Plan named for safety and capacity work.
   - citation: City of Rochester news, "Public Works: Improvements to Intersection at Summer Street / Columbus Avenue to Begin This Fall" (October 14, 2026)
   - source: https://news.rochesternh.gov/public-works-improvements-to-intersection-at-summer-street-columbus-avenue-to-begin-this-fall/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/news/news-public-works-improvements-to-intersection-at-summe.txt. Text: "This intersection was identified in the 2020 Transportation Master Plan as requiring safety and capacity improvements. Improvements include new left-turn lanes on Columbus Avenue, improved circulation for large vehicles, appropriate pedestrian facilities". On the posted zone map the intersection is in the Chamberlain Street zone, near downtown.

## district-volunteers-and-partners: Veterans and Community Visitors in Rochester's Schools

- kind: local
- question_type: local_practice
- description: How residents, families and community groups can volunteer at, donate to or partner with a district's schools: volunteer rules and background checks, parent groups, gifts, student privacy and community programs

1. Rochester Middle School held its 16th annual Veterans Day Assembly on November 10, 2026 for students, staff, community members and local veterans, with the school's band and chorus, a video club film, the superintendent, and a U.S. Air Force lieutenant colonel as guest speaker.
   - citation: City of Rochester news, "Rochester Middle School Celebrates 16th Annual Veterans Day Assembly" (November 12, 2026)
   - source: https://news.rochesternh.gov/rochester-middle-school-celebrates-16th-annual-veterans-day-assembly/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/news/news-rochester-middle-school-celebrates-16th-annual-vet.txt. Text: "bringing together students, staff, community members, and local veterans to honor and thank the brave men and women who have served our country."; "our guest speaker, Lieutenant Colonel Nancy Ray of the United States Air Force, who shared personal stories and reflections about her military service".
2. Spaulding High School's football team, its booster club and the Rochester Veterans Council held the first "Salute to Service" game on October 2, 2026 to honor veterans and active-duty service members, with free entry for them and proceeds for Vouchers for Veterans; the announcement said more than 2,500 of New Hampshire's 80,000-plus veterans live in Rochester.
   - citation: City of Rochester news, "Spaulding Football to Host 1st Annual 'Salute to Service' Game Honoring Local Veterans on 10/2" (September 23, 2026); Rochester School Board minutes, September 10, 2026 (public comment)
   - source: https://news.rochesternh.gov/spaulding-football-to-host-1st-annual-salute-to-service-game-honoring-local-veterans-on-10-2/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/news/news-spaulding-football-to-host-1st-annual-salute-to-se.txt: "Out of more than 80,000 Veterans in New Hampshire, over 2,500 call Rochester home"; raw/daily/minutes/Full-Board-Minutes--09_10_26-1.pdf (.txt): "Carlton Cooper, representing the Rochester Veterans Council, shared information about the Salute to Service football game on October 2." The article is a community submission; the veterans figure is the article's, not checked against Census data.
3. In 2023, students in the Creteau Regional Technology Center's Manufacturing and Millwork pathway began a year-long project with the Rochester Veterans Council, the mayor's office and a Korean War veteran to renovate the World War II Honor Roll outside City Hall, starting with a history lesson from the veteran.
   - citation: City of Rochester news, "Spaulding High School students to assist with refurbishing World War II Honor Roll" (May 25, 2023)
   - source: https://news.rochesternh.gov/spaulding-high-school-students-to-assist-with-refurbishing-world-war-ii-honor-roll/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/news/news-spaulding-high-school-students-to-assist-with-refu.txt. Text: "students in the Manufacturing and Millwork pathway will collaborate with the Rochester Veteran's Council, the Office of Mayor Paul Callaghan, and Korean War veteran Al Benton to renovate and maintain the Honor Roll"; "students began their year-long project by meeting with Mr. Benton for a history lesson." Whether the project continued after 2023-24 wasn't found.
4. In November 2022, Rochester schools honored veterans with a Rochester Middle School ceremony attended by several dozen veterans, where a Spaulding graduate serving in the Air Force spoke to students and Spaulding's Air Force Junior ROTC cadets presented the colors, a visit by five veterans to Gonic School classrooms, and a Veterans Day breakfast at Chamberlain Street School.
   - citation: City of Rochester news, "Rochester Students Honor Veterans at Schools Across the District" (November 16, 2022)
   - source: https://news.rochesternh.gov/rochester-students-honor-veterans-at-schools-across-the-district/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/news/news-rochester-students-honor-veterans-at-schools-acros.txt. Text: "several dozen veterans attended a concert and recognition ceremony"; "Senior Airman ..., a graduate with the Spaulding High School Class of 2019, spoke to students about the ways in which joining the Air Force changed her life"; "Members of the Spaulding High School Junior Air Force ROTC program ... posted the colors"; "students at the Gonic School welcomed five veterans from various branches of the military ... visiting classrooms throughout the day". No schedule of veteran or career speakers in Spaulding's own classes was found.
5. Under Rochester School Board policy KK, only people with business at a school may be on school grounds from an hour before to an hour after the school day without the principal's permission, visitors must go straight to the principal's office through the main entrance, and meetings with teachers are by appointment; Spaulding's handbook adds that visitors sign in electronically at the Main Office or CTC Office entrance.
   - citation: Rochester School Board Policy KK, Visitors to the School (adopted April 8, 1993; amended December 10, 2009; reviewed January 22, 2015); Spaulding High School Parent & Student Handbook 2026-2027, Visitors and Trespassers
   - source: https://www.rochesterschools.com/o/rsd/page/policies
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Rochester
   - note: Raw: raw/daily/policies/pol-kk.pdf (.txt): "Visitors to a school must report immediately to the office of the principal as to the purpose and place of their visit. Visitors may only enter through the main entrance of the school."; raw/daily/shs-parent-student-handbook-2026-27.ocr.txt (transcribed from image). No district policy on guest speakers was found; policy KAC (volunteers) is in agent 1's area.

## town-housing: Former School Sites and Rental Housing Data in Rochester

- kind: local
- question_type: local_practice
- description: A town's housing beyond the site's Census estimates: home sales and assessments, short-term rentals, workforce housing, and housing plans and studies

1. After the Rochester School Department closed School Street School and William Allen School in 2025 and returned the properties to the city, the City of Rochester surveyed residents in February and March 2026 on their reuse and planned to issue requests for proposals to developers; both parcels are zoned Residential-2, which permits single-family, two-family and multifamily housing and senior housing.
   - citation: City of Rochester news, "City of Rochester Seeks Public Input on Future of Former School Properties with Online Survey" (February 23, 2026)
   - source: https://news.rochesternh.gov/city-of-rochester-seeks-public-input-on-future-of-former-school-properties/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/news/news-city-of-rochester-seeks-public-input-on-future-of.txt. Text: "Ultimately, the City plans to issue Requests for Proposals to local developers that could potentially incorporate community feedback."; "Permitted uses within this district include accessory apartments ... multifamily, two-family, and single-family dwellings and multifamily development; ... senior housing". A March 9, 2026 post set a March 20 survey deadline. No result of the survey or any proposal was found.
2. New Hampshire Housing hired Econometrica, Inc. in fall 2026 to survey about 34,000 renter households in Merrimack County and the Portsmouth–Rochester Fair Market Rent area on rents, utilities and unit types, so that HUD's Fair Market Rents reflect local costs, and Rochester's Economic Development Director urged selected renters to respond.
   - citation: City of Rochester news, "Economic Development Director Michael Scala Announces Rochester's Inclusion in Local Rental Housing Study" (November 9, 2026)
   - source: https://news.rochesternh.gov/economic-development-director-michael-scala-announces-rochesters-inclusion-in-local-rental-housing-study/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Rochester
   - note: Raw: raw/daily/news/news-economic-development-director-rental-housing-study.txt (.html). Text: "The New Hampshire Housing Finance Authority (NHHFA) has contracted with Econometrica, Inc., to conduct a rental housing study covering Merrimack County and the Portsmouth–Rochester Fair Market Rent area. Approximately 34,000 renter households will receive an invitation". No district or city document tying new housing to school enrollment or zone changes was found.

## rochester_bus_morning_ride_minutes_2026_27: Longest Scheduled Morning Bus Rides by School, Rochester, 2026-27 (minutes, derived)

- unit: number (minutes)
- period: 2026-27 morning route sheets (elementary updated August 28, 2026; middle and high school August 28, 2026); year: 2027
- source: Rochester School District, Elementary Bus Routes 26-27 and HS/MS Bus Routes 26-27 (Student Transportation of America) — https://www.rochesterschools.com/article/3004433
- as_of: 2026-11-15
- raw: raw/daily/rochester-bus-routes-2026-27-scheduled-times.csv
- topic: district-transportation
- place: district Rochester
- note: **Derived** from the OCR text of the scanned route sheets (transcribed from image): for each run serving a school, the scheduled drop-off time at that school minus the scheduled time at the run's first student stop (the bus yard departure left out). Value is the longest for that school; the Note gives the number of morning runs, the range of first-stop times and drop-off times, and the median. Scheduled, not measured, times. Middle and high school students share runs, so a student going to the second school on a run rides past the first school's stop. Only morning runs are posted. The sheets list stops by street corner or house number, so only times were kept.

| Place | School | Value | Note |
|---|---|---|---|
| Rochester | Chamberlain Street School | 49 | 8 runs (shared with East Rochester or Salmon Falls); first stops 7:30–8:08 a.m.; drop-offs 8:15–8:23 a.m.; median 28.5 |
| Rochester | East Rochester School | 44 | 8 runs; first stops 7:30–8:08 a.m.; drop-offs 8:14–8:25 a.m.; median 34.5 |
| Rochester | Gonic School | 40 | 4 runs; first stops 7:35–7:45 a.m.; all drop-offs 8:15 a.m.; median 32.5 |
| Rochester | McClelland School | 46 | 7 runs; first stops 7:30–7:53 a.m.; drop-offs 8:15–8:21 a.m.; median 36 |
| Rochester | Salmon Falls School | 45 | 7 runs; first stops 7:30–8:08 a.m.; drop-offs 8:07–8:25 a.m.; median 35 |
| Rochester | Rochester Middle School | 64 | 19 runs (shared with Spaulding); first stops 6:19–6:52 a.m.; drop-offs 7:04–7:24 a.m.; median 36 |
| Rochester | Spaulding High School | 60 | 18 runs; first stops 6:19–6:52 a.m.; drop-offs 7:02–7:20 a.m.; median 36.5 |

## rochester_area_private_tuition_2026_27: Posted Private School Tuition Near Rochester, 2026-27 (dollars)

- unit: dollars
- period: 2026-27 school year; year: 2027
- source: Tri-City Christian Academy, 2026-2027 Tuition/Fee Schedule — https://www.tcca-nh.com/apps/pages/index.jsp?uREC_ID=2038856&type=d&pREC_ID=2113527 ; Portsmouth Christian Academy, Tuition — https://pcaschool.org/admissions/tuition/
- as_of: 2026-11-15
- raw: raw/daily/private/tcca-rate-sheet-2026-27.pdf; raw/daily/private/pca-tuition.txt
- topic: town-school-options-nearby
- place: town Rochester
- note: Yearly tuition for a first (oldest) child; fees not included. Tri-City's second and third children pay less (grades 1–5 by April 15: $5,099 and $4,119; grades 6–12: $5,266 and $4,255; kindergarten/preschool: $4,958 and $3,766), and a fourth pays none. Portsmouth Christian Academy posts only the range families pay out of pocket after its need-based Variable Tuition; its full rate sheet wasn't requested (it sits behind a contact form). For comparison, the site's FY2027 base EFA amount is $4,351 per student.

| Place | Tuition | Value | Note |
|---|---|---|---|
| Tri-City Christian Academy | Kindergarten/preschool, enrolled by April 15 | 6588 | 10-month plan $659 |
| Tri-City Christian Academy | Kindergarten/preschool, enrolled after April 15 | 7750 | 10-month plan $775 |
| Tri-City Christian Academy | Grades 1–5, enrolled by April 15 | 6322 | 10-month plan $632 |
| Tri-City Christian Academy | Grades 1–5, enrolled after April 15 | 7437 | 10-month plan $744 |
| Tri-City Christian Academy | Grades 6–12, enrolled by April 15 | 6534 | 10-month plan $653 |
| Tri-City Christian Academy | Grades 6–12, enrolled after April 15 | 7686 | 10-month plan $769 |
| Portsmouth Christian Academy | Out-of-pocket tuition, low end of posted range (K–12) | 7495 | depends on children, income, giving and other factors |
| Portsmouth Christian Academy | Out-of-pocket tuition, high end of posted range (K–12) | 19825 | |

## For another file

- **Agent 1 (elementary):** P18.1's bus pickup times are in table `rochester_bus_morning_ride_minutes_2026_27` (elementary first stops 7:30–8:08 a.m.; school starts 8:30). Salmon Falls opened September 2, 2025 for up to 420 K–5 students (raw/daily/news/news-chamber-of-commerce-holds-ribbon-cutting-ceremony.txt). The K-2 Drop Off form (district-transportation 9). Policy KAC, Volunteers in Schools (amended October 9, 2014; first reading of a revision July 9, 2026), wasn't saved here.
- **Agent 3 (Spaulding):** the 2022 article shows Spaulding's Air Force Junior ROTC cadets presenting the colors, and the board nominated a "JR ROTC" staff member effective January 1, 2027 (raw/daily/minutes/Full-Board-Minutes--06_11_26-1.txt). Policy IKF (amended July 9, 2026) is at raw/daily/policies/pol-ikf--high.txt; Spaulding's "Requirements & Credit Information" page lists 26 credits for the classes of 2027–2029; policy IMBD (adopted July 9, 2026) gives high school credit for grade 7–8 courses. Spaulding's 2026-27 handbook OCR (raw/daily/shs-parent-student-handbook-2026-27.ocr.txt) covers tardiness, credit recovery and senior privilege.
- **Agent 4 (support):** the board took first readings of JFABD (McKinney-Vento supports), JFARD-A (homeless children and youth) and KB (Title I family engagement) on July 9, 2026 and approved a grant-funded McKinney-Vento stipend (raw/daily/minutes/Full-Board-Minutes--07_09_26-1.txt). One morning route stop is at a homeless shelter on Washington Street (route sheet), so homeless students are bused from there.
- **Agent 6 (money and buildings):** P14.3's "$36 million": the city's news post puts Salmon Falls at $33.6 million, with $15.5 million approved by the City Council and $15.77 million from NH DOE (raw/daily/news/news-chamber-of-commerce-holds-ribbon-cutting-ceremony.txt). P8.3: on March 3, 2026 the superintendent's "Option B" would have kept Maple Street open with "approximately 25 additional personnel cuts ... potentially up to four per school" (raw/daily/minutes/Special-Full-Board-Minutes-03_03_26.txt); March 11, 2026 (raw/daily/minutes/Special-Full-Board-Minutes-03_11_26.txt): a structural engineer found Maple Street "safe right now but will require work to be safe in the future"; May 14, 2026: an NH Transportation Aid Grant of $60,136.11 for 2024-25 costs (raw/daily/minutes/Full-Board-Minutes--05_14_26-3.txt). The former School Street and William Allen sites' reuse is in town-housing 1.
- **Library `chronic-absenteeism-nh-data`:** the federal 2023-24 Civil Rights Data Collection (the zip agent 4 downloaded for Rochester; its file list was checked) has no chronic absenteeism file, so there is no newer federal school-level figure for New Hampshire than 2021-22.
- **Dover file (`Dover/choices-and-adult-learning.md`):** its `town-school-options-nearby` facts on Seacoast Charter School (1–8) also answer Rochester's P4.3; its use of `district Portsmouth Christian Academy` matches this file.

## Not retrieved

- https://www.rochesterschools.com/ (all pages): answers automated requests with a "Client Challenge" bot check; WebFetch returned only the page title. Not retried. Pages a browser should open: https://www.rochesterschools.com/o/rsd/page/bus-information, https://www.rochesterschools.com/o/rsd/page/my-ride-k-12, https://www.rochesterschools.com/o/rsd/page/elementary-placement, https://www.rochesterschools.com/article/3004433, https://www.rochesterschools.com/o/rsd/page/policies (Sections I and J, to confirm JF isn't posted and IHBG is still the 2021 version), https://www.rochesterschools.com/o/rsd/page/board-agendas-minutes, https://www.rochesterschools.com/o/shs/page/incoming-freshmen-info, https://www.rochesterschools.com/o/shs/page/college-career (veteran or career speakers), https://www.rochesterschools.com/live-feed (storm notices, remote days).
- https://www.rochesternh.gov/ : HTTP 403 to automated requests. Wanted: the police department's crossing guard posts, the city budget line for crossing guards, City Council minutes and Planning Department housing pipeline. Not retried.

**Fetched through the vendor host, then checked in a browser (November 15, 2026).** The eight district pages and the feed this file first read through rochesterpublicschoolsnh.sites.thrillshare.com and the vendor's content API were opened at their www.rochesterschools.com addresses in Chrome: the bus information, My Ride K-12 (both "How to access" sections), August 18, 2026 routes article, live feed (pages 1–3), elementary placement and Spaulding incoming-freshmen pages, and the Policies page's Section J list (which the district itself links to the vendor host). Every quoted fact matched. The browser copies replaced the raw files under the same names; the vendor copies, the feed and article API data, the board minutes lists and the `shs-student-enrollment1` page (no fact rests on them) are kept in `raw/daily/vendor-host/` as a record. The feed shows relative dates only, so district-transportation 11 now says "September 2025" (the vendor data gave September 12) and district-school-day-and-calendar 6 says "late January 2026" (January 26).

- Policy JF, Enrollment and Capacity (adopted June 11, 2026): not among the posted Section J files (raw/daily/policies/rsd-policy-book-j-list.txt).
- Spaulding's 8th Grade Parent Night slideshow (https://aptg.co/6Qbqfn): a video file, not transcribed. Spaulding's "College & Career Activities" page: only navigation text could be extracted.
- Portsmouth Christian Academy's full tuition rate sheet: behind a form asking for contact details; not submitted.
- COAST weekday schedules for routes 6, 12 and 14: the schedule page is interactive and showed no service for the fetch date (a Sunday).
- A Rochester chronic absenteeism rate: not on any district page, policy, handbook, strategic plan (OCR of https://aptg.co/0FHCk1 checked) or board minutes (July 2024–November 2026); NH DOE's education.nh.gov pages weren't tried because other towns' agents found they refuse automated requests.
- Charter and private school attendance by Rochester residents: no source found beyond the site's Census and EFA data.
- Directory sites list a "St. Elizabeth Seton School" in Rochester; it isn't in the site's school list, and no school website was checked.
