"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

from random import random

# Генерация случайного челого числа
print("Генерация челочисленного числа\n")
try:
    LOWER_BORDER = int(input("Введите нижнюю границу:\n"))
    UPPER_BORDER = int(input("Введите верхнюю границу:\n"))

    if LOWER_BORDER > UPPER_BORDER:
        print("Границы заданы неверно")
    else:
        GENERATE_NUMBER = int(
            LOWER_BORDER + (UPPER_BORDER - LOWER_BORDER) * random())
        print(f"Сгенерированное число = {GENERATE_NUMBER}")
except ValueError:
    print("Нужно ввести целое число")

# Генерация вещественного числа
print("Генерация вещественного числа\n")
try:
    LOWER_BORDER = float(input("Введите нижнюю границу:\n"))
    UPPER_BORDER = float(input("Введите верхнюю границу:\n"))

    if LOWER_BORDER > UPPER_BORDER:
        print("Границы заданы неверно")
    else:
        GENERATE_NUMBER = round(
            LOWER_BORDER + (UPPER_BORDER - LOWER_BORDER) * random(), 2)
        print(f"Сгенерированное число = {GENERATE_NUMBER}")
except ValueError:
    print("Нужно ввести число\n")

# Генерация символа
print("Генерация символов a - z\n")

try:
    LOWER_BORDER = input("Введите нижнюю границу:\n")
    UPPER_BORDER = input("Введите верхнюю границу:\n")

    LOWER_BORDER_CODE = ord(LOWER_BORDER)
    UPPER_BORDER_CODE = ord(UPPER_BORDER)

    if LOWER_BORDER_CODE > ord('z') or LOWER_BORDER_CODE < ord('a'):
        print("Нижняя граница задана неверно")
    elif UPPER_BORDER_CODE > ord('z') or UPPER_BORDER_CODE < ord('a'):
        print("Верхняя граница задана неверно")
    elif LOWER_BORDER_CODE > UPPER_BORDER_CODE:
        print("Границы заданы неверно")
    else:
        GENERATE_NUMBER = int(
            LOWER_BORDER_CODE + (UPPER_BORDER_CODE + 1 - LOWER_BORDER_CODE) * random())
        CHAR = chr(GENERATE_NUMBER)
        print(f"Сгенерированный символ = {CHAR}")
except TypeError:
    print("Нужно вводить символ от a до z")
