

def tribonacci(s, n):
    _l = len(s)
    if n < _l:
        return s[:n]
    for i in range(n - _l):
        s.append(sum(s[i:i + 3]))
    return s


def Xbonacci(s, n):
    _l = len(s)
    if n < _l:
        return s[:n]
    for i in range(n - _l):
        s.append(sum(s[i:i + _l]))
    return s
