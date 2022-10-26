import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer
class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Moe's Bar", 1000.00)

        self.customer_1 = Customer("Struan", 33, 100.00, 5)
        self.customer_2 = Customer("Rory", 12, 3.50, 0)
        self.customer_3 = Customer("Ed", 30, 1000, 10)
        self.customer_4 = Customer("Bob", 12, 1000, 0)

        self.pub.stock_bar(Drink("Tennants", 3.50, 1, 10))
        self.pub.stock_bar(Drink("Vodka", 1.0, 2))
        self.pub.stock_bar(Drink("Cider", 3.50, 1))
        self.pub.stock_bar(Drink("Shandy", 1.50, 0.5))
        self.pub.stock_bar(Drink("Coke", 0.50, 0))
    
    def test_pub_has_name(self):
        self.assertEqual("Moe's Bar", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(1002.50, self.pub.till)

    
    def test_stock_the_pub(self):
        # self.pub.stock_bar(Drink("Tennants", 3.50, 1))
        self.assertEqual(5,len(self.pub.drinks))
        
        print(self.pub.drinks)


    def sell_drink_test(self):
        self.pub.sell_drink(self.customer_1,"Tennants")
        self.assertEqual(1003.50,self.pub.till)
        self.assertEqual(96.50,self.customer_1.cash)

    def sell_drink_test_drunk_customer(self):
        self.pub.sell_drink(self.customer_3,"Tennants")
        self.assertEqual(1003.50,self.pub.till)
        self.assertEqual(1000.00,self.customer_3.cash)

    def sell_drink_test_underage_customer(self):
        self.pub.sell_drink(self.customer_2, "Tennants")
        self.pub.sell_drink(self.customer_4, "Coke")
        self.assertEqual(1004.00, self.pub.till)
        self.assertEqual(3.50, self.customer_3.cash)
        self.assertEqual(999.50, self.customer_4.cash)

   

    