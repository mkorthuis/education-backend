# Getting to School and the School Day

Part of the Chatham research (town/Chatham). Gathered November 13, 2026.

## Summary

This file covers how Chatham children get to their schools in Maine and what their school day and year look like. Chatham runs no schools. Its younger students attend Maine School Administrative District 72 (MSAD 72) schools: New Suncook School in Lovell and Molly Ockett School in Fryeburg. Its high school students attend Fryeburg Academy. The file covers who drives the buses, routes and ride distances, late buses, storm closings, Route 113's winter status, school hours, early release, after-school care, the 2026-27 calendars, school meals, attendance and truancy rules, and extended school year (ESY) services.

- **6 topics, 52 facts and 2 number tables.**
- **Main sources:**
  - Chatham School Board minutes (2020–2026), agendas and the 2026 annual report, from SAU 9's Google Drive folders.
  - MSAD 72's website, policies (EBCE, ICA, JE, JEA), 2026-27 and 2025-26 calendars, late-bus calendar, route sheet, the Molly Ockett 2026-27 and New Suncook 2025-26 handbooks, board minutes, the August 2026 annual report and the Pequawket Kids Afterschool (PKA) pages.
  - Fryeburg Academy's 2026-27 calendar, bell schedule, athletics and dining pages.
  - Maine statutes (20-A MRSA §§3272, 5001-A, 5051-A, 6602).
  - White Mountain National Forest road status and MaineDOT notices for Route 113.
- **Derived figures:**
  - Driving distances and times from three points in Chatham to the three schools, from OSRM on OpenStreetMap data (geocoded with Nominatim under the `nhfacts-research` identifier).
  - Days off for each 2026-27 break at MSAD 72, Fryeburg Academy and SAU 9, counted from the published calendars.
- **Main gaps:**
  - Chatham's own bus routes and stop times are not published anywhere.
  - The Bennett Transportation contract text was not found.
  - No delayed-opening schedule for MSAD 72 was found.
  - Fryeburg Academy's student handbook (attendance, transportation, late buses) was not found online.
  - No Maine source says whether "publicly funded student" in the universal meals law includes New Hampshire tuition students.
  - No official source gives the location of the Route 113 winter gates.
  - No MSAD 72 summer school was found.

**Premises checked:**

- **"Early-release Wednesdays at 12:30 p.m." (P5.1, P15.1).** True for 2025-26, when MSAD 72 released students at 12:30 every Wednesday. For 2026-27 there is only one early-release Wednesday a month (nine dates) plus the last day. Fryeburg Academy uses the same Wednesdays but dismisses at 12:45.
- **"A 4th grader at Molly Ockett School" (P5.1).** Chatham children in grades K–4 attend both New Suncook (Lovell) and Molly Ockett (Fryeburg). On April 1, 2025, two Chatham 4th graders were at each school. The early-release and calendar dates are district-wide, so they are the same at both.
- **"The MSAD #72 school bus" in Chatham (P10.1).** Chatham does not ride MSAD 72 buses. The Chatham School District contracts its own transportation with Bennett Transportation. MSAD 72 took over transportation for its Maine towns in 2021, and Bennett continued to serve Chatham.
- **"Evans Notch Road" (P10.1).** This is the National Forest's name for Route 113 in Maine. In Chatham, OpenStreetMap names Route 113 "Main Road" and has no road called Evans Notch Road. The Evans Notch section through the White Mountain National Forest is in Maine (Stow, Batchelders Grant and Gilead), and the Forest Service lists it as "Not maintained for winter travel".
- **"Maine's universal school meals program, even though we live in NH" (P5.2).** In 2022 the Chatham board was told Chatham students were "not eligible" because they live in New Hampshire. MSAD 72's three schools now serve all their students breakfast and lunch at no charge under the federal Community Eligibility Provision or Provision II, and Chatham's board pays Fryeburg Academy for Chatham students' meals.
- **"20-A MRSA §3272" (P15.3).** That section is in Maine's chapter for the unorganized territory. For a school unit like MSAD 72, the matching rules are §5001-A (attendance and excused absences) and §5051-A (truancy).
- **"Both K–8 and 9–12 are in Fryeburg" (P20.2).** A 3rd grader and a 7th grader are both MSAD 72 students and share one calendar. A Chatham 3rd grader may attend New Suncook in Lovell rather than Fryeburg. MSAD 72 and Fryeburg Academy do not share one calendar.

**Proposed new shared topic:** `maine-school-rules` (kind rule, question type rules, no place), "Maine laws that apply in Maine schools attended by students tuitioned from New Hampshire: compulsory attendance, excused absences and truancy, and school meals." It holds the Maine statute facts below. Other Maine rules (diploma requirements, tuition rates) could merge into it.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.3 Morning bus ride from North Chatham down Route 113, and after-school care | district-transportation 1–6; chatham_drive_distance_to_schools_derived; town-streets-and-safe-routes 3; district-school-day-and-calendar 1–2, 7–10, 12 | partial | Chatham's contracted bus routes and times are not published, so ride times can't be given. Driving from North Chatham is about 35 minutes by car to Fryeburg and 25 minutes to New Suncook in Lovell (derived). After-school care: PKA (K–4) at Molly Ockett until 5:30 p.m. Licensed child care is in the community file. |
| P5.1 Snow delays and early-release Wednesdays against child care | district-school-day-and-calendar 4–5, 7–9, 13; district-transportation 6, 11 | partial | Early release is now monthly (nine Wednesdays, 12:30). PKA runs 12:30–5:30 on those days for registered children, and does not run when school closes or dismisses early for weather. MSAD 72 can delay openings, but no delay schedule was found. |
| P5.2 Free breakfast and lunch for Chatham students | district-meals 1–6; maine-school-rules 6 | full | MSAD 72 schools serve all students free; Chatham pays Fryeburg Academy for Chatham students' meals. Whether the Maine law itself covers NH tuition students is not settled by any source found. |
| P5.3 Storm closes Route 113: excused absence? | district-transportation 11; maine-school-rules 2; district-school-day-and-calendar 21; town-streets-and-safe-routes 1–3 | partial | MSAD 72 policy EBCE leaves attendance on open days "to parents." Neither Maine law nor MSAD 72 policy names road closures or weather as an excused reason. No record of Route 113 closures south of Evans Notch was found. |
| P10.1 Does a bus go up the Evans Notch end of Route 113 in winter? | district-transportation 1–5; town-streets-and-safe-routes 1–3 | partial | Chatham's buses are Bennett's, not MSAD 72's. The Evans Notch section is in Maine and is not maintained in winter. Chatham's stop list is kept by SAU 9 but not published. |
| P11.3 Late buses or carpools for Fryeburg Academy athletics, theater, ski team | district-transportation 7–10; district-school-day-and-calendar 12 | partial | MSAD 72's two late buses (4:55 p.m. from Molly Ockett, about 5:00 from the Academy) go to Lovell and Brownfield/Denmark only. No late bus to Chatham or carpool program was found. The 2027 Jackson–Academy agreement (Jackson file: district-transportation 45 in `Jackson/getting-to-school-and-the-school-day.md`) gives Jackson students the same extracurricular transportation as other day students; no Chatham agreement was found. |
| P15.1 Why early release, and free or low-cost after-school programs | district-school-day-and-calendar 4–11 | full | Early release gives teachers meeting time. It was cut from weekly to monthly for 2026-27 "to provide more instructional time." PKA costs $110 or $225 per session, with limited scholarships (fees shown on an older PKA page). |
| P15.3 Fryeburg Fair and farm work: Maine truancy rules for NH residents | maine-school-rules 1–5; district-school-day-and-calendar 13–14, 18–21; library: compulsory-attendance, truancy (NH) | partial | Both MSAD 72 and Fryeburg Academy close for Fryeburg Fair Day (October 9, 2026). MSAD 72 counts extra vacations as unexcused, and planned absences need prior approval. No source says how Maine's civil-violation step applies to New Hampshire parents. |
| P18.3 Summer school or ESY transport from South Chatham | district-special-education-services 1–2; district-transportation 13 | partial | ESY is decided by the IEP team at no cost to parents (SAU 9 manual). Chatham budgets for ESY and special education transport, but no source describes ESY transport from South Chatham. No MSAD 72 summer school was found. |
| P20.2 Maine vs NH calendars, February and April vacations, snow days; shared calendar? | district-school-day-and-calendar 13–17, 22; chatham_calendar_days_off_2026_27_derived | full | In 2026-27, February vacation is the same week in MSAD 72 and SAU 9, while April vacation differs by a week. Fryeburg Academy's February and April breaks start two days earlier than MSAD 72's. MSAD 72 builds in five snow days. |

## district-transportation: Bus Service

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. The Chatham School District contracts its school bus service with a private company, Bennett Transportation; the Chatham School Board approved the transportation contract with Bennett Transportation on June 1, 2022, and the contract ends June 30, 2027.
   - citation: Chatham School Board minutes, June 1, 2022 (III.C) and December 9, 2025 (3)
   - source: https://drive.google.com/file/d/1ZPaTv5XZUG5O4b_154svDLxKTdw5PFeu/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: June 1, 2022 text: "C. Award Chatham Transportation Contract- Motion by Sue Crowley, seconded by Sue Perry to approve the transportation contract with Bennett Transportation. (2-0-0)". December 9, 2025 (scanned; transcribed from image): "Mike Wade stated that the transportation contract ends June 30, 2027. Mike Wade will reach out to Bennett prior to next budget season to seek a contract renewal." December 2025 minutes source: https://drive.google.com/file/d/1X7DXxpuu1v4p92UZskoEukNwRxtZLSk7/view. Raw copies: raw/daily/chatham-board/chatham-min-2022-06-01.txt; raw/daily/chatham-board/chatham-min-2025-12-09.ocr.txt
2. In June 2021 the Chatham School Board was told that MSAD 72 was taking over school transportation for its Maine towns and that Bennett Transportation would continue to serve Chatham under its contract, so Chatham children do not ride MSAD 72's district buses to school.
   - citation: Chatham School Board minutes, June 22, 2021 (IV.C)
   - source: https://drive.google.com/file/d/1h46LUN2mYvYp-ENH94qr8PR9vRBiDUTW/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "C. Transportation- MSAD 72 is taking over transportation for the Maine towns as Bennett Transportation will continue to support Chatham and continue to honor their contract." The last clause of the statement is a plain reading of this line plus fact 5 (no Chatham stops on MSAD 72's route sheet). Earlier minutes show Bennett working with Chatham by January 2020 ("Jim noted that we need to investigate transportation (contract to be discussed). Jim will communicate with Bill Bennett") and September 2020 ("Jim Hill noted that he has worked with Bennett Transportation on bus routes and schedules"). Raw copies: raw/daily/chatham-board/chatham-min-2021-06-22.txt; chatham-min-2020-01-07.txt; chatham-min-2020-09-01.txt
3. In June 2026 SAU 9's business administrator told the Chatham board that Bennett preferred a three-year renewal rather than five years "given all of the changes in fuel," and in October 2026 he reported working with Bennett on 2027-28 transportation with "no major changes that we can anticipate at this time."
   - citation: Chatham School Board minutes, June 30, 2026 (4.d) and October 13, 2026 draft minutes (3.c)
   - source: https://drive.google.com/file/d/19aFgV21YcDG4UWbR_04nqsIrvrhQIZ67/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: June 30, 2026: "Mike Wade shared that he has communicated with the bus company regarding a five-year contract. William Bennett stated that he preferred a three-year contract, given all of the changes in fuel, etc. The current contract expires in June 2027. Mike Wade will begin drafting a contract with Bennett." October 13, 2026 (draft): "Mike Wade shared that he is working on transportation with Bennett. There are no major changes that we can anticipate at this time." October source: https://drive.google.com/file/d/1L3K4PO3zbSLmrGKbRlXNT45GnSw8ywCi/view. Raw copies: raw/daily/chatham-board/chatham-min-2026-06-30.txt; chatham-min-2026-10-13-draft.txt
4. Chatham's school budget has a pupil transportation line (2720) made up of three accounts: contracted transportation service, special education transportation, and fuel for buses; the 2026-27 budget for the line is $85,804.
   - citation: Chatham School District 2026-2027 Proposed Budget (2026 annual report); Chatham Budget Status Report, October 8, 2026 (Chatham School Board agenda, October 13, 2026, item 3-b)
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Accounts: "31-10-2720-5513-0120 TRANSPORTATION,CONT SERVICE", "31-10-2720-5519-0120 TRANSPORTATION,SPECIAL ED", "31-10-2720-5626-0086 FUEL, BUSES"; 2026-27: $68,189 + $7,200 + $10,415 = "TOTAL 2720 PUPIL TRANSPORTATION $85,804". Annual report page 6 is a scan, read from the page image. The full year-by-year figures are listed under "For another file" for the money file. Agenda source: https://drive.google.com/file/d/1YbkVLG1VHhVPvahLRpMpZCoNdVWd9vVW/view. Raw copies: raw/daily/chatham-board/chatham-ar2026-p6.png; raw/daily/chatham-board/chatham-ag-2026-10-13.txt (page 5)
5. Chatham's bus routes and stop times are not published: SAU 9's 2026-27 bus route page lists routes for Albany, Eaton, Conway, Jackson and Bartlett but none for Chatham, MSAD 72's 2026-27 route sheet lists no stop on Chatham's Main Road, and in April 2023 SAU 9's business administrator gave the Chatham board "a list of all of the Chatham students with their bus stop and pick up and drop off times," after which the board recommended no changes.
   - citation: SAU 9 Transportation page, "SAU#9 Bus Routes & Schedules 2026-2027"; MSAD 72 Bus Routes and Stop Times (2026-27 spreadsheet); Chatham School Board minutes, April 4, 2023 (5.A)
   - source: https://www.sau9.org/transportation
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: April 4, 2023 text: "Transportation Options - Jim Hill presented a list of all of the Chatham students with their bus stop and pick up and drop off times. Jim also reviewed the geography of the bus routes. All of the routes were reviewed and discussed and there are no recommended changes to take place." The SAU 9 page lists route PDFs for Eaton and Conway, Albany ("contact Eldridge Transportation"), Conway, North Conway, Intervale, Jackson and Bartlett, and SAU 13. The MSAD 72 sheet (https://docs.google.com/spreadsheets/d/199G4tpRqXEEDdFpwV9NRiQWy2vbk9jIefCA74EKLKCs/edit) covers nine buses (Black, Blue, Green, Grey, Orange, Red, Tan, Teal, Yellow). Its stops nearest Chatham are on Stow Road, South Chatham Road and "Green Hill & Kimball Shores"; OpenStreetMap places South Chatham Road and Kimball Lake Shores Road in Stow and Fryeburg, Maine. The sheet gives no Chatham addresses. April 2023 source: https://drive.google.com/file/d/1AYTkocoPQ8M761zSERed-MeXe0RBgfEr/view. Raw copies: raw/daily/sau9/sau9-transportation.txt; raw/daily/msad72/msad72-bus-routes.tsv; raw/daily/chatham-board/chatham-min-2023-04-04.txt; raw/daily/routing/nominatim-3.json
6. Chatham's K–8 students attend more than one MSAD 72 school: on April 1, 2025, MSAD 72 counted 28 Chatham students, 12 in grades K–4 at New Suncook School in Lovell and 16 in grades 2–8 at Molly Ockett School in Fryeburg, plus one Chatham child in the Head Start pre-K class at New Suncook.
   - citation: MSAD 72, "April 1st K - 8 Enrollment by Town/School 2025," attached to Chatham School Board minutes, June 17, 2025
   - source: https://drive.google.com/file/d/1iIVh4EDAYBrcKx2jVDhmPrmKho-3nZ1N/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Transcribed from image (page 5 of the minutes PDF). CHTM column: New Suncook K 4, grade 1 1, grade 2 3, grade 3 2, grade 4 2; Molly Ockett K 0, 1 0, 2 1, 3 1, 4 2, 5 3, 6 2, 7 4, 8 3; total 28; "Headstart Pre-K - NS" 1. So in April 2025, two Chatham 4th graders were at New Suncook and two at Molly Ockett. The minutes text says: "There are currently 28 students across Brownfield Denmark, New Suncook, and Molly Ockett," but the table shows none at Brownfield Denmark. The 2026 Chatham annual report lists "K-5 New Suncook School, Lovell" and "K-8 Molly Ockett School, Fryeburg" (raw/daily/chatham-board/chatham-ar2026-p1.png). See table chatham_drive_distance_to_schools_derived. Raw copies: raw/daily/chatham-board/chatham-min-2025-06-17-p5.png; chatham-min-2025-06-17.ocr.txt
7. MSAD 72 runs its own bus fleet for its seven Maine towns, "transporting almost 1,200 students in the school district every day," and Fryeburg Academy students from those towns ride the same district buses, with bus alerts sent to Academy families through Remind.
   - citation: MSAD 72 Transportation page; "Remind Notification System for Transportation for Fryeburg Academy Students & Families"
   - source: https://www.msad72.org/departments/transportation
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Page text: "Transporting almost 1,200 students in the school district every day!" and "Links to sign up for Bus Notifications (Fryeburg Academy only)". Remind document: "PLEASE NOTE: This is for Fryeburg Academy Students grade 9-12 only. MSAD 72 students K-8 are notified using our Student Information Systems messaging system," listing the Black, Blue, Orange, Grey, Teal, Tan, Green, Red and Yellow buses. The MSAD 72 August 2026 annual report says "All in-district vehicles are now equipped with GPS tracking for the new school year." Raw copies: raw/daily/msad72/msad72-departments_transportation.txt; msad72-remind-bus-notifications-fa.txt; msad72-annual-report-2026-08.txt
8. MSAD 72 runs two late buses that leave Molly Ockett School at 4:55 p.m. and Fryeburg Academy at about 5:00 p.m.: one goes up Route 5 to Lovell (New Suncook School, Hobbs Memorial Library, Center Lovell Market, A.J.'s) and the other goes to Brownfield and Denmark (Grant's, Brownfield Denmark Elementary School, Jim Bob's); MSAD 72 says "There is no late bus for the Fryeburg area," and none of the listed stops is in Chatham.
   - citation: MSAD 72 Transportation page, "Late Bus"; MSAD 72 Athletics page
   - source: https://www.msad72.org/departments/transportation
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Transportation page: "The school district provides 2 buses for late bus. These buses load then depart Molly Ockett School at 4:55 PM and travel to Fryeburg Academy. Departure time from FA is approximately 5:00 PM. The route: Route 5 - stops are New Suncook School / Hobbs Memorial Library / (West Lovell Rd/Rt 5, if requested) / Center Lovell Market / A.J's. Route 113 - stops are Grant's / Brownfield Denmark Elementary School / Jim Bob's." Athletics page (https://www.msad72.org/information/athletics): "There are two late buses; one bus travels to Lovell, and the other bus travels to Brownfield & Denmark. Please note that the late bus routes do not include the normal bus stops and have an abbreviated route. There is no late bus for the Fryeburg area." The "Route 113" late bus runs south of Fryeburg toward Brownfield, not north toward Chatham. Raw copies: raw/daily/msad72/msad72-departments_transportation.txt; msad72-information_athletics.txt
9. MSAD 72's late buses run Monday through Friday but not on early-release Wednesdays, the day before a long weekend or vacation, or when Fryeburg Academy is closed and MSAD 72 is not; MSAD 72 says the Academy is "sometimes" on a different schedule, starting its winter break a week before the district's.
   - citation: MSAD 72 Transportation page, "Late Bus"; MSAD 72 2026-2027 School Calendar with Late Bus Schedule
   - source: https://www.msad72.org/departments/transportation
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Page text: "The late bus runs on Monday, Tuesday, Wednesday, Thursday, & Friday (Not on early-release Wednesdays)"; "A Monday holiday – There's no late bus the Friday before a long weekend"; "There's no late bus a day prior to the start of a vacation"; "Fryeburg Academy, sometimes, is not on the same academic schedule as MSAD #72. When FA is closed, such as during their winter break holiday - their vacation starts one week prior to the school district - no late bus services are provided." The late-bus calendar (https://drive.google.com/file/d/1q44RYJHQRRGL43yNTca5_rdljft9uGhj/view) marks "NO LATE BUS" days in grey, including June 7–14, 2027. The athletics page says the late bus began running Tuesday, September 8. Raw copies: raw/daily/msad72/msad72-departments_transportation.txt; latebus-cal-2026-27-p1.png
10. Fryeburg Academy's athletics page lists 2026 fall preseason practices that end as late as 7:00 p.m. (football, 5:00–7:00 p.m. in the first week); its alpine ski teams race at Pleasant Mountain and its Nordic teams train on trails at Stark's Hill, and its snow sports program offers "afternoon, evening, and weekend trips to nearby ski resorts."
   - citation: Fryeburg Academy, Athletics and Snow Sports pages
   - source: https://www.fryeburgacademy.org/athletics
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Athletics page: "Football ... Practices are scheduled 7:30-9:30 am and 5:00–7:00 pm throughout the first week"; "Field hockey will train 7:00 – 8:30 am and 4:00 – 5:30 pm"; boys' and girls' soccer "practice at 7:00 am and again at 6:00 pm"; golf at "Lake Kezar Country Club in Lovell, Maine, at 4:00 pm". Snow Sports (https://www.fryeburgacademy.org/athletics/snow-sports): "Our teams race Slalom and Giant Slalom at our local ski resort, Pleasant Mountain"; "Our local trails at Stark's Hill". Neither page says how day students get home after practice. Raw copies: raw/daily/fa/fa-athletics.txt; raw/daily/fa/fa-athletics_snow-sports.txt
11. MSAD 72's policy EBCE lets the superintendent cancel school, delay opening or dismiss early for severe weather or "hazardous travel conditions," with closing decisions made by 6:00 a.m.; when school closes or dismisses early, all after-school and evening activities are cancelled, and "When school is in session, it remains the responsibility of parents to decide whether or not their children shall attend school under the existing conditions."
   - citation: MSAD 72 policy EBCE, School Closings and Cancellations (adopted July 12, 2017)
   - source: https://docs.google.com/document/d/1531fOkcH5jRmDH8N7VnDgp1CwfyKoBPV6K8trjK8H0g/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Policy text: "The Board authorizes the Superintendent to cancel or close school(s) for the day, delay opening, or dismiss school(s) early in the event of severe weather, hazardous travel conditions, or other emergencies ... Decisions to close school for the day will be made no later than 6:00 A.M." Posted on MSAD 72's policy page as "BCE"; the document's file code is EBCE. The Molly Ockett 2026-27 handbook lists radio and TV stations and www.msad72.org for closing notices. The policy does not say whether an absence on a day a family judges travel unsafe is excused. Raw copies: raw/daily/msad72/msad72-policy-EBCE.txt; raw/daily/msad72/mos-handbook-2026-27.txt
12. MSAD 72's handbooks say K–8 students should have consistent pick-up and drop-off locations, district buses may be used after school for school activities such as band, chorus or PKA (and for town recreation programs if space allows), and changes to a child's afternoon bus or pick-up must reach the school in writing before 11:00 a.m.
   - citation: Molly Ockett School Student-Parent Handbook 2026-2027, "Busing/Transportation Arrangements"; MSAD 72, "Change of Dismissal Plans?"
   - source: https://docs.google.com/document/d/1ucywQEBp7sGDvuLR7IITnxJjyR891s69idRfpQhjU7o/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Handbook text: "For after-school transportation, students may use District transportation for the following: school-sponsored activities like after-school band/chorus or PKA. If space allows, students may also use District transportation to attend town recreational programs." Dismissal notice (https://docs.google.com/document/d/182hbawCNFAo-V5RFt9Ac4BHpmZ8RIdDnKXCDyfNkWr8): "we require that a written notice of the change is delivered to the school prior to 11 AM ... the school will not be able to honor changes made over the phone or after 11 AM." These rules describe MSAD 72's district buses; no source says how they apply to Chatham's contracted bus. Raw copies: raw/daily/msad72/mos-handbook-2026-27.txt; raw/daily/msad72/msad72-change-of-dismissal.txt
13. Chatham pays separately for special education transportation: the account spent $6,421 in 2023-24 and $7,773 in 2024-25, and in October 2026, $32,864 was already committed against its 2026-27 budget of $7,200, a point the board chair asked about at the October 13, 2026 meeting.
   - citation: Chatham School District Special Education Expenses/Revenue 2023-2024, 2024-2025 (2026 annual report, p. 12); Chatham Budget Status Report, October 8, 2026; Chatham School Board draft minutes, October 13, 2026
   - source: https://drive.google.com/file/d/1YbkVLG1VHhVPvahLRpMpZCoNdVWd9vVW/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Annual report (scan, OCR checked against image): "2720.519.120 Transportation, Special Education $6,421 [2023-24] ... $7,773 [2024-25]". Budget status: "31-10-2720-5519-0120 TRANSPORTATION,SPECIAL ED 7,200.00 7,200.00 4,576.00 32,864.00 (30,240.00) (420.00)%" (adopted, revised, spent, encumbered, remaining). Draft minutes: "Sue Perry asked about special education transportation and the cost associated." No source says what the transportation is for. Raw copies: raw/daily/chatham-board/chatham-ar2026.ocr.txt (page 12); chatham-ag-2026-10-13.txt (page 5); chatham-min-2026-10-13-draft.txt

## district-school-day-and-calendar: School Hours, Care and Calendar

- kind: local
- question_type: local_practice
- description: School hours, before- and after-school care, the school calendar and vacations, and attendance and absence rules

1. At Molly Ockett School in 2026-27, classroom instruction begins at 8:00 a.m., students are expected in class by 7:45 a.m., there is no supervision before 7:30 a.m., and dismissal is at 2:30 p.m.
   - citation: Molly Ockett School Student-Parent Handbook 2026-2027, "Student Drop Off/Pick Up" and daily schedule
   - source: https://docs.google.com/document/d/1ucywQEBp7sGDvuLR7IITnxJjyR891s69idRfpQhjU7o/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Handbook text: "Classroom instruction begins at 8:00 AM. In order to have time for handing in notes, taking off winter clothes, and settling into the school day, we expect all students to be in their classrooms by 7:45 AM ... children should not be in the school building or schoolyard before 7:30 AM. There is no supervision before that time." and "We ask that parents do not arrive to pick up their child before 2:30 each day". The middle school schedule runs from "7:30 -7:50 HR / Breakfast" to "2:30 Dismissal". Raw copy: raw/daily/msad72/mos-handbook-2026-27.txt
2. New Suncook School in Lovell, MSAD 72's K–4 school, listed a 7:30 a.m. arrival, an 8:00 a.m. start and a 2:30 p.m. dismissal in its 2025-26 handbook, with a 12:30 p.m. dismissal on Wednesdays that year.
   - citation: New Suncook Elementary School Student-Parent Handbook 2025-2026, "New Suncook Daily Schedule"; MSAD 72, New Suncook "Information and Links"
   - source: https://docs.google.com/document/d/1W9R9H63HFFTwfqMDGczc_quwqIrZIQCY2s2VyFAEubM/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Handbook text: "Student school arrival time: 7:30 AM / School start time: 8:00 AM (Instruction begins) / School dismissal time: 2:30 PM Wednesday dismissal: 12:30". The 2026-27 New Suncook handbook was not found; for 2026-27, Wednesday early release is monthly (fact 4). Information page: "New Suncook School is a public school operated by MSAD 72 providing for the education of pupils in grades K through 4." Raw copies: raw/daily/msad72/new-suncook-handbook-2025-26.txt; msad72-schools_new-suncook-elementary_nses-information.txt
3. Fryeburg Academy's 2026-27 class day runs 8:00 a.m. to 2:35 p.m. Monday through Friday, and on its once-monthly early-release Wednesdays classes end at 12:45 p.m.; the Academy's calendar says it "will follow the MSAD72 schedule of early release one Wednesday per month."
   - citation: Fryeburg Academy 2026-27 Bell Schedule; Fryeburg Academy School Calendar 2026-27
   - source: https://resources.finalsite.net/images/f_auto,q_auto,t_image_size_6/v1781187192/fryeburgacademyorg/qb3kg6an0647kolec2s1/2026-27BellSchedulePUBLIC11JUN.png
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Bell schedule image (linked as "2026-27 Class Bell Schedule" on https://www.fryeburgacademy.org/parents): first period 8:00 AM every day; last period ends 2:35 PM; "Once-Monthly Early Release Schedule Wednesday ... EE 11:30 AM 12:45 PM". Calendar: "Fryeburg Academy will follow the MSAD72 schedule of early release one Wednesday per month" and "16 Wed Early Release 12:45pm" (September), with the same Wednesdays as MSAD 72 through May 19. Raw copies: raw/daily/fa/fa-bell-schedule-2026-27.png; raw/daily/fa/fa-calendar-2026-27.txt
4. In 2026-27, MSAD 72 dismisses students at 12:30 p.m. on nine Wednesdays (September 16, October 21, November 18, December 16, January 20, February 24, March 17, April 28 and May 19) and on the last day of school.
   - citation: MSAD 72 2026-2027 School Calendar (FINAL 5/6/2026)
   - source: https://drive.google.com/file/d/1CPwY4ANIxMG0QPb60q537KspUYxJ_0gB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Read from the calendar image; the legend reads "Early Release - 12:30 Dismissal" (dotted days) and "*Last day of school - 12:30 dismissal time". The Molly Ockett 2026-27 handbook: "Students will be released at 12:30 p.m. one Wednesday per month and on the last day of school in June as per our district calendar." The New Suncook newsletter also lists "November 18th - Early Release - Dismissal @ 12:30". Raw copies: raw/daily/msad72/msad72-cal-2026-27-p1.png; msad72-cal-2026-27.txt; mos-handbook-2026-27.txt
5. MSAD 72's handbooks say early-release days give teachers "an extended amount of time to meet" for staff development; in 2025-26 students were released at 12:30 p.m. every Wednesday, and in March 2026 the superintendent told the board there would be "only one early-release Wednesday per month" in 2026-27 "to provide more instructional time for students."
   - citation: Molly Ockett School handbook 2026-2027 and New Suncook handbook 2025-2026, "Professional Development"; MSAD 72 2025-2026 School Calendar; MSAD 72 Board minutes, March 11, 2026
   - source: https://drive.google.com/file/d/17XNiKbjsDLSz-bvh8YwZi8DhcjuMlEC6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: New Suncook 2025-26: "Staff development is an ongoing school improvement process which provides a structure for M.S.A.D. #72 educators to meet. While these activities happen throughout the week, one structure we will be using is early release days on Wednesday afternoons to allow educators an extended amount of time to meet. Students will be released at 12:30 p.m. every Wednesday starting September 3rd, 2025". The 2025-26 calendar (https://drive.google.com/file/d/1_xcFg6qCndpeqVbais5EqhkBo-NMRmJq/view) marks nearly every Wednesday as "Early Release". Board minutes (March 11, 2026): "There will be only one early-release Wednesday per month to provide more instructional time for students." The board approved the 2026-27 calendar on May 6, 2026. Raw copies: raw/daily/msad72/new-suncook-handbook-2025-26.txt; mos-handbook-2026-27.txt; msad72-cal-2025-26-p1.png; msad72-board-minutes-2026-03-11.txt; msad72-board-minutes-2026-05-06.txt
6. In May 2022, MSAD 72's board discussed "the multiple early-release days on Wednesdays and concerns raised on the impact on families" while drafting the 2022-23 calendar, without deciding the number.
   - citation: MSAD 72 Board minutes, May 4, 2022 ("2022-2023 School Calendar")
   - source: https://drive.google.com/file/d/18wRnFymDGFt6LfQMkQi84ldY1z6RBs4L/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Page text: "There was discussion regarding the multiple early-release days on Wednesdays and concerns raised on the impact on families. No final determination was made on the number of early-release days." Raw copy: raw/daily/msad72/msad72-board-minutes-2022-05-04.txt
7. MSAD 72 offers an after-school program, Pequawket Kids Afterschool (PKA), for kindergarten through 4th-grade students attending MSAD 72 schools: it meets at Molly Ockett School Monday through Friday from 2:30 to 5:30 p.m. with snack, homework help and enrichment, and New Suncook and Brownfield-Denmark students are bused to Molly Ockett for it.
   - citation: PKA website (pka.msad72.org), "PKA Information" and "Daily Schedule"; MSAD 72 District Annual Report, August 2026
   - source: http://pka.msad72.org
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Page text: "Our program is available for all children in the MSAD 72 School District who are attending kindergarten through fourth grade. PKA is located at the Molly Ockett School in Fryeburg. Students from New Suncook and Brownfield-Denmark Schools will be transported by bus to the Molly Ockett School at the end of the school day. PKA runs five sessions through the school year, Monday through Friday from 2:30 to 5:30 p.m." Daily schedule: "2:45 - 3:00 Snack Time / 3:00 - 4:00 Homework Help / 4:00 - 5:00 Enrichment Activities / 5:00 - 5:30 Free Choice Games / 5:30 Parent Pick-up". The page's session dates are from 2023-24 ("Session #5 will start on May 1st 2024"). The page does not say whether tuition students from Chatham may enroll. The August 2026 annual report lists "after-school support through partnership with the Pequawket Kids Association (PKA)". Raw copies: raw/daily/msad72/pka-home.txt; raw/daily/msad72/msad72-annual-report-2026-08.txt
8. PKA's posted fees are $110 per session for part time (up to two days a week) and $225 per session for full time (three to five days a week), for sessions of about two months; a limited number of scholarships are available each session, a late pick-up after 5:30 p.m. costs $20 per 15 minutes, and a registered child may attend for an emergency single afternoon for $10.
   - citation: PKA "Frequently asked questions"
   - source: https://docs.google.com/document/d/1wIUHAlkAwA5M9ldbZdIehpFthlPiV1mgEdpCbUxqIOw
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: FAQ text: "PKA has two options for attendance, PART TIME (up to two days a week) and FULL TIME (three to five days a week) for the two month PKA session. Part time for one session is $110 ... Full time is $225 for one session." "A limited number of scholarships are available each session." "PKA charges a late pick up fee of $20 if you arrive after the 5:30 program end time. This $20 fee applies to the first 1 to 15 minutes you are late and an additional $20.00 fee is charged for every 15 minute interval thereafter." "your child may attend PKA for an individual afternoon for a fee of $10.00". The FAQ is undated and linked from a PKA page last updated for 2023-24, so current fees were not confirmed. Raw copy: raw/daily/msad72/pka-faq.txt
9. PKA runs extended hours from 12:30 to 5:30 p.m. on early-release days for children registered for Wednesdays, and there is no PKA when school is closed, cancelled or dismissed early because of bad weather.
   - citation: PKA "Frequently asked questions" and "Pequawket Kids After School Program" family guide
   - source: https://docs.google.com/document/d/1wIUHAlkAwA5M9ldbZdIehpFthlPiV1mgEdpCbUxqIOw
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: FAQ text: "When school is closed, canceled or dismissed early due to inclement weather, there will be no PKA." and "PKA will have extended program hours (12:30 to 5:30)on early release days, but your child must be registered Wednesdays to attend." Family guide (https://docs.google.com/document/d/1lNzLnC-U1Zm2SvstBcNbYYJyIOkhCXiL1vRY-AKqQxk): "CANCELLATION When school is closed, or dismissed early due to inclement weather, there will be no PKA." Neither says what happens on a delayed-opening day. Raw copies: raw/daily/msad72/pka-faq.txt; raw/daily/msad72/pka-guide.txt
10. New Suncook's 2025-26 handbook says "Lovell Recreation provides activities for students on Wednesday afternoons but sign up is required," a note written for the year when every Wednesday was an early release.
   - citation: New Suncook Elementary School Student-Parent Handbook 2025-2026, "Professional Development"
   - source: https://docs.google.com/document/d/1W9R9H63HFFTwfqMDGczc_quwqIrZIQCY2s2VyFAEubM/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: The 2026-27 Molly Ockett handbook's "Professional Development" section does not repeat the Lovell Recreation sentence. Whether Lovell Recreation still runs Wednesday activities in 2026-27, and whether Chatham children may join, was not checked. Raw copy: raw/daily/msad72/new-suncook-handbook-2025-26.txt
11. MSAD 72's August 2026 annual report lists the supports the district provides for families: free meals for students, a "Backpack Program" giving food to families, support for families without housing, the "GO" play-based program, telehealth mental-health care, dental care through "Mainely Teeth," and after-school support through PKA.
   - citation: MSAD 72 District Annual Report, August 2026, p. 2
   - source: https://drive.google.com/file/d/1UBFD1ENFSNmyebt6a3SvkCdo98VjK0MV/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Report text: "we were able to provide: free meals for students, food for families through the "Backpack Program," support for "unhoused" families through McKinney Vento funding, self-regulation and play-based opportunities through the "GO" program, mental-health support through telehealth services, dental support for families through a collaboration with "Mainely Teeth," after-school support through partnership with the Pequawket Kids Association (PKA)". Raw copy: raw/daily/msad72/msad72-annual-report-2026-08.txt
12. Molly Ockett School's sports practices run 2:45 to 4:45 p.m. Monday through Friday except on monthly early-release Wednesdays, and students who stay to watch an after-school game need a note by 8:00 a.m. and must leave by 4:45 p.m. unless a parent stays.
   - citation: MSAD 72 Athletics page; MSAD 72, "Change of Dismissal Plans?"
   - source: https://www.msad72.org/information/athletics
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Athletics page: "Practices will be from 2:45-4:45 on Mondays-Fridays, except for early release Wednesdays one day each month". Dismissal notice: "when there are after school sporting events and your child wishes to stay and watch, a note must be presented by 8:00 AM of that day and students will need to leave the game by 4:45 or have their parent come to stay with them until they leave." Middle school sports listed: soccer, field hockey, football and cross country (fall); basketball, unified basketball and Nordic skiing (winter); softball, baseball, track and field and ultimate frisbee (spring). Raw copies: raw/daily/msad72/msad72-information_athletics.txt; msad72-change-of-dismissal.txt
13. MSAD 72's 2026-27 calendar starts students on September 2, 2026 and has these breaks: Fryeburg Fair Day (October 9), Thanksgiving (November 25–27), winter break (December 23–January 3, classes resume January 4), February vacation (February 15–19) and April vacation (April 19–23); it builds in five snow make-up days (June 15, 16, 17, 21 and 22), and the last day is June 22 if all five are used.
   - citation: MSAD 72 2026-2027 School Calendar (FINAL 5/6/2026)
   - source: https://drive.google.com/file/d/1CPwY4ANIxMG0QPb60q537KspUYxJ_0gB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Calendar list: "Sept 2 First Day of School for Students"; "Sep 4 No School"; "Oct 9 Fryeburg Fair Day"; "Nov 25 Start of Thanksgiving Break"; "Dec 23-Jan 3 Winter Break"; "Jan 4 Classes Resume"; "Feb 15-19 February Vacation"; "Mar 12 Teacher Workshop"; "Apr 19-23 April Vacation"; "June 18 Juneteenth Holiday Observed"; "Jun 22 Last Day of School if 5 Snow Days are Used". June grid: "S1 S2 S3" on June 15–17 and "S4 S5" on June 21–22. **Derived:** with no snow days used, the last day would be Monday, June 14, 2027, the school day before S1. Raw copies: raw/daily/msad72/msad72-cal-2026-27-p1.png; msad72-cal-2026-27.txt
14. Fryeburg Academy's 2026-27 calendar starts classes on September 1 (August 31 for 9th graders and new students) and has no classes for Fryeburg Fair Day (October 9), Thanksgiving recess (after November 24 to November 30), the winter break (December 18 to January 4, second semester begins January 5), winter recess (after February 10 to February 22) and spring recess (after April 14 to April 26); commencement is May 21 and the last day is June 4, and no snow make-up days are listed.
   - citation: Fryeburg Academy School Calendar 2026-27 (updated 9/1/26)
   - source: https://resources.finalsite.net/images/v1788271260/fryeburgacademyorg/dwq0tmlj6cfzqn5p1ztq/2026-27FRYEBURGACADEMYSCHOOLCALENDAR11.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Calendar text (linked as "2026-27 School Calendar (Printable)" on https://www.fryeburgacademy.org/calendar): "31 Mon Freshman & New Student Orientation - First day for all 9th & new 10th-12th"; "September 1 Tues First Day of Class for all Students"; "9 Fri Fryeburg Fair Day - No School"; "24 Tue Thanksgiving Recess begins - end of school day / 30 Mon Classes Resume"; "18 Fri End of First Semester - No Classes - academic makeup day - travel day"; "January ... 4 Mon Teacher Workshop Day - No School / 5 Tues Second Semester Begins"; "10 Wed Winter Recess begins - end of school day ... 22 Mon Classes Resume"; "14 Wed Spring Recess begins - end of school day ... 26 Mon Classes Resume"; "21 Fri Commencement 4:30pm"; "4 Fri End of May Term/Last Day of School". Raw copies: raw/daily/fa/fa-calendar-2026-27.txt; fa-calendar-2026-27-p1.png
15. **Derived comparison:** in 2026-27, Fryeburg Academy's winter, February and April breaks contain all of MSAD 72's matching days off plus eight weekdays when MSAD 72 is in session (December 18, 21 and 22, January 4, February 11–12 and April 15–16), and the Academy's year runs September 1 to June 4 while MSAD 72's runs September 2 to between June 14 and June 22.
   - citation: MSAD 72 2026-2027 School Calendar; Fryeburg Academy School Calendar 2026-27 (derived)
   - source: https://drive.google.com/file/d/1CPwY4ANIxMG0QPb60q537KspUYxJ_0gB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: **Derived** by comparing the two calendars (see chatham_calendar_days_off_2026_27_derived). Academy-only days: December 18 ("No Classes"), December 21–22, and January 4 (the Academy's "Teacher Workshop Day - No School"; MSAD 72 "Classes Resume"). Also February 11–12 (Academy winter recess begins after February 10) and April 15–16 (spring recess begins after April 14). Other Academy-only days in the year: November 6 (conferences, "no classes") and May 14 ("No Classes"). Shared days off include Fryeburg Fair Day (October 9), Columbus/Indigenous Peoples' Day (October 12), Veterans Day (November 11), Thanksgiving (November 25–27), MLK Day (January 18), March 12, and MSAD 72's February 15–19 and April 19–23 weeks. Both schools also share the nine early-release Wednesdays (12:30 at MSAD 72, 12:45 at the Academy). Raw copies: raw/daily/msad72/msad72-cal-2026-27-p1.png; raw/daily/fa/fa-calendar-2026-27.txt
16. MSAD 72's policy ICA says the board adopts the school calendar each year "after consultation with the P.V.E.A. and Fryeburg Academy (Liaison Committee)," and that days lost to cancellation are made up at the end of the school year; policy EBCE adds that storm days beyond those built into the calendar may be made up on weekends, by shortening vacations or by extending the year.
   - citation: MSAD 72 policy ICA, School Calendar (reviewed October 14, 2015); MSAD 72 policy EBCE
   - source: https://docs.google.com/document/d/16dFTh1YY8zPX2y2MTXGIVBMdbd8Gb_5sxmybVLIWehE/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: ICA text: "Days lost due to cancellation shall be made up at the end of the school year. 2. The school calendar shall be adopted by the Board of Directors each year after consultation with the P.V.E.A. and Fryeburg Academy (Liaison Committee.)" P.V.E.A. is the teachers' association named in MSAD 72 minutes as the "PVEA contract". EBCE: "Storm days lost in excess of the number provided for in the school year calendar may be made up by conducting classes on the weekend, rescheduling or shortening scheduled vacation periods or postponing the close of the school year, as determined by the Board." EBCE also allows one-hour extensions of the day, five of which count as one make-up day, with the Commissioner's approval. Raw copies: raw/daily/msad72/msad72-policy-ICA.txt; msad72-policy-EBCE.txt
17. MSAD 72 shares its calendar with MSAD 55 and MSAD 61 before adopting it because all three send students to the Lake Region Vocational Center, and those calendars are "required to match within a few days."
   - citation: MSAD 72 Board minutes, March 13, 2024 ("Draft 24/25 School Calendar") and March 11, 2026 ("Draft 26/27 School Calendar")
   - source: https://drive.google.com/file/d/1kw-fbzoUs7XSN0QH00Nr8-_zbMcA2ZH5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: March 13, 2024: "Jay explained that we have to coordinate with MSAD 61 and MSAD 55 in creating a school calendar because we all send students to the Lake Region Vocational Center. These calendars are required to match within a few days." March 11, 2026: "due to our District sending secondary students to the Lake Region Vocational Program, he needs to share the calendar with the Superintendents of MSAD 55 and 61 before finalizing it." Raw copies: raw/daily/msad72/msad72-board-minutes-2024-03-13.txt; msad72-board-minutes-2026-03-11.txt
18. MSAD 72 and Fryeburg Academy both close for "Fryeburg Fair Day," on Friday, October 9, in 2026-27; MSAD 72's 2025-26 calendar closed on Friday, October 3, 2025, for the same day.
   - citation: MSAD 72 2026-2027 and 2025-2026 School Calendars; Fryeburg Academy School Calendar 2026-27
   - source: https://drive.google.com/file/d/1CPwY4ANIxMG0QPb60q537KspUYxJ_0gB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: MSAD 72 2026-27: "Oct 9 Fryeburg Fair Day" (marked FF, school closed); 2025-26: "Oct 3 Fryeburg Fair Day"; Academy: "9 Fri Fryeburg Fair Day - No School". Only one fair day is a school holiday in each calendar; other fair days are school days. Raw copies: raw/daily/msad72/msad72-cal-2026-27.txt; msad72-cal-2025-26.txt; raw/daily/fa/fa-calendar-2026-27.txt
19. MSAD 72's attendance policy JE (adopted August 21, 2024) calls a student chronically absent after missing 10% or more of school days, excused or not, and sets a truancy process: the principal tells the superintendent within five school days, a student assistance team builds an intervention plan, and if that fails the superintendent sends the written notice required by Maine law.
   - citation: MSAD 72 policy JE, Student Attendance (Student Attendance, Chronic Absenteeism, and Truancy)
   - source: https://docs.google.com/document/d/1Z4I3T2Y2D7z4L6DznqsQ-PvU9HJ-G3rzfU10cW6bZVw/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Policy text: "An individual student is considered chronically absent if they have missed 10% or more school days in the current school year, including both excused and unexcused absences." Truancy procedure A–E, ending "If the intervention plan does not correct the student's truancy, the Superintendent shall follow the notice requirements outlined in 20-A MRSA § 5051-A (C) through (F)." JE says it "replaces Policies: JEAA ... and; JHB", though JEAA and JHB are still posted. The policy does not mention students who live outside the district. Raw copy: raw/daily/msad72/msad72-policy-JE.txt
20. MSAD 72's policy JEA lists six excusable absences: personal health (physical, mental and behavioral), a health appointment that must be during the school day, a required religious observance, a family emergency, "a planned absence for a personal or educational purpose that has been approved," and education disruption from events such as homelessness or an unplanned hospitalization.
   - citation: MSAD 72 policy JEA, Compulsory Attendance (amended January 11, 2023), "Excusable Absences"
   - source: https://docs.google.com/document/d/1ivZonjVbdsQ2S8cEWFmjM2ql6odiBXPXFsk_VRzSDHM/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Policy text items 1–6 as in the statement; item 5: "A planned absence for a personal or educational purpose that has been approved". The list follows 20-A MRSA §5001-A(4). Fair attendance and farm work are not named. Raw copy: raw/daily/msad72/msad72-policy-JEA.txt
21. Molly Ockett School's 2026-27 handbook says families should "align their vacations with the scheduled school vacations" and that "Additional vacations are considered unexcused absences," that a planned absence must be "pre-approved by the school," and that a child is marked unexcused if the family does not call or email the reason.
   - citation: Molly Ockett School Student-Parent Handbook 2026-2027, "Attendance Requirements"
   - source: https://docs.google.com/document/d/1ucywQEBp7sGDvuLR7IITnxJjyR891s69idRfpQhjU7o/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Handbook text: "A planned absence for a personal or an educational purpose that has been pre-approved by the school"; "Please call or email us to let us know your child will not be attending and the reason for the absence, or the child will be marked unexcused."; "Extended Vacations: We encourage families to align their vacations with the scheduled school vacations. (A copy of the School Calendar is included in this handbook.) Additional vacations are considered unexcused absences." It also says students must attend school on a game or practice day to take part. Raw copy: raw/daily/msad72/mos-handbook-2026-27.txt
22. SAU 9's New Hampshire calendar for 2026-27, which Chatham's board receives for information but which governs SAU 9's own schools rather than the Maine schools Chatham children attend, has February vacation on February 15–19 (the same week as MSAD 72), April vacation on April 26–30 (one week after MSAD 72's), a holiday break of December 24–January 1, a last student day of June 18, and three make-up days on June 22–24.
   - citation: SAU 9 2026-27 School Calendar (amended, approved by the SAU 9 Board July 9, 2026), attached to the Chatham School Board agenda, September 8, 2026 (item 4-e)
   - source: https://drive.google.com/file/d/1NqWAn2DTw0So0IZYy_OaWGgYWFhQ1H2c/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Calendar text: "February 15 President's Day (X)"; "February 16-19 February Vacation (X)"; "April 26-30 April Vacation (X)"; "Dec. 24 - Jan. 1 Holiday Break"; "June 18 Last Day of School for Students (ER)"; "June 22-24 Make-Up Days (MU)"; "September 3 First Day of School for Students". Board report: "FYI - Amended 2026-27 School Calendar ... adopted by the SAU #9 School Board on July 9, 2026." Raw copies: raw/daily/chatham-board/chatham-ag-2026-09-08.txt (pages 5–6); chatham-ag-2026-09-08-p6-sau9-calendar.png

## district-meals: School Meals

- kind: local
- question_type: local_practice
- description: School meals: what is served, prices, free and reduced-price applications, meal charges, summer meals, food service providers and local food

1. In 2025-26, MSAD 72 served breakfast and lunch at no charge to all students at Brownfield-Denmark, New Suncook and Molly Ockett schools under the federal Provision II or Community Eligibility Provision (CEP), which lets a school serve every enrolled student free without household applications.
   - citation: MSAD 72, "News Release for MSAD 72 School Year 2025-2026" (Food Services page)
   - source: https://drive.google.com/file/d/1AaswNSfCvTdAy63upxKZkrazZajzKZAU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Release text: "MSAD 72 has one or more schools that participate in Special Provision II or Community Eligible Provision ... All students enrolled in schools listed below may participate in the School Breakfast Program and the National School Lunch Program at no charge. Household free/reduced meal applications are not to be distributed or received" and "All students will be served breakfast and lunch at no charge at Brownfield-Denmark School, New Suncook Schools, and Molly Ockett Schools." The release covers "All students enrolled," with no exception for students from outside the district. A 2026-27 release was not posted. Raw copies: raw/daily/msad72/msad72-meals-news-release-2025-26.txt; msad72-departments_food-services.txt
2. Molly Ockett School's 2026-27 handbook says "This year, all students can eat school breakfast and lunch for free," while milk alone costs 60 cents and students need money in their account for other purchases; MSAD 72 says breakfast and lunch "will never be denied to a student."
   - citation: Molly Ockett School Student-Parent Handbook 2026-2027, school meals section
   - source: https://docs.google.com/document/d/1ucywQEBp7sGDvuLR7IITnxJjyR891s69idRfpQhjU7o/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine MSAD 72
   - note: Handbook text: "This year, all students can eat school breakfast and lunch for free. We encourage parents to add a small amount of money to their students' accounts ... Students will not be allowed to make purchases without money in their accounts. Breakfast and Lunch will never be denied to a student. If your student takes milk only, it is .60 cents." The New Suncook 2025-26 handbook has the same "all students can eat school breakfast and lunch for free" sentence. Raw copies: raw/daily/msad72/mos-handbook-2026-27.txt; new-suncook-handbook-2025-26.txt
3. In September 2022 the Chatham School Board was told that Maine was paying for breakfast and lunch for all Maine students but that "Chatham students are not eligible as they are from New Hampshire"; the board planned to urge Chatham families to file free and reduced-price meal applications and asked SAU 9 to estimate the cost of providing meals to all Chatham students.
   - citation: Chatham School Board minutes, September 6, 2022 (IV)
   - source: https://drive.google.com/file/d/1FFLfpEyC_gRAROs4kMCioCLS-0bQFJrj/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "Sue Perry had called about Free and Reduced Lunch for Chatham students. The State of Maine is paying for lunch and breakfast for all Maine students. Chatham students are not eligible as they are from New Hampshire. The School Board will send out a letter to all Chatham families to encourage them to fill out the Free and Reduced Lunch application. ... The SAU #9 office will estimate the cost of providing lunch and breakfast for all students." The minutes do not name the source of the eligibility ruling. Raw copy: raw/daily/chatham-board/chatham-min-2022-09-06.txt
4. In September 2023 the SAU 9 superintendent reported that Chatham would pay for Chatham students at Fryeburg Academy to receive the same free meals as Maine students, and that MSAD 72's superintendent had said Chatham students would also be provided free breakfast and lunch.
   - citation: Chatham School Board minutes, September 12, 2023 (IV)
   - source: https://drive.google.com/file/d/1YpoS-dlI4T93lqQO8hasMYeJUjnmqztM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Page text: "Superintendent Richard spoke to Head of Fryeburg Academy Joe Manning and stated that Chatham would cover the cost of the Chatham students to receive the same benefit as the Maine students. Superintendent Richard also spoke to MSAD 72 Superintendent Jay Robinson who stated that Chatham students would be provided free breakfast and lunch as well." Raw copy: raw/daily/chatham-board/chatham-min-2023-09-12.txt
5. Since 2023-24, Fryeburg Academy has billed the Chatham School District for Chatham students' meals through its tuition bills so that the meals cost Chatham families nothing, and in November 2024 the Chatham board decided to keep funding meals for Chatham students at the Academy.
   - citation: Chatham School Board minutes, September 3, 2024 (5.c) and November 5, 2024 (5)
   - source: https://drive.google.com/file/d/1yrh_q6tNqK4r-4qMl1T7NtgJdIKAcVW4/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: September 3, 2024: "Board members directed Pam to contact Fryeburg Academy to: i. Confirm lunches will continue to be provided for all Chatham students at no cost to the students nor their families. The board would like Fryeburg Academy to bill the Chatham School District for meals as was done for the 2023-2024 school year in the tuition bills." November 5, 2024 (draft): "Chatham Student lunches the board will continue funding meals for Chatham students enrolled at Fryeburg Academy". No later minutes read (through October 2026) change this; the meal cost is not shown as its own budget line. November source: https://drive.google.com/file/d/1l4hkHDaFqkYS9cWRPGMGpAh-jV4HU7B6/view. Raw copies: raw/daily/chatham-board/chatham-min-2024-09-03.txt; chatham-min-2024-11-05.txt
6. Fryeburg Academy's students eat in the LaCasce Dining Room, which has 19 meal sittings a week, and students pay for food items with money loaded onto their Academy ID cards through mykidsspending.com, using self-checkout scanners at each food station.
   - citation: Fryeburg Academy, Dining page
   - source: https://www.fryeburgacademy.org/student-life/dining
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: maine Fryeburg Academy
   - note: Page text: "With 19 meal sittings each week, LaCasce is more than a dining hall"; "The dining hall has introduced self-checkout scanners at the end of each food station ... Students can manage their money accounts online at mykidsspending.com to add funds to their FA ID cards." The page also says "Nearly 23% of our food products are purchased from local sources." It does not say which meals are free for day students. Raw copy: raw/daily/fa/fa-student-life_dining.txt

## maine-school-rules: Maine School Laws for Students Tuitioned From New Hampshire

- kind: rule
- question_type: rules
- description: Maine laws that apply in Maine schools attended by students tuitioned from New Hampshire: compulsory attendance, excused absences and truancy, and school meals

1. Maine law requires "persons in the State" who are 6 or older and under 17 to attend a public day school while it is in session, and a 5-year-old who is enrolled in a public school and has not withdrawn must also attend.
   - citation: 20-A MRSA §5001-A(1), (1-A)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5001-A.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Statute text: "Attendance at school shall be required of persons in the State as follows. 1. Requirement. Persons 6 years of age or older and under 17 years of age shall attend a public day school during the time it is in regular session. 1-A. ... A person 5 years of age or older and under 6 years of age who is enrolled in and who has not withdrawn from a public day school is required to attend that school during the time it is in session." The statute does not address students who live in another state. New Hampshire's own attendance law for Chatham residents is in the library topic compulsory-attendance. Data extracted 10/05/2026. Raw copy: raw/daily/law/20-A-5001-A.txt
2. Under Maine law an absence is excused for personal health (physical, mental and behavioral), a health appointment that must be during the school day, a required religious observance, a family emergency, "a planned absence for a personal or educational purpose that has been approved," or education disruption from events such as homelessness, an unplanned hospitalization or a foster care placement.
   - citation: 20-A MRSA §5001-A(4)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5001-A.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Statute text: "4. Excusable absence. A person's absence is excused when the absence is for the following reasons: A. Personal health ... B. An appointment with a health professional that must be made during the regular school day; C. Observance of a recognized religious holiday ...; D. A family emergency; E. A planned absence for a personal or educational purpose that has been approved; or F. Education disruption resulting from homelessness, unplanned psychiatric hospitalization, unplanned hospitalization for a medical emergency, foster care placement, youth development center placement or some other out-of-district placement". Weather, road closures, fairs and farm work are not named. Raw copy: raw/daily/law/20-A-5001-A.txt
3. Under Maine law a student who has completed grade 6 is truant after the equivalent of 10 full days or 7 days in a row of unexcused absences in a school year, and a younger student (age 6 and up, or age 5 and enrolled) is truant after the equivalent of 7 full days or 5 days in a row.
   - citation: 20-A MRSA §5051-A(1)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5051-A.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Statute text: "B. Has completed grade 6 and has the equivalent of 10 full days of unexcused absences or 7 consecutive school days of unexcused absences during a school year; C. Is at least 6 years of age and has not completed grade 6 and has the equivalent of 7 full days of unexcused absences or 5 consecutive school days of unexcused absences during a school year; or D. Is enrolled in a public day school, is at least 5 years of age and has not completed grade 6 and has the equivalent of 7 full days ... or 5 consecutive school days". Raw copy: raw/daily/law/20-A-5051-A.txt
4. When a Maine student is truant, the principal must tell the superintendent within 5 school days, the student is referred for an intervention plan, and if the plan does not work the superintendent must give the parent a written notice that failing to keep the child in school is a civil violation under 20-A MRSA §5053-A and that law enforcement and, for younger children, the Department of Health and Human Services may be notified.
   - citation: 20-A MRSA §5051-A(2)(A-1), (A-2), (C)
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec5051-A.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Statute text: "The principal, upon determining that a student is truant ... shall notify the superintendent of the student's truancy within 5 school days of the last unexcused absence." and "(3) Explain that the failure to send the student to school and maintain the student in regular attendance is a civil violation in accordance with section 5053‑A ... (4) State that the superintendent may notify the local law enforcement department of a violation of section 5053‑A and the Department of Health and Human Services of a violation under subsection 1, paragraph C". No source read says how a Maine civil violation is enforced against a parent living in New Hampshire. Raw copy: raw/daily/law/20-A-5051-A.txt
5. Section 3272 of Maine's education law, sometimes cited for truancy, is in the chapter for Maine's unorganized territory; it uses the same truancy thresholds and a similar excused-absence list as sections 5001-A and 5051-A, which are the sections that apply to school units such as MSAD 72.
   - citation: 20-A MRSA §§3271–3272 (Chapter 119, Unorganized Territory, Subchapter 2-A); 20-A MRSA §§5001-A, 5051-A
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec3272.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: §3271(1): "Persons residing in the unorganized territory who are at least 6 years of age and under 17 years of age shall attend". The page header reads "Chapter 119: UNORGANIZED TERRITORY / Subchapter 2-A: COMPULSORY SCHOOL ATTENDANCE". §3272(3) lists five excused reasons (A–E, without "education disruption"). MSAD 72's policies JE and JEA cite §§5001-A and 5051-A. Raw copies: raw/daily/law/20-A-3271.txt; raw/daily/law/20-A-3272.txt
6. Maine law requires a public school, or a private school approved for tuition purposes that enrolls at least 60% publicly funded students and takes part in the National School Lunch Program, to give a "publicly funded student" breakfast and lunch at no cost even if the student does not qualify for free or reduced-price meals, with the State paying the difference; the sections read do not define "publicly funded student."
   - citation: 20-A MRSA §6602(1)(H), (I); §6602-A
   - source: https://legislature.maine.gov/statutes/20-A/title20-Asec6602.html
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: §6602(1)(I): "A public school or a private school approved for tuition purposes that enrolls at least 60% publicly funded students as determined by the previous year's October and April average enrollment and participates in the National School Lunch Program ... that serves lunch shall provide a publicly funded student who is ineligible for free or reduced-price meals ... a meal that meets the requirements of the federal National School Lunch Program ... at no cost to the publicly funded student. The State shall provide ... funding equal to the difference between the federal reimbursement for a free lunch and the federal reimbursement for a full-price lunch". Paragraph H is the same for breakfast. "Publicly funded student" is not defined in §§6601, 6602 or 6602-A, or in the parts of §1 searched. Whether a student tuitioned by a New Hampshire district counts was not settled by any source found (see Not retrieved). Raw copies: raw/daily/law/20-A-6602.txt; raw/daily/law/20-A-6602-A.txt

## town-streets-and-safe-routes: Roads and Winter Travel

- kind: local
- question_type: local_practice
- description: Sidewalks, crosswalks, Safe Routes to School and road maintenance near schools

1. The White Mountain National Forest's road status page lists "Rte 113 (Evans Notch Rd, Maine)" with the note "Not maintained for winter travel, Snowmobile trail system"; on November 13, 2026 the page showed the road as "Open," with that status last updated May 1, 2026.
   - citation: White Mountain National Forest, Forest Roads Status (page last updated November 13, 2026)
   - source: https://www.fs.usda.gov/r09/whitemountain/alerts/forest-roads-status
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Chatham
   - note: Page row: "Rte 113 (Evans Notch Rd, Maine) / Open / 05/01/2026 / Andro / Not maintained for winter travel, Snowmobile trail system." The page says "Seasonal road closures are common on the White Mountain National Forest ... Some roads are closed because they are not passable due to snow, snow drifts and ice". The page does not say where the winter closure points are. The road is in Maine, north of Chatham (fact 2). Raw copy: raw/daily/roads/wmnf-forest-roads-status.txt
2. MaineDOT describes the stretch of Route 113 through the White Mountain National Forest as lying in Stow, Batchelders Grant Township and Gilead, Maine, so the Evans Notch section is north of Chatham, New Hampshire, rather than in it.
   - citation: MaineDOT, "UPDATE - Route 113 Daytime Closures Lifted" (September 2025)
   - source: https://www.maine.gov/dot/index.php/news/update-route-113-daytime-closures-lifted
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Chatham
   - note: Page text: "The Maine Department of Transportation initially scheduled daytime closures of Route 113 through the White Mountain National Forest ... All traffic restrictions along Route 113 in the towns of Stow, Batchelders Grant Township, and Gilead were lifted on Saturday, September 20." The earlier notice (https://www.maine.gov/dot/news/route-113-daytime-closures) puts that project "just south of the Spruce Hill Trail parking area ... south to the Brickett Place." Raw copies: raw/daily/roads/mdot-update-route-113-daytime-closures-lifted.txt; mdot-route-113-daytime-closures.txt
3. **Derived:** on OpenStreetMap, Route 113 in Chatham is named Main Road, and the fastest drive from North Chatham to Fryeburg runs south on Main Road, then Stow Road through Stow, Maine, then North Fryeburg Road and East Conway Road into Fryeburg village; OpenStreetMap has no road named "Evans Notch Road" in Chatham.
   - citation: OSRM public router on OpenStreetMap data; OpenStreetMap Nominatim search (derived)
   - source: https://router.project-osrm.org/route/v1/driving/-71.0166395,44.2408977;-70.9734466,44.0186045?overview=false&steps=true
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Chatham
   - note: **Derived** from OSRM step names: "Main Road | ME 113" (4,578 m), "Stow Road | ME 113" (8,024 m), "North Fryeburg Road | ME 113", "East Conway Road | ME 113", "River Street | ME 113", "Main Street | US 302; ME 113". A Nominatim search for "Evans Notch Road, Chatham, New Hampshire" returned no result, while "Main Road, Chatham" returned three road segments, including one in North Chatham. Absence from OpenStreetMap does not prove no local road uses the name. Raw copies: raw/daily/routing/osrm-chatham-routes.json; raw/daily/routing/nominatim-1.json; nominatim-2.json

## district-special-education-services: Special Education Services

- kind: local
- question_type: local_practice
- description: Who provides special education and related services in a district (on staff or contracted), reading specialists, 504 practice, IEP moves between schools, and out-of-district placements

1. SAU 9's special education procedures manual, which covers the Chatham School District, says extended school year (ESY) services are special education and related services provided beyond the normal school year under the child's IEP "at no cost to the parents," that the IEP team decides whether a child needs them, and that they are not limited to the summer.
   - citation: SAU 9 School District Special Education Procedures Manual (2026), "Extended School Year Services (ESY) (Ed 1110)," p. 32
   - source: https://files.smartsites.parentsquare.com/10271/sau_9_special_education_procedures_manual_2026.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Manual text: "Extended school year services are special education and related services provided to a child with a disability beyond the normal school year and in accordance with the child's IEP, and at no cost to the parents of the child. ... The child's IEP team shall determine the child's need for extended school year services. The District shall not limit extended school year services to particular categories of disability or unilaterally limit the type, amount or duration of those services." The cover lists "Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location, Jackson". The manual's ESY section does not mention transportation. Raw copy: raw/daily/sau9/sau9-sped-procedures-manual-2026.txt (copied from town/Conway/raw/community/sau9/)
2. Chatham's budget has a contracted ESY special education account, which spent $5,435 in 2023-24 and $511 in 2024-25, and at its June 30, 2026 meeting the Chatham board discussed "summer programming and how many students attend extended school year programs."
   - citation: Chatham School District Special Education Expenses/Revenue 2023-2024, 2024-2025 (2026 annual report, p. 12); Chatham School Board minutes, June 30, 2026 (4.a)
   - source: https://drive.google.com/file/d/1CCu3jbXNgbiQsMzmr2-GCK7Gcu8xb8X8/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Chatham
   - note: Annual report (scan, OCR): "1200.330.135 ESY, Special Education $5,435 [2023-24] ... $511 [2024-25]". The 2026-27 budget lists "31-10-1200-5330-0135 CONTR SERV, ESY SPEC EDUC". June 30, 2026 minutes: "There was discussion about summer programming and how many students attend extended school year programs." No source says where ESY is provided for Chatham students or how they get there; special education transportation is a separate account (district-transportation 13). Raw copies: raw/daily/chatham-board/chatham-ar2026.ocr.txt (page 12); chatham-min-2026-06-30.txt

## chatham_drive_distance_to_schools_derived: Driving Distance and Time From Chatham to Its Students' Schools (derived)

- unit: number (miles; minutes)
- period: Road network as of November 13, 2026; year: 2027
- source: OSRM public router (router.project-osrm.org) on OpenStreetMap data; places geocoded with OpenStreetMap Nominatim
- as_of: 2026-11-13
- raw: raw/daily/routing/ (nominatim-1.json, osrm-chatham-routes.json)
- note: **Derived**. Method: Nominatim (queried as `nhfacts-research`, contact webmaster@nhfacts.com) gave North Chatham (OSM place node, 44.2408977, -71.0166395), the Chatham Town House at 1071 Main Road, used for the middle of town (44.1642393, -71.0109837), and South Chatham (OSM place node, 44.0994605, -71.0074411). It also gave Molly Ockett School, 25 Molly Ockett Drive, Fryeburg (44.0214326, -70.9671495), New Suncook School, 95 Main Street, Lovell (44.1211395, -70.9027202) and Fryeburg Academy, 745 Main Street, Fryeburg (44.0186045, -70.9734466). OSRM's "driving" profile gave the fastest route. Times are for a car at typical speeds with no stops, traffic or weather. A school bus making stops takes longer, and Chatham's actual bus routes and times are not published (district-transportation 5). Routes from all three points run through Maine on Route 113 (Stow Road, North Fryeburg Road). Routes to Lovell turn east on Harbor Road and Shave Hill Road. Place is Chatham (town id 91 / district id 91).

| Place | Trip | Miles | Minutes | Note |
|---|---|---|---|---|
| Chatham | North Chatham to Molly Ockett School (Fryeburg) | 17.2 | 34.8 | OSRM 27,652 m, 2,086 s; via ME 113, Fish Street, Lovell Road, US 302 |
| Chatham | North Chatham to New Suncook School (Lovell) | 13.4 | 25.1 | OSRM 21,580 m, 1,508 s; via ME 113, Harbor Road, Shave Hill Road |
| Chatham | North Chatham to Fryeburg Academy | 18.3 | 34.5 | OSRM 29,388 m, 2,071 s; via ME 113, US 302 |
| Chatham | Chatham Town House (1071 Main Road) to Molly Ockett School | 12.7 | 26.9 | OSRM 20,375 m, 1,615 s; via NH 113B, ME 113 |
| Chatham | Chatham Town House to New Suncook School | 8.9 | 17.3 | OSRM 14,303 m, 1,038 s |
| Chatham | Chatham Town House to Fryeburg Academy | 13.7 | 26.7 | OSRM 22,111 m, 1,600 s |
| Chatham | South Chatham to Molly Ockett School | 8.8 | 18.3 | OSRM 14,224 m, 1,098 s; via Green Hill Road, ME 113 |
| Chatham | South Chatham to New Suncook School | 7.8 | 15.1 | OSRM 12,632 m, 907 s; via Green Hill Road, South Chatham Road, Harbor Road |
| Chatham | South Chatham to Fryeburg Academy | 8.4 | 17.5 | OSRM 13,463 m, 1,052 s |

## chatham_calendar_days_off_2026_27_derived: Weekdays Without School for Students During Each 2026-27 Break (derived)

- unit: count
- period: 2026-27 school year; year: 2027
- source: MSAD 72 2026-2027 School Calendar (https://drive.google.com/file/d/1CPwY4ANIxMG0QPb60q537KspUYxJ_0gB/view); Fryeburg Academy School Calendar 2026-27 (https://resources.finalsite.net/images/v1788271260/fryeburgacademyorg/dwq0tmlj6cfzqn5p1ztq/2026-27FRYEBURGACADEMYSCHOOLCALENDAR11.pdf); SAU 9 2026-27 School Calendar, amended July 9, 2026 (Chatham School Board agenda, September 8, 2026)
- as_of: 2026-11-13
- raw: raw/daily/msad72/msad72-cal-2026-27-p1.png; raw/daily/fa/fa-calendar-2026-27.txt; raw/daily/chatham-board/chatham-ag-2026-09-08-p6-sau9-calendar.png
- note: **Derived**: weekdays (Monday–Friday) with no school for students, counted from each calendar, including holidays inside the break. Fryeburg Academy breaks run from the day after "recess begins - end of school day" to the day before "Classes Resume". Its winter count includes December 18 ("No Classes") and January 4 ("Teacher Workshop Day - No School"). SAU 9's calendar governs SAU 9's New Hampshire schools, not the Maine schools Chatham students attend; it is shown for comparison only (question P20.2). Snow make-up days are those the calendar sets aside; the Academy's calendar lists none.

| Place | Break | Value | Note |
|---|---|---|---|
| MSAD 72 (Maine) | Thanksgiving | 3 | Nov 25–27 |
| Fryeburg Academy (Maine) | Thanksgiving | 3 | Nov 25–27 (recess begins end of day Nov 24) |
| SAU 9 (NH, for comparison) | Thanksgiving | 3 | Nov 25–27 |
| MSAD 72 (Maine) | Winter break | 8 | Dec 23–Jan 1; classes resume Jan 4 |
| Fryeburg Academy (Maine) | Winter break | 12 | Dec 18–Jan 4; second semester begins Jan 5 |
| SAU 9 (NH, for comparison) | Winter break | 7 | Dec 24–Jan 1 |
| MSAD 72 (Maine) | February vacation | 5 | Feb 15–19 (Feb 15 holiday) |
| Fryeburg Academy (Maine) | February vacation | 7 | Feb 11–12 and 15–19 |
| SAU 9 (NH, for comparison) | February vacation | 5 | Feb 15 (Presidents' Day) and 16–19 |
| MSAD 72 (Maine) | April vacation | 5 | Apr 19–23 |
| Fryeburg Academy (Maine) | April vacation | 7 | Apr 15–16 and 19–23 |
| SAU 9 (NH, for comparison) | April vacation | 5 | Apr 26–30 |
| MSAD 72 (Maine) | Snow make-up days set aside | 5 | June 15, 16, 17, 21, 22 |
| Fryeburg Academy (Maine) | Snow make-up days set aside | 0 | None listed; last day June 4 |
| SAU 9 (NH, for comparison) | Snow make-up days set aside | 3 | June 22–24 |
| MSAD 72 (Maine) | Early-release days | 10 | Nine Wednesdays at 12:30 plus the last day |
| Fryeburg Academy (Maine) | Early-release days | 9 | Same nine Wednesdays, at 12:45 |

## For another file

- **Money and governance (agent 4), transportation figures:**
  - Chatham's line 2720 (source: 2026 annual report p. 6, raw/daily/chatham-board/chatham-ar2026-p6.png; 2025-26 summary in the September 8, 2026 agenda, raw/daily/chatham-board/chatham-ag-2026-09-08.txt p. 4). Contracted service / special education / fuel / total: 2024-25 adopted $64,400 / $10,000 / $10,415 / $84,815; 2024-25 actual $60,570 / $7,773 / $8,956 / $77,298; 2025-26 adopted $66,203 / $7,480 / $10,415 / $84,098, with 2025-26 actual total $79,894 ("Transportation-Contr Serv/SpecEduc"); 2026-27 $68,189 / $7,200 / $10,415 / $85,804.
  - October 8, 2026 status: contracted service $7,219.20 spent and $55,948.80 encumbered; special education $4,576 spent and $32,864 encumbered, (420.00)% remaining; fuel $904.93 spent and $9,095.07 encumbered; line total (28.90)% remaining.
  - Bennett contract: awarded June 1, 2022; ends June 30, 2027; a three-year renewal is being drafted (minutes December 9, 2025, June 30, 2026, October 13, 2026).
  - February 10, 2025 minutes: "WEX invoice was discussed. Michael Wade will explore other options." The minutes do not say what the invoice was for.
- **Money and governance (agent 4), meals and meetings:**
  - Meals for Chatham students at Fryeburg Academy are billed to Chatham through tuition bills (September 3 and November 5, 2024 minutes).
  - **Premise P2.3 (board at 9:00 a.m. in Conway):** at its April 7, 2026 reorganization the board set meetings for "the first Tuesday every other month at 9:30am in the SAU9 conference room". The September 8, October 13 and December 8, 2026 meetings were set at 9:30 a.m. in the Kennett High School conference room. The June meeting is held in the evening with MSAD 72 and Fryeburg Academy. The sau9.org/chatham page and chathamnh.org/school-board still say 9:00 a.m. (raw/daily/chatham-board/chatham-min-2026-04-07.txt, chatham-min-2026-09-08.txt).
  - Enrollment budgeted for 2026-27: "15 high school students and one placeholder. There are 26 students slated for elementary" (January 20, 2026). The 2026 annual report counts 26 K–8 and 14 at Fryeburg Academy.
  - Chatham/Stow residency dispute over a house on the state line (2022–2025 minutes).
- **MSAD 72 schools (agent 1):**
  - April 1, 2025 enrollment by town and school (district-transportation 6).
  - Grade spans conflict: the 2026 Chatham annual report lists New Suncook as K–5, but MSAD 72's New Suncook page says K–4. Molly Ockett has a K–5 principal and a 6–8 principal (2026-27 handbook), and MSAD 72's annual report has a "MOS K-5" section.
  - The MSAD 72 board's ad hoc committee on the future of Brownfield Denmark Elementary School ran a survey open "until November 16" (msad72.org home page).
  - Pre-K for ages 3–5 is becoming a district duty in Maine by July 1, 2028 (MSAD 72 August 2026 annual report).
  - The 2026-27 Molly Ockett handbook is at https://docs.google.com/document/d/1ucywQEBp7sGDvuLR7IITnxJjyR891s69idRfpQhjU7o/edit (raw/daily/msad72/mos-handbook-2026-27.txt).
- **Fryeburg Academy (agent 3):**
  - Chatham residents enrolling at the Academy must "obtain a letter from the Chatham or Albany town office confirming your residency" (https://www.fryeburgacademy.org/admissions/how-to-apply/day-students).
  - The Academy's Quick Facts page now says 712 students and 223 boarding students; the Jackson file's 2026-27 profile says 704 and 220.
  - June 2025 minutes: the Academy had 689 students, 14 from Chatham.
  - MSAD 72 sends secondary students to the Lake Region Vocational Program (MSAD 72 minutes, March 11, 2026; March 13, 2024), which bears on P7.1.
  - MWV Ski & Study winter term tuition is $17,750.
  - Summer Term runs July 6–24, 2027, costs $4,300 for domestic students, and offers scholarships "to members of the local community".
- **Community and families (agent 5):**
  - PKA and Lovell Recreation's Wednesday activities are covered here (district-school-day-and-calendar 7–10).
  - The Academy has a partnership with Pleasant Mountain for "discounted seasonal passes and ski rentals" (Snow Sports page), which bears on P11.2.
  - chathamnh.org posts town annual reports only through 2015, and its site search for "bus," "school," "plow," "winter" and "113" found nothing about roads.
- **Jackson file:**
  - town/Jackson/getting-to-school-and-the-school-day.md, district-transportation 45 in `Jackson/getting-to-school-and-the-school-day.md`: the Jackson–Fryeburg Academy agreement makes Jackson responsible for daily transport. This is consistent with Chatham, which runs its own contracted transport to the Academy and to MSAD 72.
  - The Jackson file's SAU 9 vacation dates for 2027 (February 15–19, April 26–30) match the amended SAU 9 calendar used here.

## Not retrieved

- Chatham bus routes and stop times (Bennett Transportation): not on https://www.sau9.org/transportation. The Chatham Drive folders (agendas and minutes 2019–2026, annual reports, policies; folder ids in raw/daily/chatham-board/folder-*.html) were also checked. The April 4, 2023 minutes refer to a list held by SAU 9 that is not posted. So no ride times from North Chatham can be given.
- The Bennett Transportation contract itself: not in the Chatham Drive folders. SAU 9's Tuition Agreement Overview page (additional-data/raw/districts/batch-1/sau9-tuitions.txt) lists no Chatham contracts. It is not known whether Bennett's runs also carry Chatham's Fryeburg Academy students, or whether Bennett follows MSAD 72's or the Academy's closing and delay decisions.
- MSAD 72 delayed-opening schedule (for example, a two-hour delay): not found. Searched were policy EBCE, the Molly Ockett 2026-27 and New Suncook 2025-26 handbooks, the transportation page and the PKA pages.
- Fryeburg Academy student or family handbook (attendance rules, transportation, late or activity buses, storm closings): not linked on https://www.fryeburgacademy.org/parents. A web search found no copy.
- Maine DOE guidance on whether students tuitioned by a New Hampshire district are "publicly funded students" under 20-A MRSA §6602:
  - The Child Nutrition laws page (https://www.maine.gov/doe/schools/nutrition/laws) was checked.
  - The "Key Terms and Definitions" (8.20.2026), "Overview of School Nutrition Programs" (8.18.2026) and two "Additional Requirements" PDFs were checked.
  - A linked "What Application and Accountability system can I use" PDF on apps.web.maine.gov returned 404.
  - Whether Fryeburg Academy meets the law's 60% publicly funded threshold was also not found.
- Official location of the Route 113 winter gates at Evans Notch: the Forest Service road status page gives none. Only forum posts (vftt.org) describe gate locations, so they were not used.
- NHDOT winter maintenance of Route 113 and 113B within Chatham, and any record of storm closures of Route 113 between Chatham and Fryeburg: not checked or not found.
- Town of Chatham road agent or plowing policy: chathamnh.org has no roads page. Its site search for "plow," "winter" and "113" returned nothing.
- MSAD 72 summer school: no mention on msad72.org pages read, in the August 2026 annual report, or in board minutes from March 2024 to August 2026 (searched for "summer," "ESY" and "extended school").
- ESY transportation for Chatham students: no source describes where ESY is held or how Chatham students travel to it.
- Current PKA sessions and fees for 2026-27: the PKA site (http://pka.msad72.org) still shows 2023-24 session dates, and the FAQ is undated. PKA's eligibility for tuition students from Chatham is not stated.
- New Suncook 2026-27 handbook: not posted. The 2025-26 handbook was used for New Suncook's hours.
- Whether Lovell Recreation still runs Wednesday activities in 2026-27: not checked.
- MSAD 72 2026-27 meals news release: the Food Services page still links the 2025-26 release.
- Bennett Transportation company details: found only on third-party carrier-listing sites (bubba.ai, carrieratlas.com), which were not used.
