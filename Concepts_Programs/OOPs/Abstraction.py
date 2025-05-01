from abc import ABC,abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):

    def sound(self):
        print('bow bow')

class Tiger(Animal):
    pass

d =Dog()
d.sound()
t=Tiger()
a = Animal() # can't create with abstract method .



