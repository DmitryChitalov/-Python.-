"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import randint

try:
    GUESS_NUMBER = randint(0, 100)
    ATTEMPT_COUNTER = 0
    while ATTEMPT_COUNTER < 11:
        NUMBER = int(input("Введите число от 0 до 100: "))
        if NUMBER > GUESS_NUMBER:
            print("Загаданное число меньше вашего")
        elif NUMBER < GUESS_NUMBER:
            print("Загаданное число больше вашего")
        else:
            print("Вы угадали число!")
            break
        ATTEMPT_COUNTER += 1
    else:
        print(f"Загаданное число {GUESS_NUMBER}")
except ValueError:
    print("Введите корректное значение")
