import random
#Exercitiu 1
note = [3, 7, 5, 8, 10]
rev_it = iter(reversed(note))
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
print(next(rev_it))
print(next(rev_it))
print("*" * 200)
#Exercitiul 2
def lotto_generator():

    for number in range(6):
        yield random.randint(1, 49)


    noroc = random.randint(1000000, 9999999)
    yield noroc



lottery_numbers = lotto_generator()
print("Numerele pentru loteria 6/49 sunt:")
for number in range(6):
    print(next(lottery_numbers))

noroc_number = next(lottery_numbers)
print(f"Numarul de noroc este: {noroc_number}")

#Exercitiul 3
print("*" * 80)

with open("hello.txt", "w") as file:
    content = file.write("Ce mai faci jane")

try:
    file = open("hello.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()

with open("hello.txt") as file:
    print(file.readlines())
print("*"*80)
#Exercitiul 4





