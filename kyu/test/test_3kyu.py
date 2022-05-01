import unittest
import time
from .._3kyu.metaclasses_simple_django_models import *
from .._3kyu.binomial_expansion import expand
from .._3kyu.million_fibonacci import fib
from .._3kyu.closest_pair import closest_pair

default_date = datetime.datetime(2000, 1, 1, 0, 0)


class SimpleDjangoModelTestCase(unittest.TestCase):
    class User(Model):
        first_name = CharField(max_length=30, default='Adam')
        last_name = CharField(max_length=50)
        email = EmailField()
        is_verified = BooleanField(default=False)
        date_joined = DateTimeField(auto_now=True, default=default_date)
        age = IntegerField(min_value=5, max_value=120, blank=True)

    def test_date_time_field(self):
        date = DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0))
        self.assertIsInstance(date.default, datetime.datetime)
        t1 = date.default
        time.sleep(1)
        t2 = date.default
        self.assertEqual(t1, t2)
        date = DateTimeField(auto_now=True)
        self.assertIsInstance(date.default, datetime.datetime)

    def test_basic(self):
        self.assertFalse(hasattr(self.User, 'first_name'))
        user1 = self.User()
        self.assertEqual(user1.first_name, 'Adam')
        user1.first_name = 'adam'
        self.assertEqual(user1.first_name, 'adam')
        self.assertEqual(user1.last_name, None)
        self.assertEqual(user1.is_verified, False)

        user = self.User()
        user.email = 'adam@example.com'
        self.assertEqual(user.email, 'adam@example.com')

        user = self.User(first_name='Liam', last_name='Smith', email='liam@example.com')
        self.assertEqual(user.first_name, 'Liam')
        self.assertEqual(user.date_joined, default_date)
        self.assertEqual(user.last_name, 'Smith')
        self.assertEqual(user.email, 'liam@example.com')

    def test_failure_assign(self):
        user = self.User(first_name='Liam', last_name='Smith', email='liam@example.com')
        self.assertTrue(user.validate())
        user.age = 999
        with self.assertRaises(ValidationError):
            user.validate()

    def test_validation(self):
        field = CharField()
        field.value = "aa"
        field.validate()

    def test_dif_data(self):
        user1 = self.User(first_name="John", last_name="Doe")
        user2 = self.User(first_name="Somebody", last_name="Else")

        self.assertNotEqual(user1.first_name, user2.first_name)
        self.assertNotEqual(user1.last_name, user2.last_name)


class Kata3TestCase(unittest.TestCase):
    def test_closest_pair(self):
        points = (
            (2, 2),  # A
            (2, 8),  # B
            (5, 5),  # C
            (6, 3),  # D
            (6, 7),  # E
            (7, 4),  # F
            (7, 9)  # G
        )
        expected = ((6, 3), (7, 4))

        self.assertIn(closest_pair(points), expected)

    def test_millionth_fibonacci(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(1000),
                         43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)

    def test_binomial_expansion(self):
        self.assertEqual(expand("(-c-11)^1"), '-c-11')
        self.assertEqual(expand("(-q-8)^3"), '-q^3-24q^2-192q-512')
        self.assertEqual(expand("(-h-16)^3"), "h^3-48h^2-768h-4096")
        self.assertEqual(expand("(-k-13)^3"), "-k^3-39k^2-507k-2197")
        self.assertEqual(expand("(x+1)^0"), "1")
        self.assertEqual(expand("(x+1)^1"), "x+1")
        self.assertEqual(expand("(x+1)^2"), "x^2+2x+1")
        self.assertEqual(expand("(x-1)^0"), "1")
        self.assertEqual(expand("(x-1)^1"), "x-1")
        self.assertEqual(expand("(x-1)^2"), "x^2-2x+1")
        self.assertEqual(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
        self.assertEqual(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
        self.assertEqual(expand("(7x-7)^0"), "1")
        self.assertEqual(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
        self.assertEqual(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
        self.assertEqual(expand("(-7x-7)^0"), "1")


if __name__ == '__main__':
    unittest.main()
