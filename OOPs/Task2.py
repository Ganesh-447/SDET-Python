# class Person:
#     name = None
#     age = None
#     address = None
#
#     def person_details(self):
#         print('your details are ',self.name,self.age,self.address)
#
# person1 = Person()
# name = input("Enter the name\n")
# age = int(input("Enter the age\n"))
# address = input("Enter the address\n")
# person1.name = name
# person1.age = age
# person1.address = address
# person1.person_details()
#
# person2 = Person()
# name = input("Enter the name\n")
# age = int(input("Enter the age\n"))
# address = input("Enter the address\n")
# person2.name = name
# person2.age = age
# person2.address = address
# person2.person_details()
#
class Person:
    name = None
    age = None
    address = None

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def repeat(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Address = ", self.address, "\n")


ram_obj = Person()
ram_obj.name = input("enter name : ")
ram_obj.age = input("enter age : ")
ram_obj.address = input("enter address : ")

sam_obj = Person()
sam_obj.name = input("\nenter name : ")
sam_obj.age = input("enter age : ")
sam_obj.address = input("enter address : ")


# print(sam_obj.name,sam_obj.age,sam_obj.address)