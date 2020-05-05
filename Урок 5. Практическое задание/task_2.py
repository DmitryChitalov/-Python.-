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
    ALPHABET = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    add_one = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = ALPHABET[x.pop()] + ALPHABET[y.pop()] + add_one
        else:
            res = ALPHABET[x.pop()] + add_one
        add_one = 0
        if res < 16:
            result.appendleft(ALPHABET[res])
        else:
            result.appendleft(ALPHABET[res - 16])
            add_one = 1
    if add_one:
        result.appendleft('1')
    return list(result)

def mult_hex(x, y):
    ALPHABET = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)
    for i in range(len(y)):
        m = ALPHABET[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * ALPHABET[x[j]])
        for _ in range(i):
            spam[i].append(0)
    add_one = 0
    for _ in range(len(spam[-1])):
        res = add_one
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(ALPHABET[res])
        else:
            result.appendleft(ALPHABET[res % 16])
            add_one = res // 16
    if add_one:
        result.appendleft(ALPHABET[add_one])
    return list(result)


a = list(input('Enter a: ').upper())
b = list(input('Enter b: ').upper())

print(f"Sum: {''.join(sum_hex(a, b))}")

print(f"Mult: {''.join(mult_hex(a, b))}")

