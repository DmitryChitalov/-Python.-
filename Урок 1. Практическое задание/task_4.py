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
    print("Целое число:")
    VAL1 = int(input("Введите нижнюю границу : "))
    VAL2 = int(input("Введите верхнюю границу : "))
    NUM = int(random() * (VAL2 - VAL1 + 1)) + VAL1
    print(NUM)
except ValueError:
    print("Введите число. Попробуйте еще раз.")

try:
    print("Вещественное число:")
    VAL1 = float(input("Введите нижнюю границу : "))
    VAL2 = float(input("Введите верхнюю границу : "))
    NUM = random() * (VAL2 - VAL1) + VAL1
    print(round(NUM, 3))
except ValueError:
    print("Введите число. Попробуйте еще раз.")

print("Символ:")
VAL1 = ord(input("Введите нижнюю границу : "))
VAL2 = ord(input("Введите верхнюю границу : "))
NUM = int(random() * (VAL2 - VAL1 + 1)) + VAL1
print(chr(NUM))
