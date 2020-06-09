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
import random

left_border = input('левая граница: ')
right_border = input('правая граница: ')
try:
    if left_border > right_border:
        left_border, right_border = right_border, left_border

    if len(left_border) == len(right_border) == 1:
        print(chr(round(ord(left_border) + random.random()
                        * (ord(right_border) - ord(left_border)))))
    else:
        print('Невозможно сопределить граници символьного диапазона')

    left_border = float(left_border)
    right_border = float(right_border)
    print(
        f'Целое случайное из диапазона '
        f'{round(left_border + random.random() * (right_border - left_border))}')
    print(
        f'Вещественное случайное из диапазона '
        f'{left_border + random.random() * (right_border - left_border)}')
except ValueError:
    print('Невозможно сопределить числовые граници диапазона')
