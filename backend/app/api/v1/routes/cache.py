from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.core.cache import cache_service

router = APIRouter()

@router.get("/stats",
    summary="Get cache statistics",
    description="Retrieves cache statistics including connection status, memory usage, and key count",
    response_description="Cache statistics")
def get_cache_stats() -> Dict[str, Any]:
    """Get cache statistics"""
    return cache_service.get_stats()

@router.delete("/clear",
    summary="Clear all cache",
    description="Clears all cached data",
    response_description="Number of keys deleted")
def clear_all_cache() -> Dict[str, int]:
    """Clear all cache"""
    deleted_count = cache_service.clear_all()
    return {"deleted_keys": deleted_count}

@router.delete("/clear/{pattern}",
    summary="Clear cache by pattern",
    description="Clears cache keys matching the specified pattern",
    response_description="Number of keys deleted")
def clear_cache_pattern(pattern: str) -> Dict[str, int]:
    """Clear cache by pattern"""
    if not pattern:
        raise HTTPException(status_code=400, detail="Pattern is required")
    
    deleted_count = cache_service.clear_pattern(pattern)
    return {"deleted_keys": deleted_count}

@router.get("/health",
    summary="Cache health check",
    description="Check if cache is healthy and connected",
    response_description="Cache health status")
def cache_health_check() -> Dict[str, Any]:
    """Cache health check"""
    stats = cache_service.get_stats()
    is_healthy = stats.get("enabled", False) and stats.get("connected", False)
    
    return {
        "healthy": is_healthy,
        "enabled": stats.get("enabled", False),
        "connected": stats.get("connected", False),
        "error": stats.get("error") if not is_healthy else None
    } 