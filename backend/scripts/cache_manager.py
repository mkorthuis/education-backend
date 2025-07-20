#!/usr/bin/env python3
"""
Cache Management Script for Education Backend

This script provides command-line tools for managing the Redis cache.
"""

import argparse
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.core.cache import cache_service

def main():
    parser = argparse.ArgumentParser(description='Cache Management Tool')
    parser.add_argument('action', choices=['stats', 'clear', 'clear-pattern', 'health'],
                       help='Action to perform')
    parser.add_argument('--pattern', type=str, help='Pattern for clear-pattern action')
    
    args = parser.parse_args()
    
    if args.action == 'stats':
        stats = cache_service.get_stats()
        print("Cache Statistics:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
    
    elif args.action == 'clear':
        deleted_count = cache_service.clear_all()
        print(f"Cleared {deleted_count} cache keys")
    
    elif args.action == 'clear-pattern':
        if not args.pattern:
            print("Error: --pattern is required for clear-pattern action")
            sys.exit(1)
        deleted_count = cache_service.clear_pattern(args.pattern)
        print(f"Cleared {deleted_count} cache keys matching pattern: {args.pattern}")
    
    elif args.action == 'health':
        stats = cache_service.get_stats()
        is_healthy = stats.get("enabled", False) and stats.get("connected", False)
        print(f"Cache Health: {'HEALTHY' if is_healthy else 'UNHEALTHY'}")
        print(f"  Enabled: {stats.get('enabled', False)}")
        print(f"  Connected: {stats.get('connected', False)}")
        if not is_healthy and stats.get('error'):
            print(f"  Error: {stats['error']}")

if __name__ == '__main__':
    main() 