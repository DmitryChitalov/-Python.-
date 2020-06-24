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
import collections

# Решение через ООП и коллекцию
class MyIntHex:
    def __init__(self, list_value):
        self.hex_list = collections.deque(list_value)

    def __str__(self):
        return f'{self.hex_list}'

    def __add__(self, other):
        return list(hex(int(''.join(self.hex_list), 16) + int(''.join(other.hex_list), 16)))[2:]

    def __sub__(self, other):
        return list(hex(int(''.join(self.hex_list), 16) - int(''.join(other.hex_list), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.hex_list), 16) * int(''.join(other.hex_list), 16)))[2:]

    def __eq__(self, other):
        return True if int(''.join(self.hex_list), 16) == int(''.join(other.hex_list), 16) else False

    def __truediv__(self, other):
        return list(hex(int(''.join(self.hex_list), 16) // int(''.join(other.hex_list), 16)))[2:]

    @classmethod
    def from_str(cls, str_value):
        int(str_value, 16)
        return cls(list(str_value))


a = MyIntHex.from_str('EEEE')
b = MyIntHex.from_str('1111')
print(a, b, a+b, a*b, a/b, a==b, sep='\n')
