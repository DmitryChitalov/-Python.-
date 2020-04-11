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


# Вариант 1 - ООП
class HexNum:
    def __init__(self, hex_str):
        self.hex_list = list(hex_str)

    def __add__(self, obj):
        add_int = int("".join(self.hex_list), 16) + int("".join(obj.hex_list), 16)
        return list(hex(add_int).upper()[2:])

    def __mul__(self, obj):
        mul_int = int("".join(self.hex_list), 16) * int("".join(obj.hex_list), 16)
        return list(hex(mul_int).upper()[2:])


num1 = HexNum(input("Введите первое число: "))
num2 = HexNum(input("Введите второе число: "))

print(f"Сумма чисел - {num1 + num2}")
print(f"Произведение чисел - {num1 * num2}")


# Вариант 2 - Collections
import collections

nums = collections.defaultdict(list)
nums['num1'] = list(input("Введите первое число: "))
nums['num2'] = list(input("Введите первое число: "))
nums['sum'] = list(hex(int("".join(nums['num1']), 16) + int("".join(nums['num2']), 16)).upper()[2:])
nums['mul'] = list(hex(int("".join(nums['num1']), 16) * int("".join(nums['num2']), 16)).upper()[2:])

print(f"Сумма чисел - {nums['sum']}")
print(f"Произведение чисел - {nums['mul']}")
