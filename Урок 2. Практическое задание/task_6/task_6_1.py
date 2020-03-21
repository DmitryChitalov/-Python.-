"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import random


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено целое
def input_number(l_try_left):
    while True:
        try:
            num = input(f"Введите число от 0 до 100. Осталось {l_try_left} попыток\n")
            num = int(num)
            if 0 <= num <= 100:
                break
            else:
                print('Введено некорректное число')
        except ValueError:
            print("Не удалось преобразовать в число")
    return num


answer = random.randint(0, 100)
try_left = 10
while True:
    if try_left == 0:
        break
    number = input_number(try_left)
    try_left -= 1
    if number < answer:
        print('Больше')
    elif number > answer:
        print('Меньше')
    else:
        print(f'Вы отгадали число {answer}')
        break;
if number != answer:
    print(f'Было загадано число {answer}')