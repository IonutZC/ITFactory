class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []   # children pot fi ori alte foldere, ori fisiere

    @property
    def size(self):
        total_size = 0
        for obj in self.children:
            total_size += obj.size
        return total_size

    def add_child(self, child):
        self.children.append(child)

    def delete_child(self, child):
        self.children.remove(child)

    def print_structure(self, level=0):
        print('\t' * level, f'Folder {self.name} [{self.size}] KB')
        for child in self.children:
            child.print_structure(level+1)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def print_structure(self, level):
        print('\t' * level, f'File {self.name} [{self.size} KB]')


root = Folder('root')
a = Folder('a')
b = Folder('b')
root.add_child(a)
root.add_child(b)

f1 = File('ceva.txt', 100)
f2 = File('altceva.csv', 50)
a.add_child(f1)
a.add_child(f2)

f3 = File('gjkdfso', 220)
f4 = File('gjrkd', 80)
c = Folder('c')
b.add_child(f3)
b.add_child(f4)
b.add_child(c)

f5 = File('nekrw', 100)
c.add_child(f5)

print(root.size)