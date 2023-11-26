lista = [1, 2, 3, 4, 5, 6, 7]

iter_obj = iter(lista)

while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break