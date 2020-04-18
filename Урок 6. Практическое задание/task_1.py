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

from collections import deque
from memory_profiler import profile
import memory_profiler
import time


@profile
def add(x, y):
    """
    Сложение шестнадцатиричных чисел
    """
    hex_numbers = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    if len(y) > len(x):
        x, y = y, x

    result_deque = deque()
    digit = 0

    while x:
        if y:
            tmp = hex_numbers[x.pop()] + hex_numbers[y.pop()] + digit
        else:
            tmp = hex_numbers[x.pop()] + digit

        digit = 0

        if tmp > 16:
            result_deque.appendleft(hex_numbers[tmp - 16])
            digit = 1
        else:
            result_deque.appendleft(hex_numbers[tmp])

    if digit == 1:
        result_deque.appendleft('1')

    return result_deque


@profile
def mul(x, y):
    """
    Умножение шестнадцатиричных чисел
    """
    hex_numbers = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    if len(y) > len(x):
        x, y = y, x

    result_deque = deque()
    tmp_deque = deque()
    tmp_list = list()
    digit = 0

    for i in range(len(y)):
        el = hex_numbers[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            tmp = hex_numbers[x[j]] * el + digit
            tmp_deque.appendleft(hex_numbers[tmp % 16])
            digit = tmp // 16

        if digit != 0:
            tmp_deque.appendleft(hex_numbers[digit])

        if len(tmp_list) != 0:
            for k in range(len(tmp_list)):
                tmp_deque.append('0')

        digit = 0
        tmp_list.append(tmp_deque.copy())
        tmp_deque.clear()

    for i in range(len(tmp_list)):
        tmp_deque = add(tmp_deque, tmp_list[i])

    result_deque = tmp_deque.copy()

    return result_deque


if __name__ == "__main__":
    # начало отсчета
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()

    # вводим два числа, с которыми проводим операции
    NUMBER_ONE = deque('A2')
    NUMBER_TWO = deque('C4F')
    # вычисляем сумму
    # add(NUMBER_ONE, NUMBER_TWO)
    # вычисляем произведение
    mul(NUMBER_ONE, NUMBER_TWO)

    # окончание отсчета
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f'Время выполнения: {time_diff}, занимаемая память {mem_diff}')

# ОС Winx64, Python v 3.8.0
# для работы с памятью выбрал последнюю задачу
# сложение шестнадцатиричных чисел производится быстрее в два раза, однако
# занимает больше памяти, чем произведение.
# комментарии из задачи убраны, чтобы не нагружать вывод
#

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     22     14.6 MiB     14.6 MiB   @profile
#     23                             def add(x, y):
#     24                                 """
#     25                                 Сложение шестнадцатиричных чисел
#     26                                 """
#     27     14.6 MiB      0.0 MiB       hex_numbers = {
#     28     14.6 MiB      0.0 MiB           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
#     29     14.6 MiB      0.0 MiB           8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
#     30     14.6 MiB      0.0 MiB           '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
#     31     14.6 MiB      0.0 MiB           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
#     32                                 }
#     33
#     34     14.6 MiB      0.0 MiB       if len(y) > len(x):
#     35     14.6 MiB      0.0 MiB           x, y = y, x
#     36
#     37     14.6 MiB      0.0 MiB       result_deque = deque()
#     38     14.6 MiB      0.0 MiB       digit = 0
#     39
#     40     14.6 MiB      0.0 MiB       while x:
#     41     14.6 MiB      0.0 MiB           if y:
#     42     14.6 MiB      0.0 MiB               tmp = hex_numbers[x.pop()] + hex_numbers[y.pop()] + digit
#     43                                     else:
#     44     14.6 MiB      0.0 MiB               tmp = hex_numbers[x.pop()] + digit
#     45
#     46     14.6 MiB      0.0 MiB           digit = 0
#     47
#     48     14.6 MiB      0.0 MiB           if tmp > 16:
#     49     14.6 MiB      0.0 MiB               result_deque.appendleft(hex_numbers[tmp - 16])
#     50     14.6 MiB      0.0 MiB               digit = 1
#     51                                     else:
#     52     14.6 MiB      0.0 MiB               result_deque.appendleft(hex_numbers[tmp])
#     53
#     54     14.6 MiB      0.0 MiB       if digit == 1:
#     55                                     result_deque.appendleft('1')
#     56
#     57     14.6 MiB      0.0 MiB       return result_deque
#
#
# Время выполнения: 0.046875, занимаемая память 0.24609375

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     60     14.6 MiB     14.6 MiB   @profile
#     61                             def mul(x, y):
#     62                                 """
#     63                                 Умножение шестнадцатиричных чисел
#     64                                 """
#     65     14.6 MiB      0.0 MiB       hex_numbers = {
#     66     14.6 MiB      0.0 MiB           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
#     67     14.6 MiB      0.0 MiB           8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
#     68     14.6 MiB      0.0 MiB           '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
#     69     14.6 MiB      0.0 MiB           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
#     70                                 }
#     71
#     72     14.6 MiB      0.0 MiB       if len(y) > len(x):
#     73     14.6 MiB      0.0 MiB           x, y = y, x
#     74
#     75     14.6 MiB      0.0 MiB       result_deque = deque()
#     76     14.6 MiB      0.0 MiB       tmp_deque = deque()
#     77     14.6 MiB      0.0 MiB       tmp_list = list()
#     78     14.6 MiB      0.0 MiB       digit = 0
#     79
#     80     14.6 MiB      0.0 MiB       for i in range(len(y)):
#     81     14.6 MiB      0.0 MiB           el = hex_numbers[y.pop()]
#     82     14.6 MiB      0.0 MiB           for j in range(len(x) - 1, -1, -1):
#     83     14.6 MiB      0.0 MiB               tmp = hex_numbers[x[j]] * el + digit
#     84     14.6 MiB      0.0 MiB               tmp_deque.appendleft(hex_numbers[tmp % 16])
#     85     14.6 MiB      0.0 MiB               digit = tmp // 16
#     86
#     87     14.6 MiB      0.0 MiB           if digit != 0:
#     88     14.6 MiB      0.0 MiB               tmp_deque.appendleft(hex_numbers[digit])
#     89
#     90     14.6 MiB      0.0 MiB           if len(tmp_list) != 0:
#     91     14.6 MiB      0.0 MiB               for k in range(len(tmp_list)):
#     92     14.6 MiB      0.0 MiB                   tmp_deque.append('0')
#     93
#     94     14.6 MiB      0.0 MiB           digit = 0
#     95     14.6 MiB      0.0 MiB           tmp_list.append(tmp_deque.copy())
#     96     14.6 MiB      0.0 MiB           tmp_deque.clear()
#     97
#     98     14.6 MiB      0.0 MiB       for i in range(len(tmp_list)):
#     99     14.6 MiB      0.0 MiB           tmp_deque = add(tmp_deque, tmp_list[i])
#    100
#    101     14.6 MiB      0.0 MiB       result_deque = tmp_deque.copy()
#    102
#    103     14.6 MiB      0.0 MiB       return result_deque
#
#
# Время выполнения: 0.09375, занимаемая память 0.23046875
