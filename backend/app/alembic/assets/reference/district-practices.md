# District Practices: Kindergarten, Preschool, Budget Votes and High School Options

Strategy type 1 (local practices that each district sets and no state dataset records). Gathered November 8, 2026, from district and SAU websites and two statewide sources. Each fact cites the page it came from; `place: district <name>` uses the name in the site's `district` table.

## Summary

**Districts covered** (183 current public districts in the site database, including 3 that are not ordinary districts: the two academies and the state-run facility):

| Field | Found on district page | State source only | Not found on district site | Not checked | Not applicable |
|---|---|---|---|---|---|
| `kindergarten-day-length` | 36 | 0 | 119 | 0 | 28 |
| `kindergarten-entry-cutoff` | 117 | 0 | 41 | 0 | 25 |
| `kindergarten-registration` | 97 | 0 | 61 | 0 | 25 |
| `district-preschool` | 101 | 20 | 36 | 0 | 26 |
| `budget-form-and-vote-dates` | 138 | 10 | 32 | 0 | 3 |
| `high-school-tuition-options` | 86 | 0 | 19 | 0 | 78 |

**Largest districts.** Among the 60 largest districts by 2025 enrollment, found on the district's own pages: kindergarten cutoff 48 of 56, kindergarten registration 44 of 56, preschool 46 of 57 (+6 from a state source), budget form and dates 54 of 60 (+2 from a state source), kindergarten day length 15 of 56.

**Districts without a high school.** 86 of the 105 districts that run no high school have a cited statement of where their high school students go and on what terms. Arrangements vary: cooperative membership (e.g. Hollis-Brookline, Winnacunnet, Exeter Region, Pemi-Baker, John Stark, Profile), AREA agreements (e.g. Dunbarton with Bow, Grantham and Plainfield with Lebanon, New Boston with Goffstown, Surry with Keene, the SAU 50 towns with Portsmouth), a designated high school or academy (e.g. Derry and Hooksett with Pinkerton Academy; Allenstown, Chichester and Epsom with Pembroke Academy; Chesterfield, Marlborough and other SAU 29 towns with Keene High School), a joint maintenance agreement (Alton and Barnstead, Prospect Mountain High School), or school choice, often with a tuition cap (e.g. Croydon, Lempster, Lyme, Monroe, Warren, Cornish).

**Statewide sources found**
- *Budget form:* the NH Municipal Association's "Municipal Data" list (file dated January 5, 2026; data from the NH Department of Revenue Administration) names 81 SB2 school districts (including regional ones) and 8 cities with charter tax or budget caps. It is the only source for 10 districts whose own pages had no voting information. Some district pages differ from it: Londonderry and Kearsarge Regional describe a deliberative first session and a March ballot vote but are not on the list, and Merrimack Valley's 2026 warrant had a petitioned article to adopt SB2 whose result is not posted.
- *Preschool:* NH DOE's iPlatform "Preschool Enrollments" report (October 1, 2026, preliminary) shows preschool enrollment in 104 districts (table below). It is the only source for 20 districts with no preschool page.
- *Not available statewide:* NH DOE's "Kindergarten Enrollments" report gives only totals (the 2017-18 and 2026-27 reports were checked), with no full-day or half-day split, and no state source lists entry cutoffs or registration windows. NH DOE's "High School/Town Cross Reference", "District/Town Cross Reference" and "SAU List" reports returned server errors on November 8, 2026, so high school options come from district pages.

**Main gaps**
- *Kindergarten day length* is the weakest field (36 found): most district sites list school hours but never say "full day" or "half day". Where a page gives only hours, the statement gives the hours and does not call it full day. This is the best question for the planned SAU survey.
- *Little or nothing online:* Winchester (its school websites now show a parked domain page), Sullivan, Hale's Location and Coos County School District (no website found), Benton, Clarksville and Columbia, and most of SAU 7 (Colebrook area) and SAU 23 (Haverhill area), which post no warrants or meeting dates. Gilmanton's and Goshen's sites require a Google sign-in.
- *Budget form and dates not found* for 32 districts, including the cities of Berlin, Franklin and Laconia, whose sites do not say how the school budget is approved.
- *Unreadable policy portals:* Simbli (Hanover, SAU 24), Diligent/HighBond (Lebanon), SharePoint (Hinsdale). Several districts' kindergarten cutoffs are missing for this reason.
- *Scanned documents:* 67 cited facts come from scanned PDFs or images with no text layer. Their quotes are transcriptions of the page image, and each fact's note says so.
- *Year:* most facts are for 2026-27. Few districts had posted 2027-28 kindergarten registration by November 8, 2026. A few facts come only from older pages, and their statements name the year. Several districts have already posted 2027 budget dates (e.g. Barrington, Mascenic, Mascoma, Shaker, Hillsboro-Deering, Grantham), and these are included.
- *To recheck next cycle:* Timberlane's March 2026 Article 14 (tuition-free full-day kindergarten; result not posted), Merrimack Valley's SB2 petition, Landaff (tuition-only since its March 9, 2026 meeting), and the Profile/Bethlehem/Lafayette minutes that refer to a "pre-existing District of Bethlehem/Lafayette".

**Method.** District and SAU sites were read with curl and headless Chrome, and policy PDFs with a text extractor. Each fact keeps a verbatim quote that a script checked against the saved raw text, and the dates and dollar figures in statements were also checked against the raw text. Per-district raw copies are in `raw/districts/batch-1` to `batch-8` (one `records.jsonl` per batch holds every field, including the notes on what was checked when nothing was found). `raw/districts/batch-coordinator/records.jsonl` holds one coordinator correction (Hampton's high school), and the SAU 48 town statements were reworded at compile time. The web search allowance ran out partway through, so many smaller districts were done by following links on their own sites.

## Coverage

`found` = stated on a district or SAU page (cited below). `state list only` = the district's own page was not found, but the statewide SB2 list names it. `state count only` = no district preschool page found, but NH DOE counted preschool children in its schools on October 1, 2026. `not found` = looked on the district site and searched, and it does not say (see *Not retrieved*). `n/a` = does not apply (the district has a high school, or runs no schools). Full table with source links: `raw/districts/coverage.csv`.

| District | id | SAU | K day | K cutoff | K registration | Preschool | Budget/vote | HS options |
|---|---|---|---|---|---|---|---|---|
| Albany | 5 | 9 | n/a | n/a | n/a | n/a | found | found |
| Allenstown | 9 | 53 | not found | not found | not found | found | found | found |
| Alton | 15 | 72 | not found | not found | not found | found | found | found |
| Amherst | 17 | 39 | found | not found | found | found | state list only | found |
| Andover | 19 | 46 | not found | found | not found | not found | not found | found |
| Ashland | 23 | 2 | not found | found | not found | not found | found | found |
| Auburn | 29 | 15 | found | found | found | found | found | found |
| Barnstead | 31 | 86 | found | found | found | found | found | found |
| Barrington | 33 | 74 | not found | not found | found | found | found | found |
| Bartlett | 35 | 9 | not found | found | found | found | found | found |
| Bath | 39 | 23 | not found | found | not found | state count only | not found | not found |
| Bedford | 41 | 25 | found | found | not found | found | found | n/a |
| Benton | 47 | 23 | n/a | n/a | n/a | n/a | not found | not found |
| Berlin | 51 | 3 | not found | found | not found | not found | not found | n/a |
| Bethlehem | 53 | 35 | not found | found | not found | found | found | found |
| Bow | 57 | 67 | not found | not found | found | found | found | n/a |
| Brentwood | 63 | 16 | not found | found | not found | found | found | found |
| Brookline | 71 | 41 | found | not found | found | found | found | found |
| Campton | 75 | 48 | not found | not found | not found | found | found | found |
| Candia | 79 | 15 | found | found | found | not found | found | found |
| Chatham | 91 | 9 | n/a | n/a | n/a | n/a | found | not found |
| Chester | 93 | 82 | found | not found | not found | found | found | found |
| Chesterfield | 95 | 29 | not found | found | not found | not found | found | found |
| Chichester | 99 | 53 | not found | found | found | found | found | found |
| Claremont | 101 | 6 | found | found | found | not found | found | n/a |
| Clarksville | 103 | 7 | n/a | n/a | n/a | n/a | not found | not found |
| Coe-Brown Northwood Academy | 998 | 201 | n/a | n/a | n/a | n/a | n/a | n/a |
| Colebrook | 105 | 7 | not found | found | not found | state count only | not found | n/a |
| Columbia | 107 | 7 | n/a | n/a | n/a | n/a | not found | not found |
| Concord | 111 | 8 | found | found | found | found | found | n/a |
| Contoocook Valley | 112 | 1 | not found | found | not found | found | found | n/a |
| Conway | 113 | 9 | not found | not found | found | not found | found | n/a |
| Coos County School District | 114 | 98 | n/a | n/a | n/a | n/a | not found | not found |
| Cornish | 115 | 100 | found | found | found | found | found | found |
| Croydon | 117 | 99 | found | found | found | found | found | found |
| Deerfield | 127 | 53 | not found | found | found | found | found | found |
| Derry Cooperative | 131 | 10 | found | found | found | found | found | found |
| Dover | 141 | 11 | not found | found | found | found | found | n/a |
| Dresden | 142 | 70 | n/a | n/a | n/a | n/a | found | n/a |
| Dummer | 147 | 20 | n/a | n/a | n/a | n/a | found | found |
| Dunbarton | 149 | 67 | not found | not found | found | not found | not found | found |
| East Kingston | 153 | 16 | not found | found | found | found | found | found |
| Eaton | 159 | 9 | n/a | n/a | n/a | n/a | found | found |
| Ellsworth | 162 | 48 | n/a | n/a | n/a | n/a | not found | found |
| Epping | 165 | 14 | not found | found | found | found | found | n/a |
| Epsom | 167 | 53 | not found | found | not found | found | found | found |
| Errol | 171 | 20 | not found | not found | not found | not found | found | found |
| Exeter | 173 | 16 | not found | found | not found | found | found | found |
| Exeter Region Cooperative | 172 | 16 | n/a | n/a | n/a | not found | found | n/a |
| Fall Mountain Regional | 174 | 60 | not found | not found | not found | state count only | found | n/a |
| Farmington | 175 | 61 | not found | not found | not found | found | state list only | n/a |
| Franklin | 185 | 18 | not found | found | found | state count only | not found | n/a |
| Freedom | 187 | 13 | not found | not found | found | found | not found | not found |
| Fremont | 189 | 83 | found | not found | not found | found | found | found |
| Gilford | 191 | 73 | not found | not found | found | not found | found | n/a |
| Gilmanton | 195 | 79 | not found | not found | not found | not found | found | not found |
| Goffstown | 199 | 19 | found | found | found | found | found | n/a |
| Gorham Randolph Shelburne Cooperative | 203 | 20 | not found | not found | not found | not found | found | n/a |
| Goshen | 204 | 102 | n/a | not found | n/a | n/a | not found | found |
| Governor Wentworth Regional | 208 | 49 | not found | found | found | found | found | n/a |
| Grantham | 211 | 75 | not found | found | found | found | found | found |
| Greenland | 215 | 50 | found | found | not found | found | state list only | found |
| Hale's Location (Carroll County) | 222 | 97 | n/a | n/a | not found | n/a | not found | not found |
| Hampstead | 223 | 55 | found | found | found | found | found | found |
| Hampton | 225 | 90 | not found | found | not found | found | found | found |
| Hampton Falls | 227 | 21 | found | found | found | found | found | found |
| Hanover | 233 | 70 | not found | not found | not found | not found | found | found |
| Harrisville | 235 | 29 | not found | found | not found | not found | found | found |
| Hart's Location | 236 | 9 | n/a | n/a | n/a | n/a | found | not found |
| Haverhill Cooperative | 238 | 23 | not found | found | not found | state count only | not found | n/a |
| Henniker | 245 | 24 | not found | found | found | state count only | found | found |
| Hill | 247 | 103 | not found | not found | not found | state count only | found | found |
| Hillsboro-Deering Cooperative | 251 | 34 | not found | found | found | found | found | n/a |
| Hinsdale | 255 | 92 | not found | not found | found | found | found | n/a |
| Holderness | 257 | 48 | found | found | found | not found | not found | found |
| Hollis | 259 | 41 | found | not found | found | found | found | found |
| Hollis-Brookline Cooperative | 260 | 41 | n/a | n/a | n/a | n/a | found | n/a |
| Hooksett | 261 | 15 | found | found | found | found | found | found |
| Hopkinton | 263 | 66 | not found | not found | not found | found | found | n/a |
| Hudson | 267 | 81 | found | found | found | found | found | n/a |
| In-State Facility | 838 | 501 | n/a | n/a | n/a | n/a | n/a | n/a |
| Inter-Lakes Cooperative | 269 | 2 | not found | found | not found | found | found | n/a |
| Jackson | 271 | 9 | not found | found | found | not found | found | found |
| Jaffrey-Rindge Cooperative | 274 | 47 | not found | found | found | found | found | n/a |
| John Stark Regional | 275 | 24 | n/a | n/a | n/a | n/a | found | n/a |
| Kearsarge Regional | 276 | 65 | not found | found | found | found | found | n/a |
| Keene | 279 | 29 | found | found | not found | found | found | n/a |
| Kensington | 281 | 16 | not found | found | found | found | found | found |
| Laconia | 285 | 30 | not found | found | found | found | not found | n/a |
| Lafayette Regional | 288 | 35 | not found | found | not found | not found | not found | found |
| Landaff | 291 | 35 | n/a | found | n/a | n/a | found | found |
| Lebanon | 295 | 88 | not found | found | found | found | found | n/a |
| Lempster | 299 | 71 | not found | found | not found | found | found | found |
| Lincoln-Woodstock Cooperative | 305 | 68 | not found | found | found | not found | found | n/a |
| Lisbon Regional | 306 | 110 | not found | found | not found | found | not found | n/a |
| Litchfield | 315 | 27 | not found | not found | found | found | found | n/a |
| Littleton | 317 | 84 | not found | found | found | not found | found | n/a |
| Londonderry | 319 | 12 | found | found | found | found | found | n/a |
| Lyme | 327 | 76 | not found | found | found | not found | not found | found |
| Madison | 333 | 13 | not found | not found | found | found | state list only | found |
| Manchester | 335 | 37 | not found | found | found | found | found | n/a |
| Marlborough | 339 | 29 | not found | not found | not found | found | found | found |
| Marlow | 341 | 29 | found | found | not found | found | found | found |
| Mascenic Regional | 342 | 87 | not found | found | not found | state count only | found | n/a |
| Mascoma Valley Regional | 343 | 62 | not found | found | found | found | found | n/a |
| Mason | 345 | 89 | found | found | found | found | found | found |
| Merrimack | 351 | 26 | not found | found | found | found | found | n/a |
| Merrimack Valley | 352 | 46 | not found | found | found | found | found | n/a |
| Middleton | 353 | 69 | not found | found | found | found | found | found |
| Milan | 355 | 20 | not found | not found | not found | not found | found | found |
| Milford | 357 | 40 | not found | found | found | found | found | n/a |
| Milton | 359 | 64 | not found | not found | not found | found | found | n/a |
| Monadnock Regional | 363 | 93 | not found | found | not found | found | found | n/a |
| Monroe | 365 | 77 | not found | found | found | found | not found | found |
| Mont Vernon | 367 | 39 | found | not found | found | not found | state list only | found |
| Moultonborough | 369 | 45 | found | found | not found | found | found | n/a |
| Nashua | 371 | 42 | found | found | found | found | found | n/a |
| Nelson | 375 | 29 | not found | found | not found | not found | found | found |
| New Boston | 377 | 19 | found | found | found | state count only | found | found |
| New Castle | 381 | 50 | not found | found | not found | found | not found | found |
| Newfields | 387 | 16 | not found | found | not found | found | found | found |
| Newfound Area | 388 | 4 | not found | found | not found | found | found | n/a |
| Newington | 391 | 50 | not found | found | not found | found | not found | found |
| Newmarket | 399 | 31 | found | found | found | found | found | n/a |
| Newport | 401 | 43 | not found | found | found | state count only | found | n/a |
| North Hampton | 405 | 21 | found | not found | found | found | found | found |
| Northumberland | 407 | 58 | not found | not found | not found | not found | found | n/a |
| Northwood | 411 | 44 | not found | found | not found | found | found | found |
| Nottingham | 413 | 107 | not found | found | found | found | state list only | found |
| Oyster River Coop | 423 | 5 | not found | found | found | found | found | n/a |
| Pasquaney | 584 | 108 | found | found | found | found | found | found |
| Pelham | 425 | 28 | not found | found | found | found | found | n/a |
| Pembroke | 427 | 53 | not found | found | found | found | found | n/a |
| Pemi-Baker Regional | 428 | 48 | n/a | n/a | n/a | n/a | found | n/a |
| Piermont | 435 | 23 | not found | found | found | found | not found | not found |
| Pinkerton Academy | 999 | 202 | n/a | n/a | n/a | n/a | n/a | n/a |
| Pittsburg | 437 | 7 | not found | found | not found | state count only | not found | n/a |
| Pittsfield | 439 | 51 | not found | found | not found | not found | found | n/a |
| Plainfield | 441 | 32 | not found | found | found | not found | not found | found |
| Plymouth | 447 | 48 | not found | not found | found | found | found | found |
| Portsmouth | 449 | 52 | found | found | found | found | found | n/a |
| Profile | 450 | 35 | n/a | n/a | n/a | n/a | found | n/a |
| Prospect Mountain JMA | 970 | 301 | n/a | n/a | n/a | n/a | found | n/a |
| Raymond | 453 | 33 | not found | found | found | found | found | n/a |
| Rivendell | 457 | 78 | not found | not found | not found | found | found | n/a |
| Rochester | 461 | 54 | not found | found | found | found | found | n/a |
| Rollinsford | 463 | 104 | not found | found | found | not found | found | found |
| Rumney | 467 | 48 | not found | found | found | not found | found | found |
| Rye | 471 | 50 | not found | found | found | found | state list only | found |
| Salem | 473 | 57 | not found | found | found | found | found | n/a |
| Sanborn Regional | 476 | 17 | not found | found | found | found | state list only | n/a |
| Seabrook | 485 | 21 | found | found | found | found | found | found |
| Shaker Regional | 486 | 80 | not found | found | found | found | found | n/a |
| Somersworth | 491 | 56 | not found | found | found | found | found | n/a |
| Souhegan Cooperative | 493 | 39 | n/a | n/a | n/a | n/a | state list only | n/a |
| South Hampton | 495 | 21 | not found | found | not found | not found | found | not found |
| Stark | 499 | 58 | not found | not found | not found | not found | found | not found |
| Stewartstown | 501 | 7 | not found | found | not found | state count only | not found | not found |
| Stoddard | 503 | 24 | not found | found | found | not found | found | found |
| Strafford | 507 | 105 | not found | found | found | found | not found | found |
| Stratford | 509 | 58 | not found | not found | not found | state count only | found | not found |
| Stratham | 511 | 16 | not found | found | found | found | found | found |
| Sullivan | 513 | 96 | n/a | n/a | n/a | n/a | not found | not found |
| Sunapee | 515 | 85 | not found | not found | not found | found | found | n/a |
| Surry | 519 | 91 | n/a | n/a | found | n/a | found | found |
| Tamworth | 525 | 13 | not found | not found | found | found | found | found |
| Thornton | 531 | 48 | not found | not found | not found | not found | found | found |
| Timberlane Regional | 534 | 106 | found | found | found | found | found | n/a |
| Unity | 539 | 109 | not found | not found | found | state count only | not found | not found |
| Wakefield | 543 | 101 | not found | found | found | state count only | found | not found |
| Warren | 549 | 23 | not found | found | not found | state count only | not found | found |
| Washington | 551 | 34 | not found | found | found | found | found | found |
| Waterville Valley | 553 | 48 | not found | found | found | not found | found | found |
| Weare | 555 | 24 | not found | found | found | state count only | found | found |
| Wentworth | 559 | 48 | not found | found | found | not found | found | found |
| Westmoreland | 563 | 29 | not found | found | found | not found | found | found |
| White Mountains Regional | 568 | 36 | not found | found | not found | state count only | found | n/a |
| Wilton-Lyndeborough Cooperative | 572 | 63 | found | found | found | found | found | n/a |
| Winchester | 573 | 94 | not found | not found | not found | state count only | state list only | not found |
| Windham | 575 | 95 | not found | found | found | found | found | n/a |
| Windsor | 579 | 34 | n/a | found | found | found | found | found |
| Winnacunnet Cooperative | 581 | 21 | n/a | n/a | n/a | n/a | found | n/a |
| Winnisquam Regional | 582 | 59 | not found | found | found | state count only | not found | n/a |

## Statewide sources

## budget-form-statewide-list: Which School Districts Vote by Official Ballot (SB2)

- kind: local
- question_type: local_practice
- description: The New Hampshire Municipal Association's list, from NH Department of Revenue Administration data, of school districts that use the official ballot (SB2) and of cities whose charters cap taxes or budgets.

1. The New Hampshire Municipal Association's "Municipal Data" list, which gives the NH Department of Revenue Administration as its source, names these school districts as official ballot referendum (SB2) districts: Allenstown, Alton, Amherst, Ashland, Auburn, Barrington, Bedford, Brookline, Candia, Claremont, Contoocook Valley, Conway, Deerfield, Derry Cooperative, East Kingston, Epping, Epsom, Exeter, Exeter Region Cooperative, Fall Mountain Regional, Farmington, Fremont, Gilford, Gilmanton, Goffstown, Governor Wentworth Regional, Greenland, Hampstead, Hampton, Hampton Falls, Henniker, Hillsboro-Deering Cooperative, Hooksett, Hudson, Jaffrey-Rindge Cooperative, John Stark Regional, Keene, Kensington, Lebanon, Litchfield, Littleton, Madison, Mascenic Regional, Mascoma Valley Regional, Mason, Merrimack, Middleton, Milford, Milton, Monadnock Regional, Mont Vernon, New Boston, Newfields, Newfound Area, Newmarket, Newport, North Hampton, Northwood, Nottingham, Oyster River Coop, Pelham, Pemi-Baker Regional, Pittsfield, Raymond, Rollinsford, Rumney, Rye, Salem, Sanborn Regional, Seabrook, Shaker Regional, Souhegan Cooperative, South Hampton, Sunapee, Timberlane Regional, Wakefield, Weare, White Mountains Regional, Winchester, Windham, Winnacunnet Cooperative.
   - citation: NH Municipal Association, "Municipal Data" (lists "Official Ballot Referendum (SB2) School Districts" and "(SB2) Regional School Districts"; data source NH Department of Revenue), file dated 2026-01-05
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: Names matched to the site's district table by hand (e.g. "Derry" = Derry Cooperative, "ConVal" = Contoocook Valley, "Exeter Coop" = Exeter Region Cooperative, "Oyster River" = Oyster River Coop). Raw copy: raw/districts/statewide/nhma-municipal-data-2025.pdf (+ .txt). A district missing from the list is not proof that it holds a traditional meeting; check its own page.
2. The same list names these cities as having tax or budget caps in their charters: Dover, Franklin, Laconia, Manchester, Nashua, Portsmouth, Rochester, Somersworth. How each city's school budget is approved is given in that district's own entry under `budget-form-and-vote-dates`, where found.
   - citation: NH Municipal Association, "Municipal Data", section "Cities with Tax or Budget Caps Per Charter"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - note: The list gives only the names; it does not describe the cities' budget processes.

## district_preschool_enrollment_oct2026: Public Preschool Enrollment by District, October 1, 2026

- unit: count
- period: 2026-2027, as of October 1, 2026 (NH DOE marks the data "Preliminary"); year: 2027
- source: NH Department of Education, iPlatform "Preschool Enrollments" report (Report ID 10) — https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
- as_of: 2026-11-08
- raw: raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx
- note: Children enrolled in preschool in each district's public schools. A count above zero shows that the district's schools enrolled preschool children on that date; it does not say whether the program is open to all families or only to children with disabilities, or what it costs (see `district-preschool`). The statewide total in the report is 4,218, including 15 at Northeast Woodland Chartered Public School (not a district, so not in this table). Districts not listed had no preschool enrollment in the report.

| Place | District id | Value | Note |
|---|---|---|---|
| Alton | 15 | 39 | Alton Central School (Elem) (39) |
| Amherst | 17 | 40 | Clark-Wilkins School (40) |
| Auburn | 29 | 11 | Auburn Village School (11) |
| Barnstead | 31 | 16 | Barnstead Elementary School (16) |
| Barrington | 33 | 43 | Early Childhood Learning Center (43) |
| Bartlett | 35 | 16 | Josiah Bartlett Elementary School (16) |
| Bath | 39 | 7 | Bath Village School (7) |
| Bedford | 41 | 71 | Riddle Brook School (71) |
| Bethlehem | 53 | 6 | Bethlehem Elementary School (6) |
| Bow | 57 | 20 | Bow Preschool (20) |
| Brentwood | 63 | 16 | Swasey Central School (16) |
| Brookline | 71 | 24 | Richard Maghakian Memorial School (24) |
| Chester | 93 | 31 | Chester Academy (31) |
| Colebrook | 105 | 14 | Colebrook Academy and Elementary School (E) (14) |
| Concord | 111 | 106 | Abbot-Downing School (29); Beaver Meadow School (23); Mill Brook School (54) |
| Contoocook Valley | 112 | 94 | Antrim Elementary School (27); Greenfield Elementary School (18); Hancock Elementary School (22); Peterborough Elementary School (27) |
| Cornish | 115 | 16 | Cornish Elementary School (16) |
| Croydon | 117 | 2 | Croydon Village School (2) |
| Deerfield | 127 | 33 | Deerfield Community School (33) |
| Derry Cooperative | 131 | 91 | Derry Early Education Program (91) |
| Dover | 141 | 38 | Woodman Park School (38) |
| Epping | 165 | 44 | Epping Elementary School (44) |
| Exeter | 173 | 31 | Main Street School (31) |
| Fall Mountain Regional | 174 | 68 | Alstead Primary School (17); Charlestown Primary School (27); Walpole Primary School (24) |
| Farmington | 175 | 22 | Valley View Community School (22) |
| Franklin | 185 | 35 | Paul A. Smith School (35) |
| Fremont | 189 | 18 | Ellis School (18) |
| Goffstown | 199 | 59 | Glen Lake School (59) |
| Governor Wentworth Regional | 208 | 42 | New Durham Elementary School (10); Ossipee Central School (32) |
| Grantham | 211 | 23 | Grantham Village School (23) |
| Hampstead | 223 | 35 | Hampstead Central School (35) |
| Hampton | 225 | 38 | Hampton Centre School (38) |
| Hampton Falls | 227 | 15 | Lincoln Akerman School (15) |
| Haverhill Cooperative | 238 | 40 | Woodsville Elementary School (40) |
| Henniker | 245 | 19 | Henniker Community School (19) |
| Hill | 247 | 9 | Jennie D. Blake School (9) |
| Hillsboro-Deering Cooperative | 251 | 46 | Hillsboro-Deering Elementary School (46) |
| Hinsdale | 255 | 33 | Hinsdale Elementary School (33) |
| Hollis | 259 | 21 | Hollis Primary School (21) |
| Hooksett | 261 | 25 | Fred C. Underhill School (25) |
| Hopkinton | 263 | 42 | Harold Martin School (42) |
| Hudson | 267 | 96 | Nottingham West Elementary Pre School (96) |
| Inter-Lakes Cooperative | 269 | 29 | Inter-Lakes Elementary School (29) |
| Jaffrey-Rindge Cooperative | 274 | 64 | Jaffrey Grade School (31); Rindge Memorial School (33) |
| Kearsarge Regional | 276 | 49 | Kearsarge Regional Preschool Bradford (27); Kearsarge Regional Preschool New London (22) |
| Keene | 279 | 88 | Jonathan Daniels School (88) |
| Laconia | 285 | 57 | Elm Street School (13); Pleasant Street School (13); Woodland Heights Elementary School (31) |
| Lebanon | 295 | 41 | Mt. Lebanon School (41) |
| Lempster | 299 | 13 | Lempster Community School (13) |
| Lisbon Regional | 306 | 13 | Lisbon Regional School (Elem) (13) |
| Litchfield | 315 | 35 | Griffin Memorial School (35) |
| Londonderry | 319 | 114 | Moose Hill School (114) |
| Madison | 333 | 21 | Madison Elementary School (21) |
| Manchester | 335 | 418 | Bakersville School (67); Gossler Park School (21); Highland-Goffes Falls School (24); Jewett School (36); McDonough School (22); Parker-Varney School (69); Smyth Road School (12); Webster School (78); Weston Elementary School (89) |
| Marlborough | 339 | 21 | Marlborough Elementary School (21) |
| Mascenic Regional | 342 | 13 | Highbridge Hill Elementary School (13) |
| Mascoma Valley Regional | 343 | 77 | Canaan Elementary School (46); Enfield Village School (31) |
| Mason | 345 | 8 | Mason Elementary School (8) |
| Merrimack | 351 | 95 | James Mastricola Elementary School (17); Reeds Ferry School (50); Thorntons Ferry School (28) |
| Merrimack Valley | 352 | 28 | Boscawen Elementary School (16); Penacook Elementary School (12) |
| Middleton | 353 | 6 | Middleton Elementary School (6) |
| Milford | 357 | 51 | Milford Early Education Experiences (51) |
| Milton | 359 | 23 | Milton Elementary School (23) |
| Monadnock Regional | 363 | 62 | Dr. George S. Emerson Elementary School (25); Mt. Caesar Elementary School (36); Troy Elementary School (1) |
| Monroe | 365 | 9 | Monroe Consolidated School (9) |
| Moultonborough | 369 | 27 | Moultonborough Central School (27) |
| Nashua | 371 | 277 | Amherst Street School (14); Dr. Norman W. Crisp School (8); Fairgrounds Elementary School (13); Franklin Street School (190); Ledge Street School (13); New Searles School (4); Purple Panthers Preschool (35) |
| New Boston | 377 | 14 | New Boston Central School (14) |
| Newfound Area | 388 | 17 | Newfound Elementary School at New Hampton (17) |
| Newington | 391 | 4 | Newington Public School (4) |
| Newmarket | 399 | 34 | Newmarket Elementary School (34) |
| Newport | 401 | 24 | Richards Elementary School (24) |
| North Hampton | 405 | 9 | North Hampton School (9) |
| Northwood | 411 | 28 | Northwood Elementary School (28) |
| Nottingham | 413 | 37 | Nottingham Elementary School (37) |
| Oyster River Coop | 423 | 27 | Oyster River Preschool Education Program (27) |
| Pasquaney | 584 | 14 | Bridgewater-Hebron Village School (14) |
| Pelham | 425 | 50 | Pelham Elementary School (50) |
| Piermont | 435 | 3 | Piermont Village School (3) |
| Pittsburg | 437 | 5 | Pittsburg School (Elem) (5) |
| Portsmouth | 449 | 15 | PEEP School - Pre School Program (15) |
| Raymond | 453 | 50 | Raymond School District Preschool Program (50) |
| Rochester | 461 | 41 | East Rochester School (41) |
| Rye | 471 | 31 | Rye Elementary School (31) |
| Salem | 473 | 137 | Salem Preschool (137) |
| Sanborn Regional | 476 | 31 | Daniel J. Bakie School (31) |
| Seabrook | 485 | 34 | Seabrook Elementary School (34) |
| Shaker Regional | 486 | 26 | Belmont Elementary School (26) |
| Somersworth | 491 | 36 | Idlehurst Elementary School (36) |
| Stewartstown | 501 | 2 | Stewartstown Community School (2) |
| Strafford | 507 | 13 | Strafford School (13) |
| Stratford | 509 | 3 | Stratford Public School (3) |
| Stratham | 511 | 21 | Stratham Memorial School (21) |
| Sunapee | 515 | 16 | Sunapee Central School (16) |
| Timberlane Regional | 534 | 135 | Atkinson Academy (26); Danville Elementary School (15); Pollard Elementary School (36); Sandown Central School (58) |
| Unity | 539 | 9 | Unity Elementary School (9) |
| Wakefield | 543 | 19 | Paul Elementary School (19) |
| Warren | 549 | 5 | Warren Village School (5) |
| Weare | 555 | 35 | Center Woods School (35) |
| White Mountains Regional | 568 | 28 | Lancaster Elementary School (16); Whitefield Elementary School (12) |
| Wilton-Lyndeborough Cooperative | 572 | 4 | Lyndeborough Central School (4) |
| Winchester | 573 | 33 | Winchester School (33) |
| Windham | 575 | 60 | Golden Brook Elementary School (60) |
| Winnisquam Regional | 582 | 19 | Winnisquam Early Learning Center (19) |

## kindergarten-day-length: Kindergarten Day Length by District

- kind: local
- question_type: local_practice
- description: Whether each district offers full-day or half-day kindergarten, from its own pages.

1. The Amherst School District offers full-day kindergarten; pre-K and kindergarten students attend the Clark School, and Wilkins School serves grades 1-4.
   - citation: Clark & Wilkins Elementary Schools - Welcome
   - source: https://sites.google.com/sau39.org/clarkwilkins/school-info/welcome
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Amherst
   - note: Page text: "Pre-K and full day kindergarten students attend the Clark School, while Wilkins School houses students in grades one through four." Page undated. Raw copy: raw/districts/batch-2/sau39-cw-welcome.txt
2. Auburn Village School lists its elementary school hours (kindergarten through grade 4) as 8:50 a.m. to 3:25 p.m.; no separate half-day kindergarten session is listed.
   - citation: Auburn Village School site (hours in page sidebar)
   - source: https://auburn.sau15.net/student-services/preschool-early-education-program-peep/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Auburn
   - note: Page text: "Elementary School (K-4) 8:50 a.m. - 3:25 p.m." The site does not use the words 'full day'; the statement reports posted hours only. Raw copy: raw/districts/batch-3/auburn-peep.txt
3. Barnstead Elementary School's 2026-27 school hours page lists one schedule for kindergarten through grade 8, 7:45 AM to 2:25 PM, Monday to Friday.
   - citation: Barnstead Elementary School - School Hours and Bell Schedule
   - source: https://bes.pmsau.nh.gov/o/bes/page/school-hours-and-bell-schedule
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barnstead
   - note: Page text: "School Hours K-8 For the 2026-2027 school year, the hours at Barnstead Elementary are 7:45 AM - 2:25 PM, Monday - Friday." The page gives hours for K-8 together and does not use the words 'full-day kindergarten'. Raw copy: raw/districts/batch-5/barnstead-bes-school-hours-and-bell-schedule.txt
4. The Bedford School District offers full-day kindergarten; the superintendent's FY2027 budget summary (December 2025) refers to the implementation of full-day kindergarten in 2025-26. Kindergarten is taught at the district's three elementary schools (Memorial, Peter Woodbury and Riddle Brook), which serve kindergarten through grade 4.
   - citation: Bedford School District, 12.01.25 Superintendent's Executive Summary FY27 (FY27 Budget Information for Website folder, linked from Business Services)
   - source: https://drive.google.com/file/d/1BstfNbxZKij42JDryLYQP-TZgriyyCVP/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bedford
   - note: Page text: "These enrollments are 56 students higher than our 9.03.24 projections. We believe this increase in students is due to the implementation of full day Kindergarten. ... All three schools educate Bedford students in grades Kindergarten through fourth grade." Memorial School's traffic procedures page (raw bedford-mem-traffic.txt) still describes morning and afternoon kindergarten sessions; it also places BEEP at Memorial, so it appears to predate 2026-27. A March 2025 news report (Union Leader via Yahoo) said voters approved full-day kindergarten funding 2,515-2,502; used only as a lead. Raw copy: raw/districts/batch-3/bedford-fy27-supt-summary.txt
5. The Brookline School District offers full-day kindergarten at Richard Maghakian Memorial School for eligible children living in Brookline.
   - citation: Richard Maghakian Memorial School - Kindergarten Registration
   - source: https://www.sau41.org/fs/pages/2136
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brookline
   - note: Page text: "RMMS welcomes all eligible children residing in Brookline, NH to our full-day Kindergarten program." Page text still refers to the 2025-2026 school year. Raw copy: raw/districts/batch-5/brookline-rmms-kindergarten.txt
6. The Candia School District's kindergarten at the Henry W. Moore School is a full-day program.
   - citation: Henry W. Moore School, Registration & Enrollment (Fall 2026 Kindergarten Registration)
   - source: https://candia.sau15.net/registration-enrollment/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Candia
   - note: Page text: "The Candia School District kindergarten program is a full day child-centered program developed to maximize each child's ability." Raw copy: raw/districts/batch-3/candia-registration.txt
7. The Chester School District offers full-day kindergarten at Chester Academy.
   - citation: Chester Academy - Kindergarten
   - source: https://ca.sau82nh.gov/grade_level_teams/kindergarten
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chester
   - note: Page text: "Chester Academy now offers a full day Kindergarten program" Raw copy: raw/districts/batch-4/chester-ca-kindergarten.txt
8. In the Claremont School District, the kindergarten parent guide says a kindergartner's school day starts at 8:30 and students are dismissed at 3:10. Kindergarten is at Disnard Elementary School (kindergarten to grade 2).
   - citation: Claremont School District, 'Ready, Set, Go! A Parent's Guide to Starting Kindergarten' (linked from Disnard Elementary's Kindergarten Handbook page https://www.des.sau6.org/kindergarten-handbook)
   - source: https://files.smartsites.parentsquare.com/6594/kindergarten_handbook.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Claremont
   - note: Page text: "What will my child’s day look like? ● The school day starts at 8:30 and students are dismissed at 3:10." The guide does not use the words 'full day'; it shows no school year. Grade span from SAU 6 Student Registration page. Raw copy: raw/districts/batch-6/claremont-k-handbook-pdf.txt
9. The Concord School District's school hours page lists kindergarten on the same hours as grades 1-5, 7:45 AM to 2:30 PM, at its elementary schools (Abbot-Downing, Beaver Meadow, Christa McAuliffe and Mill Brook).
   - citation: Concord School District - School Hours
   - source: https://sau8.org/school-hours
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Concord
   - note: Page text: "Abbot-Downing School ... Grades Start/Stop Time K-5 7:45 AM - 2:30 PM" The page gives hours by grade span (K-5; K-2 at Mill Brook) and does not use the words 'full-day kindergarten'. Raw copy: raw/districts/batch-5/concord-school-hours.txt
10. The Cornish School District offers full-day kindergarten at Cornish Elementary School (stated in its 2025-2026 pre-registration notice).
   - citation: Cornish Elementary School - Pre-Registration for Half-Day Pre-Kindergarten & Full-Day Kindergarten (2025-2026)
   - source: https://www.cornishschool.org/ourpages/auto/2024/6/26/50870748/PreK-K%20Pre-Enrollment%20Statement%202025-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Cornish
   - note: Page text: "PRE-REGISTRATION FOR HALF-DAY PRE-KINDERGARTEN & FULL-DAY KINDERGARTEN" Linked from the Registration Info page; this is the 2025-26 notice (no 2026-27 version posted). Raw copy: raw/districts/batch-2/cornish-prek-k-statement-2025-26.txt
11. In the Croydon School District, kindergarten at Croydon Village School is a full-day program, Monday to Friday, 8:00 to 2:15, with after-care available until 5:30 pm.
   - citation: Croydon Village School - A Day in the Life
   - source: https://croydonsd.org/cvs/day-in-the-life/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Croydon
   - note: Page text: "Kindergarten (8:00 – 2:15, Monday – Friday) Our full-day program enhances children’s growth and development through teacher-led activities and exploration." After-care from the program overview table at https://croydonsd.org/cvs/ (raw croydon-cvs.txt). Raw copy: raw/districts/batch-6/croydon-day.txt
12. The Derry Cooperative School District's kindergarten FAQ refers to its kindergarten students as full-day kindergarten students; kindergarten is offered at the district's elementary schools, which run 8:50 a.m. to 3:10 p.m. in 2026-27.
   - citation: Derry Cooperative School District, Kindergarten FAQs (linked from Registration - Kindergarten page)
   - source: https://docs.google.com/document/d/15yOA5xGqgl6y0CHtF3mI7OLmcKPA3gY_VWtHGE1B91g/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Derry Cooperative
   - note: Page text: "Is lunch offered for full-day Kindergarten students? Yes, Kindergarten students can participate in the school's general lunch program." Full-day status is stated indirectly in the FAQ question wording; the School Hours page lists 'Elementary Schools: 8:50 AM - 3:10 PM' for 2026-27 with no separate kindergarten session. Raw copy: raw/districts/batch-3/derry-k-faq.txt; raw/districts/batch-3/derry-school-hours.txt
13. The Fremont School District's Ellis School runs a full school day for kindergarten through grade 8, 8:20 am to 3:05 pm.
   - citation: Ellis School - SAU 83: School Hours
   - source: https://www.sau83.org/page/school-hours/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Fremont
   - note: Page text: "School Year Hours Full Day (K-8) 8:20 am - 3:05 pm" Site blocks curl; rendered in headless Chrome. Raw copy: raw/districts/batch-4/fremont-pages.txt
14. The Goffstown School District's kindergarten, at Glen Lake School, is a half-day program, with a morning session (drop-off 8:30-8:45, pickup 11:15) and an afternoon session (drop-off 12:30-12:45, pickup 3:15), Monday through Friday, with bus transportation both ways. Families state an AM or PM preference, and a lottery is used if requests exceed a session's capacity.
   - citation: SAU 19 - Glen Lake Kindergarten Registration
   - source: https://www.sau19.org/index.php/en/information-7/familes/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Goffstown
   - note: Page text: "Kindergarten is a half-day program. The morning session drop off is from 8:30 to 8:45 and the pickup is at 11:15 am. The afternoon session drop off is from 12:30 to 12:45 and the pickup is at 3:15 pm." Principal's message (https://www.sau19.org/index.php/en/information-7/about/principals-message) also says: 'Glen Lake School houses Goffstown's public kindergarten, which is a half-day program.' Raw copy: raw/districts/batch-7/goffstown-kindergarten-registration-sau19.txt
15. The Greenland School District's Greenland Central School (K-8) offers full-time kindergarten.
   - citation: SAU 50 - schools overview
   - source: https://www.sau50.org/pages/32bfca09-8390-4f0b-bc2d-c425b4ea9011
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Greenland
   - note: Page text: "Greenland Central School is a K-8 facility with a student enrollment of close to 400. The school features full-time kindergarten" Raw copy: raw/districts/batch-8/sau50-schools.txt
16. The Hampstead School Board approved a one-year pilot of universal full-day kindergarten for 2026-27 at Hampstead Central School: only full-day kindergarten is offered that year (no half-day option), and full-day tuition is waived for all students during the pilot. Kindergarten remains optional for children under 6.
   - citation: Hampstead Central School news - Full Day Kindergarten Pilot 2026-2027
   - source: https://hcs.hampsteadschools.net/o/hcs/article/2843048
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampstead
   - note: Page text: "the Hampstead School Board approved a pilot of universal full-day kindergarten for the 2026–2027 school year." Also: 'a half-day option will not be offered next year'; 'Full-day tuition will be waived for all students during the pilot year'. Article undated (spring 2026; mentions screening on Friday, May 8). Implies full-day kindergarten previously carried tuition; 2027-28 not stated. Raw copy: raw/districts/batch-8/hampstead-fdk-pilot.txt
17. In the Hampton Falls School District, kindergarten at Lincoln Akerman School follows the same hours as grades 1-8, 8:30 a.m. to 2:50 p.m., Monday through Friday (2026-27 family handbook).
   - citation: Lincoln Akerman School 2026-27 Family Handbook
   - source: https://docs.google.com/document/d/1qxbFt85CdOT9Bl2PC-E1kvkMXvhmhK_n18LrSwcJsPo/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton Falls
   - note: Page text: "Kindergarten - 8th grade - Monday through Friday 8:30 AM- 2:50 PM" Handbook linked from https://www.sau21.nh.gov/las/index; gives hours, not the words 'full-day'. Raw copy: raw/districts/batch-7/hamptonfalls-las-family-handbook-2026-27.txt
18. In the Holderness School District, kindergarten at Holderness Central School is a full-day program.
   - citation: Holderness Central School 2026-2027 Parent-Student Handbook (linked from https://sites.google.com/pemibaker.org/sau48/for-families/student-handbooks)
   - source: https://drive.google.com/file/d/1uNNd-UWyo6jTR4v1kWqp8pAdXPqqGzw6/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Holderness
   - note: Page text: "Kindergarten: at Holderness Central School is a full-day program." Raw copy: raw/districts/batch-6/holderness-handbook-2627.txt
19. The Hollis School District offers full-day kindergarten at Hollis Primary School.
   - citation: Hollis Primary School - Kindergarten Registration
   - source: https://www.sau41.org/fs/pages/1941
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hollis
   - note: Page text: "HPS is excited to welcome new students and families to our full day Kindergarten program." Raw copy: raw/districts/batch-5/hollis-hps-kindergarten.txt
20. The Hooksett School District offers full-day kindergarten to all incoming kindergarten students at Fred C. Underhill School; it began in the 2022-23 school year after voters approved the operating budget on March 8, 2022.
   - citation: Fred C. Underhill School, 'Full Day Kindergarten to be Implemented for the 2022-2023 School Year' (April 6, 2022; linked from the Hooksett School District site)
   - source: http://underhill.sau15.net/full-day-kindergarten/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hooksett
   - note: Page text: "The Hooksett School District will be offering Full Day Kindergarten to all incoming Kindergarten students at Fred C. Underhill School starting in the 2022-2023 School Year." Announcement dated 2022; still linked from hooksett.sau15.net navigation in Nov 2026. Raw copy: raw/districts/batch-3/hooksett-fdk.txt
21. The Hudson School District holds full-day kindergarten at Library Street School, part of its Early Learning Center; kindergarten hours are 8:50 am to 3:05 pm.
   - citation: Hudson School District - Early Learning Center home; hours from https://www.sau81.org/elc/aboutus/index
   - source: https://www.sau81.org/elc
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hudson
   - note: Page text: "Full-day kindergarten is held at Library Street school ... Kindergarten - Library Street Building, 22 Library Street ... Hours 8:50 am to 3:05pm" Raw copy: raw/districts/batch-5/hudson-elc-home.txt; raw/districts/batch-5/hudson-elc-about.txt
22. In the Keene School District, the Symonds School handbook (2025-26) says kindergarten students are dismissed at 2:35 PM; the school's hours are 8:00 AM to 2:40 PM. No district page found states 'full day' or 'half day' in words.
   - citation: Symonds School Handbook (SAU 29 School Handbooks folder)
   - source: https://docs.google.com/document/d/16dWArIceN0c9V36ycWNSohhtP6-O9LZWQH0cP-SfwJs/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Keene
   - note: Page text: "Kindergarten students who are being picked up by a parent will be dismissed at 2:35 PM. ... School Hours 8:00 AM - 2:40 PM" Evidence of a full school day at one Keene school (Symonds) only; Franklin, Fuller and Wheelock handbooks (2026-27) did not state kindergarten hours. Coordinator may prefer to treat as 'not found' for an explicit full/half-day statement. Handbooks folder: https://drive.google.com/drive/folders/1AHbNBroFGq-Wt9MNsMAG3JXrvlhYFIP5 Raw copy: raw/districts/batch-4/keene-symonds-school-handbook.txt
23. The Londonderry School District offers full-day kindergarten starting in 2026-27, at its three neighborhood elementary schools (Matthew Thornton, North and South). Voters approved the full-day kindergarten article (Article 3) on March 10, 2026, 3,255 yes to 1,369 no. Before 2026-27, kindergarten was held at Moose Hill School.
   - citation: Town of Londonderry, 2026 Town & School Election Results (official, March 10, 2026); Londonderry School District, Full Day Kindergarten in Neighborhood Schools 2026
   - source: https://www.londonderrynh.gov/DocumentCenter/View/2480/2026-03-10-Town-School-Election-Results-Official-PDF
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Londonderry
   - note: Page text: "School District Article 3 - Special Article - Full Day Kindergarten ... Yes 3,255 ... No 1,369 | Starting Full Day Kindergarten for 2026-27 School Year. | Kindergarten is at each of the elementary schoools." The results PDF is a scan; the quote and figures were transcribed by hand from page 3 into the .txt file. Plan page: https://www.londonderry.org/community/full-day-k-2026-project ('Starting Full Day Kindergarten for 2026-27 School Year... uses existing space in each of the neighborhood elementary schools'). Moose Hill page https://moose.londonderry.org: 'Kindergarten is at each of the elementary schoools.' The 2026-27 schedule itself (hours) was not found on a district page. Raw copy: raw/districts/batch-4/londonderry-2026-03-10-election-results.pdf; raw/districts/batch-4/londonderry-2026-03-10-election-results.txt; raw/districts/batch-4/londonderry-full-day-k-2026-project.txt; raw/districts/batch-4/londonderry-moosehill-home.txt
24. The Marlow School District provides full-day kindergarten at the John D. Perkins, Sr. Academy of Marlow; kindergarten follows the regular school day, according to the school's 2024-25 handbook.
   - citation: John D. Perkins, Sr. Academy of Marlow Student Handbook 2024-2025
   - source: https://drive.google.com/file/d/1ZEvjTSSpNPfO-XQc9L_5Wlw1AFaHwJ2w/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlow
   - note: Page text: "The Marlow School District provides half-day pre-kindergarten and full day kindergarten. Pre-kindergarten begins at 8:00 am and ends at 12:00 pm. The kindergarten program follows the same hours as the regular school day." Latest Marlow handbook in the SAU 29 handbooks folder is 2024-2025. Raw copy: raw/districts/batch-4/marlow-school-handbook.txt
25. The Mason School District offers full-day kindergarten at Mason Elementary School; kindergartners follow the same hours as the rest of the school, 8:50 a.m. to 3:25 p.m. (2025-26 kindergarten FAQ).
   - citation: Mason Elementary School, Kindergarten Frequently Asked Questions, 2025-2026 school year (linked from Registration page)
   - source: https://media.edlio.net/ae14b3c3/9a812a73/954805c2/f56c579e71444723ae1ec9e56653e1b7?_=Kindergarten-FAQ-25-26-sy.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mason
   - note: Page text: "How long is the kindergarten school day? Mason Elementary offers full day kindergarten. The students will follow the same school day hours as the rest of the school 8:50-3:25." Most recent FAQ posted is for 2025-26. Raw copy: raw/districts/batch-3/mason-k-faq-25-26.txt
26. The Mont Vernon School District offers full-day kindergarten at Mont Vernon Village School, which serves kindergarten through grade 6.
   - citation: Mont Vernon Village School - Welcome
   - source: https://sites.google.com/sau39.org/mvvs/school-info/welcome
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mont Vernon
   - note: Page text: "We offer a full day kindergarten program and grades first through sixth grade before we tuition our students into Amherst Middle School for seventh and eighth grade." Raw copy: raw/districts/batch-2/sau39-mvvs-welcome.txt
27. The Moultonborough School District offers full-day kindergarten at Moultonborough Central School, with bus service to and from school and lunch.
   - citation: Moultonborough Central School - welcome/about page
   - source: https://www.sau45.org/pages/ba451203-9b5d-44d1-a6ef-b17009a3275d
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Moultonborough
   - note: Page text: "The school offers full day kindergarten in which the students are able to ride the bus to and from school including lunch." Raw copy: raw/districts/batch-8/moultonborough-mcs-about.txt
28. The Nashua School District offers full-day kindergarten at each of its 12 elementary schools.
   - citation: Nashua School District - Frequently Asked Questions
   - source: https://www.nashua.edu/Page/717
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nashua
   - note: Page text: "Each of our 12 elementary schools offer full-day kindergarten." FAQ page is undated. Raw copy: raw/districts/batch-2/nashua-faq.txt
29. The New Boston School District began offering full-day kindergarten at New Boston Central School in fall 2026.
   - citation: SAU 19 - New Boston Central School Kindergarten 2026-27
   - source: https://www.sau19.org/index.php/en/information-6/familes/new-student-registration-nbcs
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Boston
   - note: Page text: "We are excited to announce that New Boston Central School will be offering Full Day Kindergarten starting in the Fall of 2026 !" Raw copy: raw/districts/batch-7/newboston-kindergarten-2026-27.txt
30. Newmarket Elementary School's Preparing for Kindergarten Handbook says kindergarten drop-off is between 8:30 and 8:40 a.m., when the school day begins, and that parent pick-up dismissal starts at 3:00 p.m. The handbook notes exact times are set each summer.
   - citation: Newmarket Elementary School - Preparing for Kindergarten Handbook (linked from the registration page)
   - source: https://docs.google.com/document/d/1XzXDFz71nmvQOH7CJtHdTIGJfe9Qsx3q/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newmarket
   - note: Page text: "Kindergarten students may be dropped off between 8:30 am and 8:40 am. Our school day begins promptly at 8:40 am." Also: 'Parent riders are dismissed starting at 3:00 pm and are done approx. 3:10 pm'. The handbook does not use the words 'full-day kindergarten'. Registration page says the handbook's dates and times are updated for 2026-27 in summer. Raw copy: raw/districts/batch-8/newmarket-k-handbook.txt
31. In the North Hampton School District, kindergarten at North Hampton School follows the same hours as grades 1-8, 8:25 a.m. to 2:50 p.m., Monday through Friday (2025-26 family handbook).
   - citation: North Hampton School Student & Family Handbook (August 2025)
   - source: https://docs.google.com/document/d/1kZE3qKrVZhh6HrHM6b570OOEH601BlXybEfrOkgLU2o/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district North Hampton
   - note: Page text: "Grades K-8 Monday through Friday - 8:25 am-2:50 pm" Handbook linked from northhamptonschool.org; gives hours, not the words 'full-day'. Raw copy: raw/districts/batch-7/northhampton-family-handbook.txt
32. The Pasquaney School District offers a full-day kindergarten program at Bridgewater-Hebron Village School; school hours are 8:00 a.m. to 2:35 p.m.
   - citation: Bridgewater-Hebron Village School - Kindergarten registration flyer (linked from https://www.sau108.org/ menu 'Kindergarten Registration')
   - source: https://aptg.co/x87s_j
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pasquaney
   - note: Page text: "WELCOME TO KINDERGARTEN FULL DAY PROGRAM BRIDGEWATER-HEBRON VILLAGE SCHOOL" School hours from the kindergarten page (https://www.sau108.org/page/kindergarten): 'School Hours: 8:00 AM to 2:35 PM'. Flyer undated. Raw copy: raw/districts/batch-8/pasquaney-k-registration.txt; raw/districts/batch-8/pasquaney-kindergarten.txt
33. A kindergarten welcome letter from New Franklin School's kindergarten teachers, posted on the Portsmouth School Department site, describes full-day kindergarten, with a daily schedule from 8:20 to about 2:05 and lunch at school. The letter is undated and does not cover the district's other elementary schools.
   - citation: Portsmouth School Department - 'Dear Kindergarten Families' (New Franklin School kindergarten letter)
   - source: https://www.portsmouthnh.gov/node/212545
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Portsmouth
   - note: Page text: "With full day kindergarten, we have lots of time to learn, explore, play, create, and reflect." No district-wide statement found; the letter is from Mrs. Shaw, Mrs. Hennigar and Mrs. Keil at New Franklin. Dondero and Little Harbour not stated. Raw copy: raw/districts/batch-8/portsmouth-node212545.txt
34. In the Seabrook School District, kindergarten at Seabrook Elementary School follows the same hours as grades 1-4, 8:00 a.m. to 2:30 p.m. (2026-27 handbook).
   - citation: Seabrook Elementary School Student Handbook 2026-2027
   - source: https://www.sau21.nh.gov/ses/files/documents/SESHandbook_2026-2027.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Seabrook
   - note: Page text: "Grades K-4: All Sessions 8:00 am to 2:30 pm" The handbook gives hours, not the words 'full-day'. Raw copy: raw/districts/batch-7/seabrook-ses-handbook-2026-27.txt
35. For 2026-27, the Timberlane Regional School District offers kindergarten as either a full day or a half day (morning only), Monday through Friday, at each neighborhood school (Atkinson Academy, Danville School, Pollard School and Sandown Central). Half-day kindergarten has no tuition; full-day kindergarten costs $4,500 for the school year, with financial aid available on request.
   - citation: Timberlane Regional School District - New Student Enrollment Process
   - source: https://www.timberlane.net/enrollment/student-enrollment/student-enrollment-process
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Timberlane Regional
   - note: Page text: "Kindergarten is offered through Full or Half Days (AM Only), Monday through Friday at each neighborhood school (Atkinson Academy, Danville School, Pollard School, and Sandown Central). ... Half day Kindergarten is district funded and has no tuition. ... Full day Kindergarten is $4,500 for the school year." The March 10, 2026 ballot (Article 14, two-thirds vote required) asked voters to amend the Articles of Agreement and raise $271,012 to implement full-day kindergarten (raw/districts/batch-2/timberlane-2026-warrant.txt). The result was not found on the district site; the enrollment page still lists $4,500 full-day tuition for 2026-27. Raw copy: raw/districts/batch-2/timberlane-enrollment-process.txt
36. In the Wilton-Lyndeborough Cooperative School District, kindergarten at Lyndeborough Central School is a full day; the 2025-26 kindergarten schedule said full days would start on Tuesday, September 2, with 2:15 pm dismissal.
   - citation: Lyndeborough Central School - Welcome to Kindergarten rollout schedule (posted July 7, 2025)
   - source: https://resources.finalsite.net/images/v1751915411/sau63org/zj7t672jnfa935bvrkgl/kindergartenrolloutschedule2025-1hasQRcode.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wilton-Lyndeborough Cooperative
   - note: Page text: "FIRST DAY OF KINDERGARTEN! We will start a full day on Tuesday September 2 nd Dismissal - 2:15pm" 2025-26 document; no 2026-27 schedule found. Raw copy: raw/districts/batch-4/wlc-lcs-k-schedule-2025.txt

## kindergarten-entry-cutoff: Kindergarten Entry Age Cutoff by District

- kind: local
- question_type: local_practice
- description: Each district's birthday cutoff for kindergarten entry (New Hampshire law sets no statewide entry age), from its policy or registration page.

1. In the Andover School District, children may enter kindergarten if they turn five on or before September 30 of the current school year (Policy JEB). A child whose fifth birthday falls within 14 days after September 30 may ask for an early entrance exception: parents send a written request to the Superintendent between January 1 and April 30 before the school year, and the School Board makes the final decision.
   - citation: Andover School Board Policy JEB - Entrance Requirements (approved 9.1.2026)
   - source: https://drive.google.com/file/d/1QACfMBhf2ZdwRTliVrWKN3RHq5lkGZFW/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Andover
   - note: Page text: "All children may enter kindergarten provided they become five (5) on or before September 30, of the current school year. Early Entrance Exception: The District recognizes that in rare circumstances a child whose fifth birthday falls within fourteen (14) days after the September 30 entrance cutoff date may demonstrate readiness for early admission." From the ASD Policies Drive folder (Section J) linked on the AEMS site. Raw copy: raw/districts/batch-1/andover-policy-jeb.txt
2. In the Ashland School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school, with no exceptions for early entrance (Policy JEB/5111). Grade one requires age six before September 30.
   - citation: Ashland Policy Manual JEB/5111 - Age of Entrance (linked from https://sau2.k12.nh.us/fs/pages/1490)
   - source: https://sau2.k12.nh.us/fs/resource-manager/view/f85ae488-966e-45ec-8566-5b4b615013a2
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Ashland
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year entering school. No exceptions shall be made for early entrance to kindergarten." Raw copy: raw/districts/batch-5/ashland-jeb.txt; raw/districts/batch-5/ashland-policies.txt
3. In the Auburn School District, a child entering kindergarten must be five years old on or before September 30 (Policy JEB: Age of Entrance).
   - citation: Auburn School District Policy JEB: Age of Entrance
   - source: https://auburnschoolboard.sau15.net/policy-manual/age-of-entrance/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Auburn
   - note: Page text: "A child entering kindergarten must be five years of age on or before September 30." Grade one: six before September 30. Same text on the Auburn Village School registration page. Raw copy: raw/districts/batch-3/auburn-jeb.txt
4. In the Barnstead School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school.
   - citation: Barnstead Elementary School - Kindergarten Registration
   - source: https://bes.pmsau.nh.gov/o/bes/page/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barnstead
   - note: Page text: "Children may enter kindergarten if their chronological age will be five before September 30th of the year entering school." Policy JEB itself not retrieved. Raw copy: raw/districts/batch-5/barnstead-bes-kindergarten-registration.txt
5. In the Bartlett School District, a pupil may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB).
   - citation: Bartlett School Board Policy JEB - Age of Entrance (adopted June 7, 1983)
   - source: https://drive.google.com/file/d/1Gqo2jisKB4msUU3EFvwIQfNwwtlyeHT8/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bartlett
   - note: Page text: "A pupil may enter kindergarten if his/her chronological age will be five before September 30 of the year entering school." Bartlett also posts JEBA Delayed Entry Procedure and JEBB (requests to waive minimum age) in the same Section J folder; not read in detail. Raw copy: raw/districts/batch-1/bartlett-policy-jeb.txt
6. In the Bath School District, a pupil may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB).
   - citation: SAU 23 Board Policies, Section J (Google Doc linked from https://www.sau23.org/sau-23/school-boards/board-policies)
   - source: https://docs.google.com/document/d/19lj7kHI12uVHodbLgGILRoN2TS8Mi_sr7qk6aaeHi60/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bath
   - note: Page text: "JEB ENTRANCE AGE (Bath and Piermont) ... A pupil may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Adopted by Bath School Board March 12, 2009. Raw copy: raw/districts/batch-1/sau23-policies-section-j.txt
7. In the Bedford School District, a child must be five years old by September 30 of the year of entering school to be admitted to kindergarten (Policy JEB, revised 4/10/17). The policy's early-entrance provision (Appendix JEB-R) applies to grade one, not kindergarten.
   - citation: Bedford Policy JEB: Entrance Age Requirements (SAU #25 Policy Manual, Section J)
   - source: https://drive.google.com/file/d/0B4UPrDTt00nyY3p1UURjb3dpbTA/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bedford
   - note: Page text: "A child must have attained age five by September 30 th of the year of entering school to be admitted to the kindergarten program." Grade one: age six by September 30; early entrance for children born in October-December only for grade one, per Appendix JEB-R. Raw copy: raw/districts/batch-3/bedford-jeb.txt
8. In the Berlin Public Schools, a child may enter kindergarten if they will be five before September 30 of the year of entry, and grade one if they will be six before September 30 (Policy JEB, adopted December 6, 2012). A birth certificate is required at registration.
   - citation: Berlin Public Schools Policy JEB - Age of Entrance
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3537/Bps/6c17af10-e062-49f3-b011-ae4af4cd196b/JEB_-_AGE_OF_ENTRANCE.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Berlin
   - note: Page text: "A student may enter kindergarten if his/her chronol ogical age will be five before September 30" Linked from https://www.sau3.org/documents/school-board/school-board-policies/j.-students/420724. PDF text extraction splits some words (e.g. 'chronol ogical'). Raw copy: raw/districts/batch-2/berlin-jeb.txt
9. In the Bethlehem School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB, joint SAU 35 policy). Under Policy JEBA, a child whose fifth birthday falls between October 1 and October 31 may be allowed to enter kindergarten if the superintendent finds the child ready.
   - citation: White Mountains SAU35 School Board Policy JEB and JEBA (joint policy for Bethlehem, Lafayette, Landaff, Lisbon, and Profile)
   - source: https://docs.google.com/document/d/17PoXZWcc9K3zCpAnOorTuz-x-w74EXyRoaME69LdR2Q/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bethlehem
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. | A child whose fifth birthday falls between October 1 and October 31st, may be allowed to enter kindergarten if skills and maturity level strongly indicate readiness" Raw copy: raw/districts/batch-4/sau35-policy-jeb.txt; raw/districts/batch-4/sau35-policy-jeba.txt
10. In the Brentwood School District, a child may enter kindergarten if they will be five on or before September 30 of the year they start school (Policy JEB, Age of Entrance). A child whose fifth birthday falls between October 1 and October 31 may be allowed to enter if an assessment by the superintendent or designee shows strong readiness.
   - citation: Brentwood School Board Policy JEB, Age of Entrance (linked from the district's SAU 16 policy page https://www.sau16.org/pages/1814df78-8221-4e53-92cf-183369bf185f)
   - source: https://drive.google.com/file/d/1_0MsvDsb4irmELSgdPXXHcx9Bxd8FBf_/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brentwood
   - note: Page text: "A student may enter kindergarten if their chronological age will be ﬁve on, or before, September 30th of the year of entering school." Each SAU 16 district has its own JEB; text checked separately for each. Raw copy: raw/districts/batch-8/brentwood-jeb.txt
11. In the Candia School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school. A child who will be five by October 31 may be considered for early admission if the parent returns an Early Admission Request form and information packet to the District Office by June 1; there are no exceptions for birth dates after October 31 (Policy JEB, policy date 06/05/2025).
   - citation: Candia School District Policy JEB: Entrance Age
   - source: https://candiaschoolboard.sau15.net/policy-manual/entrance-age/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Candia
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. A child will be considered for early admission into kindergarten if the following condition is met: the child will be at least five years old by October 31" Registration page states 'Children who will be 5 years old by September 30th may be registered for Kindergarten.' Raw copy: raw/districts/batch-3/candia-jeb.txt
12. In the Chesterfield School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB).
   - citation: Chesterfield School District Policy JEB - Age of Entrance (approved CSB 10/10/11)
   - source: https://drive.google.com/file/d/1WmiQVxYLsVM9RI8BNS_Ypj0fZqa0usXC/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chesterfield
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Linked from https://che.sau29.org/about/chesterfield-school-board/chesterfield-district-policies. Same text is in the 2026-27 school handbook. The SAU 29 towns registration page also says 'Children residing in Chesterfield must be at least five years of age by September 30, 2021' (outdated year). Raw copy: raw/districts/batch-4/chesterfield-policy-jeb.txt
13. In the Chichester School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB, approved October 2025).
   - citation: Chichester School District Policy JEB - Age of Entrance
   - source: https://drive.google.com/file/d/1KCh3fHhvlxWlqz0FKvSREQ7Th65RqK7f/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chichester
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Also quoted on the CCS Parent FAQs page (https://ccs.sau53.org, 'Parent FAQs'). Raw copy: raw/districts/batch-7/sau53-chichester-jeb.txt; raw/districts/batch-7/sau53-ccs-parent-faqs.txt
14. In the Claremont School District, a child who will be 5 years old on or before September 30, 2026 can register for kindergarten for fall 2026.
   - citation: SAU #6 - Student Registration
   - source: https://www.sau6.org/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Claremont
   - note: Page text: "If your child will be 5 years old on or before September 30, 2026, please call your child's neighborhood school for Fall 2026. Disnard Elementary School will reach out to you to schedule your child’s Kindergarten Screening." Policy JEB not checked: the board policy manual is a Google Doc (https://docs.google.com/document/d/1JmygIGNaVc8ZfaQWtoIA25tRaBGw2Oh5k5ARsGlreqg/edit) not opened. Raw copy: raw/districts/batch-6/claremont-registration.txt
15. In the Colebrook School District, a student may enter kindergarten if he or she will be five before September 30 of the year of entering school (SAU 7 Policy JEB). Parents may send the Board a written request, no later than April 30 of the prior school year, to enroll a child who does not meet the age rule; the child is tested for readiness and the Board decides before the school year.
   - citation: SAU #7 Policy JEB - Age of Entrance (adopted by Colebrook 10/16/2018, Pittsburg 10/22/2018, Stewartstown 10/8/2018)
   - source: https://drive.google.com/file/d/15IqA9RAd_ZjmuI5BC2bqtFXb9QcbPKH5/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Colebrook
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. ... Any parent who approaches the Board with a special written request, no later than April 30th of the prior school year, to have their son or daughter enrolled in kindergarten after the age criteria currently in place, will have that request reviewed and their child tested for readiness." Policy states its adoption by the Colebrook, Pittsburg and Stewartstown school boards. Linked from https://www.sau7.org/en-US/pages/0b1e2b2d-b90a-43b2-9ed1-a527abe867a5 Raw copy: raw/districts/batch-1/sau7-policy-jeb.txt
16. In the Concord School District, a child must be five years old on or before September 30 to start kindergarten, with no exceptions (Policy 512, Entrance Age). For 2026-27 that means five on or before September 30, 2026.
   - citation: Concord School District - Registration
   - source: https://sau8.org/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Concord
   - note: Page text: "Students starting kindergarten must be 5 years old on or before September 30. There are NO exceptions (Policy 512, Entrance Age)" Same page: preschool age 3 by Sept 30, 2026; grade 1 age 6 by Sept 30, 2026. Raw copy: raw/districts/batch-5/concord-registration.txt
17. In the Contoocook Valley (ConVal) School District, a child may enter kindergarten only if he or she is five years old before September 30 of the school year of entry; the superintendent may grant a waiver for exceptions (Policy JEB, adopted June 5, 2018).
   - citation: ConVal School Board Policy JEB - Entrance Age
   - source: https://schoolboard.conval.edu/content/d2bf8137-8f48-4280-bf6a-3a84f8fad17f/28239/5419?type=accordion
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Contoocook Valley
   - note: Page text: "A child may only enter Kindergarten if his/her chronological age is five (5) before September 30 of the school year of entry. The Superintendent is hereby authorized to grant a waiver for exceptions to the Kindergarten entrance age." Grade one: age six before September 30. Superintendent decisions may be appealed to the School Board. Raw copy: raw/districts/batch-3/conval-jeb.txt
18. In the Cornish School District, students entering kindergarten must be five years old on or before September 30.
   - citation: Cornish School District - Registration Information
   - source: https://www.cornishschool.org/apps/pages/index.jsp?uREC_ID=581844&type=d
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Cornish
   - note: Page text: "Students entering kindergarten must be 5 years of age on or before September 30th." Raw copy: raw/districts/batch-2/cornish-registration.txt
19. In the Croydon School District, kindergartners must be 5 years old as of September 30 of the school year in which they enroll.
   - citation: Croydon School District - Enrollment (Pre-K & K)
   - source: https://croydonsd.org/cvs/enrollment/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Croydon
   - note: Page text: "Kindergarteners must be 5 years old as of September 30 of the school year in which they are enrolling." Raw copy: raw/districts/batch-6/croydon-cvs-enrollment.txt
20. In the Deerfield School District, children who are five years old by September 30 are eligible for kindergarten (Policy JEA, School Entry and Enrollment).
   - citation: Deerfield School District Policy JEA - School Entry & Enrollment
   - source: https://drive.google.com/file/d/1bjEy8-6ljf6xzkBqp7bMoOxpP0jzHGR6/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Deerfield
   - note: Page text: "Children who are five years of age by September 30 are eligible for kindergarten." Same rule on the DCS New Student Registration page (https://dcs.sau53.org/pages/917e280b-a99e-4077-b8ef-76c1878f58eb): 'Children who are 5 years of age by September 30th are eligible for kindergarten.' Policy found in the Deerfield policy Google Drive folder linked from the SAU 53 Deerfield page. Raw copy: raw/districts/batch-7/sau53-deerfield-jea.txt; raw/districts/batch-7/sau53-dcs-new-student-registration.txt
21. In the Derry Cooperative School District, children must be five years old on or before September 30 of the school year to be eligible for kindergarten.
   - citation: Derry Cooperative School District, Kindergarten FAQs
   - source: https://docs.google.com/document/d/15yOA5xGqgl6y0CHtF3mI7OLmcKPA3gY_VWtHGE1B91g/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Derry Cooperative
   - note: Page text: "Children must be 5 years old on or before September 30, of the school year to be eligible to attend Kindergarten." Policy JEB itself not located on sau10.nh.gov. Raw copy: raw/districts/batch-3/derry-k-faq.txt
22. In the Dover School District, a child must be five years old on or before September 30 to enter kindergarten, and six on or before September 30 to enter first grade (Policy JEB). A child who does not meet the first-grade age but has completed an approved or licensed kindergarten program may enter first grade after passing the district's screening.
   - citation: Dover School District Policy JEB, School Entrance Requirements (adopted October 10, 2005)
   - source: https://4.files.edl.io/3800/04/05/21/145053-46f744e3-afbb-49d6-b9e0-3087d8521cc5.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dover
   - note: Page text: "In order to enter first grade in the Dover School District, a child must be six years of age on or before September 30. Kindergarten students must be five years of age on or before September 30." Linked from the SAU 11 Student Registration page. Raw copy: raw/districts/batch-8/dover-jeb.txt
23. In the East Kingston School District, a child may enter kindergarten if they will be five on or before September 30 of the year they start school (Policy JEB, Age of Entrance). A child whose fifth birthday falls between October 1 and October 31 may be allowed to enter if an assessment by the superintendent or designee shows strong readiness.
   - citation: East Kingston School Board Policy JEB, Age of Entrance (linked from the district's SAU 16 policy page https://www.sau16.org/pages/5d3baeb8-267d-43b8-a93c-c2810a81f3e9)
   - source: https://drive.google.com/file/d/1JrXj_BA4CcmU0k2hmkL-O76JMk8MfMzh/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district East Kingston
   - note: Page text: "A student may enter kindergarten if their chronological age will be ﬁve on, or before, September 30th of the year of entering school." Each SAU 16 district has its own JEB; text checked separately for each. Raw copy: raw/districts/batch-8/eastkingston-jeb.txt
24. In the Epping School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school; exceptions may be considered individually, with the final decision made by the school principal (Policy JEB).
   - citation: Epping School District Policy JEB - Age of Attendance and Entrance
   - source: https://www.sau14.org/school-board/files/documents/JEB%20-%20Age%20of%20Attendance%20and%20Entrance.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epping
   - note: Page text: "Kindergarten - A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. Exceptions to this requirement may be considered on an individual basis. Final decision as to admission will be made by the school building principal." Linked from https://www.sau14.org/school-board/policyj Raw copy: raw/districts/batch-4/epping-policy-jeb.txt
25. In the Epsom School District, children must be five years old by September 30 to be eligible for kindergarten (Policy JEA, School Entry and Enrollment).
   - citation: Epsom School District Policy JEA - School Entry and Enrollment
   - source: https://drive.google.com/file/d/1O5niL9BRB-ondacjB55GqCq85OYgmriP/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epsom
   - note: Page text: "Children must be five years of age by September 30 to be eligible for kindergarten." From the Epsom policy Google Drive folder (Section J) linked on the SAU 53 Epsom page. Raw copy: raw/districts/batch-7/sau53-epsom-jea.txt
26. In the Exeter School District, a child may enter kindergarten if they will be five on or before September 30 of the year they start school (Policy JEB, Age of Entrance). A child whose fifth birthday falls between October 1 and October 31 may be allowed to enter if an assessment by the superintendent or designee shows strong readiness.
   - citation: Exeter School Board Policy JEB, Age of Entrance (linked from the district's SAU 16 policy page https://www.sau16.org/pages/157ae0ff-5334-4829-b1f5-d8fb6b395c84)
   - source: https://drive.google.com/file/d/1yg1SvKdcj4QfryqUQs50uQkqH50LUI8N/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Exeter
   - note: Page text: "A student may enter kindergarten if their chronological age will be ﬁve on, or before, September 30th of the year of entering school." Each SAU 16 district has its own JEB; text checked separately for each. Raw copy: raw/districts/batch-8/exeter-jeb.txt
27. In the Franklin School District, a pupil may enter kindergarten if he or she will be five on or before September 30 of the year of entering school (Policy JEB).
   - citation: Franklin Board Policy JEB - Age of Entrance (adopted June 21, 1993; reviewed 8-01-2017)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/1695/Sau_18/73db6abb-057e-4991-8d37-2f5402e55341/JEB_-_Age_of_Entrance_-__8-2017.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Franklin
   - note: Page text: "A pupil may enter kindergarten if his/her chronological age will be five on or before September 30th of the year entering school." Linked from Section J at https://www.sau18.nh.gov/browse/155746. Raw copy: raw/districts/batch-1/franklin-policy-jeb.txt
28. In the Goffstown School District, a child born between October 1, 2020 and September 30, 2021 is eligible for kindergarten in 2026-27 (that is, five years old by September 30, 2026).
   - citation: SAU 19 - Glen Lake Kindergarten Registration
   - source: https://www.sau19.org/index.php/en/information-7/familes/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Goffstown
   - note: Page text: "If your child was born between October 1, 2020 and September 30, 2021, your child is eligible to attend kindergarten for the 2026/2027 school year." Goffstown policy manual (GSD Policies page) not checked for JEB; registration page states the birth-date range. Raw copy: raw/districts/batch-7/goffstown-kindergarten-registration-sau19.txt
29. In the Governor Wentworth Regional School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school, and grade one if six before September 30 (Policy JEB, revised March 10, 2025). A birth certificate is required at registration.
   - citation: GWRSD Policy JEB - Age of Entrance (revised 3/10/2025)
   - source: https://gwrsd.sau49nh.gov/fs/resource-manager/view/38d18f5b-f9f8-425e-8235-fb5874eb2339
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Governor Wentworth Regional
   - note: Page text: "A student may enter kindergarten if their chronological age will be five (5) before September 30th of the year of entering school." The New Durham School registration page phrases it as 'turning five before September 30, 2026'. Raw copy: raw/districts/batch-5/gwrsd-jeb.txt
30. In the Grantham School District, children who are five years old by September 30 of the school year are expected to be in kindergarten, according to the Grantham Village School preschool page.
   - citation: Grantham Village School - Preschool
   - source: https://www.gvshawks.org/apps/pages/index.jsp?uREC_ID=3298781&type=d&pREC_ID=2578756
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Grantham
   - note: Page text: "(Students who are 5 years old by September 30th of the current academic year are expected to be in Kindergarten.)" Stated on the preschool page; policy JEB itself not checked (policies page at /apps/pages/index.jsp?uREC_ID=3442716&type=d&pREC_ID=2373610). Raw copy: raw/districts/batch-5/grantham-preschool.txt
31. In the Greenland School District, a child is eligible to enter kindergarten if they will be five on or before September 30 of the year they plan to start school (SAU 50 Policy JEB, School Age Requirements, which applies to the Rye, Greenland, New Castle (Maude H. Trefethen) and Newington schools).
   - citation: SAU 50 School Boards - Board Policies, JEB School Age Requirements
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Greenland
   - note: Page text: "A student will be eligible to enter kindergarten if his/her chronological age will be five on or before September 30 of the year the student plans to enter school." Page: 'These policies are for the Rye, Greenland, Maude H. Trefethen and Newington Schools.' Maude H. Trefethen is New Castle's school. Raw copy: raw/districts/batch-8/sau50-policies.txt
32. In the Hampstead School District, a child may enter kindergarten if they will be five before September 30 of the year they start school, and grade 1 if they will be six before September 30 (Policy JEB, Age of Entrance, revised April 9, 2024).
   - citation: Hampstead School District Policy JEB, Age of Entrance (Section J folder linked from https://www.hampsteadschools.net/page/policies-procedures)
   - source: https://drive.google.com/file/d/0Bx44V0b00-beMzdnWDNiNkczY28/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampstead
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of enter ing school." Policy says 'before September 30' (not 'on or before'). Raw copy: raw/districts/batch-8/hampstead-jeb.txt
33. In the Hampton School District, a child may enter kindergarten if they will be five before September 30 of the year they start school, and grade 1 if they will be six before September 30 (Policy JEB, Age of Entrance).
   - citation: Hampton School District Policy JEB, Age of Entrance (linked from https://www.sau90.org/o/sau-90/page/hampton-school-district-policies)
   - source: https://5il.co/stlh
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." The policy says 'before September 30', not 'on or before'. Adopted March 21, 1988 and January 11, 2011. Raw copy: raw/districts/batch-8/hampton-jeb.txt
34. In the Hampton Falls School District, kindergarten students must be five years old before October 1 of the school year.
   - citation: Lincoln Akerman School - Student Registration
   - source: https://www.sau21.nh.gov/las/about-las/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton Falls
   - note: Page text: "Kindergarten students must be 5 years old prior to October 1 of the school year." Raw copy: raw/districts/batch-7/hamptonfalls-las-registration.txt
35. In the Harrisville School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB).
   - citation: Harrisville School District Policy JEB - Age of Entrance (approved HSB 11/25/19)
   - source: https://drive.google.com/file/d/1KrdNQqcgQVkk-doKbBOZfab17GN_eonQ/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Harrisville
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." The attached administrative procedure says 'on or before September 30'. Raw copy: raw/districts/batch-4/harrisville-policy-jeb.txt
36. In the Haverhill Cooperative School District, a pupil may enter kindergarten if he or she will be five before October 1 of the year of entering school (Policy JEB, Haverhill version).
   - citation: SAU 23 Board Policies, Section J (Google Doc linked from https://www.sau23.org/sau-23/school-boards/board-policies)
   - source: https://docs.google.com/document/d/19lj7kHI12uVHodbLgGILRoN2TS8Mi_sr7qk6aaeHi60/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Haverhill Cooperative
   - note: Page text: "JEB ENTRANCE AGE (Haverhill) ... A pupil may enter kindergarten if his/her chronological age will be five before October 1 of the year of entering school." SAU 23's policy document has separate JEB versions: Bath and Piermont (September 30), Warren (October 15), Haverhill (October 1). Adopted by Haverhill Cooperative School Board March 19, 2009. Raw copy: raw/districts/batch-1/sau23-policies-section-j.txt
37. In the Henniker School District, Henniker Community School's registration page says children can start kindergarten if they reach age five by September 30 of the school year.
   - citation: Henniker Community School, Student Registration
   - source: https://www.sau24.org/schools/hennikercommunityschool/about-us/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Henniker
   - note: Page text: "Students can start kindergarten if they reach the age of five by September 30th of the school year." Policy manual on Simbli (hCaptcha); not read. Raw copy: raw/districts/batch-3/sau24-hennikercommunityschool-reg.txt
38. In the Hillsboro-Deering Cooperative School District, children registering for kindergarten for 2026-27 at Hillsboro-Deering Elementary School must live in Hillsboro, Deering or Windsor and be 5 years old on or before September 30, 2026.
   - citation: SAU #34 News, '2026-2027 Hillsboro-Deering Elementary School Kindergarten Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hillsboro-Deering Cooperative
   - note: Page text: "Children must reside in Hillsboro, Deering or Windsor and be 5 yrs. old on or before 9/30/2026." Policy JEB not checked. Raw copy: raw/districts/batch-6/sau34-home.txt
39. In the Holderness School District, a child who turns five after September 30 cannot attend kindergarten until the following school year.
   - citation: Holderness Central School 2026-2027 Parent-Student Handbook
   - source: https://drive.google.com/file/d/1uNNd-UWyo6jTR4v1kWqp8pAdXPqqGzw6/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Holderness
   - note: Page text: "Kindergarten Registration: A child who reaches his or her fifth birthday after September 30th cannot attend school until the following school year." Raw copy: raw/districts/batch-6/holderness-handbook-2627.txt
40. In the Hooksett School District, a child entering kindergarten must be five years old on or before September 30 (Policy JEB, policy date 10/21/2025).
   - citation: Hooksett School District Policy JEB: Entrance Age
   - source: https://hooksettschoolboard.sau15.net/policy-manual/entrance-age/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hooksett
   - note: Page text: "A child entering kindergarten must be five years of age on or before September 30th." Grade one: six on or before September 30. No early-entrance provision in the policy text. Raw copy: raw/districts/batch-3/hooksett-jeb.txt
41. In the Hudson School District, a child must be five years old on or before September 30 to attend kindergarten.
   - citation: Hudson School District - Registration
   - source: https://www.sau81.org/families/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hudson
   - note: Page text: "A child must be 5 years of age on or before September 30 to attend Kindergarten." A search snippet mentioned an early/delayed entrance waiver under Policy JEB with a March 15, 2026 deadline, but that text is no longer on the registration page; policy JEB itself not retrieved. Raw copy: raw/districts/batch-5/hudson-registration.txt
42. In the Inter-Lakes School District, a child is eligible for kindergarten if he or she will be at least five years old on or before September 30 of that year (Policy JEB/5111). Early admission can be considered for a child who will be five on or by October 31, after a written request to the Superintendent (preferably by mid-August) and district assessments in July and August.
   - citation: Inter-Lakes Policy JEB/5111 - Age of Entrance (Kindergarten), linked from https://www.interlakes.org/school-district-policies
   - source: https://www.interlakes.org/fs/resource-manager/view/c089dce8-e27d-45b3-9779-2d22f20466dc
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Inter-Lakes Cooperative
   - note: Page text: "A student is eligible to enter Kindergarten if the student will be at least five (5) years old on or before September 30th of that year. ... Early admission will be considered for a child who will be at least at least five (5) years old on or by October 31st of the year for which admittance is requested to kindergarten" Grade 1: six on or before September 30. Raw copy: raw/districts/batch-5/interlakes-jeb.txt
43. In the Jackson School District, children who are 5 years old on or before September 30, 2026 were eligible to register for kindergarten for 2026-27.
   - citation: Jackson Grammar School - Preschoolers and Kindergarten Registration
   - source: https://jgs.sau9.org/kindergartenregistration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jackson
   - note: Page text: "Children who are 5 years of age on or before September 30, 2026, are eligible to register for Kindergarten." Jackson policy folder not checked for JEB. Raw copy: raw/districts/batch-1/jackson-jgs-kindergarten-registration.txt
44. In the Jaffrey-Rindge Cooperative School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school, and grade one if six before September 30 (Policy JEB, approved June 6, 2005). A birth certificate is required at registration.
   - citation: JRCSD Policy JEB - Age of Entrance (linked from the district policy list at https://www.sau47.org/school_board/DistrictPoliciesLink)
   - source: https://drive.google.com/file/d/15wySaBPj5Ll-My79KqVhstieZ-KEzQjE/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jaffrey-Rindge Cooperative
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Raw copy: raw/districts/batch-5/jaffrey-rindge-jeb.txt; raw/districts/batch-5/jaffrey-rindge-policy-list.xlsx
45. In the Kearsarge Regional School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB). The district will consider parent requests for early enrollment of a child who turns five between October 1 and December 31; the child must complete a pre-approved evaluation, at the parents' expense, showing readiness at the 98th percentile or above in all areas, and the Superintendent decides.
   - citation: Kearsarge Regional School District Policy JEB - Age of Entrance (revised 11/12/17)
   - source: https://www.kearsarge.org/district/school-board-mbc/pages/jeb-age-entrance
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kearsarge Regional
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five years before September 30 of the year of entering school." The 2026-27 kindergarten registration flyer also says 'Must be 5 by Sept. 30th'. Raw copy: raw/districts/batch-6/kearsarge-jeb.txt
46. In the Keene School District, a child is eligible for kindergarten if they have reached age 5 by September 30, with no exceptions for early entrance (Policy JEB).
   - citation: Keene School District Policy JEB - Age of Entrance Requirements (approved 3/21/17)
   - source: https://drive.google.com/file/d/1YGa3cUgld8EN_UqwFAHTRgy2_Nr3o27n/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Keene
   - note: Page text: "Students shall be eligible to attend kindergarten if they have reached age 5 by September 30, with no exceptions made for early entrance." Linked from https://www.keeneschoolsnh.org/ksd/kne-board-and-policies/kne-school-board-policies (Google Drive folder). Keene K enrollment form also says 'Must be 5 by September 30th'. Raw copy: raw/districts/batch-4/keene-policy-jeb.txt
47. In the Kensington School District, a child may enter kindergarten if they will be five on or before September 30 of the year they start school (Policy JEB, Age of Entrance). A child whose fifth birthday falls between October 1 and October 31 may be allowed to enter if an assessment by the superintendent or designee shows strong readiness.
   - citation: Kensington School Board Policy JEB, Age of Entrance (linked from the district's SAU 16 policy page https://www.sau16.org/pages/df9dccc0-5a8f-479f-9159-8939e0cdbc7f)
   - source: https://drive.google.com/file/d/1xAye5X4O0jYSaTZgWV2xo9AUI-En0FFE/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kensington
   - note: Page text: "A student may enter kindergarten if their chronological age will be ﬁve on, or before, September 30th of the year of entering school." Each SAU 16 district has its own JEB; text checked separately for each. Raw copy: raw/districts/batch-8/kensington-jeb.txt
48. In the Laconia School District, the cutoff for kindergarten admission is age five by September 30, and for grade one, age six by September 30 (Policy JEB).
   - citation: Laconia School District Policy JEB - Entrance Age Requirements (last revised 11/7/2001)
   - source: https://drive.google.com/file/d/1JsMU8uEM7YUQPF3a6cT1_TAMRIVSCG6g/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Laconia
   - note: Page text: "The cutoff date for kindergarten admissions shall be age five (5) by September 30" Linked from https://www.sau30.org/j.html (Section J policy index). Raw copy: raw/districts/batch-2/laconia-jeb.txt
49. In the Lafayette Regional School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB, joint SAU 35 policy). Under Policy JEBA, a child whose fifth birthday falls between October 1 and October 31 may be allowed to enter kindergarten if the superintendent finds the child ready.
   - citation: White Mountains SAU35 School Board Policy JEB and JEBA (joint policy for Bethlehem, Lafayette, Landaff, Lisbon, and Profile)
   - source: https://docs.google.com/document/d/17PoXZWcc9K3zCpAnOorTuz-x-w74EXyRoaME69LdR2Q/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lafayette Regional
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. | A child whose fifth birthday falls between October 1 and October 31st, may be allowed to enter kindergarten" Raw copy: raw/districts/batch-4/sau35-policy-jeb.txt; raw/districts/batch-4/sau35-policy-jeba.txt
50. For the Landaff School District, the joint SAU 35 policy says a child may enter kindergarten if he or she will be five before September 30 of the year of entering school, with possible early entrance for October birthdays at the superintendent's discretion (Policies JEB and JEBA).
   - citation: White Mountains SAU35 School Board Policy JEB and JEBA
   - source: https://docs.google.com/document/d/17PoXZWcc9K3zCpAnOorTuz-x-w74EXyRoaME69LdR2Q/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Landaff
   - note: Page text: "White Mountains SAU35 Bethlehem, Lafayette, Landaff, Lisbon, and Profile School Board Policy Age of Entrance ... A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Landaff tuitions all students; the receiving school's own entry rules may also apply. Raw copy: raw/districts/batch-4/sau35-policy-jeb.txt; raw/districts/batch-4/sau35-policy-jeba.txt
51. In the Lebanon School District, the enrollment page asks families of children who will be 5 (kindergarten) or 6 (grade 1) on or before September 30, 2026 to call for an enrollment appointment, and refers to School Board Policy JEB - Age of Entrance.
   - citation: Lebanon School District (SAU 88), Enrollment
   - source: https://www.sau88.net/families/enrollment
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lebanon
   - note: Page text: "If your child will be 5/6 years old on or before Sept. 30, 2026 please call to set an enrollment appointment. School Board Policy: JEB - Age of Entrance" Policy JEB on the Diligent/HighBond portal (https://sau88.community.highbond.com/home/policies/policydoc/aff3b5e4-e58f-44bf-85db-98dc50d0b1f1) did not render its text in headless Chrome. Raw copy: raw/districts/batch-3/lebanon-enroll.txt
52. In the Lempster School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school, and grade one if six before September 30 (Policy JEB, adopted June 14, 2016). A birth certificate is required at registration.
   - citation: Lempster Policy JEB - Age of Entrance (linked from https://www.sau71.org/documents/resources/for-school-board/school-board-policies/j---students/22251747)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5611/Lsau/1ccb7cd3-ac73-4382-b7b5-e59725fe9bcd/JEB_-_Age_of_Entrance.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lempster
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Raw copy: raw/districts/batch-5/lempster-jeb.txt; raw/districts/batch-5/lempster-policies-j.txt
53. In the Lincoln-Woodstock Cooperative School District, a child may enter kindergarten if he or she will be five on or before September 30 of the year of entering school; exceptions may be granted with the Superintendent's approval (Policy JEB). For 2026-27 the district asked families of children who will be five by September 30, 2026 to register.
   - citation: Lincoln-Woodstock Cooperative School District Policy JEB - Age of Entrance
   - source: https://www.lin-wood.org/fs/resource-manager/view/445161ce-117c-4198-9ba3-45f6e0cbab47
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lincoln-Woodstock Cooperative
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five on or before September 30th of the year of entering school. Exceptions to the age requirement may be granted with the approval of the Superintendent." Linked from https://www.lin-wood.org/about-lin-wood/enrollment, which also lists Policy JEBA, Early Entrance Into Kindergarten (not read). Raw copy: raw/districts/batch-7/linwood-jeb.txt; raw/districts/batch-7/linwood-enrollment.txt
54. In the Lisbon Regional School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB, joint SAU 35 policy). Under Policy JEBA, a child whose fifth birthday falls between October 1 and October 31 may be allowed to enter kindergarten if the superintendent finds the child ready.
   - citation: White Mountains SAU35 (Bethlehem, Lafayette, Landaff, Lisbon, and Profile) School Board Policy JEB - Age of Entrance; JEBA - Early Entrance into Kindergarten (joint policy updates October 2025), linked from https://www.sau35.org/policies-8e6962b2
   - source: https://docs.google.com/document/d/17PoXZWcc9K3zCpAnOorTuz-x-w74EXyRoaME69LdR2Q/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lisbon Regional
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. | A child whose fifth birthday falls between October 1 and October 31st, may be allowed to enter kindergarten if skills and maturity level strongly indicate readiness for kindergarten as determined by the Superintendent or his/her designee." The joint policy names Lisbon. Lisbon's own older policy folder (linked from lisbon.k12.nh.us) has JEB adopted 10/10/01 with the same September 30 rule. JEBA: https://docs.google.com/document/d/1tsw9flfKRFXmGyvJucb-BdWE3wciblIi0bZpnue4-vs Raw copy: raw/districts/batch-4/sau35-policy-jeb.txt; raw/districts/batch-4/sau35-policy-jeba.txt; raw/districts/batch-4/lisbon-policy-jeb.txt
55. In the Littleton School District, a child may enter kindergarten if he or she will be five on or before October 1 of the year of entering school, and grade one if six on or before October 1 (Policy JEB, reviewed and adopted May 4, 2026). A birth certificate is required at registration.
   - citation: Littleton School Board Policy JEB - Age of Entrance (Section J policy folder linked from https://www.sau84.org/apps/pages/index.jsp?uREC_ID=2790416&type=d&pREC_ID=2309251)
   - source: https://drive.google.com/file/d/1R2RoeuD9Awv-b5z2lbpeSuH3IydxkMQ4/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Littleton
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five on or before October 1st of the year of entering school." Cutoff is October 1, not September 30. Raw copy: raw/districts/batch-5/littleton-jeb.docx; raw/districts/batch-5/littleton-jeb.txt
56. In the Londonderry School District, a child entering kindergarten must turn five by September 30, according to the district's preschool (LEEP) family handbook, which cites district policy.
   - citation: L.E.E.P. Family Handbook (updated 01/16/2025), linked from https://moose.londonderry.org/leep/family-handbook
   - source: https://drive.google.com/file/d/1_HgizU0ZTvUJlGPFNY39m3heI6YLiiMS/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Londonderry
   - note: Page text: "Prekindergarten students must turn four by September 30th to align with the district policy which states a child entering kindergarten must turn five by September 30th." The district's online policy folder (Google Drive, J section) has no JEB policy; JFAA Admission of Resident Students (adopted 2025-01-28) does not state an age. Raw copy: raw/districts/batch-4/londonderry-leep-handbook.txt
57. In the Lyme School District, children who reach age 5 on or before September 30 are eligible to attend kindergarten that year.
   - citation: Lyme School - Registration
   - source: https://www.lymeschool.org/page/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lyme
   - note: Page text: "Children who reach the age of 5 on or before September 30 are eligible to attend kindergarten that year." Raw copy: raw/districts/batch-7/lyme-registration.txt
58. In the Manchester School District, a child must be 5 years old by September 30 to register for kindergarten that year.
   - citation: Manchester School District - New Student Registration
   - source: https://www.mansd.org/o/msd/page/register-a-student
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Manchester
   - note: Page text: "Students must be 5 years old by September 30 in order to register to start kindergarten that year." Same sentence in the 2026-03-21 news release https://www.mansd.org/article/2775173. Policy JEB not located on the site. Raw copy: raw/districts/batch-1/manchester-register-a-student.txt
59. In the Marlow School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school, and pre-kindergarten if four before September 30 (Policy JEB).
   - citation: Marlow School District Policy JEB - Age of Entrance (approved 1/7/19)
   - source: https://drive.google.com/file/d/1CHD9M6v8uPLd6Ee30OByFyCKbsN55Vpb/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlow
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. A student may enter Pre-k if his/her chronological age will be four before September 30" Raw copy: raw/districts/batch-4/marlow-policy-jeb.txt
60. In the Mascenic Regional School District, a child is eligible to enter kindergarten if they will be five on or before September 30 of the year of entry (Policy JEBA). Parents of a child who turns five between October 1 and December 31 may seek a waiver by notifying the Superintendent in writing by March 1 before the school year.
   - citation: Mascenic Regional School District Policy JEBA - Kindergarten Early Entrance Policy
   - source: https://drive.google.com/file/d/1DMAJK7gqQistiljtD9vLKt207rhb4GK7/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mascenic Regional
   - note: Page text: "A pupil shall be eligible to enter grade K if the chronological age will be five on or before September 30 of the year of entering school. ... The child must turn five years old (between October 1 and December 31 of the" In the district's Policies Google Drive folder (J - Students), linked from https://www.mascenic.org. Raw copy: raw/districts/batch-2/mascenic-jeba.txt
61. In the Mascoma Valley Regional School District, children entering kindergarten must be five years old on or before September 30.
   - citation: Mascoma Valley Regional School District - Enrollment
   - source: https://www.mascomaschools.org/our-district/enrollment
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mascoma Valley Regional
   - note: Page text: "Students entering kindergarten must be 5 years of age on or before September 30th." Policy JEB - Age of Entrance is listed on https://www.mascomaschools.org/school-board/policies but its Google Drive link returned 404. Raw copy: raw/districts/batch-2/mascoma-enrollment.txt
62. In the Mason School District, children entering kindergarten must turn 5 by September 30 of the current year (Mason Elementary School kindergarten FAQ, 2025-26).
   - citation: Mason Elementary School, Kindergarten FAQ 2025-26
   - source: https://media.edlio.net/ae14b3c3/9a812a73/954805c2/f56c579e71444723ae1ec9e56653e1b7?_=Kindergarten-FAQ-25-26-sy.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mason
   - note: Page text: "What is the age requirement for kindergarten? Children entering kindergarten must turn 5 by September 30th of the current year." Raw copy: raw/districts/batch-3/mason-k-faq-25-26.txt
63. In the Merrimack School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB). Under Policy JFAAA, a child whose fifth birthday falls between October 1 and October 31 may be eligible for kindergarten through the district's early admission procedures, decided by the Superintendent or designee.
   - citation: Merrimack School Board Policy JEB - Age of Entrance
   - source: https://drive.google.com/file/d/1YiIZ03mSOVvb6LB4IxKy0_MqSB0Vy3xE/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Wording varies: the registration page says 'a child must be five years old by September 30'; Policy JFAAA (https://drive.google.com/file/d/19OttUz-cDIT41NU15q2Lq-WEn43Kfimp/view, raw merrimack-policy-early-admission.txt) says 'Any child whose fifth birthday falls on or between October 1st and October 31st may be eligible for kindergarten entrance.' Policies linked from https://www.sau26.org/school-board/district-policies. Raw copy: raw/districts/batch-1/merrimack-policy-jeb.txt
64. In the Merrimack Valley School District, children may enter kindergarten if they turn five on or before September 30 of the current school year (Policy JEB). A child whose fifth birthday falls within 14 days after September 30 may ask for an early entrance exception: parents send a written request to the Superintendent between January 1 and April 30 before the school year, and the School Board makes the final decision.
   - citation: Merrimack Valley School Board Policy JEB - Entrance Requirements (approved 3/9/26)
   - source: https://drive.google.com/file/d/1xxyafXw9QMez1uqs99-zCRzs9t0fuTTv/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack Valley
   - note: Page text: "All children may enter kindergarten provided they become five (5) on or before September 30, of the current school year. Early Entrance Exception: The District recognizes that in rare circumstances a child whose fifth birthday falls within fourteen (14) days after the September 30 entrance cutoff date may demonstrate readiness for early admission." Linked from the School Board Policies folder (Section J) on https://www.mvsdpride.org/. Raw copy: raw/districts/batch-1/mvsd-policy-jeb.txt
65. In the Middleton School District, children who will be five by September 30 are invited to register for kindergarten, according to Middleton Elementary School's 2026-27 registration flyer.
   - citation: Middleton Elementary School - Kindergarten Registration post (Feb 17, 2026), flyer image
   - source: https://www.middletonelementary.org/default-board-post-page/~board/test-board/post/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Middleton
   - note: Page text: "If you have a child that will be 5 by September 30th, call today to make an appointment for our upcoming registration day!" Text read from the flyer image. Policy JEB on the SAU 69 policy manual page not checked. Raw copy: raw/districts/batch-5/middleton-k-registration-flyer-2026-27.jpg
66. In the Milford School District, Policy 5065 (JEBA) says a child whose fifth birthday falls after September 30 and before October 31 may be eligible for early kindergarten entrance, based on a school readiness assessment. Parents send a written request to the school principal by May 1 of the preceding school year; the Superintendent's decision is final.
   - citation: Milford School District Policy 5065 (JEBA) Early Admission to Kindergarten or Grade One
   - source: https://www.milfordk12.org/ourpages/auto/2024/8/9/74255036059500421123/5065%20(JEBA)%20Early%20Admission%20to%20Kindergarten%20or%20Grade%20One.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milford
   - note: Page text: "Similarly, a child whose fifth birthday falls after September 30 and prior to October 31 may be eligible for kindergarten entrance." Section J policy list (https://www.milfordk12.org/apps/pages/section-j) has no separate JEB entrance-age policy; JEBA implies a September 30 cutoff but does not state the regular kindergarten cutoff in words. Raw copy: raw/districts/batch-6/milford-jeba.txt
67. In the Monadnock Regional School District, a child may enter kindergarten if they will be five before September 30 of the year of entry, and grade one if they will be six before September 30 (Policy JEB, last reviewed January 9, 2022). A birth certificate is required at registration.
   - citation: MRSD School Board Policies (BoardDocs), Book J, Policy JEB - Entrance Age Requirements
   - source: https://go.boarddocs.com/nh/mrsd/Board.nsf/Public
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Monadnock Regional
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." BoardDocs page opened in headless Chrome: Policies tab > Book J: Students > JEB. Raw copy: raw/districts/batch-2/mrsd-jeb.txt
68. In the Monroe School District, a student may enter kindergarten if he or she will be five before September 30 of the year of entering school, and may enter preschool if he or she will be four before September 30 (Age of Entrance policy).
   - citation: Monroe School District School Board Policy JEB - Age of Entrance
   - source: https://docs.google.com/document/d/1e6tysu5sGJCjMJ6tAlxvNEsR8dwrocIO/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Monroe
   - note: Page text: "A student may enter kindergarten if their chronological age will be five before September 30 of the year of entering school. A student may enter preschool if their chronological age will be four before September 30 of the year of entering school." Registration page for 2026-27: 'Kindergartners must be 5 years old by Sept 30, 2026'. Policies page: https://sites.google.com/a/monroeschool77.com/monroe-consolidated-school/schoolboard/policies Raw copy: raw/districts/batch-1/monroe-policy-jeb.txt
69. In the Moultonborough School District, a child may enter kindergarten if they will be five on or before September 30 of the year they start school (Policy JEB, Age of Entrance). Early entrance to kindergarten is not permitted; exceptions for early entrance to first grade are considered only in extraordinary circumstances.
   - citation: Moultonborough School District Policy JEB, Age of Entrance (linked from the Section J policy index, https://docs.google.com/document/d/1TaXY018MAMiL87LNDFjB9o5ft_ISVfupzJe4hCK4HVg/edit)
   - source: https://drive.google.com/file/d/1winzfeHpKyZviCmRG-VDX_5frPoaq67j/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Moultonborough
   - note: Page text: "Kindergarten : A child may enter Kindergarten if his/her chronological age will be five (5) on or before September 30 of the year entering school." 'Under no circumstances will early entrance into Kindergarten or Readiness be permitted.' Raw copy: raw/districts/batch-8/moultonborough-jeb.txt
70. In the Nashua School District, children must be five years old as of September 30 to enter kindergarten, and six before September 30 to enter first grade. Parents may request early admission, with no exceptions for birthdates after October 31; the request packet must be obtained from Student Services before June 1.
   - citation: Nashua School District - Frequently Asked Questions
   - source: https://www.nashua.edu/Page/717
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nashua
   - note: Page text: "Children must be five years old as of September 30 to enter kindergarten, and six years old prior to September 30 in order to enter first grade. ... There will be no exceptions for children with birthdates beyond October 31." The JEB policy PDF link found by search (nashua.edu/cms/lib/.../JEB_Age_of_Entrance.pdf) now returns 404 after the site moved to Finalsite; the FAQ states the same cutoff. Raw copy: raw/districts/batch-2/nashua-faq.txt
71. In the Nelson School District, a child is eligible for kindergarten if they have reached age 5 by September 30, with no exceptions for early entrance (Policy JEB, readopted March 6, 2026).
   - citation: Nelson School District Policy JEB - Age of Entrance (adopted NSB 3/6/26)
   - source: https://docs.google.com/document/d/15WvAJgtr-hs0s9ncKH9GuSKfNosJaawiuXKiTQKM_eQ/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nelson
   - note: Page text: "Students shall be eligible to attend kindergarten if they have reached age 5 by September 30, with no exceptions made for early entrance." Raw copy: raw/districts/batch-4/nelson-policy-jeb.txt
72. In the New Boston School District, a child must be five years old by September 30, 2026 to be eligible for kindergarten in 2026-27 (and six by September 30, 2026 for first grade or the Readiness class).
   - citation: SAU 19 - New Boston Central School Kindergarten 2026-27
   - source: https://www.sau19.org/index.php/en/information-6/familes/new-student-registration-nbcs
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Boston
   - note: Page text: "Your child must be 5 years old by September 30th 2026 to be eligible for Kindergarten." Raw copy: raw/districts/batch-7/newboston-kindergarten-2026-27.txt
73. In the New Castle School District, a child is eligible to enter kindergarten if they will be five on or before September 30 of the year they plan to start school (SAU 50 Policy JEB, School Age Requirements, which applies to the Rye, Greenland, New Castle (Maude H. Trefethen) and Newington schools).
   - citation: SAU 50 School Boards - Board Policies, JEB School Age Requirements
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Castle
   - note: Page text: "A student will be eligible to enter kindergarten if his/her chronological age will be five on or before September 30 of the year the student plans to enter school." Page: 'These policies are for the Rye, Greenland, Maude H. Trefethen and Newington Schools.' Maude H. Trefethen is New Castle's school. Raw copy: raw/districts/batch-8/sau50-policies.txt
74. In the Newfields School District, a child may enter kindergarten if they will be five on or before September 30 of the year they start school, and grade 1 if they will be six on or before September 30 (Policy JEB, Age of Entrance).
   - citation: Newfields School Board Policy JEB, Age of Entrance (linked from the district's SAU 16 policy page https://www.sau16.org/pages/668c14eb-ace8-4c6c-853f-37a25d8335ec)
   - source: https://drive.google.com/file/d/1tEfyWjITc8ENWB_F4oGgd6PBhVY3XVgU/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newfields
   - note: Page text: "A student may enter kindergarten if his or her chronological age will be five on, or before, September 30 th of the year of entering school." Each SAU 16 district has its own JEB; text checked separately for each. Raw copy: raw/districts/batch-8/newfields-jeb.txt
75. In the Newfound Area School District, a child who is five years old on or before September 30 is eligible for kindergarten, and no waiver of the kindergarten entrance age is granted (Policy JEB).
   - citation: Newfound Area School Board Policy JEB - Age of Entrance (second reading May 11, 2015), linked from the Prospective Families page
   - source: https://drive.google.com/file/d/0BzW6bJQsGjmFd2pjYUFPQi03cEU/view?resourcekey=0-0neVbMUQYr75Y1-QC07vLA
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newfound Area
   - note: Page text: "Any child reaching the age of five years old on or before September 30 will be eligible to attend kindergarten. Kindergarten attendance is optional, but encouraged. No waiver of this Kindergarten entrance age provision shall be granted." Raw copy: raw/districts/batch-4/newfound-policy-jeb.txt
76. In the Newington School District, a child is eligible to enter kindergarten if they will be five on or before September 30 of the year they plan to start school (SAU 50 Policy JEB, School Age Requirements, which applies to the Rye, Greenland, New Castle (Maude H. Trefethen) and Newington schools).
   - citation: SAU 50 School Boards - Board Policies, JEB School Age Requirements
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newington
   - note: Page text: "A student will be eligible to enter kindergarten if his/her chronological age will be five on or before September 30 of the year the student plans to enter school." Page: 'These policies are for the Rye, Greenland, Maude H. Trefethen and Newington Schools.' Maude H. Trefethen is New Castle's school. Raw copy: raw/districts/batch-8/sau50-policies.txt
77. In the Newmarket School District, a child must be five years old by September 30, 2026 to enter kindergarten in 2026-27 (birthdates October 1, 2020 to September 30, 2021).
   - citation: Newmarket School District - Registration
   - source: https://www.newmarket.k12.nh.us/sau31/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newmarket
   - note: Page text: "To enter kindergarten for the school year 2026-2027, your child must be five years old by Sept. 30, 2026." Policy manual page (https://www.newmarket.k12.nh.us/school-board/policies) not searched for JEB; registration page is explicit. Raw copy: raw/districts/batch-8/newmarket-registration.txt
78. In the Newport School District, children starting kindergarten must be 5 years old before September 30 (School Board Policy JEB).
   - citation: Newport School District - Student Enrollment (New & Returning)
   - source: https://www.sau43.nh.gov/o/sau43/page/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newport
   - note: Page text: "Students starting kindergarten must must be 5 years old before September 30. (School Board Policy JEB Age of Entrance)" The April 2, 2026 pre-registration post says 'must be 5 years old by September 30, 2026'. Raw copy: raw/districts/batch-4/newport-pages.txt
79. In the Northwood School District, children who turn five on or before September 30 are eligible for kindergarten that school year (Policy JEB, revised March 4, 2026). Under Policy JEBA, a child whose fifth birthday falls between October 1 and November 15 may be allowed to enter early if an assessment shows strong readiness, as decided by the superintendent or designee.
   - citation: Northwood School Board Policy JEB, Entrance into the School System (3/4/26); Policy JEBA, Early Entrance into Kindergarten (https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5969/Sau/98c652a6-9210-463f-b948-912a8e30d463/JEBA-Early-Entrance-into-Kindergarten.pdf?disposition=inline)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5969/Sau/fecfd06d-358b-4657-bc73-e13b819c6802/JEB---Entrance-Into-The-School-System-3-4-26.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Northwood
   - note: Page text: "Children reaching the age of five on or before September 30 will be eligible for admission into Kindergarten at the beginning of that school year." JEBA restates JEB as 'five prior to September 30'; JEB itself says 'on or before'. JEBA: 'A child, whose fifth birthday falls between October 1 and November 15, may be allowed to enter kindergarten if skills and maturity level strongly indicate readiness'. Raw copy: raw/districts/batch-8/northwood-jeb.txt; raw/districts/batch-8/northwood-jeba.txt
80. In the Nottingham School District, children who will be five years old by September 30, 2026 may register for kindergarten for 2026-27.
   - citation: Nottingham School - Kindergarten Registration
   - source: https://www.nottingham.k12.nh.us/about/kinderreg
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nottingham
   - note: Page text: "If you have a child who will be 5 years old by September 30, 2026 and will be entering Kindergarten for the 2026-2027 school year" Policy list at https://www.nottingham.k12.nh.us/school-board/policies not searched for JEB (links are individual Drive files). Raw copy: raw/districts/batch-2/nottingham-kreg.txt
81. In the Oyster River Cooperative School District, a child may enter kindergarten if they will be five before October 1 of the year of entry, and grade one if they will be six before October 1 (Policy JEB, readopted March 31, 2026). A birth certificate is required at registration.
   - citation: ORCSD Policy JEB - Age of Entrance (School Board adoption March 31, 2026)
   - source: https://www.orcsd.org/school-board/files/documents/Policies/J%20-%20Policies/JEB%20-%20Age%20of%20Entrance%20SB%2003%2031%2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Oyster River Coop
   - note: Page text: "A pupil may enter kindergarten if their chronological age will be five (5) before October 1 of the year of entering school." Linked from https://www.orcsd.org/school-board/policies. Raw copy: raw/districts/batch-2/orcsd-jeb.txt
82. In the Pasquaney School District, children who turn 5 by September 30 are eligible for kindergarten at Bridgewater-Hebron Village School.
   - citation: Bridgewater-Hebron Village School - Kindergarten registration flyer
   - source: https://aptg.co/x87s_j
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pasquaney
   - note: Page text: "CHILDREN WHO TURN 5 BY SEPTEMBER 30 ARE ELIGIBLE!" Policy JEB not checked (policies at https://www.bhvsnh.org/documents/school-board-policies/858821). Raw copy: raw/districts/batch-8/pasquaney-k-registration.txt
83. In the Pelham School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB). Children with October or November birthdays may be considered for early admission after an evaluation; a written request to the principal by April 1 allows the evaluation to be done before the school year, and children whose fifth birthday is after November 30 are not eligible to be considered.
   - citation: Pelham School District Policy JEB - Age of Entrance (with procedure JEB-R)
   - source: https://www.pelhamsd.org/Downloads/JEB%20Age%20of%20Entrance2.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pelham
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." JEB-R: https://www.pelhamsd.org/Downloads/Procedure%20JEB-R%20%20Entrance%20Age%20Requirements%20Grade%20One.pdf. JEB says testing for early admission done by district personnel after school hours is paid by the parent at an hourly rate. Raw copy: raw/districts/batch-7/pelham-jeb.txt; raw/districts/batch-7/pelham-jeb-r.txt
84. In the Pembroke School District, Pembroke Hill School's registration page says a child must be five before October 1 to register for kindergarten (the page shows the date as 10/1/23, from an earlier year).
   - citation: Pembroke Hill School - Registration
   - source: https://phs.sau53.org/pages/8a33dd54-9f64-445a-907a-b6bf59285c93
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pembroke
   - note: Page text: "In order to register for Kindergarten, a student must be 5 BEFORE 10/1/23." The year on the page is out of date (10/1/23). No Policy JEB was found in the Pembroke policy folder (Section J listing checked via Google Drive). Raw copy: raw/districts/batch-7/sau53-phs-registration.txt
85. In the Piermont School District, a pupil may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB).
   - citation: SAU 23 Board Policies, Section J (Google Doc linked from https://www.sau23.org/sau-23/school-boards/board-policies)
   - source: https://docs.google.com/document/d/19lj7kHI12uVHodbLgGILRoN2TS8Mi_sr7qk6aaeHi60/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Piermont
   - note: Page text: "JEB ENTRANCE AGE (Bath and Piermont) ... A pupil may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Adopted by Piermont School Board March 17, 2009. Raw copy: raw/districts/batch-1/sau23-policies-section-j.txt
86. In the Pittsburg School District, a student may enter kindergarten if he or she will be five before September 30 of the year of entering school (SAU 7 Policy JEB). Parents may send the Board a written request, no later than April 30 of the prior school year, to enroll a child who does not meet the age rule; the child is tested for readiness and the Board decides before the school year.
   - citation: SAU #7 Policy JEB - Age of Entrance (adopted by Colebrook 10/16/2018, Pittsburg 10/22/2018, Stewartstown 10/8/2018)
   - source: https://drive.google.com/file/d/15IqA9RAd_ZjmuI5BC2bqtFXb9QcbPKH5/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pittsburg
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. ... Any parent who approaches the Board with a special written request, no later than April 30th of the prior school year, to have their son or daughter enrolled in kindergarten after the age criteria currently in place, will have that request reviewed and their child tested for readiness." Policy states its adoption by the Colebrook, Pittsburg and Stewartstown school boards. Linked from https://www.sau7.org/en-US/pages/0b1e2b2d-b90a-43b2-9ed1-a527abe867a5 Raw copy: raw/districts/batch-1/sau7-policy-jeb.txt
87. In the Pittsfield School District, a child may enter kindergarten if they will be five before September 30 of the year of entry, and grade one if they will be six before September 30 (Policy JEB). A birth certificate is required at registration.
   - citation: Pittsfield School District Policy JEB - Age of Entrance
   - source: https://www.sau51.org/sau/wp-content/uploads/2022/05/JEB.Age_.of_.Entrance-1.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pittsfield
   - note: Page text: "student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." PDF uploaded 2022-05 on sau51.org; the current Policies page (https://sau51.org/board/policies/) did not list it in its text. Policy is undated. Raw copy: raw/districts/batch-2/pittsfield-jeb.txt
88. In the Plainfield School District, children are eligible to begin kindergarten if they are five years old before September 30.
   - citation: Plainfield School District - Registration Information
   - source: https://www.plainfieldschool.org/page/registration-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Plainfield
   - note: Page text: "Children are eligible to begin Kindergarten if they are 5 years old before September 30th." Same text on https://sites.google.com/plainfieldschool.org/studentenrollment/home. Policy JEB not checked. Raw copy: raw/districts/batch-5/plainfield-registration-info.txt; raw/districts/batch-5/plainfield-enrollment.txt
89. The Portsmouth School Department's kindergarten registration page for 2017-18 said a child had to be five years old on or before September 30 to register for kindergarten. No newer statement of the cutoff, and no posted entrance-age policy (JEB), was found on the district site.
   - citation: Portsmouth School Department - Kindergarten Registration & Screening for the 2017-2018 School Year
   - source: https://www.portsmouthnh.gov/node/3106
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Portsmouth
   - note: Page text: "If your child will be 5 years old on or before September 30, 2017, they will be eligible to register for the 2017-2018 school year." Old page (2017-18), still online. The Section J policy list (https://www.cityofportsmouth.com/school-department/portsmouth-school-district-policies-section-j) has no JEB. A WebSearch summary mentioned a 2024-25 version of the page, but it was not opened, so not used. The PEEP 2026-27 flyer uses 'by September 30, 2026' for preschool age. Raw copy: raw/districts/batch-8/portsmouth-node3106.txt; raw/districts/batch-8/portsmouth-k-registration-pdf.txt
90. In the Raymond School District, a child may enter kindergarten if they will be five before September 30 of the year of entry, and grade one if they will be six before September 30 (Policy JEB). Under Policy JEBA, a child whose fifth birthday falls between October 1 and December 1 may be allowed to enter kindergarten if skills and maturity strongly indicate readiness, as determined by the Superintendent or designee.
   - citation: Raymond School District Policy JEB - Entrance Age Requirements; Policy JEBA - Early Entrance into Kindergarten (adopted October 2, 2019)
   - source: https://www.sau33.com/school-board/school-board-policies/files/jeb-entrance-age-requirements
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Raymond
   - note: Page text: "A student may enter Kindergarten if his/her chronological age will be five (5) before September 30 of the year of entering school. ... A child whose fifth birthday falls between October 1 and December 1 may be allowed to enter kindergarten if skills" JEBA: https://www.sau33.com/school-board/school-board-policies/files/jeba-early-entrance-kindergarten Raw copy: raw/districts/batch-2/raymond-jeb-entrance-age-requirements.txt; raw/districts/batch-2/raymond-jeba-early-entrance-kindergarten.txt
91. In the Rochester School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB). Parents of children who turn six after September 30 and before November 30 may ask the Superintendent for an exception to the minimum age requirement; the Superintendent's decision is final.
   - citation: Rochester School District Policy JEB - Age of Entrance (amended December 11, 2014), linked from the Online Registration page
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/2192/Rsd/0964f504-d739-4543-b255-6effd70888ac/JEB.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rochester
   - note: Page text: "Parents of children who reach their sixth birthday after September 30 and before November 30 may request an exception from the minimum age requirement to the Superintendent. A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." Linked as https://aptg.co/1YHG5X from https://www.rochesterschools.com/o/rsd/page/online-enrollment. The City of Rochester news post for 2026-27 says 'on or before September 30, 2026'. The exception wording mentions the sixth birthday. Raw copy: raw/districts/batch-6/rochester-jeb.txt
92. In the Rollinsford School District, a child must have reached his or her fifth birthday by September 30, 2026, to be eligible for kindergarten in 2026-27, according to Rollinsford Grade School's registration notice.
   - citation: Town of Rollinsford, 'Kindergarten Registration' (May 28, 2026; notice from Rollinsford Grade School)
   - source: https://rollinsford.nh.us/kindergarten-registration/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rollinsford
   - note: Page text: "To be eligible for kindergarten, students must have reached their 5th birthday by September 30, 2026." Posted on the town website, quoting the school's notice. School policy JEB not checked. Raw copy: raw/districts/batch-3/rollinsford-k-reg.txt
93. In the Rumney School District, children whose fifth birthday is on or before September 30 are eligible to enroll in kindergarten at Russell Elementary School.
   - citation: Russell Elementary School Student Handbook 2026-2027 (approved by the school board August 19, 2026)
   - source: https://docs.google.com/document/d/1gwnEibXTHeC55d-xZTgQkJS_R9htX4W0yW9AKFwUnxo/edit?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rumney
   - note: Page text: "Kindergarten Registration: Students whose 5th birthday occurs on or before September 30th will be eligible for enrollment into kindergarten." Raw copy: raw/districts/batch-6/rumney-handbook-2627.txt
94. In the Rye School District, a child is eligible to enter kindergarten if they will be five on or before September 30 of the year they plan to start school (SAU 50 Policy JEB, School Age Requirements, which applies to the Rye, Greenland, New Castle (Maude H. Trefethen) and Newington schools).
   - citation: SAU 50 School Boards - Board Policies, JEB School Age Requirements
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rye
   - note: Page text: "A student will be eligible to enter kindergarten if his/her chronological age will be five on or before September 30 of the year the student plans to enter school." Page: 'These policies are for the Rye, Greenland, Maude H. Trefethen and Newington Schools.' Maude H. Trefethen is New Castle's school. Raw copy: raw/districts/batch-8/sau50-policies.txt
95. In the Salem School District, children who will be five years old before October 1 of the school year are eligible to attend kindergarten.
   - citation: Salem School District - Registration FAQs
   - source: https://sau57.org/enroll-faqs
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Salem
   - note: Page text: "What is the age requirement for Kindergarten? Children who will be five years of age before October 1 of the school year are eligible to attend." Policy JEB (Entrance Age, https://files.smartsites.parentsquare.com/10879/jeb_entrance_age.pdf, raw salem-jeb.txt) says only that initial entrance is on the basis of chronological age; it gives no date. Same FAQ: tuition-free kindergarten at all five elementary schools; children in the 4-year-old Salem Preschool program are automatically entered into kindergarten. Raw copy: raw/districts/batch-7/salem-enroll-faqs.txt
96. In the Sanborn Regional School District, a child must turn five by September 30 to enter kindergarten: for 2026-27 the child's birthday must be between October 1, 2020 and September 30, 2021, and for 2027-28 between October 1, 2021 and September 30, 2022. Kindergarten is tuition-free for residents of Kingston and Newton.
   - citation: Daniel J. Bakie School - Registration Information (Google Doc linked from https://bakie.sau17.net/o/djbe)
   - source: https://docs.google.com/document/d/1kTAEsgxD1GN7QQpko-mSth1Ni1-3FgAt9NjXqVPL4qE/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Sanborn Regional
   - note: Page text: "The age requirement to be eligible for 2026-2027 kindergarten is that your child’s birthday must be between 10/1/2020 and 9/30/2021. To be eligible for 2027-2028 kindergarten, your child’s birthday must be between 10/1/2021 and 9/30/2022." Policy JEB not checked separately. Raw copy: raw/districts/batch-5/sanborn-bakie-registration-doc.txt
97. In the Seabrook School District, a child may enter kindergarten if he or she will be five on or before September 30 of the year of entering school (Policy JEB, as printed in the Seabrook Elementary handbook).
   - citation: Seabrook Elementary School Student Handbook 2026-2027 (Entrance Level Requirements Policy JEB)
   - source: https://www.sau21.nh.gov/ses/files/documents/SESHandbook_2026-2027.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Seabrook
   - note: Page text: "A student may enter Kindergarten if his/her chronological age will be five on or before September 30 of the year of entering school." Raw copy: raw/districts/batch-7/seabrook-ses-handbook-2026-27.txt
98. In the Shaker Regional School District, children registering for kindergarten for 2026-27 must be five years old as of September 30, 2026 (six as of September 30, 2026 for first grade).
   - citation: Shaker Regional School District - Kindergarten and Grade One Registration
   - source: https://www.sau80.org/community/kindergarten_and_grade_one_registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Shaker Regional
   - note: Page text: "Students registering for Kindergarten must be five years old as of September 30, 2026. Students registering for first grade must be six years old as of September 30, 2026." Policy JEB not checked. Raw copy: raw/districts/batch-6/shaker-k-registration.txt
99. In the Somersworth School District, a child may enter kindergarten if he or she will be five on or before September 30 of the year of entering school, and grade one if six on or before September 30 (Policy JEB). A birth certificate, proof of residency and health records are required at registration.
   - citation: Somersworth School District Policy JEB - Entrance Age Requirements
   - source: https://sau56.ss20.sharpschool.com/UserFiles/Servers/Server_82252/File/District/School%20Board/School%20Policies/Section%20J/JEB%20Entrance%20Age%20Requirements.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Somersworth
   - note: Page text: "A student may enter kindergarten if the chronological age will be five on or before September 30 of the year of entering school." Linked from Section J policies page https://www.sau56.org/cms/One.aspx?portalId=82336&pageId=123447. JEB cross-references policy JEBA 'Early Entrance into Kindergarten' (not opened). Raw copy: raw/districts/batch-6/somersworth-jeb.txt
100. In the South Hampton School District, a pupil may enter kindergarten at Barnard School if he or she will be five on or before September 30 of the year of entering school.
   - citation: Barnard School Family Handbook 2025-2026
   - source: https://www.sau21.nh.gov/barnard/files/documents/Barnard%20Family%20Handbook%202025-2026%20(Approved).pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district South Hampton
   - note: Page text: "A pupil may enter kindergarten if his/her chronological age will be five on or before September 30 of the year of entering school." Raw copy: raw/districts/batch-7/southhampton-barnard-handbook-2025-26.txt
101. In the Stewartstown School District, a student may enter kindergarten if he or she will be five before September 30 of the year of entering school (SAU 7 Policy JEB). Parents may send the Board a written request, no later than April 30 of the prior school year, to enroll a child who does not meet the age rule; the child is tested for readiness and the Board decides before the school year.
   - citation: SAU #7 Policy JEB - Age of Entrance (adopted by Colebrook 10/16/2018, Pittsburg 10/22/2018, Stewartstown 10/8/2018)
   - source: https://drive.google.com/file/d/15IqA9RAd_ZjmuI5BC2bqtFXb9QcbPKH5/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stewartstown
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. ... Any parent who approaches the Board with a special written request, no later than April 30th of the prior school year, to have their son or daughter enrolled in kindergarten after the age criteria currently in place, will have that request reviewed and their child tested for readiness." Policy states its adoption by the Colebrook, Pittsburg and Stewartstown school boards. Linked from https://www.sau7.org/en-US/pages/0b1e2b2d-b90a-43b2-9ed1-a527abe867a5 Raw copy: raw/districts/batch-1/sau7-policy-jeb.txt
102. In the Stoddard School District, James Faulkner Elementary School's registration page says children can start kindergarten if they reach age five by September 30 of the school year.
   - citation: James Faulkner Elementary School, Student Registration
   - source: https://www.sau24.org/schools/jfes-us/about-us/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stoddard
   - note: Page text: "Students can start kindergarten if they reach the age of five by September 30th of the school year." Raw copy: raw/districts/batch-3/stoddard-registration.txt
103. In the Strafford School District, families of children turning five on or before September 30 of the current year are asked to contact the Strafford School office to register for kindergarten.
   - citation: Strafford School - Incoming Kindergarten
   - source: https://www.strafford.k12.nh.us/families/incoming-kindergarten
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Strafford
   - note: Page text: "If your child is turning 5 on or before September 30 of this year, don't hesitate to get in touch with our office to begin the registration process." District policies are on a Google Apps Script page (not fetched). Raw copy: raw/districts/batch-2/strafford-incoming-k.txt
104. In the Stratham School District, a child may enter kindergarten if they will be five on or before September 30 of the year they start school (Policy JEB, Age of Entrance). A child whose fifth birthday falls between October 1 and October 31 may be allowed to enter if an assessment by the superintendent or designee shows strong readiness.
   - citation: Stratham School Board Policy JEB, Age of Entrance (linked from the district's SAU 16 policy page https://www.sau16.org/pages/b4ee4c1b-bf69-4704-9b79-026e5affb6fb)
   - source: https://drive.google.com/file/d/1rNYLRWxhOLkotWWT2qrvyRShzWY2ReW-/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stratham
   - note: Page text: "A student may enter kindergarten if their chronological age will be ﬁve on, or before, September 30th of the year of entering school." Each SAU 16 district has its own JEB; text checked separately for each. Raw copy: raw/districts/batch-8/stratham-jeb.txt
105. In the Timberlane Regional School District, children entering kindergarten in 2026-27 must have been born between October 1, 2020 and September 30, 2021, that is, five years old by September 30. Grade 1 students are six by September 30, 2026.
   - citation: Timberlane Regional School District - New Student Enrollment Process
   - source: https://www.timberlane.net/enrollment/student-enrollment/student-enrollment-process
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Timberlane Regional
   - note: Page text: "To be eligible for kindergarten, students must have been born between October 1, 2020 -September 30, 2021. ... Grade 1 students are 6 years of age by September 30, 2026." The page's next sentence says 'Kindergarten students are 5 years of age by September 30, 2025', which appears to be a typo for 2026 given the birth-date range. Policy JEB not found on the site (policy committee page lists only one policy PDF). Raw copy: raw/districts/batch-2/timberlane-enrollment-process.txt
106. In the Wakefield School District, a child may enter kindergarten if they will be five before September 30 of the year of entry, or grade one if they will be six before September 30 (Policy JEB, reaffirmed June 1, 2011).
   - citation: Wakefield School Board Policy JEB - School Age Entrance
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5761/Sau101/99fa4d16-a95d-476c-a7fd-ad8106e1fc8f/JEB-School-Age-Entrance.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wakefield
   - note: Page text: "A pupil may enter Kindergarten if his/her chronological age will be five before September 30 of the year of entering school or grade one if he/she will be six before September 30 of the year of entering Grade 1." Linked from https://www.sau101.org/o/sau101/page/new-students-to-paul-school. Raw copy: raw/districts/batch-2/wakefield-jeb.txt
107. In the Warren School District, a pupil may enter kindergarten if he or she will be five before October 15 of the year of entering school (Policy JEB, Warren version).
   - citation: SAU 23 Board Policies, Section J (Google Doc linked from https://www.sau23.org/sau-23/school-boards/board-policies)
   - source: https://docs.google.com/document/d/19lj7kHI12uVHodbLgGILRoN2TS8Mi_sr7qk6aaeHi60/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Warren
   - note: Page text: "JEB ENTRANCE AGE (Warren) ... A pupil may enter kindergarten if his/her chronological age will be five before October 15 of the year of entering school." Adopted by Warren School Board May 12, 2009. Raw copy: raw/districts/batch-1/sau23-policies-section-j.txt
108. In the Washington School District, any Washington resident child who will be five years old by September 30, 2026 is eligible to enroll in kindergarten at Washington Elementary School for 2026-27.
   - citation: SAU #34 News, 'Washington Elementary School Kindergarten and Early Learning Group Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Washington
   - note: Page text: "Any Washington resident with a child who will be five years old by September 30, 2026 will be eligible to enroll in the Kindergarten program." Raw copy: raw/districts/batch-6/sau34-home.txt
109. In the Waterville Valley School District, children who are five years old as of September 30 are entitled to attend kindergarten; children who turn five after September 30 may attend the following year. Children must be six by September 30 for grade one.
   - citation: Waterville Valley Elementary School Parent/Student Handbook 2026-2027 (revised August 20, 2026)
   - source: https://drive.google.com/file/d/17WryCmCTHMLkS36mjvakfa0yb1AW6TN1/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Waterville Valley
   - note: Page text: "Students who are ﬁve years old as of September 30 th each year are entitled and encouraged to attend kindergarten. ● Students who reach their ﬁfth birthday after September 30 th are entitled to attend kindergarten the following year." Quote taken from line-joined text (raw waterville-handbook-2627-joined.txt); PDF uses ligature 'ﬁ'. Raw copy: raw/districts/batch-6/waterville-handbook-2627.txt
110. In the Weare School District, Center Woods Elementary School's registration page says children can start kindergarten if they reach age five by September 30 of the school year.
   - citation: Center Woods Elementary School, Student Registration
   - source: https://www.sau24.org/schools/centerwoods/about-us/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Weare
   - note: Page text: "Students can start kindergarten if they reach the age of five by September 30th of the school year." Weare policy manual is on Simbli (hCaptcha); JEB not read. Raw copy: raw/districts/batch-3/sau24-centerwoods-reg.txt
111. In the Wentworth School District, a child who turns five after September 30 cannot attend kindergarten until the following school year.
   - citation: Wentworth Elementary School Parent/Student Handbook 2026-2027
   - source: https://drive.google.com/file/d/17sKnhg4LZQ_bojPYfCtUOpDZHxOxukYf/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wentworth
   - note: Page text: "Kindergarten Registration: A child who reaches his or her fifth birthday after September 30th cannot attend school until the following school year" Raw copy: raw/districts/batch-6/wentworth-handbook-2627.txt
112. In the Westmoreland School District, kindergarten pupils must reach age five on or before September 30; parents may request a variance (waiver) in writing to the principal by May 30 before the school year, and the principal decides after readiness testing (Policy JEB procedure).
   - citation: Westmoreland School District Policy JEB - Age of Entrance, with administrative procedure (approved WSB 6/25/14)
   - source: https://drive.google.com/file/d/1HfgdPMMHH2AZL7xQGkOLo56I9aTFEtFr/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Westmoreland
   - note: Page text: "Entering kindergarten pupils must have evidence of reaching the age of five years on or before September 30 following the opening of school in September. ... Requests for variance to the above criteria must be in writing and submitted to the principal no later than May 30" 2026-27 handbook: 'Children who turn age five prior to September 30 of the current school year are eligible to enroll... Parents may request a waiver of the cut-off date by May 30'. Raw copy: raw/districts/batch-4/westmoreland-policy-jeb.txt
113. In the White Mountains Regional School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB). Under Policy JEBA, adopted January 22, 2026, a child whose fifth birthday falls between October 1 and November 1 may be allowed to enter kindergarten if the superintendent or designee finds strong readiness; the superintendent's decision is final.
   - citation: WMRSD Policies, Section J: JEB - Age of Entrance (06-18-2007) and JEBA - Early Entrance into Kindergarten (adopted 01-22-2026)
   - source: https://www.sau36.org/documents/district/for-staff/policies/j_-students/20741357
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district White Mountains Regional
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school. ... A child whose fifth birthday falls between October 1 and November 1 may be allowed to enter kindergarten if skills and maturity level strongly indicate readiness for kindergarten as determined by the Superintendent or his/her designee." Raw copy: raw/districts/batch-3/wmrsd-jeb.txt; raw/districts/batch-3/wmrsd-jeba.txt; raw/districts/batch-3/wmrsd-policies-j.txt
114. In the Wilton-Lyndeborough Cooperative School District, a child may enter kindergarten if he or she will be five before September 30 of the year of entering school (Policy JEB).
   - citation: Wilton-Lyndeborough Cooperative Policy JEB - Age of Entrance (adopted October 12, 2010), linked from https://www.sau63.org/school-board/policies
   - source: https://www.sau63.org/fs/resource-manager/view/6d028e9f-38f4-49e7-b3dd-156e40c2b275
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wilton-Lyndeborough Cooperative
   - note: Page text: "A student may enter kindergarten if his/her chronological age will be five before September 30 of the year of entering school." 2026-27 LCS registration flyer: 'YOUR CHILD MUST BE 5 YEARS OLD BY SEPTEMBER 30TH, 2026.' Raw copy: raw/districts/batch-4/wlc-policy-jeb.txt
115. In the Windham School District, a child may enter kindergarten if their age is five before September 30 of the school year of entry, and grade one if six before September 30 (Policy JEB). A birth certificate must be shown at registration.
   - citation: Windham School Board Policy JEB - Entrance Age Requirements (reviewed September 15, 2026)
   - source: https://www.windhamsd.org/common/pages/GetFile.ashx?key=Ilm4AWWn
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windham
   - note: Page text: "A student may enter kindergarten if their chronological age is five before September 30 of the school year of entry." Linked from https://www.windhamsd.org/our_district/school_board/policies_and_procedures (Section J). The 2026-27 preschool page also says: 'If your child will be age 5 by Sept. 30, he/she will enter Kindergarten.' Raw copy: raw/districts/batch-6/windham-jeb.txt
116. Windsor operates no schools; Windsor kindergartners attend Hillsboro-Deering Elementary School, where children registering for 2026-27 kindergarten had to live in Hillsboro, Deering or Windsor and be 5 years old on or before September 30, 2026.
   - citation: SAU #34 News, '2026-2027 Hillsboro-Deering Elementary School Kindergarten Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windsor
   - note: Page text: "Children must reside in Hillsboro, Deering or Windsor and be 5 yrs. old on or before 9/30/2026." The page names Windsor residents explicitly. Raw copy: raw/districts/batch-6/sau34-home.txt
117. In the Winnisquam Regional School District, a child may enter kindergarten if he or she will be five on or before September 30 of the year of entering school, and grade one if six on or before September 30; Policy JEB covers early entrance requests.
   - citation: Winnisquam Regional School District Elementary Student & Parent Handbook 2025-2026 (linked from the Parent/Student Resources page)
   - source: https://docs.google.com/document/d/19fQ2Lpe8AaX4M4mN3pWN7rhZwbb-XHUcMd5iTbFOKeA/edit?usp=drive_link
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Winnisquam Regional
   - note: Page text: "A pupil may enter kindergarten if his/her chronological age will be five on or before September 30 of the year of entering school. A birth certificate must be presented upon registration as proof of the date of birth. Please refer to Winnisquam Regional School Board Policy JEB for Age of Entrance and early entrance request requirements." Policy JEB itself not found on the site (no policy manual link found). Raw copy: raw/districts/batch-6/winnisquam-elem-handbook.txt

## kindergarten-registration: Kindergarten Registration by District

- kind: local
- question_type: local_practice
- description: When and how each district takes kindergarten registration, for the most recent year posted.

1. In SAU 39 (Amherst School District), new students register by completing an online PowerSchool pre-registration form, then the enrollment forms, and presenting an original birth certificate, proof of residency (a Certificate of Address signed by the town clerk) and health records. Pre-K and kindergarten registration questions go to Clark-Wilkins Elementary School. No registration window or dates were posted when checked.
   - citation: SAU 39 - New Student Information
   - source: https://www.sau39.org/sau-info/new-student-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Amherst
   - note: Page text: "To register your new student please complete the [https://sau39.powerschool.com/public/formbuilder/form.html?formid=5541122] Pre-Registration Form. ... Grades Pre-K and Kindergarten:" Process only; no window. Raw copy: raw/districts/batch-2/sau39-new-student.txt
2. In the Auburn School District, families register children for preschool through grade 8 at Auburn Village School with an online form; the registration page already accepts registrations for the 2027-28 school year. No specific kindergarten registration window is posted.
   - citation: Auburn Village School, Registration
   - source: https://auburn.sau15.net/registration/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Auburn
   - note: Page text: "To register a child for the 2026-2027 or the 2027-2028 school year for grades Preschool – 8, please complete this online form. Choose the enrollment year 2027-2028 for next school year!" Raw copy: raw/districts/batch-3/auburn-registration.txt
3. In the Barnstead School District, families get a kindergarten registration packet by calling Barnstead Elementary School at (603) 269-5161 or stopping by the school office. No registration dates for 2026-27 or 2027-28 were posted as of November 8, 2026.
   - citation: Barnstead Elementary School - Kindergarten Registration
   - source: https://bes.pmsau.nh.gov/o/bes/page/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barnstead
   - note: Page text: "Please contact us at (603) 269-5161 for a registration packet or stop by the school office" No window dates. Raw copy: raw/districts/batch-5/barnstead-bes-kindergarten-registration.txt
4. In the Barrington School District, new kindergarten to grade 8 students for the 2026-27 school year register online through a PowerSchool registration link on the district's New Student Registration page. Families call the Early Childhood Learning Center for preschool registration, or 603-664-5586 for preschool and kindergarten during the current year. No registration dates or 2027-28 window are posted.
   - citation: Barrington School District - New Student Registration
   - source: https://www.sau74.org/for_families/new_student_registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barrington
   - note: Page text: "This Registration link is for any NEW Kindergarten to 8th grade student who is registering for the NEXT (2026/2027) school year. Please call the ECLC for Preschool registration." Page still refers to 2026/2027 as 'NEXT' year as of 2026-11-08. Raw copy: raw/districts/batch-1/barrington-new-student-registration.txt
5. In the Bartlett School District, new students, including kindergartners, register through SAU 9's online Student Registration form, linked as 'New Students and Kindergarten' on the Josiah Bartlett Elementary School home page. No registration dates are posted.
   - citation: Josiah Bartlett Elementary School home (Quick Links)
   - source: https://jbes.sau9.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bartlett
   - note: Page text: "Student Registration New Students and Kindergarten" No window dates. Raw copy: raw/districts/batch-1/sau9-jbes-home.txt
6. In the Bow School District, new students, including kindergartners, register through SAU 67's online registration system; kindergarten families also complete a Kindergarten Parent Questionnaire. Bow Elementary School (grades K-4, 603-225-3049) serves Bow residents. No registration dates for 2026-27 or 2027-28 were posted as of November 8, 2026.
   - citation: SAU 67 - New Student Registration
   - source: https://sau67nh.gov/en/register
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bow
   - note: Page text: "If you have recently moved into Bow or Dunbarton, welcome! Please register your child with our online registration system. ... Bow Elementary (Grades K - 4) - Bow Residents ONLY - (603) 225-3049" Page rendered with headless Chrome (SchoolBlocks site). No window dates. Raw copy: raw/districts/batch-5/sau67-register.txt
7. In the Brookline School District, kindergarten pre-registration is done by bringing the pre-registration form, home language survey, developmental history form, birth certificate, immunization and physical records, and two proofs of residency to the Richard Maghakian Memorial School office; the rest is completed online over the summer. The page still describes the 2025-26 school year, and no dates for 2026-27 or 2027-28 were posted as of November 8, 2026.
   - citation: RMMS Kindergarten Registration directions (linked from https://www.sau41.org/fs/pages/2136)
   - source: https://www.myrmms.org/fs/resource-manager/view/e09add90-af24-4d70-94b3-8e43a3c438b8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brookline
   - note: Page text: "Please complete the Pre-registration form, the NH Home language survey and the Developmental History form and bring it to the RMMS office with the documentation described below." RMMS phone (603) 673-4640. Raw copy: raw/districts/batch-5/brookline-rmms-k-directions.txt; raw/districts/batch-5/brookline-rmms-kindergarten.txt
8. In the Candia School District, registration for fall 2026 kindergarten opened in February 2026 (announced February 11, 2026); registration was finalized at a kindergarten information night on Wednesday, March 18, 2026, at 5:30 p.m. at the Henry W. Moore School.
   - citation: Henry W. Moore School, Registration & Enrollment; 'Kindergarten Registration – Now Open' post (Feb 11, 2026)
   - source: https://candia.sau15.net/registration-enrollment/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Candia
   - note: Page text: "On Wednesday, March 18, 2026 at 5:30 p.m., we will be holding an information night for parents of NEW Kindergarten students ... During Kindergarten Information Night, you will finalize the registration process." Raw copy: raw/districts/batch-3/candia-registration.txt; raw/districts/batch-3/candia-k-reg.txt
9. Chichester Central School registers kindergarten students through the Alma Start online system (sau53.almastart.com); its registration page described 2026-27 registration for kindergarten students beginning in fall 2026 as "not active yet" when checked, and no dates were posted.
   - citation: Chichester Central School - Registration
   - source: https://ccs.sau53.org/pages/834ae1f4-1427-4f67-ac1b-f33c4381f67e
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chichester
   - note: Page text: "REGISTERING FOR THE 2026–2027 SCHOOL YEAR (not active yet) This registration is for: Kindergarten students beginning in fall 2026" Page appears not updated since spring 2026. A separate page is titled 'Registration Info For 2026-2027 Coming Soon!'. Raw copy: raw/districts/batch-7/sau53-ccs-registration.txt
10. In the Claremont School District, families of new kindergartners for 2026-27 complete the 2026-2027 New Student Registration and contact Disnard Elementary School (kindergarten to grade 2, 543-4260 x 4101); Disnard then schedules a kindergarten screening. Families bring a birth certificate, proof of residency and an immunization record. No registration dates are posted.
   - citation: SAU #6 - Student Registration
   - source: https://www.sau6.org/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Claremont
   - note: Page text: "If your child has never attended school within the Claremont School District and you are registering them for Kindergarten for the 2026-2027 school year, please complete the 2026-2027 New Student Registration." Raw copy: raw/districts/batch-6/claremont-registration.txt
11. The Concord School District's registration for the 2026-27 school year, including kindergarten, is open through its online enrollment system (InfoSnap); families contact their neighborhood school with questions. No 2027-28 kindergarten registration dates were posted as of November 8, 2026.
   - citation: Concord School District - Registration
   - source: https://sau8.org/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Concord
   - note: Page text: "Registration for the 2026-2027 school year is now open! To register for the 2026-2027 school year, please visit 2026-2027 Enroll | Concord District" Required documents: two proofs of residency, birth certificate, immunization records, current physical. No window dates posted. Raw copy: raw/districts/batch-5/concord-registration.txt
12. In the Conway School District, new students, including kindergartners, register through SAU 9's online Student Registration form (PowerSchool), linked as 'New Students and Kindergarten' on the Pine Tree Primary School home page. No registration dates are posted.
   - citation: Pine Tree Primary School home (Quick Links)
   - source: https://ptps.sau9.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Conway
   - note: Page text: "Student Registration New Students and Kindergarten" Form: https://sau9.powerschool.com/public/formbuilder/form.html?formid=4381149. No window dates. Raw copy: raw/districts/batch-1/sau9-ptps-home.txt
13. In the Cornish School District, kindergarten pre-registration for resident children (age five by September 30) for 2025-26 opened March 3 by email or phone to the school, with no cap on numbers; families then complete online enrollment (Alma Start). No 2026-27 or 2027-28 kindergarten dates were posted when checked.
   - citation: Cornish Elementary School - PreK-K Pre-Enrollment Statement 2025-2026
   - source: https://www.cornishschool.org/ourpages/auto/2024/6/26/50870748/PreK-K%20Pre-Enrollment%20Statement%202025-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Cornish
   - note: Page text: "To pre-register for full-day Kindergarten, children must be a resident of Cornish and turn 5 years of age on or before September 30, 2025. All resident children who are 5 years old by the date specified are welcome - there is no cap on numbers. Pre-registration is as follows: Resident students who are 5 years old Pre-registration opens March 3rd" Older-year notice; still the one linked when checked. Raw copy: raw/districts/batch-2/cornish-prek-k-statement-2025-26.txt
14. In the Croydon School District, families may enroll a child in kindergarten at any point for the current or upcoming school year using the form on the district's enrollment page; all Croydon resident children are guaranteed admission.
   - citation: Croydon School District - Enrollment (Pre-K & K)
   - source: https://croydonsd.org/cvs/enrollment/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Croydon
   - note: Page text: "Families may enroll their child in kindergarten at any point for the current or upcoming school year. Kindergarteners must be 5 years old as of September 30 of the school year in which they are enrolling. All children are guaranteed admission provided they are Croydon residents." Raw copy: raw/districts/batch-6/croydon-cvs-enrollment.txt
15. To register a child for kindergarten through grade 8 at Deerfield Community School, families email or call the school registrar (kdavitt@sau53.org, 603-463-7422 x101) and provide a birth certificate, immunization records and a residency affidavit with two proofs of residency; no registration window is posted.
   - citation: Deerfield Community School - New Student Registration
   - source: https://dcs.sau53.org/pages/917e280b-a99e-4077-b8ef-76c1878f58eb
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Deerfield
   - note: Page text: "To register your child as a student* in grades K** through 8 at DCS, please email/call Kandy Davitt at kdavitt@sau53.org or 603-463-7422 x101." The DCS home page also links a '2026-2027 NEW STUDENT REGISTRATION FORM' (Google Form https://forms.gle/xjDTTn7R9eLDQsXN8). Raw copy: raw/districts/batch-7/sau53-dcs-new-student-registration.txt
16. In the Derry Cooperative School District, online registration for 2026-27 kindergarten (and the DEEP preschool) opened at 8:00 a.m. on March 2, 2026, through PowerSchool/InfoSnap. Placement is first-come, first-served at each school; if a school's kindergarten classes fill (the board's recommended class size is 18), a child is assigned to another elementary school with openings.
   - citation: Derry Cooperative School District, Registration - Kindergarten
   - source: https://sau10.nh.gov/families/registration-kindergarten
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Derry Cooperative
   - note: Page text: "Click on the link below to register (beginning March 2, 2026) your child for Kindergarten in the 2026-2027 school year. Please note that registration is on a first-come, first-served basis at each school." No 2027-28 dates posted as of 2026-11-08. Documents: photo ID, birth certificate, immunizations, physical, two proofs of residency. Raw copy: raw/districts/batch-3/derry-k-registration.txt
17. In the Dover School District, kindergarten registration for the 2026-27 school year opened on March 16, 2026, through the district's online registration system; families can call their elementary school for in-person help. No 2027-28 dates were posted as of November 8, 2026.
   - citation: Dover School District - Student Registration
   - source: https://www.sau11.nh.gov/apps/pages/index.jsp?uREC_ID=2140303&type=d
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dover
   - note: Page text: "Kindergarten registration for the 26-27 school year opens on March 16. Any kindergarten registrations done prior to March 16 may not be valid and will need to be resubmitted." The page does not give an end date. The linked 2025 letter (raw/districts/batch-8/dover-k-registration-2025.txt) gave the 2025 steps: online registration from March 10, screening in mid-June, orientation August 28. Raw copy: raw/districts/batch-8/dover-registration.txt
18. In the Dunbarton School District, new students, including kindergartners, register through SAU 67's online registration system; kindergarten families also complete a Kindergarten Parent Questionnaire. Dunbarton Elementary School (grades K-6, 603-774-3181) serves Dunbarton residents. No registration dates were posted as of November 8, 2026.
   - citation: SAU 67 - New Student Registration
   - source: https://sau67nh.gov/en/register
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dunbarton
   - note: Page text: "Dunbarton Elementary (Grades K - 6) - Dunbarton Residents ONLY - (603) 774-3181" No window dates. Raw copy: raw/districts/batch-5/sau67-register.txt
19. East Kingston Elementary School registered kindergarten students for 2026-27 through an online new-student registration link; children had to be five on or before September 30, 2026 (born October 1, 2020 through September 30, 2021) and live in East Kingston. A parent orientation was held April 15 and a Kindergarten Camp on June 1-2. No 2027-28 dates were posted as of November 8, 2026.
   - citation: East Kingston Elementary - 2026-27 Kindergarten Registration
   - source: https://eks.sau16.org/kindergarten-registration-c6058a04
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district East Kingston
   - note: Page text: "East Kingston Elementary School is currently registering kindergarten students for the 2026-27 school year. Students must be five years old on or before September 30, 2026 (DOB 10/1/20 through 9/30/21) and be a resident of East Kingston." No opening or closing date given. Raw copy: raw/districts/batch-8/eks-k-registration.txt
20. For 2026-27 kindergarten at Epping Elementary School, the Epping School District asked families to complete the online New Student Registration (under Parent/Student Links on the district website) as soon as possible and before May 1, 2026; kindergarten screening was on May 15, 2026, and the first day for kindergarten students was September 2. No 2027-28 dates are posted yet.
   - citation: Epping Elementary School - Incoming Kindergarteners 2026-2027 School Year (flyer linked from https://www.sau14.org/)
   - source: https://www.sau14.org/district/important-news-updates/files/images/Kindergarten%20Info%2026-27%202.jpg?mask=1
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epping
   - note: Page text: "In order to let us know you have a Kindergartener who will be attending EES next school year (26-27), you will need to click on the NEW STUDENT REGISTRATION ... ASAP Prior to May 1, 2026 ... Kindergarten Screening ... May 15, 2026 ... First Day of School for K Students: Sept 2nd" Flyer is an image; quote transcribed by hand. Contact: Karen Mongeon, kmongeon@eppingsd.org, 603-679-8018 (EES FAQ). Raw copy: raw/districts/batch-4/epping-k-info-2026-27.jpg; raw/districts/batch-4/epping-k-info-2026-27.txt
21. In the Franklin School District, families of students new to the district register online at fsd.almastart.com by creating an account and enrolling the student at the right school. For help, they can call the school, such as Paul A. Smith School at 934-4144. No registration dates are posted.
   - citation: Franklin Schools SAU #18 - Student Registration
   - source: https://www.sau18.nh.gov/page/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Franklin
   - note: Page text: "Parents/Guardians - Use fsd.almastart.com to create an account and enroll your student at the appropriate school" Page says it is for students new to the district with no siblings in Franklin Schools. No window dates. Raw copy: raw/districts/batch-1/franklin-student-registration.txt
22. To enroll a new kindergarten student, Freedom families complete the kindergarten registration packet and email it to the school or drop it off at Freedom Elementary School (grades K-6, 40 Loon Lake Rd, 603-539-2077); no registration window is posted.
   - citation: Freedom Elementary School - Student Registration Information
   - source: https://www.freedomelschool.com/home/important-information/student-registration-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Freedom
   - note: Page text: "Please feel free to email your completed packet to" Page lists the '2026/2027 Registration Packet'. SAU 13 registration page links the Freedom Kindergarten Registration Packet. Raw copy: raw/districts/batch-7/freedom-registration.txt; raw/districts/batch-7/sau13-student-registration.txt
23. In the Gilford School District, new students, including kindergartners, register at Gilford Elementary School (kindergarten to grade 4) online through Alma: new families use Alma Start, and families with a child already enrolled add the child in their Alma profile. A birth certificate, immunization record and physical, and two proofs of residency are required. No registration dates are posted.
   - citation: Gilford Elementary School - New Student Registration
   - source: https://ges.sau73nh.gov/en-US/new-student-registration-2666f722
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Gilford
   - note: Page text: "Welcome to Gilford Elementary School! In order to register your child, we require a copy of their birth certificate, their immunization record and physical, custody/guardianship documents (if applicable), and two forms of proof of residency such as utility bills etc." Raw copy: raw/districts/batch-6/gilford-ges-registration.txt
24. The Goffstown School District was accepting kindergarten registration for 2026-27 through an online pre-registration form followed by online registration (Glen Lake School); no closing date was posted. No 2027-28 kindergarten registration information was posted as of November 8, 2026.
   - citation: SAU 19 - Glen Lake Kindergarten Registration
   - source: https://www.sau19.org/index.php/en/information-7/familes/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Goffstown
   - note: Page text: "Kindergarten registration is currently being accepted for the school year 2026/2027." Documents: birth certificate, two proofs of residency, etc. Glen Lake School phone (603) 497-3550. The March 10, 2026 ballot also included an open enrollment article (RSA 194-D) to admit 5 out-of-district students into kindergarten at Glen Lake School (sample ballot). Raw copy: raw/districts/batch-7/goffstown-kindergarten-registration-sau19.txt
25. In the Governor Wentworth Regional School District, new students register online through Infinite Campus (2026-27 New Student Registration). New Durham School held kindergarten registration appointments on April 10, 2026 for children turning five before September 30, 2026; families called the school at 603-859-2061. No 2027-28 dates were posted as of November 8, 2026, and no registration dates were found for the district's other elementary schools.
   - citation: New Durham Elementary School - Kindergarten Registration
   - source: https://newdurhamschool.sau49nh.gov/resources/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Governor Wentworth Regional
   - note: Page text: "If you have a child turning five before September 30, 2026 please contact the New Durham School at 603-859-2061 or e-mail for an appointment on April 10, 2026." District enrollment page https://gwrsd.sau49nh.gov/families/requirements-for-school-enrollment links the 2026-2027 New Student Registration. Raw copy: raw/districts/batch-5/gwrsd-nds-k-registration.txt; raw/districts/batch-5/gwrsd-enrollment.txt
26. In the Grantham School District, families register children for preschool through grade 6, including kindergarten, by emailing the required documents (birth certificate, residency affidavit, home language survey, record release, kindergarten questionnaire, physical and immunization records, and two proofs of residency) to Grantham Village School. No registration dates for 2026-27 or 2027-28 were posted as of November 8, 2026.
   - citation: Grantham Village School - PK-6 Registration
   - source: https://www.gvshawks.org/apps/pages/index.jsp?uREC_ID=3298781&type=d&pREC_ID=2556690
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Grantham
   - note: Page text: "Documents Required for Registration: Birth Certificate ... Kindergarten Questionnaire Most recent physical and immunization records 2 Proof of Residency Documentation" No window dates. Raw copy: raw/districts/batch-5/grantham-registration.txt
27. For 2026-27, Hampstead Central School asked families of incoming kindergarten and preschool children to fill out an interest survey, held a Kindergarten Parent Night on Thursday, February 19, 2026, and scheduled kindergarten screenings (including Friday, May 8, 2026). New students register online through PowerSchool Enrollment Express after calling the school office. No 2027-28 dates were posted as of November 8, 2026.
   - citation: Hampstead Central School news - 2026-2027 Kindergarten Interest; Hampstead School District - New Student Registration (https://www.hampsteadschools.net/page/new-student-registration)
   - source: https://hcs.hampsteadschools.net/o/hcs/article/1971679
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampstead
   - note: Page text: "There will be a Kindergarten Parent Night on Thursday, February 19th at 6:00pm at the Hampstead Central School." Registration page: 'Hampstead Central School: 603-329-6326 x1100 (PreK and Kindergarten will wish to express their preference for time slots).' May 8 screening from the full-day pilot article. The year of 'February 19th' is inferred from the 2026-27 article title. Raw copy: raw/districts/batch-8/hampstead-k-interest.txt; raw/districts/batch-8/hampstead-registration.txt; raw/districts/batch-8/hampstead-fdk-pilot.txt
28. Lincoln Akerman School (Hampton Falls) takes 2026-27 new student registration, including kindergarten, through an online registration portal, with a NH driver's license, a home purchase or lease document and a utility bill showing a Hampton Falls address; no registration window is posted. No 2027-28 information was posted as of November 8, 2026.
   - citation: Lincoln Akerman School - Student Registration
   - source: https://www.sau21.nh.gov/las/about-las/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton Falls
   - note: Page text: "2026-27 New Student Registration This information is needed only for students that have never registered for any SAU 21 schools before." Raw copy: raw/districts/batch-7/hamptonfalls-las-registration.txt
29. In the Henniker School District, Henniker Community School holds a kindergarten pre-registration program in the spring; no dates for 2027-28 are posted.
   - citation: Henniker Community School, Student Registration
   - source: https://www.sau24.org/schools/hennikercommunityschool/about-us/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Henniker
   - note: Page text: "The school has a pre-registration program for kindergarten which takes place in the Spring." Raw copy: raw/districts/batch-3/sau24-hennikercommunityschool-reg.txt
30. In the Hillsboro-Deering Cooperative School District, families pre-registered for 2026-27 kindergarten online (hdsd.powerschool.com) and picked up a registration packet at the Hillsboro-Deering Elementary School main office from March 30 to April 10, 2026, 8 a.m. to 4 p.m. A kindergarten parent information night was held May 20, 2026, and kindergarten screening sign-ups were posted April 23, 2026.
   - citation: SAU #34 News, '2026-2027 Hillsboro-Deering Elementary School Kindergarten Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hillsboro-Deering Cooperative
   - note: Page text: "Please pre-register at https://hdsd.powerschool.com/public/ and then pick up a registration packet at the Hillsboro-Deering Elementary School Main Office 3/30/26-4/10/26 between 8am-4pm." 2027-28 registration not yet posted as of 2026-11-08. Contact: Cathy Bennett, HDES main office, 464-1122. Raw copy: raw/districts/batch-6/sau34-home.txt
31. The most recent kindergarten registration notice on the Hinsdale School District site is from 2023: kindergarten registration began March 27, 2023, Monday-Friday 10:00-2:00, through the Hinsdale Elementary School office (603-336-5332). No 2026-27 or 2027-28 notice was found.
   - citation: Hinsdale School District news - Preschool and Kindergarten Registration (March 20, 2023)
   - source: https://www.hnhsd.org/?p=3662
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hinsdale
   - note: Page text: "Kindergarten Registration begins 3/27th, M-F, 10:00-2:00." Old notice; included so the Ask can say the district posts registration in late March but current dates were not found. The 2026-27 handbook says PreK and kindergarten class lists are finalized in August after spring/summer screenings and rolling enrollment. Raw copy: raw/districts/batch-8/hinsdale-k-registration.txt
32. In the Holderness School District, families register by calling the Holderness Central School main office at 603-536-2538 and providing proof of residency, general and medical information, and a records transfer authorization. No kindergarten registration dates are posted.
   - citation: Holderness Central School 2026-2027 Parent-Student Handbook
   - source: https://drive.google.com/file/d/1uNNd-UWyo6jTR4v1kWqp8pAdXPqqGzw6/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Holderness
   - note: Page text: "Registration/Transfer: To register for school, please call the main office at 603-536-2538. Families must provide proof of residency during the registration process." Raw copy: raw/districts/batch-6/holderness-handbook-2627.txt
33. In the Hollis School District, families register for kindergarten at Hollis Primary School by completing the SAU41 pre-registration form, home language survey and developmental history form and then calling the school office (603-324-5995 x7) for an appointment to drop off documents. No registration dates for 2026-27 or 2027-28 were posted as of November 8, 2026.
   - citation: Hollis Primary School - Kindergarten Registration
   - source: https://www.sau41.org/fs/pages/1941
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hollis
   - note: Page text: "Please contact our school office at the number below to set up an appointment to drop off registration documents. (603)324-5995 x7" No window dates. Raw copy: raw/districts/batch-5/hollis-hps-kindergarten.txt
34. In the Hooksett School District, online registration for 2026-27 kindergarten at Underhill School opened on March 2, 2026; children had to be Hooksett residents and 5 years old on or before September 30, 2026. A kindergarten information night for parents was held April 7, 2026.
   - citation: Underhill School, 'Kindergarten Registration for 2026-2027 School Year Now Open' (March 2, 2026)
   - source: https://underhill.sau15.net/2026/03/02/kindergarten-registration-for-2026-2027-school-year-now-open/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hooksett
   - note: Page text: "The online registration portal for incoming Kindergarten students for the 2026-2027 school year at Underhill School is now open! ... Students must be Hooksett residents and be 5 years old on or before September 30, 2026." Registration link: https://hooksett.sau15.net/upcoming-school-year/. No closing date stated; no 2027-28 notice yet. Raw copy: raw/districts/batch-3/hooksett-k-reg.txt; raw/districts/batch-3/hooksett-k-infonight.txt
35. The Hudson School District registers new students, including kindergarten, online; its registration page links to registration for the 2026-27 school year. No 2027-28 kindergarten registration dates were posted as of November 8, 2026.
   - citation: Hudson School District - Registration
   - source: https://www.sau81.org/families/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hudson
   - note: Page text: "Online registration is now available for new students entering the district in Kindergarten through grade 12. ... Register for the 2026-2027 School Year" No window dates on page. Raw copy: raw/districts/batch-5/hudson-registration.txt
36. In the Jackson School District, families register kindergartners for 2026-27 online through SAU 9's New Student Registration. Jackson Grammar School's kindergarten registration event had already taken place, and families can call the school office at 603-383-6861 to schedule a tour.
   - citation: Jackson Grammar School - Preschoolers and Kindergarten Registration
   - source: https://jgs.sau9.org/kindergartenregistration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jackson
   - note: Page text: "While the Kindergarten Regsitration event is over, parents can still register their students on the SAU 9 website" Event date not given. No 2027-28 information. Raw copy: raw/districts/batch-1/jackson-jgs-kindergarten-registration.txt
37. In the Jaffrey-Rindge Cooperative School District, registration for all grades, including kindergarten, for the 2026-27 school year opened on April 1, 2026, through the Alma student information system. Children continuing from the district's preschool use the Annual Learner Update instead. No 2027-28 dates were posted as of November 8, 2026.
   - citation: Kindergarten Registration Opening April 1 (posted 03/30/2026)
   - source: https://www.sau47.org/news/sau47/kindergarten_registration_opening_april_1
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jaffrey-Rindge Cooperative
   - note: Page text: "Registration will open on April 1, for all grades for the 2026-27 school year. ... If your child attended preschool and is continuing to kindergarten in the district, you will follow the steps for a 'Annual Learner Update'" No closing date given. Raw copy: raw/districts/batch-5/jaffrey-rindge-k-registration.txt
38. In the Kearsarge Regional School District, kindergarten registration for 2026-27 (Class of 2039) is done online at kearsarge.org: families complete a pre-registration form and then the PowerSchool registration forms, with proof of residency, a birth certificate, and immunization and physical records. Children attend Kearsarge Regional Elementary at Bradford (Newbury and Bradford), at New London (Springfield, New London, Wilmot), Simonds School (Warner) or Sutton Central School (Sutton). No registration dates are posted.
   - citation: Kearsarge Regional School District kindergarten registration flyer 2026-27 (linked from https://www.kearsarge.org/node/18241)
   - source: https://www.kearsarge.org/sites/g/files/vyhlif731/f/pages/kindergarten_26.27.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kearsarge Regional
   - note: Page text: "KINDERGARTEN REGISTRATION IS HERE! Class of 2039 REGISTRATION REQUIREMENTS Must be 5 by Sept. 30th Proof of Residency Copy of Original Birth Certificate Immunization & Physical Records REGISTER TODAY AT WWW.KEARSARGE.ORG" Flyer is an image PDF (no text layer); quote transcribed from the image as viewed. Registration steps from the New Student Registration Google Doc (raw kearsarge-registration-doc.txt): pre-registration form at kearsarge.powerschool.com, then PowerSchool forms. Raw copy: raw/districts/batch-6/kearsarge-k-2627.pdf
39. Kensington Elementary School's registration page says kindergarten registration for fall 2026 is open, through the online 'Kindergarten or New Student Registration 2026-2027' form. No dates or 2027-28 information were posted as of November 8, 2026.
   - citation: Kensington Elementary School - Student Registration
   - source: https://www.sau16.org/pages/cff44a60-7b4a-4396-880c-e892afb7e375
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kensington
   - note: Page text: "Kindergarten registration is now OPEN for the Fall of 2026!" Raw copy: raw/districts/batch-8/kes-registration.txt
40. In the Laconia School District, families new to the district register students for 2026-27 online through an Alma Start account, then upload documents (birth certificate, proof of residency, immunization records and a physical from the past 12 months). No kindergarten-specific registration dates were posted when checked.
   - citation: Laconia School District (SAU 30) home page; New Student Registration page
   - source: https://www.sau30.org
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Laconia
   - note: Page text: "Families who are new to the Laconia School District can begin the registration process online for the 2026–2027 school year." New student page: https://www.sau30.org/26-27-new-student.html. No window/dates posted. Raw copy: raw/districts/batch-2/laconia-sau30-home.txt; raw/districts/batch-2/laconia-new-student-2026-27.txt
41. In the Lebanon School District, families of incoming kindergartners call to set an enrollment appointment, and a kindergarten screening is part of enrolling; children already in the district's preschool are registered for kindergarten automatically. No registration dates for 2027-28 were posted.
   - citation: Lebanon School District (SAU 88), Enrollment
   - source: https://www.sau88.net/families/enrollment
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lebanon
   - note: Page text: "For kindergarten registration, if your student is enrolled is the district's preschool program, they are automatically registered for kindergarten. Your child's school should contact you directly about scheduling a kindergarten screening." Process only; no window dates on the page. Raw copy: raw/districts/batch-3/lebanon-enroll.txt
42. For 2026-27, the Lincoln-Woodstock Cooperative School District asked families of children who will be five by September 30, 2026 to contact Lin-Wood Elementary School (603-745-2214 ext. 233) to schedule a registration appointment, and posts a 2026-2027 Kindergarten Registration Packet. No 2027-28 information was posted as of November 8, 2026.
   - citation: Lincoln-Woodstock Cooperative School District - Enrollment
   - source: https://www.lin-wood.org/about-lin-wood/enrollment
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lincoln-Woodstock Cooperative
   - note: Page text: "If you have, or know anyone that has a child that will be 5 years old by September 30, 2026, PLEASE contact Sheila Rich at the Lin-Wood Elementary School: (603) 745-2214 ext. 233" Documents: birth certificate, proof of residence, immunization record, physical within the past year. Raw copy: raw/districts/batch-7/linwood-enrollment.txt
43. In the Litchfield School District, all new student registrations, kindergarten to grade 12, begin with an online registration application; the school then contacts the family to finish paperwork and schedule orientation. Kindergarten is at Griffin Memorial School (Pre-K to grade 4). Registration requires proof of age (such as a birth certificate), three proofs of Litchfield residency, and immunization and physical exam records. No registration dates are posted.
   - citation: Litchfield School District - Student Registration
   - source: https://www.litchfieldsd.org/StudentRegistration1.aspx
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Litchfield
   - note: Page text: "All new student registrations begin with an online registration application. Please review the required documents below before starting the registration process." Document list from the 'Kindergarten Documents' Google Doc linked on Griffin Memorial School's page (raw litchfield-k-documents.txt). Raw copy: raw/districts/batch-6/litchfield-registration.txt
44. In the Littleton School District, families new to the district register kindergarten through grade 6 students by contacting Mildred C. Lakeway Elementary School (603-444-2831); families with a child already enrolled add a new student through the Alma parent portal. No kindergarten registration dates for 2026-27 or 2027-28 were found as of November 8, 2026.
   - citation: Littleton School District - Enrollment & Registration
   - source: https://www.sau84.org/apps/pages/index.jsp?uREC_ID=2790425&type=d&pREC_ID=2309259
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Littleton
   - note: Page text: "For students who have never attended a Littleton School District school. Please contact: K-6 (Lakeway) 603-444-2831" Lakeway's Kindergarten Registration page links to a Drive flyer that no longer exists. Raw copy: raw/districts/batch-5/littleton-enrollment.txt; raw/districts/batch-5/littleton-lakeway-k-registration.txt
45. The Londonderry School District has not yet posted 2027-28 kindergarten registration dates (its Moose Hill School page says to stay tuned). For 2026-27, kindergarten registration started on November 5, 2025, through the district's online new student registration form.
   - citation: 2026-27 Full Day Kindergarten Survey and Upcoming Registration for Families (posted 2025-10-29)
   - source: https://news.londonderry.org/2025/10/29/2026-27-full-day-kindergarten-survey-and-upcoming-registration-for-families
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Londonderry
   - note: Page text: "Stay tuned for 2027-2028 Kindergarten Registration. | We will start Kindergarten Registration on Nov. 5th, 2025, about three months earlier than normal, to help us better plan for the upcoming school budget." Registration page https://www.londonderry.org/family/student-registration: 'If registering for the 26/27 school year, scroll to the bottom and complete the New Student Registration.' Registrar: registrar@londonderry.org. Raw copy: raw/districts/batch-4/londonderry-news-fdk-registration.txt; raw/districts/batch-4/londonderry-moosehill-home.txt; raw/districts/batch-4/londonderry-family-student-registration.txt
46. The Lyme School District generally holds kindergarten registration in May for the following school year; families bring the child's birth certificate and immunization records. No specific 2027-28 date was posted as of November 8, 2026.
   - citation: Lyme School - Registration
   - source: https://www.lymeschool.org/page/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lyme
   - note: Page text: "Kindergarten registration is generally held in May for the following school year." New students register through Alma (link on the page). Raw copy: raw/districts/batch-7/lyme-registration.txt
47. To enroll a new kindergarten student, Madison families download and complete the kindergarten registration packet and call the Madison Elementary School principal (603-367-4642) to set a start date; no registration window is posted.
   - citation: Madison Elementary School - home page
   - source: https://sites.google.com/a/mes-nh.com/madison-elementary-school/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Madison
   - note: Page text: "To enroll a new student, please download and complete this registration packet for Kindergarten or this registration packet for 1st through 6th graders and call to speak with the principal about setting a start date. 603-367-4642" Raw copy: raw/districts/batch-7/madison-home.txt
48. In the Manchester School District, registration for the 2026-27 school year (including kindergarten) opened online on March 21, 2026; families could also register at the District Welcome Center (148 Concord St., Monday-Friday 8 am-4 pm) or at elementary school registration events held in March and April 2026. A 2027-28 window was not yet posted.
   - citation: Registration Now Open for 2026-2027 School Year (March 21, 2026)
   - source: https://www.mansd.org/article/2775173
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Manchester
   - note: Page text: "Registration is now open for Manchester School District for the 2026-2027 school year. ... Visit our Welcome Center ... The Welcome Center is located at 148 Concord St., across from the city library. The center is staffed Monday-Friday from 8 am-4 pm." Registration page says 'Registration is open Saturday, March 21th 2026 for 2026 - 2027 School Year' and online 'starting March 20, 2026'; the two dates differ slightly on the district's own pages. Only new students register. Raw copy: raw/districts/batch-1/manchester-registration-2026-27-article.txt
49. In the Mascoma Valley Regional School District, kindergarten registration for 2026-27 opened March 2, 2026. Families of children who will be five on or before September 30, 2026 contact Canaan Elementary School (residents of Canaan, Dorchester, Grafton and Orange) or Enfield Village School (residents of Enfield or Grafton-Route 4A), and complete the online enrollment form. No 2027-28 dates were posted when checked.
   - citation: Mascoma Valley Regional School District - Enrollment
   - source: https://www.mascomaschools.org/our-district/enrollment
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mascoma Valley Regional
   - note: Page text: "MASCOMA VALLEY REGIONAL SCHOOL DISTRICT 2026-2027 KINDERGARTEN REGISTRATION ... OPEN ENROLLMENT Starting March 2, 2026" Raw copy: raw/districts/batch-2/mascoma-enrollment.txt
50. In the Mason School District, kindergarten registration uses forms posted on the Mason Elementary School registration page (personal data, health history, language survey and a kindergarten admission parent rating form); children already in the Mason preschool who are eligible for kindergarten are registered automatically. No registration window dates are posted.
   - citation: Mason School District, Registration Forms for Preschool, Kindergarten, Grade 1, Grades 2-5; Kindergarten FAQ 2025-26
   - source: https://www.sau89.nh.gov/apps/pages/index.jsp?uREC_ID=4462305&type=d&pREC_ID=2731331
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mason
   - note: Page text: "IF YOUR CHILD IS ELIGIBLE FOR KINDERGARTEN AND ALREADY ENROLLED IN THE PRESCHOOL PROGRAM THEY WILL AUTOMATICALLY BE REGISTERED" Process only. Raw copy: raw/districts/batch-3/mason-registration.txt; raw/districts/batch-3/mason-k-faq-25-26.txt
51. In the Merrimack School District, families register new students, including kindergartners, by contacting the elementary school their child will attend (James Mastricola, Reeds Ferry or Thorntons Ferry, by street address) and bringing completed forms to an appointment. The page posts no registration dates for 2026-27 or 2027-28.
   - citation: Merrimack School District - New Student Registration
   - source: https://www.sau26.org/parents/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack
   - note: Page text: "To begin the registration process, please contact the individual schools where your children will be attending" No dated registration window found. Raw copy: raw/districts/batch-1/merrimack-student-registration.txt
52. In the Merrimack Valley School District, families register a new student by calling their school for an appointment and bringing immunization records, a birth certificate and two proofs of residency. Boscawen Elementary posted that 2026-27 registration was open and asked families to call (603) 753-6512. No district-wide dates for 2026-27 or 2027-28 are posted.
   - citation: SAU 46 - New Student Registration
   - source: https://sites.google.com/a/mvsdpride.org/district/school-administrative-unit-46/new-student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack Valley
   - note: Page text: "1. Call your school for an appointment to register your child." Boscawen flyer: https://docs.google.com/document/d/1zE6DIdeauDLH0faE709vnaS8IcXUz8Ra ('2026-27 REGISTRATION IS NOW OPEN Call today (603) 753-6512'), raw mvsd-bes-kindergarten-registration-2026-27.txt. No window dates. Raw copy: raw/districts/batch-1/sau46-new-student-registration.txt
53. Middleton Elementary School held kindergarten registration for the 2026-27 school year on Wednesday, April 1, 2026, 2:00-4:30 pm, by appointment only (603-473-5000). Families brought proof of residency, a birth certificate, proof of a physical exam, immunization records and any custody papers. No 2027-28 date was posted as of November 8, 2026.
   - citation: Middleton Elementary School - Kindergarten Registration post (Feb 17, 2026), flyer image
   - source: https://www.middletonelementary.org/default-board-post-page/~board/test-board/post/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Middleton
   - note: Page text: "KINDERGARTEN REGISTRATION 2026-2027 SCHOOL YEAR WEDNESDAY, APRIL 1ST, 2026 2:00-4:30 PM BY APPOINTMENT ONLY" New students also use GWRSD's Infinite Campus registration (https://gwrsd.sau49nh.gov/families/requirements-for-school-enrollment mentions Middleton School District). Raw copy: raw/districts/batch-5/middleton-k-registration-flyer-2026-27.jpg
54. In the Milford School District, new students, including kindergartners, register online through the district website by uploading the required documents; kindergarten registration goes to Jacques Memorial Elementary School (kindergarten to grade 1). No registration dates are posted.
   - citation: Milford School District - Online Student Registration
   - source: https://www.milfordk12.org/apps/pages/Register-for-School
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milford
   - note: Page text: "You do not need to visit the district offices in person. Please follow the directions closely and be prepared to upload the required documents to complete your student registration." Page lists 'Kindergarten to 1 Jacques Memorial Elementary School 9 Elm St. ... (603) 673-4434 x 4002'. JMS home page links a kindergarten 'Screening Sign Up' (SignUpGenius) and a 'Rising Kindergarten Opportunity' Google Doc that has been deleted. Raw copy: raw/districts/batch-6/milford-register.txt
55. In the Monroe School District, preschool and kindergarten registration for 2026-27 was online through Alma Start (https://monroeschool77.almastart.com/). Registration day was May 8, with time slots booked through Alma Start. The first day of kindergarten was August 20. A 2027-28 window was not yet posted.
   - citation: Monroe Consolidated School - New Student Registration
   - source: https://sites.google.com/a/monroeschool77.com/monroe-consolidated-school/new-student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Monroe
   - note: Page text: "Preschool and Kindergarten registration for Fall 26-27 school year is now open. Please register you new student by using our online registration 'Alma Start.' ... Preschool and Kindergarten registration day is May 8th." Year of May 8 not stated on the page; read in context as 2026. Contact Karen Remick, 603-638-2800 ext. 110. Raw copy: raw/districts/batch-1/monroe-new-student-registration.txt
56. In SAU 39 (Mont Vernon School District), new students register by completing an online PowerSchool pre-registration form and the enrollment forms, with an original birth certificate, a Certificate of Address signed by the Mont Vernon town clerk, and health records; kindergarten questions go to Mont Vernon Village School. No registration window or dates were posted when checked.
   - citation: SAU 39 - New Student Information
   - source: https://www.sau39.org/sau-info/new-student-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mont Vernon
   - note: Page text: "Mont Vernon Village School ... Grades K-6:" Process only; no window. Raw copy: raw/districts/batch-2/sau39-new-student.txt
57. In the Nashua School District, registration for the 2026-27 school year (kindergarten through grade 12) opened on Monday, March 2, 2026. Families register online through the Aspen portal or by appointment at the Welcome Center at 17 Birch Hill Drive. No 2027-28 dates were posted when checked.
   - citation: Nashua School District - Enrollment & Registration
   - source: https://www.nashua.edu/fs/pages/5595
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nashua
   - note: Page text: "Registration for the 2026-2027 school year opens on Monday, March 2, 2026 for grades Kindergarten through 12th grade." Same page as https://www.nashua.edu/families-community/enrollment. Raw copy: raw/districts/batch-2/nashua-enrollment.txt
58. The New Boston School District opened online registration for incoming kindergarten, Readiness and first grade for 2026-27 early, to get a head count for budgeting and staffing; families complete an online pre-registration form, then an online registration. No closing date and no 2027-28 information were posted as of November 8, 2026.
   - citation: SAU 19 - New Boston Central School Kindergarten 2026-27
   - source: https://www.sau19.org/index.php/en/information-6/familes/new-student-registration-nbcs
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Boston
   - note: Page text: "INCOMING KINDERGARTEN, READINESS AND 1ST GRADE ONLINE REGISTRATION FOR THE 2026/27 SCHOOL YEAR IS NOW OPEN" School office 487-2211, nbcs_office@sau19.org. Raw copy: raw/districts/batch-7/newboston-kindergarten-2026-27.txt
59. The Newmarket School District's registration page says kindergarten registration for 2026-27 is open: families start with online registration, then send a birth certificate, three proofs of residency and physical and immunization records to Newmarket Elementary School by email, fax, mail or in person. No dates or 2027-28 information were posted as of November 8, 2026.
   - citation: Newmarket School District - Registration
   - source: https://www.newmarket.k12.nh.us/sau31/registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newmarket
   - note: Page text: "Kindergarten Registration is NOW OPEN for the school year 2026-2027." Raw copy: raw/districts/batch-8/newmarket-registration.txt
60. For 2026-27, kindergarten pre-registration in the Newport School District began Thursday, April 2, 2026, for Newport residents whose child would be 5 by September 30, 2026; kindergarten screenings were scheduled for June 1 or June 8 (contact: Richards School, 603-863-3710). No 2027-28 dates are posted yet.
   - citation: Newport School District news - Kindergarten Pre Registration Opens today (April 2, 2026)
   - source: https://www.sau43.nh.gov/article/2801581
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newport
   - note: Page text: "Kindergarten pre-registration begins Thursday, April 2, for all incoming kindergarten Newport students for the 2026-2027 school year. ... your child will be scheduled a time for their Kindergarten Screening on June 1st or 8th." Raw copy: raw/districts/batch-4/newport-pages.txt
61. North Hampton School's kindergarten registration portal was open January 16 to February 21 (for the 2026-27 school year), with a birth certificate and proof of residency required; no 2027-28 dates were posted as of November 8, 2026.
   - citation: North Hampton School - Kindergarten Registration
   - source: https://www.northhamptonschool.org/families/kindergarten-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district North Hampton
   - note: Page text: "Registration Portal: Open 1/16-2/21" The page does not state the year; the window is presumed to be early 2026 for 2026-27 because the page was current as of November 2026. Contact Sue MacLaughlan. Raw copy: raw/districts/batch-7/northhampton-kindergarten-registration.txt
62. In the Nottingham School District, families of children entering kindergarten in 2026-27 request a registration packet from the school (Jen Daniels, jdaniels@nhsau107.gov) and return it to the main office; kindergarten screening day was May 8, 2026. No fixed window or 2027-28 dates were posted when checked.
   - citation: Nottingham School - Kindergarten Registration
   - source: https://www.nottingham.k12.nh.us/about/kinderreg
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nottingham
   - note: Page text: "please contact Jen Daniels at [mailto:jdaniels@nhsau107.gov?subject=Kindergarten%20Registration] jdaniels@nhsau107.gov to request a registration packet. ... We will be having our Kindergarten screening day on May 8, 2026" Raw copy: raw/districts/batch-2/nottingham-kreg.txt
63. In the Oyster River Cooperative School District, kindergarten registration for 2026-27 was in person only, through the district: sessions ran January 27 to February 6, 2026 (at Oyster River High School, with evening sessions at the SAU office), with added sessions May 18-21, 2026 at the ORCSD Service Building, 33 Coe Drive, Durham. Families could not register directly with a school. No 2027-28 dates were posted when checked.
   - citation: ORCSD - 2026-2027 Kindergarten Registration Information (posted April 9, 2026; original December 18, 2025)
   - source: https://www.orcsd.org/news/1819416/2026-2027-kindergarten-registration-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Oyster River Coop
   - note: Page text: "kindergarten registration for the Oyster River Cooperative School District (ORCSD) for the 2026-2027 school year will begin on January 27, 2026. ... we will be offering additional kindergarten registration sessions for the 2026-2027 school year on May 18-21, 2026. ... No, registrations will only be accepted by the district during the in-person sessions at the locations listed above." The May flyer adds that families unavailable on those dates may make an appointment with the District Registrar (603-389-3300). Raw copy: raw/districts/batch-2/orcsd-k-registration-2026-27.txt; raw/districts/batch-2/orcsd-k-may-flyer-2026.txt
64. Bridgewater-Hebron Village School's kindergarten flyer asks families to contact the school (603-744-6969, frontoffice@sau108.org) to register for 'Kindergarten Connections' on April 23. The flyer does not give the year; no 2027-28 information was found.
   - citation: Bridgewater-Hebron Village School - Kindergarten registration flyer
   - source: https://aptg.co/x87s_j
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pasquaney
   - note: Page text: "CONTACT TO REGISTER FOR KINDERGARTEN CONNECTIONS ON APRIL 23RD! 603-744-6969" Undated flyer. Raw copy: raw/districts/batch-8/pasquaney-k-registration.txt
65. The Pelham School District registers new kindergarten to grade 5 students through an online form, after which families schedule an appointment at Pelham Elementary School to finish the paperwork; no registration dates for 2026-27 or 2027-28 were posted as of November 8, 2026.
   - citation: Pelham Elementary School - NEW Student Registration Information
   - source: https://www.pelhamsd.org/2022-2023Pre-KKand1stGradeRegistration-GoingLive129213pm.aspx
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pelham
   - note: Page text: "K-5 Registration **Please click the link below to complete the form and schedule an appointment** Online Registration Information You MUST complete the online form to come in to finish your paperwork" District registration page https://www.pelhamsd.org/Registration1.aspx covers K-12 (documents: original birth certificate, immunizations, physical within one year, proof of residency). Pelham Elementary phone (603) 635-8875. Raw copy: raw/districts/batch-7/pelham-prek-k-registration.txt; raw/districts/batch-7/pelham-registration.txt
66. The Pembroke School District registers kindergarten students for fall 2026 at Pembroke Hill School through the Alma Start online system (sau53.almastart.com), with a birth certificate, two proofs of residency, and physical and immunization records; no registration dates are posted. No 2027-28 information was posted as of November 8, 2026.
   - citation: Pembroke Hill School - Registration
   - source: https://phs.sau53.org/pages/8a33dd54-9f64-445a-907a-b6bf59285c93
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pembroke
   - note: Page text: "You will use Alma Start to register your student for Kindergarten beginning fall 2026 or students who are new to Pembroke Hill School beginning fall 2026" A Pembroke Hill news item dated Mar 2, 2026 announced kindergarten registration, and a Kindergarten Information Night was held May 7 (2026), per the rendered home page (raw sau53-phs-home-rendered.txt). Raw copy: raw/districts/batch-7/sau53-phs-registration.txt
67. Piermont Village School posts its registration forms online (student registration form, residency statement, home language survey and others). No registration dates are posted.
   - citation: Piermont Village School - Registration Paperwork
   - source: https://pvs.sau23.org/information-resources/registration-paperwork
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Piermont
   - note: Page text: "Registration Paperwork Registration Documents needed.docx Student Registration Form.docx" No window dates. Raw copy: raw/districts/batch-1/piermont-registration-paperwork.txt
68. In the Plainfield School District, new kindergarten students register online through the Alma student information system, with a birth certificate, proof of residency and immunization record; enrollment includes an educational screening and a chance to meet the teacher. No registration dates for 2026-27 or 2027-28 were posted as of November 8, 2026.
   - citation: Plainfield School District - Registration & Enrollment Instructions
   - source: https://sites.google.com/plainfieldschool.org/studentenrollment/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Plainfield
   - note: Page text: "As part of the enrollment process, students will have an educational screening along with an opportunity to meet their teacher and explore their classroom." No window dates. Raw copy: raw/districts/batch-5/plainfield-enrollment.txt
69. In the Plymouth School District, families register a student at Plymouth Elementary School by contacting the main office at (603) 536-1152; registration requires proof of residency, registration forms, medical and emergency information, and a records transfer authorization if needed. No kindergarten registration dates are posted.
   - citation: Plymouth Elementary School 2026-2027 Parent-Student Handbook (linked from https://sites.google.com/pemibaker.org/sau48/for-families/student-handbooks)
   - source: https://drive.google.com/file/d/1f5e-y8dmwwAeqhHPjPmqb5_6n3x93CF6/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Plymouth
   - note: Page text: "To register a student at Plymouth Elementary School, families should contact the Main Office at (603) 536-1152 . Registration requirements include: ● Proof of residency ● Student registration forms ● Medical and emergency information" Raw copy: raw/districts/batch-6/plymouth-handbook-2627.txt
70. The Portsmouth School Department's online registration through Infinite Campus for the 2026-27 school year was open as of November 8, 2026; the page gives no separate kindergarten window and no 2027-28 dates.
   - citation: Portsmouth School Department - Online Student Registration
   - source: https://www.cityofportsmouth.com/school/online-student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Portsmouth
   - note: Page text: "Online registration for the 26-27 academic year are live!" General registration page; kindergarten not mentioned specifically. Raw copy: raw/districts/batch-8/portsmouth-registration.txt
71. In the Raymond School District, online new-student enrollment (PowerSchool) for the 2026-27 school year was open when checked in November 2026; questions go to the child's school office (Lamprey River Elementary School, 895-3117). No separate kindergarten registration window or 2027-28 dates were posted.
   - citation: Raymond School District - Enrollment
   - source: https://www.sau33.com/district/pages/enrollment
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Raymond
   - note: Page text: "New Student Enrollment is open at this time for the 2026-2027 School Year" Raw copy: raw/districts/batch-2/raymond-enrollment.txt
72. In the Rochester School District, registration for kindergarten and first-time students for 2026-27 opened February 1, 2026, online through the district website (Infinite Campus); families were encouraged to complete kindergarten registration by April 1, 2026. Children who turn 5 on or before September 30, 2026 were eligible.
   - citation: Rochester Post (City of Rochester news), 'Rochester Schools Open Registration for Incoming Kindergarten and First-time Students', February 25, 2026
   - source: https://news.rochesternh.gov/rochester-schools-open-registration-for-incoming-kindergarten-students/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rochester
   - note: Page text: "registration opens February 1, 2026, for students entering kindergarten and first-time students to the district. Children who turn 5 years old on or before September 30, 2026, are eligible to register for kindergarten. Families are encouraged to complete kindergarten registration by April 1, 2026" City of Rochester news site, not the district site. District online registration page: https://www.rochesterschools.com/o/rsd/page/online-enrollment (PreK-5 registration 603-332-3678, student.registration@sau54.org). No 2027-28 dates posted as of 2026-11-08. Raw copy: raw/districts/batch-6/rochester-k-registration-news.txt
73. In the Rollinsford School District, Rollinsford Grade School was accepting kindergarten registrations for 2026-27 as of May 28, 2026; families download the packet from the school website, pick one up, or have one mailed, and return it to the school at 487 Locust St.
   - citation: Town of Rollinsford, 'Kindergarten Registration' (May 28, 2026)
   - source: https://rollinsford.nh.us/kindergarten-registration/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rollinsford
   - note: Page text: "Rollinsford Grade School is accepting kindergarten registrations for the 2026-2027 school year. ... You may get a registration packet by: Downloading the forms from our website Picking up a packet in person Requesting to have a packet mailed to you" No start or end dates given. Raw copy: raw/districts/batch-3/rollinsford-k-reg.txt
74. In the Rumney School District, registration at Russell Elementary School is digital, through the Alma student system linked from the school website; it includes general information, proof of residency, medication information and a records transfer authorization. No kindergarten registration dates are posted.
   - citation: Russell Elementary School Student Handbook 2026-2027
   - source: https://docs.google.com/document/d/1gwnEibXTHeC55d-xZTgQkJS_R9htX4W0yW9AKFwUnxo/edit?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rumney
   - note: Page text: "RES uses a digital registration system through our student management system called Alma. Parents should go to the school website and follow the instructions and links for registration." Raw copy: raw/districts/batch-6/rumney-handbook-2627.txt
75. Rye Elementary School registers new kindergarten through grade 4 students through an online registration link, then PowerSchool forms once approved; it asks prospective kindergarten families to register early. Children must be 5 on or before September 30 to enter kindergarten. No dates are posted.
   - citation: Rye Elementary School - K-4 Registration Forms
   - source: https://www.sau50.org/pages/529d92f9-0099-457a-a9bc-04264e8938b4
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rye
   - note: Page text: "If you are a prospective Kindergarten or Grade 1 family we appreciate you registering early." Phone questions 9:00-2:00 at +1 603 436 4731. Raw copy: raw/districts/batch-8/rye-k4-registration.txt
76. The Salem School District takes registration for new students, including kindergarten, through an online application; its registration page offers "2026-27 Registration (Next Year)" and lists no kindergarten registration dates. No 2027-28 kindergarten registration dates were posted as of November 8, 2026.
   - citation: Salem School District - Join Salem Public Schools (Registration & Enrollment)
   - source: https://sau57.org/join-us
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Salem
   - note: Page text: "New Families K-12 Start a New Student Registration: 2026-27 Registration (Next Year)" Preschool/elementary registration contact: Kathy Graziano (603) 893-7040 option 6. FAQ: children in the 4-year-old Salem Preschool are automatically entered into kindergarten. Raw copy: raw/districts/batch-7/salem-join-us.txt
77. In the Sanborn Regional School District, kindergarten registration is online through AlmaStart, selecting Daniel J. Bakie School, and registrations are processed in the order received. The district asks that new kindergarten registrations be completed by May 1. The registrar can be reached at 603-642-5272 x101.
   - citation: Daniel J. Bakie School - Registration Information
   - source: https://docs.google.com/document/d/1kTAEsgxD1GN7QQpko-mSth1Ni1-3FgAt9NjXqVPL4qE/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Sanborn Regional
   - note: Page text: "Incoming kindergarten registrations are processed in the order received. ... We request that all new kindergarten registrations be completed by May 1st to ensure sufficient time for processing." The document does not give a start date; it lists eligibility for both 2026-27 and 2027-28. Raw copy: raw/districts/batch-5/sanborn-bakie-registration-doc.txt
78. The Seabrook School District registers new kindergarten students at Seabrook Elementary School through an online registration, with a birth certificate and proof of residency; for 2026-27 it held a Kindergarten Information Night on April 21, 2026, where families learned the online registration process. No 2027-28 dates were posted as of November 8, 2026.
   - citation: Seabrook Elementary School - 2026-2027 Kindergarten Information Night flyer
   - source: https://www.sau21.nh.gov/ses/files/documents/2026-2027%20KINDERGARTEN%20INFORMATION%20NIGHT%20FLYER.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Seabrook
   - note: Page text: "Tuesday, April 21, 2026 5:30 p.m. Meet the principals & school staff Explore classrooms and meet the Kindergarten Team Familiarize yourself with the online registration process" Registration page: https://www.sau21.nh.gov/ses/kindergarten-registration ('2026-2027 New Student Registration'). Flyer: current SES preschool students do not need to re-register. Raw copy: raw/districts/batch-7/seabrook-k-info-night-2026-27.txt; raw/districts/batch-7/seabrook-ses-registration.txt
79. In the Shaker Regional School District, families register kindergartners through Belmont Elementary School (603-267-6568) or Canterbury Elementary School (603-783-9944), bringing a copy of the birth certificate and immunization records. The page posts no registration dates for 2026-27.
   - citation: Shaker Regional School District - Kindergarten and Grade One Registration
   - source: https://www.sau80.org/community/kindergarten_and_grade_one_registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Shaker Regional
   - note: Page text: "A copy of the child's birth certificate and immunization records are required for registration. For questions regarding registration, please contact the schools at the following phone numbers: Belmont Elementary School: 603-267-6568 Canterbury Elementary School: 603-783-9944" District-wide registration page: https://www.sau80.org/Student_Registration (not opened). Raw copy: raw/districts/batch-6/shaker-k-registration.txt
80. In the Somersworth School District, kindergarten registration is done through an online registration form linked from the SAU 56 and Idlehurst Elementary School web pages. No registration dates are posted.
   - citation: Somersworth School District - Idlehurst Elementary School page
   - source: https://www.sau56.org/schools/idlehurst_elementary_school
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Somersworth
   - note: Page text: "KINDERGARTEN ONLINE REGISTRATION -> https://sau56sms.powerschool.com/public/formbuilder/form.html?formid=1699711" Quote is the link label and target on the page. Same PowerSchool form is labelled 'NEW STUDENT ONLINE REGISTRATION' on the district home page. Raw copy: raw/districts/batch-6/somersworth-idlehurst.txt
81. In the Stoddard School District, James Faulkner Elementary School holds a kindergarten pre-registration program in the spring; no dates for 2027-28 are posted.
   - citation: James Faulkner Elementary School, Student Registration
   - source: https://www.sau24.org/schools/jfes-us/about-us/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stoddard
   - note: Page text: "The school has a pre-registration program for kindergarten which takes place in the Spring." Raw copy: raw/districts/batch-3/stoddard-registration.txt
82. In the Strafford School District, kindergarten registration for 2026-27 had begun when checked; families contact office@strafford.k12.nh.us, and new families register online through Alma Start or by calling the office at (603) 664-2842. No closing date or 2027-28 dates were posted.
   - citation: Strafford School - Incoming Kindergarten; Student Registration
   - source: https://www.strafford.k12.nh.us/families/incoming-kindergarten
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Strafford
   - note: Page text: "Kindergarten Registration has begun for the 2026-2027 school year!" Registration page: https://www.strafford.k12.nh.us/information/student-registration. Raw copy: raw/districts/batch-2/strafford-incoming-k.txt; raw/districts/batch-2/strafford-registration.txt
83. Stratham Memorial School's registration page says 2026-27 kindergarten registration is open: families complete the online 2026-27 New Student Form and drop registration materials at the main office, Monday-Friday 7:30 a.m.-3:30 p.m. Children must be five by September 30. No dates or 2027-28 information were posted as of November 8, 2026.
   - citation: Stratham Memorial School - Registration
   - source: https://www.sau16.org/pages/a2583520-cc3e-4e9f-8014-9bc948dd6c7b
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stratham
   - note: Page text: "2026-2027 Kindergarten registration is now open. Registration materials can be dropped off at the Main Office at the School Monday-Friday 7:30am-3:30pm." Page also: 'your child must be five years of age by September 30 in order to be eligible for kindergarten.' Raw copy: raw/districts/batch-8/sms-registration.txt
84. The Surry School District runs no schools of its own; Surry kindergartners register in March before their kindergarten year with the school they will attend (elementary children attend Wheelock School in Keene), and families also notify the Surry School Board at schoolboard@surry.nh.gov. Attending another Keene elementary school requires a variance from Keene.
   - citation: Town of Surry - Surry School District
   - source: https://surry.nh.gov/surry-school-district/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Surry
   - note: Page text: "Kindergarteners register in March preceding the kindergarten year. Please also contact the Surry School Board at schoolboard@surry.nh.gov to let us know of your child’s enrollment. Elementary children attend Wheelock School." Children may also apply to the separate Surry Village Charter School kindergarten lottery starting in January (per same page). Raw copy: raw/districts/batch-5/surry-school-district.txt
85. To enroll a new student, including kindergarten, families in Tamworth fill out a new student registration packet and submit it to Kenneth A. Brett School (grades K-8, 881 Tamworth Rd, 603-323-7271); no registration window is posted.
   - citation: SAU 13 - Student Registration
   - source: https://www.sau13.org/home/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Tamworth
   - note: Page text: "Welcome! Please fill out a new student registration packet and submit them to the appropriate school to enroll your child." Registration forms folder: https://drive.google.com/drive/folders/1nOMOKC-6iyXaSQoP0NOJN_UQ_iAxf3Re. Raw copy: raw/districts/batch-7/sau13-student-registration.txt
86. In the Timberlane Regional School District, online enrollment for new kindergarten to grade 12 students for 2026-27 opened March 13, 2026 (January 16, 2026 for preschool and pre-kindergarten), followed by bringing documents to the school registrar. A deposit of $450 for full-day kindergarten was due by April 30, 2026. No 2027-28 dates were posted when checked.
   - citation: Timberlane Regional School District - New Student Enrollment Process
   - source: https://www.timberlane.net/enrollment/student-enrollment/student-enrollment-process
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Timberlane Regional
   - note: Page text: "January 16, 2026, for Preschool and Pre-Kindergarten aged students ... March 13, 2026, for Kindergarten through grade 12 students ... A deposit of $220 for Early Childhood Multiage Programming and $450 for full day Kindergarten is due by April 30th, 2026." Raw copy: raw/districts/batch-2/timberlane-enrollment-process.txt
87. In the Unity School District, families register a student by contacting Unity Elementary School's main office ((603) 542-5888 ext. 8202). No kindergarten registration window or dates were posted when checked.
   - citation: Unity Elementary School - Student Registration
   - source: https://www.sau109.org/111373_1
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Unity
   - note: Page text: "To register your student with the Unity School District, please reach out to [#] Jessica Hiscoe. You can also call the main office directly: (603)-542-5888 ext. 8202" Process only; no window. Raw copy: raw/districts/batch-2/unity-registration.txt
88. In the Wakefield School District, families new to the district pre-enroll their child at Paul School by creating an Alma Start account and uploading documents (birth certificate, immunization record, recent physical and two proofs of residency); the school then contacts the family. No kindergarten registration window or dates were posted when checked.
   - citation: SAU 101 - New Students to Paul School
   - source: https://www.sau101.org/o/sau101/page/new-students-to-paul-school
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wakefield
   - note: Page text: "New Families-if you are new to the Wakefield School District, please create your Alma Start account to register your new student." Process only; no window. Raw copy: raw/districts/batch-2/wakefield-new-students.txt
89. In the Washington School District, families register kindergartners for 2026-27 online at hdsd.powerschool.com; because all kindergartners are in one classroom, screenings are held in the fall. Registration requires immunization records, a birth certificate, a recent physical and proof of residency. No closing date is posted.
   - citation: SAU #34 News, 'Washington Elementary School Kindergarten and Early Learning Group Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Washington
   - note: Page text: "Please register online at https://hdsd.powerschool.com/public/. Because all students are in the same classroom, screenings are conducted in the fall." Contact: Washington Elementary office 603-495-3463. Raw copy: raw/districts/batch-6/sau34-home.txt
90. In the Waterville Valley School District, new students register online through SAU 48's Alma Start system (sau48.almastart.com), following the 'New Student Registration Instructions' linked from the Waterville Valley Elementary School site. No kindergarten registration dates are posted.
   - citation: SAU48 Parent Quick Guide: New Student Registration in Alma Start (linked as 'New Student Registration Instructions' from https://wves.pemibaker.org/)
   - source: https://drive.google.com/file/d/1GMl60FV1qBqR3rRQ5N4fHd9nY04lS_ye/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Waterville Valley
   - note: Page text: "SAU48 | Parent Quick Guide New Student Registration in Alma Start | Page 1 REGISTERING A NEW STUDENT A Parent/Guardian Guide to Alma Start Start here: https://sau48.almastart.com/" Raw copy: raw/districts/batch-6/wves-registration-instructions.txt
91. In the Weare School District, kindergarten registration at Center Woods Elementary School starts as early as October for the following school year; families contact the school at 603-529-4500.
   - citation: Center Woods Elementary School, Student Registration
   - source: https://www.sau24.org/schools/centerwoods/about-us/student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Weare
   - note: Page text: "Registration for Kindergarten starts as early as October for the following school year. Contact CWES at 603-529-4500." General statement; no dated window for 2027-28. Raw copy: raw/districts/batch-3/sau24-centerwoods-reg.txt
92. In the Wentworth School District, families call Wentworth Elementary School before starting digital registration through the Alma system linked from the school website. No kindergarten registration dates are posted.
   - citation: Wentworth Elementary School Parent/Student Handbook 2026-2027
   - source: https://drive.google.com/file/d/17sKnhg4LZQ_bojPYfCtUOpDZHxOxukYf/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wentworth
   - note: Page text: "REGISTRATION: To help us prepare, please call the school before starting digital registration. Families must provide proof of residency during registration. WES has implemented a digital registration system through our student management system called ALMA." Raw copy: raw/districts/batch-6/wentworth-handbook-2627.txt
93. In the Westmoreland School District, kindergarten registration and outreach usually begins in April for the following school year; the school keeps a projected enrollment list and asks parents to tell it if they will enroll a kindergartener (2026-27 handbook). No 2027-28 dates are posted.
   - citation: Westmoreland School Handbook 2026-2027
   - source: https://docs.google.com/document/d/1sn-sMAerMs8FZ2O_lPa4RvCb4nliSgTnc943clpDoBs/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Westmoreland
   - note: Page text: "The school keeps a running projected enrollment list and asks parents to notify the school if they will be enrolling a kindergartener in the next school year. ... Our Kindergarten registration and outreach usually begins in April for the following school year." Phone: Westmoreland School (603) 399-4421. Raw copy: raw/districts/batch-4/westmoreland-school-handbook.txt
94. In the Wilton-Lyndeborough Cooperative School District, kindergarten registration for 2026-27 began Tuesday, March 3, 2026, at Lyndeborough Central School (603-732-9228), which serves Pre-K and kindergarten. No 2027-28 dates are posted yet.
   - citation: Lyndeborough Central School - Kindergarten Registration flyer (linked from https://lcs.sau63.org)
   - source: https://resources.finalsite.net/images/v1772644669/sau63org/a5wzbm9j9hprxsgojpte/25-26LCSKindergartenRegistration.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wilton-Lyndeborough Cooperative
   - note: Page text: "KINDERGARTEN REGISTRATION KICKOFF FOR THE 2026-27 SCHOOL YEAR WILL BEGIN TUESDAY, MARCH 3RD AT LYNDEBOROUGH CENTRAL SCHOOL." Flyer filename says 25-26 but its text is for 2026-27. Raw copy: raw/districts/batch-4/wlc-lcs-k-registration.txt
95. In the Windham School District, new students in grades K-12, including kindergarten, register by downloading the registration packet from the district website and emailing it with the required documents (two proofs of Windham residency, birth certificate, immunization and physical records) to the K-12 registrar. The page posts no registration dates. Golden Brook School held a Kindergarten Discovery Day for incoming kindergartners on May 13, 2026.
   - citation: Windham School District - Grades K-12 Registration Packet
   - source: https://www.windhamsd.org/registration/student_registration/grades_k-12_registration_packet
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windham
   - note: Page text: "To begin, please click on the link below to download the registration packet. After completing the packet, please email it to Diane Smith, along with all the required supporting documentation mentioned above." No kindergarten registration window found. Discovery Day: https://windhamsdgbs.ss18.sharpschool.com/news/what_s_new/kindergarten_discovery_day_ (posted 04/29/2026: 'Wednesday, May 13th from 12:45 PM – 2:30 PM'). Registrar contact dsmith@windhamsd.org, (603) 845-1558 ext. 5840. Raw copy: raw/districts/batch-6/windham-k12-packet.txt
96. Windsor kindergartners register through Hillsboro-Deering Elementary School: for 2026-27, families pre-registered online and picked up a packet at the HDES main office March 30-April 10, 2026.
   - citation: SAU #34 News, '2026-2027 Hillsboro-Deering Elementary School Kindergarten Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windsor
   - note: Page text: "Children must reside in Hillsboro, Deering or Windsor and be 5 yrs. old on or before 9/30/2026. Please pre-register at https://hdsd.powerschool.com/public/ and then pick up a registration packet at the Hillsboro-Deering Elementary School Main Office 3/30/26-4/10/26 between 8am-4pm." Raw copy: raw/districts/batch-6/sau34-home.txt
97. In the Winnisquam Regional School District, online registration for new students for 2026-27 opened on the district website; the page gives no kindergarten-specific dates.
   - citation: Winnisquam Regional School District - Online Registration
   - source: https://www.wrsdsau59.org/en-US/pages/b72deef0-a5af-4ff3-bc75-f08a39e8fb38
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Winnisquam Regional
   - note: Page text: "2026-2027 NEW STUDENT ONLINE REGISTRATION IS NOW OPEN Please follow the instructions below to complete the online registration for your new student for the 26-27 school year." Page does not say when registration opened or closes. Raw copy: raw/districts/batch-6/winnisquam-registration.txt

## district-preschool: Public Preschool Programs by District

- kind: local
- question_type: local_practice
- description: Whether each district runs a preschool program, where, and any posted tuition.

1. Allenstown children ages 3 to 5 with special education needs are served by SAU 53's preschool programs, which accept children from Pembroke, Allenstown, Chichester and Epsom and are located at the old Allenstown Elementary School (30 Main Street, Allenstown); TLC Preschool there also admits some children without identified needs after an April screening. No tuition is posted.
   - citation: SAU 53 - TLC Preschool
   - source: https://sau.sau53.org/pages/76e46815-3441-4987-aa11-2fbd2b55be4b
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Allenstown
   - note: Page text: "SAU 53 preschool programs accept children from the towns of Pembroke, Allenstown, Chichester, and Epsom. SAU 53 preschool programs are located at the old Allenstown Elementary School, 30 Main Street Allenstown, NH." Coordinator Paula Dyrkacz (603) 836-6294 x1. Raw copy: raw/districts/batch-7/sau53-tlc-preschool-page.txt
2. The Alton School District runs a preschool at Alton Central School, with a morning session (7:45 AM-10:40 AM) and an afternoon session (12:05 PM-2:50 PM) on Mondays, Tuesdays, Thursdays and Fridays; it does not meet on Wednesdays. Preschool registration for the next year was marked 'coming soon'. No tuition is posted.
   - citation: Alton Central School - School Hours and Bell Schedule; Preschool Registration page
   - source: https://acs.pmsau.nh.gov/o/acs/page/school-hours-and-bell-schedule
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Alton
   - note: Page text: "PreSchool Hours Preschool is in session: Monday, Tuesday, Thursday, Friday AM session 7:45AM-10:40AM PM session 12:05PM-2:50PM Preschool is not in session on Wednesdays" Preschool registration page https://acs.pmsau.nh.gov/o/acs/page/preschool-registration says 'Preschool Coming Soon'. NH DOE Oct 1 2026: 39 preschoolers at Alton Central School. Hours page section is not dated (K-8 hours on the same page are labeled 2024-25). Raw copy: raw/districts/batch-4/alton-pages.txt
3. The Amherst School District runs the Clark-Wilkins Preschool Program, an inclusive preschool at the Clark building where children with and without disabilities learn together. Children who qualify for special education attend at no cost, and a limited number of tuition-based spaces are offered. Classes meet Monday to Thursday, mornings 7:45-10:45 a.m. or afternoons 11:25 a.m.-2:25 p.m. Tuition for 2026-27 is $2,725 a year, with a $125 non-refundable deposit; families can submit an inquiry form beginning in January.
   - citation: Clark & Wilkins - Preschool Information
   - source: https://sites.google.com/sau39.org/clarkwilkins/academics/preschool-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Amherst
   - note: Page text: "Children who meet New Hampshire’s special education eligibility criteria may attend at no cost. We also offer a limited number of tuition-based spaces for families interested in our preschool program. ... Tuition for the 2026–2027 school year is $2,725 per year. A non-refundable deposit of $125 is required to secure your child’s placement" NH DOE Oct 1 2026 preschool count: 40 (Clark-Wilkins). Amherst policy list also has JFAC Admission and Enrollment of Preschool Students. Raw copy: raw/districts/batch-2/sau39-cw-preschool.txt
4. The Auburn School District runs the Preschool Early Education Program (PEEP) at Auburn Village School, an integrated preschool for children ages 3 to 5 with and without disabilities, aiming for a 50:50 ratio of peer models to students with IEPs. It meets Monday-Friday, 8:15-10:45 a.m. Peer models must be Auburn residents, three or four years old by September 30, and toilet trained; a waitlist opens the first school day in January before the school year, followed by a spring screening. Peer model tuition is charged monthly; the page lists '5 Day Program only $300.00'.
   - citation: Auburn Village School, Preschool Early Education Program (PEEP) (updated 6/10/25; PEEP Handbook 26-27 linked)
   - source: https://auburn.sau15.net/student-services/preschool-early-education-program-peep/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Auburn
   - note: Page text: "Peer model participation is on a monthly tuition basis. ... Tuition: Tuition will be a revenue for the district. 5 Day Program only $300.00" The $300.00 figure is stated next to 'monthly tuition basis'; the page does not say 'per month' in the same line. NH DOE Oct 1, 2026: 11 at Auburn Village School. Raw copy: raw/districts/batch-3/auburn-peep.txt
5. The Barnstead School District runs a preschool at Barnstead Elementary School. In 2026-27 it meets Monday, Tuesday, Thursday and Friday, with an AM session from 7:45 to 10:15 and a PM session from 11:45 to 2:15; it does not meet on Wednesdays. The preschool registration page said 'Preschool Coming Soon', and no tuition was posted.
   - citation: Barnstead Elementary School - School Hours and Bell Schedule
   - source: https://bes.pmsau.nh.gov/o/bes/page/school-hours-and-bell-schedule
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barnstead
   - note: Page text: "Preschool Hours: Preschool is in session: Monday, Tuesday, Thursday, Friday AM session runs 7:45- 10:15 am PM session runs 11:45- 2:15 pm. Preschool is not in session on Wednesdays" NH DOE counted 16 preschool children at Barnstead Elementary on Oct 1, 2026. Raw copy: raw/districts/batch-5/barnstead-bes-school-hours-and-bell-schedule.txt; raw/districts/batch-5/barnstead-bes-preschool-registration.txt
6. The Barrington School District runs the SAU 74 Integrated Preschool Program at the Early Childhood Learning Center for Barrington children ages 3 to 5. It serves children with identified disabilities at no cost, together with typically developing children. The 3-year-old program meets mornings (8:25-11:00) and the 4-year-old program afternoons (12:00-2:45), Monday through Thursday. Tuition is $245 per month.
   - citation: SAU 74 Preschool Program
   - source: https://eclc.sau74.org/for_parents/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barrington
   - note: Page text: "The 3-Year Old Program: Takes place in the morning from 8:25-11:00 The 4-Year Old Program: Takes place in the afternoon from 12:00-2:45 The cost is $245 monthly." Page: 'We have 3 classrooms, each running a morning and afternoon session Monday-Thursday.' Special education services 'are provided at no cost to families.' School year of the $245 fee not stated. NH DOE Oct 1 2026: 43 preschoolers. Raw copy: raw/districts/batch-1/barrington-eclc-preschool.txt
7. In the Bartlett School District, Josiah Bartlett Elementary School serves students from Early Childhood Education and kindergarten through the middle school grades. The page does not give preschool details or tuition.
   - citation: Josiah Bartlett Elementary School home
   - source: https://jbes.sau9.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bartlett
   - note: Page text: "Students range from Early Childhood Education and Kindergarten through the Elementary and Middle School grades." NH DOE Oct 1 2026: 16 preschoolers at Josiah Bartlett Elementary. Raw copy: raw/districts/batch-1/sau9-jbes-home.txt
8. NH Department of Education counted 7 preschool children enrolled in the Bath School District's schools on October 1, 2026 (Bath Village School (7)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bath
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found. NH DOE Oct 1 2026: 7 preschoolers at Bath Village School.
9. The Bedford School District runs the Bedford Early Education Program (BEEP), an inclusive preschool for three- and four-year-olds with and without special needs, which moved to Riddle Brook School for 2026-27. Three-year-olds attend two mornings a week; four-year-olds attend Monday-Friday mornings or Monday-Thursday afternoons. Tuition for typically developing children in 2026-27 is $1,450 a year for 2 days a week, $1,800 for 3 days, $2,150 for 4 days and $2,500 for 5 days, with a 90% discount for families who qualify for free or reduced-price lunch.
   - citation: Riddle Brook School, BEEP Program page, with 2026-2027 BEEP registration letter (Feb 16, 2026) and tuition agreement
   - source: https://sites.google.com/bedfordnhk12.net/rbs/beep-program
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bedford
   - note: Page text: "2 $1,450 $145 $ 72.50 ... 3 $1,800 $180 $ 90.00 4 $2,150 $215 $107.50 5 $2,500 $250 $125.00 ... Families who qualify for free/reduced lunch for 2026-2027 will receive a 90% discount." Letter: registration began Feb 18, 2026; class assignment by age as of September 30, 2026; children enroll as 'typical role models'. NH DOE Oct 1, 2026 preschool count: 71 at Riddle Brook School. Raw copy: raw/districts/batch-3/bedford-beep.txt; raw/districts/batch-3/bedford-beep-letter-2026-27.txt; raw/districts/batch-3/bedford-beep-tuition-2026-27.txt
10. The Bethlehem School District has a preschool class at Bethlehem Elementary School (registration covers PreK-6). The school said its 2025-26 preschool class was full and kept a rolling waitlist. No tuition is posted.
   - citation: Bethlehem Elementary School - New Student Registration (PreK - 6th Grade)
   - source: https://bethlehem.k12.nh.us/en-US/new-student-registration-2354a55a
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bethlehem
   - note: Page text: "Please be advised that the 2025-2026 Preschool Class is FULL. Contact Nicole Kerstetter at the email below to put your child's name on the rolling waitlist." Handbook 2025-26 gives preschool arrival time 8:00. NH DOE Oct 1 2026: 6 preschoolers at Bethlehem Elementary School. Raw copy: raw/districts/batch-4/bethlehem-pages.txt
11. The Bow School District has a public preschool: NH DOE counted 20 children at Bow Preschool on October 1, 2026, and the Town of Bow's schools page lists a special education preschool at Bow High School. No program details or tuition were found on the SAU 67 site.
   - citation: Town of Bow - Schools page; NH DOE iPlatform Preschool Enrollments 2026-2027 (raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx)
   - source: https://bownh.gov/257/Schools
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bow
   - note: Page text: "Bow High School (Grades 9-12 & Special Ed Preschool)" Town of Bow's separate Celebrating Children Preschool is a town recreation program, not the school district's. An NH DOE 2023 letter about Bow's preschool program could not be retrieved (403, no Wayback copy). Raw copy: raw/districts/batch-5/bow-town-schools-page.txt
12. The Brentwood School District runs a community preschool at Swasey Central School for children ages 3 to 5, with community peers and children with specialized learning needs; children must turn 3 by September 30. Tuition for community peers is $1,300 per year, billed at the start of the school year and in January, with tuition assistance considered for families in need.
   - citation: Swasey Central School - Preschool
   - source: https://www.sau16.org/pages/dae2e181-d7a7-4d85-9f4d-066eac5debfd
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brentwood
   - note: Page text: "Tuition for community peers is $1300 per year. Families are billed at the start of the school year and again in January." School year for the tuition not stated on the page. Community peers must be daytime toilet trained. Raw copy: raw/districts/batch-8/scs-preschool.txt
13. The Brookline School District runs an integrated preschool at Richard Maghakian Memorial School for children ages 3 to 5, with and without identified needs, Monday to Thursday in two morning sessions and one afternoon session. Typically developing children attend on a tuition basis, $270 a month paid in 10 monthly installments. Separate waitlists are kept for 3- and 4-year-olds, and enrollment for the next school year is completed in January.
   - citation: Richard Maghakian Memorial School - Preschool Program
   - source: https://www.myrmms.org/academic-programs/preschool-program
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brookline
   - note: Page text: "Typically developing students will be enrolled in our preschool programs on a tuition basis. Tuition is $270 for the programs. Tuition will be paid in 10 equal installments, collected monthly." NH DOE counted 24 preschool children at RMMS on Oct 1, 2026. Raw copy: raw/districts/batch-5/brookline-rmms-preschool.txt
14. Campton Elementary School has a preschool class with its own web page (CES Preschool), linked as 'Pre-K' from the school site. No schedule, eligibility or tuition is posted.
   - citation: CES Preschool class page
   - source: https://sites.google.com/pemibaker.org/ces-preschool/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Campton
   - note: Page text: "Welcome to our preschool web page. Here you will find our weekly newsletter, upcoming dates, teacher & school contact information, and academic focus points." NH DOE Oct 1 2026 report shows no preschool enrollment for Campton. Raw copy: raw/districts/batch-6/ces-prek.txt
15. The Chester School District has a pre-kindergarten (preschool) class at Chester Academy, with one preschool teacher. No tuition, schedule or eligibility details are posted.
   - citation: Chester Academy - Preschool
   - source: https://ca.sau82nh.gov/grade_level_teams/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chester
   - note: Page text: "The Pre- Kindergarten teacher will contact you weekly via email about classroom happenings and curriculum. ... Preschool Teacher Mrs. Johnston" NH DOE Oct 1 2026: 31 preschoolers at Chester Academy. Raw copy: raw/districts/batch-4/chester-ca-preschool.txt
16. Chichester children ages 3 to 5 with special education needs are served by SAU 53's preschool programs, which accept children from Pembroke, Allenstown, Chichester and Epsom; they include TLC Preschool at the old Allenstown Elementary School, which also admits some children without identified needs after an April screening. No tuition is posted.
   - citation: SAU 53 - TLC Preschool
   - source: https://sau.sau53.org/pages/76e46815-3441-4987-aa11-2fbd2b55be4b
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chichester
   - note: Page text: "SAU 53 preschool programs accept children from the towns of Pembroke, Allenstown, Chichester, and Epsom." Coordinator Paula Dyrkacz (603) 836-6294 x1. Raw copy: raw/districts/batch-7/sau53-tlc-preschool-page.txt
17. NH Department of Education counted 14 preschool children enrolled in the Colebrook School District's schools on October 1, 2026 (Colebrook Academy and Elementary School (E) (14)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Colebrook
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: SAU 7 site (sau7.org, SchoolBlocks) checked: home, Policies, About Our School Boards. Menus for district/school pages did not render as links; no registration, preschool, warrant, annual meeting or tuition pages found. A search hit for 'colebrookschool.org' turned out to be Colebrook, Connecticut, and was discarded. NH DOE Oct 1 2026 preschool report lists 14 preschoolers in this district.
18. The Concord School District runs the Concord Developmental Preschool for children ages 3 to 5 at Abbot-Downing, Beaver Meadow and Mill Brook schools, an integrated program for typically developing children and children with special needs. For 2026-27 the 3-year-old program meets Monday, Wednesday and Thursday 8:30-10:30 and the 4-year-old program Monday, Wednesday and Thursday 12:30-3:00. Tuition is required for typically developing children (amount not posted), and transportation is not provided for tuition students.
   - citation: Concord School District - Early Childhood & Preschool Home
   - source: https://sau8.org/early-childhood-preschool-home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Concord
   - note: Page text: "The Concord Developmental Preschool is a regular early childhood program providing the opportunity for typically developing three and four-year-old children and children identified as having special needs to learn, play and grow together. ... Tuition is required for typically developing children. Transportation is not provided for tuition students." Page says '4-year-old program – Monday, Wednesday and Thursday mornings 12:30-3:00 (must be 4 by 9/30/26)'. The school hours page shows slightly different preschool day patterns by school. No tuition amount found. Raw copy: raw/districts/batch-5/concord-preschool-home.txt
19. The Contoocook Valley (ConVal) School District runs First Friends Preschool, an inclusive program for three- and four-year-olds with varying abilities, at Antrim, Greenfield, Hancock and Peterborough elementary schools. Three-year-olds attend three mornings a week (8:45-11:45 a.m.); four-year-olds attend 4.5 days a week, full days Monday, Tuesday, Thursday and Friday (8:45 a.m.-3:00 p.m.) with an 11:45 a.m. dismissal on Wednesday.
   - citation: ConVal, First Friends Preschool
   - source: https://conval.edu/en-us/first-friends-preschool-c6ccfff3
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Contoocook Valley
   - note: Page text: "Students in our program for three-year olds attend three mornings a week from 8:45 to 11:45 am. Students in our program for four-year olds attend 4.5 days a week, for a full day Mon, Tues, Thu, Fri from 8:45 am to 3:00 pm, with a 11:45 am dismissal on Wed." No tuition posted on this page. A separate 'Preschool for All' page (conval.edu/en-US/preschool-for-all-5eea00e9) rendered with no body text on 2026-11-08. NH DOE Oct 1, 2026: 94 preschool students across the four schools. Raw copy: raw/districts/batch-3/conval-first-friends.html
20. The Cornish School District runs a half-day (8 a.m.-12 p.m.) pre-kindergarten program at Cornish Elementary School for children who are 3 or 4 by September 30, capped at 16 children. Places go first to resident 4-year-olds, then resident 3-year-olds, then children tuitioned from other districts, then children of staff (2025-26 notice). No tuition amount is posted.
   - citation: Cornish Elementary School - PreK-K Pre-Enrollment Statement 2025-2026
   - source: https://www.cornishschool.org/ourpages/auto/2024/6/26/50870748/PreK-K%20Pre-Enrollment%20Statement%202025-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Cornish
   - note: Page text: "To register for our half-day (8 am-12 pm) Pre-Kindergarten program, children must be either 3 or 4 years old on or before September 30, 2025. Please understand that there is a cap of 16 children in this program." NH DOE Oct 1 2026 preschool count: 16. Raw copy: raw/districts/batch-2/cornish-prek-k-statement-2025-26.txt
21. The Croydon School District runs a half-day preschool at Croydon Village School for children who are 4 on September 30, Monday to Thursday, 8:00 to 11:30, priced at $268 per week, with no residency requirement and no transportation. Applications open January 1; places go first-come, first-served to siblings of current students, then other Croydon children, then non-Croydon children, with families notified by March 31.
   - citation: Croydon School District - Program for Early Learners at Croydon Village School (Our Program at a Glance)
   - source: https://croydonsd.org/cvs/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Croydon
   - note: Page text: "Price $268 per Week No Charge Residency Requirement No Requirement Croydon Only Transportation Not Provided" Table columns are PRESCHOOL then KINDERGARTEN ('$268 per Week' preschool, 'No Charge' kindergarten). Enrollment rules from https://croydonsd.org/cvs/enrollment/ (raw croydon-cvs-enrollment.txt). Page shows no school year for the price. NH DOE Oct 1 2026: Croydon Village School 2 preschoolers. Raw copy: raw/districts/batch-6/croydon-cvs.txt
22. The Deerfield School District runs the DCS Preschool Program at Deerfield Community School for Deerfield residents: a class for 3- and 4-year-olds on Tuesday and Thursday and a pre-kindergarten class for 4- and 5-year-olds on Monday, Wednesday and Friday, each in a morning or afternoon session. Children must be 3 (or 4 for pre-K) by September 30; space is limited, and sign-ups are held each March. No tuition is posted.
   - citation: Deerfield Community School - Pre-School
   - source: https://dcs.sau53.org/pages/b1863d35-f7dd-4f08-8c61-fb5eedb2a6f9
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Deerfield
   - note: Page text: "Our preschool program groups student by age. The program for 3- and 4-year-olds takes place two days a week and the program for 4 and 5-year-olds is three days a week. Each class is available in either morning or afternoon sessions." Contact JoAnna Sarrasin jsarrasin@sau53.org. NH DOE counted 33 preschool children at Deerfield on Oct 1, 2026. Raw copy: raw/districts/batch-7/sau53-dcs-preschool.txt
23. The Derry Cooperative School District runs the Derry Early Education Program (DEEP), an inclusive preschool for three- and four-year-olds at Gilbert H. Hood Middle School that serves typically developing children and children with IEPs. Registration gives priority to children with IEPs; others are enrolled as space allows. In 2026-27 sessions run 8:30-11:00 a.m. and 12:20-2:50 p.m.
   - citation: Derry Early Education Program, Program Overview
   - source: https://www.sau10.nh.gov/schools/deep/program-overview
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Derry Cooperative
   - note: Page text: "The program utilizes an inclusion model (typically developing children and those who require an individualized education plan) ... Programs are held in a space designed specifically for preschool education located at Gilbert H. Hood Middle School." Tuition not found on the DEEP pages. NH DOE Oct 1, 2026: 91 preschool students at Derry Early Education Program. Raw copy: raw/districts/batch-3/derry-deep-overview.txt; raw/districts/batch-3/derry-school-hours.txt; raw/districts/batch-3/derry-k-registration.txt
24. The Dover School District runs the Dover District Preschool Program at Woodman Park School, an integrated preschool for children ages 3 to 5 with and without disabilities. Children without disabilities attend on a tuition basis chosen by lottery; for 2026-27 tuition was $55 a month for two half-day sessions a week and $82 a month for three (morning 8:15-10:45 or afternoon 11:15-1:40), applications were due March 11, 2026, and parents provide transportation.
   - citation: Woodman Park Elementary School - Preschool; Application for Dover District Preschool Program Tuition Enrollment 2026-2027 (https://4.files.edl.io/d6d7/02/10/26/131649-b7d6fdf5-df9e-47a9-82ca-c487b7a56e08.pdf)
   - source: https://wps.sau11.nh.gov/apps/pages/index.jsp?uREC_ID=1423700&type=d
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dover
   - note: Page text: "2 half days a week $55.00 ... 3 half days a week $82.00 ... *AM Session- 8:15-10:45* *PM Session 11:15-1:40* Transportation must be provided by parents" Page: 'integrated Preschool that addresses the developmental needs of children with and without disabilities'; 'entered into the lottery for school year 2026-2027'. Raw copy: raw/districts/batch-8/dover-wps-preschool.txt; raw/districts/batch-8/dover-preschool-tuition-2026-27.txt
25. The East Kingston School District does not run its own preschool program: its page says that, because of small enrollment, East Kingston Elementary has no in-house preschool, and preschoolers who receive special education services are served through community partners (such as the Exeter Developmental Preschool).
   - citation: East Kingston Elementary School - Preschool
   - source: https://www.sau16.org/pages/4ad03979-d941-4368-8d6d-8130591fd815
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district East Kingston
   - note: Page text: "Due to the small size of enrollment, East Kingston Elementary does not have an in-house preschool program." SAU 16 Preschool Coordinator: Karen Ringuette, 603-775-8644. Raw copy: raw/districts/batch-8/eks-preschool.txt
26. The Epping School District has an integrated developmental preschool program; children must be the appropriate age for the program by September 30 of the year they enter, and the school board sets the age span each year (Policy JEB). No tuition or schedule is posted.
   - citation: Epping School District Policy JEB - Age of Attendance and Entrance
   - source: https://www.sau14.org/school-board/files/documents/JEB%20-%20Age%20of%20Attendance%20and%20Entrance.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epping
   - note: Page text: "Preschool - Any child entering the integrated developmental preschool program shall be the appropriate age for the program by September 30 of the year of entering school. The School Board shall annually determine the chronological age span of children serviced in this program." NH DOE Oct 1 2026: 44 preschoolers at Epping Elementary School. 2025 annual report mentions 'the Preschool' at EES. Raw copy: raw/districts/batch-4/epping-policy-jeb.txt
27. Epsom children ages 3 to 5 with special education needs are served by SAU 53's preschool programs, which accept children from Pembroke, Allenstown, Chichester and Epsom; they include TLC Preschool, a special education preschool at the old Allenstown Elementary School, which also admits some children without identified needs after an April screening. No tuition is posted.
   - citation: SAU 53 - TLC Preschool
   - source: https://sau.sau53.org/pages/76e46815-3441-4987-aa11-2fbd2b55be4b
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epsom
   - note: Page text: "SAU 53 preschool programs accept children from the towns of Pembroke, Allenstown, Chichester, and Epsom." Coordinator Paula Dyrkacz (603) 836-6294 x1. Raw copy: raw/districts/batch-7/sau53-tlc-preschool-page.txt
28. The Exeter School District runs the Exeter Developmental Preschool at 13 School Street, an inclusive program for Exeter children ages 3 to 5 with typical and specialized learning needs. Its page lists a morning session for 3-year-olds (9:00-11:30 a.m.) and an afternoon session for 4-year-olds (12:30-3:00 p.m.), says a small tuition is charged with tuition assistance available, and says only children living in Exeter can be accepted. No tuition amount is posted.
   - citation: SAU 16 - Exeter Developmental Preschool
   - source: https://www.sau16.org/pages/67aaeb1d-1f58-4e97-9b84-27597c4a762e
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Exeter
   - note: Page text: "We charge a small tuition for our preschool program. To inquire about tuition assistance, please reach out to our principal, Beth Cadorette." Page also: 'At this time we can only accept children residing in Exeter.' The Main Street School preschool page (https://www.sau16.org/pages/56996e9f-3258-45a8-b294-4d701725d909) describes a two-day-a-week program (Mon/Thu or Tue/Fri, 9:00-11:30 or 12:00-2:30); the two pages' schedules differ. NH DOE counted 31 preschool children at Main Street School on Oct 1, 2026. Raw copy: raw/districts/batch-8/sau16-exeter-dev-preschool.txt; raw/districts/batch-8/mss-preschool.txt
29. NH Department of Education counted 68 preschool children enrolled in the Fall Mountain Regional School District's schools on October 1, 2026 (Alstead Primary School (17); Charlestown Primary School (27); Walpole Primary School (24)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Fall Mountain Regional
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on the SAU site. NH DOE Oct 1, 2026 preschool enrollment shows 68 students at Alstead, Charlestown and Walpole primary schools (statewide source held by coordinator).
30. The Farmington School District runs a preschool (pre-K) program at Valley View Community School, with morning and afternoon sessions (drop-off at 8:00 a.m. for AM Pre-K and 11:30 a.m. for PM Pre-K), according to its 2025-2026 student and family handbook. No tuition or enrollment details were found.
   - citation: Farmington School District Student Family Handbook 2025-2026
   - source: https://www.sau61.org/files/documents/Student%20Family%20Handbook%202025-2026%20Together.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Farmington
   - note: Page text: "Drop-off times: 8:00 AM for AM Pre-K, 11:30 AM for PM Pre-K." Handbook also says Middleton's departure in 2015 allowed room to expand the Preschool and Kindergarten programs at Valley View. NH DOE Oct 1 2026 preschool count: 22 (Valley View Community School). Raw copy: raw/districts/batch-2/farmington-handbook-2025-26.txt
31. NH Department of Education counted 35 preschool children enrolled in the Franklin School District's schools on October 1, 2026 (Paul A. Smith School (35)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Franklin
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found in site navigation. NH DOE Oct 1 2026 preschool report lists 35 preschoolers at Paul A. Smith School.
32. Freedom children can attend the SAU 13 preschool program at Madison Elementary School, open to children who turn three by September 30, 2026 and live in Freedom, Madison or Tamworth. Sessions are half day (9:00-11:45) or full day (9:00-3:00); tuition for children without an identified disability is $11.50 per day for half day and $23.00 per day for full day.
   - citation: SAU 13 - Preschool Program
   - source: https://www.sau13.org/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Freedom
   - note: Page text: "Children turning three by September 30, 2026, residing in SAU #13 towns (Freedom, Madison, or Tamworth) are eligible for this program." Raw copy: raw/districts/batch-7/sau13-preschool.txt
33. The Fremont School District runs the Ellis Preschool Program, an integrated preschool for children ages 3 to 5. Children with special needs attend free; other Fremont children are chosen by lottery and pay a fee (amount not posted). There is a morning session (8:30-11:00 a.m., Monday, Tuesday, Thursday and Friday) and two afternoon sessions (12:30-3:05), each with up to 12 children; preschool does not meet on Wednesdays. A 2026-27 preschool application is posted.
   - citation: Fremont Preschool Information Flyer (linked from https://www.sau83.org/page/preschool/)
   - source: https://aptg.co/gX7TRn
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Fremont
   - note: Page text: "We are an integrated preschool program for children ages 3 to 5. ... These children are chosen in a lottery and have the opportunity to enroll in the preschool program for a fee." Flyer is an image PDF; quote transcribed by hand. School hours page gives AM preschool 8:20-11:30 and PM 12:30-3:05 (slightly different morning times). Contact: Special Services (603) 895-2511 x551. NH DOE Oct 1 2026: 18 preschoolers at Ellis School. Raw copy: raw/districts/batch-4/fremont-preschool-flyer.pdf; raw/districts/batch-4/fremont-scans-transcription.txt
34. The Goffstown School District runs the Glen Lake Preschool Program at Glen Lake School, a developmental program for three- and four-year-olds where children with and without special needs learn together. Children eligible for special education attend without charge; typically developing "role model" peers pay tuition (amount not posted), apply with an on-site visit, are accepted by late March for the following September, and a lottery is used if there are more applicants than spots. Sessions run 8:30-10:55 a.m. or 12:30-2:55 p.m., Monday through Thursday (2025-26 program description), and parents transport peer students.
   - citation: Glen Lake Preschool Program 25-26 (PDF)
   - source: https://www.sau19.org/attachments/article/32/Glen%20Lake%20Preschool%20Program%2025-26.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Goffstown
   - note: Page text: "The Glen Lake Preschool Program is a developmental program for three- and four-year-olds where children with and without special needs have the opportunity to play and learn together." Tuition is stated in the principal's message: 'for typically developing peers, who pay tuition to attend' and 'For information about preschool for typically developing students (tuition based), please contact the school office at (603)497-3550.' No dollar amount posted. PDF quote on charges: 'Children who meet the New Hampshire standards for special education are eligible to attend the program without charge.' Raw copy: raw/districts/batch-7/goffstown-preschool-25-26.txt; raw/districts/batch-7/goffstown-glenlake-principals-message.txt
35. In the Governor Wentworth Regional School District, preschool children who may need special education receive services with non-disabled peers in public or local private preschools or day care centers, according to Ossipee Central School's preschool page. NH DOE counted 42 preschool children in the district's schools on October 1, 2026 (New Durham Elementary 10, Ossipee Central 32). No tuition or enrollment details for other children were found.
   - citation: Ossipee Central School - PreSchool
   - source: https://ossipeecentralschool.sau49nh.gov/our-school/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Governor Wentworth Regional
   - note: Page text: "Preschool children who may require special education receive services with non-disabled peers in public or local private preschools, or day care centers. Related services may be provided as specified in the child's IEP." New Durham School has a 'Little Wildcats (Pre-K & K)' page with no text content. NH DOE preschool count from iPlatform Preschool Enrollments 2026-27 (raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx). Raw copy: raw/districts/batch-5/gwrsd-ocs-preschool.txt
36. The Grantham School District runs a part-time public preschool at Grantham Village School for Grantham residents ages 3 to 5, with priority for children with or at risk for special education needs and remaining spaces for peer models. In 2026-27, 3-year-olds meet Monday to Thursday 8:30-11:15 and 4-year-olds Monday to Thursday 12:00-3:15. Peer-model tuition is $1,207 a year for PK3 and $1,420 a year for PK4; children who qualify for free lunch attend at no cost and those who qualify for reduced lunch at 50%. Screenings are in March and placements in April; both classes were full for 2026-27.
   - citation: Grantham Village School - Preschool
   - source: https://www.gvshawks.org/apps/pages/index.jsp?uREC_ID=3298781&type=d&pREC_ID=2578756
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Grantham
   - note: Page text: "PK3 tuition: $1,207.00/year, which equates to $8.50/day or $120.70/month PK 4 tuition: $1,420.00/year, which equates to $10/day or $142/month" NH DOE counted 23 preschool children at Grantham Village School on Oct 1, 2026. Raw copy: raw/districts/batch-5/grantham-preschool.txt
37. The Greenland School District does not have its own preschool listed; Greenland children ages 3 to 5 are eligible for the SAU 50 Community Preschool at Rye Elementary School, an inclusive half-day program (2026-27 tuition $200 a month for two sessions a week or $400 for four, September-June).
   - citation: SAU 50 Community Pre-School
   - source: https://www.sau50.org/pages/3051f5d8-1184-40ce-95bf-5c7fef95c2c6
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Greenland
   - note: Page text: "Preschool-aged students, ages 3 to 5) who live in any of our SAU 50 towns (Greenland, New Castle, Newington, and Rye) are eligible to attend." 'Does not have its own preschool listed' is based on the SAU 50 schools overview, which lists preschools only at Rye Elementary and Newington Public School. Raw copy: raw/districts/batch-8/sau50-preschool.txt
38. The Hampstead School District runs the T.E.E.C.H. preschool program at Hampstead Central School for children ages 3 to 5, including children with special needs and typical peer models; families do not have to live in Hampstead. Four groups each meet four days a week, mornings 9:00-11:35 or afternoons 12:50-3:20. The page lists a total program cost of $2,000 for 2024-25 (tuition $1,800, or 10 monthly payments of $180, plus a non-refundable $200 registration fee), with needs-based reductions.
   - citation: Hampstead Central School - TEECH Preschool Program
   - source: https://hcs.hampsteadschools.net/o/hcs/page/preschool-program
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampstead
   - note: Page text: "The total program cost is $2000 for the 2024-25 school year. The tuition will be $1800 or 10 monthly payments of $180." Tuition shown is for 2024-25; no newer figure on the page. 'you do not have to be a town resident to enroll your child in our preschool program.' Raw copy: raw/districts/batch-8/hampstead-teech.txt
39. The Hampton School District runs the Centre School Community Preschool, an inclusive program for Hampton children ages 3 to 5. It is a 2.5-hour program that meets four days a week (Monday-Thursday), with morning or afternoon sessions; space is limited and children are enrolled as space allows during the year. No tuition is posted.
   - citation: Centre School - Preschool Information
   - source: https://centre-school.sau90.org/o/centre-school/page/preschool-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton
   - note: Page text: "Hampton children ages 3-5 are eligible for this 2.5 hour program, which meets 4 days/week (Mon-Thurs) with morning or afternoon sessions available." Contact: Lauren Young, Centre School, 603-926-8706. Linked Google Site (https://sites.google.com/sau90.org/centre-preschool/childfind-preschool) has no tuition either. Raw copy: raw/districts/batch-8/hampton-centre-preschool.txt
40. The Hampton Falls School District runs the Tiger Cub Preschool at Lincoln Akerman School for children who are three or four by September 30, 2026: morning (8:30-11:00) and afternoon (12:15-2:45) classes Monday through Thursday, with an extra Friday afternoon "Get Ready for Kindergarten" session for 4-year-olds. Tuition for 2026-27 is $2,700 a year for the 3-year-old program and $3,375 for the 4-year-old program; applications were due March 2, 2026, with a lottery on March 6, 2026 if needed.
   - citation: Lincoln Akerman School - Tiger Cub Preschool Program information (2026-2027)
   - source: https://docs.google.com/document/d/1E3JtT3xDR5sK3sFiEEKQYpr9KbZmtu22hXVdopT-qy4/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton Falls
   - note: Page text: "Tuition for the preschool programs are $2700 (3 year old program) per year and $3375 (4 year old program) per year." Linked from https://www.sau21.nh.gov/las/about-las/preschool. Children must be fully toilet trained. The document's second line says 'accepting applications for the 2025-2026 school year' but its heading and dates are for 2026-2027. Contact BettyAnne Binette 603-926-2539 x302. Raw copy: raw/districts/batch-7/hamptonfalls-las-preschool-info.txt; raw/districts/batch-7/hamptonfalls-las-preschool.txt
41. NH Department of Education counted 40 preschool children enrolled in the Haverhill Cooperative School District's schools on October 1, 2026 (Woodsville Elementary School (40)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Haverhill Cooperative
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on SAU 23 or Woodsville Elementary site. NH DOE Oct 1 2026 preschool report lists 40 preschoolers at Woodsville Elementary School.
42. NH Department of Education counted 19 preschool children enrolled in the Henniker School District's schools on October 1, 2026 (Henniker Community School (19)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Henniker
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found. NH DOE Oct 1, 2026: 19 preschool students at Henniker Community School (statewide source).
43. NH Department of Education counted 9 preschool children enrolled in the Hill School District's schools on October 1, 2026 (Jennie D. Blake School (9)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hill
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page; the 2021-22 handbook lists a 'Pre-K & Kindergarten' teacher. NH DOE counted 9 preschool children at Jennie D. Blake School on Oct 1, 2026.
44. The Hillsboro-Deering Cooperative School District runs an integrated preschool at Hillsboro-Deering Elementary School, with places filled by lottery. For 2026-27, children living in Hillsboro, Deering or Windsor who would be three or four on or before September 30, 2026 were eligible; families pre-registered online and picked up packets March 30-April 10, 2026, and placements were announced by the end of June. No tuition is posted.
   - citation: SAU #34 News, '2026-2027 Hillsboro-Deering Elementary School Integrated Preschool Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hillsboro-Deering Cooperative
   - note: Page text: "Children who reside in the towns of Hillsboro, Deering or Windsor and who will be three or four years of age on or before September 30, 2026 are eligible for the preschool lottery." NH DOE Oct 1 2026: Hillsboro-Deering Elementary 46 preschoolers. Raw copy: raw/districts/batch-6/sau34-home.txt
45. The Hinsdale School District runs the Hinsdale Preschool at Hinsdale Elementary School. For 2026-27 it offers a three-year-old program (Tuesday-Thursday, 8:30-11:00), a half-day four-year-old program (Monday-Friday, 12:30-3:20) and a full-day four-year-old program (Monday-Friday, 8:30-3:20). Monthly tuition for regular education students is $200 for full day, $100 for the half-day four-year-old program and $60 for the three-year-old program, with reduced and free rates tied to lunch eligibility; children with IEPs attend at no cost. Places are limited and chosen by lottery.
   - citation: Hinsdale Elementary School Student Handbook 2026-2027, 'The Hinsdale Preschool' (linked from https://www.hnhsd.org/?page_id=4363)
   - source: https://www.hnhsd.org/wp-content/uploads/2026/08/HES-Student-Handbook-2026-2027-2.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hinsdale
   - note: Page text: "-5 full day 4-year-old option -Nap time and lunch is built in -Cost: $200/$170 Reduced/$120 Free MONTHLY" 'Students who receive special education services through an IEP attend at no cost'; 'entry into the programs is decided by lottery'. Half-day PM 4-year-old: $100/$85/$60; AM 3-year-old: $60/$51/$36 monthly. Raw copy: raw/districts/batch-8/hinsdale-hes-handbook-2026-27.txt
46. The Hollis School District runs a preschool program at Hollis Primary School, Monday to Thursday in three classes across two daily sessions. The cost is $270 a month for typically developing students; families join a waitlist to register.
   - citation: Hollis Primary School - Preschool Program
   - source: https://www.myhps.org/learning/preschool-program-1
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hollis
   - note: Page text: "Our program runs Monday- Thursday, taking place in three classes across two daily sessions. ... The cost is $270/monthly for typically developing students only." Page describes it as the Hollis Early Learning Program; services include speech and language therapy. NH DOE counted 21 preschool children at Hollis Primary on Oct 1, 2026. Raw copy: raw/districts/batch-5/hollis-hps-preschool.txt
47. The Hooksett School District runs the Hooksett Early Learning Program (HELP) at Fred C. Underhill School, a preschool coordinated by the special education department for children ages three to five with special needs; children who do not need specialized instruction may attend on a tuition basis, chosen by lottery. The program has morning and afternoon sessions.
   - citation: Hooksett Early Learning Program website (linked from Underhill School Preschool page)
   - source: https://sites.google.com/sau15.net/preschool/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hooksett
   - note: Page text: "The Hooksett Early Learning Program (HELP) is an Early Childhood Program coordinated by the Special Education Department servicing children from the ages of three to five with special needs. Children that do not require specialized instruction may attend on a tuition basis, through a lottery system." Tuition amount not stated on the site or in the program guide PDF. Calendar on the site mentions AM and PM preschool. NH DOE Oct 1, 2026: 25 at Fred C. Underhill School. Raw copy: raw/districts/batch-3/hooksett-preschool-site.txt; raw/districts/batch-3/hooksett-preschool-guide.txt
48. The Hopkinton School District runs an early childhood preschool program at Harold Martin School, which serves grades preschool through 3; the program also holds annual Child Find screenings for children ages three to five. No tuition is posted.
   - citation: Hopkinton School District - District Profile; Harold Martin School Handbook 2025-2026
   - source: https://www.hopkintonschools.org/pages/02cfab42-fbab-4117-a94a-b9387c60f172
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hopkinton
   - note: Page text: "Harold Martin School serves approximately 270 students in grades Preschool–3. | The district early childhood preschool program holds annual 'Child Find' screenings for children between the ages of three and five" Handbook: https://drive.google.com/file/d/195oTJoMU21JZnmoodZCnbsjfKdO4Qba8 . NH DOE Oct 1 2026: 42 preschoolers at Harold Martin School. Raw copy: raw/districts/batch-4/hopkinton-pages.txt; raw/districts/batch-4/hopkinton-harold-martin-handbook.txt
49. The Hudson School District runs integrated preschool classes for children with and without educational disabilities, all at Nottingham West Elementary School, with an AM session (8:50-11:20) and a PM session (12:20-2:50). The page asks families to call for tuition and availability; no tuition amount is posted.
   - citation: Nottingham West Elementary School - Preschool
   - source: https://www.sau81.org/nws/families/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hudson
   - note: Page text: "Our integrated preschool programs serve children who have been identified with educational disabilities as well as those without disabilities. ... *All preschool classes are now located at Nottingham West Elementary School! There are both AM and PM sessions offered for Preschool." Page still refers to applications for 2024-2025 or 2025-2026; phone 603-595-1570 ext. 55032 for tuition. Raw copy: raw/districts/batch-5/hudson-preschool.txt
50. The Inter-Lakes School District runs a preschool program at Inter-Lakes Elementary School for children of residents of Center Harbor, Meredith and Sandwich. For 2026-27 the 3-year-old program meets Tuesday to Thursday, 8:15 am to 11:00 am, and the 4-year-old program Tuesday to Friday, 12:00 to 2:45 pm (age 3 or 4 on or before September 30, 2026). Parents provide transportation. Applications received by May 8, 2026 had priority, and registration is ongoing. No tuition is stated on the sheet.
   - citation: Inter-Lakes Elementary School 2026-2027 Preschool Program Registration (linked from https://iles.interlakes.org)
   - source: https://resources.finalsite.net/images/v1774884695/sau2k12nhus/aghz5dmwyhyl1qbzgjky/2627PreKRegistrationInfoSheet.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Inter-Lakes Cooperative
   - note: Page text: "Applications are now being accepted for the Inter-Lakes Elementary Preschool program for the 2026/2027 school year. Open to children of residents of the Inter-Lakes School District (Center Harbor, Meredith, and Sandwich). Parents are responsible for transporting their child to and from the program." ILES office 603-279-7968. NH DOE counted 29 preschool children at Inter-Lakes Elementary on Oct 1, 2026. Raw copy: raw/districts/batch-5/interlakes-prek-registration-2026-27.txt
51. The Jaffrey-Rindge Cooperative School District has public preschool classes: NH DOE counted 64 preschool children on October 1, 2026 (31 at Jaffrey Grade School and 33 at Rindge Memorial School), and the district's kindergarten registration notice refers to children continuing from its preschool. No program page, schedule or tuition was found on the district site.
   - citation: JRCSD kindergarten registration notice; NH DOE iPlatform Preschool Enrollments 2026-2027
   - source: https://www.sau47.org/news/sau47/kindergarten_registration_opening_april_1
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jaffrey-Rindge Cooperative
   - note: Page text: "If your child attended preschool and is continuing to kindergarten in the district, you will follow the steps for a 'Annual Learner Update'" District runs free Child Find screenings for ages 2.5-5 (https://www.sau47.org/departments/student_services/child_find_screening). Raw copy: raw/districts/batch-5/jaffrey-rindge-k-registration.txt; raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx
52. The Kearsarge Regional School District runs Kearsarge Regional Preschool in New London and Bradford, a tuition-based program for 3- and 4-year-olds from its seven towns serving children with a variety of learning needs. Half-day sessions run Tuesday-Friday, 8:30-11:30 or 12:00-3:00, with limited full-day places by lottery. 2026-27 tuition for the 3-year-old program: $200 a month half day, $400 full day, $450 full day with Mondays. The preschool filled all spaces for 2026-27; applications for 2027-28 begin in January 2027.
   - citation: Kearsarge Regional Preschool - 3 Year Old Program
   - source: https://www.kearsarge.org/james-house-preschool/about-us/pages/3-year-old-program
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kearsarge Regional
   - note: Page text: "Tuition rates for 2026-2027 School Year: Half Day Programming AM or PM- $200 per month Full Day- $400 per month Full Day with Mondays- $450 per month" Program description: https://www.kearsarge.org/krps-bradford-and-new-london/about-kearsarge-regional-preschool (raw kearsarge-krps-about.txt). Filled notice: https://www.kearsarge.org/krps-bradford-and-new-london/news/kearsarge-regional-preschool-no-longer-accepting-applications-26 ('Applications for the 2027-2028 school year will begin in January 2027'). 4-year-old tuition page saved (kearsarge-krps-4yo.txt) but not checked for amounts. NH DOE Oct 1 2026: 49 preschoolers (Bradford 27, New London 22). Raw copy: raw/districts/batch-6/kearsarge-krps-3yo.txt
53. The Keene School District runs Jonathan Daniels Preschool, an integrated, play-based preschool for children ages 3 and 4, with morning (7:45-10:30 am) and afternoon (11:15 am-2:00 pm) sessions. Monthly tuition for 2026-27 is $110 for two half days a week, $165 for three half days and $280 for five half days; reductions may be available for families that qualify under the free and reduced lunch income guidelines.
   - citation: Jonathan Daniels Preschool Tuition Rates for 2026-2027 (linked from https://dan.keeneschoolsnh.org)
   - source: https://docs.google.com/document/d/11evrHfj-KAYgvwV11pNyqubcddl2QSDvwGnv4cYSaCU/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Keene
   - note: Page text: "Jonathan Preschool Tuition Rates for 2026-2027 Monthly Rates Two Half Days a Week $110 ... Three Half Days a Week $165 ... Five Half Days a Week $280 | Jonathan Daniels Preschool is a fun, play based, integrated preschool for children ages 3 and 4 years old." Handbook: https://docs.google.com/document/d/1lgieqhWni0mAviUH5HtIhYT7MAA5cUirBP9fL-rIG6k ; rolling enrollment once a child turns 3. NH DOE Oct 1 2026: 88 preschoolers at Jonathan Daniels School. Raw copy: raw/districts/batch-4/sau29-school-tuition-rates.txt; raw/districts/batch-4/keene-jd-handbook.txt
54. The Kensington School District does not run its own preschool program: its page says that, because of small enrollment, Kensington Elementary has no in-house preschool, and preschoolers who receive special education services are served through community partners (such as the Exeter Developmental Preschool).
   - citation: Kensington Elementary School - Preschool
   - source: https://www.sau16.org/pages/f4d07ee4-a641-4ee9-b467-7ae70c34c886
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kensington
   - note: Page text: "Due to the small size of enrollment, Kensington Elementary does not have an in-house preschool program." SAU 16 Preschool Coordinator: Karen Ringuette, 603-775-8644. Raw copy: raw/districts/batch-8/kes-preschool.txt
55. The Laconia School District runs a preschool; for 2026-27, families pick up a preschool registration packet at the SAU office, 39 Harvard Street, Laconia. The site's preschool page was not available, and no hours or tuition were found.
   - citation: Laconia School District (SAU 30) home page
   - source: https://www.sau30.org
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Laconia
   - note: Page text: "Preschool Registration for the 2026–2027 School Year Is Now Open! ... To begin the registration process, please visit the Laconia School District SAU Office, located at 39 Harvard Street, Laconia, NH, to pick up a preschool registration packet." https://www.sau30.org/preschool.html returned 404 on 2026-11-08. NH DOE Oct 1 2026 preschool count: 57 (Elm Street 13, Pleasant Street 13, Woodland Heights 31). Raw copy: raw/districts/batch-2/laconia-sau30-home.txt
56. The Lebanon School District runs Beginnings Preschool in two classrooms at Mount Lebanon Elementary School, each with a session for 3-year-olds and one for 4-year-olds. Spaces are limited and filled by lottery; all age-appropriate children living in the district may apply. The lottery for 2026-27 was completed and all spots were full.
   - citation: Mount Lebanon Elementary School, Beginnings Preschool
   - source: https://mls.sau88.net/programs/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lebanon
   - note: Page text: "The SAU 88 Beginnings Preschool Program offers a limited number of spaces to Lebanon residents with preschool aged children. We have completed the lottery for the 2026-2027 school year and all spots are full at this time." No tuition on the page. NH DOE Oct 1, 2026: 41 preschool students at Mt. Lebanon School. Raw copy: raw/districts/batch-3/lebanon-preschool.txt
57. Lempster Community School runs a Pre-K program: 4-year-olds attend Monday, Wednesday and Friday and 3-year-olds Tuesday and Thursday, from 8:15 to 11:00 am. Children must be fully toilet trained. No tuition was posted.
   - citation: Mrs. Dow's Pre-K (Lempster Community School teacher site, linked from https://www.sau71.org)
   - source: https://sites.google.com/sau71.org/mrsdowspre-k/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lempster
   - note: Page text: "Pre-K Program Age 4: Monday, Wednesday & Friday Age 3:Tuesday & Thursday ... Drop-off: 8:15 AM at the Pre-K Door (A2) ... Pick-up: 11:00 AM" Teacher page, not a district program page; NH DOE counted 13 preschool children at Lempster Community School on Oct 1, 2026. Raw copy: raw/districts/batch-5/lempster-prek-site.txt
58. The Lisbon Regional School District has a pre-kindergarten (Grade PK) class at Lisbon Regional School; the 2026-27 student handbook lists a Grade PK teacher and describes assessment for '(pre-school)/kindergarten through grade 5'. No tuition, schedule or eligibility details are posted.
   - citation: Lisbon Regional School 2026-27 Student Handbook
   - source: https://www.lisbon.k12.nh.us/uploads/4/6/0/3/4603503/26-27_student_handbook.docx__1_.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lisbon Regional
   - note: Page text: "Andrews, Karin - Grade PK | For students in (pre-school)/kindergarten through grade 5 the school year is divided into trimesters." NH DOE Oct 1 2026: 13 preschoolers at Lisbon Regional School (Elem). Raw copy: raw/districts/batch-4/lisbon-handbook-2026-27.txt
59. In the Litchfield School District, Griffin Memorial School serves grades Pre-K to 4. No page describing the preschool program, eligibility or tuition was found on the district site.
   - citation: Litchfield School District - Student Registration (School Placement)
   - source: https://www.litchfieldsd.org/StudentRegistration1.aspx
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Litchfield
   - note: Page text: "Griffin Memorial School - Grades Pre-K - 4" Partial: only the grade span shows a district Pre-K. NH DOE Oct 1 2026: Griffin Memorial 35 preschoolers. Student Services page (raw litchfield-studentservices.txt) does not describe preschool. Raw copy: raw/districts/batch-6/litchfield-registration.txt
60. The Londonderry School District runs the Londonderry Early Education Program (LEEP) at Moose Hill School, a developmental preschool for children aged three to four with and without special needs. Children who qualify for special education attend at no charge; typically developing 'inclusion' children pay tuition (amounts are sent in a payment schedule after registering, not posted), with registration mainly in March. Sessions run 8:25-10:55 AM or 12:00-2:30 PM, Monday through Thursday.
   - citation: L.E.E.P. Family Handbook (updated 01/16/2025)
   - source: https://drive.google.com/file/d/1_HgizU0ZTvUJlGPFNY39m3heI6YLiiMS/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Londonderry
   - note: Page text: "The Londonderry Early Education Program (L.E.E.P.) is a developmental preschool servicing youngsters aged three to four with and without special needs. ... Children who meet the New Hampshire standards for special education are eligible to attend the L.E.E.P. Program without charge." Tuition amounts not posted; handbook says a payment schedule is sent after registering. NH DOE Oct 1 2026 count: 114 preschoolers at Moose Hill School. Program page: https://moose.londonderry.org/leep/about-leep Raw copy: raw/districts/batch-4/londonderry-leep-handbook.txt; raw/districts/batch-4/londonderry-leep-about.txt
61. The SAU 13 preschool program is held at Madison Elementary School for children who turn three by September 30, 2026 and live in Freedom, Madison or Tamworth. Sessions are half day (9:00-11:45) or full day (9:00-3:00); tuition for children without an identified disability is $11.50 per day for half day and $23.00 per day for full day.
   - citation: SAU 13 - Preschool Program
   - source: https://www.sau13.org/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Madison
   - note: Page text: "The SAU #13 preschool program will be held at Madison Elementary School in Madison, NH. Session options include Half day (9:00 AM - 11:45 AM) or full day (9:00 AM - 3:00 PM)." NH DOE counted 21 preschool children at Madison on Oct 1, 2026. Raw copy: raw/districts/batch-7/sau13-preschool.txt
62. The Manchester School District runs a preschool, the Selma Deitch Early Learning Program, with two ways in: special education for children with identified disabilities, and a limited number of Title I openings for children living in Title I school neighborhoods, taught in the same classrooms. Sites include the Bishop O'Neil Center and Jewett Street, Parker Varney, Smyth Road and Weston elementary schools. The district also places some preschoolers with IEPs in community centers under formal agreements. No tuition is posted.
   - citation: Selma Deitch Early Learning Program
   - source: https://www.mansd.org/page/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Manchester
   - note: Page text: "The Manchester School District offers two ways to access our preschool program. ... Special Education for children with identified disabilities ... Title I for children residing in Title I school neighborhoods" Also https://www.mansd.org/o/msd/page/preschool-title-i ('a limited number of Title I preschool openings in which children are taught in the same classroom with students identified with educational disabilities') and https://www.mansd.org/o/msd/page/preschool-special-education, https://www.mansd.org/page/preschool-outreach-programs. FAQ answers (age, transport) are in collapsed accordions that did not render. NH DOE Oct 1 2026: 418 preschoolers. Raw copy: raw/districts/batch-1/manchester-preschool.txt
63. The Marlborough School District has a preschool (Pre-K) at Marlborough School; the 2026-27 handbook lists a preschool teacher and a preschool paraprofessional. An older SAU 29 registration page said Pre-K children must be 4 years old by September 30. No tuition is posted.
   - citation: Marlborough School Handbook 2026-2027; SAU29 Towns Kindergarten Registration page
   - source: https://docs.google.com/document/d/1VP4s-4Qmw8ABomOs0_BvCuwze743qI3kp0Ss8_m2Y58/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlborough
   - note: Page text: "Rachel Hoglund - Preschool Teacher/Case Mngr ... Jasmine Roach - Preschool Para | Marlborough School - (603) 876-4465 - For Pre-K – must be 4 years old by 9/30/24" NH DOE Oct 1 2026: 21 preschoolers at Marlborough Elementary School. The Pre-K age line on the SAU page refers to 2024. Raw copy: raw/districts/batch-4/marlborough-school-handbook.txt; raw/districts/batch-4/sau29-towns-k-registration.txt
64. The Marlow School District provides half-day pre-kindergarten at the John D. Perkins, Sr. Academy of Marlow, from 8:00 am to 12:00 pm, for children who are 4 by September 30 (2024-25 handbook). No tuition is posted.
   - citation: John D. Perkins, Sr. Academy of Marlow Student Handbook 2024-2025
   - source: https://drive.google.com/file/d/1ZEvjTSSpNPfO-XQc9L_5Wlw1AFaHwJ2w/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlow
   - note: Page text: "The Marlow School District provides half-day pre-kindergarten and full day kindergarten. Pre-kindergarten begins at 8:00 am and ends at 12:00 pm. ... Students must be 4 years old by September 30 in order to enter the pre-kindergarten program." NH DOE Oct 1 2026 preschool report lists no Marlow preschoolers, so the program may not be running in 2026-27; flag for confirmation. Raw copy: raw/districts/batch-4/marlow-school-handbook.txt
65. NH Department of Education counted 13 preschool children enrolled in the Mascenic Regional School District's schools on October 1, 2026 (Highbridge Hill Elementary School (13)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mascenic Regional
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on https://www.mascenic.org. NH DOE Oct 1 2026 preschool count: 13 (Highbridge Hill Elementary School).
66. The Mascoma Valley Regional School District runs preschool with morning and afternoon sessions for 3- and 4-year-olds, through Canaan Elementary School and Enfield Village School. For 2026-27, current preschool families registered February 5-6, 2026 and enrollment for others began February 16, 2026. No tuition is posted.
   - citation: Mascoma Valley Regional School District - Enrollment
   - source: https://www.mascomaschools.org/our-district/enrollment
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mascoma Valley Regional
   - note: Page text: "PRESCHOOL REGISTRATION ... February 5th & February 6th (Current Preschool Families) ... February 16th (Enrollment Begins) ... Morning and afternoon sessions available for 3- and 4-year-olds." NH DOE Oct 1 2026 preschool count: 77 (Canaan Elementary 46, Enfield Village 31). Raw copy: raw/districts/batch-2/mascoma-enrollment.txt
67. The Mason School District runs Mason Integrated Preschool at Mason Elementary School, Monday through Thursday, 9:00 a.m. to 12:00 p.m., for children 3 to 5 years old (3 by September 30). There is a wait list for 2027-28; families contact the school secretary at (603) 878-2962.
   - citation: Mason Elementary School, Preschool
   - source: https://www.sau89.nh.gov/apps/pages/index.jsp?uREC_ID=4462428&type=d&pREC_ID=2731607
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mason
   - note: Page text: "Mason Integrated Preschool is held Monday through Thursday from 9:00 AM to 12:00 PM For children 3 to 5 years old (3 years old by September 30th) There is a wait list for the 2027-2028 school year." No tuition stated. NH DOE Oct 1, 2026: 8 at Mason Elementary School. Raw copy: raw/districts/batch-3/mason-preschool.txt
68. The Merrimack School District runs the Merrimack Early Education Program (MEEP), a preschool for three- and four-year-olds with and without special needs, in classrooms at Reeds Ferry, Thorntons Ferry and Mastricola elementary schools. Families pay monthly tuition, except for children with special needs placed by the district. Parents transport children who do not have special needs. The page does not post the tuition amount.
   - citation: Early Education Program (MEEP)
   - source: https://www.sau26.org/departments/early-education-program-meep
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack
   - note: Page text: "The Merrimack Early Education Program (MEEP) is a developmental preschool program for three and four-year-olds where children with and without special needs have the opportunity to play and learn together. ... Families pay monthly tuition to the Merrimack School District. There are no tuition fees for children with special needs who are placed in the program by the school district." NH DOE Oct 1 2026 preschool enrollment: 95. Raw copy: raw/districts/batch-1/merrimack-meep.txt
69. In the Merrimack Valley School District, Boscawen Elementary School and Penacook Elementary School serve students from Pre-K through grade 5, according to the district's 2026 Annual Report. The district's pages give no preschool tuition, schedule or eligibility.
   - citation: Merrimack Valley School District 2026 Annual Report
   - source: https://drive.google.com/file/d/1P82wi-vCYJExipzNQDwTwCyBLqYbK7T9/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack Valley
   - note: Page text: "Boscawen Elementary School (BES) serves students in Pre-K through Fifth Grade. ... Penacook Elementary School serves roughly 315 students in grades Pre-K through 5." Annual report linked from https://www.mvsdpride.org/school-board/2026-27-budget-information. NH DOE Oct 1 2026: 28 preschoolers (Boscawen 16, Penacook 12). Raw copy: raw/districts/batch-1/mvsd-2026-annual-report.txt
70. Middleton Elementary School lists a preschool teacher in its family handbook, and NH DOE counted 6 preschool children there on October 1, 2026. No preschool program page, schedule or tuition was found.
   - citation: Middleton Elementary School Family Handbook 2025-2026; NH DOE iPlatform Preschool Enrollments 2026-2027
   - source: https://docs.google.com/document/d/1cjZwmmdGQfuVr0qLuLMQFhEoZcVLcn88RlJQ3qjbD8o/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Middleton
   - note: Page text: "PreSchool Jennifer Larson - jennifer.larson@sau69.org" Thin evidence; program details not found. Raw copy: raw/districts/batch-5/middleton-mes-family-handbook.txt; raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx
71. The Milford School District runs the Milford Early Education Experience (MEEE) preschool program through its Office of Student Support Services. Sessions run Mondays, Tuesdays, Thursdays and Fridays, mornings (8:55-11:30) or afternoons (12:35-3:15). Tuition for peer models is $250 a month; from 2026-27 cash payments are no longer accepted.
   - citation: Milford Office of Student Support Services - Milford Early Education Experience (MEEE)
   - source: https://spsvcs.milfordk12.org/apps/pages/index.jsp?uREC_ID=1620096&type=d&pREC_ID=2726511
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milford
   - note: Page text: "Tuition Tuition for peer models: $250.00 per month Payable by check or On-Line in PowerSchool NEW 2026-2027 Cash Payments will no longer be accepted" NH DOE Oct 1 2026: Milford Early Education Experiences 51 preschoolers. Online registration page lists Heron Pond Elementary as 'Grades Pre-K, 2 to 5'. Raw copy: raw/districts/batch-6/milford-meee.txt
72. The Milton School District has public preschool enrollment: NH DOE counted 23 preschool children at Milton Elementary School on October 1, 2026. No preschool program page, schedule or tuition was found on the district site.
   - citation: NH DOE iPlatform - Preschool Enrollments 2026-2027 (as of October 1, 2026)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milton
   - note: Page text: "64,Milton,359,Milton,22075,Milton Elementary School,23 (row of the NH DOE 2026-2027 Preschool Enrollments export: SAU #, SAU name, District #, District name, School #, School name, Enrollment count)" Based only on the state count; district site checked (home, MES home, handbook). Raw copy: raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx
73. The Monadnock Regional School District's Dr. George S. Emerson School website lists a preschool class. No program details, hours or tuition were found on the district site.
   - citation: Dr. George S. Emerson School home page
   - source: https://emerson.mrsd.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Monadnock Regional
   - note: Page text: "PreSchool with Ms. Gove" Thin evidence. NH DOE Oct 1 2026 preschool count: 62 (Emerson 25, Mt. Caesar 36, Troy 1). Student Services page notes special education from age 2 1/2 and Child Find. Raw copy: raw/districts/batch-2/mrsd-emerson.txt
74. The Monroe School District runs a preschool at Monroe Consolidated School. For 2026-27, preschoolers had to be 4 years old by September 30, 2026, and preschool started August 26. Registration is online through Alma Start. The page posts no tuition.
   - citation: Monroe Consolidated School - New Student Registration
   - source: https://sites.google.com/a/monroeschool77.com/monroe-consolidated-school/new-student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Monroe
   - note: Page text: "Preschoolers must be 4 years old by Sept 30, 2026 ... Our first day of school for Preschool is August 26th" NH DOE Oct 1 2026: 9 preschoolers at Monroe Consolidated School. Raw copy: raw/districts/batch-1/monroe-new-student-registration.txt
75. The Moultonborough School District offers a universal preschool program at Moultonborough Central School for all 3- and 4-year-olds living in Moultonborough. No schedule or tuition is posted on that page.
   - citation: Moultonborough Central School - welcome/about page
   - source: https://www.sau45.org/pages/ba451203-9b5d-44d1-a6ef-b17009a3275d
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Moultonborough
   - note: Page text: "The school also offers a universal preschool program for all 3 and 4 year olds living in Moultonborough." SAU 45 site search for 'preschool' found no separate preschool page. NH DOE counted 27 preschool children at Moultonborough Central School on Oct 1, 2026. Raw copy: raw/districts/batch-8/moultonborough-mcs-about.txt
76. The Nashua School District runs the Nashua Early Education Program (NEEP) at Franklin Street School, where children with special needs and typically developing children learn together. Its PlayPals program meets Tuesday to Thursday (3-year-olds 9:15-11:45 a.m., 4-year-olds 1:00-3:30 p.m.); children must be 3 or 4 by September 30, tuition is $240 a month plus a $25 registration fee, and parents provide transportation. Enrollment for 2026-27 opened March 2, 2026. The district also runs Purple Panther Preschool for 3- and 4-year-olds.
   - citation: NEEP - PlayPals; NEEP - Purple Panther Preschool
   - source: https://franklin.nashua.edu/fs/pages/5534
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nashua
   - note: Page text: "Students attend on Tuesday, Wednesday and Thursday, from September through June ... Tuition is $240/month ... A $25 non-refundable registration fee is required ... Students must be 3 or 4 by September 30th to qualify ... Enrollment will open on March 2nd, 2026 ... designed for 3- and 4-year-old children" Also https://franklin.nashua.edu/neep/programs/purple-panther-preschool (no tuition posted there). NH DOE Oct 1 2026 preschool count: 277 in Nashua schools. Raw copy: raw/districts/batch-2/nashua-playpals.txt; raw/districts/batch-2/nashua-purple-panther.txt
77. NH Department of Education counted 14 preschool children enrolled in the New Boston School District's schools on October 1, 2026 (New Boston Central School (14)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Boston
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on the SAU 19 New Boston pages (kindergarten registration page, finance page). A search result pointed to a Town of New Boston page (https://www.newbostonnh.gov/node/1223) mentioning a New Boston Central School Preschool Program, but it returned 404 when fetched. NH DOE counted 14 preschool children at New Boston schools on Oct 1, 2026.
78. The New Castle School District does not have its own preschool listed; New Castle children ages 3 to 5 are eligible for the SAU 50 Community Preschool at Rye Elementary School, an inclusive half-day program (2026-27 tuition $200 a month for two sessions a week or $400 for four, September-June).
   - citation: SAU 50 Community Pre-School
   - source: https://www.sau50.org/pages/3051f5d8-1184-40ce-95bf-5c7fef95c2c6
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Castle
   - note: Page text: "Preschool-aged students, ages 3 to 5) who live in any of our SAU 50 towns (Greenland, New Castle, Newington, and Rye) are eligible to attend." 'Does not have its own preschool listed' is based on the SAU 50 schools overview, which lists preschools only at Rye Elementary and Newington Public School. Raw copy: raw/districts/batch-8/sau50-preschool.txt
79. The Newfields School District does not run its own preschool program: its page says that, because of small enrollment, Newfields Elementary has no in-house preschool, and preschoolers who receive special education services are served through community partners (such as the Exeter Developmental Preschool).
   - citation: Newfields Elementary School - Preschool
   - source: https://www.sau16.org/pages/597b6316-b39b-47f0-a431-d091a7a13772
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newfields
   - note: Page text: "Due to the small size of enrollment, Newfields Elementary does not have an in-house preschool program." SAU 16 Preschool Coordinator: Karen Ringuette, 603-775-8644. Raw copy: raw/districts/batch-8/nes-preschool.txt
80. The Newfound Area School District runs a special education preschool at Newfound Elementary School at New Hampton; all district families interested in it are asked to contact that school (603-744-3221). No tuition or peer-model details are posted.
   - citation: SAU 4 - Prospective Families
   - source: https://www.sau4.org/for-students-families/prospective-families
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newfound Area
   - note: Page text: "New Hampton also houses our Special Education Preschool. ... Families who live in New Hampton, and all district families interested in the Special Education Preschool, should contact NES at New Hampton" NH DOE Oct 1 2026: 17 preschoolers at Newfound Elementary School at New Hampton. Raw copy: raw/districts/batch-4/sau4-prospective-families.txt
81. The Newington School District's Newington Public School runs a Pre-K that meets Monday-Friday, 8:05-3:00, for children who are 4 by September 30; tuition is $3,300 a year for Newington residents and $8,500 for non-residents. Newington children ages 3 to 5 are also eligible for the SAU 50 Community Preschool at Rye Elementary School.
   - citation: SAU 50 - schools overview; SAU 50 Community Pre-School (https://www.sau50.org/pages/3051f5d8-1184-40ce-95bf-5c7fef95c2c6)
   - source: https://www.sau50.org/pages/32bfca09-8390-4f0b-bc2d-c425b4ea9011
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newington
   - note: Page text: "The Newington PreK meets Monday through Friday, 8:05 am to 3:00 pm. Students must be 4 by September 30th to join. Tuition for Newington residents is $3,300.00" NH DOE counted 4 preschool children at Newington Public School on Oct 1, 2026. Raw copy: raw/districts/batch-8/sau50-schools.txt; raw/districts/batch-8/sau50-preschool.txt
82. The Newmarket School District runs Newmarket Preschool at Newmarket Elementary School, an inclusive program with a limited number of places for peer-model children each year; it is not a universal public program, and families apply to be placed on a wait list. No tuition or hours are posted.
   - citation: Newmarket Elementary School - Preschool
   - source: https://www.newmarket.k12.nh.us/schools/newmarket-elementary-school/curriculum-instruction/preschool/index
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newmarket
   - note: Page text: "As Newmarket Preschool is not a universal public program, there are limited spots for peer-model children each year." Page still invites applications 'for the 2025-26 school year' (not updated). NH DOE counted 34 preschool children at Newmarket Elementary on Oct 1, 2026. Raw copy: raw/districts/batch-8/newmarket-preschool.txt
83. NH Department of Education counted 24 preschool children enrolled in the Newport School District's schools on October 1, 2026 (Richards Elementary School (24)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newport
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on sau43.nh.gov (Richards School home page rendered; guessed /page/preschool URLs return 'Page Not Found'). NH DOE Oct 1 2026 report lists 24 preschoolers at Richards Elementary School, so a program likely exists but the district site was not found to describe it.
84. The North Hampton School District runs a preschool program at North Hampton School, with hours of 8:30 a.m. to 1:30 p.m., Monday through Friday (2025-26 handbook); families submit a Preschool Intent to Enroll form. Tuition and eligibility were not posted on the pages checked.
   - citation: North Hampton School - NHS Preschool Program (and Student & Family Handbook)
   - source: https://www.northhamptonschool.org/nhs-curriculum/nhs-preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district North Hampton
   - note: Page text: "SCHOOL HOURS Preschool Monday through Friday - 8:30 a.m. -1:30 p.m." Hours quote is from the handbook (https://docs.google.com/document/d/1kZE3qKrVZhh6HrHM6b570OOEH601BlXybEfrOkgLU2o/edit). Intent form https://forms.gle/869uk6icPerWaEp56. NH DOE counted 9 preschool children on Oct 1, 2026. Raw copy: raw/districts/batch-7/northhampton-preschool.txt; raw/districts/batch-7/northhampton-family-handbook.txt
85. SAU 44 runs the Step by Step Preschool for the Northwood School District; its page takes tuition payments online but posts no schedule, eligibility or tuition amount. The 2026-27 budget funds one full-time preschool teacher and two preschool assistants.
   - citation: SAU 44 - Step by Step Preschool; 2026 Deliberative Session Packet (https://aptg.co/xX6DT7)
   - source: https://www.sau44.org/o/sau/page/step-by-step-preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Northwood
   - note: Page text: "This account funds 1 full time Preschool Instructor and 2 Preschool Assistants." Page: 'Cheddar Up Payment (Click Here)' -> https://my.cheddarup.com/c/step-by-step-preschool-tuition-collection (not opened). Contact Jenn Adrien, Preschool Coordinator, 603-942-8101. NH DOE counted 28 preschool children at Northwood Elementary on Oct 1, 2026. Raw copy: raw/districts/batch-8/northwood-preschool.txt; raw/districts/batch-8/northwood-deliberative-packet-2026.txt
86. The Nottingham School District runs the Nottingham Preschool in the Nottingham School building, an early childhood program with about half children with disabilities and half typically developing peers. Sessions run Monday to Thursday: 3-year-olds 8:45-11:15 a.m. and 4-year-olds 11:15 a.m.-1:45 p.m., capped at 12 children per session. Peer-model children are chosen by a lottery drawn in April; lottery forms are available from February 1. No tuition is posted.
   - citation: Nottingham Preschool (linked from the school's Pre-K page)
   - source: https://sites.google.com/nottingham.k12.nh.us/nottinghampreschool/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nottingham
   - note: Page text: "Our preschool is an Early Childhood Program that has a 50/50 ratio of neurodiverse to neurotypical children. Two sessions are held Monday through Thursday with 3 year old children attending during the AM session(8:45-11:15) while 4 year old children attend during the PM session(11:15-1:45). Peer model children are enrolled via a lottery system." NH DOE Oct 1 2026 preschool count: 37. Raw copy: raw/districts/batch-2/nottingham-preschool-site.txt
87. The Oyster River Cooperative School District runs the Preschool Education Program (PEP), an integrated preschool at Oyster River High School staffed by Strafford Learning Center. It mainly serves children ages 3-5 who qualify for special education, and some other children from the community also enroll. Classes meet Monday to Thursday: mornings (8:15-10:45) for 3-year-olds and afternoons (12:00-2:30) for 4-year-olds. No tuition is posted.
   - citation: ORCSD - Preschool Education Program
   - source: https://www.orcsd.org/departments/student-services/pep
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Oyster River Coop
   - note: Page text: "The program runs M-Th morning classes (8:15-10:45) for 3 years old students, and M-Th afternoon classes (12:00-2:30) for 4 years old students. ... In addition, some children from the community are also enrolled in the program." NH DOE Oct 1 2026 preschool count: 27 (Oyster River Preschool Education Program). Raw copy: raw/districts/batch-2/orcsd-pep.txt
88. The Pasquaney School District's Bridgewater-Hebron Village School serves pre-kindergarten through grade 6 and has a preschool teacher on staff, according to the district's 2026 annual report. No preschool schedule, eligibility or tuition was found.
   - citation: Pasquaney School District Annual Report, March 17, 2026 (linked from https://www.sau108.org/ menu 'District Annual Report')
   - source: https://aptg.co/_b-b0k
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pasquaney
   - note: Page text: "noting this would be for the upcoming school year (pre-Kindergarten through 6 th grade)." Staff list includes 'Preschool Teacher'. NH DOE counted 14 preschool children at Bridgewater-Hebron Village School on Oct 1, 2026. Raw copy: raw/districts/batch-8/pasquaney-annual-report.txt
89. The Pelham School District runs a preschool at Pelham Elementary School with Pre-K 3 and Pre-K 4 programs; places for 2026-27 were filled by lottery. Tuition and hours were not posted on the pages checked.
   - citation: Pelham Elementary School - NEW Student Registration Information (PRE-K)
   - source: https://www.pelhamsd.org/2022-2023Pre-KKand1stGradeRegistration-GoingLive129213pm.aspx
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pelham
   - note: Page text: "PRE-K 2026-2027 Preschool Lottery Video's **Any questions please reach out to Nicole Desmarais at 603.635.8875 x 1008" Preschool class site: https://sites.google.com/pelhamsd.org/preschool (no tuition or eligibility details). NH DOE counted 50 preschool children in Pelham schools on Oct 1, 2026. Raw copy: raw/districts/batch-7/pelham-prek-k-registration.txt; raw/districts/batch-7/pelham-preschool-site-rendered.txt
90. Pembroke children ages 3 to 5 with special education needs are served by SAU 53's preschool programs, which accept children from Pembroke, Allenstown, Chichester and Epsom; they include TLC Preschool, a special education preschool at the old Allenstown Elementary School (30 Main Street, Allenstown) with four 2.5-hour sessions, which also admits some children without identified needs after an April screening. No tuition is posted.
   - citation: SAU 53 - TLC Preschool
   - source: https://sau.sau53.org/pages/76e46815-3441-4987-aa11-2fbd2b55be4b
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pembroke
   - note: Page text: "SAU 53 preschool programs accept children from the towns of Pembroke, Allenstown, Chichester, and Epsom. SAU 53 preschool programs are located at the old Allenstown Elementary School, 30 Main Street Allenstown, NH." Sessions: one for 3-year-olds Tue/Thu 8:15-10:45; three for 4-year-olds (Mon/Wed/Fri 8:15-10:45; two Tue/Wed/Thu 11:30-2:00). Placement is decided by the child's IEP team; non-identified students are screened in April. Coordinator Paula Dyrkacz (603) 836-6294 x1. NH DOE showed 0 preschool children in Pembroke's own schools on Oct 1, 2026 (program is SAU-run in Allenstown). Raw copy: raw/districts/batch-7/sau53-tlc-preschool-page.txt
91. Piermont Village School has a combined 'Grade Kindergarten & PreK' classroom and posted its newsletters for fall 2026. The site gives no preschool enrollment rules or tuition.
   - citation: Piermont Village School - Grade Kindergarten & PreK
   - source: https://pvs.sau23.org/classroom-newsletters/grade-kindergarten-prek
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Piermont
   - note: Page text: "Grade Kindergarten & PreK Jones Newsletter 11.9.26.pdf" NH DOE Oct 1 2026: 3 preschoolers at Piermont Village School. Raw copy: raw/districts/batch-1/piermont-k-prek.txt
92. NH Department of Education counted 5 preschool children enrolled in the Pittsburg School District's schools on October 1, 2026 (Pittsburg School (Elem) (5)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pittsburg
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: SAU 7 site (sau7.org, SchoolBlocks) checked: home, Policies, About Our School Boards. Menus for district/school pages did not render as links; no registration, preschool, warrant, annual meeting or tuition pages found. A search hit for 'colebrookschool.org' turned out to be Colebrook, Connecticut, and was discarded. NH DOE Oct 1 2026 preschool report lists 5 preschoolers in this district.
93. Plymouth Elementary School has a preschool class (Plymouth Elementary Preschool), with Monday/Wednesday/Friday and Tuesday/Thursday morning groups and a PM session listed on its 2026-27 class page; the school links a preschool registration form. No eligibility rules or tuition are posted.
   - citation: Plymouth Elementary Preschool class page (linked as 'Pre-K' from https://pes.pemibaker.org/)
   - source: https://sites.google.com/pemibaker.org/pespre-school/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Plymouth
   - note: Page text: "October 29th: T/Th parade 9:15 am, PM session 12:45 pm October 30th: M/W/F session Parade 9:15 am" Session pattern inferred only from the class calendar notes. 'Pre-School Registration' form (https://drive.google.com/file/d/1I4cqeEOrSRK2IZorTB-lc5q2HXn7CYc1/view) is a scanned PDF with no text. NH DOE Oct 1 2026 report shows no preschool enrollment for Plymouth. Raw copy: raw/districts/batch-6/pes-prek.txt
94. The Portsmouth School Department runs the Portsmouth Early Education Program (PEEP), an inclusive preschool at Little Harbour School for children ages 3 to 5 with and without educational disabilities. For 2026-27, sessions run 8:30 a.m. to 12:30 p.m., Monday through Thursday; tuition is $400 a month for four days a week or $200 a month for two days; children must be 3 to 5 by September 30, 2026 and toilet trained, and parents provide transportation. Portsmouth High School also lists the Little Clipper Preschool.
   - citation: Portsmouth Early Education Program 2026-2027 flyer (linked from https://www.cityofportsmouth.com/school/peep)
   - source: https://www.portsmouthnh.gov/sites/default/files/2026-01/2026-2027%20PEEP%20Flyer.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Portsmouth
   - note: Page text: "Sessions are 8:30AM-12:30PM Monday through Thursday. Two options for attendance are available: 4 days weekly for $400 monthly 2 days weekly for $200 monthly" Application says families selected for enrollment are notified by May 15. Little Clipper page (https://www.cityofportsmouth.com/school/phs/little-clipper-preschool-0) is 'under construction' and gives no tuition or schedule. Raw copy: raw/districts/batch-8/portsmouth-peep-flyer-2026-27.txt; raw/districts/batch-8/portsmouth-peep.txt; raw/districts/batch-8/portsmouth-peep-application-2026-27.txt; raw/districts/batch-8/portsmouth-little-clipper.txt
95. The Raymond School District runs a preschool program at Raymond High School for children with special education needs and for typically developing children who live in Raymond. Sessions run 8:45-11:15 a.m. and 12:30-3:00 p.m.; enrolled typically developing peers may attend up to four days a week, Monday to Thursday, and some attend on a tuition basis. Families join a waiting list through an online form rather than enrolling online. No tuition amount is posted.
   - citation: Raymond School District Preschool Program 2026-2027 Parent & Student Handbook; Preschool page; Enrollment page
   - source: https://www.sau33.com/district/preschool/files/2026-2027-preschool-parentstudent-handbook
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Raymond
   - note: Page text: "Preschool is open to typically developing children who reside in the town of Raymond. ... Morning Session - 8:45 AM to 11:15 AM ○ Afternoon Session - 12:30 PM to 3:00 PM ... Enrolled typical peers are eligible to join PK programming up to 4 days per week, Monday -Thursday." Handbook mentions 'preschool students who attend on a tuition basis' but gives no amount. Waiting-list instruction on https://www.sau33.com/district/pages/enrollment. NH DOE Oct 1 2026 preschool count: 50. Raw copy: raw/districts/batch-2/raymond-preschool-handbook-2026-27.txt; raw/districts/batch-2/raymond-preschool.txt
96. The Rivendell Interstate School District runs the Rivendell Early Childhood Program (RECP), a public preschool. It is free for in-district children from 8:00 to 11:30, and $20 a morning for children from outside the district. An extended day (11:30 to 3:00) costs $20 a day, and Extended Plus (11:30 to 5:00) costs $35. The Samuel Morey classroom serves the towns of Fairlee and Orford.
   - citation: Rivendell Early Childhood Program (Preschools)
   - source: https://www.rivendellschool.org/preschools
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rivendell
   - note: Page text: "FREE preschool for in district students from 8:00 to 11:30 $20 a morning for out of district students Extended Day program from 11:30 to 3:00 for $20 a day Extended Plus program from 11:30 to 5:00 for $35" Page also: 'Hours for the Samuel Morey Classroom Serving the Towns of Fairlee and Orford: 8:00 - 11:30 Morning Option; 8:00 - 3:00 Full Day Option; 8:00 - 5:30 Full Day option with After School Care'. Classrooms are in Vermont schools; follows Vermont early learning standards. NH DOE count includes NH resident students only and lists none. Raw copy: raw/districts/batch-1/rivendell-preschools.txt
97. The Rochester School District runs REACH Preschool at East Rochester School (773 Portland St), with special education and early childhood classrooms. Community peer spots: three-year-olds attend three mornings a week for 2 hours, tuition $80 a month; four-year-olds attend four afternoons a week (12-2:30 PM), tuition $100 a month. There is a waiting list.
   - citation: East Rochester School - REACH Preschool
   - source: https://www.rochesterschools.com/o/ers/page/reach-preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rochester
   - note: Page text: "Three-year-old students will attend three mornings of preschool a week for 2 hours each session. Tuition is $80 a month for community peer spots. Four-year-old students will attend four afternoons a week for 2.5 hours each session. Monday, Tuesday, Thursday, and Friday 12-2:30 PM Tuition is $100 a month." Page shows no school year. NH DOE Oct 1 2026 preschool enrollment: East Rochester School 41. Separately, Small Wonders lab preschool at Spaulding High School (https://sites.google.com/sau54.org/smallwonderspreschool/home) lists tuition $125/$85 a month but its page refers to 2020-2021, so not used. Raw copy: raw/districts/batch-6/rochester-reach-preschool.txt
98. Rye Elementary School houses two preschool programs: the SAU 50 Community Preschool, an inclusive half-day program for children ages 3 to 5 from Greenland, New Castle, Newington and Rye (2026-27 tuition $200 a month for two sessions a week or $400 for four, September-June), and the Rye PreK, which meets Monday-Friday 8:15-2:15 for children who are 4 by September 30, with tuition of $8,250 a year for Rye residents and $9,000 for non-residents.
   - citation: SAU 50 - schools overview; SAU 50 Community Pre-School (https://www.sau50.org/pages/3051f5d8-1184-40ce-95bf-5c7fef95c2c6)
   - source: https://www.sau50.org/pages/32bfca09-8390-4f0b-bc2d-c425b4ea9011
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rye
   - note: Page text: "The Rye PreK meets Monday through Friday, 8:15 am to 2:15 pm. Students must be 4 by September 30th to join. Tuition for Rye residents is $8,250.00 per year" Community Preschool: mornings 8:15-11:00 (ages 3-4, two mornings a week) and afternoons 11:30-2:15 (ages 4-5, two to four afternoons), Monday-Thursday; 'Financial assistance is available for families who qualify for other public assistance programs'; for 2026-27 waitlist preference to siblings. Rye PreK tuition year not stated. Raw copy: raw/districts/batch-8/sau50-schools.txt; raw/districts/batch-8/sau50-preschool.txt
99. The Salem School District runs Salem Preschool at 24 School Street, an integrated preschool for children ages 3 to 5 with a morning (8:30-11:00) or afternoon (12:15-2:45) session; typical peers attend Tuesday, Wednesday and Thursday, and the posted cost is $200 a month. It is open only to Salem residents, children must be 3 by September 30, 2026-27 registration is full (waitlist), and pre-registration for 2027-28 opens January 25, 2027 at 9:00 a.m.
   - citation: Salem Preschool - Programs and Hours
   - source: https://preschool.sau57.org/seed-program
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Salem
   - note: Page text: "Salem Preschool offers an AM or PM session of Integrated preschool for children ages 3-5. Typical peers attend preschool 3 days a week (Tue, Wed, and Thur). ... COST: $200 a month" Registration details from https://preschool.sau57.org/preschool-registration: 'Salem Preschool pre-registration will open January 25th, 2027 at 9:00am.' 'Children must be 3 years old by September 30th to register.' 'Salem Preschool is exclusively open to Salem, NH residents only.' Children must be fully potty trained. Students with specialized plans may also attend Friday mornings or Monday afternoons on team recommendation. Raw copy: raw/districts/batch-7/salem-preschool-programs-hours.txt; raw/districts/batch-7/salem-preschool-registration.txt
100. The Sanborn Regional School District runs a preschool at Daniel J. Bakie School. Children are selected through a lottery held around January and February, then registered; a separate Preschool Referral Application is used for referrals. No tuition was posted. NH DOE counted 31 preschool children at Bakie School on October 1, 2026.
   - citation: Daniel J. Bakie School - Registration Information
   - source: https://docs.google.com/document/d/1kTAEsgxD1GN7QQpko-mSth1Ni1-3FgAt9NjXqVPL4qE/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Sanborn Regional
   - note: Page text: "To attend our Preschool, your child must be selected through our lottery, which is held in January/February timeframe. Once you have been informed that they have been accepted, you will complete their registration." NH DOE count from iPlatform Preschool Enrollments 2026-27 (statewide raw file). Raw copy: raw/districts/batch-5/sanborn-bakie-registration-doc.txt
101. The Seabrook School District runs a preschool at Seabrook Elementary School with a morning session (8:00-10:45) and an afternoon session (11:45-2:30) (2026-27 handbook). Tuition and eligibility were not posted on the pages checked.
   - citation: Seabrook Elementary School Student Handbook 2026-2027
   - source: https://www.sau21.nh.gov/ses/files/documents/SESHandbook_2026-2027.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Seabrook
   - note: Page text: "Preschool: AM Sessions 8:00 am to 10:45 PM Sessions 11:45 am to 2:30 pm" NH DOE counted 34 preschool children in Seabrook schools on Oct 1, 2026. Raw copy: raw/districts/batch-7/seabrook-ses-handbook-2026-27.txt
102. The Shaker Regional School District runs a preschool program through its Office of Student Services. For 2026-27, children had to be 3 on or before September 30, 2026; applications were due April 17, 2026, with a mandatory screening at Belmont Elementary School on May 20, 2026 and the first day of school on September 3, 2026. No tuition is posted.
   - citation: Shaker Regional School District - Preschool Program
   - source: https://www.sau80.org/departments/student_services/preschool_program
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Shaker Regional
   - note: Page text: "Preschool Application Timeline Must be age 3 on or before September 30, 2026 April 17, 2026 Completed Applications Due" Quote has a tab between '2026' and 'Completed' on the page. Page also directs families who suspect a disability to Student Services (603) 267-9222. NH DOE Oct 1 2026: Belmont Elementary 26 preschoolers. Raw copy: raw/districts/batch-6/shaker-preschool.txt
103. The Somersworth School District's 2026-27 budget presentation lists preschool tuition among its estimated revenues ('Increase in Preschool Tuition: $8,000'). No page describing the preschool program, its schedule or tuition rates was found on the district site.
   - citation: Somersworth School District 2026-2027 Proposed Budget Presentation to City Council, April 6, 2026
   - source: https://www.sau56.org/common/pages/GetFile.ashx?key=3sMsAQ09
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Somersworth
   - note: Page text: "• Increase in Preschool Tuition: $8,000" Partial: shows a tuition-charging preschool exists but not details. NH DOE Oct 1 2026: Idlehurst Elementary 36 preschoolers. Idlehurst page and student services page do not describe preschool. Raw copy: raw/districts/batch-6/somersworth-council-budget-presentation-2026.txt
104. NH Department of Education counted 2 preschool children enrolled in the Stewartstown School District's schools on October 1, 2026 (Stewartstown Community School (2)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stewartstown
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: SAU 7 site (sau7.org, SchoolBlocks) checked: home, Policies, About Our School Boards. Menus for district/school pages did not render as links; no registration, preschool, warrant, annual meeting or tuition pages found. A search hit for 'colebrookschool.org' turned out to be Colebrook, Connecticut, and was discarded. NH DOE Oct 1 2026 preschool report lists 2 preschoolers in this district.
105. The Strafford School District runs the Little Spartans Preschool at Strafford School, an integrated class of typically developing children and children with disabilities, ages 3-5. Children must be 3 years old and live in Strafford; hours are 9:00-11:30. Places are filled by a spring lottery from a waiting list. No tuition is posted.
   - citation: Strafford School - Little Spartans Preschool
   - source: https://www.strafford.k12.nh.us/information/little-spartans-preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Strafford
   - note: Page text: "Children must be 3 years old and a resident of Strafford to attend the preschool program. Preschool Hours are 9:00-11:30." The page's enrollment note is out of date (refers to 2024-25 being full and a 2025-26 lottery). NH DOE Oct 1 2026 preschool count: 13. Raw copy: raw/districts/batch-2/strafford-preschool.txt
106. NH Department of Education counted 3 preschool children enrolled in the Stratford School District's schools on October 1, 2026 (Stratford Public School (3)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stratford
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No district preschool page found; SAU 58 has a page for a free online at-home pre-K program (https://www.sau58.org/page/free-online-at-home-prek-program), not checked as a district-run preschool. NH DOE Oct 1 2026 preschool count: 3 (Stratford Public School).
107. Stratham Memorial School, the Stratham School District's elementary school, serves preschool through grade 5. Its preschool pages give no schedule, eligibility or tuition details.
   - citation: Stratham Memorial School - home page
   - source: https://sms.sau16.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stratham
   - note: Page text: "Stratham Memorial School is the elementary school for Stratham, NH, serving Preschool through Grade 5." Preschool pages https://www.sau16.org/pages/6aadd27f-1c43-45f2-a612-882684c777b7 and .../590f6c8b-e764-46cf-baf7-8b4fb6f08ca1 show only resource links. NH DOE counted 21 preschool children at Stratham Memorial School on Oct 1, 2026. Raw copy: raw/districts/batch-8/sms-home.txt
108. The Sunapee School District runs the Sunapee Integrated Preschool at Sunapee Elementary School for children ages 3 to 5 of all abilities; places are filled by lottery, and 2026 lottery applications were due February 6, 2026 (families call 603-763-5675 for an application). Tuition was not posted on the page checked.
   - citation: SAU 85 Sunapee School District - 2026 Preschool Lottery
   - source: https://www.sau85.org/news/what_s_new/2026_preschool_lottery
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Sunapee
   - note: Page text: "Sunapee Integrated Preschool welcomes children ages 3-5 years old of all abilities. Lottery applications must be received by Feb. 6, 2026 for consideration." Site also has a 'Tuition' page (not read). Raw copy: raw/districts/batch-7/sunapee-2026-preschool-lottery.txt
109. Tamworth children can attend the SAU 13 preschool program at Madison Elementary School, open to children who turn three by September 30, 2026 and live in Freedom, Madison or Tamworth. Sessions are half day (9:00-11:45) or full day (9:00-3:00); tuition for children without an identified disability is $11.50 per day for half day and $23.00 per day for full day.
   - citation: SAU 13 - Preschool Program
   - source: https://www.sau13.org/preschool
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Tamworth
   - note: Page text: "Children turning three by September 30, 2026, residing in SAU #13 towns (Freedom, Madison, or Tamworth) are eligible for this program. Non-identified student tuition is $11.50 per day (half day), $23.00 per day (full day)." Before and after care may be available at extra cost. Office 603-323-5088. Raw copy: raw/districts/batch-7/sau13-preschool.txt
110. The Timberlane Regional School District runs multiage early childhood programs for 3- and 4-year-olds (age 3 or 4 by September 30, 2026) at its neighborhood schools (Atkinson Academy, Danville School, Pollard School and Sandown Central), five days a week in morning or afternoon sessions. Tuition for 2026-27 is $2,200 for the school year, with a $220 deposit due April 30, 2026.
   - citation: Timberlane Regional School District - New Student Enrollment Process
   - source: https://www.timberlane.net/enrollment/student-enrollment/student-enrollment-process
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Timberlane Regional
   - note: Page text: "Multiage Early Childhood programs are offered at your neighborhood school (Atkinson Academy, Danville School, Pollard School, and Sandown Central) 5 days a week in either AM or PM sessions. ... Early Childhood Multiage Programming is $2,200 for the school year." NH DOE Oct 1 2026 preschool count: 135. Raw copy: raw/districts/batch-2/timberlane-enrollment-process.txt
111. NH Department of Education counted 9 preschool children enrolled in the Unity School District's schools on October 1, 2026 (Unity Elementary School (9)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Unity
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on https://www.sau109.org. NH DOE Oct 1 2026 preschool count: 9 (Unity Elementary School).
112. NH Department of Education counted 19 preschool children enrolled in the Wakefield School District's schools on October 1, 2026 (Paul Elementary School (19)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wakefield
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on https://www.sau101.org. NH DOE Oct 1 2026 preschool count: 19 (Paul Elementary School).
113. NH Department of Education counted 5 preschool children enrolled in the Warren School District's schools on October 1, 2026 (Warren Village School (5)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Warren
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found. NH DOE Oct 1 2026: 5 preschoolers at Warren Village School.
114. The Washington School District offers an Early Learning Program, funded through Title I, for Washington resident children who will be 3 or 4 by September 30. For 2026-27 it accepted online applications for anticipated openings, with screenings in June and placement announced within two weeks. No tuition is posted.
   - citation: SAU #34 News, 'Washington Elementary School Kindergarten and Early Learning Group Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Washington
   - note: Page text: "The program is available to children who will reach the age of 3 or 4 by September 30, 2026 and are a resident of Washington. Early Learning Program screenings will be scheduled for June and placement will be announced within two weeks from the screening date." 'funded through Title I' from the Washington FY2027 Proposed Budget book (raw washington-budget-book-fy27.txt). NH DOE Oct 1 2026 report shows no preschool enrollment for Washington. Raw copy: raw/districts/batch-6/sau34-home.txt
115. NH Department of Education counted 35 preschool children enrolled in the Weare School District's schools on October 1, 2026 (Center Woods School (35)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Weare
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found. NH DOE Oct 1, 2026: 35 preschool students at Center Woods School (statewide source).
116. NH Department of Education counted 28 preschool children enrolled in the White Mountains Regional School District's schools on October 1, 2026 (Lancaster Elementary School (16); Whitefield Elementary School (12)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district White Mountains Regional
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found. NH DOE Oct 1, 2026 preschool enrollment shows 28 students (Lancaster Elementary 16, Whitefield Elementary 12) - statewide source held by coordinator.
117. The Wilton-Lyndeborough Cooperative School District has Pre-K at Lyndeborough Central School, which serves Pre-K and kindergarten (registration contact 603-732-9228). No tuition, schedule or eligibility details are posted.
   - citation: Welcome to SAU63 (2026), linked from https://www.sau63.org/for-parents/new-student-registration
   - source: https://resources.finalsite.net/images/v1792690101/sau63org/sxtjlfsspx8fh8ebsv49/2026WELCOMETOSAU63.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wilton-Lyndeborough Cooperative
   - note: Page text: "Lyndeborough Central School 603-732-9228 X4481 or s.leblanc@sau63.org Pre-K – Kindergarten" NH DOE Oct 1 2026: 4 preschoolers at Lyndeborough Central School. Raw copy: raw/districts/batch-4/wlc-welcome-2026.txt
118. NH Department of Education counted 33 preschool children enrolled in the Winchester School District's schools on October 1, 2026 (Winchester School (33)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Winchester
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No working district website found. NH DOE counted 33 preschool children in Winchester on Oct 1, 2026.
119. The Windham School District runs an integrated Early Childhood Program (preschool) at Golden Brook School for typical learners and children with special learning needs. New children apply through a lottery and must turn three (or four) before September 30. For 2026-27, three-year-olds attend two mornings a week (8:50-11:30) and four-year-olds four mornings (8:50-11:30) or four afternoons (12:15-2:50); tuition is $150 a month for the 2-day session and $300 a month for the 4-day session.
   - citation: Windham School District - Preschool Information 2026-27
   - source: https://www.windhamsd.org/registration/student_registration/preschool_information_2026-27
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windham
   - note: Page text: "Tuition: 2 Day Session - $150.00/month 4 Day Session: $300.00/ month" Page also links a separate '2026-27 Preschool Tuition' document (not opened). NH DOE Oct 1 2026: Golden Brook Elementary 60 preschoolers. Raw copy: raw/districts/batch-6/windham-preschool-2627.txt
120. The Windsor School District operates no schools. Its budget book says the district provides public education from an Early Learning Program for 3- and 4-year-olds through grade 12, and Windsor children who are three or four by September 30 are eligible for the Hillsboro-Deering Elementary School integrated preschool lottery.
   - citation: SAU #34 News, '2026-2027 Hillsboro-Deering Elementary School Integrated Preschool Registration' (posted March 26, 2026)
   - source: https://sau34.org/en-US
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windsor
   - note: Page text: "Children who reside in the towns of Hillsboro, Deering or Windsor and who will be three or four years of age on or before September 30, 2026 are eligible for the preschool lottery." Budget book quote (raw windsor-budget-book-fy27.txt): 'The Windsor School District provides a program of public education from an Early Learning Program for 3 and 4 year olds through grade 12.' Raw copy: raw/districts/batch-6/sau34-home.txt
121. NH Department of Education counted 19 preschool children enrolled in the Winnisquam Regional School District's schools on October 1, 2026 (Winnisquam Early Learning Center (19)). The district's site does not describe the program, who may attend, or tuition.
   - citation: NH Department of Education, iPlatform "Preschool Enrollments", 2026-2027, as of October 1, 2026 (preliminary)
   - source: https://my.doe.nh.gov/iPlatform/Report/Report?path=%2FBDMQ%2FiPlatform%20Reports%2FEnrollment%20Data%2FEnrollments%20by%20Grade%2FPreschool%20Enrollments&name=Preschool%20Enrollments&categoryName=Enrollments%20by%20Grade&categoryId=10
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Winnisquam Regional
   - note: Statewide count only; raw copy raw/districts/statewide/nhdoe-preschool-enrollments-2027.xlsx. District site checked: No preschool page found on wrsdsau59.org (home, resources, registration pages; district site menus). NH DOE Oct 1 2026 report lists 'Winnisquam Early Learning Center' with 19 preschoolers, so a program exists but the district site describes none that was found.

## budget-form-and-vote-dates: School Budget Form and Vote Dates by District

- kind: local
- question_type: local_practice
- description: Whether each district decides its budget by official ballot (SB2), at a traditional annual district meeting, or through city government, and its 2026 (or 2027) meeting and voting dates.

1. The Albany School District holds a traditional annual district meeting. In 2026, district officers were elected at the Town Hall on March 10, 2026 (polls 10 am to at least 6 pm), and the business meeting followed there at 7 pm the same day.
   - citation: Albany School District Warrant 2026
   - source: https://drive.google.com/file/d/10FsVp30GPNZlkrTUPT4QbbDghOgOacWK/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Albany
   - note: Page text: "You are hereby notified to vote for School District Officers at the Town Hall in Albany on the 10th day of March 2026. The polls will open for this purpose at 10:00 a.m. and will not close before 6:00 p.m. ... YOU ARE ALSO NOTIFIED TO MEET AT THE SAME PLACE AT 7:00 P.M. TO ACT UPON THE FOLLOWING SUBJECTS" Scanned PDF; quote transcribed from page 1 image raw/districts/batch-1/albany-warrant-2026-p1.png. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-1/albany-warrant-2026.pdf
2. The Allenstown School District held its 2026 deliberative session on January 31, 2026, with warrant articles going to a ballot vote in March 2026 (exact date not found on the district's pages). The district also held a special warrant ballot in 2026.
   - citation: Allenstown School District Deliberative Session Packet 2026/2027 (SAU 53 Allenstown board announcements)
   - source: https://drive.google.com/file/d/1sHD-zZjiWMSJPwLwONqxJDAja3LFyHnD/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Allenstown
   - note: Page text: "Allenstown School District Deliberative Session January 31st, 2026" Packet text: 'Capital and Expendable Trust transfers will be incorporated into the budget after the March ballot vote should any warrant articles be approved.' Linked from https://sau.sau53.org/pages/0918a990-8753-47e9-b835-df75611f05c7, which also lists '2026 Special Warrant Ballot Results' and '2026 Allenstown Special Warrant'. The 2026 warrant PDF is a scanned image. NHMA/DRA list shows Allenstown as SB2. Raw copy: raw/districts/batch-7/sau53-allenstown-2026-deliberative-packet.txt
3. The Alton School District uses the official ballot (SB2) form. Its 2026 first session (deliberative session) was on January 31, 2026, at 1:00 PM at Prospect Mountain High School, and the second session (official ballot voting) was on March 10, 2026, from 7:00 AM to 7:00 PM at Prospect Mountain High School.
   - citation: Alton School District 2026 Warrant (signed; DRA form), Prospect Mountain SAU documents, 2026 folder
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3643/Pmsau/18be3887-632b-47b8-bca8-0e2daf3baad1/Amended-2026-Warrant-Articles.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Alton
   - note: Page text: "First Session of Annual Meeting (Deliberative Session) Date: January 31, 2026 Time: 1:00PM Location: Prospect Mountain High School ... Second Session of Annual Meeting (Official Ballot Voting) Date: March 10, 2026 Time: 7:00AM – 7:00PM" Folder: https://www.pmsau.nh.gov/documents/alton-central---sau-72/acs-school-board/school-election%2C-warrant-articles-%26-deliberative-s/2026/25117705 ; also posts 2026 Official Ballot Results (ACS news March 11, 2026). 2027 dates not posted. Raw copy: raw/districts/batch-4/alton-2026-warrant.txt; raw/districts/batch-4/alton-docs-2026.txt
4. The Amherst School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Amherst
   - note: Statewide list only; the district's own voting page was not found. Checked: SAU 39 site board pages give no voting information (agendas moved to Simbli); Amherst town election results page lists no March 2026 results. NHMA/DRA list (Jan 2026): Amherst school district is SB2.
5. The Ashland School District votes by official ballot (SB2). Its 2026 first (deliberative) session was on Monday, February 2, 2026 at 6:00 pm in the Ashland Elementary cafeteria, and the second (voting) session was on Tuesday, March 10, 2026 in the William J. Tirone Gymnasium with the town meeting, polls open 8:00 am to at least 7:00 pm.
   - citation: Ashland School District Annual Report for fiscal year ending June 30, 2025 (includes 2026 warrant), linked from https://sau2.k12.nh.us/ashland-school-board
   - source: https://sau2.k12.nh.us/fs/resource-manager/view/a30360aa-a296-4cf6-80fe-ecec75bc210f
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Ashland
   - note: Page text: "FEBRUARY 2, 2026, AT SIX IN THE EVENING (6:00 P.M.) FOR THE FIRST (DELIBERATIVE) SESSION OF THE SCHOOL DISTRICT MEETING ... MARCH 10, 2026, VOTERS WILL MEET FOR THE SECOND (VOTING) SESSION IN THE WILLIAM J. TIRONE GYMNASIUM" On NHMA/DRA SB2 list. Raw copy: raw/districts/batch-5/ashland-annual-report-2025.txt
6. The Auburn School District uses official ballot voting (SB2): its 2026 deliberative session was held on January 31, 2026, at the Auburn Village School gymnasium, where voters moved the warrant articles to the ballot.
   - citation: Auburn School District Deliberative Session Minutes, January 31, 2026
   - source: https://auburnschoolboard.sau15.net/wp-content/uploads/sites/14/2026/02/Auburn-signed-delib-minutes-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Auburn
   - note: Page text: "AUBURN SCHOOL DISTRICT DELIBERATIVE SESSION MINUTES AUBURN VILLAGE SCHOOL GYMNASIUM- AUBURN, NH JANUARY 31, 2026 ... Mrs. Sylvia asked for a motion to move the articles to the ballot." The 2026 ballot vote date was not found on the district or school board site. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/auburn-delib-minutes-2026.txt
7. The Barnstead School District decides its budget at a traditional annual school district meeting. The 2026 meeting was on Saturday, March 21, 2026, at 9:00 am at Barnstead Elementary School. The operating budget voted there includes Barnstead's share of the Prospect Mountain High School budget, recommended by the Joint Maintenance Agreement (JMA) Budget Committee.
   - citation: Barnstead School District Annual Report 2024-2025, printed page 74 (2026 warrant); listed at https://www.pmsau.nh.gov/browse/432193
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3643/Pmsau/8956d01e-faf5-4e8d-94b0-e905a0106f80/Barnstead-Annual-Report-2024-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barnstead
   - note: Page text: "You are hereby notified to meet at the Barnstead Elementary School in said District on the 21st day of March 2026, at 9:00 o'clock in the morning to act upon the Articles set forth in the Warrant" Scanned PDF without text layer; quote transcribed from the page image. Not on NHMA/DRA SB2 list. BES news item also says 'Saturday, March 21, is the annual Barnstead School District meeting. The meeting starts at 9:00 a.m. in the school cafeteria.' Raw copy: raw/districts/batch-5/barnstead-annual-report-2024-25.pdf; raw/districts/batch-5/barnstead-annual-report-2024-25-p73-warrant-2026.jpg
8. The Barrington School District votes by official ballot (SB2). Its budget timeline for 2027-28 (a proposed revision dated October 21, 2026) sets a budget hearing for Wednesday, January 6, 2027 (6 pm, BMS Auditorium) and the deliberative session for Saturday, February 6, 2027 (9 am, BMS Auditorium). Voting is set for Tuesday, March 9, 2027, with polls open 8 am to 7 pm at the BMS Gym.
   - citation: Barrington School District Budget Development Timeline, Proposed Budget for Fiscal Year 2027-2028
   - source: https://drive.google.com/file/d/1Co2zS4ngfj5mB7JG2rPaw-8xwpXrDO9m/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barrington
   - note: Page text: "January 6, 2027 Budget Hearing Wednesday, 6:00 pm, BMS Auditoria | February 6, 2027 Deliberative Session Saturday, 9:00 am, BMS Auditoria | March 9, 2027 Voting Tuesday, Polls open 8:00am - 7:00 pm BMS Gym" Scanned PDF; quote transcribed from rotated page image raw/districts/batch-1/barrington-budget-timeline-2027-28-p1r.png. Linked from https://www.sau74.org/budget/2027-2028_documents. On NHMA/DRA SB2 list. 2026 dates not checked. Raw copy: raw/districts/batch-1/barrington-budget-timeline-2027-28.pdf
9. The Bartlett School District holds a traditional annual district meeting. In 2026 it met on Tuesday, March 3, 2026, at 6:30 pm in the Josiah Bartlett Elementary School gymnasium.
   - citation: Bartlett School District Warrant 2026
   - source: https://drive.google.com/file/d/1jmNQnwCu8JTisfU6hyApY4sHEdYZpzvE/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bartlett
   - note: Page text: "You are hereby notified to meet at the Josiah Bartlett Elementary School gymnasium in said District on Tuesday, March 3, 2026 at 6:30 in the evening to act upon the following subjects" Scanned PDF; quote transcribed from page 1 image raw/districts/batch-1/bartlett-warrant-2026-p1.png. Officer election date not on page 1. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-1/bartlett-warrant-2026.pdf
10. The Bedford School District votes by official ballot (SB2). For the 2026-27 budget, Session I (deliberative) was held on February 3, 2026, at Bedford High School, and Session II (voting by official ballot) was on March 10, 2026.
   - citation: Bedford School District Warrant, February 3, 2026 and March 10, 2026 (Final FY27 Warrant Articles, revised after Deliberative)
   - source: https://drive.google.com/file/d/1rR9N2EInIi7m1oHnQmFPg60HcNrkWPXI/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bedford
   - note: Page text: "You are hereby notified to meet at the Bedford High School in said district on Tuesday, February 3, 2026, at 6:30 p.m., for Session I (Deliberation), to discuss the matters to be voted on by official ballot; and on Tuesday, March 10, 2026, Session II (Voting)" FY27 schedule PDF: public hearing Jan 13, 2026; deliberative Feb 3, 2026; vote Mar 10, 2026. Home page has an 'FY28 Budget Prep' folder but no 2027 dates were seen. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/bedford-fy27-warrant-final.txt; raw/districts/batch-3/bedford-fy27-election-dates.txt
11. The Bethlehem School District votes its budget at an annual district meeting; its 2026 budget hearing was on February 10, 2026, and its posted minutes list annual meetings on March 18, 2025 and March 19, 2024. The 2026 annual meeting date was not found on the school site.
   - citation: Bethlehem School Board, Budget Hearing minutes 2/10/2026; Agendas & Minutes page (https://bethlehem.k12.nh.us)
   - source: https://drive.google.com/file/d/1vUvxejfLz44Mejyi03a7gpAzM0sc1ngI/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bethlehem
   - note: Page text: "Bethlehem Elementary School Budget Hearing 2/10/2026 ... ARTICLE 03: To see if the Bethlehem Elementary School District will vote to raise and appropriate the amount of $4,237,751 for the support of schools | March 18th, 2025 (Annual Meeting)" Traditional (non-SB2) form inferred from warrant wording ('raise and appropriate the amount') and 'Annual Meeting' labels; not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/bethlehem-2026-02-10-budget-hearing.txt; raw/districts/batch-4/bethlehem-pages.txt
12. The Bow School District decides its budget at a traditional annual school district meeting. The 2026 meeting was on Friday, March 13, 2026, at 6 pm in the Bow High School auditorium, where voters took up the Budget Committee's recommended operating budget of $40,850,771.
   - citation: Bow School District 2026 Warrant Articles (signed), linked from https://sau67nh.gov/en/bow-school-board
   - source: https://drive.google.com/file/d/1BxbrBGlkoGRxlYyYly48OxAz0EgrHJIE/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bow
   - note: Page text: "YOU ARE HEREBY NOTIFIED TO MEET AT THE BOW HIGH SCHOOL AUDITORIUM IN SAID DISTRICT ON FRIDAY, THE 13TH OF MARCH 2026, AT SIX O'CLOCK IN THE EVENING, TO ACT ON THE FOLLOWING SUBJECTS" Not on NHMA/DRA SB2 list. PDF is a scan with no text layer; quote transcribed from the rendered page image. Bow School Board calendar lists FY budget meetings Dec 7, 14, 16, 21 (2026). Raw copy: raw/districts/batch-5/bow-warrant-2026.pdf (scanned; text read from Drive viewer screenshot)
13. The Brentwood School District decides its budget at a traditional annual school district meeting: in 2026 the business session on the budget and warrant articles was held on Monday, March 2, 2026, at Swasey Central School, and school officials were elected by ballot on Tuesday, March 10, 2026. A budget public hearing was held February 5, 2026.
   - citation: Brentwood Local School 2026 Warrant (NH DRA form), in the Brentwood 2026-2027 folder linked from SAU 16 Brentwood 'Budget Archives & Annual Financial Reports' (https://www.sau16.org/en-US/budgets-elections-76930aaf/brentwood-50f38d8b/budget-archives-and-annual-financial-reports-0a76edd6)
   - source: https://drive.google.com/file/d/1SEHv9cUqQCKZBlbT0zF2Gyupdsa5udnd/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brentwood
   - note: Page text: "Session of Annual Meeting (Budget, Warrants & Transaction of all Other Business) Date: March 2, 2026 Time: 6pm Location: Swasey Central School" Flyer: 'Brentwood residents will vote on the FY27 school budget at this meeting.' Not on the NHMA SB2 list. Raw copy: raw/districts/batch-8/brentwood-warrant-2026.txt; raw/districts/batch-8/brentwood-budget-flyer-2026.txt
14. The Brookline School District votes by official ballot (SB2): a budget hearing, then a deliberative session, then a ballot vote in March. In 2026 the public hearing was on January 15 and the deliberative session on February 4, 2026 (6:30 pm, Captain Samuel Douglass Academy). SAU 41's dates page lists the voting session as '3/10/25' (7 am to 7:30 pm at Captain Samuel Douglass Academy); the district's budget page says the election is held on the second Tuesday of March, which in 2026 was March 10.
   - citation: SAU41 - Voter Information; Brookline financial information https://www.sau41.org/administration/business-office/brookline-financial-information
   - source: https://www.sau41.org/resources/voter-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brookline
   - note: Page text: "For SB2 Districts such as the Brookline School District, the First Session of the School District Annual Meeting is called the First Deliberative Session. ... 1/15/26-Public Hearing (6:30pm, RMMS) 2/4/26- Deliberative Session (6:30pm, CSDA) 3/10/25- Voting Session (7a-7:30p, CSDA)" '3/10/25' appears to be a typo for 2026; the second Tuesday of March 2026 is March 10, 2026 (derived). On NHMA/DRA SB2 list. Raw copy: raw/districts/batch-5/sau41-voter-information.txt; raw/districts/batch-5/sau41-brookline-financial.txt
15. The Campton School District holds a traditional annual school district meeting. The 2026 meeting was set for Tuesday, March 3, 2026, at 6:30 p.m. at Campton Elementary School (per the district's 2026 warrant, posted as a DRA draft copy).
   - citation: Campton Local School 2026 Warrant ('Campton Warrant Articles' on https://ces.pemibaker.org/school-board/budget-information)
   - source: https://drive.google.com/file/d/1J4YRVV7XXO-LxMKZ443lmblxoTejBHqK/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Campton
   - note: Page text: "the Annual School District Meeting will be held as follows: Date: Tuesday, March 3, 2026 Time: 6:30 p.m. Location: Campton Elementary School" Scanned PDF marked DRAFT; quote transcribed from page image. NHMA/DRA list: not SB2. Raw copy: raw/districts/batch-6/campton-warrant-2026.pdf
16. The Candia School District votes by official ballot (SB2). The 2026 deliberative session (first session) was on February 5, 2026, at 6:00 p.m. at the Moore School, and voting by official ballot was held with town voting on March 10, 2026.
   - citation: Candia School District 2026 Deliberative Session booklet (warrant)
   - source: https://candia.sau15.net/wp-content/uploads/sites/7/2026/01/Candia-Deliberative-session-book-26-READABLE.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Candia
   - note: Page text: "You are hereby notified to meet at the Candia Moore School, in said District, on the 5 th day of February 2026, 6:00 p.m. ... Voting on warrant articles number 1 through 4 shall be conducted by official ballot to be held in conjunction with Town voting on the 10 th day of March 2026." Operating budget article $11,585,787; default $11,817,330. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/candia-deliberative-book-2026.txt
17. The Chatham School District holds a traditional annual district meeting. In 2026 it met on Tuesday, March 10, 2026, at 6 pm in the Town Hall.
   - citation: Chatham School District Warrant 2026
   - source: https://drive.google.com/file/d/12d447FkkJAe8DQZQlbcpWbWmgR_MY8Au/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chatham
   - note: Page text: "You are hereby notified to meet in the Town Hall in said District on Tuesday, the 10th day of March, 2026 to act upon the following subjects. The meeting will take place at 6:00 p.m." Scanned PDF; quote transcribed from page 1 image raw/districts/batch-1/chatham-warrant-2026-p1.png. Warrant cites a Budget Committee. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-1/chatham-warrant-2026.pdf
18. The Chester School District's budget process ends with a school district meeting in March, after a budget public hearing in January and posting of the warrant and budget in February. The 2026 and 2027 meeting dates were not found on the district site.
   - citation: Chester School District - Budget (Budget Process Overview and Milestones)
   - source: https://www.sau82.org/budget
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chester
   - note: Page text: "January Budget to and Presentation to Budget Committee Budget Public Hearing February Post School Warrant Post School Budget ... March School District Meeting" Chester is not on the NHMA/DRA SB2 list. The page does not say whether the March meeting is a traditional meeting; 'Current Budget Files' list was empty when rendered. Site also has HB 1300 / tax cap community information posts. Raw copy: raw/districts/batch-4/chester-budget.txt
19. The Chesterfield School District holds a traditional annual district meeting. In 2026 the district meeting was on March 14 at 10:00 AM, after a budget public hearing on January 24; school district elections were on March 10, 2026.
   - citation: SAU 29 - 2026 District Meeting Dates (revised 11/25/25), linked as 'District Meetings' from https://www.sau29.org
   - source: https://docs.google.com/document/d/1jZKVq6Q_oNJ_qnSUXkGZIPErAnGBQLntiV2R0Qc_lZM/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chesterfield
   - note: Page text: "Chesterfield March 14 10:00AM February 20 February 9 January 21 January 30 January 24 10:00AM ... Elections - March 10, 2026" Form inferred from the SAU table listing a single 'District Mtg' date (not a first/second session as for Keene); Chesterfield is not on the NHMA/DRA SB2 list. The doc says meetings are held at the district's school unless indicated. Raw copy: raw/districts/batch-4/sau29-district-meetings.txt
20. The Chichester School District decides its budget at a traditional annual school district meeting; its 2026 meeting was held on March 7, 2026 at 9:00 a.m. at Chichester Central School.
   - citation: Chichester School District 2026 warrant (SAU 53 Chichester board announcements)
   - source: https://drive.google.com/file/d/1VJjFvKLRG6CQacZmmcpoY7K_7P64_DhQ/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chichester
   - note: Page text: "You are hereby notified to meet at the Chichester Central School in said District on the 7th day of March, 2026 at 9:00 in the morning to act upon the following subjects:" Linked from https://sau.sau53.org/pages/0d6bb2be-89ef-4671-b697-ac945340ef19. The warrant asks voters to act on articles at the meeting (no official ballot session); Chichester is not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-7/sau53-chichester-ann-4.txt
21. The Claremont School District holds a two-session annual school district meeting (official ballot). Its FY2026-27 budget calendar set the first (deliberative) session for February 7, 2026 (snow date February 9) and the second session, ballot voting, for March 10, 2026. A public budget hearing was set for January 20, 2026 at Stevens High School.
   - citation: Claremont School District Budget Calendar, Fiscal Year 2026-2027 (approved by the school board December 17, 2025), linked from SAU 6 School Board page https://www.sau6.org/119765_1
   - source: https://drive.google.com/file/d/1Kt6oFq9BCa6YQH2bm9dWcVwtPAOMyl0z/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Claremont
   - note: Page text: "2/7/2026 2/9/2026 First session of annual School District Meeting (Deliberative). ... 3/10/2026 Second session of annual School District Meeting (Ballot Voting)." Calendar shows planned dates; whether the snow date was used was not checked. SAU 6 news has 'How to Participate in the Deliberative Session' (Jan 27, 2026). NHMA/DRA list: SB2. FY27 warrant PDF on Drive is scanned (no text). Raw copy: raw/districts/batch-6/claremont-budget-calendar-fy27.txt
22. The Concord School District is governed by a district charter: its Board of Education adopts the annual budget after a public hearing, with no district meeting or ballot vote on the budget. For the 2026-27 (FY27) budget, the board held public hearings on March 23 and March 25, 2026 and a session to finalize the preliminary budget on March 31, 2026.
   - citation: Concord School District Charter (updated July 1, 2025); FY27 budget page https://sau8.org/206961_3
   - source: https://files.smartsites.parentsquare.com/8931/concord_school_district_charter_-_updated_july_1_2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Concord
   - note: Page text: "The budget appropriation shall be made by the Board of Education not later than sixty days prior to the beginning of the fiscal year for which it shall apply." Not on the NHMA/DRA SB2 list. Budget page lists 'Budget Meeting #10 - March 23, 2026 Public Hearing Mill Brook School' and '#11 - March 25, 2026 Public Hearing Central Office' and '#13 - March 31, 2026 Finalize Budget'. Raw copy: raw/districts/batch-5/concord-district-charter-pdf.txt; raw/districts/batch-5/concord-budget-fy27.txt
23. The Contoocook Valley (ConVal) School District votes by official ballot (SB2): Part 1 of the district meeting (deliberative session) was on February 3, 2026, at ConVal High School (snow date February 5), and Part 2, voting in the individual towns, was on March 10, 2026.
   - citation: ConVal 2025 District Annual Report (linked as 'District Annual Report' on conval.edu)
   - source: https://drive.google.com/file/d/1GHsvlSy7_T4DRzA_f5Ik8kWZ6uS1P1q_/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Contoocook Valley
   - note: Page text: "CONTOOCOOK VALLEY SCHOOL DISTRICT District Meeting Part 1 February 3, 2026 (Snow Date: February 5, 2026) 6:00 p.m. ConVal High School Gymnasium District Meeting Part 2 Voting in Individual Towns March 10, 2026" SB2 status is from the NHMA/DRA list ('ConVal'); the annual report shows the two-part meeting with town voting. 2025 Part I deliberative session was Feb 4, 2025. Raw copy: raw/districts/batch-3/conval-annual-report.txt
24. The Conway School District votes by official ballot (SB2). In 2026, the deliberative session was Monday, March 2, 2026, at 7 pm in the Kennett High School auditorium. Ballot voting was Tuesday, April 14, 2026, at the Conway Town Garage, with polls open from 8 am to 7 pm.
   - citation: Conway School District Warrant 2026
   - source: https://drive.google.com/file/d/1qak23T5vjm1IYDtdy7zb8KXPS5sVwStA/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Conway
   - note: Page text: "on Monday, March 2, 2026 at 7:00 p.m. for the deliberative portion of the Annual School District Meeting ... Final voting action on all Articles 1 through 15 shall take place by ballot on Tuesday, April 14, 2026, at the Conway Town Garage. The polls shall open for balloting at 8:00 a.m. ... and shall close at 7:00 p.m." Scanned PDF; quote transcribed from page 1 image raw/districts/batch-1/conway-warrant-2026-p1.png. Folder 'Conway Warrant Articles' linked from https://www.sau9.org/conway-home. On NHMA/DRA SB2 list; warrant also cites a Municipal Budget Committee. Raw copy: raw/districts/batch-1/conway-warrant-2026.pdf
25. The Cornish School District posts its 2026 warrant under a 'District Meeting' page, indicating an annual school district meeting. The meeting date was not readable (the warrant is a scanned image).
   - citation: Cornish School District - 2026 Warrant - District Meeting
   - source: https://www.cornishschool.org/apps/pages/index.jsp?uREC_ID=627212&type=d
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Cornish
   - note: Page text: "2026 Warrant - District Meeting" Warrant PDF https://www.cornishschool.org/ourpages/auto/2026/2/25/43892271/2026%20CES%20Warrant.pdf has no text layer. Cornish is not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-2/cornish-district-meeting.txt
26. The Croydon School District holds a traditional Annual District Meeting, where the proposed operating budget and special warrant articles are debated, amended and decided by the public after a school board budget hearing. The 2026 meeting date was not found on the district site; the site says the current budget calendar has not been set.
   - citation: Croydon School District (SAU 99) - Budgets
   - source: https://croydonsd.org/sau/budgets/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Croydon
   - note: Page text: "The proposed operating budget, as well as any special warrant articles, are put forward to debate, amendment, and decision by the public at the Annual District Meeting." Page: 'This year’s budgeting calendar has not been set.' Meeting minutes list (raw croydon-minutes.txt) shows no annual meeting entry. NHMA/DRA list: not SB2. Raw copy: raw/districts/batch-6/croydon-budgets.txt
27. The Deerfield School District uses the official ballot (SB2) form: its 2026 deliberative session was held on February 7, 2026 at 9:00 a.m. at Deerfield Community School, and voting by official ballot was on March 10, 2026, 7:00 a.m. to 7:00 p.m., at the town hall, 10 Church Street.
   - citation: Deerfield School District 2026 Warrant (Amended), posted on the SAU 53 Deerfield board announcements page
   - source: https://drive.google.com/file/d/1IV9GlAGuYevBGeKe274mycbQszRhC5He/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Deerfield
   - note: Page text: "You are hereby notified to meet at the Deerfield Community School in said District on the 7th day of February, 2026 at Nine o'clock in the forenoon (9:00 A.M.) to deliberate upon the warrant articles below." Linked from https://sau.sau53.org/pages/5e48e4c2-77df-4e1b-bda1-197a11a168b7 (Deerfield board announcements). Warrant: 'Voting on warrant articles will be conducted by official ballot at the second session scheduled for March 10, 2026 at the town hall 10 Church Street, Deerfield, NH, from 7:00 A.M. to 7:00 P.M.' Raw copy: raw/districts/batch-7/sau53-deerfield-2026-warrant-amended.txt
28. The Derry Cooperative School District holds a two-part annual meeting with voting by official ballot (SB2). In 2026 the deliberative session was on Saturday, February 7, 2026, at West Running Brook Intermediate School, and the voting session was on Tuesday, March 10, 2026, at Pinkerton Academy's Hackler Gymnasium.
   - citation: Derry Cooperative School District, Election page
   - source: https://sau10.nh.gov/election
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Derry Cooperative
   - note: Page text: "The first session is the Deliberative Session ... This will take place on Saturday, February 7, 2026 at 10:00am in the West Running Brook Intermediate School gymnasium. ... The second session is the Voting Session ... on Tuesday, March 10, 2026 from 7:00am to 8:00pm, at the Pinkerton Academy Hackler Gymnasium." 2026-27 operating budget article: $113,427,524; default $113,765,475. NHMA/DRA list: SB2 ('Derry'). Raw copy: raw/districts/batch-3/derry-election.txt
29. Dover's school budget is set through city government: the School Board adopted the School Department's fiscal 2027 budget on January 12, 2026, the City Council held a public hearing on the school portion on February 25, 2026, and the City Council adopted the city-wide fiscal 2027 budget, including $89,172,779 for School Department operations, on April 1, 2026.
   - citation: City of Dover news, 'City Council adopts FY2027 budget' (posted 4/3/2026); also 'School Board adopts FY2027 budget' (posted 1/16/2026)
   - source: https://www.dover.nh.gov/services/online-services/news-events/news-2026/city-council-adopts-fy2027-budget.html
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dover
   - note: Page text: "The City Council unanimously adopted the city's fiscal year 2027 budget during a special meeting on Wednesday, April 1, 2026 ... The General Fund includes $65,543,012 for city operations, $89,172,779 for School Department operations" School Board article (https://www.dover.nh.gov/services/online-services/news-events/news-2026/school-board-adopts-fy2027-budget.html): 'City ordinance requires the budget to be adopted annually by April 15.' Dover has a charter tax cap (NHMA list). Raw copy: raw/districts/batch-8/dover-city-council-adopts-fy2027.txt; raw/districts/batch-8/dover-school-board-adopts-fy2027.txt
30. The Dresden School District holds an annual meeting, with no voting that day, followed by a voting day. For 2027, the annual meeting is scheduled for Saturday, February 27, 2027, at 12:30 p.m. at Hanover High School, and the Hanover & Dresden voting day for Tuesday, March 2, 2027, 7 a.m.-7 p.m. at Frances C. Richmond Middle School.
   - citation: SAU 70 Voter Information, 'Annual Meetings & Voting Dates for March 2027'
   - source: https://www.sau70.org/resources/voter-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dresden
   - note: Page text: "Dresden School District Annual Meeting Saturday, February 27, 2027, 12:30 PM Hanover High School (no voting that day) Voting Day Tuesday, March 2, 2027 from 7:00 AM to 7:00 PM" Page also links a 'Dresden Absentee Ballot' procedure. Norwich voters' own dates listed separately (Town Deliberative Session Feb 7, 2027; Town Meeting Mar 2, 2027). Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-3/sau70-resources-voter-information.txt
31. The Dummer School District holds a traditional annual meeting: on March 10, 2026, official ballot voting (Articles 1-3) ran 11 a.m.-7 p.m. at Dummer Town Hall, followed by the business session at 6:30 p.m. the same day at Dummer Town Hall.
   - citation: 2024-2025 Dummer Annual Report (contains the 2026 warrant), Dummer School Board site
   - source: https://drive.google.com/file/d/177mDbGqVAo9HP55Gn7oN9nqOjsLVTs_8/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dummer
   - note: Page text: "First Session of Annual Meeting (Official Ballot Voting) Date: March 10th, 2026 Time: 11:00-7:00 PM Location: Dummer Town Hall- 75 Hill Road Details: Ballot Voting- Article 1-3 Second Session of Annual Meeting (Transaction of All Other Business) Date: March 10th, 2026 Time: 6:30 PM" Not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-3/dummer-annual-report-2024-25.txt
32. The East Kingston School District uses official ballot voting (SB2). For the fiscal 2027 budget, its public hearing was January 12, 2026, its deliberative session was January 31, 2026, and voting was on Tuesday, March 10, 2026, 8:00 a.m. to 7:00 p.m., at East Kingston Elementary School.
   - citation: EKES Budget flyer (Annual Budget & Voting Information), in the East Kingston 2026-2027 folder linked from SAU 16 East Kingston 'Budget Archives & Annual Financial Reports'
   - source: https://drive.google.com/file/d/18jPhDxtFsTAca4GgeQcn2Lf3Ia5IzSlz/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district East Kingston
   - note: Page text: "EK residents vote to move the EKES budget and warrant articles to the ballot." Flyer dates: 'Monday, January 12, 2026 @ 5:00 pm', 'Tuesday, March 10, 2026 8:00 am - 7:00 pm', 'Saturday, January 31, 2026 @ 8:00 am'; Deliberative folder has '2026 EKES Deliberative Minutes January 31, 2026.pdf'. Raw copy: raw/districts/batch-8/eastkingston-budget-flyer-2026.txt
33. The Eaton School District holds a traditional annual district meeting. In 2026, district officers were elected at the Town Hall on Tuesday, March 10, 2026 (polls 11 am to at least 6 pm), and the business meeting followed there at 5 pm the same day.
   - citation: Warrant for Annual Meeting of the Eaton School District 2026
   - source: https://drive.google.com/file/d/1yTrHvqV8HfdMccsMdBGkjV6-1jQbXq2N/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Eaton
   - note: Page text: "You are hereby notified to meet at the Town Hall in said District on Tuesday, the 10th day of March, 2026 to vote for the following District Officers. Polls will be open for this purpose at 11:00 a.m., and will not close before 6:00 p.m. ... YOU ARE ALSO NOTIFIED TO MEET AT THE SAME PLACE AT 5:00 P.M. ON THE SAME DAY" Scanned PDF; quote transcribed from page 1 image raw/districts/batch-1/eaton-warrant-2026-p1.png. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-1/eaton-warrant-2026.pdf
34. The Epping School District uses the official ballot (SB2) form. In 2026 its first (deliberative) session was on Thursday, February 5, 2026, at 7:00 p.m. in the Epping Middle-High School Allen Gymnasium, and the second session (official ballot voting) was on March 10, 2026, from 7:00 AM to at least 7:00 PM in the O'Day Gymnasium.
   - citation: Epping School District 2025 Annual Report - 2026 School District Warrant (p. 149)
   - source: https://www.sau14.org/school-board/files/Superintendent%20Reports/2025%20Epping%20School%20Report%20for%20website.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epping
   - note: Page text: "the first session of the annual meeting of the Epping School District, for the transaction of all business other than voting by official ballot, shall be held Thursday, February 5th, 2026, at 7:00 p.m. ... the second session ... on the 10th day of March, 2026" Warrant page is an image in the PDF; transcribed by hand. 2027 dates not posted. Raw copy: raw/districts/batch-4/epping-annual-report-2025.pdf; raw/districts/batch-4/epping-2026-warrant-p149.txt
35. The Epsom School District held its 2026 deliberative session on February 3, 2026; the ballot voting date was not found on the district's pages.
   - citation: Epsom School District 2026-2027 Deliberative Session Packet (SAU 53 Epsom board announcements)
   - source: https://drive.google.com/file/d/1MIVlH_FDvclfKLzOrNL77psJ04Ngopce/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epsom
   - note: Page text: "Epsom School District Deliberative Session February 3rd, 2026" Linked from https://sau.sau53.org/pages/84849d7c-49da-4753-ab4b-d002794d727a. The '2026 Epsom Warrant' PDF there is a scanned image with no text. NHMA/DRA list shows Epsom as SB2; the page also links '2026 ELECTION RESULTS'. Raw copy: raw/districts/batch-7/sau53-epsom-2026-deliberative-packet.txt
36. The Errol School District holds a traditional annual meeting: in 2026 official ballot voting (Article 1) was on March 10, 2026, 11 a.m.-7 p.m. at Errol Town Hall, and the business session was on Saturday, March 14, 2026, at 9:00 a.m. at Errol Town Hall.
   - citation: 2024-2025 Errol Annual School District Report (contains the 2026 warrant), Errol School Board site
   - source: https://drive.google.com/file/d/1lswq7V4J1Oos-7YHdP8H3lxeXks-BLNq/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Errol
   - note: Page text: "First Session of Annual Meeting (Official Ballot Voting) Date: March 10th, 2026 Time: 11:00 am -7:00 pm Location: Errol Town Hall, 33 Main St. Details: Article 1 by ballot Second Session of Annual Meeting (Transaction of All Other Business) Date: March 14th, 2026 Time: 9:00 am" Not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-3/errol-annual-report-2024-25.txt
37. The Exeter School District (elementary) uses official ballot voting (SB2). For the fiscal 2027 budget, its public hearing was January 13, 2026, its deliberative session was February 3, 2026, at Lincoln Street Elementary School, and voting was on Tuesday, March 10, 2026, 7:00 a.m. to 8:00 p.m., at Talbot Gymnasium.
   - citation: ESD Budget flyer (Annual Budget & Voting Information), in the Exeter 2026-2027 folder linked from SAU 16 Exeter Elementary 'Budget Archives & Annual Financial Reports' (https://www.sau16.org/en-US/budgets-elections-76930aaf/exeter-elementary-fa62319d/budget-archives-and-annual-financial-reports-0ed501a0)
   - source: https://drive.google.com/file/d/1NgQ14qmZwALh7fpBWx6jpyOZPTChVHMs/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Exeter
   - note: Page text: "DELIBERATIVE SESSION A second chance for Exeter residents to comment on the budget before voting day. Exeter residents vote to move the ESD budget and warrant articles to the ballot." Dates in flyer text: 'Tuesday, January 13, 2026 @ 6:00 pm' (public hearing), 'Tuesday, March 10, 2026 7:00 am - 8:00 pm' (voting day), 'Tuesday, February 3, 2026 @ 6:00 pm' (deliberative); the same folder has '2026 EXE Deliberative Minutes - Feb.3 2026.pdf'. Flyer layout pairs dates with events; pairing confirmed by the minutes file name. Raw copy: raw/districts/batch-8/exeter-budget-flyer-2026.txt
38. The Exeter Region Cooperative School District uses official ballot voting (SB2). Its 2026 deliberative session (first session) was held on February 4, 2026, at Exeter High School, and the official ballot vote was on Tuesday, March 10, 2026, at polling places in each of its six member towns (Brentwood, East Kingston, Exeter, Kensington, Newfields and Stratham).
   - citation: Exeter Coop 2026 Warrant (NH DRA form), in the ERCSD 2026-2027 folder linked from SAU 16 'Budget Archives & Annual Financial Reports' (https://www.sau16.org/en-US/budgets-elections-76930aaf/exeter-region-cooperative-9e995246/archives-1f3d398d)
   - source: https://drive.google.com/file/d/1-yi8u9qfh9gciyC-QlKO91JA2RLxyK2U/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Exeter Region Cooperative
   - note: Page text: "First Session of Annual Meeting (Deliberative Session) Date: February 4, 2026 Time: 6:30 PM Location: Exeter High School (Auditorium)" Warrant is a scan; text from OCR. Page 5: 'TUESDAY, THE TENTH DAY OF MARCH, 2026'. Deliberative minutes (raw/districts/batch-8/ercsd-deliberative-minutes-2026.txt, OCR) confirm February 4, 2026. The SAU 16 'Budget and Warrant Information' page says 'Information Coming Soon' for 2027; SAU 16 page lists 2027 candidate filing January 20-29, 2027. Raw copy: raw/districts/batch-8/ercsd-warrant-2026.txt
39. The Fall Mountain Regional School District votes on its warrant and candidates by ballot in each member town (SB2). The 2026 vote was held on March 10, 2026. The district's 2027-28 budget timeline schedules the deliberative session for February 1, 2027, at 6:30 p.m., and voting day for March 9, 2027.
   - citation: Fall Mountain 2027-2028 Budget Timeline (FY 28 Budget Documents folder, linked from sau60.org)
   - source: https://drive.google.com/file/d/1d9sMF0oEwrgFJK8SgVD-1XmoYmDRduoQ/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Fall Mountain Regional
   - note: Page text: "02/01/27 6:30pm - Deliberative Session - RSA 40:13 III ... 03/09/27 Voting Day – vote on warrant and candidates – RSA 40:13 VII – 2nd Tuesday in March" 2026 results PDF: 'FALL MOUNTAIN REGIONAL SCHOOL DISTRICT ELECTION & WARRANT RESULTS March 10, 2026' with columns for Acworth, Alstead, Charlestown, Langdon, Walpole. The 2026 warrant PDF is a scan with no text, so the 2026 deliberative date was not confirmed. NHMA/DRA list: SB2 and official budget committee. Raw copy: raw/districts/batch-3/fallmtn-fy28-timeline.txt; raw/districts/batch-3/fallmtn-2026-voting-results.txt
40. The Farmington School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Farmington
   - note: Statewide list only; the district's own voting page was not found. Checked: https://www.sau61.org/board/financial-information has no voting dates. NHMA/DRA list (Jan 2026): Farmington school district is SB2.
41. The Fremont School District uses the official ballot (SB2) form. Its 2026 deliberative session was on Saturday, January 31, 2026, at 9:00 am in the Ellis School gym, and official ballot voting was on Tuesday, March 10, 2026, from 7:00 am to 8:00 pm at the Ellis School gym.
   - citation: Fremont School District FY 27 Signed Warrant Articles (2026 DRA warrant)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3009/Ellisschool/722ed4a7-b26b-40ea-a9e6-fcf660a610e5/FY-27-Signed-Warrant-Articles.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Fremont
   - note: Page text: "First Session of Annual Meeting (Deliberative Session) Date: Saturday, January 31, 2026 Time: 9:00 am Location: Ellis School Gym ... Second Session of Annual Meeting (Official Ballot Voting) Date: Tuesday, March 10, 2026 Time: 7:00 am to 8:00 pm" Scanned; transcribed by hand. On NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/fremont-fy27-warrant.pdf; raw/districts/batch-4/fremont-scans-transcription.txt
42. The Gilford School District votes by official ballot (SB2): its 2026 operating budget article refers to the budget 'as amended by vote of the first session', and the annual school election was held March 10, 2026. Voters approved the $32,185,627 operating budget, 684 to 327. The 2026 deliberative session date was not found on the district site.
   - citation: Gilford School District '2026 Voting Results.pdf' (marked ballot with vote counts), in the '2025 Deliberative Session & Warrant' folder on the Budget Information page https://sau73nh.gov/en-US/pages/f0f47973-5d40-4149-b040-96abeadc10b6
   - source: https://drive.google.com/file/d/1t9R5-3jdjEy_6wlHlaur3JFwlT4PBqE4/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Gilford
   - note: Page text: "ABSENTEE OFFICIAL BALLOT ANNUAL SCHOOL ELECTION GILFORD, NEW HAMPSHIRE MARCH 10, 2026" Scanned PDF; quote and vote counts (handwritten 684 yes / 327 no on Article 02) transcribed from the page image. 'first session' wording from the 2026 ballot proof (raw gilford-ballot-2026.txt). NHMA/DRA list: SB2. Raw copy: raw/districts/batch-6/gilford-voting-results-2026.pdf
43. The Gilmanton School District votes by official ballot (SB2): a first (deliberative) session followed by a second session of official ballot voting. The most recent warrant found is for 2025: the deliberative session was Saturday, February 1, 2025 at Gilmanton School and ballot voting was Tuesday, March 11, 2025 at the Gilmanton Academy Building. 2026 dates were not found.
   - citation: Gilmanton School District 2025 Warrant (FY 25-26), linked as 'Warrant Article' from SAU 79 home (Wayback snapshot 2026-07-16)
   - source: https://drive.google.com/file/d/1gIMls4LLXhviRI2losCCfrJHhAeeOjY-/view
   - as_of: 2026-11-08 (warrant PDF); link found via Wayback snapshot 2026-07-16
   - review_by: 2027-11-08
   - place: district Gilmanton
   - note: Page text: "First Session of Annual Meeting (Deliberative Session) Date: Saturday, February 1, 2025 ... Second Session of Annual Meeting (Official Ballot Voting) Date: Tuesday, March 11, 2025 Time: 7:00 AM to 7:00 PM Location: Gilmanton Academy Building" Scanned PDF read from the Drive viewer image. On NHMA/DRA SB2 list. Older-year dates; 2026 warrant not found because the live sites require sign-in. Raw copy: raw/districts/batch-5/gilmanton-warrant-2025.pdf; raw/districts/batch-5/gilmanton-sau79-wayback-20260716.txt
44. The Goffstown School District votes on its budget by official ballot: its 2026 school district election and ballot vote on warrant articles, including the operating budget, was held on March 10, 2026. The 2026 school deliberative session date was not found on the district's site.
   - citation: Town of Goffstown - 2026 Sample Ballot, School District Officials and Articles
   - source: https://goffstownnh.gov/DocumentCenter/View/5641/2026-Sample-Ballot---School-District-Officials-and-Articles-PDF
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Goffstown
   - note: Page text: "Official Ballot 2026 School District Election March 10, 2026 Goffstown, NH ... the amounts set forth on the budget posted with the warrant or as amended by vote of the first session" Ballot wording ('as amended by vote of the first session', default budget) is the SB2 form; the NHMA/DRA list also shows Goffstown as SB2. The town's own deliberative session was February 3, 2026 (town meeting guide), but no page found states the school district's 2026 deliberative session date; SAU 19 finance pages load documents by JavaScript and did not list it. Raw copy: raw/districts/batch-7/goffstown-2026-sample-ballot-school.txt
45. The Gorham Randolph Shelburne Cooperative School District holds a traditional annual meeting for its budget and other business, with school officers elected by ballot in each town. In 2026 the business session was on March 5, 2026, at 6:30 p.m. at Gorham Middle High School (Alumni Gymnasium), and ballot voting for officers was on March 10, 2026, at the town halls (Gorham 10 a.m.-6 p.m.).
   - citation: 2024-2025 GRS Annual District Report (contains the 2026 warrant), GRS School Board site Annual Reports
   - source: https://drive.google.com/file/d/1-rLoSfOF-W9LMCbLCLk1djuD937M5pAV/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Gorham Randolph Shelburne Cooperative
   - note: Page text: "First Session of Annual Meeting (Transaction of All Other Business) Date: March 5, 2026 Time: 6:30 PM Location: Gorham Middle High School Details: Alumni Gymnasium ... You are hereby notified to meet at the Gorham Town Hall in said District on Tuesday, the 10 th of March 2026 at 10:00 AM in the morning to 6:00 PM in the evening to act by ballot" Not on the NHMA/DRA SB2 list. Randolph and Shelburne town hall polls listed 11 a.m.-7 p.m. Raw copy: raw/districts/batch-3/grs-annual-report-2024-25.txt
46. The Governor Wentworth Regional School District votes by official ballot (SB2). Its 2026 deliberative session was on Saturday, January 31, 2026 at the Kingswood Arts Center in Wolfeboro, and the ballot vote was on Tuesday, March 10, 2026, held with each member town's town meeting.
   - citation: GWRSD Warrant FY2027 (linked from https://gwrsd.sau49nh.gov/school-board/annual-meeting)
   - source: https://gwrsd.sau49nh.gov/fs/resource-manager/view/a0290aeb-12ef-4976-b22e-bfa3c349c323
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Governor Wentworth Regional
   - note: Page text: "You are hereby notified to meet at the Kingswood Arts Center, in Wolfeboro, New Hampshire, on Saturday, the 31st day of January 2026, at 10:00 AM. ... Voting on warrant articles I through XII shall be conducted by official ballot and will occur in conjunction with the town meeting to be held in each town on Tuesday, the 10th day of March 2026." On NHMA/DRA SB2 regional list. 2027 dates not posted. Raw copy: raw/districts/batch-5/gwrsd-warrant-fy2027.txt; raw/districts/batch-5/gwrsd-annual-meeting.txt
47. The Grantham School District decides its budget at an annual school district meeting, with school officers elected at the town election. The 2026 annual meeting was on Tuesday, March 3, 2026 at 6:30 pm in the Grantham Village School gymnasium, and the school district election was on March 10, 2026. For 2027 the district lists a public budget hearing on February 2, 2027, the annual school district meeting on March 2, 2027 (snow date March 4) and school district elections on March 9, 2027 at Grantham Town Hall.
   - citation: Grantham Village School - 2026 March Annual Meeting and Elections; schedule at https://www.gvshawks.org/apps/pages/index.jsp?uREC_ID=3311616&type=d&pREC_ID=2373444
   - source: https://www.gvshawks.org/apps/pages/index.jsp?uREC_ID=3311616&type=d&pREC_ID=2727345
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Grantham
   - note: Page text: "School District Annual Meeting Tuesday, March 3, 2026, at 6:30 pm, GVS Gymnasium. ... March 2, 2027 - Annual School District Meeting (snow date is March 4th) March 9, 2027 - School District Elections, Grantham Town Hall" Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-5/grantham-2026-annual-meeting.txt; raw/districts/batch-5/grantham-school-board.txt
48. The Greenland School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Greenland
   - note: Statewide list only; the district's own voting page was not found. Checked: SAU 50 Budgets page (https://www.sau50.org/pages/c7d00935-ed21-4ee4-82ae-56989fdbaaca) lists only FY26 (2025) documents for Rye and Greenland, and their 2025 warrant PDFs require a Google sign-in. No 2026 deliberative session or vote dates found. District is on the NHMA SB2 list.
49. The Hampstead School District uses official ballot voting (SB2). For the 2026-27 budget, the public hearing was January 13, 2026, and the deliberative session February 3, 2026; the district's budget page posts the sample ballot but does not state the voting date.
   - citation: Hampstead School District - 2026-27 Budget and Voting Information
   - source: https://sites.google.com/hampsteadschools.net/2026-27-budget/home
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampstead
   - note: Page text: "February 3, 2026 Deliberative Session" SB2 from NHMA list and the deliberative session/sample ballot. The 2027-28 budget site (https://sites.google.com/hampsteadschools.net/2027-28-budget/home) lists October 2026 HB 1300 (tax cap) hearings; no 2027 session dates yet. Raw copy: raw/districts/batch-8/hampstead-2026-27-budget.txt; raw/districts/batch-8/hampstead-sample-ballot-2026.txt
50. The Hampton School District uses official ballot voting (SB2). Its 2026 deliberative session (first session) was held Wednesday, February 4, 2026, at 7:00 p.m. in the Hampton Academy auditorium, and the official ballot vote (second session) was on Tuesday, March 10, 2026, at the Winnacunnet High School Dining Hall, polls open 7:00 a.m. to at least 8:00 p.m.
   - citation: Hampton School District 2026 School District Warrant (linked from SAU 90 'Voting Information, ESSER & Annual Report', https://www.sau90.org/page/voting-information-annual-report)
   - source: https://aptg.co/v_1Nz1
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton
   - note: Page text: "FIRST SESSION (Deliberative Session): In the Auditorium at the Hampton Academy, 29 Academy Avenue in Hampton, New Hampshire on Wednesday, February 4, 2026 at 7:00PM" Warrant is a scan (OCR). 'SECOND SESSION (Balloting): At the Winnacunnet High School Dining Hall ... on Tuesday, March 10, 2026'. Operating budget article $32,220,010; default $31,840,467. The voting page has a 2026-2027 section; no 2027 dates seen. Hampton's high school students attend Winnacunnet (Winnacunnet Cooperative, SAU 21) - not stated on pages opened here. Raw copy: raw/districts/batch-8/hampton-warrant-2026.txt
51. The Hampton Falls School District uses the official ballot (SB2) form: its 2026 deliberative session was held on Wednesday, February 4, 2026 in the Lincoln Akerman School cafeteria, and official ballot voting was on Tuesday, March 10, 2026, 8:00 a.m. to 8:00 p.m., at the same location.
   - citation: SAU 21 - 2026-27 School District Voting Information (Hampton Falls tab)
   - source: https://www.sau21.nh.gov/departments/business/voting-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton Falls
   - note: Page text: "Date: Wednesday, February 4, 2026 Time: 7:00 PM Location: Lincoln Akerman School Cafeteria" Snow date Thursday, February 5, 2026. Raw copy: raw/districts/batch-7/sau21-voting-information.txt
52. The Hanover School District holds an annual meeting, with no voting that day, followed by a separate voting day. For 2027, the annual meeting is scheduled for Saturday, February 27, 2027, at 11:30 a.m. at Hanover High School, and voting day for Tuesday, March 2, 2027, from 7 a.m. to 7 p.m. at Frances C. Richmond Middle School.
   - citation: SAU 70 Voter Information, 'Annual Meetings & Voting Dates for March 2027'
   - source: https://www.sau70.org/resources/voter-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hanover
   - note: Page text: "Hanover School District Annual Meeting Saturday, February 27, 2027, 11:30 AM Hanover High School (no voting that day) ... Voting Day Tuesday, March 2, 2027 from 7:00 AM to 7:00 PM Frances C. Richmond Middle School - Gymnasium" Not on the NHMA/DRA SB2 list; the page shows a meeting with no voting followed by a ballot day, but does not name the legal form. 2026 dates not on the page. Raw copy: raw/districts/batch-3/sau70-resources-voter-information.txt
53. The Harrisville School District holds a traditional annual district meeting. In 2026 the district meeting was on March 10 at 6:00 PM, after a budget public hearing on February 4; school district elections were on March 10, 2026.
   - citation: SAU 29 - 2026 District Meeting Dates (revised 11/25/25)
   - source: https://docs.google.com/document/d/1jZKVq6Q_oNJ_qnSUXkGZIPErAnGBQLntiV2R0Qc_lZM/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Harrisville
   - note: Page text: "Harrisville March 10 6:00PM February 12 February 9 January 21 January 30 February 4 6:00PM" Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/sau29-district-meetings.txt
54. The Hart's Location School District holds a traditional annual district meeting. In 2026, district officers were elected on Tuesday, March 10, 2026 (polls at the Notchland Inn from 8 am, and at the Town Hall from 4:30 to 5 pm), and the business meeting was held at the Town Hall at 4:30 pm the same day.
   - citation: Hart's Location School District Warrant 2026
   - source: https://drive.google.com/file/d/1X8dWyibhAw4LavM_npipd9AiuQtokFyG/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hart's Location
   - note: Page text: "You are hereby notified to meet at the Notchland Inn at 2 Morey Road in said Hart's Location on Tuesday, March 10, 2026, to vote for the following District Officers. Polls will be open for this purpose at 8:00 a.m. and will not close before 4:00 p.m. Voting between the hours of 4:30 p.m. and 5:00 p.m. will take place at the Town Hall." Scanned PDF; quote transcribed from page 1 image raw/districts/batch-1/harts-location-warrant-2026-p1.png. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-1/harts-location-warrant-2026.pdf
55. The Henniker School District votes by official ballot (SB2). In 2026, the deliberative session was on Monday, February 2, 2026, at 7:00 p.m. in the Henniker Community School cafeteria, and voting by official ballot was on Tuesday, March 10, 2026, 7 a.m.-7 p.m. at Henniker Community School.
   - citation: Henniker School District 2026 School Warrant (signed 1.13.26)
   - source: https://drive.google.com/file/d/1hPmtmymQKOwLQgNVrt4eRrTvGkHu32T1/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Henniker
   - note: Page text: "You are hereby notified to meet at the Henniker Community School Cafeteria, 51 Western Avenue, Henniker, NH, on Monday, the 2nd day of February 2026 at 7:00 p.m. ... on Tuesday, the 10th day of March 2026 to vote by official ballot" NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/henniker-warrant-2026.txt
56. The Hill School District decides its budget at a traditional annual school district meeting: in 2026 officers were elected on March 10, 2026, 11 a.m.-7 p.m., at the Hill Public Library, and the business meeting was held March 18, 2026, at 7:00 p.m. in the Amsden Auditorium at Jennie D. Blake School.
   - citation: Hill School District Warrant 2026 (linked from https://sites.google.com/sau103.org/jdbs/annual-district-meeting)
   - source: https://drive.google.com/file/d/1R8r62PVekTvNgWZ1GYgGxZlwNVxEqjki/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hill
   - note: Page text: "YOU ARE HEREBY NOTIFIED TO MEET AT THE AMSDEN AUDITORIUM AT THE JENNIE D. BLAKE SCHOOL IN SAID DISTRICT ON THE EIGHTEENTH (18th) DAY OF MARCH 2026, AT 7:00 PM" Warrant is a scan (OCR). Not on the NHMA SB2 list. Raw copy: raw/districts/batch-8/hill-warrant-2026.txt
57. The Hillsboro-Deering Cooperative School District votes by official ballot (SB2). Its 2026 deliberative session was held February 4, 2026, and ballot voting was held Tuesday, March 10, 2026 (Hillsborough voters at Hillsboro-Deering Middle School, 7 a.m.-7 p.m.; Deering voters at Deering Town Hall, 8 a.m.-7 p.m.). The district's preliminary FY2028 timeline lists the next deliberative session (SB2 first session) for February 1, 2027 and voting (second session) for March 9, 2027.
   - citation: FY27 HD Deliberative Session Presentation 02-04-2026 (Hillsboro-Deering FY2027 budget folder, linked from https://sau34.org/pages/bfdfb88a-7021-449d-91f5-f40d21dbc109)
   - source: https://drive.google.com/file/d/1OnzxD-Ldbi-8xoTjCo8vNUc1pI6eDl5k/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hillsboro-Deering Cooperative
   - note: Page text: "DELIBERATIVE SESSION FEBRUARY 4, 2026 ... SECOND VOTING SESSIONS Ballot Voting Tuesday, March 10, 2026 Hillsborough Voters 7:00am – 7:00pm Hillsboro-Deering Middle School Gymnasium Deering Voters 8:00am – 7:00pm Deering Town Hall" 2027 dates from 'H-D Budget Timeline FY28' (raw hillsboro-deering-timeline-fy28.txt): 'February 1, 2027 Deliberative Session (SB2 1st session)' and 'March 9, 2027 Voting (SB2 2nd session)'; its comment column cites a 'February 4th - 11th' window, so the Feb 1 date may change; marked preliminary. A special election was held July 14, 2026 (SAU 34 news). NHMA/DRA list: SB2. Raw copy: raw/districts/batch-6/hd-deliberative-presentation-2026.txt
58. The Hinsdale School District decides its budget at a traditional annual school district meeting: in 2026 school officers were elected by ballot on Tuesday, March 10, 2026, at the Hinsdale Millstream Community Center, and the business meeting was held Saturday, March 14, 2026, in the Hinsdale Middle High School gymnasium, starting at 10:30 a.m. or after Town Meeting, whichever was later.
   - citation: Hinsdale School District - Financial Information (2026 Annual School District Voting & District Meeting)
   - source: https://www.hnhsd.org/?page_id=137
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hinsdale
   - note: Page text: "The Annual School District Meeting follows on: Saturday, March 14th, 2026 Starting at either 10:30 AM, or the conclusion of the Town Meeting, whichever occurs later" Not on the NHMA SB2 list. Page links the 2026 warrant and 2026-27 proposed budget. Raw copy: raw/districts/batch-8/hinsdale-financial.txt
59. The Hollis School District decides its budget at an annual district meeting. In 2026 its public hearing was on February 10, 2026 (7 pm, Town Hall) and its annual meeting on March 17, 2026 (7 pm, Hollis Brookline High School).
   - citation: SAU41 - Voter Information (Important Dates)
   - source: https://www.sau41.org/resources/voter-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hollis
   - note: Page text: "2/10/26- Hollis Public Hearing (7:00pm, Town Hall) 3/17/26- Hollis Annual Meeting (7:00pm, HBHS)" Not on NHMA/DRA SB2 list (on the official budget committee list). Raw copy: raw/districts/batch-5/sau41-voter-information.txt
60. The Hollis-Brookline Cooperative School District decides its budget at an annual district meeting. In 2026 its public hearing was on February 19, 2026 (6:30 pm, Hollis Brookline Middle School) and its annual meeting on March 19, 2026 (6:30 pm, Hollis Brookline High School).
   - citation: SAU41 - Voter Information (Important Dates)
   - source: https://www.sau41.org/resources/voter-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hollis-Brookline Cooperative
   - note: Page text: "2/19/26-COOP Public Hearing (6:30pm, HBMS) 3/19/26- COOP Annual Meeting (6:30pm, HBHS)" Not on NHMA/DRA SB2 list (it is on the official budget committee regional list). Raw copy: raw/districts/batch-5/sau41-voter-information.txt
61. The Hooksett School District votes by official ballot (SB2). In 2026 the first (deliberative) session was held on Friday, February 6, 2026, at 6:00 p.m. at David R. Cawley Middle School, and the ballot vote was on Tuesday, March 10, 2026, at Cawley Middle School.
   - citation: Hooksett School District 2026 Deliberative Session Booklet (warrant)
   - source: https://hooksettschoolboard.sau15.net/wp-content/uploads/sites/13/2026/02/HSD-Deliberative-Book-2026.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hooksett
   - note: Page text: "Hooksett School District Deliberative Sessions Session 1 Friday, February 6, 2026 at 6:00 pm Session 2 Tuesday, March 10, 2026 6:00 am to 7:00 pm" NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/hooksett-deliberative-book-2026.txt
62. The Hopkinton School District holds an annual school district meeting; its FY27 budget page posts the presentation from the annual meeting of March 14, 2026.
   - citation: Hopkinton School District - FY27 Budget Info
   - source: https://www.hopkintonschools.org/pages/8ff695a2-c0c3-40ea-b33b-a8b08da63f31
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hopkinton
   - note: Page text: "FY27 Budget Info ... HSD ANNUAL MEETING PRESENTATION 3.14.26" Hopkinton is not on the NHMA/DRA SB2 list. The 'School Meeting' page (https://www.hopkintonschools.org/en-US/schoolmeeting) links only the 2022 warrant (meeting Saturday March 19, 2022 at Hopkinton High School gym; read from scanned page, raw/districts/batch-4/hopkinton-warrant.pdf). The 'traditional meeting' form is inferred from 'Annual Meeting' wording and the Saturday date, not stated in words. FY28 budget page exists but has no dates yet. Raw copy: raw/districts/batch-4/hopkinton-pages.txt
63. The Hudson School District votes on its budget by official ballot (SB2). In 2026 the school deliberative session was on Saturday, February 7, 2026, and the ballot vote was on Tuesday, March 10, 2026 (7 am to 8 pm). The Budget Committee public hearing was on January 8, 2026. The FY2028 (2027-28) budget was in its school board phase in fall 2026.
   - citation: Hudson School District - Election Information - March 2026
   - source: https://www.sau81.org/schoolboard/election-information/election-information-march-2026
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hudson
   - note: Page text: "Election Day - Tuesday, March 10, 2026 VOTE 7am to 8pm ... School Deliberative Session - Saturday, February 7, 2026 – 9:00am" On NHMA/DRA SB2 list. Ballot article 1 was the operating budget; Article 12 'Default Budget Determination (By Petition)'. 2027 dates not yet posted. Raw copy: raw/districts/batch-5/hudson-election-info-2026.txt; raw/districts/batch-5/hudson-election-results-2026.txt; raw/districts/batch-5/hudson-district-budget.txt
64. The Inter-Lakes School District decides its budget at an annual district meeting. The 2026 annual meeting was on Wednesday, March 4, 2026, at 6:00 pm in the Inter-Lakes Middle High School Community Auditorium (in person only).
   - citation: Inter-Lakes School District - Budget
   - source: https://www.interlakes.org/school-board/budget
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Inter-Lakes Cooperative
   - note: Page text: "Inter-Lakes School District Annual Meeting Wednesday, March 4, 2026 6:00 p.m. Inter-Lakes Middle High School Community Auditorium In-Person Only, Child Care will be Available" Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-5/interlakes-budget.txt
65. The Jackson School District holds a traditional annual district meeting. In 2026 it met on March 5, 2026, at 7 pm at the Whitney Center.
   - citation: Jackson School District Warrant 2026
   - source: https://drive.google.com/file/d/10mSffksL1k97gsgdAhCEoLiWf-Hes0op/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jackson
   - note: Page text: "You are hereby notified to meet at the Whitney Center in said District on March 5th 2026 at 7:00 pm to act upon the following subjects" Scanned PDF; quote transcribed from page 1 image raw/districts/batch-1/jackson-warrant-2026-p1.png. JGS High School Options page also refers to 'the March 5, 2026, annual School District meeting'. A 'Jackson Warrant Elections' folder exists (officer elections) but was not opened. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-1/jackson-warrant-2026.pdf
66. The Jaffrey-Rindge Cooperative School District votes by official ballot (SB2). In 2026 the school board budget hearing was January 15, the deliberative session was Wednesday, February 4, 2026 at 6:30 pm at the Conant Middle High School Pratt Auditorium, and the ballot vote was on town election day, Tuesday, March 10, 2026 (7 am to 7 pm; Rindge voters at Rindge Memorial School, Jaffrey voters at Conant Middle High School).
   - citation: JRCSD 2026 Public Notices (linked from https://www.sau47.org/departments/business/budget_information/budget_documents_fiscal_year_2026-2027/)
   - source: https://drive.google.com/file/d/1d7x1Se7QQwMVI19ZtcUB-fzMq2JHG5hq/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jaffrey-Rindge Cooperative
   - note: Page text: "First Session of Annual Meeting (Deliberative) Wednesday, February 4, 2026, at 6:30 p.m. ... The vote will take place by official ballot on town election day, Tuesday, March 10, 2026." On NHMA/DRA SB2 regional list. The district's 'Budget and Voting Information' page still shows 2023 documents. Raw copy: raw/districts/batch-5/jaffrey-rindge-public-notices-2026.txt; raw/districts/batch-5/jaffrey-rindge-budget-fy27.txt
67. The John Stark Regional School District votes by official ballot (SB2). In 2026, the deliberative session was on Friday, February 6, 2026, at 7:00 p.m. in the John Stark Regional High School cafeteria in Weare, and voting by official ballot was on Tuesday, March 10, 2026, at Henniker Community School and Weare Middle School (7 a.m.-7 p.m.).
   - citation: John Stark School District 2026 School Warrant (signed 1.15.26)
   - source: https://drive.google.com/file/d/14atMFMSRurjikAmEIDq02oIB4pLra41g/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district John Stark Regional
   - note: Page text: "You are hereby notified to meet at the John Stark Regional High School Cafeteria, 618 North Stark Highway, Weare, NH, on Friday, the 6th day of February 2026 at 7:00 p.m. ... on Tuesday, the 10th day of March 2026 to vote by official ballot" NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/johnstark-warrant-2026.txt
68. The Kearsarge Regional School District holds a two-session annual district meeting. The 2026 first (deliberative) session was held January 10, 2026, at 9:00 AM at Kearsarge Regional Middle School, where warrant articles could be discussed and amended; the school district election and ballot vote was held March 10, 2026. The district has a Municipal Budget Committee, which recommended the 2026 operating budget amount.
   - citation: Kearsarge Regional School District 2026 Warrant
   - source: https://www.kearsarge.org/sites/g/files/vyhlif731/f/pages/warrant_2026_final.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kearsarge Regional
   - note: Page text: "ANNUAL DISTRICT MEETING - 1ST SESSION (Deliberative), JANUARY 10, 2026" Vote date from the Annual Meeting/Voter Information page https://www.kearsarge.org/district/pages/annual-meetingvoter-information: 'March 10, 2026 - School District Election in the Kearsarge School District' (raw kearsarge-annual-meeting.txt). Warrant: 'warrant articles that are amended shall be placed on the official ballot for a final vote'. NHMA/DRA list does not list Kearsarge as SB2; the warrant does not use the term SB2. Raw copy: raw/districts/batch-6/kearsarge-warrant-2026.txt
69. The Keene School District has used the official ballot (SB2) form since 1997. In 2026, its first (deliberative) session was on February 7 at Keene High School, and the second session (ballot voting) was on March 10, 7:30 AM to 7:00 PM, at the Keene Recreation Center.
   - citation: Keene School District - Official Ballot, Budget and Warrant Information; SAU 29 2026 District Meeting Dates
   - source: https://www.keeneschoolsnh.org/ksd/kne-board-and-policies/official-ballot-budget-and-warrant-inforrmation
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Keene
   - note: Page text: "The Keene School District has been an official ballot school district since 1997. | Keene February 7 - First Session 9:00AM Keene High School ... March 10 - Second Session 7:30AM to 7:00PM- Keene Recreation Center" Dates from SAU 29 '2026 District Meeting Dates' (Google Doc revised 11/25/25): https://docs.google.com/document/d/1jZKVq6Q_oNJ_qnSUXkGZIPErAnGBQLntiV2R0Qc_lZM . Budget public hearing January 20, 2026. 2027 dates not posted. Raw copy: raw/districts/batch-4/keene-official-ballot-page.txt; raw/districts/batch-4/sau29-district-meetings.txt
70. The Kensington School District uses official ballot voting (SB2). For the fiscal 2027 budget, its public hearing was January 6, 2026, its deliberative session was February 3, 2026, and voting was on Tuesday, March 10, 2026, 8:00 a.m. to 7:30 p.m., at Kensington Elementary School.
   - citation: KES Budget flyer (Annual Budget & Voting Information), in the Kensington 2026-2027 folder linked from SAU 16 Kensington 'Budget Archives & Annual Financial Reports'
   - source: https://drive.google.com/file/d/16cdJZOLD1GYiXk8d3ViRUoW-YJuoYowA/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kensington
   - note: Page text: "Kensington residents vote to move the KES budget and warrant articles to the ballot." Flyer dates: 'Tuesday, January 6, 2026 @ 6:00 pm', 'Tuesday, March 10, 2026 8:00 am - 7:30 pm', 'Tuesday, February 3, 2026 @ 6:00 pm'; Deliberative folder has '2026 KES Deliberative Minutes Feb 3 2026.pdf'. Raw copy: raw/districts/batch-8/kensington-budget-flyer-2026.txt
71. The Landaff School District holds an annual meeting; at its annual meeting on March 9, 2026, the town and school board decided to close the Blue School and make Landaff a tuition-only school district.
   - citation: SAU 35 - Landaff District page
   - source: https://sau35.org/en-US/landaff-blue-school-2ffaf60b
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Landaff
   - note: Page text: "At the Annual Meeting on March 9, 2026 the town and school board decided to close the Blue School and turn Landaff into a tuition only School District." Form (traditional vs SB2) is not stated beyond 'Annual Meeting'; Landaff is not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/sau35-pages.txt; raw/districts/batch-4/landaff-district-page.txt
72. The Lebanon School District holds a deliberative session followed by a ballot vote (SB2). For 2026-27, the deliberative session was on Saturday, January 31, 2026, at the Lebanon Middle School gym, and the school district election was on Tuesday, March 10, 2026. For 2027-28, the deliberative session is scheduled for Saturday, January 30, 2027, at 9 a.m. at Lebanon Middle School (snow date February 1, 2027), and the election for Tuesday, March 9, 2027.
   - citation: Lebanon School District, Budget Documents (2027-28) and 2026-2027 archive
   - source: https://www.sau88.net/budget-documents
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lebanon
   - note: Page text: "Deliberative Session, Saturday, January 30, 2027 at 9 a.m. in the Lebanon Middle School gymnasium (Snow Date Monday, February 1, 2027 at 6 p.m. at LMS) School District Election, Tuesday, March 9, 2027" 2026-27 archive (http://www.sau88.net/budget-documents/2026-2027): public hearing Jan 14, 2026; deliberative Jan 31, 2026; election Mar 10, 2026. Nov 4, 2026 post: HB 1300 tax cap Question 2 did not pass in Lebanon. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/lebanon-budget-docs.txt; raw/districts/batch-3/lebanon-budget-2026-27.txt
73. The Lempster School District decides its budget at a traditional annual school district meeting. The 2026 meeting was on Saturday, March 7, 2026, at 7:00 pm at Lempster Community School; school board members were elected the same day from 4:00 to 7:30 pm.
   - citation: Lempster Local School 2026 Warrant, linked from https://www.sau71.org/page/for-voters
   - source: https://drive.google.com/file/d/1tlQMeXYL7YDlM9NKNJmLMHzIVwcPSMx8/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lempster
   - note: Page text: "You are hereby notified to meet at the Lempster Community School in Lempster, on Saturday the 7th of March, 2026 at (7:00) PM to act upon the articles set forth in the Warrant. Article 1 of the Warrant covers the election of: School Board Members, and will be acted upon at four (4:00) PM until seven-thirty (7:30) PM." Scanned PDF read from the Drive viewer image. Not on NHMA/DRA SB2 list. The For Voters page also lists a 'Sample Official Ballot' (for the election article). Raw copy: raw/districts/batch-5/lempster-warrant-2026.pdf; raw/districts/batch-5/lempster-for-voters.txt
74. The Lincoln-Woodstock Cooperative School District decides its budget at an annual meeting; its website posts minutes of the 2026 annual meeting dated March 17, 2026.
   - citation: Lincoln-Woodstock Cooperative School District - Annual Meeting 2026
   - source: https://www.lin-wood.org/school-board/meetings/annual-meeting-2026
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lincoln-Woodstock Cooperative
   - note: Page text: "Annual Meeting Minutes 3.17.2026" Date taken from the minutes' link title; the minutes and the 2026 warrant PDFs are scanned images with no text layer, so the meeting form (traditional meeting) is inferred from the 'Annual Meeting' page and the district's absence from the NHMA/DRA SB2 list, not read in the warrant. Raw copy: raw/districts/batch-7/linwood-annual-meeting-2026.txt
75. The Litchfield School District holds a two-session annual meeting with official ballot voting (SB2). In 2026, the first (deliberative) session was held Saturday, January 31, 2026, at Campbell High School, and the second session, official ballot voting, was held Tuesday, March 10, 2026, at Campbell High School. Voters approved the $28,411,138 operating budget 755 to 730.
   - citation: Official Election Results, 2026 Litchfield School District Warrant, As Amended at Deliberative Session 1/31/2026 (attested March 12, 2026), linked from Finance & Operations page https://www.litchfieldsd.org/FinanceOperations.aspx
   - source: https://drive.google.com/file/d/1RlRRDvwhqQmj7ZRUKdlWci4qmN19rx1-/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Litchfield
   - note: Page text: "on Saturday, January 31, 2026, at 10:00 o'clock in the forenoon for explanation, discussion, and debate of warrant articles ... on Tuesday, March 10, 2026, at 7:00 o'clock in the forenoon for the choice of School District Officers elected by official ballot" Scanned PDF with no text layer; quote transcribed from the page images as viewed. NHMA/DRA list: SB2. 2027 dates not found. Raw copy: raw/districts/batch-6/litchfield-voting-results-2026.pdf
76. The Littleton School District votes by official ballot (SB2). Its 2026 first (deliberative) session was on Monday, February 2, 2026 at 6:00 pm in the Littleton High School cafeteria, and the second session, electing officers and voting on warrant articles by official ballot, was on Tuesday, March 10, 2026 at the Littleton Public Works Department (polls 8:00 am to at least 7:00 pm).
   - citation: Littleton School District Deliberative Session Notice 2026 (in the '2026 Voter Information' folder linked from https://www.sau84.org)
   - source: https://docs.google.com/document/d/1QbFcVX220Fu493lQlgNFgDuKHKNS9wkCzXtxbk4eIT8/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Littleton
   - note: Page text: "You are hereby notified to meet for the First (Deliberative) Session of the Littleton School District Annual Meeting, to be held at the Littleton High School Cafeteria ... on the second day of February 2026 ... to be held at the Littleton Public Works Department, 2 Boynton Lane, Littleton, New Hampshire, on the tenth day of March 2026, being Tuesday" On NHMA/DRA SB2 list. Budget hearing minutes dated 1.5.26 in the same folder. Raw copy: raw/districts/batch-5/littleton-deliberative-notice-2026.txt; raw/districts/batch-5/littleton-voter-2026-folder.txt
77. The Londonderry School District holds a deliberative session and then votes by ballot: its 2026 annual meeting (deliberative session) was on Friday, February 6, 2026, at Londonderry High School, and voting on the school district warrant was on March 10, 2026. A tax cap question went to Londonderry voters on November 3, 2026.
   - citation: Londonderry School District Deliberative Session - Friday, February 6, 2026 (posted 2026-02-03)
   - source: https://news.londonderry.org/?p=598
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Londonderry
   - note: Page text: "The Londonderry School District will hold it's Annual Meeting on Friday, February 6, 2026 at 7:oo PM in the Cafe at Londonderry High School. | ...warrant articles ... that you will find next week when you go to vote on March 10th, 2026." Londonderry is NOT on the NHMA/DRA SB2 school district list, but the district's own posts describe a deliberative session plus a March ballot vote (SB2 form). Coordinator: flag the discrepancy. March vote post: https://news.londonderry.org/2026/03/04/simple-and-quick-explanation-of-the-march-2026-school-district-warrant-and-questions ; tax cap: https://news.londonderry.org/2026/10/19/superintendent-fall-newsletter-2026-part-3a-understanding-the-tax-cap-question Raw copy: raw/districts/batch-4/londonderry-news-deliberative-2026.txt; raw/districts/batch-4/londonderry-news-march-2026-warrant.txt; raw/districts/batch-4/londonderry-news-taxcap.txt
78. The Madison School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Madison
   - note: Statewide list only; the district's own voting page was not found. Checked: SAU 13 Madison board pages (Google Sites) list agendas/minutes but no 2026 deliberative session or ballot date was found. NHMA/DRA list shows Madison as SB2.
79. In Manchester, there is no voter budget vote for schools. The Board of School Committee adopts the school budget and submits it on the Mayor's schedule under the City Charter. The Board of Mayor and Aldermen then accepts it, or rejects it and sets a maximum amount.
   - citation: MSD Policy Fiscal 901 Annual Budget [DB]
   - source: https://www.mansd.org/page/msd-policy-fiscal-901-annual-budget
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Manchester
   - note: Page text: "The Board shall submit its budget proposal in accord with the budget schedule established by the Mayor under the City Charter. The Budget shall be subject to the approval of the Board of Mayor and Aldermen." City with charter tax cap (NHMA list). Policy also requires two public hearings. News (manchester.inklink.news) reported FY2027 budgets finalized June 2026 after a tax cap override; not cited as source. FY2027 budget documents at https://www.mansd.org/page/finance-budgets. Raw copy: raw/districts/batch-1/manchester-policy-901-annual-budget.txt
80. The Marlborough School District holds a traditional annual district meeting. In 2026 the district meeting was on March 3 at 7:00 PM, after a budget public hearing on January 26; school district elections were on March 10, 2026.
   - citation: SAU 29 - 2026 District Meeting Dates (revised 11/25/25)
   - source: https://docs.google.com/document/d/1jZKVq6Q_oNJ_qnSUXkGZIPErAnGBQLntiV2R0Qc_lZM/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlborough
   - note: Page text: "Marlborough March 3 7:00PM February 16 February 2 January 21 January 30 January 26 7:00PM" Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/sau29-district-meetings.txt
81. The Marlow School District holds a traditional annual district meeting. In 2026 the district meeting was on March 12 at 7:00 PM, after a budget public hearing on February 2; school district elections were on March 10, 2026.
   - citation: SAU 29 - 2026 District Meeting Dates (revised 11/25/25)
   - source: https://docs.google.com/document/d/1jZKVq6Q_oNJ_qnSUXkGZIPErAnGBQLntiV2R0Qc_lZM/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlow
   - note: Page text: "Marlow March 12 7:00PM February 25 February 9 January 21 January 30 February 2 7:00PM" Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/sau29-district-meetings.txt
82. The Mascenic Regional School District votes by official ballot (SB2). Its FY28 (2027-28) budget timeline sets the public hearing for January 11, 2027, the deliberative session for Wednesday, February 3, 2027 at 6 p.m. in the Mascenic Regional High School auditorium (snow date February 4), and voting day for Tuesday, March 9, 2027.
   - citation: Mascenic Regional School District - FY28 Budget Timeline (Budget Information > FY28 Budget Information)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/2060/Mrsd/b32c6dc3-d822-485e-9f13-19b90a2ba4a0/FY28-BudgetTimeline.docx.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mascenic Regional
   - note: Page text: "6:00pm Deliberative Session at MRHS Auditorium (snow date Thursday February 4, 2027) ... Tuesday March 9, 2027 -Voting Day as required by law (the second Tuesday in March)" Folder: https://www.mascenic.org/documents/school-board/budget-information/fy28-budget-information/31848924. The timeline labels January 11, 2027 a Tuesday (it is a Monday). 2026 dates not checked. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-2/mascenic-fy28-timeline.txt
83. The Mascoma Valley Regional School District holds a deliberative session before its vote (official ballot, SB2). For the 2027-28 budget, the budget committee's public hearing is scheduled for January 13, 2027 and the deliberative session for Saturday, January 30, 2027 at 9 a.m. in the Mascoma Valley Regional High School auditorium (snow date February 1, 2027). The 2026 dates and the 2027 voting date were not found on the district site.
   - citation: Mascoma Valley RSD - 2026-2027 Budget Committee Calendar of Events (linked from the Budget Committee page's 2026-2027 Budget Meeting Packets folder)
   - source: https://docs.google.com/spreadsheets/d/1Labiza6Pw3sBDewZ3YyBqLtSlvKPT4GZ-SNo5WD-QQw/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mascoma Valley Regional
   - note: Page text: "Jan. 30, 2027','Deliberative Session" Budget Committee page: https://www.mascomaschools.org/school-board/budget-committee. SB2 status from NHMA/DRA list (Mascoma); the calendar itself shows a deliberative session, which happens only under SB2. Raw copy: raw/districts/batch-2/mascoma-budget-calendar-2026-27.csv
84. The Mason School District votes by official ballot (SB2); its 2026 first session (deliberative session) on the budget and warrant articles was held Saturday, February 7, 2026, at 9:00 a.m. in the Mason Elementary School multipurpose room.
   - citation: Mason School District, 2026 Deliberative Session Posting (Budgets & Reports page)
   - source: https://4.files.edl.io/1b72/04/08/26/035019-2a70d138-4dda-434d-8a62-231a06c27bf3.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mason
   - note: Page text: "Notice is hereby given that the First Session, the DELIBERATIVE SESSION for discussion on the budget and warrant articles will be held Saturday February 07, 2026 at 9:00 a.m. at the Mason Elementary School Multi Purpose Room" The 2026-2027 Warrant Articles PDF is a scan with no extractable text, so the ballot vote date was not confirmed. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/mason-deliberative-posting-2026.txt; raw/districts/batch-3/mason-budgets-reports.txt
85. The Merrimack School District votes by official ballot (SB2). In 2026, the deliberative session was on Tuesday, March 3, 2026 at James Mastricola Upper Elementary School. Ballot voting was on Tuesday, April 14, 2026, at Merrimack Middle School or Merrimack High School.
   - citation: Merrimack School District Warrant, March 3, 2026 (Deliberation) and April 14, 2026 (Voting)
   - source: https://drive.google.com/file/d/1jCWBGitTYjSK8t309NC6E8sL1hBHee-N/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack
   - note: Page text: "meet at the James Mastricola Upper Elementary School in said District on Tuesday March 3, 2026, at 7:00 p.m. for Session 1 (Deliberation), to discuss the matters to be voted on by official ballot; and to meet at the designated polling sites, Merrimack Middle School, or Merrimack High School on Tuesday, April 14, 2026, Session 2 (Voting)" Scanned PDF; quote transcribed from page 1 image (raw/districts/batch-1/merrimack-warrant-2026-27-page1.jpg). Linked as '26-27 Warrant' from https://www.sau26.org/departments/finance. On NHMA/DRA SB2 list. 2027 dates not found on district site. Raw copy: raw/districts/batch-1/merrimack-warrant-2026-27.pdf
86. The Merrimack Valley School District held a traditional annual district meeting on Thursday, March 5, 2026, at 7 pm at Merrimack Valley High School. Polls for the moderator and school board elections were open from 11 am to 7 pm. The 2026 warrant included a petitioned article asking whether to adopt official ballot voting (SB2); the district's posted pages did not show the result.
   - citation: Merrimack Valley School District 2026 Annual Report - Warrant for Annual District Meeting, March 5, 2026
   - source: https://drive.google.com/file/d/1P82wi-vCYJExipzNQDwTwCyBLqYbK7T9/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Merrimack Valley
   - note: Page text: "You are hereby notified to meet at the Merrimack Valley High School on Thursday the 5th day of March 2026 at seven o'clock in the evening to act on the following subjects. The polls will be open for balloting on Articles I and II from 11:00 a.m. to 7:00 p.m." Article III: 'Shall we adopt the provisions of RSA 40:13 (known as SB 2) ... (By Petition) (3/5 Majority Vote Required)'. Result not found on district site; check before stating the 2027 form. Not on NHMA/DRA SB2 list (Jan 2026). Raw copy: raw/districts/batch-1/mvsd-2026-annual-report.txt
87. The Middleton School District votes by official ballot (SB2). Its 2026 deliberative session was on Saturday, February 7, 2026 at 10:00 am at Middleton Elementary School, and official ballot voting was on Tuesday, March 10, 2026, 7:00 am to 7:00 pm at the Old Town Hall, with the town meeting.
   - citation: Middleton School District Warrant 2026 (MSD FY2027 - Warrant Signed), linked from https://sites.google.com/a/sau69.org/sau-69---middleton-school-district/school-board/annual-meeting
   - source: https://drive.google.com/file/d/1bMACUcO6lxGLTK3XFuQ6br-HWnXwIypa/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Middleton
   - note: Page text: "You are hereby notified to meet at Middleton Elementary School, in Middleton, New Hampshire, on Saturday, the 7th day of February 2026, at 10:00 AM. ... Voting on warrant articles I through VIII shall be conducted by official ballot and will occur in conjunction with the town meeting to be held on Tuesday, the 10th day of March 2026." Scanned PDF read from the Drive viewer image. On NHMA/DRA SB2 list. Raw copy: raw/districts/batch-5/middleton-warrant-2026.pdf; raw/districts/batch-5/middleton-annual-meeting.txt
88. The Milan School District holds a traditional annual meeting: in 2026 the business session was on March 9, 2026, at 6:30 p.m. in the Milan Village School gymnasium, and official ballot voting (for officers) was on March 10, 2026, 11 a.m.-7 p.m. at Milan Village School.
   - citation: 2024-2025 Milan Annual School District Report (contains the 2026 warrant), Milan School Board site
   - source: https://drive.google.com/file/d/1Bx8tKI2IgtBT-YsnTl3V33uSSKKir2Lb/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milan
   - note: Page text: "First Session of Annual Meeting (Transaction of All Other Business) Date: March 9, 2026 Time: 6:30 PM Location: Milan Village School, 11 Bridge St. Details: Gymnasium Second Session of Annual Meeting (Official Ballot Voting) Date: March 10, 2026 Time: 11:00am- 7:00pm" Not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-3/milan-annual-report-2024-25.txt
89. The Milford School District uses official ballot voting (SB2). Its 2026 deliberative session was held Thursday, February 5, 2026, at 7:00 PM in the Milford High School cafeteria; attendance was required to participate and vote. The school district's 2026 ballot voting date was not found on the district site.
   - citation: Milford School District calendar event - School Deliberative Session (February 5, 2026)
   - source: https://hp.milfordk12.org/apps/events/2026/2/5/35673525/?id=0
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milford
   - note: Page text: "The Milford School District Deliberative Session will be held on Thursday, February 5, 2026 at 7:00 PM in the MHS Cafeteria." NHMA/DRA list: SB2. Town of Milford voter page (Wayback snapshot 2026-01-25, raw milford-town-voterinfo-wb20260125.txt) gives 'Tuesday March 10th, 2026 - SESSION II - TOWN VOTE' at Milford High School, 6 am-8 pm; it does not mention the school district, so not used in the statement. Deliberative packet PDF (scanned) and FY27 warrant PDF (scanned) saved but have little extractable text. Raw copy: raw/districts/batch-6/milford-delib-2026.txt
90. The Milton School District votes by official ballot (SB2). Its 2026 deliberative session was on Saturday, February 7, 2026 at 9:00 am in the Nute Middle High School and Library cafeteria, and the official ballot vote was on Tuesday, March 10, 2026, 8:00 am to 7:00 pm, in the Nute Middle High School gymnasium.
   - citation: FY 27 Milton School District Warrant (linked from https://www.sau64.org/o/sau64/page/budgetinformation)
   - source: https://aptg.co/NV_fLq
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milton
   - note: Page text: "You are hereby notified to meet at the Nute Middle High School and Library Cafeteria in said District on Saturday, the 7th day of February 2026, at 9:00 AM. ... on Tuesday, March 10, 2026, between the hours of 8:00 AM and 7:00 PM to vote by official ballot" On NHMA/DRA SB2 list. Budget page also lists 'Deliberative Session Minutes February 7, 2026'. Raw copy: raw/districts/batch-5/milton-warrant-fy27.pdf; raw/districts/batch-5/milton-warrant-fy27.txt; raw/districts/batch-5/milton-budget.txt
91. The Monadnock Regional School District votes by official ballot (SB2). Its 2026 deliberative session was held February 7, 2026 in the Monadnock Regional Middle/High School auditorium in Swanzey, and the ballot vote was March 10, 2026.
   - citation: MRSD - 2026 Deliberative & Election Information; February 7, 2026 Deliberative Minutes
   - source: https://www.mrsd.org/budget-voting/2026-deliberative-election-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Monadnock Regional
   - note: Page text: "Deliberative Session February 7, 2026 ... March 10th, 2026 Sample Ballots (All Towns)" Minutes PDF: https://www.mrsd.org/fs/resource-manager/view/97d4cf81-018f-4891-831d-c02741d6b3df. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-2/mrsd-2026-deliberative-minutes.txt; raw/districts/batch-2/mrsd-2026-voting.txt
92. The Mont Vernon School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mont Vernon
   - note: Statewide list only; the district's own voting page was not found. Checked: No voting information on the SAU 39 Mont Vernon School Board page. NHMA/DRA list (Jan 2026): Mont Vernon school district is SB2.
93. The Moultonborough School District decides its budget at a traditional annual school district meeting. In 2026 the meeting was held March 14, 2026, at 9:00 a.m. in the Community Auditorium at Moultonborough Academy.
   - citation: Moultonborough School District, School Warrant - March 14, 2026 (linked from SAU 45 Business Office page, https://www.sau45.org/pages/95ecc2a1-e316-41f8-991c-f11dd5bd6adc)
   - source: https://drive.google.com/file/d/1fTtj99vR69Fod1fxcEouV9ZOVRh5D6Mq/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Moultonborough
   - note: Page text: "You are hereby notified to meet at the Community Auditorium at Moultonborough Academy on the 14th day of March, 2026 at 9:00 A.M." Not on the NHMA SB2 list. Article IV of the 2026 warrant asked voters to adopt an open enrollment program (RSA 194-D) for the district's three schools; outcome not checked. Raw copy: raw/districts/batch-8/moultonborough-warrant-2026.txt
94. Nashua is a city: the Nashua Board of Education prepares the school budget and sends it to the city's Board of Aldermen; there is no school district meeting or ballot vote. For 2026-27 the Board of Education's budget committee began on February 17, 2026, held a public hearing on March 9, 2026, and met March 11, 2026 to approve the budget before sending it to the aldermen.
   - citation: Nashua School District - NSD Operating Budget
   - source: https://www.nashua.edu/our-district/board-of-education/nsd-operating-budget
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nashua
   - note: Page text: "On Monday, March 9, 2026, a public hearing for comment on the proposed operating budget will be held at 6:00 pm at Nashua High School North (Board Room). ... The BOE Budget Committee will reconvene on Wednesday, March 11, 2026 at 6:00 pm for budget review and approval before sending it to the Board of Alderman." NHMA/DRA list: city with charter tax/budget cap. FY27 Budget Notebook lists a presentation to the Board of Aldermen on 5-5-26. Raw copy: raw/districts/batch-2/nashua-operating-budget.txt
95. The Nelson School District holds a traditional annual district meeting. In 2026 the district meeting was on March 6 at 7:00 PM, after a budget public hearing on January 14; school district elections were on March 10, 2026.
   - citation: SAU 29 - 2026 District Meeting Dates (revised 11/25/25)
   - source: https://docs.google.com/document/d/1jZKVq6Q_oNJ_qnSUXkGZIPErAnGBQLntiV2R0Qc_lZM/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nelson
   - note: Page text: "Nelson March 6 7:00PM February 19 February 4 January 21 January 30 January 14 5:00PM" Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/sau29-district-meetings.txt
96. The New Boston School District uses official ballot voting: for 2025 its first (deliberative) session was held on February 4, 2025 at New Boston Central School and the ballot vote on March 11, 2025. The 2026 dates were not found on the district's site.
   - citation: 2025 New Boston School District Warrant Article Voters' Guide (FY26)
   - source: https://www.sau19.org/attachments/article/751/NBSD%20-FINAL%20-Voters%20Guide%20FY%2026%20School%20Year%202-5-2025_247.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Boston
   - note: Page text: "You are hereby notified to meet on Tuesday, February 4, 2025, in the Tom Mansfield Gym at New Boston Central School, at 7:00 P.M. for the first session of the School District Annual Meeting, also known as the first Deliberative Session" Older year only (FY26 budget, voted March 2025). The NHMA/DRA list also shows New Boston as SB2. 2026 searches found only a third-party tracker noting a January 2026 'Election/Deliberative Session Information' news item; the SAU 19 finance page loads documents by JavaScript. Raw copy: raw/districts/batch-7/newboston-voters-guide-fy26.txt
97. The Newfields School District uses official ballot voting (SB2). For the fiscal 2027 budget, its public hearing was January 14, 2026, its deliberative session was February 5, 2026, at Newfields Elementary School, and voting was on Tuesday, March 10, 2026, 8:00 a.m. to 7:00 p.m., at Newfields Town Hall.
   - citation: NES Budget flyer (Annual Budget & Voting Information), in the Newfields 2026-2027 folder linked from SAU 16 Newfields 'Budget Archives & Annual Financial Reports'
   - source: https://drive.google.com/file/d/1HloYZrZFcHpv5vPKdHpWEvczHbyCQXE3/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newfields
   - note: Page text: "Newfields residents vote to move the NES budget and warrant articles to the ballot." Flyer dates: 'Wednesday, January 14, 2026 @ 6:00 pm', 'Tuesday, March 10, 2026 8:00 am - 7:00 pm', 'Thursday, February 5, 2026 @ 6:00 pm'; folder has '2026 NES Deliberative Minutes Feb. 5, 2026.pdf'. Raw copy: raw/districts/batch-8/newfields-budget-flyer-2026.txt
98. The Newfound Area School District uses the official ballot (SB2) form. Its 2026 first (deliberative) session was on January 31, 2026, at Newfound Regional High School, and the second session (official ballot voting) was on March 10, 2026.
   - citation: SAU 4 - 2026-2027 School Budget Information (deliberative session minutes; 2026 Annual School District Meeting Calendar)
   - source: https://www.sau4.org/school-board/annual-budget-process/2026-2027-school-budget-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newfound Area
   - note: Page text: "Newfound Area School District First Deliberative Session 2026-2027 School Year January 31, 2026 ~ 10 am NRHS Auditorium | Second Session – Official Ballot Voting Second Tuesday in March March 10, 2026" Budget hearing January 12, 2026. Minutes: https://drive.google.com/file/d/19sNQlQEEHZzykjG59vy6p4HmkBnq_a_W ; calendar: https://drive.google.com/file/d/19ARW_WlDM2vka6hbkb97J63i3zcx-wqH . Page also has a '2027 Budget Committee Meetings' page; 2027 vote dates not posted. Raw copy: raw/districts/batch-4/newfound-2026-deliberative-minutes.txt; raw/districts/batch-4/newfound-2026-annual-meeting-calendar.txt; raw/districts/batch-4/sau4-budget-2026-27.txt
99. The Newmarket School District uses official ballot voting (SB2). In 2026 its first (deliberative) session was held Saturday, January 31, 2026, at 10:00 a.m. at Newmarket Junior Senior High School, and the official ballot vote was on Tuesday, March 10, 2026, 7:00 a.m. to 7:00 p.m., at the Town Hall Auditorium, with the town election.
   - citation: Newmarket School District 2026 School Warrant (linked from 'School Election and Budget Information', https://www.newmarket.k12.nh.us/school-board/election)
   - source: https://www.newmarket.k12.nh.us/school-board/files/documents/2026%20SCHOOL%20WARRANT%20ARTICLES%20Signed%20Dated.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newmarket
   - note: Page text: "The first session, for the transaction of all business other than voting by official ballot, shall be held Saturday, January 31, 2026; at 10:00 a.m. at the Newmarket Junior Senior High School." Warrant is a scan (OCR). The election page has a '2027 School District Election and Budget' heading with 'Links will be updated as information is made available.' Raw copy: raw/districts/batch-8/newmarket-warrant-2026.txt; raw/districts/batch-8/newmarket-budget-flyer-2026.txt
100. The Newport School District uses the official ballot (SB2) form. Its 2026 deliberative session (session 1) was on January 31, 2026, at 9:00 AM in the Newport Middle High School gym, and voting day (session 2) was on March 10, 2026, starting at 8:00 AM at the LaValley Family Community Center.
   - citation: Newport School District - School Elections and Voter Information
   - source: https://www.sau43.nh.gov/page/voter-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newport
   - note: Page text: "Deliberative Session-1 Date & Time: January 31, 2026, at 9:00 AM (Snow Date February 6, 2026) Location: NMHS Gym ... Voting Day Session-2 Date & Time: March 10, 2026, starting at 8:00 AM Location: LaValley Family Community Center" On NHMA/DRA SB2 list. 2027 dates not posted. Raw copy: raw/districts/batch-4/newport-pages.txt
101. The North Hampton School District uses the official ballot (SB2) form: its 2026 deliberative session was held on Tuesday, February 3, 2026 at the North Hampton School cafeteria, and official ballot voting was on Tuesday, March 10, 2026, 8:00 a.m. to 7:00 p.m., at the North Hampton School gymnasium.
   - citation: SAU 21 - 2026-27 School District Voting Information (North Hampton tab)
   - source: https://www.sau21.nh.gov/departments/business/voting-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district North Hampton
   - note: Page text: "Date: Tuesday, February 3, 2026 Time: 7:00 PM Location: North Hampton School Cafeteria" Snow date Wednesday, February 4, 2026. Raw copy: raw/districts/batch-7/sau21-voting-information.txt
102. The Northumberland School District decides its budget at a traditional annual school district meeting where voters act on the warrant articles. The most recent dates posted were for 2025: the meeting was held on Saturday, March 15, 2025 at Groveton High School. No 2026 or 2027 dates were posted when checked.
   - citation: SAU #58 Notice of Meetings, March 2025 Annual School District Meetings (School Boards > Annual Meeting Information > Annual Meeting Dates)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3822/Sau58/ded2fb81-271c-48f3-adb0-26ab4d5fd39d/2025_Annual_School_District_Meetings.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Northumberland
   - note: Page text: "ANNUAL SCHOOL DISTRICT MEETINGS VOTERS ARE HEREBY NOTIFIED to meet in their respective school districts at the dates, places, and times listed below for the purpose of acting on the school district warrant articles for the 2025-2026 fiscal year: ... Northumberland – Saturday, March 15, 2025 – 9:00 a.m. – Groveton High School, Ryan Memorial Gymnasium." Folder: https://www.sau58.org/documents/school-boards/annual-meeting-information/annual-meeting-dates/18860503. Only 2025 materials posted (warrants are scanned images). Not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-2/sau58-2025-annual-meetings.txt
103. The Northwood School District uses official ballot voting (SB2). Its 2026 deliberative session was held Thursday, February 5, 2026, at 6:00 p.m. at Northwood School, and the official ballot vote was on Tuesday, March 10, 2026, 7:00 a.m. to 7:00 p.m., at Northwood Elementary School.
   - citation: Northwood School District 2026 Deliberative Session Guide/Packet (linked from SAU 44 Financial Reports/Budget, https://www.sau44.org/o/sau/page/reports)
   - source: https://aptg.co/xX6DT7
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Northwood
   - note: Page text: "You are hereby notified to meet at the Northwood Elementary School on Tuesday, the 10th day of March, 2026 to vote by official ballot on Articles 1 to 4 as amended." Packet: 'meet at the Northwood School on Thursday, the 5th day of February at 6:00 PM, for the Annual School District Deliberative Session'. SAU 44 reports page also lists 'FY2028 Budget Working Documents'. Raw copy: raw/districts/batch-8/northwood-deliberative-packet-2026.txt
104. The Nottingham School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nottingham
   - note: Statewide list only; the district's own voting page was not found. Checked: Financial Reports page links a '2026 Warrant Articles' PDF that is a scanned image (no text). NHMA/DRA list (Jan 2026): Nottingham school district is SB2.
105. The Oyster River Cooperative School District votes by official ballot (SB2). Its 2026 deliberative session (Annual Meeting Session I) was held February 3, 2026, and voting was on Tuesday, March 10, 2026 in Durham, Lee and Madbury.
   - citation: ORCSD - Voting Day and Ballot Information - March 10, 2026
   - source: https://www.orcsd.org/news/1822868/voting-day-and-ballot-information-march-10-2026
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Oyster River Coop
   - note: Page text: "operating budget will be on the ballot this coming Tuesday, March 10, 2026. ... All warrants were presented and discussed during the February 3 [https://www.youtube.com/watch?v=Yu0yd_Rlp4c] Annual Meeting Session I (Deliberative Session)." NHMA/DRA list: SB2 (Oyster River). Raw copy: raw/districts/batch-2/orcsd-voting-2026.txt
106. The Pasquaney School District (Bridgewater, Groton and Hebron) decides its budget at a traditional annual school district meeting: in 2026 officers and ballot questions were voted at each town's polling place on Tuesday, March 10, 2026, and the annual school district meeting was held Tuesday, March 17, 2026, at 6 p.m. in the Bridgewater-Hebron Village School gymnasium.
   - citation: Pasquaney School District Annual Report, March 17, 2026 - Warrant 2026-2027
   - source: https://aptg.co/_b-b0k
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pasquaney
   - note: Page text: "to meet at the Bridgewater-Hebron Village School Gymnasium on 25 School House Road in Bridgewater, New Hampshire on Tuesday, March 1 7, 2026, at 6 PM for the Annual School District Meeting" Quote keeps the PDF's text spacing ('March 1 7'). The district was newly formed; its inaugural annual meeting was March 25, 2025. Not on the NHMA SB2 list. Raw copy: raw/districts/batch-8/pasquaney-annual-report.txt
107. The Pelham School District uses the official ballot (SB2) form: its 2026 deliberative session was held on Wednesday, February 4, 2026 at 7:00 p.m. in Sherburne Hall, and voting was on Tuesday, March 10, 2026, 7 a.m. to 8 p.m., at Pelham High School.
   - citation: Pelham School District - Voting & Elections (2026 Deliberative Session Posting)
   - source: https://www.pelhamsd.org/VotingElections.aspx
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pelham
   - note: Page text: "Wednesday, February 4, 2026 Deliberative Session starts at 7:00pm in Sherburne Hall" Voting page: 'Voting Day is Tuesday March 10th 2026 from 7AM until 8PM at Pelham High School'. Deliberative posting PDF: https://www.pelhamsd.org/Downloads/Deliberative%202026.pdf. Page also lists default budget (MS-DS) documents. Raw copy: raw/districts/batch-7/pelham-voting.txt; raw/districts/batch-7/pelham-2026-deliberative-posting.txt
108. The Pembroke School District decides its budget at an annual school district meeting; its 2026 annual meeting was held on March 7, 2026.
   - citation: SAU 53 - Pembroke 2026 School District Meeting (Annual Meeting Budget Packet)
   - source: https://sau.sau53.org/pages/b5a514c5-6631-4be8-9d15-7fd4745ecb7f
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pembroke
   - note: Page text: "Pembroke School District FY2627 Annual Meeting Budget Information March 7th,2026" Packet PDF embedded on the page: https://drive.google.com/file/d/1abOoCuDxgKEvsarde-fZBFqI_32BzChd. Pembroke is not on the NHMA/DRA SB2 list. Time and place of the meeting were not in the text extracted (the 'School District Meeting Reminder' file was a scanned image). Raw copy: raw/districts/batch-7/sau53-pembroke-2026-annual-meeting-packet.txt
109. The Pemi-Baker Regional School District votes by official ballot (SB2). Its 2026 deliberative session was held Tuesday, February 3, 2026, at 6:30 p.m. at Plymouth Regional High School, and official ballot voting was held Tuesday, March 10, 2026, at polling places in Ashland, Campton, Holderness, Plymouth, Rumney, Thornton and Wentworth.
   - citation: Pemi-Baker Regional School District 2026 Warrant ('2026-2027 Warrant Articles' on the PRHS Budget Information page https://prhs.pemibaker.org/school-board/budget-information)
   - source: https://drive.google.com/file/d/18H7G1QTwK8BX2_6mSdPmeZrtC6HPWRN_/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pemi-Baker Regional
   - note: Page text: "First Session of Annual Meeting (Deliberative Session) Date: Tuesday, February 3, 2026 Time: 6:30 p.m. Location: Plymouth Regional High School Second Session of Annual Meeting (Official Ballot Voting) Date: Tuesday, March 10, 2026" NHMA/DRA list: SB2. Raw copy: raw/districts/batch-6/pemibaker-warrant-2026.txt
110. The Pittsfield School District votes by official ballot (SB2). Its 2026 deliberative session was held February 5, 2026 at 6 p.m. in the Pittsfield Middle High School cafeteria, and voting was March 10, 2026 at the Middle High School. A special meeting on a collective bargaining agreement followed, with a deliberative session on July 7, 2026 and official ballot voting on August 4, 2026.
   - citation: Pittsfield School District (SAU 51) - News
   - source: https://sau51.org/news/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pittsfield
   - note: Page text: "VOTING: March 10, 2026 PMHS, 23 Oneida Street, Pittsfield NH 7 am to 7 pm The Pittsfield School District Deliberative Session will take place at 6:00 pm on February 5, 2026 in the PMHS Cafeteria ... Deliberative Session: July 7, 2026 ... Official Ballot Voting: August 4, 2026" NHMA/DRA list: SB2. Raw copy: raw/districts/batch-2/pittsfield-news.txt
111. The Plymouth School District holds a traditional annual school district meeting. The 2026 meeting was set for Monday, March 2, 2026, at 7:00 p.m. at Plymouth Elementary School.
   - citation: Plymouth Local School 2026 Warrant ('Plymouth Warrant Articles' on https://pes.pemibaker.org/school-board/budget-information)
   - source: https://drive.google.com/file/d/1WceG6239toZP7k69Woj0obSFk2kInBwd/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Plymouth
   - note: Page text: "the Annual School District Meeting will be held as follows: Date: Monday, March 2, 2026 Time: 7:00 p.m. Location: Plymouth Elementary School" Plymouth's high school budget is voted separately as part of the Pemi-Baker Regional School District (SB2). NHMA/DRA list: Plymouth not SB2. Raw copy: raw/districts/batch-6/plymouth-warrant-2026.txt
112. Portsmouth's school budget is approved through city government: on June 8, 2026, the City Council adopted the fiscal 2027 General Fund budget of $157,856,390, including $71,637,655 for the School Department.
   - citation: City of Portsmouth, FY27 Adopted Budget Resolutions
   - source: https://files.portsmouthnh.gov/finance/fy27/AdoptedBudget6082026%20FINAL.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Portsmouth
   - note: Page text: "The following FY27 budget resolutions were adopted by the City Council on June 8, 2026." Line 'SCHOOL $71,637,655'; General Fund adopted 8-1. Portsmouth has a charter tax/budget cap (NHMA list). Raw copy: raw/districts/batch-8/portsmouth-fy27-adopted-budget.txt
113. The Profile School District holds a traditional annual district meeting. In 2026 the annual election (polls 7:00-7:30 P.M.) and school district meeting were held on March 19, 2026, where voters of Bethlehem, Easton, Franconia and Sugar Hill acted on the budget by voice vote. A SAU 35 budget hearing was held November 5, 2026, and individual district budget hearings are planned for January and February 2027.
   - citation: Profile School District 2026 School District Meeting Minutes, March 19, 2026 (linked from Profile School's School Board Minutes page)
   - source: https://drive.google.com/file/d/17xieCb39xkTDmkLTIw0bM9CXzXBh5ZFR/preview
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Profile
   - note: Page text: "The Profile School District held their annual election and meeting on March 19, 2026. ... The District Moderator announced the commencement of the 2026 School District Meeting at 7:30 P.M. | Individual SAU35 School District Budget Hearings will be held in January & February 2027" Minutes are a scan; transcribed by hand. The minutes elect board members 'from the pre-existing District of Bethlehem' and 'of Lafayette' - coordinator may want to check whether a district reorganization is under way. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/profile-2026-03-19-annual-minutes.pdf; raw/districts/batch-4/profile-2026-03-19-annual-minutes-transcription.txt; raw/districts/batch-4/profile-2026-11-05-budget-hearing.txt
114. Prospect Mountain High School is run jointly by the Alton and Barnstead school districts under a Joint Maintenance Agreement. Its operating budget is recommended by the JMA Budget Committee and included in each district's own budget, so voters approve it at the Alton and Barnstead district votes; in 2026 Barnstead's annual meeting was on March 21, 2026. Cost items in the Prospect Mountain teachers' contract required approval by both districts (Alton 45.55%, Barnstead 54.45%).
   - citation: Barnstead School District Annual Report 2024-2025, printed page 74 (2026 warrant)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3643/Pmsau/8956d01e-faf5-4e8d-94b0-e905a0106f80/Barnstead-Annual-Report-2024-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Prospect Mountain JMA
   - note: Page text: "the net appropriation for the Prospect Mountain High School operating budget which is included in the gross budget amount listed above and recommended by the Joint Maintenance Agreement (JMA) Budget Committee ... The adoption of this Article shall be contingent upon both the Alton (45.55%) and Barnstead (54.45%) Districts approving the cost items" Alton's 2026 vote date was not checked (Alton is in another batch). The SAU 301 'Annual district meetings' link points to an Alton deliberative session page. Raw copy: raw/districts/batch-5/barnstead-annual-report-2024-25-p73-warrant-2026.jpg; raw/districts/batch-5/pmsau-policies-business.txt
115. The Raymond School District votes by official ballot (SB2). Its 2026 first (deliberative) session was held February 7, 2026 at Raymond High School, and the annual school election was March 10, 2026.
   - citation: Raymond School District - Voter Information (2026 Deliberative Session Minutes; 2026 School District Voting Results)
   - source: https://www.sau33.com/school-board/voter-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Raymond
   - note: Page text: "FIRST SESSION (DELIBERATIVE SESSION) February 7, 2026 ... Annual School Election March 10, 2026" PDFs: https://www.sau33.com/sites/g/files/vyhlif5441/f/uploads/2026_deliberative_session_minutes.pdf and .../school_district_results-2026.pdf. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-2/raymond-2026_deliberative_session_minutes.txt; raw/districts/batch-2/raymond-school_district_results-2026.txt
116. The Rivendell Interstate School District (Orford, NH, and Fairlee, Vershire and West Fairlee, VT) holds an annual district meeting under the New Hampshire-Vermont Interstate Compact. The 2026 meeting was on Saturday, March 21, 2026, at Rivendell Academy in Orford, NH. Polls for electing officers opened at 9:30 am, and the other business began at 10:00 am.
   - citation: Warrant, Annual District Meeting, Rivendell Interstate School District, March 21, 2026 (revised & approved 02-17-2026)
   - source: https://content.myconnectsuite.com/api/documents/2a37452773194edeb90b4cd31e858bfe.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rivendell
   - note: Page text: "are hereby notified and warned to meet at the Rivendell Academy, Orford, New Hampshire, on Saturday, March 21, 2026, for the purpose of holding the annual district meeting of the Rivendell Interstate School District pursuant to Article IV.G of the New Hampshire-Vermont Interstate Compact. The polls for the election of officers under Articles 1 and 2 will open at 9:30 a.m." Scanned PDF; quote transcribed from page image raw/districts/batch-1/rivendell-warrant-2026-p1.png. Linked from https://www.rivendellschool.org/voterinformation ('Annual Meeting - March 21, 2026'). Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-1/rivendell-warrant-2026.pdf
117. Rochester is a city, and the Rochester School District's budget is approved by the City Council. The district's FY2027 (2026-27) approved budget document labels the FY2027 figures 'City Council Approved' (summary dated June 10, 2026).
   - citation: Rochester School District - Annual Budget page, 'FY2027 Rochester School District Approved Budget' PDF (https://aptg.co/H61m2K)
   - source: https://www.rochesterschools.com/o/rsd/page/annual-budget
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rochester
   - note: Page text: "2027 CITY 2023 2024 2025 2026 COUNCIL EXPENDED EXPENDED EXPENDED BUDGET APPROVED" Quote is the column header of the budget summary (page 3 of PDF), as extracted; header words are split across lines in the PDF ('2027 CITY COUNCIL APPROVED'). Page 4 header reads 'FY 2027 ... City Council Budget ... Approved'. NHMA/DRA list: city with charter tax/budget cap. Raw copy: raw/districts/batch-6/rochester-fy2027-budget.txt
118. The Rollinsford School District votes by official ballot (SB2). In 2026 the first session (deliberative) of the annual meeting was on Tuesday, February 3, 2026, at 6:00 p.m. at Rollinsford Grade School, and the second session, voting by official ballot, was on Tuesday, March 10, 2026.
   - citation: Rollinsford Warrant Articles for FY2026-27 FINAL 1.23.26 (SAU 104 Budget 2026-2027 page)
   - source: https://drive.google.com/file/d/1oxyKBXs_YkS0CCDW_s9g1y05y3eHCxZn/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rollinsford
   - note: Page text: "You are hereby notified to meet on Tuesday, February 3, 2026, at 6:00 PM ... at the Rollinsford Grade School ... You are also hereby notified to meet again on Tuesday, March 10, 2026 for the second session of the Annual School District Meeting to vote by official ballot" Operating budget $7,134,902; default $7,085,923. Snow date in legal notice Feb 7 at 9:00 AM; warrant says 10:00 AM. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/rollinsford-warrant-2026.txt; raw/districts/batch-3/rollinsford-notice-2026.txt; raw/districts/batch-3/rollinsford-budget-2026-27.txt
119. The Rumney School District votes by official ballot (SB2). Its 2026 deliberative session was held Wednesday, February 4, 2026, at 6:00 p.m., and official ballot voting was held Tuesday, March 10, 2026, 8:00 a.m. to 7:00 p.m., both at Russell Elementary School.
   - citation: Rumney Local School 2026 Warrant ('Rumney Warrant Articles' on https://res.pemibaker.org/school-board/budget-information)
   - source: https://drive.google.com/file/d/1EWq-VFuc3Pk33lGmlo9WFB8j-6ieAYmA/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rumney
   - note: Page text: "First Session of Annual Meeting (Deliberative Session) Date: Wednesday, February 4, 2026 Time: 6:00 p.m. Location: Russell Elementary School Second Session of Annual Meeting (Official Ballot Voting) Date: Tuesday, March 10, 2026" NHMA/DRA list: SB2. Raw copy: raw/districts/batch-6/rumney-warrant-2026.txt
120. The Rye School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rye
   - note: Statewide list only; the district's own voting page was not found. Checked: SAU 50 Budgets page (https://www.sau50.org/pages/c7d00935-ed21-4ee4-82ae-56989fdbaaca) lists only FY26 (2025) documents for Rye and Greenland, and their 2025 warrant PDFs require a Google sign-in. No 2026 deliberative session or vote dates found. District is on the NHMA SB2 list.
121. The Salem School District uses the official ballot (SB2) form: its 2026 deliberative session was held on Thursday, February 5, 2026 at 7:00 p.m. at Salem High School's Seifert Performing Arts Center, and voting on the warrant articles was by official ballot on March 10, 2026, with town meeting voting.
   - citation: Salem School District - 2026-27 Salem School District Annual Meeting
   - source: https://sau57.org/board-26-27-annual
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Salem
   - note: Page text: "You are notified to meet at Salem High School in the Seifert Performing Arts Center Salem on Thursday, February 5, 2026 at 7:00 p.m. ... Voting on warrant articles 1 through 5 shall be conducted by official ballot to be held in conjunction with Town Meeting voting on March 10, 2026." Page refers to the Municipal Budget Committee's proposed 2026-2027 budget and to SB2 postponement rules. No 2027 dates posted. Raw copy: raw/districts/batch-7/salem-annual-meeting.txt
122. The Sanborn Regional School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Sanborn Regional
   - note: Statewide list only; the district's own voting page was not found. Checked: On NHMA/DRA SB2 regional list (official ballot), but no 2026 deliberative session or vote dates found: checked sau17.net home, School Board, Budget Committee, Board Meeting Archive and news pages (Apptegy site, rendered headless). Web search budget was exhausted before a targeted search.
123. The Seabrook School District uses the official ballot (SB2) form: its 2026 deliberative session was held on Monday, February 2, 2026 at the Seabrook Middle School gymnasium, and official ballot voting was on Tuesday, March 10, 2026, 7:00 a.m. to 7:00 p.m., at the Seabrook Recreation Center.
   - citation: SAU 21 - 2026-27 School District Voting Information (Seabrook tab)
   - source: https://www.sau21.nh.gov/departments/business/voting-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Seabrook
   - note: Page text: "Date: Monday, February 2, 2026 Time: 7:00 PM Location: Seabrook Middle School Gymnasium" Snow date Wednesday, February 4, 2026. Raw copy: raw/districts/batch-7/sau21-voting-information.txt
124. The Shaker Regional School District votes by official ballot (SB2) in two sessions. For the 2026-27 budget, the deliberative session was set for February 5, 2026 at 6:00 PM at Belmont High School (weather date February 7) and second-session ballot voting for March 10, 2026. For the 2027-28 budget, the calendar sets the deliberative session for February 4, 2027 (snow date February 6) and ballot voting for March 9, 2027.
   - citation: Shaker Regional School District 26-27 Budget Development Calendar (Updated), on the FY 2026-2027 Budget page
   - source: https://www.sau80.org/common/pages/GetFile.ashx?key=Z8dJAtE6
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Shaker Regional
   - note: Page text: "2/5/2026 6:00 PM BHS Deliberative Session ... 3/10/2026 All Day BHS Second Session Voting by Ballot" 2027 dates from 27-28 Budget Development Calendar https://www.sau80.org/common/pages/GetFile.ashx?key=U6NSAv5e (raw shaker-calendar-2728.txt: '2/4/2027 6:00 PM BHS Deliberative Session', '3/9/2027 All Day BHS Second Session Voting by Ballot'). Calendars are plans; whether the weather date was used was not checked. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-6/shaker-calendar-2627.txt
125. Somersworth is a city, and the Somersworth School District's budget goes to the City Council. The district presented its 2026-27 budget to the City Council on April 6, 2026, including a 'Tax Cap Compliant Budget' that meets the tax cap in the city charter (a 2.6% increase over the approved 2025-26 budget) alongside its proposed budget (an 8.9% increase).
   - citation: Somersworth School District 2026-2027 City Council Budget Presentation, April 6, 2026 (District Budget page, 2026-2027 Budget folder)
   - source: https://www.sau56.org/common/pages/GetFile.ashx?key=3sMsAQ09
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Somersworth
   - note: Page text: "Tax Cap Compliant Budget: The tax cap budget includes reductions to the proposed budget and current staff and programs in order to meet the tax cap based on the city charter." Folder also has a 'Mandatory Report to Voters on School Expenses' and a City Council and School Board joint workshop presentation. Date the City Council adopted the budget not found. NHMA/DRA list: city with charter tax/budget cap. Raw copy: raw/districts/batch-6/somersworth-council-budget-presentation-2026.txt
126. The Souhegan Cooperative School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Souhegan Cooperative
   - note: Statewide list only; the district's own voting page was not found. Checked: No voting information on the SAU 39 Souhegan Cooperative School Board page. NHMA/DRA list (Jan 2026): Souhegan is an SB2 regional district.
127. The South Hampton School District uses the official ballot (SB2) form: its 2026 deliberative session was held on Tuesday, February 3, 2026 in the Eleanor M. Batchelder Gymnasium, and official ballot voting was on Tuesday, March 10, 2026, 11:00 a.m. to 8:00 p.m., at South Hampton Town Hall.
   - citation: SAU 21 - 2026-27 School District Voting Information (South Hampton tab)
   - source: https://www.sau21.nh.gov/departments/business/voting-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district South Hampton
   - note: Page text: "Date: Tuesday, February 3, 2026 Time: 7:00 PM Location: Eleanor M. Batchelder Gymnasium" Snow date Thursday, February 5, 2026. Raw copy: raw/districts/batch-7/sau21-voting-information.txt
128. The Stark School District decides its budget at a traditional annual school district meeting where voters act on the warrant articles. The most recent dates posted were for 2025: the meeting was held on Tuesday, March 11, 2025 at the Stark Fire Station. No 2026 or 2027 dates were posted when checked.
   - citation: SAU #58 Notice of Meetings, March 2025 Annual School District Meetings (School Boards > Annual Meeting Information > Annual Meeting Dates)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3822/Sau58/ded2fb81-271c-48f3-adb0-26ab4d5fd39d/2025_Annual_School_District_Meetings.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stark
   - note: Page text: "ANNUAL SCHOOL DISTRICT MEETINGS VOTERS ARE HEREBY NOTIFIED to meet in their respective school districts at the dates, places, and times listed below for the purpose of acting on the school district warrant articles for the 2025-2026 fiscal year: ... Stark – Tuesday, March 11, 2025 – 5:30 p.m. – Stark Fire Station" Folder: https://www.sau58.org/documents/school-boards/annual-meeting-information/annual-meeting-dates/18860503. Only 2025 materials posted (warrants are scanned images). Not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-2/sau58-2025-annual-meetings.txt
129. The Stoddard School District decides its budget at a March annual meeting (not official ballot); SAU 24's fall 2026 public hearing slides on the tax cap describe the 'Public Hearing and March Meeting' budget process. The 2026 meeting date was not found in readable form.
   - citation: SAU 24 Stoddard Public Hearing presentation (RSA 32:5-i tax caps), fall 2026
   - source: https://www.sau24.org/school-boards/stoddard/files/documents/SAU%2024_Stoddard%20Public%20Hearing.pptx%20-%20Google%20Slides.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stoddard
   - note: Page text: "Budget process Public Hearing and March Meeting continue within the cap ... To exceed the cap A 3/5 majority at the March meeting" The 2026 Stoddard warrant (signed, posted March 2, 2026) is a scanned PDF with no text, so the meeting date could not be read. Not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-3/stoddard-public-hearing.txt; raw/districts/batch-3/stoddard-warrant-2026.txt
130. The Stratford School District decides its budget at a traditional annual school district meeting where voters act on the warrant articles. The most recent dates posted were for 2025: the meeting was held on Wednesday, March 12, 2025 at Stratford Public School. No 2026 or 2027 dates were posted when checked.
   - citation: SAU #58 Notice of Meetings, March 2025 Annual School District Meetings (School Boards > Annual Meeting Information > Annual Meeting Dates)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3822/Sau58/ded2fb81-271c-48f3-adb0-26ab4d5fd39d/2025_Annual_School_District_Meetings.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stratford
   - note: Page text: "ANNUAL SCHOOL DISTRICT MEETINGS VOTERS ARE HEREBY NOTIFIED to meet in their respective school districts at the dates, places, and times listed below for the purpose of acting on the school district warrant articles for the 2025-2026 fiscal year: ... Stratford – Wednesday, March 12, 2025 – 5:30 p.m. – Stratford Public School Multi Purpose Room." Folder: https://www.sau58.org/documents/school-boards/annual-meeting-information/annual-meeting-dates/18860503. Only 2025 materials posted (warrants are scanned images). Not on the NHMA/DRA SB2 list. Raw copy: raw/districts/batch-2/sau58-2025-annual-meetings.txt
131. The Stratham School District decides its budget at a traditional annual school district meeting: in 2026 the business session, where residents debated and voted on the fiscal 2027 budget and warrant articles, was held on Wednesday, March 4, 2026, at Stratham Memorial School, and school officials were elected by ballot on Tuesday, March 10, 2026.
   - citation: Stratham Local School 2026 Warrant (NH DRA form), in the Stratham 2026-2027 folder linked from SAU 16 Stratham 'Budget Archives & Annual Financial Reports'
   - source: https://drive.google.com/file/d/1Bu08mmYDyDlEya4R08wmMVLOESjgUSJA/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stratham
   - note: Page text: "Session of Annual Meeting (Transaction of All Other Business) Date: March 4, 2026 Time: 6pm Location: Stratham Memorial School" Warrant is OCR text. Flyer: 'SCHOOL DISTRICT TOWN MEETING Stratham residents will have an opportunity to comment on and vote for the SMS FY27 school budget and warrant articles at this meeting.' Public hearing January 28, 2026. Not on the NHMA SB2 list. Raw copy: raw/districts/batch-8/stratham-warrant-2026.txt; raw/districts/batch-8/stratham-budget-flyer-2026.txt
132. The Sunapee School District uses the official ballot (SB2) form: the first session (deliberative session) of its 2026 annual meeting was held on Monday, February 2, 2026 at 6 p.m. at the Sunapee Middle High School gymnasium, and ballot voting was on Tuesday, March 10, 2026, 8 a.m. to 7 p.m., at the David W. Sherburne Gymnasium.
   - citation: Sunapee School District Warrant 2026-2027 (draft), linked from Budget Information
   - source: https://www.sau85.org/UserFiles/Servers/Server_3299417/File/School%20Board/2026/26-27%20draft%20Warrants.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Sunapee
   - note: Page text: "on Monday, February 2, 2026, at 6 PM for the first session of the Annual School District Meeting to deliberate upon the articles, and to meet again at the David W. Sherburne Gymnasium located on Route 11 in said Sunapee, New Hampshire on Tuesday, March 10, 2026, between the hours of 8 AM and 7 PM" The file is labeled draft; the Budget Information page (https://www.sau85.org/schoolboard/budget_information) also says 'Deliberative Session February 2, 2026 Sunapee Middle High School 6:00pm'. Raw copy: raw/districts/batch-7/sunapee-2026-warrant-draft.txt; raw/districts/batch-7/sunapee-budget-information.txt
133. The Surry School District decides its budget at a traditional annual school district meeting, held just before the town meeting. The 2026 meeting was on March 12, 2026 at 7 pm, where voters took up a 2026-27 operating budget of $2,727,720 recommended by the School Board and Budget Committee.
   - citation: Surry School District Annual Meeting Minutes 2026 (linked from https://surry.nh.gov/surry-school-district/annual-school-district-meetings-reports/)
   - source: https://surry.nh.gov/wp-content/uploads/2026/06/SSD-Annual-Meeting-031226.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Surry
   - note: Page text: "Surry School District Annual Meeting March 12, 2026 Meeting called to order at 7 pm by School District and Town moderator Wayne Hartz. ... The school board meeting is scheduled for 30 minutes, with a town meeting following at 7:30." Not on NHMA/DRA SB2 list (on the official budget committee list). Raw copy: raw/districts/batch-5/surry-annual-meeting-minutes-2026.txt; raw/districts/batch-5/surry-annual-meetings.txt
134. The Tamworth School District holds an annual district meeting; the most recent date found on its pages was the 2024 meeting, held Wednesday, March 6, 2024 at 7 p.m. in the Brett School gymnasium. The 2026 meeting date was not found.
   - citation: Kenneth A. Brett School - High School Options Committee (Tamworth School District Notice)
   - source: https://sites.google.com/tamworth.k12.nh.us/welcome-ka-brett-school/high-school-options-committee
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Tamworth
   - note: Page text: "Following the Annual District Meeting which is scheduled for Wednesday March 6, 2024 at 7PM in the Brett School Gymnasium" Older year only. Tamworth is not on the NHMA/DRA SB2 list. SAU 13 board agenda pages (Google Sites) did not show 2026 meeting details. Raw copy: raw/districts/batch-7/tamworth-hs-options-committee.txt
135. The Thornton School District holds a traditional annual school district meeting. The 2026 meeting was set for Thursday, March 5, 2026, at 6:00 p.m. at Thornton Central School (per the district's 2026 warrant, a DRA draft dated December 22, 2025).
   - citation: Thornton Local School 2026 Warrant ('Warrant Articles' on https://tcs.pemibaker.org/school-board/agendasminutesbudgets)
   - source: https://drive.google.com/file/d/13DEyde8WySu_rCma0xFntSEoNfHzyVuO/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Thornton
   - note: Page text: "the Annual School District Meeting will be held as follows: Date: Thursday, March 5, 2026 Time: 6:00 p.m. Location: Thornton Central School" Warrant is marked DRAFT 12/22/2025. NHMA/DRA list: not SB2. Raw copy: raw/districts/batch-6/thornton-warrant-2026.txt
136. The Timberlane Regional School District votes by official ballot (SB2). Its 2026 deliberative session was held Thursday, February 5, 2026 at the Timberlane Performing Arts Center, and voting was on Tuesday, March 10, 2026 at polling places in Atkinson, Danville, Plaistow and Sandown. The budget public hearing was January 15, 2026.
   - citation: Timberlane Regional School District - Annual Meetings and Voting Information; 2026 TRSD Notice of Public Meetings
   - source: https://www.timberlane.net/about/annual-meetings-and-voting-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Timberlane Regional
   - note: Page text: "THURSDAY, FEBRUARY 5, 2026 7:00 PM ... The Board will meet immediately after the session to finalize the warrant for ballot. ... TUESDAY, MARCH 10, 2026" Notice PDF: https://www.timberlane.net/fs/resource-manager/view/d0ff318f-a84c-4227-89b6-6cafc0fe8f76. Warrant says voting on articles 1-18 is by official ballot. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-2/timberlane-2026-notice-public-meetings.txt; raw/districts/batch-2/timberlane-voting.txt
137. The Wakefield School District votes by official ballot (SB2). Its FY 2026-27 budget calendar scheduled the first (deliberative) session for Saturday, January 31, 2026 at 9 a.m. at the Opera House, and the second session (ballot voting) for Tuesday, March 10, 2026.
   - citation: Wakefield School District Budget Calendar FY 2026-27 (SAU/School Board > Annual Reports & Budgets > 2027 Budget Documents)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5761/Sau101/dd7f22da-2d32-4ab8-bf80-e187d1df9ded/Districts-Budget-Calendar-for-fy-26-27---Sheet1.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wakefield
   - note: Page text: "Saturday, January 31 (…between the first and second Saturdays following the last Monday in January, inclusive of those Saturdays 9:00 AM First Deliberative Session ... Tuesday, March 10 TBD Second Session Ballot Voting" Planned schedule dated 11/25/2025; the 2026 deliberative minutes and warrant PDFs in the same folder are scanned images, so the held dates could not be read. NHMA/DRA list: SB2. Raw copy: raw/districts/batch-2/wakefield-budget-calendar-fy27.txt
138. The Washington School District holds a traditional annual school district meeting. The 2026 meeting was held March 7, 2026, with officers elected by ballot during the meeting (polls open 9:05 to 11:30 AM). The district's FY2028 timeline sets the next annual meeting for March 6, 2027, with a budget hearing on February 8, 2027.
   - citation: March 7, 2026 Washington SD Annual Meeting minutes (signed), Washington FY2027 budget folder linked from https://sau34.org/pages/1102db1f-3615-46ca-993d-108850cd57f7
   - source: https://drive.google.com/file/d/1BJWk5EB4vsU5g20qKX5HvHGgKt_s2Fml/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Washington
   - note: Page text: "Annual School District Meeting Washington New Hampshire March 7, 2026 Moderator Guy Eaton called the meeting to order at 9:01 AM." 2027 dates from 'WSD Budget Timeline FY 28' (raw washington-timeline-fy28.txt: 'March 6, 2027 School District Annual Meeting 197:1'). NHMA/DRA list: not SB2. Raw copy: raw/districts/batch-6/washington-annual-meeting-minutes-2026.txt
139. The Waterville Valley School District holds a traditional annual school district meeting. The 2026 meeting was set for Monday, March 9, 2026, at 6:00 p.m. at Waterville Valley Elementary School (per the district's 2026 warrant, a DRA draft dated December 11, 2025).
   - citation: Waterville Valley Local School 2026 Warrant ('2026-2027 Warrant Articles - Draft' on https://wves.pemibaker.org/school-board/budget)
   - source: https://drive.google.com/file/d/1NDtVcBiaHf-OznotkocA-zQr_mpkfMKP/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Waterville Valley
   - note: Page text: "the Annual School District Meeting will be held as follows: Date: Monday, March 9, 2026 Time: 6:00 p.m. Location: Waterville Valley Elementary School" Warrant marked DRAFT. NHMA/DRA list: not SB2. Raw copy: raw/districts/batch-6/waterville-warrant-2026.txt
140. The Weare School District votes by official ballot (SB2). In 2026, Session One (deliberative) was on Wednesday, February 4, 2026, at 7:00 p.m. at Weare Middle School, and Session Two (voting) was on Tuesday, March 10, 2026, 7 a.m.-7 p.m. at Weare Middle School.
   - citation: Weare School District 2026 School Warrant (signed 1.14.26), SAU 24 Budget Information
   - source: https://drive.google.com/file/d/1c9hroly-dhnVmUZxAL5V6Jkb7aO5o5yf/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Weare
   - note: Page text: "You are hereby notified to meet at the Weare Middle School, 16 East Road, Weare, NH on Wednesday, the 4th day of February 2026 at 7:00 p.m. ... with the polls opening at 7:00 a.m. and closing at 7:00 p.m. on Tuesday, the 10th day of March 2026 to vote by official ballot" NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/weare-warrant-2026.txt
141. The Wentworth School District holds a traditional annual school district meeting. The 2026 meeting was set for Saturday, March 7, 2026, at 10:30 a.m. at Wentworth Elementary School, with district officers elected on March 10, 2026 (per the 2026 warrant, posted as a DRA draft copy).
   - citation: Wentworth Local School 2026 Warrant ('Wentworth Warrant Articles' on https://wes.pemibaker.org/school-board/budget)
   - source: https://drive.google.com/file/d/1n1dNqZJPLX2NsQ1L6kC7ToQplnSwtI45/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wentworth
   - note: Page text: "the Annual School District Meeting will be held as follows: Date: Saturday, March 7, 2026 Time: 10:30 a.m. Location: Wentworth Elementary School" Scanned PDF marked DRAFT (12/1/2025); quote transcribed from page image. Article 01: 'To choose all necessary School District Officials for the year ensuing. (First Session, March 10, 2026)'. NHMA/DRA list: not SB2. Raw copy: raw/districts/batch-6/wentworth-warrant-2026.pdf
142. The Westmoreland School District holds a traditional annual district meeting. In 2026 the district meeting was on March 13 at 7:00 PM, after a budget public hearing on February 6 at the Town Hall; school district elections were on March 10, 2026.
   - citation: SAU 29 - 2026 District Meeting Dates (revised 11/25/25)
   - source: https://docs.google.com/document/d/1jZKVq6Q_oNJ_qnSUXkGZIPErAnGBQLntiV2R0Qc_lZM/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Westmoreland
   - note: Page text: "Westmoreland March 13 7:00PM February 26 February 9 January 21 January 30 February 6 7:00PM Town Hall" Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/sau29-district-meetings.txt
143. The White Mountains Regional School District holds a two-session annual meeting with voting at the polls (SB2). In 2026 the first session (deliberative session) was on February 4, 2026, at 6:00 p.m. at White Mountains Regional High School in Whitefield, and the second session, voting at polling places in Carroll, Dalton, Jefferson, Lancaster and Whitefield, was on March 10, 2026.
   - citation: WMRSD Deliberative Session Meeting Minutes, February 4, 2026 (linked from 2026-2027 Proposed Budget page)
   - source: https://aptg.co/pQpPnJ
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district White Mountains Regional
   - note: Page text: "You are hereby notified to meet for the first session of the Annual School District Meeting (Deliberative Session) at the White Mountains Regional High School auditorium in the town of Whitefield on the 4th day of February 2026 at 6:00 in the evening ... the second session of the Annual School District Meeting (voting at the polls) on the 10th day of March 2026 at your respective polling places" Budget page: https://www.sau36.org/o/wmrsd/page/2026-2027-proposed-budget. Polling hours vary by town (Jefferson noon-8 p.m.). NHMA/DRA list: SB2. Raw copy: raw/districts/batch-3/wmrsd-delib-minutes-2026.txt; raw/districts/batch-3/wmrsd-budget-2026-27.txt
144. The Wilton-Lyndeborough Cooperative School District holds a traditional annual district meeting, with officers elected by ballot in each town. The most recent warrants posted are for 2025: the annual district meeting was March 8, 2025, at the WLC Middle/High School, and the election of officers was March 11, 2025. The district's 2026 meeting dates were not found on its site.
   - citation: SAU 63 - Warrants and School Budget Forms (Warrant Articles 2025-2026 tab)
   - source: https://www.sau63.org/budget-committee/warrants-and-school-budget-forms/warrants-and-school-budget-forms
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wilton-Lyndeborough Cooperative
   - note: Page text: "WARRANT FOR ANNUAL DISTRICT MEETING ON MARCH 8, 2025 ... Date: March 8, 2025, Time: 9:00 a.m., Location: WLC Middle/High School | WARRANT FOR ELECTION OF OFFICERS ON MARCH 11, 2025" Warrants are scans; transcribed by hand. The 'Warrant Articles 2026-2027' tab (for the March 2026 meeting) has no documents. Not on NHMA/DRA SB2 list. Raw copy: raw/districts/batch-4/wlc-warrants-2025-transcription.txt; raw/districts/batch-4/wlc-warrant-2025-4-7.pdf; raw/districts/batch-4/wlc-warrant-2026-1-3.pdf
145. The Winchester School District is listed as an official ballot (SB2) school district on the NH Municipal Association's list, which uses NH Department of Revenue Administration data (file dated January 2026). Its deliberative session and voting dates were not found on the district's site.
   - citation: NH Municipal Association, "Municipal Data", "Official Ballot Referendum (SB2) School Districts"
   - source: https://www.nhmunicipal.org/sites/default/files/uploads/Website/municipal-data-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Winchester
   - note: Statewide list only; the district's own voting page was not found. Checked: No working district website found. NHMA/DRA list shows Winchester as SB2.
146. The Windham School District votes by official ballot (SB2): its 2026 operating budget article refers to the budget 'as amended by vote of the first session', and voting was held on Tuesday, March 10, 2026, 7 a.m. to 8 p.m., at Windham High School. The school board's budget hearing was January 8, 2026. The school district's 2026 deliberative session date was not found on the district site.
   - citation: Windham School District 2026 Voters' Guide (SAU 95)
   - source: https://cdnsm5-ss18.sharpschool.com/UserFiles/Servers/Server_27316100/Image/Our%20District/School%20Board/Windham%20School%20District%20Voters%20Guide%202026_FINAL.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windham
   - note: Page text: "encourages Windham citizens to exercise their right to vote on Tuesday, March 10, 2026, from 7:00 a.m. - 8:00 p.m. at Windham High School." 'first session' wording from FY27 budget hearing slides (Jan 8, 2026) in the district's Public Budget Documents Drive folder linked from https://www.windhamsd.org/our_district/school_board/district_budget_and_voting_information (raw windham-budget-1cWYDdlfJHjyCzm89wKXz6RElb1UNh807.txt). Town of Windham notice gives the TOWN deliberative session as January 31, 2026 (raw windham-town-2026-notice.txt); not used for the school district. Voters' guide URL found via Patch. NHMA/DRA list: SB2. Next budget hearing on district calendar: January 7, 2027. Raw copy: raw/districts/batch-6/windham-voters-guide-2026.txt
147. The Windsor School District holds a traditional annual school district meeting. Its preliminary timeline sets the next annual meeting for March 9, 2027, with a budget hearing on February 9, 2027 (snow date February 10). The district posted 'Windsor SD Election Results of March 10, 2026' for its 2026 election.
   - citation: Windsor Budget Timeline FY28 (Windsor SD FY28 Budget Information folder linked from https://sau34.org/en-US)
   - source: https://drive.google.com/file/d/1trCKfKKSnOXbNbBtTwijRBkO8-XO42Ox/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windsor
   - note: Page text: "March 9, 2027 School District Annual Meeting 197:1 Between March 1 and March 25" The timeline's header says 'PRELIMINARY BUDGET TIMELINE FOR 2027 FISCAL YEAR' but the file is named FY28 and lists 2026-27 dates. 2026 annual meeting date not confirmed: the FY27 timeline PDF is an image and the 2026 warrant PDF is scanned; only the file name 'Windsor SD Election Results of March 10, 2026.pdf' (FY2027 folder) gives a 2026 date. NHMA/DRA list: not SB2. Raw copy: raw/districts/batch-6/windsor-timeline-fy28.txt
148. The Winnacunnet Cooperative School District uses the official ballot (SB2) form: its 2026 deliberative session was held on Thursday, February 5, 2026 at the Winnacunnet High School auditorium, and official ballot voting was on Tuesday, March 10, 2026 at polling places in each member town (Hampton: Winnacunnet High School dining hall; Hampton Falls: Lincoln Akerman School; North Hampton: North Hampton School gymnasium; Seabrook: Seabrook Recreation Center).
   - citation: SAU 21 - 2026-27 School District Voting Information (Winnacunnet tab)
   - source: https://www.sau21.nh.gov/departments/business/voting-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Winnacunnet Cooperative
   - note: Page text: "Date: Thursday, February 5, 2026 ... Location: Winnacunnet High School Auditorium ... Date: Tuesday, March 10, 2026 ... Location: HAMPTON – Winnacunnet High School Dining Hall" Snow date Friday, February 6, 2026. Page also posts warrant, budget, default budget, deliberative minutes and video. Raw copy: raw/districts/batch-7/sau21-voting-information.txt

## high-school-tuition-options: High School Options for Districts Without a High School

- kind: local
- question_type: local_practice
- description: For districts that do not run a high school: which high schools their students attend or may choose, and the arrangement the district describes.

1. The Albany School District operates no schools. SAU 9 lists tuition contracts between Albany and the Conway School District for grades K-6, 7-8 and 9-12, so Albany high school students attend Conway's Kennett High School. New Albany-Conway contracts for grades 7-8 and 9-12 take effect at the start of the 2027-28 school year.
   - citation: SAU 9 Tuition Agreement Overview
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Albany
   - note: Page text: "9-12 TUITION CONTRACTS ... Albany & Conway" Contract PDFs are scanned; terms not transcribed. 'Kennett High School' named from the Conway warrant/SAU school list, not the tuition page. Raw copy: raw/districts/batch-1/sau9-tuitions.txt
2. The Allenstown School District runs Allenstown Community School; its students attend Pembroke Academy for high school.
   - citation: SAU 53 - Allenstown School District page
   - source: https://sau.sau53.org/pages/9c32396e-4d3e-48a6-88ad-9e5a932d6087
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Allenstown
   - note: Page text: "Students in the Allenstown school district attend Allenstown Community School for their elementary education and Pembroke Academy for their high school education." Page also links 'AREA Presentation 2025' and 'ARD/TRS Joint Tuition Committee' (not read); arrangement not confirmed in text read. Raw copy: raw/districts/batch-7/sau53-allenstown-page.txt
3. The Alton School District's high school students attend Prospect Mountain High School in Alton, which Alton runs jointly with Barnstead under a Joint Maintenance Agreement (JMA); Alton's 2026 operating budget included $4,936,894 as its net appropriation for the Prospect Mountain High School operating budget.
   - citation: Alton School District 2026 Warrant
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3643/Pmsau/18be3887-632b-47b8-bca8-0e2daf3baad1/Amended-2026-Warrant-Articles.pdf?disposition=inline
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Alton
   - note: Page text: "The amount of $4,936,894.00 is the net appropriation for the Prospect Mountain High School operating budget which is included in the gross budget amount listed above and recommended by the Joint Maintenance Agreement (JMA) Budget Committee. | Prospect Mountain School Board (JMA Alton/Barnstead)" The site does not say in words that all Alton grade 9-12 students attend PMHS; the warrant shows Alton funds PMHS under the JMA. SAU home: 'The Prospect Mountain Joint Board, comprised of the Alton and Barnstead school boards'. Raw copy: raw/districts/batch-4/alton-2026-warrant.txt; raw/districts/batch-4/pmsau-home.txt
4. The Amherst School District does not run a high school. SAU 39 serves the Amherst, Mont Vernon and Souhegan Cooperative school districts, and students in grades 9-12 enroll at Souhegan High School.
   - citation: SAU 39 - New Student Information
   - source: https://www.sau39.org/sau-info/new-student-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Amherst
   - note: Page text: "The Amherst, Mont Vernon & Souhegan Cooperative School Districts! ... Souhegan High School ... Grades 9-12:" The page does not spell out the cooperative's member towns; the site's database lists Souhegan Cooperative's towns as Amherst and Mont Vernon. Raw copy: raw/districts/batch-2/sau39-new-student.txt
5. The Andover School District runs Andover Elementary/Middle School and sends its high school students to Merrimack Valley High School under a contract. The Merrimack Valley School District's 2026 Annual Report lists the 2025-26 contracted cost for Andover students at MVHS as $16,047.05.
   - citation: Merrimack Valley School District 2026 Annual Report (Andover - High School Tuition Payments 2025-2026)
   - source: https://drive.google.com/file/d/1P82wi-vCYJExipzNQDwTwCyBLqYbK7T9/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Andover
   - note: Page text: "$16,047.05 2025-2026 Contracted cost for Andover students to attend MVHS" The source is the receiving district's report, which names Andover. Also: 'MVHS serves the communities of Andover, Boscawen, Loudon, Penacook, Salisbury, and Webster' (same report). The SAU 46 registration page lists 'Andover (high school only)'. The AEMS home page links a 'Merrimack Valley High School-HS Andover Route' bus route. The site does not say whether other high schools may be chosen. Raw copy: raw/districts/batch-1/mvsd-2026-annual-report.txt
6. Ashland Elementary School serves kindergarten through grade 8, and Ashland students go on to Plymouth Regional High School for grade 9. The Ashland School District's annual report mentions Memorandums of Understanding with SAU 48 and the Pemi-Baker School District, which runs Plymouth Regional High School, but does not describe the tuition or membership arrangement.
   - citation: Ashland School District Annual Report (FY2025)
   - source: https://sau2.k12.nh.us/fs/resource-manager/view/a30360aa-a296-4cf6-80fe-ecec75bc210f
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Ashland
   - note: Page text: "ensure that when students complete eighth grade they are prepared and primed for success as ninth graders entering Plymouth Regional High School (PRHS). ... Established Memorandum of Understandings with SAU #48 and the Pemi- Baker School District support ongoing collaboration and alignment." Arrangement type (Pemi-Baker membership vs tuition) not stated on pages checked. Raw copy: raw/districts/batch-5/ashland-annual-report-2025.txt
7. The Auburn School District serves preschool through grade 8 at Auburn Village School. The Auburn School Board's documents page posts an approved agreement with Pinkerton Academy, and the school posts Pinkerton Academy's orientation schedule for incoming 9th graders (Class of 2031).
   - citation: Auburn School Board, Documents (Pinkerton Agreement Approved); Auburn Village School post of Oct 26, 2026
   - source: https://auburnschoolboard.sau15.net/documents/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Auburn
   - note: Page text: "Pinkerton Agreement Approved ... Pinkerton Academy's 8th grade orientation schedule" The agreement PDF is a scan with no extractable text, so its terms and dates were not read. The site does not state in words whether other high schools may be chosen. Raw copy: raw/districts/batch-3/auburn-board-docs.txt; raw/districts/batch-3/auburn-pinkerton-orientation.txt; raw/districts/batch-3/auburn-pinkerton-agreement.txt
8. Barnstead high school students attend Prospect Mountain High School, which the Barnstead and Alton school districts run together under a Joint Maintenance Agreement (JMA). Barnstead's share of the high school budget is included in its own operating budget, and the 2026 warrant set Barnstead's share of new high school contract costs at 54.45% (Alton 45.55%).
   - citation: Barnstead School District Annual Report 2024-2025, printed page 74 (2026 warrant)
   - source: https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3643/Pmsau/8956d01e-faf5-4e8d-94b0-e905a0106f80/Barnstead-Annual-Report-2024-2025.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barnstead
   - note: Page text: "(Fiscal Note: The amount of $5,901,513.00 is the net appropriation for the Prospect Mountain High School operating budget which is included in the gross budget amount listed above and recommended by the Joint Maintenance Agreement (JMA) Budget Committee)" Not a tuition arrangement; a joint high school with Alton. Article 3: 'contingent upon both the Alton (45.55%) and Barnstead (54.45%) Districts approving the cost items'. Raw copy: raw/districts/batch-5/barnstead-annual-report-2024-25-p73-warrant-2026.jpg
9. The Barrington School District has no high school. Its High Schools page features Coe-Brown Northwood Academy, Dover High School and Oyster River High School, and posts its tuition agreements: a signed Coe-Brown Northwood Academy MOU for 2025-2027, a Dover tuition agreement approved by the State Board of Education on February 20, 2025, and an Oyster River tuition agreement. Oyster River admission is by lottery: for 2027-28, eighth graders who plan to attend Oyster River High School must return the application and residency affidavit by January 29, 2027.
   - citation: Barrington School District - High Schools (Tuition Agreements and High School Enrollment Procedure folders)
   - source: https://www.sau74.org/high_schools
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Barrington
   - note: Page text: "These two documents must be completed and returned no later than January 29, 2027 if your 8th grader plans on attending Oyster River High School. If you do not return these documents by January 29th, 2027 your child will not be eligible for the lottery." Quote is from the Oyster River Lottery Packet for 2027/2028 (letter dated Oct 19, 2026), scanned: raw/districts/batch-1/barrington-oyster-river-lottery-2027-28-p1.png. Dover approval letter: raw/districts/batch-1/barrington-dover-tuition-agreement-p1.png ('At its February 20, 2025 meeting, the State Board of Education voted to approve the Dover and Barrington School Districts' Tuition Agreement'). Agreement terms not transcribed. Raw copy: raw/districts/batch-1/barrington-high-schools-rendered.html
10. The Bartlett School District has no high school. SAU 9 lists a grades 9-12 tuition contract between Bartlett and the Conway School District, which runs Kennett High School, and a new Bartlett-Conway 9-12 contract that takes effect at the start of the 2027-28 school year. SAU 9 also lists a grades 7-8 contract between Bartlett and Jackson.
   - citation: SAU 9 Tuition Agreement Overview
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bartlett
   - note: Page text: "9-12 TUITION CONTRACTS ... Bartlett & Conway ... Please Note: The following contracts have been ratified by the respective Boards and approved by the State Board of Education. They will go into effect as of the start of the 2027-28 School Year." Contract PDFs are scanned; terms not transcribed. 7-8 contract listed under current as 'Bartlett & Jackson'; direction (which district sends) not stated on the page. Josiah Bartlett Elementary serves through the middle school grades per its home page. Raw copy: raw/districts/batch-1/sau9-tuitions.txt
11. The Bethlehem School District serves Bethlehem students in kindergarten through grade 6; students in grades 7-12 from Bethlehem attend Profile School, run by the Profile School District, which serves Bethlehem, Easton, Franconia and Sugar Hill.
   - citation: Profile School - About Us / Employment page text (SchoolBlocks site)
   - source: https://profile.k12.nh.us
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Bethlehem
   - note: Page text: "Bethlehem School District serves approximately 160 K-6 students from the town of Bethlehem. ... The Profile School District serves approximately 230 students in grades 7-12 from all four towns." Not a tuition arrangement: Profile is a separate school district covering the same towns. Raw copy: raw/districts/batch-4/profile-pages.txt
12. The Brentwood School District does not run a high school; it is one of the six member districts of the Exeter Region Cooperative School District (Brentwood, East Kingston, Exeter, Kensington, Newfields and Stratham), whose middle school (grades 6-8) and high school (Exeter High School, grades 9-12) serve its students.
   - citation: Exeter Region Cooperative School District 2026 Warrant; ERCSD 2026 Deliberative Session minutes (https://drive.google.com/file/d/1PqJ1vo1dM_GxSoKVeUwa6-j-Xwxp0f1B/view)
   - source: https://drive.google.com/file/d/1-yi8u9qfh9gciyC-QlKO91JA2RLxyK2U/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brentwood
   - note: Page text: "To the inhabitants of the School Districts of the Towns of Exeter, East Kingston, Brentwood, Newfields, Stratham, and Kensington, County of Rockingham, State of New Hampshire, qualified to vote on District affairs" Warrant and minutes are scans (OCR). Minutes Article 01 gives ERCSD cost per pupil for 'Middle School (Grades 6-8)' and 'High School (Grades 9-12)'; session held at Exeter High School. Grade spans 6-8 / 9-12 from the minutes; the name 'Exeter High School' from the warrant location and minutes. This is cooperative membership, not tuition. Raw copy: raw/districts/batch-8/ercsd-warrant-2026.txt; raw/districts/batch-8/ercsd-deliberative-minutes-2026.txt
13. Brookline students in grades 7-8 attend Hollis Brookline Middle School and students in grades 9-12 attend Hollis Brookline High School, run by the Hollis-Brookline Cooperative School District.
   - citation: SAU41 - New Student Registration
   - source: https://www.sau41.org/for-families/new-student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Brookline
   - note: Page text: "Students living in Brookline attend Richard Maghakian Memorial School Grades PK-3 Captain Samuel Douglass Academy Grades 4-6 Hollis Brookline Middle School Grades 7-8 Hollis Brookline High School Grades 9-12" Cooperative membership, not tuition. Raw copy: raw/districts/batch-5/sau41-registration.txt
14. Campton is one of the seven towns of the Pemi-Baker Regional School District, whose high school is Plymouth Regional High School: the Pemi-Baker 2026 warrant lists a Campton polling place (the Campton Municipal Building) for its March 10, 2026 ballot vote, and the SAU 48 site lists Plymouth Regional High School as the Pemi Baker Regional high school.
   - citation: Pemi-Baker Regional School District 2026 Warrant (polling places by member town)
   - source: https://drive.google.com/file/d/18H7G1QTwK8BX2_6mSdPmeZrtC6HPWRN_/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Campton
   - note: Page text: "Campton – 8:00 a.m. – 7:00 p.m. – Campton Municipal Building (12 Gearty Way)" Cooperative membership shown by regional polling place; not a tuition arrangement. Coordinator: reworded so the statement says only what the warrant and SAU 48 page show; no page found states in words which grades the town's students attend. SAU 48 page: raw/districts/batch-6/sau48-pemibaker.txt. Raw copy: raw/districts/batch-6/pemibaker-warrant-2026.txt
15. The Candia School District has no high school of its own. Its High School page posts the Candia-Pinkerton Academy Agreement for 2018-2038, along with a 2016 capital cost settlement agreement with Manchester and a 2015 High School Task Force report.
   - citation: Henry W. Moore School / Candia School District, High School page
   - source: https://candia.sau15.net/high-school/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Candia
   - note: Page text: "High School Documents 8-2016 Capital Cost Manchester Candia Settlement Agreement Candia-Pinkerton Academy Agreement 2018-2038" Agreement PDF is a scan with no extractable text; whether students may choose other schools is not stated in page text. Raw copy: raw/districts/batch-3/candia-hs.txt; raw/districts/batch-3/candia-pinkerton-agreement.txt
16. The Chester School District (Chester Academy, grades preschool-8) publishes school bus routes to Pinkerton Academy in Derry and links to Pinkerton Academy from its home page; its site does not describe the terms of its high school arrangement.
   - citation: Chester School District - Pinkerton Bus Routes
   - source: https://www.sau82.org/district/pinkerton_bus_routes
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chester
   - note: Page text: "Pinkerton Bus Routes ... Please check carefully between AM and PM schedules as there are five routes in the morning and four routes in the afternoon." Partial: the page shows transportation to Pinkerton Academy but not whether it is a contract or the only option. Pinkerton is listed in the site database as its own 'district' (id 999). Raw copy: raw/districts/batch-4/chester-pinkerton-bus.txt; raw/districts/batch-4/chester-sau82-rendered.txt
17. The Chesterfield School District runs Chesterfield School (grades K-8); its students in grades 9-12 attend Keene High School under a long-term arrangement with the Keene School District.
   - citation: Keene School District home page - Sending Towns
   - source: https://www.keeneschoolsnh.org/ksd
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chesterfield
   - note: Page text: "Chesterfield School, SAU 29, currently enrolls students in grades K-8, who reside in Chesterfield, NH; Spofford, NH; and West Chesterfield, NH. Students in grades 9-12 attend Keene School School" Source is the receiving district's page ('has entered into long-term arrangements, completing the K-12 educational path for these sending towns'). SAU 29 has an A.R.E.A. committee page (minutes only). The agreement text was not found. Raw copy: raw/districts/batch-4/keene-ksd-home.txt
18. The Chichester School District runs Chichester Central School; its students attend Pembroke Academy for high school.
   - citation: SAU 53 - Chichester School District page
   - source: https://sau.sau53.org/pages/7bf6404b-8c6d-4d73-a5f8-2cd4e7f215ba
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Chichester
   - note: Page text: "Students in the Chichester school district attend Chichester Central School for their elementary education and Pembroke Academy for their high school education." Page also links 'AREA Presentation 2025' (not read). Raw copy: raw/districts/batch-7/sau53-chichester-page.txt
19. The Cornish School District has no high school; its students may choose among five high schools: Claremont, Hanover, Hartford, Lebanon and Windsor. Families who choose Hanover High School pay an additional amount above the set tuition rate. The district suggests starting with its school counselor.
   - citation: Cornish School District - High School Choice
   - source: https://www.cornishschool.org/apps/pages/index.jsp?uREC_ID=597058&type=d
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Cornish
   - note: Page text: "Cornish School District offers students the unique opportunity to choose from five different high schools—Claremont, Hanover, Hartford, Lebanon, and Windsor ... The choice of Hanover High School requires families to pay an additional amount for tuition above the set tuition rate for all students." Hartford and Windsor are Vermont schools; the page names schools only by town. Raw copy: raw/districts/batch-2/cornish-hs-choice.txt
20. The Croydon School District runs only a preschool and kindergarten. From grade 1 through grade 12, Croydon students enroll in a partner school through the district's School Choice program, and the district pays tuition up to a cap ($18,000 for 2026-27); families pay any difference. Kearsarge Regional is the anchor school, where all Croydon students are guaranteed admission; other listed schools include Claremont, Lebanon, Mascoma, Newport and Sunapee public schools, private schools such as Kimball Union Academy, and online programs including VLACS.
   - citation: Croydon School District - School Choice
   - source: https://croydonsd.org/school-choice/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Croydon
   - note: Page text: "Once students reach grade 1, they leave the Village School and are enrolled into one of our partner schools as part of our School Choice program. The Croydon School District will pay tuition up to the tuition cap (currently $18,000 for the 26/27 school year) as per our Tuition Policy." Anchor: 'Kearsarge: Our Anchor School ... As anchor school, all Croydon students are guaranteed admission.' Full partner list on page also includes Claremont Christian Academy, Enlightium Academy, Mount Royal Academy, Newport Montessori, Prisma. Not every partner serves high school grades; the page does not separate them by grade. Raw copy: raw/districts/batch-6/croydon-school-choice.txt
21. The Deerfield School District runs Deerfield Community School (through grade 8); for high school its students have a choice of Concord High School, Coe-Brown Northwood Academy and Pembroke Academy. The district posts a memorandum of understanding with each school and a High School Assignment Request form.
   - citation: SAU 53 - Deerfield School District page
   - source: https://sau.sau53.org/pages/7cb5b493-aeb4-48a2-96d1-3d1bd20e796a
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Deerfield
   - note: Page text: "Students in the Deerfield school district attend Deerfield Community School for their elementary education and have a choice of Concord High, Coe-Brown Northwood Academy and Pembroke Academy for their high school education." MOUs: Coe Brown https://drive.google.com/file/d/11uuVjidaIG2wbeRHZFddT6BmMAjb2qk-/view; Concord High https://drive.google.com/file/d/1mTVoYZCIjmv0QmFwYrr8hIQ211_lfBND/view; Pembroke Academy https://drive.google.com/file/d/1Ds1JQgKGWy6QyUinwwmh1C-7vxzvUEsY/view (not downloaded/read). Tuition amounts not checked. Raw copy: raw/districts/batch-7/sau53-deerfield-page.txt
22. The Derry Cooperative School District serves preschool through grade 8. Derry high school students attend Pinkerton Academy in Derry, with their tuition paid by the district.
   - citation: Derry Cooperative School District, About
   - source: https://www.sau10.nh.gov/about/index
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Derry Cooperative
   - note: Page text: "The Derry Cooperative School District is a PreK-8 public district in Derry, NH ... High school students have their tuition paid by the town to Pinkerton Academy." Page says 'paid by the town'; the payer is the school district. Contract terms and tuition rate not found on the SAU site. Raw copy: raw/districts/batch-3/derry-about.txt
23. The Dummer School District operates no schools and pays tuition for all its students; its annual report says schools in Milan and Berlin educate Dummer students, and its tuition table lists Milan Elementary School, Berlin Middle School and Berlin High School.
   - citation: 2024-2025 Dummer Annual Report
   - source: https://drive.google.com/file/d/177mDbGqVAo9HP55Gn7oN9nqOjsLVTs_8/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dummer
   - note: Page text: "the Dummer School District operates on a tuition- and service-based budget ... The schools in Milan and Berlin continue to provide a strong educational experience for students from Dummer. ... Tuition Cost FY2025 FY2026 FY2027 Change % Change Milan Elementry School Berlin Middle School Berlin High School" Report lists 9 high school students for FY27. Arrangement (contract vs. choice) not stated. Raw copy: raw/districts/batch-3/dummer-annual-report-2024-25.txt
24. Dunbarton students in grades 7-8 attend Bow Memorial School and students in grades 9-12 attend Bow High School, according to SAU 67's registration page. The Bow School District's 2026 warrant refers to tuition payments from Dunbarton under a 2024-2039 AREA agreement.
   - citation: SAU 67 - New Student Registration; Bow School District 2026 Warrant Articles (https://drive.google.com/file/d/1BxbrBGlkoGRxlYyYly48OxAz0EgrHJIE/view)
   - source: https://sau67nh.gov/en/register
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Dunbarton
   - note: Page text: "Bow Memorial (Grades 5 - 8) Bow Residents; (Grades 7 - 8 ONLY) Dunbarton Residents - (603) 225-3212 Bow High - (Grades 9 -12) Bow and Dunbarton Residents" Bow warrant Article 3: 'AREA School Capital Improvements – Dunbarton Fees Capital Reserve Fund ... tuition payments received in the 2026-27 fiscal year in accordance with the 2024-2039 AREA agreement.' The registration page is SAU-wide and names Dunbarton residents explicitly. Raw copy: raw/districts/batch-5/sau67-register.txt; raw/districts/batch-5/bow-warrant-2026.pdf
25. The East Kingston School District does not run a high school; it is one of the six member districts of the Exeter Region Cooperative School District (Brentwood, East Kingston, Exeter, Kensington, Newfields and Stratham), whose middle school (grades 6-8) and high school (Exeter High School, grades 9-12) serve its students.
   - citation: Exeter Region Cooperative School District 2026 Warrant; ERCSD 2026 Deliberative Session minutes (https://drive.google.com/file/d/1PqJ1vo1dM_GxSoKVeUwa6-j-Xwxp0f1B/view)
   - source: https://drive.google.com/file/d/1-yi8u9qfh9gciyC-QlKO91JA2RLxyK2U/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district East Kingston
   - note: Page text: "To the inhabitants of the School Districts of the Towns of Exeter, East Kingston, Brentwood, Newfields, Stratham, and Kensington, County of Rockingham, State of New Hampshire, qualified to vote on District affairs" Warrant and minutes are scans (OCR). Minutes Article 01 gives ERCSD cost per pupil for 'Middle School (Grades 6-8)' and 'High School (Grades 9-12)'; session held at Exeter High School. Grade spans 6-8 / 9-12 from the minutes; the name 'Exeter High School' from the warrant location and minutes. This is cooperative membership, not tuition. Raw copy: raw/districts/batch-8/ercsd-warrant-2026.txt; raw/districts/batch-8/ercsd-deliberative-minutes-2026.txt
26. The Eaton School District operates no schools. SAU 9 lists tuition contracts between Eaton and the Conway School District for grades K-6, 7-8 and 9-12, so Eaton high school students attend Conway's Kennett High School. New Eaton-Conway contracts for grades 7-8 and 9-12 take effect at the start of the 2027-28 school year.
   - citation: SAU 9 Tuition Agreement Overview
   - source: https://www.sau9.org/tuitions
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Eaton
   - note: Page text: "9-12 TUITION CONTRACTS ... Eaton & Conway" The 2026 Eaton warrant (Article 7) proposed adopting open enrollment (RSA 194-D) as a party to Conway's open enrollment provisions, and limiting Eaton residents at open enrollment schools outside Conway to 0%. Article 8 proposed a five-year 7-8 tuition agreement with Conway from July 1, 2027. Results not checked. Raw copy: raw/districts/batch-1/sau9-tuitions.txt
27. Ellsworth has no school of its own; its students are tuitioned to another school within SAU 48. The SAU page does not name the schools.
   - citation: SAU 48 - Schools in SAU 48
   - source: https://sites.google.com/pemibaker.org/sau48/schools
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Ellsworth
   - note: Page text: "The town of Ellsworth is part of SAU #48. Since the town has no school, students are tuitioned to another school within SAU #48." Raw copy: raw/districts/batch-6/sau48-schools.txt
28. The Epsom School District runs Epsom Central School; its students attend Pembroke Academy for high school.
   - citation: SAU 53 - Epsom School District page
   - source: https://sau.sau53.org/pages/10e488d9-2abc-4b3e-a427-2797457471db
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Epsom
   - note: Page text: "Students in the Epsom school district attend Epsom Central School for their elementary education and Pembroke Academy for their high school education." The page also links an 'AREA Presentation 2025' (https://drive.google.com/file/d/1XH1q-7mkU1I-q0m9V8Th3GPDUhcW2Pnd/view, not read), so the arrangement may be an AREA agreement; not confirmed. Raw copy: raw/districts/batch-7/sau53-epsom-page.txt
29. The Errol School District pays tuition for its students in grades 9-12; its 2026 operating budget article includes a high school tuition total of $148,000. The report does not name the receiving high schools.
   - citation: 2024-2025 Errol Annual School District Report
   - source: https://drive.google.com/file/d/1lswq7V4J1Oos-7YHdP8H3lxeXks-BLNq/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Errol
   - note: Page text: "for the payment of tuition for students in grades 9-12 (High School total $148,000 which is included above)" Receiving schools not named on the district site. Raw copy: raw/districts/batch-3/errol-annual-report-2024-25.txt
30. The Exeter School District does not run a high school; it is one of the six member districts of the Exeter Region Cooperative School District (Brentwood, East Kingston, Exeter, Kensington, Newfields and Stratham), whose middle school (grades 6-8) and high school (Exeter High School, grades 9-12) serve its students.
   - citation: Exeter Region Cooperative School District 2026 Warrant; ERCSD 2026 Deliberative Session minutes (https://drive.google.com/file/d/1PqJ1vo1dM_GxSoKVeUwa6-j-Xwxp0f1B/view)
   - source: https://drive.google.com/file/d/1-yi8u9qfh9gciyC-QlKO91JA2RLxyK2U/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Exeter
   - note: Page text: "To the inhabitants of the School Districts of the Towns of Exeter, East Kingston, Brentwood, Newfields, Stratham, and Kensington, County of Rockingham, State of New Hampshire, qualified to vote on District affairs" Warrant and minutes are scans (OCR). Minutes Article 01 gives ERCSD cost per pupil for 'Middle School (Grades 6-8)' and 'High School (Grades 9-12)'; session held at Exeter High School. Grade spans 6-8 / 9-12 from the minutes; the name 'Exeter High School' from the warrant location and minutes. This is cooperative membership, not tuition. Raw copy: raw/districts/batch-8/ercsd-warrant-2026.txt; raw/districts/batch-8/ercsd-deliberative-minutes-2026.txt
31. The Fremont School District does not have a high school. It has a 2024 memorandum of understanding with the Epping School District under which Epping High School accepts any Fremont high school students, and a 2024 agreement with Pinkerton Academy in Derry; both charge tuition set each year from per-pupil operating costs. The Epping agreement says it does not stop Fremont from making other tuition agreements.
   - citation: Ellis School - SAU 83: Future High School (Epping Contract Final, Agreement with Pinkerton Final)
   - source: https://www.sau83.org/page/future-high-school/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Fremont
   - note: Page text: "Epping shall accept any and all high school students from Fremont, with no minimum or maximum enrollment requirements during the Term. Nothing in this agreement shall prohibit Fremont from entering into other tuition agreements | THIS AGREEMENT made this 7th day of May, 2024, by and between the FREMONT SCHOOL DISTRICT ... and PINKERTON ACADEMY of Derry" Agreements are scans; first pages transcribed by hand. The Epping MOU page 1 is dated July 25, 2024 (link label says 'Signed May 2024'). Term lengths and tuition figures are in later pages, not transcribed. The page does not say how families choose between the two schools. Raw copy: raw/districts/batch-4/fremont-hs-agreements-transcription.txt; raw/districts/batch-4/fremont-epping-contract-2024.pdf; raw/districts/batch-4/fremont-pinkerton-agreement-2024.pdf
32. The Goshen School District operates no schools; according to the Town of Goshen, it provides public school choice in grades K through 12 through approved school tuition agreements, and families with school-aged children should contact the Goshen School District (SAU 102). The specific schools are not listed on the public page.
   - citation: Town of Goshen, New Hampshire - School
   - source: https://goshennh.org/school/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Goshen
   - note: Page text: "The Town of Goshen is an inviting community supportive of public education, providing public school choice in grades K through 12 through approved school tuition agreements. Families with school-aged children should contact the Goshen School District" Town page, not the school district's own page (the district's Google Site requires sign-in). Partial: names no receiving schools. Raw copy: raw/districts/batch-4/goshen-town-school-page.txt
33. The Grantham School District runs grades K-6 and pays tuition for students in grades 7-12 to attend Lebanon Middle School and Lebanon High School under an AREA agreement with the Lebanon School District. New residents get a residency form approved by the Grantham SAU office before registering at Lebanon.
   - citation: Grantham School District 2026 Annual Report (linked from the 2026 March Annual Meeting page)
   - source: https://drive.google.com/file/d/1623By-YiLZlCuUYe_a2eU_k3o8t_UPU2/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Grantham
   - note: Page text: "The Grantham School District serves students in grades K-6 and tuition students through an AREA agreement with the Lebanon School District for grades 7-12 as a New Hampshire Public School District." School board schedule lists AREA meetings with Lebanon, Grantham and Plainfield (Nov 10, 2026; Feb 18, 2027). Raw copy: raw/districts/batch-5/grantham-annual-report-2026.txt
34. The Greenland School District runs Greenland Central School (K-8) and no high school; its students in grades 9-12 attend Portsmouth High School. Under SAU 50 Policy JFAC, the SAU 50 districts pay the per diem tuition rate charged by the Portsmouth School District under their Authorized Regional Enrollment Area (AREA) agreement.
   - citation: SAU 50 Policy JFAC, Tuition for Resident High School Students; SAU 50 schools overview (https://www.sau50.org/pages/32bfca09-8390-4f0b-bc2d-c425b4ea9011)
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Greenland
   - note: Page text: "According to the Authorized Regional Enrollment Area agreement, the school districts of SAU 50 will pay the per diem tuition rate charged by the Portsmouth School District." Schools page: 'Students in grades 9-12 attend Portsmouth High School.' Raw copy: raw/districts/batch-8/sau50-policies.txt; raw/districts/batch-8/sau50-schools.txt
35. The Hampstead School District runs schools through grade 8; its site has a 'Pinkerton Academy Transition' page under counseling resources and posts bus routes for Pinkerton Academy along with its own schools. The pages opened do not describe the arrangement with Pinkerton Academy or any other high school option.
   - citation: Hampstead Central School news - Bus Routes and Lunch Menus are Posted; Hampstead School District - Pinkerton Academy Transition (https://www.hampsteadschools.net/page/pinkerton-academy-transition)
   - source: https://hcs.hampsteadschools.net/o/hcs/article/2375341
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampstead
   - note: Page text: "Bus Routes for Hampstead Central and Middle Schools, as well as Pinkerton Academy are posted here" Quote is from the article teaser in the menu dump; the Pinkerton transition page body was empty when rendered. Contract terms not found. Raw copy: raw/districts/batch-8/hampstead-hcs-menu.txt; raw/districts/batch-8/hampstead-pinkerton.txt
36. Winnacunnet High School in Hampton, a four-year public cooperative high school, serves the towns of Hampton, Seabrook, Hampton Falls and North Hampton, according to North Hampton School's (SAU 21) high school page. Hampton's own SAU 90 pages do not describe the arrangement.
   - citation: North Hampton School - On to High School (SAU 21)
   - source: https://www.northhamptonschool.org/families/on-to-high-school/index
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton
   - note: Page text: "Winnacunnet is a four-year, comprehensive high school. ... The school serves the towns of Hampton, Seabrook, Hampton Falls, and North Hampton." Coordinator record: replaces batch-8's 'not found' (SAU 90 pages checked: home menus, voting page, warrant, parent links). The page names Hampton among the towns Winnacunnet serves; that Hampton is a member of the Winnacunnet Cooperative School District is not stated on a Hampton page. Raw copy: raw/districts/batch-7/northhampton-on-to-high-school.txt
37. Hampton Falls is a member of the Winnacunnet Cooperative School District; Winnacunnet High School in Hampton, a public cooperative high school, serves the towns of Hampton, Seabrook, Hampton Falls and North Hampton.
   - citation: North Hampton School - On to High School (SAU 21)
   - source: https://www.northhamptonschool.org/families/on-to-high-school/index
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hampton Falls
   - note: Page text: "The school serves the towns of Hampton, Seabrook, Hampton Falls, and North Hampton." Hampton Falls runs Lincoln Akerman School (K-8). Raw copy: raw/districts/batch-7/northhampton-on-to-high-school.txt
38. Children living in Hanover attend Bernice A. Ray Elementary School through grade 5, then Frances C. Richmond Middle School in Hanover and Hanover High School for grades 9-12. SAU 70 describes itself as the first interstate school district, serving Hanover, NH and Norwich, VT.
   - citation: SAU 70 Enroll
   - source: https://www.sau70.org/our-districts/enroll
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hanover
   - note: Page text: "students living in Hanover, NH attend Bernice A. Ray Elementary School until 5th grade. Students then move on to the Frances C. Richmond Middle School in Hanover, NH and then to Hanover High School for grades 9-12." Not a tuition arrangement. The site database lists Richmond Middle and Hanover High under the Dresden School District; the enroll page itself does not name Dresden. Raw copy: raw/districts/batch-3/sau70-our-districts-enroll.txt
39. The Harrisville School District runs Harrisville-Wells Memorial School (grades K-6); its students in grades 7-8 attend Keene Middle School and grades 9-12 attend Keene High School under a long-term arrangement with the Keene School District.
   - citation: Keene School District home page - Sending Towns
   - source: https://www.keeneschoolsnh.org/ksd
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Harrisville
   - note: Page text: "Harrisville-Wells Memorial School, SAU29, currently enrolls students in K-6, who reside in Harrisville, NH. Students in grades 7-8 attend Keene Middle School ... Students in grades 9-12 attend Keene High School" Raw copy: raw/districts/batch-4/keene-ksd-home.txt
40. Henniker is one of the two towns (with Weare) in the John Stark Regional School District, which runs John Stark Regional High School in Weare; the John Stark warrant is addressed to the inhabitants of Henniker and Weare.
   - citation: John Stark School District 2026 School Warrant (signed 1.15.26)
   - source: https://drive.google.com/file/d/14atMFMSRurjikAmEIDq02oIB4pLra41g/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Henniker
   - note: Page text: "JOHN STARK SCHOOL DISTRICT THE STATE OF NEW HAMPSHIRE 2026 SCHOOL WARRANT To the inhabitants of the School District in the towns of Henniker and Weare" Cooperative membership, not tuition. Raw copy: raw/districts/batch-3/johnstark-warrant-2026.txt
41. The Hill School District runs Jennie D. Blake School and pays tuition for its middle and high school students; the school's website lists Newfound Memorial Middle School (grades 7-8) and Newfound Regional High School (grades 9-12) as the schools for those grades. The pages opened do not describe the agreement or any choice of other schools.
   - citation: Hill School District Warrant 2026, Article 5; Jennie D. Blake School home page (https://sites.google.com/sau103.org/jdbs/home)
   - source: https://drive.google.com/file/d/1R8r62PVekTvNgWZ1GYgGxZlwNVxEqjki/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hill
   - note: Page text: "Tuition Capital Reserve Fund (established in 2018 for the payment of tuition for middle and high school students)" Home page lists 'Newfound Memorial Middle School (7-8)' and 'Newfound Regional High School (9-12)' with links to nmms.sau4.org and nrhs.sau4.org. The 'Intergovernmental Agreement' page is a town/school board agreement (raw/districts/batch-8/hill-intergovernmental-agreement.txt), not a tuition agreement. Raw copy: raw/districts/batch-8/hill-warrant-2026.txt; raw/districts/batch-8/hill-home.txt
42. Holderness is one of the seven towns of the Pemi-Baker Regional School District, whose high school is Plymouth Regional High School: the Pemi-Baker 2026 warrant lists a Holderness polling place (Holderness Town Hall) for its March 10, 2026 ballot vote, and the SAU 48 site lists Plymouth Regional High School as the Pemi Baker Regional high school.
   - citation: Pemi-Baker Regional School District 2026 Warrant (polling places by member town)
   - source: https://drive.google.com/file/d/18H7G1QTwK8BX2_6mSdPmeZrtC6HPWRN_/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Holderness
   - note: Page text: "Holderness – 10:00 a.m. – 7:00 p.m. – Holderness Town Hall" Cooperative membership shown by regional polling place. Coordinator: reworded so the statement says only what the warrant and SAU 48 page show; no page found states in words which grades the town's students attend. SAU 48 page: raw/districts/batch-6/sau48-pemibaker.txt. Raw copy: raw/districts/batch-6/pemibaker-warrant-2026.txt
43. Hollis students in grades 7-8 attend Hollis Brookline Middle School and students in grades 9-12 attend Hollis Brookline High School, run by the Hollis-Brookline Cooperative School District.
   - citation: SAU41 - New Student Registration
   - source: https://www.sau41.org/for-families/new-student-registration
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hollis
   - note: Page text: "Students living in Hollis attend Hollis Primary School Grades PK-3 Hollis Upper Elementary Grades 4-6 Hollis Brookline Middle School Grades 7-8 Hollis Brookline High School Grades 9-12" Cooperative membership, not tuition. Raw copy: raw/districts/batch-5/sau41-registration.txt
44. The Hooksett School District has no high school of its own. The Hooksett School Board has designated Pinkerton Academy as the school of record, and all Hooksett 8th graders are assigned to attend Pinkerton. Parents may petition to send their child instead to Londonderry High School, Goffstown High School, Bow High School, Pembroke Academy, or Manchester Central, West or Memorial High School (for the Class of 2027 the petition form was due October 2, 2026).
   - citation: Cawley Middle School letter to 8th grade parents, Class of 2027 (August 10, 2026), on High School Information for Hooksett Students
   - source: https://hooksetthighschoolinfo.sau15.net/wp-content/uploads/sites/12/2026/08/High-School-Parent-Letter-Class-of-2027-.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Hooksett
   - note: Page text: "The Hooksett School Board has designated Pinkerton Academy as the school of record for all Hooksett 8th grade students. All students are assigned to attend Pinkerton Academy. Parents will have the option to petition to send their child to Londonderry High School, Goffstown High School, Bow High School, Pembroke Academy, Manchester Central High School, Manchester West High School or Manchester Memorial High School." District site also links a Pinkerton Agreement PDF (hooksett.sau15.net/wp-content/uploads/sites/3/2022/02/Pinkerton-Agreement.pdf), not opened. 'Class of 2027' here is the Cawley 8th-grade class of 2026-27. Raw copy: raw/districts/batch-3/hooksett-hs-letter-2027.txt; raw/districts/batch-3/hooksett-hsinfo.txt
45. The Jackson School District has no high school. Its students attend Kennett High School under a tuition contract with the Conway School District, which comes up for renewal in 2027. At the March 5, 2026 annual meeting, Jackson voters approved two new high school tuition agreements, one with the Conway School District (Kennett High School) and one with Fryeburg Academy in Maine. Under the Fryeburg agreement, the academy will accept up to all resident Jackson high school students in grades 9-12 and becomes a school maintained by Jackson. SAU 9 lists both agreements as approved by the State Board of Education, taking effect at the start of 2027-28.
   - citation: Jackson Grammar School - High School Options
   - source: https://jgs.sau9.org/324669_2
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Jackson
   - note: Page text: "At the March 5, 2026, annual School District meeting, Jackson voters approved two tuition agreements with area high schools. ... The Jackson School District contract with the Conway School District to educate Jackson students at Kennett High School is up for renewal in 2027." Fryeburg agreement p.1 (scanned; raw/districts/batch-1/sau9-contract-9-12-jackson-fryeburg-2027-p1.png): 'The Academy shall accept up to all resident high school students from Jackson to attend grades 9 to 12' and 'the Jackson School District Board has determined that in order to offer meaningful school choice to its residents ... make a contract in another state'. State Board approval Aug 13, 2026 in the PDF text. Contracts listed under 'Effective 2027' on https://www.sau9.org/tuitions. Raw copy: raw/districts/batch-1/jackson-jgs-high-school-options.txt
46. The Kensington School District does not run a high school; it is one of the six member districts of the Exeter Region Cooperative School District (Brentwood, East Kingston, Exeter, Kensington, Newfields and Stratham), whose middle school (grades 6-8) and high school (Exeter High School, grades 9-12) serve its students.
   - citation: Exeter Region Cooperative School District 2026 Warrant; ERCSD 2026 Deliberative Session minutes (https://drive.google.com/file/d/1PqJ1vo1dM_GxSoKVeUwa6-j-Xwxp0f1B/view)
   - source: https://drive.google.com/file/d/1-yi8u9qfh9gciyC-QlKO91JA2RLxyK2U/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Kensington
   - note: Page text: "To the inhabitants of the School Districts of the Towns of Exeter, East Kingston, Brentwood, Newfields, Stratham, and Kensington, County of Rockingham, State of New Hampshire, qualified to vote on District affairs" Warrant and minutes are scans (OCR). Minutes Article 01 gives ERCSD cost per pupil for 'Middle School (Grades 6-8)' and 'High School (Grades 9-12)'; session held at Exeter High School. Grade spans 6-8 / 9-12 from the minutes; the name 'Exeter High School' from the warrant location and minutes. This is cooperative membership, not tuition. Raw copy: raw/districts/batch-8/ercsd-warrant-2026.txt; raw/districts/batch-8/ercsd-deliberative-minutes-2026.txt
47. The Lafayette Regional School District serves students in kindergarten through grade 6 from Easton, Franconia and Sugar Hill; students in grades 7-12 from those towns attend Profile School, run by the Profile School District.
   - citation: Profile School - About Us / Employment page text (SchoolBlocks site)
   - source: https://profile.k12.nh.us
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lafayette Regional
   - note: Page text: "Lafayette Regional School District serves approximately 125 K-6 students from Easton, Franconia, and Sugar Hill. The Profile School District serves approximately 230 students in grades 7-12 from all four towns." Not a tuition arrangement: Profile is a separate district covering the same towns. Raw copy: raw/districts/batch-4/profile-pages.txt
48. The Landaff School District is a tuition-only district for all grades. Its tuition voucher says it has agreements with Bath Village School, Lafayette Regional School, Lisbon Regional School and Profile School through June 30, 2027; families must file a tuition voucher and residency statement with the SAU 35 superintendent before December 1 each year. The district contacts the bus company for students attending Lisbon and Bath.
   - citation: Landaff School District Tuition Voucher (JFABC Tuition/Voucher Policy), linked from the Landaff Tuition Process page https://sau35.org/pages/a23d2119-5d00-4f7d-8f73-5bfe3fb96551
   - source: https://docs.google.com/document/d/19YLjJAWsaovcub-5NKW2yVRXvn7fo1N4_Q3fISBHaPk/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Landaff
   - note: Page text: "The Landaff School District has agreements with the Bath Village School, Lafayette Regional School, Lisbon Regional School, and Profile School through June 30, 2027. Please submit to SAU #35 Superintendent before December 1st ANNUALLY." High school options among these: Profile School (7-12) and Lisbon Regional School (K-12). Lisbon's January 14, 2026 board minutes also mention 'verbal tuition agreements with Landaff and Bath'. Superintendent's letter PDF (https://drive.google.com/file/d/1IjH-EceyXDec0d8AyJJEVyKuhr_VpmEh) is an image and was not transcribed. Raw copy: raw/districts/batch-4/landaff-tuition-voucher.txt; raw/districts/batch-4/landaff-tuition-pages.txt
49. A Lempster resident eligible for grades 9-12 may have tuition paid by the Lempster School District to a public high school in another district, under RSA 194:27. Since a 2002-2003 policy, the tuition paid is capped at the amount paid to Lempster's 'anchor school', Fall Mountain Regional High School; the current cap is available from the SAU 71 office.
   - citation: Lempster Community School Student/Parent Handbook (linked from https://www.sau71.org)
   - source: https://drive.google.com/file/d/1dPAjFsghtzhVyysit4rSo12DJFgXe8F0/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lempster
   - note: Page text: "Any student who is eligible to attend grades 9-12 and who resides in the town of Lempster is eligible to have his/her tuition paid by the Lempster School District to a public high school in another school district in accordance with RSA 194:27 . As a result of the 2002-2003 policy, a cap has been placed on high school tuition. This amount is currently the tuition paid to our anchor school, Fall Mountain Regional High School." Handbook year not printed on the extracted pages; the SAU phone given there (863-2420 x123) differs from the site's 603-863-1080. Raw copy: raw/districts/batch-5/lempster-handbook.txt
50. The Lyme School District runs Lyme School (through grade 8); for high school, Lyme students have a choice, and the district has tuition agreements with Rivendell Academy (Orford, NH), Lebanon High School (Lebanon, NH), St. Johnsbury Academy (St. Johnsbury, VT), Hanover High School (Hanover, NH) and Thetford Academy (Thetford, VT). Students may also attend independent or private schools, with families paying the costs.
   - citation: Lyme School - High School Choice Info, General Info
   - source: https://sites.google.com/lymeschool.org/hschoiceinfo/general-info
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Lyme
   - note: Page text: "In Lyme, Students have choice for their high school experience - we have tuition agreements with the following schools: Rivendell Academy - Orford, NH Lebanon High School - Lebanon, NH St. Johnsbury Academy - St. Johnsbury, VT Hanover High - Hanover, NH Thetford Academy - Thetford, VT" Linked from lymeschool.org as 'High School Choice Information'. Quote on private schools: 'Students can also choose to attend independent/private schools, however, families are responsible for any costs associated.' Contact: School Counselor Rachel Stanton, 603.795.2125 ext 105. Tuition amounts not posted on this page. Raw copy: raw/districts/batch-7/lyme-hs-choice-general.txt
51. The Madison School District runs Madison Elementary School (K-6); Madison students in the higher grades enroll at Kennett Middle School and Kennett High School, according to the district's residency form. The form does not describe the arrangement.
   - citation: Madison School District Kindergarten Registration Packet (Residency Requirement Document for Grades K-12)
   - source: https://drive.google.com/file/d/1BwN-VAAiCfT6-ixKgUOVKEziIHbGAqCY/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Madison
   - note: Page text: "As a Madison resident, in order to enroll your child in the Madison Elementary School, Kennett Middle School, or Kennett High School, you must complete this document and provide evidence of your residency in Madison." Linked from https://www.sau13.org/home/student-registration. Raw copy: raw/districts/batch-7/madison-kindergarten-packet.txt
52. The Marlborough School District runs Marlborough School (grades K-8); its students in grades 9-12 attend Keene High School under a long-term arrangement with the Keene School District.
   - citation: Keene School District home page - Sending Towns
   - source: https://www.keeneschoolsnh.org/ksd
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlborough
   - note: Page text: "Marlborough School, SAU29, currently enrolls students in grades K-8 who reside in Marlborough, NH. Students in grades 9-12 attend Keene High School" Raw copy: raw/districts/batch-4/keene-ksd-home.txt
53. The Marlow School District runs the John D. Perkins, Sr. Academy of Marlow (grades K-6); its students in grades 7-8 attend Keene Middle School and grades 9-12 attend Keene High School under a long-term arrangement with the Keene School District.
   - citation: Keene School District home page - Sending Towns
   - source: https://www.keeneschoolsnh.org/ksd
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Marlow
   - note: Page text: "John D. Perkins, Sr. Academy of Marlow, SAU29, currently enrolls students in grades K-6 who reside in Marlow, NH. Students in grades 7-8 attend Keene Middle School ... Students in grades 9-12 attend Keene High School" Raw copy: raw/districts/batch-4/keene-ksd-home.txt
54. Mason Elementary School serves students through grade 5. Starting in grade 6, Mason students go to the Milford School District (Milford Middle School, grades 6-8, and Milford High School, grades 9-12); Mason pays their tuition and provides bus transportation. Families may instead choose other options such as school choice through open enrollment or parent-paid tuition, private or charter schools, with parents then responsible for transportation.
   - citation: Mason School District, 'After 5th Grade: Where Students Go'
   - source: https://www.sau89.nh.gov/apps/pages/index.jsp?uREC_ID=4462943&type=d&pREC_ID=2732905
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mason
   - note: Page text: "Starting in Grade 6, Mason students transition to the Milford School District to complete their middle and high school education ... Tuition: The Town of Mason pays tuition for each student attending Milford Middle School and Milford High School. Transportation: Bus transportation is provided for all Mason students attending Milford Middle School and Milford High School." Page says 'Town of Mason pays tuition'; the payer is the school district. Mason remains district of responsibility for special education. Raw copy: raw/districts/batch-3/mason-after5.txt
55. Since July 2015 the Middleton School District has had a long-term tuition agreement with the Governor Wentworth Regional School District to educate Middleton students in grades 7-12. Governor Wentworth also provides Middleton's superintendent services.
   - citation: SAU 69 - Middleton School District home
   - source: https://sites.google.com/a/sau69.org/sau-69---middleton-school-district/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Middleton
   - note: Page text: "In July 2015, the Middleton School District entered into a long-term tuition agreement with the Governor Wentworth Regional School District for the purpose of educating Middleton students in grades 7-12." Governor Wentworth's middle and high schools are Kingswood Regional Middle and High School (from GWRSD site), but the Middleton page does not name them. Raw copy: raw/districts/batch-5/middleton-sau69-home.txt
56. The Milan School District pays tuition for its students in grades 7-12; its 2026 operating budget article includes a high school total of $1,235,101, and the district's FY26 tuition cost table lists Berlin Middle School, Gorham Middle School, Berlin High School and Gorham High School.
   - citation: 2024-2025 Milan Annual School District Report
   - source: https://drive.google.com/file/d/1Bx8tKI2IgtBT-YsnTl3V33uSSKKir2Lb/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Milan
   - note: Page text: "for the payment of tuition for students in grades 7-12 (Junior High School total $583,802.87 and the High School total $1,235,101 which is included above) ... FY26 Tuition Cost # of Students Extra Students Total Berlin Middle School Gorham Middle School Berlin High School Gorham High School" The report does not describe how families choose between Berlin and Gorham (contract or choice). Raw copy: raw/districts/batch-3/milan-annual-report-2024-25.txt
57. The Monroe School District has no high school and offers school choice: it pays tuition to an approved public or independent high school chosen by parents, in or out of state (Policy JFBC). For FY26, the district funded tuition up to $24,600, and families pay any remaining amount. The district provides transportation only to St. Johnsbury Academy in Vermont.
   - citation: Monroe School District - High School Information
   - source: https://sites.google.com/a/monroeschool77.com/monroe-consolidated-school/home/high-school-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Monroe
   - note: Page text: "The town of Monroe offers school choice, tuition is funded up to $24,600.00 for FY26; any remaining tuition must be funded by families. Transportation is provided to St. Johnsbury Academy only." Policy JFBC (https://docs.google.com/document/d/1n--cD2sM-lcrKwtbEHi3efg3yrc5nn7o/edit; raw monroe-policy-jfbc.txt): 'paying tuition ... to an approved public or independent high school, to be selected by the parents or guardians of the pupil, within or without the state' and 'shall not pay a tuition amount greater than the highest announced tuition of the school to which it provides transportation'. Families get tuition vouchers through Alma. Raw copy: raw/districts/batch-1/monroe-high-school-information.txt
58. The Mont Vernon School District runs Mont Vernon Village School (kindergarten to grade 6) and pays tuition for its students to attend Amherst Middle School in grades 7 and 8. SAU 39 serves the Amherst, Mont Vernon and Souhegan Cooperative school districts, and students in grades 9-12 enroll at Souhegan High School.
   - citation: Mont Vernon Village School - Welcome; SAU 39 - New Student Information
   - source: https://sites.google.com/sau39.org/mvvs/school-info/welcome
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Mont Vernon
   - note: Page text: "before we tuition our students into Amherst Middle School for seventh and eighth grade. ... The Amherst, Mont Vernon & Souhegan Cooperative School Districts! ... Grades 9-12:" Second source: https://www.sau39.org/sau-info/new-student-information. Raw copy: raw/districts/batch-2/sau39-mvvs-welcome.txt; raw/districts/batch-2/sau39-new-student.txt
59. The Nelson School District runs Nelson Elementary School (grades K-5, also serving Sullivan children); Nelson students in grades 6-8 attend Keene Middle School and grades 9-12 attend Keene High School under a long-term arrangement with the Keene School District.
   - citation: Keene School District home page - Sending Towns
   - source: https://www.keeneschoolsnh.org/ksd
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nelson
   - note: Page text: "Nelson Elementary School, SAU 29, currently enrolls students in grades K-5 who reside in Nelson, NH and Sullivan, NH. Nelson students in grades 6-8 attend Keene Middle School ... Nelson students in grades 9-12 attend Keene High School" Raw copy: raw/districts/batch-4/keene-ksd-home.txt
60. The New Boston School District runs New Boston Central School and pays tuition for its students at Goffstown's Mountain View Middle School and Goffstown High School under an AREA agreement with the Goffstown School District; the tuition is calculated with a formula in that agreement. The FY26 (2025-26) budget assumed 157 New Boston students at Mountain View and 338 at Goffstown High School.
   - citation: 2025 New Boston School District Warrant Article Voters' Guide (FY26)
   - source: https://www.sau19.org/attachments/article/751/NBSD%20-FINAL%20-Voters%20Guide%20FY%2026%20School%20Year%202-5-2025_247.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Boston
   - note: Page text: "The proposed operating budget also includes the cost of tuition for New Boston to send 157 students to Mountain View Middle School (the same as in FY 25 ) and 338 students to Goffstown High School (decrease of 1). The tuition payments to the Goffstown School District are calculated using a formula from the AREA Agreement ." SAU 19 posts the signed 'Final AREA Agreement (2024-2034) with Appendix A and B' at https://www.sau19.org/attachments/article/215/Final%20AREA%20Agreement%20%28%202024-2034%29%20%20with%20Appendix%20A%20and%20B%20%28Signed%29%20%204-18-2022.pdf (scanned; no text layer, raw goffstown-newboston-area-agreement-2024-2034.pdf). The guide names the schools, not the grade levels. Raw copy: raw/districts/batch-7/newboston-voters-guide-fy26.txt
61. The New Castle School District runs Maude H. Trefethen School (K-5); its students in grades 6-8 attend either Portsmouth Middle School or Rye Junior High School. SAU 50 Policy JFAC says the SAU 50 districts pay the per diem tuition rate charged by the Portsmouth School District for resident high school students under their Authorized Regional Enrollment Area (AREA) agreement.
   - citation: SAU 50 Policy JFAC, Tuition for Resident High School Students; SAU 50 schools overview (https://www.sau50.org/pages/32bfca09-8390-4f0b-bc2d-c425b4ea9011)
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district New Castle
   - note: Page text: "According to the Authorized Regional Enrollment Area agreement, the school districts of SAU 50 will pay the per diem tuition rate charged by the Portsmouth School District." Schools page gives grades 6-8 only for New Castle; the high school (Portsmouth) is from policy JFAC, which names Portsmouth's tuition rate but not the school by name. Raw copy: raw/districts/batch-8/sau50-policies.txt; raw/districts/batch-8/sau50-schools.txt
62. The Newfields School District does not run a high school; it is one of the six member districts of the Exeter Region Cooperative School District (Brentwood, East Kingston, Exeter, Kensington, Newfields and Stratham), whose middle school (grades 6-8) and high school (Exeter High School, grades 9-12) serve its students.
   - citation: Exeter Region Cooperative School District 2026 Warrant; ERCSD 2026 Deliberative Session minutes (https://drive.google.com/file/d/1PqJ1vo1dM_GxSoKVeUwa6-j-Xwxp0f1B/view)
   - source: https://drive.google.com/file/d/1-yi8u9qfh9gciyC-QlKO91JA2RLxyK2U/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newfields
   - note: Page text: "To the inhabitants of the School Districts of the Towns of Exeter, East Kingston, Brentwood, Newfields, Stratham, and Kensington, County of Rockingham, State of New Hampshire, qualified to vote on District affairs" Warrant and minutes are scans (OCR). Minutes Article 01 gives ERCSD cost per pupil for 'Middle School (Grades 6-8)' and 'High School (Grades 9-12)'; session held at Exeter High School. Grade spans 6-8 / 9-12 from the minutes; the name 'Exeter High School' from the warrant location and minutes. This is cooperative membership, not tuition. Raw copy: raw/districts/batch-8/ercsd-warrant-2026.txt; raw/districts/batch-8/ercsd-deliberative-minutes-2026.txt
63. The Newington School District runs Newington Public School (Pre-K-6); its students in grades 7-8 attend Portsmouth Middle School and in grades 9-12 Portsmouth High School. Under SAU 50 Policy JFAC, the SAU 50 districts pay the per diem tuition rate charged by the Portsmouth School District under their Authorized Regional Enrollment Area (AREA) agreement.
   - citation: SAU 50 Policy JFAC, Tuition for Resident High School Students; SAU 50 schools overview (https://www.sau50.org/pages/32bfca09-8390-4f0b-bc2d-c425b4ea9011)
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Newington
   - note: Page text: "According to the Authorized Regional Enrollment Area agreement, the school districts of SAU 50 will pay the per diem tuition rate charged by the Portsmouth School District." Schools page: 'Students in grades 7-8 attend Portsmouth Middle School; students in grades 9-12 attend Portsmouth High School.' Raw copy: raw/districts/batch-8/sau50-policies.txt; raw/districts/batch-8/sau50-schools.txt
64. North Hampton is a member of the Winnacunnet Cooperative School District; many North Hampton School graduates go on to Winnacunnet High School in Hampton, the public cooperative high school for Hampton, Seabrook, Hampton Falls and North Hampton, and some families choose private high schools.
   - citation: North Hampton School - On to High School
   - source: https://www.northhamptonschool.org/families/on-to-high-school/index
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district North Hampton
   - note: Page text: "Many of our students matriculate to Winnacunnet High School, our public cooperative high school located in Hampton, New Hampshire. Some of our families choose to send their children to private high schools." Raw copy: raw/districts/batch-7/northhampton-on-to-high-school.txt
65. The Northwood School District runs Northwood School through grade 8; high-school-age students who live in Northwood are enrolled at Coe-Brown Northwood Academy, and the district pays their tuition. The 2026-27 budget projects 175 students at a cost of $21,617 each.
   - citation: SAU 44 - High School Registration and Residency; 2026 Deliberative Session Packet (https://aptg.co/xX6DT7)
   - source: https://www.sau44.org/o/sau/page/high-school-registration-and-residency
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Northwood
   - note: Page text: "Families of high school aged students moving into the town of Northwood are enrolled in Coe-Brown Northwood Academy." Registration page: 'This ensures that the correct town of residence is reponsible for paying your tuition to Coe-Brown.' Packet line 'Tuition Coe Brown HS ... $3,847,826.00' with note 'This represents 175 projected students ... The cost per student is $21,617 for SY27.' Families file a High School Assignment form with SAU 44. Raw copy: raw/districts/batch-8/northwood-hs-registration.txt; raw/districts/batch-8/northwood-deliberative-packet-2026.txt
66. The Nottingham School District runs Nottingham School (through grade 8) and no high school. Its website's High Schools page lists Coe-Brown Northwood Academy, Dover High School and the Dover Career Technical Center. The page does not describe the tuition arrangement.
   - citation: Nottingham School - High Schools
   - source: https://www.nottingham.k12.nh.us/community-resources/high-schools
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Nottingham
   - note: Page text: "High Schools ... Coe Brown Northwood Academy ... Dover High School ... Dover Career Technical Center" Arrangement (contract, choice) not stated on the site. Raw copy: raw/districts/batch-2/nottingham-high-schools.txt
67. The Pasquaney School District runs Bridgewater-Hebron Village School (pre-K to grade 6) and no high school. At its March 2025 annual meeting, voters were asked to approve a reciprocal tuition agreement with the Newfound Area School District for middle and high school (up to four years from July 1, 2025) and a memorandum of understanding with the Pemi-Baker Regional School District (SAU 48, Plymouth) for grades 9-12, which the superintendent describes as giving families high school enrollment choice.
   - citation: Pasquaney School District Annual Report, March 17, 2026 (Superintendent's report; March 2025 meeting minutes)
   - source: https://aptg.co/_b-b0k
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Pasquaney
   - note: Page text: "we maintained our partnership with SAU 48, providing families with high school enrollment choice." Minutes: 'ratify and approve the Reciprocal Tuition Agreement between the Pasquaney School District and the Newfound Area School District for the education of Pasquaney students in middle and high school' and 'Memorandum of Understanding between the Pasquaney School District and the Pemi-Baker Regional School District, for the education of Pasquaney students in grades 9-12'. Article outcomes not quoted here; the superintendent's report says SAU 4 (Newfound) enrollment support and the SAU 48 partnership continued. Raw copy: raw/districts/batch-8/pasquaney-annual-report.txt
68. The Plainfield School District is part of an AREA agreement and pays tuition for all its high school students to attend Lebanon High School. Families contact the Plainfield SAU office before enrolling a student at Lebanon High School.
   - citation: Plainfield School District - Registration Information
   - source: https://www.plainfieldschool.org/page/registration-information
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Plainfield
   - note: Page text: "Plainfield is part of the AREA agreement and tuitions all high school students to Lebanon High School." The two registration pages give different SAU phone numbers (603.469.3250 ext. 263 and 603.469.3442). Site also links Kimball Union Academy, without saying it is a tuition option. Raw copy: raw/districts/batch-5/plainfield-registration-info.txt; raw/districts/batch-5/plainfield-enrollment.txt
69. Plymouth is one of the seven towns of the Pemi-Baker Regional School District, whose high school is Plymouth Regional High School: the Pemi-Baker 2026 warrant lists a Plymouth polling place (Plymouth Elementary School) for its March 10, 2026 ballot vote, and the SAU 48 site lists Plymouth Regional High School as the Pemi Baker Regional high school.
   - citation: Pemi-Baker Regional School District 2026 Warrant (polling places by member town)
   - source: https://drive.google.com/file/d/18H7G1QTwK8BX2_6mSdPmeZrtC6HPWRN_/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Plymouth
   - note: Page text: "The inhabitants of the Regional School District of Pemi-Baker ... Ashland ... Campton ... Holderness ... Plymouth – 8:00 a.m. to 7:00 p.m. – Plymouth Elementary School Gym Rumney ... Thornton ... Wentworth" Quote abridged with '...' from the warrant's polling list. Membership is shown by the regional warrant's polling places; the warrant does not use the word 'member'. Cooperative membership, not a tuition arrangement. Coordinator: reworded so the statement says only what the warrant and SAU 48 page show; no page found states in words which grades the town's students attend. SAU 48 page: raw/districts/batch-6/sau48-pemibaker.txt. Raw copy: raw/districts/batch-6/pemibaker-warrant-2026.txt
70. The Rollinsford School District runs Rollinsford Grade School (K-6). Through a partnership with Maine School Administrative District (MSAD) 35 in South Berwick, Maine, Rollinsford students in grades 7-12 attend Marshwood Middle School and Marshwood High School.
   - citation: SAU 104 home, 'Welcome to SAU 104'
   - source: https://www.sau104.org/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rollinsford
   - note: Page text: "the Rollinsford School District includes Rollinsford Grade School, a K-6 elementary school and, through a partnership with Maine School Administrative District (MSAD) 35 in South Berwick, Maine, Rollinsford students in grade 7-12 attend school in the Marshwood School District." Interstate arrangement; tuition amounts not checked. Raw copy: raw/districts/batch-3/rollinsford-sau104.txt
71. Rumney is one of the seven towns of the Pemi-Baker Regional School District, whose high school is Plymouth Regional High School: the Pemi-Baker 2026 warrant lists a Rumney polling place (Russell Elementary School) for its March 10, 2026 ballot vote, and the SAU 48 site lists Plymouth Regional High School as the Pemi Baker Regional high school.
   - citation: Pemi-Baker Regional School District 2026 Warrant (polling places by member town)
   - source: https://drive.google.com/file/d/18H7G1QTwK8BX2_6mSdPmeZrtC6HPWRN_/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rumney
   - note: Page text: "Rumney – 8:00 a.m. to 7:00 p.m. – Russell Elementary School" Cooperative membership shown by regional polling place. Coordinator: reworded so the statement says only what the warrant and SAU 48 page show; no page found states in words which grades the town's students attend. SAU 48 page: raw/districts/batch-6/sau48-pemibaker.txt. Raw copy: raw/districts/batch-6/pemibaker-warrant-2026.txt
72. The Rye School District does not run a high school; Rye students in grades 9-12 attend Portsmouth High School. Under SAU 50 Policy JFAC, the SAU 50 districts pay the per diem tuition rate charged by the Portsmouth School District under their Authorized Regional Enrollment Area (AREA) agreement.
   - citation: SAU 50 Policy JFAC, Tuition for Resident High School Students; SAU 50 schools overview (https://www.sau50.org/pages/32bfca09-8390-4f0b-bc2d-c425b4ea9011)
   - source: https://www.sau50.org/pages/2d7687e0-b29d-4edb-be9c-3d8ade7f1ec8
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Rye
   - note: Page text: "According to the Authorized Regional Enrollment Area agreement, the school districts of SAU 50 will pay the per diem tuition rate charged by the Portsmouth School District." Schools page: 'Rye students in grades 9-12 attend Portsmouth High School.' Raw copy: raw/districts/batch-8/sau50-policies.txt; raw/districts/batch-8/sau50-schools.txt
73. Seabrook is a member of the Winnacunnet Cooperative School District; Winnacunnet High School in Hampton, a public cooperative high school, serves the towns of Hampton, Seabrook, Hampton Falls and North Hampton.
   - citation: North Hampton School - On to High School (SAU 21)
   - source: https://www.northhamptonschool.org/families/on-to-high-school/index
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Seabrook
   - note: Page text: "The school serves the towns of Hampton, Seabrook, Hampton Falls, and North Hampton." Seabrook runs Seabrook Elementary and Seabrook Middle School. Membership in the cooperative also shown by Seabrook voting in the Winnacunnet ballot (SAU 21 voting page). Raw copy: raw/districts/batch-7/northhampton-on-to-high-school.txt
74. The Stoddard School District has no high school of its own and pays tuition for its high school students; its fall 2026 budget presentation lists 'Keene and HD tuition' among anticipated FY2028 cost increases. The district site does not list the high school options in more detail.
   - citation: SAU 24 Stoddard Public Hearing presentation, fall 2026
   - source: https://www.sau24.org/school-boards/stoddard/files/documents/SAU%2024_Stoddard%20Public%20Hearing.pptx%20-%20Google%20Slides.pdf
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stoddard
   - note: Page text: "Anticipated cost increases identified for FY28 Contracts, tuition, special education, insurance and transportation ... Keene and HD tuition (5% rate, 9 fewer students) $20,000" 'HD' is not spelled out on the slide. Whether the tuition covers only high school or also other grades is not stated. Raw copy: raw/districts/batch-3/stoddard-public-hearing.txt
75. The Strafford School District has no high school; Coe-Brown Northwood Academy is its high school of record. A parent may ask the Superintendent, with School Board approval, to reassign a student to another public high school that has accepted the student; the family is then responsible for transportation and for any tuition above Coe-Brown Northwood Academy's annual rate.
   - citation: Strafford School District - High School Reassignment Request form (linked from SAU 105 'Other Important Information' page)
   - source: https://drive.google.com/file/d/1Sx9pRXEn6yx9O4KdNgfn8bOpISTWVTcJ/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Strafford
   - note: Page text: "to reassign a pupil from Coe-Brown Northwood Academy (CBNA), our high school of record, to another public high school where the pupil has been accepted. ... Tuition above that of Coe Brown Northwood Academy’s annual rate for the assigned school year is the responsibility of the parent/guardian." Page: https://sites.google.com/strafford.k12.nh.us/straffordsau/other-important-information (also links a CBNA Assignment Form). Raw copy: raw/districts/batch-2/strafford-hs-reassignment-form.txt; raw/districts/batch-2/strafford-other-info.txt
76. The Stratham School District does not run a high school; it is one of the six member districts of the Exeter Region Cooperative School District (Brentwood, East Kingston, Exeter, Kensington, Newfields and Stratham), whose middle school (grades 6-8) and high school (Exeter High School, grades 9-12) serve its students.
   - citation: Exeter Region Cooperative School District 2026 Warrant; ERCSD 2026 Deliberative Session minutes (https://drive.google.com/file/d/1PqJ1vo1dM_GxSoKVeUwa6-j-Xwxp0f1B/view)
   - source: https://drive.google.com/file/d/1-yi8u9qfh9gciyC-QlKO91JA2RLxyK2U/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Stratham
   - note: Page text: "To the inhabitants of the School Districts of the Towns of Exeter, East Kingston, Brentwood, Newfields, Stratham, and Kensington, County of Rockingham, State of New Hampshire, qualified to vote on District affairs" Warrant and minutes are scans (OCR). Minutes Article 01 gives ERCSD cost per pupil for 'Middle School (Grades 6-8)' and 'High School (Grades 9-12)'; session held at Exeter High School. Grade spans 6-8 / 9-12 from the minutes; the name 'Exeter High School' from the warrant location and minutes. This is cooperative membership, not tuition. Raw copy: raw/districts/batch-8/ercsd-warrant-2026.txt; raw/districts/batch-8/ercsd-deliberative-minutes-2026.txt
77. The Surry School District pays tuition for its students to attend Keene's elementary, middle and high schools (Wheelock School, Keene Middle School and Keene High School). Surry is part of an AREA agreement with Keene for grades 6-12 that gives a 2.5% tuition discount in exchange for a 20-year commitment, and because of the contract Surry cannot pay tuition for schools in other towns, charter schools or private schools. Transportation is provided to Wheelock, Keene Middle and Keene High.
   - citation: Town of Surry - Surry School District
   - source: https://surry.nh.gov/surry-school-district/
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Surry
   - note: Page text: "Surry tuitions its students to Keene, NH elementary, middle, and senior high schools. Surry is part of the AREA agreement for grades 6-12 with Keene that provides a 2.5% tuition discount in exchange for a 20-year commitment to send our students." Page is on the town website but written by/about the Surry School District (SAU 91). Raw copy: raw/districts/batch-5/surry-school-district.txt
78. The Tamworth School District runs Kenneth A. Brett School (K-8); its school site has information for 8th graders transitioning to Kennett High School, and a 2024 district notice describes a contract between Tamworth and Moultonborough allowing up to 6 Tamworth students to attend Moultonborough Academy starting in September 2024.
   - citation: Kenneth A. Brett School - High School Options Committee; Kennett High School Information
   - source: https://sites.google.com/tamworth.k12.nh.us/welcome-ka-brett-school/high-school-options-committee
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Tamworth
   - note: Page text: "the recently signed contract between Tamworth and Moultonborough which provides for up to 6 Tamworth students to attend Moultonborough Academy in September of 2024." Kennett page: https://sites.google.com/tamworth.k12.nh.us/welcome-ka-brett-school/home/kennett-high-school-information ('Transitioning to Kennett High School Information', info night December 5, 2024). Pages are from 2024; the current arrangement was not confirmed. Raw copy: raw/districts/batch-7/tamworth-hs-options-committee.txt; raw/districts/batch-7/tamworth-kennett-info.txt
79. Thornton is one of the seven towns of the Pemi-Baker Regional School District, whose high school is Plymouth Regional High School: the Pemi-Baker 2026 warrant lists a Thornton polling place (Thornton Central School) for its March 10, 2026 ballot vote, and the SAU 48 site lists Plymouth Regional High School as the Pemi Baker Regional high school.
   - citation: Pemi-Baker Regional School District 2026 Warrant (polling places by member town)
   - source: https://drive.google.com/file/d/18H7G1QTwK8BX2_6mSdPmeZrtC6HPWRN_/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Thornton
   - note: Page text: "Thornton – 8:00 a.m. to 7:00 p.m. – Thornton Central School" Cooperative membership shown by regional polling place. Coordinator: reworded so the statement says only what the warrant and SAU 48 page show; no page found states in words which grades the town's students attend. SAU 48 page: raw/districts/batch-6/sau48-pemibaker.txt. Raw copy: raw/districts/batch-6/pemibaker-warrant-2026.txt
80. The Warren School District has no high school. Under its High School Tuition Policy (JFB), Warren has a multi-year tuition agreement with the Haverhill Cooperative School District for students to attend Woodsville High School. Through a voucher program, families may instead choose Plymouth Regional High School, Rivendell Academy or St. Johnsbury Academy. Warren pays up to the Woodsville tuition amount, parents pay any cost above that, and Warren does not pay for high school transportation.
   - citation: SAU 23 Board Policies, Section J (Google Doc linked from https://www.sau23.org/sau-23/school-boards/board-policies) - JFB Warren School District High School Tuition Policy (adopted June 10, 2014; revised November 9, 2016)
   - source: https://docs.google.com/document/d/19lj7kHI12uVHodbLgGILRoN2TS8Mi_sr7qk6aaeHi60/edit
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Warren
   - note: Page text: "The Warren School District has a multi-year tuition agreement with the Haverhill Cooperative School District for high school students to attend Woodsville High School. The Warren School District has agreed to a voucher program that will allow students to attend Plymouth Regional High School, Rivendell Academy or St. Johnsbury Academy" Raw copy: raw/districts/batch-1/sau23-policies-section-j.txt
81. The Washington School District runs one elementary school (kindergarten to grade 5). By agreement, its students in grades 6 through 12 are tuitioned to Hillsboro-Deering Middle and High Schools.
   - citation: Washington School District FY 2027 Proposed Budget (December 2025), Profile of the School District
   - source: https://drive.google.com/file/d/1E1HObtJUXlS5qnMjStdm9Ux4YIzpa8a9/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Washington
   - note: Page text: "By agreement, students in grades six through twelve are tuitioned to Hillsboro-Deering Middle and High Schools." Same page: 'As of October 1, 2025, the total student population of the Washington School District was 93 with 49 of those students tuitioned to other districts.' Tuition rates not extracted. Raw copy: raw/districts/batch-6/washington-budget-book-fy27.txt
82. Waterville Valley Elementary School serves kindergarten through grade 8. The Waterville Valley School District pays tuition for resident students who attend Plymouth Regional High School.
   - citation: Waterville Valley Elementary School Parent/Student Handbook 2026-2027
   - source: https://drive.google.com/file/d/17WryCmCTHMLkS36mjvakfa0yb1AW6TN1/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Waterville Valley
   - note: Page text: "Waterville Valley Elementary School is a kindergarten through grade eight (8) public school. The Waterville Valley Elementary School District is responsible for the tuition of students residing in Waterville Valley who attend Plymouth Regional High School." Does not say whether other high schools are allowed; type of agreement not stated. Raw copy: raw/districts/batch-6/waterville-handbook-2627.txt
83. Weare is one of the two towns (with Henniker) in the John Stark Regional School District, which runs John Stark Regional High School in Weare; the John Stark warrant is addressed to the inhabitants of Henniker and Weare.
   - citation: John Stark School District 2026 School Warrant (signed 1.15.26)
   - source: https://drive.google.com/file/d/14atMFMSRurjikAmEIDq02oIB4pLra41g/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Weare
   - note: Page text: "JOHN STARK SCHOOL DISTRICT THE STATE OF NEW HAMPSHIRE 2026 SCHOOL WARRANT To the inhabitants of the School District in the towns of Henniker and Weare" Cooperative (regional) membership, not tuition. The SAU site does not state in words which grades John Stark serves; the site database lists John Stark Regional High School. Raw copy: raw/districts/batch-3/johnstark-warrant-2026.txt
84. Wentworth is one of the seven towns of the Pemi-Baker Regional School District, whose high school is Plymouth Regional High School: the Pemi-Baker 2026 warrant lists a Wentworth polling place (Wentworth Elementary School) for its March 10, 2026 ballot vote, and the SAU 48 site lists Plymouth Regional High School as the Pemi Baker Regional high school.
   - citation: Pemi-Baker Regional School District 2026 Warrant (polling places by member town)
   - source: https://drive.google.com/file/d/18H7G1QTwK8BX2_6mSdPmeZrtC6HPWRN_/view?usp=sharing
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Wentworth
   - note: Page text: "Wentworth – 11:00 a.m. to 7:00 p.m. – Wentworth Elementary School" Cooperative membership shown by regional polling place. Coordinator: reworded so the statement says only what the warrant and SAU 48 page show; no page found states in words which grades the town's students attend. SAU 48 page: raw/districts/batch-6/sau48-pemibaker.txt. Raw copy: raw/districts/batch-6/pemibaker-warrant-2026.txt
85. The Westmoreland School District runs Westmoreland School (grades K-8); its students in grades 9-12 attend Keene High School under a long-term arrangement with the Keene School District.
   - citation: Keene School District home page - Sending Towns
   - source: https://www.keeneschoolsnh.org/ksd
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Westmoreland
   - note: Page text: "Westmoreland School, SAU29, currently enrolls students in grades K-8 who reside in Westmoreland, NH. Students in grades 9-12 attend Keene High School" Raw copy: raw/districts/batch-4/keene-ksd-home.txt
86. The Windsor School District operates no schools. By agreement, its students in kindergarten through grade 12 are tuitioned to the Hillsboro-Deering School District, with limited capacity to attend Washington Elementary School beginning in 2026-27. The FY2027 budget uses Hillsboro-Deering tuition rates of $25,719 (elementary), $25,409 (middle school) and $27,171 (high school).
   - citation: Windsor FY2027 Budget Book Updated February 2026, Profile of the School District and Proposed FY27 Budget
   - source: https://drive.google.com/file/d/1QPPtCSb5exTtJiUQ9t21OSFy8Sr5-YZg/view
   - as_of: 2026-11-08
   - review_by: 2027-11-08
   - place: district Windsor
   - note: Page text: "The Windsor School District does not operate any schools. By agreement, students in kindergarten through grade twelve are tuitioned to the Hillsboro-Deering School District. There is also a limited capacity for students to attend Washington Elementary School beginning in the 2026-2027 school year." Tuition rates quoted in budget book: 'Hillsboro-Deering High School Tuition Rate: $27,171.00' etc. The book also says the district must provide transportation through grade eight. As of October 1, 2025, Windsor had 11 students. Raw copy: raw/districts/batch-6/windsor-budget-book-fy27.txt

## SAU websites and contacts

Where to ask: each SAU's home page and contact page, as found during this check.

| SAU | Districts | Website and contact (as found) | Source |
|---|---|---|---|
| 1 | Contoocook Valley | SAU 1 (ConVal School District) website: https://conval.edu/en-US; school board site: https://schoolboard.conval.edu/en-us. Office: 106 Hancock Rd, Peterborough, NH 03458, 603-924-3336. | https://conval.edu/en-US (as of 2026-11-08) |
| 2 | Ashland, Inter-Lakes Cooperative | SAU 2 (Inter-Lakes and Ashland School Districts) website: https://sau2.k12.nh.us ; Inter-Lakes School District: https://www.interlakes.org (103 Main Street, Meredith; 603-279-7947). | https://www.interlakes.org/school-board/budget (as of 2026-11-08) |
| 3 | Berlin | SAU 3 (Berlin Public Schools) website: https://www.sau3.org; central office page: https://www.sau3.org/page/central-office-sau3. | https://www.sau3.org (as of 2026-11-08) |
| 4 | Newfound Area | SAU 4 (Newfound Area School District) website: https://www.sau4.org. Office: 20 North Main Street, Bristol, NH 03222, phone 603-744-5555. | https://www.sau4.org/ (as of 2026-11-08) |
| 5 | Oyster River Coop | SAU 5 (Oyster River Cooperative School District) website: https://www.orcsd.org; contact page: https://www.orcsd.org/about/district-directory. | https://www.orcsd.org (as of 2026-11-08) |
| 6 | Claremont | SAU 6 (Claremont and Unity) website: https://www.sau6.org/ ; contact page: https://www.sau6.org/contact-us ; office 165 Broad Street, Claremont, phone (603) 543-4200. | https://www.sau6.org/ (as of 2026-11-08) |
| 7 | Clarksville, Colebrook, Columbia, Pittsburg, Stewartstown | SAU 7 (Clarksville, Colebrook, Columbia, Pittsburg and Stewartstown school districts) website: https://www.sau7.org/ ; 21 Academy St, Colebrook, NH 03576, phone 603-237-5571. | https://www.sau7.org/pages/222e630d-edcd-4617-ad37-ff173b145b33 (as of 2026-11-08) |
| 8 | Concord | SAU 8 (Concord School District) website: https://sau8.org ; contact page: https://sau8.org/contact-us (38 Liberty St, Concord; 603-225-0811). | https://sau8.org/contact-us (as of 2026-11-08) |
| 9 | Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location, Jackson | SAU 9 (Albany, Bartlett, Chatham, Conway, Eaton, Hart's Location and Jackson school districts) website: https://www.sau9.org/ ; contact page: https://www.sau9.org/contact-us | https://www.sau9.org/contact-us (as of 2026-11-08) |
| 10 | Derry Cooperative | SAU 10 (Derry Cooperative School District) website: https://www.sau10.nh.gov; SAU directory: https://www.sau10.nh.gov/about/sau-directory. Office: 28 South Main Street, Derry, NH 03038, (603) 432-1210. | https://www.sau10.nh.gov/about/index (as of 2026-11-08) |
| 11 | Dover | SAU 11 (Dover School District) website. Contact page: https://www.sau11.nh.gov/apps/pages/index.jsp?uREC_ID=1236202&type=d&pREC_ID=2114968 | https://www.sau11.nh.gov/ (as of 2026-11-08) |
| 12 | Londonderry | SAU 12 (Londonderry School District) website: https://www.londonderry.org. District office: 6A Kitty Hawk Landing, Londonderry, NH 03053, phone 603-432-6920. | https://www.londonderry.org (as of 2026-11-08) |
| 13 | Freedom, Madison, Tamworth | SAU 13 (Freedom, Madison, Tamworth) website: https://www.sau13.org/; office 881A Tamworth Road, Tamworth, phone 603-323-5088. Contact page: https://www.sau13.org/home/student-registration | https://www.sau13.org/ (as of 2026-11-08) |
| 14 | Epping | SAU 14 (Epping School District) website: https://www.sau14.org, with a contact page at https://www.sau14.org/contact. | https://www.sau14.org/ (as of 2026-11-08) |
| 15 | Auburn, Candia, Hooksett | SAU 15 (Auburn, Candia and Hooksett school districts) website: https://sau15.net/; district sites: https://hooksett.sau15.net/, https://auburn.sau15.net/, https://candia.sau15.net/; school board sites at hooksettschoolboard.sau15.net, auburnschoolboard.sau15.net and candiaschoolboard.sau15.net. About SAU 15: https://sau15.net/about-sau-15/. | https://sau15.net/ (as of 2026-11-08) |
| 16 | Brentwood, East Kingston, Exeter, Exeter Region Cooperative, Kensington, Newfields, Stratham | SAU 16 (Exeter area) website. Contact page: https://www.sau16.org/en-US/pages/ceeefbec-b6ca-454f-a21e-febdcc15210a | https://www.sau16.org/en-US (as of 2026-11-08) |
| 17 | Sanborn Regional | SAU 17 (Sanborn Regional School District, Kingston and Newton) website: https://www.sau17.net (phone 603-642-3688). | https://www.sau17.net/ (as of 2026-11-08) |
| 18 | Franklin | SAU 18 (Franklin School District) website: https://www.sau18.nh.gov/ ; 119 Central St., Franklin, NH 03235, phone (603) 934-3108. | https://www.sau18.nh.gov/page/mandatory-information-for-voters (as of 2026-11-08) |
| 19 | Goffstown, New Boston | SAU 19 (Goffstown, New Boston) website: https://www.sau19.org/; SAU office 11 School Street, Goffstown, phone (603) 497-4818. Contact page: https://www.sau19.org/index.php/en/information-8/information2/sau19-info | https://www.sau19.org/ (as of 2026-11-08) |
| 20 | Dummer, Errol, Gorham Randolph Shelburne Cooperative, Milan | SAU 20 (Gorham Randolph Shelburne, Milan, Errol and Dummer school districts) website: https://www.sau20.org/; district directory: https://www.sau20.org/district-directory. Office: 123 Main Street, Gorham, NH 03581, (603) 466-3632. | https://www.sau20.org/ (as of 2026-11-08) |
| 21 | Hampton Falls, North Hampton, Seabrook, South Hampton, Winnacunnet Cooperative | SAU 21 (Winnacunnet, Hampton Falls, North Hampton, Seabrook, South Hampton) website: https://www.sau21.nh.gov/; contact form https://forms.office.com/r/CSjDGnrh0t. | https://www.sau21.nh.gov/ (as of 2026-11-08) |
| 23 | Bath, Benton, Haverhill Cooperative, Piermont, Warren | SAU 23 (Bath, Benton, Haverhill Cooperative, Piermont and Warren school districts) website: https://www.sau23.org/ ; 2975 Dartmouth College Highway, North Haverhill, NH 03774, tel (603) 787-2113. School contacts: https://www.sau23.org/our-schools | https://www.sau23.org/sau-23/2026-budget-infographic (as of 2026-11-08) |
| 24 | Henniker, John Stark Regional, Stoddard, Weare | SAU 24 (Henniker, John Stark Regional, Stoddard and Weare school districts) website: https://www.sau24.org/; staff directory: https://www.sau24.org/about/staff-directory. Office: 258 Western Ave, Henniker, NH 03242. | https://www.sau24.org/ (as of 2026-11-08) |
| 25 | Bedford | SAU 25 (Bedford School District) website: https://sites.google.com/bedfordnhk12.net/sau-25-bedford-school-district/home; SAU staff: https://sites.google.com/bedfordnhk12.net/sau-25-bedford-school-district/information/sau-staff. District office: 103 County Road, Bedford, NH 03110, 603-472-3755. | https://sites.google.com/bedfordnhk12.net/sau-25-bedford-school-district/home (as of 2026-11-08) |
| 26 | Merrimack | SAU 26 (Merrimack School District) website: https://www.sau26.org/ ; central office contacts: https://www.sau26.org/about-us/contacts-central-office ; 36 McElwain St., Merrimack, (603) 424-6200. | https://www.sau26.org/ (as of 2026-11-08) |
| 27 | Litchfield | SAU 27 (Litchfield School District) website: https://www.litchfieldsd.org/ ; contacts page: https://www.litchfieldsd.org/SAU27StaffMembers.aspx ; office 1 Highlander Court, Litchfield, phone 603-578-3570. | https://www.litchfieldsd.org/ (as of 2026-11-08) |
| 28 | Pelham | SAU 28 (Pelham School District) website: https://www.pelhamsd.org/; contact guide https://www.pelhamsd.org/ContactGuide.aspx; SAU office phone (603) 635-1145. | https://www.pelhamsd.org/ (as of 2026-11-08) |
| 29 | Chesterfield, Harrisville, Keene, Marlborough, Marlow, Nelson, Westmoreland | SAU 29 (Keene, Chesterfield, Harrisville, Marlborough, Marlow, Nelson and Westmoreland school districts) website: https://www.sau29.org. Central office: 193 Maple Avenue, Keene, NH 03431, phone (603) 357-9002. The Keene School District site is https://www.keeneschoolsnh.org. | https://www.sau29.org/ (as of 2026-11-08) |
| 30 | Laconia | SAU 30 (Laconia School District) website: https://www.sau30.org (the old site laconiaschools.org says it is no longer updated); district office staff page: https://www.sau30.org/district-office-staff.html; office at 39 Harvard Street, Laconia, (603) 524-5710. | https://www.sau30.org (as of 2026-11-08) |
| 31 | Newmarket | SAU 31 (Newmarket School District) website. Contact page: https://www.newmarket.k12.nh.us/about/contact-us | https://www.newmarket.k12.nh.us/ (as of 2026-11-08) |
| 32 | Plainfield | SAU 32 (Plainfield School District) website: https://www.plainfieldschool.org ; contact page: https://www.plainfieldschool.org/page/contact (phone 603-469-3250). | https://www.plainfieldschool.org/ (as of 2026-11-08) |
| 33 | Raymond | SAU 33 (Raymond School District) website: https://www.sau33.com; contact page: https://www.sau33.com/district/pages/contact-us; office at 43 Harriman Hill Road, Raymond, 603-895-4299. | https://www.sau33.com (as of 2026-11-08) |
| 34 | Hillsboro-Deering Cooperative, Washington, Windsor | SAU 34 (Hillsboro-Deering Cooperative, Washington and Windsor) website: https://sau34.org/ ; office 78 School St, 3rd Floor, Hillsboro, phone 603-464-4466. | https://sau34.org/en-US (as of 2026-11-08) |
| 35 | Bethlehem, Lafayette Regional, Landaff, Profile | SAU 35 (White Mountains SAU: Bethlehem, Lafayette Regional, Landaff and Profile school districts) website: https://www.sau35.org. Office: 691 Profile Road, Bethlehem, NH 03574, phone 603-444-3925. School sites: https://bethlehem.k12.nh.us, https://lafayetteregional.org, https://profile.k12.nh.us. | https://www.sau35.org/en-US (as of 2026-11-08) |
| 36 | White Mountains Regional | SAU 36 (White Mountains Regional School District) website: https://www.sau36.org/. Office: 135 Regional Road, Whitefield, NH 03598, 603-837-9363, commentsandquestions@sau36.org. | https://www.sau36.org/ (as of 2026-11-08) |
| 37 | Manchester | SAU 37 (Manchester School District) website: https://www.mansd.org/ ; district office 20 Hecker Street, Manchester, phone (603) 624-6300. | https://www.mansd.org/ (as of 2026-11-08) |
| 39 | Amherst, Mont Vernon, Souhegan Cooperative | SAU 39 (Amherst, Mont Vernon and Souhegan Cooperative school districts) website: https://www.sau39.org; contact page: https://www.sau39.org/sau-info/contact-information; office at 1 School Street, Amherst, (603) 673-2690. | https://www.sau39.org (as of 2026-11-08) |
| 40 | Milford | SAU 40 (Milford School District) website: https://www.milfordk12.org/ ; contact page: https://www.milfordk12.org/apps/contact/ ; phone (603) 673-2202. | https://www.milfordk12.org/ (as of 2026-11-08) |
| 41 | Brookline, Hollis, Hollis-Brookline Cooperative | SAU 41 (Hollis, Brookline and Hollis-Brookline Cooperative School Districts) website: https://www.sau41.org (4 Lund Lane, Hollis; 603-324-5999); voter information: https://www.sau41.org/resources/voter-information. | https://www.sau41.org/resources/voter-information (as of 2026-11-08) |
| 42 | Nashua | SAU 42 (Nashua School District) website: https://www.nashua.edu; contact page: https://www.nashua.edu/our-district/contact-us. | https://www.nashua.edu (as of 2026-11-08) |
| 43 | Newport | SAU 43 (Newport School District) website: https://www.sau43.nh.gov. Office: 86 N. Main Street, Newport, NH 03773, phone 603-865-9500. | https://www.sau43.nh.gov/ (as of 2026-11-08) |
| 44 | Northwood | SAU 44 (Northwood School District) website. Contact page: https://www.sau44.org/o/sau/page/high-school-registration-and-residency | https://www.sau44.org/ (as of 2026-11-08) |
| 45 | Moultonborough | SAU 45 (Moultonborough School District) website. Contact page: https://sau45.nh.gov/en-US | https://www.sau45.org/en-US (as of 2026-11-08) |
| 46 | Andover, Merrimack Valley | SAU 46 (Merrimack Valley and Andover school districts) website: https://www.mvsdpride.org/ ; SAU office 105 Community Drive, Penacook, NH 03303, phone 603.753.6561. Andover Elementary/Middle School: https://sites.google.com/a/aemseagles.org/andover-elementary-middle-school/home | https://sites.google.com/a/mvsdpride.org/district/school-administrative-unit-46 (as of 2026-11-08) |
| 47 | Jaffrey-Rindge Cooperative | SAU 47 (Jaffrey-Rindge Cooperative School District) website: https://www.sau47.org ; contacts: https://www.sau47.org/school_board/contacts (1 Conant Way, Jaffrey; 603-532-8122). | https://www.sau47.org/ (as of 2026-11-08) |
| 48 | Campton, Ellsworth, Holderness, Pemi-Baker Regional, Plymouth, Rumney, Thornton, Waterville Valley, Wentworth | SAU 48 (Plymouth area: Campton, Ellsworth, Holderness, Pemi-Baker Regional, Plymouth, Rumney, Thornton, Waterville Valley, Wentworth) website: https://sites.google.com/pemibaker.org/sau48 ; office 47 Old Ward Bridge Road, Plymouth, phone 603-536-1254. Each school has its own site (e.g. https://pes.pemibaker.org/) with that district's school board and budget pages. | https://sites.google.com/pemibaker.org/sau48 (as of 2026-11-08) |
| 49 | Governor Wentworth Regional | SAU 49 (Governor Wentworth Regional School District) website: https://gwrsd.sau49nh.gov (gwrsd.org redirects there). | https://gwrsd.sau49nh.gov/ (as of 2026-11-08) |
| 50 | Greenland, New Castle, Newington, Rye | SAU 50 (Greenland, New Castle, Newington, Rye) website. Contact page: https://www.sau50.org/en-US/pages/e5244bce-6033-4c90-b70a-69b51e4f94c0 | https://www.sau50.org/en-US (as of 2026-11-08) |
| 51 | Pittsfield | SAU 51 (Pittsfield School District) website: https://sau51.org; contacts page: https://sau51.org/contacts/. | https://sau51.org (as of 2026-11-08) |
| 52 | Portsmouth | SAU 52 (Portsmouth School Department) website. Contact page: https://www.cityofportsmouth.com/school/central-office-staff-directory | https://www.cityofportsmouth.com/school (as of 2026-11-08) |
| 53 | Allenstown, Chichester, Deerfield, Epsom, Pembroke | SAU 53 (Pembroke, Allenstown, Chichester, Deerfield, Epsom) website: https://sau.sau53.org/; office 267 Pembroke St, Pembroke, phone 603-485-5187, receptionist@sau53.org. Contact page: https://sau.sau53.org/en-US | https://sau.sau53.org/ (as of 2026-11-08) |
| 54 | Rochester | SAU 54 (Rochester School District) website: https://www.rochesterschools.com/ ; office 150 Wakefield Street, Rochester, phone (603) 332-3678. | https://www.rochesterschools.com/ (as of 2026-11-08) |
| 55 | Hampstead | SAU 55 (Hampstead School District) website. Contact page: https://www.hampsteadschools.net/page/new-student-registration | https://www.hampsteadschools.net/ (as of 2026-11-08) |
| 56 | Somersworth | SAU 56 (Somersworth School District) website: https://www.sau56.org/ ; contact page: https://www.sau56.org/contact_information ; office 51 West High Street, Somersworth, phone 603-692-4450. | https://www.sau56.org/ (as of 2026-11-08) |
| 57 | Salem | SAU 57 (Salem School District) website: https://sau57.org; contact page https://sau57.org/contact-us; district office 38 Geremonty Drive, Salem, phone 603-893-7040. | https://sau57.org (as of 2026-11-08) |
| 58 | Northumberland, Stark, Stratford | SAU 58 (Northumberland, Stark and Stratford school districts) website: https://www.sau58.org; contact page: https://www.sau58.org/page/contact-info; office at 15 Preble Street, Groveton, 603-636-1437. | https://www.sau58.org (as of 2026-11-08) |
| 59 | Winnisquam Regional | SAU 59 (Winnisquam Regional School District) website: https://www.wrsdsau59.org/ ; office 433 West Main St, Tilton, phone 603-286-4116. | https://www.wrsdsau59.org/en-US (as of 2026-11-08) |
| 60 | Fall Mountain Regional | SAU 60 (Fall Mountain Regional School District) website: https://www.sau60.org/; staff directory: https://www.sau60.org/staff. Office: 122 NH Route 12A Unit 5, PO Box 720, Langdon, NH 03602, 603-835-0006. | https://www.sau60.org/ (as of 2026-11-08) |
| 61 | Farmington | SAU 61 (Farmington School District) website: https://www.sau61.org; contact page: https://www.sau61.org/about-us/contact-us; office at 35 School Street, Farmington, 603-755-2627. | https://www.sau61.org (as of 2026-11-08) |
| 62 | Mascoma Valley Regional | SAU 62 (Mascoma Valley Regional School District) website: https://www.mascomaschools.org; staff list: https://www.mascomaschools.org/our-district/staff-list; office at 547 US Route 4, Enfield, (603) 632-5563. | https://www.mascomaschools.org (as of 2026-11-08) |
| 63 | Wilton-Lyndeborough Cooperative | SAU 63 (Wilton-Lyndeborough Cooperative School District) website: https://www.sau63.org. Office: 192 Forest Rd, Lyndeborough. | https://www.sau63.org/ (as of 2026-11-08) |
| 64 | Milton | SAU 64 (Milton School District) website: https://www.sau64.org (phone 603-652-0262). | https://www.sau64.org/ (as of 2026-11-08) |
| 65 | Kearsarge Regional | SAU 65 (Kearsarge Regional School District) website: https://www.kearsarge.org/ ; contact page: https://www.kearsarge.org/district/district/pages/contact-us ; office 114 Cougar Court, New London, phone (603) 526-2051. | https://www.kearsarge.org/ (as of 2026-11-08) |
| 66 | Hopkinton | SAU 66 (Hopkinton School District) website: https://www.hopkintonschools.org. Office: 204 Maple St, Contoocook, NH 03229, phone 603-746-5186. | https://www.hopkintonschools.org/en-US (as of 2026-11-08) |
| 67 | Bow, Dunbarton | SAU 67 (Bow and Dunbarton School Districts) website: https://sau67nh.gov (55 Falcon Way, Bow; 603-224-4728). | https://sau67nh.gov/en-US (as of 2026-11-08) |
| 68 | Lincoln-Woodstock Cooperative | SAU 68 (Lincoln-Woodstock Cooperative School District) website: https://www.lin-wood.org/; office 72 Linwood Drive, Lincoln, phone (603) 745-2214. | https://www.lin-wood.org/ (as of 2026-11-08) |
| 69 | Middleton | SAU 69 (Middleton School District) website: https://sites.google.com/a/sau69.org/sau-69---middleton-school-district/ (PO Box 190, Wolfeboro Falls; 603-569-1658). Middleton Elementary School: https://www.middletonelementary.org (603-473-5000). | https://sites.google.com/a/sau69.org/sau-69---middleton-school-district/ (as of 2026-11-08) |
| 70 | Dresden, Hanover | SAU 70 (Hanover, Dresden and Norwich school districts) website: https://www.sau70.org/; school board contacts: https://www.sau70.org/school-boards/school-board-contact-information. | https://www.sau70.org/ (as of 2026-11-08) |
| 71 | Lempster | SAU 71 (Lempster School District) website: https://www.sau71.org (29 School Road, Lempster; 603-863-1080); contact page: https://www.sau71.org/page/contact-us. | https://www.sau71.org/page/for-voters (as of 2026-11-08) |
| 72 | Alton | SAU 72 (Alton School District) is part of the Prospect Mountain SAU website: https://www.pmsau.nh.gov; Alton Central School: https://acs.pmsau.nh.gov/o/acs (41 School Street, Alton). | https://www.pmsau.nh.gov/ (as of 2026-11-08) |
| 73 | Gilford | SAU 73 (Gilford School District) website: https://sau73nh.gov/ ; office 2 Belknap Mountain Rd, Gilford, phone 603-527-9215, email gsd@sau73.org. | https://sau73nh.gov/en-US (as of 2026-11-08) |
| 74 | Barrington | SAU 74 (Barrington School District) website: https://www.sau74.org/ ; 572 Calef Highway, Barrington, NH 03825, phone 603-664-2715. | https://www.sau74.org/ (as of 2026-11-08) |
| 75 | Grantham | SAU 75 (Grantham School District) website: https://www.gvshawks.org (Grantham Village School, 75 Learning Drive, Grantham; 603-863-1681); contact page: https://www.gvshawks.org/apps/contact/. | https://www.gvshawks.org/ (as of 2026-11-08) |
| 76 | Lyme | SAU 76 (Lyme School District) website: https://www.lymeschool.org/ (SAU 76 district page https://www.lymeschool.org/page/sau-76-district-office); Lyme School, 35 Union Street, Lyme, phone (603) 795-2125. | https://www.lymeschool.org/ (as of 2026-11-08) |
| 77 | Monroe | SAU 77 (Monroe School District) website: https://sites.google.com/a/monroeschool77.com/monroe-consolidated-school/home ; phone 603-638-2800. | https://sites.google.com/a/monroeschool77.com/monroe-consolidated-school/new-student-registration (as of 2026-11-08) |
| 78 | Rivendell | SAU 78 (Rivendell Interstate School District) website: https://www.rivendellschool.org/ ; contact page https://www.rivendellschool.org/contact ; District Office, PO Box 271, 10 School Drive, Orford, NH 03777, phone 1-603-353-2170. | https://www.rivendellschool.org/voterinformation (as of 2026-11-08) |
| 79 | Gilmanton | SAU 79 (Gilmanton School District) website: https://www.sau79.org (a Google Site; on November 8, 2026 it redirected to a Google sign-in page). Gilmanton School: http://gilmantonschool.org (same). | http://web.archive.org/web/20260716202432/https://www.sau79.org/ (as of Wayback snapshot 2026-07-16) |
| 80 | Shaker Regional | SAU 80 (Shaker Regional School District) website: https://www.sau80.org/ ; contact page: https://www.sau80.org/cms/one.aspx?portalId=318877&pageId=1189323 ; office 58 School Street, Belmont, phone 603-267-9223. | https://www.sau80.org/ (as of 2026-11-08) |
| 81 | Hudson | SAU 81 (Hudson School District) website: https://www.sau81.org ; registration and school contacts: https://www.sau81.org/families/registration. | https://www.sau81.org/families/registration (as of 2026-11-08) |
| 82 | Chester | SAU 82 (Chester School District) website: https://www.sau82.org (also https://www.sau82nh.gov); Chester Academy: https://ca.sau82nh.gov. Office: 22 Murphy Drive, Chester, NH 03036, phone 603-887-3621. | https://www.sau82.org/ (as of 2026-11-08) |
| 83 | Fremont | SAU 83 (Fremont School District, Ellis School) website: https://www.sau83.org, with a contact page at https://www.sau83.org/page/contact/. Ellis School: 432 Main Street, Fremont, NH 03044; SAU office phone (603) 895-6903. | https://www.sau83.org/page/registration/ (as of 2026-11-08) |
| 84 | Littleton | SAU 84 (Littleton School District) website: https://www.sau84.org ; contact page: https://www.sau84.org/apps/contact/ (65 Maple Street, Littleton; 603-444-5215). | https://www.sau84.org/ (as of 2026-11-08) |
| 85 | Sunapee | SAU 85 (Sunapee School District) website: https://www.sau85.org/; office 70 Lower Main Street, Sunapee, phone 603-763-4627. | https://www.sau85.org/ (as of 2026-11-08) |
| 86 | Barnstead | Prospect Mountain SAU (SAU 86 Barnstead, SAU 72 Alton and SAU 301 Prospect Mountain JMA) website: https://www.pmsau.nh.gov (Central Administrative Office, 252 Suncook Valley Rd, Alton; 603-875-7890). Barnstead Elementary School: https://bes.pmsau.nh.gov/o/bes (603-269-5161). | https://www.pmsau.nh.gov/ (as of 2026-11-08) |
| 87 | Mascenic Regional | SAU 87 (Mascenic Regional School District) website: https://www.mascenic.org. | https://www.mascenic.org (as of 2026-11-08) |
| 88 | Lebanon | SAU 88 (Lebanon School District) website: https://www.sau88.net/; enrollment and contacts: https://www.sau88.net/families/enrollment. | https://www.sau88.net/ (as of 2026-11-08) |
| 89 | Mason | SAU 89 (Mason School District) website: https://www.sau89.nh.gov/; phone (603) 878-2962. | https://www.sau89.nh.gov/ (as of 2026-11-08) |
| 90 | Hampton | SAU 90 (Hampton School District) website. Contact page: https://www.sau90.org/page/superintendent | https://www.sau90.org/ (as of 2026-11-08) |
| 91 | Surry | SAU 91 (Surry School District) has a page on the Town of Surry website: https://surry.nh.gov/surry-school-district/ (contact: schoolboard@surry.nh.gov). | https://surry.nh.gov/surry-school-district/ (as of 2026-11-08) |
| 92 | Hinsdale | SAU 92 (Hinsdale School District) website. Contact page: https://www.hnhsd.org/?page_id=4363 | https://www.hnhsd.org/ (as of 2026-11-08) |
| 93 | Monadnock Regional | SAU 93 (Monadnock Regional School District) website: https://www.mrsd.org; staff directory: https://www.mrsd.org/parents-students/staff-directory/staff-directory; office at 600 Old Homestead Highway, Swanzey, (603) 352-6955. | https://www.mrsd.org (as of 2026-11-08) |
| 95 | Windham | SAU 95 (Windham School District) website: https://www.windhamsd.org/ ; contact page: http://windhamsd.ss18.sharpschool.com/our_district/superintendent_s_office/leadership ; office 19 Haverhill Rd, Windham, phone 603-845-1550. | https://www.windhamsd.org/ (as of 2026-11-08) |
| 99 | Croydon | SAU 99 (Croydon School District) website: https://croydonsd.org/ ; contact page: https://croydonsd.org/contact-us/ ; 889 NH-10, Croydon (mail PO Box 389, Newport), phone 603-863-2080. | https://croydonsd.org/ (as of 2026-11-08) |
| 100 | Cornish | SAU 100 (Cornish School District) website: https://www.cornishschool.org; contact page: https://www.cornishschool.org/apps/contact/. | https://www.cornishschool.org (as of 2026-11-08) |
| 101 | Wakefield | SAU 101 (Wakefield School District) website: https://www.sau101.org; Paul School page: https://www.sau101.org/o/ps; phone 603-871-8502 (as listed on the home page). | https://www.sau101.org (as of 2026-11-08) |
| 102 | Goshen | SAU 102 (Goshen School District) website: https://sites.google.com/goshenschooldistrictnh.org/district/home, as linked from the Town of Goshen School page; on November 8, 2026 it required a Google sign-in. | https://goshennh.org/school/ (as of 2026-11-08) |
| 103 | Hill | SAU 103 (Hill School District, Jennie D. Blake School) website. Contact page: https://sites.google.com/sau103.org/jdbs/about/directions | https://sites.google.com/sau103.org/jdbs/home (as of 2026-11-08) |
| 104 | Rollinsford | SAU 104 (Rollinsford School District) website: https://www.sau104.org/; SAU staff directory: https://www.sau104.org/district-info/sau-staff-directory. Office: 487 Locust Street, Rollinsford, NH 03869, 603-742-2351. | https://www.sau104.org/ (as of 2026-11-08) |
| 105 | Strafford | SAU 105 (Strafford School District) website: https://sites.google.com/strafford.k12.nh.us/straffordsau/strafford-school-district; Strafford School: https://www.strafford.k12.nh.us, office (603) 664-2842. | https://sites.google.com/strafford.k12.nh.us/straffordsau/strafford-school-district (as of 2026-11-08) |
| 106 | Timberlane Regional | SAU 106 (Timberlane Regional School District) website: https://www.timberlane.net; staff directory: https://www.timberlane.net/about/staff-directory; office at 30 Greenough Rd., Plaistow, (603) 382-6119. | https://www.timberlane.net (as of 2026-11-08) |
| 107 | Nottingham | SAU 107 (Nottingham School District) website: https://www.nottingham.k12.nh.us; contact page: https://www.nottingham.k12.nh.us/about/contact; Nottingham School, 245 Stage Road, Nottingham, 603-679-5632. | https://www.nottingham.k12.nh.us (as of 2026-11-08) |
| 108 | Pasquaney | SAU 108 (Pasquaney School District, Bridgewater-Hebron Village School) website. Contact page: https://www.sau108.org/page/contact-us | https://www.sau108.org/ (as of 2026-11-08) |
| 109 | Unity | SAU 109 (Unity School District) website: https://www.sau109.org; contact page: https://www.sau109.org/contact-us; Unity Elementary School, 864 2nd NH Turnpike, Unity, 603-542-5888. | https://www.sau109.org (as of 2026-11-08) |
| 110 | Lisbon Regional | Lisbon Regional School District (SAU 110 in the site's database) website: https://www.lisbon.k12.nh.us. Its student information system and finance portals are shared with SAU 35 (sau35.powerschool.com). | https://www.lisbon.k12.nh.us/sau-110.html (as of 2026-11-08) |
| 301 | Prospect Mountain JMA | SAU 301 (Prospect Mountain JMA) website: https://pmhs.pmsau.nh.gov/o/pmhs (www.pmhschool.com redirects there); SAU office site https://www.pmsau.nh.gov. | https://www.pmsau.nh.gov/ (as of 2026-11-08) |

## Not retrieved

Fields that were looked for on a district's site and not found (or not reached). What was checked for each is in `raw/districts/not-found-notes.csv`.

| District | id | Not found | Not checked |
|---|---|---|---|
| Allenstown | 9 | K day, K cutoff, K registration |  |
| Alton | 15 | K day, K cutoff, K registration |  |
| Amherst | 17 | K cutoff |  |
| Andover | 19 | K day, K registration, Preschool, Budget/vote |  |
| Ashland | 23 | K day, K registration, Preschool |  |
| Barrington | 33 | K day, K cutoff |  |
| Bartlett | 35 | K day |  |
| Bath | 39 | K day, K registration, Budget/vote, HS options |  |
| Bedford | 41 | K registration |  |
| Benton | 47 | Budget/vote, HS options |  |
| Berlin | 51 | K day, K registration, Preschool, Budget/vote |  |
| Bethlehem | 53 | K day, K registration |  |
| Bow | 57 | K day, K cutoff |  |
| Brentwood | 63 | K day, K registration |  |
| Brookline | 71 | K cutoff |  |
| Campton | 75 | K day, K cutoff, K registration |  |
| Candia | 79 | Preschool |  |
| Chatham | 91 | HS options |  |
| Chester | 93 | K cutoff, K registration |  |
| Chesterfield | 95 | K day, K registration, Preschool |  |
| Chichester | 99 | K day |  |
| Claremont | 101 | Preschool |  |
| Clarksville | 103 | Budget/vote, HS options |  |
| Colebrook | 105 | K day, K registration, Budget/vote |  |
| Columbia | 107 | Budget/vote, HS options |  |
| Contoocook Valley | 112 | K day, K registration |  |
| Conway | 113 | K day, K cutoff, Preschool |  |
| Coos County School District | 114 | Budget/vote, HS options |  |
| Deerfield | 127 | K day |  |
| Dover | 141 | K day |  |
| Dunbarton | 149 | K day, K cutoff, Preschool, Budget/vote |  |
| East Kingston | 153 | K day |  |
| Ellsworth | 162 | Budget/vote |  |
| Epping | 165 | K day |  |
| Epsom | 167 | K day, K registration |  |
| Errol | 171 | K day, K cutoff, K registration, Preschool |  |
| Exeter | 173 | K day, K registration |  |
| Exeter Region Cooperative | 172 | Preschool |  |
| Fall Mountain Regional | 174 | K day, K cutoff, K registration |  |
| Farmington | 175 | K day, K cutoff, K registration |  |
| Franklin | 185 | K day, Budget/vote |  |
| Freedom | 187 | K day, K cutoff, Budget/vote, HS options |  |
| Fremont | 189 | K cutoff, K registration |  |
| Gilford | 191 | K day, K cutoff, Preschool |  |
| Gilmanton | 195 | K day, K cutoff, K registration, Preschool, HS options |  |
| Gorham Randolph Shelburne Cooperative | 203 | K day, K cutoff, K registration, Preschool |  |
| Goshen | 204 | K cutoff, Budget/vote |  |
| Governor Wentworth Regional | 208 | K day |  |
| Grantham | 211 | K day |  |
| Greenland | 215 | K registration |  |
| Hale's Location (Carroll County) | 222 | K registration, Budget/vote, HS options |  |
| Hampton | 225 | K day, K registration |  |
| Hanover | 233 | K day, K cutoff, K registration, Preschool |  |
| Harrisville | 235 | K day, K registration, Preschool |  |
| Hart's Location | 236 | HS options |  |
| Haverhill Cooperative | 238 | K day, K registration, Budget/vote |  |
| Henniker | 245 | K day |  |
| Hill | 247 | K day, K cutoff, K registration |  |
| Hillsboro-Deering Cooperative | 251 | K day |  |
| Hinsdale | 255 | K day, K cutoff |  |
| Holderness | 257 | Preschool, Budget/vote |  |
| Hollis | 259 | K cutoff |  |
| Hopkinton | 263 | K day, K cutoff, K registration |  |
| Inter-Lakes Cooperative | 269 | K day, K registration |  |
| Jackson | 271 | K day, Preschool |  |
| Jaffrey-Rindge Cooperative | 274 | K day |  |
| Kearsarge Regional | 276 | K day |  |
| Keene | 279 | K registration |  |
| Kensington | 281 | K day |  |
| Laconia | 285 | K day, Budget/vote |  |
| Lafayette Regional | 288 | K day, K registration, Preschool, Budget/vote |  |
| Lebanon | 295 | K day |  |
| Lempster | 299 | K day, K registration |  |
| Lincoln-Woodstock Cooperative | 305 | K day, Preschool |  |
| Lisbon Regional | 306 | K day, K registration, Budget/vote |  |
| Litchfield | 315 | K day, K cutoff |  |
| Littleton | 317 | K day, Preschool |  |
| Lyme | 327 | K day, Preschool, Budget/vote |  |
| Madison | 333 | K day, K cutoff |  |
| Manchester | 335 | K day |  |
| Marlborough | 339 | K day, K cutoff, K registration |  |
| Marlow | 341 | K registration |  |
| Mascenic Regional | 342 | K day, K registration |  |
| Mascoma Valley Regional | 343 | K day |  |
| Merrimack | 351 | K day |  |
| Merrimack Valley | 352 | K day |  |
| Middleton | 353 | K day |  |
| Milan | 355 | K day, K cutoff, K registration, Preschool |  |
| Milford | 357 | K day |  |
| Milton | 359 | K day, K cutoff, K registration |  |
| Monadnock Regional | 363 | K day, K registration |  |
| Monroe | 365 | K day, Budget/vote |  |
| Mont Vernon | 367 | K cutoff, Preschool |  |
| Moultonborough | 369 | K registration |  |
| Nelson | 375 | K day, K registration, Preschool |  |
| New Castle | 381 | K day, K registration, Budget/vote |  |
| Newfields | 387 | K day, K registration |  |
| Newfound Area | 388 | K day, K registration |  |
| Newington | 391 | K day, K registration, Budget/vote |  |
| Newport | 401 | K day |  |
| North Hampton | 405 | K cutoff |  |
| Northumberland | 407 | K day, K cutoff, K registration, Preschool |  |
| Northwood | 411 | K day, K registration |  |
| Nottingham | 413 | K day |  |
| Oyster River Coop | 423 | K day |  |
| Pelham | 425 | K day |  |
| Pembroke | 427 | K day |  |
| Piermont | 435 | K day, Budget/vote, HS options |  |
| Pittsburg | 437 | K day, K registration, Budget/vote |  |
| Pittsfield | 439 | K day, K registration, Preschool |  |
| Plainfield | 441 | K day, Preschool, Budget/vote |  |
| Plymouth | 447 | K day, K cutoff |  |
| Raymond | 453 | K day |  |
| Rivendell | 457 | K day, K cutoff, K registration |  |
| Rochester | 461 | K day |  |
| Rollinsford | 463 | K day, Preschool |  |
| Rumney | 467 | K day, Preschool |  |
| Rye | 471 | K day |  |
| Salem | 473 | K day |  |
| Sanborn Regional | 476 | K day |  |
| Shaker Regional | 486 | K day |  |
| Somersworth | 491 | K day |  |
| South Hampton | 495 | K day, K registration, Preschool, HS options |  |
| Stark | 499 | K day, K cutoff, K registration, Preschool, HS options |  |
| Stewartstown | 501 | K day, K registration, Budget/vote, HS options |  |
| Stoddard | 503 | K day, Preschool |  |
| Strafford | 507 | K day, Budget/vote |  |
| Stratford | 509 | K day, K cutoff, K registration, HS options |  |
| Stratham | 511 | K day |  |
| Sullivan | 513 | Budget/vote, HS options |  |
| Sunapee | 515 | K day, K cutoff, K registration |  |
| Tamworth | 525 | K day, K cutoff |  |
| Thornton | 531 | K day, K cutoff, K registration, Preschool |  |
| Unity | 539 | K day, K cutoff, Budget/vote, HS options |  |
| Wakefield | 543 | K day, HS options |  |
| Warren | 549 | K day, K registration, Budget/vote |  |
| Washington | 551 | K day |  |
| Waterville Valley | 553 | K day, Preschool |  |
| Weare | 555 | K day |  |
| Wentworth | 559 | K day, Preschool |  |
| Westmoreland | 563 | K day, Preschool |  |
| White Mountains Regional | 568 | K day, K registration |  |
| Winchester | 573 | K day, K cutoff, K registration, HS options |  |
| Windham | 575 | K day |  |
| Winnisquam Regional | 582 | K day, Budget/vote |  |

**Sites and documents that could not be read (checked November 8, 2026):**
- Winchester School District: winchesterschool.org and sau94.com lead to a parked domain page; the Wayback Machine copy is the parked page too.
- Sullivan, Hale's Location (Carroll County), Coos County School District: no district website found (searches and guessed domains).
- Gilmanton (sau79.org, gilmantonschool.org) and Goshen (district Google Site): Google sign-in required. A July 2026 Wayback copy was used for Gilmanton, and the Town of Goshen page for Goshen.
- Simbli policy portals for Hanover (SAU 70) and the SAU 24 districts: CAPTCHA, not bypassed. Lebanon's policy on Diligent/HighBond did not render. Hinsdale's policies are on SharePoint.
- Lisbon Regional's kindergarten page is password protected. Fall Mountain's policy and school pages were empty even in a browser.
- Rye and Greenland: their 2025 warrants require a Google sign-in and no 2026 documents are posted. New Castle and Newington post only 2023 warrants. Wilton-Lyndeborough posts warrants only through 2025.
- NH DOE iPlatform "High School/Town Cross Reference", "District/Town Cross Reference" and "SAU List": "Internal Server Error" in Chrome (the enrollment reports on the same site worked).
- Scanned 2026 warrants whose dates could not be read: Fall Mountain, Stoddard, Mason, Nottingham and Cornish. The Pinkerton agreements posted by Auburn and Candia are also scans.
