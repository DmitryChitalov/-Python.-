import matplotlib.pyplot as plt
from random import randrange
from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time() - start
        return end
    return wrapper


def get_list(stop, length, start=1):
    return [randrange(start, stop) for _ in range(length)]


def swap(i, j):
    temp = b_list[i]
    b_list[i] = b_list[j]
    b_list[j] = temp


def bubble_sort(lst_):
    for j in range(len(lst_) - 1, 0, -1):
        for i in range(j):
            if lst_[i] < lst_[i + 1]:
                swap(i, i + 1)
    return lst_


def merge_sort(arr):
    def wrapper(arr_):
        if len(arr_) > 1:
            mid = len(arr_) // 2
            left = arr_[:mid]
            right = arr_[mid:]

            merge_sort(left)
            merge_sort(right)

            i = j = k = 0

            # Copy data to temp arr_ays l[] and right[]
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr_[k] = left[i]
                    i += 1
                else:
                    arr_[k] = right[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left):
                arr_[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr_[k] = right[j]
                j += 1
                k += 1
    wrapper(arr)


def hoare_sort(arr):
    if len(arr) <= 1:
        return
    barrier = arr[0]
    left = []
    middle = []
    right = []
    for el in arr:
        if el < barrier:
            left.append(el)
        elif el == barrier:
            middle.append(el)
        else:
            right.append(el)
    hoare_sort(left)
    hoare_sort(right)
    k = 0
    for el in left + middle + right:
        arr[k] = el
        k += 1


@timer
def run_bubble_sort(lst_):
    bubble_sort(lst_)


@timer
def run_hoare_sort(lst_):
    merge_sort(lst_)


@timer
def run_merge_sort(lst_):
    hoare_sort(lst_)


if __name__ == "__main__":
    results = dict(
        b_sort=(list(), list()),
        h_sort=(list(), list()),
        m_sort=(list(), list())
    )
    for x in [1, 50, 100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000]:
        lst = get_list(start=-100, stop=100, length=x)
        m_list = lst[:]
        b_list = lst[:]
        h_list = lst[:]
        m_sort = run_merge_sort(m_list)
        b_sort = run_bubble_sort(b_list)
        h_sort = run_hoare_sort(h_list)
        for i in ['b_sort', 'h_sort', 'm_sort']:
            results[i][1].append(eval(i))
            results[i][0].append(x)


    print(results.get('b_sort'))
    plt.plot(*results.get('b_sort'), 'r--', *results.get('h_sort'), 'b-', *results.get('m_sort'), 'g--')
    plt.show()
