#single


class A(object):

    def method(self):
        return 'im the parent'

class B(A):

    def method(self):
        return super().method()

a = B()
print(a.method())

#multi -level

class grandfathter():

    def grand(self):
        return 'im the grandfather'
class father(grandfathter):

    def fathe(self):
        return 'im the fatehr'
class Son(father):

    def so(self):
        pass
b = Son()
print(b.fathe())
print(b.grand())


