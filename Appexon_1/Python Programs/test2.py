# #single inheritance
# class Father:
#
#     def test_1(self):
#         print("Hi son ")
#
# class Son(Father):
#
#     def test_2(self):
#         print("hi Father")
#
# s = Son()
# s.test_1()
# s.test_2()

#Multi-level inheritance.
#
# class GrandhFather:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b =b
#
#     def grand_pa(self):
#         print('im old person', self.a,self.b)
# class Father(GrandhFather):
#
#     def father(self):
#         print("i'm father", self.b)
# class Son(Father):
#
#     def son(self):
#         print("i'm young", self.a)

#f = Father(2,3)
# Multiple
# class Father:
#
#     def method1(self):
#         print('Im the father')
# class Mother:
#     def method2(self):
#         print('Im the Mother')
# class Son(Father,Mother):
#
#     def method3(self):
#         print('Im son')
# s = Son()
# s.method1()

# hiearchical
# class Father:
#     def test_1(self):
#         print('one')
# class Son(Father):
#     def test_2(self):
#         print('two')
# class Sister(Father):
#     def test_3(self):
#         print('three')
#
# s = Sister()
# s.test_1()

# Hybrid

class A:
    def test_1(self):
        print('1st')
class B(A):
    def test_2(self):
        print('2nd')
class C(A):
    def test_3(self):
        print('1st')
class D(B,C):
    def test_4(self):
        print('2nd')
