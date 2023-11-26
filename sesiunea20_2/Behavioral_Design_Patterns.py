class Blog:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def add_observer(self, obs):
        # subscribe
        self.observers.append(obs)

    def remove_observer(self, obs):
        # unsubscribe
        self.observers.remove(obs)

    def notify(self):
        # notify, va fi de obicei apelata intern, in functie de setari/preferinte (ex cand se adaug un nou BlogPost)
        for obs in self.observers:
            obs.notify(self.name)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def notify(self, blog_name):
        print(f'Notifying {self.name} about new blog post on {blog_name}')
        # aici de exemplu am putea trimite un email


blog = Blog('IT Factory Blog')
u1 = User('Ion Popescu', 'ceva@ceva.com')
u2 = User('Maria', '1234@yahoo.com')
u3 = User('Gheo', 'gheo@gmail.com')

# 2 useri fac subscribe
blog.add_observer(u1)
blog.add_observer(u3)

# apare un blog post nou
blog.notify()
print('_' * 80)

blog.remove_observer(u1)
blog.add_observer(u2)

blog.notify()
