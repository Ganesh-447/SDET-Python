class Father:

    def father_money(self):
        print(5)

class Mother:

    def mother_money(self):
        print(5)

class Son(Father,Mother):
    pass

s = Son()
s.mother_money()
s.father_money()