# API Cache System

This document describes the Redis-based caching system implemented for the Education Backend API.

## Overview

The cache system provides automatic caching for API responses with the following features:

- **No expiration by default**: Cache entries persist until explicitly cleared
- **Configurable TTL**: Optional time-to-live for specific endpoints
- **Pattern-based invalidation**: Clear cache entries matching specific patterns
- **Health monitoring**: Check cache connection and statistics
- **Graceful degradation**: API continues working even if Redis is unavailable

## Configuration

### Environment Variables

Add these to your `.env` file:

```bash
# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=
REDIS_SSL=false

# Cache Configuration
CACHE_ENABLED=true
CACHE_DEFAULT_TTL=3600
CACHE_KEY_PREFIX=education_api:
```

### Docker Setup

The Dockerfiles have been updated to include Redis installation and startup. Redis runs as a daemon alongside the application.

## Usage

### Caching Endpoints

Endpoints are automatically cached using the `@cache_response` decorator:

```python
from app.core.cache import cache_response

@router.get("/data")
@cache_response("data_endpoint")
async def get_data(session: SessionDep, year: Optional[int] = None):
    return service.get_data(session=session, year=year)
```

### Cache Management API

The following endpoints are available for cache management:

- `GET /api/v1/cache/stats` - Get cache statistics
- `DELETE /api/v1/cache/clear` - Clear all cache
- `DELETE /api/v1/cache/clear/{pattern}` - Clear cache by pattern
- `GET /api/v1/cache/health` - Check cache health

### Command Line Tools

Use the cache management script:

```bash
# Check cache statistics
python scripts/cache_manager.py stats

# Clear all cache
python scripts/cache_manager.py clear

# Clear cache by pattern
python scripts/cache_manager.py clear-pattern "education_api:assessment*"

# Check cache health
python scripts/cache_manager.py health
```

## Cache Key Generation

Cache keys are automatically generated based on:
- Function name/prefix
- All function arguments (positional and keyword)
- None values are excluded from key generation
- Keys are hashed using MD5 for consistent length

Example key: `education_api:assessment_state:abc123def456`

## Updated Endpoints

The following endpoints now include caching:

### Assessment Endpoints
- `GET /api/v1/assessment/subgroup`
- `GET /api/v1/assessment/subject`
- `GET /api/v1/assessment/state`
- `GET /api/v1/assessment/district`
- `GET /api/v1/assessment/school`

### Class Size Endpoints
- `GET /api/v1/class-size/school`
- `GET /api/v1/class-size/district`
- `GET /api/v1/class-size/state`

### Education Freedom Account Endpoints
- `GET /api/v1/education-freedom-account/entry-type`
- `GET /api/v1/education-freedom-account/entry`
- `GET /api/v1/education-freedom-account/state-entry`

## Cache Patterns

Common cache patterns for invalidation:

- `education_api:assessment*` - All assessment data
- `education_api:class_size*` - All class size data
- `education_api:efa*` - All education freedom account data
- `education_api:*` - All cached data

## Monitoring

### Cache Statistics

The cache provides detailed statistics including:
- Connection status
- Total cached keys
- Memory usage
- Uptime

### Health Checks

Use the health endpoint to monitor cache status:
```bash
curl http://localhost:8000/api/v1/cache/health
```

## Troubleshooting

### Cache Not Working

1. Check if Redis is running:
   ```bash
   redis-cli ping
   ```

2. Verify cache configuration:
   ```bash
   python scripts/cache_manager.py health
   ```

3. Check application logs for cache connection errors

### Performance Issues

1. Monitor cache hit rates via statistics
2. Consider adjusting TTL for frequently changing data
3. Use pattern-based invalidation for related data updates

### Memory Usage

1. Monitor Redis memory usage via statistics
2. Clear old cache entries if needed
3. Consider implementing cache size limits

## Development

### Adding Cache to New Endpoints

1. Import the cache decorator:
   ```python
   from app.core.cache import cache_response
   ```

2. Add the decorator to your endpoint:
   ```python
   @cache_response("your_endpoint_prefix")
   async def your_endpoint():
       # Your endpoint logic
   ```

3. Consider adding cache invalidation for data updates:
   ```python
   from app.core.cache import invalidate_cache_pattern
   
   @invalidate_cache_pattern("education_api:your_pattern*")
   async def update_data():
       # Update logic
   ```

### Testing Cache

1. Make a request to a cached endpoint
2. Check cache statistics to verify caching
3. Make the same request again and verify cache hit
4. Clear cache and verify cache miss

## Production Considerations

1. **Redis Persistence**: Configure Redis persistence for production
2. **Memory Limits**: Set appropriate memory limits for Redis
3. **Monitoring**: Implement cache monitoring and alerting
4. **Backup**: Regular Redis data backups
5. **Security**: Secure Redis access in production environments 