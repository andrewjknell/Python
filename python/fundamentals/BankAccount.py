

# account1 = bankAccount(10,500)
# account2 = bankAccount(5,0)

# account1.deposit(1000)
# account1.deposit(1000)
# account1.deposit(500)
# account1.withdrawl(500)
# account1.yield_interst()
# account1.display_account_balance()

# account2.deposit(500)
# account2.deposit(5500)
# account2.withdrawl(200)
# account2.withdrawl(200)
# account2.withdrawl(2000)
# account2.withdrawl(200)
# account2.yield_interst()
# account2.display_account_balance()

class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account = bankAccount(int_rate = 2, balance = 0)
    def make_deposit(self, amount):
        self.account.deposit += amount
        return self
    def make_withdrawl(self, amount):
        self.account.withdrawl -= amount
        return self
    def display_user_balance(self):
        print('User: '+self.name + '\nBalance: ' + str(self.account))
        return self
    def transfer_money(self, to, amount):
        self.account.withdrawl(amount)
        to.account.deposit(amount)
        return self
    

class bankAccount:
    def __init__(self, int_rate, balance):
        self.int = int_rate
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

