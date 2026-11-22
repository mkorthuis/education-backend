# Timberlane Regional: Shared Research

Facts about the Timberlane Regional School District (SAU 106), the cooperative of Atkinson, Danville, Plaistow and Sandown. Written by the Atkinson and Plaistow research on November 21, 2026 (`../Atkinson/`, `../Plaistow/`) for any member town to reuse. Each fact is placed in `district Timberlane Regional`, or `sau 106` for the SAU itself, unless it is about one town's own taxes.

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `timberlane-high-school.md` | 19 AP courses in person and 6 SNHU dual enrollment courses, CTE at Salem (bused) and Pinkerton (no bus), ELOs (half a credit per 65 hours), shop and engineering courses, counselors (five plus a director, about 186 students each), weighted GPA and rank, SAT (mean 951 for the class of 2027), graduation (92.5% in 2025), no school social worker, personal finance required from the class of 2030 | 8 | 60 | 2 | 21 MB |
| `timberlane-middle-school-and-student-life.md` | The move from the elementary schools, Pre-Algebra and Algebra I by 8th grade, IEP transitions, band, strings and drama, the Performing Arts Center (2002) and its roof and air handlers, athletics (no pay-to-play fee; 30 state wrestling titles), eligibility, late buses Tuesday–Thursday, phones and bullying, the high school bathrooms ($625,033, to bid January 2027) | 15 | 103 | 1 | 26 MB |
| `timberlane-money-and-governance.md` | Each town's share of costs (FY2026: Atkinson 22.78% with 22.24% of students; Plaistow 30.66% with 30.65%), the $25,243,000 energy and facilities lease (about $1.0 million a year to 2044), the fund balance (5% repealed in 2025), the 2.5% cap petition (amended to 25%) and Question 2, 49.5 vacant positions and contracted staff, SAU 106 since July 1, 2021, Sandown's 2015 withdrawal study, default budgets, teacher pay | 7 | 80 | 4 | 33 MB |
| **Total** | | **30** | **243** | **7** | **80 MB** |

All three files pass the backend's parser (`tools/check_town.sh timberlane`), and every table is linked to a topic. 12 facts cite draft minutes. 475 of 583 quoted passages were found word for word in the raw copies. The three agents used about 1.63 million tokens. Spot checks are in `../Atkinson/README.md`.

**For a member town's research** (Danville, Sandown): read these files first, then add only that town's own elementary school, its taxes and exemptions, and its share. The question tables label each question with its town ("Atkinson P7.1", "Plaistow P7.1"); `coverage.py` reads only the P-number, so count a town's coverage from its own rows.

**Still not retrieved:**
- the 2026-27 student handbooks (a Canva page);
- the middle school clubs and supply lists;
- district-wide totals for the March 2026 ballot;
- board policies IK, IHBH and JG;
- the NH DRA tax rate files (HTTP 403).

## Later research and corrections

- **Danville and Sandown** were researched on November 21, 2026 (`../Danville/`, `../Sandown/`). They cite these files and add district-wide facts these lacked: the 2026 district-wide vote totals, bus stop times, CTE and athletics budget lines, and SNHU's $100 course fee.
- **Year labels corrected:** the site's school enrollment "2025" rows are the October 1, 2024 count. So "364 at Atkinson Academy, 723 at TRMS" and TRHS's 932 are now labeled 2024-25, not 2025-26. The same fix was made in the Atkinson and Plaistow files; the error came from the first-wave briefs.
- **Algebra I:** the middle school file's premise note now adds that TRMS reported no grade 7–8 Algebra I classes to the federal Civil Rights Data Collection for 2023-24 (Danville `middle-and-high-school.md`).

## Privacy cleanup, November 22, 2026

Done by the main session after loading:
- House numbers removed from street addresses in 6 saved bus and transportation copies (6 in all; schools, child care centers, businesses and other public places keep theirs).
