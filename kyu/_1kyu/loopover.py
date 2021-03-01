from numpy import roll, where, array, nditer, vectorize, sign, subtract
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
    return Solver(array(mixed), array(solved)).solve()


class Solver:
    def __init__(self, mixed, solved):
        self.mixed = mixed
        self.solved = solved
        self.x, self.y = subtract(array(mixed.shape), 1)

    def solve(self):
        sub_matrix = self.solved[:self.x, :self.x]
        with nditer(sub_matrix, flags=['multi_index']) as it:
            for item in it:
                pull(self.mixed, item, it.multi_index[0])
                push(self.mixed, item, it.multi_index[0])

        self.last_row()
        self.last_column()

        return path

    def last_row(self):
        mask = self.solved[self.x, :self.x]

        for item in self.mixed[self.x, self.x - 1::-1]:
            if item not in mask:
                continue
            for _, column in zip(*where(self.mixed == item)):
                while self.mixed[self.x, self.x] in mask:
                    up(self.mixed, self.x)

                move(self.mixed, self.x, self.x - column, horizontal)

        for item in self.solved[self.x, self.x - 1::-1]:
            for row, column in zip(*where(self.mixed == item)):
                move(self.mixed, self.x, self.x - row, vertical)
                right(self.mixed, self.x)

    def last_column(self):
        m = self.solved[:self.x + 1, self.x]
        for i in range(1, self.x):
            for row, column in zip(*where(self.mixed == m[i])):
                move(self.mixed, self.x, self.x - row, vertical)
                right(self.mixed, self.x)

                for r, _ in zip(*where(self.mixed == m[i - 1])):
                    move(self.mixed, self.x, self.x - r - 1, vertical)

                left(self.mixed, self.x)
        up(self.mixed, self.x)


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
