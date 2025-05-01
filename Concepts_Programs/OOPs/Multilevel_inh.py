class GrandFather:

    def grandparent_method(self):
        return "I'm grandh father"

class Father(GrandFather):

    def father_method(self):
        return "I'm the father"
class Son(Father):

    def son_method(self):
        return "I'm son"

s = Son()
print(s.grandparent_method())