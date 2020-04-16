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

from collections import defaultdict, deque


class Hexnum:

    def __init__(self, name):
        self.name = name

    def save(self):
        self.name = list(self.name)

    def __add__(self, other):
        sum = int("".join(self.name), 16)+ int("".join(other.name), 16)
        return list(hex(sum).upper())[2:]

    def __mul__(self, other):
        sum = int("".join(self.name), 16) * int("".join(other.name), 16)
        return list(hex(sum).upper())[2:]


num1 = Hexnum(input("Введите первое 16-ное число: "))
num2 = Hexnum(input("Введите второе 16-ное число: "))

print(
    f'Сумма чисел - {num1 + num2}\n'
    f'Произведение чисел - {num1 * num2}'
)

def get_sum(num1, num2):
    num1 = "".join([i for i in num1])
    num2 = "".join([j for j in num2])
    s = hex(int(float.fromhex(num1) + float.fromhex(num2)))
    return f'Сумма чисел - {list(s.upper())[2:]}'


def get_mul(num1, num2):
    num1 = "".join([i for i in num1])
    num2 = "".join([j for j in num2])
    s = hex(int(float.fromhex(num1) * float.fromhex(num2)))
    return f'Произведение чисел - {list(s.upper())[2:]}'


NUM1 = deque(input("Введите первое 16-ричное число: "))
NUM2 = deque(input("Введите второе 16-ричное число: "))
print(get_sum(NUM1, NUM2))
print(get_mul(NUM1, NUM2))












