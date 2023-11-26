import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def describe_circle(self):
        print(f"The circle is {self.color} and has a radius of {self.radius}.")

    def area(self):
        return math.pi * self.radius**2

    def diameter(self):
        return 2 * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

# Example of using the Circle class
circle1 = Circle(5, "red")
circle1.describe_circle()
print(f"The area of the circle is: {circle1.area()}")
print(f"The diameter of the circle is: {circle1.diameter()}")
print(f"The circumference of the circle is: {circle1.circumference()}")
