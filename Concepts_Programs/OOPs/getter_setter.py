#Encapsulation
class Person:


    def __init__(self,name,age,height):
        self.__name = name
        self.__age = age
        self.height=height

    def get_name(self):
        return self.__name
    def set_name(self,name):
        if name == 'Ganesh':
            print("Don't set the name")
        else:
            self.__name = name


    def display_details(self):
        print(f'The person details are {self.__name} and age is {self.__age}')

person1=Person('Ramu',25,5.6)
person1.display_details()

person1.set_name('Ganesh')
print(person1.height)
#print(person1.__name)
print(person1.get_name())


person1.display_details()