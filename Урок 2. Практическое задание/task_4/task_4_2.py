"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursive_summ(num, res_sum = 0.0, el = 1.0):
    if num == 0:
        return res_sum
    return recursive_summ(num - 1, res_sum + el, el / -2)


try:
    user_num = int(input('Введите целое число: '))
    print(f'Количество элементов - {user_num}, их сумма - {recursive_summ(user_num)}')
except ValueError:
   print('Необходимо ввести целое число')
