class Bank:

    def __init__(self):

        self.account_balance = 0

    def deposit_amount(self, deposit_amount):

        self.account_balance += deposit_amount
        print(f'Your current balance after adding {deposit_amount} is {self.account_balance}')

    def _withdraw(self, withdraw_amount):

        if withdraw_amount >= 100:
          self.account_balance -= withdraw_amount
          print(f'Your current balance after withdrawing {withdraw_amount} is {self.account_balance}')
        else:
            print(f'please enter the withdraw amount more than or equal to 100')

    def withdraw_option(self, amount):
        self._withdraw(withdraw_amount=amount)

    def __display_balance(self):
        print(f"Your remaining balance is {self.account_balance}")

    def is_auth(self, auth):

        if auth:
            self.__display_balance()
        else:
            print(f'Your Authentication failed')


Hdfc = Bank()
Hdfc.deposit_amount(50000)
Hdfc.withdraw_option(90)
Hdfc.is_auth(True)
