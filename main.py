import math
import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Перемножать можно только числа")
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Делить на 0 нельзя")
    return x / y

def power(x, y):
    if x == 0 and y < 0:
        raise ValueError("0 нельзя возводить в отрицательную степень")
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Корень можно брать лишь от положительных чисел")
    return math.sqrt(x)

def factorial(x):
    if not isinstance(x, int):
        raise TypeError("Факториал можно брать только от целых чисел")
    if x < 0:
        raise ValueError("Факториал можно брать лишь от положительных целых чисел")
    return math.factorial(x)

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(23, 6), 29)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(-7, -4), -11)

    def test_add_negative(self):
        with self.assertRaises(TypeError):
            add("три", 9)

    def test_subtract(self):
        self.assertEqual(subtract(14, 8), 6)
        self.assertEqual(subtract(-3, 5), -8)
        self.assertEqual(subtract(-7, -7), 0)

    def test_subtract_negative(self):
        with self.assertRaises(TypeError):
            subtract("шесть", 8)

    def test_multiply(self):
        self.assertEqual(multiply(12, 5), 60)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(-3, -3), 9)

    def test_multiply_negative(self):
        with self.assertRaises(TypeError):
            multiply("двадцать", 8)

    def test_divide(self):
        self.assertEqual(divide(15, 3), 5)
        with self.assertRaises(ValueError):
            divide(34, 0)

    def test_divide_negative(self):
        with self.assertRaises(TypeError):
            divide("семь", 1)

    def test_power(self):
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(-1, 5), -1)
        self.assertEqual(power(4, 0.5), 2)

    def test_power_negative(self):
        with self.assertRaises(ValueError):
            power(0, -3)

    def test_sqrt(self):
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(sqrt(0), 0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-25)

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_factorial_negative(self):
        with self.assertRaises(TypeError):
            factorial("пяти")

if __name__ == '__main__':
    unittest.main()