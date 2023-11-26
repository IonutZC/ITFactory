class Cat:
    name = None

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("meau")


class Dog:
    name = None

    def make_sound(self):
        print("Ham")

    def __init__(self, name):
        self.name = name


cat_1 = Cat("Mircea")
dog_1 = Dog("Rex")

animal_list = [cat_1, dog_1]

for animal in animal_list:
    print(animal.name)
    animal.make_sound()
