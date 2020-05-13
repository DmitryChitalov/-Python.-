import timeit
import random
numbers = [random.randint(-100,100) for _ in range(100)]

print(numbers)

def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1

    return orig_list

print(bubble_sort(numbers))
numbers = [random.randint(-100, 100) for _ in range(10)]
# замеры 10
print(timeit.timeit("bubble_sort(numbers)", \
    setup="from __main__ import bubble_sort, numbers", number=1000))

numbers = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(numbers)", \
    setup="from __main__ import bubble_sort, numbers", number=1000))

numbers = [random.randint(-100, 100) for _ in range(1000)]

#замеры 1000
print(timeit.timeit("bubble_sort(numbers)", \
    setup="from __main__ import bubble_sort, numbers", number=1000))

"""
Результаты:
0.017631659
0.875264772
73.884469962
"""

# Оптимизированыи вариант
def bubble_sort(orig_list, is_sorted=False):
    n = 1
    while n < len(orig_list):
        is_sorted = True
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                is_sorted = False
            if is_sorted:
                break
        n += 1

    return orig_list