#!/usr/bin/env python3
""" Writing strings to Redis """
import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator that takes a single method Callable argument
    returns a Callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ function that increments the count for that key """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs
    for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        function that the decorator will return
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper

def replay(method: Callable) -> None:
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"
    inputs = [eval(i) for i in self._redis.lrange(inputs_key, 0, -1)]
    outputs = [eval(o) for o in self._redis.lrange(outputs_key, 0, -1)]

    B
    print('{} was called {} times:'.format(
        method.__qualname__, len(inputs_key)))
    for i, o in zip(inputs, outputs):
        B
        print(f"{method.__qualname__}({i}) -> {o}")


class Cache:
    """ Cache class """
    def __init__(self) -> None:
        """
        method, store an instance of the Redis client as a private
        variable named _redis and flush the instance
        B
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method that takes a data argument and returns a string.
        The method generate a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """
        method that take a key string argument and an optional Callable
        argumen named fn. The callable converts the data back to
        the desired format
        """
        data = self._redis.get(key)
        if data is not None and fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        automatically parametrize Cache.get with the correct conversion
        function
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        automatically parametrize Cache.get with the correct conversion
        function
        """
        return self.get(key, fn=int)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
