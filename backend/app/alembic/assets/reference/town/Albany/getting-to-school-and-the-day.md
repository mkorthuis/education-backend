# Getting to School, the School Day and Family Support for Albany Students

Part of the Albany research (town/Albany). Gathered November 13, 2026.

## Summary

Albany runs no schools. Its students attend Conway's Pine Tree Primary (K–2), Conway Intermediate (3–5), Kennett Middle (6–8) and Kennett High under tuition contracts. This file covers what is specific to Albany families: Albany's own contractor bus (Eldridge Transportation), its 2026–2031 contract, its 2026-27 route sheet and **derived** ride times, the Passaconaway Road arrangement with Conway, and the absence of any bus stop on the Kancamagus Highway. It also covers care before and after school for an early shift, free and reduced-price meal applications and Title I, public preschool and Child Find, school costs, moving between towns (McKinney-Vento), changing a bus stop, and help with food and clothing.

Most school-side answers were already gathered in the Conway files (`town/Conway/daily-life.md`, `schools-k-8.md`, `community-and-choice.md`) and the Jackson file on storm closings. The question table names those facts by file, slug and number; this file does not repeat them.

- **10 fact topics, 46 facts and 1 number table.** Places: `district Albany` for Albany's bus, contracts and choices; `district Conway` for new facts about Conway's schools; `sau 9` for SAU-wide facts; `town Albany` and `town Conway` for geography and community programs; none for state and federal rules.
- **Proposed shared topics (rule, rules, no place):**
  - `homeless-student-school-stability`: federal and New Hampshire rules for homeless children: who counts, staying in the school of origin, immediate enrollment, transportation between districts and residency disputes. No library topic covers McKinney-Vento; the Jackson and Conway files hold only local policy facts.
  - `dyslexia-screening-and-intervention`: New Hampshire's required screening of students in kindergarten through grade 3 for signs of dyslexia, its timelines and what parents are told (RSA 200:59).
- **New data concepts:** Albany's contractor bus route and derived ride times; the bus contract's terms (routes, storm days, stops); the Passaconaway Road arrangement with Conway; road distance from Passaconaway to Kennett Middle (OSRM, derived); NH DOE Title I allocations and the Title I school list for SAU 9 schools. The free or reduced-price meal and English learner counts in NH DOE's adequacy aid calculation are in the site's data (adequacy_aid), so this file does not repeat them.
- **Main sources:** Albany's 2026-27 route sheet (SAU 9 transportation page); the Albany–Conway K–6 (2025), 7–8 (2026) and 9–12 (2003) tuition contracts; Albany School Board and annual meeting minutes, September 2022 to September 2026 (29 sets searched, plus 2 agendas), and the Eldridge 2026–2031 contract attached to the December 9, 2025 minutes; Albany's 2026 annual report; SAU 9's transportation, food services, student services and federal programs pages; SAU 9's 2026 special education procedures manual; NH DOE Title I allocation reports and Title I school list (Wayback copies); Conway School Board and John Fuller committee minutes; Project SUCCEED's site; End 68 Hours of Hunger's Conway page; RSA 193:12, RSA 200:59 and 42 U.S.C. 11432; OpenStreetMap Nominatim and OSRM.
- **Premises checked:**
  - "Pine Tree Elementary or Conway Elementary" (P1.1): out of date. Since September 2024 Conway runs one school per grade band, so there is no choice between them: K–2 children attend Pine Tree Primary and grades 3–5 Conway Intermediate (formerly Conway Elementary). Albany's own 2026-27 bus sheet still calls the 3–5 school "Conway Elementary School."
  - "Strictly assigned by bus route" (P1.1): no. The grade decides the school, and Albany's one bus serves both elementary schools.
  - "High poverty rate" (P1.3), as far as school data goes: NH DOE's adequacy counts in the site's data (adequacy_aid) put about 53% of Albany's resident students as eligible for free or reduced-price meals for FY2027 (2025-26 membership), against about 35% for Conway and 25% statewide (**derived**). Even so, NH DOE listed no Title I allocation for Albany in 2024-25 and $284.98 for 2025-26 (preliminary). Title I money reaches Albany children through Conway's schoolwide programs at Pine Tree and Conway Intermediate; Kennett Middle is not a Title I school. Census poverty is for agent 4.
  - "Upper Kanc/Passaconaway" bus ride (P3.1): no SAU 9 route sheet, Albany's or Conway's, lists a stop on the Kancamagus Highway west of Conway village, so no scheduled ride time exists. Albany's bus runs along Route 16 (Chocorua Mountain Highway). Conway's buses pick up on Albany's part of Passaconaway Road under an agreement.
  - "Remote learning days" in storms (P3.3): partly correct. SAU 9 and Conway's policy IMBA allow remote instruction days at Conway's schools, but no 2025-26 or 2026-27 remote day was found in Conway minutes (Conway file). Albany's bus contract follows the superintendent's closing decisions.
- **Questions answered wholly by earlier files:** 2 of 15 (P10.1, P10.3). Most others were mostly answered by earlier files, and this file adds the Albany-specific parts.
- **Main gaps:** measured (not scheduled) ride times; any time limit for adding or moving a stop; how Albany children in the Passaconaway Road area are picked up today; whether Albany transfers its small Title I allocation to Conway; any kindergarten readiness screening tool or alignment with local preschools; a confidential sign-up process for weekend food bags; a current Purple Star school list.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.1 Choice between Pine Tree and "Conway Elementary," or assigned by bus route | Conway file schools-k-8.md: district-consolidation-history 1, 5–6, 14 (one school per grade band since 2024; names); district-classrooms-and-staff 3 (no teacher requests); this file: district-transportation 1, 5; district-student-support 3 | full | **Premise out of date** (see Summary). The grade decides the school. Albany's contract gives Conway's terms "as is the case with pupils residing in the Town of Conway." A transfer request under RSA 193:3 is in the library (change-of-school-assignment), but Conway has only one school per grade band. |
| P1.2 Before- and after-school care for a 7:00 a.m. shift | Conway file daily-life.md: district-school-day-and-calendar 5–10, 20–21; this file: district-school-day-and-calendar 1–3; Jackson file: town-child-care 1–5 in `Jackson/community-and-families.md` (private care); site data: child_care (licensed programs' weekday hours, Conway district) | partial | Project SUCCEED opens at 7:30 a.m. and runs to 5:15 p.m. Albany's elementary bus picks up from 8:03 a.m. Project SUCCEED's 5:15 late bus has no Albany stops. Nothing school-based starts before 7:30. Private child care is for agent 4; the hours licensed programs list with NH DHHS are in the site's data. |
| P1.3 Free and reduced-price applications for Albany residents; Title I support | Conway file daily-life.md: district-meals 1–4, school-meals-eligibility 1–3; Jackson file: district-meals 10–11, 17 in `Jackson/policies-safety-meals-and-support.md`; library: school-meals-eligibility 9; Conway file schools-k-8.md: district-curriculum-and-assessment 1–3; this file: district-meals 1–3, district-curriculum-and-assessment 1–4; site data: adequacy_aid (Albany and Conway districts and the state: free or reduced-price meal and resident counts); site data: free and reduced lunch | full | Albany families use SAU 9's application, which counts all Conway-school siblings on one form. Pine Tree and Conway Intermediate are schoolwide Title I schools; Kennett Middle and Kennett High are not on NH DOE's list. Site data for 2025-26: Pine Tree 40.4%, Conway Intermediate 41.8%, Kennett Middle 37.3%, state 23.2%. **Premise checked** (see Summary). |
| P3.1 Bus ride length from upper Kanc/Passaconaway to Kennett Middle | this file: district-transportation 4–11; albany_transport_scheduled_ride_minutes_2026_27; Conway file daily-life.md: district-transportation 2, 9, 11 | partial | **Premise checked:** no route reaches the Kancamagus area. Scheduled rides on Albany's Route 16 run take 39–60 minutes to Kennett Middle (**derived**). Passaconaway is 13.2 road miles and about 25 minutes' free-flow drive from Kennett Middle (**derived**, OSRM). No measured winter times. |
| P3.3 Kancamagus and Route 16 storms: remote days vs snow days | Jackson file: district-transportation 48–51; district-school-day-and-calendar 1 in `Jackson/getting-to-school-and-the-school-day.md`; Conway file daily-life.md: district-school-day-and-calendar 21–22, district-family-communication 1–3; this file: district-transportation 12 | full | SAU 9 decides closings, two-hour delays and early releases (elementary 12:30, KMS 11:20, KHS 11:30). Conway's IMBA allows remote days. Albany's contractor must follow the superintendent's decision. **Premise:** remote days are allowed but none was found in use. Kancamagus road status: see Not retrieved. |
| P8.1 Public pre-K in Albany or Conway | this file: district-preschool 1–6; Bartlett file jbes.md: district-preschool 1–9 (JBES pre-K, for Bartlett); library: district-preschool, early-supports-to-preschool-special-ed, head-start-eligibility; Jackson file: town-child-care 1–5 in `Jackson/community-and-families.md` | full | Neither Albany nor Conway runs a public preschool. In August 2026 Conway's board voted 5-1-0 to keep studying one. Children with disabilities from age 2.5 are found and served through SAU 9's Child Find and preschool special education. Private care is for agent 4. |
| P9.1 Kindergarten full or half day; busing a 5-year-old | Conway file schools-k-8.md: district-classrooms-and-staff 5–6; Conway file daily-life.md: district-school-day-and-calendar 1, 29; library: kindergarten-rules, kindergarten-day-length; this file: district-transportation 3, 5–7; albany_transport_scheduled_ride_minutes_2026_27 | full | Kindergarten runs Pine Tree's full 9:00–3:15 day; no half-day session is described. An Albany kindergartner rides the elementary run: 22 to 57 minutes in the morning, depending on the stop (**derived**), getting home 3:55 to 4:20 p.m. No kindergarten-specific bus rule was found for Albany's bus. |
| P9.3 Supplies, Chromebooks, field trips and fees | Jackson file: district-fees 10, 12–13 in `Jackson/policies-safety-meals-and-support.md` (Kennett; Conway field trip policy IICA); Conway file daily-life.md: district-technology-and-phones 1–2; this file: district-fees 1–3 | partial | No supply list or fee schedule is posted for Pine Tree, Conway Intermediate or Kennett Middle. KMS Chromebooks stay at school, and families pay for damage. Field trip costs are in the expenses that set Albany's K–6 tuition. Per-trip charges to families are not published. |
| P10.1 English learner support and Spanish communications | Conway file schools-k-8.md: district-student-support 1–4; Conway file daily-life.md: district-family-communication 8–10; sau9 file: district-family-communication 1–4; Jackson file: district-student-support 1–6; district-family-communication 1 in `Jackson/policies-safety-meals-and-support.md`; library: english-learner-rights; site data: English learners; site data: adequacy_aid (Albany district, English learner count) | partial | Answered by earlier files: ESOL support at Pine Tree, two ESL teachers at Conway Intermediate, an ESL teacher and interpreters at KMS; no Spanish-language handbooks or forms found. The site's adequacy aid data adds one data point: NH DOE counts no English learners among Albany's resident students in FY2020–FY2027. |
| P10.3 Bilingual liaisons or interpreters for conferences and registration | Conway file daily-life.md: district-family-communication 8–10; Conway file community-and-choice.md: district-student-support 7 (family liaisons); sau9 file: district-family-communication; library: interpreters-and-translation-for-parents | partial | Answered by earlier files. Interpreters may be used at KMS conferences and for forms. No named bilingual liaison was found; family support liaisons are not described as bilingual. |
| P16.2 Support for military and veteran families at KMS | library: military-children-compact 1–2, military-families-nh 1–5; this file: district-student-support 2 | partial | KMS has a school counselor offering individual, group and crisis counseling. No KMS or SAU 9 program for military-connected or veteran families was found, and no SAU 9 school is known to be a Purple Star school. The interstate compact covers active-duty families, not veterans. |
| P17.1 Kindergarten readiness screening and local preschools | additional-data/district-practices.md: kindergarten-registration 12; Conway file schools-k-8.md: district-curriculum-and-assessment 6, 9; this file: dyslexia-screening-and-intervention 1–2, district-preschool 3–4 | partial | State law requires screening for dyslexia risk within 60 school days of entry. Conway uses Acadience early-literacy screening, and nearly all incoming kindergartners took summer programming in 2025. SAU 9's Child Find contacts community programs every year. **No document on aligning screening with local preschool curricula was found.** In 2025 local child care directors told Conway's board they wanted to be part of the preschool conversation. |
| P19.1 McKinney-Vento: staying in the same school across Albany, Conway and Bartlett; who pays transport | this file: homeless-student-school-stability 1–6, district-student-support 3, district-transportation 1, 15; Conway file community-and-choice.md: district-student-support 1–2, 6–9; Jackson file: district-student-support 7–9 in `Jackson/policies-safety-meals-and-support.md` | full | A move between Albany and Conway does not change the child's school. A homeless child may stay in the school of origin for the rest of the homelessness, and the two districts share the extra transport cost (equally if they can't agree). Whether a family moving between seasonal leases counts as homeless depends on the federal and state definition; the district's homeless liaison decides. Albany has no homeless-student policy of its own posted. |
| P19.2 How fast a stop changes after a mid-year move | this file: district-transportation 13–14; Conway file daily-life.md: district-transportation 17 (Conway policy EEA); homeless-student-school-stability 4 | partial | Albany's contract has the district and contractor work together on "daily changes," and SAU 9 sends Albany route questions to Eldridge. Conway sends stop requests to SAU 9's transportation coordinator. **No time limit is written anywhere.** |
| P19.3 Confidential food, clothing and weekend backpacks through the nurse or counselor | Conway file schools-k-8.md: district-student-support 7; Conway file community-and-choice.md: district-student-support 7; Conway file daily-life.md: town-family-help 1; this file: district-student-support 1, town-family-help 1 | partial | Pine Tree's Family Support Liaison works confidentially and helps with winter clothing. Each school level keeps a supply space (snacks, socks, boots, coats). End 68 Hours of Hunger delivers weekend food bags to Pine Tree and Conway Intermediate and stocks food closets at KMS and Kennett High. How a family signs up for bags is not published. |

## district-transportation: Albany's School Bus, Its Contract, Route Times and the Kancamagus

- kind: local
- question_type: local_practice
- description: Bus service: who runs it, routes and times, eligibility, late and activity buses, storm closings and delays, and transport to schools outside the district

1. Albany's tuition contracts with Conway for grades K–6 (dated April 20, 2025), 7–8 (dated March 10, 2026, for 2027-28) and 9–12 (2003) each make the Albany School District "responsible for the transportation methods and expenses" of its students' attendance, while Conway accepts Albany students "on the same terms and conditions" as students who live in Conway.
   - citation: Albany/Conway Tuition Agreement, Grades K-6 (April 20, 2025), "Tuition Arrangement"; Albany/Conway Tuition Agreement, Grades 7-8 (March 10, 2026), section I; Albany/Conway Tuition Agreement, Grades 9-12 (May 2003), section 1
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Scanned; read by OCR. K–6 text: "Albany School District shall send pupils, grades K through 6, with the exceptions hereinafter noted, exclusively to Conway for schooling; and Albany School District shall be responsible for the transportation methods and expenses in connection with such attendance. Conway shall accept said pupils and be responsible for their education on the same terms and conditions, providing them with the same opportunities for educational and cultural advancement and improvement as is the case with pupils residing in the Town of Conway." The 7–8 and 9–12 contracts use the same transportation wording. The K–6 contract also makes Albany pay for transport to any out-of-district special education placement. Contract terms and costs belong to the money file. Raw copies: raw/daily/albany/contracts/sau9-contract-k-6-albany-conway-current.pdf, .ocr.txt; sau9-contract-9-12-albany-conway-current.ocr.txt; contract-7-8-albany-conway-2027.ocr.txt (copied from town/Conway/raw/money/contracts/)
2. Albany's students ride a bus run by a private company, Eldridge Transportation, under a contract with the Albany School Board. On December 9, 2025 the board voted 3-0-0 for a new five-year contract running from July 1, 2026 to June 30, 2031, after a board member said the company had been reliable. Eldridge had replaced an earlier contractor, MacIver Transportation, by September 2022.
   - citation: Albany School Board minutes, December 9, 2025, item 5.a, and attached "Albany School District 2026-2031 Transportation Contract," section 2; minutes of October 14, 2025, item 5.A, and September 13, 2022, item V.B
   - source: https://drive.google.com/file/d/1S5JKCiqNrOnMtJ5av_TbyibTZgli8BQ1/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Scanned; read by OCR. December 9, 2025: "Mike Wade explained that the proposal is identical to the current one, with the exception of the cost per mile increase, and is for a five year term ... Dan Bianchino feels that the company has been reliable. Curtis Coleman made a motion to approve the contract from Eldridge Transportation, seconded by Kristin Stelmok, 3-0-0." Contract: "The term of the contract is five (5) years beginning July 1, 2026 to June 30, 2031." October 14, 2025: "Bianchino said they have been satisfied with Eldridge and stated he would like to continue with another five year contract." September 13, 2022: "The previous transportation contract with MacIver Transportation did have a clause in the contract for fuel costs beyond $2.50/gallon." The per-mile rates and fuel clause are in "For another file". Conway, by contrast, runs its own buses with district drivers (Conway file daily-life.md, district-transportation 1). Raw copies: raw/daily/albany/minutes/Albany-School-Board-Minutes-12-December-9-2025-with-Attachment.pdf, .ocr.txt; Albany-School-Board-Minutes-10-October-14-2025.txt; Albany-School-Board-Minutes-22-9-September-13-2022.txt
3. Albany's 2026–2031 bus contract requires a bus "large enough to accommodate all Albany Students." It pays by the mile from the first pickup to the last drop-off, and drivers must follow the rules and policies of both the Albany and Conway districts. No driver may refuse an eligible student, and students may leave the bus only at scheduled stops, where a parent or guardian is required to be present, or with written permission.
   - citation: Albany School District 2026-2031 Transportation Contract, sections 11, 12, 21 and 23(e) and (g) (attached to Albany School Board minutes, December 9, 2025)
   - source: https://drive.google.com/file/d/1S5JKCiqNrOnMtJ5av_TbyibTZgli8BQ1/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: OCR text: "The Contractor shall provide a bus large enough to accommodate all Albany Students." "Mileage shall be calculated from first student picked up to the final destination in the morning. Then from the first school to the last drop off in the afternoon." "All drivers shall follow the rules and policies, practices and procedures of the Albany and Conway School District at all times." "No driver will allow students to leave the bus except at scheduled stops or when a parent/guardian is required to be there or upon written permission." "A driver does not have the authority to refuse transportation to any eligible student nor does the driver have the authority to remove a student from the bus." Buses may be no older than ten years. The contract does not say which stops require a parent, such as for kindergartners. Raw copy: raw/daily/albany/minutes/Albany-School-Board-Minutes-12-December-9-2025-with-Attachment.ocr.txt
4. On the 2026-27 Albany run to Kennett Middle and Kennett High, the bus starts at the Madison/Albany town line at 6:25 a.m. It stops along Chocorua Mountain Highway (NH Route 16) and on Nickerson Road, Priscilla Road, Bald Hill Road, Kelly Drive and Brookside Avenue until 6:46, then reaches Kennett High School at 7:15 and Kennett Middle School at 7:25.
   - citation: Albany School District Bus Route – KHS/KMS, 2026-2027 (updated 8/11/2026), linked from SAU 9's Transportation page
   - source: https://files.smartsites.parentsquare.com/10271/albany26-27.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Read from the page images, since the left edge of some lines is cut off. Sheet text: "6:25 From the Madison/Albany Town line – Bus will continue south on Chocorua Mtn. Hwy / 6:27 2020 Chocorua Mtn. Hwy / 6:28 2192 Chocorua Mtn. Hwy (Blakes Towing) / [6:]30 Right onto Nickerson Road to "Bus Hut" ... / 6:35 Left onto Chocorua Mtn. Hwy and Priscilla Road, (turning around) / 6:38 2061 Chocorua Mtn. Hwy / 6:39 Left onto Bald Hill Road / 6:40 Bald Hill Road and Cook Farm Road / 6:41 Bald Hill Road and Stacy Lane / 6:44 1297 Chocorua Mtn. Hwy, (Albany Auto) / 6:45 Right onto Kelly Drive ... / 6:46 Brookside Ave and Chocorua Mtn. Hwy / 7:15 Drop off at Kennett High School / 7:25 Drop off at Kennett Middle School". Kennett Middle starts at 7:35 (Conway file daily-life.md, district-school-day-and-calendar 4). Albany's sixth graders attend Kennett Middle, so they ride this run. Chocorua Mountain Highway is NH Route 16: OpenStreetMap tags it "ref NH 16" with "alt_name Chocorua Mtn Hwy" (Nominatim, raw/daily/geo/chocorua-hwy-names.json). Raw copies: raw/daily/routes/albany26-27.pdf, -p1.png, -p2.png, .txt; raw/daily/sau9/sau9-transportation.txt
5. On the 2026-27 Albany elementary run, the bus picks up from 8:03 a.m. (Wildwood Road and Tabor Circle) to 8:38 a.m. (Bald Hill Road), along Route 16, Nickerson Road, Drake Hill Road and Bald Hill Road. It drops off at "Conway Elementary School," the former name of Conway Intermediate, at 8:50 and at Pine Tree Primary at 9:00, so one run serves both schools.
   - citation: Albany School District Bus Route – Elementary Schools, 2026-2027 (updated 8/11/2026)
   - source: https://files.smartsites.parentsquare.com/10271/albany26-27.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Sheet text: "8:03 Right onto Wildwood Road, then left onto Tabor Cir. / 8:05 Right onto Chocorua Mtn. Hwy / 8:08 2020 Chocorua Mtn. Hwy / 8:10 2192 Chocorua Mtn. Hwy (Blake Towing) / 8:15 Priscilla Road and Chocorua Mtn. Hwy / 8:16 Turn around at the Tamworth/Albany Town line / 8:18 2521 Chocorua Mtn. Hwy / [8]:20 Left onto Nickerson Road to "Bus Hut" ... / 8:21 Left onto Cocorua Mtn. Hwy to Drake Hill Road / 8:22 426 Drake Hill Road to end ... / 8:24 Right onto Chocorua Mtn. Hwy to Bald Hill Road / 8:30 Bald Hill Road and Cook Farm Road / 8:38 Bald Hill Road, returning to Chocorua Mtn. Hwy, turning left / 8:50 Drop off at Conway Elementary School / 9:00 Drop off at Pine Tree Primary School". Conway Intermediate's day starts at 8:50 and Pine Tree's at 9:00 (Conway file daily-life.md, district-school-day-and-calendar 1–2). Raw copies: raw/daily/routes/albany26-27-p2.png, -p3.png, .txt
6. In the afternoon, the 2026-27 Albany sheet lists the middle and high school run's first stop at 2:40 p.m. (Albany Auto) and its last at 3:10 (Bald Hill Road and Stacy Lane), after which the "Bus proceeds to the Conway Elementary Schools." The elementary return lists pickups at Conway Intermediate and Pine Tree with no times, a first timed stop at 3:55 (Bald Hill Road) and a last at 4:20 (426 Drake Hill Road).
   - citation: Albany School District Bus Route – Return (KHS/KMS) and Return (Elementary), 2026-2027 (updated 8/11/2026)
   - source: https://files.smartsites.parentsquare.com/10271/albany26-27.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Sheet text: "2:40 Albany Auto / 2:42 Brookside Ave ... / 2:43 Kelly Drive ... (Coleman Rental) / 2:54 2020 Chocorua Mtn. Highway / 2:55 2192 ... (Blake Towing) / 2:58 Left onto Nickerson Road to turn around / 3:00 ... / 3:02 ... Priscilla Road, turning around / 3:05 2061 ... / 3:08 Left onto Bald Hill Road / 3:09 Bald Hill Road and Cook Farm Road / 3:10 Bald Hill Road and Stacy Lane / Bus proceeds to the Conway Elementary Schools" and "Pick up at Conway Elementary School / Pick up at Pine Tree Primary School / ... 3:55 Left onto Bald Hill Road / ... 4:05 2020 Chocorua Mtn. Hwy / ... 4:12 Turn around at the Tamworth/Albany Town line / ... 4:18 ... to Drake Hill Road / 4:20 426 Drake Hill Road". The sheet gives no departure time from Kennett or from the elementary schools. Albany has no late bus from Kennett (a KMS principal's 2024 remark is in the Conway file, daily-life.md, district-transportation 15 note). Raw copies: raw/daily/routes/albany26-27-p3.png, -p4.png, .txt
7. **Derived:** on Albany's 2026-27 sheet, a middle schooler is scheduled to ride 39 to 60 minutes to Kennett Middle School, depending on the stop, and an elementary child 12 to 57 minutes, with the longest rides to Pine Tree Primary. In the afternoon, the last middle and high school stop comes about 60 minutes after Kennett Middle's 2:10 p.m. bus dismissal, and the elementary drop-offs, from 3:55 to 4:20 p.m., come 25 to 65 minutes after Conway Intermediate's 3:15–3:30 dismissal.
   - citation: Albany School District Bus Route 2026-2027; A. Crosby Kennett Middle School Handbook 2026-2027, "Schedule"; Conway Intermediate School Family Handbook 2026-2027, "Arrival/Dismissal"
   - source: https://files.smartsites.parentsquare.com/10271/albany26-27.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Scheduled arrival minus the scheduled time at the stop; afternoon figures use the handbooks' dismissal times because the sheet prints no departure times. These are scheduled, not measured, times, with no weather delays. Each stop is in table albany_transport_scheduled_ride_minutes_2026_27. Conway's own elementary routes run 28 to 55 minutes in the morning (Conway file daily-life.md, district-transportation 7), and in 2024 SAU 9 reported all Conway rides under one hour (same file, fact 9). KMS handbook: "Students who take the bus are dismissed at 2:10"; CIS handbook: "Dismissal will be from 3:15-3:30pm." Raw copies: raw/daily/routes/albany26-27-p1.png to -p4.png; raw/daily/conway/kms-handbook-2026-27.txt; cis-handbook-2026-27.txt
8. Albany's bus contract does not cover the Passaconaway Road part of Albany. In February 2024 the superintendent told the Albany School Board that Conway picks up students there under an agreement with Albany.
   - citation: Albany School Board minutes, February 13, 2024, public hearing on the 2024-25 proposed budget
   - source: https://drive.google.com/file/d/1RRWa7FLDiblyPXuRjZUhJJF5-1_Gyvma/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Text: "Tim Sorgi asked about the transportation costs being higher than he expected. Kevin explained that the bus contract with Eldridge transportation does not include the Passaconaway Road portion of Albany. There is an agreement with Conway to pick up those students at a cost of approximately $4,200." Whether the arrangement continued in 2025-26 and 2026-27 is not stated in later minutes (searched through September 8, 2026). Passaconaway Road runs west from Conway along the Swift River into Albany; OpenStreetMap places segments of it in Albany (raw/daily/geo/passroad-albany.json). It is a different place from the Passaconaway area on the Kancamagus Highway (fact 10). Raw copies: raw/daily/albany/minutes/Albany-School-Board-Minutes-24-2-February-13-2024.pdf, .txt
9. Conway's 2026-27 West Side route (driver Larry, bus 35) lists a "Passaconaway Road" stop at 6:48 a.m. on its morning run, 18 minutes before Kennett High (7:06) and 32 minutes before Kennett Middle (7:20) (**derived**). The sheet does not say where on Passaconaway Road the stop is or whether it is the stop for Albany students, and the route's afternoon and elementary runs do not list Passaconaway Road.
   - citation: SAU 9 Bus Routes & Schedules 2026-2027, "West Side" (Larry, bus 35)
   - source: https://files.smartsites.parentsquare.com/10271/larry_day_-_west_side_road.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Read from the page image: "6:45 Side Track Road / 6:48 Passaconaway Road / 6:54 Washington Street / 7:06 Kennett High School / 7:20 Kennett Middle School". Afternoon: "3:05 Side Track Road / 3:08 Washington Street / 3:18 Pine Tree". Elementary run: no Passaconaway Road stop. Raw copy: raw/daily/conway/route-larry_day_-_west_side_road-p1.png (copied from town/Conway/raw/daily/routes/)
10. No 2026-27 SAU 9 route sheet, Albany's or Conway's, lists a stop on the Kancamagus Highway west of Conway village or in the Passaconaway area of Albany. Conway's "Conway" route (driver Gail) stops only at "Route 16 / Top of Kancamagus Hwy" in Conway, at 6:47 a.m. and 2:58 p.m., and Albany School Board minutes from September 2022 to September 2026 do not mention the Kancamagus.
   - citation: SAU 9 Bus Routes & Schedules 2026-2027 (Albany sheet and the eight Conway sheets); Albany School Board minutes, September 13, 2022 to September 8, 2026 (draft)
   - source: https://www.sau9.org/transportation
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Statement of absence. Searched the route sheets' text for "Kanc", "112", "Passaconaway", "Bear Notch" and "Swift". The only matches are Gail's "Route 16 / Top of Kancamaugus Hwy" (as printed in the morning) and Larry's "Passaconaway Road" (fact 9). Searched 29 sets of Albany board and annual meeting minutes plus two 2026 agendas for "Kanc", "route", "bus" and "transport". How families on the upper Kancamagus get to school, such as driving to a stop, is not recorded. Raw copies: raw/daily/conway/route-gail_goodman_-_conway-p1.png; raw/daily/routes/albany26-27.txt; raw/daily/albany/minutes/
11. **Derived:** the Passaconaway area of Albany is about 13.2 road miles and a 25-minute free-flow drive from Kennett Middle School along the Kancamagus Highway and Main Street, and about 17.8 miles and 36 minutes from Kennett High School.
   - citation: OpenStreetMap Nominatim geocoding and OSRM driving routes from the Passaconaway hamlet, Albany (43.99507, -71.34007) to Kennett Middle School (176 Main Street, Conway) and Kennett High School (409 Eagles Way, Conway)
   - source: https://router.project-osrm.org/route/v1/driving/-71.3400733,43.9950700;-71.1253473,43.9796649?overview=false&steps=true
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Albany
   - note: OSRM returned 13.18 miles and 25.3 minutes to Kennett Middle (roads: "Kancamagus Highway", "Main Street") and 17.82 miles and 36.1 minutes to Kennett High. These are free-flow car estimates with no weather, traffic or bus stops, not bus times. "Passaconaway" is OpenStreetMap's hamlet point in Albany. Called with the generic identifier nhfacts-research (webmaster@nhfacts.com). Raw copies: raw/daily/geo/passaconaway.json; kms.json; khs.json; osrm-passaconaway-to-kms.json; osrm-passaconaway-to-khs.json
12. Albany's 2026–2031 bus contract says only the superintendent decides to cancel or delay school, and the contractor must follow that decision. Buses and drivers must be ready on two hours' notice for an early closing for weather. The district may cancel school days or open two hours late, and the contractor is paid only for the miles actually driven.
   - citation: Albany School District 2026-2031 Transportation Contract, sections 4, 17 and 23(j)
   - source: https://drive.google.com/file/d/1S5JKCiqNrOnMtJ5av_TbyibTZgli8BQ1/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: OCR text: "The District reserves the right to cancel scheduled school days or open school on a delayed basis with a two (2) hour notice because of weather or other emergencies. ... Should the District operate less than one hundred eighty (180) days the Contractor will not be paid for the fewer miles traveled." "All buses and drivers must be available on two (2) hours' notice for early closing of one of more schools due to weather or other emergency". "The decision to cancel of delay school shall be mase solely by the Superintendent and the Contractor shall abide by such decision." SAU 9's closing, delay and early release procedure and Conway's remote-day policy IMBA are in the Jackson file (district-transportation 48–51; district-school-day-and-calendar 1 in `Jackson/getting-to-school-and-the-school-day.md`) and the Conway file (daily-life.md, district-school-day-and-calendar 21–22). Raw copy: raw/daily/albany/minutes/Albany-School-Board-Minutes-12-December-9-2025-with-Attachment.ocr.txt
13. Under Albany's bus contract, the contractor proposes routes by August 1 and the district changes and approves them by August 10 each year, and the two "work together when scheduling changes and making daily changes of daily routes as necessary." SAU 9's transportation page sends questions about the Albany route to Eldridge Transportation (603-387-9452), and neither document sets a time limit for adding or moving a stop.
   - citation: Albany School District 2026-2031 Transportation Contract, sections 3 and 18; SAU 9 Transportation page
   - source: https://www.sau9.org/transportation
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: OCR text: "The Contractor shall provide the District routes by August 1 of each school year. The District shall make changed and approve the routes by August 10«. The District Contractor shall work together when scheduling changes and making daily changes of daily routes as necessary." Section 3: "This contract may be amended by the district with notice due to changes in the transportation scheduled route to be covered, or the number of students to be transported." Page text: "*For any questions or concerns regarding the Albany Bus Route, please contact Eldridge Transportation 603-387-9452". Statement of absence for a timeline. For Conway's own buses, stop requests go to SAU 9's transportation coordinator under policy EEA (Conway file daily-life.md, district-transportation 17). Raw copies: raw/daily/albany/minutes/Albany-School-Board-Minutes-12-December-9-2025-with-Attachment.ocr.txt; raw/daily/sau9/sau9-transportation.txt
14. SAU 9's 2026-27 transportation page says not every stop is listed. A family whose stop falls between two listed stops should expect the bus between those two times, students should be at the stop 5 to 7 minutes early, and afternoon times fall within a 5-to-10-minute window. The page says "All bus routes will be updated by October 1st," but the Albany sheet posted on November 13, 2026 was last "Updated 8/11/2026."
   - citation: SAU 9 Transportation page, "SAU#9 Bus Routes & Schedules 2026-2027"; Albany School District Bus Route 2026-2027
   - source: https://www.sau9.org/transportation
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Page text: "SAU9 does not list every bus stop. ... If your stop falls between two stops that are listed, please insert your stop between the two times and have the student at your stop ready to go. If your stop is close to another stop, we ask that students combine stops. Students should be out at their bus stop 5-7 minutes prior to bus arrival time." and "The afternoon bus stop times are within a 5-10 minute window as well. ... All bus routes will be updated by October 1st once the school year gets going". The downloaded Albany PDF was byte-for-byte the same as the copy saved in the Conway research earlier on November 13. Raw copies: raw/daily/sau9/sau9-transportation.html, .txt; raw/daily/routes/albany26-27.pdf
15. The Albany School Board's posted policy folders hold 11 policies, in sections A, B, D and J, and none covers student transportation, homeless students, children in foster care or school meals. Conway, whose schools Albany students attend, has its own policies on these (EEA, JFABD and JFABE).
   - citation: Albany School Board, "Policies - Albany" Google Drive folders, sections A–L, linked from the SAU 9 Albany School Board page
   - source: https://drive.google.com/drive/folders/1fk72EHxT_E_G0TfQU3D0DQroR-msXV5j
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Statement of absence. Listed files: A: AC, ACAA-R/JBAA-R, ACAA/JBAA, ACF; B: BIE; D: DAF, DK ("Reimbursement for Special Education Travel"); J: JE, JECA, JECAA, JFCJ. Sections C and E–L were empty. The Conway policies are in the Conway files (daily-life.md, district-transportation 17 and district-student-support 1–4; community-and-choice.md, district-student-support 1–5). Raw copies: raw/daily/albany/drive-policies-root.html; drive-policies-section-A.html to -L.html

## district-school-day-and-calendar: Early Shifts, Project SUCCEED and the Albany Bus

- kind: local
- question_type: local_practice
- description: School hours, before- and after-school care, the school calendar and vacations, and attendance and absence rules

1. **Derived:** for a parent whose shift starts at 7:00 a.m., the earliest school-based care, Project SUCCEED's morning program at Pine Tree and Conway Intermediate, opens 30 minutes later at 7:30, and Albany's elementary bus picks up between 8:03 and 8:38 a.m. No SAU 9, Conway or Albany document found offers school care or transport earlier.
   - citation: Project SUCCEED 2026-2027 Parent and Caregiver Handbook, "Hours"; Albany School District Bus Route – Elementary Schools, 2026-2027
   - source: https://www.projectsucceed.com/program-information
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Handbook: "The morning program is open from 7:30 to 8:30 AM Monday through Friday, when staff is available." Statement of absence for earlier care, from the Project SUCCEED pages, the 2026-27 Pine Tree, Conway Intermediate and Kennett Middle handbooks, and the Albany bus contract and sheet. Project SUCCEED's hours, fees, capacity (Pine Tree's fall 2026 session was full) and closures are in the Conway file (daily-life.md, district-school-day-and-calendar 5–11). Licensed child care is for the community file. Raw copies: raw/daily/project-succeed/ps-parent-handbook.txt (copied from town/Conway/raw/daily/project-succeed/); raw/daily/routes/albany26-27.txt
2. Project SUCCEED's 5:15 p.m. late bus lists three routes for 2026-27 (Conway; Center, East and South Conway; North Conway and Intervale), with no stop in Albany, and its handbook requires parents to pick children up by 5:15 p.m.
   - citation: Project SUCCEED "Program Information" page, "Transportation: (5:15 PM Late Bus)"; Parent and Caregiver Handbook 2026-2027
   - source: https://www.projectsucceed.com/program-information
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Page text: "A modified bus route is provided at 5:15 PM at both Conway Intermediate and Pine Tree Primary." Route headings: "Conway Bus", "Ctr Conway/East Conway/ South Conway Bus" (last stop "East Conway Road @ Sherman's Farm"), "North Conway/Intervale Bus" (last stop "Saw Mill Lane"). Handbook: "Parents are required to pick their children up promptly by 5:15 p.m." No Albany road appears on any list. Raw copies: raw/daily/project-succeed/ps-program-information.html, .txt; ps-parent-handbook.txt
3. No Project SUCCEED page or its 2026-27 handbook limits enrollment by town of residence. They describe a program for the Conway School District's elementary schools, where Albany's K–5 children are enrolled, and for sixth graders at Kennett Middle.
   - citation: Project SUCCEED website (Home, Program Information, Pine Tree and Conway Intermediate pages); Parent and Caregiver Handbook 2026-2027
   - source: https://www.projectsucceed.com/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Statement of absence. Searched the saved pages and handbook for "Albany", "Eaton", "resident", "tuition", "eligib" and "enrolled". The only eligibility statement found is "6th grade students at Kennett Middle School are eligible to join the after school program at Conway Intermediate school." Whether Albany children are enrolled today is not published. Raw copies: raw/daily/project-succeed/ps-program-information.txt; ps-parent-handbook.txt

## district-meals: Applying for Free or Reduced-Price Meals From Albany

- kind: local
- question_type: local_practice
- description: School meals: what is served, prices, free and reduced-price applications, meal charges, summer meals, food service providers and local food

1. SAU 9's Food Services page posts free and reduced-price meal packets for the Bartlett, Conway and Jackson districts and none for Albany. Its online application tells families to enter "SAU #9" as the district, and the 2026-27 Conway packet's letterhead names all seven SAU 9 districts, including Albany, and asks families to return the form to their child's school.
   - citation: SAU 9 Food Services page; SAU 9 letter to families and Conway Free & Reduced Application Packet 2026-27 (September 3, 2026)
   - source: https://www.sau9.org/food-services
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Page text: "Free & Reduced Lunch Online App (EZMeal­App) When selecting the District, please enter "SAU #9."" and links "Bartlett Free & Reduced Application Packet (2026-27) ... Conway Free & Reduced Application Packet (2026-27) ... Jackson Free & Reduced Application Packet (2026-27)". Packet letter: "Please fill out and return the attached application to your student's school as soon as possible"; letterhead footer "Albany • Bartlett • Chatham • Conway • Eaton • Hart's Location • Jackson". No document says in so many words which packet Albany families use. Albany children eat at Conway's schools, whose food service director is listed on the page. Raw copies: raw/daily/sau9/sau9-food-services.html, .txt; raw/daily/conway/conway-free-reduced-packet-2026-27.ocr.txt (copied from town/Conway/raw/daily/meals/)
2. The 2026-27 Conway application instructions say a household needs only one application "even if your children attend more than one school in the Conway School District," so siblings at Pine Tree, Conway Intermediate, Kennett Middle and Kennett High go on one form.
   - citation: Conway Free & Reduced Application Packet 2026-27, "How To Apply for Free and Reduced Price School Meals"
   - source: https://drive.google.com/file/d/1v6lYad_dZ1B27rW4SUYCCEOYBqhnf8A5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Scanned; OCR text: "You only need to submit one application per household, even if your children attend more than one school in the Conway School District". The federal rule is in the library (school-meals-eligibility 9). Applying when income drops, the "current income" rule and categorical eligibility are in the Conway file (daily-life.md, district-meals 2–4). Raw copy: raw/daily/conway/conway-free-reduced-packet-2026-27.ocr.txt
3. SAU 9 says there is no universal free meal program in 2026-27, so families must apply for 2026-27 benefits, and that "qualifying has a positive affect on our grant allocations." SAU 9's letter says a school "may be eligible for additional funds based on free and reduced lunch numbers," and Pine Tree's handbook says an approved application lowers Project SUCCEED fees and affects staffing through programs "such as Title I."
   - citation: SAU 9 Food Services page; SAU 9 letter to families, September 3, 2026; Pine Tree Family Handbook 2026-2027, "Food Service"
   - source: https://www.sau9.org/food-services
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Page text: "Please be aware that there is no universal free meal program for the 2026-27 school year. ... It is VERY important that families apply for free/reduced lunch benefits for 2026-27 ... Additionally, qualifying has a positive affect on our grant allocations each year." Letter: "Your student's school may be eligible for additional funds based on free and reduced lunch numbers. Therefore, it may benefit all the students in the school for you to apply". Pine Tree: "A completed and approved application has many benefits including reduced fees for families to attend Project SUCCEED. Additionally, it impacts programming and staffing for students through state-funded programs such as Title I and other grant sources". (Title I is federal; the handbook's wording is quoted as printed.) Raw copies: raw/daily/sau9/sau9-food-services.txt; raw/daily/conway/conway-free-reduced-packet-2026-27.ocr.txt; ptps-handbook-2026-27.clean.txt

## district-curriculum-and-assessment: Title I for the Schools Albany Students Attend

- kind: local
- question_type: local_practice
- description: The curriculum programs a district uses (math, reading, science), how reading is taught and supported, its local tests, and how teachers fit local content into lessons

1. NH DOE's list of Title I schools for 2024-25 shows Conway's two elementary schools, listed by their 2024-25 names Lakeside Primary (now Pine Tree Primary) and Mountainside Intermediate (now Conway Intermediate), as schoolwide Title I programs ("SWP"). Neither Kennett Middle School nor Kennett High School is on the list.
   - citation: NH DOE, "Title I Schools 2024-2025" ("TitleISchoolsTASSWP 2025")
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/title-i-schools-2024-2025_0.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-13
   - place: district Conway
   - note: Rows: "9 Conway SAU Office 113 Conway 29272 Lakeside Primary School" and "9 Conway SAU Office 113 Conway 29271 Mountainside Intermediate School". The Title I column prints on a separate page (p. 7); matched row by row from the page images, rows 18 and 19 read "SWP" ("TAS" means targeted assistance). In a schoolwide program, Title I money supports the whole school. The handbook's own statement and the reading interventions are in the Conway file (schools-k-8.md, district-curriculum-and-assessment 1–3). NH DOE refuses automated requests, so the archived copy was used. Raw copies: raw/daily/title1/t1-schools-2024-25.pdf, .txt; t1schools-p1.png; t1schools-p7.png
2. SAU 9's Federal Programs page posts Title I plans and school compacts for Conway Intermediate and Pine Tree Primary, and for Bartlett and Jackson Grammar, but none for Kennett Middle School. It says Title I services add to regular instruction and that "students do NOT have to be from low-income families to receive support through Title I funded programming."
   - citation: SAU 9 Federal Programs page, "Title I"
   - source: https://www.sau9.org/title-ix
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Page text: "Title I, Part A of the Elementary Secondary Education Act (ESEA) provides financial assistance to schools with high numbers or high percentages of students from low-income families. ... Please note that students do NOT have to be from low-income families to receive support through Title I funded programming. Services provided are supplemental to instuction that already occurs within the school setting." Links: "CIS Title I Plan", "CIS School Compact", "PTPS Title I Plan", "PTPS School Compact", "Bartlett Title I Plan", "Jackson Grammar School Title I Plan", plus Conway, JBES and JGS parent guides. The page's address is /title-ix, though it is headed "Federal Programs". Raw copies: raw/daily/sau9/sau9-federal-programs.html, .txt
3. NH DOE's Title I allocation reports list no allocation for the Albany School District in 2024-25 (first final) and $284.98 for 2025-26 (preliminary), against $534,670.55 and $583,562.58 for the Conway School District.
   - citation: NH DOE, "2024-2025 First Final Allocations Report for Title I, Part A" and "2025-2026 Preliminary Allocations Report for Title I, Part A"
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/uniform-document-for-preliminary-allocation-postings_title-i-part-a.pdf
   - as_of: Wayback snapshot 2025-08-31
   - review_by: 2027-11-13
   - place: district Albany
   - note: 2024-25 rows: "Albany -" and "Conway 534,670.55" (statewide "Local Educational Agency Allocation: $44,646,630.86"). 2025-26 preliminary rows (July 40%, October 60%, total): "Albany 113.99 170.99 284.98"; "Conway 233,425.03 350,137.55 583,562.58". Chatham, Eaton, Hart's Location and Jackson show "-" for 2025-26 and Bartlett $64,547.97. The reports do not explain the amounts. Final 2025-26 and any 2026-27 figures were not reachable (see Not retrieved). 2024-25 file: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/uniform-document-for-first-final-allocation-postings_title-i-part-a.pdf. Raw copies: raw/daily/title1/t1a-final-2024-25.pdf, .txt; t1a-prelim-2025-26.pdf, .txt; nhdoe-title-i-part-a-page-wayback-2025-08-31.txt
4. NH DOE's Title I transfer process (April 2024) lets a district with no schools ask to move its Title I allocation to the district its students attend, using a signed agreement between the two districts. No Albany transfer request was found, and Albany's 2026-27 proposed budget lists IDEA (special education, $31,000) as its only federal grant.
   - citation: NH DOE, "ESEA Title I, Part A Allocation Transfer Among LEAs Request Process and Form" (April 8, 2024); Albany School District 2026-2027 Proposed Budget (2026 Annual Report), "Federal Grants"
   - source: https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/title-ia-allocation-transfer-request-final_.pdf
   - as_of: Wayback snapshot 2025-02-21
   - review_by: 2027-11-13
   - place: district Albany
   - note: Form text: "Per ESEA Section 1126(b) allocations among local educational agencies (LEAs), may be transferred among LEAs that receive Title I, Part A funds ... if a LEA provides free public education for children who reside in the school district of another LEA" and the example "LEA A (transferring LEA) received 2023-2024 Title I, Part A funding, however, LEA A has no schools, therefore all students attend LEA B (receiving LEA)". Budget page (read from the rotated image): "FEDERAL GRANTS / IDEA $31,000" in each column (FY25 adopted, FY25 actual, FY26, FY27 proposed). Statement of absence: searched Albany minutes from September 2022 to September 2026 for "Title". Raw copies: raw/daily/title1/t1a-transfer-request.pdf, .txt; raw/daily/albany/albany-annual-report-2026.pdf, -p6-budget.png

## district-preschool: Public Preschool, Child Find and Preschool Special Education for Albany and Conway

- kind: local
- question_type: local_practice
- description: Whether each district runs a preschool program, where, and any posted tuition.

1. The Conway School District runs no public preschool. On August 24, 2026 its board voted 5-1-0 to have a group keep studying the need for one and where it would be offered; the member who voted no spoke against public preschool as a burden on taxpayers.
   - citation: Conway School Board minutes, August 24, 2026 (amended), item 13.a.v (John Fuller Ad Hoc Committee report)
   - source: https://drive.google.com/file/d/1kz1OvzV0GaV1zk6OObfPtIQLsX7klagk/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Hodge said a committee has been formed to examine the use of the facilities for preschool. Burke asked the Board to issue a directive to conduct a feasibility study regarding the need for preschool, and where it would be offered. ... Hodge recommended speaking with Madison and Bartlett about their programs, and spoke in support of offering preschool. Mosca spoke against offering public preschool, as it puts a burden on taxpayers. Motion was made by Sarah Burke and seconded by Megan Beckwith to direct the group to continue a feasibility study. ... The vote was 5-1-0 [Mosca]." The Pine Tree, Conway Intermediate and SAU 9 pages describe no preschool. This fills the "Preschool: not found" entry for Conway in additional-data/district-practices.md. Albany runs no schools. Bartlett's JBES pre-K is for Bartlett (Bartlett file jbes.md, district-preschool). Raw copy: raw/daily/conway/conway-sb-minutes-2026-08-24-amended.txt (copied from town/Conway/raw/daily/minutes/)
2. In July 2026, a Conway John Fuller Ad Hoc Committee group working with SAU 9's student services director sketched a combined pre-kindergarten, special education and child care program that would need a warrant article. Ideally it would run Monday to Friday year-round, possibly until 9 or 10 p.m. The group said two local daycares or pre-K programs were slated to close soon.
   - citation: Conway John Fuller Ad Hoc Committee minutes, July 29, 2026, item c ("Pre-K/Special Education/Childcare")
   - source: https://drive.google.com/file/d/1dfXNdPoc4WL0AB-y_YmSHx68xl6vkdFw/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The team determined that ideally, the childcare would be open M-F, year-round, possibly open until 9 p.m. or 10 p.m., and would include childcare and pre-kindergarten, and that this aligns with needs. This option would not be able to operate as a stand-alone within the John Fuller facility. Sarah Burke said it would need to be a warrant article. ... There are two daycares/pre-k in the area that are slated to close soon. This option is viable, needs-based, but would not generate income ... The survey that was conducted indicated childcare as a need." The superintendent noted "a feasibility study conducted many years ago". In public comment a speaker objected that the project "will put area preschools and daycares out of business." No decision had been made by November 2026. Raw copies: raw/daily/conway/john-fuller-committee-2026-07-29.pdf, .txt (copied from town/Conway/raw/money/fuller/)
3. At a March 2025 Conway School Board meeting, a speaker for the Mount Washington Valley Directors Network said 14 local early childhood directors had signed a letter about the idea of a district preschool. They argued that pulling every child with an IEP into one program would end inclusive private classrooms, and that three or four public preschool classrooms would close many centers and their infant and toddler care.
   - citation: Conway School Board minutes, March 31, 2025, public comment
   - source: https://drive.google.com/file/d/1AUnDgxSrJ0aE-WZvOSWpLlvDpmDk0xvB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "14 members have signed a letter ... If you take every child who has an IEP in the school district and pull them into one program it would rob our programs of that diversity. ... If there were 3 or 4 classrooms of pre-school then many of their centers will close. ... every single one of the 14 people who are signing this letter say that we wouldn't be able to run an infant/toddler program without doubling our tuition. ... We really would love to be part of that conversation." Bears on P17.1, since it records how local preschools and the district relate. The letter itself was not found. Raw copy: raw/daily/conway/conway-sb-minutes-2025-03-31.txt (copied from town/Conway/raw/daily/minutes/)
4. SAU 9's special education manual says its member districts, Albany included, must find, locate and evaluate every resident child with a possible disability from age 2.5 to 22 ("child find"). It also says they join transition meetings so a plan is in place by a child's third birthday, contact community agencies every year, and post notices at libraries, medical offices and schools.
   - citation: SAU 9 Special Education Procedures Manual (2026), "Child Find Procedure"
   - source: https://files.smartsites.parentsquare.com/10271/sau_9_special_education_procedures_manual_2026.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Text: "The SAU 9 member school districts (The District) ensure that all children who have disabilities, from 2.5 years of age to age 22 years, who reside in The Districts, and who are in need of special education and related services are identified, located and evaluated." "For those students who are transitioning from Early Supports and Services to preschool, the District will participate in a transition planning meeting ... by the child's third birthday." "At least on an annual basis, the District publicizes and disseminates information, which describes its Child Find Program through notices at public libraries, at medical providers offices and public schools." Referral reasons include "Inability to progress or participate in developmentally appropriate preschool activities". A first meeting on a referral is held within 15 business days. Contacts: SAU 9 Student Services, 603-447-8951. Statewide rules: library early-supports-to-preschool-special-ed. Raw copies: raw/daily/sau9/sped-manual-2026.pdf, .txt; raw/daily/sau9/sau9-student-services.txt
5. SAU 9's manual says children with disabilities ages 3 to 5 receive special education "through the District's preschool programs and services." Settings include a regular early childhood program with at least 50% nondisabled children, the child's home, a service provider's location or a special education classroom of no more than 12 preschoolers.
   - citation: SAU 9 Special Education Procedures Manual (2026), "Preschool Programs 1111.03(c)"
   - source: https://files.smartsites.parentsquare.com/10271/sau_9_special_education_procedures_manual_2026.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 9
   - note: Text: "Children with disabilities shall be provided with appropriate special education and related services through the District's preschool programs and services. The maximum number of preschool children in an early childhood special education program shall be 12". Settings listed: "Early Childhood Program: a preschool child with a disability attends an early childhood program that includes at least 50% nondisabled children", "Home", "Early Childhood Special Education Program", "Service Provider Location", "Separate School", "Residential Facility". This is not a general public preschool. Raw copy: raw/daily/sau9/sped-manual-2026.txt
6. Albany's K–6 tuition contract with Conway covers grades K through 6 and does not mention preschool.
   - citation: Albany/Conway Tuition Agreement, Grades K-6 (April 20, 2025)
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Statement of absence; OCR text searched for "preschool", "pre-school" and "pre-k". Text: "Albany School District is desirous of having its pupils, grades K through 6 attend school in Conway". Raw copy: raw/daily/albany/contracts/sau9-contract-k-6-albany-conway-current.ocr.txt

## district-student-support: Supplies, Counseling and Moving Between Towns

- kind: local
- question_type: local_practice
- description: Counseling, social work and mental health support, English learner services, homeless student support, welcoming families of all backgrounds, and enrollment documents

1. In December 2024 SAU 9's superintendent told the Conway School Board that the elementary, middle and high schools each keep a space with supplies any child can use, including snacks, deodorant, socks, boots, hats, mittens, gloves, coats and clothing. Staff said they find children in need and provide what they can, and that one or two organizations donate new coats almost every year.
   - citation: Conway School Board minutes, December 23, 2024 (dress code discussion)
   - source: https://drive.google.com/file/d/1Pvw-Vp5mGAL6oWpgCicV8VeWWX2hHrB5/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "Frechette responded that at the elementary level we do have kids who do not have proper outdoor clothing and we do supply it as best we are able. Carpenter responded that we identify if there are kids in need and we try to provide it. A comment from Stimpson indicated that almost annually one or two organizations drop off brand new coats for preschool through high school aged students and we make sure they get distributed. A comment from Frechette indicated that at the elementary, middle school and high school there are spaces designated for supplies that any kids need to access: snacks, deodorant, change of socks, extra boots, hats, mittens, gloves, coats and clothing." Pine Tree's handbook asks families needing winter clothing to contact the Family Support Liaison, who works confidentially (Conway file schools-k-8.md, district-student-support 7). Raw copy: raw/daily/conway/conway-sb-minutes-2024-12-23.txt (copied from town/Conway/raw/daily/minutes/)
2. Kennett Middle School's 2026-27 handbook offers a school counselor for personal and group counseling, crisis counseling and referrals, with parent appointments by phone. No Conway school handbook or the KMS home page mentions military-connected or veteran families, and no SAU 9 school was found among New Hampshire's Purple Star schools.
   - citation: A. Crosby Kennett Middle School Handbook 2026-2027, "School Counseling Services"; Pine Tree, Conway Intermediate and Kennett High handbooks 2026-2027; Kennett Middle School home page
   - source: https://files.smartsites.parentsquare.com/10271/student_handbook_2026-2027.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Handbook: "The school counseling program offers a counselor who is here to help you with such services as ongoing personal and group counseling, crisis counseling, scheduling, referral process for special needs, and coordination of appropriate programming for students. Parents/guardians can feel free to make appointments with the School Counselor by calling the school during school hours." Statement of absence: searched the four handbooks and kms.sau9.org for "military", "veteran", "deploy" and "Purple"; the only matches are Kennett High's military recruiter and military-service information. NH DOE's 2021 Purple Star announcement named schools in other towns, and no current list was found (library military-families-nh 5). The interstate compact covers active-duty families, not veterans (library military-children-compact 1–2). Raw copies: raw/daily/conway/kms-handbook-2026-27.txt; ptps-handbook-2026-27.clean.txt; cis-handbook-2026-27.txt; raw/daily/sau9/kms-home.txt
3. **Derived:** a family moving between Albany and Conway keeps its child in the same school, because Albany's K–6 students attend Conway's schools on Conway's terms and Conway places each grade band in one school (Pine Tree K–2, Conway Intermediate 3–5, Kennett Middle 6–8). A move to Bartlett makes Bartlett the district of residence, and Bartlett's school is Josiah Bartlett Elementary (preschool to grade 8), unless the homeless-student rules let the child stay in the school of origin.
   - citation: Albany/Conway Tuition Agreement, Grades K-6 (2025); Conway file schools-k-8.md, district-consolidation-history 1; RSA 193:12, II(a); 42 U.S.C. 11432(g)(3)(A)
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: Combines the contract ("Conway shall accept said pupils ... on the same terms and conditions ... as is the case with pupils residing in the Town of Conway"), Conway's grade regrouping, and RSA 193:12, II(a) ("In the case of a minor, legal residence is where his or her parents reside"). The bus does change: Albany families ride Eldridge's bus, while Conway families ride Conway's district buses. JBES is described in the Bartlett files. When a move is caused by loss of housing, see homeless-student-school-stability below. Raw copies: raw/daily/albany/contracts/sau9-contract-k-6-albany-conway-current.ocr.txt; raw/daily/rules/rsa-193-12.txt
## district-fees: Field Trips, Supplies and Other Costs at Albany Students' Schools

- kind: local
- question_type: local_practice
- description: Costs families may pay: sports, field trips, supplies, technology, instruments and other fees, and help with them

1. Albany's K–6 contract counts "student activities cost (i.e. - field trips, athletic transportation)" among the Conway elementary expenses that set the yearly tuition Albany pays, and the 9–12 contract uses the same wording.
   - citation: Albany/Conway Tuition Agreement, Grades K-6 (April 20, 2025), section IX.A.1; Grades 9-12 (2003), computation of student charges
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Albany
   - note: OCR text: "Actual expenses shall refer to elementary Conway School K-6 General Fund expenses as reported in the DOE-25 ... plus student activities cost (i.e. - field trips, athletic transportation) less revenue from co-curricular, transportation, special education ...". This is how tuition is computed. It does not say whether families are also asked to pay toward a trip. Conway's field trip policy IICA asks teachers for any "Amount paid by students" and how "scholarship needs are being addressed" (Jackson file, district-fees 12–13 in `Jackson/policies-safety-meals-and-support.md`). Raw copies: raw/daily/albany/contracts/sau9-contract-k-6-albany-conway-current.ocr.txt; sau9-contract-9-12-albany-conway-current.ocr.txt
2. No school supply list or fee schedule is posted on the Pine Tree, Conway Intermediate or Kennett Middle home pages or in their 2026-27 handbooks. Kennett Middle's handbook requires a signed consent form for field trips, mentions no trip fee, and makes students pay for lost or damaged school property, including Chromebook repairs beyond normal wear.
   - citation: Pine Tree, Conway Intermediate and Kennett Middle 2026-27 handbooks and home pages; A. Crosby Kennett Middle School Handbook 2026-2027, "Field Trips" and "School Property"
   - source: https://files.smartsites.parentsquare.com/10271/student_handbook_2026-2027.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Statement of absence for supply lists: searched for "suppl", "fee" and "cost". KMS text: "You must submit a signed parental consent form prior to participating in any field trip experience." "If your school property is damaged or lost you must pay for repairs or a replacement. Computer repairs outside of normal wear and tear will be made and charged before being returned to the student. These types of repair include but are not limited to screen breakage or damage, key breakage, case breakage, drops, and hinge breakage." KMS Chromebooks stay at school (Conway file daily-life.md, district-technology-and-phones 2). Kennett High's costs are in the Jackson file (district-fees 10–11 in `Jackson/policies-safety-meals-and-support.md`). Raw copies: raw/daily/conway/kms-handbook-2026-27.txt; ptps-handbook-2026-27.clean.txt; cis-handbook-2026-27.txt; raw/daily/sau9/ptps-home.txt; cis-home.txt; kms-home.txt
3. At Kennett Middle School, adding money to a meal account by debit or credit card through EZSchoolPay costs $2.50 per deposit; cash or check deposits are free, and a returned check costs $25.
   - citation: A. Crosby Kennett Middle School Handbook 2026-2027, meal account section
   - source: https://files.smartsites.parentsquare.com/10271/student_handbook_2026-2027.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Conway
   - note: Text: "The Conway School District utilizes EZSchoolpay.com for electronic payments. ... There is a fee of $2.50 per deposit for adding funds using a debit or credit card. There will be no processing fee for deposits made to a student meal account made by cash or check. A fee of $25.00 will be charged to the parents for each check returned for insufficient funds." Meal prices are in the Conway file (daily-life.md, district-meals 1). SAU 9's food page noted on November 13, 2026 that EZ School Pay had login problems from October 26, 2026 (raw/daily/sau9/sau9-food-services.txt). Raw copy: raw/daily/conway/kms-handbook-2026-27.txt

## town-family-help: Weekend Food for Children at the Schools Albany Students Attend

- kind: local
- question_type: help
- description: Local programs and funds that help families with costs

1. End 68 Hours of Hunger's Conway page lists weekend food deliveries to Pine Tree, Conway Elementary (now Conway Intermediate) and other valley schools, with food closets at Kennett Middle and Kennett High and a program email (Conway@end68hoursofhunger.org). The undated page still lists John Fuller School, which closed in 2024, and does not say how a family signs up.
   - citation: End 68 Hours of Hunger, "Conway" community page
   - source: https://www.end68hoursofhunger.org/find-your-community/new-hampshire/conway/
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: town Conway
   - note: Page text: "The schools we are delivering to are: Children Unlimited, Conway Elementary, Conway Head Start, Freedom Elementary, Jackson Grammar, John Fuller, Josiah Bartlett School, Madison Elementary, Northeast Woodlands Charter School, Pine Tree, and Robert Frost Charter School / Food Closets: Kennett Middle School and Kennett High School". Drop-off sites for donations include Conway Elementary, Pine Tree School and Memorial Hospital. The page lists program coordinators; one is listed at "Conway Elementary School, 160 Main Street." Statement of absence for a sign-up process: the page, SAU 9's pages and the 2026-27 handbooks were searched. In February 2025 the program said it filled 180 bags a week, one per student, and older students use the food closets to avoid being seen with bags (Conway file daily-life.md, town-family-help 1). Raw copies: raw/daily/help/e68-conway.html, .txt

## homeless-student-school-stability: Homeless Students: Staying in the School of Origin and Transportation Between Districts

- kind: rule
- question_type: rules
- description: Federal and New Hampshire rules for homeless children and youth: who counts as homeless, staying in the school of origin, immediate enrollment, and transportation when a family moves between districts

1. Under New Hampshire law, "homeless children and youths" lack a fixed, regular and adequate nighttime residence, including children sharing others' housing because of loss of housing or economic hardship, children living in motels, hotels, trailer parks or campgrounds for lack of adequate alternatives, children in shelters, and children living in cars, parks or similar settings.
   - citation: RSA 193:12, IV
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The term "homeless children and youths" means individuals who lack a fixed, regular, and adequate nighttime residence, and shall include the following: (a) Children and youths who are sharing the housing of other persons due to loss of housing, economic hardship, or a similar reason; are living in motels, hotels, trailer parks, or camping grounds due to the lack of alternative adequate accommodations; are living in emergency or transitional shelters; are abandoned in hospitals ... (c) Children and youths who are living in cars, parks, public spaces, abandoned buildings, substandard housing, bus or train stations, or similar settings." The law does not mention seasonal leases. Whether a family moving between leases qualifies depends on these facts, and the district's homeless liaison makes the first decision (Conway file community-and-choice.md, district-student-support 1–2). Raw copy: raw/daily/rules/rsa-193-12.txt
2. Under the federal McKinney-Vento Act, the district must, based on the child's best interest, keep a homeless child in the school of origin for as long as the child is homeless, and for the rest of the school year if the family finds permanent housing during the year. It may instead enroll the child in the school that children living where the family now lives attend, and staying in the school of origin is presumed to be in the child's best interest unless the parent asks otherwise.
   - citation: 42 U.S.C. 11432(g)(3)(A)–(B)
   - source: https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap119-subchapVI-partB-sec11432.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "(i) continue the child's or youth's education in the school of origin for the duration of homelessness— (I) in any case in which a family becomes homeless between academic years or during an academic year; and (II) for the remainder of the academic year, if the child or youth becomes permanently housed during an academic year; or (ii) enroll the child or youth in any public school that nonhomeless students who live in the attendance area in which the child or youth is actually living are eligible to attend." Best interest: "presume that keeping the child or youth in the school of origin is in the child's or youth's best interest, except when doing so is contrary to the request of the child's or youth's parent or guardian". Raw copy: raw/daily/rules/usc-42-11432.txt
3. Under the same law, the "school of origin" is the school the child attended when permanently housed or last enrolled in, including a preschool, and when the child finishes that school's last grade it includes the next school in the usual feeder pattern.
   - citation: 42 U.S.C. 11432(g)(3)(I)
   - source: https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap119-subchapVI-partB-sec11432.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The term "school of origin" means the school that a child or youth attended when permanently housed or the school in which the child or youth was last enrolled, including a preschool." and "When the child or youth completes the final grade level served by the school of origin ... the term "school of origin" shall include the designated receiving school at the next grade level for all feeder schools." For an Albany child, that would be Conway's next school in the K–2, 3–5, 6–8 sequence. Raw copy: raw/daily/rules/usc-42-11432.txt
4. Federal law requires transportation to the school of origin when the parent asks. If the child still lives in the area of the district where that school is, that district provides it. If the child now lives in another district, the two districts agree on how to split the duty and cost, and if they cannot agree, they share it equally.
   - citation: 42 U.S.C. 11432(g)(1)(J)(iii)
   - source: https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap119-subchapVI-partB-sec11432.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "(I) If the child or youth continues to live in the area served by the local educational agency in which the school of origin is located, the child's or youth's transportation to and from the school of origin shall be provided or arranged by the local educational agency in which the school of origin is located. (II) If the child's or youth's living arrangements in the area served by the local educational agency of origin terminate and the child or youth, though continuing the child's or youth's education in the school of origin, begins living in an area served by another local educational agency, the local educational agency of origin and the local educational agency in which the child or youth is living shall agree upon a method to apportion the responsibility and costs ... If the local educational agencies are unable to agree upon such method, the responsibility and costs for transportation shall be shared equally." The law does not address a district like Albany that runs no schools and sends its students to another district under contract; no SAU 9 or Albany document says how this is handled (Albany has no homeless-student policy posted; district-transportation 15). Raw copy: raw/daily/rules/usc-42-11432.txt
5. Under federal law, the chosen school must enroll a homeless child immediately, even without records normally required, such as school or immunization records or proof of residency, and must immediately ask the last school for the child's records.
   - citation: 42 U.S.C. 11432(g)(3)(C)
   - source: https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap119-subchapVI-partB-sec11432.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "The school selected in accordance with this paragraph shall immediately enroll the homeless child or youth, even if the child or youth— (I) is unable to produce records normally required for enrollment, such as previous academic records, records of immunization and other required health records, proof of residency, or other documentation; or (II) has missed application or enrollment deadlines during any period of homelessness." and "The enrolling school shall immediately contact the school last attended". Conway's JFABD restates this (Conway file community-and-choice.md, district-student-support 1). Raw copy: raw/daily/rules/usc-42-11432.txt
6. Under New Hampshire law, when districts dispute a student's residency, the student stays in the school of origin until the dispute is decided, and the education commissioner decides within 30 days (14 if schooling would be interrupted). The law does not require a district to transport a student beyond its own boundaries.
   - citation: RSA 193:12, VI(a)–(b) and VII
   - source: https://gc.nh.gov/rsa/html/XV/193/193-12.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "A pupil shall remain in attendance in the pupil's school of origin during the pendency of a determination of residency. ... "school of origin" means the school the child attended when permanently housed or the school in which the child was last enrolled." "the commissioner of the department of education, or designee, shall make a determination within 30 days of notice of the residency dispute ... the determination shall be made within 14 days." VII: "Nothing in this section shall require a district to provide transportation for a student beyond the geographical limits of that district." Paragraph VI(a) excludes homeless children from the commissioner's residency decisions. Raw copy: raw/daily/rules/rsa-193-12.txt

## dyslexia-screening-and-intervention: Screening Young Students for Dyslexia and Reading Risk

- kind: rule
- question_type: rules
- description: New Hampshire's law on screening students in kindergarten through grade 3 for dyslexia and related reading difficulties, its timelines, follow-up assessment, interventions and what parents are told (RSA 200:58–62)

1. New Hampshire law requires every public and chartered public school to screen each student entering kindergarten through grade 3, English learners included, with an evidence-based screener for signs of dyslexia and related disorders within 60 school days of entry. The screening is repeated once more that year and at least twice a year through grade 3.
   - citation: RSA 200:59, I
   - source: https://gc.nh.gov/rsa/html/XV/200/200-59.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "School districts shall screen all public school and chartered public school students, including English learners, using an evidence-based screener for the identification of potential indicators or risk factors of dyslexia and related disorders upon entry to public school. The initial screening shall be completed no later than 60 school days of a student entering public school in kindergarten through third grade. The screening shall be repeated one additional time during the current school year, and repeated at a minimum of twice yearly through third grade to monitor progress." Source: 2016, 262:1; 2023, 151:1. Conway reports using Acadience and fluency measures (Conway file schools-k-8.md, district-curriculum-and-assessment 6). This is a reading screen after school entry, not a readiness test before kindergarten. Raw copy: raw/daily/rules/rsa-200-59.txt
2. If a screening shows a student below benchmarks, the school must do a second assessment within 30 days, tell the parents the results, and start interventions by January 1 for a student showing risk factors. Parents may submit an independent evaluation at their own cost.
   - citation: RSA 200:59, I-a, II, III and IV
   - source: https://gc.nh.gov/rsa/html/XV/200/200-59.htm
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - note: Text: "the school must complete a secondary assessment within 30 days to determine whether the school shall provide such student with modified, differentiated, or supplementary evidence-based reading instruction intervention or refer the student to special education for further evaluation. The school shall inform the student's parent or legal guardian of the screening results." "During this time general education accommodations shall be initiated within 21 days of the initial screening". II: "intervention strategies to begin by the January 1 of the school year". IV: "A parent or legal guardian who submits an independent evaluation shall assume all fiscal responsibility for that independent evaluation." Raw copy: raw/daily/rules/rsa-200-59.txt

## albany_transport_scheduled_ride_minutes_2026_27: Scheduled Bus Ride Times for Albany Students, 2026-27 (minutes, derived)

- unit: number (minutes)
- period: 2026-27 school year route sheet (updated 8/11/2026); year: 2027
- source: Albany School District Bus Route 2026-2027 (KHS/KMS, Elementary Schools, Return runs), linked from SAU 9's Transportation page — https://files.smartsites.parentsquare.com/10271/albany26-27.pdf; Conway West Side sheet (Larry) — https://files.smartsites.parentsquare.com/10271/larry_day_-_west_side_road.pdf
- as_of: 2026-11-13
- raw: raw/daily/routes/albany26-27-p1.png to -p4.png (read from the images), albany26-27.txt; raw/daily/conway/route-larry_day_-_west_side_road-p1.png
- note: **Derived**: scheduled arrival time minus the scheduled time at the boarding stop. The afternoon rows count from the dismissal times in the 2026-27 Kennett Middle (2:10 p.m. for bus riders) and Conway Intermediate (3:15–3:30 p.m.) handbooks, because the Albany sheet prints no departure times; they include any waiting at school. These are scheduled, not measured, times with no weather delays, and not every stop is listed. Place is Albany (district and town id 5) except the last two rows, which are Conway's West Side route (id 113). KHS = Kennett High; KMS = Kennett Middle; CIS = Conway Intermediate (printed "Conway Elementary School" on the Albany sheet).

| Place | Trip | Value | Note |
|---|---|---|---|
| Albany | To KHS, AM: Madison/Albany town line (6:25) to KHS (7:15) | 50 | First stop |
| Albany | To KMS, AM: Madison/Albany town line (6:25) to KMS (7:25) | 60 | Longest middle school ride; KMS starts 7:35 |
| Albany | To KMS, AM: 2020 Chocorua Mtn. Hwy (6:27) to KMS (7:25) | 58 | |
| Albany | To KMS, AM: Nickerson Road "Bus Hut" (6:30) to KMS (7:25) | 55 | Time cut off on the page image; text layer reads 6:30 |
| Albany | To KMS, AM: Priscilla Road (6:35) to KMS (7:25) | 50 | |
| Albany | To KMS, AM: Bald Hill Road and Cook Farm Road (6:40) to KMS (7:25) | 45 | |
| Albany | To KMS, AM: 1297 Chocorua Mtn. Hwy, Albany Auto (6:44) to KMS (7:25) | 41 | |
| Albany | To KHS, AM: Brookside Ave and Chocorua Mtn. Hwy (6:46) to KHS (7:15) | 29 | Last morning stop |
| Albany | To KMS, AM: Brookside Ave and Chocorua Mtn. Hwy (6:46) to KMS (7:25) | 39 | Shortest middle school ride |
| Albany | To CIS, AM: Wildwood Road / Tabor Circle (8:03) to CIS (8:50) | 47 | First elementary stop; CIS starts 8:50 |
| Albany | To Pine Tree, AM: Wildwood Road / Tabor Circle (8:03) to Pine Tree (9:00) | 57 | Longest elementary ride; Pine Tree starts 9:00 |
| Albany | To Pine Tree, AM: 2192 Chocorua Mtn. Hwy (8:10) to Pine Tree (9:00) | 50 | |
| Albany | To Pine Tree, AM: Priscilla Road (8:15) to Pine Tree (9:00) | 45 | |
| Albany | To Pine Tree, AM: 426 Drake Hill Road (8:22) to Pine Tree (9:00) | 38 | |
| Albany | To CIS, AM: Bald Hill Road and Cook Farm Road (8:30) to CIS (8:50) | 20 | |
| Albany | To Pine Tree, AM: Bald Hill Road and Cook Farm Road (8:30) to Pine Tree (9:00) | 30 | |
| Albany | To CIS, AM: Bald Hill Road (8:38) to CIS (8:50) | 12 | Last elementary stop |
| Albany | To Pine Tree, AM: Bald Hill Road (8:38) to Pine Tree (9:00) | 22 | |
| Albany | From KMS, PM: bus dismissal (2:10) to Albany Auto (2:40) | 30 | First afternoon stop; no school departure time printed |
| Albany | From KMS, PM: bus dismissal (2:10) to Bald Hill Road and Stacy Lane (3:10) | 60 | Last stop; bus then goes to the elementary schools |
| Albany | From CIS, PM: start of dismissal (3:15) to Bald Hill Road (3:55) | 40 | First timed elementary stop |
| Albany | From CIS, PM: end of dismissal (3:30) to 426 Drake Hill Road (4:20) | 50 | Last stop |
| Albany | From CIS, PM: start of dismissal (3:15) to 426 Drake Hill Road (4:20) | 65 | Longest afternoon span |
| Conway | To KHS, AM, West Side (Larry): Passaconaway Road (6:48) to KHS (7:06) | 18 | Location of the stop on Passaconaway Road not stated |
| Conway | To KMS, AM, West Side (Larry): Passaconaway Road (6:48) to KMS (7:20) | 32 | |

## For another file

- **Money agent (agent 3):**
  - Albany's pupil transportation lines (2026 annual report, budget p. 2, read from the rotated image raw/daily/albany/albany-annual-report-2026-p6-budget.png): Transportation, Regular: FY25 adopted $114,215, FY25 actual $120,113, FY26 adopted $128,150, FY27 proposed $134,435 (+$6,285, 4.90%). Transportation, Special Ed: FY25 $100 (actual $0), FY26 $39,000, FY27 $100. Total 2720: $134,535 for FY27, down $32,615 (19.51%). Federal grants: IDEA $31,000 in every column. In February 2026 the business administrator said special education transportation was reduced "as the need is less and some of it is offset by special education grant funding" (raw/daily/albany/minutes/Albany-School-Board-Minutes-26-2-February-10-2026.txt).
  - Budget status at the November 10, 2026 board meeting: transportation appropriation $134,535, expended $12,702.08, encumbered $126,054.60, balance ($4,221.68), (3.13)% (raw/daily/albany/minutes/Albany-School-Board-Agenda-26-11-November-10-2026.txt).
  - Eldridge 2026–2031 contract per-mile rates: $6.98 (2026-27), $7.68, $8.29, $8.80, $9.54 (2030-31). In December 2025 the business administrator put the increase over five years at "approximately $63,000," and a board member called the 11% increase "pretty standard". The district pays fuel above $5.00 a gallon on receipts (clause first granted September 13, 2022, 3-0). Eldridge raised fuel prices with the board in April 2026, and the board chose to wait a month (raw/daily/albany/minutes/, December 9, 2025; September 13, 2022; April 14, 2026).
  - Conway picks up Albany's Passaconaway Road students "at a cost of approximately $4,200" (February 13, 2024 minutes).
  - The December 2025 minutes report 2025-26 special education tuition overspent by $85,988, a likely deficit, a new $50,000 tuition trust fund article and a $30,000 special education reserve article. The March 11, 2025 annual meeting approved the eight-year K–6 agreement with Conway (2026 annual report, OCR raw/daily/albany/albany-annual-report-2026.ocr.txt), which bears on the "8-year K–6 contract" premise.
  - Title I allocations (district-curriculum-and-assessment 3–4) and the free or reduced-price counts in the site's adequacy aid data bear on P11.1, since NH DOE's adequacy formula uses "EV per F&R pupil": Albany's FY2027 equalized valuation per F&R pupil is 7,323,193.88, above the $7.003 million cutoff, so its extraordinary need aid per F&R ADM is 0 (additional-data/raw/town/adequacy-aid.csv).
- **Programs agent (agent 1):** the K–6 contract (section VIII) promises "A written quarterly report ... to the Albany School Board concerning achievement and attendance records of all pupils from the Albany School District who are enrolled in the elementary schools of the Conway School District" and individual student information on request. This bears on P4.3 (raw/daily/albany/contracts/sau9-contract-k-6-albany-conway-current.ocr.txt).
- **Community agent (agent 4):** Conway's July 2026 child care survey and the plan for evening child care with pre-K (district-preschool 2); the Mount Washington Valley Directors Network's 2025 letter (district-preschool 3); End 68 Hours of Hunger's Conway page (town-family-help 1); the Passaconaway hamlet's distance from Kennett (district-transportation 11).
- **Gap fills and corrections for earlier files:**
  - `additional-data/district-practices.md` coverage lists Conway "Preschool: not found." Conway runs no public preschool and was still studying one in August 2026 (this file, district-preschool 1).
  - `town/Conway/daily-life.md`, district-transportation 2, says Albany's students ride Eldridge's route. Albany's Passaconaway Road students are picked up by Conway under an agreement (this file, district-transportation 8), and Eldridge's contract was renewed for 2026–2031 (fact 2).
  - `town/Conway/schools-k-8.md`, district-curriculum-and-assessment 1, cites the handbook for schoolwide Title I. NH DOE's 2024-25 list confirms both elementary schools as "SWP" and shows Kennett Middle and Kennett High are not Title I schools (this file, district-curriculum-and-assessment 1).
  - `town/Conway/community-and-choice.md`, town-family-help, and `daily-life.md`, town-family-help 1: End 68 Hours of Hunger's own Conway page still lists John Fuller and "Conway Elementary" (this file, town-family-help 1).

## Not retrieved

- How the Passaconaway Road students are picked up in 2025-26 and 2026-27: the February 13, 2024 minutes describe the agreement, but later Albany minutes (through September 8, 2026) and the Conway sheets do not say which stop serves them.
- Any bus service, or family arrangement, for the Kancamagus/Passaconaway area of Albany: not in any route sheet or Albany minutes (September 2022 to September 2026; earlier minutes from 2010–2022 were not searched).
- Winter status of the Kancamagus Highway and Bear Notch Road: the White Mountain National Forest page (https://www.fs.usda.gov/recarea/whitemountain/recarea/?recid=74977) redirected to a general recreation page and was not followed. A web search returned only travel sites and news, which were not used. NHDOT pages were not checked.
- Measured (not scheduled) ride times, winter delays or late arrivals on Albany's bus: no reports in Albany minutes.
- A time limit for adding or moving a bus stop after a move: not in the Eldridge contract, the SAU 9 page or Conway policy EEA. Eldridge was not contacted.
- NH DOE's final 2025-26 and any 2026-27 Title I allocations and Title I school list: NH DOE returns 403 to automated requests. The Wayback snapshot of the Title I page (August 31, 2025) has only the 2025-26 preliminary report and the 2024-25 school list.
- Whether Albany has ever transferred its Title I allocation to Conway: no request or agreement found in Albany minutes or posted documents.
- A kindergarten readiness screening tool or any document on aligning SAU 9 screening with local preschools: none on the SAU 9, Pine Tree or Project SUCCEED pages, the Pine Tree handbook (which lists only nurse vision and hearing screening), or the Conway and Albany minutes searched. The Directors Network letter of March 2025 was not found.
- A confidential sign-up process for End 68 Hours of Hunger bags in SAU 9: not on the program's Conway page, SAU 9's pages or the 2026-27 handbooks.
- A current list of New Hampshire Purple Star schools: none on NH DOE pages found by search; only the 2021 announcement (library).
- Whether Albany children are enrolled in Project SUCCEED, and Project SUCCEED fees: not published (Conway file Not retrieved).
- The Albany School Board's 2026-27 minutes beyond the September 8, 2026 draft: none posted on November 13, 2026.
- **Spot checks (November 13, 2026):** re-read against raw copies: (1) Albany KHS/KMS run 6:25 first stop, 7:25 Kennett Middle (raw/daily/routes/albany26-27-p1.png, -p2.png): matches. (2) Eldridge contract term "July 1, 2026 to June 30, 2031" and the 3-0-0 vote (raw/daily/albany/minutes/Albany-School-Board-Minutes-12-December-9-2025-with-Attachment.ocr.txt): matches. (3) NH DOE 2025-26 preliminary "Albany 113.99 170.99 284.98" (raw/daily/title1/t1a-prelim-2025-26.txt): matches. (4) "does not include the Passaconaway Road portion of Albany" (raw/daily/albany/minutes/Albany-School-Board-Minutes-24-2-February-13-2024.txt): matches.
- **Personal information:** none was sent to any outside service. Nominatim and OSRM were called with the generic identifier nhfacts-research (webmaster@nhfacts.com). Other sites (SAU 9, Google Drive, ParentSquare files, projectsucceed.com, end68hoursofhunger.org, govinfo.gov, gc.nh.gov, the Wayback Machine) were fetched with a generic browser user agent or the generic nhfacts-research identifier, with no form submissions.
