"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


import random


def num_enter():
    num_user = input("Enter your number: ")
    if num_user.isdigit():
        return int(num_user)
    else:
        print("Invalid number. Repeat entry.")
        return num_enter()


def guess_number(num_rand=random.randint(0, 100), count=10):
    num_user = num_enter()
    if num_user == num_rand:
        print(f"Congratulations! You guessed! This is the number {num_rand}")
        return
    count -= 1
    if count == 0:
        print(f"Wrong. You used all the attempts. "
              f"That was the number {num_rand}")
        return
    elif num_rand < num_user:
        print("Wrong. Your number is greater. Try again.")
        guess_number(num_rand, count)
    else:
        print("Wrong. Your number is less. Try again.")
        guess_number(num_rand, count)


guess_number()

