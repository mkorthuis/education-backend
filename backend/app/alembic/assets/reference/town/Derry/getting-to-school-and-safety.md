# Getting to School, the School Day and Safety in Derry

Part of the Derry research (town/Derry). Gathered November 15, 2026.

## Summary

This file covers how Derry students get to school and what surrounds the school day: the 2026-27 start times and why they changed, the three-tier bus system run by First Student (including the buses to Pinkerton Academy), bus eligibility and stop changes, scheduled ride times on every posted route, late and activity buses, before- and after-school care at the schools, storm closings and Emergency Remote Learning Days, walking and crosswalks, traffic around Pinkerton Street, school resource officers, building entrances and security grants, and how the district and Pinkerton tell families about emergencies.

- **7 topics, 72 facts, 2 number tables.** Places: `district Derry Cooperative` for SAU 10's schools, buses, policies and handbooks; `district Pinkerton Academy` for Pinkerton's own bell schedule, drop-off map, bus lineup, crisis communications and security grants; `town Derry` for police and school resource officers, the Highway Safety Committee, road projects, CART public transit and the Boys & Girls Club.
- **New data concepts:** scheduled ride times for all 150 posted 2026-27 routes (derived; table `derry_bus_scheduled_ride_minutes_2026_27`); the old and new start times and the board's reasons; the fleet size (29 large buses, down from 34); the town's school resource officer staffing and Pinkerton's payments for it; per-school 2026 SAFE security grants (table `derry_safe_grants_2026`); Pinkerton's crisis-communication rules and its drop-off and afternoon bus layout; the Exit 4A road work at Pinkerton Street.
- **Main sources:** SAU 10 pages (transportation, school hours, closure procedures), the 2026-27 district and school handbooks (Google Docs), board policies EEA, EBCD, IMBA, IC, KI, EBCA, EBCC and ECE, school board minutes (March to October 2026) and the board's "At a Glance" summaries, the 2026-27 route sheets and calendar, Pinkerton Academy pages, the Town of Derry FY2027 adopted budget, Town Council minutes (June 30 and September 1, 2026), Highway Safety Committee minutes (scanned; read by OCR), NHDOT's Exit 4A project site, the Boys & Girls Club of Greater Derry and Manchester Transit's CART page.
- **Premises checked:**
  - "The elementary start time pushed to 8:50 AM" (P1.1): correct. On April 14, 2026 the board moved elementary hours from 8:35–2:55 to 8:50–3:10 for 2026-27, and grades 5–8 40 minutes later.
  - "Crossing guards at the busy intersections" near Grinnell (P11.2): no town or district crossing guards were found. Grinnell's handbook says school staff stand at the crosswalk, sidewalk and drop-off from 8:40 and walk children across.
  - Bus routes in East Derry "taking almost an hour each way" (P21.2): not shown in the posted schedules. The longest scheduled ride on any 2026-27 route is 42 minutes in the morning (a Pinkerton route and a West Running Brook route) and 47 minutes in the afternoon (a West Running Brook route); East Derry Memorial's longest is 39. Scheduled times are not measured times, and no actual ride times are published.
  - Snow days "or remote learning days" (P16.2): both are possible. Board policy allows Emergency Remote Learning Days, but the district also closes for traditional snow days (for example March 6, 2026). No remote learning day was found in the 2025-26 or 2026-27 sources read.
  - School resource officers "in every building every day" (P18.1): no. The town's SROs have been assigned to Pinkerton (two), West Running Brook and, for part of 2025-26, Hood; on September 22, 2026 the superintendent said police staffing means there are currently no SROs, with police doing drive-bys and walkthroughs instead.
  - A Pinkerton bus stop "on Crystal Ave" and late buses (P5.3): the posted 2026-27 routes list no stop on Crystal Avenue and no late or second Pinkerton run.
  - Pinkerton Street "gridlocked at 2:30 PM" (P13.3): congestion can't be measured from the sources. Pinkerton's buses leave at 1:58; Hood (2:30) and West Running Brook (2:35) now dismiss in that window, after the 2026-27 change moved them 40 minutes later.
  - Late buses from Hood (P26.1): none found. A Boys & Girls Club bus picks up activity students at 4:00.
- **Questions answered wholly by earlier files:** 0 of 12. No earlier town is in SAU 10; the library supplied only the child care scholarship topics and the site's child care data.
- **Main gaps:** any measured ride times or a study of the West Running Brook drop-off line; crossing guard posts, if any; the Greater Derry Extended Day Program's rates and waitlists (no website found); news of specific lockdowns or social-media threats in 2025-26 (the web search budget ran out before news could be searched, including the "May 20 incident" the June 9 minutes mention at Pinkerton); whether Derry has used an Emergency Remote Learning Day since 2021; the ages of Grinnell and East Derry Memorial (agent 7's facilities area).
- **Privacy:** the route sheets list stops by house number, and one sheet's text layer contains what looks like a person's name. They were read only to compute times; they were not copied into `raw/`, and no address or name is used. A derived CSV of route times (no stops) is saved instead. Highway Safety Committee and board minutes name residents who spoke; facts leave those names out. Nothing with personal information was sent to any outside service; OpenStreetMap Nominatim was asked only for four school addresses, with the `nhfacts-research` identifier.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.1 Elementary start pushed to 8:50; making an 8:00 shift without costly before-school care | district-school-day-and-calendar 1–3, 5, 7–9; town-recreation-and-summer 1–2; site data: child_care (the Greater Derry Extended Day Program's licensed sites at Barka, Grinnell, South Range and West Running Brook, hours from 7:00 a.m., 6:45 at West Running Brook, accept the NH Child Care Scholarship; no rates listed); library: child-care-scholarship-eligibility, child-care-scholarship-how-to-apply | partial | **Premise correct** (8:35 to 8:50). The district runs no before-school care; staff supervise from 8:40 (Barka drop-off from 8:25). An independent nonprofit runs Extended Day care inside the elementary schools; at Barka it opens at 7:00 a.m. with a daily or weekly fee. Its rates aren't posted. The Boys & Girls Club is after school only ($160 a month). |
| P3.2 West Running Brook drop-off line; is anyone fixing the traffic flow | district-school-day-and-calendar 1–4, 11; district-transportation 7, 10; town-streets-and-safe-routes 1, 3, 11; district-safety-and-security 12 | partial | The 2026-27 schedule moved West Running Brook from 7:20 to 8:00 and gave grades 5–6 their own bus tier; in September 2026 the transportation director said intermediate arrivals are on time. **No study or plan for the drop-off line was found**, and West Running Brook's handbook gives no car-line procedure. Traffic concerns go to the town's Highway Safety Committee, which has a school representative. |
| P5.3 Missed Pinkerton bus on Crystal Ave: late buses or backup rides | district-transportation 1–4, 6–8, 14, 16 | partial | **No late or second Pinkerton run** is in the posted routes; all 19 morning runs reach Pinkerton at 6:45. No posted stop is on Crystal Avenue (Pinkerton riders must live more than two miles away). Pinkerton doesn't run buses; questions go to First Student, 603-432-7417. CART public transit starts at 8:00 a.m., after Pinkerton's 7:15 start. Pinkerton's attendance rules are agent 2's. |
| P11.2 Walking to Grinnell from downtown; crossing guards | town-streets-and-safe-routes 2, 4–6; district-transportation 3, 13 | partial | **No crossing guards found.** Grinnell staff are at the crosswalk, sidewalk and drop-off from 8:40 and cross walkers at the playground entrance; walkers leave first at dismissal. Children within one mile get no bus unless the board waives the distance for a hazard. In May 2026 the town declined a mid-block crosswalk on West Broadway. |
| P13.3 Pinkerton Street gridlock at 2:30; is the town doing anything | town-streets-and-safe-routes 1, 8–11; district-transportation 7, 14; district-school-day-and-calendar 1, 19 | partial | Pinkerton dismisses at 1:58, with buses for seven towns along North Main Street; Hood (2:30, 13 routes) and West Running Brook (2:35, 16 routes) now dismiss near 2:30. NHDOT's Exit 4A project, meant to cut congestion on Route 102 through downtown, is widening Folsom Road up to Pinkerton Street (to June 2028) and adding a signal at Pinkerton Street and Tsienneto Road. **No town study of Pinkerton Street school traffic was found.** |
| P16.1 Affordable after-school program right at South Range, for last-minute schedule changes | district-school-day-and-calendar 7–9; town-recreation-and-summer 1–2; site data: child_care (Greater Derry Extended Day Program – South Range, licensed, accepts the scholarship) | partial | Extended Day runs inside South Range (and Grinnell, Barka, West Running Brook); rates and drop-in rules aren't posted; the Barka listing mentions a daily or weekly fee. The Boys & Girls Club buses from every Derry school but charges $160 a month with no daily option. Dismissal changes go through PickUp Patrol by 2:30 p.m., or a call to the office in an emergency. |
| P16.2 Snow days: cancel school or remote learning days | district-school-day-and-calendar 13–18; district-family-communication 1; town-recreation-and-summer 2 | full | **Premise partly correct** (see Summary). Closures are usually announced by 5:30 a.m. by call, text and email. Missed days are made up at the end of the year or during vacations, or the year can be counted in hours. The calendar's June 11, 2027 last day is "tentative". |
| P18.1 Are SROs in every building every day | town-emergency-services 1–3 | full | **Premise not correct** (see Summary). Pinkerton pays the town for its SROs ($304,351 budgeted for FY2027). |
| P18.2 How secure are the front entrances at Grinnell and East Derry Memorial | district-safety-and-security 1–7, 11; table derry_safe_grants_2026 | partial | Visitors sign in at the office and wear a sticker; visits need 24 hours' notice. In 2026 the board accepted SAFE security grants for every school (cameras; re-keying at Hood); district-wide re-keying finished in August 2026; a new intercom and mass-notification system was bought; the visitor-management system needed troubleshooting in September 2026. **The schools' entrance layouts (vestibules, buzzers) were not described in any source**; building ages are agent 7's. |
| P18.3 Lockdown drills and social-media rumors: how fast parents hear | district-family-communication 1–7; district-safety-and-security 8–10, 14 | partial | SAU 10's threat policy says families of the affected building are told under its crisis plan or "as soon as deemed appropriate"; no time limit is set. Pinkerton says it messages every family whenever it calls a Secure, Lockdown, Evacuate or Shelter, by ParentSquare email and text, and may not message for a Hold. **No account of a specific 2025-26 lockdown or rumor was found** (news not searched). |
| P21.2 East Derry bus routes taking almost an hour | district-transportation 4–5, 7, 9–11; table derry_bus_scheduled_ride_minutes_2026_27 | partial | **Premise not shown** (see Summary). Possible reasons in the sources: consolidated stops, three tiers sharing one fleet, 29 large buses (34 in earlier years) and driver shortages. Stop changes are requested through a district form reviewed by First Student; appeals go to the superintendent and then a three-member board committee. |
| P26.1 Late buses home from Hood after track and drama | district-school-day-and-calendar 10, 12; district-transportation 7, 11; town-recreation-and-summer 1 | partial | **No district late or activity bus was found**; Hood's handbook says students must be picked up promptly after activities. The Boys & Girls Club bus picks up activity students at Hood at 4:00 and takes them to the Club (open to 7:30 p.m.; $160 a month). A YMCA after-school program at Hood is free. Hood offers track and field and a drama club. |

## district-school-day-and-calendar: Derry's 2026-27 School Hours, Before- and After-School Care, and Storm Days

- kind: local
- question_type: local_practice
- description: School hours, before- and after-school care, the school calendar and vacations, and attendance and absence rules

1. In 2026-27 the Derry Cooperative School District's school hours are 7:55 a.m. to 2:30 p.m. at Gilbert H. Hood Middle School, 8:00 a.m. to 2:35 p.m. at West Running Brook Intermediate School and 8:50 a.m. to 3:10 p.m. at the four elementary schools; on early release days they dismiss at 12:25, 12:30 and 1:10 p.m., and the district's delayed opening is two hours.
   - citation: Derry Cooperative School District, School Hours
   - source: https://www.sau10.nh.gov/families/school-hours
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Page text: "School Start Times for 2026-2027 School Year ● Gilbert H. Hood Middle School: 7:55 AM – 2:30 PM (shifted 40 minutes later) ● West Running Brook Intermediate School: 8:00 AM – 2:35 PM (shifted 40 minutes later) ● Elementary Schools: 8:50 AM – 3:10 PM (shifted 15 minutes later)"; "Middle: Dismissal at 12:25 pm ... Intermediate: Dismissal at 12:30 pm ... Elementary: Dismissal at 1:10 pm"; "**The District observes a two-hour delay." Delayed opening hours: middle 9:55, intermediate 10:00, elementary 10:50. The library already has the DEEP preschool sessions and the elementary hours (district-practices). Raw: raw/daily/sau10-school-hours.txt
2. On April 14, 2026 the Derry Cooperative School Board voted 6 to 0, with one abstention, to change the school day for 2026-27 from 8:35–2:55 to 8:50–3:10 at the elementary schools, from 7:20–1:55 to 8:00–2:35 at West Running Brook and from 7:15–1:50 to 7:55–2:30 at Hood, after a committee met four times from November and a survey drew 1,400 responses.
   - citation: Derry Cooperative School Board minutes, April 14, 2026, "School Start Times"
   - source: https://drive.google.com/file/d/1_X7_H3L0JszeLDOAh8GifGl9BHF41ZjQ/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Minutes text: "The committee started back in November, with four meetings held. They had 1400 respondents to the survey ... - Elementary School: 8:35 a.m.-2:55 p.m. adjusted to 8:50 a.m.-3:10 p.m. (shifted 15 mins. later) - Intermediate School: 7:20 a.m.-1:55 p.m. adjusted to 8:00 a.m.-2:35 p.m. (shifted 40 mins. later) - Middle School: 7:15 a.m.-1:50 p.m. adjusted to 7:55 a.m.-2:30 p.m." "Vote : 6, Yes 1, Abstained". A board member said the committee "was split on whether they wanted to recommend this" and the superintendent said its vote was anonymous. Answers the P1.1 premise. Raw: raw/daily/minutes/sb-minutes-2026-04-14.txt
3. The Derry superintendent told the board in April 2026 that the new times let the same fleet run three separate bus runs (elementary, West Running Brook and Hood) and then return for Pinkerton, so students no longer wait long at Pinkerton or arrive very early at other schools for athletics, and that the change began with instructional time at West Running Brook; a board member said child care and getting to work on time were raised in the committee, and the board approved agreements with the teachers' and support staff unions on the effect on staff hours.
   - citation: Derry Cooperative School Board minutes, April 14, 2026; School Board at a Glance, April 2026
   - source: https://drive.google.com/file/d/1_X7_H3L0JszeLDOAh8GifGl9BHF41ZjQ/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Minutes text: "we will be able to run three different bus routes with the same fleet of buses. One is dedicated to elementary, one is dedicated to West, and one is dedicated to Hood. Then they will wrap back around and dedicate it to Pinkerton. This will help our efficiency; we will not have kids hanging out at Pinkerton anymore for a long period of time. We will not have our students arriving super early at other schools for athletics"; "There was interest in childcare, getting out to work on time ... it was what was in the best interest of the students"; "15 minutes a day added up to four school days"; "we have a shorter school day in comparison to local areas". At a Glance: "This change allows for three dedicated bus routes and eliminates long wait times for students at Pinkerton Academy." MOUs with the DEA and AFSCME passed 7–0. Raw: raw/daily/minutes/sb-minutes-2026-04-14.txt; raw/daily/sb-glance.txt
4. In October 2025 the Derry Cooperative School Board formed an advisory committee on start times to address the stress of the intermediate and middle schools starting at the same time as Pinkerton Academy and the early start for 5th and 6th graders.
   - citation: Derry Cooperative School District, School Board at a Glance, October 2025
   - source: https://www.sau10.nh.gov/school-board/school-board-at-a-glance
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Page text: "The committee aims to address stressors caused by intermediate and middle schools starting simultaneously with Pinkerton Academy, as well as the early 7:25 a.m. start time for 5th and 6th graders." The April 2026 minutes give West Running Brook's old start as 7:20 a.m.; the two sources differ by five minutes. Raw: raw/daily/sb-glance.txt
5. Derry's elementary schools don't run before-school care: staff supervision outdoors begins at 8:40 a.m. at East Derry Memorial, Grinnell and South Range (Barka's handbook says drop-off starts at 8:25 but that walkers should not arrive before 8:50), and the handbooks ask parents not to drop children off when no staff member is outside.
   - citation: Derry Cooperative School District 2026-27 family handbooks for East Derry Memorial, Ernest P. Barka, Grinnell and South Range, "School Hours" and "Arrival/Dismissal Procedures"
   - source: https://docs.google.com/document/d/1-VOKgszG-ycSCotPKOldJQ_vPSj-Qjs5R_Ua0nc3Qkw/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Grinnell: "Children should not arrive at school prior to 8:40AM as there is no staff supervision prior to 8:40AM. PLEASE DO NOT DROP OFF YOUR CHILDREN IF STAFF ARE NOT PRESENT OUTSIDE." South Range: "Students can be dropped off starting at 8:40 a.m." East Derry Memorial: "Students can be dropped off as early as 8:40 a.m." Barka: "Students can be dropped off starting at 8:25 a.m." and "Children who walk should not arrive at school before 8:50 a.m., when they are supervised". The school handbooks are linked from the district handbook (source). Raw: raw/daily/handbook-2026-27-grinnell.txt; raw/daily/handbook-2026-27-srs.txt; raw/daily/handbook-2026-27-eds.txt; raw/daily/handbook-2026-27-barka.txt
6. At West Running Brook in 2026-27 students may enter at 7:55 a.m. and the tardy bell rings at 8:00; at Hood supervision begins at 7:55 a.m. and students must be in advisory by 8:05.
   - citation: West Running Brook Intermediate School and Gilbert H. Hood Middle School handbooks, 2026-2027
   - source: https://docs.google.com/document/d/1jDUfo9RfYHbjRaWrr6LQuk2HE1cQwpN0-w57ImMfDUE/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: WRB: "Students can begin entering the building at 7:55 am and the tardy bell will ring at 8:00am." Hood (https://docs.google.com/document/d/1Bbd1s3ajl6O0k6g3EcmJCbFfYv3wql6IABfapMZZ4no/edit): "Supervision is available at 7:55 AM. School should be considered to be in session at 8:05 AM., when students move to their advisory." Raw: raw/daily/handbook-2026-27-wrb.txt; raw/daily/handbook-2026-27-ghh.txt
7. Before- and after-school care inside Derry's schools is run by the Greater Derry Extended Day Program, a nonprofit that operates independently within Barka, Grinnell, South Range and West Running Brook and is not affiliated with or funded by the school district (603-327-1334); East Derry Memorial has its own independent Extended Day Program (603-260-9578).
   - citation: Derry Cooperative School District 2026-27 school handbooks (Barka, Grinnell, South Range, West Running Brook, East Derry Memorial)
   - source: https://docs.google.com/document/d/1rqOhIR0X-03Dyh1DWh0qs7S-J_H0fsvQk3-0rylqRew/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: WRB: "The Greater Derry Extended Day Program is a nonprofit organization that operates independently within West Running Brook Intermediate School and is not affiliated with or funded by the school district." Grinnell: "operates independently within the Grinnell Elementary School". South Range's handbook (source) uses the same paragraph but says "within the Grinnell School", apparently copied; it lists "Extended Day Program (603) 327-1334" among its numbers, and the site's child care data has a licensed "Greater Derry Extended Day Program - South Range" at 1 Drury Lane. EDS: "The Extended Day Program is a nonprofit organization that operates independently within the East Derry Elementary School". No program website or rate sheet was found. Raw: raw/daily/handbook-2026-27-srs.txt; raw/daily/handbook-2026-27-grinnell.txt; raw/daily/handbook-2026-27-wrb.txt; raw/daily/handbook-2026-27-eds.txt; raw/daily/handbook-2026-27-barka.txt
8. Barka's handbook says its Extended Day Program, for children whose parents work, runs 7:00 to 8:50 a.m. and 3:10 to 6:00 p.m., charges a daily or weekly fee, requires enrollment, and gives children a snack, recreation and a quiet place to do homework.
   - citation: Ernest P. Barka Elementary School Family/Student Handbook 2026-2027, "Ernest P. Barka Extended Day Program"
   - source: https://docs.google.com/document/d/1FdCzVzhP1sfkH13nlTLCCcVpqoZB0Ss2C1qPnzwld7M/edit?tab=t.0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "There is a daily or weekly fee, and children must be enrolled in the program to participate. ... Hours of operation are from 7:00-8:50 a.m. and 3:10-6:00 p.m. After school, children are provided with a snack, recreation, and a quiet place to do homework with a helping hand." The fee amounts are not given. Raw: raw/daily/handbook-2026-27-barka.txt
9. Derry's elementary schools use PickUp Patrol for changes to a child's way home: changes must be entered by 2:30 p.m. at East Derry Memorial, Grinnell and South Range and by 1:30 p.m. at Barka (2:00 p.m. at West Running Brook), and families call the main office for an emergency change.
   - citation: Derry Cooperative School District 2026-27 school handbooks, "Arrival/Dismissal Procedures" and "Dismissal"
   - source: https://docs.google.com/document/d/1rqOhIR0X-03Dyh1DWh0qs7S-J_H0fsvQk3-0rylqRew/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: South Range: "ALL dismissal changes should be submitted through PickUp Patrol ... Please be sure to submit any changes to dismissal before 2:30 p.m. If you have an emergency and need to change your child's dismissal, please call our main office." Barka: "Please ensure that you submit any changes to dismissal by 1:30 p.m." WRB: "Pickup Patrol should be updated no later than 2:00pm." Bears on P16.1. Raw: raw/daily/handbook-2026-27-srs.txt; raw/daily/handbook-2026-27-barka.txt; raw/daily/handbook-2026-27-wrb.txt
10. Hood Middle School's 2026-27 handbook says students must be picked up promptly at the end of any after-school activity unless arrangements have been made with the Boys & Girls Club of Greater Derry, whose bus picks students up at Hood at 2:30 p.m. and again at 4:00 p.m. for students in after-school activities (fees go through the Club), and that the YMCA, with the district and the Marion Gerrish Community Center, offers a free after-school program at Hood.
   - citation: Gilbert H. Hood Middle School Handbook 2026-2027, "Dismissal" and "Boys & Girls' Club Middle School Program"
   - source: https://docs.google.com/document/d/1Bbd1s3ajl6O0k6g3EcmJCbFfYv3wql6IABfapMZZ4no/edit?tab=t.0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "Dismissal begins at 2:30 PM. ... All students must be picked up promptly at the end of any activity or detention unless prior arrangements have been made with the Boys and Girls' Club." "A bus picks students up at 2:30 PM and a second one returns at 4:00 to pick up students involved in after school activities. Any fees connected with these services will be processed through the Boys and Girls' Club." "The YMCA in collaboration with the Derry Cooperative School District and Marion Gerrish Community Center offers a free after school program at GHHMS. Please contact our office for more information." **No district late or activity bus is described** in the handbook or the posted routes (district-transportation 7). Answers P26.1. Raw: raw/daily/handbook-2026-27-ghh.txt
11. At West Running Brook the Boys & Girls Club bus picks students up at 2:35 p.m. (a second pickup time for activities was listed as "TBD" in the 2026-27 handbook), and in 2025-26 the school told families picking up from clubs to pull around the right side of the building, fill the left lane only and keep the right lane open.
   - citation: West Running Brook Intermediate School Handbook 2026-2027, "Boys & Girls' Club Program"; WRB News, September 5, 12 and 19, 2025
   - source: https://www.sau10.nh.gov/schools/wrb/news/1815261/wrb-news-9-19-25
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Handbook: "A bus picks students up at 2:35 PM and a second one returns at TBD to pick up students involved in after school activities." Newsletters (2025-26, the year before the schedule change): "Pick up for all clubs is at 3:00pm. During pick-up, please pull around the building on the right side and fill the left lane only. Please leave the right lane open." One club notice: "Transportation is not provided by the school; students in the club will need to be picked up or have permission to walk home." August 28, 2025: "Thank you for your cooperation during pick up and arrival! Each day things are getting more efficient." No 2026-27 newsletters are posted (they go out by ParentSquare). Raw: raw/daily/handbook-2026-27-wrb.txt; raw/daily/wrb-news-9-19-25.txt; raw/daily/wrb-news-8-28-25.txt
12. Hood Middle School's interscholastic sports are cross country, soccer, field hockey, cheerleading, basketball, baseball, softball, track and field, golf and lacrosse; its clubs include drama, art, yearbook, jazz band, select chorus, ski club and Lego club; and, as in all Derry schools, a student must be in school that day to take part after school.
   - citation: Gilbert H. Hood Middle School Handbook 2026-2027, "Athletics, Clubs & Activities"; Derry Cooperative School District Student & Family Handbook 2026-2027, "Clubs & Activities"
   - source: https://docs.google.com/document/d/1Bbd1s3ajl6O0k6g3EcmJCbFfYv3wql6IABfapMZZ4no/edit?tab=t.0
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "The following sports are offered at Gilbert H. Hood Middle School: Cross Country, Soccer, Field Hockey, Cheerleading, Basketball, Baseball, Softball, Track and Field, Golf, and Lacrosse." "Drama Club, Art Club, Yearbook Staff, Jazz Band, Select Chorus, Ski Club, Lego Club, and our Husky Herald." District handbook: "Students must be present in school to participate in after-school activities." Raw: raw/daily/handbook-2026-27-ghh.txt; raw/daily/sau10-family-handbook-2026-27.txt
13. SAU 10 decides on storm delays, early dismissals and closings ("traditional snow day or emergency remote learning day") with the Derry police and public works departments, its maintenance staff, First Student, Pinkerton Academy and nearby districts, and usually announces a delay or closing by 5:30 a.m. by phone call, text and email, on its website and social media, and on Boston and Manchester TV stations.
   - citation: Derry Cooperative School District, Closure Procedures
   - source: https://www.sau10.nh.gov/families/closure-procedures
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Page text: "school closures (traditional snow day or emergency remote learning day)"; "ongoing collaboration between the following personnel and municipalities occurs: Derry Police Department, Derry Public Works, Derry School District Maintenance Department, First Student, Pinkerton Academy, and other local school districts"; "An announcement for either a delay or closure is typically made by 5:30 am the morning of the decision. ... a telephone call/voice message, text, and email". TV: WBZ, WCVB, WMUR, WHDH, NECN. The 2026-27 district handbook says the automated message comes "at approximately 5:00 a.m." Raw: raw/daily/sau10-closure.txt; raw/daily/sau10-family-handbook-2026-27.txt
14. Derry's policy EBCD (January 2023) lets the superintendent delay opening by two hours (canceling the DEEP preschool's morning session, with after-school activities unaffected), close for the day (canceling all afternoon and evening programs), approve an Emergency Remote Learning Day announced together with the closing, or release students early, notifying families as soon as possible so they can arrange care and rides.
   - citation: Derry Cooperative School District Policy EBCD, Emergency School and District Closings (January 2023)
   - source: https://drive.google.com/file/d/1noUDmt8nukvKDb8dvy0zd9ctQDV0Bm7J/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "The public announcement will report a two-hour delayed opening, including the cancellation of the Derry Early Education Program morning session. ... after-school activities and events will not be affected by a delayed opening." "If school is closed for the entire day, all afternoon and evening programs shall also be canceled." "D. ... the Superintendent or designee may approve an Emergency Remote Learning Day for district-wide instruction. The Superintendent or designee will include the necessary information regarding the Emergency Remote Learning Day in the announcement that school has been canceled." "E. ... will notify families as soon as possible in order to allow for the arrangement of after-school care and transportation". The older policy EBCE (reviewed 2013), still linked from the handbook, says 90 minutes. Raw: raw/daily/sau10-policy-EBCD.txt; raw/daily/sau10-policy-EBCE.txt
15. Derry's policy IMBA (November 2021) says the district will call an Emergency Remote Learning Day when bad weather makes travel unsafe, that students and staff stay home and learn online, that the day counts toward the 180-day year or the required hours with regular attendance rules, that IEPs and 504 plans still apply, and that students check in for attendance, follow Google Classroom and attend scheduled live sessions.
   - citation: Derry Cooperative School District Policy IMBA, Distance Education & Remote Learning (November 2021)
   - source: https://drive.google.com/file/d/14Wc1zbAnJk-e_d92H4swZfVpvSH6J4nB/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "The District will initiate an Emergency Remote Learning Day when inclement weather causes unsafe transportation conditions ... all students and school-year educational staff remain home, and both teaching and learning are fully remote ... The Emergency Remote Learning Day will count toward the accumulation of either the required 180-day school year or instructional hours. Accordingly, regular attendance rules and procedures will apply". "Participate in an attendance check-in ... Attend all scheduled live sessions with educator(s)." Raw: raw/daily/sau10-policy-IMBA.txt
16. Derry's policy IC (revised February 2026) says school days lost to emergency closings are made up at the end of the year or during vacations as the board approves, or the year may instead be counted in hours, with the superintendent able to propose a revised schedule after many closings.
   - citation: Derry Cooperative School District Policy IC, School Year/School Calendar (revised February 2026)
   - source: https://drive.google.com/file/d/0B4MduX0xeMqJVzRLb3d4LThQYnM/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "Any days that the schools are closed for emergency reasons will be made up at the end of the school year or during recess periods, as approved by the Board upon the Superintendent's recommendation. ... Alternatively, the school year may consist of the number of hours as required by New Hampshire Department of Education Rules. In the event schools are closed for excessive days for emergency reasons, the Superintendent may recommend to the School Board a revised schedule". February 2026 At a Glance: "updated to reflect flexibility in instructional hours vs. days". Raw: raw/daily/sau10-policy-IC.txt; raw/daily/sb-glance.txt
17. Derry's 2026-27 calendar starts classes on August 25, 2026, has early release days on September 23, 2026 and May 18, 2027, half days on December 23, 2026 and June 11, 2027, and marks June 11, 2027 as the tentative last day of school; in February 2026 the board cut early release days from four to two in response to family feedback.
   - citation: Derry Cooperative School District 2026-2027 Calendar; School Board at a Glance, February 2026
   - source: https://drive.google.com/file/d/1ba1cNLWG02L6q2UuuJ58BeG90HBkwqW1/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Calendar text: "25: First Day of School"; "23: Early Release Day"; "18: Early Release Day"; "23: Half Day"; "11: Half Day: Tentative Last Day of School". Vacations: Thanksgiving November 25–27, December 24–31, February 22–26, April 26–30. The monthly counts printed on the calendar add to 179 student days (**derived**). At a Glance: "reduces the number of early release days from four to two in response to family feedback." Early release days are agent 3's P6.2. Raw: raw/daily/sau10-calendar-2026-27.txt; raw/daily/sau10-calendar-2026-27-p1.png; raw/daily/sb-glance.txt
18. On March 6, 2026 Derry's schools were closed because of icy roads, a regular closure rather than a remote learning day.
   - citation: Derry Cooperative School District alert, "School Closed, Friday, March 6, 2026"
   - source: https://www.sau10.nh.gov/alert/1617819/two-hour-delay-friday-march-6-2026
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "Due to the icy road conditions there is no school Friday March 6, 2026". The March 24, 2026 minutes mention an author visit at Grinnell "delayed because of the snow day". **No Emergency Remote Learning Day** was found in the board minutes (March–October 2026), the At a Glance summaries (July 2025–June 2026) or the district news page; earlier years were not searched. Raw: raw/daily/alert-20260306.txt; raw/daily/minutes/sb-minutes-2026-03-24.txt
19. Pinkerton Academy's regular 2026-27 bell schedule runs from 7:15 a.m. to 1:58 p.m.; on a two-hour delay classes start at 9:15 and still end at 1:58, early release days end at 12:23 p.m., and Pinkerton has a remote learning day schedule of four one-hour blocks from 8:00 a.m. to 12:30 p.m.
   - citation: Pinkerton Academy, Bell Schedule
   - source: https://www.pinkertonacademy.org/academics/bell-schedule
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Page text: "REgular Schedule ... R1/W1 7:15 AM 8:35 AM ... R4/W4 12:38 PM 1:58 PM"; "2 Hour Delay ... R1/W1 9:15 AM ... R4/W4 1:01 PM 1:58 PM"; "Early Release Days ... R3/W3 10:48 AM 12:23 PM"; "Remote Learning Day Schedule R1/W1 8:00 AM 9:00 AM ... R4/W4 11:30 AM 12:30 PM". Pinkerton's start time and its start-time committee are agent 2's (P30.1, town/pinkerton/). Raw: raw/daily/pinkerton/pa-bell.txt

## district-transportation: Derry's School Buses: First Student, Eligibility, the Three Tiers and Ride Times

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. The Derry Cooperative School District's buses, including those to Pinkerton Academy, are run by First Student (33 Chester Road, Derry; 603-432-7417), which answers questions about routes; the district posts AM and PM route sheets for each school (updated September 7, 2026) and personal bus information in the PowerSchool parent portal.
   - citation: Derry Cooperative School District, Transportation
   - source: https://www.sau10.nh.gov/departments/transportation/index
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Page text: "Derry School District students also have personalized bus information posted on the parent portal of PowerSchool ... the PowerSchool office has no information regarding bus stops. To inquire about bus routes after the information has been posted you may contact the First Student offices at 603-432-7417." "2026-2027 BUS ROUTES (Updated September 7, 2026)" with sheets for each elementary school, WRB, Hood and Pinkerton. The Pinkerton sheets say "Route Last Updated: 11/2/2026". Raw: raw/daily/sau10-transportation.txt
2. Derry families can follow their child's bus in real time with First Student's FirstView app (district code R7D7U in 2026-27), which shows the bus's location and sends arrival alerts; in January 2026 the district said more than 630 students were being tracked.
   - citation: Derry Cooperative School District, Transportation; School Board at a Glance, January 2026
   - source: https://www.sau10.nh.gov/departments/transportation/index
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Page text: "FirstView®, a real-time GPS vehicle tracking and student transportation monitoring platform ... Receive multiple distanced-based ETA notifications when the vehicle is getting close ... The District code has changed this year. The new code is R7D7U". At a Glance (January 13, 2026): "Announced the First View bus app is fully operational with over 630 students being tracked by parents/guardians." Raw: raw/daily/sau10-transportation.txt; raw/daily/sb-glance.txt
3. Under Derry's policy EEA (revised October 2024), the district buses students in grades K–8 who live more than one mile from their assigned school and Pinkerton Academy students who live more than two miles from the Academy; students in alternative high school programs off Pinkerton's campus may not be eligible, high school students are not charged, and the School Board may waive the distances where a hazardous condition exists.
   - citation: Derry Cooperative School District Policy EEA, Transportation – Riders (revised October 2024)
   - source: https://drive.google.com/file/d/0B4MduX0xeMqJa3NGSE5RUzYxUjQ/view?resourcekey=0-gwyntXJHw4ka16OS5gHMzg
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "1. Elementary students (grades K-8) who live more than one mile from the school to which they are assigned. 2. Senior high students attending school on the Pinkerton Academy campus (grades 9-12) who live more than two miles from the Academy. 3. Senior high students attending alternative high school programs off Pinkerton's campus may not be eligible to receive transportation." "In accordance with a vote at the School District Meeting of March 1978, high school students will not be charged for bus transportation." "These distances may be waived by the School Board if a hazardous condition exists." Approved private school pupils get the same privileges if their calendar and hours match Derry's. State law requires busing only beyond 2 miles for K–8 (library: school-transportation-rules). Raw: raw/daily/sau10-policy-EEA.txt
4. Under policy EEA, a Derry student may ride only the assigned bus unless the principal approves; a change longer than four days needs a written request from a parent and is granted only in exceptional cases of health or welfare; and parents seeking an exception to the transportation rules go to the superintendent and then, as a last appeal, to a board committee (for 2026-27, a Transportation Appeal Committee of three board members).
   - citation: Derry Cooperative School District Policy EEA; School Board minutes, April 14, 2026
   - source: https://drive.google.com/file/d/0B4MduX0xeMqJa3NGSE5RUzYxUjQ/view?resourcekey=0-gwyntXJHw4ka16OS5gHMzg
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Policy text: "Any request for a transfer or change of bus in excess of four days must be submitted in written form by the parent or guardian to the building principal. Transfers are to be made only in exceptional cases involving the health or welfare of the student." "Parents who wish to request a change or exemption ... shall direct that request to the Superintendent or designee. As a last appeal, the parent may request to appear before the Board's Transportation Committee." Minutes: "they will have a Transportation Appeal Committee of three Board members that will meet with the transportation coordinator as needed to hear appeals under Board policy EEA." Raw: raw/daily/sau10-policy-EEA.txt; raw/daily/minutes/sb-minutes-2026-04-14.txt
5. Derry's transportation page says not every student has a stop in front of the house because stops are combined at corners to keep routes shorter; requests to add, move or report a concern about a stop go through an online form that First Student reviews against the whole route, road conditions, safety and ride times, and the page warns that changes may lengthen other students' rides.
   - citation: Derry Cooperative School District, Transportation, "Find Your Child's Bus Stop" and "Bus Service Provider"
   - source: https://www.sau10.nh.gov/departments/transportation/index
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Page text: "Consolidating stops at corners and grouping neighbors into one stop helps to make the bus routes shorter by not having to make multiple stops on one road." "Requests to add, remove, or change a bus stop must be reviewed in coordination with First Student. The district Transportation Director does not independently establish or change bus stops." "First Student will review requests based on the overall route, road conditions, safety considerations, transportation time, and the needs of all students served by the route. If you have not received a response within two business days ... contact First Student directly at 603-432-7417". "Please note that changes to established routes may result in longer transportation times for other students". Urgent safety concerns go to the school, then transportationcoordinator@sau10.org. Raw: raw/daily/sau10-transportation.txt
6. Derry's 2026-27 family handbook says the bus will not wait for children who stay in their houses, whatever the weather; students may ride only their own bus unless the school gives a bus pass; and a student suspended from the bus must be driven by the family, with absences for that reason not excused.
   - citation: Derry Cooperative School District Student & Family Handbook 2026-2027, "Bus Procedures and Conduct"
   - source: https://docs.google.com/document/d/1-VOKgszG-ycSCotPKOldJQ_vPSj-Qjs5R_Ua0nc3Qkw/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "The bus WILL NOT wait for children who remain in their houses waiting for the bus regardless of the weather." "Students may ride only on their own bus. (unless a bus pass is assigned by the school administration.)" "Absenteeism due to transportation issues (because of a bus suspension) is not an acceptable excuse." The route sheets say "ALL STUDENTS SHOULD BE AT THE STOP 5 MINUTES EARLY". Raw: raw/daily/sau10-family-handbook-2026-27.txt
7. Derry's posted 2026-27 routes run in three tiers: 19 morning routes reach Pinkerton Academy at 6:45 a.m. (first stops from 6:03), 13 reach Hood at 7:45 and 16 reach West Running Brook at 7:50, and 26 elementary routes reach the four elementary schools at 8:40; in the afternoon 21 Pinkerton routes leave at 1:58 p.m. (one at 1:50), Hood's 13 at 2:30, West Running Brook's 16 at 2:35 and the elementary routes at 3:10.
   - citation: Derry Cooperative School District, 2026-2027 bus route sheets (AM and PM, each school)
   - source: https://www.sau10.nh.gov/departments/transportation/index
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: **Derived** by counting the posted route sheets: Pinkerton AM 19, PM 21; Hood 13; WRB 16; East Derry Memorial 8; Barka 8; Grinnell 5; South Range 5. Every Pinkerton morning sheet ends "DEST PINKERTON ACAD CLOCKTOWER" at 6:45, 30 minutes before Pinkerton's 7:15 start (derived; district-school-day-and-calendar 19). **No late, activity or second run appears on any posted sheet.** The sheets list stops by house number, so they were not copied; a CSV of each route's times without stops is saved. See table derry_bus_scheduled_ride_minutes_2026_27. Raw: raw/daily/derry-bus-routes-2026-27-scheduled-times.csv
8. None of Derry's posted 2026-27 route sheets lists a stop on Crystal Avenue, and Derry's Pinkerton riders must live more than two miles from the Academy to be bused.
   - citation: Derry Cooperative School District, 2026-2027 bus route sheets; Policy EEA
   - source: https://www.sau10.nh.gov/departments/transportation/index
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: **Derived** by searching the text of all 14 route sheets (Pinkerton, Hood, WRB and four elementary schools, AM and PM) for "Crystal": no match. Whether a given Crystal Avenue address is more than two miles from Pinkerton was not checked. Bears on the P5.3 premise. Raw: raw/daily/derry-bus-routes-2026-27-scheduled-times.csv; raw/daily/sau10-policy-EEA.txt
9. On Derry's posted 2026-27 schedules, the longest scheduled ride from a route's first stop to school is 42 minutes in the morning (Pinkerton route PA19, 6:03 to 6:45 a.m., 33 stops, and West Running Brook route WRB12, 7:08 to 7:50) and the longest from school to the last stop is 47 minutes (WRB12, 2:35 to 3:22 p.m.); the longest East Derry Memorial ride is 39 minutes, and the median Pinkerton morning ride is 19 minutes.
   - citation: Derry Cooperative School District, 2026-2027 bus route sheets
   - source: https://www.sau10.nh.gov/departments/transportation/index
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: **Derived**: scheduled school arrival minus the scheduled time at the first stop (morning), or the scheduled time at the last stop minus the school departure (afternoon), for all 150 posted routes. These are scheduled, not measured, times; the first student picked up rides longest. The sheets don't say which neighborhood each route serves. See table derry_bus_scheduled_ride_minutes_2026_27. Bears on the P21.2 premise ("almost an hour"). Raw: raw/daily/derry-bus-routes-2026-27-scheduled-times.csv
10. In September 2026 Derry's transportation director reported that the new three-tier system had been adjusted, including added Pinkerton buses, that intermediate-school arrivals were on time and middle-school timing was improving, and that the district had 29 large buses, the same for the past three or four years, compared with 34 in earlier years.
   - citation: Derry Cooperative School Board minutes, September 22, 2026, Director of Information Services & Transportation report
   - source: https://drive.google.com/file/d/1wGf6GK0Vkrmeec9h0eEjOgqySUeS6I89/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Minutes text: "The new three-tier busing system was adjusted, including additional Pinkerton Academy buses. Intermediate-school arrivals are on time; middle-school timing is improving." "The district has 29 large buses, the same as the past three to four years, compared with 34 in previous years." August 25, 2026 minutes: "The first day had high bus ridership, and transportation adjustments were underway." Raw: raw/daily/minutes/sb-minutes-2026-09-22.txt; raw/daily/minutes/sb-minutes-2026-08-25.txt
11. In September 2026 Derry's superintendent reported continuing trouble busing 5th and 6th grade athletes, citing driver shortages, route changes, more riders and a trial shuttle with the Boys & Girls Club; First Student then set up a route carrying nearly 60 students a day from West Running Brook to Hood for after-school athletics.
   - citation: Derry Cooperative School Board minutes, September 9 and September 22, 2026, Superintendent's Report
   - source: https://drive.google.com/file/d/157kqYny4UczNBfcwS_p_hH8vDnsBJwYe/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: September 9: "continuing athletic busing challenges for grades five and six, including driver shortages, route adjustments, increased ridership, and shuttle testing between the Boys and Girls Club. The district continued evaluating stops and communicating changes to families." September 22: "First Student arranged a route for five/six athletes to travel from West Running Brook Intermediate School to Gilbert H. Hood Middle School for after-school athletics; nearly 60 students make the trip daily." Raw: raw/daily/minutes/sb-minutes-2026-09-09.txt; raw/daily/minutes/sb-minutes-2026-09-22.txt
12. Derry is getting 25 electric school buses through a federal grant; First Student owns the buses and their charging stations, which are at First Student's lot rather than on school property, and in September 2026 the buses were expected on the road by January 2027.
   - citation: Derry Cooperative School Board minutes, June 9 and September 22, 2026; School Board at a Glance, March 2026
   - source: https://drive.google.com/file/d/1_nzGh8GcD16Tt_DL_KNpuAEZNjfPpghS/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: At a Glance: "the delivery of 25 electric school buses acquired through a federal grant." June 9: "the district owns nothing; First Student owns everything. Charging stations will be at First Student, not on school property." September 22: "Electric buses are expected in late November/early December, with depot infrastructure permits underway; buses are expected on the road by January." A board member asked about recouping savings through the First Student contract; that was left to fall contract talks. Raw: raw/daily/minutes/sb-minutes-2026-06-09.txt; raw/daily/minutes/sb-minutes-2026-09-22.txt; raw/daily/sb-glance.txt
13. A Derry Cooperative School Board meeting in August 2026 heard a parent ask for a safety review of a bus stop where four students walk about half a mile along a road without sidewalks or street lights; the chair said stops are reviewed through the transportation coordinator and the superintendent's office would follow up.
   - citation: Derry Cooperative School Board minutes, August 25, 2026, Public Comment
   - source: https://drive.google.com/file/d/1esFvQUesscF6FYdPKLAlTKVV8poQRb5z/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Minutes text: "four students walk approximately half a mile along a road without sidewalks or street lighting. She described conflicting information about responsibility for assigning stops and requested clarification, a safety review, and consideration of a safer location. Chairman Thiele stated that bus stops are reviewed through the transportation coordinator and that the Superintendent's office would ensure her concern was addressed." The speaker's name and street are left out here. Raw: raw/daily/minutes/sb-minutes-2026-08-25.txt
14. Pinkerton Academy says it does not manage bus routes or schedules, which each sending district posts; in the afternoon Derry's and Chester's buses (First Student, 603-432-7417) line up with Auburn, Candia, Hooksett and Hampstead buses along Bypass 28 (North Main Street) and beside the Hackler Gymnasium, and Fremont's buses park in front of Pinkerton Hall.
   - citation: Pinkerton Academy, Bus Schedules to/from Pinkerton; "Afternoon Bus Lineup" (updated September 3, 2026)
   - source: https://www.pinkertonacademy.org/portals/students/bus-schedules
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Page text: "Please note that the links below are the most current based on the district postings. Pinkerton does not manage bus routes and schedules." Lineup (read from the image): "--- Bypass 28 (North Main Street) --- ... Derry Buses ... All Chester Buses ... Hackler Gymnasium ... Fremont Buses (Orange & Green) will be parked in front of Pinkerton Hall. Updated 9.3.26"; phone list: Chester and Derry "603-432-7417 First Student"; Fremont "Butler's Bus Service". Lineup PDF: https://drive.google.com/file/d/1dwh051goYevlotP9YF9yJ8Gt8nUwymsl/view. Raw: raw/daily/pinkerton/pa-bus.txt; raw/daily/pinkerton/pa-bus-lineup-p1.png; raw/daily/pinkerton/pa-bus-lineup.pdf
15. Pinkerton Academy's start time committee wrote that its 7:15 a.m. start requires first bus pickups between 5:45 and 6:03 a.m. in five of its six sending towns.
   - citation: Pinkerton Academy, Start Time Committee Problem Statement
   - source: https://drive.google.com/file/d/1JuXCPXEotUn8K162KU2aDAMFU44cZSiJ/view?usp=drive_link
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Text: "Pinkerton Academy's current start time is 7:15a, which is substantially earlier than other schools in the region. This start time requires the first bus pick-up time to be between 5:45a and 6:03a in 5 of the 6 sending towns." The statement is undated (it names six sending towns, before Fremont joined) and says "no decision has been made". Linked from https://www.pinkertonacademy.org/about/start-time-committee-information. Derry's earliest 2026-27 Pinkerton pickup is 6:03 (fact 9). The start-time question itself is agent 2's (P30.1). Raw: raw/daily/pinkerton/pa-start-problem.txt
16. CART, the Greater Derry-Salem public transit service run by Manchester Transit, gives curb-to-curb rides in Derry on weekdays from 8:00 a.m. to 7:30 p.m. (last pickup 7:15) and Saturdays 9:30 a.m. to 1:30 p.m., for $2 a trip ($1 for ages 5 to 15, exact cash), booked by calling 603-623-8801, option 2.
   - citation: Manchester Transit Authority, CART; Town of Derry, Human Services – Transportation
   - source: https://mtabus.org/cart/
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Page text: "Derry Hours of Operation: Monday – Friday, 8:00 am to 7:30 pm Last pickup no later than 7:15pm Saturday, 9:30 am to 1:30 pm ... -$2 per passenger per trip -$1 per child age 5-15 -Children under age 5 ride free *Please bring exact cash*"; "Rides may be requested by contacting our call takers at 603-623-8801; opt. #2". The town page (https://www.derrynh.gov/366/Transportation) lists "Greater Derry-Salem Cooperative Alliance for Regional Transportation (CART) Call 603-623-8801 to schedule a ride". CART's weekday service starts after Pinkerton's 7:15 a.m. start (**derived**). The page doesn't say whether minors may ride alone. Raw: raw/daily/community/cart.txt; raw/daily/town/town-transportation.txt

## district-safety-and-security: Visitors, Security Grants, Emergency Plans and Drills in Derry's Schools

- kind: local
- question_type: local_practice
- description: Building security, visitor rules, drills and emergency plans, and school security grants

1. In Derry's schools every visitor must sign in at the main office and wear an identification sticker, and under policy KI (revised February 2024) parents or citizens who want to visit while school is in session must arrange it with the principal 24 hours ahead.
   - citation: Derry Cooperative School District Policy KI, Visitors to Schools (revised February 2024); Student & Family Handbook 2026-2027, "Visitors to Schools"
   - source: https://drive.google.com/file/d/1iBiL5cx-eTjwg08MzUqr9sLt0GKXzNfm/view?usp=drive_link
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Policy text: "Any visitor to the school must report to the office of the principal upon arrival at the school. ● Parents/guardians or citizens who wish to visit the school while school is in session must arrange such visits in advance with the principal ... (Twenty-four hour notification is required.)" Handbook: "All guests/visitors must sign in and report to the office before proceeding to any part of the building. All visitors will be required to wear an identification sticker." Volunteers must be fingerprinted and complete online training (school handbooks). Raw: raw/daily/sau10-policy-KI.txt; raw/daily/sau10-family-handbook-2026-27.txt
2. Derry's elementary handbooks say a child leaves early only after the adult picking up reports to the lobby, is identified and signs the child out; after school, children and parents may return to classrooms only with an office escort and before 4:00 p.m.; and Grinnell asks parents to stay away from Door 12 at arrival and dismissal.
   - citation: Derry Cooperative School District 2026-27 handbooks (district; Grinnell, South Range, East Derry Memorial, Barka)
   - source: https://docs.google.com/document/d/1GNAcRsZgJsT0rJqSqKg5uHwxK3hW0tV2_ZBCHj45y2k/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "A student may not leave the school building until the person receiving the student has reported to the school lobby, has been properly identified by a school official, and has been signed out." "children and parents may only come back into the school and the classrooms for forgotten items or homework if someone is in the office to escort them ... (Before 4:00 p.m.) For safety/security reasons, neither children nor parents are allowed in the classrooms without permission". Grinnell: "For safety considerations, no parents/guardians should be near Door 12." No handbook or minutes describe the entrances themselves (vestibules, buzzers or card readers). Raw: raw/daily/handbook-2026-27-grinnell.txt; raw/daily/sau10-family-handbook-2026-27.txt
3. In March 2026 the Derry Cooperative School Board accepted two state Security Action for Education (SAFE) grants for each of its six schools, for additional security cameras and, at Hood, re-keying; East Derry Memorial's were $21,378.32 and $16,000 and Grinnell's $18,393.46 and $16,000.
   - citation: Derry Cooperative School Board minutes, March 24, 2026, "Security Action for Education (SAFE) Grant"; School Board at a Glance, March 2026
   - source: https://drive.google.com/file/d/1ogVztqbO03RfQZ6Du6vEUi90jwpc_vjQ/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Minutes text: "There are two Grants for each school. ... East Derry Memorial Elementary School: $21,378.32 & $16.000, Ernest P. Barka Elementary School: $25,974.99 & $16,000, Gilbert H. Hood Middle School: $26,510.65 & $16,000, Grinnell Elementary School: $18,393.46 & $16,000, South Range Elementary School: $15,734.82 & $16,000, and West Running Brook Intermediate School: $21,127.75 & $16,000." "we already have a camera system; the only thing we are adding are additional cameras." Re-keying "was just Hood" (not DEEP or Next Charter) in the minutes, while the March 2026 At a Glance says the grants cover "security upgrades, including additional cameras and rekeying systems, across all six district schools". The superintendent and At a Glance give "approximately $260,000"; the twelve amounts read into the minutes add to $225,119.99 (**derived**). See table derry_safe_grants_2026. Raw: raw/daily/minutes/sb-minutes-2026-03-24.txt; raw/daily/sb-glance.txt
4. Derry's facilities director reported in August 2026 that district-wide re-keying was finished, with new keys handed out from August 12, 2026; the district was also planning district-wide door replacements, but as of September 22, 2026 the bond-funded interior and exterior door projects had not started.
   - citation: Derry Cooperative School Board minutes, August 11, September 9 and September 22, 2026
   - source: https://drive.google.com/file/d/1tQc6vtpwgljIetLnNyhd3PcInBpQEx6L/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: August 11: "District-wide re-keying was completed, with keys scheduled for distribution beginning August 12, 2026." September 9: "The district was also planning district-wide door replacements and window replacements for the fifties section at Gilbert H. Hood Middle School." September 22: "Some projects, including interior and exterior doors, Gilbert H. Hood Middle School windows, and exterior door and frame repairs, have not started." October 13: Grinnell's capital plan lists "Playground, fencing, school sign, exterior lighting, and masonry repointing" (agent 7's area). Raw: raw/daily/minutes/sb-minutes-2026-08-11.txt; raw/daily/minutes/sb-minutes-2026-09-09.txt; raw/daily/minutes/sb-minutes-2026-09-22.txt; raw/daily/minutes/sb-minutes-2026-10-13.txt
5. In May 2026 the Derry Cooperative School Board approved an $85,884 bid from Telephone Network Technologies to upgrade the intercom and mass-notification systems in all six schools, so the SAU office can make synchronized district-wide announcements; in September 2026 the public address and visitor-management systems still needed troubleshooting.
   - citation: Derry Cooperative School District, School Board at a Glance, May 2026; School Board minutes, September 22, 2026
   - source: https://www.sau10.nh.gov/school-board/school-board-at-a-glance
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: At a Glance: "The Board approved a bid from Telephone Network Technologies (TNT) for $85,884 to upgrade mass notification and intercom systems across all six district schools. This safety improvement allows for synchronized, district-wide announcements from the SAU office and provides school-wide coverage for emergencies." September 22 minutes: "PA (public address) and visitor-management systems need further troubleshooting." The minutes for May 26, 2026 were not posted in the list read; the At a Glance summary is the source. Raw: raw/daily/sb-glance.txt; raw/daily/minutes/sb-minutes-2026-09-22.txt
6. Through a state-funded grant, Derry's schools are being mapped in high resolution for police, fire and EMS to use in emergencies; in May 2026 the superintendent said a vendor had been chosen after a statewide bid, the district pays nothing, and no timeline was set.
   - citation: Derry Cooperative School Board minutes, May 12, 2026; School Board at a Glance, May 2026
   - source: https://drive.google.com/file/d/1A9yG8HB4NS79CYpWDIFdOJIYDUA481ic/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Minutes text: "He discussed the partnering of local authorities, police, fire, and EMS on Safety Maps for all the schools. ... the state as a whole was going to put out a higher statewide bid. They finally went out and chose a vendor. Now all of our buildings and facilities will be mapped out ... They do not know timelines yet; this is grant-funded, and we do not have to spend any money." Raw: raw/daily/minutes/sb-minutes-2026-05-12.txt; raw/daily/sb-glance.txt
7. In the state's first two rounds of SAFE school security grants (2022), the Derry Cooperative School District applied for 25 projects totaling $700,000 and 18 were funded for $321,925; it made no application in Round 3 (2023).
   - citation: NH Department of Education, "Security Action for Education (SAFE) Grant" handout, list of all SAFE grant awards (last revised December 13, 2024), page 1 of 7
   - source: https://gc.nh.gov/lba/budget/operating_budgets/2026-2027/HF_Division_II/Division%20II%20-%20NHED%20SAFE%20Grants%20(PSIF)%20Overview%20-%2012-13-24.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Table row (read from the image): "10 Derry Cooperative 25 $700,000 18 $321,925 7 $378,075" for Rounds 1–2, then "0 $ -" for Round 3. The grants cover access control, surveillance or emergency alerting (Jackson file: district-safety-and-security 13). The 2026 awards (fact 3) are later than this list. Raw: raw/daily/town/safe-grants-psif-overview-2024-12-13.txt; raw/daily/town/safe-grants-p3.png (copied from town/Jackson/raw/policies/grants/)
8. Derry's policy EBCA (April 2022) requires a district crisis plan and a site-specific emergency response plan for each school, made with police and fire and covering violence, threats, natural disasters, fire, hazardous materials and medical emergencies, reviewed every year and sent to the NH Department of Education by September 1 when changed; the district's Emergency Management Team reviewed the plans in fall 2025, with each building having its own.
   - citation: Derry Cooperative School District Policy EBCA, Crisis Prevention and Emergency Response Plans (April 2022); School Board at a Glance, September 2025
   - source: https://drive.google.com/file/d/1RL4jddYnSP9AtU2AFKjeoIXg9QbDzVBJ/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Policy text: "shall develop a Districtwide Crisis Prevention and Response Plan, which must, at a minimum, include a site-specific Emergency Response Plan for each school ... addresses hazards including, but not limited to: acts of violence, threats, natural disasters, fire, hazardous materials, medical emergencies"; "If an Emergency Response Plan is updated/revised, the Superintendent shall submit the updated Emergency Response Plan to the New Hampshire Department of Education no later than September 1." At a Glance: "Emergency Management Team (First Meeting of the Year) Reviewed the emergency operations plan, which is due to the State of New Hampshire by October 15, 2025. Each building has its own individual plan." The plans themselves are not public. Raw: raw/daily/sau10-policy-EBCA.txt; raw/daily/sb-glance.txt
9. Derry's 2026-27 handbook says students take part in evacuation drills and periodic lockdown drills, that participation is mandatory, and that families are asked to talk with children about the drills; policy EBCB calls for a fire drill every month of the school year.
   - citation: Derry Cooperative School District Student & Family Handbook 2026-2027, "Emergency Procedures"; Policy EBCB, Fire Drills
   - source: https://docs.google.com/document/d/1-VOKgszG-ycSCotPKOldJQ_vPSj-Qjs5R_Ua0nc3Qkw/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Handbook text: "Throughout the school year, students will participate in both evacuation drills and other drills ... Lockdown drills are periodically conducted to review appropriate procedures and to prepare students and staff for any possible emergency. ... Participation in these drills is mandatory". EBCB (https://drive.google.com/file/d/0B4MduX0xeMqJcngyNXp1M3hUZVU/view): "The principal will schedule fire drills each month during the school year." The handbook does not say whether families are told before or after a drill. Raw: raw/daily/sau10-family-handbook-2026-27.txt; raw/daily/sau10-policy-EBCB.txt
10. Under Derry's policy EBCC (February 2024), when a violent threat is made or a false alarm is set off, the superintendent decides whether to evacuate, police are notified at the same time and investigate, students return only after police clear the building, and the person who made the threat faces school discipline and referral for prosecution.
   - citation: Derry Cooperative School District Policy EBCC, False Alarms, Active Shooter, Bomb & Other Such Threats (February 2024)
   - source: https://drive.google.com/file/d/1XUGIX4l49E8yB8KnfVSAh94B-tDVeZnx/view?usp=drive_link
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "1. The Superintendent or designee shall make a determination as to whether an immediate evacuation of school buildings is required ... 2. Simultaneously, local law enforcement authorities shall be notified. 3. An investigation of the threat should be made by local law enforcement ... 4. Any decision to re-enter ... only after such clearance has been given by the appropriate law enforcement agency." "Making such threats or false alarms will be deemed a violation of the applicable code of conduct ... and will be referred to law enforcement for potential criminal prosecution." Its rule on telling parents is district-family-communication 2. Raw: raw/daily/sau10-policy-EBCC.txt
11. The Derry Cooperative School Board allows video and audio recording on district property and school buses for the safety of students, staff and visitors.
   - citation: Derry Cooperative School District Student & Family Handbook 2026-2027, "Video & Audio Surveillance" (policies EEAA and ECAF)
   - source: https://docs.google.com/document/d/1-VOKgszG-ycSCotPKOldJQ_vPSj-Qjs5R_Ua0nc3Qkw/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "The Derry Cooperative School Board authorizes the use of video and/or audio devices on District property and on school buses to ensure the health, welfare and safety of all staff, students, and visitors to District property". Raw: raw/daily/sau10-family-handbook-2026-27.txt
12. Derry's policy ECE (hours last revised in 2007) keeps private cars out of school bus areas from 6:30 a.m. to 2:30 p.m. at the middle schools and from 7:00 a.m. to 3:30 p.m. at the elementary schools.
   - citation: Derry Cooperative School District Policy ECE, Traffic and Parking Controls – Use of Motor Vehicles on School Property
   - source: https://drive.google.com/a/sau10.org/file/d/0B4MduX0xeMqJZmc4eEJJaHRJMjA/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "2. Private cars are excluded from bus routing areas between the hours of 6:30 am and 2:30 pm at middle schools; and 7 am and 3:30 pm at elementary schools." Footer: "Reviewed 2013, Hours Revised October 2007". The hours were set before the 2026-27 schedule (dismissal now 2:35 at WRB). Barka's handbook: "Parents are not permitted to drive in our front driveway from 2:30-3:10 to allow time for buses to load and leave." Raw: raw/daily/sau10-policy-ECE.txt; raw/daily/handbook-2026-27-barka.txt
13. In the state's SAFE school security grants, Pinkerton Academy had 2 of 3 applications funded for $44,625 in Rounds 1–2 (2022) and both of its Round 3 (2023) applications funded for $99,925.
   - citation: NH Department of Education, SAFE Grant handout, list of all SAFE grant awards (last revised December 13, 2024)
   - source: https://gc.nh.gov/lba/budget/operating_budgets/2026-2027/HF_Division_II/Division%20II%20-%20NHED%20SAFE%20Grants%20(PSIF)%20Overview%20-%2012-13-24.pdf
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Text row: "202 Pinkerton Academy 3 100,000$ 2 44,625$ 1 55,375$ 2 99,925$ 2 99,925$ 0 ‐$ 0 ‐$". Round 2 was the round open to nonpublic schools; Round 3's columns are applications, amount requested, applications funded and amount funded. Raw: raw/daily/town/safe-grants-psif-overview-2024-12-13.txt
14. Pinkerton Academy uses the "I Love U Guys" Foundation's Standard Response Protocol, with five actions: Hold (stay in your room, as for a medical emergency), Secure (get inside and lock outside doors, as for a nearby threat), Lockdown ("Locks, Lights, Out of Sight", as for a violent intruder), Evacuate and Shelter.
   - citation: Pinkerton Academy, Crisis Communications
   - source: https://www.pinkertonacademy.org/about/communications/crisis-communications
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Page text: "The SRP uses five simple, action-based terms that everyone can remember and follow: Hold, Secure, Lockdown, Evacuate, and Shelter." "Secure is followed by the Directive: 'Get Inside. Lock Outside Doors' ... if there is a potential threat nearby like a wild animal or police activity." "Lockdown is followed by 'Locks, Lights, Out of Sight' ... in a violent intruder situation." Belongs with the shared Pinkerton research as well (see For another file). Raw: raw/daily/pinkerton/pa-crisis.txt

## district-family-communication: How Derry Schools and Pinkerton Tell Families About Closings and Emergencies

- kind: local
- question_type: local_practice
- description: How schools reach families: parent portals, grade tracking, emergency notices, and translation and interpreting

1. Derry's schools use ParentSquare as their main way to send timely information to families and ask every family to set up an account before school starts; storm closings and delays go out through the district's rapid notification service as a phone call, text and email.
   - citation: Derry Cooperative School District Student & Family Handbook 2026-2027, "Parent/Guardian Communication"; Closure Procedures
   - source: https://docs.google.com/document/d/1-VOKgszG-ycSCotPKOldJQ_vPSj-Qjs5R_Ua0nc3Qkw/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Handbook: "our district uses a tool known as Parent Square as a primary means of sharing timely information with parents/guardians. All parents/guardians are strongly encouraged to create a ParentSquare account prior to the start of the school year." Closure page: "The District utilizes a rapid notification service, allowing a telephone call/voice message, text, and email to be sent to parents/guardians as the primary means of immediate communication." Hood's handbook: "Please do not call the school when receiving an alert message." Translation and portals are agent 6's. Raw: raw/daily/sau10-family-handbook-2026-27.txt; raw/daily/sau10-closure.txt; raw/daily/handbook-2026-27-ghh.txt
2. Derry's threat policy EBCC says the superintendent will tell the parents of students in an affected building about any threat, whether or not the building was evacuated, under the district's crisis plan or communication plan or "as soon as deemed appropriate under the circumstances"; it sets no time limit.
   - citation: Derry Cooperative School District Policy EBCC (February 2024), item 5
   - source: https://drive.google.com/file/d/1XUGIX4l49E8yB8KnfVSAh94B-tDVeZnx/view?usp=drive_link
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "5. The Superintendent or her/his designee will communicate the occurrence of any threat under this policy to the parents of any students in the affected building, whether or not a full evacuation occurred EITHER in accordance with the District Crisis Prevention and Response Plan OR the District Communication Plan OR as soon as deemed appropriate under the circumstances." The District Communication Plan was not found online. Answers part of P18.3. Raw: raw/daily/sau10-policy-EBCC.txt
3. In September 2025 West Running Brook's principal used the weekly family newsletter to explain that a medical situation that morning had led the school to use a "Clear Hallways" protocol, in which students and staff stay in classrooms behind closed doors and lessons continue, and that the person was okay.
   - citation: West Running Brook Intermediate School, WRB News, September 12, 2025
   - source: https://www.sau10.nh.gov/schools/wrb/news/1814895/wrb-news-9-12-25
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "This morning a member of our community experienced a medical situation that required us to enact a 'Clear Hallways' protocol. During a 'Clear Hallways' protocol students and staff remain in classrooms behind closed doors. This allows us to maintain the privacy of the individual(s) experiencing the emergency ... We are pleased to report that the individual is okay". An example only; no record of how Derry communicated about a lockdown or threat was found. Raw: raw/daily/wrb-news-9-12-25.txt
4. Pinkerton Academy says it will message families whenever it calls a Secure, Lockdown, Evacuate or Shelter and in any situation that disrupts normal operation or instruction, but may not for a Hold that doesn't affect most of campus; during an active situation messages usually come from its Director of Communications, followed by the Head of School or Associate Head of School, by ParentSquare email and text (sometimes phone) in each family's preferred language.
   - citation: Pinkerton Academy, Crisis Communications
   - source: https://www.pinkertonacademy.org/about/communications/crisis-communications
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Page text: "We will communicate in all situations that cause a disruption of normal operation or instruction during a school day." "The nature of an emergency will dictate how quickly you will hear from the school, who the message will come from, and what is shared. If it is an active situation, the messages will most often come from the Director of Communications with follow-up messaging coming from the Head of School or Associate Head of School at the end of the event. Communications will be sent via email and text messaging (and sometimes phone) using ParentSquare to ensure it reaches all families in their preferred language." "We will communicate any time SECURE, LOCKDOWN, EVACUATE, or SHELTER are initiated. We may not communicate for a HOLD if it does not impact most of campus." Raw: raw/daily/pinkerton/pa-crisis.txt
5. Pinkerton Academy's crisis-communication examples say all families are told about weather closings, outages, unplanned building evacuations and its intruder protocols, while only the families involved are contacted about fights, reported crimes, medical issues at school and staff terminations.
   - citation: Pinkerton Academy, Crisis Communications Examples (published spreadsheet)
   - source: https://docs.google.com/spreadsheets/d/e/2PACX-1vQhLuRqZ8Vetv8Qdq8BIHdCFh_g-d0G8dGGbhHMP_s_ciRmx4OyOR2aIYs7ubGwLthzHHjMarlWRue9/pubhtml?gid=0&single=true
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Rows: "School closure, delay or event cancellation due to weather" (all families: ParentSquare, web pop-up, social media, local news); "Power, phone or internet outages" (all); "Building evacuation due to fire alarm, gas leak or other facility issue (not a planned drill)" (all); "**ALICE Protocols" (all; ParentSquare, web pop-up, local news); "Physcial altercations", "Reported criminal activity", "Medical issue at school", "Employee termination" (affected families; school admin contacts them). "*This is not an exhaustive list." "**Initial message and follow-up messages as the situation allows." The sheet still names ALICE, while the page now uses the Standard Response Protocol. Raw: raw/daily/pinkerton/pa-crisis-examples.csv
6. Pinkerton Academy says its emergency messages leave out anything that identifies a student, anything that could hinder a police investigation, and, when a situation threatens only a group, classroom or bus, may go only to the affected families.
   - citation: Pinkerton Academy, Crisis Communications, "What is NOT included"
   - source: https://www.pinkertonacademy.org/about/communications/crisis-communications
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Page text: "Student information - Pinkerton Academy is legally bound to protect student privacy and will not share information that can identify an individual student or students." "Information that might hinder any active law enforcement investigations." "Information might not be shared with all families if a situation is not a safety threat beyond a specific group, classroom, or bus. Only the affected families might be notified." Raw: raw/daily/pinkerton/pa-crisis.txt
7. Pinkerton Academy sends snow-day and emergency messages through ParentSquare, and emergency notifications arrive at once whatever notification settings a family has chosen; families who reply STOP to texts must text START to 66458 to get them again.
   - citation: Pinkerton Academy, Alert System
   - source: https://www.pinkertonacademy.org/about/alert-system
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Page text: "ParentSquare will be used for the Head of School and Associate Head of School updates, report card distribution, snow day notifications, and emergency/crisis communications." "To receive weather-related messages, be sure to leave the option for 'School Alerts' on. *Regardless of your notification settings, you will continue to receive emergency notifications instantly." "if you reply 'STOP' to opt out of text notifications, you cannot resume receiving text messages unless you text, 'START' to 66458." Raw: raw/daily/pinkerton/pa-alert-system.txt

## town-emergency-services: Derry Police School Resource Officers

- kind: local
- question_type: local_practice
- description: A town's police, fire and emergency management, dispatch, mutual aid, emergency alerts and cell coverage

1. The Derry Police Department's FY2027 budget says it staffed two school resource officers at Pinkerton Academy in FY2026, paid for under an annual contract with Pinkerton, and expected to do the same in FY2027; it also staffed an SRO at West Running Brook and, for part of FY2026, one at Hood, and hoped to fully staff those posts in FY2027 while it had eight police officer vacancies.
   - citation: Town of Derry, FY2027 Adopted Budget, Police Department Mission and Objectives, objectives 1 and 4 (pages 91–92)
   - source: https://www.derrynh.gov/DocumentCenter/View/6127/FY2027-Adopted-Budget
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Text: "4. Continue with our School Resource Officer Program. Our annual contract with Pinkerton Academy provides a revenue source for the Town to cover the officers who are assigned to work in that capacity. We have staffed two officers at Pinkerton Academy during FY26 and anticipate doing the same for FY27. During FY26 we have been able to staff an SRO at West Running Brook School and for part of FY26 an additional SRO at Hood School. We are hopeful that we will be able to fully staff these positions as we move into FY27." "As of this writing there are eight vacancies for police officers." No SRO is mentioned for the elementary schools. The budget PDF is 31 MB and was not kept; its text is. Police: (603) 432-6111. Raw: raw/daily/town/town-fy2027-adopted-budget.txt
2. Derry's town budget counts Pinkerton Academy's payments for school resource officers as revenue: $230,375.31 in FY2023, $233,143.25 in FY2024 and $254,763.15 in FY2025, with $278,676 budgeted for FY2026 and $304,351 for FY2027; the town's finance director told the Town Council that FY2026's SRO revenue came in $6,700 below budget.
   - citation: Town of Derry, FY2027 Adopted Budget, Police revenue account "SRO REIMBURSEMENTS-NONGOV-SRO" (page 94); Town Council minutes, September 1, 2026
   - source: https://www.derrynh.gov/DocumentCenter/View/6127/FY2027-Adopted-Budget
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Budget row under "PRIOR FY3 / PRIOR FY2 / LAST FY1 ACTUALS / CY ACTUALS / CY REV BUDGET / PROJECTION LEVEL 5": "12005000 035063 SRO REIMBURSEMENTS-NONGOV-SRO -230,375.31 -233,143.25 -254,763.15 .00 -278,676.00 -304,351.00 9.2%". The year labels are read from the budget's FY2027 projection header (**derived**). Council minutes (https://www.derrynh.gov/AgendaCenter/ViewFile/Minutes/_09012026-352): "SRO, which is a school resource officer over at Pinkerton, that was $6,700 below budget." Raw: raw/daily/town/town-fy2027-adopted-budget.txt; raw/daily/town/council/tc-09012026-352.txt
3. At a joint School Board and Town Council workshop on September 22, 2026, Derry's school superintendent said that police staffing shortages mean there are currently no school resource officers, and that police continue drive-bys and walkthroughs.
   - citation: Derry Cooperative School Board/Town Council Joint Workshop minutes, September 22, 2026
   - source: https://drive.google.com/file/d/16Ihx6xYYDfoU4ZvIOl9jCgCFrRXC-Xud/view?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Minutes text: "Michael Flynn thanked the Derry Police Department, Chief Fioli, and Captain Breen for supporting families and students over the last 15 months. Although staffing challenges mean there are currently no SROs, police continue drive-bys and walkthroughs." The minutes don't say whether this covers the officers at Pinkerton, which the town budget (fact 1) planned to keep. Answers the P18.1 premise. Raw: raw/daily/minutes/sb-minutes-2026-09-22-joint.txt

## town-streets-and-safe-routes: Walking to School, Crosswalks and Traffic Near Derry's Schools and Pinkerton Street

- kind: local
- question_type: local_practice
- description: Sidewalks, crosswalks, Safe Routes to School and road maintenance near schools

1. Derry's Highway Safety Committee, an advisory board of the Town Council made up of public works, fire and police staff, citizens and a school department representative, reviews traffic safety concerns at specific locations and recommends changes to the Town Council; residents raise a location by mailing or dropping off a "Report a Concern" form at the Municipal Center, and it meets the third Thursday of the month at 9 a.m.
   - citation: Town of Derry, Highway Safety Committee
   - source: https://www.derrynh.gov/663/Highway-Safety-Committee
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Page text: "The Highway Safety Committee is comprised of the three major departments (DPW, Fire, Police) and several citizens to review safety concerns at specific locations. ... Final approval of all recommended highway ordinances or policy changes, additions, or deletions rests with the Town Council." "please complete the Report A Concern Form and mail it to Town of Derry, Attention: Highway Safety Committee, 14 Manning Street". Members include "School Department Representative"; the 2026 minutes list the SAU 10 business administrator and facilities director. Form: https://www.derrynh.gov/DocumentCenter/View/664/Highway-Safety-Committee-Report-a-Concern-Form. The minutes read (March, May, August, September 2026) and the October 2026 agenda had no item on school drop-off at West Running Brook or dismissal traffic on Pinkerton Street. Raw: raw/daily/town/town-hsc.txt; raw/daily/town/hsc/
2. In May 2026 Derry's Highway Safety Committee voted 0 to 8 against recommending a lighted mid-block crosswalk at the Marion Gerrish Community Center on West Broadway; public works said a mid-block crossing gives pedestrians a false sense of security, the five crosswalks from Birch Street to Maple Street line up with blocks, a crosswalk is within about 600 feet, and speeding there is a matter for police enforcement.
   - citation: Derry Highway Safety Committee minutes, May 21, 2026, New Business item 1
   - source: https://www.derrynh.gov/AgendaCenter/ViewFile/Minutes/_05212026-325
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Scanned minutes, read by OCR: "Requesting the need for a lighted crosswalk at the Marion Gerrish Community Center at 39 W. Broadway. Motorists in this area are not adhering to the 30-mph posted speed limit ... A crosswalk at this location was not recommended ... as it provides a false sense of security to pedestrians ... the other 5 cross walks from Birch St to Maple St line up with blocks. Clint said there was already a solar lit 30 mph zone sign for that area and this would be police enforcement." "the distance to a cross walk from this location was no more than 600 ft." "Motion did not pass 0-8". The requester's name is left out. Bears on P11.2 (walking from downtown Broadway). Raw: raw/daily/town/hsc/hsc-Minutes-05212026-325.ocr.txt; raw/daily/town/hsc/hsc-Minutes-05212026-325.pdf
3. In August and September 2026 Derry's Highway Safety Committee asked the school district to send families its usual yearly reminder to slow down during school drop-off and pickup, and the town added a link to tips for driving in school zones to the committee's web page.
   - citation: Derry Highway Safety Committee minutes, August 20 and September 17, 2026
   - source: https://www.derrynh.gov/AgendaCenter/ViewFile/Minutes/_09172026-354
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: OCR text, August 20: "the Derry School District usually emails a letter to parents to slow down when dropping and picking up their children. Jill Jamro will email Jane Simard; to request that a letter/email be sent to all parents." September 17: "It is unknown if any letters were distributed this year, but that is usually the case each year. Jill Jamro added a Tips for Driving in School Zones & Residential Areas | Town of Derry NH to the Highway Safety Committee website page." Raw: raw/daily/town/hsc/hsc-Minutes-08202026-331.ocr.txt; raw/daily/town/hsc/hsc-Minutes-09172026-354.ocr.txt
4. Grinnell Elementary's 2026-27 handbook says school staff are posted at the crosswalk, the sidewalk and parent drop-off from 8:40 a.m.; parents walking children from Lenox Road wait on the sidewalk at the playground crosswalk until a staff member in the crosswalk crosses the students; walkers leave first at dismissal and are met by a staff member at the crosswalk; and drivers are asked not to arrive early so Mt. Pleasant Street doesn't back up.
   - citation: Grinnell Elementary School Family/Student Handbook 2026-2027, "School Hours", "School Arrival" and "School Dismissal Procedures"
   - source: https://docs.google.com/document/d/1GNAcRsZgJsT0rJqSqKg5uHwxK3hW0tV2_ZBCHj45y2k/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Text: "School staff are posted at the crosswalk, sidewalk, and by parent drop off beginning at 8:40AM." "Parents walking children to/from school from Lenox Rd, please remain on the sidewalk by the crosswalk at the playground entrance. Once a staff member is in the crosswalk, students will be crossed." "Please do not arrive at the parking lot too early to avoid backups on Mt. Pleasant Street." "Walkers are dismissed first and will be met by a staff member at the crosswalk." **No crossing guards** (town or district) were found: the Derry police pages, the town's FY2027 budget and job listings, SAU 10's pages and the board minutes read have none. Answers part of P11.2. Raw: raw/daily/handbook-2026-27-grinnell.txt
5. At East Derry Memorial, school staff are posted at the crosswalk from 8:40 a.m. and walk students to the crosswalk at dismissal, and South Range asks walkers not to arrive before 8:40, when staff supervision begins.
   - citation: East Derry Memorial and South Range Elementary handbooks, 2026-2027
   - source: https://docs.google.com/document/u/0/d/1ljzHJRX74zuBzgdTeJAVPpJlARxzKNcVzWdNeb_y2iw/edit
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: EDS: "Children who are walkers should not arrive at school before 8:40 AM ... School Staff are posted at the crosswalk at this time." "We will escort students to the crosswalk as we have done in previous years. For safety, no cars should move or inch forward while students are walking to their rides." South Range: "Children who are walkers should not arrive at school prior to 8:40 a.m. at which time children are supervised by South Range School Staff." Raw: raw/daily/handbook-2026-27-eds.txt; raw/daily/handbook-2026-27-srs.txt
6. Derry's elementary schools let 4th graders (3rd and 4th graders at Barka) ride bicycles to school with written parent permission, remind riders that New Hampshire law requires a helmet, and ban skateboards and rollerblades on school property.
   - citation: Derry Cooperative School District 2026-27 elementary handbooks (Grinnell, South Range, Barka)
   - source: https://docs.google.com/document/d/1GNAcRsZgJsT0rJqSqKg5uHwxK3hW0tV2_ZBCHj45y2k/edit?usp=sharing
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: Grinnell: "Students in grade 4 may ride their bicycles to school. ... All students riding bicycles must have written parental consent ... WEAR A HELMET as required by NH law." Barka: "Students in grades three and four may ride their bicycles to and from school. A parent or guardian must accompany students in grades K-2." Raw: raw/daily/handbook-2026-27-grinnell.txt; raw/daily/handbook-2026-27-barka.txt; raw/daily/handbook-2026-27-srs.txt
7. Pinkerton Academy's commuter map tells drivers to enter on Pinkerton Street at the Academy Building, drop off at one of two marked spots along the campus road, and for pickup park on the left side of the road beside the Fine Arts building, where students come to the car, then exit onto North Main Street; the lot off North Main Street is for buses and staff only.
   - citation: Pinkerton Academy, Student Drop-off & Pick-up ("Commuter Line" map)
   - source: https://www.pinkertonacademy.org/portals/parents/student-drop-off-pick-up
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Pinkerton Academy
   - note: Map text (read from the image; transcribed from image): "DROP-OFF ~Enter on Pinkerton St. @ the Academy Bldg. (Astro Cafe). ~Two locations for DROP-OFF PICK-UP ~Park on the LEFT side of the road next to the Fine Arts Bldg. ~Students will come to you." It marks "EXIT" on N. Main St., "BUSES & STAFF ONLY", "STUDENT PARKING" across N. Main St., and several crossed-out entrances on Pinkerton Street and N. Main Street. The map is labeled 2024. Map PDF: https://www.pinkertonacademy.org/uploads/files/Portals/Parents/Pick_Up-Drop_Off_Map.pdf. Raw: raw/daily/pinkerton/pa-dropoff-map-p1.png; raw/daily/pinkerton/pa-dropoff.txt
8. Pinkerton Academy is at 5 Pinkerton Street in Derry; in 2026-27 its classes end at 1:58 p.m. and Derry's Pinkerton buses leave then, while Hood Middle School, about 0.6 mile away in a straight line, dismisses at 2:30 with 13 bus routes and West Running Brook, about 1.1 miles away, at 2:35 with 16, a window the 2026-27 schedule change moved 40 minutes later.
   - citation: Pinkerton Academy, Bell Schedule and site footer; Derry Cooperative School District, School Hours and 2026-27 route sheets; OpenStreetMap Nominatim geocodes of the school addresses
   - source: https://www.sau10.nh.gov/families/school-hours
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: **Derived**: straight-line distances between the OpenStreetMap points for 5 Pinkerton Street, 5 Hood Road and 1 West Running Brook Lane (Hood–Pinkerton 0.63 mile, WRB–Pinkerton 1.13, Hood–Grinnell 0.14); route counts from the route sheets. Before 2026-27, Hood ended at 1:50 and WRB at 1:55 (district-school-day-and-calendar 2). Pinkerton footer: "5 Pinkerton Street, Derry, NH 03038". Whether this is what causes congestion on Pinkerton Street at 2:30 is not stated in any source. Bears on P13.3. Raw: raw/daily/sau10-school-hours.txt; raw/daily/pinkerton/pa-bell.txt; raw/daily/derry-bus-routes-2026-27-scheduled-times.csv; raw/daily/geo/
9. NHDOT's I-93 Exit 4A project, whose stated purpose is to reduce congestion and improve safety on NH Route 102 from I-93 through downtown Derry, is widening and rebuilding 0.9 mile of Folsom Road between Franklin Street and Pinkerton Street, with connected traffic signals; that contract began in December 2024 and is expected to finish in June 2028, and the whole project in 2029.
   - citation: NHDOT, Derry-Londonderry 13065 I-93 Exit 4A, About the Project
   - source: https://www.i93exit4a.com/about-the-project
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Page text: "The purpose of the I-93 Exit 4A Project is twofold: To reduce congestion and improve safety along NH Route 102 (Chester Road), from I-93 easterly through downtown Derry; To promote economic vitality in the Derry/Londonderry area". "Widening and reconstructing 0.9 miles of Folsom Road between Franklin Street and Pinkerton Street. A connected traffic signal system that will enhance capacity and operations on Folsom Road. Status: Construction began in December 2024 and is anticipated to be completed in June 2028". "Projected construction completion: 2029". The interchange contract (13065A) "was completed in July 2025". Raw: raw/daily/town/exit4a-about.txt; raw/daily/town/exit4a-updates.txt
10. The Exit 4A project also calls for widening 1.6 miles of Tsienneto Road between Pinkerton Street and Route 102; NHDOT lists that contract as in final design and due to be advertised in April 2027, while Derry's town administrator told the Town Council in June 2026 that it would not be bid until 2029, with construction probably in 2030–2032, and that a new signal at Pinkerton Street and Tsienneto Road is part of the Folsom Road contract due by June 2028.
   - citation: NHDOT, I-93 Exit 4A, About the Project (13065C); Town of Derry, Town Council minutes, June 30, 2026
   - source: https://www.derrynh.gov/AgendaCenter/ViewFile/Minutes/_06302026-332
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: NHDOT: "Widening and rehabilitation of 1.6 miles of Tsienneto Road between Pinkerton Street and NH Route 102 (Chester Road) ... Status: This project is in final design and scheduled to advertise in April 2027". Council minutes (transcript): "There'll be a signal that has to go in place at Pinkerton Street and Tsienneto ... all that should be done by June of 2028. Contract C is not even going to be bid out until 2029 at this point. And our expectation of the actual construction probably is now between 2030 and 2032." **The two sources differ on Contract C's timing.** Raw: raw/daily/town/council/tc-06302026-332.txt; raw/daily/town/exit4a-about.txt
11. In 2025-26 West Running Brook's newsletters thanked families for their cooperation at arrival and pickup and directed club pickups to pull around the right side of the building in the left lane only, and in June 2026 the board approved $35,000 to replace guardrail at West Running Brook; no district or town study of the school's drop-off line was found.
   - citation: WRB News, August 28 and September 12, 2025; Derry Cooperative School Board minutes, June 23, 2026
   - source: https://www.sau10.nh.gov/schools/wrb/news/1814312/wrb-news-8-28-25
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: district Derry Cooperative
   - note: August 28, 2025: "Thank you for your cooperation during pick up and arrival! Each day things are getting more efficient." September 12, 2025: "During pick-up, please pull around the building on the right side and fill the left lane only. Please leave the right lane open." June 23 minutes: "Guardrail replacement at West Running Brook Intermediate School: $35,000" (the minutes don't say where on the grounds). The 2026-27 WRB handbook has no car-line procedure. Searched: board minutes March–October 2026, At a Glance July 2025–June 2026, Highway Safety Committee minutes 2026. Answers part of P3.2. Raw: raw/daily/wrb-news-8-28-25.txt; raw/daily/wrb-news-9-12-25.txt; raw/daily/minutes/

## town-recreation-and-summer: Boys & Girls Club of Greater Derry After-School Program

- kind: local
- question_type: help
- description: Town recreation, after-school and summer programs, youth sports and camps, and their costs and scholarships

1. The Boys & Girls Club of Greater Derry (40 East Derry Road, 603-434-6695) runs a 2026-27 after-school program from 2:00 to 7:30 p.m. on school days for children who are at least 6 and in first grade, provides transportation from all Derry schools and Chester Academy, and charges $160 a month, with no daily or weekly option.
   - citation: Boys & Girls Club of Greater Derry, After School and home page FAQ
   - source: https://www.derrybgclub.org/after-school
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Page text: "After School Program 2026-2027 The after-school program begins the first day of school, August 25th, 2026. After-School Program hours of operation are from 2:00pm to 7:30pm. Cost: $160 a month- No daily or weekly options." "Must be 6 years old to attend and in first grade." Home page: "Q: What schools do you service for transportation? A: All Derry schools and Chester Academy." "Q: What time can my child stay if they are in elementary school? A: On school days 7:30pm on non-school days it is 6:00pm." The site's child care data lists the Club as licensed and accepting the NH Child Care Scholarship. Raw: raw/daily/community/bgc-after-school.txt; raw/daily/community/bgc-home.txt
2. The Boys & Girls Club of Greater Derry charges $75 a year in membership dues; on no-school days children not in the after-school program may attend for $8 a day paid ahead, and when Derry schools close for weather the Club opens from 8 a.m. to 6 p.m. for $8 a day (free that week for children already paid for after school), unless severe weather closes it.
   - citation: Boys & Girls Club of Greater Derry, Membership Dues & Fees; Snow Day Policy; After School
   - source: https://www.derrybgclub.org/snow-day-policy-1
   - as_of: 2026-11-15
   - review_by: 2027-11-15
   - place: town Derry
   - note: Dues page: "School Year Membership Dues $75 Applies to the current calendar year". After School: "There are a few days when the Club is open because of no school ... Payments for those days should be made in advance ($8 for each day)". Snow day page: "The Boys & Girls Club of Greater Derry's snow day programs are based on the Derry School District's cancellations. If schools are closed due to weather the Club will open at 8AM and close at 6PM ... Snow days cost $8.00 for the day ... Members who have already paid for the After-School Program that week, may attend on snow days at no additional cost". Raw: raw/daily/community/bgc-membership-dues.txt; raw/daily/community/bgc-snow-day-policy-1.txt; raw/daily/community/bgc-after-school.txt

## derry_bus_scheduled_ride_minutes_2026_27: Longest Scheduled Bus Rides on Derry's 2026-27 Routes (minutes, derived)

- unit: number (minutes)
- period: 2026-27 school year route sheets (updated September 7, 2026; Pinkerton sheets November 2, 2026); year: 2027
- source: Derry Cooperative School District, 2026-2027 bus routes (First Student) — https://www.sau10.nh.gov/departments/transportation/index
- as_of: 2026-11-15
- raw: raw/daily/derry-bus-routes-2026-27-scheduled-times.csv
- topic: district-transportation
- place: district Derry Cooperative
- note: **Derived** from the posted route sheets: morning = scheduled school arrival minus the scheduled time at the route's first stop; afternoon = scheduled time at the last stop minus the school departure. Value is the longest route for that school and run; the Note gives the number of routes and the median. Scheduled, not measured, times; the first student on (or last off) rides longest. The sheets list stops by house number, so only times were kept. Pinkerton routes are Derry's own buses to the Academy.

| Place | Trip | Value | Note |
|---|---|---|---|
| Derry Cooperative | Pinkerton Academy, morning (route PA19, 6:03 to 6:45 a.m.) | 42 | 19 routes, all arriving 6:45; median 19 |
| Derry Cooperative | Pinkerton Academy, afternoon (route PA19, 1:58 to 2:36 p.m.) | 38 | 21 routes, 20 leaving 1:58 and one 1:50; median 16 |
| Derry Cooperative | Gilbert H. Hood Middle, morning (GHH01, 7:07 to 7:45 a.m.) | 38 | 13 routes, all arriving 7:45; median 32 |
| Derry Cooperative | Gilbert H. Hood Middle, afternoon (GHH01, 2:30 to 3:05 p.m.) | 35 | 13 routes leaving 2:30; median 32 |
| Derry Cooperative | West Running Brook Intermediate, morning (WRB12, 7:08 to 7:50 a.m.) | 42 | 16 routes, all arriving 7:50; median 31.5 |
| Derry Cooperative | West Running Brook Intermediate, afternoon (WRB12, 2:35 to 3:22 p.m.) | 47 | 16 routes leaving 2:35; median 29 |
| Derry Cooperative | East Derry Memorial, morning (EDME17, 8:01 to 8:40 a.m.) | 39 | 8 routes, all arriving 8:40; median 33.5 |
| Derry Cooperative | East Derry Memorial, afternoon (EDME17, 3:10 to 3:49 p.m.) | 39 | 8 routes leaving 3:10; median 30.5 |
| Derry Cooperative | Ernest P. Barka, morning (EBES05, 8:03 to 8:40 a.m.) | 37 | 8 routes; median 31 |
| Derry Cooperative | Ernest P. Barka, afternoon (EBES07, 3:10 to 3:45 p.m.) | 35 | 8 routes; median 28.5 |
| Derry Cooperative | Grinnell, morning (GES28, 8:07 to 8:40 a.m.) | 33 | 5 routes; median 29 |
| Derry Cooperative | Grinnell, afternoon (GES28, 3:10 to 3:41 p.m.) | 31 | 5 routes; median 30 |
| Derry Cooperative | South Range, morning (SRES06, 8:09 to 8:40 a.m.) | 31 | 5 routes; median 27 |
| Derry Cooperative | South Range, afternoon (SRES27, 3:10 to 3:41 p.m.) | 31 | 5 routes; median 25 |

## derry_safe_grants_2026: SAFE Security Grants Accepted by the Derry Cooperative School Board, March 2026

- unit: dollars
- period: Accepted March 24, 2026; year: 2026
- source: Derry Cooperative School Board minutes, March 24, 2026 — https://drive.google.com/file/d/1ogVztqbO03RfQZ6Du6vEUi90jwpc_vjQ/view?usp=sharing
- as_of: 2026-11-15
- raw: raw/daily/minutes/sb-minutes-2026-03-24.txt
- topic: district-safety-and-security
- place: district Derry Cooperative
- note: Two grants per school, as read into the minutes ("$16.000" for East Derry Memorial is printed with a period). The minutes describe them as additional security cameras and re-keying at Hood. The total row is **derived** ($225,119.99); the superintendent and the board's summary say "approximately $260,000".

| Place | School | Value | Note |
|---|---|---|---|
| Derry Cooperative | East Derry Memorial Elementary | 21378.32 | plus a second grant of 16,000 |
| Derry Cooperative | Ernest P. Barka Elementary | 25974.99 | plus 16,000 |
| Derry Cooperative | Gilbert H. Hood Middle | 26510.65 | plus 16,000; includes re-keying |
| Derry Cooperative | Grinnell Elementary | 18393.46 | plus 16,000 |
| Derry Cooperative | South Range Elementary | 15734.82 | plus 16,000 |
| Derry Cooperative | West Running Brook Intermediate | 21127.75 | plus 16,000 |
| Derry Cooperative | All six schools, both grants (derived) | 225119.99 | 129,119.99 plus 6 × 16,000 |

## For another file

- **Agent 2 (Pinkerton student life, P30.1 start time):** Derry's earliest 2026-27 Pinkerton pickup is 6:03 a.m. (route PA19) and every Derry morning run reaches Pinkerton at 6:45 for a 7:15 start (district-transportation 7, 9). Pinkerton's start-time committee page links a problem statement (5:45–6:03 a.m. first pickups in five of six sending towns), a sending-town presentation with a table of NH high school start times (Pinkerton 7:15–1:58; Windham 7:52; Bedford 7:50/7:55; Portsmouth 8:30) and survey results: https://www.pinkertonacademy.org/about/start-time-committee-information (raw: raw/daily/pinkerton/pa-start-problem.txt; the presentation was read at https://drive.google.com/file/d/1n9BPvXwCB6zcvqq6Csl9CXQevll-8YyE/view). The October 2025 and April 2026 Derry board items say Derry's own change was meant partly to end long waits at Pinkerton.
- **Shared Pinkerton folder (`town/pinkerton/`):** the Pinkerton facts here (district-school-day-and-calendar 19; district-transportation 14–15; district-safety-and-security 13–14; district-family-communication 4–7; town-streets-and-safe-routes 7) are written for any sending town and could move to the shared folder.
- **Agent 7 (money, P25.1 voting at Pinkerton's gym):** the Town Council's October 6, 2026 minutes discuss one-hour parking at Pinkerton for voters and recall that splitting the 2018 vote between West Running Brook and Hood "caused tons of traffic" (https://www.derrynh.gov/AgendaCenter/ViewFile/Minutes/_10062026-369; downloaded to the scratchpad, not copied to raw). Also for agent 7: the October 13, 2026 minutes list each school's 2024 bond and capital plan items (raw/daily/minutes/sb-minutes-2026-10-13.txt); Derry's 2022 SAFE grant row is in district-safety-and-security 7.
- **Agent 3 (elementary, P6.2 early release days):** the February 2026 board summary says the 2026-27 calendar cut early release days from four to two "in response to family feedback" (raw/daily/sb-glance.txt); the dates are September 23 and May 18 (district-school-day-and-calendar 17).
- **Agent 4 (grades 5–8, P24.1 driver retention):** September 9, 2026 minutes cite driver shortages for 5th–6th grade athletic busing; the fleet is 29 large buses versus 34 in earlier years (district-transportation 10–11). The district's 2026-27 board goal is a new contract with AFSCME, the educational assistants' union (August 25, 2026 minutes).
- **Agent 6 (families, P17.3 Next Charter buses):** policy EEA covers approved private school pupils and does not mention charter school students; no Next Charter route is posted (raw/daily/sau10-policy-EEA.txt).
- **Earlier towns:** none of this contradicts another town's file. The NH DOE SAFE handout already saved in `town/Jackson/raw/policies/grants/` was copied here for Derry's and Pinkerton's rows.

## Not retrieved

- Web searches: the session's shared web search budget ran out partway through. Not searched as a result: news of lockdowns, threats or social-media rumors at Derry schools or Pinkerton in 2025–2026 (including the "May 20 incident report" the June 9, 2026 board minutes mention from a May 28 meeting with Pinkerton), news on Derry SRO staffing, and any Derry crossing guard program.
- Greater Derry Extended Day Program: no website was found in one search; its rates, registration and waitlists are not posted on SAU 10's pages. Directory sites (winnie.com) were not used.
- https://www.derrynh.gov/police-department: 404. The department's pages under /425/ have no SRO or crossing guard page.
- https://drive.google.com/file/d/1URx9pC997T45Q9M-yGO5PASVqatxlC4X (SAU 10 general ledger FY2025): the PDF is encrypted; its readable text had no crossing guard or SRO lines. Not used.
- Board minutes for May 26, 2026 (intercom bid, policy readings): not listed on the agendas page as a file; the "At a Glance" summary was used instead.
- 2026-27 school newsletters for West Running Brook and Hood: sent by ParentSquare, not posted online.
- https://mtabus.org/cart-service-derry-demand-response/ (linked from the town page): 404; https://mtabus.org/cart/ was used.
- The Derry route sheets (https://www.sau10.nh.gov/departments/transportation/index, 14 PDFs): retrieved and read, but not copied to raw because they list stops by house number and one contains a stray name; only route times were kept.
- NH DOE's list of 2026 (Round 4) SAFE awards: not retrieved; Derry's 2026 amounts come from the board minutes.
