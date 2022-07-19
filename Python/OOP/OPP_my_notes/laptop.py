from item import Item


class Laptop(Item):  # child class
    pay_rate = 0.7 # we modified the pay rate for the apply_discount method
    def __init__(self, name: str, price: float, quantity=0):
        # call to super functions to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
