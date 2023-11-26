

# for i in range(0, 10, 2):
#     print(i)
# print("Am terminat")

students = ["Ionut", 'Nicolae', "valentin", "Paul", "Petre"]
student = " "
# for i, student in enumerate(students):
#     # if i % 2 == 0:
#     #     students[i] = students[i] + "S"
#     if student == "valentin":
#         # print(f'Indicele lui {student} este {i}')
#         students[i] = students[i] + "M."
#     else:
#         continue
#     print("Am terminat un ciclu ")
#
# print(students)
# for i, student in enumerate(students):
#     # if i % 2 == 0:
#     #     students[i] = students[i] + "S"
#     if student == "valentin":
#         # print(f'Indicele lui {student} este {i}')
#         students[i] = students[i] + "M."
#         break
#     else:
#         print("Am gasit un element diferit de valentin")
#         continue
#     # print("Am terminat un ciclu ")
#
# print(students)

cars_dict = {
    'Dacia': 15000,
    'Audi': 35000,
    "BMW": 38000,
    "Mercedes-Benz": 40000,
    'Opel': 26000,

}
buget = 32000
for masina, pret in cars_dict.items():
    if pret <= buget:
        print(f"Masina {masina} se incatreaza in buget si are pret de {pret} euro")

vector = [1, 2, 3, 4, 5, 6, 7]
print("************" * 50)
matrice = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
for row in matrice:
    for elm in row:
        print(elm)
