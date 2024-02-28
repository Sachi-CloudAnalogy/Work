class bank_account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def withdraw(self):
        amount = int(input("Enter amount to withdraw ="))
        self.bal -= amount
        print("Left amount =", self.bal)

    def deposit(self):
        amount = int(input("Enter amount to deposit ="))
        self.bal += amount
        print("Left amount =", self.bal)

    def check_bal(self):
        print("Balance =", self.bal)

    def option(self, case):
        match case:
            case 1:
                return self.withdraw()
            case 2:
                return self.deposit()
            case 3:
                return self.check_bal()
            case default:
                return "Invalid !!"
        

print("WELCOME TO YOUR BANK !!")
acc_no = int(input("Enter account no : "))
balance = int(input("Current Balance : "))
acc1 = bank_account(balance, acc_no)

print("""Choose option :
      1. withdraw
      2. deposit
      3. check balance""")
case = int(input("Enter option : "))
acc1.option(case)
