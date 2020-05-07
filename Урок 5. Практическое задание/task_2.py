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

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def hex_sum(x, y):
    result = deque()
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = hex_dict[x.pop()] + hex_dict[y.pop()] + transfer
        else:
            res = hex_dict[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(hex_dict[res])
        else:
            result.appendleft(hex_dict[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return list(result)

def hex_mult(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)
    for i in range(len(y)):
        m = hex_dict[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * hex_dict[x[j]])
        for _ in range(i):
            spam[i].append(0)
    transfer = 0
    for _ in range(len(spam[-1])):
        res = transfer
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(hex_dict[res])
        else:
            result.appendleft(hex_dict[res % 16])
            transfer = res // 16
    if transfer:
            result.appendleft(hex_dict[transfer])
    return list(result)

a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(*a, '+', *b, '=', *hex_sum(a, b))
print(*a, '*', *b, '=', *hex_mult(a, b))

# Введите 1-е шестнадцатиричное число: AAA
# Введите 2-е шестнадцатиричное число: BBB
# A A A + B B B = 1 6 6 5
# A A A * B B B = 7 D 1 8 2 E