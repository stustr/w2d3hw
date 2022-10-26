class Drink:
    def __init__(self, name, price, alcohol_level):
        self.name = name
        self.price = price
        self.alcohol_level = alcohol_level

    def __repr__(self) -> str:
        rep = f"Name is: {self.name}, price is {self.price} and alcohol level is {self.alcohol_level}"
        return rep

    

    
