"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import random

def compare_numbers(try_count, number):
    try:
        if try_count <= 10:
            user_number = int(input(f"Попытка {try_count}. Ваше число: "))
            if user_number == number:
                return print(f"Ура! Вы отгадали число за {try_count} попыток!")
            if user_number > number:
                print("Ваше число больше загаданного.")
            elif user_number < number:
                print("Ваше число меньше загаданного.")
            compare_numbers(try_count+1, number)
        else:
            print(f"Увы, вы програли. Загаданное число {number}.")
    except ValueError:
        print("Вы ввели не число.")

print("Компьютер загадал число от 0 до 100. Попробуйте угадать его за 10 попыток.")
compare_numbers(1, int(random() * 100))
