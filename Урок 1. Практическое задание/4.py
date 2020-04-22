#!/usr/local/bin/python3

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


print("Введите грацины диапозона")
symbol_left_border = input("Левая граница: ")
symbol_right_border = input("Правая граница: ")
if symbol_left_border.isdigit() and symbol_right_border.isdigit():
    symbol_left_border = int(symbol_left_border)
    symbol_right_border = int(symbol_right_border)
    numb = int(random() * (symbol_right_border - symbol_left_border + 1)
               + symbol_left_border)
    print(numb)
elif symbol_left_border.isalpha() and symbol_right_border.isalpha():
    rand_sym = int(random() * (ord(symbol_right_border) -
                               ord(symbol_left_border))) + ord(symbol_left_border)
    rand_sym = chr(rand_sym)
    print(rand_sym)
else:
    symbol_left_border = float(symbol_left_border)
    symbol_right_border = float(symbol_right_border)
    numb = random() * (float(symbol_right_border) -
                       float(symbol_left_border)) + float(symbol_left_border)
    print(numb)
