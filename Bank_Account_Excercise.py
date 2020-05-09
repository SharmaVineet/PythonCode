class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner: " + self.owner + "\n" + "Account Balance: " + "$" + str(self.balance)

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Deposit Accepted")

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount <= self.balance:
            self.balance -= withdrawal_amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")


acct1 = Account('Jose', 100)
print(acct1)
acct1.deposit(50)
acct1.deposit(150)
print(acct1)
acct1.withdraw(50)
acct1.withdraw(50)
acct1.withdraw(250)
print(acct1)
