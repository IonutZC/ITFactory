lista = [1, 2, 3, "patru", 5.1]
print(type(lista))
print(lista[0])  # apelam index
print(lista[-2])
print(len(lista))  # lungime

lista.append(5)  # adaugam element  - numeLista.append
print(lista)
lista.remove(5)

lista.insert(3, 3.5)
print(lista)

element_sters = lista.pop()
print(f'elementul sters este {element_sters}')
print(lista)

lista.pop(0)
print(lista)

lista_noua = ['Andreea', 'Bianca', 'Matei', 'Nicolae', 'Stefania']
print(len(lista_noua))
print(lista_noua[-1])
print(lista_noua[3][0:5])
print(lista_noua[0][-1])
print(lista_noua[1])
print(lista_noua.pop(2))
print(lista_noua[0:3])
print(lista_noua[-2:])
# lista_complexa = [1 , 2 ['sdasda', 'wdawd' ,] , 'wadwa']
# print(lista_complexa)
