"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursive_value_count(value):
    global COUNT, COUNT_NUMBER
    if value != 0:
        if value % 10 == COUNT_NUMBER:
            COUNT += 1
        recursive_value_count(value // 10)


def recursive_count(n):

    global COUNT_NUMBER, COUNT, NUMBERS
    if n == 0:
        print(f"Было введено {COUNT} цифр {COUNT_NUMBER}")
    else:
        value = int(input(f"Число {NUMBERS - n + 1} "))
        recursive_value_count(value)
        recursive_count(n-1)


NUMBERS = int(input("Сколько будет чисел?\n"))
COUNT_NUMBER = int(input("Какую цифру считать?\n"))
COUNT = 0

recursive_count(NUMBERS)