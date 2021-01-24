from numpy import roll, where, array, nditer


def loopover(mixed, solved):
    return solve(array(mixed), array(solved))


def solve(mixed, solved):
    for item in nditer(solved):
        for i, j in zip(*where(mixed == item)):
            print(i, j)

    print(mixed)
    return []


def right(a, j):
    horizontal(a, j + 1, 1)


def left(a, j):
    horizontal(a, j + 1, -1)


def up(a, i):
    vertical(a, i + 1, -1)


def down(a, i):
    vertical(a, i + 1, 1)


def horizontal(a, j, d):
    """
    @param j: row
    @param a: array
    @param d: direction
    """
    a[:j, :] = roll(a, d, axis=1)[:j, :]


def vertical(a, i, d):
    """
    @param i: column
    @param a: array
    @param d: direction
    """
    a[:, :i] = roll(a, d, axis=0)[:, :i]
