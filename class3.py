class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def debit(self):
        amount = int(input("Enter amount to debit ="))
        self.bal -= amount
        print("Left amount =", self.bal)

    def credit(self):
        amount = int(input("Enter amount to credit ="))
        self.bal += amount
        print("Left amount =", self.bal)

    def show(self):
        print("Balance =", self.bal)   


acc1 = Account(1000, 11)
print(acc1.bal)
print(acc1.acc)
acc1.debit()
acc1.credit()
acc1.show()

