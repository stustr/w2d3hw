import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink_tennants = Drink("Tennants", 3.50, 1)
        self.drink_vodka = Drink("Vodka", 1.0, 2)
        self.drink_cider = Drink("Cider", 3.50, 1)
        self.drink_shandy = Drink("Shandy", 1.50, 0.5)
        self.drink_coke = Drink("Coke", 0.50, 0)

    def test_drink_has_name(self):
        self.assertEqual("Tennants", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(1, self.drink.alcohol_level)