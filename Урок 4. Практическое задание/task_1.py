"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit
import cProfile
from random import randint

# Для начала рассмотрим программу, состоящую из атомарных действия над числами
# Это урок 1, задание 2
# Эта программа имеет константную сложность O(7), которая зависит от количества операций,
# но не от входных данных
# Проверим это:


def bit_operations(a_val: int, b_val: int) -> int:
    """
    Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
    и др. над числами 5 и 6. Выполнить
    над числом 5 побитовый сдвиг вправо и влево на два знака.
    """
    result = a_val & b_val
    result = a_val | b_val
    result = a_val ^ b_val
    result = a_val >> 2
    result = a_val << 2
    result = ~a_val
    return result


print('Битовые опарации, маленькие числа: ',
      timeit.timeit(
          'bit_operations(5, 6)',
          setup='from __main__ import bit_operations',
          number=1000))
print('Битовые опарации, большие числа: ',
      timeit.timeit(
          'bit_operations(555555555, 666666666)',
          setup='from __main__ import bit_operations',
          number=1000))

# >>>
# Битовые операции, маленькие числа: 0.0005612910026684403
# Битовые операции, большие числа: 0.0005420910019893199
# Несмотря на то, что входные данные различаются на несколько порядков,
# врем работы функции сопоставимо.
# Это доказывает отсутствие влияния входных данных на работу функции


# Рассмотрим программу, которая имеет сложность O(n)
# Это урок 2, задание 3
# Проверим работу рекурсивного и циклического алгоритмов реализации
# программы на разных входных данных

def cycle_reverse(value: int) -> int:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ """
    invert_value = 0

    if value <= 0:
        return invert_value
    while value > 0:
        if 1 <= value <= 9:
            invert_value = (invert_value + value % 10)
            value = value // 10
        else:
            invert_value = (invert_value + value % 10) * 10
            value = value // 10

    return invert_value


def recursion_reverse(value: int) -> int:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ """
    def recursion(r_value: int):
        if r_value <= 0:
            return 'Недопустимое значение.'
        if 1 <= r_value <= 9:
            return r_value
        return str((r_value % 10)) + str(recursion(r_value // 10))

    invert_value = recursion(value)
    return int(invert_value)

# Также, попробуем использовать инверсию списка как более
# производительное решение


def list_reverse(value: int) -> int:
    """ Реализацие через список """
    result = str(value)
    result = result[::-1]
    return int(result)


print('Циклическая реализация, 3-х значное число: ',
      timeit.timeit(
          'cycle_reverse(123)',
          setup='from __main__ import cycle_reverse',
          number=1000))
print('Рекурсивная реализация, 3-х значное число: ',
      timeit.timeit(
          'recursion_reverse(123)',
          setup='from __main__ import recursion_reverse',
          number=1000))
print('Реализация через список, 3-х значное число: ',
      timeit.timeit(
          'list_reverse(123)',
          setup='from __main__ import list_reverse',
          number=1000))

print('Циклическая реализация, 9-и значное число: ',
      timeit.timeit(
          'cycle_reverse(1234567890)',
          setup='from __main__ import cycle_reverse',
          number=1000))
print('Рекурсивная реализация, 9-и значное число: ',
      timeit.timeit(
          'recursion_reverse(1234567890)',
          setup='from __main__ import recursion_reverse',
          number=1000))
print('Реализация через список, 9-и значное число: ',
      timeit.timeit(
          'list_reverse(123456789)',
          setup='from __main__ import list_reverse',
          number=1000))

print('Циклическая реализация, 27-и значное число: ',
      timeit.timeit(
          'cycle_reverse(123456789123456789123456789)',
          setup='from __main__ import cycle_reverse',
          number=1000))
print('Рекурсивная реализация, 27-и значное число: ',
      timeit.timeit(
          'recursion_reverse(123456789123456789123456789)',
          setup='from __main__ import recursion_reverse',
          number=1000))
print('Реализация через список, 27-и значное число: ',
      timeit.timeit(
          'list_reverse(123456789123456789123456789)',
          setup='from __main__ import list_reverse',
          number=1000))

# >>>
# Циклическая реализация, 3-х значное число:  0.0008862990071065724
# Рекурсивная реализация, 3-х значное число:  0.0032265670015476644
# Реализация через список, 3-х значное число:  0.0007724159804638475

# Циклическая реализация, 9-и значное число:  0.0031779569981154054
# Рекурсивная реализация, 9-и значное число:  0.008668075985042378
# Реализация через список, 9-и значное число:  0.0007350459927693009

# Циклическая реализация, 27-и значное число:  0.006827684002928436
# Рекурсивная реализация, 27-и значное число:  0.01513635300216265
# Реализация через список, 27-и значное число:  0.000575503014260903

# Посмотрим график
# https://yadi.sk/i/fhGqnMKV_m2WFQ

# Из графика видно, что лучшее решение - это инверсия списка
# данный алгоритм имеет константный порядок роста.
# Циклическая и рекурсивная реализации имеют линейный порядок роста O(n)
# При этом рекурсивная реализация менее предпочтительна, тк в данной реализации
# дополнительное время тратиться на рекурсивные вызовы.
# Это видно на графике


# Рассмотрим программу, которая имеет сложность O(n^2)
# Это урок 3, задание 8

def sum_matrix_string(n_string: int, n_column: int) -> list:
    """
    Генерация матрицы и вычисление суммы всех элементов строки.
    Добавление этой суммы в качестве последнего элемента строки
    """
    result_matrix = []
    for _ in range(n_string):
        tmp_list = []
        for _ in range(n_column):
            tmp_list.append(randint(1, 100))
        tmp_list.append(sum(tmp_list))
        result_matrix.append(tmp_list)
    return result_matrix


print('Матрица 4х4: ',
      timeit.timeit(
          'sum_matrix_string(4, 4)',
          setup='from __main__ import sum_matrix_string',
          number=100000))
print('Матрица 5х5: ',
      timeit.timeit(
          'sum_matrix_string(5, 5)',
          setup='from __main__ import sum_matrix_string',
          number=100000))
print('Матрица 6х6: ',
      timeit.timeit(
          'sum_matrix_string(6, 6)',
          setup='from __main__ import sum_matrix_string',
          number=100000))
print('Матрица 7х7: ',
      timeit.timeit(
          'sum_matrix_string(7, 7)',
          setup='from __main__ import sum_matrix_string',
          number=100000))
print('Матрица 8х8: ',
      timeit.timeit(
          'sum_matrix_string(8, 8)',
          setup='from __main__ import sum_matrix_string',
          number=100000))


# На графиках со 100 000 повторений и  1 000 000 квадратичная зависимость
# увеличения времени работы программы от увеличения входных данных не очевидна
# 100 000 повторений
# https://yadi.sk/i/iZM0LR7guQkaKQ
# 1 000 000 повторений
# https://yadi.sk/i/MqTJ4mBS7AHEKg

# Посмотрим на количество вызовов и расход времени в этой программе
print(cProfile.run('sum_matrix_string(64, 64)'))
# >>>
# 25931 function calls in 0.009 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  4096    0.003    0.000    0.006    0.000 random.py:173(randrange)

# Наибольшие временные затраты происходят на генерацию новых элементов матрицы функцией random
# Кроме того, количество вызовов как раз показывает квадратичную зависимость от входных данных
# (64 ^ 2 = 4096 вызовов)


# Попробуем оптимизировать задачу 9 из урока 3
# Задание_9.Найти максимальный элемент среди минимальных элементов
# столбцов матрицы.

def find_max_min(n_string: int, n_column: int):
    """  Исходный вариант алгоритма """
    matrix = []
    for i in range(n_string):
        tmp_list = []
        for j in range(n_column):
            item = randint(1, 100)
            tmp_list.append(item)
        matrix.append(tmp_list)

    min_list = []
    for j in range(n_column):
        tmp_list = []
        for i in range(n_string):
            tmp_list.append(matrix[i][j])
        min_list.append(min(tmp_list))

    return matrix, min_list, max(min_list)

# Текущее решение имеет сложность O(2* n^2)

# Попробуем оптимизировать алгоритм


def find_max_min_opt(n_string: int, n_column: int):
    """ Оптимизированный алгоритм """
    matrix = []
    temp_dict = {}
    for _ in range(n_string):
        tmp_list = []
        for j in range(n_column):
            item = randint(1, 100)
            tmp_list.append(item)
            if temp_dict.get(j) is None:
                temp_dict[j] = [item]
            else:
                temp_dict[j].append(item)
        matrix.append(tmp_list)

    min_list = []
    for j in range(n_column):
        min_list.append(min(temp_dict[j]))

    return matrix, min_list, max(min_list)

# Я попытался привести этот алгоритм к сложности O(n^2 + n)
# Исключив 1 цикл, но добавив словарь


# Змерим производительность обоих алгоритмов
print('Исходный алгоритм. Матрица 10х10: ',
      timeit.timeit(
          'find_max_min(10, 10)',
          setup='from __main__ import find_max_min',
          number=1000))
print('Оптимизированный алгоритм. Матрица 10х10: ',
      timeit.timeit(
          'find_max_min_opt(10, 10)',
          setup='from __main__ import find_max_min_opt',
          number=1000))

print('Исходный алгоритм. Матрица 20х20: ',
      timeit.timeit(
          'find_max_min(20, 20)',
          setup='from __main__ import find_max_min',
          number=1000))
print('Оптимизированный алгоритм. Матрица 20х20: ',
      timeit.timeit(
          'find_max_min_opt(20, 20)',
          setup='from __main__ import find_max_min_opt',
          number=1000))

print('Исходный алгоритм. Матрица 30х30: ',
      timeit.timeit(
          'find_max_min(30, 30)',
          setup='from __main__ import find_max_min',
          number=1000))
print('Оптимизированный алгоритм. Матрица 30х30: ',
      timeit.timeit(
          'find_max_min_opt(30, 30)',
          setup='from __main__ import find_max_min_opt',
          number=1000))

# >>>
# Исходный алгоритм. Матрица 10х10:  0.13057814099011011
# Оптимизированный алгоритм. Матрица 10х10:  0.13671998400241137
# Исходный алгоритм. Матрица 20х20:  0.4793751209799666
# Оптимизированный алгоритм. Матрица 20х20:  0.5067923949973192
# Исходный алгоритм. Матрица 30х30:  1.038695770985214
# Оптимизированный алгоритм. Матрица 30х30:  1.120901924005011

# Посмотрим на график
# https://yadi.sk/i/CQf5caTVadFCkQ
# Видим, что оптимизация прошла неудачно.
# Таким образом понятно, что работа с индексами списка, даже при наличии дополнительного цикла
# является более производительным решением, чем работа со словарем
