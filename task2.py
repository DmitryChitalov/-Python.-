from collections import defaultdict

from memory_profiler import profile


@profile
def task_five():
    a = [-5, -10, -20, 1, 6, 12, 54]
    b = [el for el in a if el < 0]
    i = b[0]
    for elem in range(len(b)):
        if a[elem] > i:
            i = a[elem]
    print(i)


task_five()

"""Line #    Mem usage    Increment   Line Contents
================================================
     6     15.5 MiB     15.5 MiB   @profile
     7                             def task_five():
     8     15.5 MiB      0.0 MiB       a = [-5, -10, -20, 1, 6, 12, 54] //При использовании генератора выделяется
     9     15.5 MiB      0.0 MiB       b = [el for el in a if el < 0]   //достаточно мало памяти, поэтому здесь потимизация
    10     15.5 MiB      0.0 MiB       i = b[0]                         // не требуется
    11     15.5 MiB      0.0 MiB       for elem in range(len(b)):
    12     15.5 MiB      0.0 MiB           if a[elem] > i:
    13                                         i = a[elem]
    14     15.5 MiB      0.0 MiB       print(i)
"""
