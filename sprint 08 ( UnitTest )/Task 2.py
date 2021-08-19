import unittest

def divide(num_1,num_2):
    return float(num_1)/ num_2

class DivideTest(unittest.TestCase):

    def test_check_number(self):
        self.assertEqual(divide(6.0,2) , 3)
        self.assertEqual(divide(10.0, 5), 2)
        self.assertEqual(divide(100.0, 50), 2)
        self.assertEqual(divide(90.0, 30), 3)

    def test_value(self):
        self.assertRaises(TypeError,divide, 'two' )
        self.assertRaises(TypeError, divide, 10+2j )
        self.assertRaises(TypeError, divide, [42])
        self.assertRaises(TypeError, divide, '[36,12]')
        self.assertRaises(TypeError, divide, True)

    def test_zerodivision(self):
        self.assertRaises(ZeroDivisionError,divide, 1,0)

