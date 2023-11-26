input_string = input("Intr un string ")
#Extragem primul caracter
first_char = input_string[0]

#extragem stringul din mijloc
middle_string = input_string[1:-1]

#schimbam caracterul
middle_string = middle_string.replace(first_char , first_char.upper())

reconstructed_string = first_char + middle_string + input_string[-1]
print(reconstructed_string)
