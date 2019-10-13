class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print('User: '+self.name + '\nBalance: ' + str(self.account_balance))
        return self
    def transfer_money(self, to, amount):
        self.make_withdrawl(amount)
        to.make_deposit(amount)
        return self


andrew = User('Andrew', 'andrewjk@yahoo.com')
andrew.make_deposit(500).make_deposit(500).make_deposit(100).make_withdrawl(600).display_user_balance()

nate = User('Nate', 'nate@yahoo.com')
nate.make_deposit(1200).make_deposit(100).make_withdrawl(350).display_user_balance()

kyle = User('Kyle', 'kyle@yahoo.com')
kyle.make_deposit(5600).make_withdrawl(3000).make_withdrawl(100).display_user_balance()

andrew.transfer_money(nate, 500)
nate.display_user_balance()
andrew.display_user_balance()


