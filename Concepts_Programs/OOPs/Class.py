# class, #object

class Person:
    name = None
    age = None
    gender = None
    weight = None

    def talk(self):
        print('Talk')

    def sleep(self):
        print('Sleep')

    def walk(self):
        return "I'm walking"

Ganesh_Object = Person()
Ganesh_Object.name = "Ganesh"
Ganesh_Object.age = 25
Ganesh_Object.gender="Male"
Ganesh_Object.weight = 79

Ram_Object = Person()
Ram_Object.name='Ram'

print(Ganesh_Object)
print(Ram_Object)