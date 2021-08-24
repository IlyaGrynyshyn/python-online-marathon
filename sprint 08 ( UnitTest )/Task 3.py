import math
import unittest


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError
    d = (b ** 2) - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        x = (-b / 2 * a)
        return x
    else:
        x1 = ((-b + math.sqrt(d)) / (2 * a))
        x2 = ((-b - math.sqrt(d)) / (2 * a))
        return x1, x2


class QuadraticEquationTest(unittest.TestCase):

    def test_without_answer(self):
        self.assertEqual(quadratic_equation(10, 2, 2), None)
        self.assertEqual(quadratic_equation(100, 20, 2), None)
        self.assertEqual(quadratic_equation(89, 12, 3), None)
        self.assertEqual(quadratic_equation(144, 24, 24), None)

    def test_with_one_answer(self):
        self.assertEqual(quadratic_equation(5, 10, 5), -25)
        self.assertEqual(quadratic_equation(1, 4, 4), -2)
        self.assertEqual(quadratic_equation(5, -10, 5), 25)
        self.assertEqual(quadratic_equation(1, 2, 1), -1)

    def test_with_two_answer(self):
        self.assertEqual(quadratic_equation(2, 7, -30), (2.5, -6.0))
        self.assertEqual(quadratic_equation(1, 1, -12), (3, -4))
        self.assertEqual(quadratic_equation(1, 3, -10), (2, -5))
        self.assertEqual(quadratic_equation(1, -70, 600), (60, 10))

    def test_value(self):
        self.assertRaises(ValueError, quadratic_equation, 0, 2, 2)
        self.assertRaises(ValueError, quadratic_equation, 0, 144, 256)
        self.assertRaises(ValueError, quadratic_equation, 0, 2122, 333)
        self.assertRaises(ValueError, quadratic_equation, 0, 6666, 9999)
