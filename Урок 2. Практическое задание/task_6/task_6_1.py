"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import random

quest_number = round(random() * 100)
user_tries = 1
print("Отгадайте число с 10 попыток")
while user_tries <= 10:
    try:
        user_answer = int(input(f'{user_tries} попытка: '))
        if user_answer < quest_number:
            print('Загаданное число больше')
        elif user_answer > quest_number:
            print('Загаданное число меньше')
        elif user_answer == quest_number:
            print(f'Вы отгадали, правильный ответ {quest_number}')
            break
        user_tries += 1
    except ValueError:
        print('Введите число от 1 до 100')
else:
    print(f'Вы проиграли, правильный ответ {quest_number}')


