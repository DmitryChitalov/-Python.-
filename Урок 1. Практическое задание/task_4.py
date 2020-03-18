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
try:
    A_NUM = int(input("Введите нижнюю границу: "))
    B_NUM = int(input("Введите верхнюю границу: "))
    C_NUMB = int(random() * (B_NUM - A_NUM + 1)) + A_NUM
    print(C_NUMB)
except ValueError:
    print("Вы ввели неккоректные данные")

try:
    A_NUM = float(input("Введите нижнюю границу: "))
    B_NUM = float(input("Введите верхнюю границу: "))
    C_NUMB = float(random() * (B_NUM - A_NUM + 1)) + A_NUM
    print(C_NUMB)
except ValueError:
    print("Вы ввели неккоректные данные")

try:
    A_SIN = ord(input("Введите нижнюю границу: "))
    B_SIN = ord(input("Введите верхнюю границу: "))
    C_SIN = int(random() * (B_SIN - A_SIN + 1)) + A_SIN
    print(chr(C_SIN))
except ValueError:
    print("Вы ввели неккоректные данные")
