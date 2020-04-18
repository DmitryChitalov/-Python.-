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


USER_NUMBERS = defaultdict(list)
FIRST = input("Введите первое число: ")
SECOND = input("Введите второе число: ")
USER_NUMBERS[FIRST] = list(FIRST)
USER_NUMBERS[SECOND] = list(SECOND)


SUMM = hex(sum([int("".join(i), 16) for i in USER_NUMBERS.values()]))[2:]
MULT = hex(int("".join(USER_NUMBERS[FIRST]), 16) * int("".join(USER_NUMBERS[SECOND]), 16))[2:]

print(f"Сумма чисел {USER_NUMBERS[FIRST]} и {USER_NUMBERS[SECOND]} равна: {list(SUMM)}\n"
      f"Произведение чисел {USER_NUMBERS[FIRST]} и {USER_NUMBERS[SECOND]} равно: {list(MULT)}")
