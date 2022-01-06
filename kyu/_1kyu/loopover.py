from numpy import roll, where, array, nditer, subtract as sub, in1d, argwhere, ndarray, asarray
from numpy.ma import masked_array
from enum import Enum


def loopover(mixed: str, solved: str):
    return Solver(Puzzle.from_str(mixed), Puzzle.from_str(solved)).solve()


class Direction(Enum):
    Up = 'U'
    Down = 'D'
    Right = 'R'
    Left = 'L'

    def __str__(self):
        return self.value


class Move:
    d: Direction
    i: int

    def __init__(self, d, i):
        assert i >= 0

        self.d = d
        self.i = i

    def __str__(self):
        return '{0}{1}'.format(self.d, self.i)

    @classmethod
    def build(cls, i, steps, d: Direction):
        for _ in range(abs(steps)):
            yield Move(d, i)


class Puzzle(ndarray):

    def __new__(cls, a):
        self = asarray(a).view(cls)
        self.moves = {Direction.Up: self.up,
                      Direction.Down: self.down,
                      Direction.Left: self.left,
                      Direction.Right: self.right}
        return self

    @staticmethod
    def from_str(s: str):
        return Puzzle(list(map(list, s.split('\n'))))

    def right(self, row):
        return horizontal(self, row + 1, 1)

    def left(self, row):
        return horizontal(self, row + 1, -1)

    def up(self, column):
        return vertical(self, column + 1, -1)

    def down(self, column):
        return vertical(self, column + 1, 1)

    def horizontal(self, r, d):
        return horizontal(self, r, d)

    def vertical(self, c, d):
        return vertical(self, c, d)

    def apply(self, *args: Move):
        for m in args:
            yield self.moves[m.d](m.i)


class Solver:
    def __init__(self, mixed: Puzzle, solved: Puzzle):
        self.mixed = mixed
        self.solved = solved

        assert mixed.shape == solved.shape

        self.x, self.y = sub(array(mixed.shape), 1)

    def solve(self):
        print(self.mixed)
        yield from self.first_step()
        # yield from self.second_step()
        # yield from self.last_step()

        print(self.mixed)

    def first_step(self):
        """Solve (m-1, n-1) rectangle"""

        with nditer(self.solved[:self.x, :self.y], flags=['multi_index']) as it:
            for item in it:
                i, _ = it.multi_index
                yield from self.pull(item, i)
                yield from self.push(item, i)

    def second_step(self):
        yield from self.stack_last_row()
        yield from self.push_last_row()

    def last_step(self):
        column = self.solved[:self.x + 1, self.y]
        for i in range(1, self.y):
            for row, _ in zip(*where(self.mixed == column[i])):
                yield from self.mixed.apply(*Move.build(self.y, self.x - row, Direction.Up))

                yield self.mixed.right(self.x)

                print(self.mixed)
                for r, _ in zip(*where(self.mixed == column[i - 1])):
                    yield from self.mixed.apply(*Move.build(self.y, self.x - r - 1, Direction.Up))

                print(self.mixed)
                yield self.mixed.left(self.x)
                print(self.mixed)
        yield self.mixed.up(self.y)

    def stack_last_row(self):
        mask = self.solved[self.x, :self.y]
        sliced = self.mixed[self.x, self.y - 1::-1]

        for item in masked_array(sliced, ~in1d(sliced, mask)).compressed():
            for _, column in zip(*where(self.mixed == item)):
                while self.mixed[self.x, self.y] in mask:
                    yield self.mixed.up(self.y)

                yield from self.mixed.apply(*Move.build(self.x, self.y - column, Direction.Right))

    def push_last_row(self):
        for item in self.solved[self.x, self.y - 1::-1]:
            for row, _ in zip(*where(self.mixed == item)):
                yield from self.mixed.apply(*Move.build(self.y, self.x - row, Direction.Up))
                yield self.mixed.right(self.x)

    def push(self, item, row):
        for i, column in zip(*where(self.mixed == item)):
            r = list(Move.build(i, self.y - column, Direction.Right))
            yield from self.mixed.apply(*r)

            u = list(Move.build(self.y, row - i, Direction.Up))
            yield from self.mixed.apply(*u)
            yield self.mixed.left(row)

    def pull(self, item, row):
        s = argwhere(self.mixed[row] == item)

        if s.size == 0:
            return

        for column in s.reshape(1):
            yield self.mixed.down(column)
            yield self.mixed.right(row + 1)
            yield self.mixed.up(column)


def horizontal(a, r, d):
    """
    @param r: row
    @param a: array
    @param d: direction
    """
    a[r - 1:r, :] = roll(a, d, axis=1)[r - 1:r, :]
    return Move(Direction.Right if d > 0 else Direction.Left, abs(r - 1))


def vertical(a, c, d):
    """
    @param c: column
    @param a: array
    @param d: direction
    """
    a[:, c - 1:c] = roll(a, d, axis=0)[:, c - 1:c]
    return Move(Direction.Down if d > 0 else Direction.Up, abs(c - 1))
