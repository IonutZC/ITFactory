dictionar = {
    "nume" : "George",
    "Varsta" : 27 ,
    "major" : True
}
print(type(dictionar))

print(dictionar["nume"])
print(dictionar["major"])

dictionar_ca_lista = {
    0 : "George",
    1 : 'Flutur'

}
print(dictionar_ca_lista[0] + " " + dictionar_ca_lista[1])

dictionar["Varsta"] = 28
print(dictionar["Varsta"])

dictionar_complex ={
    "cheie" : [1, 2, 3, 4, 5, 6, 7],
    'dict_interior' : {
        "cheie_interioara" : 1
    }
}

dictionar_complex['cheie'][-1] = 7.5
print(dictionar_complex)
print(dictionar_complex['dict_interior']["cheie_interioara"])

# print(dictionar_complex.pop("cheie"))
print("x" * 80)
print(dictionar_complex.keys())
lista_noua = list(dictionar_complex.keys())
print(type(lista_noua))
lista_valori = list(dictionar_complex.values())
print(lista_valori)
lista_noua.clear()
dictionar_complex['dict_interior'].clear()
print(dictionar_complex)
