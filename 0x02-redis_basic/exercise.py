#!/usr/bin/env python3
""" Writing strings to Redis """
import uuid
import redis
from typing import Union


class Cache:
    """ Cache class """
    def __init__(self) -> None:
        """
        method, store an instance of the Redis client as a private
        variable named _redis and flush the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method that takes a data argument and returns a string.
        The method generate a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
