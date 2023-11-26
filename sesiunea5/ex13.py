zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri' , 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('Luni')
print(zile_sapt)

# if len(zile_sapt.intersection(weekend)):
#     print("weekendul este subset")
# else:
#     print("weekendul  nu este subset")
#
if weekend.issubset(zile_sapt):
    print("weekendul este subset")
else:
    print("Nu este")

print(zile_sapt.difference(weekend)) # zile - weekend
print(weekend.difference(zile_sapt)) # wekend - zile

print(zile_sapt.intersection(weekend)) # intersectia





