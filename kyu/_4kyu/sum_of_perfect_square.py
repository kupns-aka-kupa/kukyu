from math import isqrt


def fac(n):
    c = 0
    while n > 0:
        r = isqrt(n)
        n = n - r ** 2
        # print(r, n)
        c += 1

    return c


def sum_of_squares(n):
    if (n - 1) % 4 == 0:
        return 2

    print(n)
    return fac(n)
