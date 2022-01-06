import unittest
from kyu._1kyu.loopover import loopover, Puzzle, Move, Direction
from numpy import array_equal


def run_test(start, end):
    return list(loopover(start, end))


class PuzzleTestCase(unittest.TestCase):

    def test_move_class(self):
        self.assertEqual(str(Move(Direction.Up, 1)), "U1")
        self.assertEqual(str(Move(Direction.Down, 0)), "D0")

        with self.assertRaises(AssertionError):
            self.assertEqual(str(Move(Direction.Right, -2)), "R-2")

        self.assertEqual(str(Move(Direction.Left, 4)), "L4")

    def test_puzzle_from_str(self):
        p = Puzzle.from_str('ACDBE\nFGHIJ\nKLMNO\nPQRST')
        self.assertIsNotNone(p)
        self.assertEqual(p.shape, (4, 5))
        p = Puzzle.from_str('12\n34')
        self.assertEqual(p.shape, (2, 2))
        self.assertIsNotNone(p)

    def test_horizontal_rotation(self):
        p = Puzzle.from_str('12\n'
                            '34')
        p.right(0)
        self.assertTrue(array_equal(p, Puzzle.from_str('21\n'
                                                       '34')))
        p.right(1)
        self.assertTrue(array_equal(p, Puzzle.from_str('21\n'
                                                       '43')))

        p.right(0)
        p.right(0)
        self.assertTrue(array_equal(p, Puzzle.from_str('21\n'
                                                       '43')))

    def test_vertical_rotation(self):
        p = Puzzle.from_str('12\n34')
        p.down(0)
        self.assertTrue(array_equal(p, Puzzle.from_str('32\n'
                                                       '14')))
        p.down(1)
        self.assertTrue(array_equal(p, Puzzle.from_str('34\n'
                                                       '12')))

        p.down(0)
        p.down(0)
        self.assertTrue(array_equal(p, Puzzle.from_str('34\n'
                                                       '12')))

    def test_move_lang(self):
        p = Puzzle.from_str('12\n34')
        p.apply(Move(Direction.Down, 0))
        self.assertTrue(array_equal(p, Puzzle.from_str('32\n'
                                                       '14')))
        p.apply(Move(Direction.Down, 1))
        self.assertTrue(array_equal(p, Puzzle.from_str('34\n'
                                                       '12')))

        p.apply(*iter([]))
        self.assertTrue(array_equal(p, Puzzle.from_str('34\n'
                                                       '12')))


class LoopoverTestCase(unittest.TestCase):

    def test_2x2(self):
        def data():
            yield '42\n31', '12\n34'
            yield '12\n34', '12\n34'

        for mixed, solved in data():
            moves = run_test(mixed, solved)
            a = Puzzle.from_str(mixed)

            a.apply(*moves)

            self.assertTrue(array_equal(a, Puzzle.from_str(solved)))

    def test_4x5_1(self):
        mixed = 'ACDBE\nFGHIJ\nKLMNO\nPQRST'
        solved = 'ABCDE\nFGHIJ\nKLMNO\nPQRST'

        moves = run_test(mixed, solved)
        a = Puzzle.from_str(mixed)

        self.assertTrue(moves)

        a.apply(*moves)

        self.assertEqual(a, Puzzle.from_str(solved))

    def test_5x5_1(self):
        mixed = 'ACDBE\nFGHIJ\nKLMNO\nPQRST\nUVWXY'
        solved = 'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY'

        moves = run_test(mixed, solved)
        a = Puzzle.from_str(mixed)

        self.assertTrue(moves)

        a.apply(*moves)
        self.assertEqual(a, Puzzle.from_str(solved))

    def test_5x5_2(self):
        m = run_test('ABCDE\nKGHIJ\nPLMNO\nFQRST\nUVWXY',
                     'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY')
        self.assertIsNotNone(m)

    @unittest.skip('Test 5x5 (3)')
    def test_5x5_3(self):
        m = run_test('CWMFJ\nORDBA\nNKGLY\nPHSVE\nXTQUI',
                     'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY')

    @unittest.skip('Test 5x5 (unsolvable)')
    def test_5x5_4(self):
        m = run_test('WCMDJ\nORFBA\nKNGLY\nPHVSE\nTXQUI',
                     'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY')
        self.assertIsNone(m)

    @unittest.skip('Test 6x6')
    def test_6x6(self):
        m = run_test('WCMDJ0\nORFBA1\nKNGLY2\nPHVSE3\nTXQUI4\nZ56789',
                     'ABCDEF\nGHIJKL\nMNOPQR\nSTUVWX\nYZ0123\n456789')
        self.assertIsNotNone(m)


if __name__ == '__main__':
    unittest.main()
