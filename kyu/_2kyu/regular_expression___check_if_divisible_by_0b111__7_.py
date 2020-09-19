import re


def solution(n):
    res = [bin(j)[2:] + bin(i)[2:] for j in range(100) for i in range(10) if (j - 2 * i) % 7 == 0]

    print(res)
    b = bin(n)
    rgx = re.compile(r"")
    return bool(rgx.match(b[2:]))

