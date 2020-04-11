"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import deque

CONST_COUNT = 16

HEX_NUM = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'A', 'B', 'C', 'D', 'E', 'F')

BIN_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_sum(first, second):

    first = first.copy()
    second = second.copy()

    if len(first) < len(second):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    res = deque()
    overflow = 0
    while len(first) != 0:
        first_num = BIN_NUM[first.pop()]
        second_num = BIN_NUM[second.pop()]

        res_num = first_num + second_num + overflow

        if res_num >= CONST_COUNT:
            overflow = 1
            res_num -= CONST_COUNT
        else:
            overflow = 0

        res.appendleft(HEX_NUM[res_num])

    if overflow == 1:
        res.appendleft('1')

    return res


user_first = deque(input('Введите превое число в hex формате (от 0 до F): ').upper())
user_second = deque(input('Введите второе число в hex формате (от 0 до F): ').upper())
print(f'Сумма {user_first} и {user_second} равняется {hex_sum(user_first, user_second)}')





