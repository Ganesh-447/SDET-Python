class Person:

    def __init__(name1,age,gender):
        a.name = name1
        a.age = age
        self.gender = gender

    def person_address(self):
        print(f" The address of the given person is {self.name} {self.age} {self.gender}")


Ganesh = Person('Ganesh',24,'male')
Ganesh.person_address()

Sai = Person('Sai Kumar',29,'male')
Sai.person_address()
