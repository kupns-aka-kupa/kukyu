from numpy import roll, where, array, nditer, sign, subtract as sub, in1d, argwhere
from numpy.ma import masked_array

move_format = '{0}{1}'


def loopover(mixed, solved):
    return Solver(array(mixed), array(solved)).solve()


class Solver:
    def __init__(self, mixed, solved):
        self.mixed = mixed
        self.solved = solved
        self.x, self.y = sub(array(mixed.shape), 1)

    def solve(self):
        sub_matrix = self.solved[:self.x, :self.x]
        with nditer(sub_matrix, flags=['multi_index']) as it:
            for item in it:
                yield from self.pull(item, it.multi_index[0])
                yield from self.push(item, it.multi_index[0])

        yield from self.last_row()
        yield from self.last_column()

        print(self.mixed)

    def last_row(self):
        mask = self.solved[self.x, :self.x]
        sliced = self.mixed[self.x, self.x - 1::-1]

        for item in masked_array(sliced, ~in1d(sliced, mask)).compressed():
            for _, column in zip(*where(self.mixed == item)):
                while self.mixed[self.x, self.x] in mask:
                    yield self.up(self.x)

                yield from self.move(self.x, self.x - column, self.horizontal)

        for item in self.solved[self.x, self.x - 1::-1]:
            for row, _ in zip(*where(self.mixed == item)):
                yield from self.move(self.x, self.x - row, self.vertical)
                yield self.right(self.x)

    def last_column(self):
        m = self.solved[:self.x + 1, self.x]
        for i in range(1, self.x):
            for row, _ in zip(*where(self.mixed == m[i])):
                yield from self.move(self.x, self.x - row, self.vertical)
                yield self.right(self.x)

                for r, _ in zip(*where(self.mixed == m[i - 1])):
                    yield from self.move(self.x, self.x - r - 1, self.vertical)

                yield self.left(self.x)
        yield self.up(self.x)

    def push(self, item, row):
        for i, column in zip(*where(self.mixed == item)):
            yield from self.move(i, self.x - column, self.horizontal)
            yield from self.move(self.x, row - i, self.vertical)
            yield self.left(row)

    def pull(self, item, row):
        s = argwhere(self.mixed[row] == item)

        if s.size == 0:
            return

        for column in s.reshape(1):
            yield self.down(column)
            yield self.right(row + 1)
            yield self.up(column)

    def right(self, row):
        return self.horizontal(row + 1, 1)

    def left(self, row):
        return self.horizontal(row + 1, -1)

    def up(self, column):
        return self.vertical(column + 1, -1)

    def down(self, column):
        return self.vertical(column + 1, 1)

    def horizontal(self, r, d):
        return horizontal(self.mixed, r, d)

    def vertical(self, c, d):
        return vertical(self.mixed, c, d)

    def move(self, index, steps, func):
        for _ in range(abs(steps)):
            yield func(index + 1, sign(steps))


def right(a, row):
    return horizontal(a, row + 1, 1)


def left(a, row):
    return horizontal(a, row + 1, -1)


def up(a, column):
    return vertical(a, column + 1, -1)


def down(a, column):
    return vertical(a, column + 1, 1)


def horizontal(a, r, d):
    """
    @param r: row
    @param a: array
    @param d: direction
    """
    a[r - 1:r, :] = roll(a, d, axis=1)[r - 1:r, :]
    return move_format.format('R' if d > 0 else 'L', abs(d))


def vertical(a, c, d):
    """
    @param c: column
    @param a: array
    @param d: direction
    """
    a[:, c - 1:c] = roll(a, d, axis=0)[:, c - 1:c]
    return move_format.format('D' if d > 0 else 'U', abs(d))
