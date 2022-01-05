from numpy import roll, where, array, nditer, sign, subtract as sub, in1d, argwhere, array_equal
from numpy.ma import masked_array
from enum import Enum


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


class Puzzle:
    a: array

    def __init__(self):
        self.__moves = {Direction.Up: self.up,
                        Direction.Down: self.down,
                        Direction.Left: self.left,
                        Direction.Right: self.right}

    def __eq__(self, other):
        return array_equal(self.a, other.a)

    @staticmethod
    def from_str(s: str):
        p = Puzzle()
        p.a = array(list(map(list, s.split('\n'))))
        return p

    def right(self, row):
        return horizontal(self.a, row + 1, 1)

    def left(self, row):
        return horizontal(self.a, row + 1, -1)

    def up(self, column):
        return vertical(self.a, column + 1, -1)

    def down(self, column):
        return vertical(self.a, column + 1, 1)

    def apply(self, *moves: Move):
        for m in moves:
            self.__moves[m.d](m.i)


def loopover(mixed: str, solved: str):
    return Solver(Puzzle.from_str(mixed).a, Puzzle.from_str(solved).a).solve()


class Solver:
    def __init__(self, mixed, solved):
        self.mixed = mixed
        self.solved = solved
        self.x, self.y = sub(array(mixed.shape), 1)

    def solve(self):
        yield from self.first_step()
        yield from self.second_step()
        yield from self.last_step()

        print(self.mixed)

    def first_step(self):
        with nditer(self.solved[:self.x, :self.y], flags=['multi_index']) as it:
            for item in it:
                yield from self.pull(item, it.multi_index[0])
                yield from self.push(item, it.multi_index[0])

    def second_step(self):
        yield from self.stack_last_row()
        yield from self.push_last_row()

    def last_step(self):
        column = self.solved[:self.x + 1, self.y]
        for i in range(1, self.y):
            for row, _ in zip(*where(self.mixed == column[i])):
                yield from move(self.y, self.x - row, self.vertical)
                yield self.right(self.x)

                print(self.mixed)
                for r, _ in zip(*where(self.mixed == column[i - 1])):
                    yield from move(self.y, self.x - r - 1, self.vertical)

                print(self.mixed)
                yield self.left(self.x)
                print(self.mixed)
        yield self.up(self.y)

    def stack_last_row(self):
        mask = self.solved[self.x, :self.y]
        sliced = self.mixed[self.x, self.y - 1::-1]

        for item in masked_array(sliced, ~in1d(sliced, mask)).compressed():
            for _, column in zip(*where(self.mixed == item)):
                while self.mixed[self.x, self.y] in mask:
                    yield self.up(self.y)

                yield from move(self.x, self.y - column, self.horizontal)

    def push_last_row(self):
        for item in self.solved[self.x, self.y - 1::-1]:
            for row, _ in zip(*where(self.mixed == item)):
                yield from move(self.y, self.x - row, self.vertical)
                yield self.right(self.x)

    def push(self, item, row):
        for i, column in zip(*where(self.mixed == item)):
            yield from move(i, self.y - column, self.horizontal)
            yield from move(self.y, row - i, self.vertical)
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
        horizontal(self.mixed, r, d)
        return Move(Direction.Right if d > 0 else Direction.Left, abs(r - 1))

    def vertical(self, c, d):
        return vertical(self.mixed, c, d)


def move(index, steps, func):
    for _ in range(abs(steps)):
        yield func(index + 1, sign(steps))


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
