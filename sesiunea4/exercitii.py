# original = (1, 2, 3)
# element = 4
# new_tuple = original + (element ,)
# print(new_tuple)

note_muzicale = ["do" , "re" , "mi" , "fa" ,"Sol" , "la" , "si" , "do"]
#1
print(note_muzicale)
#2
slice_note_muzicale = note_muzicale[::-1]
#4
print(slice_note_muzicale)
slice_note_muzicale.reverse()
print(slice_note_muzicale)
#5
print(note_muzicale.count("do"))

#6
tuple_note_muzicale = tuple(note_muzicale)
print(tuple_note_muzicale)
#7
#8
dictionar_note = {
    'do' : 2 ,
    're' : 1 ,
    'mi' : 1 ,
    'fa' : 1 ,
    'sol' : 1,
    'si' : 1 ,
}
print(dictionar_note)
