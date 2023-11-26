from abc import ABC, abstractmethod


class GeometricShape(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")

    @classmethod
    def describe(cls):
        print("Most likely, I have corners.")


class Square(GeometricShape):
    def __init__(self, side_length):
        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, new_length):
        if new_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.__side_length = new_length

    @side_length.deleter
    def side_length(self):
        print("Deleting side length.")
        del self.__side_length

    def area(self):
        return self.side_length ** 2

    def describe(self):
        print("I am a square. I have 4 equal sides.")

    def custom_description(self):
        print("I do not have corners.")


class Circle(GeometricShape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = new_radius

    @radius.deleter
    def radius(self):
        print("Deleting radius.")
        del self.__radius

    def area(self):
        return GeometricShape.PI * self.radius ** 2

    def describe(self):
        print("I am a circle. I have no corners.")

    def custom_description(self):
        print("I do not have corners.")

# Exemplu de utilizare:


square = Square(5)
print(f"Initial side length: {square.side_length}")
square.describe()
square.custom_description()

circle = Circle(5)
print(f"Initial radius: {circle.radius}")
circle.describe()
circle.custom_description()
