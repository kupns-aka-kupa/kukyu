from itertools import combinations
from collections import Counter


def ulam_seq(u0, u1, n):
    out = [u0, u1]
    for i in range(n - 2):
        d = Counter(sum(j) for j in combinations(out, 2))
        u = set(j for j in d if d[j] < 2 and j > out[-1])
        out.append(min(u))
    return out
