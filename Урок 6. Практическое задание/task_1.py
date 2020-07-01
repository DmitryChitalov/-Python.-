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
from memory_profiler import profile
from time import time
from random import randint


@profile()
def multiple_num():
    # Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
    # сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
    # Для наглядности работы с памятью увеличим диапазон.
    count = 0
    t = time()
    number_list = [i for i in range(2, 999999)]
    print(time() - t)
    for multiple in range(2, 5):
        for el in number_list:
            if el % multiple == 0:
                count += 1
        print(f'в диапазоне 2-99: {count} чисел кратны {multiple}')
        count = 0


# multiple_num()

"""
Для запуска программы выделено 39.2 MiB
Далее мы создаем список при помощи генератора и выделяем 0.8 MiB по Increment
но по факту выделяется (78,3-39,2) = 39,1 MiB
Line #    Mem usage    Increment   Line Contents
================================================
    19     39.2 MiB     39.2 MiB   @profile()
    20                             def multiple_num():
    21                                 # Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
    22                                 # сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
    23                                 # Для наглядности работы с памятью увеличим диапазон.
    24     39.2 MiB      0.0 MiB       count = 0
    25     39.2 MiB      0.0 MiB       t = time()
    26     78.3 MiB      0.8 MiB       number_list = [i for i in range(2, 999999)]
    27     78.3 MiB      0.0 MiB       print(time() - t)                               
    33     78.3 MiB      0.0 MiB       for multiple in range(2, 5):
    34     78.3 MiB      0.0 MiB           for el in number_list:
    35     78.3 MiB      0.0 MiB               if el % multiple == 0:
    36     78.3 MiB      0.0 MiB                   count += 1
    37     78.2 MiB      0.0 MiB           print(f'в диапазоне 2-99: {count} чисел кратны {multiple}')
    38     78.2 MiB      0.0 MiB           count = 0

Меня смутило время заполнения списка при помощи генератора и я решил заменить его на встроенные функции 
+ освободить память в конце.
"""


@profile()
def multiple_num_2():
    count = 0
    t = time()
    number_list = list(range(2, 999999))
    print(time() - t)
    for multiple in range(2, 5):
        for el in number_list:
            if el % multiple == 0:
                count += 1
        print(f'в диапазоне 2-99: {count} чисел кратны {multiple}')
        count = 0
    del number_list


# multiple_num_2()

"""
Время заполнения списка снизилось с * до 0.023999452590942383
выделение памяти снизилось до 38,6 MiB
+ при помощи del снизили нагрузку на память в конце.

Line #    Mem usage    Increment   Line Contents
================================================
    70     39.2 MiB     39.2 MiB   @profile()
    71                             def multiple_num_2():
    72     39.2 MiB      0.0 MiB       count = 0
    73     39.2 MiB      0.0 MiB       t = time()
    74     77.7 MiB     38.6 MiB       number_list = list(range(2, 999999))
    75     77.7 MiB      0.0 MiB       print(time() - t)
    76     77.7 MiB      0.0 MiB       for multiple in range(2, 5):
    77     77.8 MiB      0.0 MiB           for el in number_list:
    78     77.8 MiB      0.0 MiB               if el % multiple == 0:
    79     77.8 MiB      0.0 MiB                   count += 1
    80     77.7 MiB      0.0 MiB           print(f'в диапазоне 2-99: {count} чисел кратны {multiple}')
    81     77.7 MiB      0.0 MiB           count = 0
    
Такого снижения оказалось недостаточно, потому было принято решение использовать генератор
"""


@profile()
def multiple_num_3():
    count = 0
    t = time()
    for multiple in range(2, 9):
        number_list = (i for i in range(2, 999999))
        for el in number_list:
            if el % multiple == 0:
                count += 1
        print(f'в диапазоне 2-99: {count} чисел кратны {multiple}')
        count = 0
    print(time() - t)


# multiple_num_3()

"""
В данном случае мы еще выигрываем и по времени и по памяти
так как список не создается, а генерируется на лету и не занимает
память вообще.

Line #    Mem usage    Increment   Line Contents
================================================
    70     39.1 MiB     39.1 MiB   @profile()
    71                             def multiple_num_2():
    72     39.1 MiB      0.0 MiB       count = 0
    73     39.1 MiB      0.0 MiB       t = time()
    74     39.1 MiB      0.0 MiB       for multiple in range(2, 3):
    75     39.1 MiB      0.0 MiB           number_list = (i for i in range(2, 999999))
    76     39.1 MiB      0.0 MiB           for el in number_list:
    77     39.1 MiB      0.0 MiB               if el % multiple == 0:
    78     39.1 MiB      0.0 MiB                   count += 1
    79     39.1 MiB      0.0 MiB           print(f'в диапазоне 2-99: {count} чисел кратны {multiple}')
    80     39.1 MiB      0.0 MiB           count = 0
    81                                 # del number_list
    82     39.1 MiB      0.0 MiB       print(time() - t)
"""


# Пример №2

@profile()
def frequent_number():
    number_list = [randint(100000000000000000, 100000000000000009) for i in range(9999)]
    temp_list = number_list[:]
    count = 0
    max_count = 0
    common_num = 0
    while temp_list:
        now_element = temp_list[0]
        for el in temp_list:
            if el == now_element:
                count += 1
        if count > max_count:
            common_num = now_element
            max_count = count
        while now_element in temp_list:
            temp_list.remove(now_element)
        count = 0

    print(f'число {common_num} встречается в массиве {number_list} чаще всего')
    del temp_list
    del number_list


frequent_number()

"""
Для запуска программы выделено 39.3 MiB
далее мы генерируем список занимая 0.1 MiB (по факту 0.7 MiB)
и создаем его глубокую копию в временной переменной тратя еще 0.1 MiB
Что бы оптимизироать скрипт в конце добавлены del для освобождения памяти.
Что бы еще оптимизировать скрипт, нужно применить алгоритм, в котором не нужно будет
создавать еще одну переменную, содержащую массив. Что и было выполнено в след варианте ниже.

Line #    Mem usage    Increment   Line Contents
================================================
   148     39.3 MiB     39.3 MiB   @profile()
   149                             def frequent_number():
   150     39.9 MiB      0.1 MiB       number_list = [randint(100000000000000000, 100000000000000009) for i in range(9999)]
   151     39.9 MiB      0.1 MiB       temp_list = number_list[:]
   152     39.9 MiB      0.0 MiB       count = 0
   153     39.9 MiB      0.0 MiB       max_count = 0
   154     39.9 MiB      0.0 MiB       common_num = 0
   155     39.9 MiB      0.0 MiB       while temp_list:
   156     39.9 MiB      0.0 MiB           now_element = temp_list[0]
   157     39.9 MiB      0.0 MiB           for el in temp_list:
   158     39.9 MiB      0.0 MiB               if el == now_element:
   159     39.9 MiB      0.0 MiB                   count += 1
   160     39.9 MiB      0.0 MiB           if count > max_count:
   161     39.9 MiB      0.0 MiB               common_num = now_element
   162     39.9 MiB      0.0 MiB               max_count = count
   163     39.9 MiB      0.0 MiB           while now_element in temp_list:
   164     39.9 MiB      0.0 MiB               temp_list.remove(now_element)
   165     39.9 MiB      0.0 MiB           count = 0
   166                             
   167     40.0 MiB      0.1 MiB       print(f'число {common_num} встречается в массиве {number_list} чаще всего')
   168     40.0 MiB      0.0 MiB       del temp_list
   169     39.8 MiB      0.0 MiB       del number_list

"""
@profile()
def frequent_number2():
    lst = [randint(100000000000000000, 100000000000000009) for i in range(9999)]
    numb = max(lst, key=lst.count)
    print(f'Число {numb} встречается {lst.count(numb)} раз')
    del lst


# frequent_number2()
"""
Этот вариант не только работает быстрее, из-за быстрых встроенных функций, но и занимает в 2 раза меньше
дополнительной памяти,из-за отсутствия необходимости создавать дополнительные списки.

Line #    Mem usage    Increment   Line Contents
================================================
   175     39.4 MiB     39.4 MiB   @profile()
   176                             def frequent_number2():
   177     39.9 MiB      0.1 MiB       lst = [randint(100000000000000000, 100000000000000009) for i in range(9999)]
   178     39.9 MiB      0.0 MiB       numb = max(lst, key=lst.count)
   179     39.9 MiB      0.0 MiB       print(f'Число {numb} встречается {lst.count(numb)} раз')
   180     39.6 MiB      0.0 MiB       del lst
"""
