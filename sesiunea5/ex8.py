dict1 = {
    "Ana" : 8,
    "Gigel" : 10,
    "Dorel" : 5,
}
elevi = list(dict1.keys())

print(f'{elevi[0]} a luat nota :{dict1[elevi[0]]}')
print(f'{elevi[1]} a luat nota :{dict1[elevi[1]]}')
print(f'{elevi[2]} a luat nota :{dict1[elevi[2]]}')

dict1["Dorel"] = 6
print(f'Dorel a luat dupa contestatie {dict1["Dorel"]}')
dict1.pop("Gigel")
dict1['Ionica'] = 9
print(dict1)



