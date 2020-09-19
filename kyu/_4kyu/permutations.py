from itertools import permutations as perm


def permutations(s):
    return [''.join(i) for i in set(perm(s))]
