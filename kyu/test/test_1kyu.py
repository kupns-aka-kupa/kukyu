import unittest
from kyu._1kyu.loopover import loopover


def board(s):
    return [list(row) for row in s.split('\n')]


def run_test(start, end):
    return loopover(board(start), board(end))


class LoopoverTestCase(unittest.TestCase):

    def test_2x2_1(self):
        """Test 2x2 (1)"""
        m = run_test('12\n34', '12\n34')
        self.assertIsNotNone(m)

    def test_2x2_1(self):
        """Test 2x2 (2)"""
        m = run_test('42\n31', '12\n34')
        self.assertIsNotNone(m)

    @unittest.skip('Test 4x5')
    def test_4x5_1(self):
        m = run_test('ACDBE\nFGHIJ\nKLMNO\nPQRST',
                     'ABCDE\nFGHIJ\nKLMNO\nPQRST')
        self.assertIsNotNone(m)

    def test_5x5_1(self):
        m = run_test('ACDBE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
                     'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY')
        self.assertIsNotNone(m)

    @unittest.skip('Test 5x5 (2)')
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
