class Car:
    brand = "Hyundai"
    model = None
    max_speed = 0
    current_speed = 0
    color = "grey"
    aviable_colors = {"white", "black", "grey", "blue"}
    is_registred = False

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def describe(self):
        print(f'{self.brand} {self.model} {self.max_speed} {self.current_speed} {self.color} {self.is_registred}')

    def registred(self):
        self.is_registred = True
        print(f'Car {self.brand} {self.model}  has been registred')

    def paint(self, color):
        if color in self.aviable_colors:
            self.color = color
        else:
            print("Eroare culoarea nu este valabila")

    def accelerate(self, new_speed):
        if new_speed > 0:
            if new_speed < self.max_speed:
                self.current_speed = new_speed
            else:
                print(f"Viteza maxima pentru {self.brand} {self.model} este 150")
                self.current_speed = self.max_speed
        else:
            self.current_speed = 0

    def foot_break(self):
        self.current_speed = 0


masina_A = Car("138", 150)
masina_A.describe()
masina_A.paint("blue")
masina_A.paint("Magenta")
masina_A.accelerate(180)
print(masina_A.current_speed)
masina_A.accelerate(100)
print(masina_A.current_speed)
masina_A.registred()
masina_A.describe()
