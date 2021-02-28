from numpy import roll, where, array, nditer, vectorize, sign
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import depth_first_tree

to_char = vectorize(ord)

path = []
move_format = '{0}{1}'


def extend_path(func):
    def wrapper(*args):
        path.append(func(*args))
    return wrapper


def loopover(mixed, solved):
    return solve(array(mixed), array(solved))


def solve(mixed, solved):
    cut = solved[:len(solved) - 1, :len(solved) - 1]
    with nditer(cut, flags=['multi_index']) as it:
        for item in it:
            pull(mixed, item, it.multi_index[0])
            push(mixed, item, it.multi_index[0])

    print(mixed)
    print(len(path), path)
    return path


def push(a, item, i):
    for row, column in zip(*where(a == item)):
        move(a, row, len(a) - column - 1, horizontal)
        move(a, len(a) - 1, i - row, vertical)
        left(a, i)


def pull(a, item, i):
    for row, column in zip(*where(a == item)):
        if i == row:
            down(a, column)
            right(a, row + 1)
            up(a, column)


def move(a, index, steps, func):
    for _ in range(abs(steps)):
        func(a, index + 1, sign(steps))


def right(a, row):
    return horizontal(a, row + 1, 1)


def left(a, row):
    return horizontal(a, row + 1, -1)


def up(a, column):
    return vertical(a, column + 1, -1)


def down(a, column):
    return vertical(a, column + 1, 1)


@extend_path
def horizontal(a, r, d):
    """
    @param r: row
    @param a: array
    @param d: direction
    """
    a[r - 1:r, :] = roll(a, d, axis=1)[r - 1:r, :]
    return move_format.format('R' if d > 0 else 'L', abs(d))


@extend_path
def vertical(a, c, d):
    """
    @param c: column
    @param a: array
    @param d: direction
    """
    a[:, c - 1:c] = roll(a, d, axis=0)[:, c - 1:c]
    return move_format.format('D' if d > 0 else 'U', abs(d))
