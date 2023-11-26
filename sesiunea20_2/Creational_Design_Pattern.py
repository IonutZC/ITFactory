class Car:
    make = None
    def __init__(self, make):
        self.make = make
        pass


c1 = Car('Toyota')
c2 = Car('Mitsubishi')
"""
c1 si c2 sunt obiecte DIFERITE, adica au ID-uri diferite, si se afla in locatii de memorie diferite.
"""
print(id(c1))
print(id(c2))
print(c1 == c2)


class SingletonLogger:
    __instance = None   # atributul de clasa __instance va actiona ca un "obiect" fals
    # pe care noi il vom returna de fiecare data cand se incearca crearea unui nou obiect din aceasta clasa
    path_to_file = None
    """
    Functia init in Python nu este chiar constructorul de-facto, ci este un initializator.
    Inainte de aceasta functie, este de fapt apelata functia __new__, unde se creaza un obiect in realitate.
    """

    def __new__(cls, *args, **kwargs):
        # Functia new nu are self ca si prim argument, pentru ca self inca nu exista la moment de runtime
        # In schimb, avem cls ca prim argument, care este de fapt clasa curenta
        if cls.__instance is None:
            # prima data cand este cerut un nou obiect, trebuie sa il cream
            cls.__instance = object.__new__(cls)
        # Apoi il returnam, acelasi obiect de fiecare data
        return cls.__instance

    def log(self, message):
        print(message)




print('_' * 80)
s1 = SingletonLogger(1,2)
s2 = SingletonLogger()
s3 = SingletonLogger()

print(id(s1))
print(id(s2))
print(id(s3))

# s1, s2, si s3 sunt de fapt acelasi obiect, ADICA referinte catre acelasi loc in memorie
print(s1 == s2)
s1.logger_level = 'DEBUG'
s2.log('aaa')
s1.log('abcd')
print(s2.logger_level)