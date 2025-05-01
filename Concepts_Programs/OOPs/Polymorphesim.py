#Polymorphism - behave differently as per the situation.

# allows objects of different classes to be treated as objects of super class.
class Shape:

    def area(self):
        print(f'this is shape area')

class Rectangle(Shape):

    def __init__(self,length, breadth):
        self.length =length
        self.breadth = breadth

    def area(self):
        #super().area()
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return  3.14 * self.radius * self.radius


#function demonstrating poly
def print_area(shape:Shape):
    print(f"area:{shape.area()}")

r = Rectangle(5,6)
# print(r.area())
#
# c = Circle(10)
# print(c.area())

print_area(r)

# s=Shape()
# s.area()