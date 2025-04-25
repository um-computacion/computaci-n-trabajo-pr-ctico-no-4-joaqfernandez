import unittest
from src.fibonacci import fibonacci

class testFibonacci(unittest.TestCase):
    def test_es_fibonacci_1(self):
        n = 1
        resultado = fibonacci(n)
        self.assertEqual(resultado, 1)

    def test_es_fibonacci_0(self):
        n = 0
        resultado = fibonacci(n)
        self.assertEqual(resultado, 0)

    def test_es_fibonacci_4(self):
        n = 4
        resultado = fibonacci(n)
        self.assertEqual(resultado, 3)

    def test_es_fibonacci_8(self):
        n = 8
        resultado = fibonacci(n)
        self.assertEqual(resultado, 21)

    def test_es_fibonacci_31(self):
        n = 31
        resultado = fibonacci(n)
        self.assertEqual(resultado, 1346269)



if __name__ == '__main__':
    unittest.main()