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


class HexNum:
    """
    Hexadecimal
    """
    def __init__(self, hex_num):
        self.hex_num = deque(hex_num)

    def __str__(self):
        return ''.join(self.hex_num)

    def __add__(self, other):
        # производим поразрядное сложение
        transfer = 0
        result = deque()
        for i in range(max(len(self.hex_num), len(other.hex_num))):
            value_a = int(self.hex_num[-i-1], 16) if len(self.hex_num) > i else 0
            value_b = int(other.hex_num[-i-1], 16) if len(other.hex_num) > i else 0
            value_c = value_a + value_b + transfer
            transfer = 1 if value_c > 16 else 0
            value_c = value_c - 16 if value_c > 16 else value_c
            result.appendleft(f"{value_c:X}")
        if transfer:
            result.appendleft('1')
        return HexNum("".join(result))

    def __mul__(self, other):
        # здесь порязрядное умножение не стал реализовывать - использовал простое преобразование
        # предположил что для целей задачи достаточно реализации поразрядного __add__:
        # 1) применение коллекции из модуля collections
        # 2) применение знаний по перегрузке методов в ООП
        result = int(''.join(self.hex_num), 16) * int(''.join(other.hex_num), 16)
        return HexNum(f"{result:X}")


NUM_1 = HexNum('A2')
NUM_2 = HexNum('C4F')
print(f"{NUM_1} + {NUM_2} = {NUM_1 + NUM_2}")
print(f"{NUM_1} * {NUM_2} = {NUM_1 * NUM_2}")
