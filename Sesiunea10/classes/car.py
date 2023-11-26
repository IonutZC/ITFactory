# Clasa car ce are atribute si metode specifice
import time


class Car:
    make = None
    model = None
    fuel = None
    capacity = None
    category = None
    color = None
    year = None
    speed = 0
    is_blinking_left = False
    is_blinking_right = False

    def __init__(self, make, model, fuel, capacity, category, color, year):
        self.make = make
        self.model = model
        self.fuel = fuel
        self.capacity = capacity
        self.category = category
        self.color = color
        self.year = year

    def accel(self):
        self.speed += 1
        print(f"{self.make} {self.model} is accelerating")

    def breaking(self):
        self.speed -= 1
        print(f"{self.make} {self.model} is breaking")

    def turn_left(self):
        self.is_blinking_right = False
        self.is_blinking_left = True
        print(f"{self.make} {self.model} is bleking left")
        time.sleep(4)
        self.is_blinking_left = False
        print(f"{self.make} {self.model} has finish bleking left")

    def turn_right(self):
        self.is_blinking_left = False
        self.is_blinking_right = True
        print(f"{self.make} {self.model} is bleking right")
        time.sleep(4)
        self.is_blinking_right = False
        print(f"{self.make} {self.model} has finish bleking right")

    def set_speed(self, desired_speed):
        while desired_speed > self.speed:
            self.accel()
        else:
            while desired_speed < self.speed:
                self.breaking()
        print(f'{self.make}{self.model} has {self.speed}')


first_car = Car("BMW", "330i", "Gasoline", "2998", "Sedan", "white", "2007")
second_car = Car("Mercedes", "S-Class", "Gasoline", "2998", "Sedan", "white", "2008")
first_car.set_speed(50)
second_car.set_speed(80)

first_car.set_speed(30)
second_car.set_speed(40)
second_car.turn_right()
first_car.turn_left()

car_list = []
car_list.append(first_car)
car_list.append(second_car)
print(car_list)