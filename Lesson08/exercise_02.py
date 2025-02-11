# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Debited {amount} from account no {self.account_no}")
        self.print_info()

    # credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount} to account no {self.account_no}")
        self.print_info()

    def print_info(self):
        print(f"Account No: {self.account_no}\tBalance: {self.balance}")


acc1 = Account(123456, 1000)
acc1.debit(500)
acc1.credit(200)
acc1.credit(200)
acc1.debit(100)
