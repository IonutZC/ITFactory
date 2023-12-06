'''
Creaza o functie Python care primeste un numar n, si o lista de numere de dimensiune n-1. In lista se afla toate numerele de la 1 la n, in afara de 1. Functia trebuie sa gaseasca acel numar in cel mai eficient mod posibil si sa-l returneze.
Exemple:
find_missing(5, [1,2,3,5]) => 4
find_missing(2, [1]) => 2
find_missing(7, [6,5,1,3,2,7]) => 4
'''
def find_missing(n, numbers):
    # Calculăm suma totală a numerelor de la 1 la n folosind range
    total_sum = sum(range(1, n + 1))

    # Calculăm suma actuală a numerelor din listă
    list_sum = sum(numbers)

    # Găsim numărul lipsă
    missing_number = total_sum - list_sum

    return missing_number

# Exemple
print(find_missing(5, [1, 2, 3, 5]))      # Output: 4
print(find_missing(2, [1]))               # Output: 2
print(find_missing(7, [6, 5, 1, 3, 2, 7])) # Output: 4
