class Rectangle:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def describe(self):
        print(f"The rectangle is {self.culoare}, and it has a length of {self.lungime} and a width of {self.latime}.")

    def area(self):
        return self.lungime * self.latime

    def perimeter(self):
        return 2 * (self.lungime + self.latime)

    def change_color(self, new_color):
        self.culoare = new_color

# Example of using the Rectangle class


rectangle1 = Rectangle(4, 2, "blue")
rectangle1.describe()
print(f"The area of the rectangle is: {rectangle1.area()}")
print(f"The perimeter of the rectangle is: {rectangle1.perimeter()}")

# Changing the color of the rectangle
rectangle1.change_color("green")
rectangle1.describe()
