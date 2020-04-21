"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randint



def median_search(lst, first, last):

    lst = lst.copy()
    mid = len(lst) // 2         # Порядковый номер предполагаемого медианного элемента

    if first >= last:
        return lst[mid]

    pivot = lst[mid]
    i = first
    j = last

    while i <= j:

        while lst[i] < pivot:
            i += 1

        while lst[j] > pivot:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if mid < i:
        lst[mid] = median_search(lst, first, j)

    elif mid > j:
        lst[mid] = median_search(lst, i, last)

    return lst[mid]


"""ПИРАМИДАЛЬНАЯ СОРТИРОВКА (Сортировка кучей)"""


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
        
        # строим новую кучу для нового корневого эл-та чтобы убедиться что он наибольший
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
        
    return nums



MIN_NUM = 1
MAX_NUM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1

arr = [randint(MIN_NUM, MAX_NUM) for _ in range(size)]
print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', arr, sep='\n')

median = median_search(arr, 1, len(arr) - 1)
print(f'Медиана: {median}')

print('Отсортированный массив: ', heap_sort(arr), sep='\n')

if median == heap_sort(arr)[len(arr)//2]:
    print('\nВерно')
else:
    print('\nОшибка!!!')