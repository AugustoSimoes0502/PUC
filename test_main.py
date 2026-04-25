import unittest
from app import soma, subtrai, multiplica, divide, potencia

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtrai(self):
        self.assertEqual(subtrai(10, 5), 5)

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
