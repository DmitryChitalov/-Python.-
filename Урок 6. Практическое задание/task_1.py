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

# Python 3.8.2
# Windows 10 64
from memory_profiler import profile
from random import randint

@profile
def multiple_count_1():
    for i in range(2, 10):
        my_array = list(range(100000))
        multiple = 0
        for j in my_array:
            if j % i == 0:
                multiple += 1
        print(f"В диапазоне 2-99: {multiple} чисел кратны {i}")
    del my_array


#multiple_count_1()

"""
Line #    Mem usage    Increment   Line Contents
================================================
    20     13.3 MiB     13.3 MiB   @profile
    21                             def multiple_count_1():
    22     16.3 MiB      0.0 MiB       for i in range(2, 10):
    23     16.3 MiB      1.9 MiB           my_array = list(range(100000))
    24     16.3 MiB      0.0 MiB           multiple = 0
    25     16.3 MiB      0.0 MiB           for j in my_array:
    26     16.3 MiB      0.0 MiB               if j % i == 0:
    27     16.3 MiB      0.0 MiB                   multiple += 1
    28     16.3 MiB      0.0 MiB           print(f"В диапазоне 2-99: {multiple} чисел кратны {i}")
    29     13.9 MiB      0.0 MiB       del my_array
    
Инкримент при создании списка. После выполнения функции, список уже не нужен,
и при удалении освобождаем память.
"""


@profile
def multiple_count_2():
    for i in range(2, 4):
        my_array = [i for i in range(100000)]
        multiple = 0
        for j in my_array:
            if j % i == 0:
                multiple += 1
        print(f"В диапазоне 2-99: {multiple} чисел кратны {i}")
    del my_array


#multiple_count_2()

"""
Line #    Mem usage    Increment   Line Contents
================================================
    53     13.8 MiB     13.8 MiB   @profile
    54                             def multiple_count_2():
    55     16.6 MiB      0.0 MiB       for i in range(2, 10):
    56     17.6 MiB      0.3 MiB           my_array = [i for i in range(100000)]
    57     16.6 MiB      0.0 MiB           multiple = 0
    58     16.6 MiB      0.0 MiB           for j in my_array:
    59     16.6 MiB      0.0 MiB               if j % i == 0:
    60     16.6 MiB      0.0 MiB                   multiple += 1
    61     16.6 MiB      0.0 MiB           print(f"В диапазоне 2-99: {multiple} чисел кратны {i}")
    62     13.9 MiB      0.0 MiB       del my_array
    
Получилось снизить инкремент при использовании генератора, при 
этом на само использование программы ушло больше памяти.
"""


@profile
def finder():
    ORIGIN_LIST = [randint(-100, 100) for i in range(100000)]
    MODIFIED_LIST = [i for i in ORIGIN_LIST if i < 0]
    print(f"Базовый список: {ORIGIN_LIST} \nМаксимальный отрицательный элемент +"
          f"в данном массиве = {max(MODIFIED_LIST)} его индекс {ORIGIN_LIST.index(max(MODIFIED_LIST))}")
    del MODIFIED_LIST, ORIGIN_LIST


finder()
"""
Line #    Mem usage    Increment   Line Contents
================================================
    87     13.4 MiB     13.4 MiB   @profile
    88                             def finder():
    89     14.8 MiB      0.2 MiB       ORIGIN_LIST = [randint(-100, 100) for i in range(100000)]
    90     14.8 MiB      0.0 MiB       MODIFIED_LIST = [i for i in ORIGIN_LIST if i < 0]
    91     14.8 MiB      0.0 MiB       print(f"Базовый список: {ORIGIN_LIST} \nМаксимальный отрицательный элемент +"
    92                                       f"в данном массиве = {max(MODIFIED_LIST)} его индекс {ORIGIN_LIST.index(max(MODIFIED_LIST))}")
    93     13.6 MiB      0.0 MiB       del MODIFIED_LIST, ORIGIN_LIST
    
Инкремент при формировании списков. Освобождаем память удалением списков после окончания работы функции
"""
