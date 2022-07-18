class ineuron:
    __students = "data science"

    def students(self):
        print("print the class of students",ineuron.__students)


i = ineuron()
i.students()

# not accesible
# i.__students
print(i._ineuron__students)

# abstraction --> we hide __students variable behind the ineuro class