class Car(object):

    color = None
    tyres = None
    engine_type = None
    model = None
    name = None

    def color_name(self):
        print(f' the colour of the {self.name} is {self.color}')

    def tyre_company(self):
        print(f' the tyres used for this {self.name} are {self.tyres}')

    def engine(self):
        print(f'the engine type for this {self.name} is {self.engine_type}')

    def model_version(self):
        print(f'the version type of this {self.name} is {self.model}')


Tesla = Car()
Tata = Car()

Tesla.name = "Tesla"
Tesla.tyres = "MRF"
Tesla.model = "1st gen"
Tesla.color = "Red"
Tesla.engine_type = "Petrol"

Tata.name = "Tata EV"
Tata.tyres = 'Tata tyres'
Tata.model ='new model'
Tata.color = 'white'
Tata.engine_type = "Electric"

Tesla.engine()
Tata.engine()














# class Ganesh(object):
#
#     def __init__(self,name,age):
#
#         self.name = name
#         self.age = age
#
#
#     def test(self,location):
#
#         print(f'{self.name} is name')
#         print(f'{self.age} is age')
#         print(f'{location} is resident')
#
# a = Ganesh('many',23)
#
# a.test('newyork')
#
# b = Ganesh('sai',34)
# b.test('dkdkd')
