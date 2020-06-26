from memory_profiler import profile
from sys import getrefcount
from pympler import asizeof

"""
Анализ 1.
"""


@profile
def ar_switch(values, args):
    tmp_arr = args
    i = 0
    q = 1
    for el in values:
        tmp_arr[tmp_arr.index(values[q])] = values[i]
        i += 1
        q -= 1
    return tmp_arr


preset_arr = [
    10, 2, 45, 12, 45, 75, 45, 75, 78,
    4, 6, 5, 4, 78, 89, 45, 452, 123,
    456, 789, 457, 854, 78, 4, 1024,
    78, 69, 7, 8, 65, 24, 78, 98, 65, 32,
    12, 45, 75, 45, 75, 78, 4, 6, 5, 4, 78,
    89, 45, 452, 123, 456, 789, 457, 854, 12, 45, 75, 45,
    75, 78, 4, 6, 5, 4, 78, 89, 45, 452, 123,
    456, 789, 457, 854
]


mini = preset_arr[0]
maxi = preset_arr[0]
for el in preset_arr:
    if el > maxi:
        maxi = el
    if el <= mini:
        mini = el
min_max = [mini, maxi]
(ar_switch(min_max, preset_arr))


vars = [
    preset_arr, mini,
    maxi, min_max
        ]

for el in vars:
    print(f'Object {el} has {getrefcount(el)} number of links')
print(asizeof.asizeof(preset_arr))
'''
Изначальный код программы. 
Использует 15.5 MiB.
Переменную vars не считаем, так как для работы алгоритма она не требуется.
'''

"""
Оптимизация
"""


@profile
def ar_switch(values, args):
    tmp_arr = args
    i = 0
    q = 1
    for el in values:
        tmp_arr[tmp_arr.index(values[q])] = values[i]
        i += 1
        q -= 1
    return print(tmp_arr)


preset_arr = [
    10, 2, 45, 12, 45, 75, 45, 75, 78,
    4, 6, 5, 4, 78, 89, 45, 452, 123,
    456, 789, 457, 854, 78, 4, 1024,
    78, 69, 7, 8, 65, 24, 78, 98, 65, 32,
    12, 45, 75, 45, 75, 78, 4, 6, 5, 4, 78,
    89, 45, 452, 123, 456, 789, 457, 854, 12, 45, 75, 45,
    75, 78, 4, 6, 5, 4, 78, 89, 45, 452, 123,
    456, 789, 457, 854
]

min_max = [min(preset_arr), max(preset_arr)]
ar_switch(min_max, preset_arr)
del preset_arr
del min_max
# print(asizeof.asizeof(preset_arr))
# не выполнится, т.к. объекта больше не существует.
'''
Даже при отсутствующем видимом уменьшении затраченной памяти,
можно делать вывод о том, что программа после оптимизации будет 
потреблять меньше памяти, так как все "хвосты" в виде ссылок на
объекты удаляются в конце работы программы
'''
"""
Анализ 2.
"""


@profile
def sum_of_line(args):
    for el in args:
        el_sum = 0
        for i in el:
            el_sum += i
        el.append(el_sum)
    return args


matrix_1 = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4]
]


print(f'{sum_of_line(matrix_1)}')

'''
Изначальный код программы. 
Использует 15.5 MiB.
Хранит в памяти постоянно матрицу и
имеет вложенный цикл, вместо внутренней
функции.
'''

"""
Оптимизация
"""


@profile
def sum_of_line(args):
    for el in args:
        el.append(sum(el))
    return args


matrix_1 = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4]
]


print(f'{sum_of_line(matrix_1)}')
del matrix_1

'''
К сожалению, и во втором случае не получается добиться 
показательных цифр, однако в отличии от неоптимизированной
версии, оптимизированная не хранит объект и ссылку на него,
а так же использует встроенную функцию.

Итого: в обоих вариантах оптимизации,
освобожденная память колеблется в рацоне 0.1 MiB,
что в рамках 'боевой оптимизации' сложно назвать результатом,
однако при увеличении объема данных результат будет скалироваться,
что позволит освободить память при работе с большими цифрами.
'''

'''
Phyton version 3.8
OS Win10 x64
'''
