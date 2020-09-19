import math


def rectangle_rotation(a, b):
    s = math.sqrt(2) / 2
    bc = b * s
    ac = a * s
    outer_rect = [math.floor(bc), math.floor(ac)]
    inner_rect = [math.floor(bc), math.floor(ac)]
    if bc - math.floor(bc) > .5:
        bc += 1
    if ac - math.floor(ac) > .5:
        ac += 1
    res = ac * bc + (ac - 1) * (bc - 1)

    print(ac * bc, (ac - 1) * (bc - 1), res)
    return res

