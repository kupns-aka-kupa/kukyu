def ips_between(start, end):
    s = [*map(int, start.split("."))]
    e = list(map(int, end.split(".")))
    return sum((e[i] - s[i]) * 256 ** (3 - i) for i in range(4))
