class Ganesh(object):

    def __init__(self,name,age):

        self.name = name
        self.age = age


    def test(self,location):

        print(f'{self.name} is name')
        print(f'{self.age} is age')
        print(f'{location} is resident')

a = Ganesh('many',23)

a.test('newyork')

b = Ganesh('sai',34)
b.test('dkdkd')
