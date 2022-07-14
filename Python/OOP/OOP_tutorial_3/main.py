# oop concept day 3 notes.
# Inhetritence

class car() :

    def __init__(self,engine_type,body_type,model,brand):
        self.engine_type = engine_type
        self.body_type = body_type
        self.model = model
        self.brand = brand

    def millage():
        print("this is millage of the car")


class toyota(car):
    pass

c = car('v6','sedan','toyota','auris')
print(c)

t = toyota(c.engine_type,c.body_type,'toyota','auris')
print(t)

