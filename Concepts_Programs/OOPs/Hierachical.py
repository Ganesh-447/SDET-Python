class Vehicle:

    def veh_info(self):
        return 'this is vehicle'
class Car(Vehicle):

    def car_info(self):
        return  'car info'

class Bike(Vehicle):

    def bike_info(self):
        return  'bike info'


b = Bike()
print(b.veh_info())