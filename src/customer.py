class Customer:
    def __init__(self, name, age, cash, drunkeness):
        self.name = name
        self.age = age
        self.cash = cash
        self.drunkeness = drunkeness

    def buy_drink(self, price, alc_level):
        self.cash -= price
        self.drunkeness += alc_level
        
    def buy_food(self, price, rej_level):
        self.cash -= price
        self.drunkeness -= rej_level
