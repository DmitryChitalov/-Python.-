"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
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


# Сортировка массива по убыванию пузырьком
def bubble_sort_min(array):
    """
    Функция сортировки массива по убыванию пузырьком
    :param array: Массив
    :return: отсортированный массив
    """
    for i in range(len(array), 0, -1):
        for j in range(1, i):
            if array[j - 1] < array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


def better_bubble_sort_min(array):
    """
    Улучшенная функция сортировки массива по убыванию пузырьком
    :param array: Массив
    :return: отсортированный массив
    """
    len_array = len(array) - 1
    while True:
        count = 0
        for i in range(len_array, 0, -1):
            if array[i - 1] < array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                count += 1
        if count == 0:
            break
    return array


LEN_ARRAY = 100
# Инициализация массива случайными целыми числами от -100 до 100
ARRAY = [random.randint(-100, 100) for _ in range(LEN_ARRAY)]
# Копируем сгенерированный массив
ARRAY_COPY = [element for element in ARRAY]

# Вывод на экран исходного массива по 10 элементов
print(f'\nИсходный массив:\n')
print_array(ARRAY)

# Сортировка массива по убыванию пузырьком
bubble_sort_min(ARRAY)
# Вывод на экран отсортированного массива по 10 элементов
print(f'\nОтсортированный массив:\n')
print_array(ARRAY)

# Вывод времени выполнения алгоритма сортировки пузырьком по убыванию
time_bubble = timeit.timeit('bubble_sort_min(ARRAY)',
                            setup='from __main__ import bubble_sort_min, ARRAY',
                            number=1000)
print(f'\nВремя сортировки пузырьком: {time_bubble}')

del ARRAY

"""
 ---------------------  Результаты работы улучшенного алгоритма сортировки пузырьком  ---------------------
"""

# Восстановление исходного массива из копии
ARRAY = ARRAY_COPY

# Улучшенная сортировка массива по убыванию пузырьком
better_bubble_sort_min(ARRAY)

# Вывод на экран отсортированного массива по 10 элементов
print(f'\nОтсортированный массив:\n')
print_array(ARRAY)

# Вывод времени выполнения улучшенного алгоритма сортировки пузырьком по убыванию
time_better_bubble = timeit.timeit('better_bubble_sort_min(ARRAY)',
                                   setup='from __main__ import better_bubble_sort_min, ARRAY',
                                   number=1000)
print(f'\nВремя улучшенной сортировки пузырьком: {time_better_bubble}')
