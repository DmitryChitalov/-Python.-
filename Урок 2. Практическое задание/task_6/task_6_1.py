"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import random

MIN = 0
MAX = 100
PC_NUMBER = int(random() * (MAX - MIN + 1) + MIN)
MAX_COUNT = 10  # Максимальное число попыток
while MAX_COUNT > 0:
    try:
        USER_NUMBER = int(input('Введите число: '))
        if USER_NUMBER < 0 or USER_NUMBER > 100:
            print('Число должно быть от 0 до 100.')
            continue
        MAX_COUNT -= 1
        if USER_NUMBER == PC_NUMBER:
            print('Вы угадали!')
            break
        if USER_NUMBER > PC_NUMBER:
            print(f'Ваше число слишком большое.', end=' ')
            print(f'У вас {MAX_COUNT} попыткок(-и/а)' if MAX_COUNT else '')
        elif USER_NUMBER < PC_NUMBER:
            print(f'Ваше число слишком маленькое.', end=' ')
            print(f'У вас {MAX_COUNT} попыткок(-и/а)' if MAX_COUNT else '')
    except ValueError as err:
        print(f'Неверный ввод, ошибка: {err}')
        continue
else:
    print(f'Загаданное число {PC_NUMBER}')
