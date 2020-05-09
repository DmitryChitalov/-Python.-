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

# Задача с тремя алгоритмами для получения i-го простого числа.

import platform
import sys
from memory_profiler import profile
from pympler import asizeof

print(sys.version)
print(sys.platform)
print(platform.architecture())


# 3.7.5 (default, Apr 19 2020, 20:18:17)
# [GCC 9.2.1 20191008]
# linux
# ('64bit', 'ELF')


def show_size(x, level=0):
    result_size = asizeof.asizeof(x)
    print('\t' * level, f'type={type(x)}, size={asizeof.asizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key, level + 1)
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size


# Первый метод - решето Эратосфена, генераторы

@profile
def sieve(n):
    p_func = {4: 10, 25: 10 ** 2, 168: 10 ** 3, 1229: 10 ** 4, 9592: 10 ** 5, 78498: 10 ** 6, 664579: 10 ** 7,
              5761455: 10 ** 8, 50847534: 10 ** 9, 455052511: 10 ** 10}  # тут я перебрала, он и сотню едва потянул
    for key in p_func.keys():
        if n <= key:
            length = p_func[key]
            break
    s = [x for x in range(2, length + 1) if
         x not in [i for sub in [list(range(2 * j, length + 1, j)) for j in range(2, length // 2)] for i in sub]]
    show_size(locals())
    return s[n - 1]
sieve(20)

# type=<class 'dict'>, size=248, obj={'n': 5, 'p_func': {4: 10, 25: 100, 168: 1000, 1229: 10000, 9592: 100000, 78498:
# 1000000, 664579: 10000000, 5761455: 100000000, 50847534: 1000000000, 455052511: 10000000000}, 'key': 25, 's':
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 'length': 100}
# 	 type=<class 'str'>, size=50, obj=n
# 	 type=<class 'int'>, size=28, obj=5
# 	 type=<class 'str'>, size=55, obj=p_func
# 	 type=<class 'dict'>, size=376, obj={4: 10, 25: 100, 168: 1000, 1229: 10000, 9592: 100000, 78498: 1000000, 664579:
# 	 10000000, 5761455: 100000000, 50847534: 1000000000, 455052511: 10000000000}
# 		 type=<class 'int'>, size=28, obj=4
# 		 type=<class 'int'>, size=28, obj=10
# 		 type=<class 'int'>, size=28, obj=25
# 		 type=<class 'int'>, size=28, obj=100
# 		 type=<class 'int'>, size=28, obj=168
# 		 type=<class 'int'>, size=28, obj=1000
# 		 type=<class 'int'>, size=28, obj=1229
# 		 type=<class 'int'>, size=28, obj=10000
# 		 type=<class 'int'>, size=28, obj=9592
# 		 type=<class 'int'>, size=28, obj=100000
# 		 type=<class 'int'>, size=28, obj=78498
# 		 type=<class 'int'>, size=28, obj=1000000
# 		 type=<class 'int'>, size=28, obj=664579
# 		 type=<class 'int'>, size=28, obj=10000000
# 		 type=<class 'int'>, size=28, obj=5761455
# 		 type=<class 'int'>, size=28, obj=100000000
# 		 type=<class 'int'>, size=28, obj=50847534
# 		 type=<class 'int'>, size=28, obj=1000000000
# 		 type=<class 'int'>, size=28, obj=455052511
# 		 type=<class 'int'>, size=32, obj=10000000000
# 	 type=<class 'str'>, size=52, obj=key
# 	 type=<class 'int'>, size=28, obj=25
# 	 type=<class 'str'>, size=50, obj=s
# 	 type=<class 'list'>, size=272, obj=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 		 type=<class 'int'>, size=28, obj=2
# 		 type=<class 'int'>, size=28, obj=3
# 		 type=<class 'int'>, size=28, obj=5
# 		 type=<class 'int'>, size=28, obj=7
# 		 type=<class 'int'>, size=28, obj=11
# 		 type=<class 'int'>, size=28, obj=13
# 		 type=<class 'int'>, size=28, obj=17
# 		 type=<class 'int'>, size=28, obj=19
# 		 type=<class 'int'>, size=28, obj=23
# 		 type=<class 'int'>, size=28, obj=29
# 		 type=<class 'int'>, size=28, obj=31
# 		 type=<class 'int'>, size=28, obj=37
# 		 type=<class 'int'>, size=28, obj=41
# 		 type=<class 'int'>, size=28, obj=43
# 		 type=<class 'int'>, size=28, obj=47
# 		 type=<class 'int'>, size=28, obj=53
# 		 type=<class 'int'>, size=28, obj=59
# 		 type=<class 'int'>, size=28, obj=61
# 		 type=<class 'int'>, size=28, obj=67
# 		 type=<class 'int'>, size=28, obj=71
# 		 type=<class 'int'>, size=28, obj=73
# 		 type=<class 'int'>, size=28, obj=79
# 		 type=<class 'int'>, size=28, obj=83
# 		 type=<class 'int'>, size=28, obj=89
# 		 type=<class 'int'>, size=28, obj=97
# 	 type=<class 'str'>, size=55, obj=length
# 	 type=<class 'int'>, size=28, obj=100

# ================================================
#     49     38.3 MiB     38.3 MiB   @profile
#     50                             def sieve(n):
#     51     38.3 MiB      0.0 MiB       p_func = {4: 10, 25: 10 ** 2, 168: 10 ** 3, 1229: 10 ** 4, 9592: 10 ** 5, 78498: 10 ** 6, 664579: 10 ** 7,
#     52     38.3 MiB      0.0 MiB                 5761455: 10 ** 8, 50847534: 10 ** 9, 455052511: 10 ** 10}  # тут я перебрала, он и сотню едва потянул
#     53     38.3 MiB      0.0 MiB       for key in p_func.keys():
#     54     38.3 MiB      0.0 MiB           if n <= key:
#     55     38.3 MiB      0.0 MiB               length = p_func[key]
#     56     38.3 MiB      0.0 MiB               break
#     57     38.3 MiB      0.0 MiB       s = [x for x in range(2, length + 1) if
#     58     38.3 MiB      0.0 MiB            x not in [i for sub in [list(range(2 * j, length + 1, j)) for j in range(2, length // 2)] for i in sub]]
#     59     38.3 MiB      0.0 MiB       show_size(locals())
#     60     38.3 MiB      0.0 MiB       return s[n - 1]


# Второй метод - проверка делителей

@profile
def prime(num):
    count = 1
    next_num = 2

    while count < num:
        next_num += 1
        for i in range(2, int(next_num ** 0.5) + 1):
            if next_num % i == 0:
                break
        else:
            count += 1
    show_size(locals())
    return next_num
prime(20)

# type=<class 'dict'>, size=248, obj={'num': 5, 'count': 5, 'next_num': 11, 'i': 3}
# 	 type=<class 'str'>, size=52, obj=num
# 	 type=<class 'int'>, size=28, obj=5
# 	 type=<class 'str'>, size=54, obj=count
# 	 type=<class 'int'>, size=28, obj=5
# 	 type=<class 'str'>, size=57, obj=next_num
# 	 type=<class 'int'>, size=28, obj=11
# 	 type=<class 'str'>, size=50, obj=i
# 	 type=<class 'int'>, size=28, obj=3

# ================================================
#    141     38.8 MiB     38.8 MiB   @profile
#    142                             def prime(num):
#    143     38.8 MiB      0.0 MiB       count = 1
#    144     38.8 MiB      0.0 MiB       next_num = 2
#    145
#    146     38.8 MiB      0.0 MiB       while count < num:
#    147     38.8 MiB      0.0 MiB           next_num += 1
#    148     38.8 MiB      0.0 MiB           for i in range(2, int(next_num ** 0.5) + 1):
#    149     38.8 MiB      0.0 MiB               if next_num % i == 0:
#    150     38.8 MiB      0.0 MiB                   break
#    151                                     else:
#    152     38.8 MiB      0.0 MiB               count += 1
#    153     38.8 MiB      0.0 MiB       show_size(locals())
#    154     38.8 MiB      0.0 MiB       return next_num

# Третий метод - решето Эратосфена

@profile
def classic(n):
    p_func = {4: 10, 25: 10 ** 2, 168: 10 ** 3, 1229: 10 ** 4, 9592: 10 ** 5, 78498: 10 ** 6, 664579: 10 ** 7,
              5761455: 10 ** 8, 50847534: 10 ** 9, 455052511: 10 ** 10}
    for key in p_func.keys():
        if n <= key:
            length = p_func[key]
            break
    sieve = [0] * length
    for i in range(length):
        sieve[i] = i
    sieve[1] = 0
    m = 2

    while m < length:
        if sieve[m] != 0:
            j = m * 2
            while j < length:
                sieve[j] = 0
                j = j + m
        m += 1

    result = [x for x in sieve if sieve[x] != 0]
    show_size(locals())
    return result[n - 1]

classic(20)

# type=<class 'dict'>, size=376, obj={'n': 5, 'p_func': {4: 10, 25: 100, 168: 1000, 1229: 10000, 9592: 100000, 78498: 1000000, 664579: 10000000, 5761455: 100000000, 50847534: 1000000000, 455052511: 10000000000}, 'key': 25, 'length': 100, 'i': 99, 'm': 100, 'j': 194, 'result': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 'sieve': [0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 29, 0, 31, 0, 0, 0, 0, 0, 37, 0, 0, 0, 41, 0, 43, 0, 0, 0, 47, 0, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 59, 0, 61, 0, 0, 0, 0, 0, 67, 0, 0, 0, 71, 0, 73, 0, 0, 0, 0, 0, 79, 0, 0, 0, 83, 0, 0, 0, 0, 0, 89, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0]}
# 	 type=<class 'str'>, size=50, obj=n
# 	 type=<class 'int'>, size=28, obj=5
# 	 type=<class 'str'>, size=55, obj=p_func
# 	 type=<class 'dict'>, size=376, obj={4: 10, 25: 100, 168: 1000, 1229: 10000, 9592: 100000, 78498: 1000000, 664579: 10000000, 5761455: 100000000, 50847534: 1000000000, 455052511: 10000000000}
# 		 type=<class 'int'>, size=28, obj=4
# 		 type=<class 'int'>, size=28, obj=10
# 		 type=<class 'int'>, size=28, obj=25
# 		 type=<class 'int'>, size=28, obj=100
# 		 type=<class 'int'>, size=28, obj=168
# 		 type=<class 'int'>, size=28, obj=1000
# 		 type=<class 'int'>, size=28, obj=1229
# 		 type=<class 'int'>, size=28, obj=10000
# 		 type=<class 'int'>, size=28, obj=9592
# 		 type=<class 'int'>, size=28, obj=100000
# 		 type=<class 'int'>, size=28, obj=78498
# 		 type=<class 'int'>, size=28, obj=1000000
# 		 type=<class 'int'>, size=28, obj=664579
# 		 type=<class 'int'>, size=28, obj=10000000
# 		 type=<class 'int'>, size=28, obj=5761455
# 		 type=<class 'int'>, size=28, obj=100000000
# 		 type=<class 'int'>, size=28, obj=50847534
# 		 type=<class 'int'>, size=28, obj=1000000000
# 		 type=<class 'int'>, size=28, obj=455052511
# 		 type=<class 'int'>, size=32, obj=10000000000
# 	 type=<class 'str'>, size=52, obj=key
# 	 type=<class 'int'>, size=28, obj=25
# 	 type=<class 'str'>, size=55, obj=length
# 	 type=<class 'int'>, size=28, obj=100
# 	 type=<class 'str'>, size=50, obj=i
# 	 type=<class 'int'>, size=28, obj=99
# 	 type=<class 'str'>, size=50, obj=m
# 	 type=<class 'int'>, size=28, obj=100
# 	 type=<class 'str'>, size=50, obj=j
# 	 type=<class 'int'>, size=28, obj=194
# 	 type=<class 'str'>, size=55, obj=result
# 	 type=<class 'list'>, size=272, obj=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 		 type=<class 'int'>, size=28, obj=2
# 		 type=<class 'int'>, size=28, obj=3
# 		 type=<class 'int'>, size=28, obj=5
# 		 type=<class 'int'>, size=28, obj=7
# 		 type=<class 'int'>, size=28, obj=11
# 		 type=<class 'int'>, size=28, obj=13
# 		 type=<class 'int'>, size=28, obj=17
# 		 type=<class 'int'>, size=28, obj=19
# 		 type=<class 'int'>, size=28, obj=23
# 		 type=<class 'int'>, size=28, obj=29
# 		 type=<class 'int'>, size=28, obj=31
# 		 type=<class 'int'>, size=28, obj=37
# 		 type=<class 'int'>, size=28, obj=41
# 		 type=<class 'int'>, size=28, obj=43
# 		 type=<class 'int'>, size=28, obj=47
# 		 type=<class 'int'>, size=28, obj=53
# 		 type=<class 'int'>, size=28, obj=59
# 		 type=<class 'int'>, size=28, obj=61
# 		 type=<class 'int'>, size=28, obj=67
# 		 type=<class 'int'>, size=28, obj=71
# 		 type=<class 'int'>, size=28, obj=73
# 		 type=<class 'int'>, size=28, obj=79
# 		 type=<class 'int'>, size=28, obj=83
# 		 type=<class 'int'>, size=28, obj=89
# 		 type=<class 'int'>, size=28, obj=97
# 	 type=<class 'str'>, size=54, obj=sieve
# 	 type=<class 'list'>, size=872, obj=[0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 29, 0, 31, 0, 0, 0, 0, 0, 37, 0, 0, 0, 41, 0, 43, 0, 0, 0, 47, 0, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 59, 0, 61, 0, 0, 0, 0, 0, 67, 0, 0, 0, 71, 0, 73, 0, 0, 0, 0, 0, 79, 0, 0, 0, 83, 0, 0, 0, 0, 0, 89, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0]
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=2
# 		 type=<class 'int'>, size=28, obj=3
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=5
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=7
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=11
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=13
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=17
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=19
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=23
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=29
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=31
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=37
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=41
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=43
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=47
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=53
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=59
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=61
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=67
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=71
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=73
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=79
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=83
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=89
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=28, obj=97
# 		 type=<class 'int'>, size=24, obj=0
# 		 type=<class 'int'>, size=24, obj=0

# ================================================
#    185     38.9 MiB     38.9 MiB   @profile
#    186                             def classic(n):
#    187     38.9 MiB      0.0 MiB       p_func = {4: 10, 25: 10 ** 2, 168: 10 ** 3, 1229: 10 ** 4, 9592: 10 ** 5, 78498: 10 ** 6, 664579: 10 ** 7,
#    188     38.9 MiB      0.0 MiB                 5761455: 10 ** 8, 50847534: 10 ** 9, 455052511: 10 ** 10}
#    189     38.9 MiB      0.0 MiB       for key in p_func.keys():
#    190     38.9 MiB      0.0 MiB           if n <= key:
#    191     38.9 MiB      0.0 MiB               length = p_func[key]
#    192     38.9 MiB      0.0 MiB               break
#    193     38.9 MiB      0.0 MiB       sieve = [0] * length
#    194     38.9 MiB      0.0 MiB       for i in range(length):
#    195     38.9 MiB      0.0 MiB           sieve[i] = i
#    196     38.9 MiB      0.0 MiB       sieve[1] = 0
#    197     38.9 MiB      0.0 MiB       m = 2
#    198
#    199     38.9 MiB      0.0 MiB       while m < length:
#    200     38.9 MiB      0.0 MiB           if sieve[m] != 0:
#    201     38.9 MiB      0.0 MiB               j = m * 2
#    202     38.9 MiB      0.0 MiB               while j < length:
#    203     38.9 MiB      0.0 MiB                   sieve[j] = 0
#    204     38.9 MiB      0.0 MiB                   j = j + m
#    205     38.9 MiB      0.0 MiB           m += 1
#    206
#    207     38.9 MiB      0.0 MiB       result = [x for x in sieve if sieve[x] != 0]
#    208     38.9 MiB      0.0 MiB       show_size(locals())
#    209     38.9 MiB      0.0 MiB       return result[n - 1]

## Вывод #########################################################################

# Метод генераторов и метод проверки делителей разделили между собой первое место по занимаемой памяти, классический
# способ занял больше всего места. Но по быстродействию в одном из предыдущих заданий первое место поделили метод
# проверки делителей и классический метод. Целесообразность использования конкретного алгоритма необходимо смотреть
# для конкретной ситуации, машины и задачи. Узких мест с серьезным приростом памяти в алгоритмах не найдено.
