"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import random

num_rand = random.randint(0, 100)

count = 10

while True:
    while True:
        num_user = input("Enter your number: ")
        if num_user.isdigit():
            num_user = int(num_user)
            break
        else:
            print("Invalid number. Repeat entry.")
    if num_user == num_rand:
        print(f"Congratulations! You guessed! This is the number {num_rand}")
        break
    else:
        count -= 1
        if count == 0:
            print(f"Wrong. You used all the attempts. That was the number {num_rand}")
            break
        elif num_rand < num_user:
            print("Wrong. Your number is greater. Try again.")
        else:
            print("Wrong. Your number is less. Try again.")
