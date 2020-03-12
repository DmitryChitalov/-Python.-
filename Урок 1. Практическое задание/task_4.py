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


from random import random, choice
import string

try:
    LEFT = int(input("Min value of positive integer: "))
    RIGHT = int(input("Max value of positive integer: "))
    NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
    print(NUMB)

    LEFT = float(input("Min value of real number: "))
    RIGHT = float(input("Max value of real number: "))
    NUMB = random() * (RIGHT - LEFT) + LEFT
    print(NUMB)

    LEFT = ord(input("First letter: "))
    RIGHT = ord(input("Second letter: "))
    NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
    print(chr(NUMB))

except ValueError:
    print('Incorrect')
