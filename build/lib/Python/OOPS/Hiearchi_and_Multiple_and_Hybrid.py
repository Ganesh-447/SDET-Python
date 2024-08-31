#Hiearchi

class Father(object):

    def father_method(self):

        return 'im the father mehtod '

class Son(Father):

    def son_method(self):

        return 'im the son method'
class daughter(Father):

    def daughter_method(self):

        return  'im the daughter method'

a = daughter()
print(a.father_method())
b = Son()
print(b.father_method())


# Multiple

class Father1(object):

    def money1(self):

        return 5
class Mohter(object):

    def money(self):

        return 10
class Sond(Mohter,Father1):

    def son_money(self):
        return (Mohter().money() + Father1().money1())


c = Sond()
print(c.money1())
print(c.money())
print(c.son_money())