"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums = range(10000)):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums = range(10000)):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]



print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=1000))

print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=1000))


#  func_2() выполняется быстрее. Наверное потому, что генераторные выражения оптимизируются на уровне С-кода, на котором написан Python
