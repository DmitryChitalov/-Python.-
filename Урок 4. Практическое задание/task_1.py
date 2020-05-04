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

import random
import cProfile

# Урок 3 Задание_5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


def task3_5(num_list):
    min_el = float('-inf')
    for i, item in enumerate(num_list):
        if min_el < item < 0:
            min_el = item
            min_idx = i

# python -m timeit -n 100 -s "import random" "x = [random.randint(-100, 0) for _ in range(10)]" "import task_1" "task_1.task3_5(x)"
# 100 loops, best of 5: 18 usec per loop
# 100 loops, best of 5: 99.1 usec per loop [random.randint(-100, 0) for _ in range(100)]
# 100 loops, best of 5: 1.1 msec per loop [random.randint(-100, 0) for _ in range(1000)]
# 100 loops, best of 5: 10.8 msec per loop [random.randint(-100, 0) for _ in range(10000)]
# 100 loops, best of 5: 104 msec per loop [random.randint(-100, 0) for _ in range(100000)]

# python -m timeit -n 100 -s "import random" "x = [random.randint(-100, 0) for _ in range(500000)]" "import task_1" "task_1.task3_5(x)"
# 100 loops, best of 5: 533 msec per loop

def task3_5_v2(num_list):
    new_list = [i for i in num_list if i < 0]
    maximum = max(new_list)
    idx = new_list.index(maximum)

# 100 loops, best of 5: 10.9 usec per loop
# 100 loops, best of 5: 103 usec per loop
# 100 loops, best of 5: 1.01 msec per loop
# 100 loops, best of 5: 10.9 msec per loop
# 100 loops, best of 5: 108 msec per loop

# python -m timeit -n 100 -s "import random" "x = [random.randint(-100, 0) for _ in range(500000)]" "import task_1" "task_1.task3_5_v2(x)"
# 100 loops, best of 5: 555 msec per loop

# cProfile.run('task3_5_v2(import random" "x = [random.randint(-100, 0) for _ in range(500000)])')

# task3_5 и task3_5_v2 при увеличении значений in range(значение) быстродествие в пользу функции task3_5

# ==================================================================================================================

#  Урок 3 Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

def task3_7(random_list):
    min_first = min(random_list)
    list_copy = random_list.copy()
    list_copy.remove(min_first)
    min_second = min(list_copy)

# 100 loops, best of 5: 11.5 usec per loop random.randint(-100, 0) for _ in range(10)
# 100 loops, best of 5: 100 usec per loop random.randint(-100, 0) for _ in range(100)
# 100 loops, best of 5: 999 usec per loop random.randint(-100, 0) for _ in range(1000)
# 100 loops, best of 5: 10.1 msec per loop random.randint(-100, 0) for _ in range(10000)
# 100 loops, best of 5: 103 msec per loop random.randint(-100, 0) for _ in range(100000)
# 100 loops, best of 5: 208 msec per loop random.randint(-100, 0) for _ in range(200000)

def task3_7_v2(random_list):
    min_first = 100
    min_second = 100
    for el in random_list:
        if el < min_first:
            min_second = min_first
            min_first = el
        elif el == min_first:
            min_second = el
        elif el < min_second:
            min_second = el

# 100 loops, best of 5: 10.8 usec per loop
# 100 loops, best of 5: 99.1 usec per loop
# 100 loops, best of 5: 999 usec per loop
# 100 loops, best of 5: 10.1 msec per loop
# 100 loops, best of 5: 106 msec per loop
# 100 loops, best of 5: 210 msec per loop random.randint(-100, 0) for _ in range(200000)

# функции min/max работают быстрее

# ==================================================================================================================

# Урок 3 Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

def task3_9(matrix):
    for i, line in enumerate(matrix):
        if i == 0:
            min_line = line.copy()
            continue
        for idx, item in enumerate(line):
            if item < min_line[idx]:
                min_line[idx] = item
    max_min = min_line[0]
    for item in min_line:
        if item > max_min:
            max_min = item


# python -m timeit -n 100 -s "import random" "x = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]" "import task_1" "task_1.task3_9(x)"
# 100 loops, best of 5: 11.6 usec per loop 3x3
# 100 loops, best of 5: 28.4 usec per loop 5x5
# 100 loops, best of 5: 105 usec per loop 10x10
# 100 loops, best of 5: 56.6 usec per loop 5x10
# 100 loops, best of 5: 54.1 usec per loop 10x5
# 100 loops, best of 5: 2.55 msec per loop 50x50
# 100 loops, best of 5: 10.2 msec per loop 100x100
# 100 loops, best of 5: 41.4 msec per loop 200x200
# 100 loops, best of 5: 94.7 msec per loop 300x300c
# 100 loops, best of 5: 263 msec per loop 500x500

def task3_9_v2(matrix):
    max_ = float('-inf')
    for j in range(len(matrix[0])):
        min_ = matrix[0][j]
        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]
        if min_ > max_:
            max_ = min_

# 100 loops, best of 5: 13.3 usec per loop 3x3
# 100 loops, best of 5: 29.6 usec per loop 5x5
# 100 loops, best of 5: 109 usec per loop 10x10
# 100 loops, best of 5: 2.59 msec per loop 50x50
# 100 loops, best of 5: 10.3 msec per loop 100x100
# 100 loops, best of 5: 41.4 msec per loop 200x200
# 100 loops, best of 5: 94.4 msec per loop 300x300
# 100 loops, best of 5: 267 msec per loop 500x500

# task3_9_v2 менее быстродейственна чем task3_9

