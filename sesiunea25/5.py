'''
Creaza o functie Python care primeste doua stringuri ce reprezinta niste numere foarte mari, si returneaza rezultatul adunarii “numerelor”, tot sub format string:
Exemple:
add_two(‘12345’, ‘12345’) => ‘24690’
add_two(‘1234’, ‘4321’) => ‘5555’
add_two(‘563895634’, ‘548967348053’) => ‘549531243687’
'''

def add_two(num1, num2):
    # Ajustăm lungimile numerelor pentru a le face egale prin adăugarea de zerouri la început
    len1, len2 = len(num1), len(num2)
    if len1 < len2:
        num1 = '0' * (len2 - len1) + num1
    else:
        num2 = '0' * (len1 - len2) + num2

    result_digits = []
    carry = 0

    # Adunăm cifrele corespunzătoare
    for digit1, digit2 in zip(num1[::-1], num2[::-1]):
        total = int(digit1) + int(digit2) + carry
        result_digits.append(str(total % 10))
        carry = total // 10

    # Adăugăm eventualele cifre rămase
    if carry:
        result_digits.append(str(carry))

    # Construim rezultatul ca șir
    result = ''.join(result_digits[::-1])

    return result

# Exemple
print(add_two('12345', '12345'))           # Output: '24690'
print(add_two('1234', '4321'))             # Output: '5555'
print(add_two('563895634', '548967348053'))# Output: '549531243687'

