from numpy import roll, where, array, nditer, vectorize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import depth_first_tree

to_char = vectorize(ord)

path = []


def extend_path(func):
    def wrapper(*args):
        path.append(func(*args))
    return wrapper


def loopover(mixed, solved):
    return solve(array(mixed), array(solved))


def solve(mixed, solved):
    print('Solved\n', solved)
    print('Mixed\n', mixed, '\n')

    up(mixed, 1)
    print('Mixed\n', mixed, '\n')
    for item in nditer(solved):
        for row, column in zip(*where(mixed == item)):
            offset_right(mixed, row)
            offset_up(mixed, column)
            pass
        print(mixed)
        print(path)
        return path

    return path


def offset_right(a, row):
    while row != len(a) - 1:
        right(a, row)
        row += 1


def offset_up(a, column):
    while column != 0:
        up(a, column)
        column -= 1


@extend_path
def right(a, row):
    horizontal(a, row + 1, 1)
    return f'R{row}'


@extend_path
def left(a, row):
    horizontal(a, row + 1, -1)
    return f'L{row}'


@extend_path
def up(a, column):
    vertical(a, column + 1, -1)
    return f'U{column}'


@extend_path
def down(a, column):
    vertical(a, column + 1, 1)
    return f'D{column}'


def horizontal(a, row, d):
    """
    @param row: row
    @param a: array
    @param d: direction
    """
    a[row - 1:row, :] = roll(a, d, axis=1)[row - 1:row, :]


def vertical(a, column, direction):
    """
    @param column: column
    @param a: array
    @param direction: direction
    """
    a[:, column - 1:column] = roll(a, direction, axis=0)[:, column - 1:column]
