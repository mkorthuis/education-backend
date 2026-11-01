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
- AI Integration with multiple LLM providers (Claude, OpenAI, Gemini)

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

# Optional: AI Integration (summary endpoints)
GEMINI_API_KEY=your-gemini-api-key
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

Datasets: `location`, `enrollment`, `town-enrollment`, `measurement`, `measurement-state-target`, `class-size`, `assessment`, `finance`, `cost-per-pupil`, `state-expenditure`, `education-freedom-account`, `safety`, `staff`, `teacher-education`, `teacher-salary`, `teacher-salary-band`, `early-exit`, `post-graduation`, `graduation-cohort`.

- Most datasets update existing rows and insert new ones, so loading a year twice changes nothing. `assessment` and `measurement` replace the year's rows instead (their keys contain NULLs), so reloaded rows get new ids.
- Dependent materialized views are refreshed. `safety` also rebuilds that year's state and district totals; `finance` recomputes the state revenue and expenditure totals.
- `location` loads the state's current school, district and SAU lists. Schools missing from a newer list are kept; SAU staff and grade/town links are replaced by the list. Load it before a year's other datasets so new schools exist.
- `finance` reads about 2,600 workbooks, so parsed forms are cached in `backend/.etl_cache` (git-ignored). The cache key includes each file's contents, the parsing code and the config, so changes are picked up automatically; deleting the folder is always safe. Set `ETL_CACHE_DIR` to move it, or to an empty value to turn it off. A full `alembic upgrade head` takes about 4 minutes the first time and under a minute after that.
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