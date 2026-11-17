# Hampton Research Brief

Read `/Users/michaelkorthuis/workspace/education/town/research-brief-template.md` first. It holds the goal, rules, format, safety rules and output layout. This file fills in its blanks for Hampton and lists what is already researched. Use the topics in `/Users/michaelkorthuis/workspace/education/town/shared-topics.md`. The questions are in `/Users/michaelkorthuis/workspace/education/town/Hampton/questions.md`: 20 profiles and 60 questions, shared by four agents.

Dates: `as_of` is the day you check a page, `review_by` is one year later for local facts, and 2027-08-15 for state law.

**Web search may be refused.** Start from the sites below and follow their links (WebFetch works when search doesn't). If a search is refused, don't keep retrying it; work from pages you can reach.

## What you need to know about Hampton

- **Hampton** is a seacoast town in Rockingham County, with Hampton Beach, North Beach and the Route 1 and Route 101 corridors; flooding and king tides affect some streets. Site town id 225. It has a Board of Selectmen and a town manager; the school districts are separate. Its library is the Lane Memorial Library.
- **Two school districts serve Hampton:**
  - **The Hampton School District** (site district id 225) is **SAU 90**, preschool to grade 8: Hampton Centre School (20770, preschool to grade 2, with the Centre School Community Preschool), Adeline C. Marston School (20795, grades 3–5) and Hampton Academy (20790, grades 6–8).
  - **The Winnacunnet Cooperative School District** (site district id 581) runs Winnacunnet High School (20780, grades 9–12) in Hampton for Hampton, Hampton Falls, North Hampton and Seabrook (members) and South Hampton (tuition), in **SAU 21**, which also serves those towns' K–8 districts.
- **Career and technical education:** Winnacunnet students attend the Seacoast School of Technology at Exeter High School (the library's career center list names Winnacunnet as a sending school).
- **Both districts vote by official ballot (SB2)**; the library has their 2026 dates.
- **Starting pages:** SAU 90, https://www.sau90.org (Hampton's schools, board, budget, policies); Winnacunnet and SAU 21, https://www.sau21.org and https://whs.sau21.org; the town, https://www.hamptonnh.gov (selectmen, tax rate, revaluation, elections and warrants, recreation).
- **Site figures that frame the questions:**
  - Resident public school students (the site's town enrollment): 1,677 in 2014-15, 1,556 in 2019-20, 1,362 in 2025-26.
  - Winnacunnet High's enrollment: 1,083 in 2015-16, 1,052 in 2019-20, 970 in 2024-25.
  - Cost per pupil, FY2025: Hampton $28,051; Winnacunnet $28,650; state $22,699; North Hampton $34,105; Hampton Falls $35,941; Seabrook $30,121; Rye $32,559.
  - Tax rates per $1,000 (NH DRA, 2025): total $12.61, local school $6.13 (Hampton's and its Winnacunnet share together), municipal $4.71.
  - Question 2 (November 2026): Hampton voted 5,154 to 3,325, 60.8% yes (the site's data; check what that means for SAU 90 and for Winnacunnet, a cooperative).
  - The site also has every school's enrollment by grade, test scores, class sizes, staff and salary schedules, free and reduced-price meals, English learners, safety counts, graduation and plans, licensed child care, EFAs by town, Census estimates, adequacy aid, special education aid, tax rates and school taxes (with the cooperative share). Point to these; don't restate them.
- **Saved pages:** `additional-data/raw/districts/*/hampton-*` (Centre School and its preschool, Marston, policy JEB, the 2026 warrant) and `winnacunnet-home`.
- **Library facts already loaded** (don't repeat them): Hampton's kindergarten cutoff, the Centre School Community Preschool, both districts' SB2 dates, and Winnacunnet's member towns (`high-school-tuition-options` 36). Read them: `grep -n -B2 -A10 -E "place: district (Hampton|Winnacunnet Cooperative)$" /Users/michaelkorthuis/workspace/education/additional-data/district-practices.md`.

## Several questions contain premises: check them

Report each in your "Premises checked" table.
- **Money:** voting on two school budgets and the split of the tax bill between them (P2.1); "a $32 million budget" with HVAC and auditorium seat articles (P2.2); "$350,000 maintenance work at Centre School and Batchelder Pond" (P6.1); a petition requiring the tax impact on a $600,000 home next to SAU 90 articles (P10.2); "Hampton's 47% share of the Winnacunnet budget" (P14.2); coastal revaluations raising assessments and a senior exemption (P10.1); paying for buses and services for Sacred Heart students (P6.3; RSA 189:9 and special education child-find duties); non-union support staff raises (P19.1); the Hawley Library redesign "on the ballot" (P9.3; find what Hawley is).
- **Schools and programs:** Centre School PreK full- or half-day (P1.1); a 3:00 pickup (P1.3); bell times and early releases across four buildings (P12.3); SROs in all four buildings (P12.1); buses rerouted for coastal flooding and king tides (P3.3, P20.3); Winnacunnet culinary or hospitality programs (P4.2); SST access for welding and trades (P7.1); sports fees and tryouts (P7.3); counselors stretched thin (P9.2); Marston always hiring behavioral techs and paras (P15.1).

## Already researched, or being researched now

- **Being researched at the same time** (November 16, 2026): **Exeter** and **Milford**. Exeter's agents own the **Seacoast School of Technology** (its programs, credentials, schedule, adult classes and admission); write only Winnacunnet's side of SST (how Winnacunnet students apply, transportation, credit and how many attend). Don't write facts about Exeter or Milford.
- **Portsmouth** (`town/Portsmouth/`, finished): Portsmouth High's CTE center, Little Harbour and the Seacoast comparisons; cite it for P5.2 and P14.1 comparisons rather than gathering Portsmouth facts again. **Dover** (`town/Dover/`) covers Dover's career center and Seacoast private and charter schools (`choices-and-adult-learning.md`, `town-school-options-nearby`).
- **State rules already written:** the library and earlier towns cover EFAs and school funding, home education access, special education (including out-of-state IEPs and transfers, `special-education-placements-across-states` and the 30-day comparable services rule), 504 plans, English learner services and translation, free and reduced-price meals, services owed to private school students (RSA 189:9, child find), bullying (the library's new `students-hb-131-bullying-law` and the three rule topics), phones, default budgets, tax caps (`budget-hb-1300-school-tax-cap`, `local-tax-and-budget-caps`), property tax bills (`property-tax-bills-and-escrow`) and CTE admission (`cte-admission-and-cost-rules`). Read Manchester's `student-support.md`, Nashua's `special-education.md`, Concord's `families-and-support.md`, Dover's `money-buildings-and-governance.md` and Portsmouth's `student-support.md`; cite what's there by file, topic and fact number, and don't write those rules again. Where they and the library lack a state rule you need, write it with no place.

## Where facts go

- `district Hampton` for SAU 90, its three schools, the preschool, programs, policies, staff, budget and board.
- `district Winnacunnet Cooperative` for Winnacunnet High, its budget, board, programs and its side of SST; `sau 21` for facts that apply to every SAU 21 district.
- **Agent 2 writes the shared folder `town/winnacunnet/`** (its file and `raw/` there), so North Hampton, Hampton Falls and Seabrook research can use it later. Agent 4 writes Winnacunnet's budget and tax facts in its own Hampton file, with `place: district Winnacunnet Cooperative`. Two agents never write the same file.
- `town Hampton` for town government and services: selectmen, the town's tax rate, revaluation and exemptions, police and SROs, flooding, recreation and community use of buildings, the library.
- Private schools (Sacred Heart School): `town Hampton` with the school named. No place for general NH rules.

All agents write in `town/Hampton/` except agent 2 (`town/winnacunnet/`). Shared slugs may repeat across files; within one file each slug appears once.

- **Raw copies:** under your own area folder (named in your prompt). Keep each area under about 100 MB, and save only files your facts cite.
- **Scripts:** in your own scratchpad subfolder.
- **Overlap:** budgets, taxes, warrants, buildings and staff pay for both districts belong to agent 4; Winnacunnet's programs to agent 2; transportation and bell times for the K–8 schools to agent 1. Put what you find for another area in your "For another file" section rather than writing it twice.
- **Blocked pages:** if a page refuses automated requests (HTTP 403, a bot check), list its URL under "Not retrieved" and move on. Don't retry it or route around it through mirrors or archives; the main session opens those in a browser.

## Agent split

| Agent | Area | Output file | Raw folder | Questions |
|---|---|---|---|---|
| 1 | Hampton's K–8 schools and daily life: the Centre School preschool, kindergarten classes and aides, after-school care, advanced math and reading at Marston, Hampton Academy clubs and supports, buses from the beach and in floods, Hampton Academy's Chromebooks and basics, attendance and family travel, the move to Hampton Academy, bell times and early releases, enrolling mid-year, pickup lines, late buses, room for new families | `k8-schools-and-daily-life.md` | `town/Hampton/raw/k8/` | P1.1, P1.2, P1.3, P3.1, P3.2, P3.3, P6.2, P11.1, P11.2, P12.3, P14.3, P17.1, P17.3, P20.1, P20.3 |
| 2 | Winnacunnet High School (shared folder): culinary and hospitality, SST access, translation for families, sports fees and tryouts, the move from Hampton Academy or a private school, AP and dual enrollment, counselors, the library and the Hawley redesign, financial literacy, mental health counselors, band and theater, honors science and math, labs and technology, phones, paths besides four-year college | `town/winnacunnet/winnacunnet-high-school.md` | `town/winnacunnet/raw/high/` | P4.2, P7.1, P7.2, P7.3, P8.2, P9.1, P9.2, P9.3, P13.1, P13.2, P17.2, P18.1, P18.2, P18.3, P19.2 |
| 3 | Special education, student support, safety, private schools and community: out-of-state IEPs, services for Sacred Heart students, bullying programs, SROs and security, lockdowns and storm plans, staffing for 504 plans and the main contact on a hard morning, summer reading help, discreet free meals, community use of buildings, how the two districts fit together, comparisons with North Hampton and Portsmouth, reputation, getting involved | `student-support-and-community.md` | `town/Hampton/raw/support/` | P4.3, P5.1, P5.2, P5.3, P6.3, P8.1, P11.3, P12.1, P12.2, P14.1, P15.1, P15.2, P15.3, P19.3, P20.2 |
| 4 | Money, taxes, governance and buildings (both districts): two ballots and the tax split, warrant articles for HVAC and seats, budget growth, rent and school taxes, the Centre School and Batchelder Pond work, the SAU 90 ballot, senior exemptions and revaluation, the $600,000 home petition, the default budget, young voters' turnout, Hampton's share of Winnacunnet, year-round taxes for seasonal residents, reading warrants from away, value per pupil against Seabrook and Hampton Falls, support staff raises | `money-and-governance.md` | `town/Hampton/raw/money/` | P2.1, P2.2, P2.3, P4.1, P6.1, P8.3, P10.1, P10.2, P10.3, P13.3, P14.2, P16.1, P16.2, P16.3, P19.1 |
