import unittest

class Calculator:
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Деление на ноль невозможно")
        return x / y

# Тестовые кейсы
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_multiply(self):
        result = self.calculator.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calculator.divide(8, 4)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()

