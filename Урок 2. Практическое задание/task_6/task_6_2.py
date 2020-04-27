"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from random import random

# загдываем число
R_NUMBER = int(random() * 100)
MAX_TRIES = 10


# отгадываем число
def gessing(r_number, max_tries, user_try=1):
    """игра в угадайку"""
    if user_try != max_tries + 1:
        user_number = int(input(f'попытка {user_try}. Введите число от 0 до 100\n'))
        if user_number == r_number:
            return print("Вы угадали!!!")
        elif user_number > r_number:
            print("Ваше число больше загаднного\n")
            return gessing(r_number, max_tries, user_try + 1)
        else:
            print("Ваше число меньше загаднного\n")
            return gessing(r_number, max_tries, user_try + 1)
    else:
        return print(f"Вы не угадали, число было {r_number}")


# поехали
gessing(R_NUMBER, MAX_TRIES)
