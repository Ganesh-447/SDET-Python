class Person:
    name = 'Ganesh'
    age = '24'
    phone_no = '1234'
    Gender = 'M'

    def walk(self):
        print(self.name+' can walk')

    def sleep(self):
        return "I can sleep"

    def talk(self):
        print(self.name+ ' can talk')

person1 = Person()
person1.name = 'Ganesh Grandhi'
person1.age = '20'
person1.Gender = 'Male'
person1.walk()
person1.sleep()
person1.talk()


person2 = Person()
person2.name = 'Lokesh'
person2.age = '20'
person2.Gender = 'Male'
person2.walk()
person2.sleep()
person2.talk()
print(person2.sleep())
