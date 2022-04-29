from numpy import average, array, where


def closest_pair(points):
    if len(points) == 2:
        return points

    a = array(points)

    _min = a.min(0)
    _max = a.max(0)

    print(_min, _max)
    d = _max - _min
    if d[0] > d[1]:
        r = where(a[1] > d[1], a, a)
        l = where(a[1] <= d[1], a, a)

    else:
        r = where(a[0] > d[0], a, a)
        l = where(a[0] <= d[0], a, a)

    t = r if len(r) > len(l) else l
    print(t)
    return closest_pair(t)
