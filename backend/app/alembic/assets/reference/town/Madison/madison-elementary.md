# Madison Elementary School: Classrooms, Programs, Support and Safety

Part of the Madison research (town/Madison). Gathered November 13, 2026.

## Summary

This file covers Madison Elementary School (MES), the Madison School District's only school (grades K–6), and the SAU 13 preschool it hosts: how classes are grouped and staffed, class sizes and enrollment, substitutes, curriculum, reading and math interventions, state test results against the state, enrichment and advanced learners, special education and related services (speech, occupational therapy, behavior analysts), the preschool's enrollment rules, counseling, English learners, weekend food bags, volunteers and community partners, and building security, emergency plans and drills.

- **9 topics, 109 facts and 2 number tables.** Raw copies are in `raw/school/` (about 64 MB, 121 files). Spot-checked against raw copies: the preschool's first-come, first-served rule, the June 2023 $60,000 security vote, the 0.80 FTE occupational therapy assistant vote, and the October 2025 IEP and 504 counts. A copy of the backend parser's rules finds no format problems apart from the `sau 13` places. Eight topics use shared slugs from `town/shared-topics.md`. One topic, `district-volunteers-and-partners`, is a **proposed new shared topic** (kind local, question type local_practice): "How residents, families and community groups can volunteer at, donate to or partner with a district's schools: volunteer rules and background checks, parent groups, gifts and community programs." No existing shared topic covers volunteers, gifts and partner organizations.
- **Places:** `district Madison` for the school and district; `sau 13` for policies adopted by all three SAU 13 boards ("Freedom, Madison & Tamworth School Board Policy"), the SAU 13 student services office and the SAU 13 preschool's rules. The current backend parser (`app/etl/reference.py`) accepts only `district` and `town` places, so the `sau 13` facts will be rejected until the loader supports them (the Bartlett file reported the same for `sau 9`).
- **Main sources:** the Madison School District Annual Report of January 2026 (with the fall 2025 "School Report Card") and of January 2024; Madison School Board packets and minutes from 2022 to November 2, 2026 on the SAU 13 site; the MES 2026-27 Family Handbook; the MES website (Google Sites) and its weekly newsletters; Madison's 2024-25 Title I plan; SAU 13 policies and forms; the SAU 13 preschool flyer for 2026-27; NH DOE's SAFE grant handout (December 2024); RSA 189:64; and the site's own database (read-only) for derived comparisons.
- **Main gaps:**
  - No written gifted program or accelerated math course for grades 5–6 appears in any source; policy IHBB is one sentence.
  - The number of preschool seats, and so the chance of getting a seat, is not published.
  - No public source names a school social worker after a 2022 Title IV contract, or an SRO.
  - The site-specific Emergency Operations Plan is not public (it was approved in non-public session), and no source says how often police or fire take part in drills.
  - NH DOE's 2026 (Round 4) SAFE grant list and the iPlatform profiles refused automated access.
  - No source names the Madison Boulder, Silver Lake's railroad era or the town's one-room schoolhouses as part of MES lessons.

**Premises checked**
- **"~11:1 student-teacher ratio":** about right only for 2024-25 if preschoolers are counted (129 students per 11.7 teacher FTE = 11.0, derived). Counting K–6 only, it was 9.4 in 2024-25 and 8.1 in 2025-26 (derived). Actual classes in fall 2026 held 12 to 18 students.
- **"Cohorts fluctuate between 11 and 26":** accurate for October 2024 (grade sizes 11 to 26). October 2025 ranged 10 to 27; fall 2026 ranges 11 to 17.
- **"~125 students" / "stable around 120–130":** out of date. K–6 enrollment was 130 (2021), 124 (2022), 114 (2023), 110 (2024), 102 (2025) and 90 in October 2026, plus 10 Madison preschoolers. A draft 2027 warrant article proposes a study of closing the school.
- **"Lottery odds" for the integrated Pre-K:** not a lottery. The 2026-27 flyer says applications were taken April 1–May 1 "on a first-come, first-served basis", with a waitlist. The program is integrated, as the question says.
- **"SAS scores trail the state average":** partly. Math trailed the state by 10 to 15 points every year 2022–2026; reading was within 6 points either way (above the state in 2023 and 2024, below in 2022, 2025 and 2026); grade 5 science was above the state in 2022, 2023 and 2026 (derived from the site's data).
- **"Speech and OT therapists stationed full-time" (P4.1):** the speech-language pathologist is a full-time Madison employee. Occupational therapy is a 0.80 FTE certified OT assistant (an employee from 2026-27, after years as a contractor) supervised by a contracted OT who splits time with Tamworth. SAU 13 does share special education administration.
- **"4th-grade NH history":** MES groups grades 3 and 4 in the same classrooms; New Hampshire history work (a Concord field trip, a Madison history lesson, the maple sugaring unit) is done by the grade 3–4 band.
- **"Share an SRO with Freedom and Tamworth":** no source shows an SRO at MES or in SAU 13. Madison Police teach DARE at MES.

## Persona questions

| Question | Answered by | Coverage | Notes |
|---|---|---|---|
| P1.1 How does the "~11:1" ratio translate to differentiated instruction when grades range 11 to 26? | district-classrooms-and-staff (facts 1–10); district-curriculum-and-assessment (facts 3–5, 7); madison_elementary_enrollment_by_grade; madison_elementary_staff_by_role; site data: class size, staff counts, enrollment | full | Multi-age bands (K–2, 3–4, 5–6), two classes per band, looping, flexible grouping, common planning, MTSS cycles. The ratio premise is checked above. The site's 2026 class-size figure for grades 1–2 (31.30) does not match the school's counts; see "For another file". |
| P2.1 Integrated Pre-K: eligibility, lottery odds, tuition | district-preschool (facts 1–8); existing district-practices.md fact 61 (dates, sessions, tuition) | full | First-come, first-served with a waitlist, not a lottery. Seat numbers aren't published, so odds can't be given. Tuition ($11.50 half day, $23.00 full day for non-identified children) is already in district-practices.md. |
| P2.2 Why MES SAS scores trail the state; reading and math interventions | district-curriculum-and-assessment (facts 1–12); district-student-support fact 11; site data: test scores; existing slug comparing-small-schools | partial | The site's data and the school's report card give results; interventions and programs are named. Sources list factors (54% of students with an "at-risk" factor, 25% with IEPs), but no source can show why scores differ. Tested groups are 10–30 students per grade. |
| P3.1 Advanced math or enrichment for grades 5–6 | district-enrichment-and-advanced-learners (facts 1–10) | partial | STEAM program (Project Lead the Way), Makerspace stipends, instrument lessons, chess club, drama, summer enrichment. No gifted program, acceleration procedure or advanced math class was found; policy IHBB is one sentence. Kennett Middle School options are in agent 3's file. |
| P4.1 Are speech and OT therapists full-time at MES? | district-special-education-services (facts 1–11) | full | Full-time SLP on staff; 0.80 FTE COTA; contracted OT shared with Tamworth; weekly service hours for September 2026. |
| P6.1 (school side) English learner services | district-student-support (facts 13–15); district-special-education-services fact 1; site data: English learners; existing slug english-learner-rights | partial | One English learner at MES at the end of 2024-25; ESOL is bought as a service ($20,000 budgeted for 2026-27). The provider and hours aren't named. Kennett is in agent 3's file. |
| P7.2 Enrollment trend and grade combinations | district-classrooms-and-staff (facts 1, 2, 4–6, 11, 12); madison_elementary_enrollment_by_grade; site data: enrollment | full | K–6 fell from 139 (2019) to 90 (fall 2026); multi-age K–2 classes since 2024-25; a draft warrant article would study closing the school. |
| P10.2 Trauma-informed support and counseling, on site vs shared | district-student-support (facts 1–10, 12); district-special-education-services (facts 5, 8–10) | partial | Full-time counselor on site; Responsive Classroom; trauma-informed approach in the Title I plan; two BCBA-certified staff; school psychologist bought as a service; SAU-level student services director. No social worker or trauma training hours found. |
| P13.3 Volunteering and substitute teaching | district-volunteers-and-partners (facts 1–5, 9); district-classrooms-and-staff (facts 13–15) | full | Designated vs other volunteers, fingerprint checks ($25 volunteer, $50 substitute), district pays check fees, substitute packet, $150 a day. OASIS intergenerational tutoring is a listed partner; how to join it was not found. |
| P15.1 (school side) Free and reduced meals; weekend backpacks | district-meals (facts 1–4); site data: free and reduced lunch | full | End 68 Hours of Hunger bags are offered to every student; families ask the counselor. Site data: 44 of 102 eligible in 2025-26 (43.1%, derived) against 23.2% statewide. |
| P15.2 Social worker or family liaison | district-student-support (facts 2, 7–9) | partial | The counselor is the family liaison and homeless liaison. A Title IV social worker contract was awarded in 2022; no later social worker was found. |
| P15.3 (school side) How community groups partner | district-volunteers-and-partners (facts 1–12) | partial | Volunteer and gift policies, PTO, partner list, facility-use forms. No church or civic summer reading program or supply drive was found in school sources (agent 5 covers the town side). |
| P16.3 Covering absences when several staff are out | district-classrooms-and-staff (facts 13–17) | partial | Substitute list and coordinator, support staff paid $30 to substitute, rates, examples of vacancies covered by substitutes. No written plan for multiple absences on one day was found. |
| P18.1 Security upgrades funded | district-safety-and-security (facts 1–7) | partial | 2023 camera and alarm system ($85,000; up to $60,000 from fund balance after state grants were not won); 32 cameras from 2015; SAFE Rounds 1–3. No vestibule project or radio boosters found; Round 4 list not retrieved. |
| P18.2 Joint drills with police and fire | district-safety-and-security (facts 8–13) | partial | Policies EBCA, EBCB, EBB, RSA 189:64 drill rules, EOP approved October 2026, armed-assailant training by the police chief (2023), safety week. How often first responders join drills is not public. |
| P18.3 School resource officer | district-safety-and-security (facts 14–15) | partial | No SRO found in any school source; Madison Police teach DARE. Agent 5 covers police staffing. |
| P20.1 Local history in the grade 3–4 NH history curriculum | district-curriculum-and-assessment (facts 13–17) | partial | Concord trip, Tin Mountain lesson on Madison history, maple sugaring unit, Historical Society visits. No source mentions the Madison Boulder, Silver Lake's railroad era or one-room schoolhouses in lessons. The district owns the 1835 Madison Corner School (see "For another file"). |

## district-classrooms-and-staff: Madison Elementary Classrooms, Class Sizes, Staff and Substitutes

- kind: local
- question_type: local_practice
- description: How a district's schools group classes and grades, their staff and roles, staffing changes, substitutes and aides, and how the schools describe themselves

1. Madison Elementary School is organized into grade bands of K–2, 3–4 and 5–6 with more than one teacher in each band; teachers weigh academic performance, social-emotional development, behavior and student dynamics to build balanced classes, families have a voice in placement, and teachers in each band share regular common planning time.
   - citation: Madison School District Annual Report, January 2026, p. 19 (Principal's Annual Report)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "MES is organized into grade-level bands of K–2, 3–4, and 5–6. This structure benefits both students and staff by allowing for flexible grouping, targeted instruction, and collaborative planning. ... Having multiple teachers within each grade band allows families a voice in classroom placement". Raw: raw/school/docs/madison-annual-report-jan-2026.txt (page 22 of the PDF).

2. In the 2026-27 school year Madison Elementary has six classrooms: two K–2 classes of 18 and 17 students, two grade 3–4 classes of 14 and 12, and two grade 5–6 classes of 15 and 14, according to the principal's count of October 23, 2026.
   - citation: Madison School Board packet, November 2, 2026, p. 14 (2026-27 Madison School District Enrollment)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Table "Madison Elementary School Class Configuration Enrollment: Gr. K-2 18; Gr. K-2 17; Gr. 3-4 14; Gr. 3-4 12; Gr. 5-6 15; Gr. 5-6 14", labeled "MES Enrollment Numbers as of 10.23.2026". Read from the page image raw/school/board/png/madison-sb-packet-2026-11-02-p14.png; text in raw/school/board/madison-sb-packet-2026-11-02.txt. The site's database has average class sizes by grade span through 2025-26.

3. Madison School Board policy IIB sets the most students per classroom at 18 for grades K–2, 20 for grades 3–4 and 22 for grades 5–6; if a class goes over, the principal may adjust class sizes and the administration must tell the board and recommend a fix.
   - citation: Madison School Board Policy IIB, Class Size (adopted 2008, last readopted August 1, 2016)
   - source: https://drive.google.com/file/d/1-D6WhtVPfNZ4MNBfVwmOq6rT9TisKjYm/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The Board shall establish the maximum number of students per classroom for grades K-2 at 18- students per classroom, and 20 students per classroom for grades 3-4 and 22 students per classroom for grades 5-6." Raw: raw/school/policies/madison-policy-iib.txt.

4. Madison Elementary's website says the school began moving to multi-age classes with two grade 1/2 classes in 2015-16 and switched to K–2, 3/4 and 5/6 classroom groupings starting in 2016-17; the same page lists Universal Design for Learning, Response to Intervention in reading and math for all K–6 students, a device for each student, and inclusion of all children in their classrooms with peers.
   - citation: Madison Elementary School website, "About Us"
   - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/home/about-us
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "We began with two Grades 1/2 classes in 2015-16. Beginning in 2016-17 we transitioned to having a classroom configuration of: Grades K-2, Grades 3/4, and Grade 5/6." The page is undated. The 2024 annual report (fact 5) describes the K–2 grouping as new for 2024-25, so the K–2 grouping appears to have been used, dropped and brought back; no source explains the gap. Raw: raw/school/mes/about-us.txt.

5. In spring 2023 Madison Elementary announced a new primary-grade structure; 2023-24 was a transition year with one K–2, one K/1 and one grade 1/2 class, and the school moved to K–2 classes in 2024-25, with students taught in grade-level groups for core subjects and in mixed-grade groups for literacy blocks and science and social studies units.
   - citation: Madison School District Annual Report, January 2024, p. 19 ("K-2 Classes – Year 1 Update")
   - source: https://drive.google.com/file/d/17ect0TR75moUGzxU_gjdjDGHg8Gux6UU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The 2023-24 school year has served as a transition year as we move to a grades K-2 structure in 2024-25. ... During the 2023-24 school year we had one classroom of each configuration: gr. K-2, gr. K/1, and gr. 1/2. ... our students have participated in core instructional times with grade level groups, mixed grade level instruction for Literacy Blocks, Discovery, and thematic units for science and social studies." Raw: raw/school/docs/madison-annual-report-jan-2024.txt.

6. In multi-age classrooms at Madison Elementary, students "loop" with the same teacher for more than one year, and the School Leadership Team chose multi-age education as the first topic for staff Professional Learning Community work in 2026-27, to look at what works and what could improve.
   - citation: Madison School Board packets, October 5, 2026, p. 14 and November 2, 2026, p. 12 (Principal's Reports)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: November 2026: "Our School Leadership Team has identified multi-age education as the first focus for our Professional Learning Community (PLC) work this year." October 2026 (https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view): "With multi-age classrooms, that timeline is typically sped up as students who loop with teachers have many of these things already established". Raw: raw/school/board/madison-sb-packet-2026-11-02.txt; raw/school/board/madison-sb-packet-2026-10-05.txt.

7. Madison Elementary's fall 2025 report card counts 6 classroom teachers in FY2026, down from 10 in FY2022, while the highest student count of the year fell from 130 to 104; it also counts 2 intervention teachers, 3 special education teachers (case managers and speech), 2 health and wellness staff (counselor and nurse), part-time integrated arts teachers and 7 paraprofessionals in FY2026. See table madison_elementary_staff_by_role.
   - citation: Madison School District Report Card, Fall 2025, p. 6 (in the January 2026 Annual Report, p. 28)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Read from the page image raw/school/docs/png/madison-annual-report-jan-2026-p31.png. Row text: "Highest student count for the year 104 112 116 127 130; Classroom Teachers 6 8 9 9 10" (FY26 to FY22). The site's database holds DOE staff FTE counts by category.

8. Madison Elementary's fall 2025 report card says that in 2025-26, 11 of its 18 teachers held master's degrees and 7 held bachelor's degrees; 13 staff had worked at the school 1–5 years and 16 had worked there 6 years or more; resignations, retirements and non-renewals totaled 5, 4, 6, 7 and 2 in the years 2020-21 through 2024-25.
   - citation: Madison School District Report Card, Fall 2025, p. 6 (January 2026 Annual Report, p. 28)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p31.png: "Teacher: Bachelors 7, Masters 11; Paraeducator: Associates 5, Bachelors 2"; years of service "1-5 Years 13; 6-10 Years 3; 11-15 Years 5; 16-20 Years 2; 20-25 Years 2; 25-30 Years 1; 30+ Years 3"; staffing changes "20-21 Resignation 4, Non Renewal 1, Total 5; 21-22 4; 22-23 Resignation 5, Reduction in Force 1, Total 6; 23-24 7; 24-25 2". The 16 with 6+ years is a sum (derived): 3+5+2+2+1+3.

9. All paraprofessionals at Madison Elementary hold the NH Department of Education's Para II certification, and their schedules are set to match students' IEP goals so students still get core instruction and related services.
   - citation: Madison School District Annual Report, January 2026, p. 20 (Principal's Annual Report)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "All paraprofessionals at MES are certified by the New Hampshire Department of Education with Para II credentials. They provide essential support to students based on individual needs, including academic assistance, executive functioning support, behavioral guidance, and sensory regulation." Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

10. Derived from the site's data, Madison Elementary had about 9.4 K–6 students per teacher FTE in 2024-25 (110 students, 11.7 FTE) and about 8.1 in 2025-26 (102 students, 12.6 FTE); the "11 to 1" figure appears only if the 2024-25 preschoolers are counted (129 students per 11.7 FTE = 11.0).
   - citation: Derived from NH DOE staff and enrollment data held in the site's database (district 333, school 20360) and the October 1, 2025 enrollment in the January 2026 Annual Report, p. 75
   - source: https://www.education.nh.gov/data-reports
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Derived by dividing enrollment by "Teacher" FTE (district_staff, which counts all teachers, including special education, intervention and arts teachers, not only classroom teachers). 110/11.7 = 9.40; 129/11.7 = 11.03; 102/12.6 = 8.10. The 129 is the site's 2024-25 total including 19 preschoolers. Raw: raw/school/site-data/madison-elementary-site-data-2026-11-13.txt. The NH DOE data page is the one the school's report card points readers to.

11. Madison Elementary's official K–6 enrollment on October 1 was 139 in 2019, 127 in 2020, 130 in 2021, 124 in 2022, 114 in 2023, 110 in 2024 and 102 in 2025; the principal's count in October 2026 was 90 K–6 students plus 10 Madison preschoolers. See table madison_elementary_enrollment_by_grade.
   - citation: Madison School District Annual Report, January 2026, p. 75 (Report of Official Enrollment as of October 1st); Madison School Board packet, November 2, 2026, p. 14
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The Madison Elementary School's official enrollment for Grades K through 6, as of October 1st 2025 was 102." Checked against the page image raw/school/docs/png/madison-annual-report-jan-2026-p78.png. The 2026-27 row (PreK 10, K 12, Gr. 1 11, Gr. 2 12, Gr. 3 14, Gr. 4 12, Gr. 5 17, Gr. 6 12, total 100) is from the November 2 packet (raw/school/board/png/madison-sb-packet-2026-11-02-p14.png), counted October 23, 2026, not the official October 1 count. The January 2026 report had projected 90 K–6 for 2026-27.

12. A draft Article 8 for Madison's 2027 school district warrant, in the school board's November 2, 2026 packet, would direct the board to form an advisory committee to study the possible closure of Madison Elementary School, looking at enrollment trends, savings or costs, educational effects and relocation plans, and future use of the building, and to report before the 2028 annual meeting.
   - citation: Madison School Board packet, November 2, 2026, pp. 53–54 (Madison School District School Warrant Articles 2027, draft)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Article 8: Shall the School District vote to direct the School Board to establish an advisory study committee to evaluate the potential closure of Madison Elementary School and to present its findings and recommendations to the District prior to the 2028 Annual District Meeting." The draft has blank amounts and vote counts; minutes of the November 2 meeting were not yet posted, so whether the article stays on the warrant is not known. Raw: raw/school/board/madison-sb-packet-2026-11-02.txt.

13. Madison policy GCG has the superintendent keep a list of qualified substitute teachers; a substitute who stays more than ten school days in a row takes on lesson planning and grading and is paid at the minimum step of the teacher salary scale, and after twenty days a fully qualified substitute moves to the matching step; all substitutes must pass a criminal history records check first.
   - citation: Madison School Board Policy GCG, Part-Time and Substitute Professional Staff Employment (readopted August 4, 2014)
   - source: https://drive.google.com/file/d/1vTFMZPkvDgUw-rsz8haI4RJdx6ZaIt_y/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Whenever a fully qualified substitute is required for a period in excess of ten consecutive school days the substitute will have full responsibility for the instruction to include planning lessons and marking students, and such a substitute will be placed on the minimum salary step." Raw: raw/school/policies/madison-policy-gcg.txt.

14. For 2026-27 Madison pays substitute teachers $150 a day, whether they are certified or retired educators, have a two- or four-year degree, or have no degree; substitute paraprofessionals and office staff earn $20 an hour and substitute lunch staff and custodians $25 an hour, within the budgeted hours of the position.
   - citation: SAU 13, "Madison Substitute Pay Rates 2026-2027" (approved by the Madison School Board August 3, 2026)
   - source: https://drive.google.com/file/d/18EMIEbmVranHvs1OPUoHjJEKfpuuYOR9/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Certified or Retired Educator Who Held Certification $150.00/day; College Degree (2 or 4 year) & No Degree $150.00/day ... Paraprofessional $20.00/hrly; Lunch Personnel $25.00/hrly; Custodian $25.00/hrly; Office $20.00/hrly". The board kept the 2025-26 rates on August 3, 2026 (minutes). A motion to raise certified substitutes to $175 a day failed 2–3 on August 4, 2025 (raw/school/board/older/madison-august-4-2025-approved-minutes.txt). Raw: raw/school/sau13/madison-substitute-rates.txt.

15. To substitute in SAU 13, an applicant sends the SAU a substitute packet, which goes to the building principals to decide whether to add the person to the substitute list; the applicant then gets fingerprinted, may be listed while the background check is pending, and must complete the SAU 13 bullying prevention training.
   - citation: SAU 13 Substitute Packet (linked from the SAU 13 Job Opportunities page)
   - source: https://drive.google.com/file/d/1TkicYK75dy1ufu9nvDCQSY8yNfDqQl_6/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "First, you will need to submit to the SAU your completed substitute packet. Once we receive this, it will be forwarded onto the Building Principal's to review if you can be added to the substitute list ... Once you have started the criminal background process, you can then be put on the substitute list pending your criminal background results. ... ALL SUBSTITUTES MUST COMPLETE THE BULLYING PREVENTION KIT". Raw: raw/school/sau13/substitute-application-packet.txt.

16. Madison funds a substitute coordinator as a stipend position (the board voted 3–1–1 on June 1, 2026 to fund it), and a 2023 agreement with the Madison Employees' Association lets Madison Elementary support staff who fill in as substitutes receive a $30 flat fee.
   - citation: Madison School Board minutes, June 1, 2026 (approved) and November 6, 2023 (approved)
   - source: https://drive.google.com/file/d/1XPYZQo6CViR6yfLffirjmPp735HdtJKO/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: June 1, 2026: "Motioned by Ed Robisnon motioned to fund the substitute coordinator and head teacher positions ... The motion passed 3-1-1". November 6, 2023 (https://drive.google.com/file/d/1-TfGma0BoUmKlKVn92L2dZM-xVohPCzN/view): "MOU with MEA-Substitutes: Michael said the updated version allows support staff to receive a $30-dollar flat fee for work as a substitute." Raw: raw/school/board/older/madison-june-1-2026-public-approved-minutes.txt; raw/school/board/older/madison-november-6-2023-approved-minutes.txt.

17. Madison Elementary's recent reports show vacancies covered from within: in October 2026 the preschool was still looking for a second paraprofessional and was using substitutes; in spring 2026 the kitchen ran a community lunch one worker short by spreading out preparation and using volunteers; and the principal's job description says the principal must "step into any role as needed".
   - citation: Madison School Board minutes, October 5, 2026; MES newsletter, April 6, 2026; Madison School District Annual Report, January 2026, p. 21
   - source: https://drive.google.com/file/d/1WyF6kj-vpCHSJ7hlH0ki2gbDXfM_8kxf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Minutes: "Principal Heather Woodward stated that the school is still searching for a second paraprofessional and is currently utilizing substitutes." Newsletter (https://docs.google.com/presentation/d/14heYX-CucoiSVF9ZA2_YD7jSN-QXrhnOW4BmJdWxsxc/edit): "Our crew has been down one member for the past several weeks, but Ms. Janet ... divided up the preparation over a period of time and through use of volunteers." Annual report: "The principal must be prepared to step into any role as needed". The report also notes custodial "staffing challenges during the second half of 2025". No written plan for days when several staff are out was found. Raw: raw/school/board/madison-sb-minutes-2026-10-05.txt; raw/school/newsletters/mes-newsletter-4.6.2026.txt; raw/school/docs/madison-annual-report-jan-2026.txt.

## district-curriculum-and-assessment: Madison Elementary Curriculum, Interventions, Test Results and Local History

- kind: local
- question_type: local_practice
- description: The curriculum programs a district uses (math, reading, science), how reading is taught and supported, its local tests, and how teachers fit local content into lessons

1. Madison Elementary began teaching Illustrative Mathematics, an inquiry-based program, in 2022-23, and the principal wrote that SAU 9 later adopted it too, easing the move to Kennett Middle School.
   - citation: Madison School District Annual Report, January 2024, p. 16 (Principal's Report)
   - source: https://drive.google.com/file/d/17ect0TR75moUGzxU_gjdjDGHg8Gux6UU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The 2022-23 school year provided us the opportunity to initiate a new math instructional program, Illustrative Math, which is a rigorous inquiry-based program. ... it was recently adopted in SAU 9, providing our students a more seamless transition to the middle school." Raw: raw/school/docs/madison-annual-report-jan-2024.txt.

2. Starting in 2023-24, after staff took the state's LETRS science-of-reading course, Madison Elementary taught Fundations phonics to all K–2 students, offered it in grade 3 to students who could benefit, and used the Just Words spelling program in grades 4–6.
   - citation: Madison School District Annual Report, January 2024, p. 17 (Principal's Report)
   - source: https://drive.google.com/file/d/17ect0TR75moUGzxU_gjdjDGHg8Gux6UU/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Our students in grades 1 and 2 already learned through the phonics program Fundations. This school year we expanded the instruction to include all students in K-2. In grade 3 we offered Fundations for those who could benefit from the last level of instruction. In grades 4-6 we implemented Just Words spelling program." Raw: raw/school/docs/madison-annual-report-jan-2024.txt.

3. Madison's 2024-25 Title I plan says reading and math progress is measured with STAR at least three times a year; students in intervention groups get 30 minutes of targeted instruction 4–5 days a week in 4–6 week cycles; staff are trained in Lindamood-Bell LIPS and Visualizing and Verbalizing; and students who don't progress after two cycles go to the data team, whose options include Tier 3 help in school, tutoring outside the school day, a 504 plan or a special education referral.
   - citation: Madison School District, NH DOE Title I, Part A Plan 2024-2025 (signed April 2024), component 1
   - source: https://drive.google.com/file/d/14bLrh0SyuHvH0i-lCrnYgMCzeJB54iK0/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Student data in reading and math is gathered using STAR at minimum 3 times per year. ... targeted interventions assessed in 4-6 week cycles. All students who do not make adequate progress over the period of 2 intervention cycles, will be referred to our data team ... Options include Tier 3 intervention during school hours, beyond school day tutoring, and potential referral for 504 accommodations or specialized instruction ... Madison School uses the Fundations program by Wilson in the primary grades and the Just Words program in grades 4-6 as a Tier 2 intervention ... students will participate in 30 minutes of targeted instruction 4-5 days a week. Several intervention staff are trained to use specific programs to support interventions such as Lindamood-Bell LIPS and Visualizing and Verbalizing programs." Linked from the MES Title I page. Raw: raw/school/docs/madison-title-i-plan-2024-25.txt.

4. Madison Elementary's intervention team, a reading specialist and a Response to Intervention (RTI) teacher, runs benchmark tests for all students three times a year, progress checks for students in intervention, and the dyslexia screening the state requires, and gives small-group or one-on-one help in 6–8 week cycles to any student who needs it.
   - citation: Madison School District Annual Report, January 2026, p. 20 (Principal's Annual Report, "Intervention Teachers")
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "the intervention team coordinates the administration of benchmark assessments three times per year of all students, progress monitoring assessments receiving interventions, and dyslexia screening as required by the state. ... Intervention services are available to any student based on identified needs and are delivered in 6–8 week instructional cycles". The state dyslexia screening rule is in the library (slug gov-ed-306-2024-rewrite and related). Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

5. Madison Elementary tests reading and math with STAR, a nationally normed computer test, and checks reading skills one-on-one with DIBELS; the school treats grades 1–6 as the valid results for comparing trends.
   - citation: Madison Elementary School website, "MES Data Information"
   - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/mes-data-information
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "At Madison Elementary School we consistently assess and monitor reading and math skills using the STAR nationally normed test. ... Students are also tested in a one on one situation for reading skills using the Dibels assessment system. Although assessment begins in Kindergarten, we look at grades 1-6 as valid test results". Raw: raw/school/mes/data-information.txt.

6. For 2026-27 Madison Elementary staff spent summer 2026 revising math curriculum maps and some attended an Arts & Letters reading workshop; the three SAU 13 principals are working on aligning math, and the district's 2027-28 working budget lists "Fundations & Arts & Letters Student Workbooks" under language arts materials.
   - citation: Madison School Board packets, September 14, 2026, p. 19 and November 2, 2026, p. 33; Madison School Board minutes, October 5, 2026
   - source: https://drive.google.com/file/d/1FqIWm7n4M2TEfI9g4t9WY13e4FSF8Itb/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: September report: "others were able to take part in an Arts & Letters workshop. In addition, our staff have worked this summer to collaborate, review and revise math curriculum maps, and make revisions to the Social-Emotional Screener." October 5 minutes: "The three district principals met and are currently focusing on math alignment." November packet budget line: "Language Arts Materials ... Fundations & Arts & Letters Student Workbooks" (https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view). No source says Arts & Letters has fully replaced earlier materials at MES. Raw: raw/school/board/madison-sb-packet-2026-09-14.txt; raw/school/board/madison-sb-minutes-2026-10-05.txt; raw/school/board/madison-sb-packet-2026-11-02.txt.

7. Madison pays its own teachers to tutor outside class with federal Title I money: in March 2024 the board approved before-school tutors at $25 an hour for up to 1.25 hours a day, and in December 2024 it approved Title I tutors for up to 4 days a week, one hour a day, at $50 an hour.
   - citation: Madison School Board minutes, March 4, 2024 and December 2, 2024 (approved)
   - source: https://drive.google.com/file/d/1GqP-VE50xWsj3ewPNAjC7wLShoPBsSvg/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: December 2, 2024: "The board approved the nominations of staff members for Title 1 tutors up to 4 days a week, 1 hour a day, and $50.00 an hour". March 4, 2024 (https://drive.google.com/file/d/15CskgR3JqpJxu9MV25F3h2F2Zl_a8KQq/view): "before-school tutoring, using Title 1 funds, for $25 per hour for up to 1.25 hours per day". The board named Title I tutors again in November 2025 and March 2026. Raw: raw/school/board/older/madison-december-2-2024-approved-minutes.txt; raw/school/board/older/madison-march-4-2024-approved-minutes.txt.

8. SAU 13's superintendent reported in January 2026 that Madison Elementary's reading proficiency on the state test rose from 42% five years earlier to 52%, above the state average in 2023 and 2024, and math from 22% to 29%; calling the results short of the goal, he said the district is stepping up its math focus with targeted interventions, curriculum alignment and data use.
   - citation: Madison School District Annual Report, January 2026, p. 15 (Superintendent of Schools Report)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Five years ago, aggregate reading proficiency stood at 42 percent; it has since increased to 52 percent, with Madison exceeding the state average in both 2023 and 2024. Similarly, math proficiency has improved from 22 percent to 29 percent ... While these outcomes are not yet at the level we aspire to achieve, they reflect forward progress. In response, we are intensifying our focus on mathematics through targeted interventions, curriculum alignment, and the systematic use of data". Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

9. Madison Elementary's fall 2025 report card gives its spring 2025 state test results for all students tested as 49% proficient or above in English language arts, 27% in math and 30% in grade 5 science, and 50%, 24% and 25% for students who had attended MES at least three years; it lists state averages for grades 3–6 of 49–57% in English and 40–53% in math, and 38% in grade 5 science.
   - citation: Madison School District Report Card, Fall 2025, p. 7 (January 2026 Annual Report, p. 29)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Read from the image raw/school/docs/png/madison-annual-report-jan-2026-p32.png: "2025 NH SAS Results ... All Tested: ELA 49%, Math 27%, Science 30%; Cohort Group (Attending MES 3+ years): 50%, 24%, 25%"; state: "Gr. 3 49% 53%; Gr. 4 53% 52%; Gr. 5 57% 40% 38%; Gr. 6 53% 41%". The site's database shows 52%, 29% and 31% for 2025, the figures the Advisory Budget Committee also used; the difference likely comes from which students are counted, but no source explains it. The same page shows each class's results by grade, often for 10–25 students.

10. Derived from the site's data, Madison Elementary's share of students proficient in math trailed the state's all-grades figure by 10 to 15 points each year from 2022 to 2026 (30% vs 44% in 2026), its reading share was within 6 points of the state (above in 2023 and 2024, below in 2022, 2025 and 2026), and its grade 5 science share was above the state's in 2022, 2023 and 2026.
    - citation: Derived from NH Statewide Assessment System results in the site's database (school 20360 and state, all students), test years 2022–2026
    - source: https://www.education.nh.gov/data-reports
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Derived as MES minus state, percentage points. Math: 30–40, 29–42, 26–41, 29–42, 30–44 (2022–2026). Reading: 49–51, 58–52, 54–53, 52–55, 51–55. Grade 5 science: 43–38, 46–36, below 10% (suppressed) vs 36, 31–38, 42–38. The state figure covers grades 3–8 and 11; MES tests grades 3–6, and its tested groups are 10–30 students per grade, so one or two students move a grade's percentage by several points (see library slug comparing-small-schools). Raw: raw/school/site-data/madison-elementary-site-data-2026-11-13.txt.

11. Madison Elementary's fall 2025 report card says 54% of students have one or more "at-risk" factors (low income measured by free or reduced lunch, no stable housing, guardianship, or a single parent or separated parents), and that 26 students (25%) had IEPs and 15 (15%) had 504 plans on October 1, 2025, up from 19% and 7% in 2021.
    - citation: Madison School District Report Card, Fall 2025, pp. 7–8 (January 2026 Annual Report, pp. 29–30)
    - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: From the images raw/school/docs/png/madison-annual-report-jan-2026-p33.png ("54% OF STUDENTS Identified as having one or more 'at-risk' factors that can impact a students' educational experience and progress") and -p32.png ("Students with IEP 26 25% ... 24 19%; Students with 504 Plan 15 15% ... 9 7%", 2025 to 2021). These are the school's own descriptions; no source measures how these factors affect test results.

12. Madison Elementary's report card also tracks STAR results for the same group of students over time, and a chart of STAR math proficiency against the state benchmark shows a fall from about 51% in spring 2022 to about 40% in spring 2024, rising to about 45% in fall 2025.
    - citation: Madison School District Report Card, Fall 2025, p. 8 (January 2026 Annual Report, p. 30)
    - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Values read by eye from the line chart "Star Math Proficiency Rate (State Benchmark)" in raw/school/docs/png/madison-annual-report-jan-2026-p33.png; the chart has no data labels, so the values are approximate (derived). The STAR reading chart on the same page ranges from about 54% to about 71% (winter 2025-26).

13. In fall 2026 Madison Elementary's grade 3–4 students took a field trip to Concord to visit the State House and the New Hampshire Historical Society while studying New Hampshire history and the three branches of government, and grade 5–6 students studied land formations and the rock cycle with Tin Mountain Conservation Center, including a trip to Redstone Quarry.
    - citation: Madison School Board packet, November 2, 2026, p. 12 (Principal's Report, November 2026)
    - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "Students in grades 3 and 4 explored New Hampshire history and the three branches of government during a field trip to Concord, where they visited the State House and the New Hampshire Historical Society." Raw: raw/school/board/madison-sb-packet-2026-11-02.txt.

14. In April 2026 a Tin Mountain Conservation Center educator taught Madison Elementary's grade 3–4 students about Madison history through a game on how towns form, covering rock walls, farms, the town pound and other places a small town needs.
    - citation: MES newsletter, April 13, 2026
    - source: https://docs.google.com/presentation/d/1R1WdV0RWOlXc8sUThEuO9n3s6LH50uvFgw_qa8Qa3Zk/edit
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "our Gr. 3-4 students had a visit last week to learn more about Madison History. They played a 'game' that helped them learn about how towns are created through understanding about rock walls, farms, the town pound, and other important areas that a small town needs." Raw: raw/school/newsletters/mes-newsletter-4.13.2026.txt.

15. Madison Elementary's grades 3–4 have made maple syrup on the school grounds each March for eight years, in a unit tied to reading, math, science and social studies that covers the history of maple syrup from Native Americans through colonial times and the Revolutionary War; the classes won first place in the 2026 Tucker Mountain Maple Challenge, a statewide school contest.
    - citation: MES newsletter, May 11, 2026
    - source: https://docs.google.com/presentation/d/19mlUVFWZ0OppnKgAcx5DW77JD0XtnA0GrJynr6ZCsMk/edit
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "This is the 8th year 3rd & 4th grade has made maple syrup at MES. ... Our students learn about the science behind the process and the history of the discovery of maple syrup by Native Americans to the uses of maple syrup during the early colonial times and the Revolutionary War." and "MES 3rd & 4th Graders take 1st Place!" Raw: raw/school/newsletters/mes-nl-5.11.26.txt.

16. During National School Lunch Week in fall 2023, Madison Historical Society members visited Madison Elementary, one telling of her family's ten generations in Madison and another of how "the surrounding family schools became one in 1951", and the school librarian presented the history of the Madison and Silver Lake post offices.
    - citation: Madison School District Annual Report, January 2024, p. 22 (Food Service Director's report)
    - source: https://drive.google.com/file/d/17ect0TR75moUGzxU_gjdjDGHg8Gux6UU/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "From the Madison Historical Society we welcomed Nancy Harmon Martin & Linda Smith ... She also told some of the history of food service and how the surrounding family schools became one in 1951. ... Mrs. Flanigan, our Librarian, presented to the students about the history of the Post Office in Madison & Silver Lake." These are one-time visits, not a curriculum unit. Raw: raw/school/docs/madison-annual-report-jan-2024.txt.

17. In April 2025 author Natalie Kinsey-Warnock worked with Madison Elementary students on early historical heritage, with students telling their own families' stories, and in spring 2026 grade 3–4 media classes ended a unit on immigration with "My Family Heritage" posters.
    - citation: Madison School Board minutes, April 7, 2025; MES newsletter, May 11, 2026
    - source: https://docs.google.com/presentation/d/19mlUVFWZ0OppnKgAcx5DW77JD0XtnA0GrJynr6ZCsMk/edit
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Newsletter: "The 3rd and 4th graders in Media Class are completing their unit on Immigration by creating a My Family Heritage poster." Minutes of April 7, 2025 (https://drive.google.com/file/d/1YJm-vs--9zVQU3_jXADCu3AgpYe3ieFF/view): "author Natalie Kinsey-Warnock who came early April and worked with students focusing on early historical heritage with the students telling of their own family's stories." Raw: raw/school/newsletters/mes-nl-5.11.26.txt; raw/school/board/older/madison-april-7-2025-approved-minutes.txt.

## district-enrichment-and-advanced-learners: Enrichment, STEAM and Advanced Learners at Madison Elementary

- kind: local
- question_type: local_practice
- description: Enrichment, STEM, arts, music and world languages, and how a district serves advanced or gifted students (acceleration, placement, early high school courses)

1. Madison's gifted policy, IHBB, says only that "The Madison School Board recognizes the need for programs for gifted and talented pupils"; it sets no identification process, program or acceleration rule.
   - citation: Madison School Board Policy IHBB, Programs for Gifted Pupils (readopted September 8, 2014)
   - source: https://drive.google.com/file/d/11LpoXt3XXkCdt09af2UO01aaOC6OOfmD/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: The whole policy text is one sentence. Madison's 2024-25 Title I plan says help for "identifying and serving gifted and talented students" is "funded through the general budget and not through Title I" (raw/school/docs/madison-title-i-plan-2024-25.txt, component 13). No source describes a gifted program or an advanced math class at MES. Raw: raw/school/policies/madison-policy-ihbb.txt.

2. In 2026-27 Madison Elementary started a STEAM (science, technology, engineering, arts and math) program using the Project Lead the Way curriculum, which Tamworth's Brett School also uses; the first session is for grades 3–6, K–2 students began an engineering unit in November 2026, and the before- and after-school STEAM programs had "steady, strong participation with no students turned away" in October.
   - citation: Madison School Board packet, September 14, 2026, p. 19 (Principal's Report); Madison School Board minutes, October 5, 2026
   - source: https://drive.google.com/file/d/1FqIWm7n4M2TEfI9g4t9WY13e4FSF8Itb/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: September: "We anticipate Mrs. Flanigan giving a presentation in Nov. or Dec. after she completes the first session with students in grades 3-6. I can say that we are excited to implement Project Lead the Way which is also implemented in Tamworth". October 5 minutes: "Before and after-school STEAM programs are seeing steady, strong participation with no students turned away." November newsletter (https://docs.google.com/presentation/d/1WSF03hhXUwWcpAGsQUF0qdmzKE4UD3sOaKWVJJIA1mY/edit): "The K-2s began an engineering unit called Structure and Function: Exploring Design". Raw: raw/school/board/madison-sb-packet-2026-09-14.txt; raw/school/board/madison-sb-minutes-2026-10-05.txt; raw/school/newsletters/mes-newsletter-26.27.txt.

3. Madison Elementary's STEAM and Makerspace work is grant-funded: in May 2026 the board named two teachers to Title IV-A–funded stipend positions for the Makerspace program, the school announced a grant for a before- and after-school STEAM program for grades 3–6 with limited spots, and in August 2026 the board approved an agreement for a grant-funded 0.20 FTE STEM position.
   - citation: Madison School Board minutes, May 4, 2026 and August 24, 2026; MES newsletter, May 5, 2026
   - source: https://drive.google.com/file/d/1-hgBx39Uwc9eF93kr91uREOtF2dpTsr_/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: May 4: "The board approved the nominations of Kate Stanley and Tammy Flannigan for the Title IVA Grant STEM teaching positions for the Makerspace program. These are stipend positions." Newsletter (https://docs.google.com/presentation/d/1LXiUix_R5tKHHz-B9UGE2mXwlo68bbLrgwambz2CVC8/edit): "We have received a grant to provide a STEAM ... before/after school program for students in Gr. 3-6. ... it will be limited to enrollment size due to available materials." August 24 (https://drive.google.com/file/d/1Bqt8NihZ5K7J413RSnZd6FvmR_-cJ8P-/view): "Memorandum of Understanding with the Madison Employee's Association specific to the grant funded STEM position of .20 FTE ... The motion passed 3-1-1". Raw: raw/school/board/older/madison-may-4-2026-approved-minutes.txt; raw/school/newsletters/mes-newsletter-5.5.2026.txt; raw/school/board/madison-sb-minutes-2026-08-24-special.txt.

4. Madison Elementary's integrated arts teachers (visual art, library and media, music and physical education) offer enrichment beyond weekly classes, including art club, book clubs, instrument lessons, STEM activities, talent shows, tutoring, concerts, theater productions and unicycling.
   - citation: Madison School District Annual Report, January 2026, p. 20 (Principal's Annual Report)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Integrated Arts teachers provide a wide range of extracurricular and enrichment opportunities, including art club, book clubs, instrumental instruction, STEM activities, talent shows, tutoring, performances (such as Talent Show, concerts, and theater productions) and unique offerings such as unicycling." Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

5. Madison Elementary's grades 5–6 have weekly art (60 minutes), music (60 minutes), library and media (60 minutes) and PE (60 minutes); grades 3–4 have art and music for 45 minutes each, library and media for 60 and PE for 30 and 45; and grades K–2 have art, music and media for 45 minutes each, library for 30 and PE for 30 and 45; instrument lessons are offered in grades 4–6.
   - citation: Madison School District Report Card, Fall 2025, p. 5 (January 2026 Annual Report, p. 27)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p30.png: "Instrument Lessons Gr. 4-6 ... Weekly Classes- K-2 Art (45 mins), Music (45 mins), Media (45 mins), Library (30 mins), PE (30 & 45 mins); Gr. 3-4 Art (45 mins), Music (45 mins), Library & Media (60 mins), PE (30 & 45 mins); Gr. 5-6 Art (60 mins), Music (60 mins), Library & Media (60 mins), PE (60 mins)". The page also lists chorus, concerts, a variety show, an Integrated Arts Day and musicals for grades K–2 and 3–6.

6. Madison Elementary's report card lists "beyond the curriculum" activities: art club, student assembly leaders, enrichment in the before- and after-school care program, chess club, the MES Mustang Players drama club, student-run morning announcements and a student mentor program.
   - citation: Madison School District Report Card, Fall 2025, p. 5 (January 2026 Annual Report, p. 27)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p30.png: "Beyond the Curriculum Opportunities: Art Club; Assembly Leaders; Before and After School Care Enrichment Programs; Chess Club; MES Mustang Players (Drama Club); Morning Announcements; Student Mentor Program".

7. Madison Elementary offers a summer enrichment program to all students enrolled in grades K–6, taught by staff paid with Title I funds; in 2026 extended school year students were combined with the eleven enrichment students.
   - citation: MES newsletter, May 5, 2026; Madison School Board minutes, April 6, 2026 and June 1, 2026
   - source: https://docs.google.com/presentation/d/1LXiUix_R5tKHHz-B9UGE2mXwlo68bbLrgwambz2CVC8/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Newsletter: "We are pleased to offer Summer Enrichment to all students currently enrolled at MES in Grades K-6." April 6, 2026 (https://drive.google.com/file/d/1e3Dus-KJDap-CSlzWm4EXYy41zv-POOJ/view): "The board approved the nominations for Title I Funded Summer Enrichment Teachers". June 1, 2026: ESY students "will be combined with the enrichment students. There are currently eleven enrichment students." Raw: raw/school/newsletters/mes-newsletter-5.5.2026.txt; raw/school/board/older/madison-april-6-2026-approved-minutes.txt; raw/school/board/older/madison-june-1-2026-public-approved-minutes.txt.

8. A Children's Literacy Foundation (CLiF) grant gave each Madison Elementary student 10 books during 2024-25 and brought authors to the school, and a follow-on Momentum grant in 2025-26 focused on writing.
   - citation: Madison School District Report Card, Fall 2025, p. 5 (January 2026 Annual Report, p. 27)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The 2024-25 School Year provided us with grant funds from the Children's Literacy Foundation to give each child 10 books throughout the year, bring several authors to work with our children ... This grant provides additional funding through the Momentum Grant in the 2025-26 academic year ... In 2025-26 the grant will focus on supporting writing." Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

9. Madison Elementary's 2026-27 school theme is "Full STEAM Ahead", and the principal reported plans for special days with STEAM activities that invite community members to take part.
   - citation: Madison School Board packet, October 5, 2026, p. 14 (Principal's Report, October 2026)
   - source: https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "I am super excited for the year ahead as we plan special days to infuse STEAM activities including inviting community members to take part. We are truly moving Full STEAM Ahead!" Raw: raw/school/board/madison-sb-packet-2026-10-05.txt.

10. Madison Elementary's report card says personalized learning is offered through data-based interventions and grant-funded tutoring outside the school day; it does not describe acceleration or above-grade work for advanced students.
    - citation: Madison School District Report Card, Fall 2025, p. 6 (January 2026 Annual Report, p. 28)
    - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p31.png: "Additional Personalized Support: Personalized learning opportunities are provided through data based interventions and beyond school day grant funded tutoring." The second clause states what the page omits. Kennett Middle School's accelerated math is in town/Conway/schools-k-8.md and agent 3's file.

## district-special-education-services: Special Education and Related Services at Madison Elementary

- kind: local
- question_type: local_practice
- description: Who provides special education and related services in a district (on staff or contracted), reading specialists, 504 practice, IEP moves between schools, and out-of-district placements

1. SAU 13's Student Services department, led by a director at the SAU office in Tamworth, oversees special education, English learner (ESOL) services and Section 504 plans for Madison, and the director is also responsible for Madison students placed out of district, attending charter schools, or attending Kennett Middle and High Schools.
   - citation: Madison School District Annual Report, January 2026, p. 17 (Madison Annual Student Service Report, January 2026)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "The Student Services department is responsible for ensuring that students identified as having an educational disability are afforded the rights that are outlined in IDEA, that students that are English Second Language Learners have access to ESOL services and that students that require a 504 Plan are afforded their rights ... the director is also responsible for our students ... placed in out of district placements ... students who attend local charter schools, as well as our middle and high school students attending Kennett Middle School and Kennett High School." Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

2. SAU 13's student services director has changed often in 2026: the director who wrote the January 2026 report resigned in June 2026, a new director was introduced in July 2026, and the SAU 13 office page now lists an interim director of student services.
   - citation: SAU 13 website, "SAU Office"; Madison School Board minutes, June 1, 2026 and July 6, 2026
   - source: https://www.sau13.org/home/sau-office
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Page text: "Interim Director of Student Services - Patricia Stone". June 1, 2026: "the SAU #13 Joint Board accepted the resignation of Student Service Director Lisa DuBois". July 6, 2026 (https://drive.google.com/file/d/1Gmb7J23mY_3IAQchNVpKupy_dNW8NF3J/view): "Superintendent Dr. Kathleen Scholand introduced Christina Smith as the Student Services Director." On October 5, 2026 the principal said she "was unable to connect with the previous Director of Students Services". Raw: raw/school/sau13/sau-office.txt; raw/school/board/older/madison-june-1-2026-public-approved-minutes.txt; raw/school/board/madison-sb-minutes-2026-07-06.txt.

3. Madison Elementary's related services are speech-language therapy and occupational therapy, given by a full-time speech-language pathologist and a part-time certified occupational therapy assistant (COTA) to students with IEPs and 504 plans, and sometimes as early intervention for grades K–2 under the school's tiered support system.
   - citation: Madison School District Annual Report, January 2026, p. 21 (Principal's Annual Report, "Related Service Providers")
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Related service providers at MES include both staff and contracted professionals. Currently, based on student needs, services are provided in speech-language therapy and occupational therapy. Our full-time Speech-Language Pathologist and part-time Certified Occupational Therapist Assistant deliver services to students with IEPs, 504 plans, and, in some cases, as part of our Multi-Tiered System of Support (MTSS), particularly for early intervention in grades K–2." The 2026-27 handbook lists the speech-language pathologist as staff and the COTA as a contracted provider (raw/school/docs/mes-family-handbook-2026-27.txt). Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

4. In August 2026 Madison's business administrator reported that the occupational therapy assistant position had been filled by the same independent contractor for four or more years and that, with the auditor, she judged the job to be more like employment; the board voted 4–1 to offer the person a 0.80 FTE staff contract, which was accepted by September.
   - citation: Madison School Board special meeting minutes, August 24, 2026 (approved); Madison School Board minutes, September 14, 2026
   - source: https://drive.google.com/file/d/1Bqt8NihZ5K7J413RSnZd6FvmR_-cJ8P-/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "the Certified Occupational Therapy Assistant (COTA) position has been contracted out for the last 4 or more years to the same independent contractor. ... they both agreed that the relationship is more like an employee than an independent contractor. ... Deb Parsons motioned to allow administration to offer a staff contract of .80 FTE to the current contracted individual ... The motion passed 4-1-0". September 14 minutes (https://drive.google.com/file/d/1jW5cNSqj2SZJmecyCZAoSf2NlloZJ3bZ/view): "Business Administrator Heather Sherwood replied that person did accept the COTA position." Raw: raw/school/board/madison-sb-minutes-2026-08-24-special.txt; raw/school/board/madison-sb-minutes-2026-09-14.txt.

5. For 2026-27 SAU 13 contracted with a company for an occupational therapist who supervises Madison Elementary's occupational therapy assistant and splits her time between the Madison and Tamworth schools; in December 2024 the district said it had not been able to hire an occupational therapist locally.
   - citation: Madison School Board minutes, September 14, 2026 (Director of Student Services Report) and December 16, 2024
   - source: https://drive.google.com/file/d/1jW5cNSqj2SZJmecyCZAoSf2NlloZJ3bZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: September 14, 2026: "A company has been contracted with to provide an Occupational Therapist to provide services including supervision to the COTA who works at MES. The OT will split her time between Madison and Tamworth schools." December 16, 2024 (https://drive.google.com/file/d/1JZjypctmV_kZm7of6BNbBBW-WThukrgJ/view): "Occupational Therapy – Budget increase, have not been able to hire local, outsourcing through a company." The number of days the OT spends in Madison is not given. Raw: raw/school/board/madison-sb-minutes-2026-09-14.txt; raw/school/board/older/madison-december-16-2024-approved-minutes.txt.

6. SAU 13's September 2026 service report for Madison lists, per week at Madison Elementary, 47.5 hours of specialized instruction from special education teachers, 38.25 hours of paraeducator support, 15.5 hours of speech and language services and 18.75 hours of occupational therapy for 24 students with IEPs, with 2 special educators and 6 paraeducators; no physical therapy or behavior analyst hours were listed.
   - citation: Madison School Board packet, October 5, 2026, p. 40 (Student Services Director Report – Madison, Special Education Services Quarterly Update, September 2026)
   - source: https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Read from the image raw/school/board/png/madison-sb-packet-2026-10-05-p40.png: "Students with an IEP 24 ... Special Educator 2 ... Para Educator 6 ... Specialized Instruction from SpEd Teacher 47.5 ... Para Educator 38.25 ... Speech and Language 15.5 ... Occupational Therapy 18.75 ... Physical Therapy 0 ... Board Certified Behavior Analyst 0", with "*Hours may fluctuate as student services are evaluated annually. **Total Hours are on a weekly basis". At the October 5 meeting the principal said the list "is inaccurate, as certain out-of-district and 504 students were omitted" (minutes). These are hours of service on IEPs, not staff schedules.

7. Madison Elementary had 24 students with IEPs and 14 with 504 plans in September 2026, compared with 29 IEPs and 17 504 plans at the end of 2024-25, and one English language learner at the end of 2024-25.
   - citation: Madison School Board minutes, September 14, 2026; Madison School District Annual Report, January 2026, p. 17
   - source: https://drive.google.com/file/d/1jW5cNSqj2SZJmecyCZAoSf2NlloZJ3bZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: September 14, 2026: "Madison Elementary School: 24 students ... 504 Plans (Madison Elementary School): 14 students". Annual report: "The Madison School District ended the 2024-2025 school year with the following special services population: Madison Elementary 29 ... 504 Plans (Madison Elementary) 17; English Language Learners (Madison El) 1". Raw: raw/school/board/madison-sb-minutes-2026-09-14.txt; raw/school/docs/madison-annual-report-jan-2026.txt.

8. Madison Elementary's special education teachers are certified in both elementary and special education and act as case managers for students with IEPs, and evaluations also draw on the speech-language pathologist, the occupational therapist and a school psychologist, whose work Madison buys as a service (a $22,000 "psychological services" line in the 2026-27 budget).
   - citation: Madison School District Annual Report, January 2026, p. 22; Madison School Board packet, September 14, 2026 (FY2027 expenditure report)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Annual report: "Special education teachers at MES are dual-certified in elementary and special education and serve as case managers ... Additional evaluation components are completed in collaboration with related service providers, including speech-language pathologist, occupational therapist, and school psychologist." Expenditure report (https://drive.google.com/file/d/1FqIWm7n4M2TEfI9g4t9WY13e4FSF8Itb/view): "01.2140.320.120 Psychological Services $22,000.00" (object code 320 is purchased professional services). Raw: raw/school/docs/madison-annual-report-jan-2026.txt; raw/school/board/madison-sb-packet-2026-09-14.txt.

9. Two Madison Elementary staff members hold Board Certified Behavior Analyst (BCBA) certification, and in September 2026 the Madison board approved, 5–0, an agreement for Madison to provide BCBA services to Freedom Elementary on set days each week, with Freedom paying $108 an hour plus mileage; Madison stays the employer.
   - citation: Madison School Board minutes, October 5, 2026 and September 23, 2026 (draft); Madison School Board packet, September 14, 2026, p. 40 (Inter-district Staff Sharing Agreement, draft 9/4/26)
   - source: https://drive.google.com/file/d/1RTg8jZoTDMtZo69C2coq6f4brPMM9Q3e/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: September 23 (draft, approved October 5): "Dr. Scholand presented an Inter-District Staff Sharing Agreement between Madison and Freedom School Districts for Board Certified Behavior Analyst (BCBA) services ... The motion passed unanimously, 5-0-0." Agreement: "Services will be the same days each week ... Reimburse Madison at a rate of $108/hour plus mileage at the current IRS rate". October 5: "Two current MES staff members are BCBA – certified." Raw: raw/school/board/madison-sb-minutes-2026-09-23-special-draft.txt; raw/school/board/madison-sb-packet-2026-09-14.txt; raw/school/board/madison-sb-minutes-2026-10-05.txt.

10. Madison's board first rejected (0–4–1, September 23, 2026) and then approved (4–0–1, October 5, 2026) contracts for Madison staff, a BCBA-certified special educator, the occupational therapy assistant and the speech-language pathologist, to serve Freedom and Tamworth children in the SAU 13 preschool at Madison Elementary, with the added words "as time allows".
    - citation: Madison School Board minutes, September 23, 2026 (draft) and October 5, 2026
    - source: https://drive.google.com/file/d/1WyF6kj-vpCHSJ7hlH0ki2gbDXfM_8kxf/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: October 5: "The agreement is for the district to 'sell' BCBA services to Freedom & Tamworth as part of the ECE program on site at Madison Elementary School. Additional wording will be added to each contract saying, 'as time allows'. ... The motion passed 4-0-1". September 23: "contracts between Madison and Tamworth/Freedom for services related to the SAU Early Childhood Education (ECE) program ... BCBA ... Certified Occupational Therapy Assistant; and Speech Language Pathologist. ... Motion failed 0-4-1". Raw: raw/school/board/madison-sb-minutes-2026-10-05.txt; raw/school/board/madison-sb-minutes-2026-09-23-special-draft.txt.

11. In September 2026 the NH Department of Education selected SAU 13 for Program Approval and General Supervision (PAGS) monitoring, a full review of its special education program, procedures, records, IEPs and evaluations.
    - citation: Madison School Board minutes, September 14, 2026 (Director of Student Services Report)
    - source: https://drive.google.com/file/d/1jW5cNSqj2SZJmecyCZAoSf2NlloZJ3bZ/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: sau 13
    - note: Text: "The SAU received notification from the New Hamshire Department of Education Bureau of Special Education Support that it has been selected for Program Approval & General Supervision (PAGS) monitoring. This is a comprehensive review of the district's special education program, procedures, student records, IEPs, evaluations". An introduction session was set for October 21, 2026 (October packet p. 41). Raw: raw/school/board/madison-sb-minutes-2026-09-14.txt.

## district-preschool: The SAU 13 Integrated Preschool at Madison Elementary

- kind: local
- question_type: local_practice
- description: Public preschool programs by district (already in `additional-data/district-practices.md`)

1. For 2026-27 the SAU 13 Integrated Preschool Program took applications from April 1 to May 1, 2026 "on a first-come, first-served basis"; accepted families had 10 days to return a registration packet with a $100 non-refundable deposit, and spaces not filled or secured were offered to families on the waitlist.
   - citation: SAU 13, "SAU #13 Integrated Early Childhood Program 2026-2027" flyer (linked from the SAU 13 Preschool page)
   - source: https://drive.google.com/file/d/1r8pXF9r_H3pewmqfGYG6aW-mQg97wPUH/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "Registration Period: April 1, 2026 to May 1, 2026 ... Applications accepted until May 1, 2026, on a first-come, first-served basis. Upon acceptance, a registration packet will be sent to you which must be completed and submitted with a $100.00 non-refundable deposit within 10 days to secure enrollment. Unfilled or unsecured spaces after the deadline will be offered to waitlisted applicants". No lottery is described. Dates, sessions and tuition are already in additional-data/district-practices.md (Madison fact 61). Raw: raw/school/sau13/preschool-2026-27-website-info.txt.

2. Tuition for SAU 13 preschool children without an identified disability is billed monthly by the number of school days on the Madison Elementary calendar, with canceled or delayed days credited the next month; families sign a tuition agreement and must show residency in Freedom, Madison or Tamworth.
   - citation: SAU 13, "SAU #13 Integrated Early Childhood Program 2026-2027" flyer
   - source: https://drive.google.com/file/d/1r8pXF9r_H3pewmqfGYG6aW-mQg97wPUH/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "Billed monthly based on student days per the approved MES school calendar; Cancellations or delays will be credited the following month; A completed tuition agreement form is required for enrollment ... Proof of residency in one of the SAU #13 towns, Freedom, Madison, or Tamworth, will be required for enrollment." The daily rates ($11.50 half day, $23.00 full day) are in district-practices.md. Raw: raw/school/sau13/preschool-2026-27-website-info.txt.

3. The SAU 13 preschool at Madison Elementary uses an integrated model that teaches children receiving special education alongside typically developing peers; it enrolled 18 children in 2024-25 (9 from Madison, 7 from Tamworth, 2 from Freedom) and 18 at the start of 2025-26 (8, 7 and 3).
   - citation: Madison School District Annual Report, January 2026, p. 16 (Superintendent of Schools Report)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "offering an integrated model that supports both students receiving special education services and their typically developing peers in a collaborative and inclusive learning environment. During the 2024–2025 school year, total enrollment was 18 students, including 9 from Madison, 7 from Tamworth, and 2 from Freedom. For the 2025–2026 school year, the program continues to serve 18 students, with 8 from Madison, 7 from Tamworth, and 3 from Freedom." Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

4. The SAU 13 preschool had 20 children enrolled in August 2026 and 22 in September 2026, 5 of them with IEPs; 10 of the September children lived in Madison, 3 of whom had IEPs.
   - citation: Madison School Board minutes, August 3, 2026 and September 14, 2026 (Director of Student Services Reports)
   - source: https://drive.google.com/file/d/1jW5cNSqj2SZJmecyCZAoSf2NlloZJ3bZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: September 14: "10 Preschoolers from Madison; 3 Madison students with IEPs; Total 22 students, 5 with IEPs". August 3 (https://drive.google.com/file/d/1xPpM2qPYcMia_sLj-qrNl9ayuqaasHnw/view): "Currently, there are twenty total enrollments. Nine of those students reside in Madison. Out of those nine, two have IEPs." The number of seats is not published, so the chance of a seat cannot be worked out. district-practices.md notes NH DOE counted 21 preschool children at Madison on October 1, 2026. Raw: raw/school/board/madison-sb-minutes-2026-09-14.txt; raw/school/board/madison-sb-minutes-2026-08-03.txt.

5. In September 2026 the SAU 13 preschool was staffed by a special educator serving as coordinator and one paraeducator, with a second paraeducator position open; in October the school was still searching for that paraeducator and using substitutes.
   - citation: Madison School Board packet, October 5, 2026, p. 40; Madison School Board minutes, October 5, 2026
   - source: https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: From the image raw/school/board/png/madison-sb-packet-2026-10-05-p40.png: "Total Madison ECE ... Special Educator: Coordinator for ECE ... Para Educator: 1 (+1 open)". Minutes: "the school is still searching for a second paraprofessional and is currently utilizing substitutes." Raw: raw/school/board/madison-sb-minutes-2026-10-05.txt.

6. SAU 13's October 2026 report lists the related services children receive at the SAU 13 preschool at Madison Elementary: speech sessions of 30 minutes (twice a week for the Freedom and Tamworth children who need them, and once or twice a week for three Madison children), occupational therapy twice a week for 30 minutes for one Tamworth and one Madison child, and no behavior analyst services.
   - citation: Madison School Board packet, October 5, 2026, p. 41 (Early Childhood Education Update)
   - source: https://drive.google.com/file/d/1kJiZTBXODchBP88NUxN4wsXMEUywYloM/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "SPEECH SERVICES: Freedom: 2 Sessions week x 30 minutes; Tamworth: 2 Sessions week x 30 minutes; Madison: 1 sessions week x 30 minutes, 2 sessions week x 30 minutes, 2 sessions week x 30 minutes. OT SERVICES: Freedom: No OT; Tamworth: 2 sessions week x 30 minutes; Madison: 2 sessions week x 30 minutes. BCBA SERVICES: Freedom: No BCBA; Tamworth: No BCBA; Madison: No BCBA". Reading each line as one child is an interpretation. Raw: raw/school/board/madison-sb-packet-2026-10-05.txt.

7. On September 14, 2026 the Madison School Board voted 5–0 to put "Preschool Governance" on the 2027 district warrant as an article, and it confirmed this on October 5, 2026; the wording of the article was not in the November 2 draft warrant.
   - citation: Madison School Board minutes, September 14, 2026 and October 5, 2026
   - source: https://drive.google.com/file/d/1jW5cNSqj2SZJmecyCZAoSf2NlloZJ3bZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: September 14: "Preschool Governance: Deb Parsons motioned to add the Preschool Governance as a warrant article, seconded by Ed Robinson. The motion passed unanimously 5-0-0." October 5: "Preschool Governance: The Board agreed to add this item as a Warrant Article." The November 2, 2026 draft warrant (articles 1–8) has no preschool article (raw/school/board/madison-sb-packet-2026-11-02.txt, pp. 52–54). Raw: raw/school/board/madison-sb-minutes-2026-09-14.txt.

8. Madison Elementary's parent forms page has a separate 2026-27 packet for SAU 13 preschool families, with the same handbooks, school-family compact, free and reduced meal application and housing form as K–6, and notes that some forms say "Madison Elementary because the program is being housed here".
   - citation: Madison Elementary School website, "For Parents"
   - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/for-parents-1
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "SAU #13 ECE PARENT HOMEWORK 2026-27 ... (Some of these do say Madison Elementary because the program is being housed here.)" The linked ECE family handbook (https://drive.google.com/file/d/1-gVTkYdsBK9WYo-3zthAOvCXQpEGOi8g/view) requires a Google sign-in and was not read. Raw: raw/school/mes/for-parents.txt.

## district-student-support: Counseling, Behavior Support, Families and English Learners at Madison Elementary

- kind: local
- question_type: local_practice
- description: Counseling, social work and mental health support, English learner services, homeless student support, welcoming families of all backgrounds, and enrollment documents

1. Madison Elementary has a full-time school counselor who teaches weekly "Success Classes" to all students as part of the integrated arts schedule and gives short-term individual and small-group help based on social-emotional screeners, needs assessments, behavior data and teacher or family concerns.
   - citation: Madison Elementary School Family Handbook 2026-2027, "School Counselor"
   - source: https://docs.google.com/document/d/18meMeocc7iPmnpxYHDobKHm0ZjxbJHiNG5ZBWQjdncc/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "MES has a full-time School Counselor who provides preventative and responsive services ... all students participate in weekly Success Classes, which provide universal instruction through a comprehensive school counseling program ... The counselor also provides short-term individual and small-group interventions based on student needs identified through SEL screeners, needs assessments, behavior data, teacher or family concerns". The board approved the handbook August 3, 2026. Raw: raw/school/docs/mes-family-handbook-2026-27.txt.

2. Madison Elementary's school counselor also serves as the family liaison, connecting families with food, clothing and community services; as the district's homeless liaison, for a group of students the principal says grew significantly in 2025-26; and as the school's 504 coordinator.
   - citation: Madison School District Annual Report, January 2026, p. 21 (Principal's Annual Report, "School Counselor")
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The counselor serves as a family liaison, connecting families with essential resources such as food, clothing, and community support services. She is also the district's homeless liaison, coordinating services for students experiencing housing instability—a population that has increased significantly during the 2025–26 school year. In addition, she serves as the school's 504 coordinator". The handbook also names the counselor as Suicide Prevention Liaison, with the principal as backup. Raw: raw/school/docs/madison-annual-report-jan-2026.txt.

3. Madison Elementary uses the Responsive Classroom approach school-wide and is working to train all its education staff in it; the 2024 annual report says guidance classes had used the Choose Love curriculum for several years.
   - citation: Madison School Board packet, September 14, 2026, p. 19 (Principal's Report); Madison School District Annual Report, January 2024, p. 17
   - source: https://drive.google.com/file/d/1FqIWm7n4M2TEfI9g4t9WY13e4FSF8Itb/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: September 2026: "Responsive Classroom training as we work to have all of our education staff trained." January 2024 report (https://drive.google.com/file/d/17ect0TR75moUGzxU_gjdjDGHg8Gux6UU/view): "We have been using the Choose Love Curriculum in our Guidance classes for the past few years in addition to the implementation of Responsive Classroom". Whether Choose Love is still used in 2026-27 is not stated. Raw: raw/school/board/madison-sb-packet-2026-09-14.txt; raw/school/docs/madison-annual-report-jan-2024.txt.

4. Madison's 2024-25 Title I plan says the school "continues building the process of using a trauma-informed approach" with social-emotional training for all staff, and lists among grant-funded strategies interventionists for social-emotional development under its behavior support system and a school-wide tiered behavior model such as Responsive Classroom.
   - citation: Madison School District, NH DOE Title I, Part A Plan 2024-2025, components 1 and 14
   - source: https://drive.google.com/file/d/14bLrh0SyuHvH0i-lCrnYgMCzeJB54iK0/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Madison continues building the process of using a trauma-informed approach and has a strong focus on providing training to all staff in the areas of social-emotional needs." and "Interventionists to support social emotional development through the schools MTSS-B approach to intervention; Implement a schoolwide tiered model for behavior support, such as Responsive Classroom". No source gives trauma-informed training hours or names a trauma program. Raw: raw/school/docs/madison-title-i-plan-2024-25.txt.

5. Madison Elementary's handbook sorts misbehavior into "minor" problems handled by the classroom teacher, which escalate on repeat to a Student Support referral, and "major" problems handled by the principal, which on a third offense bring a family conference and a referral to the expanded Student Support Team; consequences are meant to be logical and decided case by case.
   - citation: Madison Elementary School Family Handbook 2026-2027, "Behaviors: Minor and Majors" and "Behavior Continuum"
   - source: https://docs.google.com/document/d/18meMeocc7iPmnpxYHDobKHm0ZjxbJHiNG5ZBWQjdncc/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The goal at MES is that all consequences assigned be logical and decided on a case-by-case basis ... Minor behaviors are primarily handled at the classroom level ... the student may process with a teacher from our Support Team or the principal ... Major behaviors will be handled by a building administrator". Continuum: "3rd Offense Referral to Expanded Student Support Team ... Conference with student, teacher, reporting staff, and the parent(s)/guardian". Raw: raw/school/docs/mes-family-handbook-2026-27.txt.

6. In fall 2026 some Madison Elementary paraprofessionals took a professional learning series on understanding student behavior and responding to individual needs, offered through North Country Education Services and led by Jeanine Fitzgerald, and from November all paraprofessionals join a monthly book study led by the special education team.
   - citation: Madison School Board packet, November 2, 2026, p. 12 (Principal's Report, November 2026)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Beginning in November, paraprofessionals will take part in a monthly book study led by our special education team. In addition, several paraprofessionals have participated in a professional learning series offered through North Country Education Services and led by Jeanine Fitzgerald. This series focuses on understanding student behavior and developing effective responses". Raw: raw/school/board/madison-sb-packet-2026-11-02.txt.

7. In August 2022 the Madison School Board accepted a bid from Norcross Circle Associates for a social worker contract paid with federal Title IV grant funds; later reports describe the counselor, not a social worker, as the school's family liaison.
   - citation: Madison School Board minutes, August 1, 2022 (approved)
   - source: https://drive.google.com/file/d/1FIs_5SERTHuH9xxEzrqrAWtSoo_EGJeT/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Award Social Worker Contract – Title IV Grant Funding: The Superintendent recommended accepting the bid from Norcross Circle Associates. Motion by Sarah DeMartino to accept he bid from Norcross Circle Associates ... The motion passed unanimously." No later minutes, budget lines or staff lists checked (2023–2026) mention a social worker. Raw: raw/school/board/older/madison-august-1-2022-approved.txt.

8. Madison Elementary's Title I page says the school counselor is the district's homeless education liaison, works with the SAU's director of student services, the nurse and administrators to identify families in transition and migrant students, and that the director's office monitors students in foster care, with immediate enrollment and transportation planning.
   - citation: Madison Elementary School website, "Title I"
   - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/for-parents-1/title-i
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Each district is required to appoint a Homeless Education Liaison, MES school counselor ... The Homeless Liaison is in communication with the Director of Student Services, school nurse, and administration to help identify families in transition and migrant students. The Director of Student Services' office monitors students in foster care. The District is committed to ensuring the same quality educational services for homeless, foster and migrant students by ensuring immediate enrollment and determining transportation needs." Federal and state rules are in the library (foster-care-school-stability and related). Raw: raw/school/mes/title-i.txt.

9. Madison's Title I plan says money set aside for homeless students can pay for clothing, fees for school activities such as the ski and skate program, field trips, musical instrument rental and school supplies, plus tutoring, counseling and transportation to the school of origin when in the child's interest; the 2026-27 parent packet includes a housing information form.
   - citation: Madison School District, NH DOE Title I, Part A Plan 2024-2025, component 6
   - source: https://drive.google.com/file/d/14bLrh0SyuHvH0i-lCrnYgMCzeJB54iK0/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "These services, materials and supplies range from clothing and fees so the students (who qualify) may participate in other school wide activities such as our ski/skate program, cover field trip costs or pay for the rental of a musical instrument ... Madison School District will provide transportation assistance to ensure that homeless students can attend their school of origin, if feasible and in the student's best interest ... including tutoring, counseling". The "Housing Information Form" is listed on the For Parents page (raw/school/mes/for-parents.txt). Raw: raw/school/docs/madison-title-i-plan-2024-25.txt.

10. Madison Elementary lists community partners for student health and needs: dental hygiene visits by Conway Village Dental, vision screening by the Conway Area Lions Club, free flu vaccine through the Carroll County Coalition for Public Health, healthy relationship lessons with Starting Point, hygiene bags for grades 5–6 from the PTO, winter clothing from the Madison Food Pantry and shoe gift cards from a Madison church.
    - citation: Madison School District Report Card, Fall 2025, p. 3 (January 2026 Annual Report, p. 25)
    - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p28.png: "PARTNERS WITH LOCAL COMMUNITY RESOURCES: Dental Hygiene Visit- Conway Village Dental; Vision Screening- Conway Area Lions Club; Free Student Influenza Vaccine- Carroll County Coalition for Public Health; Healthy Relationship Education- Starting Point Collaboration; Hygiene Bags for Students in Grades 5 & 6- MES PTO; Winter Clothing and Other Student Needs- Madison Food Pantry; Shoe Gift Cards- Madison Church". The church is not named further.

11. Madison Elementary's fall 2025 report card says 54% of its students have at least one "at-risk" factor: low income (free or reduced lunch), being a student in transition without stable housing, living under guardianship, or a single parent or separated parents with split schedules.
    - citation: Madison School District Report Card, Fall 2025, p. 8 (January 2026 Annual Report, p. 30)
    - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p33.png: "54% OF STUDENTS Identified as having one or more 'at-risk' factors ... Low socio-economic status generally based on qualification for free/reduced lunch program; Identified as a student in transition lacking stable permanent housing; Students under guardianship; Students who have a single parent or whose parents are separated resulting in split schedules and potential changes in housing".

12. In October 2026 Madison Elementary's K–6 students went to Freedom Elementary for the "Tiger" presentation on strategies for managing stress and anxiety.
    - citation: Madison School Board minutes, October 5, 2026 (Principal's Report)
    - source: https://drive.google.com/file/d/1WyF6kj-vpCHSJ7hlH0ki2gbDXfM_8kxf/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "Students in Gr. K-6 visited Freedom Elementary School for the 'Tiger' presentation; students were engaged and learned strategies for managing stress and anxiety." Raw: raw/school/board/madison-sb-minutes-2026-10-05.txt.

13. Madison buys English for Speakers of Other Languages (ESOL) instruction as an outside service: the 2026-27 budget has a $20,000 "ESOL Services" purchased-services line, none of which had been spent by August 31, 2026, and the line was level-funded in the budget prepared in December 2024.
    - citation: Madison School Board packet, September 14, 2026 (2026-2027 expenditure report through August 31, 2026); Madison School Board minutes, December 16, 2024
    - source: https://drive.google.com/file/d/1FqIWm7n4M2TEfI9g4t9WY13e4FSF8Itb/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Report row: "01.2190.300.120 ESOL SERVICES $20,000.00 $0.00 $0.00 $20,000.00 ... 100.00%" (object 300 = purchased professional services). December 16, 2024: "ESOL – Level funded." November 7, 2022 minutes (https://drive.google.com/file/d/1DCbJe2VV-de_6EiBXuXnFVZfukVHY1C7/view): "ESOL (English teachers of other languages) is up based on student needs." The provider and hours are not named. Raw: raw/school/board/madison-sb-packet-2026-09-14.txt; raw/school/board/older/madison-december-16-2024-approved-minutes.txt; raw/school/board/older/madison-november-7-2022-approved.txt.

14. Madison policy IHBBA, on limited English proficiency instruction (readopted 2014), says that if the district receives federal funds for such programs, parents will be told why their child was placed in a language program, the child's English level and progress, the teaching method, how the program helps the child learn English, and the exit requirements.
    - citation: Madison School Board Policy IHBBA, Limited English Proficiency Instruction
    - source: https://drive.google.com/file/d/1dYk6OO7BgH4qvhTl6XFsDp2gM_lW6OW2/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "If the Madison School District receives federal funding for Limited English Proficient (LEP) Programs, the following will be provided: 1. Parents will be notified of their student's placement in a language program ... E. Exit requirements for the program." The policy cites the No Child Left Behind Act of 2001, since replaced by ESSA. Statewide rights are in the library slug english-learner-rights. Raw: raw/school/policies/madison-policy-ihbba.txt.

15. NH DOE data in the site's database show Madison with 0 current English learners and 2 former English learners being monitored in 2025-26, and between 0 and 5 current English learners each year since 2014.
    - citation: NH DOE English learner counts in the site's database (district 333)
    - source: https://www.education.nh.gov/data-reports
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: district_english_learner rows: 2026 eligible 0, monitor 2; 2025 eligible 1, monitor 3; peak 5 in 2020 and 2021. The Ask can fetch these directly; this fact only links them to the services above. Raw: raw/school/site-data/madison-elementary-site-data-2026-11-13.txt.

## district-meals: Weekend Food Bags and Meal Access at Madison Elementary

- kind: local
- question_type: local_practice
- description: School meals: what is served, prices, free and reduced-price applications, meal charges, summer meals, food service providers and local food

1. Madison Elementary's report card says the school makes food available to every student "so no one feels targeted or singled out": breakfast and lunch through the National School Lunch Program, daily fresh fruit or vegetables through a federal grant, classroom snacks donated by the Madison Food Pantry, and weekend food bags through End 68 Hours of Hunger for all students.
   - citation: Madison School District Report Card, Fall 2025, p. 3 (January 2026 Annual Report, p. 25)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p28.png: "While fulfilling a need for those who have food insecurity, we make food available to all students so no one feels targeted or singled out. ... The Fresh Fruits and Vegetables Grant provides each student the opportunity to access fresh fruits or vegetables every day. Additional snacks- The Madison Food Pantry generously supplies our school with snacks ... All students have access to weekend food bags through End 68 Hours of Hunger."

2. Madison Elementary's End 68 Hours of Hunger bags hold kid-friendly, non-perishable breakfast, lunch and dinner foods, are packed each week and sent home with students on Friday afternoons at no cost, and any family can sign up at any time by contacting the school counselor by email, phone or ClassDojo message.
   - citation: MES newsletters, September 8, 2025 and November 3, 2025
   - source: https://docs.google.com/presentation/d/1g67Cz2AkIzqIkTdTOnFszkzvG_IRmNbJv8Am0BL8wQ0/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: November 3, 2025: "All students are welcome to receive a weekend food bag through the End 68 Hours of Hunger program. Each bag includes kid-friendly, easy-to-prepare, non-perishable foods for breakfast, lunch, and dinner. Bags are packed weekly and sent home with students every Friday afternoon—at no cost to families. ... Just say 'yes'—and we'll take care of the rest!" September 8, 2025 (https://docs.google.com/presentation/d/1bot42BvB1lO0RZfFMhtKLRZUbH2hE9rWNW-fOadqZ1w/edit): "We have a weekend food program in SAU 13 and 9 to help!" Raw: raw/school/newsletters/mes-nl-11.3.25.txt; raw/school/newsletters/mes-nl-9.8.25.txt.

3. Madison Elementary's report card gives its free and reduced-price lunch rate on October 31 as 43% in 2025, 30% in 2024, 35% in 2023 and 2022, 39% in 2021 and 41% in 2020, against a statewide rate of 21% to 24% in those years.
   - citation: Madison School District Report Card, Fall 2025, p. 3 (January 2026 Annual Report, p. 25)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p28.png: "As of Oct. 31 2025 2024 2023 2022 2021 2020; Enrollment 102 110 113 125 127 127; Free/Reduced Lunch Rate 43% 30% 35% 35% 39% 41%; State Avg. F/R Rate (Rounded) 23% 24% 24% 24% 21% 21%". The site's database has the official NH DOE counts (44 of 102 eligible in 2025-26, 43.1%, derived; 37 of 110 in 2024-25, 33.6%), which differ slightly for 2024.

4. On October 5, 2026 the Madison School Board asked the administration for a proposal on what universal free meals, particularly breakfast, would cost the district.
   - citation: Madison School Board minutes, October 5, 2026 (Budget Discussion, Board Feedback)
   - source: https://drive.google.com/file/d/1WyF6kj-vpCHSJ7hlH0ki2gbDXfM_8kxf/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The board also requested a proposal on what universal feeding, particularly breakfast, would look like financially." Raw: raw/school/board/madison-sb-minutes-2026-10-05.txt.

## district-safety-and-security: Building Security, Emergency Plans and Drills at Madison Elementary

- kind: local
- question_type: local_practice
- description: Building security, visitor rules, drills and emergency plans, and school security grants

1. At Madison Elementary all visitors park near the Little Red School House, enter through the front lobby doors and sign in at the office; all other doors are kept secured, and students arriving after 9:07 am also come in through the front door.
   - citation: Madison Elementary School Family Handbook 2026-2027, "Access to the Building" and "Arrival"
   - source: https://docs.google.com/document/d/18meMeocc7iPmnpxYHDobKHm0ZjxbJHiNG5ZBWQjdncc/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "All visitors should park near the Little Red School House. For the security and safety of our students and staff, all visitors to our school must use the front lobby doors and sign-in in the Office. All other doors are secured." and "The doors are closed at 9:07 AM, any students arriving after that are considered tardy and must enter through the front door". Policy KI (raw/school/policies/madison-policy-ki.txt) requires all visitors to report to the office. No source describes a secure vestibule. Raw: raw/school/docs/mes-family-handbook-2026-27.txt.

2. Madison Elementary has security cameras inside and outside the building, placed only in public areas such as entrances, hallways, the gym and cafeteria and the building's exterior, and never in classrooms, offices, restrooms or changing areas.
   - citation: Madison Elementary School Family Handbook 2026-2027, "Cameras"
   - source: https://docs.google.com/document/d/18meMeocc7iPmnpxYHDobKHm0ZjxbJHiNG5ZBWQjdncc/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Madison Elementary School has cameras that provide surveillance inside and outside the school building. ... school entrances, hallways, gymnasium/cafeteria, exterior of buildings and other open areas on campus. The cameras will not be installed in any place ... such as classrooms, offices, teacher workrooms, restrooms, locker rooms". Raw: raw/school/docs/mes-family-handbook-2026-27.txt.

3. In June 2023, after state security grants "fell through", the Madison School Board approved security bids from Pope Security, discussed in non-public session, with up to $60,000 to come from the district's retained fund balance.
   - citation: Madison School Board minutes, June 5, 2023 (approved August 7, 2023)
   - source: https://drive.google.com/file/d/1pVHacAiC-b8wvzpG-oZ9VC0E1jmQcI2U/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Public hearing: "Michael Wade said our security grants fell through but we are looking at using up to $60,000 from the FY22 retained fund balance of $139,608 for security matters." Vote: "Motion by Jeremy Cox to approve security bids from Pope Security that were discussed in non-public session, with up to $60,000 to come from the 2.5% fund balance retention ... The motion passed unanimously." What the bids covered is not in the public minutes. Raw: raw/school/board/older/madison-june-5-2023-approved.txt.

4. Madison's capital improvement plan (updated May 21, 2026) lists a camera and alarm security system bought from Pope Security in 2023 for $85,000, due for replacement in 2033 at a projected $108,807 with $10,881 a year set aside, and detectors bought in 2022 for $10,000, due in 2032.
   - citation: Madison School District Capital Improvement Plan, in the Madison School Board packet of November 2, 2026, p. 16
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Read from the image raw/school/board/png/madison-sb-packet-2026-11-02-p16.png: "Security System (Cameras, Alarm) | Priority 1 | $108,807 | $85,000 | 2023 Pope Security | 2033 | 10 | 10,881" and "Detectors | 1 | $12,801 | $10,000 | 2022 Pope Security | 2032 | 10 | 1,280". The January 2024 plan also listed "Existing Cameras (32)" installed in 2015 by Pope Security (raw/school/docs/madison-annual-report-jan-2024.txt). The rest of the plan is in agent 4's file.

5. In the state's Security Action for Education (SAFE) grants, the Madison School District applied for 2 projects totaling $65,000 in Rounds 1 and 2 (2022) and neither was funded, and it did not apply in Round 3 (2023).
   - citation: NH DOE, "Security Action for Education (SAFE) Grant" handout, list of all awards, last revised December 13, 2024, page 2 of 7
   - source: https://gc.nh.gov/lba/budget/operating_budgets/2026-2027/HF_Division_II/Division%20II%20-%20NHED%20SAFE%20Grants%20(PSIF)%20Overview%20-%2012-13-24.pdf
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Row text: "13 Madison 2 65,000$ 0 ‐$ 2 65,000$ 0 ‐$ 0 ‐$ 0 ‐$ 0 ‐$"; columns checked on the page image raw/school/state/safe-grants-p4.png (Round 1 & 2: apps, requested, apps funded, funded, apps not funded, not funded; Round 3: apps, requested, funded ...). SAFE grants pay 100% of access control, surveillance or emergency alerting projects up to $100,000 per school. Madison's 2026 (Round 4) result was not found. Raw: raw/school/state/safe-grants-psif-overview-2024-12-13.pdf (.txt).

6. In December 2025 Madison's Building and Grounds committee was looking at adding a power line from the school's existing generator so it would also keep the security cameras, phones and internet running.
   - citation: Madison School Board minutes, December 1, 2025 (approved)
   - source: https://drive.google.com/file/d/1yfnXWDOyeFvvHpAJCQq-DWHntkuzpq6r/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Building & Grounds is currently looking into adding an additional line of power from the existing generator to include coverage for security cameras, phone & internet." No later decision was found. Raw: raw/school/board/older/madison-december-1-2025-approved-minutes.txt.

7. In September 2026, during the change to a new bus company, Madison Elementary's principal reported that work was under way to get the bus radios fully running; no source describes radio boosters or other radio equipment inside the school.
   - citation: Madison School Board minutes, September 14, 2026 (Principal's Report, Transportation Update)
   - source: https://drive.google.com/file/d/1jW5cNSqj2SZJmecyCZAoSf2NlloZJ3bZ/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "New Vendor Transition: There have been a few initial bumps during the transition to the new bus company. Communications: Work is underway to get the bus radios fully up and running." The second clause states a gap. Raw: raw/school/board/madison-sb-minutes-2026-09-14.txt.

8. Madison policy EBCA (2018) makes the superintendent responsible for an emergency response plan that meets RSA 189:64 and covers violence, threats, natural disasters, fire, hazardous materials and medical emergencies; site plans are reviewed every year, emergency response drills are held at least twice a year, and the superintendent works with local and state emergency and law enforcement agencies.
   - citation: Madison School Board Policy EBCA, Emergency Plans (readopted July 2, 2018)
   - source: https://drive.google.com/file/d/1m3jHvukLIXx8L7aFOKh2i_qBA3w66shB/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "The Superintendent is responsible for ensuring that at least two times per year, the District conducts emergency response drills. The Superintendent will establish a relationship with local and state emergency and law enforcement authorities." A new SAU-wide EBCA had its first reading on November 2, 2026 (fact 12). Raw: raw/school/policies/madison-policy-ebca.txt.

9. Madison policy EBCB calls for a fire drill at least once a month while school is in session; under RSA 189:64, at least 4 of a school's required fire drills must be all-hazard drills, one of them testing the response to an armed assailant (which may be a discussion), with the drill types set by the school together with local public safety, emergency management and public health officials.
   - citation: Madison School Board Policy EBCB, Fire Drills (readopted August 4, 2014); RSA 189:64, III
   - source: https://drive.google.com/file/d/1lpHk3B3qJr7-bC96z-a3meWpyUq2DgFQ/view
   - as_of: 2026-11-13
   - review_by: 2027-08-15
   - place: district Madison
   - note: EBCB: "Fire Drills should be conducted at least once per month while school is in session." RSA 189:64, III (https://gc.nh.gov/rsa/html/XV/189/189-64.htm): "at least 4 of the currently required number of fire evacuation drills shall be emergency, all-hazard response drills of which at least one shall test emergency response to an armed assailant. The armed assailant drill may be discussion based. The types of all-hazard drills ... shall be determined by the school in collaboration with local public safety, emergency management, and public health officials. The school may include students and first responders". review_by follows the state-law rule. Raw: raw/school/policies/madison-policy-ebcb.txt; raw/school/state/rsa-189-64.txt.

10. SAU 13's school safety policy EBB, adopted by all three boards in 2023, has the superintendent keep a district safety plan that includes each school's emergency operations plan, drills for fire and all hazards, procedures for visitors, and regular security assessments by school safety professionals and law enforcement officers.
    - citation: Freedom, Madison & Tamworth School Board Policy EBB, School Safety Program (Madison adoption May 1, 2023)
    - source: https://drive.google.com/file/d/1lE2F33hcw6TGtsbgqGhS-30uh9NcUhMR/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: sau 13
    - note: Text: "5. Training programs for staff and students in emergency response procedures that include practice drills for fire and all hazard as required by law and Board policy EBCB. ... 10. Procedures for regular assessments by school security/safety professionals and law enforcement officers to evaluate the security needs of each school building". Raw: raw/school/policies/madison-policy-ebb.txt.

11. On October 5, 2026 the Madison School Board approved the district's Emergency Operations Plan in a non-public session held under RSA 91-A:3, II(i), the exemption for emergency plans meant to thwart deliberate acts of violence, so the plan itself is not public.
    - citation: Madison School Board minutes, October 5, 2026
    - source: https://drive.google.com/file/d/1WyF6kj-vpCHSJ7hlH0ki2gbDXfM_8kxf/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "Deb Parsons motioned to go into non-public to consider matters relating to the preparation for and the carrying out of emergency functions ... specifically to discuss and approve the School District Emergency Operations Procedures ... Action as a Result of Non – Public Session: The board approved the Emergency Operation Plan (EOP)." Raw: raw/school/board/madison-sb-minutes-2026-10-05.txt.

12. A draft SAU-wide policy EBCA, first read by the Madison board on November 2, 2026, would have each principal review the school's emergency operations plan by October 10 each year, the plan or a no-change notice go to the state by October 15, a district crisis plan go to the board by October 31, and the superintendent coordinate with police, fire and ambulance services.
    - citation: Madison School Board packet, November 2, 2026, pp. 121–123 (draft Freedom, Madison & Tamworth School Board Policy EBCA, Crisis Prevention and Emergency Response Plans)
    - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: sau 13
    - note: Text: "School building principals, or their designee, shall annually review their site-specific EOP and submit updated plans (or report of no changes) to the Superintendent for review by October 10th. ... The District Crisis Plan shall be updated and provided to the Board for review by October 31 each year ... The Superintendent will establish a relationship with local and state emergency services (e.g., police, fire, ambulance, etc.)." The adoption dates in the draft are blank. Raw: raw/school/board/madison-sb-packet-2026-11-02.txt.

13. Madison Elementary held a school safety week of drills at the start of the 2025-26 year, with teachers reviewing each drill with students beforehand, and at a November 2023 teacher workshop the Madison police chief led staff discussions on armed assailant drills.
    - citation: MES newsletter, September 8, 2025; Madison School Board minutes, September 8, 2025 and November 6, 2023
    - source: https://docs.google.com/presentation/d/1bot42BvB1lO0RZfFMhtKLRZUbH2hE9rWNW-fOadqZ1w/edit
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Newsletter: "This week we will practice school safety drills ... Classroom teachers are reviewing these drills with students prior to each one happening so that students are prepared." September 8, 2025 minutes (https://drive.google.com/file/d/1FpENUE8LQy60h6XpLOWSJ1PXEe315BGp/view): "This week is school safety week we are practicing safety drills." November 6, 2023 (https://drive.google.com/file/d/1-TfGma0BoUmKlKVn92L2dZM-xVohPCzN/view): "November 9 Teacher Workshop Day: Heather said Chief Bob King will be in with discussions about armed assailant drills". How often police or fire join drills is not stated anywhere found. Raw: raw/school/newsletters/mes-nl-9.8.25.txt; raw/school/board/older/madison-september-8-2025-approved-minutes.txt; raw/school/board/older/madison-november-6-2023-approved-minutes.txt.

14. In 2025-26 a Madison Police officer taught the ten-week DARE (Drug Abuse Resistance Education) program to Madison Elementary's grades 5–6 together with the school counselor and nurse, ending with a graduation in April 2026; staff noted the program had returned after a gap.
    - citation: Madison School Board minutes, May 4, 2026 (MES Staff/Student Presentation); MES newsletter, April 6, 2026
    - source: https://drive.google.com/file/d/1-hgBx39Uwc9eF93kr91uREOtF2dpTsr_/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "The ten-week program involved meeting once a week with the School Guidance Counselor ..., School Nurse ..., and Madison Police Officer Tessa Llewellyn. Heather O'Donnell expressed gratitude for the return of the program". No school source mentions a school resource officer (SRO) for MES or SAU 13; checked the 2026-27 handbook, MES and SAU 13 pages, annual reports for 2024 and 2026, and board minutes 2022–2026. Police staffing is in agent 5's file. Raw: raw/school/board/older/madison-may-4-2026-approved-minutes.txt; raw/school/newsletters/mes-newsletter-4.6.2026.txt.

15. Madison policy ECA calls for close cooperation with local police and fire departments, a key-control system limiting building access to authorized staff, and locking buildings after the last activity of the day.
    - citation: Madison School Board Policy ECA, Buildings and Grounds Security (readopted August 4, 2014)
    - source: https://drive.google.com/file/d/1nX3LvzD2dDKuNLIY0zd2RlfSSZAC1Cw2/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "The Madison School Board requires and encourages close cooperation with local police and fire departments, and with insurance company inspectors. ... An adequate key control system shall be established ... School buildings shall be closed and locked after the last school activity has concluded". Raw: raw/school/policies/madison-policy-eca.txt.

## district-volunteers-and-partners: Volunteers, Gifts, the PTO and Community Partners at Madison Elementary

- kind: local
- question_type: local_practice
- description: How residents, families and community groups can volunteer at, donate to or partner with a district's schools: volunteer rules and background checks, parent groups, gifts, student privacy and community programs

1. SAU 13's volunteer policy IJOC requires a background investigation and criminal records check for "designated volunteers", those who work with students daily, regularly or one-on-one; other volunteers helping with a single presentation or occasional event must always be with staff and may never be alone with students.
   - citation: Freedom, Madison & Tamworth School Board Policy IJOC, Volunteers (Madison adoption December 2, 2024)
   - source: https://drive.google.com/file/d/1M_ZGGFbMWpHAgudaYC55brBQ6oZOUtfs/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "'Designated volunteer' means any volunteer who: 1. Comes in direct contact with pupils on a daily basis; 2. Meets regularly with students; 3. Meets with students on a one-on-one basis ... Undesignated volunteers, assisting for a single presentation or occasional event, must always be accompanied by staff while on school premises. At no time shall any undesignated volunteer be alone with a student". Raw: raw/school/policies/madison-policy-ijoc.txt.

2. Under SAU 13 policy IJOC, people who want to volunteer fill out an application at the principal's office describing their skills and availability; volunteers are placed only with teachers who asked for help, get an orientation and building-level training, work under certified staff on supervisory, tutoring, clerical and preparation tasks, and may share special talents or hobbies with students on a schedule.
   - citation: Freedom, Madison & Tamworth School Board Policy IJOC, Volunteers
   - source: https://drive.google.com/file/d/1M_ZGGFbMWpHAgudaYC55brBQ6oZOUtfs/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Text: "Persons wishing to volunteer at the District should complete a Volunteer Application form describing their skills, interests and availability. Such forms will be made available at the Principal's office. ... Volunteers shall be assigned only to those teachers who have requested volunteer assistance. ... Assignments shall be limited to assisting staff members with duties such as routine supervisory, tutorial, clerical, housekeeping and material preparation tasks. ... Volunteers with special talents, hobbies or experiences may share those with students on a scheduled basis". Raw: raw/school/policies/madison-policy-ijoc.txt.

3. Madison Elementary's handbook says the school sends a volunteer survey home each September; classroom helpers, field trip chaperones, homeroom parents and PTO volunteers who are not "designated volunteers" need no background check but must be supervised by staff, and every volunteer gets a "Notice to Volunteers" covering chaperone rules, drug-free schools, privacy and bullying law.
   - citation: Madison Elementary School Family Handbook 2026-2027, "Volunteer Program"
   - source: https://docs.google.com/document/d/18meMeocc7iPmnpxYHDobKHm0ZjxbJHiNG5ZBWQjdncc/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "A survey will be sent home in September asking for volunteer support ... Volunteers (e.g. field trip chaperones, classroom assistants and helpers, homeroom parents, PTO volunteers) who are not 'designated volunteers' are not required to have a Background Investigation and Criminal Records Check. Volunteers who are not 'designated volunteers' must always be supervised by a staff member". Raw: raw/school/docs/mes-family-handbook-2026-27.txt.

4. Madison Elementary asks every volunteer and substitute to review the SAU 13 bullying tool kit and short videos on using an EpiPen and on bloodborne pathogens and to return a signed page to the office, and says only volunteers with a recent background check may be alone with students.
   - citation: Madison Elementary School website, "For Community, Substitutes, & Volunteers"
   - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/for-communitysubstitutesvolunteers
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "Only those volunteers with a recent background check are permitted to be alone with students. ... SAU #13 Bullying Tool Kit-required to be reviewed by all Staff, Substitutes and Volunteers; How To Use An Epi Pen; Blood Borne Pathogens; A signature page is required for all volunteers and substitutes." Raw: raw/school/mes/community-subs-volunteers.txt.

5. SAU 13 requires staff, substitutes, volunteers and contractors to complete a criminal history records check before they start: they book a fingerprinting appointment at a NH State Police barracks (such as Troop E) online, results go straight to the SAU office within about 4 weeks, and the state fee is $25 for a volunteer and $50 for an employee, substitute or contractor; under policy GBCD the districts pay the check fees of individual applicants not employed by a contractor.
   - citation: SAU 13, "Background Check Process" / Volunteer Form; Freedom, Madison & Tamworth School Board Policy GBCD, section 6
   - source: https://drive.google.com/file/d/1HKLhjUuPWWLX-iV8qX2ouifm_jaqN5od/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: sau 13
   - note: Form: "Schedule an appointment at a NH State Police Barracks (ex: Troop E) ... Please allow up to 4 weeks for fingerprint submissions to be processed. ... Employee/Substitute/Contracted Service $50.00 ... Volunteer $25.00". GBCD (https://drive.google.com/file/d/1rawI4Rf_L8EWvS8hIi0mFtMUFyummCSM/view): "The CHRC fees of individual applicants not otherwise employed by third party contractors/organizations shall be paid by the Districts." The MES page still shows older fees ($48.25 and $21.25) and says "you may request reimbursement". Raw: raw/school/sau13/volunteer-form.txt; raw/school/policies/madison-policy-gbcd.txt; raw/school/mes/community-subs-volunteers.txt.

6. Madison Elementary's PTO meets monthly; its stated goals are to support classrooms and teachers, give extra financial support, connect home and school, and complete two main projects a year, and its events include Read Across America, a calendar raffle fundraiser and Teacher Appreciation Week.
   - citation: Madison Elementary School website, "PTO"; Family Handbook 2026-2027, "Parent/Teacher Organization"
   - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/for-parents-1/pto
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Page text: "Provide support for classrooms and teachers. Provide supplemental financial support for the benefit of the elementary school experience. Work to enhance the sense of community connection between home and school. 4. Accomplish two primary projects within the school year". Handbook: "The PTO has been established as a vehicle for parental involvement. Meetings are scheduled monthly." The page also names the officers. Raw: raw/school/mes/pto.txt; raw/school/docs/mes-family-handbook-2026-27.txt.

7. Madison Elementary's principal wrote in November 2026 that a small core group runs the PTO, which provides basic-needs and hygiene kits for students, runs a cabin at Halloween Town and the Re-Store, funds special events and visiting presenters, gives staff appreciation gifts, awards scholarships to graduating high school seniors and sponsors parent nights.
   - citation: Madison School Board packet, November 2, 2026, p. 13 (Principal's Report)
   - source: https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Text: "There is a small core group of individuals who work hard ... Their efforts include providing basic-needs and hygiene kits for students, hosting a cabin at Halloween Town, continuing the tradition of Re-Store, and raising funds to support special events and visiting presenters ... They also provide staff appreciation gifts and treats, award scholarships to graduating high school seniors, and support families through sponsored parent nights." Raw: raw/school/board/madison-sb-packet-2026-11-02.txt.

8. Madison Elementary lists these community connections: Believe in Books, fall and spring community lunches with a student play, Green Mountain Conservation Group school programs, the Kiwanis book giveaway, the Madison Recreation Department, OASIS intergenerational tutoring, student-led Veterans Day assemblies and Tin Mountain Conservation Center school programs.
   - citation: Madison School District Report Card, Fall 2025, p. 5 (January 2026 Annual Report, p. 27)
   - source: https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: From the image raw/school/docs/png/madison-annual-report-jan-2026-p30.png under "Madison Community Connections": "Believe in Books; Fall & Spring Community Lunch & a Play Performance; Green Mt. Conservation Integrated School Programs; Kiwanis Book Giveaway; Madison Recreation Department; OASIS Intergenerational Tutoring; Student Led Veterans Day Assemblies; Tin Mountain School Programs". How to join OASIS tutoring at MES was not found; OASIS's national site lists no New Hampshire location in search results.

9. Madison Elementary's ski program with the Eastern Slope Ski Club at King Pine, part of PE for grades 1–6, depends on volunteers, and the school held a volunteer and parent information night on November 12, 2026.
   - citation: MES newsletter, 2026-27 (November 2026); Family Handbook 2026-2027, "Ski Program & Winter Sports Program"
   - source: https://docs.google.com/presentation/d/1WSF03hhXUwWcpAGsQUF0qdmzKE4UD3sOaKWVJJIA1mY/edit
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district Madison
   - note: Newsletter: "For those of you planning to volunteer during our ESSC Ski Program this year, please be sure to join us on Nov. 12 in the gym for our Volunteer and Parent Info Night." Handbook: "The ESSC ski program is available to all students in grades 1-6 for minimal cost. ... Volunteer support is critical; please call for more information." Raw: raw/school/newsletters/mes-newsletter-26.27.txt; raw/school/docs/mes-family-handbook-2026-27.txt.

10. Madison Elementary's grade 3–4 maple sugaring program is supported by three nearby sugar houses (Mooney Hill Maples, Turkey Street Maples and Mac Hill Maple) that donate supplies or advice, and by White Mountain Oil & Propane, which donates all the propane used to boil sap.
    - citation: MES newsletter, May 11, 2026
    - source: https://docs.google.com/presentation/d/19mlUVFWZ0OppnKgAcx5DW77JD0XtnA0GrJynr6ZCsMk/edit
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Text: "We have generous support from 3 sugar houses in our immediate area: Mooney Hill Maples, Turkey Street Maples and Mac Hill Maple. ... White Mountain Oil & Propane has also played a huge part in our program, donating all of the propane needed". Raw: raw/school/newsletters/mes-nl-5.11.26.txt.

11. SAU 13's gifts policy KCD encourages groups and individuals to talk with the principal or superintendent first about what gifts are needed; the superintendent may accept gifts of $2,500 or less, larger gifts need a board vote, gifts of $20,000 or more need a public hearing, and online crowdfunding for a school or class must be approved under policy DFGA.
    - citation: Freedom, Madison & Tamworth School Board Policy KCD, Public Gifts/Donations (Madison readings December 4, 2023 and January 8, 2024)
    - source: https://drive.google.com/file/d/15kwQhjeUeNTh7ZH1HbSTVxji6pS9ioGE/view
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: sau 13
    - note: Text: "Individuals or groups contemplating presenting a gift to a school or the District shall be encouraged to discuss in advance with the Building Principal or the Superintendent what gifts are appropriate and needed. ... The Superintendent may accept gifts subject to the terms of this policy in the amount of $2,500.00 or less. ... Gifts of more than $2,500.00 may be accepted only by the Board. ... gifts in the amount of $20,000.00 or more shall require the Board to hold a public hearing ... Active solicitation of gifts ... through online crowdfunding or donor web sites ... must be approved in accordance with Board policy DFGA." Raw: raw/school/policies/madison-policy-kcd.txt.

12. Community groups can request use of Madison Elementary's building or its kitchen with facility use forms posted on the school's community page.
    - citation: Madison Elementary School website, "For Community, Substitutes, & Volunteers"
    - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/for-communitysubstitutesvolunteers
    - as_of: 2026-11-13
    - review_by: 2027-11-13
    - place: district Madison
    - note: Page text: "Community Forms: Facility Use Form; Facility Use Form-Kitchen". The forms (Google Drive PDFs) were not opened. Raw: raw/school/mes/community-subs-volunteers.txt.

## madison_elementary_enrollment_by_grade: Madison Elementary K–6 Enrollment by Grade

- unit: count
- period: October 1, 2021 to October 1, 2025 (official counts); October 23, 2026 (principal's count); year: 2022–2027 (school year end)
- source: Madison School District Annual Report, January 2026, p. 75 — https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view ; 2026-27 row: Madison School Board packet, November 2, 2026, p. 14 — https://drive.google.com/file/d/1S3i9eZFdhY96rYezX9LrUwZHfyRIBHiz/view
- as_of: 2026-11-13
- raw: raw/school/docs/png/madison-annual-report-jan-2026-p78.png; raw/school/board/png/madison-sb-packet-2026-11-02-p14.png
- note: The site's database already holds official enrollment by grade through 2024-25; this table adds October 2025 and fall 2026. The 2026-27 row is not the official October 1 count. Preschool is not included (10 Madison preschoolers in fall 2026). Years 2016–2020 are on the same page: 131, 137, 134, 139, 127.

| Place | Year | K | Gr. 1 | Gr. 2 | Gr. 3 | Gr. 4 | Gr. 5 | Gr. 6 | Total K–6 | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| Madison (333) | Oct 1, 2021 | 13 | 15 | 24 | 20 | 20 | 23 | 15 | 130 | official |
| Madison (333) | Oct 1, 2022 | 13 | 14 | 14 | 25 | 17 | 19 | 22 | 124 | official |
| Madison (333) | Oct 1, 2023 | 16 | 12 | 14 | 12 | 26 | 16 | 18 | 114 | official |
| Madison (333) | Oct 1, 2024 | 11 | 18 | 11 | 17 | 11 | 26 | 16 | 110 | official |
| Madison (333) | Oct 1, 2025 | 10 | 11 | 14 | 12 | 16 | 12 | 27 | 102 | official |
| Madison (333) | Oct 23, 2026 | 12 | 11 | 12 | 14 | 12 | 17 | 12 | 90 | principal's count; total derived (packet total of 100 includes 10 PreK) |

## madison_elementary_staff_by_role: Madison Elementary Staff by Role, FY2022–FY2026

- unit: count (positions; some part-time as noted)
- period: fiscal years 2022 to 2026 (FY26 = 2025-26); year: 2022–2026
- source: Madison School District Report Card, Fall 2025, p. 6 (January 2026 Annual Report, p. 28) — https://drive.google.com/file/d/1lceCBlc7Itp358OCJ15ZLGMK1FJBpUJq/view
- as_of: 2026-11-13
- raw: raw/school/docs/png/madison-annual-report-jan-2026-p31.png
- note: Transcribed from the page image. "Intervention teachers" are the reading specialist, RTI and student support teachers; "@.5" means half-time positions. Special education teachers include the speech-language pathologist. Integrated arts (library/media, PE, art, music) were 1 full-time plus part-time positions each year (FY26: 1 full-time, 2 at 0.6 FTE, 1 at 0.4 FTE). The site's database holds NH DOE staff FTE by category, which counts differently.

| Place | Year | Highest student count | Classroom teachers | Intervention teachers | Special education teachers | Counselor and nurse | Paraprofessionals | Note |
|---|---|---|---|---|---|---|---|---|
| Madison (333) | FY2022 | 130 | 10 | 2 + 2 at 0.5 | 3 | 2 | 6 | |
| Madison (333) | FY2023 | 127 | 9 | 3 + 1 at 0.5 | 3 | 2 | 5 | |
| Madison (333) | FY2024 | 116 | 9 | 3 + 2 at 0.5 | 3 | 2 | 6.5 | |
| Madison (333) | FY2025 | 112 | 8 | 2 | 3 | 2 | 5.4 | |
| Madison (333) | FY2026 | 104 | 6 | 2 | 3 | 2 | 7 | |

## For another file

- **Agent 4 (money and governance):**
  - Draft 2027 warrant (November 2, 2026 packet, pp. 52–54): deliberative session Monday, February 1, 2027, 7:00 pm, in James Noyes Memorial Hall at Madison Elementary; ballot voting March 9, 2027 at the school; Article 8 would create a study committee on closing MES; Article 7 is a $300,000 grant appropriation. Raw: raw/school/board/madison-sb-packet-2026-11-02.txt.
  - Superintendent changes: Dr. Michael Whaland (January 2026 report) → Dr. Kathleen Scholand (hired by the Joint Board, June 1, 2026 minutes; first meeting July 6) → Interim Superintendent Dr. Ronna HasBrouck (introduced October 5, 2026). Student services director also changed twice (district-special-education-services fact 2).
  - MES inter-district tuition rate set at $17,118 on September 14, 2026; on August 3 the business administrator reported the cost per MES student as $25,085 (raw/school/board/madison-sb-minutes-2026-08-03.txt, -09-14.txt).
  - The Advisory Budget Committee's January 2026 report projected MES enrollment falling "from 111 to approximately 80" and recorded that no class-size or school-size analysis had been started (annual report, pp. 41–42).
  - ALPHA facilities contract (up to $13,000 from the Building Capital Reserve, October 5, 2026); CIP building sections (Section 1 built 2000; Section 2 built 1980, remodeled 2019; Section 3 gym/kitchen built 1989) on the November 2 packet p. 16.
  - The board has authorized the superintendent to approve fees for Madison students in Conway School District sports (August 24, 2026).
  - Annual report p. 75 lists 19 Madison homeschool students and 19 EFA students in fall 2025, plus charter counts.
- **Agent 2 (daily life):** ESY ran July 6–August 5, 2026, Monday–Wednesday (11 Madison students per the student services report; the principal reported 28 students at ESY); a new bus company in 2026-27 with a requested drop-off liability waiver (September 14 minutes); arrival 9:00–9:07 and dismissal from 3:20 (handbook); a 2-hour delay starts school at 11:07 (handbook) while the home page says the morning program begins at 9:45 on delay days; the handbook names both "Final Site" and "Blackboard Connect" as the alert system; before/after programs 7:45–9:00 and 3:30–5:00, fee-based, with Ossipee Children's Fund help; parent-teacher conference day moved to November 3, 2026; vended meal contract with Freedom Elementary.
- **Agent 3 (Kennett):** KMS offered a shared field trip with MES sixth graders and help for parents moving to PowerSchool (October 5, 2026 minutes); Kennett seniors who attended MES visit for a walkthrough each June (June 12, 2026); KMS and KHS September 2026 principal's reports are in the Madison October 5 packet (Arts and Letters, Acadience and Beacon at KMS; ALICE training at KHS); Madison special education counts at KMS/KHS were 16 in September 2026.
- **Agent 5 (community):** Madison Police teach DARE at MES; the Madison Historical Society, Madison Food Pantry, a Madison church and Madison Recreation all partner with the school; the district owns the Madison Corner School (built 1835, a school for 114 years and then a library for 49 years), which is on the NH Preservation Alliance's "Seven to Save" list, has a Corner Schoolhouse capital reserve ($76,323 in July 2026) and holds open houses (January 2026 annual report, p. 33). The deliberative session is held in James Noyes Memorial Hall (the gym) at MES.
- **Site data issue:** the site's school_class_size row for MES in 2026 (2025-26) gives grades 1–2 an average of 31.30, far above every earlier year (10.3–16.5) and above policy IIB's K–2 cap of 18. In 2025-26 MES had 35 K–2 students and six classroom teachers in total, so two K–2 classes would average about 17.5 (derived). The DOE source row should be checked before the Ask quotes it.
- **SAU 13 shared folder:** the December 2024 SAFE handout (raw/school/state/safe-grants-psif-overview-2024-12-13.txt, page 4 of the PDF) also has rows for Freedom and Tamworth; their Round 3 columns need the full-width page image to read correctly. Policies IJOC, GBCD, KCD, EBB and the draft EBCA are three-district policies that Freedom and Tamworth files can reuse.
- **Earlier town files:** the Jackson table sau9_safe_security_grant_awards (town/Jackson/policies-safety-meals-and-support.md) could take an SAU 13 companion; nothing found here contradicts the Jackson, Bartlett, Conway or SAU 9 files.

## Not retrieved

- https://drive.google.com/file/d/1-gVTkYdsBK9WYo-3zthAOvCXQpEGOi8g/view (SAU 13 ECE family handbook 2026-27): download redirected to a Google sign-in page.
- NH DOE SAFE Round 4 award list (February 2026): https://education.nh.gov/news-and-media/funding-recommended-more-260-school-safety-projects-throughout-state and the SAFE grant page returned 403 to curl and WebFetch; the Manchester Ink Link copy (https://manchester.inklink.news/?p=273877) lists only Manchester schools. Madison board minutes from 2025–2026 mention no SAFE grant.
- NH DOE iPlatform (https://my.doe.nh.gov/iPlatform): 403 to automated requests; school profiles were not read. The site's database was used instead.
- Number of preschool seats and waitlist length: not on the SAU 13 preschool page, the 2026-27 flyer, board minutes or annual reports.
- Days per week the contracted OT and the ESOL provider spend at MES: not in minutes, budgets or the handbook.
- A school social worker after 2022, a school resource officer, the site Emergency Operations Plan, and how often police and fire join drills: searched the handbook, MES and SAU 13 pages, 2024 and 2026 annual reports, and board minutes and packets from August 2022 to November 2026.
- Gifted identification or advanced math for grades 5–6: searched policies (IHBB), the Title I plan, annual reports, newsletters and minutes; none found.
- Local history units naming the Madison Boulder, Silver Lake's railroad era or one-room schoolhouses: searched newsletters (2025-26 and 2026-27), principal's reports and annual reports; none found.
- OASIS intergenerational tutoring at MES (how retirees join): the school lists the partner, but no sign-up information was found on the MES or SAU 13 sites; a web search found no New Hampshire OASIS location.
- MES staff directory page (https://sites.google.com/a/mes-nh.com/madison-elementary-school/home/staff-directory): the page is empty in the fetched HTML (content likely embedded); the handbook staff list was used instead.
- November 2, 2026 board minutes (not yet posted on November 13, 2026), so the fate of draft warrant Article 8 is unknown.
