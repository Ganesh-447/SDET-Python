class Car:

    name = None
    colour = None

    def car_details(self):
        print('your car details are ', self.name, self.colour)

car_colour = input('Enter car colour')
car_name = input("Enter car name")

ganesh_car_details = Car()
ganesh_car_details.name = car_name
ganesh_car_details.colour = car_colour
ganesh_car_details.car_details()