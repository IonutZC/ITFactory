class Person:
    first_name = None
    last_name = None
    age = None
    hight = 0
    weight = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def walk(self):
        print(f"{self.first_name} is walking")

    def speak(self, words):
        print(f"{self.first_name} is speaking {words}")
