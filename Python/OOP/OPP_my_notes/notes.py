import csv

item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1))  # str class
print(type(item1_price))  # int class
print(type(item1_quantity))  # int class
print(type(item1_price_total))  # int class


# ------------------Creating class------------------

class Item:
    # methods started with __ called as magic methods
    # self --> pointer for the object
    # instead of self you can use another term like my_self but not suggested

    # class attributes --> global for all instances, and you can access from the instance level as well

    pay_rate = 0.8  # the pay rate after %20  discount
    all = []  # to store all the object that belongs to class and access later

    def __init__(self, name: str, price: float, quantity: 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"  # error message
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # When you create a new object from the class Python automatically run __init__ method itself
        # print('I am created')
        # There are 2 type of attributes class and instance attributes.
        # Below attributes are the instance attributes means unique for the instance
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    # decorators -->  quick way to change the behaviour of the functions
    @classmethod
    def instantiate_from_csv(cls):  # we don't have items(self s) in csv format so we can't use method  this way, We need to convert this method to class method which we will be able to access class level.
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
        # We will count out the floats that are point zero
        # For i.e : 5.0,10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    # When to use staticmethod or classmethod
    # staticmethod --> This should do sth that has a relatioship with the class, but not something that must be unique per instance !
    # classmethod --> This should also do sth that has a relationship with the class, but usually , those are used to manipulate diffferent structures od data to instantiate objects, like we have done with csv, maybe from json etc
    # both can be called from instance level but not recommended

    def __repr__(self):  # helps to represent oject in a good way
        return f"Item('{self.name}', '{self.price}','{self.quantity}')"

    def calculate_total_price(self):  # self always should be the first parameter for the method
        return self.price * self.quantity

    def apply_discount(self):
        # here we use class level attribute for calculation
        # thats why when we assign new pay rate for the item1 it will still class oay_rate, we need to change it to the instence level
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate


# ------------------Creating Object or Instance------------------

# item1 = Item()  # same like creating string # str(abcd)
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 5
#
## At the beginning there was no relationship between item1, item1_price,... etc but now all attributes related to item.
## Let's check all of their datatypes again
# print(type(item1))  # item class  !! not str class anymore
# print(type(item1.price))  # int class
# print(type(item1.quantity))  # int class
#
# item2 = Item()  # same like creating string # str(abcd)
# item2.name = 'Laptop'
# item2.price = 1000
# item2.quantity = 2
#
# print(item1.calculate_total_price(item1.price,item1.quantity))
# print(item2.calculate_total_price(item2.price, item2.quantity))

# Above attributes creation is hard codded, we can solve this problem by passing attributes via __init__ constructer
# method while creating object
# dynamic attributes assigning with the help of __init__ function

item1 = Item('Phone', 100, 5)
# item2 = Item('Laptop', '1000', -2)  # the data type of the attributes  needs to be specified
item2 = Item('Laptop', 1000, 2)
item3 = Item('Kindle', 120, 4)

print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price())

print(item3.name)
print(item3.price)
print(item3.quantity)
print(item3.calculate_total_price())

# define new attribute
item2.has_numped = False

# access class attribute
print(Item.pay_rate)  # class level access

print(item1.pay_rate)  # object level access
print(item2.pay_rate)
print(item3.pay_rate)

print(Item.__dict__)  # all the attributes for class level
print(item1.__dict__)  # all the attributes for instance level

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7  # we can apply different discount by changing instance level parameter
item2.apply_discount()
print(item2.price)

print(Item.all)
for instance in Item.all:
    print(instance.name)

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.5))
print(Item.is_integer(7.0))
print(Item.is_integer(7))


# setter getter -->
# @property will give you control of what you would like to do when you get an attributr
# name.setter will give you control what you would like to do when you set an attribute


# 4 Principles of OOP
# Encapsulation : restricting the direct access to the some attributes
# for example we can't chane the price of item by accessing we can apply increment and discount methods to be able to change we encapsulated it


# Abstraction : only show necessary attributes and hide the unnecessary information
# for example if you want to send_email you just need to call send_email() method as a user,
# but in the background email sending has a lot of process like server connection, creating budy of the mail,


# Inheritance :  allows us to reuse code across our classes
# Phone inherited from Item class an all the attributes / methods of Item can be accessible via Phone

# Polymorphism : many forms of the function ,
# great example of this is len built_in function
# print(len('Merve')) # count the characters of string
# print(len['Merve', 'Bayram']) # count the number of list items
# same method but different behaviour
# one entity used with different object, for example applied_discount work with Phone and Item objects



