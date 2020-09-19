# R E C U R S I V E
# _________________


def string_func(s, x):
    if x > 0:
        return string_func(string_iter(s), x - 1)
    else:
        return s


def string_iter(s):
    if len(s) > 0:
        return s[-1] + string_iter(s[::-1][1:])
    else:
        return s


# N O N R E C U R S I V E
# _______________________


def string_func(s, x):
    for i in range(x):
        s = string_iter(s)
    return s


def string_iter(s):
    res = ''
    while len(s) > 0:
        res += s[-1]
        s = s[::-1][1:]
    return res

