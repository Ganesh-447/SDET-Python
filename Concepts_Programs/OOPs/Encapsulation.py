#Encapsulation - Attributes , Methods. #Visibility

#Public , Private , Protected.


class Myclass:

    def __init__(self):
        self.public_var = 10
        self._protected_var = 12
        self.__private_var = 15

    def public_method(self):
        print('this is public method')
        print(f'Calling this private method from public method {self.__private_var}')


obj=Myclass()
obj.public_method()
#print(obj.public_var)
