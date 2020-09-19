from functools import lru_cache


def count_Kprimes(k, start, end):
    return [i for i in range(start, end + 1) if kprime(i) == k]


def puzzle(s):
    a = count_Kprimes(1, 0, s)
    b = count_Kprimes(3, 0, s)
    c = count_Kprimes(7, 0, s)
    return sum(1 for x in a for y in b for z in c if x + y + z == s)


@lru_cache(None)
def kprime(n):
    k = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            k += 1
        i += 1
    if n > 1:
        k += 1
    return k
