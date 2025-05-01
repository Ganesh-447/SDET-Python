class Person:

    def __init__(self,name,age):

        self.__name = name
        self.__age = age

    def get_name(self):

        return self.__name
    def set_name(self, name):
        self.__name = name
        print(f'the updated name is {self.__name}')

    def get_details(self):

        print(f'the details are {self.__name} {self.__age}')


a = Person("Ganesh",24)
a.get_details()
#a.__name = 'Suresh'
# print(a.__name)
print(a.get_name())

a.set_name('Lokesh')