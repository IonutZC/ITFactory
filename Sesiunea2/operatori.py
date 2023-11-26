# operatori de atribuire si aritmetici
x = 5 # egal este operatorul de atribuire
x = x + 5 # operator de atribuire ( = ) si aritmetic (+)
x += 5

x = x-5
x -= 5

x = x * 2
x *= 2

x = x / 4
x /= 5

x = 20
rest_impartire = x % 3 #aflare restului
cat_impartire = x // 3 #aflarea catului
print(rest_impartire)
print(cat_impartire)

x = 20 ** 2 #ridicarea la putere
print(x)

# operatori de comparare
print("*****************")
a = 10
b = -4

print(a == b) # false
print(a < b)  # false
print( a > b)  # true
print(a >= b) # true
print(a != b) # true
print(a <= b) #false

# Operatori logici
print("********************")

a = 12
b = -5
print( a > 0 and a <= 12 ) #  operator and = ambele conditii trebuiesc respectate
print(a < 0 and a != 12)

print(a > b or a > 100)
print(not (a < 5))
print( a !=b and  not( a > 120 or a - b == 3))
