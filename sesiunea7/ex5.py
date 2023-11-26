alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lenght = len(alte_numere)

sorted = False
while not sorted:
    sorted = True
    for i in range(lenght -1):
        if alte_numere[i] > alte_numere[i + 1]:
            temp = alte_numere[i]
            alte_numere[i] = alte_numere[i+1]
            alte_numere[i +1] = temp
            sorted = False

print(alte_numere)