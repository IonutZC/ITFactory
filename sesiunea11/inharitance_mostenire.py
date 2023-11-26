class Vehicle:

    def __init__(self, nr_whells, color, dors_cnt):
        self.nr_whells = nr_whells
        self.color = color
        self.dors_cnt = dors_cnt

    def drive(self):
        print("I m driveing ")

    def describe(self):
        print(f' i m a {self.color} wehicle , i have {self.nr_whells}wheels , {self.dors_cnt} dors ')


class Car(Vehicle):
    year = None
    horse_power = None

    def __init__(self, color, dors_cnt, year, horse_power):
        super(Car, self).__init__(4, color, dors_cnt)
        self.year = year
        self.horse_power = horse_power


car_1 = Car("Black", "4", "2004", "205")
print(car_1.horse_power)
print(car_1.nr_whells)
