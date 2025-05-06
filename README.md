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

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
ADMIN_EMAIL=admin@example.com

# Optional: AI Integration
DEFAULT_LLM_PROVIDER=gemini  # Options: claude, openai, gemini
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