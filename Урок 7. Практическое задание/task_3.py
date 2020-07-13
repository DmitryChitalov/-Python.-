"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random
from statistics import median
import timeit


def get_median(orig_list):
    orig_list = orig_list.copy()
    while len(orig_list) > 1:
        el_min, el_max = 'not', 'not'
        for el in orig_list:
            if el_min == 'not':
                el_min = el
            if el_max == 'not':
                el_max = el
            if el_min > el:
                el_min = el
            elif el_max < el:
                el_max = el
        orig_list.pop(orig_list.index(el_min))
        orig_list.pop(orig_list.index(el_max))
    return orig_list[0]


def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


LIST_SIZE = 2 * int(input("Создаём размер массива исходя из формулы: 2m + 1. Введите m: ")) + 1
ORIG_LIST = [random.randint(0, 100) for _ in range(LIST_SIZE)]

# Проверяем, что оно работает
random_list_of_nums = ORIG_LIST.copy()
heap_sort(random_list_of_nums)


print(f"Исходный массив - {ORIG_LIST}",
      f"Реализация без сортировки - {get_median(ORIG_LIST)}",
      f"Сортировка пирамидой - {random_list_of_nums[int(len(random_list_of_nums) / 2)]}",
      f"Проверка встроенной функцией statistics.median - {median(ORIG_LIST)}",
      sep="\n")

print("Скорость моей реализации без сортировки: ", timeit.timeit("get_median(ORIG_LIST)", \
    setup="from __main__ import get_median, ORIG_LIST", number=100))

print("Скорость сортировкой пирамидой: ", timeit.timeit("heap_sort(random_list_of_nums)", \
    setup="from __main__ import heap_sort, random_list_of_nums", number=100))

print("Скорость встроенной функции нахождения медианы: ", timeit.timeit("median(ORIG_LIST)", \
    setup="from __main__ import median, ORIG_LIST", number=100))


"""
Создаём размер массива исходя из формулы: 2m + 1. Введите m: 12
Исходный массив - [93, 0, 58, 11, 28, 58, 66, 78, 9, 85, 47, 88, 41, 91, 28, 100, 17, 63, 76, 29, 97, 21, 3, 25, 47]
Реализация без сортировки - 47
Сортировка пирамидой - 47
Проверка встроенной функцией statistics.median - 47
Скорость моей реализации без сортировки:  0.005673300000000214
Скорость сортировкой пирамидой:  0.012780400000000025
Скорость встроенной функции нахождения медианы:  0.00017500000000003624

Process finished with exit code 0
"""