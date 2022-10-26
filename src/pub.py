class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {}
        self.foods = {}
        self.total_value = 0

    def age_check(self, customer):
        return customer.age >= 18

    def drunk_check(self, customer):
        return customer.drunkeness <= 10

    def stock_bar(self, stock_drink, quantity):
        if stock_drink.name not in self.drinks:
            self.drinks[stock_drink.name] = {
                "price": stock_drink.price,
                "alcohol level": stock_drink.alcohol_level,
                "quantity": quantity,
            }
        else:
            self.drinks[stock_drink.name]["quantity"] += quantity

    def stock_foods(self, stock_food, quantity):
        if stock_food.name not in self.foods:
            self.foods[stock_food.name] = {
                "price": stock_food.price,
                "rejuvenation level": stock_food.rejuvenation_level,
                "quantity": quantity,
            }
        else:
            self.foods[stock_food.name]["quantity"] += quantity

    def check_stock_value(self):
        for drink in self.drinks:
            price = self.drinks[drink]["price"]
            quantity = self.drinks[drink]["quantity"]
            ind_val = price * quantity
            self.total_value += ind_val

    def increase_till(self, amount):
        self.till += amount

    def check_stock_drink(self, chosen_drink):
        return chosen_drink in self.drinks

    def check_stock_food(self, chosen_food):
        return chosen_food in self.foods

    def check_zero_alcohol_level(self, chosen_drink):
        return self.drinks[chosen_drink]["alcohol level"] == 0

    def sell_drink(self, customer, chosen_drink):
        price = self.drinks[chosen_drink]["price"]
        alc_level = self.drinks[chosen_drink]["alcohol level"]
        if self.check_stock_drink(chosen_drink) and customer.cash > price:
            if self.age_check(customer) and self.drunk_check(customer):
                self.increase_till(price)
                self.drinks[chosen_drink]['quantity'] -= 1
                customer.buy_drink(price, alc_level)
            elif self.check_zero_alcohol_level(chosen_drink):
                self.increase_till(price)
                self.drinks[chosen_drink]['quantity'] -= 1
                customer.buy_drink(price, alc_level)

    def sell_food(self, customer, chosen_food):
        price = self.foods[chosen_food]["price"]
        rej_level = self.foods[chosen_food]["rejuvenation level"]

        if self.check_stock_food(chosen_food) and customer.cash > price:
            self.increase_till(price)
            self.foods[chosen_food]['quantity'] -= 1
            customer.buy_food(price, rej_level)
