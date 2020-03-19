"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import randint

INCREMENT = 0
NUMBER = randint(0, 100)
while True:
    try:
        ANSWER = int(input(f'Отгадай число: '))
        INCREMENT += 1
    except ValueError:
        print(f'Ошибка ввода!')
    if NUMBER == ANSWER:
        print(f'Поздравляем вы угадали!\nКоличество попыток {INCREMENT}')
    elif NUMBER > ANSWER:
        print(f'Число {ANSWER} меньше загаданного.\nОсталось {10 - INCREMENT} попыток')
    else:
        print(f'Число {ANSWER} больше загаданного.\nОсталось {10 - INCREMENT} попыток')
    if INCREMENT == 10:
        print(f'Вы неугадали(\nЗагаданное число {NUMBER}')
        break
