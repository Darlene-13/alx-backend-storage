#!/usr/bin/env python3
"""
Cache module for Redis operations.

This module provides a Cache class for storing and retrieving data from Redis
using randomly generated keys.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for storing data in Redis with random keys.
    
    This class provides a simple interface for storing various types of data
    in Redis using UUID-generated keys for retrieval.
    """
    
    def __init__(self) -> None:
        """
        Initialize Cache instance with Redis client and flush database.
        
        Creates a Redis client connection and clears all existing data
        from the current database to start with a clean state.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key.
        
        Generates a random UUID key, stores the provided data in Redis
        using that key, and returns the key for later retrieval.
        
        Args:
            data: The data to store. Can be a string, bytes, integer, or float.
            
        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key