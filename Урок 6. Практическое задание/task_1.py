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
import sys
import memory_profiler
import time


'''Функция поиска i-го простого числа,
    без использования алгоритма «Решето Эратосфена»
def sieve_without_erato():
'''
def sieve_without_erato(n):
    list = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            list.append(i)
    return list
if __name__ == '__main__':
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()

    res = sieve_without_erato(10000)

    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")
    print(sys.getrefcount(list))


'''Функция поиска i-го простого числа,
    используя алгоритм «Решето Эратосфена»
    '''
def sieve_erato(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

if __name__ == '__main__':
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()

    res =sieve_erato(10000)

    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")
    print(sys.getrefcount(list))

"""
Результат при n = 10000: без решета время 6,765 сек.,  память - 0,019 Мб
                         с решетом время 0,00 сек., память - 0,164 Мб
При попытке получить результат для n = 100000 завис комп, но понятно, что выигрыш по скорости и проигрыш по памяти
у решета будет расти. 
По скорости ожидаемо выигрывает решето, причины на уже известны, но по объему выделяемой памяти решето проигрывает,
так как, несмотря на то, что вычеркнутые непростые числа будут из массива удалены,
изначально требуется выделить большой объем памяти для фильтрумых чисел.
"""

from memory_profiler import profile

@profile
def fac(n):
    mult = 1
    fuct_list = []
    for i in range(1, n + 1):
        mult = mult * i
        fuct_list.append(mult)
    return fuct_list

print(fac(10000))
"""
Line #    Mem usage    Increment   Line Contents
================================================
     3     13.4 MiB     13.4 MiB   @profile
     4                             def fac(n):
     5                                 # Вычисление с помощью цикла
     6     13.4 MiB      0.0 MiB       mult = 1
     7     13.4 MiB      0.0 MiB       fuct_list = []
     8     84.5 MiB      0.0 MiB       for i in range(1, n + 1):
     9     84.5 MiB      0.1 MiB           mult = mult * i
    10     84.5 MiB      0.0 MiB           fuct_list.append(mult)
    11     84.5 MiB      0.0 MiB       return fuct_list
В результате получаем очень большой инкремент при создании списка, который программа должна хранить
в памяти при вычислениях с помощью цикла. Альтернатива - использование генераторов.
"""