class Car:
    name = None
    colour = None
    engine = None
    Model_no = None

    def start(self):
        print('car started')
    def stop(self):
        print('car stopped')
    def car_break(self):
        print(f'Applied Breaks for {self.name} ')


Tesla_obj = Car()
Lambo_obj = Car()

Tesla_obj.name = 'Tesla'
Lambo_obj.name = 'Lambo'
Lambo_obj.car_break()
Tesla_obj.car_break()


