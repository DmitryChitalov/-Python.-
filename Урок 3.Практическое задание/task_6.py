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


def input_count_el():
    """ Функция запрашивает и возвращает положительное количество введённое пользователем"""
    try:
        count_el = int(input("Введите количество элементов в массиве: "))
        if count_el < 0:
            raise ValueError("Вы ввели число меньше 0")
        return count_el
    except ValueError as exception:
        print(f"Нужно вводить положительное число!\n{exception}")
        return input_count_el()


COUNT_EL = input_count_el()
MASSIVE = [randint(-100, 100) for el in range(COUNT_EL)]
MAX_EL = max(MASSIVE)
MIN_EL = min(MASSIVE)
MAX_EL_IDX = MASSIVE.index(MAX_EL)
MIN_EL_IDX = MASSIVE.index(MIN_EL)
SUM_EL = sum(MASSIVE[MIN_EL_IDX + 1:MAX_EL_IDX] if MAX_EL_IDX > MIN_EL_IDX
             else MASSIVE[MAX_EL_IDX + 1:MIN_EL_IDX])

print(f"Массив: {MASSIVE}\n Сумма элементов между минимальным "
      f"({MIN_EL}) и максимальным ({MAX_EL}) элементами: {SUM_EL}")
