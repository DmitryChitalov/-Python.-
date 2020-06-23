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
from collections import defaultdict


def dec_to_hex(n):
    let = '0123456789ABCDEF'
    if n <= 15:
        return let[n]
    return f'{dec_to_hex(n // 16)}{let[n%16]}'


def task_2():
    d = defaultdict(list)
    l = list()
    l.append(input('Введите первое число в 16 системе счисления: '))
    l.append(input('Введите второе число: '))
    l.append(dec_to_hex(int(l[0], 16) + int(l[1], 16)))
    l.append(dec_to_hex(int(l[0], 16) * int(l[1], 16)))
    for i, el in enumerate(l):
        for j in el:
            d[i].append(j)
    return f'Элементы {d[0]} и {d[1]}\n' \
           f'Сумма элементов: {d[2]}\n' \
           f'Произведение элементов: {d[3]}\n'


class Hex:
    def __init__(self, s='0'):
        self.s = s

    def __add__(self, other):
        result = Hex()
        result.s = dec_to_hex(int(self.s, 16) + int(other.s, 16))
        return result

    def __mul__(self, other):
        result = Hex()
        result.s = dec_to_hex(int(self.s, 16) * int(other.s, 16))
        return result

    def __str__(self):
        return f'{list(self.s)}'


try:
    print(task_2())

    s1 = Hex(input('Введите первое число в 16 системе счисления: '))
    s2 = Hex(input('Введите второе число: '))
    print(f'Элементы {s1} и {s2}\n'
          f'Сумма элементов: {s1 + s2}\n'
          f'Произведение элементов: {s1 * s2}')
except ValueError:
    print('Введено неверное 16-ое число')
except Exception as e:
    print(e)
