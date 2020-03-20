"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import randint

N = randint(0, 100)
P = 0
print(N)

print('Угадайте число от 0 до 100.\nУ вас 10 попыток')

while P <= 10:
    try:
        t = int(input('Угадайте'))
    except ValueError:
        print('Это не число.')
    else:
        if t < N:
            P += 1
            print('маленькое')
        elif t == N:
            print('Вы угадали!')
            break
        else:
            P += 1
            print('Большое')
