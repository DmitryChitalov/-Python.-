import cProfile
from timeit import Timer
import random
from memory_profiler import profile
from guppy import hpy
import numpy as np
from time import sleep


# os
# elementary OS 5.1.5 Hera (64)
# python
# Python 3.6.9


@profile()
def my_func():
    x = 15
    array = [1, 1, 1, 2, 2, 3, 4, 2, 8, 8, 8, 8, 8, 8, 1, 9]

    num = array[0]
    max_frq = 1
    for i in range(x - 1):
        frq = 1
        for k in range(i + 1, x):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]

    print(f'number {num} will found {max_frq} times')


my_func()


# можно сделать вывод что прироста памяти по мере прохождения скрипта не присутствует
# работу скрипта можно назвать оптимальной - Increment 0.0 MiB на протяжении всей работы

@profile()
def my_func_with_max(lst):
    print(f'source list - {lst}')
    numb = max(lst, key=lst.count)
    print(f'number {numb} will found {lst.count(numb)} times')


LST = [random.randint(-100, 100) for i in range(50)]
my_func_with_max(LST)
# ситуация аналогична перому скрипту Increment 0.0 MiB

from copy import deepcopy


@profile()
def copy():
    x = list(range(1000))
    y = deepcopy(x)
    z = my_func()
    s = sleep(5)
    sl = s


copy()
# ситуация аналогична перому скрипту Increment 0.0 MiB
# следовательно сслыка даже на ф-ю внутри другой ф-ии не влияет на прирост инкремента
# ссылки не нужно удалять
