import unittest

from src.factorial import factorial, factorial_recursivo, factorial_no_recursivo


class TestFactorial(unittest.TestCase):

    def test_con_8(self):
        n = 8

        result = factorial_recursivo(n)

        self.assertEqual(result, 40320)

    def test_with_0(self):
        n = 0

        result = factorial_no_recursivo(n)

        self.assertEqual(result, 1)

    def test_with_1(self):
        n = 1

        result = factorial_no_recursivo(n)

        self.assertEqual(result, 1)

    def test_with_more_than_1(self):
        n = 2

        result = factorial_no_recursivo(n)

        self.assertEqual(result, 2)

    def test_with_20(self):
        n = 20

        result = factorial_no_recursivo(n)

        self.assertEqual(result, 2432902008176640000)


if __name__ == '__main__':
    unittest.main()