class Bank(object):


    def __init__(self):
        self.balance = 0



    def deposit(self,amount):
        self.balance += amount

    def _withdraw(self,amount):
        self.balance -= amount

    def __display_balance(self):
        print(f'current balance is {self.balance}')

    def show_balance_auth(self,isAuth):
        if isAuth:
            self.__display_balance()
        else:
            print('you are not authorized')

    def withdraw_balance(self,amount):
        self._withdraw(amount= amount)


HDFC = Bank()
HDFC.deposit(1000)
HDFC.withdraw_balance(100)
HDFC.show_balance_auth(True)
