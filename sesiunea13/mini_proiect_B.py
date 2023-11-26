class ToDo:
    def __init__(self, nume, descriere):
        self.nume = nume
        self.descriere = descriere


class ToDoList:
    def __init__(self):
        self.todo_list = []

    def adauga_task(self, nume, descriere):
        self.todo_list.append(ToDo(nume, descriere))

    def finalizare_task(self, nume):
        self.todo_list = [todo for todo in self.todo_list if todo.nume != nume]

    def afiseaza_todo_list(self):
        for todo in self.todo_list:
            print(todo.nume)

    def afiseaza_detalii(self, nume):
        todo = self.generat_todo(nume)
        if todo is None:
            descriere_task = input(f'Taskul {nume} nu este în lista de activități, dorești să-l adaugi? (Y/N): ')
            if descriere_task == 'Y':
                descriere_task = input(f'Dați descriere pentru taskul {nume}: ')
                self.adauga_task(nume, descriere_task)
            else:
                print("La revedere")

    def generat_todo(self, nume):
        for todo in self.todo_list:
            if todo.nume == nume:
                return todo
        return None


to_do_list = ToDoList()
to_do_list.adauga_task("task1", "descriere")

to_do_list.afiseaza_todo_list()
