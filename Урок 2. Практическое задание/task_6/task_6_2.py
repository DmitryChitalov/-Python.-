"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import randint


ANSWER = randint(1, 100)


def recur_count(i, user_answer):
    if i == 0:
        print("Попытки кончились!")
    if user_answer == ANSWER:
        print("Вы угадали!")
    if user_answer != ANSWER:
        if user_answer > ANSWER:
            print("Меньше!")
        else:
            print("Больше!")
        i = i - 1
        user_answer = int(input("Введите число: "))
        return recur_count(i, user_answer)


recur_count(10, 50)
