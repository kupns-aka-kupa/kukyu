import unittest
from .._6kyu.super_coordinate_sums_ import super_sum
from .._6kyu.ulam_sequences import ulam_seq
from .._6kyu.convert_integer_to_whitespace_format import whitespace_number


class Kata6TestCase(unittest.TestCase):

    def test_whitespace_convert(self):
        def unbleach(ws):
            return ws.replace(' ', '[space]').replace('\t', '[tab]').replace('\n', '[LF]')
        self.assertEqual(unbleach(whitespace_number(1)), unbleach(" \t\n"))
        self.assertEqual(unbleach(whitespace_number(0)), unbleach(" \n"))
        self.assertEqual(unbleach(whitespace_number(-1)), unbleach("\t\t\n"))
        self.assertEqual(unbleach(whitespace_number(2)), unbleach(" \t \n"))
        self.assertEqual(unbleach(whitespace_number(-3)), unbleach("\t\t\t\n"))

    def test_super_sum(self):
        self.assertEqual(super_sum(1, 1), 0)
        self.assertEqual(super_sum(1, 10), 45)
        self.assertEqual(super_sum(2, 2), 4)
        self.assertEqual(super_sum(2, 3), 18)
        self.assertEqual(super_sum(2, 10), 900)
        self.assertEqual(super_sum(3, 3), 81)
        self.assertEqual(super_sum(4, 4), 1536)
        self.assertEqual(super_sum(5, 5), 31250)
        self.assertEqual(super_sum(6, 6), 699840)
        self.assertEqual(super_sum(7, 7), 17294403)
        self.assertEqual(super_sum(8, 8), 469762048)

    def test_ulam_seq(self):
        self.assertEqual(ulam_seq(1, 2, 5), [1, 2, 3, 4, 6])
        self.assertEqual(ulam_seq(1, 2, 5), [1, 2, 3, 4, 6])
        self.assertEqual(ulam_seq(3, 4, 5), [3, 4, 7, 10, 11])
        self.assertEqual(ulam_seq(5, 6, 8), [5, 6, 11, 16, 17, 21, 23, 26])
        self.assertEqual(ulam_seq(3, 4, 5), [3, 4, 7, 10, 11])
        a = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69]
        self.assertEqual(ulam_seq(1, 2, 20), a)
        a = [1, 3, 4, 5, 6, 8, 10, 12, 17, 21, 23, 28, 32, 34, 39, 43, 48, 52, 54, 59, 63, 68, 72, 74, 79, 83, 98, 99,
             101, 110, 114, 121, 125, 132, 136, 139, 143, 145, 152, 161, 165, 172, 176, 187, 192, 196, 201, 205, 212,
             216, 223, 227, 232, 234, 236, 243, 247, 252, 256, 258]
        self.assertEqual(ulam_seq(1, 3, 60), a)


if __name__ == '__main__':
    unittest.main()
