"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""


from random import randint

try:
    count = int(input("Введите количество элементов в массиве: "))
    my_list = [randint(0, 100) for i in range(0, count)]

    min_idx = my_list.index(min(my_list))
    max_idx = my_list.index(max(my_list))
    result_sum = 0

    for i in range(min([min_idx, max_idx]) + 1, max([min_idx, max_idx])):
        result_sum += my_list[i]

    print(f"Массив: {my_list}")
    print(f"Сумма элементов между минимальным ({my_list[min_idx]}) и "
          f"максимальным ({my_list[max_idx]}) элементами: {result_sum}")
except ValueError as err:
    print(f"Неверное значение:\n{err}")
