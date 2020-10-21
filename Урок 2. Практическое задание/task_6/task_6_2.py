"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
import random


def big_quest(the_n, val, min_n=1, max_n=100):
    if the_n == 0:
        print('Все попытки исчерпаны. Ты неудчник и самое слабое звено!!!')
        return
    try:
        users_val = int(
            input(f'Осталось {the_n} попыток. Введите число [{min_n}..{max_n}]: '))
        if users_val == val:
            print('Поздравляю, кожанный мешок, ты угадал!!')
            return
        if users_val < val:
            print('Ваше число меньше загаданного')
            big_quest(
                the_n - 1,
                val,
                users_val if users_val > min_n else min_n,
                max_n)
        else:
            print('Ваше число меньше загаданного')
            big_quest(
                the_n - 1,
                val,
                min_n,
                users_val if users_val < max_n else max_n)
    except ValueError:
        print('Пф...Надо вводить натуральное число!!')
        big_quest(the_n, val, min_n, max_n)
    except Exception:
        print('Что-то пошло не так... на всякий случай завершаю игру')


big_quest(10, round(random.random() * 100))
