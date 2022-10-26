import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Struan", 33, 100.00, 5)
        self.customer_2 = Customer("Rory", 26, 3.50, 0)
        self.customer_3 = Customer("Ed", 30, 1000, 10)

    def test_customer_has_name(self):
        self.assertEqual("Struan", self.customer_1.name)

    def test_customer_has_dosh(self):
        self.assertGreaterEqual(3.50, self.customer_2.cash)
