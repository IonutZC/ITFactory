import csv
from tabulate import tabulate

with open("documents/p1.csv") as csv_file:
    pasrsed_file = csv.reader(csv_file)
    print(tabulate(pasrsed_file, headers='firstrow', tablefmt='fancy_grid'))