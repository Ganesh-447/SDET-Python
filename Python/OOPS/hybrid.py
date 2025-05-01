class A(object):

    def method_A(self):
        return 'Method A'
class B(A):

    def method_B(self):
        return 'Method B'

class C(A):
    def method_C(self):
        return 'Method C'

class D(B,C):

    def method_D(self):
        return 'method d'

a = D()
print(a.method_A())