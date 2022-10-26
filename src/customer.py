from src.pub import Pub
class Customer:
    def __init__(self, name, age, cash, drunkeness):
        self.name = name
        self.age = age
        self.cash = cash
        self.drunkeness = drunkeness

    def buy_drink(self, chosen_drink):
        if self.pub.drinks.chosen_drink.price <= self.cash:
            self.cash -= chosen_drink.price
            return True

