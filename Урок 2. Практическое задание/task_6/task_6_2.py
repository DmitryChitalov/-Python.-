"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import random


def quest_number_func(quest_number, user_tries=1):
    if user_tries > 10:
        return print(f'Игра окончена, правильный ответ {quest_number}')
    try:
        user_answer = int(input(f'{user_tries} попытка: '))
        if user_answer < quest_number:
            print('Загаданное число больше')
        elif user_answer > quest_number:
            print('Загаданное число меньше')
        elif user_answer == quest_number:
            print(f'Вы отгадали, правильный ответ {quest_number}')
            user_tries = 10
        user_tries += 1
        quest_number_func(quest_number, user_tries)
    except ValueError:
        print('Введите число от 1 до 100')
        quest_number_func(quest_number, user_tries)


quest_number_func(round(random() * 100))
