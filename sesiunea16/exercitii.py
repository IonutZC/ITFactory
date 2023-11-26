import  random
# Creează o listă, o tuplă și un șir de caractere
my_list = [1, 2, 3]  # Creează o listă cu trei elemente întregi: 1, 2, 3
my_tuple = (4, 5, 6)  # Creează o tuplă cu trei elemente întregi: 4, 5, 6
my_string = "abcdefghijklmnopqrstuvwxyz"  # Creează un șir de caractere cu literele alfabetului

# Iterează prin lista folosind o buclă 'for'
for item in my_list:  # Începe o buclă 'for' care iterează prin fiecare element din listă
    print(f'Element: {item}')  # Afișează elementul din listă folosind formatarea f-string

# Creează un iterator pentru lista și iterează folosind 'next'
list_iterator = iter(my_list)  # Creează un iterator pentru lista
print(f'Primul element: {next(list_iterator)}')  # Afiseaza primul element din lista
print(f'Al doilea element: {next(list_iterator)}')  # Afiseaza al doilea element din lista
print(f'Al treilea element: {next(list_iterator)}')  # Afiseaza al treilea element din lista

try:
    # Iterează pentru a forța o excepție 'StopIteration'
    print(f'Aici va da eroare: {next(list_iterator)}')  # Folosește 'next' pentru a forța o excepție 'StopIteration'
except StopIteration:
    print('Am ajuns la finalul listei.')  # Gestionăm excepția 'StopIteration' afișând un mesaj

# Iterează prin șirul de caractere cu enumerate
for index, letter in enumerate(my_string):  # Iterăm prin șirul de caractere și obținem atât indexul cât și caracterul
    ordinal = index + 1  #
    if ordinal == 1:
        print(f'Pe mine mă cheamă {letter} și sunt prima literă din alfabet.')
    else:
        print(f'Pe mine mă cheamă {letter} și sunt a {ordinal}-a literă din alfabet.')


people = ["Alice", "Bob", "Charlie"]
jobs = ["Inginer", "Profesor", "Designer"]
salaries = [5000, 6000, 4000]


random.shuffle(people)
random.shuffle(jobs)
random.shuffle(salaries)


for person, job, salary in zip(people, jobs, salaries):
    print(f'Pe mine mă cheamă {person}, sunt de profesie {job}, și câștig {salary} RON pe lună.')
