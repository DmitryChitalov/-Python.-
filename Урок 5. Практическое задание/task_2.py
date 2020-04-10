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

# Решение через коллекции

from collections import defaultdict
from functools import reduce


def def_dict():
    '''функция для проверки дефолтдикт'''
    dd_nums = defaultdict(list)
    nums = input('Введите числа в 16-тиричном виде через пробел: ').split()
    for i, num in enumerate(nums):
        dd_nums[i] = list(num.upper())
        print(f'Введенное число {i + 1}: {dd_nums[i]}')
    nums_oct = [int(''.join(num), 16) for num in dd_nums.values()]
    nums_sum_hex = hex(sum(nums_oct))[2:].upper()
    nums_mult_hex = hex(reduce(lambda x, y: x * y, nums_oct))[2:].upper()

    print(f'Сумма чисел: {list(nums_sum_hex)}')
    print(f'Произведение: {list(nums_mult_hex)}')


# Решение через классы
# с классами у меня пока не очень, но вроде норм получилось

class MyHex:
    '''мой хекс'''

    def __init__(self, x_value):
        self.x_value = x_value.upper()
        self.oct = int(x_value, 16)

    def __add__(self, obj):
        return MyHex(str(hex(self.oct + obj.oct)[2:].upper()))

    def __mul__(self, obj):
        return MyHex(str(hex(self.oct * obj.oct)[2:].upper()))

    def __str__(self):
        return str(self.x_value)


def my_hex():
    '''функция для проверки класса'''
    nums = input('Введите числа в 16-тиричном виде через пробел: ').split()
    # формируем из введенных строк список экземпляров MyHex
    nums = [MyHex(num) for num in nums]
    summ = sum(nums, MyHex('0'))
    mult = reduce(lambda x, y: x * y, nums)

    print(f'Введенные числа: {list(map(str, nums))}')
    print(f'Сумма чисел: {summ}')
    print(f'Произведение: {mult}')


def_dict()
my_hex()
