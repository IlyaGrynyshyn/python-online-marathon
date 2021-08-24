import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:

    def __init__(self, product):
        self.product = product

    def get_total_price(self):
        dic = {}
        for i in range(len(self.product)):
            dic[self.product[i].price] = self.product[i].count

        lst = []

        for key, value in dic.items():
            item = key * value

            if 0 <= value < 5:
                lst.append(item)
            elif 5 <= value < 7:
                lst.append(item - ((item / 100) * 5))
            elif 7 <= value < 10:
                lst.append(item - ((item / 100) * 10))
            elif 10 <= value < 20:
                lst.append(item - ((item / 100) * 20))
            elif value == 20:
                lst.append(item - ((item / 100) * 30))
            elif value > 20:
                lst.append(item - ((item / 100) * 50))
        return sum(lst)


class CartTest(unittest.TestCase):

    def setUp(self):
        self.product1 = Product('p1', 10, 4)
        self.product2 = Product('p2', 100, 5)
        self.product3 = Product('p3', 200, 6)
        self.product4 = Product('p4', 300, 7)
        self.product5 = Product('p5', 400, 9)
        self.product6 = Product('p6', 500, 10)
        self.product7 = Product('p7', 1000, 20)

    def test_cart(self):
        self.assertEqual(Cart((self.product1, self.product2, self.product3,
                               self.product4, self.product5, self.product6, self.product7)).get_total_price(),
                         24785.0)
