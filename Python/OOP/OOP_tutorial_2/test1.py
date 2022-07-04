from Utils.util1 import person2

obj = person2("sudhansu " , "kumar" , 345345)
print(obj.yob1)

class person1 :
    def __init__(self , name ,surname , yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

sudh = person1("sudhanshu" , "kumar" , 1990)
print(sudh._name1)
print(sudh._person1__surname1)

# --name --> private variable, whenever you call it add _classname__name. ex : _person__name2
# -name --> protected
# the system not recommend the name for private end proected name just give public one