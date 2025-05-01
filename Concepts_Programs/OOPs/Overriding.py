#Overriding  - Same name in parent and child.
#child always override the  parent methods.
#super() will call parent class.

class Animal:

    def sound(self):
        print('Animal Sound')

class Dog(Animal):

    def sound(self):
        super().sound()   #stops child class to override the method of parent class.parent class method calls
        print('Dog Sound')


dog=Dog()
dog.sound()