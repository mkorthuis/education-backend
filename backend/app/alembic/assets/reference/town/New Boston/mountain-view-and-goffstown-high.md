# Mountain View and Goffstown High From New Boston

Part of the New Boston research (town/New Boston). Gathered November 21, 2026.

## Summary

This file covers New Boston's students in grades 7–12 at Mountain View Middle School and Goffstown High School (GHS), which they attend under the AREA agreement with Goffstown: their buses (scheduled ride times on every 2026-27 New Boston route sheet, the transfers at New Boston Central School, the late bus, bus tracking), getting to GHS without the bus, technology and trade classes, New Boston's share of the Manchester School of Technology (MST), fees, counseling and mental health support at GHS, and what the schools say about graduates' readiness for work. Goffstown's own research (`town/Goffstown/`) already covers GHS's courses, AP, Early College, MST, outcomes, counselors and fees in depth; this file cites those facts and adds New Boston's side and what they lack.

- **7 fact topics, 33 facts and 1 number table.** Places: `district New Boston` 13 (its buses, late bus, tracking, carpools, MST costs), `district Goffstown` 17 (Mountain View and GHS classes, clubs, counseling, rules, the GHS parking lot), `sau 19` 2 (the K-12 counseling program and the Portrait of a Graduate), `town New Boston` 1 (the regional community mental health center).
- **Raw copies** are in `raw/high/` (about 14 MB): the SAU 19 Bus Routes page and its file list; a times-only CSV derived from New Boston's three 2026-27 route sheets (`routes/nb-derived-bus-route-times-2026-27.csv`; the route PDFs list stops by house number and were not saved); OCR text and page images of the Transfers sheet and the New Boston late bus sheet (intersections only); the SafeStop flyer text with its access code removed; New Boston School Board minutes of September 23 and October 14, 2026; New Boston's FY28 requested budget with notes (November 18, 2026); the Goffstown School Board's May 11, 2026 meeting PDF (with the K-12 counseling program); the GHS 2026-27 handbook and Program of Studies (class of 2030); Mountain View's 2026-27 handbook, home, clubs, music, sports and staff pages; three Paws News issues (text and the cited page as an image); the SAU 19 Academics and Portrait of a Graduate pages (with the image and its OCR); and the Mental Health Center of Greater Manchester's child and teen page.
- **New data concepts:** New Boston's two-round bus day (a high school run from 6:23 a.m., then a Central School and Mountain View run from 7:16 a.m.), the Central School transfer system and scheduled ride times by route (derived; table `new_boston_scheduled_bus_minutes_2026_27`); the New Boston late run's times, stops and cost; Mountain View's grade 7–8 "digital integration" and "technical education" classes, robotics and makerspace; GHS's full computer course list and the AP Computer Science Principles discussion; MST's state shortfall reaching New Boston's tuition; GHS's counseling services for anxiety and crises.
- **Premises checked:**

| Question | Premise | What the sources show |
|---|---|---|
| P2.1 | GHS may no longer offer "hands-on shop and vocational tracks" | Not supported. GHS teaches wood engineering, timber framing, architectural courses, welding, CAD and engineering, and runs five trade pathways that finish at MST in grades 11–12; Goffstown must give New Boston students the same access, including transport to MST. 60% of the class of 2026 planned four-year college and 13% two-year (Goffstown's file). |
| P2.2, P15.2 | The bus leaves "at 6:30 in the morning" for GHS | About right. The nine New Boston high school runs have first stops from 6:23 to 6:42 a.m.; the three direct buses reach GHS at 7:00–7:08 for an 8:00 start, and the other six riders change buses at Central School by 7:00. Mountain View riders are picked up from 7:16 to 7:52 and reach Mountain View at 8:20–8:23 (derived). |
| P2.3 | A "welding club in Goffstown" | No welding club appears in GHS's handbook list of clubs (a partial list); welding is taught in two half-credit art courses. |
| P2.3 | A late bus back to New Boston | Yes: one late run, scheduled to leave GHS at 5:30 p.m. and end at Central School at 5:47 p.m., with stops on New Boston Road and River Road; it is not door to door. |
| P14.2 | Wi-Fi on the buses | Not found in any page, route sheet, budget line or minutes read. |
| P14.2 | A bus tracking app | Yes: SafeStop, posted on SAU 19's Bus Routes page beside New Boston's sheets. |
| P19.1 | Waits of "three weeks" to talk to someone | No source reports wait times at GHS or at the regional mental health center. GHS counselors offer short-term individual counseling for anxiety and crisis response, and crisis lines run 24/7. |

- **Questions answered wholly by earlier files:** 0 of 10. P11.1 rests almost entirely on Goffstown's `mountain-view-high-school-and-mst.md` (AP, Early College, outcomes), with one new fact here on AP Computer Science Principles.
- **Main gaps:** what Mountain View's digital integration and technical education classes teach; when transfer buses G 14 and G 15 reach GHS; how New Boston Mountain View students reach the New Boston late run; any carpool network; the GHS sports participation fee, field trip costs and instrument rental arrangements; wait times for counseling or outside therapy; how many New Boston students attend MST.
- **No new shared topics proposed.**
- **Privacy:** route sheets were read for times and road names only; no house-number address was saved or sent anywhere. Board minutes name residents who spoke; no facts use their names. No personal information was sent to any outside service.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P2.1 Does GHS still offer hands-on shop and vocational tracks, or is everything geared to four-year college? | cte-center-programs 1; school-programs-after-grade-6 5–6; Goffstown `mountain-view-high-school-and-mst.md` school-programs-after-grade-6 14, 17–19, 22, cte-center-programs 1–9, high-school-outcomes 1; Goffstown `money-buildings-and-governance.md` district-tuition-contracts 5; library cte-centers-overview, registered-apprenticeship-basics | full | Premise not supported. Trade courses (wood, timber framing, welding, CAD, engineering and manufacturing) and five pathways ending in two-year MST programs; New Boston students get the same access and transport to MST under the AREA agreement, and MST's costs reach New Boston through its tuition. About 95 GHS students (Goffstown and New Boston) were in MST sessions in 2026-27; no count by town was found. |
| P2.2 How long is the morning bus ride from the far side of New Boston to Mountain View and GHS? | district-transportation 1–5; table new_boston_scheduled_bus_minutes_2026_27; Goffstown `getting-to-school-and-choices.md` district-school-day-and-calendar 1 | full | Scheduled, not measured (derived). High school: first stops 6:23–6:42; direct buses take 25–42 minutes from the first stop to GHS; transfer riders take 21–34 minutes to Central School, then ride G 14 or G 15, whose GHS arrival isn't posted. Mountain View: 55–67 minutes from a route's first stop (median 58), 28–41 from its last stop; the longest is the route starting on Greenfield Road at 7:16. A rider's own time depends on the stop. |
| P2.3 Is there a late bus back for sports or a welding club, or do I drive every day? | district-transportation 6–9; school-programs-after-grade-6 8; Goffstown `getting-to-school-and-choices.md` district-transportation 18–20; Goffstown `mountain-view-high-school-and-mst.md` district-pe-outdoor-and-athletics 7 | full | One late run to New Boston each school day (scheduled 5:30–5:47 p.m.; the handbook says 5 p.m.), stopping on New Boston Road and River Road and ending at Central School, so families on outlying roads still pick up there; New Boston budgets $26,314 for it in FY28. Athletes return from away games to GHS, not New Boston. No welding club is listed; welding is a course. How Mountain View riders reach the New Boston late run isn't stated. |
| P11.1 Does GHS offer enough AP and dual enrollment for competitive colleges? | school-programs-after-grade-6 7; Goffstown `mountain-view-high-school-and-mst.md` school-programs-after-grade-6 1–11, high-school-outcomes 1–7, tables goffstown_ghs_ap_courses_2026_27, goffstown_ghs_early_college_courses_2026_27, goffstown_ghs_postsecondary_plans_2022_2026; library dual-enrollment-rules, early-college-at-your-high-school; research-ap-and-dual-enrollment in `sau9/kennett-and-sau9.md`; site data: graduates' plans, SAT results | full | 20 AP, 38 honors and 15 Early College courses in 2026-27; 89% of 2026 AP scores were 3 or higher; Class of 2026 acceptances include Harvard, Tufts and other selective colleges (no admission rates). AP Computer Science Principles was under discussion in fall 2026. "Enough" is a judgment the data can't make. |
| P14.1 What tech or coding classes do kids get at Mountain View? | school-programs-after-grade-6 1–5; Concord `high-school-and-pathways.md` high-school-offerings-and-seals-rules 1–2 | partial | Every grade 7–8 student takes "digital integration" and "technical education" as unified arts; Mountain View has a robotics team (a FIRST Tech Challenge award in January 2026), a video production club and a library makerspace used for coding. **No page describes what the two classes teach or how long they run.** At GHS, computer courses range from block-coding game design to Python, web design and network courses. State rules require a computer science program in each school. |
| P14.2 Do the buses have Wi-Fi or a tracking app? | district-transportation 10–11 | full | Tracking: yes, SafeStop (real-time map, alerts near a stop). Wi-Fi: not found in any source read. |
| P15.2 Is there a carpool network for New Boston parents going to GHS? | district-transportation 7, 12–13; Goffstown `mountain-view-high-school-and-mst.md` district-fees 5, school-programs-after-grade-6 19; Rindge `conant-from-rindge.md` school-transportation-rules 1 | partial | No carpool network or ride-matching was found. The late bus sheet puts GHS 7.46 miles from Central School. Licensed students may buy a $125 parking permit (seniors first), and GHS's lot was being expanded in fall 2026. New Hampshire limits young drivers' passengers in their first six months. The Manchester Transit Authority's New Boston shuttle couldn't be read (see Not retrieved). |
| P15.3 What do field trips, sports fees and band rentals cost over a year? | district-fees 1–2; Goffstown `mountain-view-high-school-and-mst.md` district-fees 1–5, district-pe-outdoor-and-athletics 6; Bedford `high-school-and-pathways.md` ap-and-ib-exam-fees-and-deadlines 2–3 | partial | Known: GHS parking $125; AP exams $99 each (free for students with financial need in NH); the district budget pays team bus trips. **Not found:** the GHS sports participation fee amount, Mountain View sports costs, field trip costs and instrument rental arrangements. Teacher-led vacation trips are not school-sponsored. |
| P16.2 Are GHS graduates ready to show up on time and work? | district-goals-and-performance-reporting 1; district-school-day-and-calendar 1; district-student-support 4; Goffstown `mountain-view-high-school-and-mst.md` school-programs-after-grade-6 14, 19, 22, cte-center-programs 1, 7; Madison `kennett-for-madison.md` research-workforce-readiness 1–2; site data: graduates' plans | partial | GHS teaches résumé writing, offers a senior School to Career Internship, records career readiness on transcripts (policy IKFG, 2026) and adds a Career Pathway Diploma from the class of 2030; its attendance rules refer students to an administrator from the second unexcused tardy. Site data: 49 of 240 GHS graduates in 2025 reported going to work (derived share 20%). Whether graduates are "ready to work" is a judgment no public data measures. |
| P19.1 What mental health support does GHS have; can kids talk to someone without waiting three weeks? | district-student-support 1–3, 5–7; Goffstown `mountain-view-high-school-and-mst.md` district-student-support 1; Goffstown `getting-to-school-and-choices.md` district-student-support 3, 5–7; library community-mental-health-centers 2, 4; school-staffing-and-class-size 2 | partial | Five counselors who keep the same students all four years, a director, a school psychologist, one student assistance counselor and a 504 interventionist (about 168–201 students per counselor, derived from 1,005 students and 5 or 6 counselor positions, within the state's 300 maximum); short-term individual counseling for anxiety, suicide screening, crisis response and a re-entry team; Mobile Crisis and NH Rapid Response for emergencies. **No wait-time data** for GHS or outside therapists. |

## district-transportation: New Boston's Buses to Mountain View and Goffstown High: Ride Times, Transfers, the Late Bus and Tracking

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. SAU 19 posts New Boston's 2026-27 bus routes on its Bus Routes page: high school students are on the "NB HS AM" and "NB HS-MV PM" sheets, Central School and Mountain View students share the "NB ELEM-MV" morning sheet, Mountain View students "travel with the high school students in the PM," and a New Boston late bus sheet and a Transfers sheet are also posted; families find their stop by searching the PDF for their street.
   - citation: SAU 19, Bus Routes (2026-2027), and its file list
   - source: https://www.sau19.org/index.php/en/bus-routes
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Page text: "If your child resides in New Boston and is attending Goffstown High School , the route will be listed as a NB HS-AM or NB HS-MV PM . If your child is attending NBCS or MVMS the AM route will be listed as NB ELEM-MV . If your child attends NBCS , the PM route will be listed as NB ELEM PM"; "New Boston MVMS students travel with the high school students in the PM. their route is listed under NB HS-MV PM"; "Type your street name (or the closest cross street) to find stop options." File list: New Boston HS AM, Elem-MV AM, HS-MV PM and Elem PM posted August 28, 2026; New Boston Latebus September 10, 2026; Transfers August 18, 2026. Raw: raw/high/sau19/sau19-bus-routes.txt; raw/high/sau19/sau19-bus-routes-file-list.txt
2. New Boston's nine regular bus routes (NB 01 to NB 09) are run by Student Transportation of America (STA) from its Goffstown depot, and New Boston's FY28 requested budget prices them as nine STA buses at $498.13 a day for 180 days; under the AREA agreement, New Boston, not Goffstown, pays to transport its students to Mountain View and Goffstown High.
   - citation: New Boston 2026-27 route sheets (NB HS AM, NB Elem-MV AM); New Boston School District FY28 General Fund Requested Budget with Notes (November 18, 2026), line 421, p. 19
   - source: https://www.sau19.org/index.php/files/1352/20261118/7331/FY28-NB-General-Fund-Proposed-with-Notes-2026-11-18
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Route sheets (read, not saved, because they list stops by house number): most routes begin at "GTC - Goffstown Truck Center / STA / 62 E. UNION ST", the contractor's depot. Budget note: "STA (9 BUSES X $498.13 PER DAY X 180 DAYS) $ 806,971". The AREA terms are in Goffstown's money-buildings-and-governance.md, district-tuition-contracts 5 ("Transportation of students from the sending district, to and from the AREA schools, shall be the responsibility of the sending district at their sole expense"). Budget figures are requested, before any vote. Raw: raw/high/routes/nb-derived-bus-route-times-2026-27.csv; raw/high/nb/nb-fy28-general-fund-requested-with-notes-2026-11-18.txt and -p19.png
3. Each New Boston bus makes a high school run first: on the 2026-27 sheets, first stops are scheduled from 6:23 to 6:42 a.m.; three buses (NB 02, NB 03 and NB 04) go straight to Goffstown High, arriving at 7:00, 7:05 and 7:08 a.m. for an 8:00 start; the other six end at New Boston Central School between 6:55 and 7:00 a.m., where high school students change to Goffstown buses G 14 (from NB 1, 6 and 8) or G 15 (from NB 5, 7 and 9), which the Transfers sheet says depart Central School "by 7:00am" (**derived**).
   - citation: SAU 19, New Boston HS AM route sheet and Transfers sheet, 2026-27
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=574&id=7050
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: **Derived** by reading all nine pages of the NB HS AM sheet (first and last stop before the sheet's "GHS - Goffstown High School" or "NBCS - New Boston Elementary School" line; the sheets weren't saved, the times are in the CSV). Transfers sheet (https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=574&id=7009), transcribed from image: "*NB AM GHS* (Departs NBCS by 7:00am) Transfer Bus (G14): NB1, NB6, NB8 Transfer Bus (G15): NB5, NB7, NB9 NB2, NB3 & NB4 drops off their own students". GHS hours (8:00 a.m.–2:45 p.m.) are in Goffstown's getting-to-school-and-choices.md, district-school-day-and-calendar 1. Scheduled times, not measured. See table new_boston_scheduled_bus_minutes_2026_27. Raw: raw/high/routes/nb-derived-bus-route-times-2026-27.csv; raw/high/routes/sau19-transfers-sheet-2026-27-ocr.txt and .png
4. On New Boston's 2026-27 morning high school runs, the scheduled time from a route's first stop to Goffstown High is 25, 42 and 26 minutes on the three direct buses, and 21 to 34 minutes from the first stop to Central School on the six transfer routes, plus the ride on G 14 or G 15, whose arrival at Goffstown High is not on any posted sheet (Goffstown's own morning sheet starts G 15's next route at the high school at 7:24 a.m.) (**derived**).
   - citation: SAU 19, New Boston HS AM route sheet and Transfers sheet, 2026-27; Goffstown ELEM-MV-GL AM route sheet
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=574&id=7050
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: **Derived** from first-stop and arrival times: NB 02 6:35→7:00, NB 03 6:23→7:05, NB 04 6:42→7:08; to Central School NB 01 6:31→6:56, NB 05 6:23→6:56, NB 06 6:26→7:00, NB 07 6:34→6:55, NB 08 6:30→7:00, NB 09 6:29→6:58. Riders boarding later on a route ride less. The G 15 time is from Goffstown's getting-to-school-and-choices.md, district-transportation 4 (note). The longest direct route (NB 03) runs along Bog Brook, Bedford and Chestnut Hill Roads. See table new_boston_scheduled_bus_minutes_2026_27. Raw: raw/high/routes/nb-derived-bus-route-times-2026-27.csv
5. After the high school run, the same nine buses carry Central School and Mountain View students: first stops are scheduled from 7:16 to 7:27 a.m., every bus reaches Central School at 7:50–7:55, and Mountain View students change there to NB 1 (from NB 5 and 9), NB 2 (from NB 3, NB 7 and walkers) or NB 8 (from NB 4 and 6), which depart "by 8:00am" and reach Mountain View at 8:20–8:23 for its 8:25 start, so the scheduled time from a route's first stop to Mountain View is 55 to 67 minutes (median 58) and from its last stop 28 to 41 minutes (**derived**).
   - citation: SAU 19, New Boston Elem-MV AM route sheet and Transfers sheet, 2026-27; Mountain View Middle School home page (school hours)
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=574&id=7046
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: **Derived** from the NB Elem-MV AM sheet ("MVMS - Mountain View Middle School / 41 LAUREN LN" at 8:23 on NB 01 and NB 02 and 8:20 on NB 08) and the Transfers sheet ("*NB AM MVMS* (Departs NBCS by 8:00am) Transfer Bus (NB1): NB5, NB9 Transfer Bus (NB2): NB3, NB7, Walkers Transfer Bus (NB8): NB4, NB6"). Longest: NB 09, first stop on Greenfield Road at 7:16, Central School 7:50, Mountain View 8:23 on NB 1 (67 minutes). The sheets don't say which stops have Mountain View riders. Mountain View home page: "School Hours: 8:25 am - 3:18 pm". Scheduled, not measured. See table new_boston_scheduled_bus_minutes_2026_27. Raw: raw/high/routes/nb-derived-bus-route-times-2026-27.csv; raw/high/routes/sau19-transfers-sheet-2026-27-ocr.txt; raw/high/mvms/mvms-home.txt
6. On New Boston's 2026-27 afternoon sheet, buses are scheduled at Goffstown High at 3:10 p.m. (NB 2) and 3:20 p.m. (NB 5 and NB 7), after its 2:45 dismissal, and at Mountain View at 3:10 p.m. (NB 1, NB 3, NB 4) and 3:25 p.m. (NB 2); other riders change buses at Central School, and the last scheduled stops are between 4:00 and 4:33 p.m., 75 to 108 minutes after the high school's dismissal; the longest ride on one bus is NB 3's, 83 minutes from Mountain View to its last stop (**derived**).
   - citation: SAU 19, New Boston HS-MV PM route sheet and Transfers sheet, 2026-27
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=574&id=7051
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: **Derived.** Transfers sheet: "*NB PM GHS* Transfer Bus (NB5): NB4, NB6, NB8 Transfer Bus (NB7): NB1, NB3, NB9, Walkers ... NB2 picks up their own students *NB PM MVMS* Transfer Bus (NB1): NB7, Walkers Transfer Bus (NB3): NB6, NB8 Transfer Bus (NB4): NB5, NB9 NB2 picks up their own students". The sheet's 3:10 Mountain View pickup matches the dismissal printed in Mountain View's handbook ("Students are dismissed at 3:10 pm"), but the school's home page and the board's 2026-27 change put dismissal at 3:18 (Goffstown's getting-to-school-and-choices.md, district-school-day-and-calendar 2–3). Some transfer times don't line up on paper (NB 5 is due at Central School at 3:49, after routes it feeds are scheduled to leave at 3:30–3:40), so the sheets don't show how long buses wait. See table new_boston_scheduled_bus_minutes_2026_27. Raw: raw/high/routes/nb-derived-bus-route-times-2026-27.csv; raw/high/routes/sau19-transfers-sheet-2026-27-ocr.txt; raw/high/mvms/mvms-handbook-2026-27.txt
7. Goffstown High's 2026-27 handbook says a late bus runs daily at 5 p.m. with one late run to New Boston, stopping at major roads and intersections; New Boston's late bus sheet schedules it to leave Goffstown High at 5:30 p.m., stop on New Boston Road at Bell Road and at Hermsdorf Avenue (5:36), on River Road at Parker Road (5:39) and at Byam Road (5:42), and end at New Boston Central School at 5:47 p.m., Monday to Friday, a distance of 7.46 miles.
   - citation: Goffstown High School Student Handbook 2026-27, Late Bus (pp. 30–31); SAU 19, New Boston Latebus sheet (dated September 20, 2023; posted September 10, 2026)
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=574&id=7096
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Handbook: "A late bus runs daily at 5PM. The late run routes do not travel the same path as regular home to school routes. They were developed with the intent of having stops at major roads/intersections ... There is one late run to New Boston." Sheet, transcribed from image: "Bus Driver Directions For NB Late Bus Route: NB Start Time: 05:30 pm ... End Time: 05:47 pm ... Route Days: MTWHF Anchor: GOFFSTOWN HIGH SCHOOL Distance: 7.46 mi."; "5:36 pm (stop) NEW BOSTON RD @ BELL RD", "5:36 pm (stop) NEW BOSTON RD@HERMSDORF AVE", "5:39 pm (stop) RIVER RD @ PARKER RD", "5:42 pm (stop) RIVER RD @ BYAM RD", "5:47 pm END NEW BOSTON ELEMENTARY SCHOOL". The Bus Routes page: "Stop times for late buses are estimated; actual times are based on daily ridership." The handbook's 5 p.m. and the sheet's 5:30 differ; the sheet is dated 2023. Raw: raw/high/ghs/ghs-handbook-2026-27.txt; raw/high/routes/sau19-new-boston-latebus-sheet-ocr.txt and .png (the OCR drops "(stop)" on two lines; the image shows it); raw/high/sau19/sau19-bus-routes.txt
8. Mountain View's 2026-27 handbook says its late bus, open to all students in supervised after-school activities, leaves Mountain View at 5:00 p.m. with sign-up in the office by 1:00 p.m., but New Boston's late bus sheet starts at Goffstown High and lists no Mountain View stop, and no SAU 19 page or sheet read says how a New Boston Mountain View student reaches the New Boston late run.
   - citation: Mountain View Middle School Student Handbook 2026-27, The Late Bus (p. 30); SAU 19, New Boston Latebus sheet
   - source: https://www.sau19.org/attachments/article/62/MVMS%20Student%20Handbook%2026-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Handbook: "The Late Bus is available to all students who take part in supervised after school activities. Students needing to use the late bus must sign up in the office by 1:00 pm. The late bus departs MVMS at 5:00 pm." and "Please be advised that the Goffstown School District's late bus route will be posted on the district website." Goffstown's late bus sheet leaves Mountain View at 5:15 and stops at Goffstown High at 5:27 (Goffstown's getting-to-school-and-choices.md, district-transportation 20), three minutes before the New Boston run's scheduled 5:30 start, but no source says riders transfer there. Raw: raw/high/mvms/mvms-handbook-2026-27.txt; raw/high/routes/sau19-new-boston-latebus-sheet-ocr.txt
9. New Boston's FY28 requested school budget (November 18, 2026) carries one late bus at $146.19 a day for 180 days, $26,314, within its regular transportation line.
   - citation: New Boston School District FY28 General Fund Requested Budget with Notes, line 421, p. 19
   - source: https://www.sau19.org/index.php/files/1352/20261118/7331/FY28-NB-General-Fund-Proposed-with-Notes-2026-11-18
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Note text: "1 LATE BUS ($146.19 X 180 DAYS) $ 26,314", followed by "@INCREASE OF $1,253 TO NEW". The page's two prior-year columns are both headed "FY26 BUDGET" in the source. Requested figures, before the deliberative session and vote. Raw: raw/high/nb/nb-fy28-general-fund-requested-with-notes-2026-11-18.txt and -p19.png
10. SAU 19's Bus Routes page, which carries New Boston's route sheets, also posts a flyer for the SafeStop app, which shows "a real-time, map-based bus locator" while routes run and sends alerts when the bus enters a zone the parent draws around a stop; parents enter a school access code printed on the flyer and their child's student ID.
   - citation: SAU 19, SafeStop Phone App flyer (Bus Routes page, posted September 1, 2025)
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=574&id=5969
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Flyer text: "2. Enter the school access code provided below. 3. Enter your child's unique Student ID. 4. Select the (bus or route name based on school communications preference) you wish to track. 5. Create alert zones around drop-off and pick-up points. You're all set! You will be able to track the bus's movement during active route times and receive notifications when the bus enters your custom alert zone(s)." The flyer is one SAU-wide sheet; New Boston's buses are STA's (fact 2), the company whose app it is. The access code is not repeated here. Goffstown's equivalent fact is district-transportation 21 in its getting-to-school-and-choices.md. Raw: raw/high/routes/sau19-safestop-app-flyer.txt (code removed)
11. No SAU 19 page, New Boston route sheet, New Boston budget line or New Boston School Board minutes read (June to November 2026) mentions Wi-Fi on school buses; New Boston's budget prices its STA buses by the day without listing equipment.
   - citation: SAU 19, Bus Routes page and New Boston route sheets; New Boston FY28 General Fund Requested Budget with Notes; New Boston School Board minutes, June 17 to October 28, 2026
   - source: https://www.sau19.org/index.php/en/bus-routes
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Searched the saved texts for "wifi", "wi-fi", "hotspot" and "internet" with no bus-related result; Goffstown's raw copies (its minutes and budget, November 2026) also have none. This is an absence in the sources read, not a statement that no bus has Wi-Fi. Raw: raw/high/sau19/sau19-bus-routes.txt; raw/high/nb/nb-fy28-general-fund-requested-with-notes-2026-11-18.txt; raw/high/nb/nbsb-minutes-2026-09-23.txt; raw/high/nb/nbsb-minutes-2026-10-14.txt
12. At the New Boston School Board's October 14, 2026 meeting, the superintendent reported that the Goffstown High School parking-lot expansion was "well underway" and that the added parking was expected to become available to students "in the coming months."
   - citation: New Boston School Board minutes, October 14, 2026 (approved), Superintendent's Report
   - source: https://www.sau19.org/index.php/files/1331/20261014/7275/20261014NBSBMeetingMinsApproved
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Minutes text: "He reported that the Goffstown High School parking-lot expansion was well underway and that the contractor was making significant progress. The additional parking was expected to become available to students in the coming months." Permit rules and the $125 fee are in Goffstown's mountain-view-high-school-and-mst.md, district-fees 5. GHS's handbook says "Due to limited space, parking will be available first to seniors." Raw: raw/high/nb/nbsb-minutes-2026-10-14.txt; raw/high/ghs/ghs-handbook-2026-27.txt
13. No SAU 19, Goffstown High, Mountain View or New Boston School District page read describes a carpool network or ride-matching list for New Boston families; Goffstown High's handbook lets licensed students park with a registered permit, seniors first, and offers late arrival and early release as a privilege for students in good academic standing and passing all subjects.
   - citation: Goffstown High School Student Handbook 2026-27, Student Parking (p. 33) and Early Release/Late Arrival (p. 32)
   - source: https://www.sau19.org/attachments/article/945/GHS_Handbook_26-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Handbook: "Licensed students who wish to obtain a parking permit must register their vehicle or a parent's/legal guardian's vehicle with the school"; "Early release/late arrival is offered to encourage the productive use of out-of-school time ... Must be in good academic standing. Must be passing all subjects." Searched: the SAU 19 Bus Routes page, the GHS and Mountain View handbooks, New Boston School Board minutes (June to November 2026) and a web search for a New Boston carpool to GHS (no result). New Hampshire's limits on young drivers' passengers are in Rindge's conant-from-rindge.md, school-transportation-rules 1. Raw: raw/high/ghs/ghs-handbook-2026-27.txt

## new_boston_scheduled_bus_minutes_2026_27: New Boston's Scheduled Bus Rides to Goffstown High and Mountain View, 2026-27 (minutes, derived)

- unit: number (minutes)
- period: 2026-27 school year route sheets (posted August 28, 2026); year: 2027
- source: SAU 19 Bus Routes page, New Boston HS AM, Elem-MV AM and HS-MV PM sheets and the Transfers sheet — https://www.sau19.org/index.php/en/bus-routes
- as_of: 2026-11-21
- raw: raw/high/routes/nb-derived-bus-route-times-2026-27.csv; raw/high/routes/sau19-transfers-sheet-2026-27-ocr.txt
- topic: district-transportation
- place: district New Boston
- note: **Derived.** Morning: Value = minutes from the route's first scheduled stop to the scheduled arrival at Goffstown High, at Central School (for high school riders who change to G 14 or G 15, whose GHS arrival isn't posted) or at Mountain View (through the transfer bus named). Afternoon: minutes from the bus's first scheduled school stop to its last stop, on the same bus. A rider boarding later (morning) or getting off earlier (afternoon) rides less, and riders who change buses in the afternoon also wait at Central School. Times are scheduled, not measured. Roads are the main roads on each route; stops by house number were not kept.

| Place | Route | Trip | Value | First stop | Last stop | Arrives | Note |
|---|---|---|---|---|---|---|---|
| New Boston | NB 01 | High school, morning | 25 | 6:31 | 6:50 | Central School 6:56 | Changes to G 14 (leaves by 7:00); Francestown Rd, Bunker Hill Rd, Tucker Mill Rd |
| New Boston | NB 02 | High school, morning | 25 | 6:35 | 6:51 | GHS 7:00 | Direct; Parker Rd, Riverdale Rd, Styles Rd, Whipplewill Rd |
| New Boston | NB 03 | High school, morning | 42 | 6:23 | 6:56 | GHS 7:05 | Direct; Bog Brook Rd, Bedford Rd, Chestnut Hill Rd |
| New Boston | NB 04 | High school, morning | 26 | 6:42 | 6:54 | GHS 7:08 | Direct; Bedford Rd, Wilson Hill Rd, Byam Rd |
| New Boston | NB 05 | High school, morning | 33 | 6:23 | 6:51 | Central School 6:56 | Changes to G 15; Old Coach Rd, Clark Hill Rd |
| New Boston | NB 06 | High school, morning | 34 | 6:26 | 6:54 | Central School 7:00 | Changes to G 14; Beard Rd, Lull Rd, Weare Rd, Middle Branch Rd, Twin Bridge Rd |
| New Boston | NB 07 | High school, morning | 21 | 6:34 | 6:46 | Central School 6:55 | Changes to G 15; McCurdy Rd, Carriage Rd |
| New Boston | NB 08 | High school, morning | 30 | 6:30 | 6:56 | Central School 7:00 | Changes to G 14; Joe English Rd, Mont Vernon Rd, South Hill Rd |
| New Boston | NB 09 | High school, morning | 29 | 6:29 | 6:52 | Central School 6:58 | Changes to G 15; Cochran Hill Rd, Butterfield Mill Rd, Lyndeborough Rd, Hopkins Rd |
| New Boston | NB 01 | Mountain View, morning | 56 | 7:27 | 7:45 | Mountain View 8:23 | Stays on NB 1 (Central School 7:53); Meetinghouse Hill Rd, Bedford Rd, Wilson Hill Rd, Byam Rd |
| New Boston | NB 02 | Mountain View, morning | 60 | 7:23 | 7:51 | Mountain View 8:23 | Stays on NB 2 (Central School 7:55); Tucker Mill Rd, Bunker Hill Rd, Francestown Rd |
| New Boston | NB 03 | Mountain View, morning | 64 | 7:19 | 7:46 | Mountain View 8:23 | Changes to NB 2 at Central School (7:55); Bog Brook Rd, Christie Rd, Chestnut Hill Rd, Bedford Rd |
| New Boston | NB 04 | Mountain View, morning | 56 | 7:24 | 7:52 | Mountain View 8:20 | Changes to NB 8 (7:55); Parker Rd, Styles Rd, Whipplewill Rd, Beard Rd, Weare Rd |
| New Boston | NB 05 | Mountain View, morning | 58 | 7:25 | 7:50 | Mountain View 8:23 | Changes to NB 1 (7:55); Old Coach Rd, Clark Hill Rd |
| New Boston | NB 06 | Mountain View, morning | 57 | 7:23 | 7:51 | Mountain View 8:20 | Changes to NB 8 (7:55); Weare Rd, Middle Branch Rd, Twin Bridge Rd, Lull Rd, River Rd |
| New Boston | NB 07 | Mountain View, morning | 58 | 7:25 | 7:45 | Mountain View 8:23 | Changes to NB 2 (7:55); McCurdy Rd, Carriage Rd, Bog Brook Rd |
| New Boston | NB 08 | Mountain View, morning | 55 | 7:25 | 7:49 | Mountain View 8:20 | Stays on NB 8 (Central School 7:55); Joe English Rd, Mont Vernon Rd, South Hill Rd |
| New Boston | NB 09 | Mountain View, morning | 67 | 7:16 | 7:42 | Mountain View 8:23 | Changes to NB 1 (Central School 7:50); Greenfield Rd, Cochran Hill Rd, Butterfield Mill Rd, Lyndeborough Rd |
| New Boston | NB 01 | Afternoon, same bus | 54 | Mountain View 3:10 | 4:04 | | Central School 3:32; high school riders arrive on NB 7 |
| New Boston | NB 02 | Afternoon, same bus | 42 | GHS 3:10 | 3:52 | | Mountain View 3:25; no transfer |
| New Boston | NB 03 | Afternoon, same bus | 83 | Mountain View 3:10 | 4:33 | | Central School 3:44; high school riders arrive on NB 7 |
| New Boston | NB 04 | Afternoon, same bus | 50 | Mountain View 3:10 | 4:00 | | Central School 3:30; high school riders arrive on NB 5 |
| New Boston | NB 05 | Afternoon, same bus | 67 | GHS 3:20 | 4:27 | | Central School 3:49; Mountain View riders arrive on NB 4 |
| New Boston | NB 06 | Afternoon, from Central School | 39 | Central School 3:30 | 4:09 | | Riders arrive on NB 5 (high school) and NB 3 (Mountain View) |
| New Boston | NB 07 | Afternoon, same bus | 40 | GHS 3:20 | 4:00 | | Central School 3:33; Mountain View riders arrive on NB 1 |
| New Boston | NB 08 | Afternoon, from Central School | 50 | Central School 3:40 | 4:30 | | Riders arrive on NB 5 (high school) and NB 3 (Mountain View) |
| New Boston | NB 09 | Afternoon, from Central School | 40 | Central School 3:40 | 4:20 | | Riders arrive on NB 7 (high school) and NB 4 (Mountain View) |

## school-programs-after-grade-6: Technology, Robotics and Trade Classes at Mountain View and Goffstown High

- kind: local
- question_type: local_practice
- description: Middle and high school programs that a district's students attend: AP, honors, dual enrollment, early credit, transitions between schools, activities

1. Mountain View Middle School's 2026-27 handbook says every student in grades 7 and 8 takes unified arts classes in art, music, wellness, physical education, "digital integration" and "technical education," with band, chorus, orchestra and Spanish as electives, and the school's staff directory lists one Digital Integration teacher, one Technical Education teacher and a Technology Integrator.
   - citation: Mountain View Middle School Student Handbook 2026-27, Teams ~ Including Unified Arts and Electives (p. 12); Mountain View staff directory
   - source: https://www.sau19.org/attachments/article/62/MVMS%20Student%20Handbook%2026-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Handbook text: "All students are enrolled in unified arts classes as follows: Grade 5/6: music, art, physical education; Grades 7/8: art, music, wellness, physical education, digital integration, and technical education. Students may enroll in the following electives: Grades 5- 8: band, chorus, and orchestra; Grades 7/8: Spanish." Directory (https://www.sau19.org/index.php/en/contact-5) headings under Unified Arts include "Digital Integration" and "Technical Education", and under Technology "Technology Integrator"; read for job titles only. Raw: raw/high/mvms/mvms-handbook-2026-27.txt; raw/high/mvms/mvms-staff-directory.txt
2. No Mountain View or SAU 19 page read describes what Mountain View's digital integration or technical education classes teach (for example, whether they include coding or keyboarding) or how long each runs, and SAU 19's Academics page lists curriculum standards by subject with no computer science or technology education heading, citing International Society for Technology in Education standards under library media.
   - citation: SAU 19, Academics page; Mountain View Middle School Student Handbook 2026-27; Mountain View home, clubs and staff pages
   - source: https://www.sau19.org/index.php/en/information/curriculum-2/academics
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Academics page headings: Arts, English Language Arts, English for Speakers of Other Languages, Library Media ("International Society for Technology in Education ... ISTE Standards for Students"), Mathematics, Music, Physical Education/Health, Pre-K, School Counseling, Science, Social Studies, World Language. New Hampshire's school approval rules require a computer science program at each school (Concord's high-school-and-pathways.md, high-school-offerings-and-seals-rules 2). Mountain View's Transition Info page is a Canva video and was not read. Raw: raw/high/sau19/sau19-academics.txt; raw/high/mvms/mvms-handbook-2026-27.txt
3. Mountain View lists nine clubs whose times and advisors may change during the year (Drama, Chess, Robotics, Dungeons & Dragons, Student Government, Yearbook, Art, Video Production and Volenteens through Crispin's House), and its robotics team won the Sustain Award at the FIRST Tech Challenge Merrimack qualifier on January 24, 2026.
   - citation: Mountain View Middle School, MVMS Clubs page; Paws News, March 6, 2026, p. 2
   - source: https://www.sau19.org/index.php/en/information-3/students/mvms-clubs
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Clubs page: "The time frames and advisors may change throughout the year. If your student is interested in joining, please contact the MVMS main office for more information." Paws News (https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=1109&id=6781): "The MVMS robotics team won an award on January 24, 2026, at the FIRST Tech Challenge Merrimack qualifier ... they competed in five qualifying matches ... The team won the Sustain Award". Raw: raw/high/mvms/mvms-clubs.txt; raw/high/mvms/paws-news/paws-news-2026-03-06.txt and -p2.png
4. Mountain View's library has a makerspace where students "create, build, and design," which the school's newsletter said in October 2025 had seen "creating, designing, building, coding, and more," and the library offered coding and artificial intelligence activities for Computer Science Week in December 2025.
   - citation: Mountain View Middle School Student Handbook 2026-27, Information Center Services (p. 16); Paws News, October 17, 2025 and December 11, 2025
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=1109&id=6695
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Handbook: "There is also a Makerspace area that provides opportunities for students to create, build, and design." October 17, 2025 issue (https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=1109&id=6692): "There has already been a lot of creating, designing, building, coding, and more in our Makerspace!" December 11, 2025 issue: "Coding and Learn about AI acitvities for Computer Science Week!" (spelling as printed). These are library activities, not a class. Raw: raw/high/mvms/mvms-handbook-2026-27.txt; raw/high/mvms/paws-news/paws-news-2025-10-17.txt and -p22.png; raw/high/mvms/paws-news/paws-news-2025-12-11.txt and -p9.png
5. Goffstown High's 2026-27 computer courses are Intro to Computer Animation and Game Design (block coding, grades 9–12), Intro to Information Technology (grades 9–10), Early College Intro to Programming in VB.net and in Python, Early College Web Design I, Web Design II Honors (PHP and MySQL), Early College Intro to Computer Repair (toward CompTIA A+) and Early College Intro to Computer Networks (toward Network+), alongside Intro to CAD I, Early College Engineering and Manufacturing and Early College Introduction to Robotics (programming in C++); all count toward the digital literacy graduation requirement.
   - citation: Goffstown High School Program of Studies 2026-27, Class of 2030, Technology Education Course Offerings, pp. 53–55
   - source: https://www.sau19.org/index.php?option=com_dropfiles&format=&task=frontfile.download&catid=1092&id=6746
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Text: "Intro to Computer Animation & Game Design Grades 9-12 ... basic programming concepts through the use of 3D animations and interactive games ... block coding"; "EC Intro to Programming (Python) Grades 10-12 ... Prerequisite: Algebra I with a C or better ... help prepare students for the Python Institute's PCEP & PCAP"; "Web Design II Honors ... learning both PHP and MySQL"; "EC Introduction to Robotics Grades 10-12 ... programming in C++"; "All computer courses satisfy the Digital Literacy graduation requirement." Goffstown's mountain-view-high-school-and-mst.md (school-programs-after-grade-6 18) mentions the CompTIA and Python courses within career pathways; this lists the full set. Raw: raw/high/ghs/ghs-program-of-studies-2026-27-class-of-2030.txt
6. Goffstown High's 2026-27 handbook lists FIRST Robotics, Culinary Club, Environmental Club, Future Business Leaders of America and 11 other clubs in a "partial listing" that includes no welding club; welding is taught in Creative Welding I and Creative Welding II Honors, half-credit courses that count as art credit and require a score of at least 90% on a safety exam.
   - citation: Goffstown High School Student Handbook 2026-27, Clubs/Organizations & Activities (p. 9); Program of Studies 2026-27, Class of 2030, Welding Technology (p. 57)
   - source: https://www.sau19.org/attachments/article/945/GHS_Handbook_26-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Handbook: "The following is a partial listing of these clubs, organizations and activities: Art Club Culinary Club Environmental Club Equestrian Club FIRST Robotics Future Business Leaders of America (FBLA) Goffstown Performing Arts Junior Classical League Model Congress National Honor Society Paw Print (Student Newspaper) Peer Outreach Student Council Yearbook (Nisa 'Tin) Youth Forum". Program of Studies: "Creative Welding Grades 9-12 Course #1425 0.5 credit ... shielded metal arc welding, oxyacetylene techniques, plasma arc cutting"; "Students must score a minimum of 90% on the safety exam to participate in this course. These courses count as an Art credit." GHS's full clubs page is a Canva design that couldn't be read. Raw: raw/high/ghs/ghs-handbook-2026-27.txt; raw/high/ghs/ghs-program-of-studies-2026-27-class-of-2030.txt
7. In September 2026, Goffstown's Curriculum and Education Committee discussed adding AP Computer Science Principles to Goffstown High's technology education program and a high school pre-algebra course for students not yet ready for algebra, as a New Boston board member reported to the New Boston School Board; AP Computer Science is not among the 20 AP courses in GHS's 2026-27 school profile.
   - citation: New Boston School Board minutes, September 23, 2026 (approved), Goffstown Curriculum and Education Committee report
   - source: https://www.sau19.org/index.php/files/1321/20260923/7250/20260923NBSBMeetingMinsApproved
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Minutes text: "Goffstown Curriculum and Education Committee ... reported that the committee discussed: • A high-school pre-algebra course for students not yet prepared for the next algebra curriculum • AP Computer Science Principles in the high school's technology-education program". The minutes record a discussion, not an adopted course. The 2026-27 AP list is in Goffstown's mountain-view-high-school-and-mst.md, school-programs-after-grade-6 1 and table goffstown_ghs_ap_courses_2026_27. New Boston board members sit on Goffstown's committees under the AREA agreement (Goffstown's money-buildings-and-governance.md, district-sau-governance 11). Raw: raw/high/nb/nbsb-minutes-2026-09-23.txt
8. Goffstown High's 2026-27 handbook requires student athletes to use school transportation both ways whenever it is provided to practices and games and says athletes "will not be dropped off at any point short of the high school on return," so New Boston athletes return to Goffstown High unless the principal gives prior written permission for a parent to take the student at the site.
   - citation: Goffstown High School Student Handbook 2026-27, Athletic Related School Rules, Transportation (p. 5)
   - source: https://www.sau19.org/attachments/article/945/GHS_Handbook_26-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Handbook text: "Whenever transportation is required and provided to practice and/or game sites, school transportation must be used both ways. Student-athletes will not be dropped off at any point short of the high school on return from practice or a game. The only exception to this rule would be if after receiving prior written permission from the principal, a parent/legal guardian takes custody of a student athlete at the practice or away game site directly from the coach." Goffstown's mountain-view-high-school-and-mst.md, district-pe-outdoor-and-athletics 7, gives the same rule from the 2019 athletics handbook; this adds the 2026-27 handbook's return rule. Raw: raw/high/ghs/ghs-handbook-2026-27.txt

## cte-center-programs: New Boston Students at the Manchester School of Technology

- kind: local
- question_type: local_practice
- description: The programs at a regional career and technical center, which schools send students, credentials and college credit

1. At its September 23, 2026 meeting the New Boston School Board discussed the state's funding shortfall for Manchester School of Technology tuition, which the minutes say affects New Boston's tuition because New Boston shares Goffstown's secondary school costs proportionally, and the superintendent said Goffstown had raised its FY 2027 budget lines because the administration "did not want to cap student access" to career and technical education; New Boston's FY28 requested budget has no separate MST tuition or vocational transportation line.
   - citation: New Boston School Board minutes, September 23, 2026 (approved), Goffstown Administration and Finance Committee report; New Boston FY28 General Fund Requested Budget with Notes (November 18, 2026)
   - source: https://www.sau19.org/index.php/files/1321/20260923/7250/20260923NBSBMeetingMinsApproved
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district New Boston
   - note: Minutes text: "The Board also discussed the state funding shortfall for Manchester School of Technology tuition. Because New Boston shares Goffstown's secondary-school costs proportionally, Goffstown's shortfall affects New Boston tuition. Brian Balke stated that the district had increased the relevant FY 2027 budget lines because the administration did not want to cap student access to career and technical education programs." The budget was searched for "vocational", "MST", "CTE" and "Manchester" with no tuition or transport line (its only AREA lines are Mountain View and GHS tuition). Goffstown's MST budget ($481,000 tuition in FY27 and FY28; $38,645 transport) and the state's proration are in Goffstown's mountain-view-high-school-and-mst.md, cte-center-programs 4 and 9; the AREA agreement's promise of equal access and transport to vocational programs is Goffstown's money-buildings-and-governance.md, district-tuition-contracts 5. Raw: raw/high/nb/nbsb-minutes-2026-09-23.txt; raw/high/nb/nb-fy28-general-fund-requested-with-notes-2026-11-18.txt

## district-student-support: Counseling and Mental Health Support at Goffstown High

- kind: local
- question_type: local_practice
- description: Counseling, social work and mental health support, English learner services, homeless student support, welcoming families of all backgrounds, and enrollment documents

1. SAU 19's K-12 Comprehensive School Counseling Program, approved 9-0 by the Goffstown School Board on April 20, 2026 for two years, lists counselors' responsive services as group counseling, short-term individual "Tier 3" check-ins and counseling for executive functioning, anxiety and emotional support, suicide safety screening, crisis intervention and a re-entry team, referrals to tutoring and a 504 interventionist, and the GHS "Grizzly Den" overseen by that interventionist.
   - citation: Goffstown School Board minutes, April 20, 2026 (approved May 11, 2026; in the May 11, 2026 meeting PDF, pp. 4–9), K-12 Comprehensive School Counseling Program
   - source: https://www.sau19.org/index.php/files/1271/2026-05-11/6926/05-11-2026-Goffstown-Meeting-PDF
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: sau 19
   - note: Text: "Responsive Services: School counselors respond to a variety of student needs as they arise ... • Group counseling. • 504 case managers and IEP team member. • Referrals to 504 Interventionist, tutoring, academic support. • Tier 3, short term individual check-ins and counseling – executive functioning, anxiety, emotional support check in. • Suicide safety screening, crisis intervention, reentry team. ... • GHS Grizzly Den overseen by the 504 Interventionist." The program's vision covers "every student in the Goffstown and New Boston School Districts." Vote: "Vote: 9-0-0 – All in Favor – Motion Passed." The pages don't describe what the Grizzly Den is. Raw: raw/high/gsb/gsb-meeting-pdf-2026-05-11.txt
2. Goffstown High assigns its five school counselors by students' last names so each student keeps the same counselor for all four years, and has one Student Assistance Program counselor, at the high school only; presenting the counseling program to the school board in April 2026, the director of school counseling said that if she "could have 12 more counselors that would be wonderful."
   - citation: Goffstown School Board minutes, April 20, 2026 (approved May 11, 2026), questions on the counseling program
   - source: https://www.sau19.org/index.php/files/1271/2026-05-11/6926/05-11-2026-Goffstown-Meeting-PDF
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Minutes text: "inquired if there was a Student Assistance Program (SAP) counselor at both the middle school and high school, or just the high school? Response: We have one at the high school for student assistance program."; "We have 5 school counselors at the high school who are assigned to students as they fall into an alphabetic category ... These students have the same counselor through their 4 years."; "Ms. Mazzone replied, not at this time however, if she could have 12 more counselors that would be wonderful." GHS's counseling staff list (director, school psychologist, student assistance counselor, 504 case manager) and the FY28 count of 6 counselor positions are in Goffstown's mountain-view-high-school-and-mst.md, district-student-support 1. The state maximum is one counselor per 300 high school students (library school-staffing-and-class-size 2). Raw: raw/high/gsb/gsb-meeting-pdf-2026-05-11.txt
3. SAU 19's counseling program lists for Goffstown High Challenge Day, the Signs of Suicide "Connor's Climb" curriculum "throughout the year" in grades 9–12, support groups such as "Good Grief" and "Boys to Men," bi-weekly reviews of failure reports, and credit checks at least twice a year.
   - citation: K-12 Comprehensive School Counseling Program, in Goffstown School Board minutes of April 20, 2026 (May 11, 2026 meeting PDF)
   - source: https://www.sau19.org/index.php/files/1271/2026-05-11/6926/05-11-2026-Goffstown-Meeting-PDF
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Text: "Personal/Social: Challenge Day: Signs of Suicide: Connor's Climb Curriculum utilized in grades 9-12 throughout the year. Various Groups running each year. Examples include: 'Good Grief' and 'Boys to Men'."; "Graduation verification via credit checks, completed at minimum twice per year. • Bi-weekly review of failure reports and interventions." The suicide prevention plan, crisis team and Mobile Crisis number are in Goffstown's getting-to-school-and-choices.md, district-student-support 3, 5–7. Raw: raw/high/gsb/gsb-meeting-pdf-2026-05-11.txt
4. SAU 19's counseling program lists Goffstown High's career and college lessons by grade: a Naviance personality inventory ("Do What You Are") in grade 9, work with sophomore English teachers in grade 10, junior and senior future planning, and a career and college workshop, a résumé workshop and career and college field trips for seniors.
   - citation: K-12 Comprehensive School Counseling Program, in Goffstown School Board minutes of April 20, 2026 (May 11, 2026 meeting PDF)
   - source: https://www.sau19.org/index.php/files/1271/2026-05-11/6926/05-11-2026-Goffstown-Meeting-PDF
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Text: "Career and College: Grade level presentations in classrooms. Grade 9: Do What You Are: Naviance AchieveWorks, Personality Inventory. Grade 10: Collaboration with sophomore English teaches on Passon. Grade 11: Junior Future Planning. Grade 12: Senior Future Planning. Career and College Workshop, Resume Workshop. Career and College Field Trips." ("teaches on Passon" as printed.) Raw: raw/high/gsb/gsb-meeting-pdf-2026-05-11.txt
5. Goffstown High's 2026-27 handbook says the assessment and crisis procedures for students with safety concerns are in policy regulations JLDBB and JLDB-1 and an SAU 19 Suicide Prevention Manual written under RSA 193-J:2, and that home tutoring for an extended illness or accident is arranged through the school counseling coordinator at (603) 497-4841, with a health care provider's statement possibly required.
   - citation: Goffstown High School Student Handbook 2026-27, Safety Plan (p. 32) and Home Tutoring (p. 30)
   - source: https://www.sau19.org/attachments/article/945/GHS_Handbook_26-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Handbook: "Processes which address the assessment and crisis intervention procedures for students with safety concerns can be found in policy regulations JLDBB and JLDB-1, and the Suicide Prevention Manual. This manual is a resource for the mental health teams of SAU19 ... Individual school websites will be updated each year with the contact information for the building's suicide prevention liaisons."; "Home tutoring is designed to help students keep up with class work in the event of an extended illness or accident ... A health care provider's written statement verifying the student's inability to attend school may be required ... Please contact the School Counseling Coordinator at (603) 497-4841". Raw: raw/high/ghs/ghs-handbook-2026-27.txt
6. The Mental Health Center of Greater Manchester, the community mental health center New Hampshire assigns to New Boston and Goffstown, offers children and teens an evaluation followed by an individual treatment plan with services in the office, home or community, and for crises lists NH Rapid Response (833-710-6477), round-the-clock crisis response for young people in emergency rooms with Catholic Medical Center and Elliot Hospital, and crisis stabilization at its Cypress Street office during business hours; its page gives no wait times.
   - citation: The Mental Health Center of Greater Manchester, Child & Adolescent Services page; DHHS community mental health center regions (library raw/programs/community-mental-health-centers-towns-served.csv)
   - source: https://www.mhcgm.org/mhcgm-programs/child-teen-services/
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: town New Boston
   - note: Page text: "Following a thorough evaluation, we'll develop an individualized treatment plan. Based on individual and family needs, some services are provided in the office and others are provided in the home and community."; "If you or someone you know is experiencing a mental health or substance misuse crisis, CALL (833) 710-6477"; "In collaboration with CMC and Elliot hospital, we provide 24/7 mental health crisis response services, including suicide evaluation and prevention, to children or adolescents in emergency rooms. During regular business hours, we provide crisis stabilization services at our Cypress Street location". The library's CSV lists New Boston (377) and Goffstown (199) in Region 7, The Mental Health Center of Greater Manchester (library programs-and-help.md, community-mental-health-centers 4). Raw: raw/high/town/mhcgm-child-teen-services.txt
7. No Goffstown High, SAU 19 or Mental Health Center of Greater Manchester page or board document read reports how long students wait to see a school counselor, the school psychologist or an outside therapist, so wait times can't be stated from public sources.
   - citation: Goffstown High School Student Handbook 2026-27; Goffstown School Board minutes, April 20, 2026 (counseling program); The Mental Health Center of Greater Manchester, Child & Adolescent Services page
   - source: https://www.sau19.org/index.php/files/1271/2026-05-11/6926/05-11-2026-Goffstown-Meeting-PDF
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: The counseling program says data use "remains an ongoing area of growth" and plans to share data at its 2028 re-approval ("Share school counseling data and set goals"). Also read: Goffstown's raw copies of the GHS counseling pages and newsletters (town/Goffstown/raw/high/). Raw: raw/high/gsb/gsb-meeting-pdf-2026-05-11.txt; raw/high/town/mhcgm-child-teen-services.txt

## district-goals-and-performance-reporting: SAU 19's Portrait of a Graduate

- kind: local
- question_type: local_practice
- description: A district's strategic plan and goals, the measures it reports to the public besides state test scores (surveys, staff evaluation, annual reports, outside rankings it cites), and where residents can find them

1. SAU 19's Portrait of a Graduate (December 2024) names four qualities it wants graduates to have: critical thinking ("adept thinkers and communicators" who solve complex problems alone and with others), connection (contributing through the arts, athletics, co-curriculars and community service), citizenship (strong character, ethical conduct and digital responsibility) and community (caring relationships with peers, staff and community members); it doesn't mention attendance, punctuality or job skills by name.
   - citation: SAU 19, Portrait of a Graduate (December 2024), posted on the SAU 19 and Mountain View websites
   - source: https://www.sau19.org/index.php/en/information-3/about/portrait-of-a-graduate
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: sau 19
   - note: Transcribed from image (https://www.sau19.org/images/SAU/Portrait%20of%20a%20Grad%20December%202024.jpg): "CRITICAL THINKING Our graduates are adept thinkers and communicators, able to adapt to solve complex problems independently and collaboratively. CONNECTION Our graduates contribute positively within and beyond the classroom through the arts, athletics, co-curriculars, and community service. CITIZENSHIP Our graduates work toward a common good, inclusive of personal and cultural differences while embodying strong character, ethical conduct, and digital responsibility. COMMUNITY Our graduates value the unique contributions of--and build caring relationships with--their peers, school staff, and all members of their community." Raw: raw/high/sau19/sau19-portrait-of-a-graduate-2024-12.jpg and -ocr.txt; raw/high/sau19/sau19-portrait-of-a-graduate.txt

## district-school-day-and-calendar: Attendance and Tardiness Rules at Goffstown High

- kind: local
- question_type: local_practice
- description: School hours, before- and after-school care, the school calendar and vacations, and attendance and absence rules

1. Goffstown High's 2026-27 handbook refers a student to an administrator starting with the second unexcused tardy to class, counts ten half-days of unexcused absence in a school year as habitual truancy, bars students absent from school from that day's activities and practices, and requires athletes to attend at least half the school day to practice or play and to be in school and on time the day after an event.
   - citation: Goffstown High School Student Handbook 2026-27, Attendance (p. 6) and Daily School Attendance (pp. 4–5)
   - source: https://www.sau19.org/attachments/article/945/GHS_Handbook_26-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Handbook: "Unauthorized Tardies: starting with the 2nd unexcused tardy to class, the student will be referred to an administrator."; "Ten half-days of unexcused absences during a school year constitutes habitual truancy and the school will respond accordingly."; "Students who do not attend school will not be allowed to participate in or attend school activities that day"; "Student athletes must be in attendance no less than half the school day (7:56-11:01 am or 11:06 am -2:41 pm) ... Athletes are expected to be in school and on time the day following an athletic event." (The half-day times are the 2025-26 bell times; 2026-27 runs 8:00–2:45.) The list of excused absences is in Goffstown's getting-to-school-and-choices.md, district-school-day-and-calendar 16. Raw: raw/high/ghs/ghs-handbook-2026-27.txt

## district-fees: Costs at Mountain View and Goffstown High Not Found in Public Pages

- kind: local
- question_type: local_practice
- description: Costs families may pay: sports, field trips, supplies, technology, instruments and other fees, and help with them

1. Goffstown High's 2026-27 handbook offers families an optional school accident and health insurance plan at the start of the year, gives no price, and says teacher-led tours and trips during summer or school vacations are not sponsored by the school and that teachers on them are "not acting under school district's jurisdiction."
   - citation: Goffstown High School Student Handbook 2026-27, Insurance Program (p. 30) and Tours/Trips Sponsored by Teachers (p. 34)
   - source: https://www.sau19.org/attachments/article/945/GHS_Handbook_26-27.pdf
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Handbook: "A school accident/health insurance plan is available to students at the beginning of the school year. This program is optional and provides reasonably priced coverage"; "Teachers may act on their own or in association with other organizations to sponsor tours and trips during the summer or school vacations. GHS does not sponsor such excursions, and teachers are not acting under school district's jurisdiction. Students and parents/legal guardians are urged to closely scrutinize all aspects of these ventures". Raw: raw/high/ghs/ghs-handbook-2026-27.txt
2. No Mountain View, Goffstown High or SAU 19 page read gives the amount of a sports participation fee, the cost of school field trips or how families rent band and orchestra instruments: Mountain View's sports page sends registration through the PowerSchool parent portal without listing a fee, and its music page lists the band, chorus and orchestra teachers and a calendar without rental information.
   - citation: Mountain View Middle School, Sports and Music pages; Goffstown High School Student Handbook 2026-27
   - source: https://www.sau19.org/index.php/en/information-3/students/mvms-sports
   - as_of: 2026-11-21
   - review_by: 2027-11-21
   - place: district Goffstown
   - note: Sports page: "Log into the parent portal ... Click on Forms in left Navigation menu. Scroll down to Athletic Registration - MVMS and GHS". Music page (https://www.sau19.org/index.php/en/departments-2/academics/mvms-music): "For more information on our programs, please click on the paw or click on a name to send an email". Goffstown's own search for the GHS participation fee also came up empty (Goffstown's mountain-view-high-school-and-mst.md, district-fees 1). Known costs: GHS parking $125 (Goffstown district-fees 5); AP exams $99 each, with New Hampshire covering students with financial need (Bedford's high-school-and-pathways.md, ap-and-ib-exam-fees-and-deadlines 2–3). Raw: raw/high/mvms/mvms-sports.txt; raw/high/mvms/mvms-music.txt

## For another file

- **Agent 4 (money):** New Boston's FY28 requested budget with notes (November 18, 2026; raw/high/nb/nb-fy28-general-fund-requested-with-notes-2026-11-18.txt, p. 19 image saved) gives regular transportation "STA (9 BUSES X $498.13 PER DAY X 180 DAYS) $806,971", "@INCREASE OF $34,584 TO DEFAULT (ELEMENTAY AND MIDDLE)", "@INCREASE OF $3,843 TO NEW (HIGH SCHOOL)", fuel $5,000, late bus $26,314, "@REDUCTION OF $75,184 TO DEFAULT, ALL DAY K"; in-district special education transport (2 buses) $161,968, ESY $20,929, out of district $108,675; field trips $11,472 requested; homeless transportation $25,000; and FY28 AREA tuition "FY28 MVMS TUITION BASED ON 121 STUDENTS AT $18,473" ($2,235,233) and "FY28 GHS TUITION BASED ON 301 STUDENTS AT $19,746" (P12.1, P12.2). The September 23, 2026 minutes record the MST shortfall flowing into New Boston's tuition (cte-center-programs 1 here). The October 14, 2026 minutes list $52,309 of transportation in the September manifest.
- **Agent 2 (support):** the SAU 19 counseling program minutes (raw/high/gsb/gsb-meeting-pdf-2026-05-11.txt, p. 8) say there is "1 school counselor in New Boston" and list "Transitions, 4-5, 6-7 (NB), 8-9" and a "Teacher Support Team at NBCS" (P13.2, P8.1). The September 9, 2026 New Boston minutes say "New Boston sixth-grade teachers met with Mountain View Middle School sixth-grade teachers" on the workshop day (P8.1). Mountain View's grade 7 Signs of Suicide lessons and community meetings are in the same program document.
- **Agent 1 (elementary):** New Boston's NB Elem PM route sheet (dropfiles id 7045) covers Central School afternoons; the morning Elem-MV sheet (id 7046) has Central School arrivals at 7:50–7:55 a.m. (raw/high/routes/nb-derived-bus-route-times-2026-27.csv). The Transfers sheet lists "Walkers" who board transfer buses at Central School. The May 11, 2026 Goffstown PDF has Goffstown's 2026-27 meal prices (Goffstown's, not New Boston's).
- **Goffstown's files:** Goffstown's getting-to-school-and-choices.md, district-transportation 19, gives the GHS handbook's 5 p.m. late bus with "one late run to New Boston"; New Boston's late bus sheet schedules it at 5:30–5:47 p.m. (district-transportation 7 here). Goffstown's district-transportation 4 note ("the Transfers sheet says G 14 and G 15 carry New Boston high school students from transfer points") matches the Transfers sheet read here. Mountain View's handbook and New Boston's afternoon sheet still use the 3:10 dismissal that Goffstown's district-school-day-and-calendar 3 flags.

## Not retrieved

- https://mtabus.org/?p=55 (the Manchester Transit Authority's New Boston Shuttle page, which a search result describes as a free weekday shuttle for New Boston residents to New Boston, Goffstown and Bedford): the site failed with a TLS error for both curl and WebFetch (not a bot block). The town's 2020 flyer (https://www.newbostonnh.gov/sites/g/files/vyhlif4756/f/news/manchester_transit_flyer_2020.pdf) and community services page (https://www.newbostonnh.gov/print/53761) returned HTTP 404. Whether students may use the shuttle to reach school is unknown.
- What Mountain View's digital integration and technical education classes teach: no course description on the Mountain View, SAU 19 Academics or staff pages; the Mountain View Transition Info page is a Canva video (https://www.canva.com/design/DAFgEWi8rec/view) and the Middle School Library Media Presentation 2024 is a Canva design; neither was read.
- The arrival time at Goffstown High of transfer buses G 14 and G 15: not on the New Boston or Goffstown sheets posted on https://www.sau19.org/index.php/en/bus-routes.
- The number of New Boston students at MST: not in New Boston's FY28 budget or the 2026 New Boston minutes read; Goffstown's packet gives about 95 GHS students in MST sessions without a town breakdown.
- GHS sports participation fee, field trip costs and instrument rental arrangements: not on the Mountain View sports and music pages, the GHS handbook or the SAU 19 pages read; registration runs through the PowerSchool parent portal (https://sms.sau19.org/public/), which needs a login.
- Instrument rental rates: a Manchester music store's store page (https://stores.musicarts.com/manchester), read through WebFetch, names New Boston and Goffstown among the towns it serves and says rental pricing varies by school, but posts no rates; not saved or used as a fact.
- Measured bus ride or on-time data: none posted; all ride times here are scheduled.
- Counseling and therapy wait times: no source found (see district-student-support 7).
