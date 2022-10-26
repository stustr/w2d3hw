import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Moe's Bar", 1000.00)

        self.customer_1 = Customer("Struan", 33, 100.00, 5)
        self.customer_2 = Customer("Rory", 12, 3.50, 0)
        self.customer_3 = Customer("Ed", 30, 1000, 11)
        self.customer_4 = Customer("Bob", 12, 1000, 0)

        self.pub.stock_bar(Drink("Tennants", 3.50, 1), 10)
        self.pub.stock_bar(Drink("Vodka", 1.0, 2), 10)
        self.pub.stock_bar(Drink("Cider", 3.50, 1), 20)
        self.pub.stock_bar(Drink("Shandy", 1.50, 0.5), 10)
        self.pub.stock_bar(Drink("Coke", 0.50, 0), 10)
        self.pub.stock_bar(Drink("Coke", 0.50, 0), 10)

        self.pub.stock_foods(Food("Pizza", 8, 3), 10)
        self.pub.stock_foods(Food("Burger", 10, 2), 10)
        self.pub.stock_foods(Food("Salad", 8, 1), 10)

    def test_pub_has_name(self):
        self.assertEqual("Moe's Bar", self.pub.name)

    def test_age_check(self):
        self.assertEqual(True, self.pub.age_check(self.customer_1))

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(1002.50, self.pub.till)

    def test_stock_bar(self):
        self.assertEqual(5, len(self.pub.drinks))

    def test_check_stock_drink(self):
        self.assertEqual(True, self.pub.check_stock_drink("Coke"))

    def test_check_zero_alcohol_level(self):
        self.assertEqual(True, self.pub.check_zero_alcohol_level("Coke"))

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer_1, "Tennants")
        self.assertEqual(1003.50, self.pub.till)

    def test_sell_drink_drunk_customer(self):
        self.pub.sell_drink(self.customer_3, "Tennants")
        self.assertEqual(1000.00, self.pub.till)
        self.assertEqual(1000.00, self.customer_3.cash)

    def test_sell_drink_underage_customer(self):
        self.pub.sell_drink(self.customer_2, "Tennants")
        self.pub.sell_drink(self.customer_4, "Coke")
        self.assertEqual(1000.50, self.pub.till)
        self.assertEqual(3.50, self.customer_2.cash)
        self.assertEqual(999.50, self.customer_4.cash)

    def test_sell_food(self):
        self.pub.sell_food(self.customer_1, "Pizza")
        self.assertEqual(2, self.customer_1.drunkeness)
        print(self.pub.foods)
