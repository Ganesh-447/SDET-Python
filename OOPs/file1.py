class Car:
    colour = None
    name = None
    model = None
    Speed = None
    engine = None

    def start_engine(self):
        print("Engine has started",self.colour, self.company)

    def drive (self):
        print("drive")
    def stop_engine (self):
        print("Car has stopped")
    def who_is_driving (self):
        print('I am driving',self.name,self.colour)


tesla_obj = Car()
lambo_obj = Car()

tesla_obj.name = 'Tesla'
tesla_obj.colour = 'Red'

lambo_obj.name = 'lambo'
lambo_obj.colour= 'white'

tesla_obj.who_is_driving()
lambo_obj.who_is_driving()