"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from random import random


def recursuion_guess(number, try_count):
    """
    Get number to guess and max try count.
    Compare user input and return reply depending on input.
    """
    try:
        if try_count != 0:
            user_number = int(input('Введите число: '))
            if user_number < 0 or user_number > 100:
                print('Число должно быть от 0 до 100.')
                recursuion_guess(number, try_count)
                return
            try_count -= 1
            if user_number > number:
                print(f'Ваше число слишком большое.', end=' ')
                print(f'У вас {try_count} попыткок(-и/а)' if try_count else '')
            elif user_number < number:
                print(f'Ваше число слишком маленькое.', end=' ')
                print(f'У вас {try_count} попыткок(-и/а)' if try_count else '')
            else:
                print('Вы угадали!')
                return
            recursuion_guess(number, try_count)
        else:
            print(f'Попытки закончились. Загаданное число: {number}')
            return
    except ValueError as err:
        print(f'Неверный ввод, ошибка: {err}')
        recursuion_guess(number, try_count)


MIN = 0
MAX = 100
PC_NUMBER = int(random() * (MAX - MIN + 1) + MIN)
TRY_COUNT = 10  # Максимальное число попыток

recursuion_guess(PC_NUMBER, TRY_COUNT)
