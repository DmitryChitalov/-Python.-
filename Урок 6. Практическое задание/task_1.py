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

@profile
def reverse_func():
    NUM = int(input('Введите число: '))
    NUM_1 = ''
    while NUM != 0:
        NUM_2 = NUM % 10
        NUM_1 += str(NUM_2)
        NUM = NUM // 10
    print(f'Перевернутое число: {NUM_1}')
reverse_func()
'''
Line #    Mem usage    Increment   Line Contents
================================================
    17     14.5 MiB     14.5 MiB   @profile
    18                             def reverse_func():
    19     14.5 MiB      0.0 MiB       NUM = int(input('Введите число: '))
    20     14.5 MiB      0.0 MiB       NUM_1 = ''
    21     14.5 MiB      0.0 MiB       while NUM != 0:
    22     14.5 MiB      0.0 MiB           NUM_2 = NUM % 10
    23     14.5 MiB      0.0 MiB           NUM_1 += str(NUM_2)
    24     14.5 MiB      0.0 MiB           NUM = NUM // 10
    25     14.5 MiB      0.0 MiB       print(f'Перевернутое число: {NUM_1}')
Python 3.8, WindowsX64
Функция не требует дополнительной памяти, оптимизировать нечего.
'''

@profile
def ev_unev(num, ev, unev):
    if num == 0:
        return f'Количество четных и нечетных цифр в числе равно: {ev}, {unev}'
    else:
        a = num % 10
        if a % 2 == 0:
            ev += 1
        else:
            unev += 1
        return ev_unev(num // 10, ev, unev)
print(ev_unev(985214782, 0, 0))
'''
Line #    Mem usage    Increment   Line Contents
================================================
    44     13.4 MiB     13.3 MiB   @profile
    45                             def ev_unev(num, ev, unev):
    46     13.4 MiB      0.0 MiB       if num == 0:
    47     13.4 MiB      0.0 MiB           return f'Количество четных и нечетных цифр в числе равно: {ev}, {unev}'
    48                                 else:
    49     13.4 MiB      0.0 MiB           a = num % 10
    50     13.4 MiB      0.0 MiB           if a % 2 == 0:
    51     13.4 MiB      0.0 MiB               ev += 1
    52                                     else:
    53     13.4 MiB      0.0 MiB               unev += 1
    54     13.4 MiB      0.0 MiB           return ev_unev(num // 10, ev, unev)
Python 3.8, WindowsX64
Функция не требует дополнительной памяти, оптимизировать нечего.
'''

@profile
def max_count(my_list):
    return max(my_list, key=lambda x: my_list.count(x))
NUMBERS = [2, 8, 79, -9, 1, 2, 79, 15, -7, 2, 4, 2, -159, 79, 79, 79]
print(max_count(NUMBERS))
'''
Line #    Mem usage    Increment   Line Contents
================================================
    73     13.4 MiB     13.4 MiB   @profile
    74                             def max_count(my_list):
    75     13.4 MiB      0.0 MiB       return max(my_list, key=lambda x: my_list.count(x))
Python 3.8, WindowsX64
Функция не требует дополнительной памяти, оптимизировать нечего.
'''

