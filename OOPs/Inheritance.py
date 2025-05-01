class Animal:

    def speak(self):
        print('I can speak')


class Dog(Animal):

    def speak(self):
        print('bow bow')

a = Dog()
a.speak()
