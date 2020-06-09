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

from_num = input('Введите нижнее ограничение: ')
to_num = input('Введите верхнее ограничение: ')

try:
    print(int(random() * (int(to_num) - int(from_num) + 1)) + int(from_num))
except ValueError:
    try:
        print(random() * (float(to_num) - float(from_num) + 1) + float(from_num))
    except ValueError:
        try:
            if len(from_num) == 1 and len(to_num) == 1:
                print(chr(int(random() * (ord(to_num) - ord(from_num) + 1)) + ord(from_num)))
            else:
                print('Вы ввели больше одной буквы')
        except ValueError:
            print('Вы ввели недопустимое значение')
