import itertools as it

lock = [[8, 0],
        [1, 2, 4],
        [1, 2, 3, 5],
        [2, 3, 6],
        [1, 4, 5, 7],
        [2, 4, 5, 6, 8],
        [3, 5, 6, 9],
        [4, 7, 8],
        [5, 7, 8, 9, 0],
        [6, 8, 9]]


def get_pins(observed):
    c = (list(map(str, lock[int(i)])) for i in observed)
    return list(map(''.join, it.product(*c, repeat=1)))
