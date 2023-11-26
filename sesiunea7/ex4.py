alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []


for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar < 0:
        numere_negative.append(numar)
    else:
        numere_pozitive.append(numar)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)


# print(alte_numere)
# print(sorted(alte_numere))
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# Inițializăm o listă goală pentru rezultatul ordonat
lista_ordonata = []

# Iterăm peste lista inițială până când aceasta devine goală
while alte_numere:
    # Găsim elementul minim din lista inițială
    minim = alte_numere[0]
    for num in alte_numere:
        if num < minim:
            minim = num

    # Adăugăm elementul minim în lista ordonată și îl eliminăm din lista inițială
    lista_ordonata.append(minim)
    alte_numere.remove(minim)

print("Lista ordonată:", lista_ordonata)
