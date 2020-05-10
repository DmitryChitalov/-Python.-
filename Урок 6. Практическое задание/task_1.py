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

# Окружение:
# Python 3.7.3
# 64-разрядная ОС Windows 10 Pro
# но функция sys.platform в PyCharm показывает -> # win32
# (устанавливал год назад, возможно как то неправильно установил)

# Для анализа взял второе задание из урока 4 - две функции, выполняющие одну задачу
# Первая функция - использование решета Эратосфена
# Вторая функция - простой перебор
# Затем попробую оптимизировать с точки зрения использования памяти

# import timeit
from memory_profiler import profile


@profile
def get_prime_number_eratosthenes(number):
    # Функция разработана только для параметра <= 9592
    # так как решето эратосфена для целей задачи рассчитываем до 100000
    # при необходимости этот параметр можем увеличить
    if number > 9592:
        return None  # Признак ошибочного завершения

    lst = [i for i in range(2, 100000)]

    for n in range(len(lst)):
        p = lst[n]
        if not p:
            continue
        k = n
        while True:
            if k + p >= len(lst):
                break
            lst[k + p] = 0
            k += p

    result = [i for i in lst if i]

    return result[number - 1]


@profile
def get_prime_number_simple(number):
    i = 1
    prime_number = 2
    while i < number:
        prime_number += 1
        for k in range(2, prime_number):
            if prime_number % k == 0:
                break
        else:
            i += 1
    return prime_number


# Оптимизированная функция с решетом
@profile
def get_prime_number_eratosthenes_improved(number):
    # Функция разработана только для параметра <= 9592
    # так как решето эратосфена для целей задачи рассчитываем до 100000
    # при необходимости этот параметр можем увеличить
    if number <= 25:
        lst_size = 100
    elif number <= 168:
        lst_size = 1000
    elif number <= 1229:
        lst_size = 10000
    elif number <= 9592:
        lst_size = 100000
    else:  # if number > 9592:
        return None  # Признак ошибочного завершения

    lst = [i for i in range(2, lst_size)]

    for n in range(len(lst)):
        p = lst[n]
        if not p:
            continue
        k = n
        while True:
            if k + p >= len(lst):
                break
            lst[k + p] = 0
            k += p

    result = [i for i in lst if i]

    return result[number - 1]

# print(get_prime_number_eratosthenes(1000))
# print(get_prime_number_simple(1000))
# print(get_prime_number_eratosthenes_improved(1000))


"""
# 1000
print("get_prime_number_eratosthenes(1000)=",
      timeit.timeit("get_prime_number_eratosthenes(1000)",
                    setup="from __main__ import get_prime_number_eratosthenes",
                    number=50))
print("get_prime_number_simple(1000)=",
      timeit.timeit("get_prime_number_simple(1000)",
                    setup="from __main__ import get_prime_number_simple",
                    number=50))
print("get_prime_number_eratosthenes_improved(1000)=",
      timeit.timeit("get_prime_number_eratosthenes_improved(1000)",
                    setup="from __main__ import get_prime_number_eratosthenes_improved",
                    number=50))
"""

# Анализируем:

# Замерим сначала для полной картины скорость (отключаем декораторы)
# Первая функция - использование решета Эратосфена
# get_prime_number_eratosthenes(1000)= 0.6516743
# Вторая функция - простой перебор
# get_prime_number_simple(1000)= 22.577132300000002
# Функция без использования решета заметно проигрывает по скорости (с увеличением значения входящего параметра)

# Проанализируем память (подключаем декораторы и отключаем timeit)

# Вторая функция - простой перебор
# Анализ показал что увеличения памяти не происходит

# Первая функция - использование решета Эратосфена
# Line #    Mem usage    Increment   Line Contents
# ================================================
#  30     14.1 MiB     14.1 MiB   @profile
#  31                             def get_prime_number_eratosthenes(number):
#  ...
#  35     14.1 MiB      0.0 MiB       if number > 9592:
#  36                                     return None  # Признак ошибочного завершения
#  37
#  38     16.1 MiB      0.2 MiB       lst = [i for i in range(2, 100000)]
#  ...

# В строке 38 хотя инкремент показан небольшой, значение используемой памяти возрастает на 2.0 MiB

# Попробуем оптимизировать функцию с использованием решета Эратосфена
# Для этого применим так называемую пи-функцию, уменьшая размер решета в зависимости от входящего параметра

# Анализируем скорость и использование памяти при использовании новой функции
# def get_prime_number_eratosthenes_improved(number)

# Замерим сначала скорость (отключаем декораторы)
# get_prime_number_eratosthenes(1000)= 0.6495114

# Проанализируем память (подключаем декораторы и отключаем timeit)

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     69     14.1 MiB     14.1 MiB   @profile
#     70                             def get_prime_number_eratosthenes_improved(number):
#     71                                 # Функция разработана только для параметра <= 9592
#     72                                 # так как решето эратосфена для целей задачи рассчитываем до 100000
#     73                                 # при необходимости этот параметр можем увеличить
#     74     14.1 MiB      0.0 MiB       lst_size = 0  # Размер пока не определен
#     75     14.1 MiB      0.0 MiB       if number <= 25:
#     76                                     lst_size = 100
#     77     14.1 MiB      0.0 MiB       elif number <= 168:
#     78                                     lst_size = 1000
#     79     14.1 MiB      0.0 MiB       elif number <= 1229:
#     80     14.1 MiB      0.0 MiB           lst_size = 10000
#     81                                 elif number <= 9592:
#     82                                     lst_size = 100000
#     83                                 else:  # if number > 9592:
#     84                                     return None  # Признак ошибочного завершения
#     85
#     86     14.3 MiB      0.1 MiB       lst = [i for i in range(2, lst_size)]
#     ...

# Как и ожидалось в данном случае памяти потребовалось значительно меньше
# 14.3 MiB - 14.1 MiB = 0.02 MiB (при показанном инкременте только 0.1 MiB)

# Таким образом, используя изученные функции анализа
# и незначительно усложнив алгоритм
# получилось заметно уменьшить расход памяти - в 10 раз (и как бонус немного увеличив скорость)
