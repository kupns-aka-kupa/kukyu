from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)