def reverse_positive_integer(number):
    if number < 0:
        print("Eroare: Numărul trebuie să fie pozitiv.")
        return

    print(int(str(number)[::-1]))


# Exemple de utilizare:
reverse_positive_integer(1234567)
reverse_positive_integer(10)
reverse_positive_integer(101)
reverse_positive_integer(10000000)
reverse_positive_integer(-65)

