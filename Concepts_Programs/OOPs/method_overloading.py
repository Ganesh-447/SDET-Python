#python doesn't support method overloading in tradional way.
# same name of function with differnt parameter

#so no method overloading.

class MathUtil:

    # def add(self,a,b):
    #     return a+b           #no natural overloading.
    # def add(self,a,b,c):
    #     return a+b+c

    #use default values
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b


a=MathUtil()
print(a.add(1,2,5))

