"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random

def select(lst):
    if len(lst) % 2 == 1:
        return median_search(lst, len(lst)/2)
    else:
        return (median_search(lst, len(lst) / 2 - 1) +
                median_search(lst, len(lst) / 2))/2


def median_search(lst, k):
    """
    Данный алгоритм базируется на разбиемнии массива на 3 подмассива:
    1-ый - опорный эелемент
    2-ой - эелемнты меньше попрного
    3-ий - элементы больше опопрного.
    Если в less есть k или больше элементов - рекурсивно обходим less.
    Если в less меньше ,чем  k-элементов - рекурсивно обходим список greater.
    Вместо поиска  k мы ищем k - len(less).
    """
    if len(lst) == 1:
        return lst[0]

    pivot = random.choice(lst)

    less = [el for el in lst if el < pivot]
    greater = [el for el in lst if el > pivot]
    pivots = [el for el in lst if el == pivot]

    if k < len(less):
        return median_search(less, k)
    elif k < len(less) + len(pivots):
        return pivots[0]
    else:
        return median_search(greater, k - len(less) - len(pivots))
# массив размером 2m + 1
LST = [random.randint(0, 50) for _ in range(2 * random.randint(0, 50) + 1)]
print(select(LST))


# Нахождение медианы с использованием пираммидальной сортировки

def heapify(lst, n, root):
    """Создание 'кучи'"""
    largest = root
    left = (2 * root) + 1
    right = (2 * root) + 2

    if left < n and lst[left] > lst[largest]:
        largest = left

    if right < n and lst[right] > lst[largest]:
        largest = right

    if largest != root:
        lst[root], lst[largest] = lst[largest], lst[root]
        heapify(lst, n, largest)


def sort_func(lst):
    """Сортировка списка"""
    n = len(lst)

    for root in range(n, -1, -1):
        heapify(lst, n, root)

    for root in range(n-1, 0, -1):
        lst[root], lst[0] = lst[0], lst[root]
        heapify(lst, root, 0)

    return lst

def median_search(lst):
    """Поиск медианы"""
    mid = len(lst) // 2
    sort_func(lst)
    if len(lst) % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2.0
    return lst[mid]

print(median_search(LST))
