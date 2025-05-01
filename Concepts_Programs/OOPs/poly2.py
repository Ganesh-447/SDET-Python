

class Animal:

    def sound(self):
        return 'this is sound of animal'
class Dog(Animal):

    def sound(self):
        return 'dog will bark'

def print_sound(animal:Animal):
    print(f"sound is {animal.sound()}")


dog = Dog()
print_sound(dog)