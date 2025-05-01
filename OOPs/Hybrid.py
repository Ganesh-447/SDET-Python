class A:

    def method_A(self):

        return 'Class A'


class B(A):

    def method_B(self):
        return 'Class B'


class C(A):

    def method_C(self):
        return 'Class C'


class D(B,C):

    def method_D(self):
        return 'Class D'


a = D()
print(a.method_A())
print(a.method_B())
print(a.method_C())
print(a.method_D())