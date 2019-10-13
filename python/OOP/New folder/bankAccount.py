class BankAccount:
    def __init__(self, int, balance):
        self.int = int
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_account_balance(self):
        print('User: '+'' + '\nBalance: ' + str(self.balance))
        return self
    def yield_interst(self):
        self.balance += (self.balance*(self.int/100))


