class Person:

    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age

    def print_details(self):
        print("your details are",self.name,self.age)

person1 = Person(None,None)

name = input("enter your name")
age = input("enter your age")

person1.name = name
person1.age = age
person1.print_details()
person2 = Person(None,None)

name = input("enter your name")
age = input("enter your age")

person2.name = name
person2.age = age
person2.print_details()



