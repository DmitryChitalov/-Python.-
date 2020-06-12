"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import random


def recursive_guess(num=False, answer_count=1):
    try:
        if not num:
            num = int(random() * 101)
        if answer_count > 10:
            print(f'Вы не угадали, загаданое число - {answer_count}')
            return
        print(f'Попытка номер - {answer_count}')
        user_num = int(input('Введите число от 0 до 100: '))
        if user_num == num:
            print('Вы угадали!')
            return
        elif user_num > num:
            print('Введенное число больше загаданного')
        elif user_num < num:
            print('Введенное число меньше загаданного')
        return recursive_guess(num, answer_count + 1)
    except ValueError:
        print('Необходимо ввести целое число')


recursive_guess()
