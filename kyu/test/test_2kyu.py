import unittest
from .._2kyu.regular_expression___check_if_divisible_by_0b111__7_ import solution


class Kata2TestCase(unittest.TestCase):
    def test_check_divisible_by_7(self):
        for num in range(0, 101):
            self.assertEqual(solution(num), num % 7 == 0)


if __name__ == '__main__':
    unittest.main()
