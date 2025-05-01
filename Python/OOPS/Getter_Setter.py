class Person(object):

    def __init__(self,name,age):
        self.__name = name
        self.__age = age


    def Setter(self,name,age):

        if name == 'ganesh' and age == 25:
            print('you cant set the name and age')
        else:
            self.__name = name
            self.__age = age
    def getter(self):

        print(f'the name is {self.__name},{self.__age}')

a = Person('ganesh',24)
a.Setter('sai',25)
a.getter()

