from collections import Counter


def factorization(n):
    k = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            k.append(i)
        i += 1
    if n > 1:
        k.append(n)
    return Counter(k)


def primeFactors(n):
    c = factorization(n)
    return "".join(f"({str(i)}**{str(c[i])})" if c[i] > 1 else f"({str(i)})" for i in c)
