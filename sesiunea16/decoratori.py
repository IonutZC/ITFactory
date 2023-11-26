import time  # Importă modulul 'time' pentru a măsura timpul


def timing_decorator(func):  # Definim un decorator numit 'timing_decorator', care primește o funcție 'func' ca argument
    def wrapper(*args, **kwargs):  # Definim o funcție intermediară 'wrapper' care primește orice argumente
        start_time = time.time()  # Măsurăm timpul la începutul execuției funcției

        result = func(*args, **kwargs)  # Apelăm funcția 'func' cu argumentele primite și stocăm rezultatul

        end_time = time.time()  # Măsurăm timpul la sfârșitul execuției funcției

        execution_time = end_time - start_time  # Calculăm timpul de execuție

        # Afișăm numele funcției și timpul de execuție
        print(f"{func.__name__} a durat {execution_time:.2f} secunde.")

        return result  # Returnăm rezultatul funcției

    return wrapper  # Returnăm funcția 'wrapper' decorată


@timing_decorator  # Aplicăm decoratorul 'timing_decorator' funcțiilor de mai jos
def slow_function():
    time.sleep(2)  # Simulăm o funcție care durează 2 secunde
    print("Funcția a fost executată.")


@timing_decorator  # Aplicăm decoratorul funcției de mai jos
def fast_function():
    print("Funcția a fost executată rapid.")


slow_function()  # Apelăm funcția 'slow_function' decorată cu 'timing_decorator'
fast_function()  # Apelăm funcția 'fast_function' decorată cu 'timing_decorator'
