'''
creaza o functie Python care primește 2 stringuri, și verifica dacă acestea sunt anagrame (case-insensitive).
Exemple:
is_anagram(‘Adela’, ‘ealad’) => True
is_anagram(‘ITFactory’, ‘acfiorty’) => False
is_anagram(‘Stringy’, ‘gringsty’) => False
is_anagram(‘ana’, ‘ioana’) => False
'''
def is_anagram(str1, str2):
    # Eliminăm spațiile și convertim la litere mici
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Verificăm dacă sortarea caracterelor șirurilor este identică
    return sorted(str1) == sorted(str2)

# Exemple de utilizare
print(is_anagram('Adela', 'ealad'))  # True
print(is_anagram('ITFactory', 'acfiorty'))  # False
print(is_anagram('Stringy', 'gringsty'))  # False
print(is_anagram('ana', 'ioana'))  # False
