"""
Question 47:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

"""

class Circle:
    def __init__(self, rad):
        self.rad = rad

    def circleArea(self):
        return(3.1416 * (self.rad ** 2))
    
cir = Circle(5)
print(cir.circleArea())


"""
Question 48:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

"""

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectArea(self):
        return self.length * self.width
    
rect = Rectangle(5,10)
print(rect.rectArea())


"""
Question 49:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

"""

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return (self.length * self.length)
    
sqr = Square(5)
print(sqr.area())
print(Square().area())


"""
Question 50:
Please raise a RuntimeError exception.

"""
raise RuntimeError("Something went wrong")