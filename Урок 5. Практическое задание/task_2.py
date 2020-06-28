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
from collections import Counter

a = input('Введите первое шестнадцатиричное число: ').upper()
b = input('Введите второе шестнадцатиричное число: ').upper()

c = [el for el in a]
d = [en for en in b]
c.reverse()
d.reverse()
di = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert(x):
    dec_x = []
    for el in x:
        if di.get(el) is None:
            dec_x.append(int(el) * (16 ** x.index(el)))
        else:
            dec_x.append(di.get(el) * (16 ** x.index(el)))
    result = sum(dec_x)
    dec_x.clear()
    return result


def sum_hex(x, y):
    i = convert(x)
    j = convert(y)
    g = i + j
    l = g
    conv_sum = []
    while True:
        if l // 16 != 0:
            l = l // 16
            k = g - 16 * l
            g = l
            conv_sum.append(k)
        else:
            conv_sum.append(g)
            break
    f = []
    for h in conv_sum:
        if h < 10:
            f.append(h)
        for key in di:
            if di[key] == h:
                f.append(key)
    f.reverse()
    return print(f)


def mult_hex(x, y):
    i = convert(x)
    j = convert(y)
    g = i * j
    l = g
    conv_sum = []
    while True:
        if l // 16 != 0:
            l = l // 16
            k = g - 16 * l
            g = l
            conv_sum.append(k)
        else:
            conv_sum.append(g)
            break
    f = []
    for h in conv_sum:
        if h < 10:
            f.append(h)
        for key in di:
            if di[key] == h:
                f.append(key)
    f.reverse()
    return print(f)


sum_hex(c, d)
mult_hex(c, d)
