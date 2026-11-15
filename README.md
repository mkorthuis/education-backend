# NH Facts AI

A reporting and analytics portal for New Hampshire K-12 schools. This application transforms data collected by the New Hampshire Department of Education (NH DOE) into accessible, insightful visualizations and reports for parents, educators, and taxpayers.

## Overview

The platform makes valuable educational data transparent and actionable, allowing stakeholders to:
- Access school performance metrics and trends
- Compare data across different NH schools and districts
- Understand resource allocation and educational outcomes
- Make informed decisions based on comprehensive NH educational data

This repository contains the backend portion of the application.

Inspired by: https://fastapi.tiangolo.com/project-generation/

## Features

The backend provides API endpoints for a variety of NH educational data categories:

- **Assessment** - Standardized test results and academic performance metrics
- **Class Size** - Student-to-teacher ratios and classroom statistics
- **Education Freedom Account** - Data on NH's school choice program
- **Enrollment** - Student population data and trends
- **Finance** - School funding, expenditures, and budget allocation
- **Location** - Geographic and district information
- **Measurement** - Various educational metrics and KPIs
- **Outcomes** - Graduate rates, college acceptance, and career readiness
- **Safety** - School safety data and incident reports
- **Staff** - Teacher and administrative staff statistics

## Technologies Used  
- FastAPI
- Python 3.13
- Conda (https://docs.anaconda.com/miniconda/)
- Postgres (brew install postgresql)
- Redis (for API caching)
- Claude (Anthropic API) for Ask a Question

## Development Setup

### Local Environment Setup

```bash
conda create -n "education-backend" python=3.13
conda activate education-backend
cd backend
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```
PROJECT_NAME=NH Facts AI
BACKEND_CORS_ORIGINS=["http://localhost:5174", "http://localhost:3000"]
FRONTEND_HOST=https://localhost:5174

# Database
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=education

# Cache Configuration (Optional)
CACHE_ENABLED=true
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=
REDIS_SSL=false

# Optional: Ask a Question (without a key, asking is off)
ANTHROPIC_API_KEY=your-anthropic-api-key
```

### Running the Application

#### With Local Python
```bash 
uvicorn app.main:app --reload --ssl-keyfile=./certs/key.pem --ssl-certfile=./certs/cert.pem
```

#### With Docker
```bash
docker-compose build
docker-compose up
# if you want to run with realtime file changes
docker-compose watch
```

### Refreshing Docker Environment
```bash
docker-compose down -v
docker-compose watch
```

### Cache Management

The application includes a Redis-based caching system for improved API performance. Cache management tools are available:

```bash
# Check cache statistics
python scripts/cache_manager.py stats

# Clear all cache
python scripts/cache_manager.py clear

# Test cache functionality
python scripts/test_cache.py
```

For detailed cache documentation, see [CACHE_README.md](backend/CACHE_README.md).

### SSL Certificate Management
If you need to create new certificates:
```bash
cd backend
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
fastapi dev app/main.py --ssl-keyfile=./certs/key.pem --ssl-certfile=./certs/cert.pem
```

### Database Management

#### Running Migrations 
```bash
PYTHONPATH=. alembic upgrade head # Don't know why there is a path issue.
```

#### Creating New Migrations 
```bash
PYTHONPATH=. alembic revision --autogenerate -m "migration_name"
```

#### Loading a New Year of Data
Data is loaded with the ETL command in `app/etl`, not by editing migrations. The data migrations call the same loaders, so a fresh database (`alembic upgrade head`) gets every configured year.

1. Add the new file under `app/alembic/assets/...` and raise `year_end` in the dataset's config in `app/alembic/config/` (measurement: add the workbook to the end of its `files` list).
2. Preview, then load (from `backend/`):
```bash
PYTHONPATH=. python -m app.etl load assessment --year 2026 --dry-run
PYTHONPATH=. python -m app.etl load assessment --year 2026
```
3. Read the warnings: rows for schools, districts or towns that aren't in the database are skipped and listed.
4. On Heroku, run it in a one-off dyno (`heroku run`), then restart the web dynos to clear the API cache.

Datasets: `location`, `enrollment`, `town-enrollment`, `measurement`, `measurement-state-target`, `class-size`, `assessment`, `finance`, `cost-per-pupil`, `state-expenditure`, `state-class-size`, `education-freedom-account`, `safety`, `staff`, `teacher-education`, `teacher-salary`, `teacher-salary-band`, `early-exit`, `post-graduation`, `graduation-cohort`, `reduced-lunch`, `english-learner`, `enrollment-type`, `naep`, `census-finance`, `child-care`, `acs`, `adequacy-aid`, `special-education-aid`, `reference`, `question-two`.

- Most datasets update existing rows and insert new ones, so loading a year twice changes nothing. `assessment` and `measurement` replace the year's rows instead (their keys contain NULLs), so reloaded rows get new ids.
- Dependent materialized views are refreshed. `safety` also rebuilds that year's state and district totals; `finance` recomputes the state revenue and expenditure totals.
- `location` loads the state's current school, district and SAU lists. Schools missing from a newer list are kept; SAU staff and grade/town links are replaced by the list. Load it before a year's other datasets so new schools exist. Districts and schools in the latest list (`year_end`) are marked `is_current`; the API's district and school lists return only those unless `include_former=true`. A school's type comes from the state's type code (`SCHOOL_TYPES` in `app/etl/location.py`), and a code it doesn't have stops the load. Operators that aren't on the district list get a `kind` from their schools' type: `charter` (a charter school's board) or `private`; the API's `kind` filters use it (`/location/school?kind=charter`). The list's open date is kept as `school.open_date` (when the school opened, or was renumbered or reorganized; blank for most long-standing schools). A school that opened after the latest school year a topic covers, and has no figures in it, lists that topic in the API's `not_yet_reported`, so its pages say its figures aren't out yet.
- `finance` reads about 2,600 workbooks, so parsed forms are cached in `backend/.etl_cache` (git-ignored). The cache key includes each file's contents, the parsing code and the config, so changes are picked up automatically; deleting the folder is always safe. Set `ETL_CACHE_DIR` to move it, or to an empty value to turn it off. A full `alembic upgrade head` takes about 4 minutes the first time and under a minute after that.
- `naep` comes from NCES's NAEP Data Service rather than a saved download. `python -m app.etl fetch naep` asks the Data Service for every year and student group in `naep_config.yaml` and saves the answers in `assets/naep/` (10 to 20 minutes); then load as usual. Student groups other than all students are fetched for New Hampshire and the national public average only (`group_jurisdictions`). For a new NAEP year, add it to the config's `years`, raise `year_end`, fetch and load.
- `census-finance` (U.S. Census Bureau school system revenue by state, FY2010 on) also comes from the source: `python -m app.etl fetch census-finance` downloads each year's school-system file and summary tables, adds the systems up by state, checks every state's federal, state and local totals against Census's Table 1, and saves the state figures in `assets/census-finance/`. For a new year, add it to `census_finance_config.yaml` with its file names, raise `year_end`, fetch and load.
- `child-care` (licensed child care programs from NH DHHS's Child Care Search) also comes from the source: `python -m app.etl fetch child-care` saves the search's provider list and its unfiltered results to `assets/child-care/child-care-<date>.json`, then each program's page, trimmed, to `child-care-<date>-pages.json.gz` (one every 2 seconds, about 40 minutes; an interrupted fetch picks up where it stopped when run again the same day). Add the date to `downloads` in `child_care_config.yaml`, then `load child-care`, which loads every listed download (it takes no `--year`): each program's latest details and page, and one capacity and vacancy snapshot per download. A program city that matches no town stops the load; add it to `town_aliases`.
- `acs` (Census American Community Survey 5-year estimates for towns, school districts and the state) comes from Census's summary files: `python -m app.etl fetch acs` reads each release in `acs_config.yaml` (64 national files per release, read four at a time: a few minutes for both releases) and saves New Hampshire's rows to `assets/acs/acs5-<year>.json.gz`; `load acs` loads every release (or `--year 2024`) and refreshes the `{level}_acs_*` views. To add a release, add it to `releases` with its file paths, fetch and load. To add a table, add it to `tables`, its lines to `acs_variables.csv`, fetch, and add a migration that recreates the views (`acs.view_statements`). The API reads the ACS lists (releases, values, measures) once per process, so restart the web dynos after a load.
- `adequacy-aid` (NH DOE's adequate education grant calculation for each town, FY2020 on, and each district's share) comes from two DOE workbooks a year in `assets/adequacy-aid/`: every town's calculation, and how split towns' grants divide among their districts. The DOE's site blocks scripted downloads, so save a new year's two workbooks through a browser, add a block for the year to `adequacy_aid_config.yaml` (the columns, the year's parameters from the DOE's explanation of the year, and its steps), and `load adequacy-aid`. The load checks each step's formula against every town's published figure, the towns against the DOE's state totals, and the split against each town's grant, and stops on a difference.
- `special-education-aid` (NH DOE's special education aid, catastrophic aid until 2017, FY2021 on: each district's costs for high-cost special education students by band and the aid paid) comes from the DOE's yearly CSV on its Other State Aid Programs page, in `assets/special-education-aid/`. The DOE's site blocks scripted downloads, so save a new year's CSV through a browser, add a block for the year to `special_education_aid_config.yaml` (its file, the threshold, the appropriation, and any rows or totals the DOE's file gets wrong) and `load special-education-aid`. The load checks each district's entitlement against the year's bands, its total against its bands, its aid against the proration and the districts against the DOE's state row, and stops on a difference. A change in the formula (HB 1563's new band from FY2029) is a new entry under `formulas`; a file with a new column needs it mapped in `special_education_aid.HEADINGS`.
- `reference` is the reference library the Ask answers rule, term, research, program and district-practice questions from: the Markdown files in `assets/reference/` (copied from `additional-data/`), one `## slug: Title` topic per section and a numbered list of facts, each with one `source` link, an `as_of` and a `review_by` date. The load checks every fact and stops on a missing field, a source that isn't a single web address, or a place that doesn't match a district or town. To change a fact, edit the file, load, and restart the web dynos (the Ask reads the topic list once per process). The Ask leaves out facts past their `review_by` date; `GET /api/v1/reference/review` lists those past due and those due soon.
- `assessment`: save the file as `assets/assessments/assessments-YYYY.csv`. District and state rows are generated from school rows only for 2009–2017, whose files have school rows only.

### Dependency Management

Updating requirements.txt:
```bash
pip freeze > requirements.txt
```

### Debug Configuration with VSCode
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Attach (remote debug)",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "127.0.0.1",
                "port": 5678
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/backend",
                    "remoteRoot": "/app"
                }
            ]
        },
    ]
}
```

## API Documentation

The API documentation is automatically generated using FastAPI's Swagger UI:

- **Development**: https://localhost:8000/docs
- **Production**: https://your-deployed-domain.com/docs

## Project Structure

```
backend/
├── app/
│   ├── api/            # API endpoints
│   │   └── v1/         # API version 1
│   │       └── routes/ # Route handlers for different data categories
│   ├── core/           # Core functionality
│   ├── model/          # Database models
│   ├── schema/         # Pydantic schemas
│   ├── service/        # Business logic
│   ├── tests/          # Unit and integration tests
│   └── main.py         # Application entry point
├── alembic/            # Database migrations
└── scripts/            # Utility scripts
```

## Production Deployment

For production deployment instructions, see [Deployment.md](Deployment.md)

## Key Python Libraries 
- **psycopg** - Connect to Postgres  
- **pydantic-settings** - Load settings from .env file
- **bcrypt** - Hash passwords
- **passlib** - Password validation
- **pyjwt** - Create JWTs
- **sqlmodel** - ORM for Postgres
- **fastapi[standard]** - Web Framework
- **alembic** - Database migrations
- **pip** - should switch to uv at some point.

## License

MIT License

Copyright (c) 2024 NH Facts AI Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.