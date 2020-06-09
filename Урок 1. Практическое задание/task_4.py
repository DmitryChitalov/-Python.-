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

user_number_1 = int(input('Введите нижнее число диапазона случайных чисел: '))
user_number_2 = int(input('Введите верхнее число диапазона случайных чисел: '))
random_number = int(random() * (user_number_2 - user_number_1)) + user_number_1
print(random_number)

user_float_number_1 = float(input('Введите нижнее число диапазона случайных чисел: '))
user_float_number_2 = float(input('Введите верхнее число диапазона случайных чисел: '))
random_float_number = random() * (user_float_number_2 - user_float_number_1) + user_float_number_1
print(random_float_number)

user_symbol_1 = ord(input('Введите нижнюю границу диапазона символов: '))
user_symbol_2 = ord(input('Введите верхнюю границу диапазона символов: '))
random_user_symbol = int(random() * (user_symbol_2 - user_symbol_1)) + user_symbol_1
print(chr(random_user_symbol))
