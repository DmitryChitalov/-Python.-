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
import memory_profiler
import timeit


from random import randint

@profile
def fun(mass):
    print(f'Базовый список: {mass}')
    mass_1 = [i for i in mass if i < 0]
    print(f"Максимальный отрицательный элемент в данном массиве = {max(mass_1)}, "
          f"его индекс {mass.index(max(mass_1))}")

MASS = [randint(-100, 100) for i in range(10)]
fun(MASS)

"""Line #    Mem usage    Increment   Line Contents
================================================
    21     13.4 MiB     13.4 MiB   @profile
    22                             def fun(mass):
    23     13.4 MiB      0.0 MiB       print(f'Базовый список: {mass}')
    24     13.4 MiB      0.0 MiB       mass_1 = [i for i in mass if i < 0]
    25     13.4 MiB      0.0 MiB       print(f"Максимальный отрицательный элемент в данном массиве = {max(mass_1)}, "
    26                                       f"его индекс {mass.index(max(mass_1))}")
"""


"""Проблем с памятью нет, можно сделать вывод, что все в пределах нормы"""


from memory_profiler import profile
import memory_profiler


@profile
def cycle_method(number):
    """четные"""
    a = 0
    """нечетные"""
    b = 0

    while number != 0:
        c = number % 10
        number = number // 10
        if c % 2 == 0:
           a += 1
        else:
            b += 1
    return a, b


try:
    NUMBER = int(input("Введите натуральное число: "))
    print(f"{cycle_method(NUMBER)}")
except ValueError:
    print("Вы ввели некорректные данные")


"""Line #    Mem usage    Increment   Line Contents
================================================
    19     13.4 MiB     13.4 MiB   @profile
    20                             def cycle_method(number):
    21                                 "четные"
    22     13.4 MiB      0.0 MiB       a = 0
    23                                 "нечетные"
    24     13.4 MiB      0.0 MiB       b = 0
    25                             
    26     13.4 MiB      0.0 MiB       while number != 0:
    27     13.4 MiB      0.0 MiB           c = number % 10
    28     13.4 MiB      0.0 MiB           number = number // 10
    29     13.4 MiB      0.0 MiB           if c % 2 == 0:
    30                                        a += 1
    31                                     else:
    32     13.4 MiB      0.0 MiB               b += 1
    33     13.4 MiB      0.0 MiB       return a, b


(0, 1)

Process finished with exit code 0"""
"""Проблем с памятью нет, можно сделать вывод, что все в пределах нормы"""


print(timeit.timeit("fun(MASS)", setup="from __main__ import fun, MASS", number=1))
print(timeit.timeit("cycle_method(NUMBER)", setup="from __main__ import cycle_method, NUMBER", number=1))

"""0.0007800999999996172 - первая задача"""
"""0.0008189000000000668 - вторая задача"""
"""Функция на нахождение  в массиве максимального максимального отрицательного элемента быстрее, чем зада на подсчет 
четных и нечетных чисел в натуральном числе"""