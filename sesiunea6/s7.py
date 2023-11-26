# import random
#
# numar_secret = random.randint(1, 30)
# numar_ghicit = None
#
# while numar_ghicit != numar_secret:
#     try:
#         input_str = input("Guess the secret number (between 1 and 30), or type 'exit' to quit: ")
#
#         if input_str.lower() == 'exit':
#             print("Quitting the game. The secret number was:", numar_secret)
#             break  # Exit the loop if the user wants to quit
#
#         numar_ghicit = int(input_str)
#     except ValueError:
#         print("Please enter a valid number.")
#         continue
#
#     if numar_ghicit < numar_secret:
#         print("The secret number is larger.")
#     elif numar_ghicit > numar_secret:
#         print("The secret number is smaller.")
#     else:
# #         print("Congratulations! You guessed the secret number.")
# num = int(input("Enter a number: "))
#
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()
# number = int(input("Enter a number: "))
#
# i = 1
#
# while i <= number:
#     print(str(i) * i)
#     i += 1

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

for i in tastatura_telefon:
    print(i)
    for j in i:
        print(f'cifra aleasa este {j}')


