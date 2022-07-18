class ineuron:

    def students(self):
        print("print the details of all the students")

    def achivers(self):
        print("print the details list of all the achivers")

    def hall_of_fame(self):
        print("print everyone form hall of fame")

class ineuro_vision(ineuron):
    #re-define or overwrite already exist method whichinherit from parent class
    def students(self):
        print('these are the filtered student list')


iv = ineuro_vision()
iv.students()