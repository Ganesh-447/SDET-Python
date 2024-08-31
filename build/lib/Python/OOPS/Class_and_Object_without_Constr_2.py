class Person(object):

    name = None
    age = None
    address = None

    def details(self):
        print(f'the details are {self.name} ,{self.age}, {self.address}')


a = input('enter your name for object 1 ')
b = int(input('enter your age for object 1 '))
c = input('enter your address for object 1 ')

d = input('enter your name for object 2 ')
e = int(input('enter your age for object 2'))
f = input('enter your address for object 2')

Anku = Person()
Ganesh = Person()

Anku.name = a
Anku.age = b
Anku.address = c

Ganesh.name = d

Ganesh.age = e

Ganesh.address =f

Anku.details()
Ganesh.details()






