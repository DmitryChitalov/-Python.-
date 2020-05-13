"""
решето Эратосфена

"""

from memory_profiler import profile
from pympler import tracker

def f_sieve(lenghth):
    empty_sieve = [0] * lenghth
    return empty_sieve


def fil_sieve(full_sieve, lenghth):
    for i in range(lenghth):
        full_sieve[i] = i
    full_sieve[1] = 0
    return full_sieve


def filter_sieve(sieve, lenghth):
    number = 2
    while number < lenghth:
        if sieve[number] != 0:
            next_number = number * 2
            while next_number < lenghth:
                sieve[next_number] = 0
                next_number = next_number + number
        number += 1
    return sieve

@profile
def eratosphen(lenghth):
    lenghth += 1
    sieve = f_sieve(lenghth)
    sieve = fil_sieve(sieve, lenghth)
    sieve = filter_sieve(sieve, lenghth)
    result = [x for x in sieve if sieve[x] != 0]
    return result

@profile
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

@profile
def eratosphen_2(n):

    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return lst


print(eratosphen_2(1000))

print(eratosphen(1000))

print(simple(1000))


"""
eratosphen_2

Line #    Mem usage    Increment   Line Contents
================================================
    61     18.7 MiB     18.7 MiB   @profile
    62                             def eratosphen_2(n):
    63                             
    64     18.7 MiB      0.0 MiB       a = list(range(n + 1))
    65     18.7 MiB      0.0 MiB       a[1] = 0
    66     18.7 MiB      0.0 MiB       lst = []
    67                             
    68     18.7 MiB      0.0 MiB       i = 2
    69     18.7 MiB      0.0 MiB       while i <= n:
    70     18.7 MiB      0.0 MiB           if a[i] != 0:
    71     18.7 MiB      0.0 MiB               lst.append(a[i])
    72     18.7 MiB      0.0 MiB               for j in range(i, n + 1, i):
    73     18.7 MiB      0.0 MiB                   a[j] = 0
    74     18.7 MiB      0.0 MiB           i += 1
    75     18.7 MiB      0.0 MiB       return lst
    
eratosphen
Line #    Mem usage    Increment   Line Contents
================================================
    32     18.7 MiB     18.7 MiB   @profile
    33                             def eratosphen(lenghth):
    34     18.7 MiB      0.0 MiB       lenghth += 1
    35     18.7 MiB      0.0 MiB       sieve = f_sieve(lenghth)
    36     18.7 MiB      0.0 MiB       sieve = fil_sieve(sieve, lenghth)
    37     18.7 MiB      0.0 MiB       sieve = filter_sieve(sieve, lenghth)
    38     18.7 MiB      0.0 MiB       result = [x for x in sieve if sieve[x] != 0]
    39     18.7 MiB      0.0 MiB       return result

simple
Line #    Mem usage    Increment   Line Contents
================================================
    41     18.7 MiB     18.7 MiB   @profile
    42                             def simple(i):
    43                                 '''Без использования «Решета Эратосфена»'''
    44     18.7 MiB      0.0 MiB       count = 1
    45     18.7 MiB      0.0 MiB       n = 2
    46     18.8 MiB      0.0 MiB       while count <= i:
    47     18.8 MiB      0.0 MiB           t = 1
    48     18.8 MiB      0.0 MiB           is_simple = True
    49     18.8 MiB      0.0 MiB           while t <= n:
    50     18.8 MiB      0.0 MiB               if n % t == 0 and t != 1 and t != n:
    51     18.8 MiB      0.0 MiB                   is_simple = False
    52     18.8 MiB      0.0 MiB                   break
    53     18.8 MiB      0.0 MiB               t += 1
    54     18.8 MiB      0.0 MiB           if is_simple:
    55     18.8 MiB      0.0 MiB               if count == i:
    56     18.6 MiB      0.0 MiB                   break
    57     18.8 MiB      0.0 MiB               count += 1
    58     18.8 MiB      0.0 MiB           n += 1
    59     18.6 MiB      0.0 MiB       return n


вывод: разделение на отдельные функции не влияет на память. У решита нет премущества по использованию
памяти по сравнению с наивным перебом.

"""