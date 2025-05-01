class MyClass:


    def __init__(self):
        self.public_var = 22
        self._protected_var = 12
        self.__private_var = 15


    def public_method(self):
        print("This is a public method")


a = MyClass()
print(a.public_var)
print(a._protected_var)
print(a.__private_var)