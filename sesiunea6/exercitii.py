# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

print(f"masina mea favorita este  {masini[3]}")


x = "Fiat"
# for masina in masini:
#    if masina == "Fiat":
#     print(f'Masina mea favorita este {masina}')
# q = 0
# while q == x:
#     print(f'Masina selectata este {x}')
#     q += 1

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

#index = 0  # Inițializăm un index care va începe de la 0

# while index < len(masini):  # Cat timp indexul este mai mic decât lungimea listei
#     print(masini[index])    # Afișăm elementul de la indexul curent
#     index += 1              # Incrementăm indexul pentru a trece la următorul element

# i = 0
# while i <= len(masini):
#     if i == x:
#         print(f'Masina mea favorita este {x}')

for index, masina in enumerate(masini):
    if index == 0 or index == len(masini) - 1:
        continue  # Trecem peste primul și ultimul element
    masini[index] = masina.upper()  # Convertim în majuscule elementele din interior
else:
    print(masini)  # Afișăm lista modificată

# Rezultatul va fi:
# ['Audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LĂSTUN', 'FIAT', 'TRABANT', 'Opel']





