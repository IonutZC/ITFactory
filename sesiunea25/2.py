def rotate_list(number_lst, k):
    # Asigură că k este în intervalul [0, len(lst))
    k = k % len(number_lst)

    # Realizează rotația
    rotated_list = number_lst[k:] + number_lst[:k]

    return rotated_list


# Exemple de utilizare:
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 8))
