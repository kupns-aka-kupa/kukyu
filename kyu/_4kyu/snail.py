from numpy import array
from numpy import concatenate


def snail(m):
    l = len(m) - 1

    if l < 0:
        return []
    elif l == 0:
        return m[0]

    a = array(m)

    up = a[0, :l]
    right = a[:l, l]
    left = a[l:0:-1, 0]
    down = a[l, l:0:-1]
    inner = snail(a[1:l, 1:l])
    return concatenate([up, right, down, left, inner]).astype(int).tolist()
