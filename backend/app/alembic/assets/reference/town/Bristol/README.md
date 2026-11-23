# Bristol: Research for Ask NH Education Facts

Cited facts and figures for answering Bristol, NH residents' questions on the Ask page (nhfacts.com/ask). The questions are 20 resident profiles with 3 questions each, numbered P1.1 to P20.3 in `questions.md`. The people are invented. The research is in the five files below, in the reference library's format. These files are the first research on Newfound.

Gathered November 22, 2026, in the third ToLoad batch. Bristol is in the Newfound Area School District (SAU 4), which runs:
- **Newfound Elementary School at Bristol** (kindergarten to grade 4) and **at New Hampton** (preschool to grade 4; Danbury Elementary closed in June 2026);
- **Newfound Memorial Middle School** (grades 5–8 since fall 2026, when fifth grade moved up) and **Newfound Regional High School** (grades 9–12), both in Bristol;
- the Huot Career and Technical Center in Laconia and the Winnisquam Career Center in Tilton as career options.

The district votes by deliberative session and ballot.

## Files

| File | What's in it | Topic sections | Facts | Tables | Raw copies |
|---|---|---|---|---|---|
| `bristol-elementary-and-families.md` | Preschool at New Hampton, a Tapply-Thompson center stop on three afternoon bus runs and Project Promise care at the school until 5:30, the 2025-26 lead letter (7 outlets at or above 5 ppb) and the April 2026 asbestos removal, Title I schoolwide funding ($401,348), classes of about 19, licensed infant and toddler care, Danbury's closing and the fifth-grade move | 16 | 77 | 6 | 13 MB |
| `newfound-middle-support-and-choices.md` | Fifth grade at the middle school (four classes, intervention time, recess), morning rides of 42–76 minutes (derived), no late bus, thin special education staffing (state rating "Needs Intervention", three case managers short), policy JJJ for homeschoolers, phones in lockers 8:00–2:45 | 11 | 68 | 3 | 8 MB |
| `newfound-high-and-huot.md` | The Huot bus and time out of class, no welding at Huot (automotive only; welding is at Winnisquam), 24 credits rising to 26 with the Class of 2030, early graduation (plan by March 15 of sophomore year), GreatSchools ratings, the Aug 31 start before Labor Day, no CDL under 18 | 14 | 51 | 6 | 6.6 MB |
| `money-and-governance.md` | The 2025 revaluation (rate $23.62 to $13.16; valuation $549,100,592 to $1,033,562,950), two failed budgets and the default, the 2% local cap, local school tax up 58.8% since 2014 while resident students fell 5.8%, the elderly exemption ($35,000, $55,000, $75,000), no repair bond pending, enrollment of about a thousand | 12 | 78 | 7 | 5 MB |
| `families-and-community.md` | Summer camps (Tapply-Thompson $125 a week; Copper Cannon Camp free for eligible children), free and reduced lunch rules, the EFA procedure against HB 1817, Livescan fingerprints for volunteers ($21.25), free state tutoring, community use of facilities, volunteering | 13 | 76 | 0 | 16 MB |
| **Total** | | **66** | **350** | **22** | **49 MB** |

`brief.md` is the brief the research agents worked from. Five agents used about 2.9 million tokens (Sonnet 5.5).

## Checks

- **Parser:** all five files pass the backend's loader, run against the loaded towns plus Bristol. All 22 tables are linked to a topic.
- **Coverage:** all 60 questions have facts: 21 full, 39 partial.
- **Topics:** two new topics, added to `../shared-topics.md`: `cdl-age-rules` and `cooperative-district-apportionment-rules`.
- **Places:** `district Newfound Area` 305, `town Bristol` 37, no place 7, `town Danbury` 1. `places.yaml` already has Newfound's tuition rows (Hill, Pasquaney); no change needed.
- **Pending facts:** 2, citing draft minutes.
- **Raw folders:** each under 100 MB. The 111 saved PDFs are policies, forms, handbooks and reports; none is a route sheet, a roster or a list of names. The bus route sheets are kept as street-name-only CSV files.
- **Privacy:** the address scan finds only the Tapply-Thompson center (30 N Main St), schools, town halls and the SAU office. The "class advisors" in the high school's page are staff. Minutes copies have resident, student and employee names removed.
- **Quotes:** 733 of 829 quoted passages found word for word in the raw copies.
- **Spot checks** (main session, all matched):

  | Fact | Checked against |
  |---|---|
  | Net assessed valuation $549,100,592 (2024) and $1,033,562,950 (2025) | The site's `town_property_tax` table |
  | The elderly exemption ($35,000 for ages 65–74) | The voters' guide and the budget hearing text |
  | Title I schoolwide funding of $401,348 for 2026-27 | The November 9, 2026 board packet |
  | About a thousand students (1,003 in February 2026) | The FY27 proposed budget and the annual report excerpt |
  | Danbury Elementary's closing and the fifth-grade move | The March 16 and April 13, 2026 minutes |

## Premises checked

| Question says | What the sources show |
|---|---|
| A school tax bill that keeps jumping | The 2025 rate fell from $23.62 to $13.16 on a revaluation; the total tax raised rose 4.6% and the local school tax 9.9% |
| About a thousand students | Right: 1,003 in February 2026 and 997 on the first day of 2026-27. The brief's 949 left out Danbury Elementary's 66 |
| A repair bond coming | None pending; Bristol Elementary's spring 2026 repairs (about $350,000) came from the Maintenance Trust Fund |
| The Huot Center's welding | Huot has automotive, not welding; welding is at the Winnisquam Career Center in Tilton |
| Newfound starts before Labor Day in rooms with no AC | Starts Aug 31 (Labor Day was Sept 7); the lack of AC isn't confirmed |
| Lead and asbestos reports | Both exist; the lead letter lists 7 Bristol outlets at or above 5 ppb; asbestos was removed April 8–9, 2026 |
| Bristol Elementary is kindergarten to grade 4 and feeds the middle school | Yes; fifth grade joined the middle school in fall 2026 |
| Affordable daycare or pre-K in Bristol | Two licensed programs take infants and toddlers |
| Free tutoring for a 3rd grader | State free tutoring starts at grade 4 |
| EFA students can use the district's sports and band | Policy JJJ (September 2026) and HB 1817 say yes; the SAU's older procedure says no free access |
| A voice for new year-round residents on the budget committee | Not shown by the sources |
| Where to vote on the school budget | The high school gym in 2026 (the Old Town Hall in 2025) |
| A CDL before graduation | No one under 18 can hold a CDL in New Hampshire; neither Newfound nor Huot lists a CDL course |

**Brief corrections the agents reported:** SAU 4's pages now name four member towns (Alexandria, Bristol, Danbury, New Hampton), with Bridgewater, Hebron and Groton students attending by tuition or leaving; the superintendent from July 2026 is Dr. Brian Connelly, not Paul Hoiriis; the site's NMMS count has no grade 5 or 2026-27 row.

## Corrections and additions to earlier files

None. The agents' checks found nothing that contradicts an earlier town's file. Laconia's Huot pathways (no welding) and its Newfound CRDC row agree with this research.

## Library notes (for review, not applied)

- **`district-practices.md`** has no Newfound kindergarten day-length or registration fact (its table marks both "not found"); `kindergarten-day-length` and `kindergarten-registration` here fill that gap only partly.
- **Newfound's own documents disagree** on the graduation credits (the profile says 24 credits and 6 electives; the handbook and the March 23, 2026 minutes say 26 and 4 for the Class of 2030) and on the AP list (12, 11 or 15 courses). NRHS counseling could say which is current.

## Browser pass

Not done. Not retrieved:
- NH DOE's determinations page and several DOE pages (HTTP 403); NH DES's lead results; NH DRA's tax rate files (access denied); NH Department of Safety pages (HTTP 403, for how long a background check takes);
- a Laconia Daily Sun article (HTTP 429, not retried);
- the Bristol and Hebron town pages (404 on older links);
- the districts' articles of agreement and Bristol's 2026 rate, the March 14, 2026 Article 20 result (elderly exemption), a high school heating or electricity figure and any teacher turnover rate (not found).
