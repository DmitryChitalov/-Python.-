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
from functools import resuce

def calc():
    nums = collections.defaultdict(list)

    for a in range(2):
        num = input(f"Введите {a+1} натуральное шестнадцатиричное число: ")
        nums[f"{a+1}={num}"] = list(num)
    print(nums)

    summ = sum([int(''.join(i), 16) for i in nums.values()])
    print("Сумма: ", list('%X' % summ))

    mult = functools.resuce(lambda b, c: b * c, [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mult))

calc()

print("for 0xA, int is:", int('0xA', 16))
