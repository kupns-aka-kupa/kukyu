def _k(i): return 1 if i % 2 == 0 else -1


def _2x2_det(m):
    return float(m[0][0] * m[1][1] - m[0][1] * m[1][0])


def _3x3_det(m):
    n = len(m[0])
    return float(sum(
        _k(i) * m[0][i] * _2x2_det(
            _minor(m, i)
        ) for i in range(n)
    ))


def _nxn_det(m):
    n = len(m[0])
    if n < 5:
        return float(sum(_k(i) * m[0][i] * _3x3_det(_minor(m, i)) for i in range(n)))
    else:
        return float(sum(_k(i) * m[0][i] * _nxn_det(_minor(m, i)) for i in range(n)))


def _minor(m, i):
    n = len(m[0])
    keys = [sorted([(i + p) % n for p in range(1, n)]) for j in range(1, n)]
    return [[m[j][keys[j - 1][p - 1]] for p in range(1, n)]
            for j in range(1, n)]


def determinant(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    elif n == 2:
        return _2x2_det(m)
    elif n == 3:
        return _3x3_det(m)
    else:
        return _nxn_det(m)
