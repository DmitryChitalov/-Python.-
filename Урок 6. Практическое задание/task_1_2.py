"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО



"""

"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
import random
import memory_profiler
import time
import numpy as np

@memory_profiler.profile
def find_elem_1(M,N):
    # M = 500
    # N = 500
    MAT = []
    for i in range(N):
        b = [random.randint(0, 100) for i in range(M)]
        MAT.append(b)
        # print(*b, sep=" ")

    MX = -1  # переменная для хранения текущего максимума
    for j in range(M):
        mn = 200    # переменная для хранения текущего минимума
        for i in range(N):
            if MAT[i][j] < mn:
                mn = MAT[i][j]
        if mn > MX:
            MX = mn
    print(
        f'Максимальный элемент среди минимальных элементов столбцов матрицы: {MX}')

# find_elem()


@memory_profiler.profile
def find_elem_2(M, N):
    MAT = np.random.randint(100, size=(M, N))

    MX = -1  # переменная для хранения текущего максимума
    for j in range(MAT.shape[0]):
        mn = 200    # переменная для хранения текущего минимума
        for i in range(MAT.shape[1]):
            if MAT[i][j] < mn:
                mn = MAT[i][j]
        if mn > MX:
            MX = mn
    print(
        f'Максимальный элемент среди минимальных элементов столбцов матрицы: {MX}')


if __name__ == '__main__':

    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    cubes = find_elem_1(1000, 1000)
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"Выполнение заняло функции'find_elem_1' {time_diff} сек and {mem_diff} Мб")

    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    cubes = find_elem_2(1000, 1000)
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"Выполнение заняло функции'find_elem_2' {time_diff} сек and {mem_diff} Мб")

# Через numpy функция поиска максимального элемента среди минимальных элементов столбцов матрицы, работает быстрее
# А именно создание самой матрицы
# Поиск самих элементов в пределах нормы.

