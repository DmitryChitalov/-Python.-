"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import random
N = round(random() * 100)
i = 1
print("The computer made up a number. Guess it. You have 10 attempts")
while i <= 10:
    U = int(input(str(i) + ' attempt: '))
    if U > N:
        print(f'Less')
    elif U < N:
        print(f'More')
    else:
        print(f'You use %d attempts' % i)
        break
    i += 1
else:
    print(f'You used all attempts. Integer was {N}')
