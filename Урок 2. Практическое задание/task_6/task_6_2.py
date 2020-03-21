"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
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


# Отгадываем число. Передается ответ и количество оставшихся попыток. Выходим, если отгадали или кончились попытки
def guess_game(answer, try_left):
    number = input_number(try_left)
    if try_left == 0:
        print(f'Было загадано число {answer}')
        return
    if number == answer:
        print(f'Вы отгадали число {answer}')
        return
    elif number > answer:
        print('Меньше')
    else:
        print('Больше')
    guess_game(answer, try_left - 1)


guess_game(random.randint(0, 100), 10)
