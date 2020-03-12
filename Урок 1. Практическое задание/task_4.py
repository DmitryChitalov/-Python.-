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


def randon_int() -> None:
    """ Генерируем случайное целое число из положительного или отрицательного диапазона,
        при условии что правая граница больше левой
    """
    print('\n Генерируем случайное целое число')
    try:
        left_int = int(input('Введите минимальную границу: ').strip())
        right_int = int(input('Введите максимальную границу: ').strip())
        if right_int >= left_int:
            rand_num = int(random() * (right_int - left_int + 1) + left_int)
        else:
            rand_num = int(random() * (left_int - right_int - 1) - left_int)
        print(
            f'Случайное целое число в гаринцах от {left_int} до {right_int} = {rand_num}')
    except ValueError as err:
        print('Введенное Вами значение не является корректным числом')
        print('Ошибка: ', err)


def random_float() -> None:
    """ Генерируем случайное вещественное число из положительного или отрицательного диапазона,
        при условии что правая граница больше левой
    """
    print('\n Генерируем случайное вещественное число')
    try:
        left_float = float(input('Введите минимальную границу: ').strip())
        right_float = float(input('Введите максимальную границу: ').strip())
        if right_float >= left_float:
            rand_num = round(
                (float(random() * (right_float - left_float) + left_float)), 2)
        else:
            rand_num = round(
                (float(random() * (left_float - right_float) - left_float)), 2)
        print(
            f'Случайное вещественное число в гаринцах'
            f' от {left_float} до {right_float} = {rand_num}')
    except ValueError as err:
        print('Введенное Вами значение не является корректным числом')
        print('Ошибка: ', err)


def random_char() -> None:
    """ Генерируем случайный символ как при прямом так и при обратном порядке символов"""
    print('\n Генерируем случайный символ')
    try:
        left_char = ord(input('Введите минимальную границу: ').strip())
        right_char = ord(input('Введите максимальную границу: ').strip())
        if right_char >= left_char:
            rand_char = chr(
                int(random() * (right_char - left_char + 1) + left_char))
        else:
            rand_char = chr(
                abs(int(random() * (left_char - right_char - 1) - left_char)))
        print(
            f'Случайное символ в гаринцах от {chr(left_char)} до {chr(right_char)} = {rand_char}')
    except TypeError as err:
        print('Введенное Вами значение не является корректным символом')
        print('Ошибка: ', err)


if __name__ == "__main__":
    randon_int()
    random_float()
    random_char()
