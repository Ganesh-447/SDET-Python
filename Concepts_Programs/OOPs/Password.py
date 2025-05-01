#Encapsulation.
class Password:

    def __init__(self,password):
        self.__password = password

    def get_password(self,auth):
        if auth:
            print(self.__password)
        else:
            print('not authorized')

    def set_password(self,password):
        if len(password) > 9:
            self.__password = password
        else:
            print(f'{password} is weak')

    def print_len(self):
        print(f'length of the password is {len(self.__password)}')



p1=Password("Anku@123")
p1.print_len()
p1.get_password(True)
p1.set_password("alkdj")
