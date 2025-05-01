class Person(object):


    def __init__(self,name,age):

        self.name = name
        self.age = age

    def details(self):
        print(f'the given object details are {self.name} ,{self.age}')


a =Person('Ganesh', 24)
b= Person('Saikumar', 28)
a.details()
b.details()
