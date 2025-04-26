import unittest
from flatten import flatten



class TestFlatten(unittest.TestCase):

    def test_flatten_lista_simple (self): 
        lista = [1, 2, 3]
        resultado = [1, 2, 3]
        self.assertEqual(flatten(lista), resultado)
    
    def test_flatten_lista_anidada (self):
        lista = [1, 2, 3, [4, 5,[6,7]], 8, 9]
        resultado = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_flatten_lista_compleja (self):
        lista = [ 1, 2, 3, {'hola': 4, 'mundo': [5, 6]}, 7, 8]
        resultado = [1, 2, 3, 'hola', 4, 'mundo', 5, 6, 7, 8]
        self.assertEqual(flatten(lista), resultado)

if __name__ == '__main__':
    unittest.main()