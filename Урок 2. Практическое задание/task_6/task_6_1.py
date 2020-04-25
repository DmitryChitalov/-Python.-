"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import random

number = random.randint(1, 100)
#Если нельзя использовать randint, то число можно найти так import math -> number = math.trunc(random.random() * 100)
count = 0
max_count = 10
is_winner = False

while not is_winner:
    count += 1
    if count > max_count:
        print(f'Вы проиграли! Было загадано число {number}')
        break

    print(f'Попытка номер {count}')
    user_number = int(input('Введите число: '))
    if user_number == number:
        is_winner = True
        break
    elif number < user_number:
        print('Ваше число больше загаданного!')
    else:
        print('Ваше число меньше загаданного!')
else:
    print('ПОБЕДА!')