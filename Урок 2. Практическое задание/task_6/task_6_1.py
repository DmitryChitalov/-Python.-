"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import random


COUNT_ATTEMPTS = int(input("Количество попыток: "))
RAND = int(random() * 100)
print(RAND)
while True:
    while True:
        NUM = input("Введите число: ")
        if NUM.isdigit():
            NUM = int(NUM)
            break
        print("Неверно введено число")
        continue

    if NUM > RAND:
        print("Вы ввели большое число")
    if NUM < RAND:
        print("Вы ввели маленькое число")
    if NUM == RAND:
        print("Угадали")
        break
    if COUNT_ATTEMPTS == 1:
        print("Вы не угадали")
        break
    COUNT_ATTEMPTS = COUNT_ATTEMPTS - 1
