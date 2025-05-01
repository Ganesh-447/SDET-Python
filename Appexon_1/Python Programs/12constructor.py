class Person:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def walk(self):
        print(self.name + 'can walk')
    def dive(self):
        print(self.name + 'should have' +self.age + 'to dive' )
    def show_address(self):
        print("my name is "+ self.name+ ' and ' +  str(self.age) + 'live in'+ self.address)

ganesh = Person('Ganesh',24,"Bng")
lokesh = Person('lokesh',25,'Mysore')
# ganesh.walk()
# ganesh.dive()
ganesh.show_address()
lokesh.show_address()

