
# slicing
sir_caractere = 'Acesta este un sir de caractere'
lungime_caractere = len(sir_caractere)
slice_sir = sir_caractere[0:lungime_caractere - 2]
print(slice_sir)

sir_caractere_2 = "AbAbAbAbAb"
slice_sir_2 = sir_caractere_2[1:len(sir_caractere_2):2]
print(slice_sir_2)

sir_caractere_3 = "123456789"
slice_sir_3 = sir_caractere_3[9::-1]
print(slice_sir_3)


my_list = list(sir_caractere_3)
print(my_list)
rev_list = list(reversed(my_list))
print(rev_list)
my_list2 = list(sir_caractere)
print(my_list2)