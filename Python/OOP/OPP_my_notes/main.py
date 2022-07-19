from item import Item
from laptop import Laptop
Item.instantiate_from_csv()
print(Item.all)

item1 = Item("MyItem", 500)

item1.apply_increment(0.2)
print(item1.price)

item1.send_email()
# item1.__connect # we can't access unnecessary information abstraction example


laptop1 = Laptop("MyLaptop", 100) # polymorphism

laptop1.apply_discount()
print(laptop1.price)




