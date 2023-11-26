import time


def my_generator():
    n = 1
    while True:
        yield n
        time.sleep(0.2)
        if n == 10:
            break
        n += 1


number = my_generator()
val = next(number)
print(val)
val2 = next(number)
print(val2)
val3 = next(number)
print(val3)
val4 = next(number)
print(val4)

