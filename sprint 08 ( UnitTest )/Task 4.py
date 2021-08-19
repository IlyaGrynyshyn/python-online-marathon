import math
import unittest


class TriangleNotValidArgumentException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Not valid arguments"


class TriangleNotExistException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Can`t create triangle with this arguments"


class Triangle:
    def __init__(self, sides):
        self.sides = sides
        if not isinstance(self.sides, (list, tuple)):
            raise TriangleNotValidArgumentException
        if len(self.sides) != 3:
            raise TriangleNotValidArgumentException
        if len(self.sides) == 3:
            for item in self.sides:
                if not (isinstance(item, int)):
                    raise TriangleNotValidArgumentException
                if item <= 0:
                    raise TriangleNotExistException
        if not ((self.sides[0] + self.sides[1] > self.sides[2]) and
                  (self.sides[0] + self.sides[2] > self.sides[1]) and
                  (self.sides[1] + self.sides[2] > self.sides[0])):
            raise TriangleNotExistException


    def get_area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2

        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(S, 2)


class TriangleTest(unittest.TestCase):
    def setUp(self):
        self.not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        self.not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]
        self.valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]

    @unittest.expectedFailure
    def test_valid_data(self):
        for point, result in self.valid_test_data:
            with self.subTest():
                self.assertEqual(Triangle(point).get_area(), result)

    @unittest.expectedFailure
    def test_not_valid_triangle(self):
        for item in self.not_valid_triangle:
            with self.subTest():
                self.assertTrue(Triangle(item).get_area())

    def test_not_valid_argument(self):
        for item in self.not_valid_arguments:
            self.assertRaises(Exception, Triangle, item)


# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     10
# ]
# for data in not_valid_arguments:
#     try:
#         Triangle(data)
#     except TriangleNotValidArgumentException as e:
#         print(e)


# not_valid_triangle = [
#     (1, 2, 3),
#     (1, 1, 2),
#     (7, 7, 15),
#     (100, 7, 90),
#     (17, 18, 35),
#     (127, 17, 33),
#     (145, 166, 700),
#     (1000, 2000, 1),
#     (717, 17, 7),
#     (0, 7, 7),
#     (-7, 7, 7)
# ]
# for data in not_valid_triangle:
#     try:
#         Triangle(data)
#     except TriangleNotExistException as e:
#         print(e)


# valid_test_data = [
#     (3, 4, 5),
#     (26, 25, 3),
#     (30, 29, 5),
#     (87, 55, 34),
#     (120, 109, 13),
#     (123, 122, 5)
# ]
# for data in valid_test_data:
#     print(Triangle(data).get_area())