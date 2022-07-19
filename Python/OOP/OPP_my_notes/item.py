import csv


class Item:


    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity= 0):

        assert price >= 0, f"Price {price} is not greater than or equal to zero!"  # error message
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.__name = name # encapsulation example
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}','{self.quantity}')"

    def calculate_total_price(self):  # self always should be the first parameter for the method
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value



    @property # DECORATOR TO MAKE READ-ONLY
    def read_only_name(self):
        return 'AAA'

    @property  # DECORATOR TO MAKE READ-ONLY, property can not be set so we will make it _name
    def name(self):
        # print( "you are trying to get ")
        return self.__name

    @name.setter
    def name(self, value):
        # print("you are trying to set")
        if len(value)>15:
            raise Exception("The name is too long.")
        else :
            self.__name = value

    @property
    def price(self):   # encapsulation example
        return self.__price

    def __connect(self, smpt_server): # private method just can call inside class
        pass

    def __prepare_body(self):
        return f"""
        Hello SomeOne,
        We have {self.name} {self.quantity} times.
        
        Regards. Merve
        
        """

    def __send(self):
        pass

    def send_email(self): # abstraction
        # send an email about the item
        self.__connect('qwee')
        self.__prepare_body()
        self.__send()