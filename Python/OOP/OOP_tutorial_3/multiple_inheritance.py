# multi label inheritance

class bank():
    def bank_name(self):
        print("this will return bank name")
    def transaction(self):
        print("this function will return transaction_detail")
    def test(self):
        print("this is a test method from bank class")


# bank and bank_A are two  independent
class bank_A():
    def bank_A_to_bank_B(self):
        print("this will show yo all the transactions from bank_A to bank_B")
    def test(self): # same method with bank class
        print("this is a test method from bank_A class")


#bank_B inherit 2 classes
class bank_B(bank,bank_A):
    pass


class bank_C(bank_A,bank): # inherit bank_A first, by doing that if there is a conflict between two class method this class will consider first class method
    pass

b_B = bank_B
b_B.bank_A_to_bank_B(b_B)
b_B.bank_name(b_B)
b_B.test(b_B) # test method comes from bank class NOT from bank_B


b_C = bank_C
b_C(b_C) # test method comes from bank_A class NOT from bank because we inherit bank_A and than bank class while creating bank_C class

# one class can be inherit from more than 2 classes like 3, 4,..