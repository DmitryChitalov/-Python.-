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

print('Случайное целое число из диапазона пользователя')
try:
    LEFT = int(input("Минимальная граница: "))
    RIGHT = int(input("Максимальная граница: "))
    if LEFT > RIGHT:
        LEFT, RIGHT = RIGHT, LEFT
        print(f'Максимальная граница должна быть больше минимальной!\n'
              f'Меняем их местами, дапазон стал от {LEFT} до {RIGHT}.')
    NUMB = int(random() * (abs(RIGHT - LEFT) + 1)) + LEFT
    print(NUMB)
except ValueError as err:
    print(f'Некорректный ввод! Ошибка: {err}')

print('Случайное вещественное число из диапазона пользователя')
try:
    LEFT = float(input("Минимальная граница: "))
    RIGHT = float(input("Максимальная граница: "))
    if LEFT > RIGHT:
        # LEFT, RIGHT = RIGHT, LEFT # тут менять местами не обязательно
        print(f'Максимальная граница должна быть больше минимальной!\n'
              f'Меняем их местами, дапазон стал от {RIGHT} до {LEFT}.')
    NUMB = random() * (RIGHT - LEFT) + LEFT
    print(round(NUMB, 3))
except ValueError as err:
    print(f'Некорректный ввод! Ошибка: {err}')

print('Случайный символ из диапазона пользователя')
try:
    LETTER_1 = ord(input('Минимальная граница (от "a" до "z"): '))
    LETTER_2 = ord(
        input(f'Максимальная граница (от "{chr(LETTER_1)}" до "z"): '))
    if not (97 <= LETTER_1 <= 122 and 97 <= LETTER_2 <= 122):
        raise ValueError('Символы должны быть от "a" до "z"')
    if LETTER_1 > LETTER_2:
        LETTER_1, LETTER_2 = LETTER_2, LETTER_1
        print(
            f'Максимальная граница должна быть больше минимальной!\n'
            f'Меняем их местами, дапазон стал от {chr(LETTER_1)} до {chr(LETTER_2)}.')
    SYMB = int(random() * (LETTER_2 - LETTER_1 + 1)) + LETTER_1
    print(chr(SYMB))
except ValueError as err:
    print(f'Некорректный ввод! Ошибка: {err}')
except TypeError as err:
    print(f'Некорректный ввод! Ошибка: {err}')

"""

Последнее задание можно было бы сделать с помощью random.choice(),
но в примечании к заданию написано, что массивами пользоваться нельзя,
а строка уж очень похожа на массив.

Текст программы был бы такой:

from random import choice

print('Случайный символ из диапазона пользователя')
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
try:
    LETTER_1 = input('Минимальная граница: ')
    LETTER_2 = input(f'Максимальная граница: ')
    if LETTER_1 not in ALPHABET or LETTER_2 not in ALPHABET:
        raise ValueError('Символы должны быть от "a" до "z"')
    if LETTER_1 > LETTER_2:
        LETTER_1, LETTER_2 = LETTER_2, LETTER_1
        print(f'Максимальная граница должна быть больше минимальной!\n'
              f'Меняем их местами, дапазон стал от {LETTER_1} до {LETTER_2}.')
    SYMB = choice(ALPHABET[ALPHABET.find(LETTER_1):ALPHABET.find(LETTER_2) + 1])
    print(SYMB)
except ValueError as err:
    print(f'Некорректный ввод! Ошибка: {err}')
except IndexError as err:
    print(f'Некорректный ввод! Ошибка: {err}')

"""