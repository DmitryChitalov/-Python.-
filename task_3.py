"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randint
from timeit import Timer
import sys

# На малых размерах сортировка вставками работает
# Быстрее чем сортировка слияниями
# При объединении этих двух методов можно получить выйгрыш во времени


def insert_sort(array):

    for i in range(1, len(array)):
        tmp = array[i]
        k = i
        while tmp < array[k - 1]:
            if k - 1 >= 0:
                array[k] = array[k-1]
                k -= 1
            else:
                break
        array[k] = tmp
        del tmp
    return array

# При размере массива = 10000 cProfile показывает полное время 0.57 при затрате на метод mixed_sort = 0.043
def mixed_sort(array):
    if len(array) == 1:
        return array
    else:
        if len(array) <= 10:
            array = insert_sort(array)
        else:
            left = mixed_sort(array[:len(array) // 2])
            right = mixed_sort(array[-len(array) // 2:])
            j = 0
            k = 0
            for i in range(len(array)):
                if j >= len(left):
                    array[i] = right[k]
                    k += 1
                elif k >= len(right):
                    array[i] = left[j]
                    j += 1
                elif left[j] > right[k]:
                    array[i] = right[k]
                    k += 1
                else:
                    array[i] = left[j]
                    j += 1
        return array

# При размере массива = 10000 cProfile показывает полное время 0.76 при затрате на метод merge_sort = 0.061
def merge_sort(array):

    if len(array) == 1:
        return array
    else:
        left = merge_sort(array[:len(array) // 2])
        right = merge_sort(array[-len(array) // 2:])
        j = 0
        k = 0
        for i in range(len(array)):
            if j >= len(left):
                array[i] = right[k]
                k += 1
            elif k >= len(right):
                array[i] = left[j]
                j += 1
            elif left[j] > right[k]:
                array[i] = right[k]
                k += 1
            else:
                array[i] = left[j]
                j += 1
        return array

# Поиск медианы при предварительной сортировке массива
# Сортировка производится методом mixed_sort
# Наиболее быстрый вариант достигается
# При T(n) = O(nlog(n)) - скорость сортировки массива
def median_sort(array):
    mixed_sort(array)
    median = array[len(array) // 2 - 1] if len(array) % 2 == 0 else array[len(array) // 2]
    return median

"""
Рекурсивный метод без предварительной сортировки
Происходит деление относительно выбранного элемента
на левый и правый массивы и затем производится 
выбор подходящего массива
Таким образом при каждом вызове
количество уменьшается в среднем в 2 раза
и T(n) = O(2n)
"""
def median_simple(array, m_index):
    rand_number = randint(0, len(array)-1)
    left = []
    right = []
    for i in range(len(array)):
        if array[i] <= array[rand_number]:
            left.append(array[i])
        else:
            right.append(array[i])

    if len(left) == m_index:
        del left, right
        return array[rand_number]
    elif len(left) < m_index:
        length = len(left)
        del left
        return median_simple(right, m_index - length)
    else:
        del right
        return median_simple(left, m_index)

"""
Функциональный метод без предварительной сортировки
Происходит деление относительно выбранного элемента
на левый и правый массивы и затем производится 
выбор подходящего массива
Таким образом при каждом вызове
количество уменьшается в среднем в 2 раза
и T(n) = O(2n)
Поскольку не задействуется стек вызова, 
то предполагается незначительный выйгрыш по времени
"""
def median_simple_func(array, m_index):
    while True:
        rand_number = randint(0, len(array) - 1)
        left = []
        right = []
        for i in range(len(array)):
            if array[i] <= array[rand_number]:
                left.append(array[i])
            else:
                right.append(array[i])

        if len(left) == m_index:
            del left, right
            return array[rand_number]
        elif len(left) < m_index:
            array = right
            m_index = m_index - len(left)
        else:
            array = left
        del right, left

"""
Функциональный метод, который на каждом шаге уменьшает количество массива на 1
Числовой ряд T(n) = n + n-1 + n-2 + ... в среднем сходится медленнее чем у метода median_simple
T(n) = n + n/2 + n/4 + ...  Поэтому этот метод не является выгодным по времени и в худшем
случае может работать как О(n^2) и работает дольше чем метод с предварительной сортировкой массива
где T(n) = O(nlog(n))
"""
def median_func(array):
    m_index = len(array) // 2 - 1 if len(array) % 2 == 0 else len(array) // 2
    length = len(array) - 1
    while True:
        rand_number = randint(0, length)
        count = 0
        for i in range(len(array)):
            if array[i] <= array[rand_number] and i != rand_number:
                count += 1
            if count > m_index:
                if rand_number != length:
                    array[rand_number], array[length] = array[length], array[rand_number]
                length -= 1
                break
        if count == m_index:
            return array[rand_number]


def median_search(m):

    array = [randint(-100, 100) for _ in range(2*m + 1)]
    m_index = len(array) // 2 if len(array) % 2 == 0 else len(array) // 2 + 1
    t_sort = Timer(f"median_sort({array.copy()})", "from __main__ import median_sort")
    t_simple = Timer(f"median_simple({array.copy()}, {m_index})", "from __main__ import median_simple")
    t_simple_func = Timer(f"median_simple_func({array.copy()}, {m_index})", "from __main__ import median_simple_func")
    t_func = Timer(f"median_func({array.copy()})", "from __main__ import median_func")
    # print(f"array = {array}")
    # print(f"sorted array = {merge_sort(array.copy())}")
    print(f"median from sort = {median_sort(array.copy())}, time = {t_sort.timeit(number=100)}")
    print(f"median from simple = {median_simple(array.copy(), m_index)}, time = {t_simple.timeit(number=100)}")
    print(f"median from simple_func = {median_simple_func(array.copy(), m_index)}, time = {t_simple_func.timeit(number=100)}")
    print(f"median from median_func = {median_func(array.copy())}, time = {t_func.timeit(number=100)}")


limit = sys.getrecursionlimit()
sys.setrecursionlimit(10**6)
median_search(50)
sys.setrecursionlimit(limit)

"""
median from sort = 10, time = 0.014068300000000002
median from simple = 10, time = 0.005065
median from simple_func = 10, time = 0.004710500000000006
median from median_func = 10, time = 0.0573821
"""

"""
После проведения замеров видно, что наиболее быстрым способом нахождения медианы является метод
median_simple_func не задействующий методы сортировки и рекурсию , однако выйгрыш по времени с 
рекурсивным методом median_simple незначителен. 
Наиболее долгим является функциональный метод median_func не задействующий сортировку
"""

"""
Следовательно наиболее оптимальным методом является простой метод без предварительной сортировки массива 
Либо рекурсивный median_simple, либо функциональный методы median_simple_func. 
Выйгрыш по времени незначительный
"""




