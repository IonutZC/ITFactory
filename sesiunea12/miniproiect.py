from abc import ABC, abstractmethod


class Elev:
    nume = None
    varsta = None
    buline_rosii = 0

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta


class Gradinita(ABC):

    @abstractmethod
    def activitate_practica(self):
        raise NotImplementedError

    @abstractmethod
    def ore_de_somn(self):
        pass


class GradinitaPublica(Gradinita):

    def activitate_practica(self):
        print("Copiii învață să deseneze")

    def ore_de_somn(self):
        print("Copiii dorm")


class GradinitaPrivata(Gradinita):
    def activitate_practica(self):
        print("Copiii învață să modeleze cu plastilină")

    def ore_de_somn(self):
        print("Copiii dorm pe bani mai mulți")


class GradinitaPublica25(GradinitaPublica):

    elevi = []
    __arie = 0
    adresa = None
    intrari = 0

    def __init__(self, elevii, aria, adresa, intrari):
        self.elevi = elevii
        self.__arie = aria
        self.adresa = adresa
        self.intrari = intrari

    @property
    def arie(self):
        return self.__arie

    @arie.setter
    def arie(self, value):
        if value < 0:
            raise ValueError("Aria nu poate fi negativă.")
        self.__arie = value

    @arie.deleter
    def arie(self):
        print("Ștergerea ariei.")
        del self.__arie

    def get_buline_rosii(self):
        suma_buline = 0
        for i, elev in enumerate(self.elevi):
            buline_rosii_actuale = int(input(f'Dați un număr de buline pentru {elev.nume}: '))
            self.elevi[i].buline_rosii = buline_rosii_actuale
            suma_buline += buline_rosii_actuale
        media_buline = suma_buline / len(self.elevi)
        if media_buline > 5:
            print("Grădinița este considerată rea.")

    def activitate_practica(self):
        print("Copiii se joacă pe balansoar")

# Crearea unor elevi


elev_1 = Elev("George", 14)
elev_2 = Elev("Mihai", 15)
elev_3 = Elev("Gabriel", 18)
elevi = [elev_1, elev_2, elev_3]

# Crearea unei grădinițe publice
gradinita_publica_25 = GradinitaPublica25(elevi, 15, "Maceselui 3", 2)

# Apelarea metodei pentru a adăuga buline roșii și a evalua dacă grădinița este "Rea"
gradinita_publica_25.get_buline_rosii()
