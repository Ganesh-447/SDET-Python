class Car:
    name = None
    colour = None
    model = None
    tyre = None
    milege = None


    def start_the_car(self):
        print("your"+ self.name +' is started')
    def car_reached(self):
        print('your '+ self.colour,self.name + ' is reached')
    def car_gear_state(self):
        print('your ' + self.model,self.name + ' is in top gear')
    def tyre_running(self):
        print('your '+ self.name,self.tyre, 'is fine')
    def milege_indicator(self):
        print(self.name,'has',self.milege, 'kms')

Tesla = Car()
Tesla.name = 'Tesla'
Tesla.colour = 'White'
Tesla.model = '2nd model'
Tesla.milege = 23
Tesla.tyre = 'MRF Tyres'

Tesla.start_the_car()
Tesla.car_reached()
Tesla.car_gear_state()
Tesla.tyre_running()
Tesla.milege_indicator()

Tata_Punch = Car()
Tata_Punch.name = 'Tata Punch'
Tata_Punch.colour = 'Red'
Tata_Punch.model = '1st model'
Tata_Punch.milege = 33
Tata_Punch.tyre = 'Ceat Tyres'

Tata_Punch.start_the_car()
Tata_Punch.car_reached()
Tata_Punch.car_gear_state()
Tata_Punch.tyre_running()
Tata_Punch.milege_indicator()