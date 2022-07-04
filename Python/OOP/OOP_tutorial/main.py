# OOP class - 2th July

# define class


class Person:
    # self --> pointer to to class Person
    # if you define a function in class firt parameter always should be the self (pointer)
    # instead of self you can use other name like __init__(merve,name,.....)
    # if you create multiple __init__ it will consider the last one

    def __init__(self,name,surname,emailid,year_of_birth): # init is a inbuilt funct that allow to pass data to class
        self.name = name
        # self.name1 = name # namme's are not the same
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth=year_of_birth

    def age(self,current_year): # generic function
        return current_year-self.year_of_birth

merve_var= Person('merve','bayram','mervebdurna@gmailcom',1991)

print(merve_var.name)
print(merve_var.surname)


saban_var  = Person('saban','durna','xyz',123)
print(saban_var.emailid)

print(type(merve_var))
print(type(merve_var.name))

print(merve_var.name + merve_var.surname)

merve_age = merve_var.age(2022)
print(merve_age)


merve_age_1 = merve_var.age(2022)
print(merve_age_1)