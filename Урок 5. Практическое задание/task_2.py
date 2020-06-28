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


def hex_input(i):
    try:
        num = input(f'Введите {i} число в шестнадцатиричной системе исчисления:')
        tmp = int(num, 16)
        return list(num)
    except ValueError:
        print('Это не похоже на число в шестнадцатиричной системе исчисления! ')
        return hex_input(i)


A = hex_input('первое')
B = hex_input('второе')

Hex = collections.namedtuple('Hex', 'a b')
numbers = Hex(a=A, b=B)
sum_num = list((str(hex(int(''.join(numbers.a), 16) + int(''.join(numbers.b), 16)))[2:].upper()))
multi_num = list((str(hex(int(''.join(numbers.a), 16) * int(''.join(numbers.b), 16)))[2:].upper()))

print('Сумма чисел:', sum_num)
print('Произведение', multi_num)

# 2 версия


class HexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return list((str(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16)))[2:].upper()))

    def __mul__(self, other):
        return list((str(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16)))[2:].upper()))


a = HexNumber(A)
b = HexNumber(B)

print('Перегрузка операторов')
print('Сумма чисел:', a + b)
print('Произведение', a * b)