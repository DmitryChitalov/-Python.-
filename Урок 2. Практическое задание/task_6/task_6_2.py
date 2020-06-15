"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import randint

RANDOM_NUMBER = randint(0, 100)


def guess_the_number(attempts):
    """Угадай число

    attempts - количество попыток
    user_num - число пользователя
    RANDOM_NUMBER - рандомное число
    """
    if not attempts:
        print(f"К сожалению Вы не отгадали число. "
              f"Правильное число: {RANDOM_NUMBER}")
        return
    try:
        user_num = int(input("Введите предполагаемое чило: "))
    except ValueError:
        print(f"Необходимо вводить число! Осталось попыток {attempts - 1}")
        return guess_the_number(attempts - 1)
    if user_num == RANDOM_NUMBER:
        print(f"Вы угадали! Это чилсло: {RANDOM_NUMBER}")
        return
    if user_num < RANDOM_NUMBER:
        print(
            f"Вы вели неверное число. Правильное число больше чем {user_num}. "
            f"\nОсталось {attempts-1} попыток")
    else:
        print(
            f"Вы вели неверное число. Правильное число меньше чем {user_num}. "
            f"\nОсталось {attempts-1} попыток")
    return guess_the_number(attempts - 1)


print("Угадайте число от 0 до 100")


guess_the_number(10)
