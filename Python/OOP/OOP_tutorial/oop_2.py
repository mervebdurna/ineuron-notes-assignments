# OOP class - 2th July

# define class


class Person:
    def __init__(self,name,surname,emailid,year_of_birth): # init is a inbuilt funct that allow to pass data to class
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth=year_of_birth


merve_var= Person('merve','bayram','mervebdurna@gmailcom',1991)

print(merve_var.name)
print(merve_var.surname)