# NH Facts - Heroku Deployment Guide

## 1. Initial Setup
```bash
# Install Heroku CLI if not already installed
brew install heroku/brew/heroku

# Login to Heroku
heroku login

# Create new Heroku app
heroku create education-backend --team nh-facts

# Set stack to container
heroku stack:set container
```

## 2. Database Setup
```bash
# Create PostgreSQL addon
heroku addons:create heroku-postgresql:essential-1

# Wait for database to be ready
heroku pg:wait

# Verify database provisioning
heroku pg:info
```

## 3. Environment Configuration
```bash
# Project settings
heroku config:set PROJECT_NAME="NH Facts"
heroku config:set STACK_NAME=nh-facts-ai
heroku config:set FRONTEND_HOST=https://nh-facts.michaelkorthuis.com
heroku config:set BACKEND_CORS_ORIGINS="http://localhost,http://localhost:5174,https://localhost,https://localhost:5174,https://nh-facts.michaelkorthuis.com,https://www.nh-facts.com"

# Get DATABASE_URL parts and set database configuration
db_host=$(heroku config:get DATABASE_URL | sed 's/.*@\([^:]*\).*/\1/')
db_port=$(heroku config:get DATABASE_URL | sed 's/.*:\([0-9]*\)\/.*/\1/')
db_name=$(heroku config:get DATABASE_URL | sed 's/.*\/\(.*\)/\1/')
db_user=$(heroku config:get DATABASE_URL | sed 's/.*:\/\/\([^:]*\):.*/\1/')
db_password=$(heroku config:get DATABASE_URL | sed 's/.*:\/\/[^:]*:\([^@]*\).*/\1/')

# Set database environment variables
heroku config:set POSTGRES_SERVER=$db_host
heroku config:set POSTGRES_PORT=$db_port
heroku config:set POSTGRES_DB=$db_name
heroku config:set POSTGRES_USER=$db_user
heroku config:set POSTGRES_PASSWORD=$db_password

# Additional settings
heroku config:set DOCKER_IMAGE_BACKEND=nh-facts-backend
heroku config:set PYTHONPATH=/app
heroku config:set PYTHONUNBUFFERED=1

heroku config:set WEB_CONCURRENCY=4 WORKER_CLASS=uvicorn.workers.UvicornWorker TIMEOUT=120

# Ask NH Education Facts: visitors' questions, answered by Claude. Without a key, asking is off and
# the site says so. Use a key made for production in the Anthropic Console; never commit it.
heroku config:set ANTHROPIC_API_KEY=<production key>
# Optional, to throttle: questions answered per day across the site (default: no limit); 0 turns
# asking off. `heroku config:unset ASK_DAILY_LIMIT` removes the limit again.
# heroku config:set ASK_DAILY_LIMIT=500


# Verify configuration
heroku config
```

## 4. Deployment
```bash
# Deploy to Heroku
git push heroku master  # or main depending on your branch name
```

## 5. Post-Deployment
```bash
# Check the application status
heroku ps

# View logs
heroku logs --tail
```

## 6. Monitoring and Management

### Check Application Status
```bash
# View process status
heroku ps

# Check logs
heroku logs --tail

# View application info
heroku apps:info
```

### Database Management
```bash
# Check database status
heroku pg:info

# Connect to database
heroku pg:psql

# Monitor database metrics
heroku pg:diagnose

#Connecting locally to the database
# Displays maintenance database,host, port, user, and password
heroku pg:credentials:url DATABASE -a education-backend

```

### Scaling
```bash
# Scale web dynos
heroku ps:scale web=1

# View current scale
heroku ps
```

## 7. Important Notes

1. **Process Management**:
   - The application runs using the start.sh script (Redis, then `scripts/start-heroku.sh`)
   - Uvicorn runs with 2 workers
   - The PORT is automatically set by Heroku
   - Migrations (`alembic upgrade head`) run in the release phase defined in `heroku.yml`: once per deploy, before the new web dynos start. If they fail, the deploy stops and the previous release keeps serving; see `heroku releases` and `heroku releases:output`.

2. **Database**:
   - Using Heroku Postgres essential-1 tier
   - Database credentials are automatically managed through DATABASE_URL
   - Connection parameters are parsed from DATABASE_URL
   - Automatic backups are included with essential-1 tier

3. **Monitoring**:
   - Use `heroku logs --tail` for real-time logs
   - Check `heroku ps` for process status
   - Monitor database with `heroku pg:info`

4. **Ask NH Education Facts** (`POST /api/v1/ask`):
   - Needs `ANTHROPIC_API_KEY`. There's no daily limit unless `ASK_DAILY_LIMIT` is set: it caps questions per day (midnight to midnight in New Hampshire) to throttle the site; repeats answered from the cache don't count. Questions are counted either way. `ASK_MODEL` and `ASK_EFFORT` default to `claude-haiku-5-5` at `high`.
   - The daily count and saved answers are in the dyno's own Redis, so each dyno counts separately and a dyno restart (Heroku restarts dynos daily) starts the count over.
   - A new answer can take more than Heroku's 30-second request limit, so it's streamed: spaces while Claude works, then the answer. Claude gets about 40 seconds an answer; the site stops waiting at 45.
   - Each answer logs its time and tokens: `heroku logs --tail | grep "Ask "`.

5. **Troubleshooting**:
   - Check logs for startup issues
   - Verify environment variables with `heroku config`
   - Check the release phase output for migration errors: `heroku releases:output`
   - Monitor process status for crashes

## 8. Useful Commands

### Quick Reference
```bash
# View logs
heroku logs --tail

# Check process status
heroku ps

# Restart application
heroku restart

# Check configuration
heroku config

# Connect to running dyno
heroku run bash

# Check database status
heroku pg:info

# View database credentials
heroku config:get DATABASE_URL

# Check database connection
heroku pg:psql
```