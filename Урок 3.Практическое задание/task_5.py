"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
base_list = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]

# def find_max_neg(base_list) -> list:
#     index = -1
#     for x in range(len(base_list)):
#         if base_list[x] and index == -1:
#             index = 1
#         elif 0 > base_list[x] > base_list[index]:
#             index = x
#     return [base_list[index], index]
#
#
# print(find_max_neg(base_list))


#  Solution from teacher

from random import randint


def task_5(lst_base):
    print(f"Базовый список: {lst_base}")
    lst = [el for el in lst_base if el < 0]
    print(f"Максимальный отрицательный элемент в данном массиве = {max(lst)}",
          f"его индекс {lst_base.index(max(lst))}")


LST_BASE = [randint(-100, 100) for i in range(10)]
task_5(LST_BASE)
