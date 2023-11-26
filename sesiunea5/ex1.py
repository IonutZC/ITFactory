list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_3 = list_1 + list_2
print(list_3)
list_1.extend(list_2)
print(list_1)
list_1.sort()
print(list_1)
list_1.remove(0)
print(list_1)

if len(list_1):
    print("Lista nu este goala")
else:
    print("Lista  este goala")



