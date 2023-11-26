pret_masini = {
    'Dacia': 15000,
    'Audi': 400,
    "BMW": 38000,
    "Mercedes-Benz": 5,
}

buget = 15000

for masina, pret in pret_masini.items():
    if pret < buget:
        print(f'Aveti buget pentru {masina}')

