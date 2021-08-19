import unittest


class Worker:
    def __init__(self, name, salaty = 0):
        self.name = name
        self.salary = salaty
        self.tax = 0
        if salaty < 0:
            raise ValueError

    def get_tax_value(self):
        if 1000 <= self.salary < 3000:
            self.tax = (self.salary - 1000) * 0.1
            return float(self.tax)
        elif 3001 <= self.salary <= 5000:
            self.tax = (3001 - 1001) * 0.1 + (self.salary - 3001) * 0.15

        elif 5001 <= self.salary <= 10000:
            self.tax = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (self.salary - 5001) * 0.21
        elif 10001 <= self.salary <= 20000:
            self.tax = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (10001 - 5001) * 0.21 + (self.salary - 10001) * 0.3
        elif 20001 <= self.salary <= 50000:
            self.tax = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (10001 - 5001) * 0.21 + (20001 - 10001) * 0.3 + (
                        self.salary - 20001) * 0.4
        elif self.salary > 50000:
            self.tax = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (10001 - 5001) * 0.21 + (20001 - 10001) * 0.3 + (
                        50000 - 20001) * 0.4 + (self.salary - 50000) * 0.47
        return float(round(self.tax))


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker1 = Worker('Alex', 500)
        self.worker2 = Worker('Steve', 2800)
        self.worker3 = Worker('Ilya', 4500)
        self.worker4 = Worker('Andew', 7777)
        self.worker5 = Worker('Artem', 15000)
        self.worker6 = Worker('Vitaly', 25000)
        self.worker7 = Worker('Rey', 140000)

    def test_worket1(self):
        self.assertEqual(self.worker1.get_tax_value(), 0)

    def test_worker2(self):
        self.assertEqual(self.worker2.get_tax_value(), 180)

    def test_worker3(self):
        self.assertEqual(self.worker3.get_tax_value(), 425)

    def test_worker4(self):
        self.assertEqual(self.worker4.get_tax_value(), 1083)

    def test_worker5(self):
        self.assertEqual(self.worker5.get_tax_value(), 3050)

    def test_worker6(self):
        self.assertEqual(self.worker6.get_tax_value(), 6550)

    def test_worker7(self):
        self.assertEqual(self.worker7.get_tax_value(), 58850)

    @unittest.expectedFailure
    def test_negative_number(self):
        self.assertEqual(Worker('Ilya',-35000).get_tax_value(),0)