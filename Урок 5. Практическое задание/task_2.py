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


class hexadecimal():

    def __init__(self, hex):

        self.hex = hex
        self.dec = self.hex_to_dec()
        self.list_hex = list(map(str, self.hex))

    def hex_to_dec(self):
        list_hex = list(map(str, self.hex))
        list_dec = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'),
                    (8, '8'), (9, '9'), (10, 'A'), (11, 'B'), (12, "C"), (13, "D"), (14, 'E'), (15, 'F'))
        dec = 0
        n = 0
        j = len(list_hex) - 1
        while n < len(list_hex):
            for item in list_dec:
                if list_hex[j] == item[1]:
                    dec += item[0] * 16 ** n
                    break
            n += 1
            j -= 1
        return dec

    def dec_to_hex(self, decnum):
        list_num = deque()  # коллекция
        list_dec = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'),
                    (8, '8'), (9, '9'), (10, 'A'), (11, 'B'), (12, "C"), (13, "D"), (14, 'E'), (15, 'F'))

        while decnum != 0:
            n = decnum % 16
            if n > 0:
                list_num.appendleft(list_dec[n][1])
            else:
                list_num.appendleft(str(n))
            decnum = decnum // 16
        return ''.join(list(list_num))

    def dec_to(self, decnum):  # рекурсия
        list_dec = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'),
                    (8, '8'), (9, '9'), (10, 'A'), (11, 'B'), (12, "C"), (13, "D"), (14, 'E'), (15, 'F'))
        if decnum == 0:
            return ''
        return f"{self.dec_to(decnum // 16)}{list_dec[decnum % 16][1]}"

    def __add__(self, other):
        return hexadecimal(self.dec_to_hex(self.dec + other.dec))

    def __mul__(self, other):
        return hexadecimal(self.dec_to_hex(self.dec * other.dec))

    def __str__(self):
        return self.hex


a = hexadecimal('A2')
print(a.dec_to_hex(162 + 162))
print(a.dec)
b = hexadecimal('C4F')
c = a + b
t = a * b
print(c)
print(t)
print(c.list_hex)
print(t.list_hex)
print(t.dec_to(162))
