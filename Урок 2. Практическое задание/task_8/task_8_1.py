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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def count_value(value):

    global COUNT, COUNT_NUMBER

    while value > 0:
        if value % 10 == COUNT_NUMBER:
            COUNT += 1
        value = value // 10


NUMBERS = int(input("Сколько будет чисел?\n"))
COUNT_NUMBER = int(input("Какую цифру считать?\n"))
COUNT = 0


for I in range(0, NUMBERS):
    VALUE = int(input(f"Число {I + 1} "))
    count_value(VALUE)


print(f"Было введено {COUNT} цифр {COUNT_NUMBER}")
