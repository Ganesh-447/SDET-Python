class Car:

    def __init__(self,make,model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f'car is starting for {self.make} {self.model}')


car1=Car("KIA",123)
car2=Car("Tata",312)

car1.make ='Jaguar'
car1.start_engine()