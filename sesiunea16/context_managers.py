class MyFileManager:
    def __enter__(self):
        self.file = open('example.txt', 'w')
        return self.file

    def __exit__(self, type1, value, traceback):
        self.file.close()

# Folosim context managerul pentru a deschide și scrie în fișier


with MyFileManager() as opened_file:
    opened_file.write("Acesta este un exemplu de context manager.")

# Fișierul este automat închis când blocul 'with' se încheie sau în caz de excepție
with open('example.txt', 'r') as read_file:
    file_contents = read_file.read()
    print("Conținutul fișierului 'example.txt':")
    print(file_contents)
    