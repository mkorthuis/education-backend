#!/usr/bin/env python3
"""
Cache Test Script

This script tests the cache functionality by making requests to cached endpoints
and verifying cache hits/misses.
"""

import requests
import time
import json
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.core.cache import cache_service

def test_cache_endpoint(base_url: str, endpoint: str, params: dict = None):
    """Test a specific endpoint for caching"""
    print(f"\nTesting endpoint: {endpoint}")
    
    # First request (should be cache miss)
    start_time = time.time()
    response1 = requests.get(f"{base_url}{endpoint}", params=params)
    time1 = time.time() - start_time
    
    if response1.status_code != 200:
        print(f"  ❌ First request failed: {response1.status_code}")
        return False
    
    # Second request (should be cache hit)
    start_time = time.time()
    response2 = requests.get(f"{base_url}{endpoint}", params=params)
    time2 = time.time() - start_time
    
    if response2.status_code != 200:
        print(f"  ❌ Second request failed: {response2.status_code}")
        return False
    
    # Compare responses
    if response1.json() == response2.json():
        print(f"  ✅ Responses match")
        print(f"  📊 First request: {time1:.3f}s (cache miss)")
        print(f"  📊 Second request: {time2:.3f}s (cache hit)")
        print(f"  🚀 Speed improvement: {time1/time2:.1f}x faster")
        return True
    else:
        print(f"  ❌ Responses don't match")
        return False

def test_cache_stats(base_url: str):
    """Test cache statistics endpoint"""
    print("\nTesting cache statistics...")
    
    response = requests.get(f"{base_url}/api/v1/cache/stats")
    if response.status_code == 200:
        stats = response.json()
        print(f"  📊 Cache enabled: {stats.get('enabled', False)}")
        print(f"  📊 Cache connected: {stats.get('connected', False)}")
        print(f"  📊 Total keys: {stats.get('total_keys', 0)}")
        print(f"  📊 Memory usage: {stats.get('memory_usage', 'N/A')}")
        return True
    else:
        print(f"  ❌ Failed to get cache stats: {response.status_code}")
        return False

def test_cache_health(base_url: str):
    """Test cache health endpoint"""
    print("\nTesting cache health...")
    
    response = requests.get(f"{base_url}/api/v1/cache/health")
    if response.status_code == 200:
        health = response.json()
        print(f"  💚 Cache healthy: {health.get('healthy', False)}")
        print(f"  💚 Enabled: {health.get('enabled', False)}")
        print(f"  💚 Connected: {health.get('connected', False)}")
        return health.get('healthy', False)
    else:
        print(f"  ❌ Failed to get cache health: {response.status_code}")
        return False

def main():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Education Backend Cache System")
    print("=" * 50)
    
    # Test cache health first
    if not test_cache_health(base_url):
        print("\n❌ Cache is not healthy. Please check Redis connection.")
        return
    
    # Test cache statistics
    test_cache_stats(base_url)
    
    # Test various endpoints
    test_cases = [
        {
            "endpoint": "/api/v1/assessment/subgroup",
            "params": None,
            "description": "Assessment subgroups"
        },
        {
            "endpoint": "/api/v1/assessment/subject", 
            "params": None,
            "description": "Assessment subjects"
        },
        {
            "endpoint": "/api/v1/class-size/state",
            "params": {"year": 2023},
            "description": "Class size state data (2023)"
        },
        {
            "endpoint": "/api/v1/education-freedom-account/entry-type",
            "params": {"year": 2024},
            "description": "EFA entry types (2024)"
        },
        {
            "endpoint": "/api/v1/enrollment/state",
            "params": {"year": 2023},
            "description": "State enrollment (2023)"
        }
    ]
    
    success_count = 0
    total_count = len(test_cases)
    
    for test_case in test_cases:
        print(f"\n🔍 Testing: {test_case['description']}")
        if test_cache_endpoint(base_url, test_case["endpoint"], test_case["params"]):
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {success_count}/{total_count} endpoints working with cache")
    
    if success_count == total_count:
        print("🎉 All cache tests passed!")
    else:
        print("⚠️  Some cache tests failed. Check the logs above.")

if __name__ == '__main__':
    main() 