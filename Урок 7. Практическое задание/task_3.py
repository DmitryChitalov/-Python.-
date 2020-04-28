"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""


from random import randint
from copy import deepcopy
from timeit import timeit


# Решение без сортировки
def median_search1(arr):
    median = None
    for i in range(0, len(arr)):
        arr_func = deepcopy(arr)
        less_arr = []
        more_arr = []

        el = arr_func[i]
        count = 0

        for j in arr_func:
            if j == el:
                count += 1
            elif el > j:
                less_arr.append(j)
            else:
                more_arr.append(j)

        if abs(len(less_arr) - len(more_arr)) == count - 1:
            median = el
            return median


# Решение с сортировкой
def find_smallest(arr):
    smalest = arr[0]
    smalest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smalest:
            smalest = arr[i]
            smalest_idx = i
    return smalest_idx


def sort_by_selection(arr):
    new_arr = []
    for i in range(0, len(arr)):
        idx = find_smallest(arr)
        new_arr.append(arr.pop(idx))
    return new_arr


def median_search2(arr):
    arr_func = sort_by_selection(deepcopy(arr))
    median = arr_func[len(arr_func) // 2]
    return median


try:
    m = int(input('Введите m: '))
except ValueError as err:
    print('Ошибка. неверное значение m')
    print(err)
    print('Взято значение по умолчанию m = 10\n')
    m = 10

input_arr = [randint(0, 100) for i in range(0, 2 * m + 1)]
print(f'Исходный массив: {input_arr}\n')

number = 1000

print('# Решение без сортировки:')
median1 = median_search1(input_arr)
print(f'Медиана исходного массива - {median1}\n')
print(f'Время выполнени с number = {number}:')
print("\033[31m{}\033[0m".format('Please wait...'), end='')
print('\r' + str(timeit(f"median_search1(input_arr)",
                        setup=f"from __main__ import median_search1, input_arr",
                        number=number)) + ' seconds\n')

print('####################################################')

print('# Решение с сортировкой:')
median2 = median_search2(input_arr)
print(f'Медиана исходного массива - {median2}\n')
print("\033[31m{}\033[0m".format('Please wait...'), end='')
print('\r' + str(timeit(f"median_search2(input_arr)",
                        setup=f"from __main__ import median_search2, input_arr",
                        number=number)) + ' seconds\n')

"""
Как видно из результатов, вариант решения с сортировкой выполняется быстрее. Это связанно с тем, что у варианта решения
без сортировки сложность О(n^2), а у вариант с сортировкой О(n log n).
"""


