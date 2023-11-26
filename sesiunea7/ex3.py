# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# three_count = 0
# for numar in numere:
#     if numar == 3:
#         three_count +=1
# print(three_count)
#
#
#
#
# suma = 0
# for numar in numere:
#     suma += numar
# print(suma)
#
# print(sum(numere))
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

max_num = float("-inf")
for numar in numere:
    if numar > max_num:
        max_num = numar
print(max_num)

min_num = float('inf')
for numar in numere:
    if numar < min_num:
        min_num = numar
print(min_num)

for i, numar in enumerate(numere):
    if numar < 0:
        numere[i] *= -1
print(numere)




