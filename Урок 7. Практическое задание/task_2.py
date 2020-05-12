"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import operator
import random
import timeit


def print_array(array):
    """
    Функция вывода на экран содержимого массива по 10 элементов
    :param array: Массив
    :return:
    """
    for i, element in enumerate(array, 1):
        print(f'{element}  ', end='')
        if i % 10 == 0:
            print(f'')
    return None


def merge_sort(array, compare=operator.lt):
    """
    :param array: подмассив
    :param compare: оператор "="
    :return:
    """
    if len(array) < 2:
        return array[:]
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle], compare)
        right = merge_sort(array[middle:], compare)
    return merge(left, right, compare)


def merge(left, right, compare):
    sorted_array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array


LEN_ARRAY = 10
# Инициализация массива случайными целыми числами от 0 до 50
ARRAY = [random.uniform(0, 49) for _ in range(LEN_ARRAY)]

# Вывод на экран исходного массива по 10 элементов
print(f'\nИсходный массив:\n')
print_array(ARRAY)

# Вывод на экран отсортированного массива по 10 элементов
print(f'\nОтсортированный массив:\n')
print_array(merge_sort(ARRAY))
