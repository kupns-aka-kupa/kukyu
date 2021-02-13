from numpy import roll, where, array, nditer, vectorize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import depth_first_tree

to_char = vectorize(ord)


def loopover(mixed, solved):
    return solve(to_char(array(mixed)), to_char(array(solved)))


def solve(mixed, solved):
    matrix = csr_matrix(mixed)
    print(matrix)
    for item in nditer(solved):
        for i, j in zip(*where(mixed == item)):
            pass

    print(mixed)
    return []


def right(a, j):
    horizontal(a, j + 1, 1)
    return f'R{j}'


def left(a, j):
    horizontal(a, j + 1, -1)
    return f'L{j}'


def up(a, i):
    vertical(a, i + 1, -1)
    return f'U{i}'


def down(a, i):
    vertical(a, i + 1, 1)
    return f'D{i}'


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
