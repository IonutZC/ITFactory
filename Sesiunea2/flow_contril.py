# flow control if - else

varsta_majorat = 18
varsta_persoana = 16



if(varsta_persoana >= varsta_majorat):
    print("Major")
else:
    print('Minor')

print("*****************************")
# flow control if - elif - else

nota_de_trecere = 5
nota_de_premiere = 8
nota_obtinuta = input("Introduceti o nota : ")
nota_obtinuta = float(nota_obtinuta)

#a trecut examenul
# daca a luat premiu
#daca a picat


# if nota_obtinuta  >= nota_de_trecere  :
#     print("Ai trecut ")
# elif nota_obtinuta >= nota_de_premiere:
#     print("Felicitari premiu")
# else:
#     print("Ai picat")
#
#
# # if nota_obtinuta >= nota_de_premiere:
# #     print("Felicitari ai obtinut premiu")
# # else:
# #     print("Nu premiu")

if nota_obtinuta >= nota_de_premiere:
    print("Ai luat un premiu")
elif nota_obtinuta >= nota_de_trecere:
    print("Ai trecut")
else:
    print("ai picat")
