import unittest
from .._4kyu.longest_slide_down import longestSlideDown
from .._4kyu.decompose_int import decompose
from .._4kyu.strip_comments import strip_comments
from .._4kyu.rectangle_rotation import rectangle_rotation
from .._4kyu.codewars_style_ranking_system import User
from .._4kyu.matrix_determinant import determinant
from .._4kyu.permutations import permutations
from .._4kyu.string_iteration import string_func
from .._4kyu.longest_palindromic_substring import longest_palindromic_substring
from .._4kyu.format_duration import format_duration
from .._4kyu.factorial_tail import zeroes
from .._4kyu.snail import snail
from .._4kyu.sum_of_perfect_square import sum_of_squares


class Kata4TestCase(unittest.TestCase):

    def test_sum_of_perfect_square(self):
        self.assertEqual(sum_of_squares(19), 3)  # 9, 9, 1
        # self.assertEqual(sum_of_squares(18), 2)  # 9, 9

        self.assertEqual(sum_of_squares(15), 4)
        self.assertEqual(sum_of_squares(16), 1)
        self.assertEqual(sum_of_squares(17), 2)
        
        self.assertEqual(sum_of_squares(2017), 2)
        self.assertEqual(sum_of_squares(1008), 3)
        self.assertEqual(sum_of_squares(4000), 2)
        # self.assertEqual(sum_of_squares(12321), 1)
        # self.assertEqual(sum_of_squares(3456), 2)

        # self.assertEqual(sum_of_squares(661915703), 4)
        # self.assertEqual(sum_of_squares(999887641), 1)
        # self.assertEqual(sum_of_squares(999950886), 3)
        # self.assertEqual(sum_of_squares(999951173), 2)
        # self.assertEqual(sum_of_squares(999998999), 1)

        # self.assertEqual(sum_of_squares(934828728), 3)
        # self.assertEqual(sum_of_squares(663367237), 2)
        # self.assertEqual(sum_of_squares(537688815), 4)
        # self.assertEqual(sum_of_squares(874270400), 3)

    def test_snail(self):

        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]

        self.assertEqual(snail(array), expected)

        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertEqual(snail(array), expected)

        array = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

        self.assertEqual(snail(array), expected)

    def test_factorial_tail(self):
        self.assertEqual(zeroes(10, 10), 2)
        self.assertEqual(zeroes(16, 16), 3)
        self.assertEqual(zeroes(17, 16), 0)
        self.assertEqual(zeroes(7, 50), 0)

    def test_format_duration(self):
        self.assertEqual(format_duration(0), "now")
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")
        self.assertEqual(format_duration(132030240), '4 years, 68 days, 3 hours and 4 minutes')
        self.assertEqual(format_duration(8468941), '98 days, 29 minutes and 1 second')

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("abababa"), "abababa")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")
        self.assertEqual(longest_palindromic_substring("ab"), "a")
        self.assertEqual(longest_palindromic_substring(""), "")

    def test_string_iteration(self):
        self.assertEqual(string_func("String", 1), "gSntir")
        self.assertEqual(string_func("String", 3), "nrtgSi")
        self.assertEqual(string_func("This is a string exemplification!", 0), "This is a string exemplification!")
        self.assertEqual(string_func("String for test: incommensurability", 1), "ySttirliinbga rfuosrn etmemsotc:n i")
        self.assertEqual(string_func("Ohh Man God Damn", 7), " nGOnmohaadhMD  ")
        self.assertEqual(string_func("Ohh Man God Damnn", 19), "haG mnad MhO noDn")

    def test_permutations(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

    def test_determinant(self):
        m1 = [[1, 3], [2, 5]]
        m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
        self.assertEqual(determinant([[1]]), 1)
        self.assertEqual(determinant(m1), -1)
        self.assertEqual(determinant(m2), -20)

    def test_rectangle_rotation(self):
        self.assertEqual(rectangle_rotation(6, 4), 23)
        self.assertEqual(rectangle_rotation(30, 2), 65)
        self.assertEqual(rectangle_rotation(8, 6), 49)
        self.assertEqual(rectangle_rotation(16, 20), 333)

    def test_ranking_system(self):
        user = User()
        self.assertEqual(user.progress, 0)
        user.inc_progress(7)
        user.inc_progress(4)
        user.inc_progress(8)
        user.inc_progress(-5)

    def test_longest_slide_down(self):
        self.assertEqual(longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]), 23)

    def test_decompose_int(self):
        self.assertEqual(decompose(11), [1, 2, 4, 10])
        self.assertEqual(decompose(50), [1, 3, 5, 8, 49])

    def test_strip_comments(self):
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                         "apples, pears\ngrapes\nbananas")
        self.assertEqual(strip_comments("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
        self.assertEqual(strip_comments("#", ["#", "!"]), "")
        self.assertEqual(strip_comments('\n§', ['#', '§']), "\n")
        self.assertEqual(strip_comments('pears - @\nwatermelons . avocados avocados watermelons\noranges\n@ '
                                        'watermelons lemons oranges\nbananas avocados avocados oranges', ['^', '=',
                                                                                                          '@', '-',
                                                                                                          "'", ',',
                                                                                                          '.', '#']),
                         'pears\nwatermelons\noranges\n\nbananas avocados avocados oranges')
        self.assertEqual(strip_comments('avocados .\n# ^ avocados\nlemons avocados',
                                        ['^', '=', ',', '!']),
                         'avocados .\n#\nlemons avocados')
        self.assertEqual(strip_comments("avocados ' avocados ,\n#\nbananas apples lemons cherries - lemons",
                                        ['=', ',', "'", '#', '!', '.', '^']),
                         'avocados\n\nbananas apples lemons cherries - lemons')


if __name__ == '__main__':
    unittest.main()
