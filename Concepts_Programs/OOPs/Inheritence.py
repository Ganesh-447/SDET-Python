class Animal:

    def speak(self):
        print('Animal is speaking')

class Dog(Animal):

    def bark(self):
        print('Bow, Bow')


d=Dog()
d.bark()
