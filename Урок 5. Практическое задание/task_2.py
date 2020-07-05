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


class HexadecimalNumber:
    """ Класс для суммы и умножения 16-ных чисел"""

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print(self.num[0], other.num[0])
        return list(map(lambda x: x.upper() if x.isalpha() else x, list(
            hex(int(self.num[0], 16) + int(other.num[0], 16))[2:])))

    def __mul__(self, other):
        return list(map(lambda x: x.upper() if x.isalpha() else x, list(
            hex(int(self.num[0], 16) * int(other.num[0], 16))[2:])))


HEX_LIB = defaultdict(list)
HEX_LIB['num_1'].append(*(input("Введите первое число: ")).split())
HEX_LIB['num_2'].append(*(input("Введите второе число: ")).split())

HEX_NUM1 = HexadecimalNumber(HEX_LIB['num_1'])
HEX_NUM2 = HexadecimalNumber(HEX_LIB['num_2'])

print(
    f"Сумма чисел из примера: {HEX_NUM1 + HEX_NUM2}, произведение - {HEX_NUM1 * HEX_NUM2}")
