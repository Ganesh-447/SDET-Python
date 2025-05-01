class Car:
    name = None
    model = None

    def Car_Details(self):
        print(f'your details are {self.name} ,{self.model}')


name= input('enter the name your car\n')
model =input('enter car mdole number\n')
tesla = Car()
tesla.name = name
tesla.model = model
tesla.Car_Details()