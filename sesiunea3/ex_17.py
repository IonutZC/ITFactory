# 10.Transformă și printează notele din sistem românesc în  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota_obtinuta = int(input("Introduceti o nota"))
if nota_obtinuta >9:
    print("A")
elif nota_obtinuta > 8:
    print("B")
elif nota_obtinuta > 7:
    print("C")
elif nota_obtinuta > 6:
    print("C")
elif nota_obtinuta > 4:
    print("E")
else:
    print("F")

