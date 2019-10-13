from bankAccount import BankAccount 
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount( int = 5, balance = 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self
    def display_user_balance(self):
        print('User: '+self.name + '\nBalance: ' + str(self.account.balance))
        return self
    def transfer_money(self, to, amount):
        self.account.withdrawl(amount)
        to.account.deposit
        return self

andrew = User('andrew','andrew@yahoo.com')
andrew.make_deposit(400)
andrew.display_user_balance()
    



