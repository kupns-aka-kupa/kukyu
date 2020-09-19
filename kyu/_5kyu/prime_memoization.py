primes = [2, 3, 5, 7]


def is_prime(n):
    if n in primes:
        return True
    elif n < 2:
        return False
    k = 0
    i = 2
    while i * i <= n:
        cond = i not in primes
        if cond:
            for p in primes:
                if i % p == 0:
                    cond = False
                    break
        if cond:
            primes.append(i)
        while n % i == 0:
            n //= i
            k += 1
        i += 1
    if n > 1:
        k += 1
    if k > 1:
        return False
    else:
        primes.append(n)
        return True
