# multi label inheritance

class bank():
    def bank_name(self):
        print("this will return bank name")
    def transaction(self):
        print("this function will return transaction_detail")

class bank_A(bank):
    def bank_A_to_bank_B(self):
        print("this will show yo all the transactions from bank_A to bank_B")

class bank_B(bank_A):
    pass


b_B = bank_B
b_B.bank_A_to_bank_B(b_B)
b_B.bank_name(b_B)

