
class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.total_value = 0
        
    #     return self.drinks

        # self.drink_tennants = Drink("Tennants", 3.50, 1)
        # self.drink_vodka = Drink("Vodka", 1.0, 2)
        # self.drink_cider = Drink("Cider", 3.50, 1)
        # self.drink_shandy = Drink("Shandy", 1.50, 0.5)
        # self.drink_coke = Drink("Coke", 0.50, 0)

    def age_check(self, customer):
        return customer.age

    def drunk_check(self,customer):
        return customer.drunkeness <= 10

    def stock_bar(self, stock_drink):
        self.drinks.append(stock_drink)
        
    def check_stock_value(self):
        for drink in self.drinks:
            self.total_value += drink.price


    def increase_till(self, amount):
        self.till += amount

    def check_stock(self,chosen_drink):
        for drink in self.drinks:
            if chosen_drink == self.drinks.name:
                return True

    def check_zero_alcohol_level(self, chosen_drink):
        for drink in self.drinks:
            if chosen_drink.alcohol_value == 0:
                return True
        
        self.pub.drinks.alcohol_level

    def sell_drink(self, customer, chosen_drink):
        if self.age_check(customer) >= 18 and self.drunk_check(customer):
            if self.check_stock(chosen_drink):
                if self.buy_drink(chosen_drink):
                    self.increase_till(chosen_drink.price)
        elif self.check_zero_alcohol_level(chosen_drink):
            if self.check_stock(chosen_drink):
                if self.buy_drink(chosen_drink):
                    self.increase_till(chosen_drink.price)

            # increase_till(drink.price) increase the pub till based on customer requested drink
            # customer.
            # call customer function to decrease customer cash