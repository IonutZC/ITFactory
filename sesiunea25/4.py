'''
Creaza o functie Python care primeste o lista de numere, si il returneaza pe al doilea cel mai mare numar distinct.
Exemple:
get_second_biggest([1,2,3,4,5]) => 4
get_second_biggest([1,2,3,4,4]) => 3
get_second_biggest([1,2,4,4,4]) => 2
get_second_biggest([-1,-2,-3,-4,-5]) => -2

'''


def get_second_biggest(numbers):
    # Eliminăm duplicatii
    unique_numbers = list(set(numbers))

    # Verificăm dacă avem cel puțin două numere distincte
    if len(unique_numbers) < 2:
        return "Nu există al doilea cel mai mare număr distinct."

    # Sortăm lista descrescător
    sorted_numbers = sorted(unique_numbers, reverse=True)

    # Returnăm al doilea cel mai mare număr distinct
    return sorted_numbers[1]


# Exemple de utilizare:
print(get_second_biggest([1, 2, 3, 4, 5]))  # Output: 4
print(get_second_biggest([1, 2, 3, 4, 4]))  # Output: 3
print(get_second_biggest([1, 2, 4, 4, 4]))  # Output: 2
print(get_second_biggest([-1, -2, -3, -4, -5]))  # Output: -2
