class A:

    def method_A(self):

        print('a method')

class B(A):
    
    def method_B(self):
        print('b method')

class C(A):

    def method_c(self):
        print('c method')
class D(B,C):

    def method_D(self):
        print('D method')