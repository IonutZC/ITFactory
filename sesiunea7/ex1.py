# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# # for masina in masini:
# #     print(f'Masina mea favorita este {masina}')
# # print("*"*80)
# #
# # i = 0
# # while i <= len(masini):
# #     print(f'Masina mea favorita este {masini[i]}')
# #     i += 1
#
# i = 0
# for masina in masini:
#     if i != 0 and i != len(masini)-1:
#         masini[i] = masini[i].upper()
#     i += 1
# else:
#     print(masini)
#
#
# i = 0
#
# for i in range(1, len(masini)-1):
#     masini[i] = masini[i].upper()
# else:
#     print(masini)
#
#
# for i, masina in enumerate(masini):
#     if i != 0 and i != len(masini) - 1:
#         masini[i] = masini[i].upper()
# else:
#     print(masini)
#
# for masina in masini:
#     if masina.upper() == "MERCEDES":
#         print("AM gasit masina dvs")
#         break
#     else:
#         print(f'Nu am gasit masina dorita')
#
# for masina in masini:
#     if masina.upper() == "TRABANT" or masina.upper() == "LASTUN":
#         continue
#     print(f"Ar putea sa va placa masina {masina}")
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi =[]

for i, masina in enumerate(masini):
    if masina == "Trabant" or masina == "Lastun":
        masini_vechi.append(masina)
print(masini)
print(masini_vechi)
