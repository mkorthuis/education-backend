import json
import hashlib
import inspect
import logging
import types
from typing import Annotated, Any, Optional, Union, get_args, get_origin, get_type_hints
from functools import wraps
import redis
from fastapi import params
from pydantic import BaseModel
from pydantic.fields import FieldInfo
from sqlalchemy.orm import Session as OrmSession
from app.core.config import settings

logger = logging.getLogger(__name__)

# Argument types that go into the cache key
_KEYABLE_TYPES = (str, int, float, bool)

class CacheService:
    def __init__(self):
        self.redis_client = None
        self.enabled = settings.CACHE_ENABLED
        
        if self.enabled:
            try:
                self.redis_client = redis.Redis(
                    host=settings.REDIS_HOST,
                    port=settings.REDIS_PORT,
                    db=settings.REDIS_DB,
                    password=settings.REDIS_PASSWORD or None,
                    ssl=settings.REDIS_SSL,
                    ssl_cert_reqs=settings.REDIS_SSL_CERT_REQS,
                    ssl_ca_certs=settings.REDIS_SSL_CA_CERTS or None,
                    ssl_certfile=settings.REDIS_SSL_CERTFILE or None,
                    ssl_keyfile=settings.REDIS_SSL_KEYFILE or None,
                    ssl_check_hostname=settings.REDIS_SSL_CHECK_HOSTNAME,
                    decode_responses=True,
                    socket_connect_timeout=5,
                    socket_timeout=5,
                    retry_on_timeout=True,
                    health_check_interval=30
                )
                # Test connection
                self.redis_client.ping()
                logger.info("Redis cache connection established successfully")
            except Exception as e:
                logger.warning(f"Failed to connect to Redis cache: {e}")
                self.enabled = False
                self.redis_client = None
        else:
            logger.info("Cache is disabled")

    def _generate_cache_key(self, prefix: str, *args, **kwargs) -> str:
        """Generate a unique cache key based on function arguments.

        Only plain values (the parsed path and query parameters) are part of the key.
        Anything else, such as the database session, is skipped: its string form
        includes a memory address, which would make every key unique.
        """
        # Create a string representation of all arguments
        key_parts = [prefix]

        # Add positional arguments
        for arg in args:
            if isinstance(arg, _KEYABLE_TYPES):
                key_parts.append(str(arg))

        # Add keyword arguments (sorted for consistency)
        for key, value in sorted(kwargs.items()):
            if value is not None and isinstance(value, _KEYABLE_TYPES):  # Skip None values and non-plain values
                key_parts.append(f"{key}:{value}")
        
        # Create a hash of the key parts
        key_string = ":".join(key_parts)
        key_hash = hashlib.md5(key_string.encode()).hexdigest()
        
        return f"{settings.CACHE_KEY_PREFIX}{prefix}:{key_hash}"

    def _serialize_value(self, value: Any) -> str:
        """Serialize a value to JSON, properly handling Pydantic models"""
        if isinstance(value, list):
            # Handle lists of Pydantic models
            serialized_list = []
            for item in value:
                if isinstance(item, BaseModel):
                    serialized_list.append(item.model_dump())
                else:
                    serialized_list.append(item)
            return json.dumps(serialized_list)
        elif isinstance(value, BaseModel):
            # Handle single Pydantic model
            return json.dumps(value.model_dump())
        else:
            # Handle other types
            return json.dumps(value)

    def _deserialize_value(self, value: str, expected_type: Optional[type] = None) -> Any:
        """Deserialize a value from JSON"""
        try:
            data = json.loads(value)
            return data
        except Exception as e:
            logger.error(f"Error deserializing cached value: {e}")
            return None

    def get(self, key: str) -> Optional[Any]:
        """Get a value from cache"""
        if not self.enabled or not self.redis_client:
            return None
        
        try:
            value = self.redis_client.get(key)
            if value:
                return self._deserialize_value(value)
            return None
        except Exception as e:
            logger.error(f"Error getting from cache: {e}")
            return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Set a value in cache with optional TTL"""
        if not self.enabled or not self.redis_client:
            return False
        
        try:
            serialized_value = self._serialize_value(value)
            if ttl is not None:
                return self.redis_client.setex(key, ttl, serialized_value)
            else:
                # No expiration unless explicitly requested
                return self.redis_client.set(key, serialized_value)
        except Exception as e:
            logger.error(f"Error setting cache: {e}")
            return False

    def delete(self, key: str) -> bool:
        """Delete a key from cache"""
        if not self.enabled or not self.redis_client:
            return False
        
        try:
            return bool(self.redis_client.delete(key))
        except Exception as e:
            logger.error(f"Error deleting from cache: {e}")
            return False

    def clear_pattern(self, pattern: str) -> int:
        """Clear all keys matching a pattern"""
        if not self.enabled or not self.redis_client:
            return 0
        
        try:
            keys = self.redis_client.keys(pattern)
            if keys:
                return self.redis_client.delete(*keys)
            return 0
        except Exception as e:
            logger.error(f"Error clearing cache pattern: {e}")
            return 0

    def clear_all(self) -> int:
        """Clear all cache keys"""
        return self.clear_pattern(f"{settings.CACHE_KEY_PREFIX}*")

    def get_stats(self) -> dict:
        """Get cache statistics"""
        if not self.enabled or not self.redis_client:
            return {"enabled": False, "connected": False}
        
        try:
            info = self.redis_client.info()
            return {
                "enabled": True,
                "connected": True,
                "total_keys": info.get("db0", {}).get("keys", 0),
                "memory_usage": info.get("used_memory_human", "N/A"),
                "uptime": info.get("uptime_in_seconds", 0)
            }
        except Exception as e:
            logger.error(f"Error getting cache stats: {e}")
            return {"enabled": True, "connected": False, "error": str(e)}

# Global cache service instance
cache_service = CacheService()

def _assert_url_only_inputs(func) -> None:
    """
    Fail at import time if a cached endpoint takes input the cache key would miss.

    The key is built from plain-value arguments, so every other input must be a
    path or query parameter with a str/int/float/bool type. A session dependency
    is allowed because it doesn't change the response. Bodies, headers, cookies,
    the raw Request and other dependencies would be left out of the key, so two
    different requests could share a cached response.
    """
    hints = get_type_hints(func, include_extras=True)
    for name, param in inspect.signature(func).parameters.items():
        hint = hints.get(name, param.annotation)
        markers = [param.default]
        if get_origin(hint) is Annotated:
            hint, *extras = get_args(hint)
            markers.extend(extras)

        if isinstance(hint, type) and issubclass(hint, OrmSession):
            continue

        for marker in markers:
            if isinstance(marker, (params.Depends, FieldInfo)) and not isinstance(marker, (params.Query, params.Path)):
                raise TypeError(
                    f"@cache_response on {func.__qualname__}: parameter '{name}' is not a path or query "
                    f"parameter ({type(marker).__name__}), so it would be left out of the cache key"
                )

        value_types = [t for t in get_args(hint) if t is not type(None)] if get_origin(hint) in (Union, types.UnionType) else [hint]
        if not all(isinstance(t, type) and issubclass(t, _KEYABLE_TYPES) for t in value_types):
            raise TypeError(
                f"@cache_response on {func.__qualname__}: parameter '{name}' has type {hint!r}; "
                f"only str, int, float and bool are included in the cache key"
            )

def cache_response(prefix: str, ttl: Optional[int] = None):
    """
    Decorator to cache API responses

    Args:
        prefix: Cache key prefix for this endpoint
        ttl: Time to live in seconds (None = settings.CACHE_DEFAULT_TTL)
    """
    if ttl is None:
        ttl = settings.CACHE_DEFAULT_TTL

    def decorator(func):
        _assert_url_only_inputs(func)

        # Plain `def` endpoints get a plain wrapper, so FastAPI still runs them in its
        # threadpool; an async wrapper would put their blocking database calls on the event loop
        if inspect.iscoroutinefunction(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                cache_key = cache_service._generate_cache_key(prefix, *args, **kwargs)
                cached_result = cache_service.get(cache_key)
                if cached_result is not None:
                    logger.info(f"Cache hit for key: {cache_key}")
                    return cached_result

                result = await func(*args, **kwargs)
                cache_service.set(cache_key, result, ttl)
                logger.info(f"Cache miss for key: {cache_key}, cached result")
                return result
        else:
            @wraps(func)
            def wrapper(*args, **kwargs):
                cache_key = cache_service._generate_cache_key(prefix, *args, **kwargs)
                cached_result = cache_service.get(cache_key)
                if cached_result is not None:
                    logger.info(f"Cache hit for key: {cache_key}")
                    return cached_result

                result = func(*args, **kwargs)
                cache_service.set(cache_key, result, ttl)
                logger.info(f"Cache miss for key: {cache_key}, cached result")
                return result
        return wrapper
    return decorator

def invalidate_cache_pattern(pattern: str):
    """
    Decorator to invalidate cache after function execution
    
    Args:
        pattern: Cache key pattern to invalidate
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            deleted_count = cache_service.clear_pattern(pattern)
            logger.info(f"Invalidated {deleted_count} cache keys matching pattern: {pattern}")
            return result
        return wrapper
    return decorator 