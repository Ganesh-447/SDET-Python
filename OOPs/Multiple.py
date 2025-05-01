class Father:

    def father_money(self):

        print('5 rupees from father')

class Mother:

    def mother_money(self):

        print(('5 rupees from mother'))

class Son(Father,Mother):

    def son_money(self):
        pass


a = Son()
a.mother_money()
a.father_money()