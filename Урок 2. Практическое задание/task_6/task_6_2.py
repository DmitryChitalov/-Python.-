"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
import random


def recur_method(count, numb):
    print(f"Attempt № {count}")
    answer = int(input("Enter a number from 0 to 100: "))
    if count == 10 or answer == numb:
        if answer == numb:
            print("You are right!")
        print(f"Guessed number was: {numb}")
    else:
        if numb > answer:
            print(f"Guessed number is greater then {numb}")
        else:
            print(f"Guessed number is less then {numb}")
        recur_method(count + 1, numb)


recur_method(1, random.randint(0, 100))
