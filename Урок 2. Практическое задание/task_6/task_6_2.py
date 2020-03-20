"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

# импортируем модуль для генерации случайного числа
from random import random


def recursion(computer_number, count=1):
    """
    Функция принимает в виде значений загаданное число и счетчик
    Счетчик имеет значение по умолчанию
    :return: завершение рекурсии, вывод результата
    """
    if count <= 10:
        user_number = int(input(f'Отгадайте загаданное число. Попытка #{count}: '))
        if user_number == computer_number:
            print('Вы угадали!')
            return
        elif user_number < computer_number:
            print('Введенное число меньше загаданного.')
            count += 1
            recursion(computer_number, count)
        elif user_number > computer_number:
            print('Введенное число больше загаданного.')
            count += 1
            recursion(computer_number, count)
        else:
            print('Вы не угадали!')
            return
    else:
        print('Вы не угадали!')
        return


# генерируем случайное число от 0 до 100
COMPUTER_NUMBER = round(random() * 100)

# вызываем нашу функцию recursion
recursion(COMPUTER_NUMBER)
