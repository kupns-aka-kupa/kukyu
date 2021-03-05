import unittest
from kyu._1kyu.loopover import loopover, horizontal, vertical
from numpy import array, array_equal, arange


def right(a, row):
    return horizontal(a, row + 1, 1)


def left(a, row):
    return horizontal(a, row + 1, -1)


def up(a, column):
    return vertical(a, column + 1, -1)


def down(a, column):
    return vertical(a, column + 1, 1)


def direction(d):
    if d == 'R':
        return right
    elif d == 'L':
        return left
    elif d == 'U':
        return up
    elif d == 'D':
        return down


def apply_config(a, moves):
    for m in moves:
        i = int(m[1:])
        func = direction(m[0])
        func(a, i)


def board(s):
    return [list(row) for row in s.split('\n')]


def run_test(start, end):
    return loopover(board(start), board(end))


class LoopoverTestCase(unittest.TestCase):

    def test_horizontal_rotation(self):
        a = array(board('12\n34'))
        right(a, 0)
        self.assertTrue(array_equal(a, array(board('21\n34'))))
        right(a, 1)
        self.assertTrue(array_equal(a, array(board('21\n43'))))

        right(a, 0)
        right(a, 0)
        self.assertTrue(array_equal(a, array(board('21\n43'))))

    def test_vertical_rotation(self):
        a = array(board('12\n34'))
        down(a, 0)
        self.assertTrue(array_equal(a, array(board('32\n14'))))
        down(a, 1)
        self.assertTrue(array_equal(a, array(board('34\n12'))))

        down(a, 0)
        down(a, 0)
        self.assertTrue(array_equal(a, array(board('34\n12'))))

    def test_sub_matrix_stage(self):
        a = arange(5 * 5).reshape(5, 5)

    def test_2x2_1(self):
        """Test 2x2 (1)"""
        solved = '12\n34'
        mixed = '12\n34'

        moves = run_test(mixed, solved)
        a = array(board(solved))

        apply_config(a, moves)

        self.assertIsNotNone(moves)
        self.assertTrue(array_equal(a, array(board(solved))))

    def test_2x2_2(self):
        """Test 2x2 (2)"""
        m = run_test('42\n31', '12\n34')
        self.assertIsNotNone(m)

    @unittest.skip('Test 4x5')
    def test_4x5_1(self):
        s = 'ABCDE\nFGHIJ\nKLMNO\nPQRST'
        m = run_test('ACDBE\nFGHIJ\nKLMNO\nPQRST', s)
        self.assertIsNotNone(m)

    def test_5x5_1(self):
        mixed = 'ACDBE\nFGHIJ\nKLMNO\nPQRST\nUVWXY'
        solved = 'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY'
        moves = run_test(mixed, solved)
        a = array(board(solved))

        apply_config(a, moves)
        self.assertIsNotNone(moves)

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
