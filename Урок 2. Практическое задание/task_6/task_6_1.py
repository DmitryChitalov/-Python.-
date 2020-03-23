"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import random


def cycle_method():
    numb = random.randint(0, 100)
    count = 1

    while count < 11:
        print(f'Try number {count}')
        user_answer = int(input('Введите число от 0 до 100: '))
        if user_answer != numb:
            if user_answer < numb:
                print(f'Введенное Вами число меньше')
            elif numb > user_answer:
                print(f'Введенное Вами число больше')
        else:
            print(f'Вы угадали!')
            break
        count += 1
    return numb


print(f'Сгенерированное число - {cycle_method()}')

