class ToDoList:
    toDo = {}

    def adauga_task(self, nume, descriere):
        self.toDo[nume] = descriere

    def finalizare_task(self, nume):
        self.toDo.pop(nume)

    def afiseaza_todo_list(self):
        for i, task in enumerate(self.toDo.keys()):
            print(f' {i + 1} {task}')

    def afiseaza_detalii(self, nume):
        if nume not in self.toDo.keys():
            raspuns = input(f'Taskul {nume}, nu este in todo list , doresti sa il adaugi ? Y/N')
            if raspuns == 'Y':
                descriere_task = input(f'Dati descriere pentru taskul {nume}')
                self.adauga_task(nume, descriere_task)
            else:
                print("La revedere")


lista_1 = ToDoList()
lista_1.adauga_task("task_1", "descriere")
lista_1.adauga_task("task_2", "descriere")
lista_1.adauga_task("task_3", "descriere")
lista_1.adauga_task("task_4", "descriere")
lista_1.afiseaza_todo_list()
lista_1.finalizare_task("task_1")
lista_1.afiseaza_todo_list()
lista_1.afiseaza_detalii("task_1")
lista_1.afiseaza_todo_list()
