import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


my_rectangle = Rectangle(5, 10)
my_circle = Circle(7)
my_triangle = Triangle(8, 6)

print(f"Area of Rectangle: {my_rectangle.area()}")
print(f"Area of Circle: {my_circle.area()}")
print(f"Area of Triangle: {my_triangle.area()}")
