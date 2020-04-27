"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import random


def unknown_number(user_num, count):
    if count == 10:
        return print(f'Вы не угадали. Загаданное число: {NUMBER}')
    elif user_num < NUMBER:
        print(f'Ваше число меньше. У вас осталось {10 - count} попыток.')
        return unknown_number(int(input('Введите число: ')), count=count + 1)
    elif user_num > NUMBER:
        print(f'Ваше число больше. У вас осталось {10 - count} попыток.')
        return unknown_number(int(input('Введите число: ')), count=count + 1)
    else:
        print('Поздравляю! Вы угадали!')
        return


NUMBER = int(random() * 100)
unknown_number(int(input('Введите число: ')), count=1)
