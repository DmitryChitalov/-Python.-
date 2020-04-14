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
import numpy as np
import memory_profiler
import time



my_array1 = [[1, 2, 3],  [2, 3, 4],  [3, 4, 5]]
my_array2 = [[4, 5, 6],  [5, 6, 7],  [6, 7, 8]]


class Matrix:
    def __init__(self, two_dim_list):
         self.two_dim_list = two_dim_list
         


    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.two_dim_list]) + '\n'

    def __add__(self, other):
        res_matrix = []             # создаем новую матрицу для заполнения строками с данными суммирования
        res_row = []                # создаем строку для заполнения данными суммирования элементов
        for i in range(len(self.two_dim_list)):
            for j in range(len(self.two_dim_list[0])):
                summa = self.two_dim_list[i][j] + other.two_dim_list[i][j]
                res_row.append(summa)
                if len(res_row) == len(self.two_dim_list):
                    res_matrix.append(res_row)
                    res_row = []        # освобождаем строку для заполнения данными следующего ряда
        return Matrix(res_matrix)


t_1 = time.process_time()
m_1 = memory_profiler.memory_usage()

m1 = Matrix(my_array1)
m2 = Matrix(my_array2)
res = (m1 + m2)

t_2 = time.process_time()
m_2 = memory_profiler.memory_usage()

print(m1)
print(m2)
print(res)

print(f"Выполнение заняло {t_2 - t_1} сек and {m_2[0] - m_1[0]} Мб")

# 2 Вариант с использованием модуля 'numpy'
print('************* 2 вариант **************************** \n')


A = np.array([[1, 2, 3],  [2, 3, 4],  [3, 4, 5]])
B = np.array([[4, 5, 6],  [5, 6, 7],  [6, 7, 8]])

t_11 = time.process_time()
m_11 = memory_profiler.memory_usage()

C = A + B

t_22 = time.process_time()
m_22 = memory_profiler.memory_usage()

print(C)

print(f"Выполнение заняло {t_22 - t_11} сек and {m_22[0] - m_11[0]} Мб")

'''
5 7 9
7 9 11
9 11 13

Выполнение заняло 0.0 сек and 0.00390625 Мб
************* 2 вариант ****************************

[[ 5  7  9]
 [ 7  9 11]
 [ 9 11 13]]
Выполнение заняло 0.0 сек and 0.00390625 Мб

Результаты замеров по времени и выделению памяти для операции сложения двух матриц с применением ООП и
модуля numpy каких-либо различиев не выявили, что означает что оба варианта решения одинаково эффективно
используют память и вычислительные ресурсы процессора
Свежения о системе: win 64 bit, Python, 3.7
'''


