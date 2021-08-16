import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:

    def __init__(self):
        self.cart = []
        self.total_price = 0
        self.product_count = 0
        self.discount = 0

    def add_product(self, product):
        try:
            if type(product.name) is str:
                self.cart.append(product)
                self.total_price += product.price
                self.product_count += product.count
        except:
            raise ValueError

    def calculate_discount(self):
        if 5 <= self.product_count < 7:
            self.discount = 5
        elif 7 <= self.product_count < 10:
            self.discount = 10
        elif 10 <= self.product_count < 20:
            self.discount = 20
        elif self.product_count == 20:
            self.discount = 30
        elif self.product_count > 20:
            self.discount = 50
        return self.total_price - ((self.total_price / 100) * self.discount)


class CartTest(unittest.TestCase):
    cart = Cart()
    product1 = Product('Laptop', 20000, 10)
    product2 = Product('Smartphone', 10000, 30)
    product3 = Product('Monitor', 5000, 6)
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    def test_product_count(self):
        self.assertEqual(self.cart.product_count, 46)

    def test_product_total_price(self):
        self.assertEqual(self.cart.total_price, 35000)

    def test_add_product_values(self):
        self.assertRaises(ValueError, self.cart.add_product, 12314)

    def test_calculate_discount(self):
        self.assertEqual(self.cart.calculate_discount(), 17500)
