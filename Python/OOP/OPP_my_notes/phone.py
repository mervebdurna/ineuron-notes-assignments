from item import Item


class Phone(Item):  # child class
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super functions to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )