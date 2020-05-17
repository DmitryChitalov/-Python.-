"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import randint
import statistics

m = 4
y = 2 * m + 1
x = [randint(1, 50) for i in range(y)]
n = len(x) // 2

def median(n, x):
    pivot = x[randint(0, len(x)-1)]
    left = []
    for i in x:
        if i < pivot:
            left.append(i)

    if len(left) > n:
        return median(n, left)
    n -= len(left)

    pivot_equal = x.count(pivot)
    if pivot_equal > n:
        return pivot
    n -= pivot_equal
    right = []
    for i in x:
        if i > pivot:
            right.append(i)
    return median(n, right)


print('Исходный список - ',x)
print('Найденная медиана - ' ,median(n, x))
print('Проверка готовой функцией , медиана - ' ,statistics.median(x))