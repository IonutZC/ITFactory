from datetime import date
today = date.today()


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

    @property
    def schimba_cantitate(self):
        return self.cantitate

    @property
    def schimba_pretul(self):
        return self.pret_buc

    @property
    def schimba_nume_produs(self):
        return self.nume_produs

    @schimba_cantitate.setter
    def schimba_cantitate(self, value):
        self.cantitate = value

    @schimba_pretul.setter
    def schimba_pretul(self, value):
        self.pret_buc = value

    @schimba_nume_produs.setter
    def schimba_nume_produs(self, value):
        self.nume_produs = value

    def generate_invoice(self):
        print(f'Factura seria {self.seria}, nr {self.numar}')
        print(f' Data {today}')
        print("Produs | Cantitate | Pret buc | Total")
        print(f'{self.nume_produs}|     {self.cantitate}     | {self.pret_buc}      | {self.cantitate * self.pret_buc}')


factura1 = Factura(57, "Telefon", 4, 500)
factura1.generate_invoice()
