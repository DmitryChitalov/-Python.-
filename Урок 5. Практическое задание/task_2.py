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


def sum_hex(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
               }
    
    RESULT = deque()
    TRANSFER = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + TRANSFER
        else:
            res = HEX_NUM[x.pop()] + TRANSFER
        TRANSFER = 0

        if res < 16:
            RESULT.appendleft(HEX_NUM[res])
        else:
            RESULT.appendleft(HEX_NUM[res - 16])
            TRANSFER = 1

    if TRANSFER:
        RESULT.appendleft('1')

    return list(RESULT)


def mult_hex(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
               }
    RESULT = deque()
    TMP = deque([deque() for _ in range(len(y))])       #Временное хранилище для представления числа 'b'
    # print(TMP)

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = HEX_NUM[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            TMP[i].appendleft(m * HEX_NUM[x[j]])
        for _ in range(i):
            TMP[i].append(0)
    TRANSFER = 0

    for _ in range(len(TMP[-1])):
        res = TRANSFER

        for i in range(len(TMP)):
            if TMP[i]:
                res += TMP[i].pop()
        if res < 16:
            RESULT.appendleft(HEX_NUM[res])
        else:
            RESULT.appendleft(HEX_NUM[res % 16])
            TRANSFER = res // 16
    if TRANSFER:
            RESULT.appendleft(HEX_NUM[TRANSFER])

    return list(RESULT)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())

b = list(input('Введите 2-е шестнадцатиричное число: ').upper())
print(a, b)

print(*a, '+', *b, '=', *sum_hex(a, b))

print(*a, '*', *b, '=', *mult_hex(a, b))