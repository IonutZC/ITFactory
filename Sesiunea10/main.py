from classes.persons import Person


person_1 = Person("Ion", "Pop", "26")
person_1.speak("Salut, ce mai faci ?")
person_1.hight = 1.80
person_1.weight = 80
print(f'{person_1.first_name} are {person_1.hight} metri inaltime si {person_1.weight} kilograme ')
