class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account = bankAccount(int_rate = 2, balance = 0)
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print('User: '+self.name + '\nBalance: ' + str(self.account_balance))
        return self
    def transfer_money(self, to, amount):
        self.withdrawl(amount)
        to.deposit(amount)
        return self


andrew = User('Andrew', 'andrewjk@yahoo.com')
andrew.deposit(500).deposit(500).deposit(100).withdrawl(600).display_user_balance()

nate = User('Nate', 'nate@yahoo.com')
nate.deposit(1200).deposit(100).withdrawl(350).display_user_balance()

kyle = User('Kyle', 'kyle@yahoo.com')
kyle.deposit(5600).withdrawl(3000).withdrawl(100).display_user_balance()

andrew.transfer_money(nate, 500)
nate.display_user_balance()
andrew.display_user_balance()


