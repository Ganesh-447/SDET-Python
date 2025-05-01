# Base class
class Animal:

    def speak(self):
        pass

# Derived class 1
class Mammal(Animal):

    def speak(self):
       pass

# Derived class 2
class Dog(Mammal):

    def describe(self):
        return f"I'm the description"

# Create an instance of the Dog class
my_dog = Dog()

# Access methods from all levels of inheritance
# print(my_dog.describe())  # Output: Buddy is a Labrador dog
print(my_dog.speak())     # Output: Buddy says Woof
