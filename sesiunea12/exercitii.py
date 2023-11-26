
class Angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f'Numele angajatului este {self.nume} {self.prenume} si are salariu de {self.salariu}')

    def nume_complet(self):
        print(f"Numele complet este {self.nume} {self.prenume}")

    def salariu_lunar(self):
        print(f'Salariul lunar este {self.salariu}')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariu anual este de {salariu_anual}')

    def marire_salariu(self, marire_salariu):
        marire_salariu = self.salariu * marire_salariu
        print(f' Marirea ssalariu este de {marire_salariu}')
        print(f' Salariu marit este {marire_salariu + self.salariu}')


angajat = Angajat("Popescu", "Marian ", 3000)
angajat.marire_salariu(0.2)


class Factura:
    seria = "x"
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
