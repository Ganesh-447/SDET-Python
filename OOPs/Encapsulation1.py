class Password:

    def __init__(self, password):

        self.__password = password

    def get_password(self):
        return  self.__password

    def set_password(self, password):

        if len(password) > 6:
            self.__password = password
        else:
            print('the password length should be greater than six characters')

    def len_pass(self):

        print(f'the length of the password is {len(self.__password)}')


a = Password('Ganesh')
a.len_pass()
print(a.get_password())
a.set_password('Loki')
print(a.get_password())
a.len_pass()
