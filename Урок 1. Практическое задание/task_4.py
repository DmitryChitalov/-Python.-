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

user_edge_min = int(input('Введите нижнюю границу диапаона для случайного целого числа '))
user_edge_max = int(input('Введите верхнюю границу диапаона для случайного целого числа '))
diff_edge = user_edge_max - user_edge_min
rand_int = user_edge_min + round(random()*diff_edge)
print(rand_int)

edge_float_min = float(input('Введите нижнюю границу диапаона для случайного вещественного числа '))
edge_float_max = float(input('Введите верхнюю границу диапаона для случайного вещественного числа '))
diff_edge_float = edge_float_max - edge_float_min
rand_float = edge_float_min + random()*diff_edge_float
print(rand_float)

edge_symbol_min = ord(input('Введите нижнюю границу диапаона для случайного символа '))
edge_symbol_max = ord(input('Введите верхнюю границу диапаона для случайного символа '))
rand_symbol = edge_symbol_min + round(random()*(edge_symbol_max-edge_symbol_min))
print(chr(rand_symbol))
