class Person:
    name = ''
    __cnp = None
    date_of_birht = None

    def __init__(self, name):

        self.name = name

    @property
    def cnp(self):
        return self.__cnp

    @cnp.getter
    def cnp(self):
        return f' CNP persoanei {self.name} este {self.cnp}'

    @cnp.setter
    def cnp(self, value):
        self.__cnp = value
        print(f'CNP-ul persoanei {self.name}a fost setat la  {value}')


p1 = Person("Marian")
p1.cnp = "123456789525"
