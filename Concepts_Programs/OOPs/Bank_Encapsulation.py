class BankAccount:

    def __init__(self):
        self.amount =0
    def deposit(self,amount):
        self.amount += amount
    def _withdraw(self,amount):
        self.amount -= amount
    def __show_balance(self):
        print(f'Your updated amount is {self.amount}')
    def withdraw_it(self,amount):
        self._withdraw(amount=amount)
    def is_auth(self,auth):
        if auth:
            self.__show_balance()
        else:
            print(f'Access denied')

Hdfc = BankAccount()
Hdfc.deposit(2000)
#Hdfc._withdraw(500)
Hdfc.withdraw_it(1500)
Hdfc.is_auth(True)