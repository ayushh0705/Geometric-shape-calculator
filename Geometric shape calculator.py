
import math

# Define a base class for shapes
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

# Define a class for circles, inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi * self.radius**2

    def circle_perimeter(self):
        return 2 * math.pi * self.radius

# Define a class for rectangles, inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width

    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)

# Define a class for triangles, inheriting from Shape
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Circle
r = 8
circle1 = Circle(r)
circle_area = circle1.circle_area()
circle_perimeter = circle1.circle_perimeter()
print("Creating a circle with radius", r)
print("Area of the circle is", circle_area)
print("Perimeter of the circle is", circle_perimeter)

# Rectangle
l = 6
w = 8
rectangle1 = Rectangle(l, w)
rectangle_area = rectangle1.rectangle_area()
rectangle_perimeter = rectangle1.rectangle_perimeter()
print("\nCreating a rectangle with length", l, "and width", w)
print("Area of the rectangle is", rectangle_area)
print("Perimeter of the rectangle is", rectangle_perimeter)

# Triangle
base = 5
height = 6
s1 = 3
s2 = 6
s3 = 2
print("\nCreating a triangle with base", base, ", height", height, ", side1", s1, ", side2", s2, ", side3", s3)
triangle = Triangle(base, height, s1, s2, s3)
area = triangle.area()  # Call the area method on the instance
perimeter = triangle.perimeter()
print("Area of the triangle is", area)
print("Perimeter of the triangle is", perimeter)
