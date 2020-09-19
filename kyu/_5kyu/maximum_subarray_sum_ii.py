from itertools import product


def find_max(arr):
    s, l = 0, len(arr)
    m = 0
    for i in range(len(arr)):
        s += arr[i]
        if s < 0:
            s = 0
        elif m < s:
            m = s
    return m


def find_subarr_maxsum(arr):
    m = find_max(arr)
    if m <= 0:
        return [[], 0]

    p = product(*[[i for i in range(len(arr) + 1)]] * 2)
    index = [i for i in p if i[0] <= i[1]]
    res = [arr[i[0]:i[1]] for i in index if sum(arr[i[0]:i[1]]) == m]

    return [res, m] if len(res) > 1 else [res[0], m]
