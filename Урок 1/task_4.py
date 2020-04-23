import random

MIN = int(input("Нижний предел: "))
MAX = int(input("Вверхний предел: "))
print(random.randint(MIN, MAX))

MIN = int(input("Нижний предел: "))
MAX = int(input("Вверхний предел: "))
print(random.uniform(MIN, MAX))

MIN = ord(input("Нижняя буква: "))
MAX = ord(input("Вверхняя буква: "))
print(chr(random.randint(MIN, MAX)))
input("Press any to exit...")