import unittest
from .._5kyu.maximum_subarray_sum_ii import find_subarr_maxsum
from .._5kyu.k_primes import *
from .._5kyu.simple_pig_latin import pig_it
from .._5kyu.number_factorization import primeFactors
from .._5kyu.regex_password_validation import validate_password
from .._5kyu.validdate_regex import date_validation, valid_date
from .._5kyu.regex_like_a_boss__4_codegolf___prime_length import prime_len
from .._5kyu.mod4_regex import mod4
from .._5kyu.count_ip_addresses import ips_between
from .._5kyu.extract_the_domain_name_from_a_url import domain_name
from .._5kyu.jumbled_string import jumbled_string
from .._5kyu.rotate_a_square_matrix_in_place import rotate_in_place
from .._5kyu.prime_memoization import is_prime


class Katas5TestCase(unittest.TestCase):

    def test_prime_memoization(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(143), False)
        self.assertEqual(is_prime(-1), False)
        self.assertEqual(is_prime(29), True)
        self.assertEqual(is_prime(53), True)
        self.assertEqual(is_prime(529), False)
        self.assertEqual(is_prime(90144263), False)

    def test_rotate_in_place(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rmatrix = [[7, 4, 1],
                   [8, 5, 2],
                   [9, 6, 3]]

        matrix2 = [[1, 2],
                   [3, 4]]
        rmatrix2 = [[3, 1],
                    [4, 2]]

        self.assertEqual(rotate_in_place(matrix2), rmatrix2)
        self.assertEqual(rotate_in_place(matrix), rmatrix)

    def test_jumbled_string(self):
        s = "".join(str(i) for i in range(17))
        self.assertEqual(s, jumbled_string(s, 22))
        self.assertEqual("123", jumbled_string("123", 2))
        self.assertEqual("1234", jumbled_string("1234", 4))
        self.assertEqual("12345", jumbled_string("12345", 4))
        self.assertEqual("123456", jumbled_string("123456", 4))
        self.assertEqual("1234567", jumbled_string("1234567", 6))
        self.assertEqual("Sc o!uhWw", jumbled_string("Such Wow!", 1))
        self.assertEqual("Such Wow!", jumbled_string("Such Wow!", 6))
        self.assertEqual("bexltept merae", jumbled_string("better example", 2))
        self.assertEqual("better example", jumbled_string("better example", 12))
        self.assertEqual("qtorieuwy", jumbled_string("qwertyuio", 2))
        self.assertEqual("Gtsegenri", jumbled_string("Greetings", 8))
        self.assertEqual("Greetings", jumbled_string("Greetings", 6))

    def test_domain_name_extract(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("https://hyphen-site.org"), "hyphen-site")
        self.assertEqual(domain_name("http://www.codewars.com/kata/"), "codewars")
        self.assertEqual(domain_name("icann.org"), "icann")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")

    def test_find_sub_arr_sum(self):
        self.assertEqual(find_subarr_maxsum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [[4, -1, 2, 1], 6])
        self.assertEqual(find_subarr_maxsum([4, -1, 2, 1, -40, 1, 2, -1, 4]), [[[4, -1, 2, 1], [1, 2, -1, 4]], 6])
        self.assertEqual(find_subarr_maxsum([-2, 1, 4, -1, 2, 1, -5, 4]), [[1, 4, -1, 2, 1], 7])
        self.assertEqual(find_subarr_maxsum([-2, -1, 2, 1, -5, 4]), [[4], 4])
        self.assertEqual(find_subarr_maxsum([2, 1, 2, 1]), [[2, 1, 2, 1], 6])
        self.assertEqual(find_subarr_maxsum([-2, -1, -2, -1]), [[], 0])
        self.assertEqual(find_subarr_maxsum([]), [[], 0])

        arr = [10, 4, -9, 10, 0, -4, -8, -2, -4, 8, -9, -9, 8, -6, -10, -6, 10, 1, -7, 8]
        self.assertEqual(find_subarr_maxsum(arr), [[[10, 4, -9, 10], [10, 4, -9, 10, 0]], 15])

        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(find_subarr_maxsum(arr), [[4, -1, 2, 1], 6])

        arr = [4, -1, 2, 1, -40, 1, 2, -1, 4]
        self.assertEqual(find_subarr_maxsum(arr), [[[4, -1, 2, 1], [1, 2, -1, 4]], 6])

        arr = [-4, -1, -2, -1, -40, -1, -2, -1, -4]
        self.assertEqual(find_subarr_maxsum(arr), [[], 0])

        arr = [2, 1, 3, 4, 1, 2, 1, 5, 4]
        self.assertEqual(find_subarr_maxsum(arr), [[2, 1, 3, 4, 1, 2, 1, 5, 4], 23])

    def test_regex_prime_len(self):
        self.assertEqual(prime_len(''), None)
        self.assertEqual(prime_len('x'), None)
        self.assertEqual(prime_len('xxxx'), None)
        self.assertEqual(prime_len('xxxxxx'), None)
        self.assertEqual(prime_len('xxxxxxxx'), None)
        self.assertEqual(prime_len('xxxxxxxxx'), None)
        self.assertEqual(prime_len('xxxxxxxxxx'), None)
        self.assertEqual(prime_len('xxxxxxxxxxxx'), None)
        self.assertEqual(prime_len('xxxxxxxxxxxxxx'), None)
        self.assertEqual(prime_len('xxxxxxxxxxxxxxx'), None)
        self.assertEqual(prime_len('xxxxxxxxxxxxxxxx'), None)
        self.assertNotEqual(prime_len('xx'), None)
        self.assertNotEqual(prime_len('xxx'), None)
        self.assertNotEqual(prime_len('xxxxx'), None)
        self.assertNotEqual(prime_len('xxxxxxx'), None)
        self.assertNotEqual(prime_len('xxxxxxxxxxx'), None)
        self.assertNotEqual(prime_len('xxxxxxxxxxxxx'), None)

    def test_ip_count(self):
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("10.0.0.0", "10.0.1.0"), 256)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)

    def test_mod4_regex(self):
        valid = ["[+05620]", "[005624]", "[-05628]", "[005632]", "[555636]", "[+05640]", "[005600]",
                 "the beginning [-0] the end", "~[4]", "[32]",
                 "the beginning [0] ... [invalid] numb[3]rs ... the end",
                 "...may be [+002016] will be."]
        for test in valid:
            self.assertNotEqual(mod4(test), None)
        invalid = ["[+05621]", "[-55622]",
                   "[005623]", "[~24]", "[8.04]",
                   "No, [2014] isn't a multiple of 4..."]
        for test in invalid:
            self.assertEqual(mod4(test), None)

    def test_valid_date(self):
        self.assertEqual(valid_date("[02-31]"), None)
        self.assertEqual(valid_date('&08-13]'), None)
        self.assertNotEqual(valid_date("[01-23]"), None)
        self.assertNotEqual(valid_date("[[[08-29]]]"), None)
        self.assertNotEqual(valid_date("[02-16]"), None)
        self.assertEqual(valid_date("[ 6-03]"), None)
        self.assertNotEqual(valid_date("ignored [08-11] ignored"), None)
        self.assertNotEqual(valid_date("[3] [12-04] [09-tenth]"), None)
        self.assertEqual(valid_date("[02-00]"), None)
        self.assertEqual(valid_date("[13-02]"), None)
        self.assertNotEqual(valid_date("[02-[08-11]04]"), None)

    def test_date_validation(self):
        self.assertEqual(date_validation("29.02.2016"), True)
        self.assertEqual(date_validation("29.02.0400"), True)
        self.assertEqual(date_validation("30.01.2009"), True)
        self.assertEqual(date_validation("29.02.2009"), False)
        self.assertEqual(date_validation("29.02.0100"), False)
        self.assertEqual(date_validation("29.02.9700"), False)
        self.assertEqual(date_validation("31.03.0000"), False)
        self.assertEqual(date_validation("29.02.0004"), True)
        self.assertEqual(date_validation("29.01.2009"), True)
        self.assertEqual(date_validation("31.03.2009"), True)
        self.assertEqual(date_validation("31.04.2009"), False)
        self.assertEqual(date_validation('01.01.2009'), True)
        self.assertEqual(date_validation('01-Jan-2009'), False)
        self.assertEqual(date_validation('05.15.2009'), False)
        self.assertEqual(date_validation("01-01-2009"), False)
        self.assertEqual(date_validation("28.02.2020"), True)

    def test_password_validation(self):
        self.assertEqual(validate_password('fjd3IR9'), True)
        self.assertEqual(validate_password('j/3XbiHwD1'), False)
        self.assertEqual(validate_password('+Zg7Y6lt'), False)
        self.assertEqual(validate_password('\\PLNy8W6fD0F1Vn'), False)
        self.assertEqual(validate_password('NX3\\O49IJnWj3y3'), False)
        self.assertEqual(validate_password('woEg81pqVa_S'), False)
        self.assertEqual(validate_password('ghdfj32'), False)
        self.assertEqual(validate_password('DSJKHD23'), False)
        self.assertEqual(validate_password('dsF43'), False)
        self.assertEqual(validate_password('4fdg5Fj3'), True)
        self.assertEqual(validate_password('DHSJdhjsU'), False)
        self.assertEqual(validate_password('fjd3IR9.;'), False)
        self.assertEqual(validate_password('fjd3  IR9'), False)
        self.assertEqual(validate_password('djI38D55'), True)
        self.assertEqual(validate_password('a2.d412'), False)
        self.assertEqual(validate_password('JHD5FJ53'), False)
        self.assertEqual(validate_password('!fdjn345'), False)
        self.assertEqual(validate_password('jfkdfj3j'), False)
        self.assertEqual(validate_password('123'), False)
        self.assertEqual(validate_password('abc'), False)
        self.assertEqual(validate_password('123abcABC'), True)
        self.assertEqual(validate_password('ABC123abc'), True)
        self.assertEqual(validate_password('Password123'), True)

    def test_k_number(self):
        self.assertEqual(count_Kprimes(5, 500, 600), [500, 520, 552, 567, 588, 592, 594])
        self.assertEqual(count_Kprimes(2, 0, 100),
                         [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69,
                          74, 77, 82, 85, 86, 87, 91, 93, 94, 95])
        self.assertEqual(count_Kprimes(2, 0, 100),
                         [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55,
                          57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95])
        self.assertEqual(count_Kprimes(5, 1000, 1100), [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100])
        self.assertEqual(count_Kprimes(5, 500, 600), [500, 520, 552, 567, 588, 592, 594])
        self.assertEqual(count_Kprimes(4, 2668458, 2668805),
                         [2668458, 2668468, 2668482, 2668485, 2668493, 2668494, 2668497,
                          2668504, 2668509, 2668515, 2668522, 2668525, 2668526, 2668530,
                          2668532, 2668533, 2668534, 2668542, 2668548, 2668551, 2668556,
                          2668562, 2668566, 2668567, 2668570, 2668578, 2668589, 2668599,
                          2668604, 2668611, 2668612, 2668614, 2668617, 2668622, 2668623,
                          2668628, 2668636, 2668645, 2668648, 2668665, 2668668, 2668674,
                          2668676, 2668686, 2668687, 2668689, 2668694, 2668699, 2668708,
                          2668712, 2668721, 2668722, 2668730, 2668731, 2668748, 2668756,
                          2668759, 2668762, 2668772, 2668779, 2668780, 2668790, 2668794,
                          2668797, 2668804, 2668805])
        self.assertEqual(count_Kprimes(3, 1019275, 1019722),
                         [1019275, 1019289, 1019290, 1019293, 1019301, 1019302, 1019303, 1019305, 1019308, 1019311,
                          1019314, 1019317, 1019319, 1019324, 1019332, 1019333, 1019334, 1019335, 1019338, 1019346,
                          1019355, 1019361, 1019366, 1019369, 1019371, 1019379, 1019389, 1019390, 1019391, 1019395,
                          1019401, 1019409, 1019414, 1019415, 1019417, 1019422, 1019427, 1019428, 1019429, 1019434,
                          1019435, 1019438, 1019447, 1019454, 1019455, 1019461, 1019465, 1019469, 1019476, 1019477,
                          1019478, 1019489, 1019492, 1019499, 1019505, 1019506, 1019511, 1019514, 1019515, 1019516,
                          1019518, 1019521, 1019522, 1019541, 1019542, 1019543, 1019548, 1019553, 1019557, 1019567,
                          1019570, 1019573, 1019579, 1019582, 1019583, 1019585, 1019596, 1019597, 1019598, 1019599,
                          1019603, 1019607, 1019609, 1019614, 1019615, 1019618, 1019621, 1019622, 1019626, 1019629,
                          1019630, 1019631, 1019635, 1019638, 1019641, 1019642, 1019643, 1019644, 1019645, 1019649,
                          1019654, 1019658, 1019659, 1019665, 1019669, 1019675, 1019678, 1019679, 1019685, 1019695,
                          1019698, 1019703, 1019705, 1019706, 1019708, 1019714, 1019716, 1019722])

    def test_kpuzzle(self):
        self.assertEqual(puzzle(138), 1)
        self.assertEqual(puzzle(143), 2)
        self.assertEqual(puzzle(1025), 393)

    def test_simple_pig(self):
        self.assertEqual(pig_it('Pig latin is cool'), "igPay atinlay siay oolcay")
        self.assertEqual(pig_it('Hello world !'), "elloHay orldway !")
        self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')

    def test_num_factorization(self):
        self.assertEqual(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")


if __name__ == '__main__':
    unittest.main()
