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
    numbers = input('Введите два целых числа через пробел:')
    n1, n2 = numbers.split(' ')
    n1 = int(n1)
    n2 = int(n2)
    rand_numb = int(random() * (n2 - n1)) + n1
    print(rand_numb)
except ValueError:
    print('Введите корректные ЧИСЛА')

try:
    numbers = input('Введите нижнюю и верхнюю границу через пробел:')
    n1, n2 = numbers.split(' ')
    n1 = float(n1)
    n2 = float(n2)
    rand_numb = random() * (n2 - n1) + n1
    print(round(rand_numb, 3))
except ValueError:
    print('Введите ЧИСЛА')

try:
    letters = input('Введите две разные буквы через пробел:')
    n1, n2 = letters.split(' ')
    n1 = ord(n1)
    n2 = ord(n2)
    rand_letter = int(random() * (n2 - n1 + 1)) + n1
    print(chr(rand_letter))
except BaseException:
    print('Введите ДВЕ БУКВЫ')
