"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from random import randint

RANDOM_INT = randint(0, 100)
TRY_COUNT = 10


def recursive_game():

    global RANDOM_INT, TRY_COUNT

    if TRY_COUNT > 0:
        answer = int(input("Введите число от 0 до 100\n"))

        if answer == RANDOM_INT:
            print(f"Вы выйграли\nПравильный ответ - {answer}")
        elif answer > RANDOM_INT:
            print("Вы ввели слишком большое число\nПопробуйте ещё раз")
            TRY_COUNT -= 1
            recursive_game()
        else:
            print("Вы ввели слишком маленькое число\nПопробуйте ещё раз")
            TRY_COUNT -= 1
            recursive_game()
    else:
        print(f"Вы проиграли\nПравильный ответ - {RANDOM_INT}")


recursive_game()
