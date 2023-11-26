x = input("dati o dimensiune ")
y = input("dati o dimensiune ")
z = input("dati o dimensiune ")

if x == y == z :
    print("Triunghi echilateral")
elif x == y or x == z or y == z:
    print("Isoscel")
else:
    print("Oarecare")
